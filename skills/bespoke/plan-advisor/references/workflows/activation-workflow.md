# Activation Workflow

The 9-step sequence executed when a user activates plan-advisor.

## Steps

### 1. Detect Invocation
- Match user input against trigger phrases (see [invocation-detection.md](../activation/invocation-detection.md))
- Confirm the user wants to activate (not just mentioning plan-advisor)

### 2. Check Current State
- Read the state file (see [state-management.md](../activation/state-management.md))
- If already active, inform the user and skip to step 5

### 3. Update State File
- Set `active: true`
- Set `activated-at` to current timestamp
- Create the state file if it doesn't exist

### 4. Acknowledge Activation
- Confirm to the user that plan-advisor is now active
- Briefly explain what it will do

### 5. Discover Plan File
- Check if a plan file path was provided
- Otherwise, auto-detect using the discovery rules (see [plan-reading.md](../assessment/plan-reading.md))
- If no plan found, ask the user to provide one

### 6. Read Plan
- Read the discovered plan file
- Parse it into structured elements

### 7. Launch Sub-Agent Evaluation
- Use the Task tool to launch a general-purpose sub-agent
- Pass the plan content and evaluation checklist (see [sub-agent-evaluation.md](../assessment/sub-agent-evaluation.md))

### 8. Present Assessment
- Display the sub-agent's assessment summary to the user
- Highlight strengths, gaps, risks, and recommendations

### 9. Update State with Assessment
- Set `plan-file` to the assessed plan's path
- Set `last-assessment` to current timestamp
- Plan-advisor is now ready for ongoing question answering

## Back to

- [Workflows overview](overview.md)
- See also: [Q&A workflow](question-answering-workflow.md) — what happens next
