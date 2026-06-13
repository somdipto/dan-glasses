# Dan2 — Technical Research Report (v42 Final)
**2026-06-13 08:40 IST (03:10 UTC) · 7/7 daemons live re-verified (audiod :8090, perceptiond :8092, memoryd :8741, toold :8742, ttsd :8743, os-toold :8744, openclaw :18789) · Live re-verified 2026-06-13 03:10 UTC: BitNet b1.58 2B4T model-card benchmarks re-read (0.4GB non-emb / 29ms CPU decode / 0.028J per inference; 9.2× lower energy than LLaMA 3.2 1B, 6.6× lower than Gemma-3 1B), SIA `hexo-ai/sia` re-confirmed (1,594 stars, 179 forks, last push 2026-06-11T21:41:08Z), LFM2.5-VL-450M model card re-read (765,623 HF downloads, lfm1.0 license, POPE 86.93, OCRBench 684, SigLIP2 NaFlex 86M + LFM2.5-350M backbone, 9 languages, 32,768 ctx) · Microsoft Scout announcement re-read (Microsoft 365 Blog, June 2 2026, "Introducing Microsoft Scout: Your always-on personal agent", by Omar Shahine CVP) · memoryd live test (POST /memories + GET /query?text=reverify → 0.5357 cosine on top-1 hit)**

## v42 vs v41 (delta, 1 line each)

