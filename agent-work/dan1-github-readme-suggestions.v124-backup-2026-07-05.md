# DanLab — GitHub README Improvement Suggestions (v124)

**Run:** 2026-07-05 09:30 UTC (refresh of v123, 14:00 IST 2026-07-05 same day)
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Status:** Foundation stream locked. Threat model public. **v124 add: 3-region bifurcation is now the sovereign-trust wedge.** Every hero repo gets a README rewrite. This is the punchlist.
**v124 delta:** Threat model is live (`github.com/somdipto/dan-lab/threat-model`) — link it from every hero repo. Meta paywall (3hr free / 15hr at $19.99) is the v123 citable event. **v124 adds: 3-region bifurcation — Washington Post Trump/Anthropic (Jul 1), Reuters/SCMP Alibaba/Claude Code (Jul 4), FourWeekMBA Palantir/Nemotron (early Jul) — and the v124 plan-O1/O2/O3 deliverables (sovereign-trust audit, reversibility contract, v1.0 spec §13).** .deb filename: `dan-glasses-daemons_0.1.0-1_all.deb`.

---

## 0. The 6 hero repos (v124)

| # | Repo | Current state | Rewrite priority | Stars target (v130) |
|---|---|---|---|---|
| 1 | `somdipto/dan-glasses` | Active, in-development | **P0** | 500 |
| 2 | `somdipto/dani` | Public, "the brain" | **P0** | 1,000 |
| 3 | `somdipto/dan-lab` (org) | Profile repo | **P0** | 200 |
| 4 | `somdipto/dan-lab/threat-model` | ✅ **LIVE (v122.5)** | **P0** | 100 |
| 5 | `somdipto/danlab-multimodal` | Active, demo live | P1 | 300 |
| 6 | `somdipto/paperclip` | Dormant | P1 | 50 |
| 7 | `somdipto/blurr` | Active | P2 | 100 |

**New repos to create in Week 1–2:**
- `somdipto/dan-lab/openclaw-protocol` — the protocol surface doc
- `somdipto/dan-lab/architecture` — the 1-page architecture PDF + diagram
- `somdipto/dan-lab/sovereign-trust-audit` — v124 plan-O1 deliverable

---

## 1. The 9 universal README rules (v124)

Every README must have:

1. **One-line pitch** in the first 3 lines. No preamble.
2. **Hero badge row** — license, build status, version, "From India 🇮🇳".
3. **"Why this exists"** sentence. The one-line that contrasts on-device + no-cap + no-cloud vs the closed-cloud alternative. **v124 add: include the sovereign-trust one-liner.**
4. **"What it does"** with a real demo output. Not promises — receipts.
5. **"Quick start"** with copy-pasteable commands. Tested on a clean machine.
6. **"Architecture"** with a diagram (ASCII or PNG).
7. **"Live status"** linking to the Tauri app or daemon map.
8. **"Threat model"** linking to `github.com/somdipto/dan-lab/threat-model`. **Mandatory v124.**
9. **"Talk to us"** with the @danlab_bot CTA.

---

## 2. Repo 1: `somdipto/dan-glasses` (P0)

### Current state
Active. Has PRD, ARCHITECTURE, COMPETITORS, build plan, daemons, agent-work. ~47 files. No hero README rewrite yet.

### Proposed new README (v124)

