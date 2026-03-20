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

## Conflicting Requirements Detection

Actively scan for requirement tensions at every step. Requirements that individually sound reasonable can be mutually exclusive or create impossible trade-offs.

| Conflict Pattern | Example | Resolution Approach |
|------------------|---------|---------------------|
| Speed vs. thoroughness | "Fast response" + "comprehensive analysis" | Ask user to prioritize; define thresholds for both |
| Simplicity vs. completeness | "Simple API" + "handle all edge cases" | Ask which edge cases are critical vs. nice-to-have |
| Security vs. usability | "Seamless login" + "maximum security" | Define acceptable trade-off; cite industry standards |
| Scope vs. quality | "Ship everything" + "zero bugs" | Ask for MVP scope; define quality bar per feature |
| Compatibility vs. modernization | "Support legacy" + "use modern stack" | Define compatibility boundary; identify migration path |
| Cost vs. reliability | "Minimal infrastructure" + "99.99% uptime" | Present cost/reliability curve; ask for target |

When a conflict is detected:

1. **State both requirements explicitly** — "You mentioned X and also Y"
2. **Explain why they conflict** — "These pull in opposite directions because..."
3. **Present 2-3 resolution options** with concrete trade-offs
4. **Ask the user to choose** — never silently resolve a conflict by favoring one requirement over another

## Rules

1. Never proceed with significant uncertainty — ask first
2. Frame questions with context about why you're asking
3. Keep mid-process questions focused and specific
4. One topic per question — don't bundle ambiguities
5. **Never silently resolve conflicting requirements** — always surface the conflict and let the user decide

## Back to

- [Questionnaire framework overview](overview.md)
