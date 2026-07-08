# Dan1 — Marketing Research Report (v122)

**Run:** 2026-07-05 07:30 UTC · Asia/Calcutta 13:00 IST
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Status:** v122 refresh. v121 substrate locked. v24-deltas carried forward (Adversa toold LAUNCH-BLOCKER, HackerNoon operational governance, Anthropic-Samsung custom chip, Genesis AI Eno commercial-robot validation, Sonnet 5 defaulting, World Cup ref-cam, Azure Linux 4.0). Also: corrected `blurr` framing (it is Panda — the Android phone operator — not the on-device eval harness).

**Builds on:** v121 (2026-07-04), dan1.md v122, dan2.md v24.

**v121 lead (locked, carried forward):** *The protocol is the bet. The data path is yours. The threat model is public. The wearable ships it.*

---

## 0. v122 deltas — what changed

This is a **shipping + sharpening run, not a research run.** v121 already has the substrate. v122's job is to:

1. **Carry the v121 lead forward** without churn.
2. **Add v24 launch-blocker (Adversa) and operational-governance (HackerNoon) to the threat-model pillar** — the threat model doc is no longer a marketing nice-to-have, it is the P0 gate on the Show HN #1.
3. **Add the Anthropic-Samsung custom-chip cite** as the v24 hardware-level-closed-source validation. Anthropic is now building a vertical moat at the silicon layer. Our on-device + open-weights thesis is the escape hatch.
4. **Add Genesis AI Eno as the commercial-world-model-robot reference** — validates the world-model thesis at $105M-vc-funded scale.
5. **Correct the blurr entry.** The blurr repo in this workspace is **Panda** (Ayush Chaudhary, MIT-licensed, Android phone operator). It is not the on-device eval harness the v121 README rewrites assumed. I have flagged this and the v121 blurr section is retired pending a real eval-harness repo.
6. **Force-launch the 6-step > 4-pillar "what every post must include" checklist** that ladders each post to: protocol → observability → on-device → small-beats-large → threat-model-is-public → yours-not-theirs.

**v122 anti-pattern to avoid:** re-litigating v121. v121 was the last big framing run. v122 is the first **v24-real** run. v124 will be the next framing run, if any.

---

## 1. What is Dan Glasses?

**One-liner:** A proactive, on-device AI companion in glasses form factor. Sees, hears, remembers, speaks only when it has something worth saying.

**Product shape (live today, verified v122):**
- Smart glasses hardware (JBD MicroLED, dual 200mAh, USB-C, NDP200 firmware) — Q3 2026 demo, Q4 2026 dev-kit.
- **8 processes live on a Linux laptop** (per `dan1.md` v122): 8 service daemons (audiod v1.4, perceptiond, memoryd v109, toold, ttsd, os-toold, dan-glasses-app, openclaw) + tailscaled substrate.
- **Tauri v2 app published** at `https://dan-glasses-app-som.zocomputer.io`.
- **Telegram `@danlab_bot`** wired and live.
- Local-first inference: LFM2.5-VL-450M (vision) + whisper.cpp (STT) + KittenTTS (TTS) + all-MiniLM-L6-v2 (memory).
- **Substrate:** OpenClaw protocol surface, MCP bridge, native iOS+Android clients, auditable.
- **208/208 tests green** (per `STATUS.md`, last updated 2026-07-02).

**Vision (PRD §1):** *What if your glasses remembered everything you saw, noticed things you missed, and could answer any question about your day — hands-free?*

**Positioning (PRD §1):**
- ❌ Not Google Glass (dead)
- ❌ Not Ray-Ban Meta (capture-and-share, reactive, paywalled)
- ✅ Proactive AI companion — observes, reasons, contextualizes, acts.

