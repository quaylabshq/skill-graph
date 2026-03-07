# Rule: bundle-defer-third-party

## Load analytics, logging, and error tracking after hydration

Third-party scripts for analytics, logging, and error tracking do not block user interaction. They should never be in the critical rendering path. Use `next/dynamic` with `{ ssr: false }` to defer them until after hydration, keeping the initial bundle lean and Time to Interactive fast.

## INCORRECT

```tsx
// Bad: top-level static imports load these into the main bundle
import { Analytics } from '@vercel/analytics/react';
import { SpeedInsights } from '@vercel/speed-insights/next';
import * as Sentry from '@sentry/nextjs';
import { PostHogProvider } from 'posthog-js/react';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <PostHogProvider>
          {children}
          <Analytics />
          <SpeedInsights />
        </PostHogProvider>
      </body>
    </html>
  );
}
```

**Why this is wrong:** Every byte of analytics, error tracking, and logging code is parsed and executed before the page becomes interactive. These libraries are not needed for the user to see or interact with the page — they exist to observe usage. Loading them eagerly penalizes every user's first load.

## CORRECT

```tsx
import dynamic from 'next/dynamic';

// Defer all observability scripts — load after hydration, skip SSR
const Analytics = dynamic(
  () => import('@vercel/analytics/react').then((m) => m.Analytics),
  { ssr: false }
);

const SpeedInsights = dynamic(
  () => import('@vercel/speed-insights/next').then((m) => m.SpeedInsights),
  { ssr: false }
);

const PostHogProvider = dynamic(
  () => import('@/components/PostHogProvider'),
  { ssr: false }
);

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        {children}
        <Analytics />
        <SpeedInsights />
        <PostHogProvider />
      </body>
    </html>
  );
}
```

**Why this is correct:** The main bundle contains zero observability code. After hydration, React lazy-loads these components in the background. Users get a faster interactive page, and analytics still capture the full session.

### Extracting a deferred wrapper component

For Sentry or other SDKs that need initialization (not just a component mount), create a dedicated client component that initializes after hydration:

```tsx
// @/components/SentryInit.tsx
'use client';

import { useEffect } from 'react';

export default function SentryInit() {
  useEffect(() => {
    import('@sentry/nextjs').then((Sentry) => {
      Sentry.init({
        dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
        tracesSampleRate: 0.1,
        replaysSessionSampleRate: 0.01,
      });
    });
  }, []);

  return null;
}
```

```tsx
// In layout.tsx
const SentryInit = dynamic(() => import('@/components/SentryInit'), {
  ssr: false,
});

// Then render <SentryInit /> in the body
```

### What qualifies as deferrable

| Library Type | Examples | Defer? |
|---|---|---|
| Analytics | Vercel Analytics, Google Analytics, Mixpanel | Yes |
| Error tracking | Sentry, Datadog RUM, Bugsnag | Yes |
| Session replay | PostHog, FullStory, LogRocket | Yes |
| Speed monitoring | Vercel Speed Insights, Web Vitals | Yes |
| Feature flags (UI only) | LaunchDarkly, Statsig | Yes |
| Auth providers | NextAuth session | No — needed for initial render |
| Theming | next-themes | No — causes flash if deferred |

## Back to

- [Bundle Size Optimization overview](overview.md)
