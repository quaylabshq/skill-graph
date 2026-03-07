# Rule: Use `React.cache()` for Per-Request Deduplication

**ID:** server-cache-react
**Category:** Server-Side Performance (Priority 3 — HIGH)

## Explanation

In React Server Components, the same data-fetching function can be called from multiple components in the same render tree. Without deduplication, each call results in a separate database query or API request. `React.cache()` memoizes function results for the duration of a single server request, so the second call with the same arguments returns the cached result instantly.

Key details:
- **Scope:** one request only. A new request gets a fresh cache.
- **Equality:** arguments are compared with shallow equality. Avoid passing inline objects (`{}`) because a new object reference is created each time, defeating the cache.
- **Typical use cases:** user session lookups, permission checks, fetching the same entity from multiple components.

## Incorrect

```tsx
// lib/queries.ts
import { db } from "@/lib/db";

// Not wrapped in React.cache — each call is a separate DB query
export async function getUser(id: string) {
  return db.user.findUnique({ where: { id } });
}

// --- components/Header.tsx (Server Component) ---
export default async function Header() {
  const user = await getUser(userId); // DB query #1
  return <nav>{user.name}</nav>;
}

// --- components/Sidebar.tsx (Server Component) ---
export default async function Sidebar() {
  const user = await getUser(userId); // DB query #2 (duplicate!)
  return <aside>Role: {user.role}</aside>;
}

// --- app/page.tsx ---
export default function Page() {
  return (
    <>
      <Header />   {/* query fires */}
      <Sidebar />  {/* same query fires again */}
    </>
  );
}
```

Problem: `getUser` is called twice with the same ID in one request, producing two identical database queries.

## Correct

```tsx
// lib/queries.ts
import { cache } from "react";
import { db } from "@/lib/db";

// Wrapped in React.cache — second call with same `id` returns memoized result
export const getUser = cache(async (id: string) => {
  return db.user.findUnique({ where: { id } });
});

// Primitive arguments (strings, numbers) work perfectly with shallow equality.
export const getTeam = cache(async (teamId: string) => {
  return db.team.findUnique({
    where: { id: teamId },
    include: { members: true },
  });
});

// --- components/Header.tsx ---
export default async function Header() {
  const user = await getUser(userId); // DB query #1
  return <nav>{user.name}</nav>;
}

// --- components/Sidebar.tsx ---
export default async function Sidebar() {
  const user = await getUser(userId); // cache hit — no DB query
  return <aside>Role: {user.role}</aside>;
}
```

## Pitfall: Inline Object Arguments

```tsx
// BAD — new object reference every time, cache never hits
const getFilteredUsers = cache(async (filters: { role: string }) => {
  return db.user.findMany({ where: filters });
});

await getFilteredUsers({ role: "admin" }); // miss
await getFilteredUsers({ role: "admin" }); // miss again! Different object ref

// GOOD — use primitive arguments
const getUsersByRole = cache(async (role: string) => {
  return db.user.findMany({ where: { role } });
});

await getUsersByRole("admin"); // miss
await getUsersByRole("admin"); // hit!
```

## When to Apply

- Any data-fetching function called from more than one Server Component in the same render.
- Auth/session checks that multiple components rely on.
- Configuration or feature-flag lookups used across the component tree.

## Back to

- [overview.md](overview.md)

## See Also

- [cache-lru.md](cache-lru.md) — when you need caching across multiple requests, not just within one
- [../async-waterfalls/parallel.md](../async-waterfalls/parallel.md) — parallelize independent fetches after deduplicating shared ones
