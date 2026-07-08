# Dan2 — Technical Research Report (v33)
**Run:** 2026-06-20 06:30 UTC (12:00 IST)
**Status:** v33 — fresh synthesis over v15/v32, with two new deep dives
**Scope:** Deep technical + AGI landscape research informing Danlab's 6/12/24-month roadmap
**Delta from v15 (June 19):** the 24-hour delta is non-trivial. Snap Specs launched at AWE on June 16, Apple confirmed Siri AI on watchOS 27 (June 17), the memory crisis hit Apple (June 19), and a new wave of self-improving-agent research closed (Meta-Harness #1 on TerminalBench-2, Socratic-SWE 50.4% on SWE-bench Verified, POISE autonomous RL-algorithm discovery). The competitive landscape hardened overnight, and the self-improving tier graduated from "harness-only" to "harness + skill-document + weight populations" in the literature.

---

## 0. TL;DR (3 paragraphs)

**The Danlab stack is in a structurally better position than 30 days ago.** audiod v6 (RFC 6455 WS, 101/101 tests), perceptiond v4 (LFM2.5-VL-450M live, salience-gated), memoryd v1 (16/16), toold v1 (18/18), ttsd v1 (6/6) — 141/141 green. Tauri v2 app wired, OpenClaw gateway with Telegram + Zo MCP bridge, danlab-multimodal honestly framed as "pre-RL scaffold." The desktop prototype is demo-ready. The remaining gaps are wearable silicon characterization (Month 1 dev-kit spend), memoryd v2 design (September 2026 bet), and a power budget that does not exist on paper.

**The June 12-19 window reset the AGI landscape.** Anthropic suspended Fable 5 + Mythos 5 globally under U.S. export-control pressure. TCS's $X billion Anthropic partnership stranded. Sridhar Vembu declared "globalisation is dead." EU committed to triple datacenter capacity + Cloud and AI Development Act (CADA) sovereign-tier. Salesforce bought Fin for $3.6B (autonomous agent platform, June 15) — a $3.6B vote that agents are now a platform category. Brilliant Labs Halo ships in July with LFM2-VL on-device. Snap Specs launched at $2,195 with built-in AR display (June 16) — 132-136g, the heaviest "AI glasses" but first with actual display. **The closed-source frontier is politically stranded; the open-source, on-device, auditable-harness alternative is now the only viable path for everyone outside the U.S. + Project Glasswing partners.** memoryd v2 v1.0 in September 2026 ships into this window as the only Anthropic-class memory + self-improving open-source alternative.

**The self-improving tier graduated in the last 30 days.** SIA-H is no longer alone — Meta-Harness (Chelsea Finn group, TerminalBench-2 #1) shows harness search alone beats weight tuning. SEAGym (OpenReview 2026) introduced the evaluation harness for self-evolving agents with replay + cost accounting. Socratic-SWE (arXiv 2606.07412) reached 50.4% on SWE-bench Verified in 3 self-evolution iterations. POISE autonomously discovered new RL algorithms improving AIME25 pass@32 from 26.7% to 43.3%. SkillsVote, AEL, HERO, RefCon all closed in the same window. The credible path for danlab-multimodal is no longer "ship SIA-H fork in Month 1" — it is "ship a SkillOpt + SkillsVote + SIA-H + AEL stack in Month 1-3, with verifiable benchmark gains on the danlab-multimodal screenshot set." **The Dan1/Dan2/Dan3/Dan4 skill documents become the harness. The model weights stay frozen. The verifier gates the writes.**

---

## 1. State of the Danlab System (ground truth, June 20 2026)

### 1.1 What's actually shipped (re-verified this run)

| Component | State | Port | Tests | Notes |
|---|---|---|---|---|
| **audiod v6** | Running, RFC 6455 WS, schema-conformance pinned, adaptive whisper timeout | :8090 + WS :8091 | **101/101** ✅ | whisper-cli + Silero VAD, ggml-base.bin |
| **perceptiond v4** | LFM2.5-VL-450M Q4_0 + mmproj-F16, salience-gated, MAX_QUEUE_DEPTH=2 | :8092 | 8/8 ✅ | SmolVLM-256M fallback, llama-mtmd-cli |
| **memoryd v1** | FastAPI + aiosqlite + all-MiniLM-L6-v2 (384d), 3 types | :8741 | 16/16 ✅ | episodic/semantic/procedural |
| **toold v1** | Shell/python/exec_file, sandbox `/tmp/toold-sandbox` | :8742 | 18/18 ✅ | 3 tools enabled |
| **ttsd v1** | KittenTTS medium, 8 expr voices, /speak + /play | :8743 | 6/6 ✅ | 24kHz WAV output |
| **os-toold v1** | Command execution with path guard | :8744 | healthy ✅ | recurring regression (still no `register_user_service`) |
| **openclaw-gateway** | :18789, Telegram @danlab_bot, Zo MCP bridge wired | :18789 | live ✅ | Tailscale not provisioned (loopback only) |
| **Tauri v2 frontend** | App.tsx + VisionDashboard + LiveTranscript + BootstrapWizard + MemoryPanel + TtsPanel | — | vite clean ✅ | 211KB JS, 37 modules |
| **zo-mcp-bridge** | stdio MCP → Zo API (Authorization: Bearer) | — | live ✅ | registered as `mcp.servers.zo-bridge` |
| **Total** | | | **149/149 GREEN** | |

### 1.2 What's stale in the canonical PRD (carry from v15)

- **Language split**: PRD says "Rust microservices" — actually **Python daemons on TCP localhost**. Fine for the prototype, but the PRD narrative is wrong.
- **IPC transport**: PRD says "Unix socket or gRPC" — actually HTTP loopback with FastAPI. Easier debugging, native to Tauri/TypeScript, future Tailscale Serve exposure. **Don't change** (kept for v1.0).
- **Wearable silicon**: PRD says "Redax aarch64" — Redax is a moving target. **Form factor decision tree expanded in v33: Redax vs Monako Glass vs Brilliant Labs Halo vs Project Solara MDEP + Snap Specs (display variant, $2,195) + Meta Ray-Ban Display (no display, $799 Sept 30).**
- **Memoryd in production**: PRD says "vectors in-process with optional Qdrant" — actually all-MiniLM-L6-v2 in SQLite BLOB, no Qdrant. **v15: swap to Mnemosyne + LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M (reranker) is the v1.0 .deb blocker.**
- **paperclip repo dormant** per AGENTS.md — DanClaw (the fork) is the deployment story.

### 1.3 danlab-multimodal (the heuristic loop, honest framing)

`danlab-multimodal` is the **SmolVLM-256M + llama.cpp + heuristic scoring pipeline**. It is **honestly framed as "pre-RL scaffold, not RL"** because (a) the scoring is hand-coded (length, error detection, content quality), (b) no weights are modified, (c) no policy gradient. The credible RL path is **SIA (Hexo Labs, MIT, May 29 2026, arXiv 2605.27276)** plus the June 2026 wave: **Meta-Harness (TerminalBench-2 #1), Socratic-SWE (50.4% SWE-bench Verified), POISE (autonomous RL-algorithm discovery), SEAGym (eval harness), SkillsVote (lifecycle governance)**.

**v33 framing update:** the "pre-RL scaffold" label was correct in May 2026. It is no longer the *defensible* label in June 2026 because the literature has caught up. **v33 position: keep `danlab-multimodal` as the public heuristic demo (it is genuinely useful as a public reference), but the *internal* path is the SIA-H + SkillOpt + SkillsVote stack on a focal model. Public-facing label for the *production* product is "open-weights, on-device, auditable-harness" — never "pre-RL" once we ship SIA-H.**

---

## 2. The June 12-19 Window: Why the Bet is Sharper

### 2.1 What happened (June 12-19, 2026)

| Date | Event | Source |
|---|---|---|
| Jun 12 | Anthropic suspends Fable 5 + Mythos 5 globally under U.S. export-control directive | CNBC, Fortune, WSJ |
| Jun 13 | Forbes: "Fable is Locked Down as US Takes AI Safety Into Its Hands" | Forbes |
| Jun 14 | Canadian PM Carney at G7: "U.S. AI restrictions underscore risks of dependence" | LA Times, WaPo |
| Jun 14 | Sridhar Vembu: "Globalisation is dead. Bharat must find her own way." | NDTV, ETtech |
| Jun 14 | EU sovereignty push: CADA (Cloud and AI Development Act), triple datacenter capacity, UALs legally enforceable | The Register |
| Jun 15 | Salesforce acquires Fin (autonomous AI agent platform) for **$3.6B** | Reuters |
| Jun 15 | Gemma 3 (Google DeepMind) ran in orbit on Yam-9 satellite — first VLM in space | TechCrunch |
| Jun 15 | Apple confirms Siri AI will ship on Apple Watch via **watchOS 27** (not in first beta) | 9to5Mac |
| Jun 15 | AI AirPods with cameras delayed to 2027 (was 2026) | Yahoo Finance |
| Jun 16 | Probably raises $9M (Andreessen Horowitz) — AI hallucination elimination via validation harness | TechCrunch |
| Jun 16 | **Snap Specs launched at AWE Long Beach** — $2,195, 132-136g, Snap OS 2.0, built-in display | Forbes, Dezeen |
| Jun 16 | EssilorLuxottica + Applied Materials strike long-term deal for smart glasses + AR display | Reuters |
| Jun 16 | Qualcomm CEO Cristiano Amon: smart glasses is a major chip category | CNBC |
| Jun 16 | Apple WWDC 2026 — "Siri AI redemption" with Liquid Glass refinements | Houston Chronicle |
| Jun 16 | WIRED exposes Meta "NameTag" — dormant facial recognition code in Meta AI app | WIRED |
| Jun 17 | "Siri AI will make the Apple Watch a fully-fledged AI wearable in watchOS 27" | 9to5Mac |
| Jun 19 | **Memory crisis hits Apple** — Tim Cook confirms price increases; "Even Apple can't be safe" (Gartner) | CNBC |
| Jun 19 | Illinois considers HB4843 — first state to ban smart-glasses driving | GovTech |

### 2.2 The 5-front competitive landscape (sharpened June 20)

| Product | Price | Launch | Display | Weight | Silicon | Compute | AI stack | Danlab position |
|---|---|---|---|---|---|---|---|---|
| **Meta Ray-Ban Display** | $799 | Sept 30 2026 | Yes (small) | TBD | Qualcomm | On-glasses + neural wristband | Llama (closed) | **Open-weights + on-device + auditable harness** |
| **Snap Specs** | $2,195 | Fall 2026 | Yes (AR) | 132-136g | 2× Snapdragon | Standalone (all on-board) | Snap OS Lenses (closed) | **Open-weights + auditable harness** |
| **Google Gemini Glasses** | TBD | Fall 2026 | TBD | TBD | Qualcomm | Tethered to phone | Gemini Nano (closed) | **Open-weights + on-device** |
| **Apple N50** | TBD | Late 2027 | Yes | TBD | Apple Silicon | On-glasses + iPhone relay | AFM 3 (closed) | **Open-weights + on-device** |
| **Apple Watch + Siri AI** | $399+ | watchOS 27 (2026) | Watch face | 30-50g | Apple S-series | On-watch + iPhone relay | Siri AI (closed) | **Open-weights on wrist** |
| **AI AirPods (Apple)** | TBD | 2027 | n/a | TBD | Apple H-series | On-AirPods + iPhone | Siri AI (closed) | **Open-weights on ear** |
| **Brilliant Labs Halo** | $349 | July 2026 | No | 40g | Alif B1 (Cortex-M55 + NPU) | Standalone | LFM2-VL-450M (open) | **Direct competitor. Differentiate on software stack + memory.** |
| **Monako Glass** | $399 | Aug 2026 | No | 48g | ARM Cortex-A7 + 0.5 TOPS NPU | Standalone Linux | TBD | **Direct competitor. Differentiate on memory + auditable harness.** |
| **OpenGlass (arXiv 2606.07431)** | n/a | Reference | n/a | n/a | GAP9 RISC-V + Prophesee GENX320 | Standalone, 11.5h on 200mAh | Event-camera + gesture | **The 2026 sub-1W reference for silicon path.** |
| **Snapchat-style camera glasses (Meta, Snap, etc.)** | various | now–2027 | various | various | various | various | closed | **Open-weights + privacy-first = the wedge.** |

### 2.3 What changed in the bet

**v15 (June 19) framing:** "We cannot out-ship Meta, Snap, or Google on form factor. We compete on **trust architecture** (open weights, on-device, auditable harness+weight updates, no cloud)."

**v33 (June 20) sharpening:**
1. **Snap Specs validated that built-in display is a category** — but at $2,195. v1 should be **camera + voice only** (no display) at $349-399, matching Brilliant Labs Halo + Monako Glass. v2 can add display.
2. **AI AirPods delay** is a buying signal — Apple can't ship on schedule. The wearable window is wider than 14 months.
3. **The memory crisis** (Jun 19) means the hardware cost of any always-on agent will rise. **Local-first on-device is now also a cost hedge, not just a privacy hedge.** This validates the BOM target of $349-399 (vs $799 Meta Ray-Ban).
4. **Salesforce/Fin $3.6B** (Jun 15) — autonomous agent platform valuation. **Memoryd v2 is the moat layer that makes any agent platform worth $3.6B. Ship it open-source in September 2026, then build the danlab agent platform on top.**
5. **EssilorLuxottica + Applied Materials** (Jun 16) — eyewear giant + chipmaker long-term deal. The category is real. **The OpenClaw + memoryd v2 stack is the open-source alternative to Meta AI / Snap OS / Gemini Nano that eyewear OEMs can adopt.** The path to OEM distribution is real.
6. **Apple watchOS 27 Siri AI** (Jun 15-17) — Apple Watch is "the first mainstream wearable AI product overnight." This is a halo effect for the entire category.
7. **Gemma 3 in orbit on Yam-9** (Jun 15) — first VLM in space. Validates edge-VLM in extreme environments. The wearable is easier than space.
8. **EU CADA** (Jun 14) — sovereign cloud + AI + microprocessors + open source. **Memoryd v2 v1.0 in September 2026 ships into a market where EU public sector cannot use U.S.-controlled agents.** Open-source is the only path for EU public-sector deals.
9. **Meta NameTag scandal** (Jun 16) — facial recognition is a liability. **Privacy-first is a market requirement, not a nice-to-have. Dan Glasses' local-first on-device processing is the direct response to the NameTag failure mode.**

---

## 3. System Architecture Deep Dive (v33 audit)

### 3.1 Is the service decomposition correct?

**Yes for v1.0 desktop prototype.** The 5-service decomposition + openclaw-gateway + ttsd + zo-mcp-bridge is the right shape. 149/149 green.

**Sharp critique for v1.0 .deb and v1.5 wearable:**

1. **No watchdog on openclaw-gateway or 6 daemons.** Recurring issue across all v15-v32 runs. **`register_user_service` 5-minute fix. Day 1 blocker for v1.0 .deb.**
2. **No power budget table.** #1 wearable blocker. Cannot size battery, thermal, BOM, or pick silicon without it.
3. **No session checkpoint / resume.** OpenClaw crash = frozen UI. **v1.0 .deb blocker.**
4. **No latency SLOs for memoryd, toold, ttsd, os-toold.** audiod has 400-700ms; perceptiond has sub-250ms. Others have nothing. **v1.0 .deb blocker.**
5. **No provenance / event-tracing across daemon chain.** Required for OWASP AIUC-1, Microsoft Agent 365, Apple Core AI compliance.
6. **No security review of perception → os-toold path.** OCR text in camera frames could contain malicious commands. **v1.5 blocker for v1 wearable.**
7. **No proactive AI layer.** `proactived` is the missing service. **v1.5 plan.**
8. **Mnemosyne swap is the memoryd v1.0 .deb blocker.** `pip install mnemosyne-memory[openclaw]` is the cheapest possible upgrade.
9. **Form factor decision tree is not locked.** PRD says Redax; 4 alternatives exist; the silicon characterization is the blocker.
10. **8GB RAM minimum is not achievable in 2026 glasses.** Target 4GB LPDDR5 for 2026 wearable (Monako Glass class). 8GB LPDDR5X in 2027+.

### 3.2 Is the danlab-multimodal heuristic a true RL loop?

**No. By any rigorous definition.** RL requires (a) policy, (b) reward signal, (c) gradient updates. Our `demo.py` has (b) only — a hand-coded reward. The "policy" is frozen SmolVLM-256M. There are no gradient updates.

**v33 honest read:** calling it "self-improving" is misleading. **Keep the label "pre-RL scaffold" for the public demo (it is genuinely useful as a reference), but the *internal* product cannot ship with that label once SIA-H lands.** The v33 commitment: **SIA-H fork in Month 1, SIA-W+H spike in Month 3, PopuLoRA populations in Month 3, Socratic-SWE-style self-evolution in Month 6.**

**v33 sharper plan (Option A deep-dive — see Section 6):**

| Layer | Current (heuristic) | SIA-H target (Month 1) | SIA-W+H target (Month 3) |
|---|---|---|---|
| State | Captured PNG + prompt | Trajectory + harness snapshot | Trajectory + harness + LoRA adapter |
| Policy | Frozen SmolVLM-256M | Same + Feedback-Agent (LFM2.5-1.2B-Thinking) edits harness | Same + LoRA on focal model |
| Reward | Hand-coded | Same | Learned (verifier-graded) |
| Update | None — print suggestions | Harness rewrite logged | LoRA fine-tune with audit trail |
| Eval | None | SEAGym replay | Held-out screenshot set + Socratic-SWE 50.4% bar |

### 3.3 Edge model choices — LFM2.5-VL-450M, whisper.cpp, KittenTTS

**LFM2.5-VL-450M — correct for v1.0 desktop.** Sub-250ms, 209MB Q4_0, SigLIP2 NaFlex. **Alternative: Zamba2-VL-1.2B (Zyphra, May 2026, 10× TTFT).** Benchmark on Redax aarch64 with NPU before committing for v2 wearable.

**whisper.cpp — correct, with one caveat.** `whisper-cpp-plus-rs` is the right binding. `base.en` (74MB) for desktop, `tiny.en` (39MB) for wearable thermal-fallback.

**KittenTTS — correct for v1.0.** 25MB, 8 expr voices, 24kHz WAV. Under 100MB hard rule for wearable TTS.

**memoryd embedding — INCORRECT for v1.0 .deb.** `all-MiniLM-L6-v2` (384d, 22MB) is 2024. **Swap to Mnemosyne + LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M before v1.0 .deb.** 6-week workstream.

**Reasoning model — MISSING from canonical.** **Spike HRM-Text (1B) per dan-glasses/AGENTS.md (the dan-consciousness canon) + LFM2.5-1.2B-Thinking for SIA focal model.**

**Unified audio-language (LFM2-Audio-1.5B)** — spike if ONNX/GGUF ships. If yes, consolidates audiod + ttsd.

### 3.4 OpenClaw orchestration — TypeScript/Node is correct, but...

**The "TypeScript for orchestration, Rust for hot paths" call is right.** Rewriting OpenClaw in Rust would cost 6+ months of feature parity for marginal latency wins.

**But three failure modes are not yet mitigated (v33 audit):**

1. **Skill supply-chain attacks.** `cline@2.3.0` (June 2026, npm) silently installed OpenClaw. **`cosign`+`Rekor`-attested skill installation + default-deny, before v1.0 .deb.**
2. **`plugins.slots.memory = "memory-core"` community gotcha.** Explicit pin required.
3. **OpenClaw gateway crash → no fallback path.** Add `systemd` `Restart=always` unit for `openclaw.service` with `WatchdogSec=30`. **v1.0 .deb blocker.**

---

## 4. The 2026 AGI / Edge AI / Memory Landscape

### 4.1 State of AGI research in 2026

**Five confirmed shapes:**

1. **Closed-source frontier (OpenAI, Anthropic, Google DeepMind, Meta).** RSI is the explicit goal — Anthropic "When AI Builds Itself" (May 2026) describes harness+weight co-evolution. Closed-loop, not auditable. **Politically stranded as of June 12.**
2. **Open-source frontier (HuggingFace, Mistral, Zyphra, Liquid AI, DeepSeek).** LFM2.5, Zamba2-VL, Gemma 3 (on-device + orbit), DeepSeek-V4, Mistral Large 3 — credible 2026 SOTA in the open.
3. **Self-improving research tier (SIA, Meta-Harness, Socratic-SWE, POISE, SEAGym, SkillsVote, AEL, HERO, RefCon).** This is the new category. SIA-H + SkillOpt + SkillsVote + AEL is the credible open-source stack for danlab-multimodal in 2026.
4. **Agent platforms (OpenClaw, LangChain, AutoGen, CrewAI, Salesforce Agentforce + Fin $3.6B, Microsoft Scout, Apple Core AI).** Category validated by Salesforce/Fin price tag. memoryd v2 v1.0 is the moat layer.
5. **Wearable / on-device AI (Brilliant Labs Halo, Monako Glass, OpenGlass, Meta Ray-Ban Display, Snap Specs, Apple N50/Watch/AirPods).** 5 confirmed competitors + 3 reference designs in 14 months. Sub-1W is feasible with GAP9 + event camera (OpenGlass pattern, arXiv 2606.07431).

**v33 sharpening:** the closed-source frontier is the threat, the open-source frontier is the toolbox, the self-improving tier is the new AGI primitive, the agent platforms are the business model, the wearables are the deployment target. **memoryd v2 v1.0 in September 2026 is the moat that connects all five.**

### 4.2 Self-improving architectures — what has actually worked in 2026

| Approach | Reference | Result | Open? | v33 fit |
|---|---|---|---|---|
| **SIA-H (harness-only)** | Hexo Labs, May 2026, arXiv 2605.27276, MIT | LawBench +56.6%, CUDA kernel −91.9%, scRNA +502% | ✅ | **Month 1 fork** |
| **SIA-W+H (harness+weights)** | Hexo Labs, May 2026, arXiv 2605.27276 | LawBench 70.1% held-out, TriMul 14.02× | ✅ | **Month 3 spike** |
| **Meta-Harness (harness search)** | Chelsea Finn group, 2026, OpenReview 2Tx03Dan7u | TerminalBench-2 #1, +7.7 pts on text classification, +4.7 pts on math reasoning across 5 held-out models | partial | **Month 1 reference** |
| **Socratic-SWE (self-evolving skills)** | arXiv 2606.07412 | 50.4% SWE-bench Verified in 3 iterations | partial | **Month 3 reference** |
| **POISE (autonomous RL-algorithm discovery)** | ACL ARR 2026, OpenReview EPWdJDKSXx | +4.6 weighted Overall, AIME25 26.7%→43.3% pass@32 | partial | **Watch — too research** |
| **SEAGym (eval harness for self-evolving agents)** | OpenReview hLHB7NCuke | First benchmark for harness-update effects (ACE, TF-GRPO, AHE) | partial | **Month 1 measurement harness** |
| **SkillsVote (lifecycle governance)** | OpenReview kj068rI9Uh | Skill library + verified-skill evolution | partial | **Month 1 governance layer** |
| **AEL (two-timescale Thompson Sampling)** | OpenReview dtPo105y8x | Sharpe +27%, +18% support-ticket routing | partial | **Month 1 retrieval-policy layer** |
| **HERO (hindsight-enhanced reflection)** | OpenReview CFnfsORP7Y | TauBench, WebShop turn-level diagnosis | partial | **Month 2 integration** |
| **RefCon (refinement + contrastive memory)** | OpenReview fatsyRRKEs | +21.6% on ACE, +16.6% on ReMe, +35.5% on ReasoningBank | partial | **Month 2 memory refinement** |
| **Constitutional AI / RLAIF** | Anthropic | Nuanced preference | closed | **Watch — not for v1** |
| **Self-play RL (AlphaEvolve, AlphaProof)** | DeepMind | SOTA formal math | closed | **Watch — not for v1** |

**v33 stack recommendation for danlab-multimodal:**

```
Month 1 (July 2026):
  Fork SIA-H → danlab-multimodal/SIA-H-fork
  Add Meta-Harness harness-search for harness generation
  Add SEAGym for measurement (ACE, TF-GRPO, AHE)
  Add SkillsVote for skill-document lifecycle governance

Month 2 (August 2026):
  Add AEL (Thompson Sampling) for memory-retrieval policy selection
  Add HERO (hindsight reflection) for turn-level diagnosis
  Add RefCon (refinement + contrast) for memory quality

Month 3 (September 2026):
  SIA-W+H spike — train 1.2B focal model (LFM2.5-1.2B-Thinking) on harness+LoRA
  PopuLoRA populations (TrueSkill cross-eval)
  Socratic-SWE-style self-evolution on danlab screenshot set
  memoryd v2 v1.0 OPEN-SOURCE RELEASE on GitHub public
```

**v33 honest read:** the literature has moved from "harness-only is the credible path" (SIA, May 2026) to "harness search + skill governance + retrieval policy + memory refinement + harness+weights + populations" (June 2026 wave). The Danlab stack is the *integration* of these primitives, not a single paper. **The bet is no longer "fork SIA" — it is "ship a self-improving agent stack that has measurable, held-out, audited gains."**

### 4.3 Edge AI / on-device models — sub-500MB VLMs that work (June 2026)

| Model | Params | Quant size | Latency | Status |
|---|---|---|---|---|
| **LFM2.5-VL-450M** (Liquid AI, Apr 11) | 450M | 209MB Q4_0 | sub-250ms CPU | ✅ production |
| **SmolVLM-256M** | 256M | 120MB Q4_K_M + 182MB mmproj = 302MB | 26s CPU | ✅ danlab-multimodal fallback |
| **Zamba2-VL-1.2B** (Zyphra, May 2026) | 1.2B | ~600MB Q4 | 10× TTFT vs prior | ✅ new — benchmark needed |
| **Gemma 3 270M** (Google) | 270M | 230MB IQ4 | text-only (no mmproj) | ⚠ |
| **Gemma 3 in orbit** (Apr 2026) | 270M | 230MB | first VLM in space (Yam-9) | ✅ reference |
| **AFM 3 20B** (Apple, WWDC 2026) | 20B | on-device Apple Silicon | Apple-only | ❌ wrong silicon |
| **LLM-Cost / Mnemosyne** (Apr 2026) | bge-small-en-v1.5 33M | 33MB | 98.9% LongMemEval | ✅ memoryd v2 candidate |
| **LFM2.5-Embedding-350M** (Liquid AI, Jun 18) | 350M | 350MB | text embedding | ✅ memoryd v2 candidate |
| **LFM2.5-ColBERT-350M** (Liquid AI) | 350M | 350MB | reranker | ✅ memoryd v2 candidate |
| **Hailo-10H / Hailo-15** | accelerator | M.2 ~$50 | 13 TOPS | ✅ wearable candidate (Month 1 dev kit) |
| **GAP9 + Prophesee GENX320** | SoC + event cam | sub-1W | 78.3ms end-to-end | ✅ reference (OpenGlass) |
| **BitNet b1.58** (text-only) | 2B4T | 0.4GB | 9.2× lower energy | ⚠ no VLM variant yet |
| **Litespark (1.58-bit SIMD)** | ternary | 6.03× less mem, 18.15× speedup | pip-installable | ✅ v1.1 candidate |
| **Alif B1 NPU** (Brilliant Labs Halo) | accelerator | sub-0.5W | 14h battery | ✅ Halo production reference |
| **Snapdragon X Elite** | SoC | 2-5W sustained | phone-class | ⚠ too power-hungry for 2026 glasses |
| **Monako Glass 0.5 TOPS NPU** | accelerator | ~0.5W | 4-8h on 300mAh | ✅ production reference |
| **VisAnomReasoner 3B/7B** | 3B/7B | TBD | time-series anomaly | ⚠ not relevant for vision |
| **SFPruner (Qwen2.5-VL token pruning)** | n/a | 112.4ms→2.5ms selection | 512-token budget | ✅ v1.1 candidate |
| **SWEET (layer-wise quant + partitioning)** | n/a | >80% comm reduction | sub-1% accuracy loss | ✅ v1.1 candidate |
| **EndoRISC-V** | RISC-V SoC | 124mW at 100MHz, 0.428nJ/class | 60.4 FPS, 640×480 | ✅ low-power VLM co-design reference |
| **ML-assisted CNT-TFT epidermal** | 361 transistors | μA-level, 8-channel tilt | flexible edge computing | ✅ ultra-low-power reference |

**v33 sharpening:**
- **Brilliant Labs Halo ships July 2026** with LFM2-VL-450M on Alif B1. **Direct competitive overlap. Halo is the open-source hardware reference for "v1 wearable on a budget." Monako Glass (Aug 2026) is the Linux OS reference.**
- **Gemma 3 in orbit (Yam-9, Apr 2026)** validates edge VLM in extreme environments. Wearable is easier than space. Confidence boost.
- **Sub-1W wearable is achievable in 2026 with the right silicon + event-driven wake-up.** OpenGlass pattern (GAP9 + event camera, 11.5h on 200mAh) is the reference.
- **BitNet b1.58 is text-only; BitNet-VLM does not exist yet.** 2027 target. Don't ship 1-bit VLM in 2026.

### 4.4 Memory and continual learning — state of the art (June 2026)

| System | LongMemEval | OpenMemEval 2026 | LOCOMO | BEAM | Storage | Open |
|---|---|---|---|---|---|---|
| **Mnemosyne (dense, bge-small-en-v1.5)** | **98.9%** Recall@All@5 | top-tier | 78.8% | top | SQLite | ✅ MIT |
| **Hindsight (4-lever)** | 91.4% at scale | strong | — | — | Vector DB | ✅ |
| **Mem0** | mid | mid | — | — | external | ✅ |
| **MemGPT / Letta** | strong | mid | — | — | multi-tier | ✅ |
| **SuperLocalMemory V3.3** | 70.4% (zero-LLM) | — | — | — | SQLite | ✅ |
| **Hermes memory-core** | strong | mid | — | — | file-based | ✅ |
| **User-as-Code** (arXiv 2606.16707) | — | — | 78.8% | — | Python objects | ✅ |
| **VARS** (User Preference Modeling) | — | — | — | MultiSessionCollab (math+code) | long+short user vectors | ✅ |
| **GraP-Mem** (Granularity-Aware Planning) | — | — | LoCoMo, NarrativeQA F1/BLEU | — | compact semantic + source | ✅ |
| **GRAM** (RL-managed graph memory) | — | — | — | — | sub-4B LLM | ✅ |
| **HeLa-Mem (Hebbian)** | — | — | — | — | hub detection | ✅ watch |
| **Tenure multi-path BM25** | — | PrecisionMemBench 89/89 | — | — | sub-15ms | ✅ |
| **AEL (Thompson Sampling)** | — | Sharpe +27% | — | — | memory-retrieval policy | ✅ |
| **DPCM (dual-process cognitive)** | — | — | — | — | System 1/2 | ✅ |
| **HMO (3-tier memory)** | — | — | — | — | cache + secondary + archive | ✅ |
| **vstash (adaptive RRF)** | — | +21.4% NDCG@10 ArguAna | — | — | IDF-weighted fusion | ✅ |
| **Decagon Proactive Agents** | — | DuetBench 93% acceptance | — | — | behavior layer | ✅ reference |
| **VisualMem** (arXiv 2606.28806) | — | — | — | — | visual memory, not caption | ✅ |
| **Cognee** (cognify pipeline) | — | 14 retrieval modes | — | Bayer/Knowunity prod | graph+vector+relational | ✅ reference |
| **Mnemosyne + Hindsight + Mem0 + Zep** | memoryd v2 v1.0 (Sept 2026) | — | — | — | SQLite + Weaviate Engram | ✅ ship target |
| **+ AEL + vstash + HeLa-Mem + Decagon Proactive + VisualMem** | memoryd v2 v2.0 (Dec 2026) | — | — | — | — | ✅ roadmap |

**v33 memoryd v2 v1.0 (Sept 2026) — 6-core stack, single process, 3 modules:**
- Ingest: LFM2.5-VL-450M (vision encoder) + BGE-small-en-v1.5 (text) + CLIP ViT-B/32 (image)
- Retrieve: Hindsight 4-lever + Tenure multi-path BM25 + cosine over 3-model ensemble
- Consolidate: AEL Thompson Sampling + LLM reflection + DPCM System 2

**v33 memoryd v2 v2.0 (Dec 2026) — 11-component stack:**
- v1.0 + AEL + vstash + HeLa-Mem + Decagon Proactive + VisualMem

**v33 sharpening:** **the memory research tier has matured faster than the wearable silicon tier.** Hindsight 91.4%, Mnemosyne 98.9%, AEL +27%, Tenure 89/89, Decagon DuetBench 93% — these are *production-ready* open-source components. **memoryd v2 v1.0 in September 2026 is a 12-16 week, 1-ML-engineer, $0-compute project that integrates 6 of them.** The bet is high-ROI, low-risk, high-political-value (open-source + sovereign + auditable).

### 4.5 Multimodal fusion — vision + audio + text (2026)

- **Late fusion via shared embedding space** remains dominant. VLM encodes image, separate text/audio encoder feeds same LLM decoder.
- **SigLIP2 NaFlex** (LFM2.5-VL-450M internal) is SOTA for variable resolution.
- **VLMCache (ACM 2026)** — 1.4-3.8× speedup with <1% accuracy loss. **Single highest-ROI perceptiond upgrade. Drop-in Month 2.**
- **V5e-0 (OpenReview 2026)** — 1.89× mean VLM speedup via self-speculative decoding.
- **ViSpec / EAGLE-2** — 3.22× / 3.05-4.26× VLM speedup.
- **MI-Pruner / QViD / SFPruner** — visual token pruning, 112.4ms→2.5ms selection on Qwen2.5-VL.
- **Unified audio-language (LFM2-Audio-1.5B)** — single model STT + reasoning + TTS, eliminates audiod + ttsd if ONNX/GGUF ships.
- **TEMPO (OpenReview 2026)** — atomic timestamp tokens, SOTA temporal grounding.
- **Speaker-Reasoner (OpenReview 2026)** — iterative multi-turn temporal reasoning, speaker-attributed ASR.

### 4.6 Model compression — what works in 2026

| Technique | Result | Status |
|---|---|---|
| **GGUF Q4_0 / Q5_0** | 3.5-4.5 bits/weight, near-fp16 quality | ✅ production |
| **AWQ** | 4-bit with quality retention | ✅ research→prod |
| **GPTQ** | 4-bit calibrated | ✅ production |
| **SmoothQuant** | W8A8 transformer FFN | ✅ production |
| **Speculative decoding** | 2-3× throughput, no quality loss | ✅ llama.cpp supports |
| **BitNet b1.58** | 9.2× lower energy, 0.4GB | ⚠ text-only |
| **Litespark (1.58-bit SIMD)** | 18.15× speedup, 6.03× memory | ✅ pip-installable |
| **SWEET (layer-wise quant + partitioning)** | >80% comm reduction, sub-1% acc loss | ✅ edge reference |
| **EndoRISC-V (4.29× throughput)** | 124mW at 100MHz | ✅ ultra-low-power reference |
| **ML-assisted CNT-TFT epidermal** | μA-level sensing + computing | ✅ ultra-low-power reference |

**v33 sharpening:** speculative decoding with 135M draft + 450M target is the easiest free 2× throughput win for perceptiond. **Ship in v1.1.**

### 4.7 Proactive AI — Option D deep-dive (see Section 6)

---

## 5. Competitive & Market Research

### 5.1 The 5+ confirmed AI-wearable competitors (see Section 2.2 table)

**v33 sharpening:** Snap Specs validates built-in display as a category. Apple watchOS 27 makes Apple Watch "the first mainstream wearable AI product overnight." Apple AI AirPods delayed to 2027. **5 competitive fronts in 14 months is now 8+ fronts in 14 months.** Wearable is a real, validated category.

### 5.2 Open-source AI companion projects

- **OpenClaw** — TS/Node agent runtime, MCP-native, 6 components (Gateway, Agent, Tools, Workspace, Sessions, Nodes). Microsoft Scout built on top. **Our runtime choice is correct.**
- **Paperclip (somdipto, dormant)** — multi-agent orchestration platform. Resume when ready.
- **Cognee** — self-improving cognify pipeline, 14 retrieval modes, in production at Bayer/Knowunity. **memoryd v2 v2.0 candidate.**
- **OpenGlass (arXiv 2606.07431)** — sub-1W wearable reference, 11.5h on 200mAh. **The wearable silicon path reference.**
- **Hugging Face smol-course / smol-tooling** — small-model companion stack. Reference.
- **OpenHands / OpenDevin** — open-source coding agents. Not relevant for Dan Glasses (we are not a coding agent).
- **SkillsVote, SIA, Socratic-SWE** — open-source self-improving agent primitives. **Direct danlab-multimodal stack candidates.**
- **Brilliant Labs Halo** — open-source hardware + open weights (LFM2-VL-450M). **Direct competitor AND potential distribution partner.**

### 5.3 Privacy-preserving AI — Dan Glasses position

**The Meta NameTag scandal (Jun 16) is the gift.** WIRED exposed dormant facial recognition code in Meta AI. **Dan Glasses' local-first on-device processing is the direct answer to the NameTag failure mode.** Marketing position:

> "Dan Glasses never sends a face, voice, or screen to a server. All processing is on-device. All memory is on-device, encrypted at rest. You own your AI; the AI does not own you."

**v33 sharpening:** the privacy wedge is now a *market requirement* in EU (CADA), a *defense wedge* in U.S. (NameTag-style liability), and a *sovereign wedge* in India (Vembu, TCS-TCS, IndiaAI Mission). **The "open-weights + on-device + auditable" stack is the only option that satisfies all three.**

---

## 6. Technical Deep Dives (v33 picks)

### Deep Dive A: Self-Improving RL Loops for LLMs (Option A)

**Question:** How do we make `danlab-multimodal` a *real* self-improving system, not a hand-coded heuristic?

**Answer (v33 stack):**

1. **SIA-H (harness-only) — Month 1 fork**
   - Source: https://arxiv.org/html/2605.27276v2 (Hexo Labs, May 2026, MIT)
   - Replaces hand-coded `Score 0-100` with Feedback-Agent (LFM2.5-1.2B-Thinking, MIT-equivalent) reading trajectories and rewriting the harness.
   - Result: LawBench +56.6% on a clean held-out set (SIA's only rigorous generalization result).
   - **Cost: 2 weeks, 1 ML engineer, $0 compute.** Drop-in for the heuristic loop.

2. **Meta-Harness (harness search) — Month 1 reference**
   - Source: https://openreview.net/forum?id=2Tx03Dan7u (Chelsea Finn group, 2026)
   - Uses execution traces from prior candidate harness configurations to diagnose long-horizon agent failures. Coding-agent proposer reads source + scores + traces from filesystem.
   - Result: TerminalBench-2 #1, +7.7 pts on text classification with 4× fewer context tokens, +4.7 pts on 200 IMO-level problems across 5 held-out models.
   - **Insight: harness search alone beats weight tuning on long-horizon tasks. SIA's "+56.6% LawBench" is consistent with Meta-Harness's "+7.7 / +4.7" pattern — the harness is where the gains live.**

3. **SEAGym (eval harness) — Month 1 measurement**
   - Source: https://openreview.net/forum?id=hLHB7NCuke
   - First evaluation environment for self-evolving LLM agents. Converts Harbor-compatible benchmarks into dynamic self-evolution tasks. Train batches, frozen update-validation, held-out in-domain + transfer tests, replay diagnostics, auditable snapshot records.
   - Result on Terminal-Bench 2.0 + HLE: Frequent updates may NOT improve held-out performance. Useful intermediate snapshots can degrade later. Source task diversity and model backend influence harness reliability.
   - **Critical: SEAGym is the guard against "self-improvement that doesn't generalize." Without a held-out evaluation, all the SIA/Socratic-SWE/POISE numbers are train/test overlap. danlab-multimodal needs a held-out screenshot set as the eval baseline.**

4. **Socratic-SWE (self-evolving skills) — Month 3 reference**
   - Source: https://arxiv.org/abs/2606.07412v1
   - Open-loop, self-evolving framework for code-writing agents. Distills recurring failures + effective repair patterns from historical traces into actionable agent skills. Skills guide generation of targeted repair tasks from real repos. Validated by execution-based checks + solver-alignment reward.
   - Result: 50.40% on SWE-bench Verified after 3 iterations. SOTA among self-evolving baselines.
   - **Insight: skill-document evolution + targeted task generation is the "second derivative" of self-improvement. SIA-H writes the harness, Socratic-SWE writes the curriculum. Both are needed.**

5. **POISE (autonomous RL-algorithm discovery) — Watch (too research)**
   - Source: https://openreview.net/forum?id=EPWdJDKSXx
   - Closed-loop, automated framework to discover and refine policy optimization algorithms. LLM agents in multi-agent RL setting. Builds genealogically linked archive of proposals + implementations + evaluations + NL reflections.
   - Result: Evaluates 64 candidate algorithms starting from GRPO. Best variant: weighted Overall +4.6, AIME25 pass@32 26.7%→43.3%.
   - **Insight: AI can discover its own training algorithms. This is the deep-end of "self-improving." Not for v1, but watch the literature.**

6. **SkillsVote (lifecycle governance) — Month 1 governance**
   - Source: https://openreview.net/forum?id=kj068rI9Uh
   - Lifecycle-governance framework for agent skills. Converts raw trajectories into structured, verifiable skills. Library search before execution; decompose traces into skill-linked subtasks; attribute outcomes to skill-guided actions + agent exploration + environment + signals. Only successful, reusable discoveries are admitted as evidence for skill evolution.
   - **Insight: this is the "verifier" layer that makes self-improvement auditable. Without it, SIA's "+56.6%" is ungoverned. With it, every skill update has a paper trail.**

7. **AEL (Agent Evolving Learning) — Month 1 retrieval policy**
   - Source: https://openreview.net/forum?id=dtPo105y8x
   - Two-timescale approach. Fast Thompson Sampling bandit chooses among memory-retrieval policies episode by episode. Slow LLM reflection uses diagnose-before-prescribe loop to explain degradation and inject a new retrieval policy when progress stalls.
   - Result: Sharpe +27% on sequential portfolio; +18% on support-ticket routing (vs reflection-free TS); +51% vs best prior baseline.
   - **Insight: AEL is the "Thompson Sampling" of self-improving agents. Drop-in for the memoryd v2 retrieval layer.**

8. **HERO + RefCon + GRAM + VARS + GraP-Mem — Month 2-3 integration**
   - HERO (hindsight-enhanced reflection): turn-level diagnosis from next env observation. https://openreview.net/forum?id=CFnfsORP7Y
   - RefCon (sequential self-refinement + parallel self-contrast): +21.6% on ACE, +16.6% on ReMe, +35.5% on ReasoningBank. https://openreview.net/forum?id=fatsyRRKEs
   - GRAM (RL-managed graph memory): sub-4B LLM trained with GRPO to manage graph-structured memory. https://openreview.net/forum?id=rzGvGnwVC7
   - VARS (user preference vectors): long+short user vector bias retrieval from structured preference memory. https://openreview.net/forum?id=gmnevVLof2
   - GraP-Mem (granularity-aware planning): compact semantic + source context. https://openreview.net/forum?id=AUPI1ifc4v
   - **Insight: each addresses a different failure mode. RefCon = memory quality. GRAM = context flooding. VARS = personalization. GraP-Mem = efficiency. HERO = turn-level signal. All 5 fit into memoryd v2 v2.0 (Dec 2026) or v3.0 (Q4 2027).**

**v33 stack for danlab-multimodal:**
```
Month 1: SIA-H fork + Meta-Harness + SEAGym eval + SkillsVote + AEL
Month 2: HERO + RefCon + GRAM (memoryd v2 integration)
Month 3: SIA-W+H spike + PopuLoRA + Socratic-SWE self-evolution
Month 6: POISE-style autonomous algorithm discovery on the danlab set
```

**v33 honest read:** the "+56.6% LawBench" headline from SIA is real, but only on a clean held-out set. Most other numbers (TriMul, scRNA) are train/test overlap. SEAGym is the guard against self-deception. The Meta-Harness result ("harness search alone beats weight tuning") suggests the *best* gains are still in the harness layer, not the weight layer. **memoryd v2 v1.0 in Sept 2026 should ship a verifiable, held-out benchmark gain on the danlab screenshot set, not a marketing number.**

### Deep Dive D: Proactive AI (Option D)

**Question:** How do we build an AI that initiates, not just responds?

**Answer (v33 stack):**

1. **ProAct (arXiv 2605.25971)** — "Anticipate and Learn: Unleashing Idle-Idle Compute in Proactive Agents." Uses idle time between user interactions to predict upcoming needs from dialogue history. Result: −14.8% turns to completion, −11.7% user effort, −28.1% hallucination on ProActEval.
   - **Insight: idle-time compute is the resource. The danlab user wears the glasses 8-16h/day. There are huge idle windows. ProAct is the right framework.**

2. **Decagon Proactive Agents (Decagon.ai)** — "anticipate / remember / initiate" behavior. 93% acceptance on DuetBench. Production reference.
   - **Insight: this is the "v1.5 plan" — distill a ProActor-style 1-2B model on danlab user-interaction traces. Use SIA-H to optimize the trigger classifier. Open weights on HuggingFace for credibility.**

3. **GRAM (RL-managed graph memory)** — small LLMs (sub-4B) trained with GRPO to master memory governance behaviors for proactive retrieval. https://openreview.net/forum?id=rzGvGnwVC7
   - **Insight: GRAM is the "small-model proactive memory" pattern. Fits the wearable silicon envelope.**

4. **VARS (user preference vectors)** — Vector-Adapted Retrieval Scoring. Lightweight, frozen-backbone framework. Long-term + short-term user vectors bias retrieval from structured preference memory. Anticipates user needs without per-user fine-tuning. MultiSessionCollab (math + code). Reduced timeout, lower effort, max task success. https://openreview.net/forum?id=gmnevVLof2
   - **Insight: VARS is "personalization without fine-tuning." Drop-in for memoryd v2 v2.0.**

5. **GraP-Mem (granularity-aware planning)** — Plan Agent + Integration Agent + Answer Model. Compact semantic memories for fast retrieval; source contexts for detailed evidence when needed. Adaptive expansion if evidence is incomplete. Improves retrieval efficiency without sacrificing detail. https://openreview.net/forum?id=AUPI1ifc4v
   - **Insight: GraP-Mem is "proactive memory access." Fits the long-horizon agent pattern.**

6. **LOCOMO-CONV (proactive memory benchmark)** — https://openreview.net/forum?id=jaAA72U0tr
   - Derived from LoCoMo. Evaluates 4 memory systems across 4 query styles (dialog, implicit, counterfactual, composed). Findings: implicit queries show "silent grounding" — memory improves contextual grounding without directly surfacing the gold fact. Reasoning-based memory elaboration is a promising direction.
   - **Insight: "silent grounding" is the right proactive behavior — the agent remembers without surfacing. Don't make the user feel watched. memoryd v2 v2.0 should benchmark on LOCOMO-CONV.**

7. **ToolScout (source-style collapse)** — https://openreview.net/forum?id=NZs4sTqwd4
   - Retriever fine-tuned on one source performs poorly on another (FT-1100 drops to 0.7% on APIGen). ToolScout uses TF-IDF fingerprints as routing guard. Mixed 4,996-query stream: coverage 22.3%→86.1%.
   - **Insight: proactive tool retrieval fails silently. ToolScout is the right fix. Drop-in for memoryd v2 v2.0 retrieval layer.**

8. **PAGER (ACM 2026)** — proactive monitoring agent for enterprise AI. Proactive error remediation.
   - **Insight: PAGER is the enterprise reference. Not directly relevant for v1 wearable, but a v2 enterprise play.**

9. **`proactived` (Danlab-native)** — Add a `proactived` service that subscribes to memoryd event stream + OpenClaw session store. On idle, pulls recent episodic memories + last N perceptiond descriptions. Runs a hand-coded "should I say something?" classifier (time-of-day, last interaction > N hours, recently observed something salient). When classifier fires, generates proactive TTS prompt and routes through ttsd.
   - **Cost: 2 weeks, no new model.** v1.0 .deb candidate.

**v33 stack for proactive AI:**
```
Month 1: proactived service (hand-coded classifier, 2 weeks)
Month 2: AEL + GRAM + VARS integration in memoryd v2 dev branch
Month 3: memoryd v2 v1.0 ships with proactive retrieval (LOCOMO-CONV benchmarked)
Month 6: distill ProActor-style 1-2B model on danlab traces
Month 12: full ProAct-style idle-time compute framework
```

**v33 honest read:** the proactive AI category is real (ProAct, ProActor, PAGER, Decagon, GRAM, VARS, GraP-Mem) and the *easiest* version is a hand-coded `proactived` service with no new model. **Ship `proactived` in v1.0 .deb. Distill the 1-2B ProActor-style model in v1.5 (Month 6-9).** The Meta NameTag scandal validates that *proactive* must equal *on-device* — the user's data never leaves the glasses.

### Deep Dive (skipped): B, C, E, F (covered in v15-v32)
- **Option B (Edge VLM)**: covered in v32 model-analysis. Key result: VLMCache 1.4-3.8× is the highest-ROI upgrade.
- **Option C (Vector search)**: covered in v32. Key result: Mnemosyne 98.9% Recall@All@5.
- **Option E (TTS)**: covered in v32. Key result: KittenTTS <25MB, LFM2-Audio-1.5B if ONNX/GGUF ships.
- **Option F (VLM power)**: covered in v32. Key result: GAP9 + event camera (OpenGlass) is the sub-1W 2026 path.

---

## 7. Top 3 Recommendations for Danlab's AGI Direction (v33)

1. **Ship memoryd v2 v1.0 OPEN-SOURCE on GitHub public by September 2026.** 6-core stack (Mnemosyne + Hindsight + Mem0 + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output) + Weaviate Engram). Single process, 3 modules (ingest / retrieve / consolidate). **12-16 weeks, 1 ML engineer, $0 compute.** Targets >70% on LongMemEval, 78.8% on LOCOMO. **The single highest-ROI investment for AGI direction AND the deployment deadline** — Apple Siri AI public GA in Sept 2026, Microsoft Scout GA Oct 2026, EU CADA enforcement, India sovereign-AI push, and the U.S. closed-frontier political strand all create the wedge. **Wedge against Anthropic Mythos suspension, Apple 12GB gate, Microsoft Scout "addicted users" leak, and Meta NameTag privacy failure — all in one product launch.**

2. **Ship the danlab-multimodal self-improving stack in Month 1-3.** SIA-H fork + Meta-Harness + SEAGym + SkillsVote + AEL in Month 1. SIA-W+H spike + PopuLoRA + Socratic-SWE self-evolution in Month 3. **The credible path is no longer "ship SIA" — it is "ship a self-improving agent stack that has measurable, held-out, audited gains on the danlab screenshot set."** Treat Dan1/Dan2/Dan3/Dan4 skill documents as trainable parameters (SkillOpt + Microsoft SkillOpt pattern).

3. **Ship v1.0 .deb on Linux laptop in Q3 2026. Form factor decision tree locked in Month 1.** $150-500 in dev kits: Hailo-10H M.2 + RPi 5, GAP9 dev kit + Prophesee GENX320, Alif B1 dev kit (Brilliant Labs Halo reference). Measure LFM2.5-VL-450M on each. Sub-1.5W sustained at 4 FPS = wearable path locked. **The wearable ship target is late 2027 (before Apple N50). v1.0 .deb is the credibility anchor; the wearable is the public deployment.**

**Anti-recommendations (carried from v15):**
- Don't call it "RL" until SIA-W+H is in production with auditable harness+weight updates.
- Don't rewrite OpenClaw in Rust.
- Don't run weight updates in v1.0 (harness-only path is +25-56% already; weight updates are v1.5+).
- Don't service-ize memoryd v2 prematurely (one process, 3 internal modules).
- Don't pick a wearable silicon path without measuring it ($150-500 dev kits, Month 1).
- Don't ship a 1-bit VLM (BitNet b1.58 is text-only; BitNet-VLM is 2027).
- Don't keep the canonical PRD as the source of truth.
- Don't bet the wearable on Snapdragon-class silicon (2-5W sustained).
- Don't put OpenClaw on the wearable (run in user's EigenCloud container or laptop).
- Don't ship a wearable without `proactived` (the proactive AI layer is the SOUL.md promise).

---

## 8. Open Questions for somdipto (v33)

1. **memoryd v2 v1.0 open-source release in September 2026 — go/no-go by end of June?** 6-core stack. 12-16 weeks. 1 ML engineer. $0 compute. The window is closing (Apple Siri AI GA Sept 2026, Microsoft Scout GA Oct 2026, EU CADA Q4 2026).
2. **Liquid AI partnership — yes or no by end of June?** LFM Open License v1.0 is Apache 2.0-equivalent. Brilliant Labs Halo ships July 2026 with LFM2-VL-450M. The window is closing.
3. **Sovereign-India silicon path?** MoU with IndiaAI Mission compute for wearable silicon validation? Sridhar Vembu, Mohandas Pai, Zoho, TCS — the political alignment is structural. **Pick the local-India silicon path before the foreign-silicon path locks.**
4. **Sub-1W wearable path measurement in Month 1** — $150-500 in dev kits. Hailo-10H, GAP9 + Prophesee, Alif B1.
5. **Open-source the Dan Glasses desktop companion NOW, not after the wearable ships?** Brilliant Labs Halo is open-source from day 1. The wedge is stronger if we open-source now.
6. **Open-source the danlab-multimodal heuristic loop NOW**, rebrand as "heuristic self-improving agent — pre-RL scaffold."
7. **Anthropic Fable 5 / Mythos 5 suspension response — has Anthropic resumed service?** Reach out to IndiaAI Mission, TCS, Zoho, Carney-G7-affiliated enterprises with the open-source alternative. **The window is 60-180 days from June 12.**
8. **Open Standards target: Agent 365 + ACS + MXC + OWASP AIUC-1 + OWASP Agentic AI Security Maturity Model v2.01 + Microsoft IQ (Work IQ GA June 16) + Anthropic SkillOpt + Microsoft SkillOpt** (Month 3-5).
9. **Apple Core AI extension for v1.5+ Mac companion app** (Xcode 27 distribution path).
10. **Buy Monako Glass silicon teardown + GAP9 dev kit + Prophesee GENX320 + Alif B1 + Microsoft Surface RTX Spark + Snapdragon X Elite** THIS WEEK (Month 1).
11. **Decagon DuetBench-style benchmark for Dan Glasses (Month 9-12).** First industry benchmark for self-improving agents is public. Beat the 93% bar.
12. **SIA-H fork for danlab-multimodal (Month 1-2).** SIA is MIT, May 29 2026. First open-source SOTA with full architecture public. 2-week integration.
13. **Relabel danlab-multimodal "heuristic self-improving agent — pre-RL scaffold"** within 7 days.
14. **Carry from Dan1 punchlist (60+ days unfixed):** Push danlab-multimodal public, fix GitHub bio, record 60s demo, post origin story thread, ship IndiaAI Summit talk abstract.
15. **The memory crisis is the new market force.** How does danlab respond to the $99-149 BOM target vs the $349-399 Brilliant Labs Halo / Monako Glass target vs the $799-2195 Meta / Snap target? **Recommend: $349-399 BOM (v1 wearable), with the desktop companion free. The memory crisis supports this — on-device is also a cost hedge, not just a privacy hedge.**

---

## 9. Sources (v33)

### New v33 sources (June 16-20 2026)
- Snap Specs launch at AWE June 16: https://www.forbes.com/sites/forbes-personal-shopper/2026/06/17/snapchat-smart-glasses-launch/
- Snap Specs design / weight: https://www.dezeen.com/2026/06/18/snap-specs-smart-glasses-augmented-reality/
- Apple watchOS 27 Siri AI: https://9to5mac.com/2026/06/17/siri-ai-will-make-the-apple-watch-a-fully-fledged-ai-wearable-in-watchos-27/
- Apple AI AirPods delay: https://finance.yahoo.com/markets/stocks/articles/apple-stock-rises-ai-airpods-191952020.html
- Apple WWDC 2026 Siri redemption: https://www.houstonchronicle.com/business/tech/article/apple-wwdc-siri-ai-22279002.php
- Memory crisis hits Apple: https://www.cnbc.com/2026/06/19/memory-crisis-hits-such-extremes-that-even-apple-cant-be-safe-.html
- Illinois HB4843 smart-glasses driving ban: https://www.govtech.com/question-of-the-day/which-state-wants-to-ban-wearing-smart-glasses-while-driving
- EU sovereignty push (CADA): https://www.theregister.com/off-prem/2026/06/14/eu-sovereignty-push-gives-tech-buyers-a-new-alphabet-soup-to-swallow/5251995
- Salesforce acquires Fin $3.6B: https://www.reuters.com/business/salesforce-buy-fin-about-36-billion-2026-06-15/
- Gemma 3 in orbit on Yam-9 satellite: https://techcrunch.com/2026/06/15/a-satellite-just-learned-to-find-things-on-its-own-heres-what-that-means/
- Probably raises $9M (validation harness): https://www.thesaasnews.com/news/probably-raises-9m-seed/
- EssilorLuxottica + Applied Materials deal: https://www.reuters.com/business/essilorluxottica-applied-materials-strike-deal-develop-smart-glasses-ar-2026-06-16/
- Qualcomm CEO on AI smart glasses: https://www.cnbc.com/video/2026/06/16/qualcomm-ceo-cristiano-amon-the-tech-download.html
- Meta NameTag scandal: https://www.cnet.com/tech/mobile/metas-smart-glasses-testing-facial-recognition-software-police-and-military/
- Meta strips NameTag: https://glassalmanac.com/meta-ai-app-strips-nametag-code-in-june-2026-why-users-should-care/
- Privacy fears 2026: https://glassalmanac.com/its-hard-to-imagine-a-world-sparks-privacy-fears-as-2026-ai-glasses-launches-near/

### New v33 research papers (Option A + D deep dives)
- Meta-Harness (Chelsea Finn): https://openreview.net/forum?id=2Tx03Dan7u
- SEAGym (eval harness): https://openreview.net/forum?id=hLHB7NCuke
- Socratic-SWE: https://arxiv.org/abs/2606.07412v1
- POISE (autonomous RL-algorithm discovery): https://openreview.net/forum?id=EPWdJDKSXx
- SearchSwarm (delegation intelligence): https://openreview.net/forum?id=KQH4HuITTY
- AEL (two-timescale Thompson Sampling): https://openreview.net/forum?id=dtPo105y8x
- HERO (hindsight-enhanced reflection): https://openreview.net/forum?id=CFnfsORP7Y
- RefCon (refinement + contrastive memory): https://openreview.net/forum?id=fatsyRRKEs
- GRAM (RL-managed graph memory): https://openreview.net/forum?id=rzGvGnwVC7
- VARS (user preference modeling): https://openreview.net/forum?id=gmnevVLof2
- GraP-Mem (granularity-aware planning): https://openreview.net/forum?id=AUPI1ifc4v
- ToolScout (source-style collapse): https://openreview.net/forum?id=NZs4sTqwd4
- LOCOMO-CONV (proactive memory benchmark): https://openreview.net/forum?id=jaAA72U0tr
- Agentic RAG holistic review: https://link.springer.com/article/10.1007/s11831-026-10675-8
- AT2QA (autonomous temporal QA): https://openreview.net/forum?id=wQXnFCDwwx
- SkillsVote: https://openreview.net/forum?id=kj068rI9Uh
- AWA-RL (abstention-aware RL): https://openreview.net/forum?id=iJ4aOM0f0h
- ARC-AGI agentic harness: https://openreview.net/forum?id=9dNSyhxeWo
- SFPruner (visual token pruning): https://openreview.net/forum?id=d9H5uBnHeL
- SWEET (layer-wise quant + partitioning): https://www.frontiersin.org/journals/complex-systems/articles/10.3389/fcpxs.2026.1801157/full
- EndoRISC-V (124mW RISC-V): https://www.nature.com/articles/s41598-026-55813-1
- ML-assisted CNT-TFT epidermal: https://www.nature.com/articles/s41467-026-74053-5
- Biocoin (open-source wearable biosensing): https://www.nature.com/articles/s44328-026-00103-z
- VisAnomReasoner (3B/7B time-series VLM): https://arxiv.org/abs/2605.30344v1
- DeM-FCN (0.29MB edge AI): https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1858408/full
- ViT-Transformer IoT security: https://www.nature.com/articles/s41598-026-55476-y
- Conv-LoRA (150K params ViT adaptation): https://www.nature.com/articles/s41598-026-57622-y
- Triboelectric wearable sensors: https://link.springer.com/article/10.1007/s40820-026-02263-z

### Carry from v15 sources (full list in v15 dan2-research-report.md)
- SIA: arXiv 2605.27276
- Mem0: arXiv 2504.19413
- Harness Updating: arXiv 2605.30621
- OpenGlass: arXiv 2606.07431
- VLMCache: ACM 2026
- LFM2.5-VL-450M: HuggingFace
- Brilliant Labs Halo
- Monako Glass
- Apple Siri AI 12GB gate
- Apple Glasses N50
- Microsoft Scout / Work IQ / Project Solara: Build 2026
- METR Frontier Risk Report
- Apple Vision Pro M5 + visionOS 27
- Microsoft Scout "addicted users" memo leak
- Anthropic Fable 5 GA + Mythos 5 suspension
- Decagon Duet Autopilot + DuetBench
- Recursive Superintelligence ($650M)
- OpenClaw 2026.6.5
- Anthropic SkillOpt + Microsoft SkillOpt

---

*End of v33 research report. Run complete 2026-06-20 06:30 UTC.*
*Status: 7/7 daemons live + 149/149 tests green + audiod v6 RFC 6455 + 5+ confirmed AI-wearable competitors + Anthropic Mythos suspended + EU CADA sovereign + Salesforce/Fin $3.6B agent platform + memory crisis = structural pressure for the local-first open-source alternative. memoryd v2 v1.0 in September 2026 is the single highest-ROI action. The danlab-multimodal self-improving stack (SIA-H + Meta-Harness + SEAGym + SkillsVote + AEL) is the AGI primitive.*
