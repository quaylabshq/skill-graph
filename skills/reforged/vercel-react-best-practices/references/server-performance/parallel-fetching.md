# Rule: Restructure RSC Trees to Parallelize Fetches

**ID:** server-parallel-fetching
**Category:** Server-Side Performance (Priority 3 — HIGH)

## Explanation

In React Server Components, a parent component that `await`s data before rendering its children creates a waterfall: the children cannot even start fetching their own data until the parent finishes. By moving data fetching into leaf (child) components and wrapping them in `<Suspense>`, React can render and fetch all sibling components in parallel.

This is different from using `Promise.all()` in a single component (which is also good). Structural parallelism lets React itself orchestrate concurrent fetching across the component tree, with each component independently streaming in as its data resolves.

## Incorrect

```tsx
// app/dashboard/page.tsx — Server Component
import { db } from "@/lib/db";

export default async function DashboardPage() {
  // Waterfall: each await blocks everything below it
  const user = await db.user.findUnique({ where: { id: userId } });  // 120ms
  const orders = await db.order.findMany({ where: { userId } });     // 200ms
  const recommendations = await fetchRecommendations(userId);         // 300ms
  // Total: ~620ms (sequential)

  return (
    <div>
      <UserProfile user={user} />
      <OrderHistory orders={orders} />
      <Recommendations items={recommendations} />
    </div>
  );
}
```

Problem: the page takes 620ms because each fetch waits for the previous one. Children cannot render or fetch until the parent finishes all three queries.

## Correct

```tsx
// app/dashboard/page.tsx — Server Component
import { Suspense } from "react";
import { UserProfile } from "./UserProfile";
import { OrderHistory } from "./OrderHistory";
import { Recommendations } from "./Recommendations";
import { Skeleton } from "@/components/Skeleton";

export default function DashboardPage() {
  // No data fetching here — each child fetches its own data.
  // React renders all three Suspense boundaries in parallel.
  return (
    <div>
      <Suspense fallback={<Skeleton variant="profile" />}>
        <UserProfile userId={userId} />
      </Suspense>

      <Suspense fallback={<Skeleton variant="table" />}>
        <OrderHistory userId={userId} />
      </Suspense>

      <Suspense fallback={<Skeleton variant="grid" />}>
        <Recommendations userId={userId} />
      </Suspense>
    </div>
  );
}
```

```tsx
// app/dashboard/UserProfile.tsx — Server Component (leaf)
import { db } from "@/lib/db";

export async function UserProfile({ userId }: { userId: string }) {
  const user = await db.user.findUnique({ where: { id: userId } }); // 120ms
  return (
    <section>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </section>
  );
}
```

```tsx
// app/dashboard/OrderHistory.tsx — Server Component (leaf)
import { db } from "@/lib/db";

export async function OrderHistory({ userId }: { userId: string }) {
  const orders = await db.order.findMany({
    where: { userId },
    orderBy: { createdAt: "desc" },
    take: 10,
  }); // 200ms

  return (
    <section>
      <h2>Recent Orders</h2>
      <ul>
        {orders.map((order) => (
          <li key={order.id}>{order.title} - ${order.total}</li>
        ))}
      </ul>
    </section>
  );
}
```

```tsx
// app/dashboard/Recommendations.tsx — Server Component (leaf)
export async function Recommendations({ userId }: { userId: string }) {
  const items = await fetchRecommendations(userId); // 300ms

  return (
    <section>
      <h2>Recommended for You</h2>
      <div className="grid grid-cols-3 gap-4">
        {items.map((item) => (
          <div key={item.id}>{item.name}</div>
        ))}
      </div>
    </section>
  );
}
```

Result: total time is ~300ms (the slowest fetch) instead of ~620ms. Each section streams in as its data resolves.

## When to Prefer `Promise.all()` Instead

If multiple fetches are needed in the same component (e.g., a component needs both `user` and `team` to render), use `Promise.all()` within that component:

```tsx
export async function UserProfile({ userId }: { userId: string }) {
  const [user, team] = await Promise.all([
    getUser(userId),
    getTeam(userId),
  ]);

  return <div>{user.name} — {team.name}</div>;
}
```

Use structural parallelism (Suspense boundaries) when different components need different data. Use `Promise.all()` when one component needs multiple pieces of data.

## When to Apply

- Dashboard pages with multiple independent data sections.
- Any page where a parent fetches data that only specific children use.
- Layouts that load user data, notifications, and navigation independently.
- Pages where some data is fast (user profile) and some is slow (recommendations) -- Suspense lets fast sections appear immediately.

## Back to

- [overview.md](overview.md)

## See Also

- [../async-waterfalls/parallel.md](../async-waterfalls/parallel.md) — `Promise.all()` for parallelizing within a single component
- [cache-react.md](cache-react.md) — if sibling components need the same data, `React.cache()` deduplicates
- [serialization.md](serialization.md) — each leaf component should only fetch/pass what it needs
