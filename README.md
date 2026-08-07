# orchestrator_prompts

A library of orchestrator system prompts. Each orchestrator prompt manages a specific
domain: it collects the input it needs, asks any clarifying questions, applies a
defined workflow, and produces output in a fixed format — routing or organizing
work across the relevant skills/agents as needed.

## Prompts

| Prompt | Purpose |
| --- | --- |
| [AI Squad Director](prompts/ai-squad-director.md) | Baseline version. Groups a list of AI agents/assistants into logical teams based on shared purpose, with configurable team granularity. |
| [AI Squad Director v2 (Enhanced)](prompts/ai-squad-director-v2.md) | Adds description/tag-aware clustering, an integrity check against dropped or invented agents, table/JSON output modes, chunking rules, an iteration loop, edge-case handling, and an optional orchestrator-layer proposal. |

Some prompts here are adapted from, or inspired by, third-party sources — see each prompt's own **Credit** line for attribution. The v2 Squad Director prompt builds on [danielrosehill/AI-Orchestration-System-Prompts](https://github.com/danielrosehill/AI-Orchestration-System-Prompts).

## Adding a new orchestrator prompt

1. Create a new file under `prompts/` named `kebab-case-name.md`.
2. Give it a short header: **Purpose** (one line) and **When to use** (one line).
3. Write the full system prompt in a fenced code block so it can be copy-pasted directly into an assistant.
4. Add a row for it to the table above.

## Live agents (`.claude/agents/`)

Some seats are wired up as real Claude Code subagents rather than copy-paste
prompts, so they can be invoked directly in this project:

| Agent | Seat |
| --- | --- |
| [atlas](.claude/agents/atlas.md) | Chief of staff — priorities, work graph, decisions, cadence, escalation. |
| [canon](.claude/agents/canon.md) | Knowledge and memory — the canon graph, diagrams, conventions, provenance. |
| [kai](.claude/agents/kai.md) | Audience and growth — ICP, content systems, community, campaigns. |
| [maya](.claude/agents/maya.md) | Operations and customer success — onboarding, support, incident learning. |

These four form one "community operating system" squad, each owning a
distinct domain and each with one thing it refuses to do: atlas won't make a
decision that belongs to the owner, canon won't present a guess as settled
fact, kai won't claim a growth number with no measurement behind it, and maya
won't pin a systemic failure on a person. They reason from whatever project
context is actually available to them (via Read/Grep/Glob) plus the lens and
checklist baked into each prompt — they don't cite or depend on any canon
documents, since this repo doesn't have any.
