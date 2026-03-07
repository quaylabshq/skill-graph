# Rule: Use startTransition for Non-Urgent Updates

**ID:** rerender-transitions
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

When a single user action triggers both an urgent update (e.g., updating an input value) and a non-urgent update (e.g., filtering a large list), wrap the non-urgent update in `startTransition`. React will prioritize the urgent update so the UI stays responsive, and render the transition update in the background when ready. If a new transition starts before the previous one finishes, React abandons the stale render — no wasted work.

This is critical for search-as-you-type, tab switching with heavy content, and any pattern where typing or clicking must stay snappy while expensive derived UI catches up.

## Incorrect

```tsx
import { useState } from "react";

interface Product {
  id: string;
  name: string;
  description: string;
  category: string;
}

function ProductSearch({ products }: { products: Product[] }) {
  const [query, setQuery] = useState("");
  const [filteredProducts, setFilteredProducts] = useState(products);

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    const value = e.target.value;
    setQuery(value);

    // Both updates have the same priority — expensive filter blocks input
    setFilteredProducts(
      products.filter(
        (p) =>
          p.name.toLowerCase().includes(value.toLowerCase()) ||
          p.description.toLowerCase().includes(value.toLowerCase()) ||
          p.category.toLowerCase().includes(value.toLowerCase())
      )
    );
  }

  return (
    <div>
      <input value={query} onChange={handleChange} placeholder="Search..." />
      <p>{filteredProducts.length} results</p>
      {filteredProducts.map((p) => (
        <ProductCard key={p.id} product={p} />
      ))}
    </div>
  );
}
```

Problem: with 10,000 products, the filter + re-render of the list blocks the input. Typing feels laggy because React treats both state updates with the same priority and renders them together.

## Correct

```tsx
import { useState, useTransition } from "react";

interface Product {
  id: string;
  name: string;
  description: string;
  category: string;
}

function ProductSearch({ products }: { products: Product[] }) {
  const [query, setQuery] = useState("");
  const [filteredProducts, setFilteredProducts] = useState(products);
  const [isPending, startTransition] = useTransition();

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    const value = e.target.value;

    // Urgent: input value updates immediately
    setQuery(value);

    // Non-urgent: list update can be deferred
    startTransition(() => {
      setFilteredProducts(
        products.filter(
          (p) =>
            p.name.toLowerCase().includes(value.toLowerCase()) ||
            p.description.toLowerCase().includes(value.toLowerCase()) ||
            p.category.toLowerCase().includes(value.toLowerCase())
        )
      );
    });
  }

  return (
    <div>
      <input value={query} onChange={handleChange} placeholder="Search..." />
      <p>
        {filteredProducts.length} results
        {isPending && <span> (updating...)</span>}
      </p>
      {filteredProducts.map((p) => (
        <ProductCard key={p.id} product={p} />
      ))}
    </div>
  );
}
```

Benefit: the input responds instantly to every keystroke. The filtered list updates when React has idle time. If the user types faster than React can filter, intermediate renders are abandoned — React only completes the render for the final query value.

## When to Apply

- Search-as-you-type with large result sets.
- Tab navigation where each tab renders heavy content.
- Any UI where a user interaction triggers both a quick feedback update and an expensive derived update.
- Router navigations in React 18+ (Next.js uses transitions for `router.push` internally).

## When NOT to Apply

- Updates that must be synchronous for accessibility (focus management, ARIA live regions).
- Animations that rely on immediate state changes.
- State updates that are already fast (small lists, simple components).

## Back to

- [overview.md](overview.md)

## See Also

- [derived-state.md](derived-state.md) — narrowing subscriptions to reduce renders in the first place
