# Rule: Cache Deep Property Lookups Before Loops

**ID:** js-cache-property-access
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

Accessing a deeply nested property like `obj.config.settings.value` requires the JavaScript engine to traverse the prototype chain and dereference multiple objects on every access. Inside a loop that runs thousands of iterations, this adds measurable overhead. Caching the value in a local variable before the loop gives the engine a direct reference, avoiding repeated traversal.

This also improves readability — a descriptive local variable name is clearer than a long property chain repeated throughout the loop body.

## Incorrect

```ts
interface AppConfig {
  config: {
    settings: {
      threshold: number;
      multiplier: number;
      precision: number;
    };
  };
}

// BAD: deep property access repeated on every iteration
function processItems(items: number[], app: AppConfig) {
  const results: number[] = [];

  for (let i = 0; i < items.length; i++) {
    // 3 property lookups × N iterations
    if (items[i] > app.config.settings.threshold) {
      results.push(
        items[i] * app.config.settings.multiplier
      );
    }
  }

  return results;
}
```

Problem: `app.config.settings.threshold` and `app.config.settings.multiplier` are dereferenced on every iteration. With 10,000 items, that's 30,000+ property lookups that could be 2.

## Correct

```ts
interface AppConfig {
  config: {
    settings: {
      threshold: number;
      multiplier: number;
      precision: number;
    };
  };
}

// GOOD: cache property values before the loop
function processItems(items: number[], app: AppConfig) {
  const { threshold, multiplier } = app.config.settings;
  const results: number[] = [];

  for (let i = 0; i < items.length; i++) {
    if (items[i] > threshold) {
      results.push(items[i] * multiplier);
    }
  }

  return results;
}
```

Benefit: the property chain is traversed once before the loop. Inside the loop, `threshold` and `multiplier` are simple local variable reads — the fastest possible access pattern in JavaScript.

## When to Apply

- Any loop body that references the same nested property (`a.b.c`) more than once.
- Hot paths in data transformation, validation, or rendering logic.
- When the object reference is stable during the loop (i.e., the property won't change mid-iteration).

## Back to

- [overview.md](overview.md)

## See Also

- [cache-function-results.md](cache-function-results.md) — caching computed results across calls
- [combine-iterations.md](combine-iterations.md) — reducing total loop iterations
