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

## Back to

- [Planning process overview](overview.md)
- See also: [Output format — core template](../output-format/core-template.md) — how decomposed tasks map to plan structure
