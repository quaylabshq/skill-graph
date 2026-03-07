# Rule: Use Primitive Dependencies in Effects

**ID:** rerender-dependencies
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

When specifying dependency arrays for `useEffect`, `useMemo`, or `useCallback`, prefer primitive values (strings, numbers, booleans) over objects. Objects are compared by reference, so even if the content is identical, a new object reference triggers the effect again. Extract the specific primitive fields you depend on, or derive a boolean from a continuous value to narrow the dependency.

## Incorrect

```tsx
import { useEffect } from "react";

interface User {
  id: string;
  name: string;
  email: string;
  preferences: Record<string, unknown>;
}

function UserProfile({ user }: { user: User }) {
  // Fires every render if `user` is a new object reference,
  // even when user.id hasn't changed
  useEffect(() => {
    fetchUserActivity(user.id);
  }, [user]);

  return <h1>{user.name}</h1>;
}

function ResponsiveLayout({ width }: { width: number }) {
  // Fires on every pixel change (e.g., 1024 -> 1023 -> 1022)
  useEffect(() => {
    adjustLayout(width < 768);
  }, [width]);

  return <div>Current width: {width}</div>;
}
```

Problem: the first effect re-runs whenever the parent creates a new `user` object, even if the `id` is the same. The second effect fires on every single pixel change even though the logic only cares about a breakpoint threshold.

## Correct

```tsx
import { useEffect } from "react";

interface User {
  id: string;
  name: string;
  email: string;
  preferences: Record<string, unknown>;
}

function UserProfile({ user }: { user: User }) {
  // Only fires when the actual user ID changes
  useEffect(() => {
    fetchUserActivity(user.id);
  }, [user.id]);

  return <h1>{user.name}</h1>;
}

function ResponsiveLayout({ width }: { width: number }) {
  // Derive a boolean — only two possible values instead of thousands
  const isMobile = width < 768;

  // Only fires when crossing the breakpoint
  useEffect(() => {
    adjustLayout(isMobile);
  }, [isMobile]);

  return <div>Current width: {width}</div>;
}
```

Benefit: effects only fire when the values they actually care about change. `user.id` is a primitive string, so reference equality works correctly. `isMobile` collapses a continuous range into two states, drastically reducing effect executions.

## When to Apply

- `useEffect` dependencies include objects, arrays, or nested structures — extract the specific primitives the effect uses.
- Dependencies include a continuous numeric value (width, scroll position, timestamp) but the logic only cares about a threshold — derive a boolean.
- Effects fire more often than expected — check if any dependency is an object recreated on each render.

## Back to

- [overview.md](overview.md)

## See Also

- [derived-state.md](derived-state.md) — subscribing to derived booleans instead of raw values at the hook level
