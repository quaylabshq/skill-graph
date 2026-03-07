# Rule: Use Functional setState for Stable Callbacks

**ID:** rerender-functional-setstate
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

When updating state based on its previous value, use the functional form `setState(prev => ...)` instead of referencing the state variable directly. The direct form captures the state value at the time the callback was created, leading to stale closures if the callback isn't recreated on every render. The functional form always receives the latest state as its argument, eliminating stale closure bugs and enabling stable callback references via `useCallback` with an empty dependency array.

## Incorrect

```tsx
import { useState, useCallback } from "react";

interface Item {
  id: string;
  name: string;
}

function ItemList() {
  const [items, setItems] = useState<Item[]>([]);

  // `items` is captured in the closure — stale if items change
  // Must include `items` in useCallback deps, breaking memoization
  const addItems = useCallback(
    (newItems: Item[]) => {
      setItems([...items, ...newItems]);
    },
    [items] // callback recreated every time items changes
  );

  const removeItem = useCallback(
    (id: string) => {
      setItems(items.filter((item) => item.id !== id));
    },
    [items] // same problem — new function reference on every change
  );

  return (
    <div>
      <MemoizedToolbar onAdd={addItems} onRemove={removeItem} />
      {items.map((item) => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  );
}
```

Problem: `addItems` and `removeItem` get new references every time `items` changes, which breaks `React.memo()` on `MemoizedToolbar` and causes it to re-render unnecessarily.

## Correct

```tsx
import { useState, useCallback } from "react";

interface Item {
  id: string;
  name: string;
}

function ItemList() {
  const [items, setItems] = useState<Item[]>([]);

  // Functional update — no dependency on `items`
  const addItems = useCallback((newItems: Item[]) => {
    setItems((curr) => [...curr, ...newItems]);
  }, []); // stable reference — never changes

  const removeItem = useCallback((id: string) => {
    setItems((curr) => curr.filter((item) => item.id !== id));
  }, []); // stable reference — never changes

  return (
    <div>
      <MemoizedToolbar onAdd={addItems} onRemove={removeItem} />
      {items.map((item) => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  );
}
```

Benefit: `addItems` and `removeItem` have stable references (empty dependency array), so `MemoizedToolbar` never re-renders due to callback changes. The functional updater always receives the latest state, eliminating stale closures.

## When to Apply

- Any `setState` call that depends on the current state value: appending to arrays, toggling booleans, incrementing counters, removing items.
- Callbacks passed to memoized children — functional updates allow an empty `useCallback` dependency array.
- Async operations (fetch callbacks, timers) where state may have changed between the start of the operation and the callback execution.

## Back to

- [overview.md](overview.md)

## See Also

- [memo.md](memo.md) — memoized components benefit most from stable callback props
