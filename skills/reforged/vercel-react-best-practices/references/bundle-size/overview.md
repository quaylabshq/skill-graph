# Bundle Size Optimization (Priority 2 — CRITICAL)

Every kilobyte of JavaScript must be parsed, compiled, and executed before the page is interactive. Reducing bundle size directly improves Time to Interactive.

## Rules

| Rule | Summary | Reference |
|------|---------|-----------|
| bundle-barrel-imports | Import directly from source, avoid barrel files | [barrel-imports.md](barrel-imports.md) |
| bundle-dynamic-imports | Use `next/dynamic` for heavy components | [dynamic-imports.md](dynamic-imports.md) |
| bundle-defer-third-party | Load analytics/logging after hydration | [defer-third-party.md](defer-third-party.md) |
| bundle-conditional | Load modules only when feature is activated | [conditional.md](conditional.md) |
| bundle-preload | Preload on hover/focus for perceived speed | [preload.md](preload.md) |

## Key Principle

**Only ship JavaScript the user needs right now.** Defer everything else — dynamic imports for heavy components, conditional loading for feature-flagged code, preloading on intent signals.

## Back to

- [SKILL.md](../../SKILL.md)

## See Also

- [Server serialization](../server-performance/serialization.md) — minimize data crossing the RSC boundary
