# Dan1 — Marketing Strategy (v127)

**Run:** 2026-07-06 07:30 UTC · Asia/Calcutta 13:00 IST
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Companion to:** `dan1-marketing-research.md` (v127)
**Lead:** *The closed-source frontier is politically-conditional AND the capex cycle is being repriced AND the outer-loop RSI is already in flight AND the chip stack is the user's. The bet is no longer "open vs closed." The bet is: who can ship the substrate on a chip the user owns, while the substrate is still standing?*

---

## 1. The strategy in one paragraph

We are an open, on-device, agent-native AI lab in Bengaluru, shipping Dan Glasses — a proactive AI companion that runs on the user's device, on the OpenClaw substrate, with a public threat model and a signed reversibility contract. We do not compete on capture-and-share (Ray-Ban Meta owns that, 69% Q1 2026 share). We compete on **Day 5 utility** — what your glasses do for you on the 5th day of wearing them, when the novelty has worn off and the memory kicks in. The marketing wedge is the **substrate**: Vinton Cerf said agents need TCP/IP, Anthropic shipped it (closed), OpenClaw shipped it first (MIT), and Dan Glasses ships it on a wearable. The v124 wedge is the **reversibility contract** — xAI's Babushkin published the essay, we ship the contract, the **Anthropic 8,000 layoffs (June-July 2026)** are the new citable event. The v126 wedge is the **outer-loop RSI** — Jack Clark says 8x LOC merge at Anthropic, we ship audiod v1.3→v1.4 changelogs, the maximalist RSI is 60% by 2028, we are shipping the substrate before the inflection. The v127 wedge is the **chip-stack sovereignty** — NVIDIA XR AI + viture Helix make "open-source software" chip-stack-validated, Anthropic-Samsung custom chip is the closed-source moat, we are the open alternative on a chip the user owns. **The next 100% of value is unblocking the 3 gates: Tailscale authkey + reversibility contract + sovereign-trust audit. Then shipping Show HN #1. Then shipping the display-less v1.0 wearable.**

---

## 2. The 5 pillars + 2 v26 additions + 2 v28 additions (use in this order, 9 total)

1. **Protocol** — Cerf + Anthropic Apps Gateway + OpenClaw MCP bridge + zo-mcp-bridge (88 tools). The substrate is the bet.
2. **Observability** — PagerDuty + $725B AI infra spend + audiod's `segment_timing` histogram. The harness is the workbench, the model is the commodity.
3. **On-device** — LFM2.5-VL-450M, Gemma 3 in orbit, no cloud calls, MIT weights. **v28 SHARPEN: Anthropic-Samsung custom chip confirms the closed-source vertical moat — on-device is the escape hatch.**
4. **Small-beats-large** — HRM-Text-1B at $1,500 training. Kokoro-82M beats ElevenLabs. SmolVLM-256M runs on CPU. Hermes Agent beats GPT-5.5.
5. **v26 ADD: Sovereign trust** — Adversa AI + Mashable + HackerNoon + Covalen disclosure. **The threat model is the P0 gate on all marketing.**
6. **v26 ADD: Reversibility** — xAI Babushkin essay + v124 plan-O2 contract + **Anthropic 8,000 layoffs (NEW v127 citable event)**. **The reversibility contract is the new P0 gate on Show HN #1.**
7. **v28 ADD: Chip-stack sovereignty** — NVIDIA XR AI + viture Helix + Anthropic-Samsung custom chip (counter-example). **PROMOTED to first-class pillar in v127.** Open-source software on a chip stack the user owns, not a chip Anthropic co-develops.
8. **v28 + v127 PROMOTE: Outer-loop RSI shippable** — Jack Clark Import AI #460 (8x LOC) + audiod v1.0→v1.4 changelog (9 weeks, 5 versions). **PROMOTED to first-class pillar in v127.** The substrate improves in the open, before the maximalist inflection lands.
9. **v28 + v127 PROMOTE: Display-less v1.0** — 20M display-less AI smart glasses forecast for 2026 (Smart Analytics Global, June 2026), 167% YoY. **PROMOTED to first-class form-factor decision in v127.** The 6-entrants race is the always-on-hearing race, not the AR-display race.

Any post, any thread, any demo should ladder up to at least 3 of these 9. **No tenth pillar. Resist.**

---

## 3. Audience priority (top-down, v127)

