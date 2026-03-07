# Rule: Reduce SVG Coordinate Precision to 1 Decimal Place

**ID:** rendering-svg-precision
**Category:** Rendering Performance (Priority 6 — MEDIUM)

## Explanation

Design tools like Figma and Illustrator export SVG paths with 6–15 decimal places of precision (e.g., `M12.482917 3.291048`). Most screens have a device pixel ratio of 1–3, meaning sub-pixel differences beyond 1 decimal place are physically invisible. Excess precision inflates SVG file size by 20–60% and adds unnecessary path data the browser must parse, store in memory, and rasterize.

Use SVGO with `--precision=1` to automatically strip excess precision. For icons and UI illustrations, even `--precision=0` (integers only) is often visually identical.

## Incorrect

```tsx
// Bad: SVG exported from Figma with excessive precision
function Logo() {
  return (
    <svg width="48" height="48" viewBox="0 0 48 48">
      <path
        d="M24.000000 4.000000C12.954305 4.000000 4.000000 12.954305 4.000000 24.000000C4.000000 35.045695 12.954305 44.000000 24.000000 44.000000C35.045695 44.000000 44.000000 35.045695 44.000000 24.000000C44.000000 12.954305 35.045695 4.000000 24.000000 4.000000Z"
        fill="#0070F3"
      />
      <path
        d="M18.285714 15.428571L18.285714 32.571429L33.714286 24.000000L18.285714 15.428571Z"
        fill="white"
      />
    </svg>
  );
}
```

```tsx
// Bad: icon library with bloated paths
function CheckIcon() {
  return (
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
      <path
        d="M20.285156 6.714844L9.428571 17.571429L3.714844 11.857143"
        stroke="currentColor"
        strokeWidth="2.000000"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}
```

**Why this is wrong:** The extra decimal places add bytes to the SVG that are invisible to the user. In a page with 50 icons, this can add 5–15 KB of unnecessary path data the browser must parse.

## Correct

```tsx
// Good: precision reduced to 1 decimal place
function Logo() {
  return (
    <svg width="48" height="48" viewBox="0 0 48 48">
      <path
        d="M24 4C13 4 4 13 4 24s9 20 20 20 20-9 20-20S35 4 24 4Z"
        fill="#0070F3"
      />
      <path
        d="M18.3 15.4v17.2l15.4-8.6L18.3 15.4Z"
        fill="white"
      />
    </svg>
  );
}
```

```tsx
// Good: clean icon paths
function CheckIcon() {
  return (
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
      <path
        d="M20.3 6.7L9.4 17.6 3.7 11.9"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}
```

**Why this is correct:** Visually identical output with 30–50% smaller path data. The browser parses less data, uses less memory, and rasterizes faster.

### Automating with SVGO

```bash
# Optimize a single file
npx svgo --precision=1 --multipass icon.svg

# Optimize an entire directory
npx svgo --precision=1 --multipass -f ./public/icons/

# Preview changes without overwriting (dry run)
npx svgo --precision=1 --multipass --pretty icon.svg -o -
```

### SVGO config file (`svgo.config.js`)

```js
// svgo.config.js — drop into project root
module.exports = {
  multipass: true,
  plugins: [
    {
      name: 'preset-default',
      params: {
        overrides: {
          // Reduce coordinate precision to 1 decimal
          cleanupNumericValues: {
            floatPrecision: 1,
          },
          // Also reduce path precision
          convertPathData: {
            floatPrecision: 1,
          },
        },
      },
    },
    // Remove unnecessary attributes
    'removeXMLNS',
  ],
};
```

### CI integration

```jsonc
// package.json
{
  "scripts": {
    "optimize:svg": "svgo --precision=1 --multipass -f ./public/icons/ -f ./src/assets/",
    "lint:svg": "svgo --precision=1 --multipass --dry-run -f ./public/icons/ 2>&1 | grep -c 'unchanged' || echo 'Unoptimized SVGs found!'"
  }
}
```

## When to Apply

- All SVG icons and illustrations in the project, especially those exported from design tools.
- SVG files in `public/` or embedded as JSX components.
- Run SVGO as part of the build pipeline or as a pre-commit hook to catch unoptimized SVGs.
- **Exception:** precision-critical SVGs like data visualizations, maps, or technical diagrams may need 2–3 decimal places. Test visually after optimization.

## Back to

- [overview.md](overview.md)
