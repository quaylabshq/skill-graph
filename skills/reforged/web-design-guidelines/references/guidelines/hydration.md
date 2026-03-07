# Hydration & Interactivity

## Hydration Safety

- Controlled inputs with `value` must have `onChange` handlers
- Prefer `defaultValue` for uncontrolled inputs to avoid hydration mismatches
- Guard date/time rendering that differs between server and client
- Minimize `suppressHydrationWarning` — fix the root cause instead

## Interactive States

- All buttons and links need `hover:` states
- Interactive state changes should increase contrast (not just color shift)
- Ensure hover/active/focus states are visually distinct

## Back to

- [Guidelines overview](overview.md)
- See also: [Forms](forms.md) — controlled vs uncontrolled input patterns
- See also: [Accessibility](accessibility.md) — focus indicators