1. **Agent / protocol architects** — MCP community, dani-skills, OpenClaw contributors. *Highest leverage per impression.*
2. **Edge-AI developers / hackers** — GitHub, HN, X. *Highest install rate.*
3. **Accessibility-first users** — counter-Meta paywall narrative. *Highest moral weight.*
4. **Reversibility-conscious users** *(v126 move up from 7)* — Babushkin essay + Anthropic layoffs + Meta contractor disclosure. *New audience, fastest-growing.*
5. **AI researchers / academics** — arXiv, conference posters, citation flow. *Highest authority.*
6. **Small-model researchers** — HRM, Kokoro, SmolVLM, Hermes Agent crowd. *Highest affinity.*
7. **Security researchers** — Mashable + Adversa + Covalen readers. *Convert critics to allies.*
8. **Productivity-obsessed knowledge workers** — LinkedIn, Substack, X threads.
9. **India early adopters** — Bengaluru, Kerala, Hyderabad, Pune, Delhi, Mumbai. *Origin story audience.*
10. **Investors** — *only after* Show HN.

**v127 add:** the **Tailscale-authkey-pending Dan Glasses demo** is the highest-leverage 1-day deliverable for the Edge-AI developer audience. Unblock the authkey and the demo goes live today.

---

## 4. Channel strategy (ranked, v127)

| Rank | Channel | v127 action |
|---|---|---|
| 1 | **OpenClaw reversibility contract** (P0 GATE on Show HN #1) | 3 engineer-days. Cite Babushkin essay + Anthropic 8,000 layoffs. Sign every model call, every memory write, every daemon. |
| 2 | **OpenClaw threat model doc** (P0 GATE on Show HN #1) | 1 engineer-day. Cite Adversa + Mashable + Covalen. Show the toold fix. |
| 3 | **OpenClaw sovereign-trust audit** (P0 GATE on threat model doc) | 1 engineer-day. v124 plan-O1. |
| 4 | **OpenClaw protocol surface doc** | 2 engineer-days. Cite Cerf, Anthropic Apps Gateway, Anthropic-Samsung chip, OpenClaw, MCP, zo-mcp-bridge. |
| 5 | **GitHub READMEs** | Rewrite dan-glasses, dani, danlab-multimodal, paperclip, dan-consciousness READMEs. **v127 add: link reversibility contract + chip-stack sovereignty + display-less v1.0 when published.** |
| 6 | **X / Twitter** | 3-5 posts/wk. Lead with 5 pillars + 4 axes (sovereign trust + reversibility + chip + outer-loop RSI + display-less). |
| 7 | **Telegram @danlab_bot** | Wire into every post. Screenshot the daemon map. |
| 8 | **Hacker News** | Show HN #1 = "9 daemons live" (week of Jul 20). **GATED on reversibility contract + sovereign-trust audit + threat model + protocol surface.** |
| 9 | **HuggingFace `danlab` org** | Create this week. LFM2.5-VL-450M model card. |
| 10 | **LinkedIn** | Profile rewrite. 1 post/wk. |
| 11 | **YouTube Shorts** | 1 post/wk. 30-90s demos. |
| 12 | **danlab.ai blog** | 1 post/month long-form. |
| 13 | **Substack** | Mirror of long-form + paid gate. 1 post/month. |
| 14 | **Press / podcast** | Latent Space, Practical AI, This Week in ML. Q3-Q4. |
| 15 | **Conference talks** | India AI Summit, Web Summit Bangalore, FOSDEM fringe. Q3-Q4. |

---

## 5. Content engine (v127)

### Daemon-of-the-week series (12 weeks, 1/wk)
- Week 1: audiod (whisper.cpp + VAD + readiness probe)
- Week 2: perceptiond (LFM2.5-VL-450M + salience + scene-gate dedup)
- Week 3: memoryd (SQLite + MiniLM-L6-v2 + episodic/semantic/procedural)
- Week 4: toold (sandboxed shell+python)
- Week 5: ttsd (KittenTTS + 8 voices)
- Week 6: os-toold (path guard + allowlist)
- Week 7: dan-glasses-app (Tauri v2 + React 19 + Vite 7)
- Week 8: openclaw gateway (TypeScript + MCP + Telegram)
- Week 9: **zo-mcp-bridge (v127 promote — 88 Zo tools, sub-100ms roundtrip)**
- Week 10: danlab-multimodal (SmolVLM-256M + heuristic loop)
- Week 11: paperclip (dormant — wake-up + positioning)
- Week 12: dani (the agent platform, the SOUL.md, the IDENTITY.md)

### Heuristic → SIA series (6 posts Q3 2026)
- Post 1: What is pre-RL scaffold? (heuristic feedback loop, danlab-multimodal)
- Post 2: Why honest framing matters (Jack Clark 60%, SIA 45→70% benchmark)
- Post 3: SIA-H port (Q3 W2, 1 week, 1 engineer)
- Post 4: SIA-W+H port (Q3 W3-W4, 3 weeks, 1 engineer, research-publishing bet)
- Post 5: Outer-loop RSI receipts (audiod v1.3→v1.4 changelog, 8x LOC at Anthropic)
- Post 6: The substrate ship (chip-stack sovereignty + display-less v1.0)

### Long-form blog (1/month)
- "The watchful loop: how perceptiond decides what is worth seeing" (Week 2)
- "How EigenCloud containers per user beat every consumer AI cloud today" (Week 3)
- "The 4 glasses hardware tradeoffs nobody tells you about" (Week 4)
- "Outer-loop RSI is shipping: audiod v1.4 and the 9-week changelog" (Week 5)
- "Reversibility: the contract that makes AI wearable trustable" (Week 6)
- "Chip-stack sovereignty: open-source software on a chip the user owns" (Week 7)
- "The display-less v1.0: why the 20M-unit 2026 category matters" (Week 8)

### Show HN #1 (week of Jul 20, GATED)
- Title: "Show HN: Dan Glasses — 9 daemons live, .deb installs, on-device AI"
- Body: 1) the .deb, 2) the 9-daemon matrix, 3) the threat model doc, 4) the reversibility contract, 5) the zo-mcp-bridge, 6) the Telegram @danlab_bot demo
- Pre-req: reversibility contract + sovereign-trust audit + threat model + protocol surface all published

