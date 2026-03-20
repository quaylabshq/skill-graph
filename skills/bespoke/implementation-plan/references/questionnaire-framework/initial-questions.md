# Initial Questions

A thinking model for generating upfront questions dynamically. This is not a hardcoded list — it is a framework for deriving the right questions from any domain.

## Step 0: Domain Classification

Before asking any questions, classify the task using [domain-classification.md](../planning-process/domain-classification.md). The classification determines which categories below get deep probing vs. light touch.

- High-subjectivity → categories 7, 4, 1 get deepest probing
- High-technical → categories 2, 5, 6 get deepest probing
- Always cover all categories, but depth varies

## Question Categories

### 0. Problem Validation

Is this the right problem to solve? Should we be doing this at all?

Thinking triggers:
- Is the stated problem the actual problem, or a symptom of something deeper?
- Has this been attempted before? What happened?
- What happens if we do nothing?
- Is the user solving the right problem at the right level of abstraction?
- Are there simpler alternatives that achieve the same underlying goal?

**This category is always probed first** — before scope, before constraints, before anything else. If the problem itself is wrong, nothing downstream matters. Even one question from this category ("What happens if we don't do this?") can save an entire planning cycle.

### 1. Scope & Boundaries

What is included? What is excluded? Where does this task end?

Thinking triggers:
- What are the core deliverables?
- What adjacent work should be explicitly out of scope?
- Is there a minimum viable version vs. a stretch goal?

### 2. Technical Constraints

What tools, languages, platforms, APIs, frameworks, or patterns are involved?

Thinking triggers:
- What technology stack is assumed or required?
- Are there version or compatibility constraints?
- What existing patterns should be followed?

### 3. Quality Requirements

What level of correctness, coverage, and polish is expected?

Thinking triggers:
- How critical is correctness? (Safety system vs. quick prototype?)
- What testing expectations exist?
- What error handling is needed?

### 4. User/Stakeholder Expectations

Who cares about this? What do they expect?

Thinking triggers:
- Who is the end user of this work?
- What does success look like to them?
- Are there existing examples to match?

### 5. Integration Points

What does this connect to? Dependencies?

Thinking triggers:
- What existing code/systems does this interact with?
- What APIs, databases, or services are involved?
- What other work depends on this?

### 6. Environment & Context

Where does this run? What constraints exist?

Thinking triggers:
- What deployment environment?
- Are there performance, security, or compliance requirements?
- What is the expected lifetime of this work?

### 7. Preferences & Taste

**Deep probe for high-subjectivity domains.** What should this look/feel/read like?

Thinking triggers:
- What existing products or designs does the user admire?
- What aesthetic direction is preferred?
- What should it NOT look like?

### 8. Success Criteria

How will we know this is done and correct?

Thinking triggers:
- What is the definition of done?
- How will quality be judged?
- What would make this a failure?

## How to Apply

1. Classify the domain first
2. **Always start with category 0 (Problem Validation)** — at least one question challenging the premise
3. Scan all nine categories
4. Weight by domain profile — subjective domains probe 7, 4, 1 deepest; technical domains probe 2, 5, 6 deepest
5. Formulate 3–5 specific questions targeting highest-uncertainty, highest-weight areas
6. Ask those first, then follow up based on answers
7. Repeat until all categories have sufficient clarity

## Back to

- [Questionnaire framework overview](overview.md)
