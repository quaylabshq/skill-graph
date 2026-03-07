# Rule: Start Promises Early, Await Late in API Routes and Server Actions

**ID:** async-api-routes
**Category:** Eliminating Waterfalls (Priority 1 — CRITICAL)

## Explanation

In Next.js API route handlers and Server Actions, start all independent async operations **immediately** — even before you `await` any of them. A promise begins executing the moment you call the function, not when you `await` it. By separating promise creation from awaiting, you get parallelism without restructuring your logic.

Pattern: **fire first, await together.**

## Incorrect

```tsx
// app/api/dashboard/route.ts
import { NextResponse } from "next/server";
import { auth } from "@/lib/auth";
import { db } from "@/lib/db";

export async function GET() {
  // Sequential: each line blocks until the previous resolves
  const session = await auth();                    // 100ms
  const config = await fetchConfig();              // 60ms
  const stats = await db.stats.getOverview();      // 130ms
  const announcements = await fetchAnnouncements(); // 50ms
  // Total: ~340ms

  return NextResponse.json({ session, config, stats, announcements });
}
```

## Correct

```tsx
// app/api/dashboard/route.ts
import { NextResponse } from "next/server";
import { auth } from "@/lib/auth";
import { db } from "@/lib/db";

export async function GET() {
  // Fire all independent promises immediately
  const sessionP = auth();
  const configP = fetchConfig();
  const statsP = db.stats.getOverview();
  const announcementsP = fetchAnnouncements();

  // Await them all together
  const [session, config, stats, announcements] = await Promise.all([
    sessionP,
    configP,
    statsP,
    announcementsP,
  ]);
  // Total: ~130ms (the slowest fetch)

  return NextResponse.json({ session, config, stats, announcements });
}
```

## Server Action Example

```tsx
"use server";

// Incorrect — sequential
export async function submitFeedback(formData: FormData) {
  const session = await auth();
  const rateLimit = await checkRateLimit(session.userId);
  if (!rateLimit.allowed) throw new Error("Rate limited");

  await saveFeedback(session.userId, formData.get("message") as string);
  const updatedCount = await getFeedbackCount(session.userId);
  return { success: true, totalFeedback: updatedCount };
}

// Correct — parallelise where possible, defer where conditional
export async function submitFeedback(formData: FormData) {
  const session = await auth(); // must resolve before rateLimit check

  const rateLimit = await checkRateLimit(session.userId);
  if (!rateLimit.allowed) throw new Error("Rate limited");

  // These two are independent of each other — parallelise
  const [, updatedCount] = await Promise.all([
    saveFeedback(session.userId, formData.get("message") as string),
    getFeedbackCount(session.userId),
  ]);

  return { success: true, totalFeedback: updatedCount };
}
```

## Key Insight

Calling an async function **returns a promise immediately** and starts the work. `await` only pauses your code until the promise settles. So this:

```tsx
const p = fetchData(); // work starts NOW
// ... other synchronous or async work ...
const data = await p;  // only blocks here if not yet resolved
```

is faster than this:

```tsx
const data = await fetchData(); // work starts AND blocks
```

whenever there is other work you could do in between.

## When to Apply

- Every API route handler (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`).
- Every Server Action (`"use server"` functions).
- Middleware that performs multiple checks (auth, feature flags, geo-lookup).

## Back to

- [overview.md](overview.md)

## See Also

- [parallel.md](parallel.md) — the general `Promise.all()` pattern this builds on
- [defer-await.md](defer-await.md) — skip fetches entirely when a branch doesn't need them
- [dependencies.md](dependencies.md) — when some of your API route fetches depend on each other
