# Rule: Build a Map for Repeated Lookups

**ID:** js-index-maps
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

When you have two arrays and need to match items between them (e.g., orders to users), using `.find()` inside `.map()` creates an O(n*m) operation. With 1,000 orders and 1,000 users, that's 1,000,000 comparisons. Building a `Map` first converts this to O(n+m) — just 2,000 operations.

The pattern: build a `Map` keyed by the join field from one array, then look up each item from the other array in O(1).

## Incorrect

```ts
interface User {
  id: string;
  name: string;
  email: string;
}

interface Order {
  id: string;
  userId: string;
  total: number;
}

// BAD: O(n * m) — .find() scans the entire users array for every order
function enrichOrders(orders: Order[], users: User[]) {
  return orders.map((order) => ({
    ...order,
    user: users.find((u) => u.id === order.userId),
  }));
}

// 1,000 orders × 1,000 users = 1,000,000 comparisons
```

Problem: `.find()` is a linear scan. Nested inside `.map()`, you get quadratic time complexity that grows rapidly with data size.

## Correct

```ts
interface User {
  id: string;
  name: string;
  email: string;
}

interface Order {
  id: string;
  userId: string;
  total: number;
}

// GOOD: O(n + m) — build Map once, then O(1) lookups
function enrichOrders(orders: Order[], users: User[]) {
  const userMap = new Map<string, User>(
    users.map((u) => [u.id, u])
  );

  return orders.map((order) => ({
    ...order,
    user: userMap.get(order.userId),
  }));
}

// 1,000 users to build Map + 1,000 lookups = 2,000 operations
```

Benefit: building the Map is O(m) and each lookup is O(1), so the total is O(n+m) instead of O(n*m). For 1,000 items each, this is a 500x improvement.

## When to Apply

- Joining two arrays by a shared key (user IDs, product IDs, category slugs).
- Any loop that calls `.find()` or `.findIndex()` on the same array repeatedly.
- Data enrichment before rendering lists (e.g., attaching user names to comments).

## Back to

- [overview.md](overview.md)

## See Also

- [set-map-lookups.md](set-map-lookups.md) — using `Set` for O(1) membership checks
- [combine-iterations.md](combine-iterations.md) — reducing passes over arrays
