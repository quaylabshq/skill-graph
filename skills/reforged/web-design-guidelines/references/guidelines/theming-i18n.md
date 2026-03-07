# Theming & Internationalization

## Dark Mode

- Apply `color-scheme: dark` on `<html>` element for dark mode
- Set `<meta name="theme-color">` to match page background color
- Explicitly style native `<select>` elements — they inherit OS styles inconsistently

## Internationalization

- Use `Intl.DateTimeFormat` for dates and times — never hardcode formats
- Use `Intl.NumberFormat` for numbers and currency
- Detect user language via `Accept-Language` header or `navigator.languages`
- Never hardcode date/number formats (e.g., `MM/DD/YYYY`, `1,000.00`)

## Back to

- [Guidelines overview](overview.md)
