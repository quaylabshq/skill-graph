# Images & Performance

## Image Optimization

- `<img>` tags require explicit `width` and `height` to prevent layout shift
- Below-fold images: `loading="lazy"`
- Above-fold critical images: `priority` (Next.js) or `fetchpriority="high"`
- All images require `alt` text (decorative images: `alt=""`)

## Virtualization

- Lists exceeding ~50 items must be virtualized — use `virtua`, `react-window`, or `content-visibility: auto`
- Unvirtualized large arrays are a flaggable anti-pattern

## DOM Performance

- Avoid layout reads in render: `getBoundingClientRect`, `offsetHeight`, `offsetWidth`, `scrollTop`
- Batch DOM operations — don't interleave reads and writes
- Prefer uncontrolled inputs for performance-sensitive forms

## Resource Loading

- Add `<link rel="preconnect">` for CDN and asset domains
- Critical fonts: `<link rel="preload" as="font">` with `font-display: swap`
- Prefer Flex/Grid layouts over JavaScript measurement for positioning

## Back to

- [Guidelines overview](overview.md)
- See also: [Animation](animation.md) — animate only compositor properties
