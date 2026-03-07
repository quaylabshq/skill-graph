# Degrees of Freedom

Match the level of specificity to the task's fragility and variability.

## Freedom Levels

**High freedom** (text-based instructions): Use when multiple approaches are valid, decisions depend on context, or heuristics guide the approach.

**Medium freedom** (pseudocode or scripts with parameters): Use when a preferred pattern exists, some variation is acceptable, or configuration affects behavior.

**Low freedom** (specific scripts, few parameters): Use when operations are fragile and error-prone, consistency is critical, or a specific sequence must be followed.

## Mental Model

Think of Claude as exploring a path: a narrow bridge with cliffs needs specific guardrails (low freedom), while an open field allows many routes (high freedom).

## Applying to Skill Graphs

When structuring a skill graph, assign freedom levels to each component:

- **Index file (SKILL.md)**: Low freedom — must follow the navigation-only pattern strictly
- **Reference files**: Medium to high freedom — content can be organized flexibly within the file, but must follow interlinking requirements
- **Scripts**: Low freedom — deterministic, executable, tested
- **Process steps**: Low freedom for mandatory steps (clarification, research), medium freedom for implementation steps

## Back to

- [Core principles overview](overview.md)
