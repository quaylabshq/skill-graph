# Question Answering Workflow

The 8-step sequence executed when a question arises during an active plan-advisor session.

## Steps

### 1. Detect Question
- A question arises during planning or implementation (e.g., AskUserQuestion, implementation choice)
- Plan-advisor is confirmed active via state file

### 2. Classify Question
- Determine if this is an auto-answerable question (see [answering overview](../answering/overview.md))
- If not auto-answerable (user preferences, credentials, etc.), let it pass through to the user

### 3. Gather Context
- Read the current plan from the state file's `plan-file` path
- Consider the assessment findings (strengths, gaps, risks)
- Review the immediate implementation context

### 4. Determine Domain
- Classify the question as front-end, back-end, product, or cross-cutting
- Apply domain-specific expertise (see [domain-expertise.md](../answering/domain-expertise.md))

### 5. Generate Answer
- Apply quality standards (see [quality-standards.md](../answering/quality-standards.md))
- Choose the simplest correct option that fits existing patterns
- Prepare a brief rationale

### 6. Display Transparently
- Show both the question and answer in the display format:
  ```
  [Plan Advisor] Auto-answering:

  Q: <question>
  A: <answer>

  Rationale: <reasoning>
  ```

### 7. Apply Answer
- Use the generated answer to continue the workflow
- The answer functions as if the user had selected/typed it

### 8. Log Decision
- The answer is visible in the conversation history
- No separate logging needed — transparency is built into the display

## Back to

- [Workflows overview](overview.md)
- See also: [Activation workflow](activation-workflow.md) — how the session started
