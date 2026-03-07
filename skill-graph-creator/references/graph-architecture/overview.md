# Graph Architecture

Skill graphs replace monolithic SKILL.md files with interlinked reference networks. Every skill produced by this creator follows graph structure — there is no monolithic option.

## Why Graphs

Monolithic skill files become bloated as complexity grows. A single 500-line SKILL.md forces Claude to load everything even when only a fraction is relevant. Graphs solve this by:

1. **Targeted loading** — Claude reads only the reference files relevant to the current task
2. **Clear boundaries** — Each file covers one focused topic with explicit scope
3. **Traceability** — Every feature, script, and extension is indexed and cross-referenced
4. **Scalability** — New features add new reference files without inflating the index

## Core Structural Principles

| Principle | Description | Reference |
|-----------|-------------|-----------|
| Lean index | SKILL.md contains only navigation tables and links | [index-design.md](index-design.md) |
| Hub-and-spoke | Hub files link down to detail files; detail files link back up | [interlinking.md](interlinking.md) |
| Logical decomposition | Content splits along natural boundaries (features, steps, domains) | [decomposition.md](decomposition.md) |
| Explicit extensions | Every future capability or division point is documented | [extension-points.md](extension-points.md) |
| Context management | Deliberate context budget planning, delegation to sub-contexts, clean main thread | [context-management.md](context-management.md) |

## Graph Invariants

These must hold true for every skill graph:

1. SKILL.md is under 100 lines and contains zero implementation details
2. Every file in `references/` is reachable from SKILL.md within 2 hops
3. No orphan files — every file is linked from at least one other file
4. No duplicate content — information lives in exactly one place
5. Every hub file (`overview.md`) links to all files in its directory
6. Reference files should be self-contained for their subtask (one-shot test)

## See Also

- [Core principles](../core-principles/overview.md) — foundational rules that apply to all skill creation
- [Creation process — step 6: implement](../creation-process/step-6-implement.md) — how to build the graph during implementation
