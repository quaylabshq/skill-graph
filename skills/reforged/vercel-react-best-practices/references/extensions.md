# Future Extensions

Planned and potential extensions to this skill graph.

## Planned

### 1. Framework-Specific Variants
- **Type**: Reference files
- **Purpose**: Specialized rules for Remix, Astro, or other React meta-frameworks
- **Pattern**: `references/framework-variants/{framework}.md`
- **Implementation**: New hub + detail files per framework

### 2. Automated Codemod Scripts
- **Type**: Tool scripts
- **Purpose**: Automated detection and fixing of rule violations
- **Pattern**: `scripts/detect-{rule-id}.py` or `scripts/fix-{rule-id}.py`
- **Operations**: AST analysis, pattern matching, auto-fix suggestions
- **Reference**: Each script links back to its rule detail file

### 3. Performance Profiling Guide
- **Type**: Reference file
- **Purpose**: How to identify which rules to apply via profiling (Chrome DevTools, Lighthouse, React Profiler)
- **Pattern**: `references/profiling-guide.md`

### 4. Testing Patterns
- **Type**: Reference files
- **Purpose**: How to write performance tests and benchmarks for each optimization
- **Pattern**: `references/testing/overview.md` with per-category details

### 5. New Rule Categories
- **Type**: Hub + detail files
- **Purpose**: As React/Next.js evolve, new optimization categories may emerge
- **Pattern**: `references/{new-category}/overview.md` + rule files
- **Examples**: React Server Functions, React Compiler optimizations, View Transitions API

## Implementation Pattern

Each extension follows the existing graph structure:

1. Create `references/{category}/` directory (if new category)
2. Write `overview.md` hub file linking to all detail files
3. Write individual detail files with standard format (explanation, incorrect/correct code, Back to, See also)
4. Update SKILL.md index table to include new hub link
5. Add cross-links from related existing rules

## Back to

- [SKILL.md](../SKILL.md)
