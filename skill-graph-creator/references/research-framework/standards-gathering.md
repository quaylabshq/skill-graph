# Standards Gathering

How to identify and apply implementation-relevant standards when building a skill graph.

## Types of Standards

### Industry Standards

Formal specifications that govern how things should work:

- File format specifications (PDF, DOCX, JSON Schema)
- Protocol specifications (HTTP, WebSocket, gRPC)
- Security standards (OWASP, SOC 2, GDPR)
- Accessibility standards (WCAG)

### Framework Conventions

Unofficial but widely adopted patterns:

- Framework-specific project structures (Rails conventions, Next.js app directory)
- Language idioms (Python PEP 8, Go conventions)
- API design conventions (REST, GraphQL best practices)
- Testing conventions (unit, integration, e2e patterns)

### Community Patterns

Patterns established through common practice:

- Common CLI argument patterns
- Configuration file formats and locations
- Error handling and logging conventions
- Documentation organization patterns

## How to Identify Relevant Standards

1. **Start from the domain** — What domain does the skill graph serve?
2. **Identify the technology stack** — What tools and frameworks are involved?
3. **Search for specifications** — Are there formal specs for the technologies?
4. **Search for conventions** — What are the accepted patterns in this ecosystem?
5. **Validate relevance** — Does this standard actually impact the skill graph design?

## Applying Standards to Graph Design

Standards inform:

- **Reference content** — Standards should be accurately represented in reference files
- **Script implementation** — Scripts should follow relevant coding standards
- **File organization** — Graph structure should mirror domain conventions where applicable
- **Naming** — Use standard terminology consistently

## Rules

1. Only gather standards that impact the skill graph — skip tangentially related ones
2. Reference standards, don't duplicate them — link to official docs when possible
3. When standards conflict with user requirements, the user's requirements take precedence (but note the conflict)

## Back to

- [Research framework overview](overview.md)
