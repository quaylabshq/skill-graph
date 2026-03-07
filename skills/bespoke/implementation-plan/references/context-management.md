# Context Management

The context window is finite. Every research result, file read, and search output reduces space for reasoning and conversation. Manage context deliberately.

## Context Budget

Typical budget during planning:

| Component | Tokens | Notes |
|-----------|--------|-------|
| SKILL.md index | ~100 lines | Loaded when skill triggers |
| 1-2 reference files | ~200 lines | Loaded for current step |
| Research findings | ~200 lines | Synthesized summaries only |
| User conversation | Variable | Must have ample room |

Loading 3+ reference files simultaneously is a warning sign — load only what the current step needs.

## Delegation Strategy

### Research Tasks — Always Delegate

Use Task tool to delegate all research:

- `subagent_type=Explore` for codebase exploration
- `subagent_type=general-purpose` for web research and multi-step investigations

**Delegation rule**: Bring back synthesized findings only — not raw results. The main context should contain conclusions and decisions, not the full exploration path.

### What to Delegate

- Codebase exploration (file reads, grep searches, architecture discovery)
- Web searches across multiple sources
- Documentation analysis
- Comparison of multiple approaches

### What to Keep in Main Context

- User requirements and preferences
- Key decisions made during questioning
- Synthesized research findings (summaries, not raw data)
- The current plan being built
- Feedback from the user

## Clean Main Thread

| Keep | Discard |
|------|---------|
| User requirements | Raw file contents from exploration |
| Key decisions | Full search results |
| Synthesized findings | Intermediate analysis |
| Current plan state | Exploratory dead-ends |
| Preferences/constraints | Verbose documentation excerpts |

## Branching Rules

**Delegate when:**
- Task has 3+ independent research threads
- Exploration scope is uncertain
- Deep-dive needed without polluting main context

**Keep in main context:**
- User preferences and decisions
- Cross-cutting constraints
- The plan being built

## Back to

- [Planning process — step 2](planning-process/step-2-research.md)
- See also: [Research framework](research-framework/overview.md)
