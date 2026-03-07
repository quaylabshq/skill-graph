# Rule: bundle-barrel-imports

## Import directly from source files, not barrel files

Barrel files (`index.ts` that re-exports from many modules) force the bundler to evaluate every re-exported module even when you only need one export. A single barrel file can contain 10,000+ re-exports, adding 200-800ms of import overhead. This bloats the client bundle and slows down both dev server startup and production page loads.

## INCORRECT

```tsx
// Bad: importing from a barrel file (index.ts re-exports everything)
import { Button } from '@/components';
import { formatDate } from '@/utils';
import { useAuth } from '@/hooks';
```

```ts
// The barrel file at @/components/index.ts looks like:
export { Button } from './Button';
export { Modal } from './Modal';
export { DataGrid } from './DataGrid';       // 150KB
export { RichTextEditor } from './RichTextEditor'; // 200KB
export { Chart } from './Chart';             // 180KB
// ... hundreds more re-exports
// Importing Button pulls in the entire dependency graph
```

**Why this is wrong:** Even though you only use `Button`, the bundler must resolve and parse every module re-exported from the barrel. Tree-shaking helps in production but is imperfect (side effects, CommonJS modules), and dev server performance suffers regardless.

## CORRECT

```tsx
// Good: import directly from the source module
import { Button } from '@/components/Button';
import { formatDate } from '@/utils/formatDate';
import { useAuth } from '@/hooks/useAuth';
```

**Why this is correct:** The bundler only needs to resolve and parse the single module you actually use. No wasted work, no accidental inclusion of heavy dependencies.

### Using `optimizePackageImports` in Next.js 13.5+

For third-party libraries that use barrel exports (e.g., `lucide-react`, `@mui/material`, `date-fns`), Next.js provides automatic barrel-file optimization:

```ts
// next.config.ts
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  experimental: {
    optimizePackageImports: [
      'lucide-react',
      '@mui/material',
      '@mui/icons-material',
      'date-fns',
      'lodash-es',
      '@heroicons/react/24/outline',
      '@heroicons/react/24/solid',
    ],
  },
};

export default nextConfig;
```

With this config, `import { Search } from 'lucide-react'` is automatically transformed to import only the `Search` icon instead of all 1,000+ icons.

**Note:** `optimizePackageImports` only works for third-party packages. For your own code, always use direct imports — do not rely on tooling to fix avoidable barrel imports in first-party code.

## Back to

- [Bundle Size Optimization overview](overview.md)
