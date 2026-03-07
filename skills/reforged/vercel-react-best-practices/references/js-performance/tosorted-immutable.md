# Rule: Use `.toSorted()` for Immutable Sorting

**ID:** js-tosorted-immutable
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

`Array.prototype.sort()` mutates the original array in place. In React, mutating state directly breaks change detection — React compares object references to decide whether to re-render, so a mutated array with the same reference is treated as unchanged. This leads to stale UI, skipped renders, and subtle bugs.

`.toSorted()` (ES2023) returns a **new sorted array** without modifying the original, making it safe for React state and any context where immutability is required. It's supported in Chrome 110+, Safari 16+, Firefox 115+, and Node.js 20+.

Other immutable array methods in the same ES2023 family: `.toReversed()`, `.toSpliced()`, and `.with()`.

## Incorrect

```tsx
import { useState } from "react";

interface Task {
  id: string;
  title: string;
  priority: number;
  createdAt: Date;
}

// BAD: .sort() mutates the state array — React won't detect the change
function TaskList({ initialTasks }: { initialTasks: Task[] }) {
  const [tasks, setTasks] = useState(initialTasks);

  function sortByPriority() {
    // This mutates `tasks` in place and sets the SAME reference
    tasks.sort((a, b) => a.priority - b.priority);
    setTasks(tasks); // React sees same reference — NO re-render!
  }

  // BAD: spread + sort works but creates an intermediate copy
  function sortByDate() {
    const sorted = [...tasks].sort(
      (a, b) => a.createdAt.getTime() - b.createdAt.getTime()
    );
    setTasks(sorted);
  }

  return (
    <div>
      <button onClick={sortByPriority}>Sort by Priority</button>
      <button onClick={sortByDate}>Sort by Date</button>
      <ul>
        {tasks.map((t) => (
          <li key={t.id}>
            [{t.priority}] {t.title}
          </li>
        ))}
      </ul>
    </div>
  );
}
```

Problem: `tasks.sort()` mutates the array in place. Setting state with the same reference causes React to skip the re-render. The `[...tasks].sort()` workaround works but is less readable and allocates an extra intermediate array.

## Correct

```tsx
import { useState } from "react";

interface Task {
  id: string;
  title: string;
  priority: number;
  createdAt: Date;
}

// GOOD: .toSorted() returns a new array — React detects the change
function TaskList({ initialTasks }: { initialTasks: Task[] }) {
  const [tasks, setTasks] = useState(initialTasks);

  function sortByPriority() {
    // Returns a new sorted array — original unchanged
    setTasks(tasks.toSorted((a, b) => a.priority - b.priority));
  }

  function sortByDate() {
    setTasks(
      tasks.toSorted(
        (a, b) => a.createdAt.getTime() - b.createdAt.getTime()
      )
    );
  }

  function reverseOrder() {
    // .toReversed() — also immutable
    setTasks(tasks.toReversed());
  }

  return (
    <div>
      <button onClick={sortByPriority}>Sort by Priority</button>
      <button onClick={sortByDate}>Sort by Date</button>
      <button onClick={reverseOrder}>Reverse</button>
      <ul>
        {tasks.map((t) => (
          <li key={t.id}>
            [{t.priority}] {t.title}
          </li>
        ))}
      </ul>
    </div>
  );
}
```

Benefit: `.toSorted()` creates a new array reference, so React correctly detects the change and re-renders. The code is cleaner than `[...arr].sort()`, and the intent (immutable operation) is explicit.

### Other immutable array methods (ES2023)

```ts
const items = [1, 2, 3, 4, 5];

// .toReversed() — immutable reverse
const reversed = items.toReversed();
// reversed: [5, 4, 3, 2, 1], items: [1, 2, 3, 4, 5]

// .toSpliced() — immutable splice
const removed = items.toSpliced(1, 2);
// removed: [1, 4, 5], items: [1, 2, 3, 4, 5]

// .with() — immutable index replacement
const replaced = items.with(2, 99);
// replaced: [1, 2, 99, 4, 5], items: [1, 2, 3, 4, 5]
```

### Browser and runtime support

| Runtime | Minimum version |
|---------|----------------|
| Chrome | 110 |
| Safari | 16 |
| Firefox | 115 |
| Node.js | 20 |
| Edge | 110 |

For older environments, use `[...arr].sort()` as a fallback.

## When to Apply

- Any sorting of React state arrays — always use `.toSorted()`.
- Any context where the original array must remain unchanged (Redux reducers, Zustand stores, shared references).
- Replace `[...arr].sort()` with `.toSorted()` for clarity when targeting supported environments.

## Back to

- [overview.md](overview.md)

## See Also

- [min-max-loop.md](min-max-loop.md) — when you don't need a full sort, use a loop instead
