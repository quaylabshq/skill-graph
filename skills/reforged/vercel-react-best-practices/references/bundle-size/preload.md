# Rule: bundle-preload

## Preload heavy bundles on hover/focus before they are needed

Dynamic imports improve initial load but introduce a delay when the user actually triggers the lazy-loaded feature. Preloading on intent signals — `onMouseEnter`, `onFocus`, or when a feature flag becomes enabled — fetches the chunk before the user clicks, eliminating the perceived latency of code-splitting.

## INCORRECT

```tsx
import dynamic from 'next/dynamic';

const HeavyModal = dynamic(() => import('@/components/HeavyModal'), {
  loading: () => <ModalSkeleton />,
});

export function Dashboard() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div>
      {/* Bad: chunk only starts downloading after the click */}
      <button onClick={() => setIsOpen(true)}>
        Open Settings
      </button>
      {isOpen && <HeavyModal onClose={() => setIsOpen(false)} />}
    </div>
  );
}
```

**Why this is wrong:** The user clicks "Open Settings" and then waits for the `HeavyModal` chunk to download, parse, and execute before seeing any content. On slow connections, this can take several seconds — the user sees either nothing or a skeleton during a moment when they expect immediate feedback.

## CORRECT

```tsx
import dynamic from 'next/dynamic';

const HeavyModal = dynamic(() => import('@/components/HeavyModal'), {
  loading: () => <ModalSkeleton />,
});

// Preload function — call this to start fetching the chunk early
function preloadHeavyModal() {
  void import('@/components/HeavyModal');
}

export function Dashboard() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div>
      {/* Good: chunk starts downloading on hover/focus, before click */}
      <button
        onMouseEnter={preloadHeavyModal}
        onFocus={preloadHeavyModal}
        onClick={() => setIsOpen(true)}
      >
        Open Settings
      </button>
      {isOpen && <HeavyModal onClose={() => setIsOpen(false)} />}
    </div>
  );
}
```

**Why this is correct:** When the user hovers over or focuses the button, the browser begins downloading the chunk immediately. By the time they click (typically 200-400ms later), the module is already cached. The modal appears instantly with no loading state visible.

### Pattern: preload on route-level intent

For page-level code-splitting, preload when a navigation link receives hover or focus:

```tsx
import Link from 'next/link';

function preloadSettingsPage() {
  // Preload both the route chunk and its heavy dependencies
  void import('@/components/SettingsPanel');
  void import('@/components/BillingForm');
}

export function Sidebar() {
  return (
    <nav>
      <Link href="/dashboard">Dashboard</Link>
      <Link
        href="/settings"
        onMouseEnter={preloadSettingsPage}
        onFocus={preloadSettingsPage}
      >
        Settings
      </Link>
    </nav>
  );
}
```

### Pattern: preload when a feature flag is enabled

When you know the user will need a module (e.g., a feature flag is on), preload it early without waiting for the user to interact:

```tsx
export function App({ featureFlags }: { featureFlags: FeatureFlags }) {
  // Preload as soon as we know the feature is enabled
  useEffect(() => {
    if (featureFlags.advancedExport) {
      void import('@/components/AdvancedExportDialog');
      void import('xlsx');
    }
  }, [featureFlags.advancedExport]);

  return <Dashboard featureFlags={featureFlags} />;
}
```

### Pattern: reusable preload hook

Abstract the preload logic into a hook for consistent use across the application:

```tsx
function usePreload(importFn: () => Promise<unknown>) {
  const preloaded = useRef(false);

  const preload = useCallback(() => {
    if (!preloaded.current) {
      preloaded.current = true;
      void importFn();
    }
  }, [importFn]);

  return { preload };
}

// Usage
const importModal = () => import('@/components/HeavyModal');
const HeavyModal = dynamic(importModal, { loading: () => <ModalSkeleton /> });

export function Feature() {
  const { preload } = usePreload(importModal);

  return (
    <button onMouseEnter={preload} onFocus={preload} onClick={open}>
      Open
    </button>
  );
}
```

### Preload timing guidelines

| Signal | When to use | Typical lead time |
|---|---|---|
| `onMouseEnter` | Desktop users, buttons/links | 200-400ms before click |
| `onFocus` | Keyboard navigation, accessibility | varies |
| Feature flag enabled | Module will definitely be needed | seconds to minutes |
| Route visible in viewport | Below-fold sections likely to scroll into view | seconds |
| `requestIdleCallback` | Non-critical modules during idle time | best-effort |

**Key point:** Preloading is free if the user never clicks — the browser fetches the chunk but only parses/executes it on actual use. The only cost is bandwidth, which is negligible for well-compressed chunks.

## Back to

- [Bundle Size Optimization overview](overview.md)