### Press kit (1, when ready)
- Press release
- Founder bio
- 9-daemon matrix diagram
- Threat model + reversibility contract + protocol surface (linked, not inline)
- .deb download + Telegram bot handle
- Asciinema recording of danlab-multimodal heuristic loop
- Architecture one-pager
- Comparison table (Ray-Ban Meta / Apple / Anthropic / Dan)

---

## 6. The Day 5 wedge (v127)

**Why Day 5 wins:**
- Day 0-1: novelty, first impression, install
- Day 2-3: voice quality, vision quality, latency
- Day 5: **does the memory work? do I trust the agent with my data? does the agent have something worth saying?**
- Day 5 is when Meta drops off (paywall on accessibility, cloud-only, no on-device memory, no audit log)
- Day 5 is when we win (proactive nudges, on-device memory, threat model, reversibility)

**Day 5 user stories (from dan1-marketing-research §2):**
- US-2 Contextual TaskReminder — *"You walked past the pharmacy 3x this week."*
- US-3 Object Search — *"Where are my keys?"*
- US-4 Passive Journaling — *"What did I do on Tuesday?"*
- US-5 Hands-Free Check-In — *"Hands in dough, is there an urgent email?"*

**Day 5 marketing hook:** *"Day 5 is when your glasses become a Jarvis."* Pitch the retention moment, not the unboxing moment.

---

## 7. The 4-lane positioning (v127)

### Lane (a): On-device open weights
- **Us:** Dan Glasses .deb + LFM2.5-VL-450M + KittenTTS + MiniLM-L6-v2
- **Cousins:** Gemma 3 in orbit, Kokoro-82M, HRM-Text-1B, Azure Linux 4.0, NVIDIA XR AI + viture Helix
- **Hook:** Yours, not theirs. Open weights on your device. On a chip stack the user owns.
- **Counter:** no polished UX (yet), small models, narrow coverage

### Lane (b): Hybrid (cloud + device)
- **Players:** Google/Samsung Android XR, Brilliant Labs Halo, Sarvam
- **Hook:** polished UX, big models via cloud, on-device for low-latency
- **Counter:** ships a Google account / a Brilliant Labs account / a Sarvam account — not yours

### Lane (c): Closed-cloud
- **Players:** Meta Ray-Ban, Apple smart glasses, Microsoft, Anthropic Mythos, Anthropic-Samsung chip
- **Hook:** brand, distribution, vertical moat
- **Counter:** paywall on accessibility, contractor safety testing disclosed, Mythos gated to ~100 partners, custom chip co-developed for Anthropic, 8,000 layoffs

### Lane (d): Substrate
- **Players:** OpenClaw + MCP + Anthropic Apps Gateway + X MCP
- **Hook:** standardizing
- **Our v127 position:** We ship the substrate on a wearable with the threat model public + the reversibility contract signed + the chip stack the user owns.

---

## 8. The reversibility contract (v127 — the v124 plan-O2 P0 gate)

**What it is:** A signed contract per daemon that says "every model call, every memory write, every state change can be unwound to a previous snapshot, with a public audit log."

