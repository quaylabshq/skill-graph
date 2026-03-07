# Rule: Use `<Activity>` to Preserve State for Toggled Components

**ID:** rendering-activity
**Category:** Rendering Performance (Priority 6 — MEDIUM)

## Explanation

When expensive components (modals, tabs, sidebars, detail panels) are conditionally rendered with `{isOpen && <Panel />}`, React unmounts the entire subtree when hidden and remounts it from scratch when shown again. This destroys all internal state, re-runs effects, re-fetches data, and re-creates DOM nodes — causing visible lag for complex components.

React's `<Activity>` component (previously called `<Offscreen>`) solves this by keeping the component mounted and its DOM in the document, but marking it as `'hidden'`. When hidden, the component's DOM is not displayed (`display: none` is applied by React), effects are cleaned up, and the subtree is deprioritized. When toggled back to `'visible'`, the existing DOM is shown instantly with all state preserved — no remount cost.

## Incorrect

```tsx
// Bad: conditional rendering destroys and recreates the entire panel
'use client';

import { useState } from 'react';

function Dashboard() {
  const [activeTab, setActiveTab] = useState<'overview' | 'analytics' | 'settings'>('overview');

  return (
    <div>
      <nav>
        <button onClick={() => setActiveTab('overview')}>Overview</button>
        <button onClick={() => setActiveTab('analytics')}>Analytics</button>
        <button onClick={() => setActiveTab('settings')}>Settings</button>
      </nav>

      {/* Each tab unmounts when switching — loses all state */}
      {activeTab === 'overview' && <OverviewPanel />}
      {activeTab === 'analytics' && <AnalyticsPanel />}   {/* expensive charts */}
      {activeTab === 'settings' && <SettingsPanel />}       {/* form state lost */}
    </div>
  );
}
```

**Why this is wrong:** Switching from Analytics to Overview destroys the `<AnalyticsPanel>` DOM entirely. Switching back remounts it from scratch — re-fetching data, re-rendering charts, and losing scroll position. The `<SettingsPanel>` loses any unsaved form input when the user navigates away and back.

## Correct

```tsx
// Good: <Activity> preserves state and DOM for hidden tabs
'use client';

import { useState, Activity } from 'react';

function Dashboard() {
  const [activeTab, setActiveTab] = useState<'overview' | 'analytics' | 'settings'>('overview');

  return (
    <div>
      <nav>
        <button onClick={() => setActiveTab('overview')}>Overview</button>
        <button onClick={() => setActiveTab('analytics')}>Analytics</button>
        <button onClick={() => setActiveTab('settings')}>Settings</button>
      </nav>

      <Activity mode={activeTab === 'overview' ? 'visible' : 'hidden'}>
        <OverviewPanel />
      </Activity>

      <Activity mode={activeTab === 'analytics' ? 'visible' : 'hidden'}>
        <AnalyticsPanel />
      </Activity>

      <Activity mode={activeTab === 'settings' ? 'visible' : 'hidden'}>
        <SettingsPanel />
      </Activity>
    </div>
  );
}
```

**Why this is correct:** All three panels stay mounted. When hidden, React applies `display: none` and cleans up effects (no timers running, no subscriptions leaking). When shown, the existing DOM is revealed instantly — no re-render, no re-fetch, no lost state. Chart zoom level, scroll position, and unsaved form inputs are all preserved.

### Modal / dialog pattern

```tsx
// Good: keep an expensive modal ready to show instantly
'use client';

import { useState, Activity } from 'react';

function ProductPage({ productId }: { productId: string }) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div>
      <button onClick={() => setIsOpen(true)}>View Details</button>

      <Activity mode={isOpen ? 'visible' : 'hidden'}>
        <ProductDetailModal
          productId={productId}
          onClose={() => setIsOpen(false)}
        />
      </Activity>
    </div>
  );
}
```

### Sidebar with form state preservation

```tsx
// Good: sidebar form state survives collapse/expand
'use client';

import { useState, Activity } from 'react';

function AppLayout({ children }: { children: React.ReactNode }) {
  const [sidebarOpen, setSidebarOpen] = useState(true);

  return (
    <div className="app-layout">
      <Activity mode={sidebarOpen ? 'visible' : 'hidden'}>
        <Sidebar>
          <FilterForm />  {/* user selections preserved when collapsed */}
          <NavigationTree /> {/* expanded/collapsed tree nodes preserved */}
        </Sidebar>
      </Activity>

      <main>{children}</main>

      <button onClick={() => setSidebarOpen((prev) => !prev)}>
        Toggle Sidebar
      </button>
    </div>
  );
}
```

## When to Apply

- Tab interfaces where each tab contains expensive components (charts, data grids, editors).
- Modals and drawers that are opened/closed frequently and contain complex content.
- Sidebars or panels with form state, scroll position, or expanded/collapsed sections.
- **Trade-off:** Hidden components keep their DOM in memory. For dozens of heavy components, this increases memory usage. Use `<Activity>` for a small number of expensive, frequently-toggled components — not for virtualizing large lists.

## Back to

- [overview.md](overview.md)
