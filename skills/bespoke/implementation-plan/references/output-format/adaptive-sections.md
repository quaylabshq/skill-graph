# Adaptive Sections

Additional plan sections added based on domain and complexity. These are appended after the core template sections when relevant.

## When to Add Adaptive Sections

Add sections based on the [domain classification](../planning-process/domain-classification.md) profile:

| Section | Add When |
|---------|----------|
| Architecture Decisions | Task involves structural choices between valid approaches |
| Risk Assessment | High-stakes task, or research revealed significant risks |
| Testing Strategy | Codebase task that modifies behavior |
| Migration Plan | Task involves data or system migration |
| Alternatives Considered | Multiple valid approaches were evaluated during research |
| Open Questions | Unresolved questions that may affect implementation |
| Rollback Strategy | Task modifies production systems or shared state |

## Section Templates

### Architecture Decisions

```markdown
## Architecture Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| [Decision point] | [What was chosen] | [Why] |
```

### Risk Assessment

```markdown
## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk description] | Low/Med/High | Low/Med/High | [How to mitigate] |
```

### Testing Strategy

```markdown
## Testing Strategy

- **Unit tests**: [What to test at unit level]
- **Integration tests**: [What interactions to verify]
- **Manual verification**: [What to check manually]
```

### Migration Plan

```markdown
## Migration Plan

1. **Pre-migration**: [Backup, validate, prepare]
2. **Migration**: [Execute changes]
3. **Verification**: [Validate results]
4. **Rollback**: [How to revert if needed]
```

### Alternatives Considered

```markdown
## Alternatives Considered

| Approach | Pros | Cons | Why Rejected |
|----------|------|------|--------------|
| [Alternative] | [Advantages] | [Drawbacks] | [Reason] |
```

### Open Questions

```markdown
## Open Questions

- [Question that may affect implementation]
- [Question to resolve during execution]
```

### Rollback Strategy

```markdown
## Rollback Strategy

If the implementation needs to be reverted:
1. [Rollback step]
2. [Verification step]
```

## Rules

1. Only add sections that provide value for the specific task — do not pad the plan
2. Each adaptive section should contain actionable information, not boilerplate
3. If a section would be trivially short (1 line), fold it into the Approach section instead
4. The combination of core + adaptive sections should fully prepare for implementation

## Back to

- [Output format overview](overview.md)
- See also: [Core template](core-template.md)
