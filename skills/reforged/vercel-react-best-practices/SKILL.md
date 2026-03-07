---
name: vercel-react-best-practices
description: "React and Next.js performance optimization guide with 58 rules across 8 priority categories. Use when writing new React components, implementing data fetching, reviewing code for performance, refactoring React/Next.js code, or optimizing bundle size and load times. Covers async waterfalls, bundle size, server-side performance, client-side data fetching, re-render optimization, rendering performance, JavaScript performance, and advanced patterns."
---

# Vercel React Best Practices

Navigable reference graph for React/Next.js performance optimization. 58 rules organized by priority and impact.

## Rule Categories by Priority

| Priority | Category | Impact | Reference |
|----------|----------|--------|-----------|
| 1 | Eliminating Waterfalls | CRITICAL | [references/async-waterfalls/overview.md](references/async-waterfalls/overview.md) |
| 2 | Bundle Size Optimization | CRITICAL | [references/bundle-size/overview.md](references/bundle-size/overview.md) |
| 3 | Server-Side Performance | HIGH | [references/server-performance/overview.md](references/server-performance/overview.md) |
| 4 | Client-Side Data Fetching | MEDIUM-HIGH | [references/client-data-fetching/overview.md](references/client-data-fetching/overview.md) |
| 5 | Re-render Optimization | MEDIUM | [references/rerender-optimization/overview.md](references/rerender-optimization/overview.md) |
| 6 | Rendering Performance | MEDIUM | [references/rendering-performance/overview.md](references/rendering-performance/overview.md) |
| 7 | JavaScript Performance | LOW-MEDIUM | [references/js-performance/overview.md](references/js-performance/overview.md) |
| 8 | Advanced Patterns | LOW | [references/advanced-patterns/overview.md](references/advanced-patterns/overview.md) |

## When to Apply

Reference these guidelines when:
- Writing new React components or Next.js pages
- Implementing data fetching (client or server-side)
- Reviewing code for performance issues
- Refactoring existing React/Next.js code
- Optimizing bundle size or load times

## How to Use

1. Identify which category matches your current task
2. Navigate to that category's overview for a summary of all rules
3. Read individual rule files for detailed explanations and code examples
4. Each rule includes incorrect/correct code patterns

## Extensions

| Topic | Reference |
|-------|-----------|
| Future extensions & contribution patterns | [references/extensions.md](references/extensions.md) |
