# Mid-Process Questions

How to identify and address gaps discovered during work. Questions are not limited to the beginning — they must happen whenever ambiguity surfaces.

## Triggers for New Questions

Ask new questions when:

1. **Multiple valid approaches exist** — "Should this be split by domain or by feature? The user's input doesn't make this clear."
2. **An assumption is being made** — "I'm assuming the user wants REST, but they haven't said. Should I ask?"
3. **Missing context is discovered** — "This reference needs API documentation that hasn't been provided."
4. **Contradictions appear** — "The user said 'simple' but the requirements imply significant complexity."
5. **Edge cases surface** — "What should happen when the input is empty? Or malformed?"
6. **Decomposition decisions require domain insight** — "I don't know enough about this domain to know where the natural boundaries are."

## How to Identify Gaps Proactively

At each step in the creation process, actively scan for:

- **Implicit assumptions** — What am I assuming that hasn't been stated?
- **Missing definitions** — Are there terms I'm using without a clear definition?
- **Untested boundaries** — Have I explored the edges of the requirements?
- **Dependencies** — Am I relying on something that hasn't been confirmed?

## How to Ask Mid-Process

1. **State what you've discovered** — "While planning the graph structure, I realized there are two ways to organize the authentication references."
2. **Present the options** — "Option A: by auth method (OAuth, JWT, etc.). Option B: by use case (login, API access, etc.)."
3. **Ask for direction** — "Which organization better matches how you think about authentication?"

## Feedback Checkpoint Questions

At each [feedback checkpoint](../creation-process/feedback-checkpoints.md), ask structured validation questions:

- "Here's my understanding of X — is this accurate?"
- "I classified this as [domain profile] — does that match your expectation?"
- "Based on your preferences, I'm leaning toward [approach] — does that direction feel right?"

## Subjective Quality Gate

When producing output for a subjective domain, pause and validate direction before completing:

- "Before I build out the full [thing], here's a preview of the direction — is this what you had in mind?"
- Show concrete early output (first reference file, first design decision) and ask for validation
- Do not complete all files before getting directional confirmation on subjective domains

## Rules

1. Never proceed with significant uncertainty — ask first
2. Frame questions with context about why you're asking
3. Keep mid-process questions focused and specific
4. One topic per question — don't bundle multiple ambiguities

## Back to

- [Questionnaire framework overview](overview.md)
- See also: [Feedback checkpoints](../creation-process/feedback-checkpoints.md)
