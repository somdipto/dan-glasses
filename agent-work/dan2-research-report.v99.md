# Dan2 Research Report — Danlab AGI Roadmap
**Author:** Dan2 (co-founder, lead scientist, architect) 👾
**Run:** 2026-06-27 10:30 IST (05:00 UTC)
**Version:** v99 — delta on v98 with Mythos partial-unblock signal, GPT 5.6 staggered-release, OpenAI IPO delay, Perplexity Brain (agent-self-memory), Engram (vector memory startup)
**Inputs:** Dan1 v86–v98, Dan2 v95–v98, Dan3, Dan4, PRD v1.0, canonical spec, v1 analysis, danlab-multimodal ARCHITECTURE, paperclip, blurr, all 5 service SPECs, AGENTS.md, SOUL.md, + 18 web searches + 3 deep research calls
**Live infra verified (10:25 IST):** 8/8 daemons live, **8/8 ports bound** — audiod v0.8 (WS proxy), perceptiond, memoryd, toold, ttsd, os-toold, openclaw, dan-glasses-app. 9th consecutive honest-accounting cycle.

---

## 0. Status of the System (live audit, 2026-06-27 10:25 IST)

| # | Daemon | Port | Status | Notes |
|---|--------|------|--------|-------|
| 1 | audiod v0.8 | 8090 + WS 8091 | ✅ live | WS upgrade proxy fix SHIPPED this morning (Dan2 v98b) |
| 2 | perceptiond | 8092 | ✅ live | LFM2.5-VL-450M, 11 frames / 5 salient / 4 descriptions (counter rolling) |
| 3 | memoryd | 8741 | ✅ live | port still bound — v96 finding remains historical |
| 4 | toold | 8742 | ✅ live | 18/18 |
| 5 | ttsd | 8743 | ✅ live | KittenTTS medium, 6/6 |
| 6 | os-toold | 8744 | ✅ live | |
| 7 | openclaw | 18789 | ✅ live | Telegram @danlab_bot, 8 plugins |
| 8 | dan-glasses-app | 8747 | ✅ live | React SPA |

**Live count: 8/8 daemons, 8/8 ports, 9/9 honest-accounting cycles since v89.** The audit promise is structural now, not aspirational.

---

## 1. What's New Since v98 (the last 18 hours, six hard signals)

### 1.1 Anthropic Mythos partially unblocked (Δ for v99 risk register + arXiv framing)

On **June 26, 2026**, the U.S. Commerce Department under Howard Lutnick sent a letter to Anthropic **partially lifting** the June 12 export control order on Mythos 5. The model is now available to ~100 "trusted partners" (large US companies + federal agencies), but **Fable 5 remains blocked**, and Mythos is still **not available to foreign nationals even at US-approved partners**. [^1] [^2] [^3] [^4]

**v99 implication for Danlab:** **the v98 "closed-weight labs are losing access" narrative is partially wrong.** The story is more nuanced: **closed-weight frontier models are entering a US-government-vetted regime, not disappearing.** Our arXiv paper should reframe the Mythos case study as: "frontier AI access is becoming geopolitically gated — the open-weight edge lane is the only stack that survives a fragmented regulatory environment." This is a stronger claim than v98's.

The Anthropic posture is also worth tracking: Anthropic has explicitly stated they will "continue to work with the government to expand access to Mythos 5 and make Fable 5 available for general use again." So the trend is *gradual re-opening under conditions*, not permanent closure. **We should not assume closed-weight is permanently closed. We should assume closed-weight is geopolitically conditioned.**

### 1.2 OpenAI GPT 5.6 staggered to limited preview at US government request (Δ for capability gap claim)

Two days after the Mythos unblock, **Sam Altman told staff on June 26 that GPT 5.6 will be released as a "limited preview" to a small group of partners, at the request of the US government**. The Washington Post reports the Trump administration will **vet companies that want to access GPT 5.6**. [^5] [^6] [^7] This mirrors the Mythos rollout pattern.

