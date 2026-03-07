# Problem Decomposition

Every problem must be broken into smaller, independent subproblems before solving. This applies at every level — requirements, design, implementation, testing.

## The Recursive Test

For every problem, ask: "Can this be broken into 2+ independent subproblems?"

- If yes → decompose and repeat the test on each subproblem
- If no → the problem is atomic; solve it directly

Continue until each subproblem is atomic.

## Atomic Subproblem Criteria

A subproblem is atomic when:

- It can be solved without referencing other subproblems
- It has clear input and output
- It can be verified independently
- Further splitting would produce fragments too small to be meaningful (<20 lines as a reference file)

## Applied to Skill Graphs

| Level | Decomposition | Graph Mapping |
|-------|---------------|---------------|
| Requirements | Break into independent feature areas | Each area becomes a reference file |
| Design | Break into independent decisions | Each decision can be asked about separately |
| Implementation | Break into independent files | Each file can be written and tested alone |
| Testing | Break into independent checks | Each check has its own success criteria |

## Graph Representation

- Subproblems become graph nodes (reference files)
- Dependencies between subproblems become links
- Independent subproblems can be worked in parallel
- The decomposition tree maps directly to the hub-and-spoke architecture

## Complexity Assessment Heuristic

Count the depth of decomposition:

| Depth | Complexity | Implication |
|-------|------------|-------------|
| 1-2 levels | Simple | Flat references, single hub |
| 3-4 levels | Moderate | Sub-hubs needed, more reference files |
| 5+ levels | Complex | Consider additional reference layers, aggressive sub-categorization |

## Anti-Patterns

- **Solving without decomposing**: Jumping to implementation on a complex problem
- **Over-decomposing**: Splitting until files are trivially small (<20 lines)
- **Coupled decomposition**: Splitting things that are tightly interdependent
- **Premature decomposition**: Splitting before understanding the full scope

## Back to

- [Core principles overview](overview.md)
- See also: [Graph decomposition strategies](../graph-architecture/decomposition.md)
