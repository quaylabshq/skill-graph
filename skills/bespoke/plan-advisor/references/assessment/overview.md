# Assessment Overview

Plan assessment is the core capability — reading a plan file, extracting its elements, and evaluating it via a sub-agent for quality, completeness, and risk.

## Process

1. **Discover** the plan file (user-provided path or auto-detected)
2. **Parse** the plan into structured elements (goals, steps, risks, dependencies)
3. **Evaluate** via sub-agent against a quality checklist
4. **Report** findings back to the user transparently

## References

| Topic | Reference |
|-------|-----------|
| Plan discovery & parsing | [plan-reading.md](plan-reading.md) |
| Sub-agent evaluation strategy | [sub-agent-evaluation.md](sub-agent-evaluation.md) |

## See Also

- [Activation overview](../activation/overview.md) — must be active before assessment
- [Quality standards](../answering/quality-standards.md) — standards applied during evaluation
- [Activation workflow](../workflows/activation-workflow.md) — assessment as part of activation
