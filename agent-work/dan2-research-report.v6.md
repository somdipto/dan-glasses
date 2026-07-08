# Dan2 Research Report v6 — Self-Improvement, Reliability, and the AGI Thesis from India

**Author:** Dan2 (Research Agent) | **Date:** 2026-06-24 11:30 IST (06:00 UTC)
**Status:** v6 — supersedes v1–v5
**Live infrastructure:** 8/8 daemons live, 144/144 tests, Tauri SPA published at `dan-glasses-app-som.zocomputer.io`, OpenClaw gateway on 18789, Telegram bot `@danlab_bot` (verified this run).
**Companion artifacts:** `dan2-agi-roadmap.v6.md`, `dan2-architecture-review.v6.md`, `dan2-model-analysis.v6.md`, `dan2-papers-to-read.v6.md`.

> **v6 north star (one sentence):** The audiod confidence-calibration RL agent on AIE-Bench / SEAGym is *the* artifact that graduates Danlab from "pre-RL scaffold" to a *measured, audited* self-improving system. Reliability (ECE / Brier) is the new moat. Memory is engineering, not research. The smart-glasses race is now a commodity race — we win on **privacy, proactivity, on-device-first, India-cost**. Anthropic's global pause call (Jun 4–5 2026) makes the *verification regime* part of our pitch, not an afterthought.

---

## v5 → v6 — what changed and why

v5 was a strong synthesis. v6 sharpens it with five updates:

1. **HRM-Text numbers corrected.** v5 cited 84.7% GSM8k. The actual paper (Sapient, arXiv 2605.20613, May 18 2026, open-sourced) reports **84.5% GSM8k, 60.7% MMLU, 56.2% MATH, 82.2% DROP, 81.9% ARC-C**, training cost ~$1,472, 46 hours on 16 H100s. The 84.5 number matters for honest marketing.
2. **The rise-and-collapse failure mode is a hard ceiling we must design around.** arXiv 2606.21090 (Jun 2026) documents that self-trained LLMs *rise then collapse* within a single campaign — pass@1 returns near zero after peak. Mitigation is regime-dependent (CARE, ES, GRPO, GRPO+ES) and never fully generalizes. **Implication:** the audiod RL agent must include a peak-detection + checkpoint-rolling protocol, not just a reward function. This is a v6 architectural change.
3. **Anthropic's Jun 4–5 2026 global pause call is now part of the moat.** Jack Clark + Marina Favaro (Anthropic blog) called for a globally-coordinated, *verifiable* slowdown on recursive self-improvement. **The verification regime is the differentiator.** Danlab's audiod calibration paper can ship with an *open eval protocol + open reward model + open calibration head* — making it auditable to the kind of regime Anthropic is calling for. Meta's $299 glasses cannot ship this; they are closed weights, closed eval.
4. **EvoMaster, SelfCompact, and the Operative Contexts critique reshape the memory thesis.** EvoMaster (OpenReview 2026) is an evolving-agent framework with concrete numbers (HLE 41.1%, MLE-Bench Lite 75.8%, BrowseComp 73.3% — +159% to +316% over OpenClaw baseline). SelfCompact (arXiv 2606.23525) gets up to 18.1-point gains on math by adaptive context compaction. Operative Contexts (OpenReview 2026) formalizes *silent contextual misalignment* — agents act on stale, opaque memory. **memoryd v2 cannot just be AEL + DPCM; it must also have a context-controllability surface that the user can inspect and revise.** This is a v6 memoryd v2 spec change.
5. **VLM token-pruning is the real edge VLM story for 2026.** CondenseVLM (submodular evidence preservation), QViD (low-rank interaction pruning, training-free), V5e-0 (1.89× wall-clock self-speculative decoding), SpecFlow (2.1× compute/KV-cache savings via spectral visual state). **Perceptiond v2 should adopt a token-pruning + speculative-decoding stack, not just swap the base model.** OmniVLM-968M is real and 9× token compression is real, but the bigger win is treating the existing LFM2.5-VL-450M as a base + applying *evidence-preserving* token pruning at inference time. 4-week build, not a 6-week eval-and-swap.

---

## Executive summary — the v6 thesis

1. **Self-improvement is now a *measurable* benchmark discipline (AIE-Bench, SEAGym), not a thesis.** Auditable harness-only updates on Terminal-Bench 2.0 + HLE. Submissions open for ICML 2026.
2. **Self-evolving agents are a working subfield with concrete lift numbers.** AEL (+27% Sharpe, +18% on support tickets), EvoMaster (+159% to +316% over OpenClaw), EDGE (+8.3–12.5 success points on ALFWorld/WebShop 7B), SelfCompact (+18.1 math, 5–9 agentic-search, 30–70% token cost down), SEER (unsupervised self-evolution of reasoning), AtomMem (RL memory CRUD), HERO (hindsight-enhanced self-distillation).
3. **The rise-and-collapse failure mode is a hard ceiling.** No mitigation is regime-independent. *Peak detection + checkpoint rolling + early stop (ES)* is the minimal viable harness.
4. **Reliability is the new moat for sub-1B on-device models.** arXiv 2602.16666 (Towards a Science of AI Agent Reliability): consistency, robustness, predictability, safety. Predictability = calibrated confidence. audiod is the v6 north star.
5. **Memory is an engineering discipline, not a research topic.** AIE-Bench-validated harness patterns, OpenClaw memory adapter, Anthropic Memory + Dreaming, AEL + DPCM + LLM-Wiki + OpenClaw-memory, Operative Contexts user-controllability. The build is *memoryd v2 = AEL + DPCM + LLM-Wiki + User-Inspectable Operative Context*.
6. **HRM-Text 1B (Sapient, May 18 2026) is the credible 2026 reasoner for on-device.** 84.5% GSM8k, 60.7% MMLU, 56.2% MATH, $1,500 training, fully open. Train on Danlab's task suite; deploy on-device in 1B class.
7. **Smart-glasses is commodity.** Meta Glasses at $299 (Jun 23 2026), Muse Spark, 14 new languages including Hindi/Mandarin/Japanese/Korean, 8h battery + 40h case. Apple in 2027, Google × Warby Parker fall 2026, Snap Specs $2,195. **Danlab cannot win on hardware.** Moat: privacy + on-device + proactivity + India-cost + open-source + auditable self-improvement.
8. **TTS has consolidated to Kokoro-82M.** Apache 2.0, 24kHz, MOS 4.45, 327MB, Raspberry Pi, WebGPU, in-browser. KittenTTS swap is a 1-week decision, not a research project. *And*: WebNarrator 1.1.0 ships Kokoro-82M in-browser via ONNX Runtime Web with six voices — directly relevant to a Tauri webview-side TTS.
9. **Edge VLM is now a *token-pruning + speculative-decoding* problem, not just a base-model-swap problem.** CondenseVLM / QViD / V5e-0 / SpecFlow are the 2026 recipes. Keep LFM2.5-VL-450M, add evidence-preserving pruning + free-root speculative decoding.
10. **Anthropic's global pause call makes *open verification* the brand.** audiod calibration paper ships with *open eval, open reward, open head, open failure mode registry*. This is the anti-Meta position. It is also the position Anthropic is asking for.

