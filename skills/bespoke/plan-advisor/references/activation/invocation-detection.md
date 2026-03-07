# Invocation Detection

Rules for detecting when the user wants to activate or deactivate plan-advisor.

## Activation Trigger Phrases

Match any of these patterns (case-insensitive):

- "use plan-advisor"
- "activate plan-advisor"
- "enable plan-advisor"
- "start plan-advisor"
- "turn on plan-advisor"
- "plan-advisor on"

## Deactivation Trigger Phrases

- "stop plan-advisor"
- "deactivate plan-advisor"
- "disable plan-advisor"
- "turn off plan-advisor"
- "plan-advisor off"

## Detection Rules

1. **Exact skill name required** — must reference "plan-advisor" explicitly
2. **Case-insensitive** — "Plan-Advisor", "PLAN-ADVISOR", "plan-advisor" all match
3. **No implicit activation** — entering plan mode or discussing plans does NOT activate the advisor
4. **No partial matches** — "use the advisor" or "plan something" do not trigger activation
5. **Immediate response** — on detection, acknowledge activation/deactivation before proceeding

## Back to

- [Activation overview](overview.md)
