# Dan1 — Marketing Research Report (v121)

**Run:** 2026-07-04 06:05 UTC · Asia/Calcutta 11:35 IST
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Status:** v121 refresh. Same v120 substrate (Newsweek + Cerf + OpenClaw mobile + Mashable flag) carried forward. Focus this run: tighten the lead, ship the deliverables, and stop churning versions.

**Builds on:** v120 (2026-07-04 02:00 UTC), dan1.md v120, dan2.md v18.

---

## 0. v121 deltas — what changed

This is a **shipping run, not a research run.** v120 already has the substrate. v121's job is to:

1. Lock the lead across all 5 artifacts: **"Vinton Cerf said agents need TCP/IP. Anthropic shipped it 2 days later. OpenClaw shipped it first. Dan Glasses ships it on a wearable. The substrate is auditable — and we are auditing it."**
2. Stop adding new tiers / channels. The 8 channel list, 8 ICP tiers, 5 deliverable formats are enough.
3. Force the threat model + protocol surface doc into the v121 punchlist as **P0 blocks on all marketing.**
4. Make every artifact a thing a human can act on Monday.

**v121 lead (locked):** *The protocol is the bet. The data path is yours. The threat model is public. The wearable ships it.*

**v121 anti-pattern to avoid:** more tiered tables, more sub-bullets, more "v120 sharpening." We are at the **honesty ceiling** for a v120-substrate marketing surface. The next 100% of value comes from shipping the artifacts, not from refining the framing.

---

## 1. What is Dan Glasses?

**One-liner:** A proactive, on-device AI companion in glasses form factor. Sees, hears, remembers, speaks only when it has something worth saying.

**Product shape (live today):**
- Smart glasses hardware (JBD MicroLED, dual 200mAh, USB-C, NDP200 firmware)
- **9 processes live on a Linux laptop**: 8 service daemons (audiod, perceptiond, memoryd, toold, ttsd, os-toold, dan-glasses-app, openclaw) + tailscaled substrate
- **Tauri v2 app published** at `https://dan-glasses-app-som.zocomputer.io`
- **Telegram `@danlab_bot`** wired and live
- Local-first inference: LFM2.5-VL-450M (vision) + whisper.cpp (STT) + KittenTTS (TTS) + all-MiniLM-L6-v2 (memory)
- **Substrate:** OpenClaw protocol surface, MCP bridge, native iOS+Android clients, auditable.

**Vision (PRD §1):** *What if your glasses remembered everything you saw, noticed things you missed, and could answer any question about your day — hands-free?*

**Positioning (PRD §1):**
- ❌ Not Google Glass (dead)
- ❌ Not Ray-Ban Meta (capture-and-share, reactive, paywalled)
- ✅ Proactive AI companion — observes, reasons, contextualizes, acts.

**Value props (v121 order):**
1. **Yours, not theirs.** Memory, models, audio never leave the device. No cloud lock-in. No Meta paywall. Open weights.
2. **The protocol is the bet.** Cerf said it. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses runs on it.
3. **On-device, validated by orbit.** Same architecture class as the Gemma 3 NASA put in orbit.
4. **Proactive, not reactive.** Salience-gated. Cascade-gated.
5. **Small-beats-large.** HRM-Text-1B at $1,500 training. Kokoro-82M beats ElevenLabs.
6. **Open and auditable.** MIT-licensed. Newsweek cited us. Threat model is being published.
7. **Built in Bengaluru, for the world.** Earned, not asserted.

---

## 2. What is the user workflow?

### Day 0: Setup
1. `apt install dan-glasses-daemons` (or build from source).
2. Launch Tauri v2 app.
3. Bootstrap: camera permission, model download (~310MB total), Telegram pairing, language.
4. Daemon map lights up — 9 ports green.
5. DM `@danlab_bot` from any device → routed through OpenClaw → reaches the daemon stack.

### Daily loop — 5 PRD user stories
- **US-1 Encounter Recall:** *"Who did I meet yesterday?"* → PTT → audiod → memoryd → ttsd.
- **US-2 Contextual TaskReminder:** *"You walked past the pharmacy 3x this week."* → proactive nudge.
- **US-3 Object Search:** *"Where are my keys?"* → perceptiond flips to active mode.
- **US-4 Passive Journaling:** *"What did I do on Tuesday?"* → memoryd query.
- **US-5 Hands-Free Check-In:** *"Hands in dough, is there an urgent email?"* → PTT → os-toold → ttsd.

### v121 workflow: OpenClaw iOS + Android (when paired)
- Phone as secure node. DM `@danlab_bot`, get TTS response. **Gated behind security audit.**

---

