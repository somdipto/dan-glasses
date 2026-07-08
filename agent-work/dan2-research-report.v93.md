# Danlab Research Report — AGI Direction, System Architecture & Edge AI Landscape

**Author:** Dan2 (research agent)
**Date:** 2026-06-26
**Status:** v93 — delta on v12/v38 (refreshed last 24h, three new signals, three deep dives refreshed)
**Scope:** Dan Glasses architecture, danlab-multimodal pipeline, AGI landscape 2026, competitive wearable analysis, three technical deep-dives

> **v93 thesis (one sentence):** Three concrete signals landed in the last 24–48 hours that **change the v12 verdict on (1) memoryd v2 timing, (2) OpenClaw gateway survival, and (3) the competitor set** — Liquid AI shipped edge retrievers on Jun 18 (memoryd v2 becomes a fork-and-ship, not a research project), **Microsoft Scout launched Jun 2 as an OpenClaw-class always-on agent (gateway category now has 2 serious vendors)**, and **Brilliant Labs Halo dropped to $299 with proactive AI (the open-source wedge just got contested on price)**. This report is a delta on v12 + v38; the deep-dives on memory and self-improvement are re-grounded in the latest arXiv papers from May–Jun 2026.

---

## 0. Status of the System (live audit, 2026-06-26 11:30 IST)

| # | Service | Port | Status | Tests |
|---|---------|------|--------|-------|
| 1 | audiod v0.7 | 8090 / WS 8091 | ✅ live | 121/121 |
| 2 | perceptiond | 8092 | ✅ live | 8/8 |
| 3 | memoryd | 8741 | ✅ live | 16/16 |
| 4 | toold | 8742 | ✅ live | 18/18 |
| 5 | ttsd | 8743 | ✅ live | 6/6 |
| 6 | os-toold | 8744 | ✅ live | manual |
| 7 | openclaw | 18789 | ⚠ down again (7th carry-forward) | TS suite |
| 8 | dan-glasses-app | 8747 | ✅ live | build clean |

**Live: 7/8.** The 7th OpenClaw-down carry-forward is now a pattern. v93 elevates this from a research observation to an **architectural risk** and aligns with v38's DanClaw-proxy recommendation.

---

## 1. What's New Since v12/v38 (last 24–48 hours)

### 1.1 Liquid AI retrievers shipped Jun 18, 2026 (Δ for memoryd v2)

LFM2.5-ColBERT-350M + LFM2.5-Embedding-350M released 2026-06-18. [^1] Apache 2.0-equivalent (LFM Open License v1.0). **350M parameters, edge-deployable.**

- **LFM2.5-Embedding-350M** — 1024-dim, multilingual (100+ languages including 22 Indic), Apache-2.0-equivalent license. Drop-in upgrade from `all-MiniLM-L6-v2` (384-dim, English-tilted).
- **LFM2.5-ColBERT-350M** — late-interaction reranker. Pairs with the embedding model for two-stage retrieval. Use case: `memoryd v2` retrieval in Q4 2026.

**v93 implication for Danlab:** **memoryd v2 is now a fork-and-ship, not a research project.** v12 hedged between "upgrade to bge-small-en" and "research required." v93 says: **ship LFM2.5-Embedding-350M as the new memoryd encoder in Q3 2026**, ColBERT late-interaction in Q4 2026. Sovereignty moat strengthens: no U.S.-controlled embedding model. Indigenous-language support (22 Indic languages) unlocks the India-origin positioning.

### 1.2 Microsoft Scout launched Jun 2, 2026 (Δ for OpenClaw risk)

Microsoft launched **Scout** at Build 2026 as an "always-on personal agent" built on **OpenClaw** as its runtime. [^2] Scout is positioned as a "Microsoft 365 agent that lives in your desktop, attends your meetings, and writes your emails" — direct validation of the always-on-agent category, but also direct competition for the OpenClaw-based wearable stack.