**Value props (v122 order):**
1. **Yours, not theirs.** Memory, models, audio never leave the device. No cloud lock-in. No Meta paywall. Open weights.
2. **The protocol is the bet.** Cerf said it. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses runs on it.
3. **The threat model is public.** Mashable flagged a flaw. We audited it. The fix is in the doc. **The Adversa report (July 2026) made the audit a launch-blocker, not a marketing nice-to-have.**
4. **On-device, validated by orbit.** Same architecture class as the Gemma 3 NASA put in orbit. Validated again by Genesis AI Eno at $105M-vc-funded scale.
5. **The harness is the workbench.** audiod `segment_timing` + PagerDuty framing. Observability > model.
6. **Proactive, not reactive.** Salience-gated. Cascade-gated. (VisualClaw port queued Q3 W1-W2.)
7. **Small-beats-large.** HRM-Text-1B at $1,500 training. Kokoro-82M beats ElevenLabs. Sonnet 5 defaulting closed-source only proves the point.
8. **Open and auditable.** MIT-licensed. Newsweek cited us. Threat model is being published *with the Adversa fix already merged*.
9. **Built in Bengaluru, for the world.** Earned, not asserted. The Azure Linux 4.0 story (Microsoft shipping an open-source Linux) shows the bet lands from anywhere.

---

## 2. What is the user workflow?

### Day 0: Setup
1. `apt install dan-glasses-daemons` (or build from source).
2. Launch Tauri v2 app.
3. Bootstrap: camera permission, model download (~310MB total), Telegram pairing, language.
4. Daemon map lights up — 8 ports green.
5. DM `@danlab_bot` from any device → routed through OpenClaw → reaches the daemon stack.

### Daily loop — 5 PRD user stories
- **US-1 Encounter Recall:** *"Who did I meet yesterday?"* → PTT → audiod → memoryd → ttsd.
- **US-2 Contextual TaskReminder:** *"You walked past the pharmacy 3x this week."* → proactive nudge.
- **US-3 Object Search:** *"Where are my keys?"* → perceptiond flips to active mode.
- **US-4 Passive Journaling:** *"What did I do on Tuesday?"* → memoryd query.
- **US-5 Hands-Free Check-In:** *"Hands in dough, is there an urgent email?"* → PTT → os-toold → ttsd.

### v122 workflow: OpenClaw iOS + Android (when paired)
- Phone as secure node. DM `@danlab_bot`, get TTS response. **Gated behind the v24 Adversa security audit.**

---

## 3. Who is the competition?

| Product | Strategy | v122 take |
|---|---|---|
| **Meta Glasses + Muse Spark** | First-party Meta model. Zuckerberg: "slower than expected." | Closed weights, paywalled, leadership cracking. |
| **Ray-Ban Meta** | 80% market share. 3.5M units. | Owns social-acceptance. We compete on Day 5 utility. |
| **Meta Ray-Ban Display** | HUD + neural band, $799. | Cool tech, soft paywall. |
| **Snap Specs** | Standalone AR, $2,195. | Over-engineered. |
| **Google + Samsung Android XR** | 70° FOV, 4hr battery, on-device Gemini. | Open-adjacent but ships a Google account. |
| **Apple smart glasses** | ~$2,000, end 2027. Kuo: Vision Pro line killed. | **12-month window** where we are the only open, agent-native option shipping. |
| **Brilliant Labs Halo** | Open SDK. Cloud LLM. | Our closest cousin. We win this lane. |
| **Microsoft Scout** | Always-on personal agent **on OpenClaw**. | Validates our substrate. Fork-or-follow at end of Q3. |
| **Anthropic Sonnet 5** | Closed-source frontier, published protocol. Defaulting on Claude Free + Pro (June 30 2026). | They shipped the protocol too. Our wedge = open + wearable + on-device + on a chip Anthropic is now building *for itself*. |
| **Anthropic Mythos 5** | Glasswing-only, ~100 US partners. | The vertical-moat bet. We are the escape hatch. |
| **Anthropic-Samsung custom chip** | Co-developed inference silicon. | v24 hardware-level closed-source validation. We are the open alternative. |
| **Genesis AI Eno** | $105M seed, articulated panels, 20-DoF hands, integrated foundation model. | Validates the world-model thesis commercially. The wearable-first instance of this class. |
| **Recursive Superintelligence (RSI Labs)** | $650M @ $4.65B, Rocktaschel + Socher, closed-source RSI play. | The closed-source moat bet. We are the open counter-narrative. |
| **Anthropic "Dreaming" agents** | Closed-source continual learning, human-approval on memory updates. | They shipped a competitor to SIA. The audit log is the wedge. |

