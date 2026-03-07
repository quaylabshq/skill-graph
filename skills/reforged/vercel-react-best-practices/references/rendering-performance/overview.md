# Rendering Performance (Priority 6 — MEDIUM)

Once a render happens, optimize what the browser actually paints: layout, compositing, hydration, and DOM operations.

## Rules

| Rule | Summary | Reference |
|------|---------|-----------|
| rendering-animate-svg-wrapper | Animate div wrapper, not SVG element directly | [animate-svg-wrapper.md](animate-svg-wrapper.md) |
| rendering-content-visibility | Use `content-visibility: auto` for long lists | [content-visibility.md](content-visibility.md) |
| rendering-hoist-jsx | Extract static JSX outside components | [hoist-jsx.md](hoist-jsx.md) |
| rendering-svg-precision | Reduce SVG coordinate precision | [svg-precision.md](svg-precision.md) |
| rendering-hydration-no-flicker | Use inline script for client-only data | [hydration-no-flicker.md](hydration-no-flicker.md) |
| rendering-hydration-suppress-warning | Suppress expected hydration mismatches | [hydration-suppress-warning.md](hydration-suppress-warning.md) |
| rendering-activity | Use `<Activity>` component for show/hide | [activity.md](activity.md) |
| rendering-conditional-render | Use ternary, not `&&` for conditionals | [conditional-render.md](conditional-render.md) |
| rendering-usetransition-loading | Prefer `useTransition` for loading states | [usetransition-loading.md](usetransition-loading.md) |

## Key Principle

**Help the browser skip work.** Use `content-visibility` to skip off-screen rendering, hoist static JSX to avoid re-creation, and handle hydration mismatches gracefully.

## Back to

- [SKILL.md](../../SKILL.md)

## See Also

- [Re-render optimization](../rerender-optimization/overview.md) — reducing how often renders happen
- [JS performance](../js-performance/overview.md) — optimizing the JavaScript that runs during renders
