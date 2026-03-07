# Advanced Patterns (Priority 8 — LOW)

Patterns for edge cases: stable callback refs, one-time initialization, and latest-value patterns. Use when simpler approaches from higher-priority categories don't suffice.

## Rules

| Rule | Summary | Reference |
|------|---------|-----------|
| advanced-event-handler-refs | Store event handlers in refs for stable subscriptions | [event-handler-refs.md](event-handler-refs.md) |
| advanced-init-once | Initialize app once per load, not per mount | [init-once.md](init-once.md) |
| advanced-use-latest | `useEffectEvent` for stable callback refs | [use-latest.md](use-latest.md) |

## Key Principle

**Use refs to escape the render cycle when needed.** Store handlers in refs to prevent effect re-subscriptions, guard initialization with module-level flags, and use `useEffectEvent` for latest-value access.

## Back to

- [SKILL.md](../../SKILL.md)

## See Also

- [Re-render optimization](../rerender-optimization/overview.md) — standard approaches before reaching for advanced patterns
