# Rule: Handle Partial Dependencies Without Full Waterfalls

**ID:** async-dependencies
**Category:** Eliminating Waterfalls (Priority 1 — CRITICAL)

## Explanation

Real-world data fetching often has **partial dependencies**: some operations depend on the results of others, but not everything is strictly sequential. Naive code either waterfalls everything or incorrectly parallelises dependent calls. The goal is to maximise parallelism while respecting actual data dependencies.

Two approaches:

1. **Manual promise orchestration** — create all independent promises immediately, `await` them only when their results are needed.
2. **`better-all` library** — declare dependencies declaratively and let the library schedule maximum parallelism automatically.

## Incorrect

```tsx
// Everything sequential — unnecessary waterfall
async function loadOrderPage(orderId: string) {
  const session = await auth();                          // 100ms
  const order = await fetchOrder(orderId);               // 150ms (needs nothing)
  const user = await fetchUser(session.userId);          // 120ms (needs session)
  const recommendations = await fetchRecommendations(order.productId); // 80ms (needs order)
  // Total: ~450ms — but session and order are independent!

  return { session, order, user, recommendations };
}
```

## Correct (Manual Promise Orchestration)

```tsx
async function loadOrderPage(orderId: string) {
  // Step 1: start all independent work immediately
  const sessionP = auth();              // starts now
  const orderP = fetchOrder(orderId);   // starts now, independent of session

  // Step 2: await results only when needed by dependent operations
  const session = await sessionP;                        // ~100ms
  const order = await orderP;                            // ~150ms (ran in parallel with session)

  // Step 3: start dependent operations in parallel with each other
  const [user, recommendations] = await Promise.all([
    fetchUser(session.userId),                           // needs session
    fetchRecommendations(order.productId),               // needs order
  ]);
  // Total: ~max(100,150) + max(120,80) = ~270ms

  return { session, order, user, recommendations };
}
```

## Correct (Using `better-all`)

```tsx
import { all } from "better-all";

async function loadOrderPage(orderId: string) {
  const { session, order, user, recommendations } = await all({
    session: auth(),
    order: fetchOrder(orderId),
    user: ({ session }) => fetchUser(session.userId),
    recommendations: ({ order }) => fetchRecommendations(order.productId),
  });
  // better-all resolves the dependency graph automatically:
  // session and order run in parallel,
  // user starts as soon as session resolves,
  // recommendations starts as soon as order resolves.

  return { session, order, user, recommendations };
}
```

`better-all` determines the optimal execution order from the function signatures — any entry that is a plain promise runs immediately, and any entry that is a function receives resolved values of its declared dependencies.

## When to Apply

- You have 3+ async operations and at least one depends on another's result.
- A waterfall diagram shows gaps where independent work could overlap.
- You find yourself writing "step 1, step 2, step 3" comments around sequential awaits.

## Back to

- [overview.md](overview.md)

## See Also

- [parallel.md](parallel.md) — simpler case where all operations are fully independent
- [defer-await.md](defer-await.md) — eliminating awaits that are not needed at all in certain branches
