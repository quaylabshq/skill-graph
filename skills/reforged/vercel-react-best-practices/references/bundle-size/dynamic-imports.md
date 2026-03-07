# Rule: bundle-dynamic-imports

## Use `next/dynamic` to lazy-load heavy components not needed on initial render

Large components like code editors, charting libraries, and rich text editors can add 100-500KB to your initial bundle. If they are not visible on first paint (e.g., they appear in modals, tabs, or below the fold), use `next/dynamic` to code-split them into separate chunks that load on demand.

## INCORRECT

```tsx
// Bad: static import loads MonacoEditor (~300KB) into the main bundle
import MonacoEditor from '@monaco-editor/react';

export function CodePlayground() {
  const [code, setCode] = useState('');

  return (
    <div>
      <h2>Code Editor</h2>
      <MonacoEditor
        height="400px"
        language="typescript"
        value={code}
        onChange={(val) => setCode(val ?? '')}
      />
    </div>
  );
}
```

**Why this is wrong:** The entire Monaco Editor bundle (~300KB gzipped) is included in the page's JavaScript, even if the user never interacts with the editor. This delays Time to Interactive for all users.

## CORRECT

```tsx
import dynamic from 'next/dynamic';
import { EditorSkeleton } from '@/components/EditorSkeleton';

// Lazy-load Monaco — only fetched when CodePlayground renders
const MonacoEditor = dynamic(() => import('@monaco-editor/react'), {
  loading: () => <EditorSkeleton />,
  ssr: false, // Monaco requires browser APIs, skip server render
});

export function CodePlayground() {
  const [code, setCode] = useState('');

  return (
    <div>
      <h2>Code Editor</h2>
      <MonacoEditor
        height="400px"
        language="typescript"
        value={code}
        onChange={(val) => setCode(val ?? '')}
      />
    </div>
  );
}
```

**Why this is correct:** The Monaco chunk is only downloaded when `CodePlayground` mounts. Until then, users see a lightweight skeleton placeholder. The initial page bundle stays small and interactive.

### When to use `next/dynamic`

Use dynamic imports for components that:

- Are **large** (50KB+ gzipped) — code editors, charting libs, PDF viewers
- Are **not visible on initial render** — modals, dialogs, tabs, below-fold content
- **Require browser APIs** — add `{ ssr: false }` to skip server rendering

```tsx
// More examples of good dynamic import candidates
const Chart = dynamic(() => import('@/components/Chart'), {
  loading: () => <ChartSkeleton />,
});

const PDFViewer = dynamic(() => import('@/components/PDFViewer'), {
  ssr: false,
  loading: () => <p>Loading document...</p>,
});

const MarkdownPreview = dynamic(() => import('@/components/MarkdownPreview'), {
  loading: () => <div className="animate-pulse h-64 bg-gray-100 rounded" />,
});
```

### Always provide a loading state

Never leave the loading prop empty. A skeleton or spinner prevents layout shift and signals to users that content is coming.

```tsx
// Bad: no loading state — content pops in with layout shift
const Editor = dynamic(() => import('./Editor'));

// Good: skeleton matches the final component dimensions
const Editor = dynamic(() => import('./Editor'), {
  loading: () => <div className="h-[400px] w-full animate-pulse bg-muted rounded-md" />,
});
```

## Back to

- [Bundle Size Optimization overview](overview.md)
