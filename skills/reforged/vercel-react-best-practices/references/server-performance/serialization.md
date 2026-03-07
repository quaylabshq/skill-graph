# Rule: Minimize Data Passed Across the Server/Client Boundary

**ID:** server-serialization
**Category:** Server-Side Performance (Priority 3 — HIGH)

## Explanation

When a Server Component renders a Client Component, every prop is serialized into the RSC payload and sent over the network. This payload is part of the initial HTML response and is also used during hydration. Passing large objects with fields the Client Component never uses wastes bandwidth, increases Time to First Byte (TTFB), and slows down hydration.

Treat the server/client boundary like an API response: only include the fields the consumer actually needs.

## Incorrect

```tsx
// app/page.tsx — Server Component
import { db } from "@/lib/db";
import { UserCard } from "@/components/UserCard";

export default async function Page() {
  const user = await db.user.findUnique({
    where: { id: userId },
    include: {
      posts: true,        // 50 posts with full content
      sessions: true,     // security-sensitive session data
      auditLog: true,     // hundreds of log entries
    },
  });

  // BAD: passes the ENTIRE user object (posts, sessions, audit log)
  // when UserCard only displays name and avatar
  return <UserCard user={user} />;
}
```

```tsx
// components/UserCard.tsx — Client Component
"use client";

// This component only uses 2 fields, but receives the entire object
export function UserCard({ user }: { user: FullUser }) {
  return (
    <div className="flex items-center gap-2">
      <img src={user.avatar} alt={user.name} className="rounded-full w-8 h-8" />
      <span>{user.name}</span>
    </div>
  );
}
```

Problems:
- Serializes hundreds of KB of unused data (posts, audit logs).
- Leaks sensitive data (sessions) to the client.
- Bloats the HTML document and RSC payload.

## Correct

```tsx
// app/page.tsx — Server Component
import { db } from "@/lib/db";
import { UserCard } from "@/components/UserCard";

export default async function Page() {
  // Option A: Query only what you need
  const user = await db.user.findUnique({
    where: { id: userId },
    select: { name: true, avatar: true },
  });

  return <UserCard name={user.name} avatar={user.avatar} />;
}
```

```tsx
// components/UserCard.tsx — Client Component
"use client";

type UserCardProps = {
  name: string;
  avatar: string;
};

export function UserCard({ name, avatar }: UserCardProps) {
  return (
    <div className="flex items-center gap-2">
      <img src={avatar} alt={name} className="rounded-full w-8 h-8" />
      <span>{name}</span>
    </div>
  );
}
```

## Pattern: Extracting a DTO at the Boundary

For complex pages with multiple Client Components, define a lightweight type for what crosses the boundary:

```tsx
// types/dto.ts
export type PostSummary = {
  id: string;
  title: string;
  excerpt: string;
  publishedAt: string;
};

// lib/queries.ts
import { cache } from "react";
import { db } from "@/lib/db";
import type { PostSummary } from "@/types/dto";

export const getPostSummaries = cache(async (): Promise<PostSummary[]> => {
  const posts = await db.post.findMany({
    select: {
      id: true,
      title: true,
      excerpt: true,
      publishedAt: true,
    },
    orderBy: { publishedAt: "desc" },
    take: 20,
  });
  return posts.map((p) => ({
    ...p,
    publishedAt: p.publishedAt.toISOString(), // Date -> string for serialization
  }));
});
```

## Checklist

- **Dates:** `Date` objects are not serializable. Convert to ISO strings on the server.
- **Circular references:** will crash serialization. Flatten or extract needed fields.
- **Functions/classes:** cannot cross the boundary. Extract plain data.
- **Sensitive fields:** passwords, tokens, internal IDs -- never send to the client.

## When to Apply

- Every Client Component that receives props from a Server Component.
- Server Action return values (the returned data is also serialized to the client).
- Any place where a database model with relations is passed directly as a prop.

## Back to

- [overview.md](overview.md)

## See Also

- [dedup-props.md](dedup-props.md) — avoid passing multiple derived copies of the same data
- [auth-actions.md](auth-actions.md) — be careful about what server actions return to the client
- [../rendering-performance/overview.md](../rendering-performance/overview.md) — smaller payloads lead to faster hydration
