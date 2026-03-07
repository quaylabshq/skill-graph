# Server-Side Performance (Priority 3 — HIGH)

Server Components and Server Actions introduce new performance considerations: serialization costs, per-request deduplication, cross-request caching, and authentication.

## Rules

| Rule | Summary | Reference |
|------|---------|-----------|
| server-auth-actions | Authenticate server actions like API routes | [auth-actions.md](auth-actions.md) |
| server-cache-react | `React.cache()` for per-request deduplication | [cache-react.md](cache-react.md) |
| server-cache-lru | LRU cache for cross-request caching | [cache-lru.md](cache-lru.md) |
| server-dedup-props | Avoid duplicate serialization in RSC props | [dedup-props.md](dedup-props.md) |
| server-hoist-static-io | Hoist static I/O (fonts, logos) to module level | [hoist-static-io.md](hoist-static-io.md) |
| server-serialization | Minimize data passed to client components | [serialization.md](serialization.md) |
| server-parallel-fetching | Restructure components to parallelize fetches | [parallel-fetching.md](parallel-fetching.md) |
| server-after-nonblocking | Use `after()` for non-blocking operations | [after-nonblocking.md](after-nonblocking.md) |

## Key Principle

**Treat the server/client boundary as an API.** Minimize what crosses it, deduplicate within requests, cache across requests, and always authenticate server actions.

## Back to

- [SKILL.md](../../SKILL.md)

## See Also

- [Eliminating waterfalls](../async-waterfalls/overview.md) — async patterns that apply on the server too
