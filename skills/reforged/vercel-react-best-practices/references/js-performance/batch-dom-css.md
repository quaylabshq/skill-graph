# Rule: Batch DOM Writes and Use CSS Classes Over Inline Styles

**ID:** js-batch-dom-css
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

Interleaving style writes with layout reads causes **layout thrashing** — the browser is forced to recalculate layout synchronously on every read after a write, instead of batching layout work at the end of the frame. Each forced reflow can take 5-20ms, and in a loop this quickly adds up to dropped frames.

The rule is: **batch all writes first, then do all reads.** Additionally, prefer toggling CSS classes over setting inline styles. Class changes are batched by the browser into a single style recalculation, while individual `style.*` assignments can each trigger a reflow when followed by a layout read.

## Incorrect

```ts
// BAD: read → write → read → write causes layout thrashing
function updateCards(cards: HTMLElement[]) {
  cards.forEach((card) => {
    const height = card.offsetHeight;           // READ (forces layout)
    card.style.marginTop = `${height * 0.5}px`; // WRITE (invalidates layout)
    const width = card.offsetWidth;             // READ (forces layout AGAIN)
    card.style.paddingLeft = `${width * 0.1}px`; // WRITE (invalidates layout)
  });
}

// BAD: setting multiple inline styles individually
function highlight(el: HTMLElement) {
  el.style.backgroundColor = "yellow";
  el.style.border = "2px solid orange";
  el.style.borderRadius = "4px";
  el.style.padding = "8px";
}
```

Problem: each `offsetHeight`/`offsetWidth` read after a style write forces the browser to synchronously recalculate layout. In a loop of 100 cards, this causes 200 forced reflows instead of 1.

## Correct

```ts
// GOOD: batch all reads, then batch all writes
function updateCards(cards: HTMLElement[]) {
  // Phase 1 — READ all measurements
  const measurements = cards.map((card) => ({
    height: card.offsetHeight,
    width: card.offsetWidth,
  }));

  // Phase 2 — WRITE all mutations (single reflow at end of frame)
  cards.forEach((card, i) => {
    card.style.marginTop = `${measurements[i].height * 0.5}px`;
    card.style.paddingLeft = `${measurements[i].width * 0.1}px`;
  });
}

// GOOD: toggle a CSS class instead of multiple inline styles
function highlight(el: HTMLElement) {
  el.classList.add("highlighted");
}

// In your CSS:
// .highlighted {
//   background-color: yellow;
//   border: 2px solid orange;
//   border-radius: 4px;
//   padding: 8px;
// }
```

Benefit: the browser performs a single layout recalculation after all writes are done, and CSS class toggling batches all visual changes into one style recalc.

## When to Apply

- Any code that reads layout properties (`offsetHeight`, `offsetWidth`, `getBoundingClientRect()`, `scrollTop`, etc.) and writes styles in the same loop.
- Animation or resize handlers that update multiple elements.
- Components that apply multiple inline style changes — prefer a CSS class.

## Back to

- [overview.md](overview.md)

## See Also

- [cache-property-access.md](cache-property-access.md) — caching repeated property reads
