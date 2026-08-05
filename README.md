# orchestrator_prompts

A library of orchestrator system prompts. Each orchestrator prompt manages a specific
domain: it collects the input it needs, asks any clarifying questions, applies a
defined workflow, and produces output in a fixed format — routing or organizing
work across the relevant skills/agents as needed.

## Prompts

| Prompt | Purpose |
| --- | --- |
| [AI Squad Director](prompts/ai-squad-director.md) | Groups a list of AI agents/assistants into logical teams based on shared purpose, with configurable team granularity. |

## Adding a new orchestrator prompt

1. Create a new file under `prompts/` named `kebab-case-name.md`.
2. Give it a short header: **Purpose** (one line) and **When to use** (one line).
3. Write the full system prompt in a fenced code block so it can be copy-pasted directly into an assistant.
4. Add a row for it to the table above.
