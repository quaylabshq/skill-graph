# Activation Overview

Plan-advisor is manually activated and maintains persistent state across conversations. It does not activate automatically — the user must explicitly invoke it.

## Key Concepts

| Concept | Description |
|---------|-------------|
| Manual invocation | Activation only via explicit trigger phrases |
| Persistent state | Active/inactive state stored in project memory directory |
| Session lifecycle | Activation persists until explicitly deactivated |

## References

| Topic | Reference |
|-------|-----------|
| Trigger phrases & detection rules | [invocation-detection.md](invocation-detection.md) |
| State file format & lifecycle | [state-management.md](state-management.md) |

## See Also

- [Activation workflow](../workflows/activation-workflow.md) — step-by-step activation sequence
- [Assessment overview](../assessment/overview.md) — what happens after activation