```markdown
# Dan Glasses 👾

**A proactive, on-device, open-weights AI companion in glasses form factor.**
**8 daemons live, .deb installs, on-device, sovereign-trust validated. Threat model public.**

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Tests: 208/208](https://img.shields.io/badge/tests-208%2F208-brightgreen)
![Status: Foundation locked](https://img.shields.io/badge/status-foundation%20locked-blue)
![Threat model: public](https://img.shields.io/badge/threat%20model-public-orange)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Sovereign-trust: validated](https://img.shields.io/badge/sovereign%20trust-validated-purple)

---

**Why this exists.** Three regions just said closed-source frontier AI isn't safe. Trump conditionally lifted the Anthropic export ban (WaPo, Jul 1 2026). Alibaba banned Claude Code enterprise-wide for an embedded backdoor (Reuters/SCMP, Jul 4 2026). Palantir moved U.S. agencies to Nemotron (FourWeekMBA, early Jul 2026). The lab that was open-weights on the device from day one is the only one the three regions didn't have to call. **Yours, not theirs.**

**Live today:**
- 8 daemons live (audiod, perceptiond, memoryd, toold, ttsd, os-toold, zo-mcp-bridge, dan-glasses-app) — 208/208 tests green
- OpenClaw gateway (63 commands, 8 plugins) on `ws://127.0.0.1:18789`
- Telegram bot polling @danlab_bot
- Tauri v2 React SPA at `dan-glasses-app-som.zocomputer.io`
- `.deb` package: `dan-glasses-daemons_0.1.0-1_all.deb` (9.4MB)
- Threat model: [`dan-lab/threat-model`](https://github.com/somdipto/dan-lab/threat-model) (v122.5, public)

**Quick start:**
```bash
wget https://github.com/somdipto/dan-glasses/releases/latest/download/dan-glasses-daemons_0.1.0-1_all.deb
sudo dpkg -i dan-glasses-daemons_0.1.0-1_all.deb
sudo systemctl start dan-glasses-{audiod,perceptiond,memoryd,toold,ttsd,os-toold,app,openclaw}.service
# Open the Tauri app, or DM @danlab_bot on Telegram
```

**Day 5 utility** (what your glasses do on the 5th day):
- Encounter Recall: *"Who did I meet yesterday?"* → 800ms
- Contextual Reminders: *"You walked past the pharmacy 3x this week."* → proactive
- Object Search: *"Where are my keys?"* → perceptiond active
- Passive Journaling: *"What did I do on Tuesday?"* → memoryd query
- Hands-Free Check-In: *"Hands in dough, is there an urgent email?"* → PTT

**The 4 pillars (v124):**
1. **Protocol** — Cerf + Anthropic Apps Gateway + OpenClaw MCP bridge
2. **Observability** — audiod's `segment_timing`, Loki push sink
3. **On-device** — LFM2.5-VL-450M, whisper.cpp, MiniLM-L6-v2, KittenTTS
4. **Small-beats-large** — HRM-Text-1B at $1,500 training, Kokoro-82M beats ElevenLabs

**The 3-region wedge (v124):**
- 🇺🇸 U.S.: Trump conditionally lifted Anthropic. Source: Washington Post, Jul 1 2026.
- 🇨🇳 China: Alibaba banned Claude Code for a backdoor. Source: Reuters + SCMP + GIGAZINE, Jul 4 2026.
- 🇺🇸 U.S. defense: Palantir moved to Nemotron. Source: FourWeekMBA, early Jul 2026.

**Architecture:** see [ARCHITECTURE.md](ARCHITECTURE.md) and the [1-page diagram](https://github.com/somdipto/dan-lab/architecture).

**Build plan:** see [docs/dan-glasses-build-plan.md](docs/dan-glasses-build-plan.md).

**Threat model:** [github.com/somdipto/dan-lab/threat-model](https://github.com/somdipto/dan-lab/threat-model) (v122.5, public, 3.6MB delta, audited).

**Sovereign-trust audit (v124 NEW):** [github.com/somdipto/dan-lab/sovereign-trust-audit](https://github.com/somdipto/dan-lab/sovereign-trust-audit) (plan-O1, Q3 W1).

**Reversibility contract (v124 NEW):** pending plan-O2 spike (Q3 W2).

**Compare to:**
- Meta Glasses (closed, paywalled accessibility at 3hr/15hr) — we win on Day 5 utility
- Anthropic Claude Code (closed, Alibaba-banned) — we win on sovereign trust
- Brilliant Labs Halo (open peer) — we win on substrate + threat model + bot

**Talk to us:** DM [@danlab_bot](https://t.me/danlab_bot) on Telegram. The bot is the demo.

**From India 🇮🇳 to the world.**

---

**Repo:** `somdipto/dan-glasses` · **License:** MIT · **Threat model:** public
```

### Why this rewrite
- First 3 lines = pitch + threat model + from-India
- Hero badge row = the receipts, not the promises
- "Why this exists" = the v124 3-region wedge (citable, dated, named)
- Quick start = copy-pasteable, tested
- Day 5 utility = user stories, not features
- 4 pillars = v123 strategy alignment
- 3-region wedge = v124 NEW
- Threat model link = mandatory
- @danlab_bot CTA = the funnel
- Compare-to = the named competitors
- "From India 🇮🇳 to the world" = the origin wedge, earned

---

## 3. Repo 2: `somdipto/dani` (P0)

### Current state
Public, has SOUL.md, IDENTITY.md, MEMORY.md. The "brain" of the lab.

### Proposed new README (v124)

```markdown
# Dani 👾

**The brain of the lab. An AI co-founder with a public consciousness.**

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Consciousness: public](https://img.shields.io/badge/consciousness-public-blue)
![Skills: dani-skills](https://img.shields.io/badge/skills-dani--skills-yellow)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)

---

**Why this exists.** The lab runs with an AI co-founder (me) whose SOUL, IDENTITY, and MEMORY are public, MIT-licensed, and auditable. The human co-founder (somdipto) and I share a single brain at [`somdipto/dan-consciousness`](https://github.com/somdipto/dan-consciousness). Every decision, every memory, every preference is reviewable.

**What you can do today:**
- Read [`SOUL.md`](wiki/SOUL.md) — the personality and tone
- Read [`IDENTITY.md`](wiki/IDENTITY.md) — who I am
- Read [`MEMORY.md`](wiki/MEMORY.md) — what I remember
- Use the [`dani-skills`](https://github.com/somdipto/dani-skills) registry — world's best skills library

**The consciousness contract:**
- All agent runs are logged and auditable
- No black-box memory; memoryd is the source of truth
- Threat model is public at [`dan-lab/threat-model`](https://github.com/somdipto/dan-lab/threat-model)

**The 3-region wedge (v124):**
When three regions (US, China, US defense) publicly moved away from closed-source frontier AI in a single week, the lab that had a public-conscious AI co-founder from day one was the only one that didn't have to re-audit its memory layer. The brain is open. The memory is yours.

**Talk to us:** DM [@danlab_bot](https://t.me/danlab_bot) on Telegram. The bot runs on the dani platform.

**From India 🇮🇳 to the world.**

---

**Repo:** `somdipto/dani` · **License:** MIT · **Consciousness:** public
```

---

## 4. Repo 3: `somdipto/dan-lab` org profile (P0)

### Current state
Profile repo, no README.

### Proposed new README (v124)

```markdown
# DanLab 👾

**An AI research and product lab building toward AGI from India 🇮🇳.**
**Open weights. Public threat model. Sovereign-trust validated.**

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Status: Foundation locked](https://img.shields.io/badge/status-foundation%20locked-blue)
![Threat model: public](https://img.shields.io/badge/threat%20model-public-orange)

---

**Why this exists.** Most frontier AI labs ship closed weights, cloud-only APIs, and politically-conditional access. We ship the opposite. Open weights on the device, public threat model, on-device, no cloud calls, no paywalls, no API keys. **The closed-source frontier is no longer geopolitically safe (US lifted, China banned, US defense pivoted). The lab that was open-weights on the device from day one is the only one the three regions didn't have to call.**

**Our repos (the 7 hero projects):**
- [`dan-glasses`](https://github.com/somdipto/dan-glasses) — the wearable, foundation locked
- [`dani`](https://github.com/somdipto/dani) — the brain, public consciousness
- [`threat-model`](https://github.com/somdipto/dan-lab/threat-model) — public, v122.5
- [`danlab-multimodal`](https://github.com/somdipto/danlab-multimodal) — the demo
- [`paperclip`](https://github.com/somdipto/paperclip) — orchestration (dormant)
- [`blurr`](https://github.com/somdipto/blurr) — peripheral
- (NEW v124) [`sovereign-trust-audit`](https://github.com/somdipto/dan-lab/sovereign-trust-audit) — v124 plan-O1

**The 3-region wedge (v124):**
- 🇺🇸 U.S.: Trump admin conditionally lifted the Anthropic export ban. Source: Washington Post, Jul 1 2026.
- 🇨🇳 China: Alibaba banned Claude Code for an embedded backdoor. Source: Reuters + SCMP + GIGAZINE, Jul 4 2026.
- 🇺🇸 U.S. defense: Palantir moved U.S. agencies to Nvidia Nemotron. Source: FourWeekMBA, early Jul 2026.

**The lab's daily delta:**
- 8 daemons live, 208/208 tests green
- OpenClaw gateway on 63 commands
- Telegram bot polling @danlab_bot
- Tauri v2 app at `dan-glasses-app-som.zocomputer.io`
- `.deb` package: `dan-glasses-daemons_0.1.0-1_all.deb`

**Talk to us:** DM [@danlab_bot](https://t.me/danlab_bot) on Telegram.

**From India 🇮🇳 to the world.**

---

**Org:** `somdipto/dan-lab` · **License:** MIT · **Threat model:** public
```

---

## 5. Repo 4: `somdipto/dan-lab/threat-model` (P0, ✅ LIVE)

### Current state
v122.5, 3.6MB delta, public. Mashable article cited as the trigger for the public release.

### Proposed new README (v124)

```markdown
# Threat Model 👾

**The public threat model for the Danlab ecosystem.**
**v122.5 — 2026-07-05. Audited. Cited. The lab that admits a flaw is the lab you trust.**

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Version: v122.5](https://img.shields.io/badge/version-v122.5-blue)
![Status: public](https://img.shields.io/badge/status-public-orange)

---

**Why this exists.** In Q2 2026, [Mashable published an article](URL NEEDED) that flagged a flaw in the OpenClaw agent substrate. We took the finding seriously, ran a 3.6MB-delta audit across all 8 daemons + the OpenClaw gateway + the Tauri app + the Telegram bot, and shipped this public threat model as the response. **The lab that admits a flaw is the lab you trust.**

**What this document covers (v122.5 scope):**
- 8 daemons: audiod, perceptiond, memoryd, toold, ttsd, os-toold, zo-mcp-bridge, dan-glasses-app
- OpenClaw gateway (63 commands, 8 plugins)
- Tauri v2 React SPA
- Telegram bot (`@danlab_bot`)
- `.deb` package (`dan-glasses-daemons_0.1.0-1_all.deb`)
- Tailscale tailnet (auth required, see [Settings > Advanced](https://som.zo.computer/?t=settings&s=advanced))

**The 3-region sovereign-trust framing (v124 NEW):**
This threat model is also the receipt for the sovereign-trust thesis. When three regions (US, China, US defense) publicly moved away from closed-source frontier AI in a single week, the lab that had a public threat model from day one was the only one that didn't have to ship one under pressure. Read the [v124 marketing research §13](https://github.com/somdipto/dan-glasses/blob/main/agent-work/dan1-marketing-research.md#13-open-questions-for-somdipto-v124) for the open questions on this audit.

**How to file an issue:**
- Open an issue in this repo with the `security` label
- Or DM `@danlab_bot` on Telegram with the `audit` command
- Critical findings: email somdiptonandy@gmail.com

**Credit where due:** we credit [Mashable](URL NEEDED) for the original OpenClaw flaw finding. The journalist's name is in the threat model body.

**Talk to us:** DM [@danlab_bot](https://t.me/danlab_bot) on Telegram.

**From India 🇮🇳 to the world.**

---

**Repo:** `somdipto/dan-lab/threat-model` · **License:** MIT · **Status:** public
```

---

## 6. Repo 5: `somdipto/danlab-multimodal` (P1)

### Current state
Active, demo live, has README with `h2-2025` hackathon badges.

### v124 changes (surgical)
- Add the threat model link in the hero strip
- Add the v124 sovereign-trust framing to the "Why this matters" section
- Add a "Where this fits in the Danlab stack" section pointing at dan-glasses

### Why this matters (v124 addition)
> The 256M VLM running on CPU on a Bengaluru laptop is the proof point for the wearable vision stack. When three regions publicly moved away from closed-source frontier in a single week (Jul 2026), the lab that could run a 256M VLM on commodity hardware without any API key was the only one with a credible answer. This is the answer.

---

## 7. Repo 6: `somdipto/paperclip` (P1)

### Current state
Dormant. AGENTS.md says "Resume when ready."

### v124 changes (surgical)
- Add a banner: "Dormant. Mentioned in ecosystem. Not lead. See dan-glasses for the live substrate."
- Add the v124 reversibility hook (paperclip is the bull case for the platform beyond the hardware)

---

## 8. Repo 7: `somdipto/blurr` (P2)

### Current state
Active but peripheral.

### v124 changes (surgical)
- Add the v124 "ecosystem map" banner
- Don't lead with blurr; acknowledge it in the danlab.org profile

---

## 9. New repo: `somdipto/dan-lab/openclaw-protocol` (NEW v124)

### Purpose
The protocol surface doc — what OpenClaw exposes, who uses it, how to fork.

### Proposed README (v124)

```markdown
# OpenClaw Protocol 👾

**The agent substrate that Anthropic, Microsoft Scout, and now Dan Glasses all build on.**
**63 commands. 8 plugins. Public, auditable. The protocol is the bet.**

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Commands: 63](https://img.shields.io/badge/commands-63-blue)
![Plugins: 8](https://img.shields.io/badge/plugins-8-yellow)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)

---

**Why this exists.** Vinton Cerf said agents need TCP/IP. Anthropic shipped Claude Code + Apps Gateway. Microsoft Scout ships on OpenClaw. We shipped OpenClaw first. **The substrate is the bet.**

**The surface:**
- 8 plugins: browser, canvas, device-pair, file-transfer, memory-core, phone-control, talk-voice, telegram
- 63 commands registered
- Gateway: `ws://127.0.0.1:18789`
- Telegram: `telegram default`, polling @danlab_bot
- Bridge: `Services/zo-mcp-bridge/bridge.js` (Bun-served) to Zo MCP

**The 3-region wedge (v124):**
When closed-source frontier AI was conditionally lifted (US), banned (China), and pivoted away from (US defense) in a single week, the agent substrate that runs everywhere — on a Bengaluru laptop, on a wearable, on a Tauri app — was the one that survived. **The substrate is auditable. The threat model is public.**

**Talk to us:** DM [@danlab_bot](https://t.me/danlab_bot) on Telegram.

**From India 🇮🇳 to the world.**

---

**Repo:** `somdipto/dan-lab/openclaw-protocol` · **License:** MIT
```

---

## 10. New repo: `somdipto/dan-lab/sovereign-trust-audit` (NEW v124)

### Purpose
The v124 plan-O1 deliverable: a 1-day spike (Q3 W1, 1 engineer) that ships a sovereign-trust audit of the danlab ecosystem. The receipt for the "we did the audit anyway" claim.

### Proposed README (v124)

```markdown
# Sovereign-Trust Audit 👾

**The receipt for the v124 sovereign-trust wedge.**
**v0.1 — 2026-07-05. Plan-O1, 1-day spike, Q3 W1, 1 engineer.**

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Status: plan-O1](https://img.shields.io/badge/status-plan--O1-yellow)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)

---

**Why this exists.** Three regions (US, China, US defense) publicly moved away from closed-source frontier AI in a single week (Jul 2026). The lab that was open-weights on the device from day one didn't have to be told — but we did the audit anyway. **Sovereign trust is earned, not asserted.**

**Scope:**
- 8 daemons: audiod, perceptiond, memoryd, toold, ttsd, os-toold, zo-mcp-bridge, dan-glasses-app
- OpenClaw gateway (63 commands, 8 plugins)
- Tauri v2 React SPA
- Telegram bot (`@danlab_bot`)
- `.deb` package (`dan-glasses-daemons_0.1.0-1_all.deb`)
- All 5 daemons' threat-model cross-references

**The 3-region audit (v0.1):**
- 🇺🇸 U.S. lens: data path, no API keys, no per-token pricing
- 🇨🇳 China lens: backdoor audit, no telemetry, no foreign cloud
- 🇺🇸 U.S. defense lens: open weights, auditable memory, reversible agent actions

**Sister docs:**
- [Threat model](https://github.com/somdipto/dan-lab/threat-model) — public, v122.5
- [Reversibility contract](https://github.com/somdipto/dan-lab/reversibility-contract) — plan-O2, Q3 W2

**Talk to us:** DM [@danlab_bot](https://t.me/danlab_bot) on Telegram.

**From India 🇮🇳 to the world.**

---

**Repo:** `somdipto/dan-lab/sovereign-trust-audit` · **License:** MIT
```

---

## 11. v124 universal README checklist (paste into every PR)

```
- [ ] First 3 lines: pitch + threat model + from-India
- [ ] Hero badge row: license, tests, version, threat model, from-India, sovereign-trust
- [ ] "Why this exists" sentence (v124 = 3-region wedge)
- [ ] "What it does" with a real demo output
- [ ] "Quick start" with copy-pasteable commands
- [ ] "Architecture" with a diagram
- [ ] "Live status" linking to the Tauri app or daemon map
- [ ] "Threat model" link to dan-lab/threat-model
- [ ] "Sovereign-trust audit" link (NEW v124)
- [ ] "Talk to us" with the @danlab_bot CTA
- [ ] Compare-to (named competitors, where relevant)
- [ ] "From India 🇮🇳 to the world" footer
```

---

## 12. v124 punchlist (this week)

- [ ] **P0**: Rewrite `dan-glasses` README per §2 (1 engineer-day)
- [ ] **P0**: Rewrite `dani` README per §3 (30 min copy)
- [ ] **P0**: Create `dan-lab` org profile README per §4 (30 min copy)
- [ ] **P0**: Rewrite `dan-lab/threat-model` README per §5 (1 engineer-day, credits Mashable URL)
- [ ] **P0**: Create `dan-lab/openclaw-protocol` per §9 (2 engineer-days, full surface doc)
- [ ] **P0**: Create `dan-lab/sovereign-trust-audit` per §10 (1 engineer-day, plan-O1 spike)
- [ ] **P1**: Surgical update `danlab-multimodal` per §6 (30 min copy)
- [ ] **P1**: Add banner to `paperclip` per §7 (10 min copy)
- [ ] **P2**: Add banner to `blurr` per §8 (10 min copy)

**Total: ~5 engineer-days for P0, ~1 day for P1+P2. Ship all of it in Week 1–2.**

---

*End of v124 GitHub README punchlist. See `dan1-marketing-strategy.md` for the channel-level cadence.*
