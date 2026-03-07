# Rule: bundle-conditional

## Load large modules only when a feature is activated

When a feature is behind a flag, A/B test, or user permission, its code should not be included in the bundle for users who will never see it. Use dynamic `import()` inside `useEffect` or event handlers to load heavy modules only when the feature is actually activated.

## INCORRECT

```tsx
// Bad: heavy-lib is always in the bundle, even when the feature is off
import { processData, generateReport } from 'heavy-lib'; // 250KB

interface Props {
  featureEnabled: boolean;
  data: DataSet;
}

export function ReportPanel({ featureEnabled, data }: Props) {
  const [report, setReport] = useState<Report | null>(null);

  useEffect(() => {
    if (featureEnabled) {
      const result = processData(data);
      setReport(generateReport(result));
    }
  }, [featureEnabled, data]);

  if (!featureEnabled) return null;

  return <ReportView report={report} />;
}
```

**Why this is wrong:** The static `import` at the top ensures `heavy-lib` (250KB) is always bundled and shipped to every user, regardless of whether the feature flag is enabled. Users who never see this feature still pay the download and parse cost.

## CORRECT

```tsx
// Good: heavy-lib is only fetched when the feature flag is true
interface Props {
  featureEnabled: boolean;
  data: DataSet;
}

export function ReportPanel({ featureEnabled, data }: Props) {
  const [report, setReport] = useState<Report | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    if (!featureEnabled) return;

    let cancelled = false;
    setIsLoading(true);

    import('heavy-lib').then((mod) => {
      if (cancelled) return;
      const result = mod.processData(data);
      setReport(mod.generateReport(result));
      setIsLoading(false);
    });

    return () => {
      cancelled = true;
    };
  }, [featureEnabled, data]);

  if (!featureEnabled) return null;
  if (isLoading) return <ReportSkeleton />;

  return <ReportView report={report} />;
}
```

**Why this is correct:** The dynamic `import('heavy-lib')` creates a separate chunk. The browser only downloads it when `featureEnabled` becomes `true`. Users with the feature disabled never download the code.

### Pattern: conditional component loading with `next/dynamic`

For feature-flagged UI components (not just utility modules), combine `next/dynamic` with a wrapper:

```tsx
import dynamic from 'next/dynamic';

const AdvancedEditor = dynamic(() => import('@/components/AdvancedEditor'), {
  loading: () => <EditorSkeleton />,
});

export function EditorPanel({ isPremiumUser }: { isPremiumUser: boolean }) {
  if (!isPremiumUser) {
    return <BasicEditor />;
  }

  // AdvancedEditor chunk is only fetched for premium users
  return <AdvancedEditor />;
}
```

### Pattern: conditional loading in event handlers

For modules needed only in response to user actions (not on render):

```tsx
export function ExportButton({ data }: { data: DataSet }) {
  const [isExporting, setIsExporting] = useState(false);

  async function handleExport() {
    setIsExporting(true);

    // xlsx library (~200KB) only loads when user clicks Export
    const XLSX = await import('xlsx');
    const worksheet = XLSX.utils.json_to_sheet(data);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Report');
    XLSX.writeFile(workbook, 'report.xlsx');

    setIsExporting(false);
  }

  return (
    <button onClick={handleExport} disabled={isExporting}>
      {isExporting ? 'Exporting...' : 'Export to Excel'}
    </button>
  );
}
```

### Key considerations

- Always handle the loading state — the dynamic import is asynchronous
- Use a cleanup flag (`cancelled`) in `useEffect` to avoid setting state on unmounted components
- Browser caches dynamic imports, so subsequent loads are instant
- Webpack/Turbopack magic comments like `/* webpackChunkName: "report" */` can name chunks for easier debugging

## Back to

- [Bundle Size Optimization overview](overview.md)
