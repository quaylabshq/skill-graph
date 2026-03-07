# Rule: Don't Wrap Simple Primitive Expressions in useMemo

**ID:** rerender-simple-expression-in-memo
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

`useMemo` itself has overhead: React must store the previous result, compare dependencies, and manage the cache entry. When the expression being memoized is a simple arithmetic operation, string concatenation, or boolean check that produces a primitive result, the `useMemo` overhead exceeds the cost of just recomputing the value. Reserve `useMemo` for genuinely expensive computations (filtering large arrays, complex calculations) or for maintaining referential identity of objects/arrays passed to memoized children.

## Incorrect

```tsx
import { useMemo } from "react";

function PriceDisplay({ price, taxRate }: { price: number; taxRate: number }) {
  // useMemo overhead exceeds the cost of a single multiplication
  const totalPrice = useMemo(
    () => price * (1 + taxRate),
    [price, taxRate]
  );

  // useMemo for simple addition
  const sum = useMemo(() => a + b, [a, b]);

  // useMemo for a boolean check
  const isExpensive = useMemo(() => price > 100, [price]);

  // useMemo for string concatenation
  const fullName = useMemo(
    () => `${firstName} ${lastName}`,
    [firstName, lastName]
  );

  return (
    <div>
      <p>Total: ${totalPrice.toFixed(2)}</p>
      <p>{isExpensive ? "Premium item" : "Regular item"}</p>
      <p>Buyer: {fullName}</p>
    </div>
  );
}
```

Problem: each `useMemo` adds memory allocation, dependency comparison, and cache management overhead that far exceeds the nanosecond cost of `price * (1 + taxRate)` or `a + b`.

## Correct

```tsx
function PriceDisplay({ price, taxRate }: { price: number; taxRate: number }) {
  // Simple expressions — just compute directly
  const totalPrice = price * (1 + taxRate);
  const sum = a + b;
  const isExpensive = price > 100;
  const fullName = `${firstName} ${lastName}`;

  return (
    <div>
      <p>Total: ${totalPrice.toFixed(2)}</p>
      <p>{isExpensive ? "Premium item" : "Regular item"}</p>
      <p>Buyer: {fullName}</p>
    </div>
  );
}
```

Benefit: cleaner code, fewer allocations, no dependency array bookkeeping. The raw computation is faster than the `useMemo` machinery.

## When useMemo IS Appropriate

```tsx
function ProductList({ products, query }: { products: Product[]; query: string }) {
  // Filtering thousands of items — useMemo is justified
  const filteredProducts = useMemo(
    () =>
      products.filter(
        (p) =>
          p.name.toLowerCase().includes(query.toLowerCase()) ||
          p.description.toLowerCase().includes(query.toLowerCase())
      ),
    [products, query]
  );

  // Object needed as stable reference for memo'd child
  const chartConfig = useMemo(
    () => ({ series: filteredProducts.map((p) => p.price), color: "blue" }),
    [filteredProducts]
  );

  return (
    <div>
      <MemoizedChart config={chartConfig} />
      {filteredProducts.map((p) => (
        <ProductCard key={p.id} product={p} />
      ))}
    </div>
  );
}
```

## Rule of Thumb

- **Primitive result from simple expression** (arithmetic, comparison, concatenation) -- skip `useMemo`.
- **Iterating over collections** (filter, map, sort, reduce) -- consider `useMemo`.
- **Object/array reference** passed to a `React.memo()` child -- use `useMemo` for referential stability.

## Back to

- [overview.md](overview.md)

## See Also

- [derived-state-no-effect.md](derived-state-no-effect.md) — derive values during render instead of storing in state
- [memo.md](memo.md) — when to use `React.memo()` on components
