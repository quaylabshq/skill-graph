# Technical TDD Planning

For all code tasks, the plan must be structured as **Test-Driven Development at the planning level**. Define what tests to write BEFORE defining what code to write. The tests are not an afterthought — they are the specification that drives the implementation.

## The TDD Planning Principle

When planning a code task, do not ask "what code do I need to write?" Ask instead: "what tests would prove this step is done correctly?" Then plan the code to pass those tests.

This applies at every level:
- **Plan level**: The overall success criteria map to the acceptance test suite
- **Step level**: Each step's acceptance criteria map to specific tests
- **Substep level**: Even within a step, the order is test → implementation

## How It Changes Plan Steps

### Before (activity-driven)

```
1. **Add user validation** — Add input validation to the user registration endpoint
   - Files: src/routes/users.ts
```

### After (TDD-driven)

```
1. **Add user validation** `straightforward`
   - Done when:
     - Registration rejects emails without @ symbol (returns 400)
     - Registration rejects passwords under 8 characters (returns 400)
     - Registration rejects duplicate emails (returns 409)
     - Valid registration still succeeds (returns 201)
   - Tests to write:
     - Unit: `test/validation/user.test.ts` — email format, password length, field presence
     - Integration: `test/routes/users.test.ts` — duplicate email handling, success path
   - Approach: Add Zod schema validation in middleware, check uniqueness against DB
   - Files: src/routes/users.ts (modify), src/validation/user.ts (create), test/... (create)
   - Depends on: none
```

The "after" version is **falsifiable**. You can look at it and determine exactly whether the step is done. The "before" version is aspirational — "add validation" could mean anything.

## Test Specification by Change Type

| Change Type | What Tests to Specify |
|-------------|----------------------|
| **New feature** | Happy path, validation/rejection cases, edge cases, integration with existing features |
| **Bug fix** | Regression test proving the bug (fails before fix, passes after), related edge cases |
| **Refactor** | Existing tests still pass (specify which), new tests for any exposed interfaces |
| **API change** | Contract tests (request/response shape), backward compatibility tests if needed |
| **Performance** | Benchmark tests with specific thresholds (e.g., "p95 < 200ms with 1000 concurrent requests") |
| **Migration** | Data integrity tests (row counts, checksums), rollback verification, idempotency tests |

## Test Level Selection

For each plan step, decide which test levels are needed:

| Level | When Required | Criteria Focus |
|-------|---------------|----------------|
| **Unit tests** | Always for new logic | Isolated function behavior, edge cases, error paths |
| **Integration tests** | When step involves 2+ components | Component interaction, data flow, API contracts |
| **E2E tests** | When step affects user-visible behavior | User workflow completion, cross-system validation |
| **Performance tests** | When step has performance criteria | Latency, throughput, resource usage under load |
| **Security tests** | When step handles auth, input, or sensitive data | Auth bypass attempts, injection, privilege escalation |

## How to Write Test Specifications in Plans

Test specifications in the plan are NOT full test code — they are **precise descriptions of what the test asserts**. They must be specific enough that the test can be written directly from the specification.

### Good Test Specification

```
- Unit: `test/auth/token.test.ts`
  - generateToken(user) returns a JWT with { sub: user.id, role: user.role, exp: +1h }
  - generateToken(null) throws InvalidUserError
  - validateToken(expired_token) returns { valid: false, reason: "expired" }
  - validateToken(tampered_token) returns { valid: false, reason: "signature" }
```

### Bad Test Specification

```
- Unit tests for token generation and validation
```

The bad version doesn't tell you what to test. The good version is a contract — you could write the test file directly from it.

## Existing Test Pattern Discovery

During [Step 2 (Research)](../planning-process/step-2-research.md), the codebase exploration must discover:

1. **Test framework**: What testing library is used? (Jest, Vitest, pytest, Go testing, etc.)
2. **Test location**: Where do tests live? (co-located, `test/` directory, `__tests__/`, etc.)
3. **Test style**: How are tests structured? (describe/it, test functions, table-driven, etc.)
4. **Test helpers**: Are there test utilities, factories, fixtures, or mocks to reuse?
5. **Coverage expectations**: Is there a coverage threshold? What's the current coverage?

The plan must follow these existing patterns — do not introduce a new test framework or style.

## TDD Step Ordering

When a plan has multiple steps, the TDD principle also applies to step ordering:

1. **Write tests for the lowest-level components first** — these are the foundation
2. **Implement those components to pass the tests**
3. **Write integration tests for how components interact**
4. **Implement the integration layer**
5. **Write e2e tests for the user-visible behavior**
6. **Verify end-to-end**

This means the plan's step ordering should interleave test-writing and implementation, not batch all tests at the end.

## Rules

1. **Every code plan step must specify tests BEFORE specifying implementation**
2. **Test specifications must be precise** — not "add tests" but "test X returns Y when given Z"
3. **Follow existing test patterns** — discovered during research
4. **Regression tests are mandatory for bug fixes** — the test must fail before the fix and pass after
5. **No plan step can be marked "done" without its tests passing**
6. **Test and implementation steps interleave** — do not batch all tests at the end

## Back to

- [Goal-driven methodology overview](overview.md)
- [Step 4 — Generate Plan](../planning-process/step-4-generate-plan.md)