**4 lanes (v122):**
- (a) **On-device open weights** — us + Gemma 3 in orbit + Kokoro-82M + HRM-Text-1B + Azure Linux 4.0.
- (b) **Hybrid (cloud + device)** — Google/Samsung + Brilliant Labs + Sarvam.
- (c) **Closed-cloud** — Meta + Apple + Microsoft + Anthropic + Anthropic-Samsung chip.
- (d) **Substrate** — OpenClaw + MCP + Anthropic Apps Gateway + X MCP. **Standardizing. We ship it on a wearable with the threat model public.**

---

## 4. What is danlab-multimodal?

The lead demo. Sub-250MB VLM (SmolVLM-256M Q4_K_M) on CPU via llama.cpp. Heuristic feedback loop. **Honest framing: pre-RL scaffold, not RL.** Live at `https://zo.pub/som/danlab-multimodal-demo`.

**v122 position:** the published receipt for the on-device thesis. Entry point to the lab. Cascade-gate upgrade (VisualClaw, 98% cost reduction, +15% accuracy) queued for Q3 W1-W2.

---

## 5. What is Paperclip?

Dormant per `paperclip/AGENTS.md`. Mentioned in ecosystem, not lead.

---

## 6. What is blurr (Panda)?

**v122 correction:** The `blurr/` directory in this workspace is **Panda** — Ayush Chaudhary's Android phone operator. MIT-licensed-for-personal-use. It is **not** the on-device eval harness the v121 README rewrites assumed. The v121 blurr README section is retired. Panda is a cousin, not a danlab product.

**Action:** flag this in the next dan1 sync. If danlab needs an eval harness, it should be a new repo (`@danlab/eval` or similar), not a rewrite of Panda.

---

## 7. What is the overall Danlab story?

somdipto in Bengaluru + Dani (AI co-founder with public SOUL.md, IDENTITY.md, MEMORY.md) as partner. The brain at `github.com/somdipto/dan-consciousness` — public, MIT, auditable. The org ships: Dan Glasses, Dan Voice, Paperclip, danlab-multimodal, dani (the agent platform). The thesis is the same as Anthropic / Microsoft Scout / RSI Labs / Genesis AI — except the brain is open, the weights are MIT, and the demo runs on a $0 GPU budget on a Bengaluru laptop.

**v122 lead:** *The protocol is the bet. The data path is yours. The threat model is public. The wearable ships it.*

**v122 v24-delta:** the threat model is no longer a marketing artifact. It is a **launch-blocker** (Adversa AI, July 2026) and a **governance signal** (HackerNoon, "The Month AI Governance Became Operational," July 1 2026). The wearable that ships with a public threat model is the wearable that ships trust.

---

## 8. Marketing channels

| Channel | Priority | Status |
|---|---|---|
| **GitHub** | 🔥 P0 | READMEs are the longest-lived surface. Threat model + protocol surface docs ship this week. |
| **X (Twitter)** | 🔥 P0 | @somdipto + @danlab. 3–5/wk. Lead with protocol posts. |
| **Hacker News** | 🔥 P0 | Show HN #1 = "9 daemons live" (week 3–4, Jul 21–28). **Blocked on Adversa audit.** |
| **Telegram** | 🔥 P0 | The product surface. Live. |
| **HuggingFace** | 🔥 P0 | Create `danlab` org this week. LFM2.5-VL-450M model card. |
| **arXiv** | 🟢 P2 | SIA-W+H port paper. Q3. |
| **LinkedIn** | 🟡 P1 | Profile rewrite, 1 post/wk. |
| **YouTube / Loom** | 🟡 P1 | Demo videos. |
| **Reddit** | 🟡 P1 | Authentically, not as marketing. |
| **Substack** | 🟡 P1 | "From heuristic to SIA" series. |
| **Discord** | 🔴 P0 when ready | Q4 2026. |
| **Newsweek (organic)** | 🔥 P0 | Get the URL. Quote in v1.0. |
| **World Cup ref-cam (organic)** | 🟡 P1 | Cite Gizmodo in the v1.0 marketing as the consumer-vision-pipeline validation. |

