# Skill Graph

A collection of [Claude skills](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/skills) built as **skill graphs** — modular, interlinked reference architectures instead of monolithic instruction files.

![cover](https://github.com/user-attachments/assets/45880f08-4feb-491d-ab3b-6d9f05b1de27)

## Why skill graphs?

A flat `SKILL.md` loads everything into context every time, whether Claude needs it or not. That works until it doesn't — the file grows, context gets noisy, and Claude starts drifting.

A skill graph fixes this:

- **Lean index** (`SKILL.md`) — a navigation map, always loaded, stays small
- **Reference files** — the actual depth, pulled in only when needed
- **Explicit links** — Claude traverses the graph purposefully instead of scanning a wall of text

Claude doesn't read your whole skill. It navigates it.

```
skill-name/
├── SKILL.md              ← index, always loaded
├── references/
│   ├── topic-a.md        ← loaded on demand
│   └── topic-b.md
└── scripts/              ← optional tooling
```

## What's here

### `skill-graph-creator/`

The core of this repo. A skill graph that teaches Claude how to build skill graphs — it's the methodology eating its own tail.

It walks Claude through the full creation process: clarifying what the skill needs to do, researching best practices, decomposing the domain into a graph structure, and packaging the result. The reference files cover core principles (conciseness, progressive disclosure, problem decomposition), graph architecture (index design, interlinking, context management), and a step-by-step creation pipeline.

### `skills/bespoke/`

Skills built as skill graphs from the ground up.

| Skill | Description |
|-------|-------------|
| `implementation-plan` | Structured implementation planning with mandatory research before coding |
| `plan-advisor` | General-purpose plan assessment and advisory |

### `skills/reforged/`

Existing skills converted into skill graph format. Each has an `ORIGIN.md` crediting the original.

| Skill | Original |
|-------|----------|
| `design-md` | [google-labs-code/stitch-skills](https://skills.sh/google-labs-code/stitch-skills/design-md) |
| `web-design-guidelines` | [vercel-labs/agent-skills](https://skills.sh/vercel-labs/agent-skills/web-design-guidelines) |
| `vercel-react-best-practices` | [vercel-labs/agent-skills](https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices) |
| `chat-ui` | [inference-sh/skills](https://github.com/inference-sh/skills/tree/main/ui/chat-ui) |

## Usage

Copy a skill's `SKILL.md` into your Claude Project instructions, or drop the entire skill folder into your Claude environment for full graph depth.

## License

[MIT](LICENSE) — individual skills may have their own licenses.