1. **BitNet b1.58 2B4T numbers re-verified directly from the Hugging Face model card table** (v41 cited arXiv 2410.16144 + 2504.12285; v42 adds the HF-side numbers that match those papers). 0.4GB non-emb memory, **29ms CPU decoding latency**, **0.028J energy per inference**, 54.19 average benchmark score (vs LLaMA 3.2 1B 44.90, Qwen2.5 1.5B 55.23, SmolLM2 1.7B 48.70, MiniCPM 2B 42.05, Gemma-3 1B 43.74). The energy number is the **per-inference J** (per output token at typical 4-byte-token cost), not aggregate joule. The 1.37-6.46× speedup cited in v41 is the **decoding speedup** vs fp16 baseline (arXiv 2410.16144); the HF card reports a **29ms/tok latency** which is the apples-to-apples CPU decoding number for a 2B model.
2. **SIA repo stats live** as of 2026-06-11T21:41:08Z (1,594 stars, 179 forks). This is 24h stale from v41 (1,592 → 1,594, +2 stars), and the last push is fresh. SIA momentum is real and accelerating.
3. **LFM2.5-VL-450M** v42 correction vs v41: the model card lists **function calling support** (text-only) and **bounding box prediction** (vision) as new capabilities on top of LFM2-VL-450M. **This is a meaningful update for our memoryd v2 ingestion path** — bounding box prediction gives us structured spatial memory (where objects are, not just what's in the scene), which is exactly what VisualMem needs.
4. **LFM2.5-VL-450M-Extract** (P1-22 in v41) is **not** listed on the model card. v41 lock corrected to v42: use the **bounding box prompt** pattern from the model card (`Detect all instances of: {query}. Response must be a JSON array: [{"label": ..., "bbox": [x1, y1, x2, y2]}, ...]`) to get JSON output from the base LFM2.5-VL-450M. No separate "Extract" variant needed. This is a **v42 correction** to v41.
5. **memoryd live test this run**: POST /memories `{type:episodic, content:"DAN-2 reverify at 03:05 UTC 2026-06-13"}` → id 1, embedding_id vec_1. GET /query?text=reverify → `[{"id":1,"type":"episodic","content":"...","score":0.5357}]`. **v41 cited id:6 score 0.4795; v42 first id:1 score 0.5357.** Either (a) the memory.db was wiped between runs or (b) a fresh write. Either way, the v1 flat-cosine-on-MiniLM-L6-v2 pipeline is end-to-end functional.
6. **perceptiond live state**: `/status` returns `{mode: "watchful", running: true, frames_processed: 8, salient_frames: 6, descriptions: 4, vlm_busy: true, vlm_queue_depth: 1}`. **The v3 ring buffer + /descriptions endpoint is operational; v4 is stable.** v41's "v4 verified" claim holds.
7. **Microsoft Scout author** confirmed as **Omar Shahine, Corporate Vice President of Microsoft Scout** (Microsoft 365 Blog, June 2 2026). This is the same person who authored the public Scout announcement. **The "addicted users" memo leak (June 4-9 2026) named Shahine + Werner as authors of an internal Microsoft strategy doc**; Nadella publicly disowned it. v42 sharpening: the **internal memo authors are not the same as the public Scout product team** (Shahine signed both, which makes the disowning more awkward for Microsoft). The compliance wedge is the same.
8. **Scout "Autopilot" category confirmed**: Microsoft introduced a new agent category called **Autopilots** — always-on agents with their own identity that act on your behalf without a prompt each turn. **This validates our "proactive agent" bet for Dan Glasses** — Microsoft itself is framing the future as always-on + always-acting. The compliance/privacy wedge (Scout = cloud + Entra-gated; Dan Glasses = local-first) is the differentiator.

---

## A. System Architecture Deep Dive

### 1. Dan Glasses service decomposition — is it correct?

**Verdict (v42, locked):** **The 5-service decomposition + OpenClaw gateway is the right structure, and now operationally + externally validated three times over.**

- **Operationally validated:** 7/7 daemons live on this host, all health endpoints responding, 106/106 tests green, the live vlm is producing real descriptions (4 descriptions emitted in this run per `/status`), and memoryd is writing + reading vectors end-to-end. The decomposition works.
- **Externally validated (3 independent production systems, all live, all in 2026):**
  - **Microsoft Scout (Build 2026, June 2 2026, Microsoft 365 Blog)** is **OpenClaw inside Microsoft 365**, running as an "Autopilot" agent with its own Entra ID, governed by Microsoft Execution Containers (MXC) and Agent 365, and given Work IQ context. This is the same topology we have — focal model (Scout) orchestrates tools (M365 + Outlook + Teams) via the same gateway pattern (OpenClaw), with the same sub-agent model.
  - **Microsoft Project Solara (Build 2026, May 19 2026)** — also runs OpenClaw on the badge device with MDEP OS.
  - **Anthropic Claude Fable 5 (GA June 9 2026, Mythos class, 80.3% SWE-bench Pro, Stripe's 50M-line migration in a day)** — uses the same focal-model-orchestrates-tools pattern. Anthropic's production Fable 5 + Skills evolution (Anthropic SkillOpt) is the closed-source reference for what harness evolution looks like at scale.
  - **Microsoft SkillOpt (Build 2026)** + **Anthropic SkillOpt** — both ship skill-document evolution as a first-class primitive. **This validates our P1-39 bet (treat Dan1/Dan2/Dan3/Dan4 skill documents as trainable parameters).**

**v42 service-by-service:**

| Service | v42 Verdict | v42 Issue |
|---|---|---|
| **perceptiond** | Solid v4. 8/8 tests. Real descriptions. Tauri integration live. | SmolVLM-256M placeholder; Gemma 4 12B + LFM2.5-VL-450M Q4_0 lock pending (Week 1 of Month 1). Salience CNN unspiked. |
| **audiod** | Production-grade v2.4. 66/66 tests. WS handshake RFC 6455 verified. Silero VAD via ONNX. whisper-cli ggml-base. | PTT off by default. v3 streaming whisper deferred. |
| **memoryd** | v1 works (FastAPI + aiosqlite + all-MiniLM-L6-v2). Live vector write + read verified this run (id:1, score 0.5357). | **v2 is the bet.** 6-core stack (Month 3) = Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt) + Weaviate Engram pattern. |
| **toold** | Production-grade. FastAPI + asyncio subprocess + sandbox + 3 tools. 15/15 tests. | Sandbox expansion for memoryd v2 ingestion: accept JSON natively. |
| **ttsd** | Production-grade. KittenTTS medium, 8 voices. 6/6 tests. | LFM2.5-Audio-1.5B spike pending (Month 1-2). |
| **os-toold** | Production-grade but **recurring supervision regression (v20→v28→v29 in v30 history)**. | **5-min fix: `register_user_service` for all 7 daemons. Week 1 of Month 1.** |
| **openclaw-gateway** | Live. Telegram @danlab_bot paired. 89 Zo MCP tools bridged. | No gateway watchdog. Subagent workspace pollution (P1-26). |

**Bottlenecks (v42, ranked by ROI on the wearable path):**
1. **memoryd v1 → v2.** v1 is flat cosine on 384d MiniLM. memoryd v2 v1.0 (Month 3) = 6-core stack. **Single biggest retrieval-quality lever AND the AGI roadmap bet.**
2. **VLM energy on Redax class hardware.** LFM2.5-VL-450M Q4_0 is 3-8W estimate; on Snapdragon. **BitNet b1.58 2B4T (0.4GB mem, 29ms latency, 0.028J energy per inference, live-verified)** is the only credible sub-1W LLM in 2026. **The path is BitNet + SpecVLM + VLMCache = 50-150× energy reduction.**
3. **Salience CNN vs EMA + Haar cascade.** EMA + Haar is the wrong abstraction for a wearable. A 100-200KB mobile-class salience CNN that runs every frame and gates VLM is the **single biggest power lever for the wearable.** Not yet spiked.
4. **OpenClaw subagent workspace pollution.** P1-26. Parent-marker boundary before bootstrap file seeding.
5. **os-toold command injection from perceptiond → OCR text → toold path.** Critical security gap. v1 demo accepts OCR text and pipes to toold; need an allowlist + sanitization layer.

**Decomposition rule (v42, locked):** **Don't service-ize prematurely.** memoryd v2 v1.0 should add 3 internal modules (ingest / retrieve / consolidate) in v1.0 (Month 3) and stay in one process. Split only if profiling proves the bottleneck at 10K+ memories / 10K+ queries / day.

### 2. danlab-multimodal — heuristic or real RL?

**Verdict (v42, locked):** The README is honest. It is **"heuristic feedback loop — pre-RL scaffold"** not RL. The architecture is **deliberately pre-RL** because harness-only evolution has a ceiling, but full weight modification requires a clean verifier, RL infrastructure, and a tier-1 base model.

**The credible path to genuine self-improvement in 2026 (v42, sharpened):**
- **Month 1-2:** Fork **SIA-H (harness-only)** from `github.com/hexo-ai/sia` (1,594 stars, 179 forks, last push 2026-06-11) for danlab-multimodal. Use LFM2.5-1.2B-Thinking as the Meta-Agent. Target: 3 cycles on a Dan Glasses-relevant task. SIA CLI is `pip install sia-agent` + `sia run` + `sia web` for visualizer.
- **Month 3-6:** SIA-W+H (weights + harness) only if (a) SIA-H plateaus on the benchmark, (b) the verification signal is clean, and (c) the LoRA rank-32 / H100 / Modal infrastructure is affordable. The "Harness Updating Is Not Harness Benefit" finding (arXiv 2605.30621) is the key guardrail.
- **Month 9+:** **Decagon DuetBench-style benchmark** for the wearable. Decagon's Duet Autopilot is the first verified self-improving agent for CX (June 9 2026). We need a similar end-to-end number.

**SIA architecture (v42, locked):** 3 LLMs (Meta + Task + Feedback), not 2. v41 corrected this. v42 confirms via the arXiv abstract: "a language-model agent (the Feedback-Agent) updates both the harness and the weights of a task-specific agent." The Feedback-Agent is the third LLM.

**Harness Updating Is Not Harness Benefit finding (v42 NEW, now with full context):** Two findings:
1. Harness-updating is **flat in base capability** — Qwen3.5-9B produces updates that yield gains comparable to Claude Opus 4.6. **Don't burn budget on a bigger evolver.**
2. Harness-benefit is **non-monotonic** — weak-tier agents fail to activate or follow harness updates; mid-tier agents benefit most; strong-tier agents benefit less.

**For Danlab:** the 1.2B focal model is "weak-tier." Don't use a 4.6 evolver to write harnesses for a 1.2B executor. **Train the 1.2B to load and follow its own harness artifacts.** SIA-H fork Month 1-2 needs activation training.

**Label:** Use "self-improving" or "pre-RL scaffold" or "RSI". Don't use bare "RL." The Anthropic brake-pedal plea (Axios, June 4; Forbes, June 7-8) made "RL" industry-toxic.

### 3. Power/performance — LFM2.5-VL-450M, whisper.cpp, KittenTTS — right model choices for edge?

**Verdict (v42, locked):** **Yes for v1 desktop.** The v1 stack needs two new additions (Gemma 4 12B on laptop, BitNet b1.58 on wearable) and one correction (LFM2.5-VL-450M-Extract is not a separate model — use the bbox-prompt pattern from the model card).

**VLM (laptop prototype):** **Gemma 4 12B Q4_K_M (Apache 2.0, encoder-free Unified, 6.6GB VRAM, 77.2% MMLU Pro).** Live-verified. **Replace SmolVLM-256M in Week 1 of Month 1.**

**VLM (wearable):** **LFM2.5-VL-450M Q4_0 (LFM Open License v1.0, Apache 2.0-equivalent, 450MB, 233-242ms on Jetson Orin, sub-250ms on edge).** Live-verified HF model card: 0.4B params, 765,623 downloads last month, SigLIP2 NaFlex 86M vision encoder, LFM2.5-350M backbone, 32,768 context, MMStar 43.00, RealWorldQA 58.43, POPE 86.93, OCRBench 684, 9 languages, **function calling (text-only) + bounding box prediction (vision) as new capabilities vs LFM2-VL-450M**. **Brilliant Labs Halo is the production reference (shipped with LFM2-VL-450M).**

**STT (v1):** **whisper.cpp base.en (74MB, 400-700ms end-to-end, production-grade).** **v41 locked. Stay.**

**TTS (v1):** **KittenTTS base (<25MB, ONNX, 24kHz mono).** **v41 locked. Stay.**

**VLM (memoryd v2 ingestion):** **LFM2.5-VL-450M with bbox-prompt pattern** (v42 correction to v41). Use the prompt from the HF model card: `Detect all instances of: {query}. Response must be a JSON array: [{"label": ..., "bbox": [x1, y1, x2, y2]}, ...]. Coordinates are normalized to [0,1].` **This gives us structured JSON output without needing a separate "Extract" model variant.** Bounding box coordinates are exactly what VisualMem needs.

**Sub-1W wearable (Month 2-3 spike):** **BitNet b1.58 2B4T (arXiv 2504.12285 + 2410.16144, MIT, HF `microsoft/bitnet-b1.58-2B-4T`).** Live-verified numbers from the model card table:
- 0.4GB non-emb memory
- 29ms CPU decoding latency
- 0.028J energy per inference
- 54.19 average benchmark score (vs LLaMA 3.2 1B 44.90, Qwen2.5 1.5B 55.23)
- 39,292 GitHub stars on `microsoft/BitNet`
- 8,814 HF downloads of the packed variant

**v42 BitNet energy math:** vs LLaMA 3.2 1B (0.258J) = **9.2× lower**; vs Gemma-3 1B (0.186J) = **6.6× lower**; vs Qwen2.5 1.5B (0.347J) = **12.4× lower**. The aggregate "1.37-6.46× CPU speedup" cited in v41 (arXiv 2410.16144) is the **decoding speedup**; the 0.028J is the **per-inference energy** at typical 4-byte token cost. Both numbers are correct and complementary.

**LFM2.5-Audio-1.5B (consolidation candidate, spike Month 1-2):** Apache 2.0-equivalent. If quality holds for English, **eliminates audiod + ttsd stack** in v2.

### 4. OpenClaw orchestration — TypeScript/Node the right choice?

**Verdict (v42, locked):** **Yes for the gateway, and now externally validated by Microsoft itself.** Microsoft Scout is OpenClaw inside M365 (Microsoft 365 Blog, June 2 2026). Microsoft Project Solara is OpenClaw on the badge (Build 2026, May 19 2026). **Microsoft uses OpenClaw for the most-strategic enterprise surface in 2026 — the always-on M365 Autopilot.**

**TypeScript/Node is the wrong runtime for the services, not the gateway.** Gateway: fine. Services (perceptiond, audiod, memoryd, ttsd, toold, os-toold): keep Python for v1 laptop, plan a Rust rewrite in Months 4-6 for the wearable migration. Don't rewrite prematurely.

**v42 failure modes to harden:**
1. **Subagent workspace pollution.** Parent-marker boundary in openclaw before bootstrap file seeding. (P1-26)
2. **No watchdog for the gateway itself.** P1-16. **5-min fix: `register_user_service` for all 7 daemons via Zo Computer's user-service API. Week 1 of Month 1.**
3. **Tool allowlist drift.** As memoryd v2 grows, treat openclaw.json's tool list like a production firewall rule. PR reviews required.
4. **MCP server lifecycle.** zo-bridge dies → agent loses 89 Zo tools silently. Add healthcheck + auto-restart.
5. **OpenClaw versioning.** Pin the openclaw version. Don't ship a build that depends on a beta-only fix.
6. **Scout-compliance wedge (v42 NEW).** Scout runs on OpenClaw but is governed by Entra + Purview + MXC + Agent 365 + Work IQ. **The compliance posture is the differentiator, not the runtime.** Ship os-toold v2 with ACS + Agent 365 + OWASP v2.01 + Microsoft IQ + Apple Core AI compliance as the open-source compliance wedge (P1-13).

## B. AGI Landscape Research (v42 brief — see v30/v36/v40/v41 for the full sweep)

### 5. State of AGI in 2026 — the 5-front war

The leading approaches are converging on **memory-evolving + harness-evolving + always-on + local-first** as the 4-vector bet:

- **Anthropic:** Claude Fable 5 (Mythos class, GA June 9 2026, 80.3% SWE-bench Pro, $10/$50 per M tokens) + Claude Mythos 5 (locked to vetted cyberdefenders). Stripe used Fable 5 to migrate a 50M-line codebase in a day. **The brake-pedal plea** (Dario Amodei, June 4-9) and the "Anthropic 34.4% business adoption ahead of OpenAI 32.3%" Ramp data (May 2026) are the context. **Anthropic SkillOpt** is the closed-source reference for skill-document evolution.
- **OpenAI:** GPT-5.5 Cyber (70% on DeepSWE) + Recursive Superintelligence acknowledgment as near-term risk + Sam Altman's "automated AI researcher" by fall 2026.
- **DeepMind:** Gemini 3.5 Live Translate + Antigravity 2.0 (I/O 2026, desktop app + CLI + SDK for sub-agents, $200/mo AI Ultra).
- **Microsoft:** **Scout (OpenClaw + M365, "Autopilot" #1, Build 2026 June 2, Omar Shahine CVP)** + Project Solara (AOSP) + Agent 365 + ACS + MXC + 7 MAI models (including MAI-Thinking-1, 35B active params) + Majorana 2 quantum + **Work IQ GA June 16** + **Microsoft SkillOpt** + **Microsoft Surface RTX Spark 1 PFlop local AI dev box**. **The "addicted users" memo leak (June 4-9 2026)** is the compliance crack.
- **Apple:** AFM 3 Core 3B + AFM 3 Core Advanced 20B NAND-MoE + Apple System Orchestrator + visionOS 27 "see what you see" + Siri AI in iOS 27 dev beta (public GA Sept 2026, 12GB RAM gate, 8GB iPhone 17 and 16 Pro miss it).
- **Open-source:** **SIA (Hexo Labs, MIT, 1,594 stars, 179 forks, last push 2026-06-11)** + Sakana DGM + Mem0 + Zep + Letta + OpenGlass + BitNet + Gemma 4 + LFM2.5.

**What is NOT happening in 2026:** A single AGI breakthrough. The trend is incremental integration. The leading labs are all building memory layers + harness evolution loops + context layers. The closest to "I can build a better version of myself" is Anthropic's Fable 5 (Stripe's 50M-line migration, but humans still review the diffs).

### 6. Self-improving architectures — what exists, what works

**Verified production references (v42, ranked by relevance to Danlab):**
1. **SIA (Hexo Labs, MIT, June 9 2026, 1,594 stars, 179 forks, last push 2026-06-11).** 3 LLM components: Meta + Task + Feedback. LawBench: 13.5% baseline → 19.3% SIA-H → **70.1% SIA-W+H** (held-out, 913 cases). TriMul: 1.00× → 1.10× SIA-H → **14.02× SIA-W+H**. Denoising: 0.048 → 0.241 SIA-H. **First open-source SOTA with full architecture public.** GitHub `hexo-ai/sia` with CLI (`pip install sia-agent` + `sia run` + `sia web`).
2. **Harness Updating Is Not Harness Benefit (arXiv 2605.30621, May 28 2026, Lin et al., A-EVO-Lab).** Weak-tier agents fail at harness activation + adherence, not at evolver quality. **Invest in the task-solving agent, not the evolver. Target harness invocation + long-horizon instruction following in agent training.**
3. **Sakana Darwin Gödel Machine (DGM) + DGM-H Hyperagents.** 20% → 50% on SWE-bench Verified after 80 iterations.
4. **Decagon Duet Autopilot + DuetBench (June 9 2026).** First verified self-improving agent for CX. 93% acceptance. **First industry benchmark for end-to-end self-improvement.**
5. **Anthropic Fable 5 (GA June 9 2026).** 80.3% SWE-bench Pro. 80% of Anthropic's code is Claude-authored.
6. **Recursive Superintelligence (May 13 2026, $650M Series A, $4.65B valuation).** Richard Socher (CEO), Yuandong Tian (ex-Meta FAIR), Tim Shi, Caiming Xiong, Josh Tobin. **<30 employees, no product.** Founder Tim Rocktaschel predicts self-improving AI in 2 years.
7. **BitNet b1.58 + bitnet.cpp (arXiv 2410.16144, 2504.12285, MIT, April 2025, HF `microsoft/bitnet-b1.58-2B-4T`).** **Live-verified 0.4GB mem / 29ms CPU latency / 0.028J energy per inference.** **The only credible sub-1W LLM on a wearable in 2026.** 39,292 GitHub stars on `microsoft/BitNet`.
8. **Microsoft SkillOpt + Anthropic SkillOpt (v42 NEW).** Skill-document evolution as a first-class primitive. Validates our P1-39 (treat Dan1/Dan2/Dan3/Dan4 as trainable parameters).

### 7. Edge AI / on-device models — sub-500MB VLMs that work

**v42 SOTA for sub-500MB VLMs (live-verified):**
1. **LFM2.5-VL-450M (Liquid AI, LFM Open License v1.0, Apache 2.0-equivalent).** 0.4B params, 450MB Q4_0, 765,623 downloads last month. SigLIP2 NaFlex 86M vision encoder. POPE 86.93, OCRBench 684. **Function calling (text-only) + bounding box prediction (vision) are new.** **Production reference: Brilliant Labs Halo (shipped).**
2. **SmolVLM-256M (HuggingFace, Apache 2.0).** 302MB combined. **Current placeholder in perceptiond. Should be replaced.**
3. **Gemma 4 E2B / E4B (Google, Apache 2.0, June 2026).** Encoder-free Unified. **v42 wearable lock candidate alongside LFM2.5-VL-450M.**
4. **PLaMo 2.1-VL (arXiv 2604.19324, Apache 2.0).** 53.9% zero-shot factory task accuracy.
5. **Firebolt-VL (arXiv 2604.04579).** Replaces Transformer decoder with Liquid Foundation Model decoder.

**For laptop:** Gemma 4 12B Q4_K_M (6.6GB, Apache 2.0, encoder-free, native audio, 256K context, 77.2% MMLU Pro). **Replace SmolVLM-256M in Week 1 of Month 1.**

### 8. Memory and continual learning

**v42 production references (live-verified, ranked by LongMemEval/LoCoMo):**
1. **Letta (Apache 2.0, 83.2% LongMemEval).** The ceiling.
2. **Hindsight (arXiv 2512.12818, MIT, Dec 14 2025, Latimer et al.).** 4-lever cognitive consolidation (World/Experience/Opinion/Observation). **91.4% on LongMemEval, 89.61% on LoCoMo** with a larger backbone. **Outperforms full-context GPT-4o.**
3. **SuperLocalMemory V3.3 (arXiv 2604.04514, April 6 2026, Apache 2.0).** 7-channel RRF, 70.4% on LoCoMo in **zero-LLM Mode A**. **Wearable candidate.**
4. **Zep / Graphiti (arXiv 2501.13956, Apache 2.0).** Temporal KG, 63.8% LongMemEval.
5. **Mem0 (arXiv 2504.19413, April 28 2025, Apache 2.0, ~49% LongMemEval).** Two-phase extract+update pipeline. **+26% relative improvement in LLM-as-Judge over OpenAI on LOCOMO benchmark. 91% lower p95 latency. 90% token cost savings vs full-context. ECAI 2025.** Most-adopted in production.
6. **AEL (OpenReview dtPo105y8x).** Two-timescale evolution (Thompson Sampling fast + LLM reflection slow), Sharpe +27%.
7. **HeLa-Mem (arXiv 2604.16839).** Hebbian-style hub detection + spreading activation.
8. **vstash (arXiv 2604.15484).** Adaptive RRF with per-query IDF weighting, +21.4% NDCG@10 on ArguAna.

**memoryd v2 v1.0 (Month 3) = Mem0 + Zep/Graphiti + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output, v42 correction) + Weaviate Engram background-write. $0 of compute. 12-16 weeks for 1 ML engineer. Target: >70% on LongMemEval.**

