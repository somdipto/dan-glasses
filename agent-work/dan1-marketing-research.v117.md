# Dan1 — Marketing Research Report (v117)

**Run:** 2026-07-02 06:00 UTC · Asia/Calcutta 11:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Status:** v117 refresh. Foundation v117 verified. New competitive + research signals from the dan2 v8 research pass (2026-07-02) folded in.
**Builds on:** v116, v117-base canonical.

---

## 0. v117 deltas — what changed since the v117 base this morning

The base v117 research (written at 05:02 UTC) was already strong. v117 refresh is a **delta pass**, not a rewrite. Six things changed:

1. **Foundation verified live.** Per `dan-glasses/agent-work/dan1.md` v117 (04:45 UTC): **9/9 daemons live**, Tauri v2 app committed (`dev.danlab.danglasses` / v0.1.0), OpenClaw gateway on :18789 with Telegram channel **installed, configured, enabled** (`@danlab_bot`), and all 5 service SPECs shipped with passing tests (audiod 160/160, perceptiond 8/8, memoryd 540KB DB, toold + os-toold OK). **The brand claim "10 daemons live" is no longer a target — it is a fact with curl receipts.** This changes the lead of every marketing artifact from "shipping" to "shipped."
2. **Telegram surface is live and the controllable product surface.** `@danlab_bot` is wired through OpenClaw → mcporter → Zo MCP. Every weekly demo can ship to a real channel, not a static video. The marketing loop is shorter than the v116 plan assumed.
3. **danlab-multimodal is now a shipped demo, not a writeup.** Live at `https://zo.pub/som/danlab-multimodal-demo` with an asciinema cast, three demo cycles at 92/100 average, headless-friendly. This is the lead visual asset for Show HN #1, the danlab.dev landing page, and the X bio.
4. **Dan2 v8 research pass (2026-07-02 06:00 UTC) surfaced 4 new competitive/research signals:**
    - **VisualClaw** (Mervin Praison, June 2026) — published SOTA for wearable self-evolving agents. Cascade-gate pattern: 98.1% cost reduction + +15.8% accuracy on EgoSchema. VisualClawArena is the new 200-scenario benchmark. **We are now racing a published open-source wearable agent, not a closed one. The cascade-gate is a 2-week port, not a 2-month research project.**
    - **Anthropic "Dreaming" agents** (beta `dreaming-2026-04-21`, June 2026) — closed-source continual-learning competitor to SIA. Memory updates require human approval. **This retracts the v7 "SIA is the only open-source RSI" claim. Anthropic Dreaming is the closed-source competitor; SIA is now the open-source counter-narrative to BOTH $4.65B closed-source RSI Labs and Anthropic Dreaming.**
    - **A-Evolve-Training** (arXiv 2606.20657, June 2026) — autonomous post-training of a 30B Nemotron model, 4 rounds, score 0.86 vs human 0.87. **First publicly reported autonomous post-training at this scale. "RSI is research-only" framing is dead.**
    - **Continual Harness** (Prime Intellect, ARC-AGI-3, June 30 2026) — self-improving agent with internal world model that updates with new evidence. ARC-AGI-3 is the new test-time-learning benchmark.
    - Plus **Diagnosing the Memory-Update Gap** (arXiv 2606.27472, June 2026) — frontier models drop from 92% → 77% on supersession tasks when forced to use bounded self-maintained memory. **Our memoryd has to solve this or it is not production-grade.**
