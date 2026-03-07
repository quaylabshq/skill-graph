# Web/Domain Research

How to research non-code domains before planning. This is the research mode for tasks without an existing codebase, or where domain knowledge is needed beyond code.

## When to Use

- Task is non-code (strategy, design, content, research)
- Task involves a domain you need to learn about
- Task requires understanding best practices or standards
- Task involves tools or APIs that need documentation review

## What to Research

### 1. Best Practices

- How are similar tasks typically approached?
- What does the community recommend?
- What patterns are proven effective?

### 2. Standards & Conventions

- Are there industry standards that apply?
- Are there framework conventions to follow?
- What documentation patterns exist?

### 3. Common Pitfalls

- What mistakes are commonly made in this domain?
- What anti-patterns should be avoided?
- What are the known failure modes?

### 4. Reference Examples

- Are there well-regarded examples of this type of work?
- What do successful implementations look like?
- What can be learned from existing approaches?

## How to Research

Use the Task tool with `subagent_type=general-purpose` for web research:

1. **Targeted searches** — search for specific questions, not broad topics
2. **Official documentation** — prioritize official docs over blog posts
3. **Multiple sources** — cross-reference findings from 2-3 sources
4. **Recency** — prefer recent sources for fast-moving domains

### Research Prompts by Domain

| Domain | Research Focus |
|--------|---------------|
| Design/UX | Current design trends, accessibility standards, component patterns |
| Business/Strategy | Industry frameworks, case studies, metrics benchmarks |
| Content | Style guides, audience analysis, format standards |
| Infrastructure | Provider documentation, security baselines, pricing |
| Data/ML | Algorithm comparisons, dataset practices, evaluation methods |

## Synthesizing Findings

Bring back to the main context:

- **Domain model** — key concepts, relationships, terminology
- **Recommended approach** — the best-practice path based on research
- **Constraints discovered** — requirements you didn't know about before
- **Warnings** — pitfalls to avoid
- **Open questions** — anything research couldn't resolve (return to clarification)

Do NOT bring back: raw search results, full article text, or tangentially related findings.

## Rules

1. Research before planning — never plan non-code tasks based solely on description
2. Delegate to sub-agents — keep main context clean
3. Focus on actionable findings — skip background/history
4. If research reveals the task is more complex than expected, return to clarification

## Back to

- [Research framework overview](overview.md)
- See also: [Context management](../context-management.md)
