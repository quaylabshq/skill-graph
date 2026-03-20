# Step 4.5: Multi-Agent Plan Verification

**Status: MANDATORY — never skip this step.**

After plan generation and before presentation, the plan must pass independent verification by multiple specialized sub-agents. No plan is presented to the user until **all verification agents unanimously agree** it meets the required quality bar.

## Why Verification Is Non-Negotiable

A plan is a contract. If the plan is flawed, implementation amplifies the flaw. NASA does not launch on one engineer's sign-off. Google does not ship on one reviewer's approval. Every plan — regardless of domain — must survive independent scrutiny from multiple specialized perspectives before it reaches the user.

## Verification Agents

Launch all verification agents **in parallel** using the Agent tool. Each agent receives the full plan, the original user requirements, the research findings, and the decomposition output. Each agent evaluates independently — they do not see each other's results.

### Default Agent Panel (minimum 3, always present)

| Agent | Role | Focus | subagent_type |
|-------|------|-------|---------------|
| **Requirements Traceability Agent** | Completeness | Every user requirement, clarification answer, and research finding maps to a specific plan step. Nothing dropped, nothing orphaned. | `general-purpose` |
| **Technical Rigor Agent** | Correctness | Architecture is sound, dependency ordering is valid, complexity signals are accurate, patterns match codebase conventions, no logical gaps. For code tasks: would this plan pass a Google/NASA design review? | `general-purpose` |
| **Security & Threat Agent** | Security | Threat modeling, attack surface analysis, data flow risks, authentication/authorization gaps, injection vectors, supply chain concerns, compliance implications. | `general-purpose` |

### Conditional Agents (added based on domain profile)

| Agent | When to Add | Focus | subagent_type |
|-------|-------------|-------|---------------|
| **Fault Tolerance Agent** | High-technical or infrastructure tasks | Failure modes, cascading failures, retry/fallback strategies, graceful degradation, data loss scenarios, rollback completeness | `general-purpose` |
| **Scalability & Performance Agent** | Tasks with scale/performance concerns | Bottleneck identification, resource contention, algorithmic complexity, caching strategy, load distribution | `general-purpose` |
| **Consistency & Standards Agent** | High-scope tasks spanning multiple areas | Cross-step consistency, naming/convention adherence, API contract alignment, style uniformity across the plan | `general-purpose` |
| **User-Requested Agent(s)** | When the user requests additional verification dimensions | Custom focus as specified by the user | `general-purpose` |

The user may request more agents at any time. Honor all such requests.

## Agent Prompt Template

Each agent receives a structured prompt. Adapt the `{FOCUS_AREA}` and `{EVALUATION_CRITERIA}` per agent role:

```
You are a verification agent responsible for: {AGENT_ROLE}.

## Your Task

Independently evaluate the following implementation plan against {FOCUS_AREA}.

## Inputs

### Original User Requirements
{requirements}

### Clarification Q&A
{clarification_answers}

### Research Findings
{research_findings}

### Decomposition
{decomposition}

### The Plan
{plan}

## Evaluation Criteria

{EVALUATION_CRITERIA}

## Your Output

Produce a structured verdict:

### Verdict: PASS | FAIL | CONDITIONAL PASS

### Issues Found (if any)
For each issue:
- **Severity**: Critical / Major / Minor
- **Location**: Which plan section or step
- **Description**: What is wrong
- **Recommendation**: How to fix it

### Confirmation (if PASS)
- Bullet list of what you verified and why it passes

Be rigorous. Do not rubber-stamp. If you are uncertain about something, flag it.
A CONDITIONAL PASS means the plan is mostly sound but has Minor issues that
should be addressed. A FAIL means Critical or Major issues exist.
```

## Agent-Specific Evaluation Criteria

### Requirements Traceability Agent

```
1. Every user requirement stated during clarification has a corresponding plan step
2. Every research finding that impacts the plan is reflected in a step or decision
3. Every decomposed subtask appears in the implementation steps
4. No plan step exists without a traceable origin (requirement, research, or decomposition)
5. Success criteria from clarification are verifiable against the plan
6. Scope boundaries are respected — nothing added beyond what was agreed
7. Every plan step has well-defined acceptance criteria ("Done when" is specific,
   observable, and complete — not vague or aspirational)
8. Acceptance criteria collectively cover both success and failure paths
9. No conflicting requirements exist unresolved — if two criteria contradict,
   the conflict must be explicitly resolved in the plan
```

### Technical Rigor Agent

```
1. Architecture decisions are sound and justified
2. Dependency ordering between steps is correct — no circular or missing dependencies
3. Complexity signals (straightforward/investigation/high-risk) are accurate
4. For codebase tasks: patterns match existing codebase conventions
5. No logical gaps — each step's output is sufficient input for the next
6. Edge cases identified during research are handled in the plan
7. GOAL-DRIVEN VALIDATION:
   - Every step's acceptance criteria are defined BEFORE the approach
   - For code tasks: test specifications are precise enough to write tests from
     (not "add tests" but "test X returns Y when given Z")
   - For non-code tasks: criteria are observable and could be evaluated by two
     independent reviewers reaching the same conclusion
   - The approach in each step is the minimum needed to satisfy its criteria
8. The plan would survive a design review at Google or NASA:
   - Every decision has documented rationale
   - Failure modes are acknowledged
   - No unstated assumptions
   - Correctness is provable or verifiable at each step
```

