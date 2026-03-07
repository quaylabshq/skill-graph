# Client-Side Data Fetching (Priority 4 — MEDIUM-HIGH)

Client-side fetching needs deduplication, caching, and efficient event handling to avoid redundant network requests and memory leaks.

## Rules

| Rule | Summary | Reference |
|------|---------|-----------|
| client-swr-dedup | Use SWR for automatic request deduplication | [swr-dedup.md](swr-dedup.md) |
| client-event-listeners | Deduplicate global event listeners | [event-listeners.md](event-listeners.md) |
| client-passive-event-listeners | Use passive listeners for scroll/touch | [passive-event-listeners.md](passive-event-listeners.md) |
| client-localstorage-schema | Version and minimize localStorage data | [localstorage-schema.md](localstorage-schema.md) |

## Key Principle

**Share and deduplicate.** Multiple components requesting the same data should share one request. Multiple instances needing the same event should share one listener.

## Back to

- [SKILL.md](../../SKILL.md)

## See Also

- [Server caching](../server-performance/cache-react.md) — server-side deduplication with `React.cache()`
