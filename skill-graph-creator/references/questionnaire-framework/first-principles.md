# First-Principles Thinking

The mental model that drives all question generation. Think like a senior staff engineer — decompose the problem to its foundations before building solutions.

## The Model

First-principles thinking means:

1. **Decompose** — Break the problem into its fundamental components
2. **Challenge** — Question every assumption, even "obvious" ones
3. **Trace** — Follow each requirement back to its root need
4. **Synthesize** — Build understanding from verified foundations, not analogies

## Applied to Skill Graph Creation

### Decompose the Request

When asked to create a skill graph, break it down:

- What is the **core capability** being requested?
- What are the **sub-capabilities** needed to support it?
- What **knowledge** does Claude need that it doesn't already have?
- What **tools** (scripts) would make execution reliable?

### Challenge Assumptions

For every piece of information, ask:

- "Is this actually true, or am I inferring it?"
- "Would a different user interpret this differently?"
- "Am I solving the stated problem or a problem I've assumed?"
- "Does this requirement actually need to exist, or is it inherited from a different context?"

### Trace to Root Needs

Requirements often come as solutions rather than problems:

- User says: "I need a script that converts CSV to JSON"
- Root need might be: "I need to integrate data from source A into system B"
- The skill graph might need to address the broader data integration problem, not just the format conversion

### Decompose to Atoms

For every subproblem identified, ask "Can this be broken down further?" Continue until each piece is independently solvable. See [problem decomposition](../core-principles/problem-decomposition.md) for the full recursive test.

### Synthesize from Foundations

Build the skill graph structure from verified components:

- Each reference file addresses a verified need
- Each script solves a confirmed problem
- Each link represents a real relationship
- Nothing exists "just in case"

## Anti-Patterns

1. **Analogy-based design** — "This is like X, so let's structure it the same way" — Verify, don't assume
2. **Inherited complexity** — "Other skills do it this way" — Challenge whether it applies here
3. **Solution-first thinking** — "Let's use a graph database" — Start with the problem, not the tool
4. **Premature specificity** — "The auth module needs 5 reference files" — Determine this from requirements, not intuition

## Beyond Engineering

First-principles thinking applies to non-code aspects with the same rigor:

- **Design taste**: What is the user's visual vocabulary? What do they mean by "clean" or "modern"? Ask for examples.
- **Content strategy**: What tone, voice, and audience are we targeting? Formal or casual? Expert or beginner?
- **Workflow design**: What is the user's actual daily workflow, not just the technical requirements?

Avoid engineering-centric bias — probe the human and subjective dimension with the same rigor as the technical dimension. A skill graph for a design-heavy task that only asks technical questions has failed at first-principles thinking.

## Back to

- [Questionnaire framework overview](overview.md)
- See also: [Initial questions](initial-questions.md) — where first-principles thinking produces concrete questions
