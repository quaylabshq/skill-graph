# Rule: Use `after()` for Non-Blocking Side Effects

**ID:** server-after-nonblocking
**Category:** Server-Side Performance (Priority 3 — HIGH)

## Explanation

Next.js provides the `after()` function (from `next/server`) to schedule work that runs **after** the response has been sent to the user. This is ideal for logging, analytics, cache warming, and other side effects that the user does not need to wait for.

Without `after()`, these operations block the response. A 50ms analytics call on every page load means every user waits an extra 50ms for no visible benefit. With `after()`, the response ships immediately, and the side effect runs in the background.

`after()` is available in Server Components, Server Actions, Route Handlers, and Middleware.

## Incorrect

```tsx
// app/api/checkout/route.ts
import { db } from "@/lib/db";
import { logAnalytics } from "@/lib/analytics";
import { sendWebhook } from "@/lib/webhooks";
import { invalidateCache } from "@/lib/cache";

export async function POST(request: Request) {
  const body = await request.json();

  // Process the order
  const order = await db.order.create({ data: body });

  // BAD: user waits for ALL of these before getting a response
  await logAnalytics("order_created", { orderId: order.id });  // 50ms
  await sendWebhook("order.created", order);                    // 200ms
  await invalidateCache(`user:${body.userId}:orders`);          // 30ms
  // Total blocking side effects: ~280ms added to response time

  return Response.json({ orderId: order.id });
}
```

Problem: the user waits an extra 280ms for operations they will never see the result of.

## Correct

```tsx
// app/api/checkout/route.ts
import { after } from "next/server";
import { db } from "@/lib/db";
import { logAnalytics } from "@/lib/analytics";
import { sendWebhook } from "@/lib/webhooks";
import { invalidateCache } from "@/lib/cache";

export async function POST(request: Request) {
  const body = await request.json();

  // Process the order — this is the only thing the user waits for
  const order = await db.order.create({ data: body });

  // Schedule side effects to run AFTER the response is sent
  after(async () => {
    await Promise.all([
      logAnalytics("order_created", { orderId: order.id }),
      sendWebhook("order.created", order),
      invalidateCache(`user:${body.userId}:orders`),
    ]);
  });

  // Response is sent immediately — user does not wait for side effects
  return Response.json({ orderId: order.id });
}
```

## In Server Components

```tsx
// app/products/[id]/page.tsx — Server Component
import { after } from "next/server";
import { db } from "@/lib/db";
import { trackPageView } from "@/lib/analytics";

export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const product = await db.product.findUnique({ where: { id } });

  // Track the page view after the response streams to the user
  after(() => {
    trackPageView({ page: `/products/${id}`, productId: id });
  });

  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <span>${product.price}</span>
    </div>
  );
}
```

## In Server Actions

```tsx
// actions/feedback.ts
"use server";

import { after } from "next/server";
import { db } from "@/lib/db";
import { notifySlack } from "@/lib/slack";

export async function submitFeedback(formData: FormData) {
  const message = formData.get("message") as string;

  const feedback = await db.feedback.create({
    data: { message },
  });

  // Notify the team on Slack without blocking the user
  after(() => {
    notifySlack(`New feedback received: "${message.slice(0, 100)}"`);
  });

  return { success: true, id: feedback.id };
}
```

## What Belongs in `after()`

| Good candidates              | Bad candidates (keep in main flow)      |
|------------------------------|------------------------------------------|
| Analytics / page view tracking | Database writes the user expects to see |
| Webhook notifications         | Validation that determines the response  |
| Logging and audit trails      | Auth checks                              |
| Cache warming / invalidation  | Data the response body depends on        |
| Sending emails / notifications| Error handling the user needs to see     |

## When to Apply

- Any `await` in a response path that does not affect what the user sees.
- Analytics and logging calls in route handlers.
- Webhook/notification dispatching after mutations.
- Cache invalidation after writes.
- Audit log entries.

## Back to

- [overview.md](overview.md)

## See Also

- [auth-actions.md](auth-actions.md) — auth checks must stay in the main flow, not in `after()`
- [../async-waterfalls/defer-await.md](../async-waterfalls/defer-await.md) — move awaits out of the critical path
- [../async-waterfalls/parallel.md](../async-waterfalls/parallel.md) — parallelize side effects within `after()` using `Promise.all()`
