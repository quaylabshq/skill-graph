# Future Extensions

Planned capabilities that can extend this skill graph.

## Planned

### 1. CSS-Specific Guidelines
- **Type**: Reference
- **Purpose**: Dedicated CSS/Tailwind rules for spacing, color tokens, responsive breakpoints
- **Implementation**: Add `references/guidelines/css-patterns.md`, link from guidelines overview

### 2. Auto-Fix Script
- **Type**: Tool script
- **Purpose**: Automatically fix simple violations (add `aria-label`, replace `...` with `…`, add `width`/`height` to images)
- **Implementation**: Add `scripts/autofix.py`, link from SKILL.md

### 3. Framework-Specific Variants
- **Type**: Reference files
- **Purpose**: Specialized rules for Vue, Svelte, Angular (current focus is React/Next.js)
- **Implementation**: Add `references/guidelines/vue.md`, etc., link from guidelines overview

### 4. Design Token Audit
- **Type**: Reference + script
- **Purpose**: Audit design token usage for consistency (spacing, colors, typography scales)
- **Implementation**: Add `references/design-tokens.md` and `scripts/audit-tokens.py`

## Implementation Pattern

Each extension follows:
```
references/<name>.md    # Reference documentation
scripts/<name>.py       # Executable script (if needed)
```

Update SKILL.md index and relevant hub files when implementing.

## Back to

- [SKILL.md](../SKILL.md)