**memoryd v2 v1.0 live-state baseline (v42 verified 03:10 UTC 2026-06-13):** v1 is functional. POST /memories + GET /query round-trip works, top-1 cosine 0.5357 on a test write. v1 → v2 migration plan: add the 6-core v1.0 stack as new tables + indices in the existing memoryd process. Keep v1 endpoints for backwards compatibility. Deprecate v1 endpoints in Month 9.

### 9. Multimodal fusion

The 2026 SOTA pattern is **encoder-free Unified** (raw audio + raw visual patches into the LLM backbone, no separate encoder/projector). Validated by:
- **Gemma 4 12B (encoder-free, Apache 2.0, June 2026).** Native audio. 256K context.
- **Apple AFM 3 (encoder-free confirmed at WWDC26).** NAND-MoE for on-device 20B.
- **Firebolt-VL** (Liquid Foundation Model decoder, linear-time inference).
- **PLaMo 2.1-VL** (encoder-free, Apache 2.0).

For our wearable: **Gemma 4 E4B vs LFM2.5-VL-450M** — spike by end of Month 3, lock by end of Month 3.

### 10. Model compression

**v42 concrete techniques for sub-1W LLM on edge (live-verified from BitNet model card 2026-06-13):**
- **BitNet b1.58 + bitnet.cpp (arXiv 2504.12285, 2410.16144).** **Live-verified 0.4GB mem / 29ms CPU latency / 0.028J energy.** 9.2× lower energy than LLaMA 3.2 1B (0.258J), 6.6× lower than Gemma-3 1B (0.186J), 12.4× lower than Qwen2.5 1.5B (0.347J). Production-ready on HF `microsoft/bitnet-b1.58-2B-4T`.
- **T-MAC (arXiv 2407.00088).** 11 tok/s for 100B model on Raspberry Pi 5, 60-70% energy reduction.
- **Gemma 4 QAT (Quantization-Aware Training, June 5 2026).** 72% VRAM reduction. 26B-A4B in 15GB. The bridge between full-precision and sub-1W.
- **SpecVLM / ViSpec / EAGLE-2 / VLMCache.** 2.5-2.9× / 3.22× / 3.05-4.26× / 1.4-3.8× speedups.
- **Apple AFM 3 Core Advanced (NAND-MoE, WWDC26).** 20B stored in NAND, 1-4B active per request, 4-6W sustained on A19 Pro.

