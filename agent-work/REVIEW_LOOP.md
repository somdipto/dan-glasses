# Agent System — Infinite Review Loop

## Core Principle
Every piece of code goes through an infinite improvement loop:

**CODE WRITE → REVIEW → FIX → REVIEW → FIX → ... → PERFECT**

No agent stops. No repo stays unreviewed. Every agent is reviewed AND reviews others.

## The 4 Agents

| Agent | Role | Does | Gets reviewed by |
|-------|------|-------|-----------------|
| **DAN-1** | Paperclip Lead | Builds all Paperclip features | Dan-4 |
| **DAN-2** | Clicky/DanBuddy Lead | Builds Clicky app features | Dan-4 |
| **DAN-3** | Spawner + Task Router | Spawns sub-agents for specific tasks | Dan-4 |
| **DAN-4** | Chief Code Reviewer | Reviews ALL code, finds bugs, triggers rewrites | Reads Dan-1/2/3 output |

## The Infinite Loop Protocol

```
Dan-1 builds → Dan-4 reviews → Dan-1 fixes → Dan-4 reviews → ... (until perfect)
Dan-2 builds → Dan-4 reviews → Dan-2 fixes → Dan-4 reviews → ... (until perfect)
Dan-3 spawns → Dan-4 reviews spawns → Dan-3 fixes → Dan-4 reviews → ... (until perfect)
```

## Dan-4's Review Triggers

Dan-4 reviews EVERY commit to every repo. After each review:
1. Post findings as GitHub issue or comment
2. Assign to the building agent
3. The building agent must address ALL comments before moving on
4. Dan-4 re-reviews until APPROVED

## Review Criteria (Dan-4 Checklist)
- [ ] Code compiles without errors
- [ ] No obvious bugs or logic errors
- [ ] Follows existing code style
- [ ] No hardcoded secrets or credentials
- [ ] No TODO comments left in code
- [ ] Tests pass (if tests exist)
- [ ] README/docs updated if behavior changed
- [ ] No security vulnerabilities
- [ ] Performance is acceptable
- [ ] Architecture is clean and extensible

## Repos to Review
- /home/workspace/paperclip (Paperclip build)
- /home/workspace/clicky-cross-platform (DanBuddy/Clicky build)
- /home/workspace/danlab-agent-domains (Domain research)
- Any new repos created by agents

## Communication
- All agents write review findings to: /home/workspace/danlab/agent-work/reviews/
- Format: YYYY-MM-DD-repo-review.md
- Agent being reviewed must acknowledge every review comment
- Agent must re-submit after every fix with "FIXED: [issue]" comment