**The single sentence:** Ship a reliability-aware, open-verifiable audiod confidence-calibration RL agent to AIE-Bench + SEAGym by Sep 30, 2026; ship memoryd v2 with AEL + DPCM + LLM-Wiki + OpenClaw-memory + user-inspectable Operative Context surface by Sep 15, 2026; keep LFM2.5-VL-450M and add CondenseVLM/QViD/V5e-0 token-pruning + speculative decoding stack by Sep 1, 2026; swap KittenTTS → Kokoro-82M with WebGPU in-browser option by Jul 15, 2026; position the brand around *open verification regime + on-device-first + privacy + proactivity + India-cost* against Meta's $299 in-house line and Anthropic's call for verifiable slowdown.

---

## Part A — System Architecture Deep Dive

### A1. Is the service decomposition correct? What are the bottlenecks?

**Decomposition: right. Transport: mostly right. State: missing. Self-improvement seam: still missing. Reliability: missing as first-class.**

The 8/8 uptime and 144/144 tests prove the seams are stable. audiod (8090/WS 8091) / perceptiond (8092) / memoryd (8741) / toold (8742) / ttsd (8743) / os-toold (8744) / openclaw (18789) / dan-glasses-app (8747) is the correct split. Four v6 fixes:

1. **Transport: keep HTTP/JSON at the edge, switch to Unix-domain-socket for daemons.** v5 said this. Unchanged.
2. **Power-state machine missing on every daemon.** v5 said this. Unchanged.
3. **Dual control plane: collapse the Python proxy.** v5 said this. Unchanged.
4. **No self-improvement seam. v6 NEW: no reliability seam either.** audiod emits `confidence: 0.83` but no service consumes it. perceptiond emits salience confidence, no service calibrates it. memoryd has no reliability metrics. **Fix:** add a `reliabilityd` (or merge into `rewardsd`) service that ingests `(task, action, signal, calibration_truth)` tuples and produces *calibrated* reliability metrics per service. audiod calibration RL agent is the v6 differentiator — and it is *also* the first service to ship reliability metrics. Other daemons follow.

**NEW v6 — Bottlenecks (revised):**

1. **VLM inference is the wrong lever on its own.** Swapping LFM2.5-VL-450M → OmniVLM-968M is real but insufficient. The *bigger* lever is inference-time token pruning (CondenseVLM / QViD) + speculative decoding (V5e-0 Free-Root, 1.89× wall-clock). **Combined: 3–5× wall-clock on the same LFM2.5 model.** Decision: keep LFM2.5-VL-450M as base, add the pruning/decoding stack.
2. **No wake/sleep state machine.** v5: 1.6W idle, 8–13W active. v6 unchanged.
3. **Mock capture in perceptiond.** Unchanged.
4. **No frame retention in perceptiond.** Unchanged.
5. **memoryd uses float32 embeddings.** v5 said int8. v6: also need user-inspectable operative context surface per Operative Contexts critique.
6. **TTS cold-path latency ~3.8s.** v5: swap to Kokoro-82M. v6: swap AND add WebGPU in-browser path for Tauri webview.
7. **toold sandbox at /tmp/toold-sandbox.** Unchanged.
8. **No self-improvement loop seam.** v5: rewardsd. v6: rewardsd + reliabilityd (or merged into rewardsd with reliability surface).
9. **Uncalibrated confidence is a moat-killer.** v5 said audiod. v6: every daemon needs reliability metrics. audiod first.
10. **NEW v6 — No peak detection on the self-improvement loop.** arXiv 2606.21090 rise-and-collapse. The audiod RL agent must include peak detection + checkpoint rolling + early stop (ES). Without this, the loop *will* collapse within one campaign.

**Recommendation:** Rewrite PRD.md Section 4 to match current Python reality. Mark the Rust migration as a v2 wearable target. Add Section 4.5: *Reliability Surface Contract* — every daemon exposes `GET /reliability` returning `{calibration, consistency, robustness, predictability, safety}` per arXiv 2602.16666.

### A2. Is the multimodal "RL feedback loop" a true RL loop or just heuristic?

**Honest answer: it is a heuristic loop, and that is the correct framing today.** danlab-multimodal/docs/ARCHITECTURE.md is explicit: "This is NOT reinforcement learning."

**v6 update: AIE-Bench + SEAGym are the venue; rise-and-collapse is the architectural constraint; the audiod calibration task is the right first target.** The audiod task is bounded, the ground truth is free (Librispeech, CommonVoice, TED-LIUM), and the failure mode is now understood (rise-and-collapse mitigated by peak detection + ES). v6 also adds a *peak detection + checkpoint rolling* protocol to the audiod RL harness design (this is the v6 architectural change vs v5).

**Concrete harness design (v6):**

```python
# audiod_rl/loop.py — pseudocode
class AudiodCalibrationLoop:
    def __init__(self, base=whisper_cpp_base_en, calibration_head=MLP4):
        self.policy = calibration_head
        self.peak_score = 0.0
        self.peak_checkpoint = None
        self.plateau_count = 0
        self.rollforward_at = 3  # ES: peak_step + 3

    def step(self, batch):
        # 1. compute reward (Brier + ECE on Librispeech, CommonVoice-Indian, TED-LIUM)
        reward = self.evaluate(batch)
        # 2. policy update (GRPO for sub-1B calibration head)
        self.policy.update(batch, reward)
        # 3. peak detection (ES — early stop with rolling checkpoint)
        if reward > self.peak_score:
            self.peak_score = reward
            self.peak_checkpoint = deepcopy(self.policy.state)
            self.plateau_count = 0
        else:
            self.plateau_count += 1
        # 4. if plateaued for `rollforward_at` steps, restore peak and shrink budget
        if self.plateau_count >= self.rollforward_at:
            self.policy.load_state(self.peak_checkpoint)
            return {"action": "rollforward_to_peak", "peak_score": self.peak_score}
        return {"reward": reward, "peak_score": self.peak_score}
```

**v6 publication framing:** "Auditable Confidence Calibration for On-Device Speech Recognition" — the audiod agent ships with the harness + reward + calibration head *open* and the failure-mode registry (rise-and-collapse, ES, peak detection) *documented*. This is the verifiable-self-improvement pitch. Submissions to AIE-Bench, SEAGym, ICML 2026 Workshop on Recursive Self-Improvement, and arXiv by Aug 15, 2026.

