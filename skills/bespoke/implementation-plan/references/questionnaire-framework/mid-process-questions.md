# Mid-Process Questions

How to identify and address gaps discovered during work. Questions must happen whenever ambiguity surfaces, not just at the beginning.

## Triggers for New Questions

Ask new questions when:

1. **Multiple valid approaches exist** — "Should this be organized by feature or by layer?"
2. **An assumption is being made** — "I'm assuming REST, but the user hasn't said."
3. **Missing context is discovered** — "This requires understanding the auth flow, which hasn't been discussed."
4. **Contradictions appear** — "The user said 'simple' but the requirements imply complexity."
5. **Edge cases surface** — "What should happen when the input is invalid?"
6. **Decomposition decisions require domain insight** — "I don't know the natural boundaries here."

## How to Identify Gaps Proactively

At each step, scan for:

- **Implicit assumptions** — What am I assuming that hasn't been stated?
- **Missing definitions** — Are there terms I'm using without a clear definition?
- **Untested boundaries** — Have I explored the edges of the requirements?
- **Dependencies** — Am I relying on something that hasn't been confirmed?

## How to Ask Mid-Process

1. **State what you discovered** — "While exploring the codebase, I noticed two possible integration points."
2. **Present the options** — "Option A: hook into the middleware. Option B: add a new route handler."
3. **Ask for direction** — "Which approach aligns better with your architecture preferences?"

## Rules

1. Never proceed with significant uncertainty — ask first
2. Frame questions with context about why you're asking
3. Keep mid-process questions focused and specific
4. One topic per question — don't bundle ambiguities

## Back to

- [Questionnaire framework overview](overview.md)
