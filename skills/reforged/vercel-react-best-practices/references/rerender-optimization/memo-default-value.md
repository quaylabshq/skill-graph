# Rule: Hoist Default Non-Primitive Props Outside Memoized Components

**ID:** rerender-memo-with-default-value
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

`React.memo()` uses shallow comparison on props. If a parent passes a new object, array, or function reference every render as a default value, memo will always see "changed" props and never bail out. The fix is to hoist these default values to module scope so they maintain stable references across renders.

This applies to any non-primitive default: empty arrays, no-op functions, empty objects, default style objects, etc.

## Incorrect

```tsx
import { memo } from "react";

interface ListProps {
  items?: string[];
  onSelect?: (item: string) => void;
  style?: React.CSSProperties;
}

const FilteredList = memo(function FilteredList({
  items = [],                    // new array reference every render
  onSelect = () => {},           // new function reference every render
  style = { padding: 16 },      // new object reference every render
}: ListProps) {
  return (
    <ul style={style}>
      {items.map((item) => (
        <li key={item} onClick={() => onSelect(item)}>
          {item}
        </li>
      ))}
    </ul>
  );
});

function Parent() {
  const [count, setCount] = useState(0);

  return (
    <>
      <button onClick={() => setCount((c) => c + 1)}>Count: {count}</button>
      {/* memo never bails out — defaults create new references each render */}
      <FilteredList />
    </>
  );
}
```

Problem: even though `FilteredList` is wrapped in `memo`, every render of `Parent` creates new default values for `items`, `onSelect`, and `style`, breaking the shallow comparison.

## Correct

```tsx
import { memo } from "react";

// Stable references — created once at module scope
const EMPTY_ITEMS: string[] = [];
const NOOP = () => {};
const DEFAULT_STYLE: React.CSSProperties = { padding: 16 };

interface ListProps {
  items?: string[];
  onSelect?: (item: string) => void;
  style?: React.CSSProperties;
}

const FilteredList = memo(function FilteredList({
  items = EMPTY_ITEMS,
  onSelect = NOOP,
  style = DEFAULT_STYLE,
}: ListProps) {
  return (
    <ul style={style}>
      {items.map((item) => (
        <li key={item} onClick={() => onSelect(item)}>
          {item}
        </li>
      ))}
    </ul>
  );
});

function Parent() {
  const [count, setCount] = useState(0);

  return (
    <>
      <button onClick={() => setCount((c) => c + 1)}>Count: {count}</button>
      {/* memo correctly bails out — all defaults are stable references */}
      <FilteredList />
    </>
  );
}
```

Benefit: the hoisted constants keep the same reference across renders, so `React.memo()` correctly skips re-rendering when no real props have changed.

## When to Apply

- Any `React.memo()` component that uses default parameter values for objects, arrays, or functions.
- Components that frequently receive `undefined` for optional props and fall back to defaults.
- When React DevTools Profiler shows a memoized component re-rendering without prop changes.

## Back to

- [overview.md](overview.md)

## See Also

- [memo.md](memo.md) — extracting expensive work into memoized components
