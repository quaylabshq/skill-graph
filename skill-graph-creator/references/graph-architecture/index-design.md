# Index Design

The SKILL.md file in a skill graph serves exclusively as a navigation index. It contains no implementation details, no explanatory prose, and no code.

## Structure of a Graph Index

A navigation-only SKILL.md follows this pattern:

```markdown
---
name: skill-name
description: [comprehensive description covering what + when]
---

# Skill Name

One-line summary stating this is a navigable reference graph.

## [Category 1]

Short contextual sentence.

| Topic | Reference |
|-------|-----------|
| Feature A | [references/feature-a.md](references/feature-a.md) |
| Feature B | [references/feature-b.md](references/feature-b.md) |

## [Category 2]

| Tool | Script | Purpose |
|------|--------|---------|
| Tool X | [scripts/tool-x.py](scripts/tool-x.py) | One-line purpose |
```

## Rules

1. **Tables for indexing** — Use markdown tables to list features, references, and scripts
2. **One-sentence descriptions** — Each table entry gets a brief purpose, not a paragraph
3. **Direct links** — Every reference file and script is linked with a relative path
4. **Grouped by category** — Related items are grouped under clear section headers
5. **Under 100 lines** — If the index exceeds this, the graph needs restructuring (too many top-level categories)

## What Does NOT Belong in the Index

- Detailed explanations of how features work
- Code examples or implementation guidance
- Extended descriptions or motivation
- Process steps (link to them instead)
- Configuration instructions

## Reference Example

The mem0 skill graph demonstrates this pattern:

- 57 lines total
- 4 sections: Offerings, Platform Reference Graph, Tool Scripts, Implementation Code Examples
- Each section is a table or bullet list with links
- Zero implementation content

## Back to

- [Graph architecture overview](overview.md)
- See also: [Skill anatomy](../core-principles/skill-anatomy.md) — structural requirements for SKILL.md
