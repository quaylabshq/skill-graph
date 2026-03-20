# Step 3: Decompose

Break the task into smaller, independent subtasks before generating the plan. This applies to every task regardless of domain — software features, design projects, research initiatives.

## The Recursive Test

For every task, ask: "Can this be broken into 2+ independent subtasks?"

- If yes → decompose and repeat the test on each subtask
- If no → the subtask is atomic; it goes into the plan as a single step

Continue until each subtask is atomic.

## Atomic Subtask Criteria

A subtask is atomic when:

- It can be completed without referencing other subtasks
- It has clear input and output
- It can be verified independently
- Further splitting would produce fragments too small to be actionable

## Criteria-First Decomposition

When a subtask is determined to be atomic, **immediately define its acceptance criteria** — BEFORE recording it as a plan step. The decomposition output is not a list of tasks. It is a list of (task, criteria) pairs.

This is the [goal-driven methodology](../goal-driven-methodology/overview.md) applied at the decomposition level. The "test" is defined before the "code."

### Process

For each atomic subtask:

1. Ask: "What must be true when this subtask is done?"
2. Write 2-5 specific, observable acceptance criteria
3. For code tasks: express criteria as test specifications (see [technical TDD](../goal-driven-methodology/technical-tdd.md))
4. For non-code tasks: express criteria using domain-appropriate frameworks (see [non-technical criteria](../goal-driven-methodology/non-technical-criteria.md))
5. Only THEN record the subtask with its criteria

If you cannot define clear criteria for a subtask, the subtask is too vague — either decompose further or return to [clarification](step-1-clarification.md).

### Decomposition Output Format

```
Subtask: [name]
Criteria:
  - [criterion 1 — observable, specific]
  - [criterion 2]
  - [criterion 3]
Dependencies: [other subtasks this depends on]
```

This output feeds directly into [Step 4 (Generate Plan)](step-4-generate-plan.md), where each subtask becomes a plan step with its criteria already defined.

## Scope Creep Detection

During decomposition, actively monitor for scope expansion:

1. **Count subtasks** — if decomposition produces more than 15 atomic subtasks for a task classified as "moderate," pause and question whether scope has expanded
2. **Check origins** — every subtask must trace back to a user requirement or research finding. If a subtask exists "because it would be nice," it is scope creep
3. **Compare to clarification** — review the scope boundaries agreed in Step 1. Does the decomposition stay within them?
4. **Flag and ask** — if scope expansion is detected, do not silently include it. Surface it to the user: "During decomposition, I identified [X] which wasn't in the original scope. Should I include it?"

## Complexity Assessment

Count the depth of decomposition:

| Depth | Complexity | Plan Implication |
|-------|------------|------------------|
| 1 level | Simple | Flat step list, lightweight plan |
| 2 levels | Moderate | Grouped steps with phases, standard plan |
| 3+ levels | Complex | Phased plan with dependencies, detailed plan |

## Dependency Identification

After decomposing, map dependencies between subtasks:

1. Which subtasks must complete before others can start?
2. Which subtasks are truly independent and can be done in any order?
3. Which subtasks share resources or state?

Express dependencies as: "Task B depends on Task A" — this drives the ordering in the plan.

## Domain-Specific Decomposition

| Domain | Natural Decomposition |
|--------|-----------------------|
| Software feature | By component/layer (API, DB, UI, tests) |
| Bug fix | By investigation, root cause, fix, verification |
| Refactor | By extract, transform, verify phases |
| Design | By research, wireframe, prototype, polish |
| Content | By outline, draft, review, publish |
| Research | By question, sources, analysis, synthesis |

## Rules

1. Decompose BEFORE generating the plan structure
2. The decomposition drives the plan's step organization
3. If decomposition reveals unclear requirements, return to [step 1](step-1-clarification.md)
4. Do not over-decompose — stop when subtasks are actionable single steps
5. **Every atomic subtask must have acceptance criteria** — no subtask is recorded without them
6. **Monitor for scope creep** — every subtask must trace to a requirement or research finding

## Back to

- [Planning process overview](overview.md)
- See also: [Goal-driven methodology](../goal-driven-methodology/overview.md) — criteria-first planning
- See also: [Output format — core template](../output-format/core-template.md) — how decomposed tasks map to plan structure