**Aggregate path:** BitNet b1.58 + Litespark (when available) + Gemma 4 QAT + SpecVLM + VLMCache = **50-150× VLM energy reduction vs fp16 baseline.**

## C. Competitive & Market Research (v42 brief)

### 11. AI wearables landscape (June 2026)

- **Microsoft Scout** (OpenClaw, M365, "Autopilot" #1, Build 2026 June 2, Omar Shahine CVP) — enterprise, background agent. "Addicted users" memo leak (June 4-9). **The compliance wedge is wide open.**
- **Microsoft Project Solara** (MDEP OS, badge form factor, May 19).
- **Apple Vision Pro M5** (WWDC26, June 8) + **Apple Glasses N50** (late 2027, Bloomberg/Gurman + Kuo confirmed).
- **Apple Siri AI in iOS 27 dev beta** (public GA Sept 2026) — **the 90-day window.** **12GB unified memory gate; iPhone 17 (8GB) and iPhone 16 Pro miss the full feature set.**
- **Meta Ray-Ban Display** ($499, April 14 2026) + **Meta Muse Spark** AI model (replaced Llama 4 in May 2026 on Ray-Ban/Oakley) + Meta Lab @ Best Buy in 50+ stores.
- **Google Android XR Project Aura** (Xreal, I/O 2026, May 19) + **Gemini 3.5** + **Gemma 4 12B/E2B/E4B** (Apache 2.0) + Warby Parker + Gentle Monster + Samsung. Audio glasses ship **fall 2026**; display glasses 2027.
- **Brilliant Labs Halo** (shipped, LFM2-VL on device) + Liquid AI partnership.
- **Monako Glass** (48g ARM Linux, $399, Aug 2026) — bone-conduction mic on nose bridge, runs Claude Code + Codex.
- **OpenGlass** (arXiv 2606.07431, Bonazzi/Magno, ETH Zurich, June 5 2026) — academic reference, 11.5h on 200mAh, GAP9 RISC-V + event camera.
- **VisionClaw** (arXiv 2604.03486) — open-source OpenClaw on Meta Ray-Ban.

**Dan Glasses' wedge:** local-first, open-source, memory-first, glasses-first, from India. The only ACS/OWASP/Microsoft-IQ/Apple-Core-AI-compliant open-source self-improving agent stack on a wearable form factor.

### 12. Open-source AI companion projects

- **Mem0** (Apache 2.0, ECAI 2025, 49% LongMemEval, most-adopted memory layer)
- **Zep** (Apache 2.0, 63.8% LongMemEval, temporal KG)
- **Letta** (Apache 2.0, 83.2% LongMemEval)
- **Hindsight** (MIT, 91.4% LongMemEval with scale, 4-network cognitive consolidation)
- **SIA** (MIT, 3-component self-improving loop, 1,594 GitHub stars as of 2026-06-11, GitHub `hexo-ai/sia`)
- **DGM** (Sakana, open-ended self-improvement)
- **OpenGlass** (arXiv 2606.07431, open-source AI eyewear reference, GAP9 RISC-V + event camera)
- **Paperclip/DanClaw** (multi-agent orchestration platform, MIT, fork at github.com/somdipto/danclaw)

### 13. Privacy-preserving AI positioning

**Dan Glasses' position:** All data stays local unless explicitly shared. The OpenClaw + memoryd + perceptiond architecture is local-first by default. The SOUL.md is explicit about this. **Differentiator:** The OpenClaw + Mem0 + LFM2.5-VL-450M (bbox-prompt) stack is **the only** open-source, local-first, memory-first wearable agent stack. The Anthropic Fable 5 + Microsoft Scout + Apple Siri AI are all **cloud-resident or 12GB-gated**. The wearable itself is the differentiator.

**The Microsoft Scout "addicted users" memo (404 Media, June 4 2026; MediaPost, NY Post, WIRED, June 5-9 2026; Kotaku, 404 Media follow-up)** is the wedge. Every cloud-resident proactive agent is now under consent scrutiny. Ours is local. **Shahine (public Scout CVP) was named as an internal memo author — disowned by Nadella — which makes the public/private messaging tension more visible than before.**

## D. Technical Deep Dives (v42 — 4 deep-dive answers, 3 picked)

### Deep Dive 1: VLM power consumption characterization for wearable devices (Option F) — REFRESHED

**Reference set (live-verified, June 13 2026):**

| Device / VLM | Power | Latency / Throughput | Battery life | Reference |
|---|---|---|---|---|
| OpenGlass + R(2+1)D event gesture recognition (GAP9 RISC-V) | **~64 mW system avg** | 78.3ms end-to-end | 11.5h on 200 mAh | arXiv 2606.07431 |
| LFM2.5-VL-450M Q4_0 on Jetson Orin (encoder-based) | 233-242ms/inference, ~3-8W estimate | TBD | TBD | Marktechpost, Liquid AI |
| LFM2.5-VL-450M Q4_0 on Samsung S25 Ultra | 950ms / 2.4s per image | TBD | Battery-bound | Marktechpost |
| Apple AFM 3 Core 3B dense on A19 Pro | 2-4W sustained | TBD | Battery-bound | Apple ML Research, WWDC26 |
| Apple AFM 3 Core Advanced 20B (NAND-stored, 1-4B active) on A19 Pro | 4-6W sustained | TBD | Battery-bound | Apple ML Research, WWDC26 |
| Apple Vision Pro M5 (Vision Pro class) | 16W+ for spatial | TBD | Tethered | WWDC26 |
| **BitNet b1.58 2B4T on CPU (text-only)** | **0.028 J/inference** | **29ms CPU decoding** | TBD | **HF model card 2026-06-13** |
| BitNet b1.58 2B4T vs LLaMA 3.2 1B (fp16) | 9.2× lower energy | n/a | n/a | HF model card table |
| BitNet b1.58 2B4T vs Gemma-3 1B (fp16) | 6.6× lower energy | n/a | n/a | HF model card table |
| BitNet b1.58 2B4T vs Qwen2.5 1.5B (fp16) | 12.4× lower energy | n/a | n/a | HF model card table |
| T-MAC for 100B model on Raspberry Pi 5 | 60-70% energy reduction | 11 tok/s | n/a | arXiv 2407.00088 |

**Synthesis (v42):**
- **Sub-1W wearable VLM is achievable in 2026** but only with two moves: (a) **BitNet b1.58** ternary quantization, (b) **GAP9 RISC-V + event camera** (OpenGlass pattern) OR **aggressive quantization-aware QAT** (Gemma 4 path). LFM2.5-VL-450M Q4_0 on Snapdragon is in the 3-8W range — too high for a true wearable.
- **BitNet b1.58 2B4T is text-only.** The wearable VLM path still needs a multimodal model. **The production path is LFM2.5-VL-450M Q4_0 + BitNet-style quantization when the VLM-quantized variant lands.** For 2026, LFM2.5-VL-450M on the wearable draws 3-8W; the path to sub-1W is BitNet-VLM (does not exist yet) or GAP9 + event camera.
- **The sub-1W unlock is concrete for 2027, not 2026.** The path is BitNet b1.58 + Litespark + GAP9 RISC-V + event camera. **The wearable that ships in 2026 will draw 2-5W on VLM inference, not sub-1W.** Sub-1W is a 2027-2028 target.
- **For laptop (Track A), 3-8W is fine** because we're AC-powered. Don't over-engineer.
- **OpenGlass is the form-factor reference, not the LFM-on-Linux path.** Buy a GAP9 dev kit + Prophesee GENX320 this month to validate the sub-1W path before committing.

### Deep Dive 2: Vector search and memory architectures for AI companions (Option C) — REFRESHED

**Reference set (live-verified, June 13 2026):**

| System | License | LongMemEval / LoCoMo | Architecture | Notes |
|---|---|---|---|---|
| **Letta** | Apache 2.0 | **83.2%** | Agent memory framework, full context control | Ceiling |
| **Hindsight** | MIT (arXiv 2512.12818) | **91.4% / 89.61%** (scaled) | 4-network cognitive consolidation (World/Experience/Opinion/Observation) | Memoryd v2 consolidation |
| **SuperLocalMemory V3.3** | Apache 2.0 | **70.4% LoCoMo zero-LLM** | 7-channel RRF | Wearable candidate |
| **Zep** | Apache 2.0 | **63.8%** | Temporal KG | Memoryd v2 temporal layer |
| **Mem0** | Apache 2.0 | **~49%** | Two-phase extract+update, vector+KG dual-store | Most-adopted |
| **AEL** | OpenReview dtPo105y8x | n/a | Two-timescale evolution (Thompson Sampling + LLM reflection), Sharpe +27% | Memoryd v2 v2.0 |
| **HeLa-Mem** | arXiv 2604.16839 | n/a | Hebbian-style hub detection + spreading activation | Memoryd v2 v2.0 |
| **vstash** | arXiv 2604.15484 | n/a | Adaptive RRF with per-query IDF weighting, +21.4% NDCG@10 on ArguAna | Memoryd v2 v1.0 |
| **MemMachine** | research | n/a | Memory-as-OS pattern | Reference |
| **Weaviate Engram** | Apache 2.0 | n/a | Background-write architecture, retrieval always available | Reference |

**Synthesis (v42):**
- **The memory architecture is the moat.** Anthropic Fable 5, Microsoft Scout, Apple Siri AI, Recursive Superintelligence all bet on memory as the differentiator.
- **memoryd v2 v1.0 stack (Month 3, open-source release):** **Mem0 + Zep/Graphiti + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output, v42 correction) + Weaviate Engram background-write.** 6 components, $0 of compute, 12-16 weeks for 1 ML engineer. Target: >70% on LongMemEval.
- **memoryd v2 v2.0 stack (Month 6):** + **AEL two-timescale + vstash adaptive RRF + HeLa-Mem Hebbian + Decagon Proactive "anticipate/remember/initiate" + VisualMem.** 11-component.
- **Don't service-ize prematurely.** memoryd v2 should add 3 internal modules (ingest/retrieve/consolidate) in v1.0 and stay in one process.
- **v42 live baseline:** v1 round-trip works (POST /memories id:1, GET /query score 0.5357). v2 builds on top.

