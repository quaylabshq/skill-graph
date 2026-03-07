# Rule: Store Event Handlers in Refs for Stable Effect Subscriptions

**ID:** advanced-event-handler-refs
**Category:** Advanced Patterns (Priority 8 — LOW)

## Explanation

When an effect subscribes to a DOM event (scroll, resize, pointer, etc.), listing the callback in the dependency array causes the effect to tear down and re-subscribe every time the callback identity changes. For handlers created inline or derived from props, that means re-subscribing on every render — adding and removing listeners unnecessarily and potentially missing events during the gap.

The fix is to store the handler in a ref that always points to the latest version. The effect reads `ref.current` when the event fires, so it always calls the up-to-date handler without needing to re-run. Alternatively, React's experimental `useEffectEvent` hook solves this at the framework level (see [use-latest.md](use-latest.md)).

## Incorrect

```tsx
import { useEffect } from "react";

interface ScrollTrackerProps {
  onScroll: (scrollY: number) => void;
}

function ScrollTracker({ onScroll }: ScrollTrackerProps) {
  useEffect(() => {
    const handle = () => onScroll(window.scrollY);

    // Subscribes and unsubscribes every time `onScroll` changes —
    // which is every render if the parent passes an inline arrow.
    window.addEventListener("scroll", handle, { passive: true });
    return () => window.removeEventListener("scroll", handle);
  }, [onScroll]);

  return <div>Tracking scroll position...</div>;
}
```

Problem: if the parent renders `<ScrollTracker onScroll={(y) => logScroll(y)} />`, the `onScroll` prop is a new function reference on every render. The effect re-runs each time, tearing down and re-creating the scroll listener — wasting work and risking dropped events during the teardown/setup gap.

## Correct

```tsx
import { useEffect, useRef } from "react";

interface ScrollTrackerProps {
  onScroll: (scrollY: number) => void;
}

function ScrollTracker({ onScroll }: ScrollTrackerProps) {
  // Always points to the latest handler — no effect re-run needed
  const onScrollRef = useRef(onScroll);
  onScrollRef.current = onScroll;

  useEffect(() => {
    const handle = () => onScrollRef.current(window.scrollY);

    // Subscribes once on mount, stable for the component's lifetime
    window.addEventListener("scroll", handle, { passive: true });
    return () => window.removeEventListener("scroll", handle);
  }, []); // no dependency on onScroll

  return <div>Tracking scroll position...</div>;
}
```

Benefit: the scroll listener is attached once and never re-subscribes. When the event fires, `onScrollRef.current` always invokes the latest `onScroll` callback without the effect needing to know it changed.

### Alternative: `useEffectEvent` (React experimental)

```tsx
import { useEffect, experimental_useEffectEvent as useEffectEvent } from "react";

function ScrollTracker({ onScroll }: ScrollTrackerProps) {
  const onScrollStable = useEffectEvent(onScroll);

  useEffect(() => {
    const handle = () => onScrollStable(window.scrollY);
    window.addEventListener("scroll", handle, { passive: true });
    return () => window.removeEventListener("scroll", handle);
  }, []); // onScrollStable is inherently stable

  return <div>Tracking scroll position...</div>;
}
```

`useEffectEvent` wraps a callback so it always sees the latest closure values but has a stable identity — no ref boilerplate needed.

## When to Apply

- Effects that add/remove DOM event listeners (scroll, resize, pointer, keyboard) where the handler comes from props or is recreated each render.
- WebSocket or EventSource message handlers passed as props.
- Any `useEffect` that re-runs only because a callback dependency changes, not because the subscription target changes.

## Back to

- [overview.md](overview.md)

## See Also

- [use-latest.md](use-latest.md) — the `useEffectEvent` pattern for stable callback refs
- [../rerender-optimization/memo.md](../rerender-optimization/memo.md) — memoize components to reduce how often callback props change
- [../rerender-optimization/defer-reads.md](../rerender-optimization/defer-reads.md) — avoid subscriptions entirely when values are only read in callbacks
