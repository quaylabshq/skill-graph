# Rule: Cache localStorage/sessionStorage/Cookie Reads

**ID:** js-cache-storage
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

`localStorage.getItem()`, `sessionStorage.getItem()`, and `document.cookie` are **synchronous** operations that block the main thread. `localStorage` and `sessionStorage` require a round-trip to the browser's storage backend (often disk I/O), and `document.cookie` parses the entire cookie string on every access. In hot code paths — event handlers, render loops, or frequent polling — these reads add measurable latency.

Cache the values in an in-memory `Map` and invalidate on `storage` events (for cross-tab changes) and `visibilitychange` (for stale tabs returning to focus).

## Incorrect

```ts
// BAD: reading localStorage on every call — synchronous and slow
function getTheme(): string {
  return localStorage.getItem("theme") ?? "light";
}

function getUserPreferences(): Record<string, string> {
  return {
    theme: localStorage.getItem("theme") ?? "light",
    locale: localStorage.getItem("locale") ?? "en",
    fontSize: localStorage.getItem("fontSize") ?? "14",
  };
}

// Called on every render of every themed component
function ThemedButton({ label }: { label: string }) {
  const theme = getTheme(); // synchronous disk read on every render
  return <button className={`btn-${theme}`}>{label}</button>;
}
```

Problem: if 50 themed components render on a page, that's 50 synchronous `localStorage` reads per render cycle. Each read can take 0.5-2ms, adding up to 25-100ms of blocking time.

## Correct

```ts
// GOOD: in-memory cache with invalidation
const storageCache = new Map<string, string | null>();

function getCached(key: string): string | null {
  if (storageCache.has(key)) {
    return storageCache.get(key)!;
  }

  const value = localStorage.getItem(key);
  storageCache.set(key, value);
  return value;
}

function setCached(key: string, value: string): void {
  localStorage.setItem(key, value);
  storageCache.set(key, value);
}

function removeCached(key: string): void {
  localStorage.removeItem(key);
  storageCache.set(key, null);
}

// Invalidate cache when another tab changes storage
if (typeof window !== "undefined") {
  window.addEventListener("storage", (event) => {
    if (event.key === null) {
      // storage.clear() was called
      storageCache.clear();
    } else {
      storageCache.set(event.key, event.newValue);
    }
  });

  // Invalidate when tab regains focus (values may be stale)
  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "visible") {
      storageCache.clear();
    }
  });
}

// Now all reads are O(1) in-memory lookups after the first access
function getTheme(): string {
  return getCached("theme") ?? "light";
}

function ThemedButton({ label }: { label: string }) {
  const theme = getTheme(); // in-memory Map lookup — instant
  return <button className={`btn-${theme}`}>{label}</button>;
}
```

Benefit: the first read hits `localStorage`, but all subsequent reads are instant `Map.get()` lookups. Cross-tab changes and tab switches correctly invalidate the cache.

## When to Apply

- Any value read from `localStorage`/`sessionStorage` more than once per page lifecycle.
- Components that read storage values during render (especially in lists).
- `document.cookie` reads in authentication checks or feature flag evaluations.

## Back to

- [overview.md](overview.md)

## See Also

- [cache-function-results.md](cache-function-results.md) — same caching pattern for function outputs
- [cache-property-access.md](cache-property-access.md) — caching object property reads
