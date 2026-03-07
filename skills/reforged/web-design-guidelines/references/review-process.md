# Review Process

How to conduct a web interface guidelines review.

## Workflow

### When files are specified

1. Read all specified files/patterns
2. Load relevant guideline references based on file content (forms → [forms.md](guidelines/forms.md), images → [images-performance.md](guidelines/images-performance.md), etc.)
3. Check each file against all applicable rules
4. Check against [anti-patterns](anti-patterns.md)
5. Output findings using [output format](output-format.md)

### When no files are specified

Prompt the user: "Which files or patterns should I review? (e.g., `src/components/**/*.tsx`)"

## Which Guidelines to Load

Load guideline references selectively based on file content:

| File contains | Load |
|---------------|------|
| `<button>`, `<a>`, `aria-*`, `role=` | [accessibility.md](guidelines/accessibility.md) |
| `<input>`, `<form>`, `<select>`, `<textarea>` | [forms.md](guidelines/forms.md) |
| `transition`, `animation`, `@keyframes` | [animation.md](guidelines/animation.md) |
| Text content, `<h1>`–`<h6>`, `font-*` | [typography-content.md](guidelines/typography-content.md) |
| `<img>`, `loading=`, virtualization, `getBoundingClientRect` | [images-performance.md](guidelines/images-performance.md) |
| `<Link>`, `useRouter`, query params, URL state | [navigation-state.md](guidelines/navigation-state.md) |
| `touch-action`, `overscroll`, `safe-area` | [mobile-layout.md](guidelines/mobile-layout.md) |
| `color-scheme`, `theme-color`, `Intl.` | [theming-i18n.md](guidelines/theming-i18n.md) |
| `value=`, `defaultValue`, `suppressHydrationWarning` | [hydration.md](guidelines/hydration.md) |
| Button labels, headings, error messages | [copy-standards.md](guidelines/copy-standards.md) |

When in doubt, load all guidelines. Always check [anti-patterns](anti-patterns.md).

## Review Scope

- Review only the files provided — do not audit the entire project unless asked
- Focus on actionable findings — skip rules that don't apply to the given code
- Group findings by file for easy navigation

## Back to

- [SKILL.md](../SKILL.md)
- See also: [Output format](output-format.md)
