# Rule: Use SWR for Automatic Request Deduplication

**ID:** client-swr-dedup
**Category:** Client-Side Data Fetching (Priority 4 — MEDIUM-HIGH)

## Explanation

SWR (stale-while-revalidate) automatically deduplicates identical requests across component instances. When multiple components call `useSWR('/api/user')`, SWR issues a single network request and shares the result with every subscriber. It also provides built-in caching, background revalidation, and focus/reconnect refetching out of the box.

Without SWR, each component instance that needs the same data typically fires its own `useEffect` + `fetch`, resulting in N identical network requests for N component instances. This wastes bandwidth, increases server load, and causes UI inconsistencies when responses arrive at different times.

## Incorrect

```tsx
// UserAvatar.tsx — each instance fires its own request
import { useState, useEffect } from "react";

interface User {
  name: string;
  avatarUrl: string;
}

function UserAvatar() {
  const [user, setUser] = useState<User | null>(null);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    // Every instance of <UserAvatar /> triggers a separate fetch
    fetch("/api/user")
      .then((res) => res.json())
      .then(setUser)
      .catch(setError);
  }, []);

  if (error) return <span>Error</span>;
  if (!user) return <span>Loading...</span>;
  return <img src={user.avatarUrl} alt={user.name} />;
}

// Page.tsx — 3 instances = 3 identical GET /api/user requests
export default function Page() {
  return (
    <div>
      <header><UserAvatar /></header>
      <sidebar><UserAvatar /></sidebar>
      <main><UserAvatar /></main>
    </div>
  );
}
```

Problem: three `<UserAvatar />` instances produce three identical `GET /api/user` requests. Each manages its own loading/error state independently, and responses may arrive out of order causing flickering.

## Correct

```tsx
// UserAvatar.tsx — all instances share one request
import useSWR from "swr";

interface User {
  name: string;
  avatarUrl: string;
}

const fetcher = (url: string): Promise<User> =>
  fetch(url).then((res) => {
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
  });

function UserAvatar() {
  // SWR deduplicates: N instances with the same key = 1 network request
  const { data: user, error, isLoading } = useSWR<User>("/api/user", fetcher);

  if (error) return <span>Error</span>;
  if (isLoading) return <span>Loading...</span>;
  return <img src={user.avatarUrl} alt={user.name} />;
}

// Page.tsx — 3 instances = 1 GET /api/user request, shared across all
export default function Page() {
  return (
    <div>
      <header><UserAvatar /></header>
      <sidebar><UserAvatar /></sidebar>
      <main><UserAvatar /></main>
    </div>
  );
}
```

Benefit: one network request regardless of how many components subscribe to the same key. All instances stay in sync, revalidate together, and share a single cache entry.

## When to Apply

- Any time multiple components need the same remote data on the client side.
- Dashboard pages where user info, notifications, or settings appear in multiple places.
- Any client-side data that would otherwise be fetched with `useEffect` + `fetch`.

## Back to

- [overview.md](overview.md)

## See Also

- [event-listeners.md](event-listeners.md) — deduplicating event listeners follows the same "share one resource across N instances" principle