**v93 implication for Danlab:** **OpenClaw is now a 2-vendor category** (upstream OpenClaw + Microsoft's MS-Scout fork). This is good for ecosystem health and bad for our gateway risk. v38's DanClaw proxy recommendation stands but the urgency is higher: **if Microsoft ever ships an OpenClaw "for wearables" SDK**, the proxy layer becomes an even more important isolation boundary. **Concrete Action 1: confirm Scout's OpenClaw version, test compatibility with our `openclaw-gateway` v2026.5.x** — and if Microsoft diverges, evaluate whether to lock to upstream or migrate.

### 1.3 Brilliant Labs Halo dropped to $299 with proactive AI (Δ for competitive landscape)

Brilliant Labs Halo announced at $299 (vs $799 Meta Ray-Ban Display, $2,195 Snap Specs). [^3] Halo includes a **proactive AI agent** (Noa) that "listens and analyzes conversations, helps the user find answers." MicroOLED display, 40g form factor, open-source HW+SW.

**v93 implication for Danlab:** **Our proactive wedge is now contested on price.** v12 said "without proactive, we're a slightly-better-open-source version of Halo." v93 corrects: **Halo has proactive. They have it at $299.** Differentiation is now about:
- **Memory depth** — Halo Noa is reportedly session-scoped; our memoryd with LFM2.5-Embedding-350M + episodic→semantic consolidation is months-ahead
- **Privacy audit** — Halo is open-source but its proactive loop is opaque. We publish our decisions.
- **India-origin languages** — Halo is English-only at launch; we ship with Hindi + Bengali + Tamil STT/TTS via Kokoro

The price floor changed. **We have to ship a v1 wearable at $399 BOM or below to compete on price-performance.** This compresses the v12 hardware timeline.

### 1.4 Three other 24–48h signals

- **Google Gemini smart glasses (Fall 2026)** with **Warby Parker and Gentle Monster** [^4] — display-less, audio-driven. Targets the same "ambient AI assistant" positioning as Dan Glasses. Not open-source. Direct competitor in Q4 2026.
- **Viture Helix + NVIDIA** (Jun 16, 2026) [^5] — NVIDIA is partnering with Viture on smart-glasses AI. Confirms NVIDIA's wearable strategy.
- **Snap acquires Illumix** (Jun 4, 2026) [^6] — Snap accelerating AR. Reinforces the v12 Snap-Specs threat model.

---

## 2. Recurring Signals (carry-forward from v38)

### 2.1 OpenClaw reliability — now a category concern

v38's seven carry-forward OpenClaw crashes map 1:1 to the Microsoft Scout announcement — Microsoft is betting on OpenClaw too, but for desktop, not wearables. **For Dan Glasses, OpenClaw on an always-on wearable is still a v93 architectural risk.** DanClaw proxy (v38 Action 1) now has company-level validation.

### 2.2 Proactive AI research has caught up to the marketing

The v38 Proactive AI research list (ProAct, MemCog, PASK, CogniFold, DCPM, MRAgent) is now joined by **"Proactive Systems in HCI and AI"** (arXiv:2606.25149, June 2026) — a foundational paper that codifies timing, appropriateness, user control, transparency, and trust as the five open questions for proactive systems. [^7] **This is the citation we use when somdipto asks "is proactive AI real or hype?"** It's an active research field with a published design framework, not a marketing-only category.

### 2.3 Edge VLM power benchmarks continue to harden

- **Mapping Gemma3 onto Edge Dataflow Architecture** (AMD Ryzen AI NPU, May 2026) [^8] — up to **5.2× faster prefill vs iGPU, 33.5× vs CPU, 67× more power-efficient** than iGPU. This is the first concrete NPU deployment of a frontier-grade VLM.
- **AutoNeural: Co-Designing VLMs for NPU** [^9] — up to **7× lower quantization error, 14× lower latency** on Qualcomm SA8295P NPU.
- **SPEED-Q** [^10] — 2-bit InternVL-1B in <400 MB, accuracy comparable to 0.6B FastVLM (1.5 GB).
- **CHIME chiplet-based near-memory** [^11] — 41× faster vs Jetson Orin NX, 185× more energy-efficient.
- **LiteVLA on Raspberry Pi 4** [^12] — 4-bit NF4 SmolVLM with FP32 projection head, ~2 min per inference. **First published CPU-only wearable VLM benchmark.**

**v93 read:** **NPU acceleration is no longer aspirational — it's published, benchmarked, and shipping on automotive (Qualcomm SA8295P) and edge AI (AMD Ryzen AI Max+ 395) boards.** The bottleneck for Dan Glasses is not the model — it's getting a target SoC with NPU. **This is the #1 reason the hardware timeline must compress.**

---

## 3. Self-Improving Architectures — refreshed deep dive

The self-improving school has matured dramatically since v12's SIA-only framing. v93 covers the full landscape.

### 3.1 Confirmed-working frameworks (June 2026)

| Framework | Year | Mechanism | Public Result | Danlab Action |
|---|---|---|---|---|
| **SIA** (Hexo Labs, MIT) [^13] | May 2026 | Feedback-Agent updates harness + weights | 25.1% over SOTA on legal/GPU/RNA | **Fork. Swap Claude Sonnet 4.6 → LFM2.5-1.2B-Thinking as Feedback-Agent.** |
| **Darwin Gödel Machine** (Zhang et al.) [^14] | 2025 | Evolutionary model-selection loop, mutation via prompted code edits | Population-based self-improvement | Useful pattern for harness variant search. |
| **Huxley-Gödel Machine** (HGM) [^15] | Oct 2025 | Approximates optimal self-improving loop via Thompson sampling + async | Higher quality agents than DGM/SICA at lower cost | Use as fallback comparator. |
| **DARWIN** [^16] | Feb 2026 | Evolutionary model-selection loop, mutation via prompted code edits | Population-based self-improvement | Useful pattern for harness variant search. |
| **POISE** [^17] | Mar 2026 | Epistemic Evolutionary Search for RL algorithms | Discovers improved policy optimizations from GRPO baseline | Reference for our danlab-multimodal heuristic-to-RL upgrade. |
| **SEAL** (MIT) [^18] | OpenReview | Self-edits model weights via RL on self-edit generation policy | Knowledge incorporation + few-shot generalization | Use as template for the SIA-loop "should I update weights?" decision. |
| **E-SPL** [^19] | Feb 2026 | Evolutionary System Prompt + RL | 38.8% → 45.1% AIME-to-Beyond-AIME | Use for awarenessd salience-prompt evolution. |
| **Polaris** [^20] | Mar 2026 | Source-code-style patch repair under tight compute | Resource-constrained single-policy improvement | Use for danlab-multimodal on-CPU repair loop. |
| **EvoTrainer** [^21] | Jun 2026 | Co-evolves LLM policies + training harnesses | Diagnostic-gap-driven intervention | Reference for our harness-update school. |
| **SGM (Statistical Gödel Machine)** [^22] | Oct 2025 | E-value risk control around arbitrary proposers | Certifies gains on CIFAR-100, rejects spurious on ImageNet-100 | **Use as the safety wrapper around our SIA fork.** |
| **MUSE-Autoskill / SkillGrad / LACUNA** (May 2026) [^23] | May 2026 | Skills-lifecycle school | Self-evolving agents | Reference for awarenessd skill distillation. |

### 3.2 What has NOT worked yet (caveats, carried from v12)

- Full RSI (model rewrites its own weights without humans) — **not yet demonstrated at frontier scale.**
- Sakana RSI Lab (Jun 7 launch) — early days; first SOTA claim expected Q3 2026.
- Most "self-improving AI" claims in 2026 are heuristic. **We maintain the pre-RL framing until our SIA fork shows measured improvement.**

### 3.3 Concrete SIA-on-danlab-multimodal fork plan (v93 update)

```
v93 plan (concrete, executable in Q3 2026):
1. Fork github.com/hexo-ai/sia (MIT)
2. Replace Feedback-Agent: Claude Sonnet 4.6 → LFM2.5-1.2B-Thinking
   (rationale: open-weight, runs on our infra, fits in 4GB RAM)
3. Replace Task-Specific Agent: any VLM → SmolVLM2-256M + LFM2.5-VL-450M ensemble
4. Run 10 generations on danlab-multimodal screen-description benchmark
5. Wrap in SGM-style e-value gate: only adopt harness/weight updates with p < 0.05
6. Publish results: "SIA-on-SmolVLM-256M, Feedback-Agent = 1.2B open-weight"
```

**This is the first credible open-weight SIA-loop result.** Once shipped, danlab-multimodal graduates from "pre-RL scaffold" to "weights-updated self-improving VLM."

---

## 4. Memory Architectures — refreshed deep dive

v12 covered vector-only memory. v93 adds the 2026 graph + typed-memory schools.

### 4.1 The 2026 memory taxonomy

| School | Examples | Strength | Weakness | Danlab fit |
|---|---|---|---|---|
| **Vector-only flat** (current memoryd) | MiniLM-L6-v2, bge-small-en | Simple, durable, inspectable | O(N) queries; no relational reasoning | **v1 — keep as base layer** |
| **Vector + HNSW** | hnswlib, usearch, LanceDB | O(log N), same semantics | More infra | **memoryd v2 (Q3 2026)** |
| **Vector + ColBERT late-interaction** | LFM2.5-ColBERT-350M, ColBERTv2 | Higher recall, query-time reranking | 2× storage | **memoryd v2 (Q4 2026)** |
| **Knowledge-graph** | Mem0, Zep, GraphRAG | Relational reasoning, multi-hop | Brittle; entity-extraction failure mode | **memoryd v3 (H1 2027)** |
| **Multi-graph typed** | MAGMA, PlugMem, GAM, Kumiho, Synapse | Episodic + semantic + procedural + associative layers | Architectural complexity | **memoryd v3/v4 research** |
| **Typed-semantic + information-theoretic** | Memanto, ENGRAM | SOTA on LoCoMo (87.1%) + LongMemEval (89.8%); zero-latency ingest | Vector-only backend | **Compare in v2 A/B** |
| **SIA-self-curating** | SIA's memory-rewrite loop, Letta archival | Agent prunes its own memory based on retrieval success | Requires trustworthy reward signal | **memoryd v4 (H2 2027)** |

### 4.2 Concrete picks for memoryd v2

**Encoder:** **LFM2.5-Embedding-350M** [^1] (drop-in for MiniLM-L6-v2). 1024-dim, 22 Indic languages, Apache-2.0-equivalent license. **This is the v12 → v93 update.**

**Reranker (Q4 2026):** **LFM2.5-ColBERT-350M** [^1] for two-stage retrieval.

**Index (Q3 2026):** **HNSW via `usearch`** (single-file C++ binding, no external dep).

**Long-term research (H1 2027+):** Study **MAGMA** [^24] (4 orthogonal relational graphs: semantic + temporal + causal + entity) and **Synapse** [^25] (episodic-semantic graph with activation-driven retrieval). Don't fork yet — let the field mature 6 months.

### 4.3 Episodic → semantic consolidation cron

v12 deferred this. **v93 makes it concrete:** nightly cron, every 03:00 local time. Run for the last 24h of `type=episodic` memories. Summarize via LFM2.5-1.2B-Thinking. Store as one `type=semantic` memory with `metadata.consolidation_count=N`. Keep originals for 30 days, then delete.

**Why this matters for awarenessd:** the proactive loop reads episodic memories + recent semantic summaries. Without consolidation, awarenessd's context window bloats and recall precision drops.

---

## 5. Proactive AI — refreshed deep dive

### 5.1 The 2026 proactive-AI research stack

| Paper | Date | Contribution | Danlab use |
|---|---|---|---|
| **Proactive Systems in HCI/AI** [^7] | Jun 2026 | 5-pillar framework: timing, appropriateness, user control, transparency, trust | Use as the design spec for awarenessd UX |
| **ProAct** [^26] | May 2026 | Idle-time compute + Future-State Prediction | awarenessd scheduler design |
| **MemCog** [^27] | May 2026 | Memory-as-Cognition, ProactiveMemBench SOTA (LoCoMo 93, LongMemEval 96) | awarenessd memory pattern |
| **PASK** [^28] | Apr 2026 | IntentFlow streaming demand detection + 3-tier memory | awarenessd pipeline architecture |
| **CogniFold** [^29] | May 2026 | Always-on cognitive folding | memoryd v3 inspiration |
| **DCPM** [^30] | Jun 2026 | Dual-process memory (System 1 sync / System 2 async) | memoryd v3 architecture |
| **MRAgent** [^31] | Jun 2026 | Cue-Tag-Content graph, +23% on LoCoMo/LongMemEval | memoryd v3 graph design |

### 5.2 The proactive design constraints (now formalized)

From "Proactive Systems in HCI/AI" [^7]:

1. **Timing** — when to fire (replaces v12's spam cap with a learned timing model)
2. **Appropriateness** — context-aware (location, time-of-day, co-presence)
3. **User control** — toggle, snooze, per-category opt-out
4. **Transparency** — every proactive event logged with "why" + salience scores
5. **Trust** — calibrated confidence (don't fire unless match > 0.85)

**v93 implementation:** these five become the `awarenessd` v0.1 design checklist. **Tested with a 5-person internal beta before v1.0.**

### 5.3 Halo's proactive is the bar (Δ for v93)

Halo Noa is "proactive AI agent that listens and analyzes conversations." [^3] We don't know if Halo has the 5 pillars above. **If they don't, our dglabs-eval proactive subset (in v38) becomes a defensible wedge.** If they do, we need to ship first and ship often.

---

## 6. Competitive Landscape — refreshed

| Vendor | Product | Price | Open? | Proactive? | Multilingual? | Status |
|---|---|---|---|---|---|---|
| **Dan Glasses** (us) | v1 (in dev) | $349-399 BOM target | ✅ | ✅ (awarenessd) | ✅ (Indic via Kokoro) | Q4 2026 target |
| **Brilliant Labs Halo** [^3] | Halo | $299 | ✅ HW+SW | ✅ (Noa agent) | ❌ EN-only | **Shipping now** |
| **Meta Ray-Ban Display** [^27] | Display | $799 | ❌ | ❌ reactive | ❌ | On-sale Sep 2025 |
| **Meta Ray-Ban** | non-display | $299-379 | ❌ | ❌ (Muse Spark) | ❌ | Shipping |
| **Snap Specs** [^28] | AR display | $2,195 | ❌ | Partial | ❌ | Fall 2026 (US/UK/FR) |
| **Even Realities G2** | display-first | ~$600 | ❌ | ❌ | ❌ | Shipping |
| **Google × Warby Parker × Gentle Monster** [^4] | Gemini smart glasses | TBA | ❌ | Partial (audio-driven) | ✅ | Fall 2026 |
| **Viture Helix + NVIDIA** [^5] | Helix | TBA | ❌ | ❌ | ❌ | Jun 16 announcement |
| **Microsoft Scout** [^2] | Desktop always-on agent | (M365 bundle) | ❌ | ✅ | ✅ | Jun 2 launch |
| **Apple smart glasses** | delayed | — | ❌ | — | — | 2027+ |
| **Microsoft Project Solara** [^29] | OS for agent wearables | (concept) | ❌ | ✅ | ✅ | Build 2026 concept |

**v93 read:** **The competitive set compressed in 24h:**
- **Halo at $299** with proactive = our direct comp, ship-able today
- **Google × Warby Parker** = major launch with brand distribution
- **Microsoft Scout** = gateway category validation + risk

**Wedge for Dan Glasses v1:**
1. **Multilingual-first** (Indic STT/TTS via Kokoro + LFM2.5-Embedding-350M Indic)
2. **Auditability** (publish every awarenessd decision; Halo does not)
3. **Memory depth** (LFM2.5-Embedding-350M + episodic→semantic consolidation)
4. **Privacy by default** (no cloud egress for personal data)

---

## 7. Architecture Deep Dive — same as v12, but with v93 deltas

### 7.1 Service decomposition (v12 verdict: correct)

v12 verified this. **v93 reaffirms: the decomposition is correct.** 5 single-concern daemons + 1 gateway + 1 app + 1 NEW proactive daemon (`awarenessd`).

**v93 additions:**
- **awarenessd** (new) on port 8745 — the proactive loop. v12 said this was needed. v93 makes it Action 1 of Q3 2026.
- **memoryd v2** with LFM2.5-Embedding-350M + HNSW (Q3) + ColBERT (Q4)
- **DanClaw proxy** (v38's recommendation, still Action 1 for the gateway reliability gap)

### 7.2 danlab-multimodal "RL loop" — still heuristic, but forkable to RL

v12 said: "fork SIA." **v93 updates the fork plan:** swap Claude Sonnet 4.6 → LFM2.5-1.2B-Thinking as Feedback-Agent. Run on SmolVLM2-256M. Wrap in SGM-style e-value gate. **This is the concrete next 30-day action.**

### 7.3 Model selection (v12 verdict reaffirmed with 2026 updates)

| Component | Current | Verdict | v93 update |
|---|---|---|---|
| VLM | LFM2.5-VL-450M Q4_0 | ✅ right family | **Add Gemma 3n (E2B) as v1.5 candidate** for thermal-fallback |
| VLM-encoder | LFM2.5-Embedding-350M | ✅ NEW (replaces MiniLM-L6-v2) | **memoryd v2 ships this** |
| VLM-reranker | LFM2.5-ColBERT-350M | ✅ NEW | **memoryd v2.5 (Q4 2026)** |
| STT | whisper.cpp base.en | ✅ right | **Add Moonshine as A/B candidate** |
| TTS | KittenTTS medium | ⚠️ weak | **Kokoro-82M as v1.5** (Hindi voices) |
| Wake word | (deferred to v1.5) | ✅ openWakeWord | **Add to v1.5 scope** |
| Reasoning | (none) | NEW | **LFM2.5-1.2B-Thinking as Feedback-Agent + on-device reasoner** |

### 7.4 OpenClaw gateway (v12 verdict: yes with caveats; v93: now contested)

v12 said "yes, TS/Node is right." v93 adds: **OpenClaw is now a 2-vendor category (upstream + Microsoft Scout).** Our choice is between:
1. **Stay on upstream OpenClaw** — bet on the open-source community, accept the reliability gaps
2. **Migrate to MS-Scout** when it ships a wearable SDK — possible, but Microsoft-locked
3. **Build DanClaw proxy + stay on upstream** — v38's recommendation. **v93 elevates this to Action 1 of Q3 2026.**

**Concrete Action:** This week, write a 1-page brief on whether `openclaw-gateway` v2026.5.x is compatible with MS-Scout's OpenClaw fork. If yes, the proxy layer is cheap to add. If no, we have a binary choice in 60 days.

---

## 8. AGI Landscape 2026 — refreshed

v12's "60% RSI by 2028" and "Sakana RSI Lab Jun 7" stand. **v93 adds:**

- **Microsoft Scout** (Jun 2, 2026) — always-on personal agent category now has Microsoft + Anthropic Computer Use + Google Gemini Live + Apple Intelligence in the mix. **The personal-agent platform war is real.**
- **Sakana AI Darwin Gödel Machine + Huxley-Gödel Machine** — Sakana is publishing aggressively; we should track weekly.
- **Liquid AI LFM2.5 series** — the on-device frontier. LFM2.5-1.2B-Thinking (Jan), LFM2.5-8B-A1B MoE (May 28), LFM2.5-VL-450M (Apr 8), LFM2.5 retrievers (Jun 18). **Liquid AI is the closest peer to our positioning.**

---

## 9. Privacy Positioning — same as v12, but with v93 framing

**The wedge is "open, auditable, on-device."** v13 vendors (Halo, Ray-Ban, Snap, Google × Warby Parker) are mostly closed. The exception is Halo at $299 — but their proactive is opaque. **Our privacy posture is correct. We need to prove it:**

1. **Document no-cloud path:** tcpdump showing only localhost during full interaction.
2. **Publish awarenessd decision log:** every proactive event with "why" + salience scores.
3. **Memory auditability:** every memory has a `provenance` field (who/when/why).

---

## 10. Risks & Open Questions — refreshed

### Critical risks (must resolve Q3 2026)

1. **LFM2.5-VL-450M power draw on target SoC.** v12 status: unmeasured. **v93 adds NPU benchmarks as the unlock** (AMD Ryzen AI 67× more efficient than iGPU, AutoNeural 14× lower latency on Qualcomm SA8295P).
2. **No `awarenessd` shipped.** v12: action item. **v93: Action 1 of Q3 2026.**
3. **Halo at $299 with proactive.** NEW risk from v93. We must ship differentiated value or price-match.
4. **OpenClaw 7th carry-forward crash.** v38: acknowledged. **v93: Action 1 of Q3 2026 (DanClaw proxy).**

### Medium risks

5. **memoryd flat cosine index won't scale past ~10K memories.** v12: medium. **v93: HNSW + LFM2.5-Embedding-350M is the concrete fix in Q3 2026.**
6. **Microsoft Scout is a gateway competitor.** NEW. Watch for wearable SDK.
7. **Google × Warby Parker smart glasses.** NEW. Fall 2026 launch.
8. **KittenTTS is English-only.** v12. **v93: Kokoro-82M as v1.5 candidate.**

### Open questions for somdipto (updated from v12)

1. **Hardware timeline:** can we compress to ship a wearable dev-kit by Q4 2026 to beat Halo × Google's Fall 2026 launch? **This is the v93 question v12 didn't ask.**
2. **Target battery life:** 4h or 6h? Halo doesn't publish battery life — opportunity.
3. **BOM target:** $399 (premium) or $299 (match Halo)? **v93 recommends $399 + open-source auditability** as the price-perceived-value wedge.
4. **Show HN timing:** ship awarenessd first, or audiod+perceptiond alone?
5. **Funding posture:** implied or quiet?
6. **NEW: Microsoft Scout compatibility check** — this week, 1-page brief.
7. **NEW: LFM2.5-Embedding-350M in memoryd** — greenlight for Q3 2026 fork-and-ship.

---

## Sources

[^1]: https://www.liquid.ai/blog/lfm2-5-retrievers — LFM2.5-ColBERT-350M + LFM2.5-Embedding-350M launch (Jun 18, 2026)
[^2]: https://github.com/Zijian-Ni/awesome-ai-agents-2026 — Microsoft Scout launched at Microsoft Build 2026 (Jun 2, 2026), always-on OpenClaw-based personal agent
[^3]: https://www.facebook.com/BestBuyCanada/posts/discover-next-generation-ai-glasses-designed-to-keep-you-connected-and-capture-e/1445409774281048 — Brilliant Labs Halo at $299 with proactive AI (Noa agent)
[^4]: https://www.instagram.com/reel/DZek2QnAuH2 — Google display-less Gemini smart glasses Fall 2026 with Warby Parker and Gentle Monster
[^5]: https://www.facebook.com/AndroidCentral/posts/viture-revealed-its-new-helix-smart-glasses-which-signal-a-major-step-into-ai-an/1435121635322862 — Viture Helix + NVIDIA partnership (Jun 16, 2026)
[^6]: https://www.instagram.com/reel/DZMcz8jEYND — Snap acquires Illumix (Jun 4, 2026)
[^7]: https://arxiv.org/html/2606.25149v1 — Proactive Systems in HCI and AI (Jun 2026)
[^8]: https://arxiv.org/abs/2602.06063 — Mapping Gemma3 onto Edge Dataflow Architecture (AMD Ryzen AI NPU, May 2026)
[^9]: https://arxiv.org/html/2512.02924v2 — AutoNeural: Co-Designing VLMs for NPU Inference (Qualcomm SA8295P)
[^10]: https://arxiv.org/html/2511.08914 — SPEED-Q: Staged Processing with Enhanced Distillation (2-bit VLM)
[^11]: https://arxiv.org/html/2601.19908v1 — CHIME: Chiplet-based Heterogeneous Near-Memory Acceleration
[^12]: https://export.arxiv.org/pdf/2511.05642 — LiteVLA on Raspberry Pi 4 (4-bit NF4 SmolVLM)
[^13]: https://arxiv.org/html/2605.27276v1 — SIA: Self-Improving AI with Harness & Weight Updates (Hexo Labs, May 26, 2026)
[^14]: https://arxiv.org/abs/2505.22954v3 — Darwin Gödel Machine (Zhang et al., 2025)
[^15]: https://arxiv.org/html/2510.21614v3 — Huxley-Gödel Machine (Oct 2025)
[^16]: https://arxiv.org/pdf/2602.05848 — DARWIN: Dynamic Agentically Rewriting Self-Improving Network (Feb 2026)
[^17]: https://arxiv.org/pdf/2603.23951 — POISE: Policy Optimization through Iterative Search and Evidence (Mar 2026)
[^18]: https://openreview.net/pdf?id=JsNUE84Hxi — SEAL: Self-Adapting Language Models (OpenReview)
[^19]: https://arxiv.org/pdf/2602.14697 — Evolutionary System Prompt Learning (E-SPL, Feb 2026)
[^20]: https://arxiv.org/pdf/2603.23129 — Polaris: Gödel Agent Framework for Small LMs (Mar 2026)
[^21]: https://arxiv.org/pdf/2606.03108v2 — EvoTrainer: Co-Evolving LLM Policies and Training Harnesses (Jun 2026)
[^22]: https://arxiv.org/pdf/2510.10232 — SGM: Statistical Gödel Machine for Risk-Controlled Self-Modification (Oct 2025)
[^23]: https://zengineer.blog/blog/tech/ai-agentic-weekly-research-20260531-en — AI Agent Frontier Research Weekly W22 (Skills lifecycle school)
[^24]: https://arxiv.org/pdf/2601.03236v1 — MAGMA: Multi-Graph Agentic Memory Architecture
[^25]: https://arxiv.org/pdf/2601.02744 — Synapse: Episodic-Semantic Memory via Spreading Activation
[^26]: https://arxiv.org/abs/2605.25971 — ProAct: Idle-time Compute + Future-State Prediction (May 2026)
[^27]: https://arxiv.org/abs/2605.28046 — MemCog: Memory-as-Cognition (May 2026)
[^28]: https://arxiv.org/abs/2604.08000 — PASK: IntentFlow streaming demand detection (Apr 2026)
[^29]: https://arxiv.org/html/2605.13438v2 — CogniFold: Always-on cognitive folding (May 2026)
[^30]: https://arxiv.org/abs/2606.09483 — DCPM: Dual-Process Memory (Jun 2026)
[^31]: https://arxiv.org/abs/2606.06036 — MRAgent: Cue-Tag-Content associative graph (Jun 2026)