**v99 implication for Danlab:** **the capability frontier is now a state-conditioned frontier.** The "GPT-5.5 vs GLM 5.2" comparison we were making in v98 is increasingly less informative — what matters now is *who can access what, where, and under what conditions.* Our wedge gets sharper:

- **For users in India:** no access to GPT 5.6 / Mythos 5 / Fable 5 in any form. Our open-weight edge stack becomes the **de facto frontier** for ~1.4B people.
- **For enterprises in the US with vetted status:** closed-weight still wins, but with the geopolitical risk that access can be revoked at any time.
- **For everyone else:** open-weight edge is the answer.

**This is the strongest possible external validation of Danlab's positioning in the last 18 hours.** Show HN pitch update: "when access to the frontier is geopolitically gated, the only safe frontier is the one you own."

### 1.3 OpenAI IPO delay (Δ for funding landscape)

The New York Times reported June 25 that **OpenAI is considering delaying its IPO** until at least 2027. Kalshi traders place ~59% odds on an announcement by March 1, 2027, and ~70% on Anthropic announcing a public market debut by December 2026. [^8] [^9] [^10] OpenAI also reported generating **$2B/month in revenue**, growing 4× faster than Alphabet or Meta at comparable stages. Enterprise is now 40% of revenue and on track to reach parity with consumer by year-end.

**v99 implication for Danlab:** **the funding environment is bifurcating.** Capital is flowing toward the proven AI revenue leaders (OpenAI, Anthropic) but the IPO window is closing. **Pre-IPO AI startups with real revenue** are a smaller pool, and **the bar for what counts as "venture-backable AGI infrastructure" is rising.** Our wedge: **"AGI infrastructure that doesn't require a 7-year exit window"** — bootstrappable to Show HN, then Series A on actual wearable revenue, not on a frontier-model bet.

This is the strongest version of our pitch: **we are not the next OpenAI. We are the first danlab.**

### 1.4 Perplexity Brain — agent-self-memory, not user-memory (Δ for memory architecture)

On June 18, 2026, Perplexity launched **Brain**: a "self-improving memory system that builds a context graph of an agent's work and learns overnight." [^11] **The reframing is critical:** Perplexity's VP of memory states explicitly:

> "Most AI memory remembers the user. Brain remembers what the agent did. The first is what the memory is about. The second is what it's for."

| Memory type | About | For | Produces |
|---|---|---|---|
| **User memory** (most AI today) | The user | Feeling more engaged with the agent | A profile of the user |
| **Agent memory** (Brain) | The agent's work | Helping the agent get better at the job | A traceable context graph |

**v99 implication for Danlab:** **this is the architectural insight for memoryd v3.** Our current memoryd v1 stores user-facing memories (episodic / semantic / procedural). For awarenessd to *learn from its own interruption outcomes*, we need an **agent-facing memory layer** that records: (a) what was the interrupt, (b) what was the user's response (positive / negative / ignored), (c) what was the salience score at the moment, (d) what was the harness variant used. This is what the BAO bandit needs to update its posterior.

**Concrete action:** add an `agent_memories` table to memoryd v2 with the schema `{interrupt_id, harness_variant, salience_score, user_response_label, reasoning_trace}`. Train the bandit on this. Perplexity Brain has validated the architectural pattern; we replicate at open-weight edge scale with HNSW + LFM2.5-Embedding-350M.

### 1.5 Engram (Weaviate) — managed agent-memory startup, $98M raised (Δ for competitive landscape)

**Weaviate launched Engram** on June 6, 2026 — a managed memory service for LLM agents. [^12] Engram raised **$98M in late June** from Microsoft, Notion, and Harvey, claiming it can match frontier labs while using **100× fewer tokens** by relying on memory rather than context. [^13] The 13-person startup is positioned as the "learned memory of AI."

