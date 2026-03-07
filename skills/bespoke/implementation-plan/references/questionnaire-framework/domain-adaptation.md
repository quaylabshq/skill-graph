# Domain Adaptation

Adapt question depth, type, and strategy based on the task's domain profile. Generic questions produce generic plans.

## Adaptation Rules

### Software Engineering Tasks

Focus on: architecture, patterns, constraints, testing strategy, file structure.

Key questions:
- "What existing patterns should I follow in this codebase?"
- "What's the testing expectation — unit, integration, e2e?"
- "Are there performance or scalability concerns?"

### Design & UX Tasks

Focus on: preferences, examples, aesthetics, user experience.

Key questions:
- "Can you show me examples of what you like?"
- "What existing products match your taste?"
- "What should it feel like to use?"
- "What should it NOT look like?"

### Business & Strategy Tasks

Focus on: goals, metrics, stakeholders, constraints, success criteria.

Key questions:
- "What is the desired outcome?"
- "Who are the stakeholders and what do they care about?"
- "What constraints exist (budget, timeline, resources)?"

### Research & Content Tasks

Focus on: audience, depth, sources, format, tone.

Key questions:
- "Who is the audience for this?"
- "What depth of analysis is needed?"
- "What format should the output take?"

### Infrastructure & DevOps Tasks

Focus on: reliability, security, scalability, monitoring, rollback.

Key questions:
- "What are the availability requirements?"
- "What's the rollback strategy if something goes wrong?"
- "Are there compliance or security requirements?"

## Mixed Domain Tasks

When a task spans multiple domains (e.g., full-stack with design), interleave questions from both domains. Don't front-load one type.

## Concrete Signals

If the user mentions: "design", "look", "feel", "style", "brand", "beautiful", "clean", "modern", "aesthetic" → immediately classify as high-subjectivity and shift questioning strategy.

If the user mentions: "performance", "scale", "security", "migrate", "refactor" → deep-probe technical constraints.

## Back to

- [Questionnaire framework overview](overview.md)
- See also: [Domain classification](../planning-process/domain-classification.md)
