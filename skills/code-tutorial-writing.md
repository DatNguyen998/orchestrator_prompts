# Code Tutorial Writing

**Purpose:** A voice for tutorials, internal guides, how-tos, runbooks, setup docs, onboarding docs, and READMEs — dry, first-person, conversational, instead of formal technical-writing tone. Blog-post rhythm (Basecamp / Julia Evans / Stripe-eng-blog lineage) applied to procedural content.

**When to use:** Writing, drafting, or rewriting a tutorial, guide, walkthrough, setup doc, script/tool writeup, or "how I automated X" post — or making an existing dev doc "less corporate," "more human," "funnier," or "sound like a real person wrote it." Not for formal external docs, API references, legal/compliance text, or anywhere a joke would undercut trust.

## How to use it

If the session has this skill installed, invoke it directly — `/code-tutorial-writing`, or just ask in plain language ("rewrite this setup doc in a more human voice"); the harness loads the full instructions for you and you never touch the block below.

If it isn't installed — this orchestrator hit exactly that case once — the instruction set is fully portable. Paste the block below as a system/style prompt ahead of whatever you're drafting, and it works the same way. No install, no dependency on the skill being registered anywhere.

This repo's own [`GUIDE.md`](../GUIDE.md) was written using this skill, as a worked example of the voice in practice.

## Skill instructions

```
name: code-tutorial-writing
description: Write code and tooling tutorials, internal guides, how-tos, runbooks, setup docs, onboarding docs, and READMEs in a dry, first-person, conversational voice instead of formal technical-writing tone. Use whenever the user asks to write, draft, or rewrite a tutorial, guide, walkthrough, setup doc, script/tool writeup, or "how I automated X" post — or asks to make an existing dev doc "less corporate," "more human," "funnier," or "sound like a real person wrote it."

# Code Tutorial Writing

A voice for internal tooling docs and how-to guides that people actually read past step 1. Source: a Notion guide about bulk-logging timesheets via a Claude Code script. Blog-post rhythm applied to procedural content — think Basecamp/Julia Evans/Stripe-eng-blog lineage, not a knowledge-base article.

Use this to draft new guides or rewrite dry ones. Not for formal external docs, API references, legal/compliance text, or anything where a joke would undercut trust.

## The core move

Every instruction is still 100% correct and complete — the humor rides on top of real information, it never replaces it. If a paragraph is funny but the reader can't actually complete the step from it, rewrite it. Correctness first, voice second.

## Voice principles

1. Second person, reader as protagonist. Not "the user configures the folder" — "you make a folder." The reader did the annoying thing, is doing the setup, will press the button. Never refer to "the user" in the body text.
2. Open with the pain, not the feature. Don't start "This guide explains how to use the bulk-log tool." Start with the tedious thing that made the tool necessary — the 20 dialog boxes, the repetitive click-through — described specifically enough that the reader recognizes their own week in it. The tool shows up as the answer, second.
3. One-line paragraphs as punchlines. After a longer explanatory sentence, drop a short, standalone line to land the point:
   Excel locks the file and likes to helpfully reformat your numbers into something the script can't read. Helpful!
   The joke is almost always the deadpan repetition or undercutting of a word from the sentence before, not a new idea.
4. Dry hyperbole for mundane pain, not for anything that matters. Exaggerate the tedium ("until you retire or the heat death of the universe") never the risk. Errors, data loss, and security stay flat and literal — no jokes there. Escalate absurdity only where the stakes are genuinely low.
5. Self-deprecating asides, stated plainly. "I'm sorry" before a setup step. "I tested this so you don't have to." The author admits the friction exists instead of pretending the tool is frictionless. This builds trust — it reads as honesty, not modesty-performance, so don't overdo it: one or two per doc, not one per section.
6. Headers that are mini-jokes, still fully scannable. "The boring bit (do this once)," "The one button you press yourself," "Look before you leap." Each header must still tell you exactly what's in the section if you're skimming — funny and functional, never funny instead of functional.
7. Branches told as stories, not specs. Don't write a decision tree or a bullet matrix for conditional logic. Narrate it as named cases the reader sorts themselves into:
   Case 1: it's your first time... Case 2: you're starting new work on a project you already log against... Case 3: it's just another week. Each case gets: how you'll recognize you're in it, then the linear sequence of steps, in that order.
8. Rhetorical questions as section transitions. "Which order do I do things in?" "Stuck?" Use the reader's actual next question as the header instead of a noun-phrase label.
9. Metaphor for the abstract, never for the mechanical. "A safety net nobody looks at is just decorative rope" explains why the preview step matters in one line, more effectively than three sentences of explanation. Reach for a metaphor when justifying a design choice or convincing the reader to actually do a step — not when just describing what a button does.
10. Close human, not corporate. End with a real offer, not "please reach out with any questions." State that you've made the mistakes yourself, then give a genuine way to reach you:
    I've made every mistake in this guide at least once, several of them twice.

### Sentence mechanics

- Short sentence after a technical one. Explain the mechanism, then land it in five words or fewer. This is the single most repeated rhythm in the source — use it every few paragraphs, not every sentence, or it stops landing.
- Imperative for instructions, always. "Open a terminal and type..." not "the terminal should be opened." No passive voice in step text, ever.
- Direct commands the reader can copy-paste, quoted plainly, e.g. what to literally say to the tool. Don't paraphrase the exact phrase — show it.
- Contractions everywhere. "you're," "don't," "that's" — never "you are," "do not," unless a sentence needs the emphasis of full form.
- Sentence fragments are fine for emphasis. "Done, no trip to the app."

### Anti-patterns — the corporate voice this replaces

Avoid, actively:
- "Please note that..." / "It is recommended that..." / "Kindly ensure..."
- "The user should..." / "One must..." / any third-person reader reference
- Passive voice in instructions ("the file is then created")
- Hedging qualifiers that add no information ("in most cases," "generally speaking") — if it's usually true, say when it isn't instead
- Headers that are just noun phrases with zero personality ("Prerequisites," "Configuration," "Troubleshooting") — replace with what the reader is actually wondering at that point
- Explaining a joke, or two jokes back to back — one beat, then move on
- Cheerfulness about genuine risk (security, data loss, money, deadlines) — flat and literal there, always

### Structural checklist for a new guide

1. Open with the specific tedious thing, described concretely, not abstractly.
2. One line stating the payoff ("type your hours, ask Claude to handle the rest, five seconds").
3. Setup steps, upfront, honestly labeled as the boring necessary part.
4. The one true prerequisite concept the reader needs before anything else makes sense — explained once, clearly, before the branching steps.
5. Branch by reader situation ("you'll know you're here because..."), not by feature.
6. A "what it won't do" section — scope and safety boundaries stated flatly, no jokes, so trust is explicit not implied.
7. Error/troubleshooting as a scannable table (symptom → meaning → fix), the one place a table beats prose.
8. Close with a personal, specific offer to help — not a generic contact line.

### Quick self-check before shipping a draft

- Read it aloud. If it sounds like a person explaining this to a coworker over Slack, keep it. If it sounds like a manual, rewrite the paragraph.
- Every joke sits next to real information — cut any joke that isn't.
- Every header still works as a pure scanning aid with the humor removed.
- Risk/safety sections are flat and literal, zero jokes.
- At least one short-sentence punchline per major section; not more than one self-deprecating aside per two sections.
```
