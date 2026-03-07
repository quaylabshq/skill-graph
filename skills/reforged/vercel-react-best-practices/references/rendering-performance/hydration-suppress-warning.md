# Rule: Use `suppressHydrationWarning` for Known Server/Client Differences

**ID:** rendering-hydration-suppress-warning
**Category:** Rendering Performance (Priority 6 — MEDIUM)

## Explanation

React's hydration process compares the server-rendered HTML with the client-rendered output. When they differ, React logs a warning and re-renders the mismatched subtree, which is both noisy in the console and wasteful. However, some mismatches are **expected and intentional** — relative timestamps ("3 minutes ago"), random IDs, locale-formatted numbers, or values that depend on the client's timezone.

For these cases, apply `suppressHydrationWarning` on the specific element whose text content is expected to differ. React will skip the comparison for that element's direct text content, avoiding the warning and the unnecessary re-render.

**Important:** This prop only suppresses warnings for the element's own text content — it does not suppress warnings for child elements or attributes. Use it surgically on individual elements, never on large subtrees.

## Incorrect

```tsx
// Bad: hydration mismatch warning on every page load
function CommentTimestamp({ createdAt }: { createdAt: Date }) {
  // Server: "3 minutes ago" at render time
  // Client: "4 minutes ago" by the time hydration runs
  return (
    <time dateTime={createdAt.toISOString()}>
      {formatRelativeTime(createdAt)}
    </time>
  );
}
```

```tsx
// Bad: random ID causes mismatch
function FormField({ label }: { label: string }) {
  const id = `field-${Math.random().toString(36).slice(2)}`;

  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input id={id} type="text" />
    </div>
  );
}
```

```tsx
// Bad: locale-formatted number differs between server and client
function PriceDisplay({ amount }: { amount: number }) {
  // Server renders in en-US locale, client might be de-DE
  return (
    <span>
      {amount.toLocaleString(undefined, {
        style: 'currency',
        currency: 'USD',
      })}
    </span>
  );
}
```

**Why this is wrong:** Each of these produces a hydration mismatch warning in the console. React detects the difference, throws away the server-rendered DOM for that element, and re-renders it from scratch on the client — wasting the SSR work.

## Correct

```tsx
// Good: suppress the expected timestamp mismatch
function CommentTimestamp({ createdAt }: { createdAt: Date }) {
  return (
    <time dateTime={createdAt.toISOString()} suppressHydrationWarning>
      {formatRelativeTime(createdAt)}
    </time>
  );
}
```

```tsx
// Good: use React's useId for deterministic IDs (preferred solution)
import { useId } from 'react';

function FormField({ label }: { label: string }) {
  const id = useId();

  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input id={id} type="text" />
    </div>
  );
}
```

```tsx
// Good: suppress locale-dependent formatting mismatch
function PriceDisplay({ amount }: { amount: number }) {
  return (
    <span suppressHydrationWarning>
      {amount.toLocaleString(undefined, {
        style: 'currency',
        currency: 'USD',
      })}
    </span>
  );
}
```

**Why this is correct:**
- The `<time>` element uses `suppressHydrationWarning` because the relative time will naturally differ between server render time and client hydration time.
- The form field uses `useId()` instead of `Math.random()`, producing the same ID on server and client — no suppression needed.
- The price display suppresses the warning because `toLocaleString` can produce different output depending on the server and client locales.

### Multiple elements pattern

```tsx
// Good: suppress on each element that has a known mismatch
function UserProfile({ user }: { user: User }) {
  return (
    <div className="profile">
      <h2>{user.name}</h2> {/* No suppression — same on server and client */}

      <p suppressHydrationWarning>
        Joined {formatRelativeTime(user.createdAt)}
      </p>

      <p suppressHydrationWarning>
        Last active {formatRelativeTime(user.lastActiveAt)}
      </p>

      <p>
        {user.postCount} posts {/* No suppression — static number */}
      </p>
    </div>
  );
}
```

## When to Apply

- Relative timestamps ("5 minutes ago", "yesterday") that shift between server render and client hydration.
- `toLocaleString()` for numbers, dates, or currencies where the server locale may differ from the client locale.
- Content injected by synchronous `<script>` tags (see [hydration-no-flicker.md](hydration-no-flicker.md)) — apply to the element whose attributes the script modifies.
- **Do not use** as a blanket fix for hydration errors caused by bugs (conditional rendering based on `window`, missing data, etc.). Fix the root cause instead.
- **Do not apply** to parent containers — only apply to the specific leaf element with the expected mismatch.

## Back to

- [overview.md](overview.md)

## See Also

- [hydration-no-flicker.md](hydration-no-flicker.md) — preventing flicker with synchronous scripts
