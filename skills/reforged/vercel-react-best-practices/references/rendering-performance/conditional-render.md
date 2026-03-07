# Rule: Use Ternary Operator, Not `&&` for Conditional Rendering

**ID:** rendering-conditional-render
**Category:** Rendering Performance (Priority 6 — MEDIUM)

## Explanation

The `&&` operator in JavaScript returns the first falsy value it encounters, or the last value if all are truthy. When used for conditional rendering in JSX, this creates a subtle bug: if the left-hand side is the number `0` (which is falsy), React renders the literal text `"0"` to the DOM instead of rendering nothing.

This is because React renders `0` as a valid text node — it is a number, and React displays numbers. The `&&` operator short-circuits and returns `0`, which JSX faithfully renders.

Always use explicit ternary expressions (`condition ? <Component /> : null`) or cast the condition to a boolean (`!!condition && <Component />`). The ternary approach is preferred because it is explicit about both branches and prevents this entire class of bugs.

## Incorrect

```tsx
// Bad: renders "0" as visible text when count is 0
function NotificationBadge({ count }: { count: number }) {
  return (
    <div className="header">
      <BellIcon />
      {count && <span className="badge">{count}</span>}
    </div>
  );
}
// When count = 0, renders: <div class="header"><BellIcon />0</div>
// The user sees a stray "0" next to the bell icon
```

```tsx
// Bad: renders "0" when array is empty
function ItemList({ items }: { items: Item[] }) {
  return (
    <div>
      <h2>Your Items</h2>
      {items.length && (
        <ul>
          {items.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
// When items = [], renders: <div><h2>Your Items</h2>0</div>
```

```tsx
// Bad: renders empty string "" (invisible but still a DOM text node)
function Greeting({ name }: { name: string }) {
  return (
    <div>
      {name && <h1>Hello, {name}!</h1>}
    </div>
  );
}
// When name = "", renders nothing visible — but "" is falsy so it
// "works" by accident. If name is ever 0 (from a type error), it breaks.
```

**Why this is wrong:** The `&&` operator does not return `true` or `false` — it returns the actual value. When that value is `0`, `NaN`, or `""`, React renders it (or in the case of `""`, creates an empty text node). This produces visible bugs with numeric conditions.

## Correct

```tsx
// Good: explicit ternary — renders null when count is 0
function NotificationBadge({ count }: { count: number }) {
  return (
    <div className="header">
      <BellIcon />
      {count > 0 ? <span className="badge">{count}</span> : null}
    </div>
  );
}
// When count = 0, renders: <div class="header"><BellIcon /></div>
```

```tsx
// Good: explicit length check with ternary
function ItemList({ items }: { items: Item[] }) {
  return (
    <div>
      <h2>Your Items</h2>
      {items.length > 0 ? (
        <ul>
          {items.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      ) : null}
    </div>
  );
}
```

```tsx
// Also acceptable: cast to boolean with !!
function NotificationBadge({ count }: { count: number }) {
  return (
    <div className="header">
      <BellIcon />
      {!!count && <span className="badge">{count}</span>}
    </div>
  );
}
// !!0 === false, so React renders nothing
```

```tsx
// Good: Boolean() conversion
function ItemList({ items }: { items: Item[] }) {
  return (
    <div>
      <h2>Your Items</h2>
      {Boolean(items.length) && (
        <ul>
          {items.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

**Why this is correct:** The ternary operator always evaluates to either the component or `null`. React renders nothing for `null`. There is no risk of accidentally rendering `0` or any other falsy value as text.

### Comparison table

```tsx
// Summary of behaviors:
//
// Expression                  | count=0 renders | count=5 renders
// ----------------------------|-----------------|----------------
// count && <Badge />          | "0" (BUG)       | <Badge />
// count > 0 && <Badge />      | nothing         | <Badge />
// !!count && <Badge />        | nothing         | <Badge />
// count > 0 ? <Badge /> : null| nothing         | <Badge />  ← PREFERRED
```

## When to Apply

- **Always** when the left-hand side of `&&` could be a number (count, length, index, amount).
- As a general habit, prefer ternary for all conditional rendering — it makes both branches explicit and prevents surprises.
- ESLint rule `@typescript-eslint/strict-boolean-expressions` can catch this automatically.

## Back to

- [overview.md](overview.md)
