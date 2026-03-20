# Planning Process

A six-step process for creating thorough implementation plans. Steps 0.5, 1–2, 4.5, and 5 are **mandatory** and must never be skipped.

## Process Summary

| Step | Name | Status | Reference |
|------|------|--------|-----------|
| 0.5 | Domain Classification | **Mandatory** | [domain-classification.md](domain-classification.md) |
| 1 | Clarification | **Mandatory** | [step-1-clarification.md](step-1-clarification.md) |
| 2 | Research | **Mandatory** | [step-2-research.md](step-2-research.md) |
| 3 | Decompose | Required | [step-3-decompose.md](step-3-decompose.md) |
| 4 | Generate Plan | Required | [step-4-generate-plan.md](step-4-generate-plan.md) |
| 4.5 | Multi-Agent Verification | **Mandatory** | [step-4.5-verification.md](step-4.5-verification.md) |
| 5 | Present | **Mandatory** | [step-5-present.md](step-5-present.md) |

### Cross-Cutting Layers

| Layer | Purpose | Reference |
|-------|---------|-----------|
| Pre/Post Eval | Evaluation gates wrapping every step | [pre-post-eval.md](pre-post-eval.md) |
| Quality Doctrine | Google/NASA-grade reasoning applied to every plan | [step-4-generate-plan.md — quality doctrine](step-4-generate-plan.md#quality-doctrine-googlenasa-grade-reasoning) |
| Goal-Driven Methodology | Criteria-first planning: TDD for code, acceptance criteria for non-code | [goal-driven-methodology overview](../goal-driven-methodology/overview.md) |

## Critical Rules

1. **Classify the task first** — before any questions are asked
2. **Always start with clarification** — never plan without questioning first
3. **Always research** — codebase tasks explore the codebase; non-code tasks research the domain via web
4. **Apply pre-eval before each step and post-eval after** — see [pre-post-eval.md](pre-post-eval.md)
5. **Questions can happen at any step** — if ambiguity is discovered mid-process, return to clarification
6. **Follow the order** — steps are sequential; skipping ahead results in shallow plans
7. **Always verify with multi-agent panel** — no plan is presented without passing independent verification by 3+ agents
8. **Always present and wait for approval** — never auto-execute after planning
9. **Delegate research to sub-agents** — keep the main context clean for planning and conversation
10. **Adapt plan depth to task complexity** — simple tasks get lightweight plans, complex tasks get detailed ones
11. **Apply the quality doctrine** — every plan must meet Google/NASA-grade standards: zero unstated assumptions, provable correctness, documented rationale, failure mode awareness
12. **Criteria before approach** — every plan step is structured acceptance-criteria-first (TDD for code, observable criteria for non-code). See [goal-driven methodology](../goal-driven-methodology/overview.md)

## Permanent Steps Checklist

Before presenting any plan, verify:

- [ ] Task was classified by domain profile
- [ ] Clarifying questions were asked and answered
- [ ] Research was performed (codebase or web)
- [ ] Task was decomposed into subtasks
- [ ] Plan was structured with core template + adaptive sections
- [ ] Every step has acceptance criteria defined BEFORE the approach (goal-driven)
- [ ] For code tasks: test specifications are precise and follow TDD structure
- [ ] For non-code tasks: criteria are observable and have defined evaluation methods
- [ ] Quality doctrine applied — rationale documented, assumptions explicit, failure modes acknowledged
- [ ] Pre/post eval performed at each step
- [ ] Multi-agent verification passed — all agents reached PASS or CONDITIONAL PASS consensus
- [ ] Verification report compiled and attached
- [ ] Plan presented for user approval

## See Also

- [Questionnaire framework](../questionnaire-framework/overview.md) — drives step 1 and ongoing questioning
- [Research framework](../research-framework/overview.md) — drives step 2
- [Context management](../context-management.md) — delegation strategies
- [Output format](../output-format/overview.md) — plan structure
- [Multi-agent verification](step-4.5-verification.md) — drives step 4.5
- [Goal-driven methodology](../goal-driven-methodology/overview.md) — criteria-first planning (TDD + acceptance criteria)
