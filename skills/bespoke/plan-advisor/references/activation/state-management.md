# State Management

Activation state is persisted in the project memory directory so it survives across conversations.

## State File

- **Path**: `/Users/saket/.claude/projects/-Users-saket-Documents-GitHub-skills-graph-cretor/memory/plan-advisor-state.md`
- **Format**: Simple markdown with YAML-style key-value pairs

## State File Format

```markdown
# Plan Advisor State

- active: true
- activated-at: 2026-03-06T10:00:00
- plan-file: /path/to/current/plan.md
- last-assessment: 2026-03-06T10:01:00
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `active` | boolean | Whether plan-advisor is currently enabled |
| `activated-at` | ISO timestamp | When it was last activated |
| `plan-file` | path or empty | Path to the plan currently being advised on |
| `last-assessment` | ISO timestamp or empty | When the plan was last evaluated |

## Lifecycle

1. **On activation**: Create or update state file with `active: true` and current timestamp
2. **On plan assessment**: Update `plan-file` and `last-assessment` fields
3. **On deactivation**: Set `active: false`, clear `plan-file` and `last-assessment`
4. **On new conversation**: Read state file to check if advisor is active; if active, resume advising

## State Checks

- Before answering any question, verify `active: true` in the state file
- If state file is missing, treat as inactive
- If state file exists but `active: false`, treat as inactive

## Back to

- [Activation overview](overview.md)
- See also: [Activation workflow](../workflows/activation-workflow.md) — full activation sequence
