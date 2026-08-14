# Changelog

All notable changes to this repository are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and versioning follows [Semantic Versioning](https://semver.org/) as applied
to a prompt/agent library: **MAJOR** for breaking renames or removed
seats/prompts, **MINOR** for new prompts/agents/skills or backward-compatible
behavior changes, **PATCH** for fixes, renames, and doc-only corrections.

Each entry lists what changed, which files it touched, and which
prompts/agents/skills are impacted so you know what to re-read before you
rely on them again.

A rendered, browsable view of this file lives at
[`docs/changelog.html`](docs/changelog.html).

## [Unreleased]

## [0.6.0] - 2026-08-14

### Added
- `CHANGELOG.md` (this file) and `docs/changelog.html`, a static HTML view
  of the same history for browsing outside a git client.

**Impacted:** repo docs only. No prompt, agent, or skill content changed.

---

## [0.5.0] - 2026-08-11

_Merged as PR #5._

### Added
- `skills/` directory as a third content category alongside `prompts/` and
  `.claude/agents/` — for portable Claude Code skill instructions kept
  self-contained enough to paste into a session where the skill isn't
  installed.
- `skills/code-tutorial-writing.md`: dry, first-person, conversational
  voice for tutorials/guides/runbooks/READMEs (the voice `GUIDE.md` itself
  is written in).

### Changed
- `README.md`: new "Skills" section (table + how to use/add one), mirroring
  the existing Prompts and Live agents sections.
- `GUIDE.md`: reframed from "two ways to use this repo" to three (prompts,
  live agents, skills), plus a fourth reader case for "you want to write
  something in this voice."

**Impacted:** `skills/code-tutorial-writing.md` (new), `README.md`,
`GUIDE.md`. No existing prompt or agent behavior changed.

---

## [0.4.0] - 2026-08-10

_Merged as PR #4._

### Added
- `GUIDE.md`: conversational, second-person how-to-use-this-repo doc.
  Covers the prompt-files-vs-live-agents distinction, three reader cases
  (paste-a-prompt user, in-repo Claude Code user, contributor adding a new
  prompt), an explicit "what this won't do" section (no canon documents
  backing the squad, no irreversible actions, routing is fixed not
  adaptive), and a symptom → meaning → fix table for seat refusals.

### Changed
- `README.md`: added one linking line to `GUIDE.md`; README's own
  reference-tone voice is otherwise untouched.

**Impacted:** new doc (`GUIDE.md`), `README.md` link only. No prompt or
agent files changed.

---

## [0.3.1] - 2026-08-10

### Changed
- Renamed `.claude/agents/maya.md` → `.claude/agents/shinsho.md`
  (seat identity/name update; operations & customer success
  responsibilities are unchanged).

**Impacted:** the operations/customer-success agent (`maya` → `shinsho`).
Any reference to the seat by its old name (`maya`) — including in
`.claude/SQUAD-ROUTING.md` cross-references and README's Live agents
table — should be re-checked against the new name.

---

## [0.3.0] - 2026-08-08

_Merged as PR #3 (2026-08-09)._

### Added
- `.claude/SQUAD-ROUTING.md`: the missing task graph for the atlas / canon /
  kai / maya squad. Single-domain questions route straight to the owning
  seat; cross-domain questions route as a diamond, with **atlas fixed as
  the merge owner** so no seat's output reaches the user pre-merged by
  anyone else.
- `LICENSE` (MIT), matching the source repo's own licensing practice.

### Changed
- `.claude/agents/atlas.md`: wired in explicit merge-owner responsibility.
- `.claude/agents/canon.md`, `.claude/agents/kai.md`,
  `.claude/agents/maya.md`: added an "out of lane, defer to X" line each.
- `prompts/ai-squad-director-v2.md`: reframed the step-5 integrity check
  from a self-graded pass into an explicit fresh-eyes/auditor pass, and
  capped the step-8 iteration loop at 3 rounds (after which it ships the
  current best version and names what's unresolved).
- `README.md`: added a License section; Live agents section now points to
  `SQUAD-ROUTING.md` instead of describing four seats with no stated
  relationship between them.

**Impacted:** all four squad agents (`atlas`, `canon`, `kai`, `maya`) via
routing/deferral behavior, `prompts/ai-squad-director-v2.md`'s integrity-check
and iteration-loop steps, plus new routing doc and license.

---

## [0.2.0] - 2026-08-07

_Merged as PR #2._

### Added
- Community-OS agent squad under `.claude/agents/`: `atlas` (chief of
  staff — priorities, work graph, decisions, cadence, escalation),
  `canon` (knowledge & memory — canon graph, conventions, provenance),
  `kai` (audience & growth — ICP, content systems, campaigns), `maya`
  (operations & customer success — onboarding, support, incident
  learning). Each converted from a supplied seat prompt into a real
  Claude Code subagent with Read/Grep/Glob access, keeping its original
  lens, pre-answer checklist, and refusal clause verbatim.

### Changed
- Dropped the numbered-canon-document grounding/citation requirement
  (canon docs 00–15) from all four seats — those documents don't exist in
  this repo, so the requirement made every seat refuse almost everything.
  Refusal rules that depended on citing a specific document were rewritten
  to keep their intent without the dependency (e.g. canon: "answering from
  general knowledge when no canon grounds the question" →
  "presenting a guess as settled fact").
- `README.md`: documents the squad; Live agents section rewritten to
  describe what each seat refuses instead of the removed citation
  requirement.

**Impacted:** all four squad agents (`atlas`, `canon`, `kai`, `maya`) —
both their creation and, in the same release, a correction to their
refusal/grounding rules.

---

## [0.1.0] - 2026-08-05

_Merged as PR #1._

### Added
- Repository scaffold: `README.md` describing the repo's purpose and how
  to add a new orchestrator prompt.
- `prompts/ai-squad-director.md` — baseline AI Squad Director prompt
  (groups a list of AI agents/assistants into logical teams based on
  shared purpose, with configurable team granularity).
- `prompts/ai-squad-director-v2.md` — enhanced version, built on v1 (itself
  sourced from `danielrosehill/AI-Orchestration-System-Prompts`), adding
  description/tag-aware clustering, an explicit clarifying-question batch
  with stated defaults, a team-count heuristic driven by inventory size,
  grouping constraints (no singleton or dominant team), a mandatory
  integrity check against dropped/invented agents, table and JSON output
  modes alongside markdown, a clarified chunking rule with an
  iteration/refinement loop, defined edge-case handling, and an optional
  orchestrator-layer proposal (off by default).

**Impacted:** new prompts only — `prompts/ai-squad-director.md`,
`prompts/ai-squad-director-v2.md`. No agents existed yet.

---

## [0.0.1] - 2026-08-05

### Added
- Initial commit — empty repository scaffold with a one-line `README.md`.

**Impacted:** repo initialization only.

[Unreleased]: https://github.com/DatNguyen998/orchestrator_prompts/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/DatNguyen998/orchestrator_prompts/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/DatNguyen998/orchestrator_prompts/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/DatNguyen998/orchestrator_prompts/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/DatNguyen998/orchestrator_prompts/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/DatNguyen998/orchestrator_prompts/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/DatNguyen998/orchestrator_prompts/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/DatNguyen998/orchestrator_prompts/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/DatNguyen998/orchestrator_prompts/releases/tag/v0.0.1