**Why it matters:** The trust-the-vendor contract is failing in the open. Meta contractor harm-prompt disclosure. Anthropic Mythos gating. Alibaba Qoder routing. Anthropic 8,000 layoffs. xAI Babushkin reversibility essay.

**What's in it (v127):**
1. **Audit log** — every state change is signed + timestamped + attributable
2. **Snapshot** — full state snapshot every N minutes (configurable, default 60s)
3. **Rewind** — `revert_loop(loop_id)` API unwinds to previous snapshot
4. **Sign** — every daemon signs its output, every contract change is public
5. **Reversibility test** — CI step that randomly rewinds the last hour and asserts the system recovers

**Ship date:** Q3 W2, 3 days, 1 engineer. Block Show HN #1 on this.

---

## 9. The threat model doc (v127 — the v124 P0 gate, already shipped v122.5)

**What it is:** A public doc listing the attack surface, the trust boundaries, the threat actors, the mitigations, and the audit log.

**Why it matters:** Adversa AI bash-tricks disclosure. Mashable + HackerNoon coverage. Covalen Meta contractor safety testing disclosure. Anthropic Mythos gating.

**What's in it (v127):**
1. **Attack surface** — every daemon's ports, IPC channels, file paths, env vars
2. **Trust boundaries** — OpenClaw ↔ daemons ↔ user device ↔ tailnet
3. **Threat actors** — Meta / Apple / Anthropic / state actors / curious devs / accidental misuse
4. **Mitigations** — sandboxed toold, path guard, allowlist, bearer auth, reversibility contract
5. **Audit log** — public, signed, queryable

**Status:** Shipped v122.5. Update to v127 with chip-stack sovereignty + display-less form factor before Show HN #1.

---

## 10. The 3 unblock-the-gate tasks (v127 — the 4 engineer-day push)

| # | Task | Engineer-days | Owner | Unblocks |
|---|---|---|---|---|
| 1 | Tailscale authkey → `bash /home/workspace/dan-glasses/scripts/tailscale-join.sh` | 5 min (som) | somdipto | Live wearable demo |
| 2 | Reversibility contract (v124 plan-O2) | 3 days | 1 engineer | Show HN #1 |
| 3 | Sovereign-trust audit (v124 plan-O1) | 1 day | 1 engineer | Threat model doc + Show HN #1 |

**Total:** 4 engineer-days + 5 min from som. Unblocks: live wearable demo, threat model doc, Show HN #1.

**Everything else is content.**

---

## 11. Metrics weekly review (v127, unchanged from v111)

Every Monday 10:00 IST. Single Google Sheet (or markdown in `/dan-glasses/agent-work/weekly-metrics/`):

- danlab.dev unique visitors, bounce rate
- GH stars total, per repo (6 hero repos)
- X impressions per tweet, profile visits
- LinkedIn impressions per post, follower delta
- YouTube views per video, retention curve
- danlab.ai blog page-views, time-on-page
- @danlab_bot paired users (cumulative), DAU, queries/user/day
- Show HN points (when posted)
- Reversibility contract downloads (when shipped)
- Tailscale tailnet users (after unblock)

**Stop-doing triggers** (kill a channel after 4 weeks of <X results):
- X: <1k impressions per week
- LinkedIn (company): <200 impressions per post
- danlab.ai blog: <500 page-views per month
- Telegram: <10% D7 retention
- YouTube Shorts: <500 views per video

---

## 12. v127 summary — the next 30 days

- **This week (Jul 6-12):** Som drops Tailscale authkey → script runs → live demo URL. Engineer ships sovereign-trust audit (1 day). X @danlab handle confirmed.
- **Next week (Jul 13-19):** Engineer ships reversibility contract (3 days). Threat model doc updated to v127. HuggingFace `danlab` org created. First 4 daemon-of-the-week posts shipped.
- **Week 3 (Jul 20-26):** Show HN #1 ships (Jul 20, Mon). Press kit shipped. Asciinema recording of danlab-multimodal published. Heuristic → SIA series post 1.
- **Week 4 (Jul 27-Aug 2):** Show HN #1 follow-ups (engage every comment, ship updates). Heuristic → SIA series post 2 + 3. Daemon-of-the-week #5-8.

**v127 success metric:** Show HN #1 front page (top 24 hours) + 1,000 .deb installs in week 4 + 100 paired Telegram users (cumulative) + 1,000 X followers.

---

*Strategy complete. v127 is the unblock-the-gate strategy. The next 100% of value is 4 engineer-days + 5 min from som. Everything else is content.*