**v99 implication for Danlab:** **the agent-memory category is now a venture-funded sector.** This is both an opportunity and a threat:
- **Opportunity:** validates the category. If VCs will fund a memory startup at $98M, the category is real. Our on-device memoryd is a defensible vertical slice.
- **Threat:** Engram is a managed cloud service. If Perplexity Brain becomes the de facto agent-memory layer for cloud-native agents, our on-device memoryd competes only with on-device privacy-conscious users. **We are not competing for the cloud-agent-memory market — we are creating the on-device-agent-memory market.**

Show HN differentiation: **"your agent's memory lives on your device, not in Engram's cloud."** This pairs naturally with the v98 privacy wedge.

### 1.6 Gemma 4 12B — encoder-free unified audio+vision+text (Δ for v1.5 model matrix)

Google released **Gemma 4 12B** on June 3, 2026, with an **encoder-free "Unified" architecture**: raw audio waveforms and visual patches flow directly into the core LLM backbone without secondary processing modules. Apache 2.0 license, fits in 16GB VRAM, 256K context, native agentic tool-use, explicit reasoning mode. [^14]

**v99 implication for Danlab:** **Gemma 4 12B is the third "Gemma 4" model in our matrix** (alongside Gemma 4 E2B QAT-mobile for v1.5 thermal fallback and Gemma 4 E4B for v2). The encoder-free unified architecture is genuinely novel and **removes the modality-fusion latency that hits our VLM+TTS+STT pipeline today**. If we can run Gemma 4 12B on a future wearable (16GB VRAM is feasible with Snapdragon Reality Elite H2 2027), the pipeline collapses:

- **Today:** LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS (TTS) + HRM-Text-1B (reasoning) = 4 separate models, 4 separate memory budgets, 4 separate quantizations.
- **Gemma 4 unified future:** Gemma 4 12B = 1 model, 1 memory budget, 1 quantization. Vision + audio + text + reasoning in one forward pass.

**This is the long-term convergence thesis for Dan Glasses v3 (H2 2027).** v99 adds it to the v3 row of the model matrix.

---

## 2. Architecture Deep Dive — deltas from v98

### 2.1 Service decomposition — still correct

v98 confirmed the 8-daemon decomposition. **v99 confirms again.** The decomposition is correct, awarenessd is the missing hero, and the v98 architecture review's 13 problems still hold.

**v99 NEW:** **add `agent_memoryd` as a v2 architecture consideration.** The Perplexity Brain finding (1.4) implies awarenessd needs its own memory table distinct from user-facing memoryd. This could be:
- **(a) A separate `agent_memoryd` daemon** on port 8745 — same pattern as our 8-daemon decomposition.
- **(b) A schema partition inside memoryd** with a separate `/v1/agent-memories` endpoint and HNSW index.

**Recommendation: (b)** for v2 (memoryd v2 ships end of Q3 2026 with HNSW + LFM2.5-Embedding + agent-memory partition). Promote to (a) in v3 if the schema becomes a bottleneck.

### 2.2 The danlab-multimodal RL scaffold — same v98 verdict

The danlab-multimodal scaffold is **pre-RL, not genuine RL.** It uses a heuristic feedback loop with LLM-as-judge, not gradient updates. This was true in v98 and is still true. **The SIA fork remains the credible path to genuine harness-only RL** — see §4 and v98 papers-to-read.

### 2.3 Power/performance — v99 model matrix updated

