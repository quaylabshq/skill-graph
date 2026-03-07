# Core Principles

These foundational principles govern all skill graph creation. Every decision — from content placement to file structure — should be evaluated against these principles.

## Principles

| Principle | Summary | Reference |
|-----------|---------|-----------|
| Conciseness | The context window is a public good — only add what Claude doesn't already know | [conciseness.md](conciseness.md) |
| Degrees of Freedom | Match specificity to task fragility — narrow bridges need guardrails, open fields allow many routes | [degrees-of-freedom.md](degrees-of-freedom.md) |
| Progressive Disclosure | Three-level loading: metadata → SKILL.md → bundled resources | [progressive-disclosure.md](progressive-disclosure.md) |
| Skill Anatomy | Required structure: SKILL.md + optional scripts/, references/, assets/ | [skill-anatomy.md](skill-anatomy.md) |
| Problem Decomposition | Every problem must be recursively broken into atomic subproblems before solving | [problem-decomposition.md](problem-decomposition.md) |
| One-Shot Design | Design skill graphs so Claude can execute tasks in minimum roundtrips | [one-shot-design.md](one-shot-design.md) |

## How These Principles Apply to Graphs

In a skill graph, these principles compound:

- **Conciseness** drives the lean index design — SKILL.md contains only navigation, never detailed content.
- **Progressive disclosure** determines which reference files load when — Claude reads only what the current task requires.
- **Degrees of freedom** guide how prescriptive each reference file should be.
- **Skill anatomy** provides the structural foundation that the graph architecture extends.
- **Problem decomposition** ensures complex skills are broken into manageable, independent subproblems before implementation.
- **One-shot design** drives reference files to be self-contained, enabling Claude to execute tasks without roundtrips.

## See Also

- [Graph architecture principles](../graph-architecture/overview.md) — how to structure the graph itself
- [Creation process](../creation-process/overview.md) — how to apply these principles during skill creation
