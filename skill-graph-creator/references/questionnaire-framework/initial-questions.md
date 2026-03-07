# Initial Questions

A general thinking model for generating upfront questions dynamically. This is not a list of hardcoded questions — it is a framework for deriving the right questions from any domain.

## Step 0: Domain Classification

Before asking any questions, classify the task using [domain-classification.md](../creation-process/domain-classification.md). The classification determines which categories below get deep probing vs. light touch.

- High-subjectivity → categories 7, 4, 1 get deepest probing
- High-technical → categories 2, 5, 6 get deepest probing
- Always cover all categories, but depth varies based on domain

## Question Categories

When approaching any skill graph creation, generate questions across these categories:

### 1. Scope & Boundaries

What is included? What is explicitly excluded? Where does this skill's responsibility end and another's begin?

Thinking triggers:
- What are the core capabilities this skill must provide?
- What adjacent capabilities should be explicitly out of scope?
- Are there related tools or skills that this overlaps with?

### 2. Technical Constraints

What tools, languages, platforms, APIs, or frameworks are involved? What are the hard constraints?

Thinking triggers:
- What technology stack is assumed or required?
- Are there version constraints or compatibility requirements?
- What external dependencies exist?
- What execution environment will this run in?

### 3. Quality Requirements

What level of detail, correctness, coverage, and polish is expected?

Thinking triggers:
- How critical is correctness? (Is this a safety system or a convenience tool?)
- What level of documentation is appropriate?
- Are there performance requirements?
- What error handling is expected?

### 4. User Expectations

Who is the user? What is their skill level? What do they expect to happen?

Thinking triggers:
- Who triggers this skill? (Developer, non-technical user, automated system?)
- What does the user expect to provide as input?
- What does the user expect to receive as output?
- What experience level should the skill assume?

### 5. Integration Points

What does this skill connect to? What does it depend on? What depends on it?

Thinking triggers:
- What external APIs or services does this interact with?
- Are there authentication or authorization requirements?
- What data formats are used for input/output?
- Are there other skills or tools this needs to work with?

### 6. Deployment Context

Where and how will this skill be used?

Thinking triggers:
- Is this for a specific project or general-purpose use?
- What operating systems or environments must be supported?
- Are there security or compliance requirements?
- What is the expected lifetime of this skill?

### 7. Taste & Preferences

**MANDATORY for domains classified as high-subjectivity.** What does the user want this to look, feel, and read like?

Thinking triggers:
- What existing products or designs does the user admire?
- What aesthetic direction — minimal, bold, playful, corporate, editorial?
- Are there specific examples or references to follow? (Ask for URLs, screenshots, names)
- What should it feel like to use?
- What should it NOT look like?
- What design system, color palette, or typography preferences exist?

For subjective decisions, ask for concrete references — not abstract descriptions. "Show me an example" is more useful than "describe your style."

See also: [Subjective vs objective](subjective-vs-objective.md) for deciding when this category applies.

### 8. Success Criteria

How will we know this skill graph is complete and correct?

Thinking triggers:
- How will we know this skill is done?
- What is the minimum viable version?
- What is the stretch goal?
- How will quality be judged — objectively (passes tests) or subjectively (looks right, feels right)?

## How to Apply

1. Classify the domain first (see Step 0 above)
2. Scan all eight categories before asking any questions
3. Weight categories by domain profile — subjective domains probe 7, 4, 1 deepest; technical domains probe 2, 5, 6 deepest
4. Formulate 3–5 specific questions targeting the highest-uncertainty, highest-weight areas
5. Ask those first, then follow up based on answers
6. Repeat until all categories have sufficient clarity

## Back to

- [Questionnaire framework overview](overview.md)
- See also: [First-principles thinking](first-principles.md) — the reasoning model behind these categories
