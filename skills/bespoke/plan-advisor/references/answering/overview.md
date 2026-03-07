# Answering Overview

When plan-advisor is active, it auto-answers questions that arise during planning and implementation workflows. All answers are displayed transparently — both the question and the answer are shown to the user.

## Answer Mode: Auto-Answer + Show

When a question arises (e.g., via AskUserQuestion during plan mode or implementation):

1. **Intercept** the question before it reaches the user
2. **Generate** an answer at senior/lead engineer quality
3. **Display** both Q and A transparently to the user
4. **Continue** the workflow with the generated answer

## Display Format

```
[Plan Advisor] Auto-answering:

Q: <the original question>
A: <the generated answer>

Rationale: <brief reasoning for the choice>
```

## When to Auto-Answer

- Architecture and design decisions
- Technology and library choices
- Implementation approach questions
- File organization and naming
- API design decisions
- Testing strategy questions

## When NOT to Auto-Answer

- Questions about user-specific preferences (credentials, names, branding)
- Deployment target or environment questions
- Budget or resource allocation
- Questions the user explicitly flagged as "ask me"
- Anything requiring access the advisor doesn't have

## References

| Topic | Reference |
|-------|-----------|
| Quality dimensions & anti-patterns | [quality-standards.md](quality-standards.md) |
| FE, BE, product expertise | [domain-expertise.md](domain-expertise.md) |

## See Also

- [Q&A workflow](../workflows/question-answering-workflow.md) — step-by-step answering sequence
- [Assessment overview](../assessment/overview.md) — plan context informs answers
