# Quality Standards

All answers must meet senior/lead engineer quality. This means practical, well-reasoned decisions that balance correctness, simplicity, and maintainability.

## Quality Dimensions

### 1. Correctness
- Answers must be technically accurate
- Reference established patterns and best practices
- Consider edge cases and failure modes

### 2. Simplicity
- Prefer the simplest solution that meets requirements
- Avoid over-engineering and premature abstraction
- Choose boring technology over novel when stakes are high

### 3. Maintainability
- Favor readability over cleverness
- Consider future developers who will read this code
- Prefer explicit over implicit behavior

### 4. Consistency
- Follow existing codebase patterns and conventions
- Match the project's established style and architecture
- Use the same libraries/tools already in the project

### 5. Pragmatism
- Optimize for shipping, not theoretical perfection
- Accept trade-offs and state them clearly
- Consider the 80/20 rule — most value from least complexity

## Decision Framework

When choosing between options:

1. **Does it work?** — correctness first
2. **Is it simple?** — remove unnecessary complexity
3. **Does it fit?** — match existing patterns
4. **Can it change?** — consider future modifications
5. **Is it clear?** — another engineer should understand why

## Anti-Patterns to Avoid

| Anti-Pattern | Better Approach |
|--------------|-----------------|
| Gold-plating with extra features | Build exactly what's needed |
| Abstract base classes for one implementation | Direct implementation |
| Feature flags for unrequested configurability | Hard-code the requirement |
| Defensive coding against impossible states | Trust internal code paths |
| Adding comments explaining obvious code | Write self-documenting code |
| Creating utilities for one-time operations | Inline the logic |
| Backward-compatibility shims for new code | Just write the new code |

## Back to

- [Answering overview](overview.md)
- See also: [Domain expertise](domain-expertise.md) — domain-specific quality guidance
