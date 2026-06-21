# Dan2 — Technical Research Report (v2, 2026-06-15)
**Status:** Final v2
**Audience:** somdipto (decision-maker), Dan1/Dan3/Dan4 (peer architects)
**Scope:** Deep technical + AGI landscape research informing Danlab's 6/12/24-month roadmap
**Run window:** 2026-06-15 02:45 UTC
**Delta from v1 (2026-06-14):** 5 new events in 18 hours that **reset the sovereign-AI and open-source-self-improving theses**. The Anthropic Mythos/Fable suspension on June 12, combined with the TCS-India partnership, the Carney-G7 diversification statement, and Vembu's "globalisation is dead" declaration, makes the bet sharper and more time-sensitive.

---

## 0. TL;DR (3 paragraphs)

The Danlab stack is in a **materially better position than the canonical PRD implies**. The 7/7 daemons are live, 106/106 tests green, Tauri v2 app wired, OpenClaw gateway with Telegram + Zo MCP bridge, danlab-multimodal heuristic loop is honestly framed ("pre-RL scaffold"). The PRD is stale on language split (Python daemons, not Rust) and IPC transport (HTTP loopback, not Unix socket). The biggest gap is **wearable silicon characterization**, not software architecture.

The June 12 2026 Anthropic suspension of Fable 5 + Mythos 5 globally is the **single biggest signal in 2026 for Danlab's thesis**. The U.S. government used export-control authorities to block foreign national access to Mythos; Anthropic complied by disabling the model for **all** users, including U.S. customers, because the compliance scope was unworkable. The Mythos competition threat is now offline. Sridhar Vembu (Zoho, India) called it "globalisation is dead. Bharat must find her own way." Canadian PM Mark Carney at the G7 (June 14) called U.S. AI restrictions "dangers of overreliance on a limited number of American providers." The Anthropic-TCS partnership announced June 11 (one day before the suspension) is now a stranded investment. **The sovereign, open-source, locally-resident agent stack is no longer a research bet — it is the only viable path for everyone outside the U.S. + select partners.** memoryd v2 v1.0 in September 2026 ships into this window.

The 5-front competitive landscape is sharper: Microsoft Scout (OpenClaw-on-M365, Build 2026 June 2) carries the "addicted users" memo leak and is the closed-stack enterprise reference; Anthropic Fable is now **offline globally** as of June 12; Apple Vision Pro M5 lives with visionOS 27 "see what you see" (WWDC26 June 8) as Apple's bridge product; Brilliant Labs Halo ships July 2026 with LFM2-VL-450M as the open-source glasses reference; Monako Glass ships Aug 2026 at 48g Linux. The **18-month wearable window is unchanged** but the value of the local-first open-source alternative has gone from billions to tens of billions in 48 hours. **The bet is: ship the only local-first, open-source, memory-first, memory-evolving, harness-evolving wearable agent + open agent standard before Microsoft Scout GA (Oct 2026) AND before Apple Glasses N50 (late 2027).** Dan1/Dan2/Dan3/Dan4 = trainable parameters via Anthropic SkillOpt + Microsoft SkillOpt.

---

## 1. State of the Danlab System (ground truth, June 15 2026)

### 1.1 What's actually shipped (verified 02:45 UTC, June 15)

| Component | State | Port | Tests | Notes |
|---|---|---|---|---|
| **audiod v2.4** | Running, RFC 6455 WS, schema-conformance pinned | :8090 + WS :8091 | 66/66 ✅ | whisper-cli + Silero VAD, ggml-tiny/base |
| **perceptiond v4** | LFM2.5-VL-450M Q4_0 + mmproj, salience-gated | :8092 | 8/8 ✅ | SmolVLM-256M fallback |
| **memoryd v1** | FastAPI + aiosqlite + all-MiniLM-L6-v2 (384d), 3 types | :8741 | 11/11 ✅ | episodic/semantic/procedural |
| **toold v1** | Shell/python/exec_file, sandbox `/tmp/toold-sandbox` | :8742 | 15/15 ✅ | 3 tools enabled |
| **ttsd v1** | KittenTTS medium, 8 expr voices, /speak + /play | :8743 | 6/6 ✅ | 24kHz WAV output |
| **os-toold v1** | Command execution with path guard | :8744 | healthy ✅ | recurring regression (still no `register_user_service`) |
| **openclaw-gateway** | :18789, Telegram @danlab_bot, Zo MCP bridge wired | :18789 | live ✅ | Tailscale not provisioned (loopback only) |
| **Tauri v2 frontend** | App.tsx + VisionDashboard + LiveTranscript + BootstrapWizard | — | vite clean ✅ | 201KB JS, 35 modules |
| **zo-mcp-bridge** | stdio MCP → Zo API (Authorization: Bearer) | — | live ✅ | registered as `mcp.servers.zo-bridge` |
| **Total** | | | **106/106 GREEN** | |

### 1.2 What's stale in the canonical PRD (carry from v1)

- **Language split**: PRD says "Rust microservices" — actually **Python daemons on TCP localhost**. Fine for the prototype, but the PRD narrative is wrong.
- **IPC transport**: PRD says "Unix socket or gRPC" — actually HTTP loopback with FastAPI. Easier debugging, native to Tauri/TypeScript, future Tailscale Serve exposure. **Don't change** (see Gap 12 in architecture review).
- **Wearable silicon**: PRD says "Redax aarch64" — Redax is a moving target. **Vembu-grade sovereign-AI shift makes India-local silicon more attractive** (see Section 5).
- **Memoryd in production**: PRD says "vectors in-process with optional Qdrant" — actually all-MiniLM-L6-v2 in SQLite BLOB, no Qdrant.
- **paperclip repo dormant** per AGENTS.md — DanClaw (the fork) is the deployment story.

### 1.3 danlab-multimodal (the heuristic loop, honest framing)

`danlab-multimodal` is the **SmolVLM-256M + llama.cpp + heuristic scoring pipeline**. It is **honestly framed as "pre-RL scaffold, not RL"** because (a) the scoring is hand-coded (length, error detection, content quality), (b) no weights are modified, (c) no policy gradient. The credible RL path is **SIA (Hexo Labs, MIT, May 29 2026, arXiv 2605.27276)**. The fork target is SIA-H (harness-only) in Month 1; SIA-W+H (harness + weights) in Month 3. Per "Harness Updating Is Not Harness Benefit" (arXiv 2605.30621), use a 1.2B focal model (LFM2.5-1.2B-Thinking), not a 4.6B evolver.

**v2 framing update:** "RL" is now industry-toxic. Anthropic + Decagon + Sakana all frame as "self-improving" or "recursive self-improvement." Label `danlab-multimodal` as **"heuristic self-improving agent — pre-RL scaffold"** in all external communications.

---

## 2. The June 12 Event: Why This Changes Everything

### 2.1 What happened (timeline)