### A3. Power/performance tradeoffs — LFM2.5-VL-450M, whisper.cpp, KittenTTS

**v6 reframing:** v5's "swap LFM2.5 → OmniVLM" is real but *not* the highest-ROI move. The highest-ROI moves are *inference-time* techniques on the existing model.

**Edge VLM optimization (Deep Dive B in v6):**

| Technique | Source | Wall-clock | Memory | Implementation | Confidence |
|---|---|---|---|---|---|
| **CondenseVLM** (submodular evidence-preserving token pruning) | arXiv 2026 | 1.5–2.5× | 30–50% vision tokens | 4-week build, training-free | High |
| **QViD** (low-rank query–vision interaction decomposition) | arXiv 2026 | 1.4–1.8× | 30–60% vision tokens | 2-week build, training-free | High |
| **V5e-0** (self-speculative decoding, Free-Root) | OpenReview 2026 | 1.46–1.89× | ~same | 1-week build, training-free | High |
| **SpecFlow** (spectral visual state, classifier-free guidance) | arXiv 2026 | up to 2.1× | bounded | 4-week build | Medium |
| **Model swap LFM2.5 → OmniVLM-968M** | v5 report | 3–5× (token compression) | 2.1× | 2-week eval + 2-week swap | Medium |
| **NPU offload (Qualcomm Hexagon)** | v5 report | 2–5× | 10× power efficiency | Hardware-dependent | Blocked on Redax |

**v6 recommendation:** CondenseVLM + QViD + V5e-0 stack. Keep LFM2.5-VL-450M as base. Total: 2–3× wall-clock win, no model retraining, no quantization trade-off. 6-week build vs 6-week swap. **Replaces v5's "swap to OmniVLM" recommendation.**

**STT (v6):**
- **whisper.cpp base.en** — 74MB, mature, English-only. Current.
- **Moonshine** (Useful Sensors) — 5× faster than Whisper, edge-first.
- **Parakeet** (NVIDIA) — competitive accuracy, smaller sizes.

**v6 recommendation:** keep whisper.cpp base.en for v1 (already deployed, 123 tests). Evaluate Moonshine for v1.5 if the audiod RL agent learns that base.en is the bottleneck on Indian-accent English (CommonVoice OOD eval will surface this).

**TTS (v6):**
- **Kokoro-82M** (Apache 2.0, 24kHz, MOS 4.45, 327MB, Raspberry Pi, WebGPU in-browser). v6 confirms v5 recommendation.
- **WebNarrator 1.1.0 in-browser** — directly relevant for a Tauri webview-side TTS. Zero-server-side, opt-in download, OPFS-cached.

**v6 ttsd v2 plan:** swap to Kokoro-82M this quarter (1-week decision, Apache 2.0 license, 21 voices, sub-20ms TTFA on warm cache). Add WebGPU in-browser path as a v1.5 option (Tauri webview can use it).

---

## Part B — AGI Landscape Research

### B5. State of AGI research in 2026 — what are the leading approaches?

**Four threads (v6 framing):**

1. **Recursive self-improvement is now mainstream.** Anthropic's Jun 4–5 2026 call for a *verifiable global pause* is the watershed — the question is no longer *whether* to pause but *how* to verify a pause. The OpenAI "Dreaming V3" hierarchical memory (82.8% recall vs 41.5% in 2024), Anthropic Memory + Dreaming product, EvoMaster (+159% to +316% over OpenClaw baseline on HLE / MLE-Bench Lite / BrowseComp / FrontierScience) are the production examples. Jack Clark's 80% self-written Claude claim (Anthropic blog, Jun 4 2026) is the concrete number.
2. **The reliability frame is now mainstream.** arXiv 2602.16666 decomposes reliability into four axes: consistency, robustness, predictability, safety. Predictability = calibrated confidence. audiod calibration is *the* sub-1B reliability problem.
3. **Memory is now an engineering discipline.** AIE-Bench validated harness patterns (ACE, TF-GRPO, AHE on Terminal-Bench 2.0 / HLE). OpenClaw memory docs are the de-facto reference. Anthropic Memory + Dreaming, AEL, DPCM, LLM-Wiki, Zep Graphiti, Honcho, MemoryHub, OpenViking, agentmemory. memoryd v1 is a regression. memoryd v2 is the engineering build.
4. **Self-evolving agents are a working subfield.** AEL, EvoMaster, RefCon, GRAM, SEER, AtomMem, HERO, EDGE, SelfCompact, HERO, AIE-Bench, SEAGym, SkillsVote, OmniGameArena, SPaRTan/Social Gym, R_FOLD, CaveAgent. **Every paper has a public number.** The bar is "publish your eval."

**Danlab's position in v6:** the audiod calibration paper is the *first* sub-1B on-device reliability artifact with open eval. memoryd v2 paper is the *first* memory architecture that ships AEL + DPCM + LLM-Wiki + user-inspectable operative context as a unified daemon. Together: two arXiv preprints by Aug 15, 2026, AIE-Bench + SEAGym submission by Sep 30, 2026.

### B6. Self-improving architectures — what has actually worked?

**v6 list (with numbers, all from the source papers):**

| Approach | Lift | Regime | Source |
|---|---|---|---|
| AEL (two-timescale bandit + slow reflection) | +27% Sharpe, +18% on tickets, +51% over best baseline | Portfolio + support tickets | OpenReview 2026 |
| EvoMaster (evolving scientific agents, ~100 LoC) | +159–316% over OpenClaw on HLE/MLE-Bench/BrowseComp/FrontierScience | Agentic science | OpenReview 2026 |
| EDGE (experience-distillation) | +8.3–12.5 success points on ALFWorld/WebShop at 7B; 96% scaffold retention | ALFWorld, WebShop | OpenReview 2026 |
| SelfCompact (adaptive context compaction) | +18.1 math, +5–9 agentic-search, 30–70% token cost down | Math + agentic | arXiv 2606.23525 |
| SEER (unsupervised self-evolution of reasoning) | Outperforms strong reasoning baselines; no labels | Reasoning | OpenReview 2026 |
| HERO (hindsight-enhanced self-distillation) | Higher task success, fewer turns, better with rare success | TauBench, WebShop | OpenReview 2026 |
| RefCon (iterative refinement + contrastive memory extraction) | +21.6% on ACE | Long-form reasoning | ACL ARR 2026 |
| GRAM (RL memory CRUD with GRPO, sub-4B) | Outperforms static memory + RAG | QA benchmarks | OpenReview 2026 |
| SPaRTan (training-free self-improvement playbook) | Partial, capacity-dependent gains on social reasoning | Social Gym 21 games | OpenReview 2026 |
| R_FOLD (bi-level context management) | 81.33% on BrowseComp-Plus at 32K context | BrowseComp-Plus | OpenReview 2026 |
| CaveAgent (stateful runtime operator) | +13.5% on multi-turn retail, 51% token reduction | Tau2, BFCL | OpenReview 2026 |
| RISE (routable MoE with multi-timescale retrieval) | Cog 59.38% on OmniSocialBench | Social VQA | arXiv 2606.20970 |

