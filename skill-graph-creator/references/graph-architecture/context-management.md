# Context Management

The context window is finite. Every reference file loaded reduces space for conversation and reasoning. Plan context usage deliberately.

## Context Budget

Typical budget for a skill graph session:

| Component | Lines | Notes |
|-----------|-------|-------|
| SKILL.md index | ~100 | Always loaded when triggered |
| 1 hub file | ~50 | Loaded for navigation |
| 2-3 detail files | ~150 each | Loaded for specific subtasks |
| **Total** | **~600** | Leaves ample room for conversation |

Loading 5+ detail files simultaneously is a warning sign — restructure to make files more self-contained.

## Delegation Strategy

### Research-Heavy Tasks

Delegate to sub-contexts (separate tool calls, agent spawns) and bring back synthesized findings only:

- Use targeted web searches rather than broad exploration
- Summarize findings before bringing them into the main context
- Discard raw results after synthesis

### Exploration Tasks

Use targeted searches rather than loading entire reference trees:

- Grep for specific patterns rather than reading full files
- Load only the section needed, not the entire reference

### Implementation Tasks

Load only the specific reference files needed for the current subtask:

- Don't pre-load "just in case" references
- Unload (stop referencing) files that are no longer relevant

## Context Branching Rules

**Branch when:**
- Task has 3+ independent research threads
- Exploration scope is uncertain
- Deep-dive needed in one area without polluting main context

**Keep in main context:**
- User preferences and taste decisions
- Architectural decisions
- Cross-cutting constraints
- The current todo list and progress state

## Clean Main Thread

The main conversation context should contain:

| Keep | Discard |
|------|---------|
| User requirements | Raw research results |
| Key decisions made | Exploratory dead-ends |
| Current task state | Intermediate analysis |
| Preferences/taste | Verbose documentation excerpts |

## Back to

- [Graph architecture overview](overview.md)
- See also: [Progressive disclosure](../core-principles/progressive-disclosure.md)
- See also: [One-shot design](../core-principles/one-shot-design.md)
