---
name: skill-graph-creator
description: Guide for creating skill graphs — interlinked, modular skill architectures that decompose knowledge into navigable reference networks. Use when users want to create a new skill graph (or upgrade an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. Always produces graph-structured output with lean index files, interlinked references, and explicit extension points.
---

# Skill Graph Creator

This skill provides a navigable reference graph for creating skill graphs. All detailed content lives in reference files and tool scripts — this file contains only navigation.

## Core Principles

Foundational rules preserved from the skill creation framework:

| Principle | Reference |
|-----------|-----------|
| Overview of all principles | [references/core-principles/overview.md](references/core-principles/overview.md) |
| Conciseness & context efficiency | [references/core-principles/conciseness.md](references/core-principles/conciseness.md) |
| Degrees of freedom | [references/core-principles/degrees-of-freedom.md](references/core-principles/degrees-of-freedom.md) |
| Progressive disclosure | [references/core-principles/progressive-disclosure.md](references/core-principles/progressive-disclosure.md) |
| Skill anatomy & structure | [references/core-principles/skill-anatomy.md](references/core-principles/skill-anatomy.md) |
| Problem decomposition | [references/core-principles/problem-decomposition.md](references/core-principles/problem-decomposition.md) |
| One-shot design | [references/core-principles/one-shot-design.md](references/core-principles/one-shot-design.md) |

## Graph Architecture

How to structure skills as interlinked graphs instead of monolithic files:

| Topic | Reference |
|-------|-----------|
| Graph principles overview | [references/graph-architecture/overview.md](references/graph-architecture/overview.md) |
| Index design (lean SKILL.md) | [references/graph-architecture/index-design.md](references/graph-architecture/index-design.md) |
| Interlinking patterns | [references/graph-architecture/interlinking.md](references/graph-architecture/interlinking.md) |
| Content decomposition | [references/graph-architecture/decomposition.md](references/graph-architecture/decomposition.md) |
| Extension points | [references/graph-architecture/extension-points.md](references/graph-architecture/extension-points.md) |
| Context management | [references/graph-architecture/context-management.md](references/graph-architecture/context-management.md) |

## Creation Process

Nine-step process for building a skill graph. Steps 0.5, 1–2, and 9 are **mandatory** and must never be skipped:

| Step | Description | Reference |
|------|-------------|-----------|
| Overview | Full process summary | [references/creation-process/overview.md](references/creation-process/overview.md) |
| 0.5. Domain classification | Classify task profile | [references/creation-process/domain-classification.md](references/creation-process/domain-classification.md) |
| 1. Clarification | Mandatory questioning phase | [references/creation-process/step-1-clarification.md](references/creation-process/step-1-clarification.md) |
| 2. Research | Gather best practices & standards | [references/creation-process/step-2-research.md](references/creation-process/step-2-research.md) |
| 3. Understand | Concrete usage examples | [references/creation-process/step-3-understand.md](references/creation-process/step-3-understand.md) |
| 4. Plan | Structure the graph & resources | [references/creation-process/step-4-plan.md](references/creation-process/step-4-plan.md) |
| 5. Initialize | Run init_skill_graph.py | [references/creation-process/step-5-initialize.md](references/creation-process/step-5-initialize.md) |
| 6. Implement | Write index, references, scripts | [references/creation-process/step-6-implement.md](references/creation-process/step-6-implement.md) |
| 7. Package | Run package_skill.py | [references/creation-process/step-7-package.md](references/creation-process/step-7-package.md) |
| 8. Iterate | Refine based on real usage | [references/creation-process/step-8-iterate.md](references/creation-process/step-8-iterate.md) |
| 9. Final eval | Bird's-eye review of entire skill graph | [references/creation-process/step-9-final-eval.md](references/creation-process/step-9-final-eval.md) |
| — Pre/Post eval | Evaluation gates wrapping every step | [references/creation-process/pre-post-eval.md](references/creation-process/pre-post-eval.md) |
| — Feedback checkpoints | Structured validation loops | [references/creation-process/feedback-checkpoints.md](references/creation-process/feedback-checkpoints.md) |

## Frameworks

Reusable frameworks referenced throughout the creation process:

| Framework | Purpose | Reference |
|-----------|---------|-----------|
| Questionnaire | Mandatory clarification & ongoing questioning | [references/questionnaire-framework/overview.md](references/questionnaire-framework/overview.md) |
| Research | Best practices & standards gathering | [references/research-framework/overview.md](references/research-framework/overview.md) |
| Planning | Todo lists & permanent process steps | [references/planning-framework/overview.md](references/planning-framework/overview.md) |

## Tool Scripts

| Tool | Script | Purpose |
|------|--------|---------|
| Initialize | [scripts/init_skill_graph.py](scripts/init_skill_graph.py) | Create a new skill graph from template |
| Validate | [scripts/validate_graph.py](scripts/validate_graph.py) | Validate graph structure, links, and metadata |
| Package | [scripts/package_skill.py](scripts/package_skill.py) | Package skill graph into distributable .skill file |

## Design Patterns

| Pattern | Reference |
|---------|-----------|
| Workflow patterns | [references/workflows.md](references/workflows.md) |
| Output patterns | [references/output-patterns.md](references/output-patterns.md) |
