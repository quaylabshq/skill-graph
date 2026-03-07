# Rule: Defer `await` to Branches Where Actually Used

**ID:** async-defer-await
**Category:** Eliminating Waterfalls (Priority 1 — CRITICAL)

## Explanation

Do not `await` a promise at the top of a function if the result is only used in a conditional branch. When the branch that skips the result is taken, you pay the full latency cost of the async operation for nothing. Instead, move the `await` (and the fetch itself) into the branch where the data is actually consumed.

This applies to any early-exit or conditional pattern: feature flags, permission checks, cache hits, `skipProcessing` booleans, etc.

## Incorrect

```tsx
// server action or API route handler
async function handleSubmission(formData: FormData) {
  const data = await fetchData(); // always waits ~200ms
  const user = await getUser();   // always waits ~150ms

  if (formData.get("skipProcessing")) {
    // data and user were fetched but never used
    return { skipped: true };
  }

  return processSubmission(data, user);
}
```

Problem: when `skipProcessing` is true the function still waits 350ms for two fetches it never uses.

## Correct

```tsx
async function handleSubmission(formData: FormData) {
  if (formData.get("skipProcessing")) {
    // early return — no fetches at all
    return { skipped: true };
  }

  // only fetch when we know we need the data
  const [data, user] = await Promise.all([fetchData(), getUser()]);
  return processSubmission(data, user);
}
```

Benefit: the skip path is instant, and the processing path still parallelises both fetches.

## When to Apply

- Any function with an early return or conditional branch that doesn't need all fetched data.
- Server Actions with validation that may reject before using remote data.
- API route handlers with auth/permission checks — check auth **before** fetching payload data.

## Back to

- [overview.md](overview.md)

## See Also

- [parallel.md](parallel.md) — once you move awaits into the right branch, parallelise them
- [api-routes.md](api-routes.md) — applying this pattern in Next.js API routes and Server Actions
