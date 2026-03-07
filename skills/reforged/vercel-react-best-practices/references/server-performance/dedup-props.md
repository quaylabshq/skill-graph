# Rule: Avoid Duplicate Serialization in RSC Props

**ID:** server-dedup-props
**Category:** Server-Side Performance (Priority 3 — HIGH)

## Explanation

When React Server Components pass props to Client Components, the data is serialized into the RSC payload (a JSON-like wire format). React deduplicates objects in this payload **by reference**, not by value. If you create a new array or object on every render (via `.filter()`, `.map()`, `.toSorted()`, etc.) in a Server Component and pass it as a prop, React sees a unique reference each time and serializes a full copy -- even if the values are identical.

The fix: move transformations (filtering, sorting, mapping) into the Client Component. Pass the raw data once, and let the client derive what it needs. This keeps the serialized payload small and avoids duplicate data in the RSC stream.

## Incorrect

```tsx
// app/page.tsx — Server Component
import { ItemList } from "@/components/ItemList";
import { db } from "@/lib/db";

type Item = { id: string; name: string; active: boolean; priority: number };

export default async function Page() {
  const items: Item[] = await db.item.findMany();

  return (
    <div>
      {/* Each transformation creates a NEW array reference.
          React serializes each one independently — 3 copies of overlapping data. */}
      <ItemList
        activeItems={items.filter((x) => x.active)}
        sortedItems={items.toSorted((a, b) => a.priority - b.priority)}
        itemNames={items.map((x) => x.name)}
      />
    </div>
  );
}
```

Problem: `activeItems`, `sortedItems`, and `itemNames` are three separate serialized arrays derived from the same source. The RSC payload bloats with redundant data.

## Correct

```tsx
// app/page.tsx — Server Component
import { ItemList } from "@/components/ItemList";
import { db } from "@/lib/db";

export default async function Page() {
  const items = await db.item.findMany();

  // Pass the raw data ONCE. Let the client derive views.
  return <ItemList items={items} />;
}
```

```tsx
// components/ItemList.tsx — Client Component
"use client";

import { useMemo } from "react";

type Item = { id: string; name: string; active: boolean; priority: number };

export function ItemList({ items }: { items: Item[] }) {
  const activeItems = useMemo(
    () => items.filter((x) => x.active),
    [items]
  );

  const sortedItems = useMemo(
    () => [...items].sort((a, b) => a.priority - b.priority),
    [items]
  );

  return (
    <div>
      <h2>Active ({activeItems.length})</h2>
      <ul>
        {activeItems.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>

      <h2>By Priority</h2>
      <ul>
        {sortedItems.map((item) => (
          <li key={item.id}>{item.name} (P{item.priority})</li>
        ))}
      </ul>
    </div>
  );
}
```

## Another Common Mistake: Inline Derived Props

```tsx
// BAD — inline object literal creates a new reference every render
<UserCard user={{ name: user.name, role: user.role }} />

// GOOD — if you must subset, extract into a stable variable
// (but prefer passing the full object if the client needs multiple fields)
const userCard = { name: user.name, role: user.role };
<UserCard user={userCard} />
```

Note: even the "stable variable" approach creates a new reference per request. The real win is avoiding multiple overlapping subsets of the same data.

## When to Apply

- Any Server Component that passes transformed/filtered/sorted versions of the same data to a Client Component.
- When you see multiple props derived from the same source array or object.
- Large lists where duplicate serialization visibly inflates the RSC payload.

## Back to

- [overview.md](overview.md)

## See Also

- [serialization.md](serialization.md) — minimize what crosses the server/client boundary overall
- [../rerender-optimization/overview.md](../rerender-optimization/overview.md) — `useMemo` patterns in client components for derived data
