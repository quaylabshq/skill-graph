# Rule: Derive State During Render, Not in Effects

**ID:** rerender-derived-state-no-effect
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

If a value can be computed purely from existing props or state, calculate it directly during render. Do not store it in a separate `useState` and synchronize it with `useEffect` — this causes an unnecessary extra render cycle: the first render uses stale state, the effect fires, state updates, and the component renders again with the correct value.

Derived values are not state. They are computations.

## Incorrect

```tsx
import { useState, useEffect } from "react";

interface UserFormProps {
  firstName: string;
  lastName: string;
}

function UserForm({ firstName, lastName }: UserFormProps) {
  const [fullName, setFullName] = useState("");

  // Unnecessary effect — causes a second render every time names change
  useEffect(() => {
    setFullName(firstName + " " + lastName);
  }, [firstName, lastName]);

  return <p>Welcome, {fullName}</p>;
}

function CartSummary({ items }: { items: { price: number; qty: number }[] }) {
  const [total, setTotal] = useState(0);

  // Same problem — redundant state + effect for a derived value
  useEffect(() => {
    setTotal(items.reduce((sum, item) => sum + item.price * item.qty, 0));
  }, [items]);

  return <p>Total: ${total.toFixed(2)}</p>;
}
```

Problem: each component renders twice per update. The first render shows stale data (`""` or `0`), then the effect fires and triggers a second render with the correct value. This doubles render work and can cause visible flicker.

## Correct

```tsx
interface UserFormProps {
  firstName: string;
  lastName: string;
}

function UserForm({ firstName, lastName }: UserFormProps) {
  // Derived during render — always correct, no extra render cycle
  const fullName = firstName + " " + lastName;

  return <p>Welcome, {fullName}</p>;
}

function CartSummary({ items }: { items: { price: number; qty: number }[] }) {
  // Derived during render — always in sync with items
  const total = items.reduce((sum, item) => sum + item.price * item.qty, 0);

  return <p>Total: ${total.toFixed(2)}</p>;
}
```

Benefit: a single render produces the correct value immediately. No wasted render cycle, no stale intermediate state, and less code to maintain.

## When to Apply

- Any time you see `useEffect(() => setSomeState(f(props)), [props])` — the state and effect can almost certainly be replaced with a simple `const`.
- Concatenations, formatting, filtering, mapping, or reducing that depend only on current props/state.
- If the computation is expensive, use `useMemo` instead — but still avoid `useState` + `useEffect`.

## Back to

- [overview.md](overview.md)

## See Also

- [simple-expression-memo.md](simple-expression-memo.md) — when a simple derivation doesn't even need `useMemo`
- [move-effect-to-event.md](move-effect-to-event.md) — another case of misusing effects
