# Typography & Content

## Typography Rules

- Use ellipsis character `…` — not three dots `...`
- Use curly quotes `"` `"` — not straight quotes `"`
- Non-breaking spaces (`&nbsp;`) for:
  - Measurements: `10&nbsp;MB`
  - Keyboard shortcuts: `⌘&nbsp;K`
  - Brand names that shouldn't break
- Loading states end with `…` (e.g., `Loading…`)
- Number columns: `font-variant-numeric: tabular-nums` for alignment
- Headings: `text-wrap: balance` or `text-wrap: pretty` for better line breaks

## Content Overflow

- Text containers must handle overflow: use `truncate`, `line-clamp-*`, or `break-words`
- Flex children need `min-w-0` for text truncation to work
- Handle empty states explicitly — never show blank screens
- Anticipate short, average, and very long user-generated content

## Back to

- [Guidelines overview](overview.md)
- See also: [Copy standards](copy-standards.md) — writing style for UI text
