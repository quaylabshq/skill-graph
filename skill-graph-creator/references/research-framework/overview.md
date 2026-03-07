# Research Framework

This framework governs how to gather information before implementation. Research ensures the skill graph reflects current best practices and avoids known pitfalls.

## Core Principle

Implementation is easy. Understanding the requirement correctly is the hard part. Research bridges the gap between what the user stated and what the implementation needs.

## When to Research

- **Always in step 2** — Research is mandatory before planning
- **When entering an unfamiliar domain** — Gather domain knowledge before structuring references
- **When multiple approaches exist** — Research which approach is preferred and why
- **When standards may apply** — Identify relevant specifications or conventions

## Research Components

| Component | Purpose | Reference |
|-----------|---------|-----------|
| Best practices | How similar systems are structured and why | [best-practices.md](best-practices.md) |
| Standards gathering | Industry standards, specifications, conventions that apply | [standards-gathering.md](standards-gathering.md) |

## Research Output

Research should produce actionable inputs for planning:

1. **Domain model** — Key concepts, relationships, and terminology
2. **Patterns** — Proven approaches that should inform the graph structure
3. **Constraints** — Hard requirements discovered through research
4. **Warnings** — Known pitfalls or anti-patterns to avoid

## Context Delegation for Research

Research can bloat the main context. Delegate research tasks to sub-contexts when:

- Exploring multiple competing approaches — each approach can be researched independently
- Reading extensive documentation — extract only what's relevant, discard the rest
- Performing web searches across many sources — synthesize findings before returning
- Investigating deep domain knowledge — bring back a summary, not raw material

**Delegation rule**: Bring back synthesized findings only — not raw results. The main context should contain conclusions and decisions, not the full exploration path.

See [context management](../graph-architecture/context-management.md) for the full delegation strategy.

## Rules

1. Research before planning — never design a graph structure based solely on initial understanding
2. Focus on information that impacts the skill graph design — avoid rabbit holes
3. Research may trigger return to clarification if new questions emerge
4. Document key findings — they inform decomposition and linking decisions
5. Delegate research to sub-contexts when scope is large — keep main context clean

## See Also

- [Creation process — step 2](../creation-process/step-2-research.md) — where this framework is invoked
- [Questionnaire framework](../questionnaire-framework/overview.md) — research often generates new questions
- [Context management](../graph-architecture/context-management.md) — delegation strategies
