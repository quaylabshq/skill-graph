# Rule: Use a Loop for Min/Max Instead of Sort

**ID:** js-min-max-loop
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

Finding the minimum or maximum value in an array is an O(n) operation — you only need one pass. Using `.sort()` to find min/max is O(n log n), which is wasteful. `Math.min(...arr)` and `Math.max(...arr)` are O(n) but use the spread operator to pass elements as function arguments, which hits the JavaScript engine's call stack limit at around 124,000 elements in Chrome (varies by engine).

For small arrays (< 10,000 elements), `Math.min(...arr)` is fine. For large or unbounded arrays, use `reduce` or a manual loop.

## Incorrect

```ts
// BAD: O(n log n) sort just to find min/max
function getMinMax(prices: number[]): { min: number; max: number } {
  const sorted = [...prices].sort((a, b) => a - b);
  return {
    min: sorted[0],
    max: sorted[sorted.length - 1],
  };
}

// BAD: stack overflow risk for large arrays
function getMin(values: number[]): number {
  return Math.min(...values); // RangeError for ~124K+ elements in Chrome
}

// BAD: sorting to find the top N when N is small
function getCheapestProduct(products: Product[]): Product {
  const sorted = [...products].sort((a, b) => a.price - b.price);
  return sorted[0]; // sorted 10,000 products just to find 1
}
```

Problem: sorting is O(n log n) and allocates a new array. For 100,000 elements, sort performs ~1.7M comparisons; a single loop performs 100,000. `Math.min(...arr)` crashes for large arrays.

## Correct

```ts
// GOOD: O(n) single pass with reduce
function getMinMax(prices: number[]): { min: number; max: number } {
  if (prices.length === 0) {
    throw new Error("Cannot find min/max of empty array");
  }

  return prices.reduce(
    (acc, price) => ({
      min: price < acc.min ? price : acc.min,
      max: price > acc.max ? price : acc.max,
    }),
    { min: prices[0], max: prices[0] }
  );
}

// GOOD: simple loop — clearest and fastest for large arrays
function getMin(values: number[]): number {
  if (values.length === 0) {
    throw new Error("Cannot find min of empty array");
  }

  let min = values[0];
  for (let i = 1; i < values.length; i++) {
    if (values[i] < min) {
      min = values[i];
    }
  }
  return min;
}

// GOOD: Math.min/max safe for small, bounded arrays
function getSmallArrayMin(values: number[]): number {
  // Safe when you know the array is small (< 10K elements)
  return Math.min(...values);
}

// GOOD: O(n) scan for cheapest product
interface Product {
  id: string;
  name: string;
  price: number;
}

function getCheapestProduct(products: Product[]): Product {
  if (products.length === 0) {
    throw new Error("No products provided");
  }

  let cheapest = products[0];
  for (let i = 1; i < products.length; i++) {
    if (products[i].price < cheapest.price) {
      cheapest = products[i];
    }
  }
  return cheapest;
}
```

Benefit: a loop or `reduce` is O(n), works for any array size, and allocates no intermediate arrays. For 100,000 prices: ~100K operations vs ~1.7M with sort.

## When to Apply

- Finding min, max, or top-1 of any array — always use a loop.
- `Math.min(...arr)` / `Math.max(...arr)` — safe for small, bounded arrays (< 10K). Avoid for user-supplied or unbounded data.
- When you only need the top-K elements (K << N), use a partial selection algorithm or a single pass collecting K candidates, not a full sort.

## Back to

- [overview.md](overview.md)

## See Also

- [tosorted-immutable.md](tosorted-immutable.md) — when you do need to sort, use `.toSorted()` for immutability
- [combine-iterations.md](combine-iterations.md) — combining multiple array operations into one pass
