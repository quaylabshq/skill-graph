# Rule: Combine Multiple filter/map Chains into One Loop

**ID:** js-combine-iterations
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

Chaining `.filter().filter().map()` creates a new intermediate array at each step and iterates the data multiple times. For an array of N items with two filters and a map, that's 3 full passes and 2 throwaway arrays. Combining the logic into a single `for...of` loop processes every element once, creates one output array, and avoids all intermediate allocations.

This matters most for large datasets (1,000+ items) or hot render paths where the chain runs on every re-render.

## Incorrect

```ts
interface Item {
  id: string;
  name: string;
  active: boolean;
  score: number;
  category: string;
}

// BAD: 3 passes over the data, 2 intermediate arrays
function getTopActiveNames(items: Item[]): string[] {
  return items
    .filter((item) => item.active)          // Pass 1 → intermediate array 1
    .filter((item) => item.score > 50)      // Pass 2 → intermediate array 2
    .map((item) => item.name);              // Pass 3 → final array
}

// With 10,000 items: up to 30,000 iterations + 2 garbage arrays
```

Problem: each method in the chain allocates a new array and iterates over all surviving elements. The intermediate arrays are immediately discarded, creating GC pressure.

## Correct

```ts
interface Item {
  id: string;
  name: string;
  active: boolean;
  score: number;
  category: string;
}

// GOOD: single pass, one output array, no intermediates
function getTopActiveNames(items: Item[]): string[] {
  const results: string[] = [];

  for (const item of items) {
    if (item.active && item.score > 50) {
      results.push(item.name);
    }
  }

  return results;
}

// With 10,000 items: exactly 10,000 iterations, 1 array allocated
```

Benefit: one pass through the data, one array allocation, combined condition check. For 10,000 items, this reduces iterations from up to 30,000 to exactly 10,000 and eliminates garbage collection pressure from intermediate arrays.

### More complex example with transformation

```ts
interface Order {
  id: string;
  status: "pending" | "shipped" | "delivered" | "cancelled";
  total: number;
  items: { name: string; qty: number }[];
}

interface OrderSummary {
  id: string;
  total: number;
  itemCount: number;
}

// BAD: 3 chained operations
const summaries = orders
  .filter((o) => o.status !== "cancelled")
  .filter((o) => o.total > 100)
  .map((o) => ({
    id: o.id,
    total: o.total,
    itemCount: o.items.reduce((sum, i) => sum + i.qty, 0),
  }));

// GOOD: single loop
const summaries: OrderSummary[] = [];
for (const o of orders) {
  if (o.status !== "cancelled" && o.total > 100) {
    summaries.push({
      id: o.id,
      total: o.total,
      itemCount: o.items.reduce((sum, i) => sum + i.qty, 0),
    });
  }
}
```

## When to Apply

- Three or more chained array methods (`.filter().filter().map()`, `.map().filter().reduce()`).
- Arrays with 1,000+ elements in render-path code.
- When profiling shows GC pauses from intermediate array allocations.
- Note: for short arrays (< 100 items) in non-hot paths, chaining is fine for readability.

## Back to

- [overview.md](overview.md)

## See Also

- [index-maps.md](index-maps.md) — replacing nested `.find()` with Map lookups
- [early-exit.md](early-exit.md) — skipping unnecessary work early
