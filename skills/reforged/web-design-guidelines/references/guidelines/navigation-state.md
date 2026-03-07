# Navigation & State Management

## URL State

- URLs should reflect application state: filters, tabs, pagination, expanded panels
- Use query parameters for stateful UI
- Deep-link stateful UI using `nuqs` or similar URL state libraries
- Preserve URL state across navigation

## Link Behavior

- Use `<a>` / `<Link>` for navigation — never `<div onClick>` for link-like behavior
- Links must support standard browser behavior: middle-click, cmd/ctrl-click, right-click context menu

## Destructive Actions

- Require confirmation dialog OR provide undo window for destructive actions
- Never execute destructive operations on a single click without recovery path

## Back to

- [Guidelines overview](overview.md)
- See also: [Accessibility](accessibility.md) — semantic `<a>` vs `<div>` click handlers
