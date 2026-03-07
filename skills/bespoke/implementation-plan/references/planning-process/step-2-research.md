# Step 2: Research

**Status: MANDATORY — never skip this step.**

Before planning, gather concrete information. For codebase tasks, explore the codebase. For non-code tasks, research the domain via web. Research bridges the gap between what the user stated and what the plan needs.

## Research Mode Selection

| Task Type | Research Mode | Reference |
|-----------|---------------|-----------|
| Codebase task (feature, bug fix, refactor, migration) | Codebase exploration | [codebase-exploration.md](../research-framework/codebase-exploration.md) |
| Non-code task (strategy, design, content, research) | Web/domain research | [web-research.md](../research-framework/web-research.md) |
| Mixed (full-stack with design, new project with research) | Both modes | Apply both references |

## Context Delegation

Research can bloat the main context. **Always delegate research to sub-agents**:

- Use Task tool with Explore agent for codebase exploration
- Use Task tool with general-purpose agent for web research
- Bring back synthesized findings only — not raw file contents or search results
- The main context should contain conclusions and decisions, not the exploration path

See [context management](../context-management.md) for the full delegation strategy.

## Research Output

Research should produce actionable inputs for decomposition:

1. **Architecture understanding** — how the codebase/domain is structured
2. **Patterns** — proven approaches that should inform the plan
3. **Constraints** — hard requirements discovered through research
4. **Risks** — known pitfalls or anti-patterns to avoid
5. **Dependencies** — what the task depends on and what depends on it

## Rules

1. Research is performed BEFORE decomposition — never plan based solely on initial understanding
2. Findings may trigger return to step 1 for additional clarification
3. Focus on information that directly impacts the plan — avoid rabbit holes
4. Always delegate to sub-agents — keep main context clean

## Back to

- [Planning process overview](overview.md)
- See also: [Research framework](../research-framework/overview.md) — detailed methodology
- See also: [Context management](../context-management.md) — delegation strategies
