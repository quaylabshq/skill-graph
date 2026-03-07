# Rule: Inject Synchronous Script to Prevent Hydration Flicker

**ID:** rendering-hydration-no-flicker
**Category:** Rendering Performance (Priority 6 — MEDIUM)

## Explanation

When server-rendered HTML uses a default theme (e.g., light mode) but the user's preference is stored in `localStorage` (e.g., dark mode), there is a visible flash: the page renders light, React hydrates, reads `localStorage`, then switches to dark. This creates a jarring flicker and can also cause React hydration mismatch warnings if the server and client disagree on class names or attributes.

The fix is to inject a tiny synchronous `<script>` in `<head>` that runs **before** the browser paints and **before** React hydrates. This script reads `localStorage` and applies the correct class/attribute to `<html>` or `<body>` immediately, so the first paint already matches the user's preference.

## Incorrect

```tsx
// Bad: reading localStorage in a useEffect — causes flicker
'use client';

import { useEffect, useState } from 'react';

function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  useEffect(() => {
    // This runs AFTER hydration and paint — user sees light flash first
    const saved = localStorage.getItem('theme') as 'light' | 'dark' | null;
    if (saved) {
      setTheme(saved);
      document.documentElement.setAttribute('data-theme', saved);
    }
  }, []);

  return (
    <div data-theme={theme}>
      {children}
    </div>
  );
}
```

**Why this is wrong:**
1. The server renders with `theme = 'light'` (the default `useState` value).
2. The browser paints the light theme.
3. `useEffect` runs, reads `'dark'` from `localStorage`, and triggers a re-render.
4. The user sees a light-to-dark flash. If `data-theme` was rendered in SSR as `'light'` and the client immediately sets `'dark'`, React logs a hydration mismatch warning.

## Correct

```tsx
// Good: synchronous inline script in <head> prevents flicker
// app/layout.tsx (Next.js App Router)

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `
              (function() {
                try {
                  var theme = localStorage.getItem('theme');
                  if (theme === 'dark' || (!theme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                    document.documentElement.setAttribute('data-theme', 'dark');
                    document.documentElement.classList.add('dark');
                  } else {
                    document.documentElement.setAttribute('data-theme', 'light');
                  }
                } catch (e) {}
              })();
            `,
          }}
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

**Why this is correct:**
1. The `<script>` in `<head>` runs synchronously before the browser's first paint.
2. It reads `localStorage` and sets `data-theme` and the `dark` class on `<html>`.
3. The first paint already uses the correct theme — no flicker.
4. `suppressHydrationWarning` on `<html>` avoids the mismatch warning because the script modifies `<html>` before React hydrates.

### Locale / language preference variant

```tsx
// Good: same pattern for locale stored in localStorage
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `
              (function() {
                try {
                  var lang = localStorage.getItem('locale');
                  if (lang) {
                    document.documentElement.lang = lang;
                  }
                } catch (e) {}
              })();
            `,
          }}
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

### Combining theme + sidebar collapsed state

```tsx
<script
  dangerouslySetInnerHTML={{
    __html: `
      (function() {
        try {
          var theme = localStorage.getItem('theme');
          if (theme === 'dark' || (!theme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
          }
          var sidebar = localStorage.getItem('sidebar-collapsed');
          if (sidebar === 'true') {
            document.documentElement.classList.add('sidebar-collapsed');
          }
        } catch (e) {}
      })();
    `,
  }}
/>
```

## When to Apply

- Theme (dark/light mode) preferences stored in `localStorage` or cookies.
- Locale or language preferences that affect the `lang` attribute.
- Sidebar collapsed/expanded state that shifts layout.
- Any client-only data that affects the first paint and is stored in `localStorage`.
- **Keep the script tiny** — only read storage and set attributes/classes. Do not import modules or run complex logic.

## Back to

- [overview.md](overview.md)

## See Also

- [hydration-suppress-warning.md](hydration-suppress-warning.md) — handling expected server/client mismatches