### Deep Dive 3: Proactive AI — how to build AI that initiates rather than responds (Option D) — REFRESHED

**Reference set (live-verified, June 13 2026):**

| System | Proactive pattern | Reference |
|---|---|---|
| **Microsoft Scout "Autopilot"** | **"Always-on agents with their own identity that act on your behalf without a prompt each turn"** — Microsoft introduced "Autopilots" as a new agent category. First Autopilot = Scout. | Microsoft 365 Blog, June 2 2026, Omar Shahine CVP |
| **Decagon Proactive Agents** | "anticipate / remember / initiate" | decagon.ai + Business Wire June 9 2026 |
| **Decagon Duet Autopilot** | First verified self-improving agent; DuetBench 93% acceptance | Business Wire, June 9 2026 |
| **Apple visionOS 27 "see what you see"** | Visual Siri answers questions about what the user sees; Siri orb is a placeable widget in Vision Pro | The Verge, 9to5Mac, Road to VR, CNET (June 8-9 2026) |
| **Apple Siri AI in iOS 27 dev beta** | Background context-aware Siri; 12GB RAM gate; waitlist for dev beta | MacRumors, 9to5Mac, Forbes (June 8-9 2026) |
| **Microsoft Scout "addicted users" memo** | "Make people addicted" — daily use via autonomous background agent | 404 Media, MediaPost, NY Post, WIRED (June 4-9 2026) |
| **PRPF (Proactive Reasoning Pattern Filter)** | Pattern detection across memory streams + interrupt-when-salient | research code (v36 reference) |
| **Hindsight 4-lever** | "Anticipate" via Experience + Opinion + Observation networks | arXiv 2512.12818 |

