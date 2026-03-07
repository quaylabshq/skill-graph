# Sub-Agent Evaluation

Plan evaluation runs in a sub-agent (via the Task tool) to keep the main context clean and focused.

## Why Sub-Agent

- **Context isolation** — evaluation details don't clutter the main conversation
- **Focused analysis** — the sub-agent concentrates entirely on the plan
- **Clean results** — only the summary and key findings return to the main context

## Sub-Agent Strategy

Launch a general-purpose sub-agent with the Task tool. Provide:

1. The full plan content (read from the plan file)
2. The evaluation checklist (below)
3. Instructions to return a structured summary

## Evaluation Checklist

The sub-agent evaluates the plan against these dimensions:

### Completeness
- [ ] Clear goals/objectives defined
- [ ] All implementation steps specified
- [ ] Dependencies identified
- [ ] Files affected listed
- [ ] Verification/testing strategy included

### Feasibility
- [ ] Steps are actionable and specific (not vague)
- [ ] No circular dependencies
- [ ] Required tools/APIs are available
- [ ] Scope is realistic for a single implementation session

### Risk Assessment
- [ ] Edge cases considered
- [ ] Breaking changes identified
- [ ] Rollback strategy exists (if applicable)
- [ ] Security implications addressed (if applicable)

### Quality
- [ ] Follows existing codebase patterns
- [ ] No over-engineering beyond requirements
- [ ] Consistent with project conventions
- [ ] Clear acceptance criteria

## Sub-Agent Output Format

The sub-agent returns a structured summary:

```markdown
## Plan Assessment

**Overall**: [Strong / Adequate / Needs Work]

### Strengths
- ...

### Gaps
- ...

### Risks
- ...

### Recommendations
- ...
```

## Back to

- [Assessment overview](overview.md)
- See also: [Quality standards](../answering/quality-standards.md) — quality dimensions applied