### Security & Threat Agent

```
1. THREAT MODELING: Identify attack surfaces introduced or modified by the plan
2. DATA FLOW: Trace sensitive data through the plan — where is it created,
   stored, transmitted, and destroyed?
3. AUTH/AUTHZ: Are authentication and authorization concerns addressed for
   every entry point?
4. INPUT VALIDATION: Does the plan account for untrusted input at system boundaries?
5. INJECTION VECTORS: SQL injection, XSS, command injection, path traversal —
   are relevant vectors addressed?
6. SUPPLY CHAIN: Are new dependencies vetted? Are version pins specified?
7. SECRETS MANAGEMENT: Are secrets, keys, and tokens handled correctly?
8. COMPLIANCE: Are regulatory or policy requirements (GDPR, SOC2, HIPAA, etc.)
   addressed if applicable?
9. FAILURE SECURITY: Does the system fail secure (deny by default) or fail open?
10. LOGGING & AUDIT: Are security-relevant events logged without leaking sensitive data?
```

### Fault Tolerance Agent (conditional)

```
1. What happens when each external dependency fails?
2. Are retry strategies defined with backoff and circuit breaking?
3. Is there graceful degradation or does partial failure cascade?
4. Are data loss scenarios identified and mitigated?
5. Is the rollback strategy complete and tested?
6. Are timeout values and resource limits specified?
```

## Consensus Loop

```
┌─────────────────────────────────────────┐
│           Generate Plan (Step 4)        │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│     Launch All Verification Agents      │
│         (parallel execution)            │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│       Compile Agent Verdicts            │
│                                         │
│  All PASS or CONDITIONAL PASS?          │
│  ┌─── YES ──► Proceed to Step 5        │
│  │                                      │
│  └─── NO ───► Revision Required         │
└──────────────────┬──────────────────────┘
                   │ (on FAIL)
                   ▼
┌─────────────────────────────────────────┐
│         Revise Plan                     │
│                                         │
│  1. Collect all Critical/Major issues   │
│  2. Group by plan section               │
│  3. Apply fixes to the plan             │
│  4. If fixes require new information:   │
│     → return to Step 1 or Step 2        │
│  5. Re-run ALL agents on revised plan   │
│     (not just the ones that failed)     │
└──────────────────┬──────────────────────┘
                   │
                   ▼
              (back to top)
```

### Loop Rules

1. **All agents re-verify on every revision** — a fix for one agent's issue may introduce a new issue for another
2. **Maximum 3 revision loops** before escalating to the user — "The plan has failed verification 3 times. Here are the unresolved issues: [issues]. How would you like to proceed?"
3. **CONDITIONAL PASS with only Minor issues** — the plan may proceed if all agents are CONDITIONAL PASS or PASS, but Minor issues must be listed in the plan's Open Questions section
4. **Any Critical issue** from any agent is an automatic FAIL — the loop continues
5. **Track what changed** between revisions — each loop iteration should note what was fixed and why

## Verification Report

After all agents reach consensus (all PASS or CONDITIONAL PASS), compile a verification summary to include with the plan presentation in Step 5:

```markdown
## Verification Report

**Status**: Verified — [N] agents passed on iteration [M]

| Agent | Verdict | Key Findings |
|-------|---------|--------------|
| Requirements Traceability | PASS | All [X] requirements traced to plan steps |
| Technical Rigor | PASS | Architecture sound, dependencies validated |
| Security & Threat | CONDITIONAL PASS | Minor: consider rate limiting on endpoint X |
| [Additional agents...] | ... | ... |

**Iterations**: [How many loops were needed]
**Issues Resolved**: [Count of issues fixed during verification]
**Residual Minor Issues**: [Any CONDITIONAL PASS items listed here]
```

## Adapting Agent Count

| Scenario | Minimum Agents |
|----------|----------------|
| Simple codebase task | 3 (Requirements + Technical + Security) |
| Complex codebase task | 4-5 (add Fault Tolerance, Scalability) |
| Infrastructure/DevOps | 4 (add Fault Tolerance) |
| Non-code task | 3 (Requirements + Technical Rigor + Security relevance check) |
| User requests more | Add as requested — no upper limit |

For non-code tasks, the Security agent evaluates whether the plan has security-relevant implications (e.g., a business strategy involving user data still needs privacy analysis). If the task has zero security surface, the agent's verdict should note "No security surface identified — PASS by inspection."

## Rules

1. **Never skip verification** — every plan goes through the agent panel
2. **Never present a plan that has unresolved Critical or Major issues**
3. **All agents re-run on revisions** — partial re-verification is not allowed
4. **The user can add agents** — always honor requests for additional verification dimensions
5. **Escalate after 3 failed loops** — do not loop indefinitely; surface the conflict to the user
6. **Verification agents must be independent** — they do not see each other's verdicts during evaluation
7. **Include the verification report** when presenting the plan in Step 5

## Back to

- [Planning process overview](overview.md)
- See also: [Step 4 — Generate Plan](step-4-generate-plan.md)
- See also: [Step 5 — Present](step-5-present.md)
