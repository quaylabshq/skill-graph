# Rule: Cache Function Results in a Module-Level Map

**ID:** js-cache-function-results
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

When a pure function is called repeatedly with the same arguments — for example, `slugify()` called for the same product names across re-renders — you pay the full computation cost every time. A module-level `Map` acts as a simple memoization cache: check if the result exists, return it immediately if so, otherwise compute, store, and return.

This pattern is lighter than `useMemo` (which is scoped to a single component instance) and persists across the entire module lifetime. It works best for pure functions with string or number keys.

## Incorrect

```ts
// BAD: slugify recomputes on every call, even for repeated inputs
function slugify(text: string): string {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

// Called in a list component — same product names slugified every render
function ProductList({ products }: { products: Product[] }) {
  return (
    <ul>
      {products.map((p) => (
        <li key={p.id}>
          <a href={`/products/${slugify(p.name)}`}>{p.name}</a>
        </li>
      ))}
    </ul>
  );
}
```

Problem: if the list has 200 products and re-renders 10 times, `slugify` runs 2,000 times — but the product names haven't changed, so most calls are redundant.

## Correct

```ts
// GOOD: module-level cache for repeated slugify calls
const slugCache = new Map<string, string>();

function slugify(text: string): string {
  const cached = slugCache.get(text);
  if (cached !== undefined) {
    return cached;
  }

  const slug = text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_]+/g, "-")
    .replace(/^-+|-+$/g, "");

  slugCache.set(text, slug);
  return slug;
}

// Now 200 products × 10 re-renders = 200 computations + 1,800 cache hits
function ProductList({ products }: { products: Product[] }) {
  return (
    <ul>
      {products.map((p) => (
        <li key={p.id}>
          <a href={`/products/${slugify(p.name)}`}>{p.name}</a>
        </li>
      ))}
    </ul>
  );
}
```

Benefit: each unique input is computed only once. Subsequent calls with the same input return instantly from the Map (O(1) lookup).

### Bounded cache for dynamic inputs

If inputs are unbounded (e.g., user-generated text), cap the cache size to avoid memory leaks:

```ts
const MAX_CACHE_SIZE = 1000;
const slugCache = new Map<string, string>();

function slugify(text: string): string {
  const cached = slugCache.get(text);
  if (cached !== undefined) {
    return cached;
  }

  const slug = text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_]+/g, "-")
    .replace(/^-+|-+$/g, "");

  if (slugCache.size >= MAX_CACHE_SIZE) {
    // Evict oldest entry (Map preserves insertion order)
    const firstKey = slugCache.keys().next().value;
    slugCache.delete(firstKey!);
  }

  slugCache.set(text, slug);
  return slug;
}
```

## When to Apply

- Pure functions called with the same arguments across renders (slugify, formatDate, hash).
- Expensive string transformations or calculations in list renderers.
- Any function where the computation cost exceeds the Map lookup cost and inputs repeat.

## Back to

- [overview.md](overview.md)

## See Also

- [cache-property-access.md](cache-property-access.md) — caching object property reads in loops
- [cache-storage.md](cache-storage.md) — caching browser storage reads
