# Rule: Pass a Function to useState for Expensive Initialization

**ID:** rerender-lazy-state-init
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

`useState(initialValue)` evaluates `initialValue` on every render, but only uses it on the first render. If computing the initial value is expensive (parsing JSON, reading localStorage, complex calculations), the cost is paid on every re-render for nothing. Passing a function — `useState(() => expensiveComputation())` — ensures the computation only runs once, on the initial render. React calls the initializer function lazily, only when the state is first created.

## Incorrect

```tsx
import { useState } from "react";

interface UserPreferences {
  theme: "light" | "dark";
  fontSize: number;
  language: string;
}

function SettingsPanel() {
  // JSON.parse runs on EVERY render — expensive and wasteful
  const [preferences, setPreferences] = useState<UserPreferences>(
    JSON.parse(localStorage.getItem("preferences") || "{}")
  );

  // buildInitialGrid() runs on EVERY render
  const [grid, setGrid] = useState<number[][]>(
    buildInitialGrid(50, 50) // creates a 50x50 matrix
  );

  // new Date() is cheap, but the sort and filter chain is not
  const [sortedItems, setSortedItems] = useState<Item[]>(
    rawItems
      .filter((item) => item.isActive)
      .sort((a, b) => a.priority - b.priority)
      .slice(0, 100)
  );

  return <div>{/* ... */}</div>;
}
```

Problem: `JSON.parse`, `buildInitialGrid`, and the filter/sort chain all execute on every render, even though their results are only needed once as the initial state.

## Correct

```tsx
import { useState } from "react";

interface UserPreferences {
  theme: "light" | "dark";
  fontSize: number;
  language: string;
}

function SettingsPanel() {
  // Lazy initializer — JSON.parse only runs on the first render
  const [preferences, setPreferences] = useState<UserPreferences>(
    () => JSON.parse(localStorage.getItem("preferences") || "{}")
  );

  // Lazy initializer — grid is built once
  const [grid, setGrid] = useState<number[][]>(
    () => buildInitialGrid(50, 50)
  );

  // Lazy initializer — sort and filter run once
  const [sortedItems, setSortedItems] = useState<Item[]>(() =>
    rawItems
      .filter((item) => item.isActive)
      .sort((a, b) => a.priority - b.priority)
      .slice(0, 100)
  );

  return <div>{/* ... */}</div>;
}
```

Benefit: each expensive computation runs exactly once. Subsequent re-renders skip the initializer entirely because React already has the state value.

## When to Apply

- `useState` with `JSON.parse()`, `localStorage.getItem()`, or `sessionStorage` reads.
- `useState` with array operations: `.filter()`, `.sort()`, `.map()`, `.reduce()`.
- `useState` that constructs large data structures (matrices, trees, graphs).
- Any `useState` where the initial value expression is more than a trivial literal or variable reference.

**Note:** For primitives and simple references (`useState(0)`, `useState("")`, `useState(props.initialValue)`), the overhead of wrapping in a function is not worthwhile.

## Back to

- [overview.md](overview.md)