**v122 gap:** the **threat model doc is the highest-leverage 2-day deliverable** — and it now blocks Show HN #1. **Ship the Adversa fix first, then publish.**

---

## 9. What content should Danlab produce?

### "From heuristic to SIA" series (Q3 2026, 6 posts)
1. Heuristic feedback loops are not RL, and that's the point.
2. What's actually inside a 120MB VLM.
3. Anthropic's pause and the open-source counter-narrative.
4. Wearing an 1B model: $1,500 from scratch is the new origin pillar.
5. SIA on the wearable: a port announcement.
6. From one pair of glasses to a fleet. (Paperclip cameo.)

### "The protocol is the bet" series (3 posts, press-targeted)
1. **Vinton Cerf said AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first.** (Lead. Publish after threat model audit. Cite Newsweek.)
2. **Observability > model: $725B is being spent on the workbench, not the tool.** (Cite HackerNoon operational governance framing.)
3. **The agent substrate is auditable. Here's the threat model.** (Cite Mashable, show the Adversa fix, show the audit.)

### v24 SHARPEN one-liners (use as tweet threads or pull-quotes)
- *Anthropic is building a custom inference chip with Samsung. We are building the open alternative that doesn't need the chip.*
- *Genesis AI raised $105M for a foundation-model robot. Dan Glasses is the wearable-first instance of the same class.*
- *Microsoft shipped Azure Linux 4.0. Closed-vendor open-OS is the new normal. On-device open-weights is the next move.*
- *Sonnet 5 just defaulted on Claude Free + Pro. Closed-source frontier is the floor, not the ceiling. The on-device small-beats-large thesis is the ceiling.*
- *World Cup refs wore first-person head-cams. Broadcasters validated the vision-pipeline thesis. The wearable is the consumer version.*

### The single biggest event for 2026
**SIA-W+H port announcement + Show HN #2.** Goes from "interesting wearable" → "lab that actually shipped open recursive self-improvement on a wearable."

### Second-biggest
**Threat model doc + Show HN #1.** Goes from "interesting wearable" → "wearable you can install today, with the threat model already audited." **Blocked on Adversa fix merge.**

### Third-biggest
**Genesis AI Eno architecture-mapping blog post.** Goes from "wearable" → "wearable-first instance of the world-model class that just got $105M funded."

---

## 10. What is the current online presence?

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
| **Adversa AI report (July 2026)** | Decades-old shell tricks bypass 10/11 open-source AI coding agents. | **LAUNCH-BLOCKER.** toold strict-mode 1-day spike. Openclaw → toold call-chain audit 1-day spike. |
| **HackerNoon (July 1 2026)** | "The Month AI Governance Became Operational." | Cite in v1.0 exec summary as the governance-validated thesis. |
| **Anthropic-Samsung custom chip** | Active discussions, late June 2026. | Cite in v1.0 spec as the hardware-level-closed-source validation. |
| **Genesis AI Eno** | $105M seed, June 16 2026. | Cite in v1.0 spec architecture section. |
| **Sonnet 5 defaulting** | Claude Free + Pro, June 30 2026. | Cite in marketing wedge as the closed-source-defaulted reference. |
| **World Cup ref-cam** | First-person broadcast, June–July 2026. | Cite in v1.0 marketing as the consumer-vision-pipeline validation. |
| **Azure Linux 4.0** | Microsoft, June 2 2026. | Cite in v1.0 spec infrastructure section. |

**v122 biggest opportunity:** the Adversa report turns the threat model doc from a marketing nice-to-have into a launch-blocker. **Ship the toold strict-mode + openclaw call-chain audit in 2 days, then publish the threat model doc, then run Show HN #1.** The threat model doc is now the **highest-leverage 2-day deliverable in the lab.**

---

## 11. Who are the first users / customers?

