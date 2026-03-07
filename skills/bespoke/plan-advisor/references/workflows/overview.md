# Workflows Overview

Plan-advisor has two primary workflows: activation (one-time setup) and question answering (ongoing during active sessions).

## Workflow Summary

| Workflow | Trigger | Steps | Reference |
|----------|---------|-------|-----------|
| Activation | User says "activate plan-advisor" | 9 steps | [activation-workflow.md](activation-workflow.md) |
| Question Answering | Question arises during planning/implementation | 8 steps | [question-answering-workflow.md](question-answering-workflow.md) |

## Workflow Relationship

```
Activation (once) → Assessment → [Q&A loop during implementation] → Deactivation
```

1. User activates plan-advisor
2. Plan-advisor assesses the current plan
3. During implementation, questions are auto-answered
4. User deactivates when done

## See Also

- [Activation overview](../activation/overview.md) — activation concepts
- [Assessment overview](../assessment/overview.md) — plan evaluation details
- [Answering overview](../answering/overview.md) — answer framework
