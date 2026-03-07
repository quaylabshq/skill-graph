# Rule: Initialize Once Per App Load, Not Per Mount

**ID:** advanced-init-once
**Category:** Advanced Patterns (Priority 8 — LOW)

## Explanation

Some initialization code must run exactly once for the lifetime of the application: analytics SDKs, global error handlers, feature-flag bootstrapping, third-party script setup, etc. Placing this code inside `useEffect(fn, [])` is unreliable because React 18 Strict Mode intentionally double-invokes effects during development to surface impure side effects. That means your SDK initializes twice, potentially sending duplicate events, registering duplicate listeners, or crashing on "already initialized" guards.

The solution is a module-level flag (`let didInit = false`) checked during rendering — not inside an effect. Module-level code executes once per page load regardless of Strict Mode, remounts, or hot-module replacement. The guard ensures the initialization block runs exactly once.

## Incorrect

```tsx
import { useEffect } from "react";
import { initAnalytics } from "@/lib/analytics";
import { bootstrapFeatureFlags } from "@/lib/feature-flags";

function App({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    // In React 18 Strict Mode (dev), this runs TWICE —
    // double-initializing the analytics SDK and feature flags.
    initAnalytics({ trackingId: "UA-XXXXX" });
    bootstrapFeatureFlags();
  }, []);

  return <>{children}</>;
}
```

Problem: React 18 Strict Mode mounts, unmounts, and remounts components in development to help find bugs. The empty-deps effect fires on each mount, so `initAnalytics` and `bootstrapFeatureFlags` execute twice. In production with concurrent features or future React versions, effects may also re-run after recoverable errors.

## Correct

```tsx
import { initAnalytics } from "@/lib/analytics";
import { bootstrapFeatureFlags } from "@/lib/feature-flags";

let didInit = false;

function App({ children }: { children: React.ReactNode }) {
  if (!didInit) {
    didInit = true;

    // Runs exactly once per page load — immune to Strict Mode,
    // remounts, and concurrent rendering retries.
    initAnalytics({ trackingId: "UA-XXXXX" });
    bootstrapFeatureFlags();
  }

  return <>{children}</>;
}

export default App;
```

Benefit: the initialization block runs exactly once, the first time `App` renders. The module-level `didInit` flag persists across re-renders and Strict Mode double-invocations. No cleanup is needed because the code never re-runs.

### Alternative: Top-Level Module Side Effect

For initialization that has zero dependency on React (no hooks, no component context), you can run it at the module level entirely outside the component:

```tsx
import { initAnalytics } from "@/lib/analytics";
import { bootstrapFeatureFlags } from "@/lib/feature-flags";

// Executes once when the module is first imported
initAnalytics({ trackingId: "UA-XXXXX" });
bootstrapFeatureFlags();

function App({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}

export default App;
```

This is even simpler but gives you less control over timing — the code runs at import time, not at first render. Use the `didInit` pattern when you need the initialization to happen at a specific point in the component lifecycle.

## When to Apply

- Analytics SDK initialization (`initAnalytics`, `Sentry.init`, `posthog.init`).
- Global error boundary or `window.onerror` / `window.onunhandledrejection` registration.
- Feature-flag bootstrapping that should happen once per session.
- Any side effect that is app-wide (not component-scoped) and must not run twice.

## Back to

- [overview.md](overview.md)

## See Also

- [event-handler-refs.md](event-handler-refs.md) — another pattern for escaping effect re-runs
- [../rerender-optimization/memo.md](../rerender-optimization/memo.md) — memoize components to prevent unnecessary re-renders that could trigger effects
- [../rerender-optimization/defer-reads.md](../rerender-optimization/defer-reads.md) — avoid hook subscriptions when values are only needed in callbacks