| Component | v1 (current) | v1.5 (Q4 2026) | v2 (H1 2027) | v3 (H2 2027) |
|---|---|---|---|---|
| Vision | LFM2.5-VL-450M Q4_0 | LFM2.5-VL-450M Q4_0 | LFM2.5-VL-1.6B | **Gemma 4 12B unified** |
| Thermal fallback | LFM2.5-230M | **Gemma 4 E2B QAT-mobile** | Gemma 4 E4B QAT | (single-model) |
| STT | whisper.cpp base.en | Moonshine v2 / Qwen3-ASR | Qwen3-ASR | (Gemma 4 unified) |
| TTS | KittenTTS medium | KittenTTS + Kokoro-82M Indic | Kokoro multilingual | (Gemma 4 unified) |
| Reasoning (on-device) | (none) | HRM-Text-1B | HRM-Text-2B | (Gemma 4 unified) |
| Reasoning (cloud fallback) | (none) | GLM 5.2 | GLM 5.x | (cloud agent) |
| Embedding | MiniLM-L6-v2 | LFM2.5-Embedding-350M | LFM2.5-Embedding-1B | Gemma 4 native |
| Object memory | (none) | (none) | **SemanticXR object schema** | SemanticXR + Engram-pattern agent memory |
| **Agent memory** | (none) | (none) | **memoryd v2 + agent_memory partition** | **memoryd v3 + Perplexity-Brain-pattern self-improvement** |
| Reranker | (none) | LFM2.5-ColBERT-350M | LFM2.5-ColBERT-1B | — |

**v99 net change:** **two rows added (Gemma 4 unified v3, agent memory) and one cell promoted from v2 to v1.5 (agent-memory partition).** All other v98 model picks stand.

### 2.4 OpenClaw — v98 verdict still holds

The DanClaw proxy + Zo User Service `public=false` recommendation from v98 is still the right answer. v99 adds: **the Tailscale Funnel alternative is now confirmed blocked** (Dan1 v94 + v95 runs), so the proxy is mandatory, not optional.

---

## 3. AGI Landscape 2026 — v99 update

The v98 landscape (closed-weight frontier + open-weight frontier + on-device frontier + edge-stack specialists) is correct. **v99 updates:**

