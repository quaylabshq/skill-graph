# Form Design

## Input Attributes

- Always include `autocomplete` attribute with meaningful values
- Use meaningful `name` attributes
- Use semantic input types: `email`, `tel`, `url`, `number`
- Set appropriate `inputmode` for mobile keyboards
- Disable `spellcheck` on emails, codes, and usernames (`spellCheck={false}`)
- Use `autocomplete="off"` on non-authentication fields

## Labels & Hit Targets

- Labels must be clickable — use `htmlFor` or wrap the input in `<label>`
- Checkboxes and radios: label and control share a single hit target
- Placeholders end with `…` and show example patterns (e.g., `Search…`)

## Validation & Errors

- Display errors inline next to the field, not in a banner
- Focus on the first error after submission
- Error messages should describe the fix, not just the problem
- Warn before navigation with unsaved changes

## Submit Behavior

- Submit button stays enabled until request starts
- Show spinner during submission
- Never block paste on any input

## Uncontrolled Defaults

- Prefer `defaultValue` for uncontrolled inputs (better performance)
- Controlled inputs with `value` must have an `onChange` handler

## Back to

- [Guidelines overview](overview.md)
- See also: [Accessibility](accessibility.md) — ARIA labels for form controls
- See also: [Hydration](hydration.md) — controlled vs uncontrolled input hydration
