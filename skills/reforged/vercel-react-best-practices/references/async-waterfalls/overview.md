# Eliminating Waterfalls (Priority 1 — CRITICAL)

Sequential async operations are the single biggest performance killer in React/Next.js apps. Every waterfall adds a full round-trip to your loading time.

## Rules

| Rule | Summary | Reference |
|------|---------|-----------|
| async-defer-await | Move `await` into branches where actually needed | [defer-await.md](defer-await.md) |
| async-parallel | Use `Promise.all()` for independent operations | [parallel.md](parallel.md) |
| async-dependencies | Use `better-all` for partial dependencies | [dependencies.md](dependencies.md) |
| async-api-routes | Start promises early, await late in API routes | [api-routes.md](api-routes.md) |
| async-suspense-boundaries | Use Suspense to stream content progressively | [suspense-boundaries.md](suspense-boundaries.md) |

## Key Principle

**Start all independent work as early as possible, await as late as possible.** Three sequential 100ms fetches = 300ms. Three parallel fetches = 100ms.

## Back to

- [SKILL.md](../../SKILL.md)

## See Also

- [Server-side parallel fetching](../server-performance/parallel-fetching.md) — server component composition for parallelism
