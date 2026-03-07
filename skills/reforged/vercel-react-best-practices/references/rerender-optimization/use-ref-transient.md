# Rule: Use Refs for Frequently-Changing Transient Values

**ID:** rerender-use-ref-transient-values
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

When a value changes at high frequency (mouse position, scroll offset, elapsed time, animation frames) and you don't need React to re-render in response, store it in a `useRef` instead of `useState`. Refs are mutable containers that persist across renders without triggering them. Update the DOM directly via refs or `requestAnimationFrame` when needed.

This is the right choice when the value is consumed by imperative code (DOM manipulation, canvas drawing, analytics) rather than by the JSX render output.

## Incorrect

```tsx
import { useState, useEffect } from "react";

function MouseTracker() {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    function handleMouseMove(e: MouseEvent) {
      // Triggers a re-render on every mouse move (~60 per second)
      setPosition({ x: e.clientX, y: e.clientY });
    }
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, []);

  return (
    <div>
      <div
        className="cursor-indicator"
        style={{
          transform: `translate(${position.x}px, ${position.y}px)`,
        }}
      />
      <p>Coordinates: {position.x}, {position.y}</p>
    </div>
  );
}
```

Problem: 60 state updates per second means 60 full component re-renders per second. React must diff the virtual DOM, update the real DOM, and run any effects — all for a simple position update. This causes jank and wastes CPU cycles.

## Correct

```tsx
import { useRef, useEffect } from "react";

function MouseTracker() {
  const positionRef = useRef({ x: 0, y: 0 });
  const indicatorRef = useRef<HTMLDivElement>(null);
  const coordsRef = useRef<HTMLParagraphElement>(null);

  useEffect(() => {
    function handleMouseMove(e: MouseEvent) {
      // Update ref — no re-render
      positionRef.current = { x: e.clientX, y: e.clientY };

      // Update DOM directly — bypasses React reconciliation
      if (indicatorRef.current) {
        indicatorRef.current.style.transform =
          `translate(${e.clientX}px, ${e.clientY}px)`;
      }
      if (coordsRef.current) {
        coordsRef.current.textContent =
          `Coordinates: ${e.clientX}, ${e.clientY}`;
      }
    }
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, []);

  return (
    <div>
      <div ref={indicatorRef} className="cursor-indicator" />
      <p ref={coordsRef}>Coordinates: 0, 0</p>
    </div>
  );
}
```

Benefit: zero re-renders from mouse movement. DOM updates happen directly in the event handler, which is far cheaper than going through React's reconciliation. The `positionRef` can still be read by other event handlers or callbacks that need the current position.

## Another Example: Scroll Offset for Analytics

```tsx
import { useRef, useEffect, useCallback } from "react";

function ArticlePage({ articleId }: { articleId: string }) {
  const maxScrollRef = useRef(0);

  useEffect(() => {
    function handleScroll() {
      const scrollPercent =
        window.scrollY / (document.body.scrollHeight - window.innerHeight);
      // Update ref — no re-renders during scrolling
      maxScrollRef.current = Math.max(maxScrollRef.current, scrollPercent);
    }
    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  // Only send analytics when leaving the page — reads the ref once
  useEffect(() => {
    return () => {
      sendAnalytics("max_scroll_depth", {
        articleId,
        depth: maxScrollRef.current,
      });
    };
  }, [articleId]);

  return <article>{/* ... */}</article>;
}
```

## When to Apply

- Mouse position, scroll offset, or touch coordinates used for imperative DOM updates or analytics.
- Animation values managed via `requestAnimationFrame`.
- Timers and stopwatches that update a display via direct DOM manipulation.
- "Latest value" refs used to avoid stale closures in async callbacks (e.g., storing the latest callback prop).

## When NOT to Apply

- When the render output (JSX) depends on the value — you need `useState` so React knows to re-render.
- When child components need the value as props.

## Back to

- [overview.md](overview.md)

## See Also

- [derived-state.md](derived-state.md) — when you DO need renders but want fewer of them
- [transitions.md](transitions.md) — when renders are needed but can be deferred
