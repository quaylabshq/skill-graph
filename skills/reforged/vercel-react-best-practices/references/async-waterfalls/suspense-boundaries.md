# Rule: Use Suspense Boundaries to Stream Progressive Content

**ID:** async-suspense-boundaries
**Category:** Eliminating Waterfalls (Priority 1 — CRITICAL)

## Explanation

Instead of awaiting all data at the page level before rendering anything, push data fetching into child components and wrap them with `<Suspense>`. This lets Next.js stream the page shell and fast-loading sections to the user immediately while slower data loads in the background. Combined with React's `use()` hook, you can start fetches at the parent level and pass the **promises** (not the resolved values) to children, avoiding waterfalls while still getting progressive rendering.

## Incorrect

```tsx
// app/dashboard/page.tsx
// Everything blocks on the slowest fetch — user sees nothing until all data is ready
export default async function DashboardPage() {
  const user = await fetchUser();               // 100ms
  const stats = await fetchStats();             // 300ms (slow!)
  const notifications = await fetchNotifications(); // 80ms

  return (
    <div>
      <Header user={user} />
      <StatsPanel stats={stats} />
      <NotificationList notifications={notifications} />
    </div>
  );
}
```

Problem: the user stares at a blank page for 480ms (waterfall) or at least 300ms (even if parallelised) before seeing anything.

## Correct (Suspense + Async Child Components)

```tsx
// app/dashboard/page.tsx
import { Suspense } from "react";

export default async function DashboardPage() {
  // Fast fetch — resolve at page level
  const user = await fetchUser(); // 100ms

  return (
    <div>
      <Header user={user} />

      {/* Slow sections stream in as they resolve */}
      <Suspense fallback={<StatsSkeleton />}>
        <StatsPanel />
      </Suspense>

      <Suspense fallback={<NotificationsSkeleton />}>
        <NotificationList />
      </Suspense>
    </div>
  );
}

// app/dashboard/stats-panel.tsx
export default async function StatsPanel() {
  const stats = await fetchStats(); // 300ms — streams when ready
  return <div>{/* render stats */}</div>;
}

// app/dashboard/notification-list.tsx
export default async function NotificationList() {
  const notifications = await fetchNotifications(); // 80ms — streams when ready
  return <ul>{/* render notifications */}</ul>;
}
```

Result: the user sees `<Header>` and both skeleton fallbacks after ~100ms. Notifications fill in at ~180ms. Stats fill in at ~300ms.

## Advanced: Share Promises with `use()`

When you need to start fetches at the parent level (to avoid child-level waterfalls) but still want Suspense streaming, pass promises down and consume them with `use()`:

```tsx
// app/dashboard/page.tsx
import { Suspense } from "react";

export default function DashboardPage() {
  // Start all fetches immediately at the parent — no await
  const statsPromise = fetchStats();
  const notificationsPromise = fetchNotifications();

  return (
    <div>
      <Suspense fallback={<StatsSkeleton />}>
        <StatsPanel statsPromise={statsPromise} />
      </Suspense>

      <Suspense fallback={<NotificationsSkeleton />}>
        <NotificationList notificationsPromise={notificationsPromise} />
      </Suspense>
    </div>
  );
}

// app/dashboard/stats-panel.tsx
"use client";

import { use } from "react";

export default function StatsPanel({
  statsPromise,
}: {
  statsPromise: Promise<Stats>;
}) {
  const stats = use(statsPromise); // suspends until resolved
  return <div>{/* render stats */}</div>;
}
```

Both fetches start in parallel at the parent level, but each child independently suspends and streams as soon as its data is ready.

## When to Apply

- Pages with a mix of fast and slow data sources.
- Dashboards, profile pages, or any layout with multiple independent data sections.
- Any page where you want the shell/navigation to appear instantly.
- When migrating from a single `loading.tsx` to per-section loading states.

## Back to

- [overview.md](overview.md)

## See Also

- [parallel.md](parallel.md) — parallelise fetches before layering Suspense on top
- [defer-await.md](defer-await.md) — avoid fetching data that conditional branches don't need
- [api-routes.md](api-routes.md) — the server-side equivalent of starting work early
