# Rule: Extract Static JSX Outside Components as Module-Level Constants

**ID:** rendering-hoist-jsx
**Category:** Rendering Performance (Priority 6 — MEDIUM)

## Explanation

When static JSX (elements with no props or state dependencies) is defined inside a component body, React creates a brand-new element object on every render. While React's reconciler will see it as the same element and avoid DOM mutations, the object allocation and diffing still cost time — especially in components that render frequently or appear in large lists.

Hoisting static JSX to module-level constants means the element object is created once at module evaluation time. React sees the same reference across renders and can skip diffing entirely for that subtree.

## Incorrect

```tsx
// Bad: static JSX recreated on every render
function TableHeader() {
  return (
    <thead>
      <tr>
        <th>Name</th>
        <th>Email</th>
        <th>Role</th>
        <th>Status</th>
      </tr>
    </thead>
  );
}

function UserTable({ users }: { users: User[] }) {
  return (
    <table>
      <TableHeader />
      <tbody>
        {users.map((user) => (
          <tr key={user.id}>
            <td>{user.name}</td>
            <td>{user.email}</td>
            <td>{user.role}</td>
            <td>{user.status}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

```tsx
// Also bad: inline static elements inside a component
function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="layout">
      <div className="spacer" />          {/* recreated every render */}
      <hr className="divider" />           {/* recreated every render */}
      <div className="content">{children}</div>
      <div className="spacer" />          {/* recreated every render */}
    </div>
  );
}
```

**Why this is wrong:** Every render of `Layout` creates new element objects for the spacer `<div>` and `<hr>`. React must allocate memory and diff these elements even though they never change.

## Correct

```tsx
// Good: static JSX hoisted to module-level constants
const TABLE_HEADER = (
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Role</th>
      <th>Status</th>
    </tr>
  </thead>
);

function UserTable({ users }: { users: User[] }) {
  return (
    <table>
      {TABLE_HEADER}
      <tbody>
        {users.map((user) => (
          <tr key={user.id}>
            <td>{user.name}</td>
            <td>{user.email}</td>
            <td>{user.role}</td>
            <td>{user.status}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

```tsx
// Good: static decorative elements hoisted out
const SPACER = <div className="spacer" />;
const DIVIDER = <hr className="divider" />;

function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="layout">
      {SPACER}
      {DIVIDER}
      <div className="content">{children}</div>
      {SPACER}
    </div>
  );
}
```

**Why this is correct:** The constant JSX elements are created once when the module loads. React receives the same object reference on every render, recognizes nothing changed, and skips diffing the subtree. Zero allocation cost per render.

### Multiple static elements pattern

```tsx
// Good: group related static elements together
const EMPTY_STATE = (
  <div className="empty-state">
    <svg className="empty-icon" viewBox="0 0 24 24">
      <path d="M20 6H4V4h16v2zm0 4H4V8h16v2zm-4 4H4v-2h12v2z" />
    </svg>
    <h3>No items found</h3>
    <p>Try adjusting your search or filters.</p>
  </div>
);

const LOADING_SKELETON = (
  <div className="skeleton">
    <div className="skeleton-line skeleton-title" />
    <div className="skeleton-line skeleton-text" />
    <div className="skeleton-line skeleton-text short" />
  </div>
);

function ItemList({ items, isLoading }: { items: Item[]; isLoading: boolean }) {
  if (isLoading) return LOADING_SKELETON;
  if (items.length === 0) return EMPTY_STATE;

  return (
    <ul>
      {items.map((item) => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
}
```

## When to Apply

- Decorative elements: spacers, dividers, icons, background patterns.
- Static table headers, footers, and column definitions.
- Empty states, loading skeletons, and placeholder content with no dynamic data.
- **Do not hoist** elements that depend on props, state, context, or translated strings — those must remain inside the component.

## Back to

- [overview.md](overview.md)
