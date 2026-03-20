---
name: implementation-plan
description: >
  Structured implementation planning skill that enhances Claude's plan mode with mandatory questioning,
  research, problem decomposition, goal-driven criteria-first planning, and multi-agent verification
  before any implementation begins. Use when the user asks to plan a task, create an implementation
  plan, think through an approach, or when Claude enters plan mode. Plans are goal-driven: for code
  tasks, every step follows TDD (tests specified before implementation); for non-code tasks, every
  step has observable acceptance criteria defined before the approach. Plans are held to Google/NASA-
  grade quality standards and must pass independent verification by 3+ specialized sub-agents
  (requirements traceability, technical rigor, security & threat analysis) before presentation.
  Handles any domain — software engineering, design, business, research, content — by adapting its
  questioning depth, research strategy, and plan detail to the task's complexity and type. Always
  explores the codebase for code tasks; uses web research for non-code tasks.
---

# Implementation Plan

A navigable reference graph for creating thorough implementation plans. Enhances plan mode with mandatory questioning, research, context-efficient decomposition, and multi-agent verification to Google/NASA-grade quality standards.

## Planning Process

Six-step process. Steps 0.5, 1–2, 4.5, and 5 are **mandatory** and must never be skipped:

| Step | Description | Reference |
|------|-------------|-----------|
| Overview | Full process summary + critical rules | [references/planning-process/overview.md](references/planning-process/overview.md) |
| 0.5 | Domain classification — classify the task first | [references/planning-process/domain-classification.md](references/planning-process/domain-classification.md) |
| 1 | Clarification — mandatory questioning phase | [references/planning-process/step-1-clarification.md](references/planning-process/step-1-clarification.md) |
| 2 | Research — codebase exploration or web research | [references/planning-process/step-2-research.md](references/planning-process/step-2-research.md) |
| 3 | Decompose — recursive task breakdown | [references/planning-process/step-3-decompose.md](references/planning-process/step-3-decompose.md) |
| 4 | Generate plan — create the structured plan with quality doctrine | [references/planning-process/step-4-generate-plan.md](references/planning-process/step-4-generate-plan.md) |
| 4.5 | Multi-agent verification — independent sub-agents verify the plan | [references/planning-process/step-4.5-verification.md](references/planning-process/step-4.5-verification.md) |
| 5 | Present — show plan + verification report and wait for approval | [references/planning-process/step-5-present.md](references/planning-process/step-5-present.md) |
| — | Pre/Post eval gates wrapping every step | [references/planning-process/pre-post-eval.md](references/planning-process/pre-post-eval.md) |

## Questionnaire Framework

Drives all question generation — initial, mid-process, and domain-adapted:

| Topic | Reference |
|-------|-----------|
| Overview + core rules | [references/questionnaire-framework/overview.md](references/questionnaire-framework/overview.md) |
| Initial question categories | [references/questionnaire-framework/initial-questions.md](references/questionnaire-framework/initial-questions.md) |
| Mid-process gap identification | [references/questionnaire-framework/mid-process-questions.md](references/questionnaire-framework/mid-process-questions.md) |
| Domain adaptation | [references/questionnaire-framework/domain-adaptation.md](references/questionnaire-framework/domain-adaptation.md) |

## Research Framework

How to gather information before planning — codebase or web-based:

| Topic | Reference |
|-------|-----------|
| Overview + research principles | [references/research-framework/overview.md](references/research-framework/overview.md) |
| Codebase exploration | [references/research-framework/codebase-exploration.md](references/research-framework/codebase-exploration.md) |
| Web/domain research | [references/research-framework/web-research.md](references/research-framework/web-research.md) |

## Goal-Driven Methodology

Criteria-first planning across all domains. For technical tasks: TDD. For non-technical tasks: acceptance-criteria-driven.

| Topic | Reference |
|-------|-----------|
| Overview + core principle | [references/goal-driven-methodology/overview.md](references/goal-driven-methodology/overview.md) |
| Technical TDD planning | [references/goal-driven-methodology/technical-tdd.md](references/goal-driven-methodology/technical-tdd.md) |
| Non-technical acceptance criteria | [references/goal-driven-methodology/non-technical-criteria.md](references/goal-driven-methodology/non-technical-criteria.md) |

## Context Management

| Topic | Reference |
|-------|-----------|
| Budget, delegation, clean context | [references/context-management.md](references/context-management.md) |

## Output Format

Standardized core plan structure with adaptive detail sections:

| Topic | Reference |
|-------|-----------|
| Format principles | [references/output-format/overview.md](references/output-format/overview.md) |
| Core template (fixed sections) | [references/output-format/core-template.md](references/output-format/core-template.md) |
| Adaptive sections (domain-specific) | [references/output-format/adaptive-sections.md](references/output-format/adaptive-sections.md) |
