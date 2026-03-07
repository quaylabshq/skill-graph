# Rule: Return Early to Skip Unnecessary Processing

**ID:** js-early-exit
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

When a function can determine its result early — empty input, invalid arguments, cached value, feature flag off — return immediately instead of flowing through the entire function body. Guard clauses at the top of a function eliminate unnecessary computation and flatten deeply nested conditional logic.

Early exits improve both performance (skipping work) and readability (reducing nesting depth). The most common cases should exit first.

## Incorrect

```ts
interface User {
  id: string;
  name: string;
  email: string;
  role: "admin" | "editor" | "viewer";
}

// BAD: deeply nested conditionals, no early exits
function processUserPermissions(
  user: User | null,
  resource: string,
  permissions: Map<string, Set<string>>
): { allowed: boolean; reason: string } {
  let result = { allowed: false, reason: "" };

  if (user !== null) {
    if (user.role !== "viewer") {
      const userPerms = permissions.get(user.id);
      if (userPerms !== undefined) {
        if (userPerms.has(resource)) {
          // Deep in the nesting — the actual logic
          result = { allowed: true, reason: "granted" };
        } else {
          result = { allowed: false, reason: "no access to resource" };
        }
      } else {
        result = { allowed: false, reason: "no permissions found" };
      }
    } else {
      result = { allowed: false, reason: "viewers cannot modify" };
    }
  } else {
    result = { allowed: false, reason: "not authenticated" };
  }

  return result;
}
```

Problem: the function nests 4 levels deep. Every invocation executes the full conditional tree. Reading and maintaining this code requires tracking multiple nesting levels.

## Correct

```ts
interface User {
  id: string;
  name: string;
  email: string;
  role: "admin" | "editor" | "viewer";
}

// GOOD: guard clauses with early returns — flat and fast
function processUserPermissions(
  user: User | null,
  resource: string,
  permissions: Map<string, Set<string>>
): { allowed: boolean; reason: string } {
  if (user === null) {
    return { allowed: false, reason: "not authenticated" };
  }

  if (user.role === "viewer") {
    return { allowed: false, reason: "viewers cannot modify" };
  }

  const userPerms = permissions.get(user.id);
  if (userPerms === undefined) {
    return { allowed: false, reason: "no permissions found" };
  }

  if (!userPerms.has(resource)) {
    return { allowed: false, reason: "no access to resource" };
  }

  return { allowed: true, reason: "granted" };
}
```

Benefit: each check that fails exits immediately — no wasted work. The function reads top-to-bottom with zero nesting. The most common rejection cases (not authenticated, viewer role) are checked first and exit fastest.

### Early exit in loops

```ts
// GOOD: break/continue to skip unnecessary iterations
function findFirstMatch(
  items: { id: string; tags: string[] }[],
  targetTag: string
): string | null {
  for (const item of items) {
    // Skip items with no tags — avoid unnecessary .includes()
    if (item.tags.length === 0) {
      continue;
    }

    if (item.tags.includes(targetTag)) {
      return item.id; // Found it — stop searching
    }
  }

  return null;
}
```

## When to Apply

- Functions with null/undefined checks — guard at the top.
- Permission/validation logic — reject invalid cases first.
- Search functions — return as soon as the target is found.
- Any function with 3+ levels of nesting that can be flattened with early returns.

## Back to

- [overview.md](overview.md)

## See Also

- [length-check-first.md](length-check-first.md) — a specific case of early exit for array comparisons
- [combine-iterations.md](combine-iterations.md) — using `continue` to skip items in combined loops
