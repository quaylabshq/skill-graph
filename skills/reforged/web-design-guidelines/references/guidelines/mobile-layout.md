# Mobile & Layout

## Touch Interactions

- Set `touch-action: manipulation` to remove 300ms tap delay
- Set `-webkit-tap-highlight-color` intentionally (transparent or branded)
- Apply `overscroll-behavior: contain` in modals and drawers to prevent background scroll
- Disable text selection during drag operations
- Use `autoFocus` sparingly — desktop only

## Safe Areas

- Full-bleed layouts must use `env(safe-area-inset-*)` for notched devices
- Bottom-fixed elements: add `padding-bottom: env(safe-area-inset-bottom)`

## Scroll & Overflow

- Prevent unwanted scrollbars — test at various viewport sizes
- Prefer CSS Flex/Grid over JavaScript measurement for layout
- Never set `user-scalable=no` or `maximum-scale=1` on viewport meta

## Back to

- [Guidelines overview](overview.md)
- See also: [Images & performance](images-performance.md) — layout shift prevention
