# Goal-Driven Methodology

A cross-cutting layer that transforms the entire planning process from activity-driven ("what do we do?") to goal-driven ("what does done look like, and how do we get there?"). This is not optional — it is the foundational paradigm for all plans produced by this skill.

## Core Principle: Acceptance-First Planning

Traditional planning asks "What do we need to do?" and hopes the activities produce the right outcome. Goal-driven planning inverts this: define the outcome first, then design the minimum activities to achieve it, then verify the outcome is met.

This is TDD applied to planning itself. The "test" comes before the "code" — always, in every domain.

## The Universal Cycle

Every plan step — regardless of domain — follows this cycle:

```
┌──────────────────────────────────┐
│  1. DEFINE (the "Red" phase)     │
│  What does done look like?       │
│  Write acceptance criteria.      │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│  2. PLAN (the "Green" phase)     │
│  What is the minimal approach    │
│  to meet the criteria?           │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│  3. VERIFY (the "Refactor" phase)│
│  Does the approach satisfy all   │
│  criteria? Can it be simplified? │
└──────────────────────────────────┘
```

## Domain Mapping

The cycle is universal. The expression varies by domain:

| Domain | "Define" (criteria) | "Plan" (approach) | "Verify" (check) |
|--------|---------------------|-------------------|-------------------|
| **Software engineering** | Write test specifications — unit, integration, e2e | Write implementation to pass all tests | Run tests, review coverage, check edge cases |
| **Design/UX** | Define usability criteria, user outcomes, accessibility standards | Design to meet each criterion | Validate against criteria (heuristic eval, user testing plan) |
| **Business/Strategy** | Define measurable targets — OKRs, KPIs, success metrics | Plan initiatives to move the metrics | Measure against targets, define monitoring |
| **Content** | Define audience takeaways, quality rubric, editorial criteria | Write to achieve each takeaway | Evaluate against rubric |
| **Research** | State hypotheses and falsification criteria | Design investigation to test each hypothesis | Evaluate evidence against criteria |
| **Infrastructure/DevOps** | Define SLOs, SLIs, reliability targets, health checks | Build to meet SLOs | Verify with monitoring, load testing, chaos testing |

See also:
- [Technical TDD planning](technical-tdd.md) — deep dive for code tasks
- [Non-technical acceptance criteria](non-technical-criteria.md) — deep dive for non-code tasks

## Where This Integrates

| Planning Step | How Goal-Driven Methodology Applies |
|---------------|-------------------------------------|
| Step 1 (Clarification) | Questions must uncover success criteria, not just requirements. Ask "how will you know this is done?" for every requirement. |
| Step 3 (Decompose) | Every atomic subtask gets acceptance criteria defined during decomposition — not after. Output is (subtask, criteria) pairs. |
| Step 4 (Generate Plan) | Plan steps are structured criteria-first: acceptance criteria → approach → verification method. Never the reverse. |
| Step 4.5 (Verification) | Agents verify that criteria are well-defined, testable (for code), observable (for non-code), and that the approach would satisfy them. |
| Step 5 (Present) | Criteria are visible in the plan — the user reviews both what will be done AND how success is measured. |

## Acceptance Criteria Quality

Good criteria are:

| Property | Meaning | Example |
|----------|---------|---------|
| **Observable** | Someone can see whether the criterion is met | "API returns 200 with valid JSON" not "API works correctly" |
| **Specific** | No ambiguity about what "done" means | "Response time < 200ms at p95" not "fast enough" |
| **Independent** | Does not rely on subjective judgment | "All 47 existing tests pass" not "nothing is broken" |
| **Complete** | The set of criteria fully defines success | Both happy path AND error cases are covered |

Bad criteria — reject these immediately:
- "It works" — works how? Under what conditions?
- "It's clean" — clean by whose standard? Measured how?
- "It handles errors" — which errors? What does handling look like?
- "Performance is acceptable" — acceptable to whom? Measured how?

## Handling Partial Information

Sometimes the user cannot define all criteria upfront ("I don't know the performance requirements yet"). When this happens:

1. **Mark the criterion as provisional** — use `[PROVISIONAL]` prefix
2. **Define a decision point** — "Before step N begins, performance targets must be defined"
3. **Plan for the range** — "If p95 < 100ms, use approach A. If p95 < 500ms, approach B suffices"
4. **Never leave criteria blank** — a provisional criterion is better than no criterion. Use industry defaults as the provisional value and note the assumption explicitly.

## Rules

1. **Criteria before approach** — for every plan step, at every level of decomposition
2. **No step without criteria** — if you can't define "done," the step is too vague to plan
3. **Criteria drive the approach** — the approach exists to satisfy the criteria, not the reverse
4. **Criteria are non-negotiable** — the approach can change, but criteria only change with explicit user approval
5. **For code tasks, criteria must be expressible as tests** — see [technical TDD](technical-tdd.md)
6. **For non-code tasks, criteria must be observable and verifiable** — see [non-technical criteria](non-technical-criteria.md)
7. **Provisional criteria are acceptable** — but must be flagged and resolved before implementation begins

## Back to

- [Planning process overview](../planning-process/overview.md)
- [Step 3 — Decompose](../planning-process/step-3-decompose.md) — where criteria are first defined
- [Step 4 — Generate Plan](../planning-process/step-4-generate-plan.md) — where criteria drive the plan