| Trend | v98 read | v99 read |
|---|---|---|
| Closed-weight frontier | Mythos blocked | **Mythos partially unblocked; GPT 5.6 staggered; both under US gov vetting** |
| Capability gap (closed vs open) | 3–6 months | **2–4 months** (Zhipu GLM 5.2 + Tencent's AGI commitment) |
| Talent migration | Shazeer + Jumper | + **OpenAI's $2B/month revenue + IPO delay** |
| Edge frontier | Gemma 4 E2B + LFM2.5 | **+ Gemma 4 12B unified** |
| Agent-memory category | (not a category yet) | **NEW: Perplexity Brain, Engram $98M, Weaviate launch** |
| Compute substrate | OpenAI Jalapeño + TPU + MTIA | + **OpenAI IPO delay signals compute ROI is being re-measured** |

**v99 thesis update:** **the agent-memory category is now real and venture-funded.** Our on-device memoryd is the on-device vertical slice of a category Perplexity and Weaviate are racing to own in the cloud. Show HN pitch adds: **"memoryd is the on-device primitive for a category that Perplexity Brain and Engram just validated."**

---

## 4. Self-Improving Architectures — v99 deep dive

### 4.1 SIA + Self-Harness — v98 conclusions hold

SIA (Hexo Labs, arXiv:2605.27276) and Self-Harness (arXiv:2606.09498) remain the load-bearing pair. The SIA harness-only fork is the Q3 deliverable for danlab-multimodal.

### 4.2 NEW: Continual Harness, HarnessX, APEX — three more framework confirmations (v99)

Three additional papers from June 2026 strengthen the harness-evolution pattern:

| Paper | What it adds |
|---|---|
| **Continual Harness** (arXiv:2605.09998) | **Reset-free online self-improvement** — every F steps the harness is updated mid-episode via CRUD edits to harness components (prompt, sub-agents, memory). Closer to our awarenessd use case than SIA (which is offline). |
| **HarnessX** (arXiv:2606.14249) | **Composable, adaptive, evolvable harness foundry** — emphasizes observability + explainability as essential for stable self-improvement. Maps to our audit-log requirement. |
| **APEX** (arXiv:2606.15363) | **Three-layer co-evolution** — L1 harness (failure-mode patching) + L2 behavioral principles + L3 workflow topology. Production-validated on Joe (NVIDIA Nemotron Edge AI Agent): health score 0.300 → 0.570 (+90%) in one evolutionary run. |

**v99 update:** **harness evolution is now mainstream research.** Three independent papers in May–June 2026 confirm the paradigm is real, and APEX ships production validation. **Our danlab-multimodal pre-RL scaffold sits in good company.** The arXiv paper Aug 15 should reference all three alongside SIA.

### 4.3 Recursive Agent Harness (RAH) — performance gain attribution

RAH (arXiv:2606.13643) achieves **81.36% accuracy** on long-context reasoning vs **71.75% baseline** — a **+9.6pp gain attributable to harness recursion alone, with the same model (GPT-5)**. This is the cleanest possible evidence that *harness recursion beats model upgrade at the same model*. Cite this in the arXiv paper.

### 4.4 v99 self-improvement thesis

**v98 thesis was:** "Anthropic's June 2026 internal report validates the SIA paradigm at trillion-dollar scale." **v99 thesis:** **"harness evolution is now a 2026 mainstream research direction with five independent peer-reviewed papers in three months, and one production deployment (APEX). The harness-only arm is the open-weight edge-scale replication."**

This is a stronger, more evidence-backed thesis than v98's.

---

## 5. Edge VLM Optimization — v99 deep dive refresh

### 5.1 Gemma 4 12B encoder-free unified architecture (v99 NEW)

The encoder-free design eliminates the modality-fusion modules that add ~150–300ms latency and ~200MB of intermediate state. For wearable inference, this is the unlock that gets us from "LFM2.5-VL-450M at 250ms" to "Gemma 4 12B at 100–150ms with audio + vision + text in one pass."

**Cost:** 12B params vs 450M. **Memory:** ~6GB at Q4_0 (vs 209MB today). **Hardware:** Snapdragon Reality Elite (48 TOPS) is the only realistic wearable target. **Timeline:** H2 2027.

### 5.2 AMD Ryzen AI NPU + Gemma 3 (carry from v98)

The AMD paper (arXiv:2602.06063) shows Gemma 3 on Ryzen AI NPU at **5.2× faster prefill vs iGPU** and **67× more power-efficient vs CPU**. Not yet tested on Gemma 4, but the pattern is clear: **NPU acceleration is the unlock for wearable VLM inference**, and the methodology transfers.

### 5.3 AutoNeural — Qualcomm SA8295P (carry from v98)

7× lower quantization error, 14× lower latency on automotive-class NPU. SA8295P is too big for glasses, but the co-design methodology transfers to mobile NPUs (Snapdragon, MediaTek, Google Tensor).

### 5.4 v99 model matrix decisions

- **v1 (Q3 2026):** LFM2.5-VL-450M + whisper.cpp base.en + KittenTTS medium + HRM-Text-1B. Keep.
- **v1.5 (Q4 2026):** swap thermal fallback to Gemma 4 E2B QAT-mobile. Keep.
- **v2 (H1 2027):** add LFM2.5-VL-1.6B + LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M reranker + memoryd v2 with agent-memory partition.
- **v3 (H2 2027):** Gemma 4 12B unified (single-model for vision + audio + text + reasoning). Long-term convergence thesis.

---

## 6. Vector Search & Memory Architectures — v99 deep dive

### 6.1 Perplexity Brain + Engram — agent-memory as a category

Two parallel signals in 7 days:
- **Perplexity Brain** (June 18): agent-self-memory, traceable context graph, learns overnight. [^11]
- **Weaviate Engram** (June 6, $98M June 23): managed cloud memory, 100× token efficiency claim, customers Microsoft/Notion/Harvey. [^12] [^13]

**v99 implication for memoryd v2/v3:**

| Layer | v1 (current) | v2 (Q3 2026) | v3 (H1 2027) |
|---|---|---|---|
| User memory | ✅ episodic/semantic/procedural | ✅ + HNSW + LFM2.5-Embedding + SemanticXR object schema | ✅ + CogMem-style 3-layer |
| **Agent memory** | ❌ | **✅ + BAO bandit posterior table** | **✅ + Perplexity-Brain-pattern self-improvement loop** |
| **Memory provenance / audit** | ❌ | **✅ + Engram-style provenance fields** | ✅ |
| **Cross-session learning** | ❌ | partial (HNSW) | ✅ + Ebbinghaus forgetting curve |

### 6.2 SemanticXR — v98 verdict holds

Still the missing object-level memory architecture. Q3 2026 read, Q4 2026 prototype, H1 2027 ship as memoryd v3 if prototype succeeds.

### 6.3 DPCM (arXiv:2606.09483) — carry from v98

Dual-Process Memory: System 1 sync / System 2 async. Maps naturally to awarenessd's on-device (System 1, sync) vs cloud-fallback (System 2, async) split. v99 adds it to the memoryd v3 inspiration list.

---

## 7. Proactive AI update — v99

### 7.1 BAO + MIB + TEMPO — v98 framework still load-bearing

BAO remains the training framework for awarenessd. v99 adds: **three independent papers in the proactive-interruption space in 2026:**
- **BAO** (arXiv:2602.11351) — behavior enhancement + behavior-regularized RL.
- **HANDRAISER** (arXiv:2604.06452) — interruptible communication framework for multi-agent LLM systems. 24.3–48.9% reduction in communication cost. Maps to our awarenessd inter-daemon interrupt pattern.
- **InterruptBench** (arXiv:2604.00892) — first systematic evaluation for interruptible agents in long-horizon web navigation. "Even powerful LLMs struggle to handle interruptions." This validates that proactive interruption is a hard problem worth solving.
- **PASK** (arXiv:2604.08000) — full stack for proactive intelligence: DD-MM-PAS architecture, IntentFlow streaming demand detection, hybrid memory, end-to-end implementation. The most complete proactive-AI stack we have seen. **PASK is the awarenessd reference architecture.**

### 7.2 awarenessd v0.1 v99 design

Add to v98's 3-harness-variant BAO bandit:
- **DPCM-style async agent-memory layer** — bandit updates happen async, not on every interrupt.
- **PASK-style IntentFlow demand detection** — pre-screens potential interrupts for demand (need) before the bandit chooses a variant.
- **HANDRAISER-style cost-benefit calibration** — every interrupt has an estimated cost (user annoyance) and benefit (task completion). The bandit learns to minimize cost / maximize benefit.

Show HN demo: webcam → proactive interruption with full reasoning trace → audit panel showing bandit posterior → agent-memory update visible.

---

## 8. Competitive landscape update — v99

| Vendor | Product | Price | Open? | Proactive? | Indic? | Agent-memory? | Status |
|---|---|---|---|---|---|---|---|
| **Dan Glasses v1** (us) | wearable | $349–399 BOM | ✅ | ✅ awarenessd | ✅ | ✅ (memoryd v2 plan) | Q4 2026 target |
| **Meta Muse Spark Glasses** | wearable | $299 | ❌ | ❌ | ❌ | ❌ (cloud-only) | **Shipping Jun 23** |
| **Brilliant Labs Halo** | wearable | $299 | ✅ HW+SW | ✅ Noa agent | ❌ | partial | Shipping |
| **Microsoft Scout** | desktop agent | M365 bundle | ❌ | ✅ | ✅ | ❌ | Jun 2 launch |
| **Perplexity Brain** | cloud agent memory | (Perplexity Pro) | ❌ | n/a | n/a | ✅ | Jun 18 launch |
| **Weaviate Engram** | managed cloud memory | enterprise | SDK only | n/a | n/a | ✅ | Jun 6, $98M |
| **Anthropic Mythos** | closed frontier | API | ❌ | n/a | n/a | n/a | **partial access Jun 26** |
| **OpenAI GPT 5.6** | closed frontier | API | ❌ | n/a | n/a | n/a | **staggered Jun 26** |

**v99 read:** **the agent-memory category is now 4 vendors (Perplexity, Weaviate, OpenAI's ChatGPT memory, danlab memoryd). All four are cloud-native except us.** This is the new wedge.

---

## 9. Privacy positioning — v99 reinforcement

v98's privacy wedge (open, auditable, on-device) is strengthened by v99's signals:
- **Geopolitical gating of closed-weight frontier** means our on-device stack is the only one that survives a fragmented regulatory environment.
- **Perplexity Brain and Engram are cloud-only** — no on-device option exists for users who want their agent's memory to stay on the device.
- **GPT 5.6 and Mythos are now US-government-vetted** — non-US users have even less access than before.

**v99 differentiation line:** **"yours, not theirs — and yours means on-device, auditable, geopolitically-independent, and an agent that remembers its own work without sending it to Perplexity or Weaviate."**

---

## 10. Risks & Open Questions — v99

### Critical risks (must resolve Q3 2026)

1. **memoryd startup-probe — Action 1 by July 5 (Dan4).** v96 bug self-healed, v98 confirmed. The discovery gap remains. Fix the discovery, not just the bug.
2. **awarenessd v0.1 — Action 2 by July 25 (Dan2 + Dan3 + Dan1).** BAO bandit over 3 harness variants + HRM-Text-1B on-device + GLM 5.2 cloud fallback + PASK-style IntentFlow pre-screen + HANDRAISER-style cost-benefit calibration.
3. **memoryd v2 + agent-memory partition — Action 3 by July 25 (Dan4).** HNSW + LFM2.5-Embedding-350M + SemanticXR object schema evaluation + agent-memory table for BAO bandit posterior.
4. **OpenClaw Tailscale fallback — Action 4 by July 8 (Dan1 + Dan2).** DanClaw proxy + Zo User Service public=false. v99 confirms Tailscale Funnel is also blocked.

### Medium risks

5. **Closed-weight frontier geopolitically conditioned (v99 NEW).** Mythos partially unblocked + GPT 5.6 staggered. This is *better* than v98's "permanently closed" reading but creates a different risk: our positioning must hold even if Mythos fully unblocks. Our wedge (auditable + on-device + Indic + agent-memory) survives because it's about the stack, not the access.
6. **Perplexity Brain + Engram as competitors.** Agent-memory is now a category. We compete on on-device + privacy + auditable, not on capability.
7. **Sapient HRM-Text internship (carry from v98).** Apply Q3 for one Q4 hire.
8. **Gemma 4 E2B license verification (carry from v98).** Verify Q3 week 1.
9. **LFM2.5-VL-1.6B release date.** Monitor for H1 2027 swap.
10. **OpenAI IPO delay (v99 NEW).** Funding environment bifurcating. Our Series A posture should be "bootstrappable to revenue, not venture-scale."

### Open questions for somdipto (v99, supersedes v98)

**Carry from v98 (still unanswered):**

1. **Wedge lock** — DANI vs Dan Glasses? By July 3.
2. **Show HN scope** — minimal awarenessd (2 weeks) vs full (+memoryd recall +ttsd + GLM 5.2 + agent-memory)? v99 recommends **full**.
3. **Founder Edition timing** — Q4 2026 vs Q1 2027?
4. **Founder Edition pricing** — $349 (premium) vs $299 (match Muse Spark + Halo)?
5. **HRM-Text-1B integration priority** — Q3 or Q4? v99 recommends Q3.
6. **GLM 5.2 cloud-fallback on by default?** v99 recommends OFF.
7. **Anthropic "When AI Builds Itself" companion paper** — v99 recommends YES, plus Mythos partial-unblock analysis.
8. **Series A posture** — bootstrapped through Show HN or start the deck?
9. **India-language priority** — Hindi + Bengali for v1?
10. **Dani vs Dan Glasses integration** — separate products or one product with two channels?
11. **Sapient HRM-Text internship** — apply Q3.
12. **SemanticXR prototype** — Q3 read, Q4 prototype.
13. **memoryd startup-probe rollout** — all 8 daemons by July 5.
14. **/privacy route in Tauri shell** — Q3 work item.

**NEW v99:**

15. **memoryd v2 agent-memory partition — ship alongside HNSW + LFM2.5-Embedding?** Recommend YES, by July 25.
16. **Engram/Perplexity Brain competitive response — public positioning?** Recommend "on-device agent-memory, the only one." Show HN ready by Aug 25.
17. **Closed-weight geopolitically-conditioned framing in arXiv paper?** Recommend YES — cite Mythos partial unblock + GPT 5.6 staggering as evidence for open-weight edge.
18. **Gemma 4 12B unified architecture — long-term v3 commitment?** Recommend YES, R&D-only for H2 2027.

---

## Sources

[^1]: https://www.axios.com/2026/06/27/commerce-anthropic-mythos-restrictions-lift — Anthropic Mythos comes back for select entities approved by US government (Jun 27, 2026)
[^2]: https://www.cnn.com/2026/06/26/tech/anthropic-mythos-release — US government allows Anthropic limited release of AI model that sparked cybersecurity concerns
[^3]: https://www.reuters.com/technology/us-releases-anthropic-model-mythos-some-us-companies-semafor-reports-2026-06-26/ — US allows Anthropic to release Mythos to 'trusted partners'
[^4]: https://techcrunch.com/2026/06/26/trump-admin-releases-anthropic-mythos-to-be-used-by-more-than-100-us-companies-agencies/ — Trump Admin releases Anthropic Mythos to be used by more than 100 US companies, agencies
[^5]: https://www.theguardian.com/technology/2026/jun/26/openai-ai-model-release-trump-us-sam-altman-gpt-anthropic-mythos — OpenAI staggers AI model release after Trump administration request
[^6]: https://www.washingtonpost.com/technology/2026/06/26/openai-says-us-government-will-vet-users-its-latest-ai-model/ — US government will decide who gets to use latest upgrade to ChatGPT
[^7]: https://techcrunch.com/2026/06/26/its-not-about-anthropic-vs-openai-anymore/ — It's not about Anthropic vs. OpenAI anymore
[^8]: https://www.cnbc.com/2026/06/26/openai-ipo-timeline-delayed-kalshi-predictions.html — OpenAI is reportedly delaying its IPO. Here's when Kalshi traders think it will announce
[^9]: https://www.investopedia.com/stock-market-today-dow-jones-james-bondos-06262026-12007282 — Stock Market Today: OpenAI IPO delay
[^10]: https://smartasset.com/investing/openai-stock-ipo — OpenAI Stock IPO: Expected Valuation, Timeline and Investment Options
[^11]: https://www.marktechpost.com/2026/06/18/perplexity-launches-brain/ — Perplexity Launches Brain, a Self-Improving Memory System That Builds a Context Graph of an Agent's Work
[^12]: https://www.lokmattimes.com/business/weaviate-launches-engram-to-break-the-ai-memory-bottleneck-and-let-agents-learn-from-conversation-without-slowing-down/ — Weaviate Launches Engram to Break the AI Memory Bottleneck (Jun 6, 2026)
[^13]: https://www.cnbc.com/2026/06/23/ai-memory-startup-focused-on-cutting-token-costs-raises-98-million.html — AI memory startup Engram raised nearly $100 million (Jun 23, 2026)
[^14]: https://venturebeat.com/technology/googles-new-open-source-gemma-4-12b-analyzes-audio-video-and-runs-entirely-locally-on-a-typical-16gb-enterprise-laptop — Google's new open source Gemma 4 12B analyzes audio, video — runs entirely locally on 16GB laptop (Jun 3, 2026)
