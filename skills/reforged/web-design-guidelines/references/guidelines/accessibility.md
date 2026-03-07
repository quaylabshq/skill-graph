# Accessibility & Focus Management

## Semantic HTML

- Use `<button>`, `<a>`, `<label>`, `<table>` instead of `<div>`/`<span>` with click handlers
- Semantic elements take precedence over ARIA — only add ARIA when no semantic equivalent exists

## ARIA

- Icon-only buttons require `aria-label`
- Form controls need `<label>` elements or `aria-label`
- Decorative icons: `aria-hidden="true"`
- Async status updates: `aria-live="polite"`
- Images require `alt` text; decorative images use `alt=""`

## Keyboard Navigation

- All interactive elements must support keyboard navigation via `onKeyDown`/`onKeyUp`
- Headings follow hierarchical structure `<h1>` through `<h6>`
- Provide skip links for long pages
- Anchors use `scroll-margin-top` for scroll offset

## Focus Indicators

- All interactive elements need visible focus indicators: `focus-visible:ring-*` or equivalent
- Never use `outline-none` without a replacement focus style
- Prefer `:focus-visible` over `:focus` to avoid focus rings on mouse clicks
- Use `:focus-within` for compound control groups (e.g., search bar with button)

## Back to

- [Guidelines overview](overview.md)
- See also: [Forms](forms.md) — form-specific accessibility rules
