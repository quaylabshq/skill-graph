# Rule: Parallelise Independent Async Operations with `Promise.all()`

**ID:** async-parallel
**Category:** Eliminating Waterfalls (Priority 1 — CRITICAL)

## Explanation

When multiple async operations do not depend on each other's results, run them in parallel with `Promise.all()`. Sequential `await` statements create a waterfall where each operation must complete before the next one starts. With `Promise.all()`, all operations start at the same time, and total latency equals the slowest operation instead of the sum of all operations.

**Three sequential 100ms fetches = 300ms. Three parallel fetches = 100ms.**

## Incorrect

```tsx
// page.tsx — Next.js Server Component
export default async function DashboardPage() {
  // Waterfall: each fetch waits for the previous one to finish
  const user = await fetchUser();         // 120ms
  const notifications = await fetchNotifications(); // 80ms
  const analytics = await fetchAnalytics();         // 150ms
  // Total: ~350ms

  return (
    <Dashboard
      user={user}
      notifications={notifications}
      analytics={analytics}
    />
  );
}
```

## Correct

```tsx
// page.tsx — Next.js Server Component
export default async function DashboardPage() {
  // Parallel: all three fetches start at the same time
  const [user, notifications, analytics] = await Promise.all([
    fetchUser(),         // 120ms
    fetchNotifications(), // 80ms
    fetchAnalytics(),     // 150ms
  ]);
  // Total: ~150ms (the slowest fetch)

  return (
    <Dashboard
      user={user}
      notifications={notifications}
      analytics={analytics}
    />
  );
}
```

## Error Handling

`Promise.all()` rejects as soon as any single promise rejects. If you need partial results even when some operations fail, use `Promise.allSettled()`:

```tsx
const results = await Promise.allSettled([
  fetchUser(),
  fetchNotifications(),
  fetchAnalytics(),
]);

const user = results[0].status === "fulfilled" ? results[0].value : null;
const notifications = results[1].status === "fulfilled" ? results[1].value : null;
const analytics = results[2].status === "fulfilled" ? results[2].value : null;
```

## When to Apply

- Any time you see two or more consecutive `await` statements where no later call uses the result of an earlier one.
- Server Components fetching data from multiple sources.
- API routes aggregating data from several services.
- Server Actions that need to read from multiple tables/APIs before responding.

## Back to

- [overview.md](overview.md)

## See Also

- [dependencies.md](dependencies.md) — when some operations depend on others but not all are sequential
- [api-routes.md](api-routes.md) — starting promises early in API routes for maximum parallelism
