# Rule: Defer State Reads to Usage Points

**ID:** rerender-defer-reads
**Category:** Re-render Optimization (Priority 5 — MEDIUM)

## Explanation

Don't subscribe to reactive state (like `useSearchParams()`) at the component level if you only read the value inside event handlers or callbacks. Subscribing causes the component to re-render every time the state changes, even though the render output doesn't depend on it. Instead, read the value on demand (e.g., `window.location.search` or a ref) at the point where you actually need it.

This pattern applies to any state that is only consumed inside callbacks: URL search params, scroll positions, form values used only on submit, etc.

## Incorrect

```tsx
import { useSearchParams } from "next/navigation";

function TrackableButton() {
  // Subscribes to search params — component re-renders on every URL change
  const searchParams = useSearchParams();

  function handleClick() {
    const utm = searchParams.get("utm_source");
    analytics.track("click", { utm });
  }

  return <button onClick={handleClick}>Buy Now</button>;
}
```

Problem: every time the URL changes (e.g., a filter is toggled, pagination updates), this component re-renders even though the rendered JSX never uses `searchParams`. The subscription is wasted work.

## Correct

```tsx
function TrackableButton() {
  // No subscription — zero re-renders from URL changes
  function handleClick() {
    const params = new URLSearchParams(window.location.search);
    const utm = params.get("utm_source");
    analytics.track("click", { utm });
  }

  return <button onClick={handleClick}>Buy Now</button>;
}
```

Benefit: the component only re-renders when its own props or parent state change. The search params are read on demand, exactly when needed — no wasted renders.

## When to Apply

- URL search params read only inside `onClick`, `onSubmit`, or other event handlers.
- Any hook-based subscription (`useStore`, `useSelector`, `useSearchParams`) where the value is only consumed in callbacks, not in the render output.
- Scroll position, mouse coordinates, or other rapidly-changing values used only on interaction.

## Back to

- [overview.md](overview.md)
