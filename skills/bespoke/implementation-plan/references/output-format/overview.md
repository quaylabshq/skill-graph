# Output Format

The implementation plan uses a **standardized core + adaptive detail** structure. Every plan has the same core sections; additional sections are added based on domain and complexity.

## Structure Principle

The core template provides consistency — every plan is navigable the same way. Adaptive sections provide depth where the specific task demands it.

## Plan Depth Tiers

From [domain classification](../planning-process/domain-classification.md):

| Tier | When | Sections |
|------|------|----------|
| Lightweight | Simple tasks, 1-2 files, clear approach | Summary + Steps only |
| Standard | Moderate tasks, 3-10 files, some decisions | Full core template |
| Detailed | Complex tasks, 10+ files, architectural decisions | Core template + adaptive sections |

## Components

| Component | Purpose | Reference |
|-----------|---------|-----------|
| Core template | Fixed sections every plan must have | [core-template.md](core-template.md) |
| Adaptive sections | Domain-specific additions based on task type | [adaptive-sections.md](adaptive-sections.md) |

## Formatting Rules

1. Use markdown headings and lists — plans must be scannable
2. Steps should be numbered and ordered by dependency
3. Mark complexity signals on steps: straightforward / needs investigation / high-risk
4. Never include time estimates — use complexity signals instead
5. File lists should include the purpose of each change, not just the filename

## Back to

- [Planning process — step 4](../planning-process/step-4-generate-plan.md)
