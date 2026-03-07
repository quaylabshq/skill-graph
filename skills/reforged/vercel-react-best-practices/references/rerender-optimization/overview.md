# Re-render Optimization (Priority 5 — MEDIUM)

Unnecessary re-renders waste CPU cycles and degrade UI responsiveness. The goal is to minimize renders without sacrificing code clarity.

## Rules

| Rule | Summary | Reference |
|------|---------|-----------|
| rerender-defer-reads | Don't subscribe to state only used in callbacks | [defer-reads.md](defer-reads.md) |
| rerender-memo | Extract expensive work into memoized components | [memo.md](memo.md) |
| rerender-memo-with-default-value | Hoist default non-primitive props outside components | [memo-default-value.md](memo-default-value.md) |
| rerender-dependencies | Use primitive dependencies in effects | [dependencies.md](dependencies.md) |
| rerender-derived-state | Subscribe to derived booleans, not raw values | [derived-state.md](derived-state.md) |
| rerender-derived-state-no-effect | Derive state during render, not in effects | [derived-state-no-effect.md](derived-state-no-effect.md) |
| rerender-functional-setstate | Use functional setState for stable callbacks | [functional-setstate.md](functional-setstate.md) |
| rerender-lazy-state-init | Pass function to useState for expensive init | [lazy-state-init.md](lazy-state-init.md) |
| rerender-simple-expression-in-memo | Don't wrap simple primitives in useMemo | [simple-expression-memo.md](simple-expression-memo.md) |
| rerender-move-effect-to-event | Put interaction logic in event handlers | [move-effect-to-event.md](move-effect-to-event.md) |
| rerender-transitions | Use `startTransition` for non-urgent updates | [transitions.md](transitions.md) |
| rerender-use-ref-transient-values | Use refs for frequently-changing transient values | [use-ref-transient.md](use-ref-transient.md) |

## Key Principle

**Render less, not faster.** Narrow subscriptions, derive instead of store, defer reads to usage points, and use transitions for non-urgent updates.

## Back to

- [SKILL.md](../../SKILL.md)

## See Also

- [Rendering performance](../rendering-performance/overview.md) — optimizing what happens during a render
