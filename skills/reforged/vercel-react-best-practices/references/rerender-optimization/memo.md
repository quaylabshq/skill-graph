# Rule: Extract Expensive Work into Memoized Components

**ID:** rerender-memo
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

When a parent component re-renders frequently (e.g., due to input state), expensive child computations re-execute every time — even if their inputs haven't changed. Extract the expensive work into a separate child component and wrap it with `React.memo()`. This way, the child only re-renders when its own props change, enabling early bailout before the expensive computation runs.

`React.memo()` performs a shallow comparison of props. If all props are the same by reference, the component skips rendering entirely.

## Incorrect

```tsx
import { useState } from "react";

function ProductPage() {
  const [query, setQuery] = useState("");

  // This expensive computation runs on EVERY keystroke
  const recommendations = computeRecommendations(products);

  return (
    <div>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <ul>
        {recommendations.map((item) => (
          <li key={item.id}>{item.name} — ${item.price}</li>
        ))}
      </ul>
    </div>
  );
}
```

Problem: every keystroke in the search input causes `computeRecommendations` to re-run, even though `products` hasn't changed.

## Correct

```tsx
import { useState, memo } from "react";

interface Product {
  id: string;
  name: string;
  price: number;
}

const Recommendations = memo(function Recommendations({
  products,
}: {
  products: Product[];
}) {
  // Only runs when `products` reference changes
  const recommendations = computeRecommendations(products);

  return (
    <ul>
      {recommendations.map((item) => (
        <li key={item.id}>
          {item.name} — ${item.price}
        </li>
      ))}
    </ul>
  );
});

function ProductPage() {
  const [query, setQuery] = useState("");

  return (
    <div>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <Recommendations products={products} />
    </div>
  );
}
```

Benefit: keystrokes only re-render the input. `Recommendations` bails out early because its `products` prop hasn't changed, so the expensive computation is skipped entirely.

## When to Apply

- A component contains expensive computation (sorting, filtering, complex layouts) alongside frequently-changing sibling state.
- A child subtree is visually static but re-renders because its parent updates often.
- Profiling shows a component re-rendering without its props changing.

## Back to

- [overview.md](overview.md)

## See Also

- [memo-default-value.md](memo-default-value.md) — ensure default props don't break memo's shallow comparison
- [simple-expression-memo.md](simple-expression-memo.md) — when NOT to reach for memoization
