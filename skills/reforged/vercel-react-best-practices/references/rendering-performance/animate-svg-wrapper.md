# Rule: Wrap SVG in a `<div>` and Animate the Wrapper

**ID:** rendering-animate-svg-wrapper
**Category:** Rendering Performance (Priority 6 — MEDIUM)

## Explanation

Animating SVG elements directly with CSS `transform` does not trigger GPU compositing in most browsers. The SVG element stays on the main thread's paint layer, causing expensive repaints on every frame. Wrapping the SVG in a `<div>` and animating the wrapper allows the browser to promote the wrapper to its own compositor layer, enabling hardware-accelerated animations at 60 fps with no main-thread paint cost.

The `will-change: transform` hint on the wrapper tells the browser to create a dedicated GPU layer upfront, avoiding the initial jank of layer promotion mid-animation.

## Incorrect

```tsx
// Bad: animating the SVG element directly — no GPU compositing
function AnimatedIcon({ rotation }: { rotation: number }) {
  return (
    <svg
      width="24"
      height="24"
      viewBox="0 0 24 24"
      style={{
        transform: `rotate(${rotation}deg)`,
        transition: 'transform 0.3s ease',
      }}
    >
      <path d="M12 2L2 22h20L12 2z" fill="currentColor" />
    </svg>
  );
}
```

**Why this is wrong:** SVG elements are not eligible for compositor-layer promotion in most rendering engines. The `transform` is applied during the paint phase on the CPU, causing layout thrashing and dropped frames — especially noticeable when animating multiple icons simultaneously.

## Correct

```tsx
// Good: animate the wrapper div — gets GPU compositing
function AnimatedIcon({ rotation }: { rotation: number }) {
  return (
    <div
      style={{
        transform: `rotate(${rotation}deg)`,
        transition: 'transform 0.3s ease',
        willChange: 'transform',
        display: 'inline-block',
      }}
    >
      <svg width="24" height="24" viewBox="0 0 24 24">
        <path d="M12 2L2 22h20L12 2z" fill="currentColor" />
      </svg>
    </div>
  );
}
```

**Why this is correct:** The `<div>` wrapper is a standard HTML element that browsers can promote to a GPU compositor layer. The `will-change: transform` property ensures the layer is created before the animation starts. The SVG inside is rasterized once into the layer texture and the GPU handles the transform — zero main-thread paint cost per frame.

### CSS animation variant

```tsx
// Also good: CSS keyframe animation on the wrapper
function SpinnerIcon() {
  return (
    <div
      style={{
        animation: 'spin 1s linear infinite',
        willChange: 'transform',
        display: 'inline-block',
      }}
    >
      <svg width="24" height="24" viewBox="0 0 24 24">
        <circle
          cx="12" cy="12" r="10"
          stroke="currentColor"
          strokeWidth="2"
          fill="none"
          strokeDasharray="60 40"
        />
      </svg>
    </div>
  );
}
```

```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

## When to Apply

- Any SVG icon or illustration that is animated with CSS `transform`, `opacity`, or `filter`.
- Loading spinners, hover effects, scroll-triggered animations on SVG content.
- Particularly important when multiple SVGs animate simultaneously (e.g., a dashboard with animated charts).

## Back to

- [overview.md](overview.md)
