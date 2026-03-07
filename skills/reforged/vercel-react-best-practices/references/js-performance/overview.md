# JavaScript Performance (Priority 7 — LOW-MEDIUM)

Micro-optimizations for JavaScript execution: DOM batching, data structure choices, caching, and loop efficiency. Apply when profiling reveals JS execution as a bottleneck.

## Rules

| Rule | Summary | Reference |
|------|---------|-----------|
| js-batch-dom-css | Group CSS changes via classes or cssText | [batch-dom-css.md](batch-dom-css.md) |
| js-index-maps | Build Map for repeated lookups | [index-maps.md](index-maps.md) |
| js-cache-property-access | Cache object properties in loops | [cache-property-access.md](cache-property-access.md) |
| js-cache-function-results | Cache function results in module-level Map | [cache-function-results.md](cache-function-results.md) |
| js-cache-storage | Cache localStorage/sessionStorage reads | [cache-storage.md](cache-storage.md) |
| js-combine-iterations | Combine multiple filter/map into one loop | [combine-iterations.md](combine-iterations.md) |
| js-length-check-first | Check array length before expensive comparison | [length-check-first.md](length-check-first.md) |
| js-early-exit | Return early from functions | [early-exit.md](early-exit.md) |
| js-hoist-regexp | Hoist RegExp creation outside loops | [hoist-regexp.md](hoist-regexp.md) |
| js-min-max-loop | Use loop for min/max instead of sort | [min-max-loop.md](min-max-loop.md) |
| js-set-map-lookups | Use Set/Map for O(1) lookups | [set-map-lookups.md](set-map-lookups.md) |
| js-tosorted-immutable | Use `toSorted()` for immutable sorting | [tosorted-immutable.md](tosorted-immutable.md) |

## Key Principle

**Choose the right data structure and avoid redundant work.** Set for membership, Map for lookups, cache repeated computations, batch DOM writes, and exit early.

## Back to

- [SKILL.md](../../SKILL.md)

## See Also

- [Re-render optimization](../rerender-optimization/overview.md) — reducing renders at the React level