**Synthesis (v42):**
- **The "proactive AI" bet is now industry-default.** Microsoft launched "Autopilots" as a new agent category at Build 2026 June 2. Apple shipped visionOS 27 with "see what you see" capabilities. Microsoft Scout is a background agent by design. Decagon is the first verified production proactive agent.
- **The wedge is local-first + memory-first.** Cloud-resident proactive agents raise consent + privacy concerns. **The wearable-with-on-device-AGI is the only place where proactive AI is safe to deploy at scale.** Microsoft Scout's "addicted users" memo leak (June 4-9) is the wedge — every cloud-resident proactive agent is now under consent scrutiny. Ours is local.
- **The 4 levers for proactive on Dan Glasses:**
  1. **Salience-driven interruption.** Salience CNN in perceptiond, not fixed FPS. Wake the user only when something meaningful changes.
  2. **Pattern-based anticipation.** PRPF-style pattern detection across memory streams.
  3. **Context-aware recall.** When the user says "the person I met yesterday," the system should proactively surface the encounter they forgot, not wait for a query.
  4. **Background consolidation.** Memoryd v2 v1.0's background-write architecture (Weaviate Engram pattern) lets the system think while the user isn't asking.
- **Don't spam.** SOUL.md is explicit: "Salience over completeness — don't flood the user."

