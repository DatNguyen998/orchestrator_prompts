# How To Actually Use This Repo

You know the drill. You need an AI to sort forty agents into teams, so you go find
the prompt you wrote for this last time. Except it's not in this chat, it's in the
other chat, the one from three weeks ago, and half of it got edited out because you
were "just testing something." So you rewrite it from memory. You forget the
clarifying questions. You forget the part where it's supposed to double-check its
own work before handing it back. You get a team list with one of your agents
quietly missing, and you don't notice for a week.

This repo is that prompt, written once, checked, and left somewhere you can find it.

I'm sorry it took a whole repo to solve "stop losing your own prompts." It did.

## Three ways to use anything in here

Everything in this repo is one of three things, and the difference matters more
than it looks like it should.

**A prompt** (anything under `prompts/`) is just text. Copy it, paste it into
whatever chat window you have open — ChatGPT, Claude.ai, whatever — and it works.
Portable by design.

**A live agent** (anything under `.claude/agents/`) is not something you paste
anywhere. If you're working in this repo with Claude Code, it's already loaded.
You call it by name and it answers. No copy, no paste, nothing to remember.

**A skill** (anything under `skills/`) is Claude Code's own notion of a
reusable capability — a voice, a workflow, a checklist. If it's installed in
your session, you invoke it directly and never touch the file. If it isn't,
the file holds the full instructions anyway, so you paste them in and get the
same result. Belt and suspenders, on purpose.

Same idea, three different jobs. Pick based on where you're sitting, not on which
one sounds fancier.

## Which one are you?

**Case 1: you just want a good prompt, and you're not in Claude Code at all.**
You know you're here because you have a pile of AI agents/assistants and no clean
way to group them. Go to [`prompts/ai-squad-director-v2.md`](prompts/ai-squad-director-v2.md),
copy the system prompt out of the fenced block, paste it into your assistant of
choice. It'll ask you a few questions before it does anything — granularity, how
many teams, whether an agent can live on two teams at once. Answer them, or tell it
to use its judgment. It'll say out loud which defaults it picked if you do.

**Case 2: you're in this repo, in Claude Code, and you want the four seats.**
You'll know you're here because you're already talking to Claude Code inside this
project. atlas, canon, kai, and maya are just there — no setup, no install. Talk to
whichever one owns what you're asking about, or just ask the room; atlas is the one
that sorts out who answers what. That routing logic isn't a secret you have to
learn — it's written down in [`.claude/SQUAD-ROUTING.md`](.claude/SQUAD-ROUTING.md)
if you want to see the actual rule instead of trusting me.

**Case 3: you want to add your own prompt to this library.**
Drop a new file in `prompts/`, name it `kebab-case-like-this.md`. Give it a
one-line **Purpose** and a one-line **When to use**. Put the actual system prompt
in a fenced code block so the next person can copy-paste it without editing
anything out. Add a row to the table in `README.md`. That's the whole process —
it's supposed to be boring.

**Case 4: you want to write something in a specific voice, like this guide.**
Check [`skills/`](skills/) first — [`code-tutorial-writing`](skills/code-tutorial-writing.md)
is what wrote this exact page. If your Claude Code session has the skill
installed, just invoke it. If it doesn't, open the file and paste its
instructions block in yourself. Either way you get the same voice, not a
watered-down version because the install step didn't happen.

## What this won't do for you

No jokes in this section. This is the part you actually need to trust.

The four seats don't have any real documents backing them up right now. There's no
shared knowledge base in this repo for them to check against. They reason from
whatever's actually in the project plus the checklist built into their own prompt —
nothing more. If you tell `canon` "we ratified this last quarter," it has no record
of that happening, because nothing here recorded it. That's not the agent being
difficult. There's genuinely nothing to check.

None of these prompts or agents take irreversible action on their own. Nothing
sends, publishes, or deletes anything by itself. `atlas` is specifically built to
escalate real decisions instead of making them — that's not a limitation, that's
the point of the seat.

The routing between seats is exactly what's written in `SQUAD-ROUTING.md`. It's not
a smart, self-organizing thing that adapts on its own. If you want different
routing, you edit that file — you don't ask nicely.

## When a seat won't answer you

| What you're seeing | What's actually going on | What to do |
|---|---|---|
| A seat says it can't help, or flat-out refuses | The question is outside its lane, or (for `canon` specifically) nothing backs the claim you're asking it to confirm | Ask the seat that actually owns it, or ask `atlas` — reconciling cross-domain questions is its whole job |
| Squad Director just echoes your agent list back with no teams | You skipped past its clarifying questions | Answer them, or say "use your judgment" — it'll tell you what it defaulted to |
| Not sure whether to use v1 or v2 of the Squad Director | v1 is the bare original. v2 adds the integrity check, extra output formats, and a 3-round cap so revisions don't run forever | Default to v2 unless you specifically want the minimal one |
| An agent's name changed, or one went missing from your team output | Shouldn't happen — v2 has a mandatory check for exactly this, run as if by someone seeing it fresh | Say so directly: "you dropped/renamed an agent, fix it." That's a bug in that one response, not expected behavior |

## If something's actually broken

I've rewritten the "ask about team size" question in the Squad Director prompt
four separate times because I kept forgetting to ask it myself, so I'm not going
to pretend everything here is bulletproof on the first read.

If a seat refuses something it obviously should know, or the Squad Director drops
an agent it swore it wouldn't — that's not you holding it wrong. Open an issue, or
just tell me what broke and what you expected instead.
