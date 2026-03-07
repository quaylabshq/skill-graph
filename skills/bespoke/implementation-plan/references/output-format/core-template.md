# Core Template

Every implementation plan includes these sections. This is the fixed structure that provides consistency across all plan types.

## Template

```markdown
## Summary

[1-3 sentences: what the task achieves and the high-level approach]

## Approach

[Key decisions and rationale. Why this approach over alternatives.
Include constraints that shaped the decision.]

## Implementation Steps

[Ordered list of steps. Each step is an atomic subtask from decomposition.]

1. **[Step name]** — [What to do] `[complexity: straightforward|investigation|high-risk]`
   - Files: [files affected]
   - Depends on: [step dependencies, if any]

2. **[Step name]** — [What to do] `[complexity]`
   ...

## Files Affected

[For codebase tasks. List files with the nature of change.]

| File | Change Type | Purpose |
|------|-------------|---------|
| path/to/file.ts | Modify | Add new handler for X |
| path/to/new-file.ts | Create | New module for Y |
| path/to/test.ts | Modify | Add tests for new behavior |
```

## Section Guidelines

### Summary
- 1-3 sentences maximum
- State what gets built/changed and the approach
- Do not restate the user's request — add value

### Approach
- Explain WHY this approach, not just WHAT
- Mention alternatives considered and why they were rejected
- Note constraints that shaped the decision

### Implementation Steps
- Each step maps to one atomic subtask from decomposition
- Order by dependency — prerequisites first
- Mark each with complexity signal
- Include file references for codebase tasks
- Note dependencies between steps explicitly

### Files Affected
- Only for codebase tasks
- Include change type (Create, Modify, Delete)
- State the purpose of each change

## Lightweight Plan (Simple Tasks)

For simple tasks, use only Summary + Steps:

```markdown
## Summary
[1 sentence approach]

## Steps
1. [Step]
2. [Step]
3. [Step]
```

## Back to

- [Output format overview](overview.md)
- See also: [Adaptive sections](adaptive-sections.md)