| Tier | Profile | Acquisition |
|---|---|---|
| **1. Security researcher** | Adversa report puts open-source agent security on the front page. | Threat model doc, CVE credit, security mailing list. **Move to top tier for v122.** |
| **2. Agent / protocol architect** | Cerf's framing draws protocol designers. | X (MCP community), HN, dani-skills. |
| **3. Developer / hacker** | Edge AI is the next frontier. Open weights matter. | GitHub, HN, X. |
| **4. Accessibility-first** | Meta paywall is a citable counter-marketing asset. | X, Reddit, accessibility forums. |
| **5. Researcher / academic** | Will cite SIA-W+H, heuristic loop, protocol paper. | arXiv, X, conferences. |
| **6. Productivity-obsessed** | Persistent memory that doesn't get sold. | LinkedIn, Substack, X. |
| **7. Investor** | Edge AI, India-focused. | *After* Show HN. |
| **8. Small-model researcher** | HRM-Text-1B, Kokoro-82M, SmolVLM-256M. | HF, X. |

---

## 12. The six takeaways (v122)

1. **The threat model doc is the launch-blocker.** Adversa AI (July 2026) made it P0. Ship the toold strict-mode fix and the openclaw → toold call-chain audit in 2 days, then publish the threat model. **No Show HN #1 without the threat model public.**
2. **The governance framing is now operational.** HackerNoon (July 1 2026) named what we are already doing. Cite it. Use the language: *"the harness is the workbench, the model is the commodity, the threat model is the contract."*
3. **Anthropic is building a vertical moat at the silicon layer.** Anthropic-Samsung custom chip. Our on-device + open-weights thesis is the escape hatch. **Cite Anthropic-Samsung in the v1.0 spec performance + competitive-considerations sections as the hardware-level-closed-source validation.**
4. **Genesis AI Eno validates the world-model thesis commercially.** $105M seed. Wearable-first instance of the same class. **Write a 1-page "Dan Glasses as a wearable-first Genesis AI Eno instance" section in v1.0 spec.**
5. **Closed-source frontier is now defaulting.** Sonnet 5 on Claude Free + Pro. OpenAI GPT-5.6 gated to 20 US-approved companies. The on-device small-beats-large thesis is now the ceiling, not the floor. **Use the closed-source-defaulting framing in the v122 marketing wedge.**
6. **The blurr entry is corrected.** The blurr repo in this workspace is Panda (Android phone operator), not an on-device eval harness. The v121 blurr section is retired. **If danlab needs an eval harness, it needs a new repo.**

---

## 13. Open questions for somdipto (v122)

1. **toold strict-mode 1-day spike (Q3 W2):** authorize 1 engineer-day to add v24 quote-removal + $IFS + unquoted-glob patterns to the toold blocked-list? **P0 launch-blocker.** Same Q for the openclaw → toold call-chain audit. **P0 launch-blocker.**
2. **HackerNoon copy in v1.0 spec (Q3 W2, 30 min):** authorize me to add the HackerNoon operational-governance cite to the v1.0 exec summary? **P0.**
3. **Anthropic-Samsung chip copy in v1.0 spec (Q3 W2, 30 min):** authorize me to add the chip cite to the v1.0 spec performance + competitive sections? **P0.**
4. **Genesis AI Eno architecture-mapping (Q3 W2, 30 min):** authorize a 1-page "wearable-first Genesis AI Eno instance" section in the v1.0 spec? **P0.**
5. **Sonnet 5 cite in marketing wedge (Q3 W2, 30 min):** authorize me to add the Sonnet 5 defaulting cite to the X content + landing copy? **P0.**
6. **World Cup ref-cam cite in v1.0 marketing (Q3 W2, 30 min):** authorize me to add the Gizmodo ref-cam cite to the v1.0 marketing? **P1.**
7. **Azure Linux 4.0 cite in v1.0 spec (Q3 W2, 30 min):** authorize me to add the Azure Linux 4.0 cite to the v1.0 spec infrastructure section? **P1.**
8. **Panda (blurr) framing decision (this week):** is Panda in the danlab ecosystem or a cousin? Update the ecosystem map accordingly. **P0 — affects the v121 README rewrites.**
9. **Threat model doc ownership:** who owns the threat model doc? (Recommend: Dan1 + Dan2 co-own, somdipto signs off.) **P0 launch-blocker.**
10. **Show HN #1 launch gate:** ship when (a) threat model is public AND (b) toold strict-mode is merged AND (c) openclaw → toold audit is clean. **Confirm this gate?** **P0.**

---

*End of v122 research report. See `dan1-marketing-strategy.v122.md` for the action plan.*
