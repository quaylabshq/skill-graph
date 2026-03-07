# Rule: Use Set/Map for O(1) Lookups Instead of Array

**ID:** js-set-map-lookups
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

`Array.includes()` and `Array.indexOf()` perform a linear scan — O(n) per call. When checking membership repeatedly in a loop, this becomes O(n*m) where n is the array length and m is the number of checks. Converting the array to a `Set` gives O(1) `.has()` lookups, reducing the total to O(n+m).

The upfront cost of building the Set is O(n), so this optimization pays off when you perform more than one or two lookups against the same collection.

## Incorrect

```ts
// BAD: O(n) lookup on every iteration
function filterAllowed(
  items: { id: string; name: string }[],
  allowedIds: string[]
): { id: string; name: string }[] {
  return items.filter((item) => allowedIds.includes(item.id));
  // 1,000 items × 500 allowedIds = 500,000 comparisons
}

// BAD: repeated .includes() in event handler
function handleSelection(
  selectedIds: string[],
  clickedId: string
): string[] {
  if (selectedIds.includes(clickedId)) {
    return selectedIds.filter((id) => id !== clickedId);
  }
  return [...selectedIds, clickedId];
}

// BAD: checking membership in nested loops
function findCommonTags(
  posts: { tags: string[] }[],
  targetTags: string[]
): string[][] {
  return posts.map((post) =>
    post.tags.filter((tag) => targetTags.includes(tag))
  );
}
```

Problem: each `.includes()` call scans up to the entire array. In loops, this creates quadratic behavior that degrades rapidly as data grows.

## Correct

```ts
// GOOD: Set for O(1) membership checks
function filterAllowed(
  items: { id: string; name: string }[],
  allowedIds: string[]
): { id: string; name: string }[] {
  const allowed = new Set(allowedIds); // O(n) one-time cost
  return items.filter((item) => allowed.has(item.id)); // O(1) per check
  // 500 (build Set) + 1,000 (filter) = 1,500 operations
}

// GOOD: Set for toggle operations
function handleSelection(
  selectedIds: string[],
  clickedId: string
): string[] {
  const selected = new Set(selectedIds);

  if (selected.has(clickedId)) {
    selected.delete(clickedId);
  } else {
    selected.add(clickedId);
  }

  return Array.from(selected);
}

// GOOD: Set for nested membership checks
function findCommonTags(
  posts: { tags: string[] }[],
  targetTags: string[]
): string[][] {
  const targetSet = new Set(targetTags);
  return posts.map((post) =>
    post.tags.filter((tag) => targetSet.has(tag))
  );
}
```

Benefit: `Set.has()` is O(1) regardless of set size. For 1,000 items filtered against 500 allowed IDs, this reduces comparisons from 500,000 to 1,500.

### When to keep the Set as state

```tsx
import { useMemo } from "react";

function UserList({
  users,
  blockedIds,
}: {
  users: { id: string; name: string }[];
  blockedIds: string[];
}) {
  // Memoize the Set so it's not rebuilt on every render
  const blockedSet = useMemo(() => new Set(blockedIds), [blockedIds]);

  const visibleUsers = users.filter((u) => !blockedSet.has(u.id));

  return (
    <ul>
      {visibleUsers.map((u) => (
        <li key={u.id}>{u.name}</li>
      ))}
    </ul>
  );
}
```

## When to Apply

- Filtering an array against an allow-list or block-list.
- Checking membership inside any loop (`.filter()`, `.map()`, `for...of`).
- Deduplication — `new Set(array)` removes duplicates in O(n).
- Any case where `.includes()` is called more than once against the same array.

## Back to

- [overview.md](overview.md)

## See Also

- [index-maps.md](index-maps.md) — using `Map` for key-value lookups (not just membership)
- [combine-iterations.md](combine-iterations.md) — reducing total array passes