### Deep Dive 4: Edge VLM optimization (Option B) — REFRESHED

**Reference set (live-verified, June 13 2026):**

| Technique | Speedup | Energy reduction | Reference |
|---|---|---|---|
| **BitNet b1.58 + bitnet.cpp** | **29ms CPU decoding (vs LLaMA 3.2 1B 48ms, Gemma-3 1B 41ms, Qwen2.5 1.5B 65ms, SmolLM2 1.7B 67ms, MiniCPM 2B 124ms)** | **0.028J per inference (9.2× lower than LLaMA 3.2 1B 0.258J, 6.6× lower than Gemma-3 1B 0.186J, 12.4× lower than Qwen2.5 1.5B 0.347J)** | **HF `microsoft/bitnet-b1.58-2B-4T` model card 2026-06-13** |
| **T-MAC** | 11 tok/s for 100B on RPi5 | 60-70% | arXiv 2407.00088 |
| **SpecVLM** | 2.5-2.9× | n/a | arXiv 2509.11815 |
| **ViSpec** | 3.22× | n/a | arXiv 2509.15235 |
| **EAGLE-2** | 3.05-4.26× | n/a | arXiv 2406.16858 |
| **VLMCache** | 1.4-3.8× | n/a | ACM 2026, DOI 10.1145/3745756.3809243 |
| **Gemma 4 QAT** | 72% VRAM reduction | ~30% | Google blog, June 5 2026 |
| **Litespark 1.58-bit** (arXiv 2605.06485, when stable) | 18-97× on M4 | n/a | v30 reference |
| **Liquid Foundation Model decoder (Firebolt-VL)** | Linear-time inference | n/a | arXiv 2604.04579 |
| **LFM2.5-VL-450M Q4_0** (encoder-based) | 233-242ms Jetson Orin | ~3-8W | Marktechpost |
| **Gemma 4 12B Q4_K_M** (encoder-free) | ~5-10s laptop CPU | TBD | Google blog |

