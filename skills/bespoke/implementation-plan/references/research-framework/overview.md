# Research Framework

Governs how to gather information before planning. Research ensures the plan reflects reality — actual codebase structure, actual domain best practices — not assumptions.

## Core Principle

Planning without research means planning on assumptions. Research bridges the gap between the user's description and the concrete reality the plan must address.

## Research Mode

Every task gets one of two research modes based on [domain classification](../planning-process/domain-classification.md):

| Task Type | Research Mode | Reference |
|-----------|---------------|-----------|
| Has existing codebase | Codebase exploration | [codebase-exploration.md](codebase-exploration.md) |
| No codebase / non-code task | Web/domain research | [web-research.md](web-research.md) |
| Mixed | Both modes | Apply both |

## Research Output

Research should produce:

1. **Concrete facts** — file structure, API signatures, existing patterns, domain standards
2. **Constraints** — hard requirements discovered through research
3. **Risks** — known pitfalls or anti-patterns
4. **Dependencies** — what the task depends on

## Context Delegation

**Always delegate research to sub-agents.** The main context must stay clean for planning and user conversation.

- Use Task tool with `subagent_type=Explore` for codebase exploration
- Use Task tool with `subagent_type=general-purpose` for web research
- Bring back synthesized findings — not raw results

See [context management](../context-management.md) for the full delegation strategy.

## Rules

1. Research before planning — never plan based solely on initial understanding
2. Findings may trigger return to clarification
3. Focus on information that impacts the plan — avoid rabbit holes
4. Always delegate to sub-agents — keep main context clean
5. Research may take multiple rounds for complex tasks

## See Also

- [Planning process — step 2](../planning-process/step-2-research.md) — where this framework is invoked
- [Context management](../context-management.md) — delegation strategies
