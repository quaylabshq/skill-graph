# Rule: Prefer `useTransition` Over Manual Loading State

**ID:** rendering-usetransition-loading
**Category:** Rendering Performance (Priority 6 — MEDIUM)

## Explanation

A common pattern for handling async operations in React is to manually manage a `isLoading` state variable: set it to `true` before the operation, `false` after. This works but has several drawbacks: it requires a `try/finally` block to handle errors correctly, the state update is treated as a high-priority update that can block user input, and it adds boilerplate to every async handler.

`useTransition` provides a built-in `isPending` boolean and a `startTransition` wrapper that marks the state update as low-priority. React automatically manages the pending state, batches the updates, and keeps the UI responsive to user input while the transition is in progress. The code is cleaner, more correct, and gives React better scheduling information.

## Incorrect

```tsx
// Bad: manual loading state management
'use client';

import { useState } from 'react';

function SearchPage() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  async function handleSearch(newQuery: string) {
    setQuery(newQuery);
    setIsLoading(true);
    try {
      const data = await fetchSearchResults(newQuery);
      setResults(data);
    } catch (error) {
      console.error('Search failed:', error);
    } finally {
      setIsLoading(false);   // easy to forget in error paths
    }
  }

  return (
    <div>
      <input
        value={query}
        onChange={(e) => handleSearch(e.target.value)}
        placeholder="Search..."
      />
      {isLoading ? <Spinner /> : <ResultList results={results} />}
    </div>
  );
}
```

```tsx
// Bad: manual loading for form submission
'use client';

import { useState } from 'react';

function ContactForm() {
  const [isSubmitting, setIsSubmitting] = useState(false);

  async function handleSubmit(formData: FormData) {
    setIsSubmitting(true);
    try {
      await submitContactForm(formData);
      // show success
    } catch (error) {
      // show error
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <form action={handleSubmit}>
      <input name="email" type="email" required />
      <textarea name="message" required />
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Sending...' : 'Send Message'}
      </button>
    </form>
  );
}
```

**Why this is wrong:**
1. Boilerplate: every async handler needs `useState` + `try/finally` for the loading flag.
2. Error-prone: forgetting `finally` or misplacing `setIsLoading(false)` leaves the UI stuck in a loading state.
3. Blocking: `setIsLoading(true)` is a high-priority update — React processes it immediately, potentially interrupting other rendering work. The `setResults` update is also high-priority and can cause input lag.

## Correct

```tsx
// Good: useTransition manages pending state automatically
'use client';

import { useState, useTransition } from 'react';

function SearchPage() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isPending, startTransition] = useTransition();

  function handleSearch(newQuery: string) {
    setQuery(newQuery);
    startTransition(async () => {
      const data = await fetchSearchResults(newQuery);
      setResults(data);
    });
  }

  return (
    <div>
      <input
        value={query}
        onChange={(e) => handleSearch(e.target.value)}
        placeholder="Search..."
      />
      {isPending ? <Spinner /> : <ResultList results={results} />}
    </div>
  );
}
```

```tsx
// Good: useTransition for form submission
'use client';

import { useTransition } from 'react';

function ContactForm() {
  const [isPending, startTransition] = useTransition();

  function handleSubmit(formData: FormData) {
    startTransition(async () => {
      await submitContactForm(formData);
      // show success
    });
  }

  return (
    <form action={handleSubmit}>
      <input name="email" type="email" required />
      <textarea name="message" required />
      <button type="submit" disabled={isPending}>
        {isPending ? 'Sending...' : 'Send Message'}
      </button>
    </form>
  );
}
```

**Why this is correct:**
1. No manual `isLoading` state — `isPending` is provided by React and managed automatically.
2. No `try/finally` boilerplate — React tracks the transition lifecycle internally.
3. Low-priority update — `startTransition` marks the state updates inside it as non-urgent. React keeps the UI responsive to typing and clicks while the transition processes in the background.
4. Automatic batching — all state updates inside `startTransition` are batched into a single render.

### With Server Actions (Next.js)

```tsx
// Good: useTransition with Server Actions
'use client';

import { useTransition } from 'react';
import { updateProfile } from '@/actions/profile';

function ProfileForm({ userId }: { userId: string }) {
  const [isPending, startTransition] = useTransition();

  return (
    <form
      action={(formData) => {
        startTransition(async () => {
          await updateProfile(userId, formData);
        });
      }}
    >
      <input name="displayName" />
      <input name="bio" />
      <button type="submit" disabled={isPending}>
        {isPending ? 'Saving...' : 'Save Profile'}
      </button>
    </form>
  );
}
```

### Tab switching with transition

```tsx
// Good: non-blocking tab switch — old tab stays visible while new one loads
'use client';

import { useState, useTransition } from 'react';

function TabbedContent() {
  const [activeTab, setActiveTab] = useState<'posts' | 'comments' | 'likes'>('posts');
  const [isPending, startTransition] = useTransition();

  function switchTab(tab: typeof activeTab) {
    startTransition(() => {
      setActiveTab(tab);
    });
  }

  return (
    <div>
      <nav>
        {(['posts', 'comments', 'likes'] as const).map((tab) => (
          <button
            key={tab}
            onClick={() => switchTab(tab)}
            className={activeTab === tab ? 'active' : ''}
          >
            {tab}
          </button>
        ))}
      </nav>

      <div style={{ opacity: isPending ? 0.7 : 1, transition: 'opacity 0.2s' }}>
        {activeTab === 'posts' && <PostsTab />}
        {activeTab === 'comments' && <CommentsTab />}
        {activeTab === 'likes' && <LikesTab />}
      </div>
    </div>
  );
}
```

## When to Apply

- Any async operation triggered by user interaction: search, form submission, data fetching, filtering.
- Tab switches or route-like transitions within a page.
- Server Action calls in Next.js client components.
- **Note:** `useTransition` is for state updates triggered by user actions. For data fetching on mount or based on props, use `use()` with Suspense or a data fetching library instead.

## Back to

- [overview.md](overview.md)