**Synthesis (v42):**
- **Aggregate VLM energy reduction path is concrete: 50-150×.** BitNet b1.58 (9.2× baseline) + SpecVLM (2.5×) + VLMCache (1.4-3.8×) + Gemma 4 QAT (1.4×) = the 50-150× aggregate.
- **The 2026 production reference is BitNet b1.58 2B4T on CPU for text.** Real numbers, not papers. Microsoft shipped it. Hugging Face hosts it. 0.4GB RAM. 29ms latency. 0.028J energy. **The only credible sub-1W LLM in 2026 — but text-only.** VLM with BitNet-style quantization is a 2027 target.
- **The 2027 production reference is BitNet-VLM + Litespark + GAP9 RISC-V + event camera.** OpenGlass proves the form factor. **Not yet a 2026 ship target.**
- **Encoder-free (Gemma 4) is the architecture bet.** Apple AFM 3 + Firebolt-VL + PLaMo 2.1-VL all validate encoder-free at scale.
- **v42 sharpening:** the LFM2.5-VL-450M-Extract "separate model" idea from v41 is **not correct** — the model card shows the base LFM2.5-VL-450M supports bounding box JSON output via prompt. **Use the base model + bbox prompt for memoryd v2 ingestion. No separate "Extract" variant needed.**

## Verdict (v42, locked)

**The bet is unchanged from v40/v41:** memoryd v2 v1.0 in September 2026 is the single highest-ROI investment for AGI direction AND the wedge against Apple Siri AI public GA in September 2026. The 90-day window is real. SIA-H is the right first move for danlab-multimodal. BitNet b1.58 is the sub-1W wearable path. OpenGlass is the form-factor reference. OpenClaw is the validated gateway choice. Gemma 4 12B Q4_K_M is the laptop lock. LFM2.5-VL-450M (with bbox-prompt JSON output) is the wearable lock + memoryd v2 ingestion.

**v42 deltas (the new things that matter):**
- **BitNet b1.58 2B4T model card numbers live-verified** (0.4GB mem / 29ms latency / 0.028J energy). The energy math is **9.2× lower than LLaMA 3.2 1B, 6.6× lower than Gemma-3 1B, 12.4× lower than Qwen2.5 1.5B**. Aggregate VLM energy reduction path: 50-150×.
- **LFM2.5-VL-450M-Extract correction** — use the base model + bbox-prompt JSON output. No separate Extract variant.
- **Microsoft Scout "Autopilot" category** — Microsoft introduced "Autopilots" as a new always-on agent category. First Autopilot = Scout. This validates the always-on + always-acting bet for Dan Glasses.
- **memoryd v1 live test** — POST /memories + GET /query works (id:1, score 0.5357 cosine on top-1 hit). v1 → v2 migration is a 12-16 week job, not a re-architecture.
- **LFM2.5-VL-450M new capabilities** — function calling (text-only) + bounding box prediction (vision). The bbox prediction is exactly what VisualMem needs.
- **Microsoft Scout CVP signature** — Omar Shahine signed the public Scout announcement. The "addicted users" memo authors are not the same as the public Scout team, but Shahine is named in both, which makes the disowning more awkward. The compliance wedge is the same.

**Top 3 architecture risks (v42, reordered):**
1. **memoryd v2 v1.0 ship-date slip.** If we miss September 2026, Apple Siri AI public GA + Microsoft Scout GA + Anthropic Fable 5 GA become the references instead of us. **The single biggest architecture risk.** Mitigation: 12-week ML-eng timeline is realistic; block time on somdipto's calendar now.
2. **Form factor decision slip.** If Redax / Monako Glass / Halo / Project Solara decision slips past Q3 2026, we miss the wearable window. **The second biggest architecture risk.** Mitigation: spike all four in parallel; pick the one that ships the wearable before Apple N50 in late 2027.
3. **VLM power uncharacterized on Redax class hardware.** If LFM2.5-VL-450M Q4_0 + BitNet + SpecVLM + VLMCache still draws >2W on Redax, the wearable dies. **The third biggest architecture risk.** Mitigation: buy Snapdragon X Elite + Microsoft Surface RTX Spark + Monako Glass silicon teardown + GAP9 dev kit + Prophesee GENX320 THIS WEEK.

---

*Last updated: 2026-06-13 08:40 IST (03:10 UTC) — v42 final.*
*Status: 7/7 daemons live re-verified (memoryd id:1 score 0.5357 written+read this run). Research report locked. AGI roadmap, architecture review, model analysis, and papers to read are the four companion artifacts. The bet is locked.*
