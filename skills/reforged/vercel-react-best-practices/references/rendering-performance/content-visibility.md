# Rule: Apply `content-visibility: auto` for Off-Screen Rendering Deferral

**ID:** rendering-content-visibility
**Category:** Rendering Performance (Priority 6 — MEDIUM)

## Explanation

`content-visibility: auto` tells the browser to skip layout, paint, and style calculations for elements that are off-screen. Combined with `contain-intrinsic-size`, the browser reserves the correct amount of space in the document flow without actually rendering the element's contents. When the element scrolls into view, the browser renders it just in time.

For long lists of 1,000+ items, this can deliver a 10x improvement in initial render time because the browser only does rendering work for the ~20 items visible in the viewport.

## Incorrect

```tsx
// Bad: all 1,000 items are fully rendered, laid out, and painted on mount
function ProductList({ products }: { products: Product[] }) {
  return (
    <div className="product-list">
      {products.map((product) => (
        <div key={product.id} className="product-item">
          <img src={product.image} alt={product.name} />
          <h3>{product.name}</h3>
          <p>{product.description}</p>
          <span className="price">${product.price}</span>
        </div>
      ))}
    </div>
  );
}
```

```css
/* No containment — browser must render all 1,000 items */
.product-item {
  padding: 16px;
  border-bottom: 1px solid #eee;
}
```

**Why this is wrong:** The browser computes styles, layout, and paint for all 1,000 items even though only ~10–20 are visible. Initial page render takes 500ms+ when it could take 50ms.

## Correct

```tsx
// Good: same component — the optimization is pure CSS
function ProductList({ products }: { products: Product[] }) {
  return (
    <div className="product-list">
      {products.map((product) => (
        <div key={product.id} className="product-item">
          <img src={product.image} alt={product.name} />
          <h3>{product.name}</h3>
          <p>{product.description}</p>
          <span className="price">${product.price}</span>
        </div>
      ))}
    </div>
  );
}
```

```css
/* content-visibility: auto skips rendering for off-screen items */
.product-item {
  content-visibility: auto;
  contain-intrinsic-size: 0 120px; /* estimated height of each item */
  padding: 16px;
  border-bottom: 1px solid #eee;
}
```

**Why this is correct:** Off-screen items are skipped entirely during layout and paint. The `contain-intrinsic-size: 0 120px` reserves 120px of vertical space per item so the scrollbar height is accurate. When an item scrolls into view, the browser renders it on demand.

### Tailwind CSS variant

```tsx
// Using Tailwind with arbitrary properties
function ProductList({ products }: { products: Product[] }) {
  return (
    <div className="space-y-0">
      {products.map((product) => (
        <div
          key={product.id}
          className="p-4 border-b border-gray-200 [content-visibility:auto] [contain-intrinsic-size:0_120px]"
        >
          <img src={product.image} alt={product.name} />
          <h3 className="font-semibold">{product.name}</h3>
          <p className="text-gray-600">{product.description}</p>
          <span className="text-lg font-bold">${product.price}</span>
        </div>
      ))}
    </div>
  );
}
```

### Choosing the intrinsic size

```css
/* For fixed-height items: use the exact height */
.fixed-row {
  content-visibility: auto;
  contain-intrinsic-size: 0 48px;
}

/* For variable-height items: use the average height */
.variable-card {
  content-visibility: auto;
  contain-intrinsic-size: 0 200px; /* average card height */
}

/* auto keyword lets the browser remember the real size after first render */
.smart-card {
  content-visibility: auto;
  contain-intrinsic-size: auto 0 200px; /* use 200px until measured, then cache */
}
```

## When to Apply

- Long lists or grids with 50+ items that extend well beyond the viewport.
- Comment threads, activity feeds, product catalogs, data tables.
- Dashboard pages with many card sections below the fold.
- **Not suitable** for items that need to be measured for virtualization — use `content-visibility` as a simpler alternative to virtualization when precise scroll position isn't critical.

## Back to

- [overview.md](overview.md)