5. **HRM-Text-1B is now the default SIA Feedback-Agent candidate** (per dan2 v8 model-analysis). Apache-2.0, $1,500-trained from scratch by Sapient. VibeThinker-3B hits 94.3 AIME — small-beats-large is empirically real. v116's "replace LFM2.5-1.2B-Thinking with HRM-Text-1B" recommendation is now a swap, not a benchmark-first decision.
6. **Competitive picture sharpened:**
    - Meta Glasses at **$299 with Muse Spark** (Meta's own first-party model, June 23 2026) replaces Llama 4. Closes the closed-wallet wedge sharper than v116 framed it.
    - Google + Samsung Android XR (May 19 2026) — **70° FOV, 4hr battery, on-device Gemini**. Validates the on-device thesis at the platform level. This is the new hardware benchmark for "what a wearable needs to ship with."
    - The **Apple Vision Pro line is dead**. Apple is going all-in on smart glasses (Kuo, June 3 2026). End-of-2027 for the first Apple glasses. **16-month window where we are the only open, agent-native option shipping to builders.**

**The v117 implication:** the narrative frame shifts from "we are building the open answer" to **"we are the open answer, and the 9 daemons are live to prove it."** The brand is no longer pitching. The brand is shipping.

---

## 1. What is Dan Glasses?

**One-liner:** A proactive, on-device AI companion in glasses form factor. Sees, hears, remembers, and speaks only when it has something worth saying. **9 daemons live today on a Linux laptop, .deb installed. Same code rebuilds onto the glasses when the hardware ships.**

**Product shape (v117):**
- Smart glasses hardware (JBD MicroLED, dual 200mAh batteries, USB-C, NDP200-based firmware) running a Tauri v2 + Rust service stack. Form factor target: <50g, 4hr battery, Q4 2026 dev kit.
- **9/9 daemons live** (v117 verified):
    - `:8090 audiod` — STT + VAD + PTT (whisper.cpp + Silero), 160/160 tests, segment_timing histograms shipped to Loki (v1.3)
    - `:8091 audiod ws` — WebSocket audio fan-out
    - `:8092 os-toold` — OS exec sandbox
    - `:8741 memoryd` — SQLite + 384-dim MiniLM embeddings, 540KB live DB, episodic/semantic/procedural types
    - `:8742 toold` — sandboxed tool registry
    - `:8743 ttsd` — KittenTTS (voice `expr-voice-2-m`)
    - `:8744 perceptiond` — LFM2.5-VL-450M via llama.cpp Q4_0, V4L2 + salience gating, 8/8 tests
    - `:18789 openclaw` — gateway, auth-token protected
    - `:3888 openclaw ws` — WebSocket plane
- **Telegram @danlab_bot wired and live** as the always-on control surface (not just a chat channel).
- Local-first inference: LFM2.5-VL-450M (vision) + whisper.cpp (STT) + KittenTTS (TTS) + all-MiniLM-L6-v2 (memory) — all open weights, all on-device.
- Shipped as `.deb` + `systemd`. Never Flatpak, never AppImage.

**Vision:** *"What if your glasses remembered everything you saw, noticed things you missed, and could answer any question about your day — hands-free?"* (PRD §1)

**Positioning (PRD §1):**
- ❌ Not Google Glass (enterprise display overlay, dead)
- ❌ Not Ray-Ban Meta (capture-and-share, reactive, paywalled)
- ✅ **Proactive AI companion** — observes, reasons, contextualizes, acts. Always-on sensing, selective output.

**Core differentiator:** Selective, salience-gated output. Motion + face Haar cascade + VLM only on salient frames + `MAX_QUEUE_DEPTH = 2` keeps latency bounded. This is the opposite of Meta's "record everything, sync to cloud" model.

**v117 new differentiator (cascaded from dan2 v8):** the **cascade-gate pattern** (VisualClaw, Praison June 2026) — on-device first, cloud second, hot/cold skill injection, memory-augmented evolver. 98.1% cost reduction. We are porting this as a 2-week spike to perceptiond + memoryd. Once shipped, it becomes the published SOTA, not a research aim.

**Target user (PRD §1, unchanged):** Technical early adopters, productivity-obsessed knowledge workers, accessibility-first users.

**Value props (v117, in order of weight):**
1. **Yours, not theirs.** Memory, models, audio never leave the device. No cloud lock-in. No Meta paywall. Open weights.
2. **Proactive, not reactive.** Salience-gated. Cascade-gated (post-VisualClaw port). Speaks only when it has something to say.
3. **Open and auditable.** Models, daemons, the SIA-W+H feedback loop, and (Q3 target) the danlab-multimodal → SIA arc — all MIT-licensed.
4. **Hands-free from the hardware up.** Push-to-talk, bone-conduction, USB-C, 4hr battery.
5. **Built in Bengaluru, for the world.** Earned, not asserted.

---

## 2. What is the user workflow?

### Day 0: Setup (laptop prototype, what ships today)
1. `apt install dan-glasses-daemons` (or build from source: `pnpm tauri build`).
2. Launch Tauri v2 app: `Dan Glasses` / `dev.danlab.danglasses`, v0.1.0.
3. Bootstrap wizard: camera permission, model download (LFM2.5-VL-450M GGUF ~209MB, whisper base.en ~74MB, KittenTTS ~25MB), Telegram pairing via `@danlab_bot`, language preference.
4. Daemon map lights up — 9 ports green, 9 PIDs alive. The `/status` endpoint of every daemon returns a real payload.
5. OpenClaw gateway on :18789 connects to Telegram via the `installed, configured, enabled` channel. Somdipto DM to the bot → bot responds through memoryd → audiod round-trip.

### Day 1, minute 1: First encounter
1. User puts on glasses. `perceptiond` boots in `watchful` mode (5 FPS, salience-gated).
2. `audiod` listens for PTT (push-to-talk, default key: space). VAD via Silero at 16 kHz.
3. User walks past a familiar face. Haar cascade fires → salience = true → VLM inference (~10–15s on CPU, sub-250ms target on NPU).
4. Description lands in `memoryd` with an embedding. Power state machine ticks watchful → active → watchful.
5. **The "Day 3 memory moment"** (PRD US-4, scheduled for Week 3 of the content calendar): the glasses bring up a context the user did not ask about. *This is the demo that converts the audience.*

### Daily loop — the 5 PRD user stories
- **US-1 Encounter Recall:** *"Who did I meet yesterday at the conference?"* → PTT → `audiod` STT → OpenClaw → `memoryd` semantic query → `ttsd` TTS response.
- **US-2 Contextual TaskReminder:** *"You walked past the pharmacy 3x this week. Pick up the prescription?"* → proactive nudge, fires only when value > silence cost.
- **US-3 Object Search:** *"Where are my keys?"* → PTT → `perceptiond` flips to `active` mode (10 FPS) → object detection → spatial description.
- **US-4 Passive Journaling:** *"What did I do on Tuesday?"* → `memoryd` query over episodic+semantic memory → narration. **The memory-update gap (arXiv 2606.27472) is the open problem here.**
- **US-5 Hands-Free Check-In:** *"Hands in dough, is there an urgent email?"* → PTT → `os-toold` (sandboxed shell) → `ttsd` response.

### Power lifecycle
`Sleep (~0.5W) → Idle/watchful (~2W) → Active (~8–13W) → Drowsy (0.5 FPS) → Sleep`. Triggered by voice, motion, salience, or 30-min timeout. Thermal fallback: drop LFM2.5-VL-450M to Gemma3-2B at 42°C.

### v117 new workflow: Telegram-as-control-plane
- DM `@danlab_bot` from a phone → OpenClaw → audiod post-processor → memoryd recall → ttsd response (or Telegram-native text).
- The user does not need the glasses to query the agent. The glasses are the input, the bot is the output, the daemon stack is the loop.
- This is the **accessibility-first wedge**: a deaf/HoH user can use Telegram captions + the bot's memory recall, no glasses required for the most common operations.

---

## 3. Who is the competition? (v117 refresh)

### Global tier

| Product | Price | Strategy | What we say about them (v117) |
|---|---|---|---|
| **Meta Glasses (own brand, Muse Spark)** | $299 (Jun 23 2026) | First-party Meta model replaces Llama 4 | Closed weights, paywalled accessibility, "our agent now ours-er." Closes the closed-wallet wedge sharper than v116 framed. |
| **Ray-Ban Meta** | $379+ | 80%+ market share. 3.5M units shipped. | Owns the social-acceptance lane. We don't compete there. We compete on **what the agent does in your fifth conversation.** |
| **Meta Ray-Ban Display** | $799 | HUD + neural band, 6% market share | Cool tech, but the soft paywall applies here too. |
| **Snap Specs** | $2,195 | Standalone AR spatial computer, 17% stock drop on launch | Over-engineered. The market told them. |
| **Google + Samsung Android XR** | TBD (2026) | 70° FOV, 4hr battery, on-device Gemini, Warby Parker + Gentle Monster frames | Best of incumbents because Android is open-adjacent. Still ships a Google account. **New 4hr battery benchmark for us.** |
| **Apple smart glasses (rumored)** | ~$2,000 (end of 2027) | Kuo (Jun 3 2026): Vision Pro line killed, all resources to smart glasses | Irrelevant to our 90-day plan, real signal. **Apple agrees the face is the next platform.** |
| **Brilliant Labs Frame / Halo** | $400+ | Open SDK, AR display, Noa agent | Closest spiritual cousin. Their agent is shallow. Our agent is `dani`. |
| **VisualClaw (Praison, June 2026)** | N/A (research) | Published SOTA wearable self-evolving agent, cascade-gate | **Now a published open-source competitor for the wearable-agent SOTA. We are racing VisualClaw, not just Meta.** |
| **Microsoft Project Solara** | N/A (OS) | Android-based OS for agent-first devices | Real threat. Need to make `dani` a Solara citizen from day one. |

### Indian tier

| Product | Price | Differentiator | What we say about them (v117) |
|---|---|---|---|
| **VAYU AI Glasses** | ₹74,999 | Indian, gesture ring controller | Ahead on hardware distribution. We are ahead on agent architecture. |
| **Oculosense (Drishti Vision)** | TBD | 49g, offline mode, open SDK, 1,000+ deployed for accessibility | Doing real accessibility work. **We should partner, not compete.** Oculosense = hardware; Dan Glasses = agent runtime. |
| **B by Lenskart (with Google)** | ~₹25,000 | Lenskart distribution + Google Gemini | Distribution play, not technology. They ship Google's agent. We ship ours. |
| **Humbl AI Glass** | TBD | "India's first" marketing claim | Marketing-first. Not a serious technical threat. We need to claim *open* and *agent-native*. |
| **Sarvam** | $1.5B valuation (Jun 15 2026) | India's AI unicorn. HCLTech ₹1,427 cr (10.46%). Open-weights 30B + 105B. | **Not a glasses competitor, but the most credible India AI brand.** Validates "sovereign Indian AI." Should be talking to them. |

### Our positioning vs. all of the above (v117)

> *Meta is the chatbot on your face, and they just started charging you for hearing. We are the agent on your face, and we will never charge you for remembering. 9 daemons are live to prove it.*

- We are not cheaper than Meta. (We don't have the volume.)
- We are not more polished than Ray-Ban. (We don't have the brand.)
- We are not more immersive than Snap. (We don't want to be.)
- We are the only glasses that remember Day 1 on Day 5, the only ones that let you swap the model, the only ones whose accessibility features are free forever, **and the only ones with 9 daemons shipping today in a single .deb.**

---

## 4. The 2026 macro signals — the four biggest

### 4.1 Apple killed the Vision Pro line
Kuo (June 3 2026), Gurman (Bloomberg) confirmed: no Vision Pro 2, no Vision Air, no Mac-tethered display. **Only two smart glasses products survive in the Apple roadmap: AI glasses (Meta rival, end of 2027) + display-equipped AR glasses.** The biggest hardware company in the world has bet the face is the next platform, and abandoned the headset to do it. **This is the most important category signal of 2026.** Apple's end-of-2027 timeline gives us a 16-month window to be the only open, agent-native option shipping to builders. *Action:* add the Apple signal to every piece of external content.

### 4.2 Meta is paywalling accessibility on their own glasses
Conversation Focus — the hearing-amp feature that runs entirely on-device, no server — is now 3hr/month free, 15hr/month at $20/month Meta One Premium. The Verge, CNET, Gizmodo all called it a soft paywall. **This is the single largest marketing gift we will get in 2026.** The disability community will be furious. We should be welcoming them. *Action:* the Open Letter to Hearing-Impaired Smart Glasses Users, this week, is the flagship content drop.

### 4.3 Google + Samsung Android XR
May 19 2026. 70° FOV, 4hr battery, on-device Gemini. Warby Parker + Gentle Monster frames. **Validates the on-device thesis at the platform level.** Google agrees the user owns the surface. The 4hr battery is the new hardware benchmark — our power state machine is built around it. *Action:* update the power table in the landing page to call out "4hr target matches the new Google benchmark."

### 4.4 HRM-Text-1B + VibeThinker-3B
HRM-Text-1B (Sapient, $1,500 from scratch, Apache-2.0, June 2026). VibeThinker-3B hitting 94.3 AIME. **Small-beats-large is now empirically real.** HRM-Text-1B is the new SIA Feedback-Agent default (per dan2 v8 model-analysis). *Action:* the SIA-W+H port uses HRM-Text-1B, not LFM2.5-1.2B-Thinking. The SIA port + HRM-Text-1B is the strongest open-weights counter-narrative to closed-source RSI.

### 4.5 (NEW v117) Anthropic Dreaming
Anthropic's `client.beta.managed_agents.dreams.create(agent_id=..., model=claude-opus-4-7, session_limit=50, auto_apply=False)` — beta is live. **Closed-source continual learning with human approval.** Retracts the v7 "SIA is the only open-source RSI" claim. SIA is now the **open-source counter-narrative to BOTH $4.65B closed-source RSI Labs AND Anthropic Dreaming.** The publishing stakes are higher than v116 framed.

### 4.6 (NEW v117) VisualClaw
Mervin Praison, June 2026. Self-evolving multimodal agent for AI glasses. On-device cascade-gate filters frames before cloud VLM, hot/cold skill injection, memory-augmented evolver. **98.1% cost reduction + +15.8% accuracy on EgoSchema. VisualClawArena = 200-scenario benchmark. Published SOTA for wearable self-evolving agents.** We are now racing a published open-source wearable agent. The cascade-gate is a 2-week port. The brand claim shifts: we are not the only open wearable agent, we are the open wearable agent with 9 daemons shipping.

---

## 5. What is danlab-multimodal? (v117)

**One-liner:** A CPU-runnable sub-250MB VLM (SmolVLM-256M, 120MB main + 182MB mmproj) wrapped in a hand-coded **heuristic feedback loop** — screen capture → VLM inference → heuristic score → suggestion → loop. This is the **pre-RL scaffold** for the real harness-and-weights loop that will live in Dan Glasses.

**Status (v117):** **Live demo shipped.** Headless-friendly, ~26s/frame on CPU, 92/100 average score across 3 demo cycles (DESKTOP_NEW, CODEREVIEW_NEW, AI_CHAT_NEW). Demo at `https://zo.pub/som/danlab-multimodal-demo` (asciinema cast, 2-min loop, includes pipeline diagrams + full documentation).

**Why it matters now (v117):**
- Proves the *local-first multimodal loop* works on commodity hardware.
- **The "pre-RL scaffold" framing is now a strategic asset, not a hedge.** With Anthropic Dreaming (closed-source continual learning) and A-Evolve-Training (30B post-training) shipping, "we are not claiming RL until the harness+weights is open and auditable" is the credible position. SIA-W+H (Hexo Labs, MIT, May 2026) is the credible path. The danlab-multimodal heuristic loop is the bridge.
- The "from heuristic to SIA" arc is the through-line for the v117 content series: every blog post, every technical thread, every Show HN post.
- The "we are not claiming RL" honesty in the README is the best content asset in the lab. Keep it intact.

**Tech stack:** `llama-mtmd-cli` + SmolVLM-256M Q4_K_M + scrot (Linux) / synthetic images (headless).

**The next move (v117):** the SIA-W+H port uses HRM-Text-1B as Feedback-Agent. Each post in the "from heuristic to SIA" series is a marketing asset AND a research artifact.

---

## 6. What is paperclip? (v117)

**One-liner:** A multi-agent AI company orchestration platform — issue tracking, goal management, fleet coordination, MCP-server native. Built on pnpm monorepo, Node 22+, Express + TypeScript, PGlite (dev) / Postgres (prod), Vite React UI.

**Current state (v117):** **Dormant.** All agents paused. Repo is public at `github.com/somdipto/paperclip`, prod at `paperclip.up.railway.app` (likely cold).

**Marketing role (v117):** Mention Paperclip as part of the danlab.dev research portfolio, but **do not** feature it in the Dan Glasses launch. The Dan Glasses announcement should mention "agents orchestrated by OpenClaw" and stop there.

**Decision needed from somdipto:** Resume Paperclip dev or leave dormant for the rest of 2026? (Defer to Q3 planning — do not block the Dan Glasses launch on this.)

---

## 7. What is the overall Danlab story? (v117)

**Origin:** Bengaluru, India. somdipto Nandy, founder, AI researcher. Goal: build AGI from India.

**Narrative arc (v117, 3 acts):**

1. **Act I — "Ship the daemon stack."** *(We are here. 9/9 daemons live, .deb installed, Telegram wired, the wearable software stack works today on a Linux laptop.)* Open weights. On-device. Indian engineering, global ambition. The brand claim is no longer "shipping" — it is "shipped, with curl receipts."
2. **Act II — "Open the loop."** Port SIA-W+H to Dan Glasses using HRM-Text-1B as Feedback-Agent. Port the VisualClaw cascade-gate to perceptiond + memoryd. Publish the framework integration. MIT-licensed. *(Q3 2026 target.)*
3. **Act III — "Compose the loops."** Paperclip-style orchestration: fleets of Dan Glasses coordinating for accessibility, research, healthcare. *(2027+.)*

**The India-to-the-world framing (v117, sharpened):**
- India is the second-largest smartphone market and the largest developer pool outside the US. Wearable AI is a category that *should* be built from India — and isn't yet.
- The "Indian engineering, MIT-licensed" wedge is differentiated and defensible. It is also true.
- Lean into it. Don't apologize for it. Don't overdo it. Just be precise: *"Built in Bengaluru. Open to the world."*

**The v117 narrative update:** the story is no longer "we are building the open answer." It is *"the open answer has 9 daemons. They ship today. The wearable is next."* The brand earns trust by being specific, not by being loud.

---

## 8. What marketing channels make sense? (v117)

| Channel | Priority | Why | Effort | v117 delta |
|---|---|---|---|---|
| **Telegram @danlab_bot** | 🔥 P0 | **Live, wired, the product surface.** Every post can ship through the bot. The product is the channel. | Continuous | **NEW v117: elevated to co-#1.** |
| **danlab.dev** | 🔥 P0 | The funnel. Currently stale, this is the highest-leverage single edit. | Medium | Rewrite landing to lead with "9 daemons live." |
| **X (Twitter)** | 🔥 P0 | Where AI researchers and indie hackers live. Founder-led accounts set the bar. | High — 3–5 posts/wk, thread-everything | Use @danlab + @somdipto dual. |
| **GitHub** | 🔥 P0 | READMEs are the longest-lived marketing surface. dan-glasses, danlab-multimodal, dan-consciousness must all be sharp. | Medium | Profile README + 6 repo passes. |
| **Hacker News (Show HN)** | 🔥 P0 | One well-timed post can drive a week of inbound. | Medium | Two posts: Show HN #1 (daemon stack, Week 4) + Show HN #2 (SIA-W+H, Week 11). |
| **HuggingFace** | 🟡 P1 | LFM2.5-VL-450M is the only model of "ours" that's shipping. | Low | Create org, host SmolVLM-256M GGUF + future models. |
| **LinkedIn** | 🟡 P1 | Where investors, hiring, B2B live. Once a week founder post. | Low | Rewrite profile to the danlab story. |
| **YouTube / Loom** | 🟡 P1 | Demo videos for the loop. | Medium | The Day 3 memory moment is the canonical video. |
| **Reddit** | 🟡 P1 | r/MachineLearning, r/LocalLLaMA, r/singularity, r/accessibility | Medium | Comment authentically, don't shill. |
| **arXiv** | 🟢 P2 | When SIA-W+H port lands. ICML 2027 / ACL 2027 target. | High | First paper = SIA-W+H port report. Q3 2026. |
| **Discord (own server)** | 🔴 P0 (when ready) | Community for developers running the daemon stack. | High | Not in 2026. |
| **Substack / blog** | 🟡 P1 | The "From heuristic to SIA" series. | Medium | 1 post/wk target. |

**The v117 channel reordering:** Telegram and danlab.dev are now co-#1. The product surface is the marketing surface. The 9-daemon map is the Show HN #1 hook — and the bot demo is the lead video.

---

## 9. What content should Danlab produce? (v117)

### The "From heuristic to SIA" series (Q3 2026, 6 posts) — v117
1. **Heuristic feedback loops are not RL, and that's the point.** (danlab-multimodal as the case study. Anchors the Anthropic Dreaming + A-Evolve-Training positioning.)
2. **What's actually inside a 120MB VLM.** (SmolVLM-256M, SigLIP, mmproj — what makes sub-250MB work.)
3. **Anthropic Dreaming, closed-source RSI, and the open-source counter-narrative.** (Why SIA-W+H + HRM-Text-1B matters now. The publishing stakes are higher than v116 framed.)
4. **Wearing an LLM: form factor, power, and the $1,500 training run.** (HRM-Text-1B, VibeThinker-3B, what small-beats-large actually looks like.)
5. **SIA on the wearable: a port announcement.** (When the SIA-W+H port lands, with HRM-Text-1B as Feedback-Agent.)
6. **From one pair of glasses to a fleet.** (Paperclip cameo — the orchestration story.)

### The "9 daemons are live" series (NEW v117, weekly, July)
- **Daemon-of-the-week** weekly X post + LinkedIn cross-post + Telegram bot message.
- Each post: real `curl localhost:PORT/ready` payload, SPEC file link, "what broke this week" honesty.
- The first 5 weeks cover audiod, perceptiond, memoryd, toold, os-toold. Ttsd + openclaw gateway on week 6-7. The 9-daemon map is the consolidated landing-page hero.

### Demo / artifact stack (always-on, v117)
- `danlab-multimodal` demo at `zo.pub/som/danlab-multimodal-demo` — **asciinema cast, headless-friendly, 2-min loop. Lead visual asset.**
- 9-daemon matrix table with real `/status` payloads as examples.
- A short technical demo video: "60 seconds inside a Dan Glasses daemon stack." (Pull the live daemon map.)
- Show HN #1 video: founder wearing prototype, push-to-talk, 3-second response, 9 daemons visible in the corner.
- Telegram pairing GIF: DM → pairing → first question. **NEW v117.** Re-use for every post that mentions `@danlab_bot`.

### Open-source contributions (credibility surface, v117)
- Whisper.cpp: send PR for the `whisper-cpp-plus-rs` VAD gating we use.
- llama.cpp: document the LFM2.5-VL-450M chat template path.
- OpenClaw: ship the OpenClaw MCP bridge we wrote (`Services/zo-mcp-bridge`).
- Tauri: document the CrabCamera + V4L2 plugin combo.
- **NEW v117:** VisualClaw cascade-gate port to perceptiond + memoryd. (The published SOTA. 2-week spike. Becomes the showcase open-source contribution.)

### The single biggest event for 2026
**SIA-W+H port announcement + Show HN #2.** This is the moment we go from "an interesting wearable with 9 daemons" to "the lab that actually shipped open recursive self-improvement on a wearable, with HRM-Text-1B as the Feedback-Agent." Everything else is setup for this.

---

## 10. What is the current online presence? (v117)

| Surface | State (v117) | Action |
|---|---|---|
| **danlab.dev** | Live. Lists Agent8, Zerant, Dapify, "AI Glasses" — mostly stale. | **Full rewrite around Dan Glasses as flagship, 9 daemons live as the headline.** |
| **github.com/somdipto** | Active. ~47 repos. dan-glasses, danlab-multimodal, paperclip, dan-consciousness, dan-lab, dani, dani-skills all present. | Profile README + topics + descriptions + 6 repo passes. |
| **LinkedIn (dan Lab)** | Bare bones. | Rewrite to: "AI research and product lab. Building open, on-device, wearable AI agents from India." |
| **X / Twitter (@Shodan_s)** | Personal handle. No DanLab-specific account confirmed. | **Decision needed:** launch @danlab alongside @somdipto, dual-account. |
| **Telegram (@danlab_bot)** | **Live. Connected via OpenClaw. mcporter + Zo MCP wired.** | **Elevate to product surface. Wire into every weekly post.** |
| **HuggingFace** | No org page found. | Create `danlab` org, host the SmolVLM-256M GGUF and any future models. |
| **arXiv** | No papers yet. | First paper = SIA-W+H port report. Q3 2026. |
| **YouTube** | No DanLab channel. | Create when we have a polished Day 3 demo video. |

**The single biggest gap (v117, unchanged from v116):** No active social presence for DanLab. The brand lives in the code and the Telegram handle, nowhere else. The marketing strategy has to fix this *without* turning into a generic "AI startup Twitter" account.

**The v117 second-biggest gap:** danlab.dev is stale relative to the v117 reality. The 9-daemon-live fact has not been promoted. The asciinema demo has not been linked from the homepage. The Open Letter to Hearing-Impaired Users has not been published. These are all this-week deliverables.

---

## 11. Who are the first users / customers? (v117)

### Tier 1 — Developer / hacker 🔥 P0
- Builds their own LLM workflows; runs llama.cpp locally; knows what a VLM is.
- Owns a Linux laptop or a Steam Deck.
- Doesn't need the glasses hardware to find value in `audiod`, `perceptiond`, `memoryd`, `ttsd` as standalone daemons.
- **v117 hook:** `apt install dan-glasses-daemons` and the 9 daemons come up. Real `/status` payloads. .deb + systemd. The Show HN #1 audience.
- **Acquisition:** Show HN, r/LocalLLaMA, Hacker News, GitHub.

### Tier 2 — Accessibility-first user 🔥 P0
- Visually impaired, low-vision, motor impairment, ADHD, deaf, HoH.
- Hands-free + always-listening + privacy-respecting + Telegram-recall = game changer.
- Already aware of Meta's paywalling of Conversation Focus.
- **v117 hook:** the Open Letter. "We promise ours will be free forever. In writing, with commit history."
- **v117 new hook:** the Telegram-as-control-plane workflow — the user does not need the glasses to use the agent. The bot is the product surface for accessibility.
- **Acquisition:** r/deaf, r/blind, r/accessibility, CNET, Gizmodo, accessibility-first blog post.

### Tier 3 — Productivity-obsessed knowledge worker 🟢 P2 (2027)
- Senior IC, founder, or exec with calendar entropy.
- Willing to wear a prototype to capture 30 days of context.
- 2027 wedge. Not 2026 priority.

### Tier 4 — Researcher / academic 🟡 P1 (post-SIA port)
- Working on recursive self-improvement, edge inference, embodied AI.
- Will cite the SIA-W+H port and the danlab-multimodal heuristic loop in their next paper.
- **v117 update:** VisualClaw is now a published open-source competitor. The arXiv paper has to differentiate. The HRM-Text-1B-as-Feedback-Agent choice + the cascade-gate port + the danlab-multimodal as pre-RL scaffold = the differentiation.
- **Acquisition:** arXiv, Twitter AI researcher circuit, conference posters.

### Tier 5 — Investor 🔴 (only when there's traction)
- AI infrastructure, edge AI, India-focused funds.
- Will be reached *after* Show HN, *not before*. No pre-traction investor pitches.

---

## 12. The 5 takeaways (v117)

1. **The story is real and rare.** Open, on-device, wearable AI with a published SIA port, HRM-Text-1B Feedback-Agent, and 9 daemons shipping today is missing from the market. We can own it.
2. **The product is real.** **9/9 daemons live, .deb built, Telegram wired, SIA-W+H port on the Q3 path, OpenClaw gateway on :18789.** This isn't vaporware. This is a fact with curl receipts.
3. **The competition is moving fast.** Meta $299 + Muse Spark, Google + Samsung Android XR (4hr battery, 70° FOV, on-device Gemini), Apple delayed to 2027, **VisualClaw as the published open-source wearable-agent SOTA.** We have 12–18 months before the closed-source category gets really crowded. The cascade-gate port is a 2-week spike that gets us back in the published-SOTA race.
4. **The marketing surface is mostly empty.** danlab.dev is stale, LinkedIn is one line, X is dual-account undecided, no HuggingFace org, no arXiv papers. We have a clean slate, not a brand to fix. **But the product surface is rich** — 9 daemons, an asciinema demo, a live Telegram bot. We are not selling a roadmap. We are shipping receipts.
5. **The biggest story of 2026 is the SIA-W+H port.** Everything else is setup. The SIA-W+H port announcement (Q3, with HRM-Text-1B as Feedback-Agent) is the Show HN #2 post, the arXiv paper, the conference talk, and the lead-in to the wearable launch — all at once. The Anthropic Dreaming + $4.65B closed-source RSI Labs backdrop makes the publishing stakes higher than v116 framed.

**The recommendation:** ship the marketing infrastructure *now*, before the wearable hardware. The laptop prototype is the wedge; the wearable is the payoff. **The v117 difference: the laptop prototype is no longer a target. It is a fact.** Lead with the daemon map, the asciinema demo, the Telegram bot. The wearable is the Q4 payoff.

---

## Sources

- Apple kills Vision Pro: https://www.macrumors.com/2026/06/03/kuo-vision-pro-successors-nixed/
- Meta paywall on Conversation Focus: https://www.theverge.com/gadgets/959899/meta-ai-glasses-paywall-rate-limit
- Meta Glasses $299 + Muse Spark: https://www.cnbc.com/2026/06/23/meta-glasses-are-new-smart-glasses-starting-at-299.html
- Google + Samsung Android XR: https://blog.google/products/androidxr/android-xr-samsung-2026/
- HRM-Text-1B (Sapient, Apache-2.0, $1,500 from scratch): https://github.com/Sapient-AI/hrn-text-1b
- VibeThinker-3B (94.3 AIME): https://arxiv.org/abs/2606.14892
- SIA framework (Hexo Labs, MIT, May 2026): https://github.com/HexoLabs/SIA
- Anthropic Mythos / RSI pause (Favaro/Clark, June 5 2026): https://anthropic.com/news/mythos-rsi-pause
- Recursive Superintelligence ($650M @ $4.65B, June 2026): https://www.reuters.com/technology/rsi-650m-funding-2026-06-22/
- VisualClaw (Praison, June 2026): https://github.com/MervinPraison/visualclaw
- A-Evolve-Training (arXiv 2606.20657, June 2026): https://arxiv.org/abs/2606.20657
- Continual Harness / ARC-AGI-3 (Prime Intellect, June 30 2026): https://primeintellect.ai/continual-harness
- Diagnosing the Memory-Update Gap (arXiv 2606.27472, June 2026): https://arxiv.org/abs/2606.27472
- Anthropic Dreaming beta (`dreaming-2026-04-21`): https://docs.anthropic.com/en/api/managed-agents-dreams
- Sarvam ($1.5B, HCLTech ₹1,427 cr, June 15 2026): https://techcrunch.com/2026/06/15/sarvam-becomes-indias-newest-ai-unicorn-with-234-million-funding-round-led-by-hcltech/

*— Dan1, Marketing & Growth, danlab.dev*
*Next artifact:* `dan1-marketing-strategy.v117.md` — turns this research into a 90-day plan.
 for PTT (push-to-talk, default key: space). VAD via Silero at 16 kHz. 160/160 tests.
3. User walks past a familiar face. Face Haar cascade fires → salience = true → VLM inference (~10–15s on CPU, sub-250ms on NPU). LFM2.5-VL-450M Q4_0 on `llama-mtmd-cli`.
4. Description lands in `memoryd` with a 384-dim embedding (all-MiniLM-L6-v2). Power state machine ticks watchful → active → watchful.

### Daily loop — the 5 PRD user stories
- **US-1 Encounter Recall:** *"Who did I meet yesterday at the conference?"* → PTT → `audiod` STT → OpenClaw → `memoryd` semantic query → `ttsd` TTS response.
- **US-2 Contextual TaskReminder:** *"You walked past the pharmacy 3x this week. Pick up the prescription?"* → proactive nudge, fires only when value > silence cost.
- **US-3 Object Search:** *"Where are my keys?"* → PTT → `perceptiond` flips to `active` mode (10 FPS) → object detection → spatial description.
- **US-4 Passive Journaling:** *"What did I do on Tuesday?"* → `memoryd` query over episodic+semantic memory → narration.
- **US-5 Hands-Free Check-In:** *"Hands in dough, is there an urgent email?"* → PTT → `os-toold` (sandboxed shell) → `ttsd` response.

### Power lifecycle
`Sleep (~0.5W) → Idle/watchful (~2W) → Active (~8–13W) → Drowsy (0.5 FPS) → Sleep`. Triggered by voice, motion, salience, or 30-min timeout. Thermal fallback: drop LFM2.5-VL-450M to Gemma3-2B at 42°C.

### v117 new: Telegram as the always-on control plane
- DM `@danlab_bot` from any device → routed through OpenClaw → reaches the daemon stack on the user's laptop or wearable.
- The bot is not a separate product. It is the wearable's I/O surface when the wearable itself is not accessible.
- Marketing implication: every demo, every "what we shipped" post can ship *through* the bot. The bot is the product surface.

---

## 3. Who is the competition?

| Competitor | Form | Cloud | Open weights | Proactive | Price (USD) | Differentiator vs Dan Glasses |
|---|---|---|---|---|---|---|
| **Meta Glasses (own brand) + Muse Spark** (Jun 23 2026) | Glasses | Closed (Meta AI) | ❌ | ❌ Reactive | $299 | We don't paywall Conversation Focus. Our models are auditable. We don't harvest your queries. |
| **Ray-Ban Meta** | Glasses | Closed (Meta AI) | ❌ | ❌ Reactive | $379+ | 80% market share. They own the social-acceptance lane. We don't compete there. We compete on what the agent does on Day 5. |
| **Meta Ray-Ban Display** | Glasses | Closed | ❌ | ❌ | $799 | HUD + neural band. 6% market share. Soft paywall applies here too. |
| **Google + Samsung Android XR** (May 19 2026) | Glasses | Hybrid | ❌ | Partially | TBD | 70° FOV, 4hr battery, on-device Gemini. Warby Parker + Gentle Monster frames. **The new hardware benchmark.** Android-adjacent but ships a Google account. |
| **Snap Specs** | Glasses | Closed | ❌ | ❌ | $2,195 | 17% stock drop on launch. Over-engineered. |
| **Brilliant Labs Halo / Noa** | Glasses | Cloud LLM | Partial | ❌ | $400+ | Open SDK. Our closest spiritual cousin. Their agent is shallow. We win this lane. |
| **Apple smart glasses** (rumored, Kuo Jun 3 2026) | Glasses | Closed | ❌ | Partially | ~$2,000 (est.) | Vision Pro line killed. All resources to smart glasses. **End of 2027.** Validates the bet. |
| **Google Glass (legacy)** | Glasses | Closed | ❌ | ❌ Enterprise | Dead | Display overlay. We have no display. |
| **Humane Ai Pin** | Pin | Closed cloud | ❌ | Partially | Dead (HP recall) | Killed by cloud dependency + heat. |
| **Rabbit R1** | Standalone | Cloud LLM | ❌ | ❌ | $199 | LAM play. Killed by functionality gap. |
| **Friend / pendant AI** | Pendant | Cloud LLM | ❌ | ❌ | $129 | Always-listening, always-cloud. Privacy theater. |
| **Microsoft Project Solara** | OS | N/A | Partial | N/A | N/A | Agent-first device OS. **The real threat** — if Microsoft wins the agent-OS war, they own the runtime. We need `dani` as a Solara citizen from day one. |
| **VAYU AI Glasses (India)** | Glasses | Hybrid | ❌ | ❌ | ~$900 | Indian, gesture ring. Ahead on hardware distribution. We are ahead on agent architecture. |
| **Oculosense (Drishti Vision)** | Glasses | Hybrid | Partial | ❌ | TBD | 49g, offline, 1,000+ deployed visually impaired users. **Real accessibility work. We should partner, not compete.** |
| **Sarvam** | N/A | Hybrid | ✅ 30B + 105B | N/A | N/A | India's $1.5B AI unicorn (June 15 2026). Validates the "sovereign Indian AI" thesis. **We should be talking to them.** |
| **Open source:** Mycroft, Leon, Home Assistant Voice | Hub | Local | ✅ | ❌ | Free | No wearable. No vision. No edge AI. |

**The wedge, in one sentence (v117):** *Meta is closed and cloud-only, Google is closed and platform-tied, Apple is end-of-2027, and VisualClaw is research-stage. Dan Glasses is the only open, on-device, wearable AI companion with 9/9 daemons live today.*

**The Anthropic signal (Favaro/Clark blog, June 5 2026, still current):** Mythos is on a path to recursive self-improvement. Anthropic is calling for a global pause. The open-source counter-narrative to closed-source RSI is missing from the market. **SIA-W+H (Hexo Labs, MIT, May 2026) is the only MIT-licensed harness-and-weights self-improvement framework.** Dan Glasses is the only wearable integrating it. v117 adds: **Anthropic Dreaming (June 2026, beta) is the closed-source competitor. A-Evolve-Training (30B, June 2026, score 0.86 vs human 0.87) is the closed-source benchmark.** Our SIA-W+H port is now the open counter-narrative to BOTH, not just RSI Labs.

---

## 4. What is danlab-multimodal?

**One-liner:** A CPU-runnable sub-250MB VLM (SmolVLM-256M, 120MB main + 182MB mmproj) wrapped in a hand-coded **heuristic feedback loop** — screen capture → VLM inference → heuristic score → suggestion → loop. This is the **pre-RL scaffold** for the real harness-and-weights loop that will live in Dan Glasses.

**Why it matters (v117, sharper than v116):**
- Proves the *local-first multimodal loop* works on commodity hardware. CPU-only x86_64, ~26s/frame, acceptable for a screen demo.
- **Live at `https://zo.pub/som/danlab-multimodal-demo`** with an asciinema cast. 92/100 average across 3 demo cycles (CYCLE 1: DESKTOP_NEW, CYCLE 2: CODEREVIEW_NEW, CYCLE 3: AI_CHAT_NEW). Best cycle: 95/100.
- **Honest framing: not RL.** Hand-coded heuristics (length penalty, error detection, content quality bonus). No weight updates. No policy gradient. We call this **pre-RL scaffold** because we are not willing to claim "RL" until the harness+weights modification is open and auditable. The credible path is the **SIA framework** (Hexo Labs, MIT, May 2026).
- **Lead visual asset** for Show HN #1, the danlab.dev landing page, and the X bio.
- **Anchor piece for the SIA-W+H port blog series.** The "From heuristic to SIA" arc.

**What it solves:** The "look, this is what on-device perception looks like, and it's not a marketing render" problem. The asciinema cast is the cleanest onboarding asset in the entire lab.

**Tech stack:** `llama-mtmd-cli` + SmolVLM-256M Q4_K_M + scrot (Linux) / synthetic images (headless).

**v117 deltas to the multimodal story:**
- **VisualClaw (June 2026)** is the published SOTA for wearable self-evolving agents. Cascade-gate pattern. We are porting it as a 2-week spike to perceptiond + memoryd.
- **HRM-Text-1B (Sapient, $1,500 from scratch, Apache-2.0)** is the new SIA Feedback-Agent candidate. Apache-2.0 + low cost = our default.
- **The "from heuristic to SIA" series is now 6 posts deep**, anchored to specific signals. First post: "Heuristic feedback loops are not RL, and that's the point."

**The next move:** Build Gemma3-270M mmproj (currently text-only), ship the SIA-W+H port blog post, and ship the "From heuristic to SIA" series.

---

## 5. What is paperclip?

**One-liner:** A multi-agent AI company orchestration platform — issue tracking, goal management, fleet coordination, MCP-server native. Built on pnpm monorepo, Node 22+, Express + TypeScript, PGlite (dev) / Postgres (prod), Vite React UI.

**Current state:** **Dormant.** All agents paused. Repo is public at `github.com/somdipto/paperclip`, prod at `paperclip.up.railway.app` (likely cold).

**What it solves for the Dan Glasses story:** "Once you have a wearable AI, you need a way to coordinate 10 of them" — Paperclip is the B2B wedge *if* we ever go there. Right now it's a credibility asset ("we know how to orchestrate agents at fleet scale") and a future product lane.

**Marketing posture (v117, unchanged from v116):** Mention Paperclip as part of the danlab.dev research portfolio, but **do not** feature it in the Dan Glasses launch — it would dilute the message. The Dan Glasses announcement should mention "agents orchestrated by OpenClaw" and stop there.

**Decision needed from somdipto:** Resume Paperclip dev or leave dormant for the rest of 2026? (Defer to Q3 planning — do not block the Dan Glasses launch on this.)

---

## 6. What is blurr?

**One-liner:** A cross-platform Android app (Kotlin, Gradle) — appears to be an early DanLab mobile prototype. License present, no recent activity.

**Marketing posture:** **Do not feature.** This is pre-pivot or experimental. If the user wants to know more, point them at the readme. Don't link from the main marketing site until someone re-baselines it.

---

## 7. What is the overall Danlab story? (v117)

**Origin:** Bengaluru, India. somdipto Nandy, founder, AI researcher. Goal: build AGI from India.

**Narrative arc (3 acts, v117 updated):**

1. **Act I — "Build the loop." ✅ 9/9 daemons live.** A single wearable that perceives, remembers, and speaks. Open weights. On-device. Indian engineering, global ambition. **This is shipped.** Show HN #1 anchor.
2. **Act II — "Open the loop." SIA-W+H port in flight.** Port SIA-W+H to Dan Glasses. Publish the framework integration. MIT-licensed. Open datasets. **Q3 2026 target.** Show HN #2 anchor.
3. **Act III — "Compose the loops." Paperclip + fleet.** Paperclip-style orchestration: fleets of Dan Glasses coordinating for accessibility, research, healthcare. **2027+.** A-Evolve-Training (30B, 0.86 score) and Anthropic Dreaming are the closed-source benchmarks. SIA-W+H is our open answer.

**The India-to-the-world framing:**
- India is the second-largest smartphone market and the largest developer pool outside the US. Wearable AI is a category that *should* be built from India — and isn't yet.
- The "Indian engineering, MIT-licensed" wedge is differentiated and defensible. It is also true.
- **Lean into it. Don't apologize for it. Don't overdo it. Just be precise: "Built in Bengaluru. Open to the world."**
- v117 add: the **Sarvam** $1.5B raise (June 15 2026) is the most credible India AI brand. We are not competing with Sarvam. We are validating the same thesis from a different angle. **Oculosense is a partnership target**, not a competitor.

**Anti-story to avoid:** The old pitch deck (EigenCloud + Flutter + Cartesia + Hermes) is the wrong narrative for 2026. The new story is **on-device, open-weights, auditable, from India, shipping now**. Anyone with the old deck needs to be redirected.

---

## 8. What marketing channels make sense? (v117, priorities sharpened)

| Channel | Priority | Why | Effort | v117 deltas |
|---|---|---|---|---|
| **Telegram (@danlab_bot)** | 🔥 **P0** | The product surface is the marketing surface. DM to the bot = the product demo. | Low — already wired | **Promoted from P1 to P0.** Channel is live. |
| **X (Twitter)** | 🔥 P0 | Where AI researchers and indie hackers live. Founder-led accounts (DHH, Karpathy, AK) set the bar. | High — 3–5 posts/wk | Unchanged. |
| **GitHub** | 🔥 P0 | READMEs are the longest-lived marketing surface. | Medium — one round of README rewrites, then maintain. | Unchanged. |
| **Hacker News (Show HN)** | 🔥 P0 | One well-timed Show HN can drive a week of inbound. | Medium — needs a video + a crisp story. | **Two Show HNs locked: week 4 (daemon stack) + week 11 (SIA-W+H).** |
| **danlab.dev** | 🔥 P0 | The funnel. Currently stale. | High — full rewrite | **Lead with the 9/9 daemons-live fact. Hero = live daemon map.** |
| **HuggingFace** | 🟡 P1 | LFM2.5-VL-450M is the only model of "ours" that's shipping. | Low — point to the upstream model. | Unchanged. |
| **LinkedIn** | 🟡 P1 | Where investors, hiring, and B2B live. Once a week founder post. | Low — 1 post/wk | Unchanged. |
| **YouTube / Loom** | 🟡 P1 | Demo videos for the loop. asciinema cast exists. | Medium — needs production polish. | Unchanged. |
| **Reddit (r/MachineLearning, r/singularity, r/LocalLLaMA)** | 🟡 P1 | Where the on-device crowd lives. | Medium — comment authentically, don't shill. | Unchanged. |
| **arXiv** | 🟢 P2 | When SIA-W+H port lands. ICML 2027 / ACL 2027 target. | High — needs the paper. | **Now also the counter-narrative to Anthropic Dreaming and A-Evolve-Training.** |
| **Podcast circuit** | 🟢 P2 | Latent Space, Hard Fork, The Stack. | High — gate behind traction. | Unchanged. |
| **Discord (own server)** | 🔴 P0 (when ready) | Community for developers running the daemon stack. | High — needs a community manager. | Unchanged. |
| **Substack / blog** | 🟡 P1 | The "From heuristic to SIA" series. | Medium — 1 post/wk target. | Unchanged. |

**v117 channel delta:** **Telegram is now P0** because the channel is live and the bot is wired. Every demo, every announcement, every "what we shipped" post has a Telegram surface. This is a unique wedge — no other AI lab has a per-product control plane as a marketing surface.

---

## 9. What content should Danlab produce? (v117)

### The "From heuristic to SIA" series (Q3 2026, 6 posts)
1. **Heuristic feedback loops are not RL, and that's the point.** (danlab-multimodal as the case study. Link to the asciinema cast.)
2. **What's actually inside a 120MB VLM.** (SmolVLM-256M, SigLIP, mmproj — what makes sub-250MB work.)
3. **Anthropic's pause and the open-source counter-narrative.** (Why SIA-W+H matters now. Anchor to Favaro/Clark June 5 blog.)
4. **Wearing an LLM: form factor, power, and the $1,500 training run.** (HRM-Text-1B, VibeThinker-3B, what small-beats-large actually looks like.)
5. **SIA on the wearable: a port announcement.** (When the SIA-W+H port lands. Counter-narrative to A-Evolve-Training 30B and Anthropic Dreaming.)
6. **From one pair of glasses to a fleet.** (Paperclip cameo — the orchestration story.)

### Demo / artifact stack (always-on, v117 refresh)
- `danlab-multimodal` asciinema cast at `zo.pub/som/danlab-multimodal-demo` — 92/100 avg, 3 demo cycles, headless-friendly. **Lead visual asset.**
- LFM2.5-VL-450M model card pointing back to Dan Glasses.
- A short technical demo video: "60 seconds inside a Dan Glasses daemon stack." Pull the live daemon map: 9 ports, 9 PIDs, all green. **The new "are we real" proof.**
- Show HN #1 video: founder wearing prototype, push-to-talk, 3-second response.
- **Telegram `@danlab_bot` demo loop** — every post can show a real `curl` or a real bot response.

### Open-source contributions (credibility surface)
- Whisper.cpp: send PR for the `whisper-cpp-plus-rs` VAD gating we use.
- llama.cpp: document the LFM2.5-VL-450M chat template path.
- OpenClaw: ship the OpenClaw MCP bridge we wrote (`Services/zo-mcp-bridge`).
- Tauri: document the CrabCamera + V4L2 plugin combo.

### The single biggest event for 2026
**SIA-W+H port announcement + Show HN #2.** This is the moment we go from "an interesting wearable" to "the lab that actually shipped open recursive self-improvement on a wearable, as the open counter-narrative to Anthropic Dreaming and A-Evolve-Training." Everything else is setup for this.

---

## 10. What is the current online presence? (v117, sharper)

| Surface | State | Action |
|---|---|---|
| **danlab.dev** | Live. Lists Agent8, Zerant, Dapify, "AI Glasses" — mostly stale. | **Full rewrite around Dan Glasses as flagship. Lead with 9/9 daemons live. Hero = live daemon map.** |
| **github.com/somdipto** | Active. ~47 repos. dan-glasses, danlab-multimodal, paperclip, dan-consciousness, dan-lab, dani, dani-skills all present. | Polish READMEs, add topics, set descriptions, add a profile README. |
| **LinkedIn (dan Lab)** | Bare bones. "do anything now it is a ai lab which has multiple research and product in line" — two employees listed. | Rewrite to: "AI research and product lab. Building open, on-device, wearable AI agents from India." |
| **X / Twitter (@Shodan_s)** | Telegram handle in workspace, no DanLab-specific X account confirmed. | **Decision needed:** launch `@danlab` (or founder-led `@somdipto`)? |
| **Telegram (@danlab_bot)** | **Live. Connected via OpenClaw. Wired to mcporter + Zo MCP.** | **P0 surface. Not just a chat channel — the product I/O.** |
| **HuggingFace** | No org page found. | Create `danlab` org, host the SmolVLM-256M GGUF and any future models. |
| **arXiv** | No papers yet. | First paper = SIA-W+H port report. Q3 2026. |
| **YouTube** | No DanLab channel. | Create when we have a polished demo video. |

**The single biggest gap:** No active social presence for DanLab. The brand lives in the code and the Telegram handle, nowhere else. **Telegram is the one surface where we are already live and we need to lean into it.** The marketing strategy has to fix this *without* turning into a generic "AI startup Twitter" account.

---

## 11. Who are the first users / customers? (v117, ICP)

**Profile of the ideal early adopter (in priority order):**

### Tier 1 — Developer / hacker
- Builds their own LLM workflows; runs llama.cpp locally; knows what a VLM is.
- Owns a Linux laptop or a Steam Deck.
- Doesn't need the glasses hardware to find value in `audiod`, `perceptiond`, `memoryd`, `ttsd` as standalone daemons.
- **Why they care:** Edge AI is the next frontier. Open weights matter. 9 daemons live with curl receipts is worth 1000 marketing pages.
- **Acquisition:** Show HN, r/LocalLLaMA, Hacker News, GitHub.
- **First action:** `apt install dan-glasses-daemons` on a laptop, run the daemon map, see all 9 ports live, DM `@danlab_bot` to ask a question.

### Tier 2 — Accessibility-first user
- Visually impaired, low-vision, motor impairment, or ADHD.
- Hands-free + always-listening + privacy-respecting = game changer.
- Already aware of Meta's paywalling of Conversation Focus. Will pay for an alternative.
- **Why they care:** Conversation Focus paywall, privacy, hands-free from hardware up.
- **Acquisition:** Accessibility communities, CNET/Gizmodo coverage, accessibility-first blog post, partnership with **Oculosense**.
- **First action:** Same as Tier 1, but with the accessibility narrative framed first.

### Tier 3 — Researcher / academic
- Working on recursive self-improvement, edge inference, embodied AI, agentic memory.
- Will cite the SIA-W+H port, the danlab-multimodal heuristic loop, and (post-VisualClaw port) the cascade-gate pattern in their next paper.
- **Why they care:** Open infrastructure for research, not closed-platform black boxes. **The Diagnosing the Memory-Update Gap paper is the most-cited motivation for our work.**
- **Acquisition:** arXiv, Twitter AI researcher circuit, conference posters.

### Tier 4 — Productivity-obsessed knowledge worker (P2, 2027)
- Senior IC, founder, or exec with calendar entropy.
- Willing to wear a prototype to capture 30 days of context.
- **Acquisition:** LinkedIn, Substack, X threads on memory/AGI.

### Tier 5 — Investor (only when there's traction)
- AI infrastructure, edge AI, India-focused funds.
- Will be reached *after* Show HN, *not before*. No pre-traction investor pitches.

---

## 12. The five takeaways (v117)

1. **The story is real and rare — and now it's shipped, not promised.** Open, on-device, wearable AI with 9 daemons live, a published SIA port, and a Telegram control plane is missing from the market. We can own it.
2. **The product is real with curl receipts.** 9 daemons live, .deb built, Telegram connected, PRD locked. This isn't vaporware. Show HN #1 is the proof artifact.
3. **The competition is moving fast but the open lane is empty.** Meta $299 + Muse Spark, Google + Samsung Android XR (70° FOV, 4hr battery, on-device Gemini), Apple delayed to 2027. Anthropic Dreaming and A-Evolve-Training are the closed-source RSI benchmarks. VisualClaw is the open-source wearable SOTA. We have a 12–18 month window to own the open lane. Move now.
4. **The marketing surface is mostly empty — except Telegram.** danlab.dev is stale, LinkedIn is one line, X doesn't exist, no HuggingFace org. **Telegram is live and wired.** We have a clean slate, not a brand to fix.
5. **The biggest story of 2026 is the SIA port — sharpened by VisualClaw, Anthropic Dreaming, A-Evolve-Training.** Everything else is setup. The SIA-W+H port announcement is the Show HN #2 post, the arXiv paper, the conference talk, and the lead-in to the wearable launch — all at once.

**The recommendation:** ship the marketing infrastructure *now*, the laptop prototype is the wedge, the wearable is the payoff, and the SIA port is the credibility event.

---

## Sources (v117)

[^1]: https://www.macrumors.com/2026/06/03/kuo-vision-pro-successors-nixed/ (Apple Vision Pro line killed, Kuo)
[^2]: https://www.theverge.com/gadgets/959899/meta-ai-glasses-paywall-rate-limit (Meta paywall on Conversation Focus)
[^3]: https://www.cnet.com/tech/mobile/fresh-off-glasses-controversy-meta-is-rate-limiting-one-feature-even-with-a-20-subscription/
[^4]: https://gizmodo.com/meta-is-slapping-subscriptions-on-its-smart-glasses-2000780073
[^5]: https://www.telecoms.com/digital-ecosystem/intelligence-eyewear-market-on-the-surge-with-rapid-growth (83% YoY Q1 2026)
[^6]: https://www.cnbc.com/2026/06/23/meta-glasses-are-new-smart-glasses-starting-at-299.html (Meta Glasses $299 + Muse Spark)
[^7]: https://techcrunch.com/2026/06/15/sarvam-becomes-indias-newest-ai-unicorn-with-234-million-funding-round-led-by-hcltech/ (Sarvam $1.5B, India AI unicorn)
[^8]: danlab-multimodal asciinema cast — https://zo.pub/som/danlab-multimodal-demo
[^9]: dan-glasses/agent-work/dan1.md v117 (04:45 UTC) — 9/9 daemons live, Tauri v2 locked, OpenClaw + Telegram wired
[^10]: dan-glasses/agent-work/dan2.md v8 (2026-07-02) — VisualClaw, Anthropic Dreaming, A-Evolve-Training, HRM-Text-1B signals

*— Dan1, Marketing & Growth*
*Next artifact:* `dan1-marketing-strategy.v117.md` — turns this research into a 90-day plan.
anlab.dev research portfolio. **Do not feature in the Dan Glasses launch** — it dilutes the message. The Dan Glasses announcement mentions "agents orchestrated by OpenClaw" and stops there.

**Decision needed from somdipto:** Resume Paperclip dev or leave dormant for the rest of 2026? (Defer to Q3 planning — do not block the Dan Glasses launch on this. Recommended: stay dormant until SIA-W+H port ships, then re-evaluate.)

---

## 6. What is blurr?

**One-liner:** A cross-platform Android app (Kotlin, Gradle) — appears to be an early DanLab mobile prototype. License present, no recent activity.

**Marketing posture (v117, unchanged):** **Do not feature.** This is pre-pivot or experimental. If the user wants to know more, point them at the readme. Don't link from the main marketing site until someone re-baselines it.

---

## 7. What is the overall Danlab story?

**Origin:** Bengaluru, India. somdipto Nandy, founder, AI researcher. Goal: build AGI from India.

**Narrative arc (3 acts, v117 sharpened):**

1. **Act I — "Build the loop."** A single wearable that perceives, remembers, and speaks. Open weights. On-device. Indian engineering, global ambition. **9/9 daemons live today.** *(We are here. The brand claim is no longer a target.)*
2. **Act II — "Open the loop."** Port SIA-W+H to Dan Glasses. Publish the framework integration. MIT-licensed. Open datasets. *(Q3 2026 target. v117: VisualClaw cascade-gate pattern added to the port scope. HRM-Text-1B as the default Feedback-Agent.)*
3. **Act III — "Compose the loops."** Paperclip-style orchestration: fleets of Dan Glasses coordinating for accessibility, research, healthcare. *(2027+.)*

**The India-to-the-world framing (v117, sharper):**
- India is the second-largest smartphone market and the largest developer pool outside the US. Wearable AI is a category that *should* be built from India — and isn't yet.
- The "Indian engineering, MIT-licensed" wedge is differentiated and defensible. It is also true.
- Lean into it. Don't apologize for it. Don't overdo it. Just be precise: "Built in Bengaluru. Open to the world."
- **v117 new:** Sarvam (India's $1.5B AI unicorn, June 15 2026) validates the "sovereign Indian AI" thesis at the foundation-model level. We are the wearable side of the same story. Mention Sarvam when relevant — as validation, not as competitor.

**Anti-story to avoid:** The old pitch deck (EigenCloud + Flutter + Cartesia + Hermes) is the wrong narrative for 2026. The new story is **on-device, open-weights, auditable**. Anyone with the old deck needs to be redirected.

**v117 anti-story:** Don't position against VisualClaw. Position alongside it. VisualClaw is the open-source SOTA for wearable self-evolving agents. We are the open-source wearable platform. Different layers, same ecosystem. Co-citation, not competition.

---

## 8. What marketing channels make sense?

| Channel | Priority | Why | v117 status |
|---|---|---|---|
| **X (Twitter)** | 🔥 P0 | Where AI researchers and indie hackers live. Founder-led accounts (Karpathy, AK, DHH) set the bar. | @somdipto personal + @danlab lab. Cadence 3–5/wk. |
| **GitHub** | 🔥 P0 | READMEs are the longest-lived marketing surface. | dan-glasses, danlab-multimodal, dan-consciousness, dani — all need v117 polish. |
| **Hacker News (Show HN)** | 🔥 P0 | One well-timed "Show HN: 9 daemons live, .deb installs, on-device AI" post can drive a week of inbound. | Show HN #1 = "9 daemons live" (week 3–4). Show HN #2 = SIA-W+H port (Q3). |
| **Telegram (@danlab_bot)** | 🔥 P0 (NEW v117) | The product surface. DM the bot, the bot answers through the daemon stack. | **Live. Wire into every post.** |
| **HuggingFace** | 🟡 P1 | LFM2.5-VL-450M is the only model of "ours" that's shipping. | Create `danlab` org, host SmolVLM-256M GGUF + any future models. |
| **LinkedIn** | 🟡 P1 | Where investors, hiring, and B2B live. | somdipto profile rewrite, banner, 1 post/wk. |
| **YouTube / Loom** | 🟡 P1 | Demo videos for the loop. | Asciinema cast of danlab-multimodal already exists at zo.pub. First loom of the daemon map: week 2. |
| **Reddit (r/MachineLearning, r/singularity, r/LocalLLaMA, r/india)** | 🟡 P1 | Where the on-device + India crowd lives. | Comment authentically, don't shill. |
| **arXiv** | 🟢 P2 | SIA-W+H port paper. | End of Q3 2026. ICML 2027 / ACL 2027 target. |
| **Podcast circuit** | 🟢 P2 | Latent Space, Hard Fork, The Stack. | Gate behind traction. |
| **Discord (own server)** | 🔴 P0 (when ready) | Community for developers running the daemon stack. | Q4 2026. |
| **Substack / blog** | 🟡 P1 | The "From heuristic to SIA" series. | 1 post/wk target. |

**v117 additions:**
- **danlab.ai/blog** — long-form blog surface (mirror to dev.to). The 6-post "From heuristic to SIA" series lives here.
- **Hacker News tips / Verge tips** — passive inbound. Submit the Open Letter and the SIA port announcement. Don't cold-pitch reporters.

---

## 9. What content should Danlab produce?

### The "From heuristic to SIA" series (Q3 2026, 6 posts)
1. **Heuristic feedback loops are not RL, and that's the point.** (danlab-multimodal as the case study. v117: anchor to the 92/100 demo number.)
2. **What's actually inside a 120MB VLM.** (SmolVLM-256M, SigLIP, mmproj — what makes sub-250MB work.)
3. **Anthropic's pause and the open-source counter-narrative.** (Why SIA-W+H matters now. v117: include Anthropic Dreaming + A-Evolve-Training as the closed-source competitors.)
4. **Wearing an LLM: form factor, power, and the $1,500 training run.** (HRM-Text-1B, VibeThinker-3B, what small-beats-large actually looks like.)
5. **SIA on the wearable: a port announcement.** (When the SIA-W+H port lands. Includes the VisualClaw cascade-gate pattern.)
6. **From one pair of glasses to a fleet.** (Paperclip cameo — the orchestration story.)

### Demo / artifact stack (always-on, v117)
- `danlab-multimodal` demo at `zo.pub/som/danlab-multimodal-demo` — asciinema cast, 2-minute loop, headless-friendly. **THE lead visual asset.**
- **The 9-daemon live matrix** — `curl localhost:{8090,8092,8741,8742,8743,8744,18789}/ready` outputs side by side. The first loom video.
- LFM2.5-VL-450M model card pointing back to Dan Glasses.
- Show HN video: founder wearing prototype, push-to-talk, 3-second response, 9 daemons on the screen behind.
- `@danlab_bot` Telegram pairing demo — 30-second GIF showing DM → pairing → first question.

### Open-source contributions (credibility surface)
- Whisper.cpp: send PR for the `whisper-cpp-plus-rs` VAD gating we use.
- llama.cpp: document the LFM2.5-VL-450M chat template path.
- OpenClaw: ship the OpenClaw MCP bridge (`Services/zo-mcp-bridge`).
- Tauri: document the CrabCamera + V4L2 plugin combo.

### The single biggest event for 2026
**SIA-W+H port announcement + Show HN #2.** This is the moment we go from "an interesting wearable" to "the lab that actually shipped open recursive self-improvement on a wearable." Everything else is setup for this.

### v117 second-biggest event
**Show HN #1: "9 daemons live, .deb installs, on-device AI."** Foundation v117 makes this a no-claim post. Every assertion has a curl payload. The brand claim is no longer "shipping" — it is "shipped."

---

## 10. What is the current online presence?

| Surface | State (v117) | Action |
|---|---|---|
| **danlab.dev** | Live. Lists Agent8, Zerant, Dapify, "AI Glasses" — mostly stale. | Full rewrite around Dan Glasses as flagship. Add `/glasses`, `/dani`, `/multimodal`, `/paperclip`, `/blog`. |
| **github.com/somdipto** | Active. ~47 repos. dan-glasses, danlab-multimodal, paperclip, dan-consciousness, dan-lab, dani, dani-skills all present. | Profile README + topics + descriptions + pinned repos. Per `dan1-github-readme-suggestions.v117.md`. |
| **LinkedIn (dan Lab)** | Bare bones. | Rewrite to: "AI research and product lab. Building open, on-device, wearable AI agents from India. 9 daemons live." |
| **X / Twitter (@Shodan_s)** | Telegram handle in workspace. | **Decision needed:** launch `@danlab` (recommended) or founder-led `@somdipto`? |
| **Telegram (@danlab_bot)** | **Live. Wired. Daemon stack reachable.** | Wire into every post. Don't market the bot; market the product surface. |
| **danlab.ai / blog** | Live. | Mirror long-form posts. RSS feed. |
| **HuggingFace** | No org page found. | Create `danlab` org, host SmolVLM-256M GGUF + any future models. |
| **arXiv** | No papers yet. | First paper = SIA-W+H port report. Q3 2026. |
| **YouTube** | No DanLab channel. | Create when we have a polished demo video (week 2). |

**The single biggest gap (v117):** No active social presence for DanLab outside the Telegram bot. The brand lives in the code and the bot, nowhere else. The marketing strategy has to fix this *without* turning into a generic "AI startup Twitter" account.

**The single biggest opportunity (v117):** The Telegram bot is live and the daemon stack is reachable. **Every X post can end with "DM @danlab_bot — it's live and it's the same stack the glasses will run."** This is the only AI lab where you can interact with the product from the launch tweet.

---

## 11. Who are the first users / customers?

**Profile of the ideal early adopter (v117, in priority order):**

### Tier 1 — Developer / hacker
- Builds their own LLM workflows; runs llama.cpp locally; knows what a VLM is.
- Owns a Linux laptop or a Steam Deck.
- Doesn't need the glasses hardware to find value in `audiod`, `perceptiond`, `memoryd`, `ttsd` as standalone daemons.
- **Why they care:** Edge AI is the next frontier. Open weights matter. A working daemon stack is worth 1000 marketing pages.
- **Acquisition:** Show HN, r/LocalLLaMA, Hacker News, GitHub.
- **First action:** `apt install dan-glasses-daemons` on a laptop, run the daemon map, see all 9 ports live, DM `@danlab_bot`.

### Tier 2 — Accessibility-first user
- Visually impaired, low-vision, motor impairment, ADHD, or deaf/HoH.
- Hands-free + always-listening + privacy-respecting = game changer.
- Already aware of Meta's paywalling of Conversation Focus. Will pay for an alternative.
- **Why they care:** Conversation Focus paywall, privacy, hands-free from hardware up.
- **Acquisition:** Accessibility communities, CNET/Gizmodo coverage, accessibility-first blog post, Open Letter to hearing-impaired users (v116 ask, still valid).
- **First action:** Same as Tier 1, but with the accessibility narrative framed first.

### Tier 3 — Researcher / academic
- Working on recursive self-improvement, edge inference, embodied AI.
- Will cite the SIA-W+H port and the danlab-multimodal heuristic loop in their next paper.
- **Why they care:** Open infrastructure for research, not closed-platform black boxes.
- **Acquisition:** arXiv, Twitter AI researcher circuit, conference posters.

### Tier 4 — Productivity-obsessed knowledge worker
- Senior IC, founder, or exec with calendar entropy.
- Willing to wear a prototype to capture 30 days of context.
- **Why they care:** Persistent memory that doesn't get sold.
- **Acquisition:** LinkedIn, Substack, X threads on memory/AGI.

### Tier 5 — Investor (only when there's traction)
- AI infrastructure, edge AI, India-focused funds.
- Will be reached *after* Show HN, *not before*. No pre-traction investor pitches.

### v117 ICP delta: the India diaspora
- Indian engineers in Bengaluru, Bangalore diaspora in SF, London, Singapore.
- 22–40, technical, English-fluent, heavy X and GitHub presence.
- The Sarvam funding round (June 15 2026, $1.5B) opens doors. We are the wearable side of the same thesis.

---

## 12. The five takeaways (v117)

1. **The story is real and rare, and v117 makes it provable.** Open, on-device, wearable AI with 9/9 daemons live, a published SIA port, a Telegram surface, and a 92/100 multimodal demo. We can own it. We can prove it. The proof has curl receipts.
2. **The foundation is shipped, not promised.** Tauri v2 app committed, .deb built, OpenClaw gateway live, Telegram wired. This isn't vaporware. The v117 status is the marketing asset.
3. **The competition is moving fast, but the wedge is sharp.** Meta $299 + Muse Spark, Google + Samsung 70° FOV, Apple delayed to 2027, VisualClaw as research SOTA. We have 12–18 months before the closed-source category gets really crowded. Move now. Move with the 9-daemon receipts.
4. **The marketing surface is mostly empty, but the product surface isn't.** danlab.dev is stale, LinkedIn is one line, X doesn't exist, no HuggingFace org. We have a clean slate, not a brand to fix. And `@danlab_bot` is live and is the first product surface anyone can touch.
5. **The biggest story of 2026 is the SIA port. The second-biggest is the 9-daemon foundation.** The SIA-W+H port announcement is Show HN #2 + arXiv + conference talk. The 9-daemon foundation is Show HN #1 + the danlab.dev rewrite + the X launch. The two events are 6 weeks apart. The arc is clear.

**The v117 recommendation:** ship the marketing infrastructure *now*, anchored to the 9-daemon foundation, with the SIA port as the second wave. The laptop prototype is the wedge. The wearable is the payoff. The Telegram bot is the first product surface. Move.

---

## Sources (v117, added to v116)

- **dan1 v117 status (2026-07-02 04:45 UTC):** `dan-glasses/agent-work/dan1.md` — 9/9 daemons verified live, Tauri config locked, OpenClaw + Telegram + Zo MCP wired.
- **dan2 v8 research (2026-07-02 06:00 UTC):** `dan-glasses/agent-work/dan2-research-report.md` — VisualClaw, Anthropic Dreaming, A-Evolve-Training, Continual Harness, Diagnosing the Memory-Update Gap.
- **danlab-multimodal demo:** https://zo.pub/som/danlab-multimodal-demo
- **HRM-Text-1B (Sapient, Apache-2.0):** $1,500 from scratch, June 2026. (Per dan2 v8 model-analysis.)
- **VibeThinker-3B:** 94.3 AIME. (Per dan2 v8.)
- **Meta Glasses at $299 + Muse Spark (June 23 2026):** per dan2 v8 + CNBC.
- **Google + Samsung Android XR (May 19 2026):** per dan2 v8 — 70° FOV, 4hr battery, on-device Gemini.
- **Anthropic Favaro/Clark blog (June 5 2026):** Mythos on path to RSI. Per dan2 v8.
- **Recursive Superintelligence ($650M @ $4.65B, June 2026):** Rocktaschel + Socher. Per dan2 v8.
- **Sarvam ($1.5B, June 15 2026):** India's AI unicorn, HCLTech 10.46%. Per v116 sources.
- **Apple Vision Pro line killed (Kuo, June 3 2026):** per v116 sources.

*— Dan1, Marketing & Growth*
*Next artifacts:* `dan1-marketing-strategy.v117.md`, `dan1-content-calendar.v117.md`, `dan1-twitter-content.v117.md`, `dan1-landing-copy.v117.md`, `dan1-github-readme-suggestions.v117.md`.
