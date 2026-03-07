# Rule: Subscribe to Derived Booleans, Not Raw Values

**ID:** rerender-derived-state
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

When a component only needs to know whether a condition is true or false, subscribe to a derived boolean rather than the raw continuous value. A boolean has only two possible states (`true` / `false`), so the component only re-renders when crossing the threshold — not on every incremental change.

This is especially impactful for values that change at high frequency: window width, scroll position, time elapsed, etc.

## Incorrect

```tsx
import { useState, useEffect } from "react";

function useWindowWidth(): number {
  const [width, setWidth] = useState(
    typeof window !== "undefined" ? window.innerWidth : 0
  );

  useEffect(() => {
    function handleResize() {
      setWidth(window.innerWidth);
    }
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return width;
}

function Navigation() {
  // Re-renders on every single pixel change during resize
  const width = useWindowWidth();
  const isMobile = width < 768;

  return isMobile ? <MobileNav /> : <DesktopNav />;
}
```

Problem: dragging the window edge from 1200px to 800px causes ~400 re-renders, even though the component only cares about crossing the 768px boundary.

## Correct

```tsx
import { useState, useEffect } from "react";

function useMediaQuery(query: string): boolean {
  const [matches, setMatches] = useState(() =>
    typeof window !== "undefined"
      ? window.matchMedia(query).matches
      : false
  );

  useEffect(() => {
    const mql = window.matchMedia(query);
    function handleChange(e: MediaQueryListEvent) {
      setMatches(e.matches);
    }
    mql.addEventListener("change", handleChange);
    return () => mql.removeEventListener("change", handleChange);
  }, [query]);

  return matches;
}

function Navigation() {
  // Only re-renders when crossing the 768px boundary
  const isMobile = useMediaQuery("(max-width: 767px)");

  return isMobile ? <MobileNav /> : <DesktopNav />;
}
```

Benefit: the `change` event on `matchMedia` only fires when the boolean result flips. The same 1200px-to-800px drag causes exactly one re-render (when crossing 768px) instead of ~400.

## When to Apply

- Components that render conditionally based on window size — use `useMediaQuery` over `useWindowWidth`.
- Scroll-based visibility (e.g., "show back-to-top button") — subscribe to `isScrolledPast(threshold)`, not raw `scrollY`.
- Online/offline status, dark-mode preference, or any binary derived state.
- Any time a continuous source of truth (number, timestamp) is only used for a boolean decision.

## Back to

- [overview.md](overview.md)

## See Also

- [dependencies.md](dependencies.md) — narrowing effect dependencies with primitives and derived values
- [use-ref-transient.md](use-ref-transient.md) — when you need the raw value but don't need renders
