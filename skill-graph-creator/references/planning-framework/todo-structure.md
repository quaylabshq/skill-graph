# Todo Structure

How to create and manage task lists during skill graph creation.

## Task Granularity

Break tasks to the level where each can be completed in a single focused action:

**Too coarse:**
- "Create all reference files"

**Right level:**
- "Write references/core-principles/overview.md"
- "Write references/core-principles/conciseness.md"
- "Write references/core-principles/degrees-of-freedom.md"

**Too fine:**
- "Write the first paragraph of overview.md"

## Task States

- **Pending** — Not yet started
- **In progress** — Currently being worked on (limit to ONE at a time)
- **Completed** — Finished and verified

## Todo List Template for Skill Graph Creation

A typical skill graph creation produces this todo structure:

1. Ask clarifying questions (step 1)
2. Research domain best practices (step 2)
3. Gather concrete usage examples (step 3)
4. Plan graph structure and file tree (step 4)
5. Initialize skill graph (step 5)
6. Write SKILL.md navigation index
7. Write hub files (one todo per hub)
8. Write detail files (one todo per file)
9. Write scripts (one todo per script)
10. Verify interlinking
11. Run validate_graph.py
12. Package with package_skill.py
13. Test the packaged skill

## Decomposition-Driven Breakdown

Before creating the todo list, apply [recursive decomposition](../core-principles/problem-decomposition.md) to the task:

1. Break the overall task into top-level problems (these become phase headers)
2. Decompose each top-level problem into atomic subproblems (these become actionable tasks)
3. Each atomic subproblem should map to a single todo item
4. Group tasks by decomposition level — maintain the hierarchy in the todo structure

Example:

- **Phase: Authentication references** (top-level problem)
  - Write references/auth/overview.md (atomic)
  - Write references/auth/oauth.md (atomic)
  - Write references/auth/jwt.md (atomic)
  - Verify auth hub links to all detail files (atomic)

This ensures no tasks are forgotten and the todo list directly mirrors the problem structure.

## Rules

1. Create the todo list at the start of the process
2. Apply recursive decomposition before listing tasks
3. Mark tasks complete immediately upon finishing — do not batch
4. Only one task should be "in progress" at any time
5. If a task reveals new work, add new todos rather than expanding the current one
6. Include validation and packaging as explicit todos

## Back to

- [Planning framework overview](overview.md)
