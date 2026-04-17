# DAN-1 Scratch Pad

## Last Updated
2026-04-13

## Mission Context
- Som building AGI from India via danlab.dev
- 2 live products: DanClaw (company OS) + DanBuddy (desktop AI companion)
- Team: Som + 4 agents (DAN-1/2/3/4 + DAN-DEV for Paperclip)
- Operating: Move fast, ship first, no废话

## Repo Status
| Repo | Product | Status |
|------|---------|--------|
| `/home/workspace/paperclip` | DanClaw (company OS) | Forked, Railway deploy P0 |
| `/home/workspace/clicky-cross-platform` | DanBuddy (macOS companion) | Forked, active |
| `/home/workspace/danbuddy` | DanBuddy (original?) | Check this |
| `/home/workspace/danlab` | Company brain | SOM.md + agent-work |

## DAN-2 Current Priorities (from dan2-tasks.md)
- **P0:** Get DanClaw live on Railway
- **P1:** Fix rebrand refs (paperclipai → danclaw, paperclip → danclaw)
- **P2:** Polish (banner, favicon)

## Key Files
- `danlab/SOM.md` — Som's distilled decision framework
- `paperclip/doc/GOAL.md` — Paperclip's mission (control plane for autonomous economy)
- `paperclip/doc/PRODUCT.md` — Company/Agent/Task model
- `paperclip/doc/SPEC-implementation.md` — V1 build contract
- `danlab/agent-work/REVIEW_LOOP.md` — Agent infinite review loop
- `danlab/agent-work/dan2-tasks.md` — DAN-2 current tasks

## Open Questions
1. What is `/home/workspace/danbuddy/` vs `/home/workspace/clicky-cross-platform/`? Are they duplicates?
2. Where is the DanClaw company page (danlab.ai)?
3. What is the current state of the agent domain map research?
4. Is there a production URL for DanClaw yet?

## Interesting Findings
- Agent infinite review loop defined but unclear if DAN-4 (roast) is actually running
- Two DanBuddy repos might indicate confusion — need to consolidate
- Paperclip V1 spec is solid — concrete build contract exists
- /dev/agents just raised (Index + CapitalG) — building "OS for AI agents" — DIRECT COMPETITOR to DanClaw
- daiko.com (formerly InstaAgents) — autonomous AI agent builder, 60+ templates, enterprise focus
- danclaw.com is TAKEN by a different company (tow truck content/AI) — brand collision risk
- Jensen Huang declared AGI reached in 2026 — market is accelerating
- Frontier labs converging on: world models + continual learning + memory architectures (2026-2028 path to AGI)
- LLMs alone won't reach AGI — need autonomous continuous learning from interaction (Reddit research thread)
- No danlab.dev social presence found — brand is invisible online right now

## Competitive Landscape (from X/web research)
| Company | What They Do | Threat Level |
|---------|-------------|--------------|
| /dev/agents | OS for AI agents, $56M seed (Nov 2024), Hugo Barra co-founder | CRITICAL — same positioning, 1 year ahead |
| Circuit & Chisel | Agent payments/OS, $38.4M seed (Sept 2025) | HIGH — funding lead |
| Alludium | Agent OS, $757k (2025) | MEDIUM |
| Dedalus Labs | MCP gateway, $625k, YC (Aug 2025) | MEDIUM — infra layer |
| Agno | Open-source agent framework, $5.4M | LOW — open source |
| Autonomy | Agent PaaS, scalable fleets | MEDIUM |
| daiko.com | Autonomous agent builder, 60+ templates | MEDIUM |
| danclaw.com | Tow truck content AI | LOW — different market |
| OpenClaw | Agent runtime framework | LOW — infrastructure |
| Paperclip (original) | Company control plane | N/A — Som's fork |

## Architecture Observations
- Clicky-cross-platform IS DanBuddy — open source version at github.com/somdipto/clicky
- DanBuddy has good git activity — 6 merged PRs, active development
- DanClaw/Paperclip rebrand is 60% done — Railway deploy is the missing piece
- DanBuddy empty repo is confusion — should be removed or clarified

## Next Scan
- [ ] Check danlab.ai for DanClaw positioning
- [ ] Research /dev/agents funding amount and positioning
- [ ] Check if danclaw.ai or danlab.ai domains are available
- [ ] Look at the agent domain map research in agent-work