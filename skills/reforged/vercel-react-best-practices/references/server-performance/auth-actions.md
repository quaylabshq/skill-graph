# Rule: Authenticate and Authorize Every Server Action

**ID:** server-auth-actions
**Category:** Server-Side Performance (Priority 3 — HIGH)

## Explanation

Server Actions are compiled into public HTTP endpoints. Any client -- including malicious ones -- can call them directly with arbitrary payloads. Never assume the caller is your own UI. Every Server Action must:

1. **Authenticate** the user (verify a valid session exists).
2. **Authorize** the operation (verify the user has permission to perform it).
3. **Validate inputs** with a schema library like zod before touching the database.

Skipping any of these steps exposes your application to unauthorized data access, privilege escalation, and injection attacks.

## Incorrect

```tsx
// actions/user.ts
"use server";

import { db } from "@/lib/db";

// DANGEROUS: no auth check, no authorization, no input validation.
// Anyone can call this endpoint with any user ID.
export async function deleteUser(id: string) {
  await db.user.delete({ where: { id } });
  return { success: true };
}

export async function updateProfile(userId: string, data: unknown) {
  // Trusts whatever the client sends — SQL injection, XSS, wrong types
  await db.user.update({ where: { id: userId }, data: data as any });
}
```

Problem: these actions are reachable as POST requests. An attacker can delete or modify any user by guessing IDs.

## Correct

```tsx
// actions/user.ts
"use server";

import { z } from "zod";
import { auth } from "@/lib/auth";
import { db } from "@/lib/db";
import { revalidatePath } from "next/cache";

const deleteUserSchema = z.object({
  userId: z.string().uuid(),
});

export async function deleteUser(input: z.infer<typeof deleteUserSchema>) {
  // 1. Authenticate — is the caller logged in?
  const session = await auth();
  if (!session?.user) {
    throw new Error("Unauthorized");
  }

  // 2. Validate — is the input well-formed?
  const { userId } = deleteUserSchema.parse(input);

  // 3. Authorize — does this user have permission?
  if (session.user.role !== "admin" && session.user.id !== userId) {
    throw new Error("Forbidden");
  }

  // 4. Perform the action
  await db.user.delete({ where: { id: userId } });
  revalidatePath("/admin/users");
  return { success: true };
}

const updateProfileSchema = z.object({
  name: z.string().min(1).max(100),
  bio: z.string().max(500).optional(),
});

export async function updateProfile(raw: z.infer<typeof updateProfileSchema>) {
  const session = await auth();
  if (!session?.user) {
    throw new Error("Unauthorized");
  }

  const data = updateProfileSchema.parse(raw);

  // Users can only update their own profile
  await db.user.update({
    where: { id: session.user.id },
    data,
  });

  revalidatePath(`/profile/${session.user.id}`);
  return { success: true };
}
```

## When to Apply

- Every Server Action without exception. There is no safe "internal only" action in a Next.js app.
- Form actions bound with `action={myServerAction}`.
- Actions called via `useActionState` or `startTransition`.
- Any mutation that writes to a database, external API, or filesystem.

## Back to

- [overview.md](overview.md)

## See Also

- [../async-waterfalls/defer-await.md](../async-waterfalls/defer-await.md) — check auth before fetching data to avoid unnecessary work
- [serialization.md](serialization.md) — minimize what you return from server actions to the client
