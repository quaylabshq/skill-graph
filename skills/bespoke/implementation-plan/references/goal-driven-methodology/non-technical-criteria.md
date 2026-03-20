# Non-Technical Acceptance Criteria

For non-code tasks, acceptance criteria must be equally rigorous as tests — just expressed differently. The criterion must be something an observer can evaluate without subjective judgment.

## The Challenge

Code tasks have a natural verification mechanism: tests pass or fail. Non-code tasks lack this binary signal. The solution: define criteria that are **observable, measurable, and evaluatable** by a defined method.

## Acceptance Criteria Patterns by Domain

### Design/UX

| Criteria Type | Evaluation Method | Example |
|---------------|-------------------|---------|
| Usability | Task completion rate | "A new user can complete signup in under 60 seconds without help" |
| Accessibility | WCAG conformance | "All interactive elements meet WCAG 2.1 AA" |
| Consistency | Design system compliance | "All components use existing design tokens — no hardcoded colors or spacing" |
| Responsiveness | Breakpoint verification | "Layout adapts correctly at 320px, 768px, 1024px, 1440px breakpoints" |
| State coverage | Interaction state enumeration | "Every interactive element has default, hover, active, focused, disabled, error, and loading states defined" |

### Business/Strategy

| Criteria Type | Evaluation Method | Example |
|---------------|-------------------|---------|
| Impact | KPI target | "Reduces customer churn by 5% within Q3" |
| Feasibility | Resource constraint | "Achievable with current team of 4 without additional hiring" |
| Alignment | Stakeholder sign-off | "VP of Product and VP of Engineering both approve the proposal" |
| Risk | Risk matrix score | "No identified risk scores above Medium likelihood + High impact" |
| Completeness | Checklist | "Addresses all 3 board concerns raised in the Q1 review" |

### Content

| Criteria Type | Evaluation Method | Example |
|---------------|-------------------|---------|
| Audience fit | Readability score | "Flesch-Kincaid grade level 8-10 for general audience" |
| Accuracy | Fact verification | "All statistics cited with primary sources published within 2 years" |
| Completeness | Topic coverage | "Covers all 5 themes from the editorial brief" |
| Engagement | Structure check | "Every section under 300 words, subheadings every 2-3 paragraphs" |
| Tone | Voice guidelines | "Matches brand voice guide: professional, direct, no jargon" |

### Research

| Criteria Type | Evaluation Method | Example |
|---------------|-------------------|---------|
| Scope | Question coverage | "Answers all 3 research questions stated in the brief" |
| Evidence | Source quality | "Minimum 5 peer-reviewed sources per claim, published within 5 years" |
| Objectivity | Bias check | "Presents minimum 2 perspectives for each contested claim" |
| Reproducibility | Method documentation | "Another researcher could replicate the analysis from the method section alone" |
| Falsifiability | Hypothesis testing | "Each conclusion states what evidence would disprove it" |

### Infrastructure/DevOps

| Criteria Type | Evaluation Method | Example |
|---------------|-------------------|---------|
| Reliability | SLO | "99.9% uptime (43.8 minutes/month maximum downtime)" |
| Performance | SLI threshold | "p95 latency < 200ms, p99 < 500ms" |
| Recovery | RTO/RPO | "Recovery time < 15 minutes, recovery point < 5 minutes" |
| Security | Compliance checklist | "Passes CIS benchmark Level 1 for the target platform" |
| Observability | Alert coverage | "Every failure mode has a corresponding alert with runbook link" |

## How to Evaluate Non-Technical Criteria

Since non-code criteria can't be "run" like tests, define the evaluation method explicitly:

| Evaluation Method | When to Use | Example |
|-------------------|-------------|---------|
| **Checklist review** | Criteria are enumerable | "Verify all 12 items on the accessibility checklist" |
| **Expert review** | Criteria require domain judgment | "UX review by designer using Nielsen's 10 heuristics" |
| **Measurement** | Criteria are quantitative | "Run Lighthouse audit, verify score > 90" |
| **Comparison** | Criteria reference a standard | "Compare output against the approved style guide" |
| **Stakeholder sign-off** | Criteria are preference-based | "Product owner confirms the mockup matches their vision" |

## Writing Good Non-Technical Criteria

### The Litmus Test

For every criterion, ask: "Could two independent reviewers evaluate this criterion and reach the same conclusion?" If yes, it is specific enough. If not, refine it.

### Transform Vague to Specific

| Vague (reject) | Specific (accept) |
|-----------------|-------------------|
| "The design looks good" | "The design passes all 10 Nielsen usability heuristics at 'minor issue' threshold or better" |
| "The document is complete" | "The document addresses all 7 sections in the RFP template with no section marked TBD" |
| "Performance is acceptable" | "Page load time < 3 seconds on 3G connection, measured by WebPageTest" |
| "The strategy is sound" | "The strategy addresses all 3 risks identified in the SWOT analysis with specific mitigations" |
| "Users will like it" | "Prototype scores > 4.0/5.0 on SUS (System Usability Scale) with 5 test users" |

## Rules

1. **Every non-code plan step must have observable acceptance criteria**
2. **Every criterion must have a defined evaluation method**
3. **Avoid subjective criteria** — if a criterion relies on taste, replace it with a framework-based evaluation
4. **When subjectivity is unavoidable**, make the evaluator and evaluation method explicit ("Product owner confirms X using criteria Y")
5. **Criteria must be defined BEFORE the approach** — same as TDD: the "test" comes first

## Back to

- [Goal-driven methodology overview](overview.md)