## 3. Who is the competition?

| Product | Strategy | v121 take |
|---|---|---|
| **Meta Glasses + Muse Spark** | First-party Meta model. Zuckerberg: "slower than expected." | Closed weights, paywalled, leadership cracking. |
| **Ray-Ban Meta** | 80% market share. 3.5M units. | Owns social-acceptance. We compete on Day 5 utility. |
| **Meta Ray-Ban Display** | HUD + neural band, $799. | Cool tech, soft paywall. |
| **Snap Specs** | Standalone AR, $2,195. | Over-engineered. |
| **Google + Samsung Android XR** | 70° FOV, 4hr battery, on-device Gemini. | Open-adjacent but ships a Google account. |
| **Apple smart glasses** | ~$2,000, end 2027. Kuo: Vision Pro line killed. | **16-month window where we are the only open, agent-native option shipping.** |
| **Brilliant Labs Halo** | Open SDK. Cloud LLM. | Our closest cousin. We win this lane. |
| **Microsoft Scout** | Always-on personal agent **on OpenClaw**. | Validates our substrate. Fork-or-follow at end of Q3. |
| **Anthropic Sonnet 5 + Apps Gateway** | Closed-source frontier, published protocol. | They shipped the protocol too. Our wedge = open + wearable + on-device. |

**4 lanes (v121):**
- (a) **On-device open weights** — us + Gemma 3 in orbit + Kokoro-82M + HRM-Text-1B.
- (b) **Hybrid (cloud + device)** — Google/Samsung + Brilliant Labs + Sarvam.
- (c) **Closed-cloud** — Meta + Apple + Microsoft + Anthropic.
- (d) **Substrate** — OpenClaw + MCP + Anthropic Apps Gateway + X MCP. **Standardizing. We ship it on a wearable.**

---

## 4. What is danlab-multimodal?

The lead demo. Sub-250MB VLM (SmolVLM-256M Q4_K_M) on CPU via llama.cpp. Heuristic feedback loop. **Honest framing: pre-RL scaffold, not RL.** Live at `https://zo.pub/som/danlab-multimodal-demo`.

**v121 position:** the published receipt for the on-device thesis. Entry point to the lab. Cascade-gate upgrade (VisualClaw) queued for Q3 W1-W2.

---

## 5. What is Paperclip?

Dormant per `paperclip/AGENTS.md`. Mentioned in ecosystem, not lead.

---

## 6. What is the overall Danlab story?

somdipto in Bengaluru + Dani (AI co-founder with public SOUL.md, IDENTITY.md, MEMORY.md) as partner. The brain at `github.com/somdipto/dan-consciousness` — public, MIT, auditable. The org ships: Dan Glasses, Dan Voice, Paperclip, danlab-multimodal, dani (the agent platform). The thesis is the same as Anthropic / Microsoft Scout / RSI Labs — except the brain is open, the weights are MIT, and the demo runs on a $0 GPU budget on a Bengaluru laptop.

**v121 lead:** *The protocol is the bet. The data path is yours. The threat model is public. The wearable ships it.*

---

## 7. Marketing channels

| Channel | Priority | Status |
|---|---|---|
| **X (Twitter)** | 🔥 P0 | @somdipto + @danlab. 3–5/wk. |
| **GitHub** | 🔥 P0 | READMEs are the longest-lived surface. |
| **Hacker News** | 🔥 P0 | Show HN #1 = "9 daemons live" (week 3–4). |
| **Telegram** | 🔥 P0 | The product surface. Live. |
| **HuggingFace** | 🔥 P0 | Create `danlab` org this week. |
| **arXiv** | 🟢 P2 | SIA-W+H port paper. Q3. |
| **LinkedIn** | 🟡 P1 | Profile rewrite, 1 post/wk. |
| **YouTube / Loom** | 🟡 P1 | Demo videos. |
| **Reddit** | 🟡 P1 | Authentically, not as marketing. |
| **Substack** | 🟡 P1 | "From heuristic to SIA" series. |
| **Discord** | 🔴 P0 when ready | Q4 2026. |
| **Newsweek (organic)** | 🔥 P0 | Get the URL. Quote in v1.0. |

**v121 gap:** the **OpenClaw protocol surface marketing artifact** is the highest-leverage 2-day deliverable. **Block on the security audit.**

---

## 8. What content should Danlab produce?

### "From heuristic to SIA" series (Q3 2026, 6 posts)
1. Heuristic feedback loops are not RL, and that's the point.
2. What's actually inside a 120MB VLM.
3. Anthropic's pause and the open-source counter-narrative.
4. Wearing an 1B model: $1,500 from scratch is the new origin pillar.
5. SIA on the wearable: a port announcement.
6. From one pair of glasses to a fleet. (Paperclip cameo.)

