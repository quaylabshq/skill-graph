# Domain Expertise

Plan-advisor applies senior/lead engineer knowledge across three domains when answering questions.

## Front-End

| Area | Guidance |
|------|----------|
| Framework choice | Match what's in the project; default to React/Next.js for new projects |
| State management | Start with React state/context; add external stores only when needed |
| Styling | Follow project conventions (Tailwind, CSS modules, styled-components) |
| Component design | Composition over inheritance; small, focused components |
| Performance | Lazy load routes, optimize images, minimize bundle size |
| Accessibility | Semantic HTML first, ARIA only when needed, keyboard navigation |
| Data fetching | Server components where possible; SWR/React Query for client |

## Back-End

| Area | Guidance |
|------|----------|
| API design | RESTful by default; GraphQL only if already in project |
| Database | Use existing ORM/query patterns; prefer migrations over manual SQL |
| Authentication | Use established libraries (NextAuth, Passport); never roll your own |
| Error handling | Typed errors, consistent response format, proper HTTP status codes |
| Validation | Validate at system boundaries (API input, external data); trust internals |
| Architecture | Start with simple request-response; add message queues only when needed |
| Security | OWASP top 10 awareness; parameterized queries; input sanitization |

## Product

| Area | Guidance |
|------|----------|
| Scope decisions | Ship the minimum viable feature; iterate based on feedback |
| UX trade-offs | Prefer convention over configuration; reduce user decisions |
| Feature priority | Core flow first, edge cases second, nice-to-haves last |
| Naming | Clear, descriptive names over clever ones; match domain language |
| Error states | Always design the unhappy path; show actionable error messages |
| Progressive disclosure | Show essentials first; advanced options on demand |

## Cross-Cutting Concerns

- **Testing**: Unit tests for logic, integration tests for workflows, skip testing glue code
- **Logging**: Structured logs at decision points; don't log sensitive data
- **Documentation**: Document "why", not "what"; code should explain "what"
- **Dependencies**: Prefer well-maintained, widely-used packages; fewer is better

## Back to

- [Answering overview](overview.md)
- See also: [Quality standards](quality-standards.md) — general quality dimensions
