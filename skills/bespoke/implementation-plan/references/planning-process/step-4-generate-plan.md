# Step 4: Generate Plan

Turn the research findings and decomposed subtasks into a structured implementation plan. Use the [core template](../output-format/core-template.md) as the foundation and add [adaptive sections](../output-format/adaptive-sections.md) based on the domain.

**Quality standard**: Every plan must be generated as if it will be submitted for a Google design review or a NASA mission-critical systems review. This is not aspirational — it is the baseline. See the [quality doctrine](#quality-doctrine-googlenasa-grade-reasoning) below.

## Plan Generation Process

1. **Select plan depth** based on [domain classification](domain-classification.md):
   - Simple → summary + steps list only
   - Moderate → full core template
   - Complex → core template + all relevant adaptive sections

2. **Fill core template sections using criteria-first structure** (see [core-template.md](../output-format/core-template.md)):
   - Summary: one-paragraph overview of approach
   - Approach: key decisions and rationale
   - Implementation steps: **criteria-first** — each step starts with "Done when" and "Verified by" before "Approach". Acceptance criteria come from the decomposition output (Step 3). See [goal-driven methodology](../goal-driven-methodology/overview.md).
   - Files affected: from codebase research (if applicable)

3. **For code tasks, apply TDD structure** (see [technical TDD](../goal-driven-methodology/technical-tdd.md)):
   - Every step's "Verified by" must include specific test specifications
   - Test specifications must be precise enough to write tests directly from
   - Test and implementation steps should interleave, not batch all tests at the end

4. **For non-code tasks, apply acceptance criteria** (see [non-technical criteria](../goal-driven-methodology/non-technical-criteria.md)):
   - Every step's "Verified by" must include an observable evaluation method
   - Criteria must pass the litmus test: "Could two independent reviewers reach the same conclusion?"

5. **Add adaptive sections** as needed (see [adaptive-sections.md](../output-format/adaptive-sections.md)):
   - Architecture decisions for complex systems
   - Risk assessment for high-stakes tasks
   - Testing strategy for code tasks
   - Alternatives considered for novel domains

6. **Map dependencies** into the step ordering:
   - Independent steps can be labeled as parallelizable
   - Dependent steps are sequenced with explicit dependencies noted

7. **Estimate complexity signals** (not time):
   - Mark steps as "straightforward", "needs investigation", or "high-risk"
   - This helps the user understand where challenges are, without guessing duration

8. **Apply the quality doctrine** — run every plan section through the NASA/Google quality gate before considering the plan ready for verification

## Quality Doctrine: Google/NASA-Grade Reasoning

This doctrine applies to **every plan**, not just complex ones. Simple plans are held to the same rigor — they just have fewer sections.

### The Standard

Ask: *"Would a senior Google staff engineer approve this design doc? Would a NASA flight director trust this plan for a mission-critical system?"* If the answer is not a confident yes, the plan is not ready.

### Mandatory Quality Properties

Every plan must demonstrate these properties:

| Property | Meaning | How to Apply |
|----------|---------|--------------|
| **Zero unstated assumptions** | Every assumption is written down explicitly | Audit each step: "What am I assuming here that is not written in the plan?" — if anything, write it down or validate it |
| **Goal-driven structure** | Criteria come before approach | Every step starts with acceptance criteria, then the approach to satisfy them. This is TDD at the planning level. See [goal-driven methodology](../goal-driven-methodology/overview.md) |
| **Provable correctness** | Each step's output can be verified | Define what "done" looks like for every step — not "implement X" but "implement X, verified by Y" |
| **Documented rationale** | Every decision explains WHY, not just WHAT | For every choice in the plan, there must be a sentence starting with "because" or "this was chosen over X because" |
| **Failure mode awareness** | The plan acknowledges what can go wrong | Each high-risk or investigation step must note its primary failure mode and what happens if it fails |
| **Defense in depth** | No single point of failure in the plan | If step N fails, the plan should not silently corrupt everything downstream — there should be a checkpoint or validation |
| **Minimal blast radius** | Changes are scoped tightly | Each step should change as little as possible. If a step touches 10 files, ask: "Can this be split into smaller, independently verifiable steps?" |
| **Reversibility** | Changes can be undone | For codebase tasks, every step that modifies state should note whether it is reversible and how |

### Rigor by Domain

| Domain | Additional Rigor |
|--------|-----------------|
| **Software engineering** | Every API change has a contract. Every state mutation has a validation. Every external call has a failure handler. Test strategy covers happy path, error path, and edge cases. |
| **Infrastructure/DevOps** | Rollback strategy for every step. Blast radius defined. Health checks specified. No manual steps without runbook. |
| **Data/Migration** | Data integrity checks before, during, and after. Backup strategy. Row count validation. Idempotency guaranteed. |
| **Design/UX** | Accessibility requirements stated. Responsive behavior defined. Interaction states enumerated (default, hover, active, disabled, error, loading). |
| **Business/Strategy** | Success metrics are measurable. Assumptions are falsifiable. Stakeholder impacts are mapped. |

### Anti-Patterns to Reject

The following patterns indicate the plan is **not** at the required quality bar:

- "Implement the feature" — too vague; what specifically gets built and how is it verified?
- Steps without verification criteria — how do you know it works?
- Missing error handling — what happens when things fail?
- Assumptions baked into steps without being called out — "this assumes the API returns JSON" should be explicit
- "Update tests" as a single step — which tests, what scenarios, what coverage?
- No rollback awareness — what if step 3 breaks production?

## Quality Checks

Before moving to [verification (step 4.5)](step-4.5-verification.md):

- Does every decomposed subtask appear in the plan?
- Does the plan address every concern raised during clarification?
- Does the plan incorporate research findings?
- Are the steps ordered correctly given dependencies?
- Is the detail level appropriate for the task complexity?
- **Does every decision have documented rationale?**
- **Does every step have a verification criterion?**
- **Are all assumptions explicitly stated?**
- **Are failure modes acknowledged for high-risk steps?**
- **Would this survive a Google/NASA design review?**
- **Does every step have acceptance criteria defined BEFORE the approach?**
- **For code tasks: are test specifications precise enough to write tests from?**
- **For non-code tasks: are criteria observable and evaluatable?**

## Rules

1. Never generate a plan without completing steps 1-3 first
2. Use the output format framework — don't invent ad-hoc structures
3. If generating the plan reveals ambiguity, return to [step 1](step-1-clarification.md)
4. Do not include time estimates — use complexity signals instead
5. **Apply the quality doctrine to every plan** — no exceptions, no "good enough"
6. **Criteria before approach** — every step is structured acceptance-criteria-first. See [goal-driven methodology](../goal-driven-methodology/overview.md)
7. **After generation, the plan proceeds to [step 4.5 — verification](step-4.5-verification.md)** — not directly to presentation

## Back to

- [Planning process overview](overview.md)
- Next: [Step 4.5 — Multi-Agent Verification](step-4.5-verification.md)
- See also: [Goal-driven methodology](../goal-driven-methodology/overview.md) — criteria-first planning
- See also: [Technical TDD](../goal-driven-methodology/technical-tdd.md) — TDD for code tasks
- See also: [Non-technical criteria](../goal-driven-methodology/non-technical-criteria.md) — acceptance criteria for non-code tasks
- See also: [Output format overview](../output-format/overview.md)
- See also: [Core template](../output-format/core-template.md)
- See also: [Adaptive sections](../output-format/adaptive-sections.md)