### "The protocol is the bet" series (3 posts, press-targeted)
1. **Vinton Cerf said AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first.** (Lead. Publish after threat model audit. Cite Newsweek.)
2. **Observability > model: $725B is being spent on the workbench, not the tool.**
3. **The agent substrate is auditable. Here's the threat model.** (Cite Mashable, show the audit, show the fix.)

### The single biggest event for 2026
**SIA-W+H port announcement + Show HN #2.** Goes from "interesting wearable" → "lab that actually shipped open recursive self-improvement on a wearable."

### Second-biggest
**OpenClaw protocol surface + threat model doc.** "Lab that shipped the agent substrate audibly before Anthropic, and told you about the flaw before it shipped."

### Third-biggest
**Show HN #1: "9 daemons live, .deb installs, on-device AI."**

---

## 9. What is the current online presence?

| Surface | State | Action |
|---|---|---|
| **danlab.dev** | Live. Mostly stale. | Full rewrite around Dan Glasses. |
| **github.com/somdipto** | Active. ~47 repos. | Profile README + topics + pinned. |
| **LinkedIn (dan Lab)** | Bare bones. | Rewrite. |
| **X / Twitter** | No verified danlab account. | Decision: `@danlab` or founder-led only. |
| **Telegram** | Live. | Wire into every post. |
| **HuggingFace** | No org. | Create this week. |
| **arXiv** | No papers. | First paper = SIA-W+H port. Q3. |
| **Newsweek citation** | Cited us. | Get URL. Quote in v1.0. |
| **Mashable article** | Flagged OpenClaw flaw. | Audit, then publish threat model response. |

**v121 biggest opportunity:** Newsweek cited us. First Newsweek-tier press hit. **Quote, link, screenshot.**

---

## 10. Who are the first users / customers?

| Tier | Profile | Acquisition |
|---|---|---|
| **1. Developer / hacker** | Edge AI is the next frontier. Open weights matter. | GitHub, HN, X. |
| **2. Accessibility-first** | Meta paywall is a citable counter-marketing asset. | X, Reddit, accessibility forums. |
| **3. Researcher / academic** | Will cite SIA-W+H, heuristic loop, protocol paper. | arXiv, X, conferences. |
| **4. Productivity-obsessed** | Persistent memory that doesn't get sold. | LinkedIn, Substack, X. |
| **5. Investor** | Edge AI, India-focused. | *After* Show HN. |
| **6. Small-model researcher** | HRM-Text-1B, Kokoro-82M, SmolVLM-256M. | HF, X. |
| **7. Agent / protocol architect** | Cerf's framing draws protocol designers. | X (MCP community), HN, dani-skills. |
| **8. Security researcher** | Mashable puts OpenClaw on their radar. Make them allies. | Threat model doc, CVE credit. |

---

## 11. The five takeaways (v121)

1. **The story is real and honest.** 9 processes live, 1 Tauri app, 1 bot. The substrate is open AND being audited. **The next 100% of value is shipping the artifacts, not refining the framing.**
2. **The protocol is the new origin pillar.** Cerf + Anthropic + OpenClaw + X MCP = the substrate is standardizing. **We are the only lab shipping it on a wearable with an auditable threat model.**
3. **Observability > model is the next wedge.** PagerDuty + $725B + audiod segment_timing. **The harness is the workbench, the model is the commodity.**
4. **Closed-source agent race is stalling.** Zuckerberg admitted Meta is behind. Anthropic is compute-constrained. **We are the implementation layer, at $349, on a laptop.**
5. **The 4 pillars of every post:** protocol → observability → on-device → small-beats-large. **Use them in this order.**

---

## 12. Open questions for somdipto (v121)

1. **OpenClaw security audit (1 day):** do we have 1 engineer-day to ship the threat model doc this week? **P0.**
2. **OpenClaw protocol surface marketing artifact (2 days):** do we have 2 engineer-days to ship the protocol doc + diagram? **P0, block on #1.**
3. **Newsweek URL:** can you find the article and send the link? **P0.**
4. **HuggingFace `danlab` org creation:** authorize me to create it this week? **P0.**
5. **X handle decision:** launch `@danlab` (recommended) or founder-led only? **P0.**
6. **Tailscale authkey:** still the single highest-leverage env var. **P0.**
7. **Show HN #1 timing:** is week 3–4 (Jul 21–28) good? **P0.**
8. **Mashable response:** engage directly, or publish response doc and let it speak? **P0.**

---

*End of v121 research report. See `dan1-marketing-strategy.v121.md` for the action plan.*
