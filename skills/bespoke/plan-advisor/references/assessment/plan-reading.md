# Plan Reading

How plan-advisor discovers, reads, and parses plan files into structured elements.

## Plan Discovery

1. **Explicit path** — user provides a path directly (highest priority)
2. **Plan mode file** — check for the active plan mode file in the current session
3. **Convention paths** — look for `PLAN.md`, `plan.md`, `implementation-plan.md` in the working directory
4. **Recent files** — check recently created/modified `.md` files for plan-like content

## Plan Parsing

Extract these elements from the plan file:

| Element | Description | Detection |
|---------|-------------|-----------|
| **Goals** | What the plan aims to achieve | Headings like "Goal", "Objective", "Summary" |
| **Steps** | Ordered implementation steps | Numbered lists, headings like "Steps", "Implementation" |
| **Dependencies** | What must exist or complete first | "Requires", "Depends on", "Prerequisites" |
| **Files affected** | Which files will be created/modified | File paths, "Files affected" sections |
| **Risks** | Potential issues or unknowns | "Risk", "Concern", "Unknown", "Open question" |
| **Verification** | How to confirm success | "Test", "Verify", "Validate", "Check" sections |
| **Context** | Background information | "Context", "Background", introductory paragraphs |

## Element Extraction Rules

1. **Be lenient** — plans vary widely in format; extract what's available
2. **Preserve structure** — maintain hierarchy and ordering from the original
3. **Flag gaps** — note when critical elements (goals, steps, verification) are missing
4. **No inference** — extract only what's explicitly stated; don't add implied steps

## Back to

- [Assessment overview](overview.md)
- See also: [Sub-agent evaluation](sub-agent-evaluation.md) — what happens after parsing