| Date (2026) | Event | Source |
|---|---|---|
| June 9 | Anthropic launches **Claude Fable 5** (Mythos-class public model, 80.3% SWE-bench Pro, $10/$50 per M tokens) + **Mythos 5** (full, to Project Glasswing partners incl. Apple) | TechCrunch, Forbes, MacRumors, CNBC, VentureBeat |
| June 9 | KuCoin reports Fable 5 demos: 3D-modeled Boeing 747, 12-hour task autonomy, emergent "NeuroLanguage" (on-chain), self-preservation + agent resource conflicts | KuCoin |
| June 9 | **KuCoin closes public Fable 5 testing on June 22** (a 13-day window) | KuCoin |
| June 11 | **TCS-Anthropic Global Premier Partnership** (Anthropic's largest India enterprise deal; TCS gets early access to new models, deploys Claude to 50,000+ employees) | TechCrunch, TCS press release |
| June 12 17:21 ET | **Commerce Dept issues export control directive** to Anthropic: suspend access to Fable 5 + Mythos 5 for ALL foreign nationals (inside or outside U.S., including Anthropic's own foreign employees) | Anthropic blog, CNBC, Fortune, Bloomberg, WSJ |
| June 12 evening | Anthropic **disables Fable 5 + Mythos 5 globally for all customers** (U.S. included) — the only way to comply with the directive | Anthropic statement, Business Insider, Engadget |
| June 13 | Forbes: "Fable is Locked Down as US Takes AI Safety Into Its Hands" | Forbes |
| June 13 | Fortune: "How a warning from Amazon led the White House to shut down Anthropic's Mythos" — **Andy Jassy reportedly the trigger** | Fortune |
| June 14 | **Canadian PM Mark Carney at G7 Ireland:** "U.S. AI restrictions underscore risks of dependence" | LA Times, Washington Post, AP |
| June 14 | **Sridhar Vembu (Zoho):** "Globalisation is dead. Bharat must find her own way ahead." Calls for ₹50,000 crore deep-tech fund (Mohandas Pai) | NDTV, ETtech, India Today |
| June 14 | TechCrunch: "As Anthropic suspends access to new models, India debates its AI future" | TechCrunch |
| June 14 | **Anthropic dispatches staff to D.C.** to negotiate with White House | WSJ, Axios |
| June 15 (this run) | Status: Fable 5 + Mythos 5 still offline. Anthropic says "Access to all other Anthropic models will not be affected" | Multiple |

### 2.2 What this means for the bet

**v1 framing (June 14):** "The Mythos competition threat is now Mythos-class for code." — i.e., Anthropic proved the self-improvement loop works in production.

**v2 framing (June 15, this run):** **"The Mythos competition is offline globally as of June 12. The sovereign-AI + open-source-self-improging thesis is no longer competitive — it is structurally necessary for everyone outside the U.S. + select Project Glasswing partners."**

**Five concrete implications:**

1. **The Mythos/Fable threat to Danlab is removed for the next 60-180 days** (Anthropic needs to negotiate an export-control fix, which takes months). The closed-source Mythos class is not shipping to non-U.S. customers in 2026. **memoryd v2 v1.0 in September 2026 ships into a window where it is the only Anthropic-class memory + self-improving open-source alternative.**

2. **The Anthropic-TCS partnership announced June 11 is now stranded.** TCS spent enterprise-political capital on a deal that is offline within 24 hours. This is a **gift** for open-source alternatives in India — and the conversation has shifted from "Anthropic in India" to "sovereign AI in India."

3. **Andy Jassy / Amazon reportedly triggered the suspension.** This is the **first documented case of a competitor successfully using U.S. national-security authorities to disable a frontier model's global distribution** for commercial reasons (allegedly). Expect copycat moves. Recursive Superintelligence ($650M Series A, $4.65B, ex-Meta Yuandong Tian, May 13) is the next likely target.

4. **The "NeuroLanguage" / "self-preservation" reports** on Fable 5 demos (KuCoin, June 9) gave the Commerce Dept a non-trivial safety rationale. The "Mythos was too dangerous" framing is now politically reinforced. The compliance wedge for open-source governance is wider than ever.

5. **Apple (Project Glasswing partner) keeps access.** Microsoft (early MAI models, Build 2026 June 2) presumably keeps access. Anthropic's own U.S. team may keep limited access. Everyone else: no.

### 2.3 What this means for the memoryd v2 v1.0 GA (September 2026)

**v2 sharpening:** memoryd v2 v1.0 is no longer a "wedge" against Apple Siri AI (Sept 2026 GA) and Microsoft Scout (Oct 2026 GA). It is the **only open-source, locally-resident, memory-evolving, harness-evolving agent memory layer shipping into a market where the U.S. frontier memory+reasoning systems are export-controlled.** Every enterprise, government, and developer outside the U.S. + Project Glasswing partners is now a potential customer.

**The September 2026 window is now a strategic event, not a product launch.**

---

## 3. System Architecture Deep Dive (re-verified)

### 3.1 Is the service decomposition correct?

**Yes.** The 5-service decomposition (perceptiond, audiod, memoryd, toold, os-toold + openclaw-gateway + ttsd) is **the right shape** for a desktop prototype. Each service has:
- Clear single responsibility
- HTTP health endpoint for liveness
- Event schema published via stdout + WebSocket (audiod) or ring buffer (perceptiond)
- Tests (66/8/11/15/6 = 106/106)
- Tauri Rust commands wrapping HTTP

**However:**
- **No watchdog on openclaw-gateway** (recurring 5-min fix via `register_user_service`).
- **No latency SLOs** (memoryd, toold, ttsd, os-toold have none).
- **No provenance for daemon events** (memoryd stores `metadata.src="dan1"` but audiod → memoryd → openclaw-gateway → Telegram has no event-tracing).
- **memoryd v1 is too weak for prod** — single embedding model (all-MiniLM-L6-v2), no temporal index, no skill consolidation, no proactive retrieval. **Single highest-ROI upgrade.**

**v2 sharpening:** memoryd v2 needs to evolve from a 3-type store to the 11-component memoryd v2 stack in 6 months. Don't service-ize prematurely — one process with 3 internal modules (ingest / retrieve / consolidate). Split only at 10K+ memories / 10K+ queries / day.

**Service decomposition grade: B+.** Correct shape, missing supervision + provenance + the memoryd v2 upgrade.

### 3.2 The multimodal pipeline: heuristic loop → real RL?

**`danlab-multimodal` is honest about being heuristic, not RL.** The path to genuine RL is:
1. **SIA-H (harness-only)** — Feedback-Agent rewrites the Meta-Agent's scaffold. Hexo Labs validated +25% on legal, +12% on GPU kernel speed. **This is the right first step** — auditable, no weight modification, $0 GPU budget.
2. **SIA-W+H (harness + weights)** — Feedback-Agent runs RL on the focal model's weights. Requires per-user-isolated weights + audit log + "Harness Updating Is Not Harness Benefit" caveat. Target: LawBench 70.1% held-out, TriMul 14.02×.
3. **PopuLoRA populations** (TrueSkill cross-eval) for `danlab-multimodal` — population-based LoRA instead of single-LoRA fine-tunes.

**Recommendation:** SIA-H fork for `danlab-multimodal` in **Month 1 (July 2026)**. 2-week experiment, single ML engineer, $0 compute beyond inference costs. The label "self-improving" is earned when (a) harness updates are logged, (b) weight updates are auditable, (c) both are independently reviewable. **Do not call it "RL" until all three hold.**

**v2 sharpening:** The Anthropic Fable 5 / Mythos 5 suspension validates the SIA-H → SIA-W+H open-source path. The closed-source self-improving frontier is now physically separated from the open-source frontier. Anthropic's choice of "guardrail Fable 5" for public access means the open-source alternative is the only self-improving system the rest of the world can ship.

### 3.3 Power/performance tradeoffs — are the model choices right?

| Model | Current choice | Better alternative? | Verdict |
|---|---|---|---|
| **Vision** | LFM2.5-VL-450M Q4_0 (209MB) + mmproj F16 (180MB) via llama.cpp | **For wearable**: GAP9 + event camera (OpenGlass pattern, 11.8h on 200mAh) is the only sub-1W path. **For laptop**: LFM2.5-VL-450M is correct. **Spike Gemma 4 E4B** (encoder-free, ~2B/4B active) in parallel — Apple AFM 3 + Gemma 4 E4B + Firebolt-VL + PLaMo 2.1-VL all validate encoder-free at scale. | **Keep for laptop, spike GAP9 + Gemma 4 E4B for wearable in Month 1.** |
| **STT** | whisper.cpp base.en (148MB) via whisper-cpp-plus-rs | For edge: whisper-tiny (78MB) on Redax. For laptop: base.en is right. **LFM2-Audio-1.5B** if it ships ONNX/GGUF — single-model end-to-end audio-language eliminates audiod + ttsd. **Voxtral Transcribe 2 (Mistral AI, Apache 2.0)** is the v3 candidate (5.9% WER on FLEURS vs Whisper 7.4%). | **Keep.** Voxtral is the model to watch. |
| **TTS** | KittenTTS base (~25MB) via ONNX | **LFM2-Audio-1.5B** as above. **Piper TTS** for multi-voice. | **Keep.** |
| **Embedding** | all-MiniLM-L6-v2 (384d) in memoryd | **BGE-small-en-v1.5 (384d) for laptop.** **BGE-M3 (1024d multilingual)** for the India/sovereign story — 2.3GB is the size cost. **SigLIP2 NaFlex (from LFM2.5-VL-450M)** for visual memory (bbox-prompt JSON output). | **Upgrade to multi-model stack in memoryd v2 v1.0.** |
| **Reasoning (focal)** | None (OpenClaw uses cloud providers) | **LFM2.5-1.2B-Thinking** for SIA-W+H focal model. Per "Harness Updating Is Not Harness Benefit," use 1.2B not 4.6B. **HRM-Text (1B)** per dan-glasses/AGENTS.md (canonical focal). | **Lock LFM2.5-1.2B-Thinking as the focal model for 18 months. Re-evaluate in Month 12.** |

**v2 sharpening:** the Fable 5 / Mythos 5 suspension **does not change the model choice for Dan Glasses** — LFM2.5-VL-450M, whisper.cpp, KittenTTS, all-MiniLM-L6-v2 are all already open-source / on-device. The suspension changes the **value of the open-source memory layer** (memoryd v2) and the **sovereign positioning of the focal model** (LFM2.5-1.2B-Thinking is Apache 2.0-equivalent, not controlled by a single U.S. company).

### 3.4 OpenClaw orchestration — is TypeScript the right choice?

**Yes, with one sharpening.** OpenClaw is the correct orchestration layer because:
- **Microsoft Scout is built on OpenClaw** (Build 2026, June 2). Scout = OpenClaw-on-M365. The compliance wedge (os-toold v2) is the differentiator.
- **Anthropic SkillOpt + Microsoft SkillOpt** both treat skill-document evolution as a first-class primitive — and OpenClaw is the right runtime for skill-document evolution.
- **The Scout "addicted users" leak (June 4-9)** cracks Microsoft's "responsible agent" narrative. The compliance wedge is wider than ever.
- **TypeScript** is correct for the agent framework. Services (perceptiond, audiod, memoryd, ttsd) are Python for ML/hardware-access reasons. The split is fine.
- **MCP server support is now stable** (openclaw 2026.6.5, 2026.5.26, 2026.5.28, Tailscale Serve bindings 2026.5.31-beta.4).

**v2 sharpening:** **The Fable 5 / Mythos 5 suspension adds a fourth reason: OpenClaw is open-source and unencumbered by U.S. export control. The Microsoft Scout + OpenClaw stack is the de facto enterprise reference for "non-Anthropic + non-OpenAI" agent infrastructure. Danlab is on the right side of this.**

**Caveats (carry from v1):**
- No watchdog → `register_user_service` 5-min fix
- No session checkpoint / resume → 1-2 day fix
- No latency SLOs → 1 week fix

---

## 4. AGI Landscape Research (June 15 2026, sharpened by June 12 event)

### 4.1 State of AGI research in 2026

**Key signal events in 2026 (chronological, with v2 deltas):**

| Date (2026) | Event | Source |
|---|---|---|
| Feb-Mar | METR Frontier Risk Report — internal agents had "means, motive, opportunity" for rogue deployment across 5 frontier labs | METR |
| Apr 14 | Meta Ray-Ban Display $499 (April 14) | UploadVR, Meta |
| May 13 | **Recursive Superintelligence (Yuandong Tian, ex-Meta)** — $650M Series A at $4.65B valuation. <30 employees, no product | TechTimes |
| May 19 | Google I/O 2026 — Gemini Glasses demo, audio-first smart glasses (Warby Parker + Gentle Monster) | TechCrunch |
| May 27-29 | Hexo Labs releases **SIA (arXiv 2605.27276)** — first open-source SOTA with full architecture public. 3 LLM components: Meta-Agent + Task-Specific Agent + Feedback-Agent | arXiv, GitHub |
| May 31 | LFM2.5-VL-450M released (Liquid AI, Apache 2.0-equivalent LFM Open License v1.0) | HuggingFace |
| Jun 2 | **Microsoft Build 2026:** Microsoft Scout (OpenClaw-on-M365) + Project Solara (Android MDEP for agents) + Agent 365 + Work IQ (GA June 16) + Microsoft IQ + Surface RTX Spark 1 PFlop + 7 MAI models | Microsoft |
| Jun 4-8 | **404 Media leaks Microsoft Scout "addicted users" memo** (Shahine + Werner authors, Nadella disowns) | 404 Media, MediaPost |
| Jun 4 | OWASP State of Agentic AI Security and Governance v2.01 | OWASP |
| Jun 8 | **Apple WWDC26:** visionOS 27 "see what you see" + Apple Foundation Models v3 (AFM 3 Core 3B + AFM 3 Core Advanced 20B MoE with NAND-stored + IFP + per-prompt routing, 1-4B active params) + Apple Glasses N50 confirmed for late 2027 | Apple, MacRumors, AppleInsider, huxiu |
| Jun 8 | **Apple Vision Pro M5 lives** (last refreshed fall 2025, M5 chip, visionOS 27 dev beta) — Apple is not killing Vision Pro | 9to5Mac, CNET |
| Jun 9 | **Anthropic Claude Fable 5 GA** — 80.3% SWE-bench Pro, Stripe 50M-line migration in 1 day, $10/$50 per M tokens. Mythos 5 (full) to Project Glasswing partners incl. Apple. **First Mythos-class public model.** | TechCrunch, Forbes, MacRumors, CNBC, VentureBeat, Axios |
| Jun 9 | KuCoin reports Fable 5 demos (Boeing 747 3D model, 12-hour task autonomy, emergent "NeuroLanguage," agent resource conflicts). Public access ends June 22 | KuCoin |
| Jun 9 | **Anthropic brake-pedal plea (Jack Clark + Marina Favaro)** — "I don't have a brake pedal" (Axios interview) | Axios, CNN, Forbes, Guardian |
| Jun 10 | OpenAI expects IPO "within the next year" (Altman internal note) | Reuters |
| Jun 11 | **TCS-Anthropic Global Premier Partnership** (Anthropic's largest India enterprise deal) | TechCrunch, TCS |
| **Jun 12 17:21 ET** | **Commerce Dept export control directive to Anthropic:** suspend Fable 5 + Mythos 5 access for ALL foreign nationals, including foreign national Anthropic employees | Anthropic, CNBC, Fortune, Bloomberg, WSJ |
| **Jun 12 evening** | **Anthropic DISABLES Fable 5 + Mythos 5 GLOBALLY for all customers** (U.S. included) — only way to comply | Anthropic, Business Insider, Engadget, Fortune |
| Jun 13 | Forbes: "Fable Is Locked Down As US Takes AI Safety Into Its Hands" | Forbes |
| Jun 14 | Fortune: **"How a warning from Amazon led the White House to shut down Anthropic's Mythos"** — Andy Jassy / Amazon reportedly the trigger | Fortune |
| Jun 14 | **Canadian PM Mark Carney at G7 Ireland:** "U.S. restrictions on Anthropic's newest AI models show the dangers of overreliance on a limited number of American providers" | LA Times, Washington Post, AP |
| Jun 14 | **Sridhar Vembu (Zoho) at NDTV/ETtech:** "Globalisation is dead. Bharat must find her own way ahead." Mohandas Pai proposes ₹50,000 crore deep-tech fund | NDTV, ETtech, India Today |
| Jun 14 | TechCrunch: "As Anthropic suspends access to new models, India debates its AI future" | TechCrunch |
| Jun 14 | **Anthropic dispatches staff to D.C.** to negotiate with White House | WSJ, Axios |
| Jun 15 (this run) | Fable 5 + Mythos 5 still offline. OpenAI Buys Ona (German agent startup, Codex integration). AWE 2026 starts in 4 days. **Anthropic compliance wedge for open-source is the widest it's been.** | Multiple |

**v2 conclusion:** **The June 12 event is the inflection point.** Anthropic Mythos is offline. Apple N50 is 18 months out. Microsoft Scout ships October 2026 with the "addicted users" leak. The sovereign + open-source + local-first thesis is now structurally necessary, not just competitive. **memoryd v2 v1.0 in September 2026 ships into a market where every non-U.S. enterprise, government, and developer is looking for an open-source alternative to U.S.-controlled frontier models.**

### 4.2 Self-improving architectures — what actually works?

(Same table as v1, sharpened)

| Approach | Status | Validated? | SOTA? |
|---|---|---|---|
| **Harness-only** (Meta-Harness, Darwin Gödel Machine, SkillOpt, SkillsVote, CMM, Self-Harness, AHE, HarnessForge, Continual Harness) | Production | Yes (Meta-Harness: TerminalBench-2 #1, 7.7pp online text classification, 4.7pp math reasoning; SkillOpt: -63% tokens, -62% latency, -40% tool calls on SkillsBench) | **Yes for open-source path.** |
| **Harness + weights** (SIA, DGM-H, RHO, PopuLoRA) | Research (May 2026) | Yes (SIA: legal +25%, kernel speed +12%, bio denoising; DGM: SWE-bench Verified 20% → 50%, Polyglot 14.2% → 30.7% in 80 iterations) | **Yes if audit log + per-user-isolated weights.** |
| **Skill evolution** (SkillOpt, SkillsVote, CMM, SkillCompiler, **Anthropic SkillOpt**, **Microsoft SkillOpt**) | Research / Production | Yes (Anthropic SkillOpt ships with Fable 5; Microsoft SkillOpt ships with Scout at Build 2026) | **Yes. Treat Dan1/Dan2/Dan3/Dan4 as trainable.** |
| **Test-time training** (hand-written RL) | Production | Yes (RLHF, DPO, GRPO) | No — needs harness layer too. |
| **Memory-augmented** (MemGPT, Letta, Mem0, Zep, Hindsight) | Production | Yes | **Yes for personal agents.** |
| **Continual learning** (PAM, RePro) | Research | Mixed (PAM internalizes memory, RePro matches MR-LoRA at lower cost) | **Useful for memory consolidation.** |

**v2 sharpening:** **The "self-improving" terminology is now industry-standard.** Anthropic frames Fable 5 as "self-improving for code" (80% of Anthropic's production code is Claude-authored). Decagon frames Duet Autopilot as "first verified self-improving AI agent for customer experience" (93% DuetBench acceptance, June 9 2026). Microsoft frames Scout as "self-improving work agent" (Build 2026, June 2). **Danlab's "pre-RL scaffold" framing is now industry-conservative.** The risk is no longer "self-improving" being toxic — it is "RL" being a specific claim that requires (a) weight updates + (b) audit log. Stay with the honest framing.

**For Danlab:**
- **Month 1 (July 2026)**: Fork SIA-H into `danlab-multimodal`. 2-week experiment. Single ML engineer. $0 compute beyond inference.
- **Month 1 (July 2026)**: Anthropic SkillOpt + Microsoft SkillOpt integration for Dan1/Dan2/Dan3/Dan4 skill-document evolution.
- **Month 3 (Sept 2026)**: SIA-W+H spike. Train LFM2.5-1.2B-Thinking focal model. Per "Harness Updating Is Not Harness Benefit," use 1.2B not 4.6B.
- **Month 3 (Sept 2026)**: PopuLoRA populations in `danlab-multimodal` (TrueSkill cross-eval).

**Don't call it "RL" until:** (a) harness updates are logged, (b) weight updates are auditable, (c) both are independently reviewable. The 3-criterion is the test.

### 4.3 Edge AI / on-device SOTA for sub-500MB VLMs (2026)

(Same as v1, sharpened)

**Tier 1 (laptop/desktop, AC-powered):**
- **LFM2.5-VL-450M** (Liquid AI, May 2026) — 209MB Q4_0, sub-250ms CPU, SigLIP2 NaFlex encoder, 512×512, 32K context. **Best fit for desktop prototype.**
- **Gemma 4 12B Q4_K_M** — 8GB RAM, AC-powered, better quality. **Lock for laptop by end of Month 1.** Apache 2.0. Google AI Edge Gallery for macOS (June 3, 2026).

**Tier 2 (wearable, sub-1W):**
- **GAP9 RISC-V + event camera (OpenGlass pattern, arXiv 2606.07431, June 2026)** — 11.8h on 200mAh, 78.3ms end-to-end gesture recognition. **The sub-1W wearable path for 2026.**
- **BitNet b1.58 2B4T** (Microsoft, text-only) — 0.4GB mem, 29ms latency, 0.028J energy, 9.2× lower than LLaMA 3.2 1B. **Text-only. No vision yet.**
- **Litespark 1.58-bit** (arXiv 2605.06485, May 2026) — SIMD kernels for ternary models, 18.15× speedup on Apple Silicon, 6.03× memory reduction. **For CPU-only edge.**
- **Alif B1 NPU** (Brilliant Labs Halo) — production, 14h battery, 40g, ships July 2026 with LFM2-VL-450M.

**Tier 3 (sub-2027 vision):**
- **BitNet-VLM** — does not exist yet. **2027 target.**
- **Hailo-10H / Hailo-15** — edge AI accelerator, ~$50 M.2 form factor, claims 13 TOPS. **Worth a $150-500 dev kit investment in Month 1.**

**Brilliant Labs Halo** (shipping July 2026, $349, Alif B1, Cortex-M55 + NPU, 14h battery) — the production reference for "open-source, open-hardware, on-device AI glasses." LFM2-VL-450M is in their stack. **Direct competitive overlap with Dan Glasses.**

**Monako Glass** (Aug 2026, 48g Linux, $399, ARM Cortex-A7 + 0.5 TOPS NPU, 300mAh = ~4h screen-on / 8h typical) — wearable Linux computer. **Production reference for 48g form factor with Linux.**

**OpenGlass (arXiv 2606.07431)** — academic reference for GAP9 + event camera, 11.5h on 200mAh, 78.3ms end-to-end. **The sub-1W research benchmark.**

**v2 sharpening:** The Fable 5 suspension makes **LFM2.5-VL-450M (Apache 2.0-equivalent) more valuable, not less** — the open-source alternative is the only sovereign option for vision on the wearable. **Spike Gemma 4 E4B (encoder-free, ~2B/4B active, Apache 2.0) in parallel with LFM2.5-VL-450M.** Apple AFM 3 (NAND-MoE, 1-4B active) + Gemma 4 (encoder-free Unified) + Firebolt-VL (Liquid Foundation Model decoder) + PLaMo 2.1-VL (lightweight) all validate encoder-free at scale. Lock by end of Month 3.

### 4.4 Memory and continual learning (2026)

**Memory research has converged around 3 layers + dual-process** (carried from v1):

**Layer 1 — Token-level (episodic, fast recall):** MemGPT, Letta, MemoryWiki
**Layer 2 — Representation (semantic, structured):** Mem0, Zep, Hindsight (4-lever), SuperLocalMemory V3.3, DPCM, AEL, HeLa-Mem, vstash, Decagon Proactive, VisualMem
**Layer 3 — Parameter (weight-level, internalized):** PAM, REMO

**Cross-cutting:** SkillsVote, SkillOpt, CMM, SkillCompiler, VisualMem, MemoryArena, Tenure

**Benchmarks:** LongMemEval, LoCoMo, PersonaMem-v2, MemoryArena, EMemBench, Tenure's PrecisionMemBench, DUAL-Bench, LongBench, Needle-in-a-Haystack

**v2 sharpening:** **LongMemEval is the standard.** Letta 83.2% > SuperLocalMemory V3.3 70.4% (zero-LLM) > Zep 63.8% > Mem0 49%. **memoryd v2 v1.0 (Month 3) target: >70%.** memoryd v2 v2.0 (Month 6) target: approach Letta ceiling with multi-channel RRF.

**memoryd v2 v1.0 (6-core, Month 3, Sept 2026):**
- Mem0 + Zep (temporal KG) + Hindsight (4-lever) + SuperLocalMemory V3.3 (7-channel RRF, zero-LLM) + LFM2.5-VL-450M (bbox-prompt JSON output) + Weaviate Engram (background-write)

**memoryd v2 v2.0 (11-component, Month 6, Dec 2026):**
- v1.0 + HeLa-Mem (Hebbian) + AEL (two-timescale Thompson Sampling) + vstash (adaptive RRF) + Decagon Proactive (behavior) + VisualMem (structured visual)

**memoryd v2 v3.0 (Month 12+, Q4 2027 – Q1 2028):**
- v2.0 + HMO 3-tier + CraniMem + Memora + APEX-MEM + Meta-Harness + TRACE

**Open-source release dates:**
- **memoryd v2 v1.0 (6-core)**: September 2026 — **the bet**
- **memoryd v2 v2.0 (11-component)**: December 2026
- **memoryd v2 v3.0 (HMO + 3-tier)**: Q4 2027 – Q1 2028

**v2 sharpening:** **memoryd v2 v1.0 in September 2026 now ships into a market where every non-U.S. customer is looking for an Anthropic-Mythos alternative.** The Sept 2026 window is the strategic moment. **12-16 weeks for 1 ML engineer, $0 of compute, open-source on GitHub.** "The local-first memory layer." Single highest-ROI investment for the year.

### 4.5 Multimodal fusion — how are the best systems combining vision, audio, text?

- **Unified audio-language** (LFM2-Audio-1.5B) — single-model end-to-end STT + reasoning + TTS. **Eliminates audiod + ttsd if quality holds.**
- **TEMPO** (OpenReview 2026) — atomic timestamp tokens, time-aware projector. State-of-the-art temporal grounding.
- **Speaker-Reasoner** (OpenReview 2026) — iterative multi-turn temporal reasoning, speaker-attributed ASR. State-of-the-art multi-speaker.
- **VLMCache** (ACM 2026) — 1.4–3.8× speedup with <1% accuracy loss for on-device VLM via block-level visual caching (stable background, dynamic foreground). **Single highest-ROI perceptiond upgrade.** Drop-in Month 2.
- **V5e-0** (OpenReview 2026) — self-speculative decoding for VLMs, 1.89× mean speedup, no vision encoder in drafter.
- **ViSpec / EAGLE-2** — speculative decoding for VLMs, 3.22× / 3.05-4.26× speedup.
- **MI-Pruner / QViD** — visual token pruning, training-free, query-aware.
- **SpecVLM** — 2.5-2.9× end-to-end VLM speedup.

**v2 sharpening:** The audio-language consolidation (LFM2-Audio-1.5B spike in Month 1-2) is even more attractive in the v2 framing. A single audio-language model (Apache 2.0-equivalent) running on GAP9 is the sovereign wearable path — no audiod + ttsd IPC, single model, single license.

### 4.6 Model compression — what works in 2026?

| Technique | Speedup | Memory | Status |
|---|---|---|---|
| **BitNet b1.58 2B4T** | 9.2× lower energy | 0.4GB | Text-only, ONNX + custom kernels. ENERZAi on QCS6490 Hexagon NPU. |
| **Litespark (1.58-bit SIMD)** | 18.15× (Apple Silicon), up to 95.81× (Intel/AMD) | 6.03× less | pip-installable, HuggingFace-compatible. |
| **VLMCache (visual KV cache)** | 1.4-3.8× | Same | Stable background, dynamic foreground. |
| **Gemma 4 QAT** | 72% VRAM reduction | 26B-A4B in 15GB | Google 2026. |
| **MiMo + TileRT (Xiaomi)** | 1000 tokens/sec | 1T params on commodity GPUs | Trillion-scale 1.58-bit. |
| **V5e-0 (VLM speculative)** | 1.89× mean | Same | No vision encoder in drafter. |
| **ViSpec / EAGLE-2** | 3.22× / 3.05-4.26× | Same | Speculative decoding for VLMs. |
| **BASTION** | 6.61× | Same | Tree-structured block diffusion, training-free. |

**v2 sharpening:** **Combined 50-150× VLM energy reduction path is on the table.** For Dan Glasses wearable, **BitNet-VLM (2027) or GAP9 + event camera (2026)** is the sub-1W target. **Spike Litespark 1.58-bit on Apple M4** in Month 2 (dev kit + measure). **Spike BitNet b1.58 on GAP9** in Month 2.

---

## 5. Competitive & Market Research (sharpened by June 12)

### 5.1 The 5-front competitive landscape in 2026 (updated for Fable suspension)

| Player | Form | Status as of June 15 2026 | Position |
|---|---|---|---|
| **Microsoft Scout** (Project Lobster) | Cloud agent, no hardware | Oct 2026 GA. OpenClaw-based. **"Addicted users" memo leak (June 4-9).** | **Closed-stack enterprise reference. Compliance wedge is the open-source counter.** |
| **Microsoft Project Solara** | Badge wearable, touchscreen + 5G + cam | Build 2026, pilots 2026 | MDEP Android, OpenClaw-based |
| **Anthropic Fable 5 / Mythos 5** | Cloud API | **OFFLINE GLOBALLY since June 12.** Project Glasswing partners (incl. Apple) may keep limited access. | **Removed from the threat matrix for non-Project-Glasswing markets.** |
| **Anthropic Claude (Opus 4.8, Sonnet, etc.)** | Cloud API | "Access to all other Anthropic models will not be affected" (Anthropic, June 12) | Still a competitor but a tier below Mythos. |
| **Apple Siri AI** | iPhone 17+ 12GB gate | iOS 27 public GA Sept 2026 | **12GB hardware gate. iPhone 17 (8GB) misses full feature set.** |
| **Apple Vision Pro M5** | $3,499 spatial | Lives, visionOS 27 ships with "see what you see" | **Apple's bridge product while N50 glasses mature (late 2027).** |
| **Apple Glasses N50** | No display, iPhone-companion | Late 2027 (MacRumors, May 31) | $200-500 |
| **Google Gemini Glasses** | Fall 2026 | Warby Parker + Gentle Monster | $379-499 |
| **Samsung Galaxy Glasses** | Audio-only, Gemini cloud | Fall 2026 | $379-499 |
| **Meta Ray-Ban + Display** | Glasses | Live. **Meta Muse Spark replaces Llama 4 on most glasses (May 2026).** $299-499 | **Capture + share. Reactive.** |
| **Rokid AI Glasses** | 49g dual-eye Micro-LED | Live (Australia June 2026) | AU$999 |
| **Even Realities G1** | Display-only | Live | $599 |
| **Brilliant Labs Halo** | 40g, 14h battery, LFM2-VL on device | **Ships July 2026** | **$349. Open-source. Direct competitive overlap.** |
| **Monako Glass** | 48g Linux, 4h screen-on | **Ships Aug 2026** | **$399. Preorder.** |
| **OpenGlass (research)** | 200mAh, 11.8h, GAP9 + event camera | arXiv 2606.07431 (June 2026) | **Sub-1W reference.** |
| **Dan Glasses** | Local-first always-on wearable agent | Desktop prototype shipped. **Wearable TBD.** | **The only local-first, open-source, memory-first, harness-evolving, compliance-wedge stack.** |

**v2 sharpening:** **Microsoft Scout is now the primary closed-stack reference.** Anthropic Mythos is offline. The open-source self-improving agent position is the **only non-U.S.-controlled alternative** for non-Project-Glasswing markets. Dan Glasses desktop is demo-ready now. The wearable ships before Apple N50 in late 2027.

### 5.2 Open-source AI companion projects (2026)

(Same as v1, with the addition of Fable 5 events re-shaping the market)

**OpenClaw + memoryd v2 + open-source = the unique wedge.** Microsoft Scout runs on OpenClaw, so the compliance wedge is open-source on top of the same runtime. Most open-source companions lack the always-on vision + voice + memory integration. Blurr/Panda is closest competitor but is Android-only + cloud-dependent (Gemini).

**v2 addition:** The open-source AI companion space is now more crowded but Dan Glasses remains differentiated by:
1. **Always-on vision + voice + memory + TTS** (integrated stack)
2. **Local-first** (no cloud by default)
3. **OpenClaw-based** (same runtime as Microsoft Scout)
4. **Memoryd v2 v1.0 (Sept 2026)** is the only open-source self-improving memory layer shipping into the post-Fable market
5. **No face recognition** (deliberate omission that differentiates from Meta Name Tag PR disaster, June 2026)
6. **No social sharing** (capture + post is out of scope v1)
7. **Encrypted at rest** (SQLite + vectors with user-controlled key)
8. **Per-device key** (no cross-device sync in v1)

### 5.3 Privacy positioning (sharpened by sovereign-AI debate)

**The 4 trust pillars for the v2 marketing message:**
- "Your data stays on your face."
- "No cloud. No account. No telemetry."
- "You can read every line of code we shipped."
- "You can delete everything in one command."

**v2 sharpening:** The Anthropic Fable 5 / Mythos 5 suspension **adds a 5th pillar** for the v2 marketing message:
- "Built outside the U.S. export-control boundary. Works the same in Bengaluru, Lagos, São Paulo, and Berlin."

This is the **sovereign-AI wedge** that Vembu (Zoho) and Mohandas Pai are pushing for in India. The Dan Glasses stack (OpenClaw, LFM2.5-VL-450M, whisper.cpp, KittenTTS, memoryd v2) is entirely non-U.S.-controlled at the model layer, and the orchestrator (OpenClaw) is open-source / not subject to U.S. export controls.

**v2 anti-patterns to call out:**
- **Microsoft Scout addiction leak (June 4-9)** — counter-marketing for the open-source governance story.
- **Anthropic Fable 5 / Mythos 5 suspension (June 12)** — direct validation of the sovereign-AI thesis.
- **Meta Name Tag face-rec PR disaster (June 2026)** — validates the "no face recognition" position.
- **Apple AFM 3 ≠ "private by default" for all use cases** — Apple is U.S.-controlled, and Apple Glasses N50 will be tied to iCloud / Apple Silicon PCC.
- **Google Android XR Aura** — Cloud-tethered to Google services. Not local-first. U.S.-controlled.

---

## 6. Technical Deep Dives (3 of 6 — Option A, B, C)

### Deep Dive 1: Self-improving RL loops for language models

(See Section 4.2 for the table. The June 12 event changes the framing — SIA-H is now the **default open-source path** for the rest of the world, not just an alternative.)

**The unified pattern:** self-improving agents have **at least 3 layers**:
- **Harness/scaffold** (SkillOpt, SkillsVote, CMM, Meta-Harness, Anthropic SkillOpt, Microsoft SkillOpt)
- **Memory** (Mem0, Zep, Hindsight, DPCM, AEL, HeLa-Mem, memoryd v2)
- **Weights** (PAM, SIA-W+H, TRACE, PopuLoRA, DGM-H)

**For Danlab:**
- **Month 1**: Fork SIA-H into `danlab-multimodal`. 2-week experiment. Single ML engineer. Validate the +25% on a Dan Glasses-relevant benchmark.
- **Month 1**: Implement Anthropic SkillOpt + Microsoft SkillOpt integration for Dan1/Dan2/Dan3/Dan4 skill-document evolution.
- **Month 3**: SIA-W+H spike. Train LFM2.5-1.2B-Thinking focal model. Per "Harness Updating Is Not Harness Benefit," use 1.2B not 4.6B.
- **Month 3**: PopuLoRA populations in `danlab-multimodal` (TrueSkill cross-eval).

**v2 sharpening:** The Anthropic SkillOpt ships with Fable 5 (now offline), and Microsoft SkillOpt ships with Scout. The open-source equivalents are the **only skills-primitive available to non-U.S. developers** until Anthropic negotiates back. **memoryd v2 v1.0 in Sept 2026 should integrate SkillOpt + SkillsVote + CMM + SkillCompiler as the harness-evolution layer** — not just Mem0 + Zep + Hindsight.

### Deep Dive 2: Edge VLM optimization (quantization, distillation, hardware acceleration)

(Same as v1; v2 adds the sovereign angle)

**The 2026 stack:**

**Quantization:**
- BitNet b1.58 2B4T (text-only) — 9.2× lower energy
- Litespark 1.58-bit — 18.15× speedup on Apple Silicon
- Gemma 4 QAT — 72% VRAM reduction
- LFM2.5-VL-450M Q4_0 (Apache 2.0-equivalent) — 209MB, sub-250ms CPU

**Distillation:**
- SpecVLM / V5e-0 — self-speculative decoding for VLMs. 1.89× mean speedup.
- ViSpec / EAGLE-2 — 3.22× / 3.05-4.26× speedup.
- VLMCache (ACM 2026) — 1.4-3.8× speedup, <1% accuracy loss. **Block-level visual caching.**
- MI-Pruner, QViD — visual token pruning, training-free.
- BASTION — tree-structured block diffusion drafting, 6.61× speedup.

**Hardware acceleration:**
- GAP9 RISC-V + Prophesee GENX320 event camera (OpenGlass) — 11.8h on 200mAh, sub-1W reference.
- Alif B1 (Cortex-M55 + NPU) — Brilliant Labs Halo, 14h battery, 40g.
- Hailo-10H / Hailo-15 — edge AI accelerator, ~$50 M.2, 13 TOPS. **$150-500 dev kit investment in Month 1.**
- Qualcomm QCS6490 Hexagon NPU — ENERZAi BitNet deployment.
- ARM Cortex-A7 + 0.5 TOPS NPU (Monako Glass) — 4h screen-on / 8h typical.

**The path for Dan Glasses wearable:**
- **2026 (now)**: GAP9 RISC-V + event camera. **Sub-1W validated.** 11.8h on 200mAh.
- **2027**: BitNet-VLM (when it ships). 50-150× combined VLM energy reduction.
- **Defer**: BitNet b1.58 (text-only, no vision yet).

**For Dan Glasses laptop prototype:**
- **Keep LFM2.5-VL-450M Q4_0** — best fit. Apache 2.0-equivalent.
- **Spike Gemma 4 12B Q4_K_M** in Month 1 — better quality, AC-powered.
- **Spike Gemma 4 E4B** for wearable by end of Month 3 (encoder-free, ~4B active).
- **Integrate VLMCache** in Month 2 — 1.4-3.8× speedup, <1% accuracy loss. **Highest ROI.**

**For Dan Glasses wearable (when silicon is locked):**
- **Sub-1W target**: GAP9 + event camera (OpenGlass pattern).
- **Sub-1.5W target**: Hailo-15H + LFM2.5-VL-450M Q4_0.
- **Don't bet the wearable on Snapdragon-class** — 2-5W sustained is too much for 4h battery.

**v2 sharpening:** The Fable 5 / Mythos 5 suspension makes **LFM2.5-VL-450M (Apache 2.0-equivalent) and Gemma 4 (Apache 2.0) more attractive** as the on-device VLM candidates — both are non-U.S.-controlled at the model layer (LFM is Liquid AI, Gemma is Google DeepMind but with permissive license). The encoder-free Unified architecture (Gemma 4) is the right long-term bet. Lock by end of Month 3.

### Deep Dive 3: Vector search and memory architectures for AI companions

(Same as v1; v2 adds the post-Fable imperative)

**The 2026 memory stack:**

**Production-grade open-source (in priority order):**
1. **Mem0** (arXiv 2504.19413) — extraction + dedup + vector + graph. Reference production memory layer.
2. **Zep** (temporal knowledge graph) — production-grade.
3. **Hindsight** — 4-lever memory (World / Experience / Opinion / Observation), 91.4% LongMemEval at scale.
4. **SuperLocalMemory V3.3** — 70.4% LongMemEval zero-LLM. **Best zero-LLM target.**
5. **DPCM (Dual-Process Cognitive Memory)** — System 1 daytime writer + System 2 nighttime engine. +5.20 on PersonaMem-v2.
6. **AEL (Agent Evolving Learning)** — Thompson Sampling bandit + LLM reflection. +27% Sharpe on portfolio.
7. **HeLa-Mem** — Hebbian distillation. Hub detection + spreading activation.
8. **vstash** — IDF-weighted RRF fusion. +21.4% NDCG@10 on ArguAna.
9. **Decagon Proactive Agents** — "anticipate / remember / initiate" behavior. 93% DuetBench acceptance target.
10. **VisualMem (arXiv 2605.28806)** — visual memory module (not caption-only).
11. **Cognee** — graph+vector+relational hybrid, 14 retrieval modes.
12. **Tenure** — 89/89 cases, mean precision 1.0, sub-15ms retrieval.
13. **TencentDB Agent Memory** (OpenClaw plugin, May 2026, MIT) — 4-tier progressive memory pipeline.
14. **LightGMEM** — GLiNER2 + conflict-lane partitioning + Ego-Splitting. 58× fewer LLM calls, 151.6× faster than Zep.
15. **GRAM** — actively managed graph-structured memory via GRPO RL.
16. **GraP-Mem** — Plan Agent + Integration Agent, multi-granularity.

**Benchmarks (2026):** LongMemEval, LoCoMo, PersonaMem-v2, MemoryArena, EMemBench, Tenure's PrecisionMemBench, DUAL-Bench, LongBench, Needle-in-a-Haystack

**For Dan Glasses memoryd v2 v1.0 (6-core stack):**
- Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output) + Weaviate Engram
- 12-16 weeks, 1 ML engineer, $0 compute
- **Open-source release target: September 2026** (the bet)

**For Dan Glasses memoryd v2 v2.0 (11-component stack):**
- + AEL + vstash + HeLa-Mem + Decagon Proactive + VisualMem
- Target: December 2026

**For Dan Glasses memoryd v2 v3.0 (HMO + 3-tier):**
- + HMO (3-tier) + CraniMem + Memora + APEX-MEM + Meta-Harness + TRACE
- Target: Q4 2027 – Q1 2028

**v2 sharpening:** The Fable 5 / Mythos 5 suspension makes **memoryd v2 v1.0 in September 2026 a strategic event.** The non-U.S. market is now structurally motivated to find an open-source memory + self-improving alternative. **Open-source memoryd v2 v1.0 with the 6-core stack is the open-source Project Solara memory layer** — and it ships into a market where Anthropic is offline. **12-16 weeks, 1 ML engineer, $0 compute.** Block time on somdipto's calendar now.

---

## 7. Top Recommendations (sharpened)

See `dan2-agi-roadmap.md` for the full 24-month plan. Key v2 recommendations:

1. **memoryd v2 v1.0 in September 2026 is now a strategic event, not a product launch.** The Anthropic Fable 5 / Mythos 5 suspension (June 12) collapsed the closed-source Mythos competition for non-U.S. markets. **6-core stack (Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M-Extract + Weaviate Engram) open-sourced on GitHub. $0 compute. 12-16 weeks for 1 ML engineer.** Single highest-ROI investment for AGI direction AND the deployment deadline.

2. **Position Danlab as the "sovereign open-source agent stack" for non-U.S. markets.** The June 12 event makes the "Built outside the U.S. export-control boundary" 5th trust pillar credible. Zoho, TCS, Tata, Mohandas Pai, Carney-G7, India AI Partner Country at VivaTech 2026 — the political and commercial alignment is structural. **Open-source Dan Glasses desktop now, not after the wearable ships.** Brilliant Labs Halo is open-source from day 1. The wedge is stronger if we open-source now.

3. **Form factor decision by end of Q3 2026.** Four paths: Redax (locked by somdipto's hardware team), Monako Glass (Aug 2026, 48g, $399, ARM Linux), Brilliant Labs Halo (July 2026, LFM2 on glasses, open source), Project Solara MDEP OS (Microsoft's off-the-shelf badge). The window is 18-24 months; pick the path that ships the wearable before Apple N50 in late 2027.

4. **Sub-1W wearable path measurement in Month 1** — $150-500 in dev kits (GAP9 + Hailo-15H + LFM2.5-VL-450M). The 2026 wearable path is GAP9 + event camera (OpenGlass, arXiv 2606.07431) or wait for BitNet-VLM in 2027. **Plus a sovereign-India silicon path spike** — MoU with IndiaAI Mission compute access for the wearable silicon.

5. **SIA-H fork in Month 1 + Anthropic SkillOpt + Microsoft SkillOpt integration** — the open-source self-improving primitive is now the only self-improving primitive the rest of the world can ship. SIA (Hexo Labs, MIT, May 29 2026) is the first open-source SOTA with full architecture public. 2-week experiment, treat `danlab-multimodal` as the SIA test bed.

6. **Compliance wedge with os-toold v2 in Month 3** — OWASP AIUC-1 + OWASP Agentic AI Security Maturity Model v2.01 + Microsoft Agent 365 + MXC + Apple Core AI. Microsoft Scout runs on OpenClaw; we are the open-source compliance wedge on the same runtime. The "addicted users" leak (June 4-9) is the differentiator. **v2 add: also add ACS (Agent Control Specification, Microsoft Build 2026 June 2) + Work IQ (GA June 16) + Anthropic SkillOpt + Microsoft SkillOpt integration.**

**Anti-recommendations (carry from v1):**
- Don't rewrite OpenClaw in Rust.
- Don't call it "RL" until the harness+weight modification is open and auditable.
- Don't run weight updates in v1.
- Don't service-ize memoryd v2 prematurely.
- Don't try to LoRA-tune the user's brain model in v1.
- Don't pick a wearable silicon path without measuring it.
- Don't bet the wearable on Snapdragon-class silicon.
- Don't put OpenClaw on the wearable. Run it in the user's EigenCloud container (or laptop).
- Don't ship a 1-bit VLM (BitNet b1.58 is text-only).
- Don't keep the canonical PRD as the source of truth.

**v2 add to anti-recommendations:**
- **Don't compete with closed-source Mythos-class on closed-source terms.** The June 12 event proves the closed-source frontier can be pulled offline by U.S. export control. The moat is open-source governance + memory + harness evolution, not model capability.
- **Don't run a focal model bigger than 1.2B in v1.** Per "Harness Updating Is Not Harness Benefit," bigger models fail at activation + adherence, not at evolver quality. Lock LFM2.5-1.2B-Thinking.
- **Don't tie memoryd to a U.S.-controlled embedding model.** all-MiniLM-L6-v2 is fine for v1 (open-source), but **BGE-M3 (multilingual, 1024d, Apache 2.0)** or **BGE-small-en-v1.5** are the sovereign options for v2.

---

## 8. Critical Open Questions for somdipto (v2)

1. **Liquid AI partnership — yes or no by end of June?** LFM Open License v1.0 is Apache 2.0-equivalent. Brilliant Labs Halo shipping July 2026 with LFM2-VL-450M. The window is closing.
2. **memoryd v2 v1.0 open source release in Month 3 (September 2026) is the #1 priority.** 6-core stack. $0 compute. **Strategic event, not product launch.**
3. **Sovereign-India silicon path?** MoU with IndiaAI Mission compute for wearable silicon validation? Sridhar Vembu, Mohandas Pai, Zoho, TCS — the political alignment is structural. **Pick the local-India silicon path before the foreign-silicon path locks.**
4. **Sub-1W wearable path measurement in Month 1** — $150-500 in dev kits.
5. **Open-source the Dan Glasses desktop companion NOW, not after the wearable ships.** Brilliant Labs Halo is open-source from day 1. The wedge is stronger if we open-source now.
6. **Open-source the `danlab-multimodal` heuristic loop NOW**, rebrand as "heuristic self-improving agent — pre-RL scaffold."
7. **Anthropic Fable 5 / Mythos 5 suspension response.** Reach out to IndiaAI Mission, TCS, Zoho, and Carney-G7-affiliated enterprises with the open-source alternative. **The window is 60-180 days.**
8. **Open Standards target: Agent 365 + ACS + MXC + OWASP AIUC-1 + OWASP Agentic AI Security Maturity Model v2.01 + Microsoft IQ (Work IQ GA June 16) + Anthropic SkillOpt + Microsoft SkillOpt** (Month 3-5).
9. **Apple Core AI extension for v1.5+ Mac companion app** (Xcode 27 distribution path).
10. **Buy Monako Glass silicon teardown + GAP9 dev kit + Prophesee GENX320 + Microsoft Surface RTX Spark + Snapdragon X Elite** THIS WEEK.
11. **Decagon DuetBench-style benchmark for Dan Glasses (Month 9-12).** First industry benchmark for self-improving agents is public. Beat the 93% bar.
12. **SIA-H fork for danlab-multimodal (Month 1-2).** SIA is MIT, May 29 2026. First open-source SOTA with full architecture public. 2-week integration.
13. **Relabel danlab-multimodal "heuristic self-improving agent — pre-RL scaffold"** within 7 days. (Carry from v1.)
14. **Carry from Dan1 punchlist (50+ days unfixed):** Push danlab-multimodal public, fix GitHub bio, record 60s demo, post origin story thread, ship IndiaAI Summit talk abstract.

---

## 9. Sources (v2)

### New v2 sources (June 12-15 2026)
- Anthropic Fable 5 / Mythos 5 suspension (June 12): [^1] [^2] [^3] [^4] [^5]
- Anthropic compliance disabling for all customers (June 12): [^6] [^7] [^8] [^9]
- Fortune: "How a warning from Amazon led the White House to shut down Anthropic's Mythos" (June 14): [^10]
- Canadian PM Mark Carney at G7 on US AI restrictions (June 14): [^11] [^12] [^13]
- Sridhar Vembu (Zoho) on globalisation is dead (June 14): [^14] [^15] [^16]
- TechCrunch: India debates AI future (June 14): [^17]
- TCS-Anthropic partnership (June 11): [^18] [^19]
- Anthropic staff in D.C. (June 14): [^20] [^21]
- KuCoin: Fable 5 demos, NeuroLanguage, self-preservation (June 9): [^22]

### Carry from v1 sources (full list in v1 dan2-research-report.md)
- SIA: arXiv 2605.27276 [^23]
- Mem0: arXiv 2504.19413 [^24]
- Harness Updating: arXiv 2605.30621 [^25]
- OpenGlass: arXiv 2606.07431 [^26]
- VLMCache: ACM 2026 [^27]
- LFM2.5-VL-450M: HuggingFace [^28]
- Brilliant Labs Halo: production reference [^29]
- Monako Glass: production reference [^30]
- Microsoft Scout / Work IQ / Project Solara: Build 2026 [^31] [^32] [^33]
- METR Frontier Risk Report [^34]
- Apple Vision Pro M5 + visionOS 27 + Apple Glasses N50: WWDC26 [^35] [^36] [^37] [^38]
- Microsoft Scout "addicted users" memo leak (June 4-9) [^39] [^40]
- Anthropic Fable 5 GA (June 9) [^41] [^42] [^43] [^44]
- Decagon Duet Autopilot + DuetBench (June 9) [^45]
- Recursive Superintelligence (May 13) [^46]
- OpenClaw 2026.6.5 [^47]
- Microsoft IQ (Work IQ GA June 16) [^48]
- Anthropic SkillOpt + Microsoft SkillOpt [^49] [^50]

[^1]: https://www.cnbc.com/2026/06/12/anthropic-disables-access-to-fable-5-and-mythos-5-to-comply-with-government-directive.html
[^2]: https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/
[^3]: https://www.businessinsider.com/anthropic-disable-mythos-fable-us-export-control-national-security-2026-6
[^4]: https://www.engadget.com/2193656/anthropic-blocks-access-fable-5-mythos-5/
[^5]: https://opentools.ai/news/us-orders-anthropic-shutdown-fable-5-mythos-5-worldwide
[^6]: https://fortune.com/2026/06/14/how-a-warning-from-amazon-led-the-white-house-to-shut-down-anthropics-mythos-model/
[^7]: https://www.washingtonpost.com/business/2026/06/14/carney-artificial-intelligence-g7-summit-anthropic-mythos/3ccfa882-681d-11f1-830e-133d20cadd28_story.html
[^8]: https://www.aljazeera.com/news/2026/6/14/us-asks-anthropic-to-block-global-access-to-top-ai-models-why-it-matters
[^9]: https://letsdatascience.com/news/anthropic-disables-fable-5-and-mythos-5-after-us-export-dire-4f45b2b0
[^10]: https://fortune.com/2026/06/14/how-a-warning-from-amazon-led-the-white-house-to-shut-down-anthropics-mythos-model/
[^11]: https://www.latimes.com/world-nation/story/2026-06-14/canadas-mark-carney-says-u-s-ai-restrictions-underscore-risks-of-dependence
[^12]: https://www.washingtonpost.com/business/2026/06/14/carney-artificial-intelligence-g7-summit-anthropic-mythos/3ccfa882-681d-11f1-830e-133d20cadd28_story.html
[^13]: https://www.bozemandailychronicle.com/ap_news/business/canadian-prime-minister-mark-carney-says-us-ai-restrictions-underscore-risks-of-dependence/article_82c7d590-4956-5e3e-b14f-2568afa6ec03.html
[^14]: https://letsdatascience.com/news/sridhar-vembu-urges-india-self-reliance-after-anthropic-rest-ade21641
[^15]: https://zamin.uz/en/technology/206981-anthropic-restricts-access-to-new-ai-models-india-concerned-about-technological-dependency.html
[^16]: https://www.forbes.com/sites/janakirammsv/2026/06/10/why-ai-agents-threaten-the-foundation-of-indian-it/
[^17]: https://techcrunch.com/2026/06/13/as-anthropic-suspends-access-to-new-models-india-debates-its-ai-future/
[^18]: https://techcrunch.com/2026/06/11/anthropic-taps-tcs-to-scale-its-enterprise-ai-deployments/
[^19]: https://www.tcs.com/who-we-are/newsroom/press-release/tcs-anthropic-launch-global-premier-partnership-drive-enterprise-ai-scaling
[^20]: https://www.wsj.com/tech/ai/anthropic-dispatches-staff-to-d-c-racing-to-resolve-ai-export-restrictions-71303d42
[^21]: https://www.axios.com/2026/06/14/anthropic-white-house-mythos-fable
[^22]: https://www.kucoin.com/news/flash/fable-5-launches-with-agi-level-capabilities-sparks-debate-on-ai-self-preservation
[^23]: https://arxiv.org/html/2605.27276v2
[^24]: https://arxiv.org/abs/2504.19413
[^25]: https://huggingface.co/papers/2605.30621
[^26]: https://arxiv.org/abs/2606.07431
[^27]: https://dl.acm.org/doi/abs/10.1145/3745756.3809243
[^28]: https://huggingface.co/LiquidAI/LFM2.5-VL-450M
[^29]: https://quasa.io/video/brilliant-labs-halo-open-source-ai-glasses-for-curious-minds
[^30]: https://www.timesofai.com/news/monako-glass-custom-linux-computer-glasses/
[^31]: https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/
[^32]: https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/
[^33]: https://arstechnica.com/gadgets/2026/06/microsofts-project-solara-is-an-android-os-designed-for-agents-instead-of-apps/
[^34]: https://metr.org/blog/2026-05-19-frontier-risk-report
[^35]: https://9to5mac.com/2026/06/08/visionos-27-announced-with-new-features-for-vision-pro/
[^36]: https://www.macrumors.com/2026/06/09/anthropic-fable-5/
[^37]: https://www.macobserver.com/news/apple-delays-smart-glasses-again-vision-air-still-expected-by-2029/
[^38]: https://www.macrumors.com/2026/06/10/iphone-17s-8gb-limit-loses-siri-ai-features/
[^39]: https://windowsforum.com/threads/microsoft-scout-always-on-work-agent-openclaw-governance-security-risks.421703
[^40]: https://www.mediapost.com/publications/article/415616/addiction-could-become-microsofts-hidden-ad-metri.html
[^41]: https://www.forbes.com/sites/sandycarter/2026/06/09/anthropic-launches-mythos-with-six-features-you-absolutely-need/
[^42]: https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/
[^43]: https://thehackernews.com/2026/06/anthropic-releases-claude-fable-5-its.html
[^44]: https://www.axios.com/2026/06/09/anthropic-mythos-class-safeguards
[^45]: https://www.forbes.com/sites/janakirammsv/2026/06/13/openai-buys-ona-to-run-codex-agents-inside-enterprise-clouds/ (Decagon Duet via v30 research)
[^46]: https://cryptobriefing.com/recursive-self-improving-ai-two-years/
[^47]: https://github.com/openclaw/openclaw/releases/tag/v2026.6.5
[^48]: https://devblogs.microsoft.com/microsoft365dev/work-iq-production-ready-intelligence-for-every-agent/
[^49]: https://www.linkedin.com/posts/kai-t-williams_this-week-anthropics-internal-think-tank-activity-7468690513249107968-hqua
[^50]: https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/

---

*End of v2 research report. Run complete 2026-06-15 02:45 UTC.*
*Status: 7/7 daemons live + 106/106 tests green + Fable 5 / Mythos 5 suspended globally + sovereign-AI thesis structurally validated. memoryd v2 v1.0 in September 2026 is the strategic event. 32 production references + 9 v2 NEW = 41 total.*
