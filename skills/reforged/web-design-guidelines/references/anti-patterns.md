# Anti-Patterns to Flag

Quick-scan checklist. If any of these patterns appear in code, flag them immediately.

## Always Flag

| Pattern | Issue | Fix |
|---------|-------|-----|
| `user-scalable=no` | Blocks pinch-to-zoom accessibility | Remove from viewport meta |
| `maximum-scale=1` | Blocks zoom accessibility | Remove from viewport meta |
| `onPaste` + `preventDefault` | Blocks paste on inputs | Remove paste prevention |
| `transition: all` | Triggers layout on every property | List properties explicitly |
| `outline-none` / `outline: none` without replacement | Removes focus indicator | Add `focus-visible:ring-*` or equivalent |
| `<div onClick>` / `<span onClick>` for navigation | Not a semantic link | Use `<a>` / `<Link>` |
| `<div onClick>` / `<span onClick>` for actions | Not a semantic button | Use `<button>` |
| `<img>` without `width`/`height` | Causes layout shift | Add explicit dimensions |
| Large array rendered without virtualization | Performance bottleneck | Use `virtua`, `react-window`, or `content-visibility: auto` |
| `<input>` without label or `aria-label` | Inaccessible | Add `<label>` or `aria-label` |
| Icon button without `aria-label` | Inaccessible | Add `aria-label` describing the action |
| Hardcoded date format (e.g., `MM/DD/YYYY`) | i18n violation | Use `Intl.DateTimeFormat` |
| Hardcoded number format | i18n violation | Use `Intl.NumberFormat` |
| `autoFocus` without justification | Disrupts mobile UX | Remove or restrict to desktop |
| `suppressHydrationWarning` | Masks hydration bug | Fix the root cause |
| `getBoundingClientRect` in render | Layout thrashing | Move to `useEffect` or `useLayoutEffect` |
| Three dots `...` instead of `…` | Typography | Use ellipsis character `…` |
| Straight quotes `"` in UI text | Typography | Use curly quotes `"` `"` |

## Back to

- [SKILL.md](../SKILL.md)
- See also: [Guidelines overview](guidelines/overview.md) — detailed rules by category
