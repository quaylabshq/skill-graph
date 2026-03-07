# Rule: Hoist RegExp to Module Scope or Memoize

**ID:** js-hoist-regexp
**Category:** JavaScript Performance (Priority 7 — LOW-MEDIUM)

## Explanation

Creating a `RegExp` object compiles the pattern into an internal automaton. When a regex is defined inside a function or loop body, this compilation happens on every call or iteration. Hoist static regex patterns to module scope so they compile once.

**Warning:** A regex with the `/g` (global) flag has mutable `lastIndex` state. After each `.test()` or `.exec()` call, `lastIndex` advances, and the next call starts from that position. This causes alternating `true`/`false` results when reusing a global regex. Either use the regex without `/g`, or reset `lastIndex = 0` before each use.

## Incorrect

```ts
// BAD: regex compiled on every function call
function isValidEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// BAD: regex compiled on every iteration
function extractHashtags(posts: string[]): string[][] {
  return posts.map((post) => {
    const hashtagRegex = /#[\w]+/g; // compiled 1,000 times for 1,000 posts
    return post.match(hashtagRegex) ?? [];
  });
}

// BAD: global regex reused without resetting lastIndex
const GLOBAL_PATTERN = /\d+/g;

function hasNumber(str: string): boolean {
  return GLOBAL_PATTERN.test(str); // alternates true/false!
}

hasNumber("abc123"); // true  (lastIndex now = 6)
hasNumber("abc123"); // false (starts at index 6, finds nothing)
hasNumber("abc123"); // true  (lastIndex reset to 0 after failure)
```

Problem: regex compilation inside loops wastes CPU. Global regex with mutable `lastIndex` produces unpredictable results when reused.

## Correct

```ts
// GOOD: regex hoisted to module scope — compiled once
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function isValidEmail(email: string): boolean {
  return EMAIL_REGEX.test(email);
}

// GOOD: non-global regex hoisted (String.match with /g is fine)
const HASHTAG_REGEX = /#[\w]+/g;

function extractHashtags(posts: string[]): string[][] {
  // String.prototype.match() with /g ignores lastIndex — safe to reuse
  return posts.map((post) => post.match(HASHTAG_REGEX) ?? []);
}

// GOOD: for RegExp.test() or RegExp.exec(), use without /g flag
const HAS_NUMBER = /\d+/; // no /g flag — lastIndex always 0

function hasNumber(str: string): boolean {
  return HAS_NUMBER.test(str); // consistent results every time
}

// GOOD: if you need /g, reset lastIndex before each use
const DIGIT_PATTERN = /\d+/g;

function findAllNumbers(str: string): string[] {
  DIGIT_PATTERN.lastIndex = 0; // reset before use
  const matches: string[] = [];
  let match: RegExpExecArray | null;

  while ((match = DIGIT_PATTERN.exec(str)) !== null) {
    matches.push(match[0]);
  }

  return matches;
}
```

### In React components: memoize with useMemo

```tsx
import { useMemo } from "react";

function SearchHighlight({ text, query }: { text: string; query: string }) {
  // Regex depends on a prop — memoize instead of hoisting
  const pattern = useMemo(
    () => new RegExp(`(${escapeRegExp(query)})`, "gi"),
    [query]
  );

  const parts = text.split(pattern);

  return (
    <span>
      {parts.map((part, i) =>
        pattern.test(part) ? <mark key={i}>{part}</mark> : part
      )}
    </span>
  );
}

function escapeRegExp(str: string): string {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
```

## When to Apply

- Any regex that doesn't depend on runtime values — hoist to module scope.
- Regex that depends on props or state — memoize with `useMemo()`.
- Validation functions called repeatedly (email, phone, URL patterns).
- Text processing loops (search, highlight, extraction).

## Back to

- [overview.md](overview.md)

## See Also

- [cache-function-results.md](cache-function-results.md) — caching computed results for repeated inputs
- [cache-property-access.md](cache-property-access.md) — hoisting invariant values out of loops
