# Rule: Use Passive Event Listeners for Touch and Wheel Events

**ID:** client-passive-event-listeners
**Category:** Client-Side Data Fetching (Priority 4 — MEDIUM-HIGH)

## Explanation

When the browser receives a `touchstart`, `touchmove`, or `wheel` event, it must wait for the JavaScript handler to finish before it can scroll the page. This is because the handler might call `event.preventDefault()` to cancel scrolling. Even if the handler never calls `preventDefault()`, the browser cannot know this in advance, so it blocks scrolling until the handler completes.

Adding `{ passive: true }` to the event listener tells the browser: "this handler will never call `preventDefault()`." The browser can then start scrolling immediately while the handler runs in parallel, eliminating scroll jank and reducing input latency. If a passive handler does call `preventDefault()`, the call is silently ignored and a console warning is logged.

Modern browsers default `touchstart` and `touchmove` to passive on `document` and `window` targets, but **not** on other elements. You must explicitly opt in for element-level listeners.

## Incorrect

```tsx
import { useEffect, useRef } from "react";

function ScrollableList({ onScrollMetric }: { onScrollMetric: (y: number) => void }) {
  const listRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = listRef.current;
    if (!el) return;

    // Non-passive: browser blocks scrolling until handler completes
    const handleTouchStart = (e: TouchEvent) => {
      onScrollMetric(e.touches[0].clientY);
    };

    const handleWheel = (e: WheelEvent) => {
      onScrollMetric(e.deltaY);
    };

    // Missing { passive: true } — scroll jank on mobile devices
    el.addEventListener("touchstart", handleTouchStart);
    el.addEventListener("touchmove", handleTouchStart);
    el.addEventListener("wheel", handleWheel);

    return () => {
      el.removeEventListener("touchstart", handleTouchStart);
      el.removeEventListener("touchmove", handleTouchStart);
      el.removeEventListener("wheel", handleWheel);
    };
  }, [onScrollMetric]);

  return (
    <div ref={listRef} style={{ overflowY: "auto", height: "400px" }}>
      {/* list items */}
    </div>
  );
}
```

Problem: the browser waits for each handler to finish before it starts or continues scrolling. On slower devices, this creates noticeable scroll jank -- the page "sticks" under the user's finger.

## Correct

```tsx
import { useEffect, useRef, useCallback } from "react";

function ScrollableList({ onScrollMetric }: { onScrollMetric: (y: number) => void }) {
  const listRef = useRef<HTMLDivElement>(null);

  // Stabilise the callback to avoid re-registering listeners on every render
  const stableMetric = useCallback(onScrollMetric, [onScrollMetric]);

  useEffect(() => {
    const el = listRef.current;
    if (!el) return;

    const handleTouchStart = (e: TouchEvent) => {
      // Cannot call e.preventDefault() in a passive listener (ignored + warning)
      stableMetric(e.touches[0].clientY);
    };

    const handleWheel = (e: WheelEvent) => {
      stableMetric(e.deltaY);
    };

    // { passive: true } — browser scrolls immediately, handler runs in parallel
    el.addEventListener("touchstart", handleTouchStart, { passive: true });
    el.addEventListener("touchmove", handleTouchStart, { passive: true });
    el.addEventListener("wheel", handleWheel, { passive: true });

    return () => {
      el.removeEventListener("touchstart", handleTouchStart);
      el.removeEventListener("touchmove", handleTouchStart);
      el.removeEventListener("wheel", handleWheel);
    };
  }, [stableMetric]);

  return (
    <div ref={listRef} style={{ overflowY: "auto", height: "400px" }}>
      {/* list items */}
    </div>
  );
}
```

Benefit: the browser begins scrolling the instant the user touches or scrolls, without waiting for JavaScript. The handler still runs and can record metrics, but it cannot block the scroll thread.

## When NOT to Use Passive

If your handler **must** call `preventDefault()` (e.g., to implement custom drag-and-drop or prevent pull-to-refresh), do not mark it as passive:

```tsx
// Custom drag behavior — needs to prevent default scrolling
el.addEventListener("touchmove", (e: TouchEvent) => {
  e.preventDefault(); // This MUST work, so do not use { passive: true }
  handleDrag(e);
}, { passive: false }); // explicit non-passive
```

## When to Apply

- Touch event listeners (`touchstart`, `touchmove`) on scrollable containers.
- Wheel event listeners (`wheel`) for analytics, parallax effects, or custom scroll indicators.
- Any event handler that reads event properties but does not call `preventDefault()`.
- Mobile-facing applications where scroll performance is critical.

## Back to

- [overview.md](overview.md)

## See Also

- [event-listeners.md](event-listeners.md) — deduplicating event listeners across component instances
