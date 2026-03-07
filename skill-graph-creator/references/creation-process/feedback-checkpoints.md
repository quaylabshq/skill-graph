# Feedback Checkpoints

Do not wait until step 8 (iterate) to get feedback. Validate understanding and direction at multiple points during creation.

## Mandatory Checkpoints

| After Step | Checkpoint Action |
|------------|-------------------|
| 0.5 (Domain Classification) | "Here's how I classified your task — does this match?" |
| 1 (Clarification) | "Here's my understanding of your requirements — what did I miss?" |
| 2 (Research) | "Here's what I found — anything I should look into further?" |
| 4 (Plan) | "Here's the proposed graph structure — does this cover everything?" |
| 6 (Implement) | For subjective domains: show early output and ask "Is this the direction you want?" |

## Feedback Quality Rules

1. Present your understanding concretely, not abstractly — show the actual structure, content, or design decisions
2. Ask specific questions about gaps — not "does this look good?"
3. Incorporate feedback before proceeding — do not acknowledge and ignore
4. If feedback contradicts earlier answers, surface the contradiction explicitly: "Earlier you said X, but now Y — which should I follow?"

## Refinement Loop

```
Checkpoint → Present understanding → Gather feedback → Refine → Proceed
```

Each checkpoint should converge — fewer unknowns each time. If a checkpoint introduces MORE unknowns than it resolves, return to the relevant earlier step.

## Checkpoint vs Pre/Post Eval

Checkpoints are user-facing validation moments (you present and ask). Pre/post eval (see [pre-post-eval.md](pre-post-eval.md)) is internal self-assessment. Both are required — they serve different purposes.

## Back to

- [Creation process overview](overview.md)
- See also: [Mid-process questions](../questionnaire-framework/mid-process-questions.md)
- See also: [Pre/post evaluation](pre-post-eval.md)