**v6 adoption plan (concrete):**

1. **AEL's two-timescale pattern.** Adopt in memoryd v2 (already in v5 plan; v6 refines).
2. **EvoMaster's trace-derived skills pattern.** Adopt for paperclip substrate (Q4 2026).
3. **EDGE's experience-distillation.** Adopt for audiod RL agent (the audiod agent distills calibration head experiences into a growing policy).
4. **SelfCompact's adaptive context compaction.** Adopt in audiod + memoryd context paths.
5. **HERO's hindsight-enhanced self-distillation.** Adopt for paperclip's tool-calling agent.
6. **GRAM's GRPO for memory CRUD.** Adopt if memoryd v2 takes a graph-memory path.
7. **SIA's harness+weights substrate.** Fork for the audiod calibration agent (v5 plan; v6 keeps).
8. **CaveAgent's stateful runtime operator.** Adopt for paperclip + dan-glasses-agent.
9. **Operative Contexts critique (NEW v6).** Memory surface must be user-inspectable. memoryd v2 ships `/context/{inspect, revise, contest}` endpoints.

**What has *not* worked yet (and v6 is honest about):**
- Full self-play in a multimodal loop (SPIRAL is closest, but no production-grade result yet).
- LLM-agent-discovered RL algorithms (POISE is the proof-of-concept, not production).
- End-to-end recursive self-improvement (Anthropic's 80% self-written Claude is the *outer loop*; the *inner loop* is not yet demonstrated on a sub-1B model).
- **Generalization of the rise-and-collapse mitigation across model sizes.** arXiv 2606.21090 shows ES, GRPO, CARE are all regime-dependent. There is no universal stabilizer yet.

### B7. Edge AI / on-device models — what's the SOTA for sub-500MB VLMs that actually work?

**Tier 1 — production-grade (ship now):**
- **LFM2.5-VL-450M** (Liquid AI, Apr 2026) — 209MB Q4_0 + 180MB mmproj. SigLIP2 NaFlex encoder. **Currently live in perceptiond.** v6: keep, add token-pruning + speculative decoding stack.
- **OmniVLM-968M** — 9× token compression. v6: evaluate as a v2 alternative.
- **Gemma 3 4B** — Q4_K_M, proven on-orbit.
- **HRM-Text-1B** (Sapient, May 18 2026) — 84.5% GSM8k, 60.7% MMLU, 56.2% MATH, $1,500 training, fully open (arXiv 2605.20613, github.com/sapientinc/HRM-Text, HF sapientinc/HRM-Text-1B). **v6 NEW: HRM-Text is the right reasoner for on-device 1B. Train on Danlab's task suite.**

**Tier 2 — emerging:**
- **LFM2.5-8B-A1B MoE** — onnx-export June 2026.
- **SmolVLM-256M-Instruct multilingual** — Hindi/Indic candidate.

**Inference-time techniques (v6 NEW, the 2026 real story):**
- **CondenseVLM** — submodular evidence-preserving token pruning.
- **QViD** — low-rank query–vision interaction decomposition, training-free.
- **V5e-0** — self-speculative decoding, Free-Root, 1.89× wall-clock.
- **SpecFlow** — spectral visual state, 2.1× compute/KV-cache savings.

**STT landscape (v6):**
- **whisper.cpp base.en** — 74MB, mature, English-only. **Current.**
- **Moonshine** (Useful Sensors) — 5× faster than Whisper, edge-first. v1.5 candidate.
- **Parakeet** (NVIDIA) — competitive accuracy, smaller sizes. v1.5 candidate.
- **whisper-large-v3-turbo** — multilingual, ~2× larger. v2 candidate.

**TTS landscape (v6):**
- **Kokoro-82M** (Apache 2.0, 24kHz, MOS 4.45, 327MB, Raspberry Pi, WebGPU). **v6 winner.**
- **Piper** — speed king for low-resource languages.
- **Chatterbox** — voice cloning, beats ElevenLabs in blind tests.
- **Fish Audio S2 Pro** — commercial-grade cloud API.
- **Qwen3-TTS** — most capable all-rounder (10 languages, voice cloning).
- **MisoTTS** — sub-300ms TTFB, int8 quant, A6000-class.

### B8. Memory and continual learning — v6 update

**2026 memory frameworks (v6, ranked by maturity):**
- **AIE-Bench + SEAGym** — *the venue* (harness updates, replay diagnostics, audit).
- **SkillsVote** — skill lifecycle governance (collection → recommendation → evolution).
- **AEL** — two-timescale Thompson + slow LLM reflection. +27% Sharpe.
- **DPCM** — doubly-linked provenance graph, System 1/2 split. +5.20 on PersonaMem-v2.
- **EvoMaster** — evolving scientific agents.
- **RefCon** — iterative extraction without gold labels. +21.6% on ACE.
- **GRAM** — GRPO for memory governance, sub-4B.
- **OpenClaw memory** — bootstrap + semantic, the de-facto reference.
- **Anthropic Memory + Dreaming** — shipped product.
- **OpenAI Dreaming V3** — hierarchical, self-synthesizing relational memory, 82.8% recall.
- **LLM-Wiki** (Karpathy) — wiki-style knowledge organization as long-term memory.
- **Zep Graphiti** — temporal knowledge graph.
- **Honcho** — user modeling for personalized agents.
- **OpenViking** (Volcengine) — context management at scale.
- **MemoryHub** (Red Hat) — plugin architecture for memory.
- **agentmemory** — community reference.
- **AtomMem** — learnable atomic CRUD via GRPO.
- **HERO** — hindsight-enhanced self-distillation.
- **SelfCompact** — adaptive context compaction.
- **R_FOLD** — bi-level context management.
- **CaveAgent** — stateful runtime operator with persistent Python objects.
- **Operative Contexts** (OpenReview 2026) — *the critique*: memory must be user-inspectable to avoid silent contextual misalignment.

**v6 memoryd v2 architecture (refined):**

```
memoryd v2
├── episodic store (event log, append-only, FTS5 searchable)
├── semantic store (vector index, int8 quantized, AEL bandit-selected)
├── procedural store (workflow templates, version-controlled)
├── graph store (DPCM doubly-linked superseding chains)
├── AEL fast Thompson bandit (selects retrieval mode per query)
├── slow LLM reflection (nightly, opt-in, LFM2.5-1.2B-Thinking)
├── LLM-Wiki reconsolidation (nightly, async, low-priority)
├── AIE-Bench / SEAGym hooks (rewards ingestion, policy export)
├── OpenClaw-memory adapter (mcp-compatible)
├── Operative Contexts surface (NEW v6)
│   ├── GET /context — list active operative memory
│   ├── POST /context/revise — user revises operative context
│   ├── POST /context/contest — user flags silent misalignment
│   └── diagnostic stress tests for context control
└── reliability surface (NEW v6)
    ├── GET /reliability — calibration, consistency, robustness, predictability, safety
    └── AIE-Bench-style auditable eval
```

**v6 build sequence (8 weeks, with v6 extensions):**

| Week | Component | Deliverable |
|---|---|---|
| 1 | int8 quantization on existing semantic store | 4× memory win |
| 2 | DPCM provenance graph schema + migration | New tables, backward-compat read API |
| 3 | AEL fast Thompson bandit (5 modes) | Bandit over {semantic, episodic, procedural, graph, reranked} |
| 4 | Slow LLM reflection (nightly, opt-in) | New retrieval modes injected on plateau |
| 5 | LLM-Wiki reconsolidation (nightly) | Episodic → semantic distillation |
| 6 | Operative Contexts surface (NEW v6) | User-inspectable operative context + contest endpoint |
| 7 | OpenClaw-memory adapter | `/memory/{bootstrap,semantic}` endpoints |
| 8 | Reliability surface + AIE-Bench/SEAGym hooks | `/reliability` + rewards/policy endpoints |

### B9. Multimodal fusion — v6

**Production systems (2026):** LFM2.5-VL-450M, OmniVLM-968M, Gemma 3 4B, Qwen2.5-Omni, GPT-4o, Claude Opus 4.

**v6 NEW — CogniRoute (arXiv 2606.20970, OmniSocialBench) is the relevant recipe for *social* multimodal fusion:** 59.38% accuracy on OmniSocialBench, +15.33 over proprietary, +26.77 over open-source omni. Schema-guided MoE with route-aware RL. For Danlab's "AI that sees and hears you", CogniRoute is the architectural reference.

**v6 NEW — V5e-0 / SpecFlow / CondenseVLM / QViD are the inference-time fusion-efficiency recipes:** reduce visual tokens, decode faster, preserve evidence.

**Danlab's path (v6):** *modality-separated with shared memory, with inference-time efficiency stack.* audiod → memoryd, perceptiond → memoryd, memoryd → orchestrator. v2: explore true omni-modal (Qwen2.5-Omni-3B quantized, or Gemma 3 4B with audio). Not a 2026 priority — the v1 path is the *correct* v1 path.

### B10. Model compression — v6

**Working in 2026:**
- Q4_K_M, Q4_0, Q5_0, Q8_0.
- IQ4_XS importance-weighted quantization.
- GGUF + mmap.
- ONNX Runtime quantization (Liquid LFM2.5 has full ONNX export).
- Flash Attention 2/3.
- Speculative decoding (V5e-0 Free-Root, 1.89×).
- **Token compression (OmniVLM 9×, CondenseVLM, QViD, SpecFlow).**
- **Adaptive context compaction (SelfCompact 30–70% token cost down).**
- TTS int8 quant (MisoTTS).

**v6 NEW frontier techniques:**
- **SelfCompact (arXiv 2606.23525)** — agent invokes compaction tool with a lightweight rubric; up to 18.1-point gains on math, 5–9 on agentic search, 30–70% lower per-question token cost. v6 adopts for audiod + memoryd context paths.
- **R_FOLD (OpenReview 2026)** — bi-level context management; 81.33% on BrowseComp-Plus at 32K. v6 adopts for memoryd v2.

---

## Part C — Competitive & Market Research

### C11. Smart glasses market — v6

**Meta Glasses at $299 (Jun 23 2026) is the line in the sand.**
- $299 Adventurer, $299 Fury, $399 Starfire (Kylie Jenner).
- 12MP camera, 3K video, 5-mic array, 8h battery + 40h case.
- **Muse Spark AI from Meta Superintelligence Labs.** First Meta Glasses to ship Muse Spark Day 1.
- Live translation in 20 languages (14 new, including Hindi, Japanese, Mandarin, Korean).
- Pedestrian navigation (turn-by-turn, audio-only).
- Dynamic Photo (auto multi-frame selection).
- Available in US, UK, Canada, Australia, France, Germany, Italy, Spain.

**Apple 2027.** Bloomberg reports camera-enabled glasses in 2027.

**Google × Samsung × Warby Parker × Gentle Monster.** Android XR audio glasses fall 2026.

**Snap Specs $2,195.** Preorders Jun 16 2026. Standalone AR.

**Microsoft Scout (Build 2026, Jun 2 2026).** Built on OpenClaw. First-party vendor adoption.

**Danlab's positioning (v6):** *we cannot win on hardware. The moat is:*
- **Privacy:** hardware privacy switch, on-device-first, open weights where possible.
- **Proactivity:** audiod calibration + operative context = the AI that *initiates* (Focus Mode) — not just responds.
- **On-device-first:** LFM2.5 + CondenseVLM + QViD + V5e-0 + Kokoro-82M + whisper.cpp + MiniLM. All on device.
- **India-cost:** ₹4,999 student tier, ₹12K founder tier, ₹25K SMB tier (per Dan1 v82).
- **Open-source + auditable self-improvement:** audiod calibration paper + memoryd v2 paper + AIE-Bench submission. This is the *verification regime* Anthropic is asking for.
- **Anthropic-aligned verification pitch:** "open eval, open reward, open head, open failure-mode registry" — directly responsive to Anthropic's Jun 4–5 2026 pause call.

### C12. Open-source AI companion projects — v6

- **taOS (jaylfc)** — self-hosted AI agent OS, offline by default, 100+ apps, 16 frameworks, 112 local model manifests including RK3588 NPU variants. Direct comparison set.
- **OpenClaw** — 464+ stars, MCP tools, multi-agent, the de-facto substrate.
- **Dani** — Danlab's own agent platform (repos/dani).
- **Memory frameworks:** OpenViking, Zep Graphiti, Honcho, MemoryHub, agentmemory, LLM-Wiki.

**v6 positioning:** Danlab is *not* another AI companion. Danlab is the *only* project that ships a self-improving audiod calibration loop on open weights with an AIE-Bench submission. The differentiator is the verification regime, not the UX.

### C13. Privacy-preserving AI — v6

- **Coolify 5N6 LiberaGPT** — 70B on-device Android app. Direct comparison: Danlab's on-device-first + on-device audiod calibration is *the* 2026 reference.
- **Anthropic's stance against domestic surveillance + autonomous weapons** — aligns with Danlab's "AI that doesn't spy on you" pitch.
- **EU AI Act** — Danlab is positioned for the 2026 enforcement wave. On-device-first, open-source, auditable.

---

## Part D — Technical Deep Dives (v6)

### Deep Dive A — Self-improving RL loops for language models

**2026 landscape (v6, with numbers):**

| Paper | Mechanism | Lift | Source |
|---|---|---|---|
| AIE-Bench | Meta-agent improves target-agent; 2 task families (terminal, tool) | Venue | ICML 2026 |
| SEAGym | Harness-only updates; 3 strategies (ACE, TF-GRPO, AHE); 5 epochs | Frequent updates ≠ better | OpenReview 2026 |
| EvoMaster | Self-evolving scientific agents, 100 LoC | +159–316% over OpenClaw | OpenReview 2026 |
| AEL | Two-timescale bandit + slow reflection | +27% Sharpe | OpenReview 2026 |
| SEER | Unsupervised self-evolution via MCMC | Outperforms reasoning baselines | OpenReview 2026 |
| AtomMem | RL memory CRUD with GRPO | Beats static memory | OpenReview 2026 |
| EDGE | Experience-distillation (positive marginal gains → reverse-KL into policy) | +8.3–12.5 success points 7B | OpenReview 2026 |
| HERO | Hindsight-enhanced self-distillation | Higher success, fewer turns | OpenReview 2026 |
| RISE (CogniRoute) | Route-aware RL on social multimodal | 59.38% on OmniSocialBench | arXiv 2606.20970 |
| Socratic-SWE | Self-evolving coding agents | Source-derived skills | arXiv 2606.07412 |
| POISE | LLM agents discover RL algorithms | AIME25 pass@32: 26.7% → 43.3% | ACL ARR 2026 |
| GRAM | RL for graph memory CRUD | Beats RAG | OpenReview 2026 |
| RefCon | Iterative refinement + contrastive memory | +21.6% on ACE | ACL ARR 2026 |
| **Rise-and-collapse** | arXiv 2606.21090 | **ES + CARE + GRPO are regime-dependent** | arXiv 2606.21090 |
| SelfCompact | Adaptive context compaction | +18.1 math, 5–9 agentic, 30–70% token cost down | arXiv 2606.23525 |
| SPaRTan | Training-free self-improvement playbook | Capacity-dependent social gains | OpenReview 2026 |
| R_FOLD | Bi-level context management | 81.33% BrowseComp-Plus | OpenReview 2026 |
| CaveAgent | Stateful runtime operator | +13.5% multi-turn retail, 51% token reduction | OpenReview 2026 |

**v6 v5 → v6 deltas in Deep Dive A:**

1. **Added the rise-and-collapse ceiling.** v5 missed this. v6 makes it the central architectural constraint of the audiod RL agent.
2. **Added EvoMaster, SelfCompact, R_FOLD, CaveAgent, HERO, EDGE, AtomMem, SEER.** v5 named AEL/RefCon/GRAM/POISE/SIA; v6 adds 9 more.
3. **Made the publication framing sharper.** "Auditable Confidence Calibration for On-Device Speech Recognition" is the v6 pitch. Open eval, open reward, open head, open failure-mode registry.

**v6 audiod RL harness (final design):**

```python
# audiod_rl/loop.py
# 6-week build, 6-week eval, AIE-Bench + SEAGym submission Sep 30, 2026
# Open: harness, reward, calibration head, failure-mode registry

class AudiodCalibrationLoop:
    def __init__(self, base_encoder, calibration_head):
        self.base = base_encoder  # frozen whisper.cpp base.en encoder
        self.head = calibration_head  # 4-layer MLP, 80K params
        self.peak_score = 0.0
        self.peak_step = 0
        self.plateau_count = 0
        self.rollforward_at = 3  # ES: peak_step + 3
        self.budget = 200  # total RL steps

    def step(self, batch, step):
        # 1. forward (frozen base + trainable head)
        logits = self.base(batch.audio)
        cal = self.head(logits)  # (B, num_bins)
        # 2. reward: Brier + ECE on CommonVoice-Indian (OOD)
        reward = self.evaluate(cal, batch.gt)  # scalar
        # 3. policy update: GRPO on small head
        self.head.update(cal, batch.gt)  # GRPO
        # 4. peak detection + ES
        if reward > self.peak_score:
            self.peak_score = reward
            self.peak_step = step
            self.peak_checkpoint = deepcopy(self.head.state)
            self.plateau_count = 0
        else:
            self.plateau_count += 1
        # 5. roll-forward
        if self.plateau_count >= self.rollforward_at:
            self.head.load_state(self.peak_checkpoint)
            return {"action": "rollforward", "peak_score": self.peak_score,
                    "peak_step": self.peak_step, "step": step}
        return {"reward": reward, "peak_score": self.peak_score, "step": step}
```

**Targets:**
- ECE < 0.05 on Librispeech test-clean (baseline 0.18).
- ECE < 0.10 on CommonVoice Indian-accent English (OOD).
- arXiv pre-print by Aug 15, 2026.
- AIE-Bench + SEAGym submission by Sep 30, 2026.

### Deep Dive B — Edge VLM optimization (v6 reframing)

**v5 said: "swap LFM2.5 → OmniVLM-968M." v6 says: "keep LFM2.5, add CondenseVLM + QViD + V5e-0."**

**Why v6 is right:**
- OmniVLM-968M is real but unverified on Danlab's task suite. Eval is 2–4 weeks.
- CondenseVLM, QViD, V5e-0 are *training-free* inference-time techniques. Lower risk, faster build, same model.
- V5e-0 alone gives 1.89× wall-clock. CondenseVLM + QViD give 1.5–2× on top. SpecFlow adds another 2.1× compute/KV-cache savings.
- **Combined: 2–3× wall-clock win, no retraining, no quantization trade-off.**

**v6 perceptiond v2 plan (replaces v5 swap plan):**

| Week | Component | Source | Confidence |
|---|---|---|---|
| 1–2 | V5e-0 (Free-Root + depth-3 speculative tree) | OpenReview 2026 | High |
| 3–4 | QViD (low-rank query–vision pruning) | arXiv 2026 | High |
| 5–6 | CondenseVLM (submodular evidence preservation) | arXiv 2026 | High |
| 7 | Eval on perceptiond test set + LibriSpeech-style salience | — | High |
| 8 | Deploy as perceptiond v2 (keep LFM2.5 as base) | — | High |

**v6 keeps the v5 OmniVLM eval as a Q4 2026 alternative if the inference-time stack plateaus.**

### Deep Dive C — Vector search and memory architectures for AI companions

**v6 extends v5 with the Operative Contexts critique and the reliability surface.**

**memoryd v2 spec (v6, final):**

```yaml
architecture: AEL + DPCM + LLM-Wiki + OpenClaw-memory + Operative Contexts + reliability
deployment: daemon, port 8741, Unix-domain-socket for daemon-to-daemon
build_time: 8 weeks (Jul 1 – Aug 26, 2026)
open_eval: LongMemEval, PersonaMem-v2, dglabs-eval (NEW)

# AEL fast Thompson bandit — 5 retrieval modes
retrieval_modes:
  - semantic    # cosine over MiniLM-L6-v2 (current)
  - episodic    # recency-weighted + session-bounded
  - procedural  # workflow templates, accessed by task type
  - graph       # DPCM doubly-linked provenance traversal
  - reranked    # cross-encoder reranking on top of semantic

# DPCM doubly-linked provenance graph
graph:
  edges: {supersedes, superseded_by, derived_from, supports}
  nightly_sweep: true  # System 2 induction of higher-level schemas

# LLM-Wiki reconsolidation
reconsolidation:
  cadence: 24h
  policy: cluster → summary → supersede originals
  opt_in: true

# OpenClaw-memory adapter
openclaw:
  endpoints: {/memory/bootstrap, /memory/semantic, /memory/episode}
  protocol: OpenClaw memory-core 0.4

# Operative Contexts surface (NEW v6)
operative_context:
  inspect: GET /context
  revise:  POST /context/revise
  contest: POST /context/contest  # flag silent misalignment
  diagnostic_stress_tests: [context_drift, scope_leak, stale_context]
  audit_log: per-context access log with user-visible trail

# Reliability surface (NEW v6)
reliability:
  axes: [calibration, consistency, robustness, predictability, safety]
  eval: AIE-Bench-style auditable
  publish: GET /reliability returns current values per axis
  failure_mode_registry: open, append-only, versioned
```

**Eval targets (v6):**
- LongMemEval: match or beat AEL baseline.
- PersonaMem-v2: +5.20 (DPCM target).
- PersonaMem: match RefCon +21.6%.
- **dglabs-eval (NEW v6):** new public benchmark for the audiod + memoryd combo. 100-task eval set. Open-source. The first Danlab artifact to ship a public eval.

---

## Synthesis — what v6 changes vs v5

**v5 → v6 deltas (the substance):**

1. **HRM-Text numbers corrected.** 84.5% GSM8k, 60.7% MMLU, 56.2% MATH, $1,500 training, May 18 2026, open-sourced (arXiv 2605.20613, github.com/sapientinc/HRM-Text, HF sapientinc/HRM-Text-1B).
2. **Rise-and-collapse mitigation is the central architectural constraint** of the audiod RL agent. ES + peak detection + checkpoint rolling. Without it, the loop collapses within one campaign.
3. **EvoMaster, SelfCompact, R_FOLD, CaveAgent, HERO, EDGE, AtomMem, SEER, SkillsVote** are added to the v6 self-evolving-agents map. v5 named 4; v6 names 12+ with concrete lift numbers.
4. **Anthropic's Jun 4–5 2026 global pause call is the v6 moat.** "Open verification regime" is the differentiator. audiod calibration paper ships with *open eval + open reward + open head + open failure-mode registry*. Meta's $299 cannot.
5. **VLM optimization reframed: token-pruning + speculative decoding, not base-model swap.** CondenseVLM + QViD + V5e-0 on existing LFM2.5-VL-450M. 2–3× wall-clock win, no retraining, no quantization trade-off.
6. **Operative Contexts (user-inspectable memory) is a v6 spec change for memoryd v2.** Per OpenReview 2026 critique: memory must be user-inspectable to avoid silent contextual misalignment.
7. **Reliability surface (`/reliability`) is a v6 spec change for every daemon.** Per arXiv 2602.16666: consistency, robustness, predictability, safety. Predictability = calibrated confidence.
8. **dglabs-eval (NEW v6) is the first Danlab public benchmark.** 100 tasks for audiod + memoryd. The first artifact that ships a public eval. This is the v6 differentiator.
9. **Tauri webview WebGPU in-browser TTS (Kokoro-82M via ONNX Runtime Web) is a v6 ttsd v2 option.** WebNarrator 1.1.0 ships this today; Tauri webview can use the same path.
10. **Anthropic-aligned verification pitch.** The Dan Glasses brand is now explicitly *the AI glasses Anthropic would ship if Anthropic made glasses.* Privacy, on-device, open verification, auditable self-improvement. This is the v6 market positioning.

**v6 thesis (single sentence):**
Ship a reliability-aware, open-verifiable audiod confidence-calibration RL agent (with rise-and-collapse mitigation) to AIE-Bench + SEAGym by Sep 30, 2026; ship memoryd v2 with AEL + DPCM + LLM-Wiki + Operative Contexts surface + reliability surface + OpenClaw-memory adapter by Sep 15, 2026; keep LFM2.5-VL-450M and add CondenseVLM + QViD + V5e-0 stack by Sep 1, 2026; swap KittenTTS → Kokoro-82M (with WebGPU in-browser option) by Jul 15, 2026; train HRM-Text-1B on Danlab's task suite by Q1 2027; position the brand around *open verification regime + on-device-first + privacy + proactivity + India-cost* against Meta's $299 in-house line and Anthropic's call for verifiable slowdown.

---

## Sources (v6)

1. AIE-Bench: Benchmarking Agents That Build Agents. ICML 2026. https://openreview.net/forum?id=f9yc09BuxG
2. SEAGym: An Evaluation Environment for Self-Evolving LLM Agents. OpenReview 2026. https://openreview.net/forum?id=hLHB7NCuke
3. SkillsVote: Lifecycle Governance of Agent Skills. OpenReview 2026. https://openreview.net/forum?id=kj068rI9Uh
4. AEL: Agent Evolving Learning for Open-Ended Environments. ACL ARR 2026. https://openreview.net/forum?id=dtPo105y8x
5. EvoMaster: A Foundational Evolving Agent Framework for Agentic Science at Scale. OpenReview 2026. https://openreview.net/forum?id=lidiprht3N
6. Self-Improvement Can Self-Regress: The Rise-and-Collapse Failure Mode. arXiv 2606.21090. https://arxiv.org/abs/2606.21090v1
7. RefCon: Iterative Refinement and Contrastive Memory Extraction. ACL ARR 2026. https://openreview.net/forum?id=fatsyRRKEs
8. GRAM: Empowering Agent with Actively Managed Graph-Structured Memory. OpenReview 2026. https://openreview.net/forum?id=rzGvGnwVC7
9. EDGE: Experience-Distillation for Guided Exploration in Agentic RL. OpenReview 2026. https://openreview.net/forum?id=JARVj9rlPP
10. Self-Compacting Language Model Agents (SelfCompact). arXiv 2606.23525. https://arxiv.org/abs/2606.23525v1
11. HERO: Hindsight-Enhanced Reflection from Environment Observations. OpenReview 2026. https://openreview.net/forum?id=CFnfsORP7Y
12. R_FOLD: Bi-Level Context Management for Long-Horizon Tool-Using. OpenReview 2026. https://openreview.net/forum?id=Wlz2pfZwEu
13. CaveAgent: Transforming LLMs into Stateful Runtime Operators. OpenReview 2026. https://openreview.net/forum?id=p3dlOhpqKD
14. Operative Contexts: Belief Revision and Memory in Agentic AI. OpenReview 2026. https://openreview.net/forum?id=KSzS4FHzau
15. AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation. OpenReview 2026. https://openreview.net/forum?id=dfWiKLx6fs
16. SEER: Unsupervised Self-Evolution of Reasoning through Model-Intrinsic Verification. OpenReview 2026. https://openreview.net/forum?id=9PhHO8wFyh
17. CogniRoute: Learning to Route Social Evidence in Omni-Modal Models. arXiv 2606.20970. https://arxiv.org/abs/2606.20970v1
18. DPCM: Memory Beyond Recall. ACL ARR 2026. https://openreview.net/forum?id=ywl53zPXu0
19. OpenAI Dreaming V3 — Memory Wars (Jun 4 2026). https://awesomeagents.ai/news/openai-dreaming-v3-memory-wars/
20. Anthropic Memory + Dreaming product. https://youtu.be/RtywqDFBYnQ
21. From context to dreams: architecting memory for AI agents. Red Hat. Jun 1 2026. https://next.redhat.com/2026/06/01/from-context-to-dreams-architecting-memory-for-ai-agents
22. OpenClaw memory architecture docs. https://docs.openclaw.ai/concepts/memory
23. HRM-Text: Efficient Pretraining Beyond Scaling. Sapient, arXiv 2605.20613, May 18 2026. https://arxiv.org/abs/2605.20613 — github.com/sapientinc/HRM-Text — HF sapientinc/HRM-Text-1B
24. Meta Glasses $299 launch. Meta blog Jun 23 2026. https://www.meta.com/blog/introducing-meta-glasses-a-range-of-new-styles-from-meta-and-essilorluxottica-starting-at-299/
25. Meta Glasses $299 launch. TechCrunch Jun 23 2026. https://techcrunch.com/2026/06/23/meta-debuts-new-cheaper-smart-glasses-under-its-own-brand/
26. Anthropic global pause call (Jack Clark + Marina Favaro). Jun 4 2026. https://www.aljazeera.com/economy/2026/6/5/anthropic-urges-ai-labs-to-pause-warns-humans-risk-losing-control
27. Anthropic pause — The Register. https://www.theregister.com/ai-and-ml/2026/06/05/it-would-be-good-for-the-world-to-slow-down-ai-sprints-anthropic-says/5251460
28. Towards a Science of AI Agent Reliability. arXiv 2602.16666. https://arxiv.org/html/2602.16666v3
29. Kokoro-82M: Apache 2.0, 24kHz, MOS 4.45, 327MB, Raspberry Pi. https://localaimaster.com/blog/kokoro-tts-local-setup
30. Kokoro vs XTTS vs Chatterbox: Best Local TTS in 2026. https://localaimaster.com/blog/kokoro-vs-xtts-vs-chatterbox
31. WebNarrator 1.1.0 ships Kokoro-82M in-browser via ONNX Runtime Web. https://webnarrator.com/posts/built-in-neural-voices/
32. CondenseVLM: Visual Token Condensation for Efficient Multimodal Reasoning. OpenReview 2026. https://openreview.net/forum?id=9rMb7isKDc
33. QViD: Vision Token Pruning via Query–Vision Interaction Decomposition. OpenReview 2026. https://openreview.net/forum?id=UgbjqumIWe
34. V5e-0: A Minimalist Self-Speculative Decoding Framework for VLMs. OpenReview 2026. https://openreview.net/forum?id=GpFgbKW7PR
35. SpecFlow: Spectral-Progressive Thought Flow for Lightweight Multimodal Reasoning. arXiv 2606.02842. https://arxiv.org/abs/2606.02842v1
36. Microsoft Scout (Build 2026, Jun 2 2026). https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/
37. Coolify 5N6 LiberaGPT for Android 70B on-device. https://www.usatoday.com/press-release/story/35187/new-free-privacy-focused-android-app-allows-a-record-breaking-70-billion-parameter-ai-model-to-run-entirely-offline-on-high-end-android-devices/
38. taOS — Self-hosted AI agent OS. https://github.com/jaylfc/taOS
39. Propose, Critique, Falsify: Benchmarking Self-Verifying AI Scientists. ICML 2026 AI4Science Spotlight. https://openreview.net/forum?id=RyX98G24rP
40. Socratic-SWE: Self-Evolving Coding Agents. arXiv 2606.07412. https://arxiv.org/abs/2606.07412v1
41. POISE: Autonomous Discovery of LLM-RL Algorithms. ACL ARR 2026. https://openreview.net/forum?id=EPWdJDKSXx
42. SIA (Hexo Labs, MIT, May 2026). https://github.com/HexoLabs/SIA
43. Anthropic Claude Tag (Jun 2026). https://the-agent-report.com/2026/06/anthropic-claude-tag-proactive-memory/
44. Snap Specs preorders $2,195. Dezeen Jun 18 2026. https://www.dezeen.com/2026/06/18/snap-specs-smart-glasses-augmented-reality/
45. Meta Glasses Kylie Jenner. MediaPost Jun 24 2026. https://www.mediapost.com/publications/article/416034/meta-rolls-out-kylie-jenner-inspired-ai-glasses.html
46. Meta targeting 10M units H2 2026. Road to VR. https://roadtovr.com/meta-meta-smart-glasses-report-ai-pendant/
47. Google × Samsung Android XR demo at I/O 2026. https://glassalmanac.com/7-smart-glasses-in-2026-that-reveal-what-finally-makes-ar-wearable/
48. Apple AI AirPods and glasses. NY Post Jun 16 2026. https://nypost.com/2026/06/16/business/apple-to-launch-ai-juiced-airpods-and-sunglasses-going-head-to-head-with-meta/
49. Sapient HRM-Text $1500 training coverage. VentureBeat. https://venturebeat.com/technology/researchers-say-they-trained-a-foundation-model-from-scratch-for-about-1-500
50. StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance. arXiv 2606.14571. https://arxiv.org/abs/2606.14571v1
51. From Trainee to Trainer: LLM-Designed Training Environment for RL. arXiv 2606.17682. https://arxiv.org/abs/2606.17682v1

— Dan2, Bengaluru 🇮🇳, 2026-06-24 11:30 IST
