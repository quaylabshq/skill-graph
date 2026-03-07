# Rule: Check Array Length Before Expensive Operations

**ID:** js-length-check-first
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

Before performing expensive operations like sorting, deep equality comparison, or serialization on two arrays, check their lengths first. If the lengths differ, the arrays cannot be equal — you can skip the expensive comparison entirely. This is an O(1) check that can save O(n log n) or O(n) work.

The same principle applies to any operation where a cheap precondition check can rule out the need for an expensive computation.

## Incorrect

```ts
// BAD: always performs deep equality check, even when lengths differ
function arraysEqual<T>(a: T[], b: T[]): boolean {
  return JSON.stringify(a) === JSON.stringify(b);
}

// BAD: sorts both arrays before comparing, ignoring obvious mismatches
function hasSameElements(a: number[], b: number[]): boolean {
  const sortedA = [...a].sort((x, y) => x - y);
  const sortedB = [...b].sort((x, y) => x - y);
  return sortedA.every((val, i) => val === sortedB[i]);
}

// Called in a useEffect dependency check — runs on every render
function useDataSync(localItems: string[], remoteItems: string[]) {
  useEffect(() => {
    if (!arraysEqual(localItems, remoteItems)) {
      syncToServer(localItems);
    }
  }, [localItems, remoteItems]);
}
```

Problem: `JSON.stringify` on two 10,000-element arrays costs O(n) serialization time even when one array has 10,000 items and the other has 5. The sort-based comparison does O(n log n) work needlessly.

## Correct

```ts
// GOOD: length check first, then element-wise comparison
function arraysEqual<T>(a: T[], b: T[]): boolean {
  if (a.length !== b.length) {
    return false; // O(1) — skip everything
  }

  // Same reference — skip comparison entirely
  if (a === b) {
    return true;
  }

  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) {
      return false; // early exit on first mismatch
    }
  }

  return true;
}

// GOOD: length check before sorting
function hasSameElements(a: number[], b: number[]): boolean {
  if (a.length !== b.length) {
    return false; // different lengths = different elements
  }

  const sortedA = [...a].sort((x, y) => x - y);
  const sortedB = [...b].sort((x, y) => x - y);
  return sortedA.every((val, i) => val === sortedB[i]);
}

// Now the common case (different lengths) is instant
function useDataSync(localItems: string[], remoteItems: string[]) {
  useEffect(() => {
    if (!arraysEqual(localItems, remoteItems)) {
      syncToServer(localItems);
    }
  }, [localItems, remoteItems]);
}
```

Benefit: the length check is O(1) and catches many inequality cases immediately, completely avoiding the expensive O(n) or O(n log n) comparison that follows.

## When to Apply

- Any equality comparison between arrays or objects (deep equals, set comparison).
- Before sorting two arrays for comparison.
- Before serializing arrays for hashing or deduplication.
- Custom React hooks that compare arrays in dependency checks.

## Back to

- [overview.md](overview.md)

## See Also

- [early-exit.md](early-exit.md) — the general pattern of returning early to skip work
- [combine-iterations.md](combine-iterations.md) — reducing total work in array processing
