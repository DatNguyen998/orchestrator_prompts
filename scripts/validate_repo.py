#!/usr/bin/env python3
"""Validate repository links and the live Claude-agent catalog."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / ".claude" / "agents"
ACTIVE_DOCS = [
    ROOT / "README.md",
    ROOT / "GUIDE.md",
    ROOT / ".claude" / "SQUAD-ROUTING.md",
    *sorted(AGENT_DIR.glob("*.md")),
]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")
FRONT_MATTER_NAME = re.compile(r"\A---\s*\n.*?^name:\s*([^\s]+)\s*$.*?^---\s*$", re.M | re.S)
IDENTITY_LINE = re.compile(r"^You are ([a-z0-9_-]+),", re.M)


def validate_links(errors: list[str]) -> None:
    for source in ROOT.rglob("*.md"):
        if ".git" in source.parts:
            continue
        for raw_target in MARKDOWN_LINK.findall(source.read_text(encoding="utf-8")):
            target = raw_target.split(maxsplit=1)[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_text = unquote(target.split("#", 1)[0])
            if path_text and not (source.parent / path_text).resolve().exists():
                errors.append(f"{source.relative_to(ROOT)}: broken local link: {target}")


def validate_agents(errors: list[str]) -> None:
    agents: set[str] = set()
    for source in sorted(AGENT_DIR.glob("*.md")):
        content = source.read_text(encoding="utf-8")
        match = FRONT_MATTER_NAME.search(content)
        if not match:
            errors.append(f"{source.relative_to(ROOT)}: missing front-matter name")
            continue
        name = match.group(1)
        agents.add(name)
        if name != source.stem:
            errors.append(
                f"{source.relative_to(ROOT)}: name {name!r} does not match filename"
            )

        identity = IDENTITY_LINE.search(content)
        if not identity:
            errors.append(f"{source.relative_to(ROOT)}: missing 'You are <name>,' identity")
        elif identity.group(1) != name:
            errors.append(
                f"{source.relative_to(ROOT)}: body identity {identity.group(1)!r} "
                f"does not match front-matter name {name!r}"
            )

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    catalog = set(re.findall(r"\| \[([^]]+)]\(\.claude/agents/[^)]+\)", readme))
    if catalog != agents:
        errors.append(
            "README agent catalog mismatch: "
            f"expected {sorted(agents)}, found {sorted(catalog)}"
        )

    routing = (ROOT / ".claude" / "SQUAD-ROUTING.md").read_text(encoding="utf-8")
    routing_catalog = set(
        re.findall(r"^\| [^|]+ \| ([a-z0-9][a-z0-9_-]*) \|$", routing, re.M)
    )
    if routing_catalog != agents:
        errors.append(
            "routing agent catalog mismatch: "
            f"expected {sorted(agents)}, found {sorted(routing_catalog)}"
        )

    for source in ACTIVE_DOCS:
        if re.search(r"\bmaya\b", source.read_text(encoding="utf-8"), re.I):
            errors.append(f"{source.relative_to(ROOT)}: stale agent name 'maya'")


def main() -> int:
    errors: list[str] = []
    validate_links(errors)
    validate_agents(errors)
    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
