# Animation Standards

## Motion Preferences

- Always respect `prefers-reduced-motion` — disable or simplify animations when set
- Test with reduced motion enabled

## Performant Properties

- Animate only `transform` and `opacity` — these run on the compositor thread
- Never use `transition: all` — list properties explicitly (e.g., `transition: transform 200ms, opacity 200ms`)

## Transform Rules

- Set correct `transform-origin` for scaling/rotating elements
- SVG transforms: apply to `<g>` wrapper elements with `transform-box: fill-box`

## Interruptibility

- Animations must be interruptible — user actions should cancel or redirect in-progress animations
- Avoid animation locks that prevent user interaction during transitions

## Back to

- [Guidelines overview](overview.md)
