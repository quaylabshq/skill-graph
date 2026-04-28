# Skill Graph

**Author Claude Skills as interlinked graphs, not monolithic SKILL.md files.**

A methodology and toolkit for building [Anthropic Claude Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) as modular reference networks — lean indexes, on-demand depth, validator-enforced invariants.

<img width="2400" height="960" alt="cover-52" src="https://github.com/user-attachments/assets/d5ee5536-adf3-4a01-9f7d-4a6798dc6769" />

## The problem

A monolithic `SKILL.md` loads everything into Claude's context every turn — the table of contents, the rationale, the edge cases, the rarely-needed appendices, all of it. That works at 50 lines. By 500 lines it's a tax: tokens are burned on instructions Claude doesn't need, the signal-to-noise ratio drops, and behavior starts drifting because the model has to re-decide what's relevant on every call.

The failure mode is structural, not stylistic. You can't prompt-engineer your way out of a context budget.

## The solution

Treat a skill like a small codebase. Split it into:

- **A lean index (`SKILL.md`)** — always loaded, kept short, contains only navigation
- **Reference files** — the actual depth, pulled in on demand via explicit links
- **Category hubs (`overview.md`)** — let the index point at a topic, not every leaf

Two design rules make the graph navigable:

- **2-hop reachability** — every reference is reachable from `SKILL.md` in at most two link traversals
- **No orphans** — every file under `references/` and `scripts/` is linked from somewhere in the graph

Claude doesn't read your whole skill. It navigates it — purposefully, one hop at a time.

## Before / after

```
# Monolithic                          # Skill graph
skill-name/                           skill-name/
└── SKILL.md      (800+ lines,        ├── SKILL.md          (≤100 lines, index only)
                   loaded every       ├── references/
                   turn)              │   ├── core-principles/
                                      │   │   ├── overview.md     (hub)
                                      │   │   ├── conciseness.md
                                      │   │   └── decomposition.md
                                      │   ├── workflows.md
                                      │   └── output-patterns.md
                                      └── scripts/
                                          └── helper.py
```

Same content. The graph version loads the 80-line index every turn and pulls a single reference (≈40 lines) when relevant — typically a 5–10× reduction in always-on context.

## Quickstart

The three scripts live in [`skill-graph-creator/scripts/`](skill-graph-creator/scripts/):

```bash
# Scaffold a new skill graph from the template
python skill-graph-creator/scripts/init_skill_graph.py my-skill --path skills/bespoke

# Lint the graph (frontmatter, links, orphans, index size)
python skill-graph-creator/scripts/validate_graph.py skills/bespoke/my-skill

# Bundle into a distributable .skill file (validates first)
python skill-graph-creator/scripts/package_skill.py skills/bespoke/my-skill ./dist
```

`package_skill.py` runs `validate_graph.py` automatically and refuses to bundle an invalid graph.

## Graph invariants

`validate_graph.py` enforces six hard rules. A graph that violates any of them is not packageable.

1. **Valid frontmatter.** `SKILL.md` has YAML frontmatter with `name` (kebab-case, ≤64 chars) and `description` (≤1024 chars, no angle brackets). Only the allowed key set — `name`, `description`, `license`, `allowed-tools`, `metadata`, `compatibility` — is permitted.
2. **Lean index.** `SKILL.md` is ≤100 lines. The index is navigation, not content.
3. **Link integrity.** Every relative markdown link in every file resolves to an existing file. Code-fence examples are excluded.
4. **No orphans.** Every file under `references/` and `scripts/` is linked from somewhere reachable in the graph.
5. **2-hop reachability.** All references are reachable from `SKILL.md` within two hops — typically index → category `overview.md` → leaf.
6. **Bounded nesting.** Subdirectories under `references/` go one level deep (e.g. `references/<category>/<file>.md`), not arbitrarily nested.

Together these act as a tiny type system for skill prose: you can refactor a graph confidently because the linter catches the structural breakage.

## What's in this repo

| Path | Kind | What it is |
|------|------|------------|
| [`skill-graph-creator/`](skill-graph-creator/) | meta-skill | A skill graph that teaches Claude to build skill graphs. Ships the three scripts above. |
| [`skills/bespoke/implementation-plan/`](skills/bespoke/implementation-plan/) | bespoke | Structured implementation planning with mandatory research before coding. |
| [`skills/bespoke/plan-advisor/`](skills/bespoke/plan-advisor/) | bespoke | General-purpose plan assessment and advisory. |
| [`skills/reforged/design-md/`](skills/reforged/design-md/) | reforged | From [google-labs-code/stitch-skills](https://skills.sh/google-labs-code/stitch-skills/design-md). |
| [`skills/reforged/web-design-guidelines/`](skills/reforged/web-design-guidelines/) | reforged | From [vercel-labs/agent-skills](https://skills.sh/vercel-labs/agent-skills/web-design-guidelines). |
| [`skills/reforged/vercel-react-best-practices/`](skills/reforged/vercel-react-best-practices/) | reforged | From [vercel-labs/agent-skills](https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices). |
| [`skills/reforged/chat-ui/`](skills/reforged/chat-ui/) | reforged | From [inference-sh/skills](https://github.com/inference-sh/skills/tree/main/ui/chat-ui). |

Every reforged skill ships an `ORIGIN.md` crediting the upstream source, the original commit reference, and any structural changes made during the reforge — so attribution travels with the skill, not just the README.

## Reforging guide

Converting a community skill into graph form is a five-step refactor:

1. **Read the source.** Note the natural section breaks in the monolithic `SKILL.md` — these become your category hubs.
2. **Initialize.** `python skill-graph-creator/scripts/init_skill_graph.py <name> --path skills/reforged`. Drop in the upstream `LICENSE.txt` and an `ORIGIN.md` with the source link, original author, and a one-line "reforged from" note.
3. **Decompose.** Move each section into a leaf file under `references/<category>/`. Keep leaves single-purpose; create a category `overview.md` only when there are 2+ siblings.
4. **Re-index.** Replace the original prose with a navigation table in `SKILL.md`. The index links to category hubs (or directly to leaves for flat categories) — never deeper than two hops away.
5. **Validate.** `python skill-graph-creator/scripts/validate_graph.py skills/reforged/<name>` until clean. Then `package_skill.py`.

The four reforged skills in this repo are worked examples of the pattern.

## How this differs

Skill graphs are **orthogonal** to existing "graph" frameworks in the agent space:

- **LangGraph** is a state-machine runtime — graphs of computation, edges of control flow, executed at inference time.
- **AutoGen / LangChain skill libraries** are imperative tool functions registered to an agent.
- **Skill graphs** apply graph structure to the **skill prose itself** — the static instruction text Claude reads — for context-budget efficiency, with the structural rules codified as validator invariants.

You can ship a LangGraph-orchestrated agent whose every node loads a skill-graph-structured skill. They sit at different layers.

## Compatibility

Conforms to the [Anthropic Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) specification. The optional `compatibility` frontmatter key is supported and validated. Drop a skill folder into any Claude environment that accepts Agent Skills, or copy its `SKILL.md` into Claude Project instructions for index-only use.

## Roadmap & contributing

- More reforged skills from the community ecosystem
- Richer validator checks (description quality heuristics, broken-anchor detection)
- A "graph linter" GitHub Action

PRs welcome — start by opening an issue describing the skill or check you'd like to add. New reforged skills must include an `ORIGIN.md` and pass `validate_graph.py`.

## License

[MIT](LICENSE) — individual skills under `skills/reforged/` retain their upstream licenses; see each skill's `LICENSE.txt` and `ORIGIN.md`.
