# Output Format

How to format review findings.

## Format

Group findings by file. Use `file:line` format (VS Code clickable links).

```
src/components/Button.tsx:12 — Icon button missing `aria-label`
src/components/Button.tsx:24 — `transition: all` → list properties explicitly
src/components/Form.tsx:8 — Input missing `autocomplete` attribute
src/components/Form.tsx:15 — Label not linked via `htmlFor`

✓ src/components/Header.tsx — pass
```

## Rules

- State the issue concisely on one line
- Skip explanation unless the fix is non-obvious
- Include the fix inline with `→` when it's a simple change
- Mark files with no issues as `✓ <file> — pass`
- Order findings by file, then by line number within each file

## Severity Indicators (optional)

When the user requests severity levels:

| Prefix | Meaning |
|--------|---------|
| (none) | Standard finding |
| `⚠` | Accessibility violation or performance issue |
| `💡` | Suggestion / nice-to-have |

Default: no severity prefixes unless requested.

## Back to

- [SKILL.md](../SKILL.md)
- See also: [Review process](review-process.md)
