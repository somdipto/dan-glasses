# Dan2 — Top 5 Research Papers to Read
**Date:** 2026-06-14
**Status:** Final v1
**Audience:** somdipto (decision-maker), Dan1/Dan3/Dan4 (peer architects), future Danlab hires
**Scope:** The 5 papers (plus 5 honorable mentions) that the Danlab team MUST read to make the right product and research decisions in 2026.

---

## How to read this list

These papers are prioritized by **direct impact on Dan Glasses / Danlab AGI roadmap decisions** in the next 6 months. They are not the "best" papers of 2026 abstractly — they are the ones that change what we should build, what we should spike, and what we should defer.

**Read order:**
- **Week 1, Paper 1 + 2**: The AGI primitive (SIA) and the wearable silicon (OpenGlass). Foundational.
- **Week 2, Paper 3 + 4**: The memory layer (Mem0) and the safety/RL debate (Harness Updating Is Not Harness Benefit). Both ship in memoryd v2 v1.0.
- **Week 3-4, Paper 5**: The edge AI acceleration (VLMCache). The single highest-ROI perceptiond upgrade.

Then read the 5 honorable mentions as time allows.

---

## Paper 1: SIA: Self Improving AI with Harness & Weight Updates (Hexo Labs, May 2026)

**Citation:** Hebbar et al., 2026. arXiv 2605.27276. https://arxiv.org/html/2605.27276v2

**GitHub:** https://github.com/hexo-ai/sia

**Why this paper:**

This is the **single most important paper for Danlab's AGI direction in 2026**. SIA is the first open-source framework that simultaneously updates both an agent's harness/scaffold AND its model weights, with auditable provenance. It validates that **harness-only self-improvement (SIA-H) is already +25% on legal classification, +12% on GPU kernel speed**, with full weight update (SIA-W+H) targeting LawBench 70.1% held-out.

**The two operating points:**
- **SIA-H (harness-only)**: A Feedback-Agent rewrites the Meta-Agent's scaffold (tools, prompts, retry logic, search procedure). No weight modification. **Auditable. Low cost.** Validated on legal classification (+25%), GPU kernel speed (+12%), biological data denoising.
- **SIA-W+H (harness + weights)**: The Feedback-Agent also runs RL on the focal model's weights. **Not auditable. Higher cost.** Validated on LawBench 70.1% held-out, TriMul 14.02×.

**Why it matters for Danlab:**

1. **It is the credible RL path** for `danlab-multimodal`. Currently, `danlab-multimodal` is honestly framed as "pre-RL scaffold, not RL" because the scoring is hand-coded. SIA-H changes that. **Fork SIA-H into `danlab-multimodal` in Month 1. 2-week experiment.**

2. **It is the bridge from harness to weights.** Anthropic SkillOpt + Microsoft SkillOpt (Build 2026 / Fable 5 launches) both treat skill-document evolution as a first-class primitive. SIA gives us the architecture for the same evolution loop at the harness level. **Treat Dan1/Dan2/Dan3/Dan4 as trainable parameters.**

3. **It is auditable.** This is the key difference from "self-improving" systems that secretly modify weights. SIA logs all harness updates. SIA-W+H can be made auditable (with per-user-isolated weights + audit log).

4. **The "Harness Updating Is Not Harness Benefit" caveat is critical.** Train the focal model (1.2B) to load and follow its own harness, not use a 4.6B evolver. This is the right scale for Danlab.

**What to do after reading:**

- **Month 1**: Fork SIA-H into `danlab-multimodal`. 2-week experiment, single ML engineer, $0 compute beyond inference costs.
- **Month 1**: Implement Anthropic SkillOpt + Microsoft SkillOpt integration for Dan1/Dan2/Dan3/Dan4 skill-document evolution.
- **Month 3**: SIA-W+H spike. Build on SIA-H from Month 1. Train the 1.2B focal model (LFM2.5-1.2B-Thinking) to load and follow its own harness.
- **Month 3**: PopuLoRA populations in `danlab-multimodal` (TrueSkill cross-eval).

**Don't call it "RL" until:**
- (a) Harness updates are logged
- (b) Weight updates are auditable
- (c) Both are independently reviewable

**The SIA paper alone validates the entire Danlab AGI roadmap for the next 12 months.**

---

## Paper 2: OpenGlass: Open-Source Smart Glasses for On-Device Event-Based Gesture Recognition (June 2026)

**Citation:** arXiv 2606.07431. https://arxiv.org/abs/2606.07431

**Why this paper:**

This is **the wearable silicon reference for 2026**. OpenGlass achieves **11.8 hours of continuous on-device ML from a 200 mAh battery** using a GAP9 RISC-V SoC + Prophesee GENX320 event camera + nRF5340 PMIC coordinator. End-to-end gesture recognition latency is **78.3 ms** with 83.94% cross-subject accuracy.

**The architecture:**
- **GAP9 RISC-V SoC** (GreenWaves Technologies) — 10-core RISC-V cluster, sub-1W typical power.
- **Prophesee GENX320 event camera** — event-based, not frame-based. 320×320 resolution, microsecond latency, ~10mW.
- **nRF5340 PMIC coordinator** — event-driven wake-up, keeps GAP9 powered down between inferences.
- **200 mAh battery** — sufficient for 11.8h of continuous ML.

**Why it matters for Danlab:**

1. **Sub-1W wearable is achievable in 2026.** The PRD's power budget estimates (8-13W active, 2-5W sustained) are wrong. Sub-1W is feasible with the right silicon + event-driven wake-up.

2. **Event cameras are the right sensor for always-on vision.** Frame-based cameras (V4L2) waste power on every frame, even if no salience. Event cameras wake up only on change.

3. **The 200 mAh reference is the right weight class.** 200 mAh is a single-temple battery that fits in the Brilliant Labs Halo / Monako Glass form factor.

4. **It is open-source.** All hardware schematics + software are open. We can replicate the architecture with our own BOM.

5. **The 78.3 ms end-to-end latency validates the salience-gated inference gate.** This is the right latency for the always-on wearable vision pipeline.

**What to do after reading:**

- **Month 1**: Buy GAP9 dev kit + Prophesee GENX320 + nRF5340 PMIC. Measure SmolVLM-256M on GAP9 with event camera. Target: sub-1W sustained at 4-10 FPS.
- **Month 1**: Lock the form factor decision tree: 4 paths (Redax vs Monako Glass vs Brilliant Labs Halo vs Project Solara MDEP) → pick one and ship.
- **Month 4-6**: Integrate event camera into perceptiond v5 (replace V4L2 with event-driven capture).
- **Month 7-9**: Wearable pilot (50-100 users) on the locked form factor.

**OpenGlass is the single most important paper for the wearable silicon path.**

---

## Paper 3: Mem0: Towards Long-Term Memory in LLM-Based Conversational Agents (Mem0, 2025-2026)

**Citation:** arXiv 2504.19413. https://arxiv.org/abs/2504.19413

**GitHub:** https://github.com/mem0ai/mem0

**Why this paper:**

Mem0 is **the production-grade open-source memory layer for AI agents in 2026**. It is the reference architecture that production agents use to handle long-term memory across sessions. The paper validates that **a 4-stage pipeline (Extract → Reflect → Update → Search) reduces LLM token cost by 90% while maintaining or improving answer quality** on the LoCoMo benchmark.

**The architecture:**
- **Extract**: LLM extracts salient facts from conversation turns.
- **Reflect**: LLM compares new facts to existing memory, dedups and merges.
- **Update**: Vector store + graph store updated.
- **Search**: Hybrid retrieval (BM25 + vector + graph) at query time.

**Why it matters for Danlab:**

1. **It is the production reference for memoryd v2.** The 4-stage pipeline is exactly the shape of the memoryd v2 ingest / retrieve / consolidate modules.

2. **It is open-source + MIT-licensed.** We can fork it, modify it, and ship it as `danlab-multimodal` + `memoryd v2`.

3. **The 90% token cost reduction is critical for cost.** Dan Glasses queries memoryd on every voice interaction. Mem0's hybrid retrieval + dedup is much cheaper than rerunning the full conversation through the LLM.

4. **The graph + vector hybrid is the right shape for personal AI.** Graph for relations (people, places, events), vector for semantic similarity. The 2026 production standard.

5. **It is one of 6 components in the memoryd v2 v1.0 stack (the bet).** Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output) + Weaviate Engram.

**What to do after reading:**

- **Month 1**: Read Mem0 codebase + paper. Spike as a single memoryd v2 module.
- **Month 2**: Spike Zep (temporal knowledge graph) as the temporal layer.
- **Month 2**: Spike Hindsight (4-lever: World/Experience/Opinion/Observation) as the consolidation layer.
- **Month 3**: memoryd v2 v1.0 OPEN-SOURCE RELEASE on GitHub public. 6-core stack. **The bet.**

**Mem0 is the single most important paper for the memory layer.**

---

## Paper 4: Harness Updating Is Not Harness Benefit (May 2026)

**Citation:** arXiv 2605.30621.

**Why this paper:**

This is the **single most important paper for understanding the limits of self-improving systems**. It is the critical caveat to SIA (Paper 1) and SkillOpt (Honorable Mention 1). The core claim: **harness gains are not the same as weight gains**, and training the focal model to load and follow its own harness is the right approach.

**The key insight:**

A naive SIA-W+H implementation uses a 4.6B evolver to update a 1.2B focal model's weights. This is **wrong**:
- The evolver's update quality is bounded by the evolver's own capability.
- The 1.2B focal model doesn't "internalize" the harness; it just gets better at following prompts.
- The weight update may be a "reward hack" that doesn't generalize.

The paper's recommendation: **train the focal model (1.2B) to load and follow its own harness artifacts**. This means:
- The focal model can read SKILL.md, MEMORY.md, etc.
- The focal model can update its own SKILL.md (within verifier-graded gates).
- The focal model's weights evolve *with* its harness, not *despite* it.

**Why it matters for Danlab:**

1. **It informs the SIA-W+H focal model choice.** Use LFM2.5-1.2B-Thinking (1.2B) as the focal model, not Gemma 4 12B or 4.6B. The 1.2B is the right scale to "internalize" its own harness.

2. **It validates PopuLoRA populations.** Multiple LoRA adapters (population), TrueSkill cross-eval, only the best adapter is kept. This avoids single-LoRA overfit.

3. **It informs the safety review for SIA-W+H in production.** Weight updates are not "self-evidencing." They require:
   - Per-user-isolated weights
   - Audit log of every weight delta (with verifier score)
   - Rollback capability
   - "Treat Dan1/Dan2/Dan3/Dan4 as trainable parameters" — but with the right scale + population + audit.

4. **It is the answer to "Don't call it RL."** The "RL" label is earned when:
   - (a) Harness updates are logged
   - (b) Weight updates are auditable
   - (c) Both are independently reviewable
   - (d) The focal model can load and follow its own harness (not just prompts)

**What to do after reading:**

- **Month 1**: Design SIA-W+H focal model = LFM2.5-1.2B-Thinking (1.2B).
- **Month 3**: SIA-W+H spike. Train the focal model to load and follow its own harness.
- **Month 3**: PopuLoRA populations in `danlab-multimodal` (TrueSkill cross-eval).
- **Month 6+**: Per-user-isolated weights + audit log + rollback in production wearable.

**The Harness Updating paper is the caveat that prevents the "RL" label from being misused.**

---

## Paper 5: VLMCache: Efficient On-Device Vision-Language Model Inference (ACM 2026)

**Citation:** ACM 2026. https://dl.acm.org/doi/abs/10.1145/3745756.3809243

**Why this paper:**

This is the **single highest-ROI perceptiond upgrade for 2026**. VLMCache achieves **1.4-3.8× speedup in inference with less than 1% average accuracy loss** across diverse VLMs and datasets, by **disaggregating visual input into stable (background) and dynamic (foreground) blocks**. Stable blocks are encoded into a reusable KV-cache prefix; dynamic blocks are recomputed.

**The architecture:**
- **Semantic disaggregation**: Robustly identifies reusable blocks (semantic similarity, not just pixel difference).
- **Isolate-then-fuse**: Separates foreground/background, preserves global attention and positional coherence.
- **Block-level visual KV-cache prefix**: Reuses computation across video frames.
- **TTFT (time-to-first-token) reduction**: 1.4-3.8× faster.

**Why it matters for Danlab:**

1. **It is the right lever for wearable power draw.** The dominant power event is VLM inference. VLMCache cuts VLM inference by 1.4-3.8× without accuracy loss. On a 4 FPS watchful mode, this is the difference between 5W and 2W sustained.

2. **It is the right architecture for always-on vision.** Dan Glasses has a stable background (the room, the desk, the user's typical environment) and a dynamic foreground (people, objects, events). VLMCache exploits exactly this.

3. **It is generic across VLMs.** Works on LFM2.5-VL-450M, SmolVLM-256M, Gemma 4 12B, Qwen2.5-VL. No model-specific code.

4. **It is the single highest-ROI upgrade for perceptiond.** Drop-in integration. 1-2 weeks of engineering.

**What to do after reading:**

- **Month 2**: Integrate VLMCache in perceptiond. Drop-in. 1-2 weeks.
- **Month 2**: Measure: watts saved, ms latency reduction, accuracy preservation.
- **Month 2**: Spike V5e-0 / ViSpec-style self-speculative decoding in perceptiond (1.89× / 3.22× / 3.05-4.26× additional speedup).
- **Month 3**: Integrate MI-Pruner (visual token pruning via mutual information) for further VLM speedup.

**VLMCache is the single highest-ROI perceptiond upgrade for 2026.**

---

## Honorable Mention 1: SkillOpt: Trajectory-Derived, Verifier-Grounded Compilation of LLM-Agent Skills

**Citation:** OpenReview 2026. https://openreview.net/forum?id=2ONrrPIFYi

**Why this paper:**

SkillOpt is the **verifier-grounded compiler that converts no-skill LLM agent trajectories into deployable SKILL.md guides plus scripts**. It iterates with verifier feedback to avoid reward regressions. On 87 SkillsBench tasks: **33 positive-reward wins (13 rescues where no-skill agent failed), -63% token usage, -62% wall-clock latency, -40% tool calls**. Knowledge base grew from 5 to 19 patterns.

**Why it matters:**

SkillOpt is the **reference implementation of the "skill-document evolution" loop**. Anthropic SkillOpt + Microsoft SkillOpt (Build 2026 / Fable 5) both treat skill-document evolution as a first-class primitive. The "trajectory → SKILL.md" compilation is the right shape for Dan1/Dan2/Dan3/Dan4 skill evolution.

**What to do:**

- **Month 1**: Implement SkillOpt-style trajectory → SKILL.md compilation for Dan1/Dan2/Dan3/Dan4.
- **Month 1**: Read the SkillsVote paper (lifecycle governance of agent skills) for the production wrapper.

---

## Honorable Mention 2: Hindsight: 4-Lever Memory for Long-Term Memory in LLM Agents

**Citation:** https://github.com/vectorize-io/hindsight

**Why this paper:**

Hindsight is the **memory layer that achieves 91.4% on LongMemEval at scale**. The 4 levers (World / Experience / Opinion / Observation) map to the cognitive memory hierarchy.

**Why it matters:**

Hindsight is one of 6 components in the memoryd v2 v1.0 stack. The 4-lever architecture is the right shape for personal AI memory (world facts, past experiences, current opinions, observed events).

**What to do:**

- **Month 2**: Spike Hindsight as a memoryd v2 module.
- **Month 3**: Integrate Hindsight in memoryd v2 v1.0.

---

## Honorable Mention 3: LightGMEM: Lightweight Agent Graph Memory Generation

**Citation:** OpenReview 2026. https://openreview.net/forum?id=FCQR2oceJ1

**Why this paper:**

LightGMEM is the **lightweight graph-based memory framework that achieves 58× fewer LLM calls and 151.6× faster construction runtime than Zep on LoCoMo**. It uses GLiNER2 (zero-shot NER) instead of per-episode LLM extraction, conflict-lane partitioning for entity disambiguation, and Ego-Splitting for multi-context retrieval.

**Why it matters:**

The 58× cost reduction on memory construction is critical for production. **Most memory layers are not cost-viable at scale.** LightGMEM is the right architecture for the Dan Glasses cost profile (per-user, on-device, long-running).

**What to do:**

- **Month 2-3**: Spike LightGMEM in memoryd v2.
- **Month 3**: Integrate as a v2.0 or v2.5 component.

---

## Honorable Mention 4: Microsoft Scout / OpenClaw / Work IQ (Build 2026, June 2)

**Sources:**
- Microsoft Build 2026: https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/
- Work IQ GA June 16, 2026: https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/
- Project Solara: https://arstechnica.com/gadgets/2026/06/microsofts-project-solara-is-an-android-os-designed-for-agents-instead-of-apps/

**Why this is on the list:**

This is **not a paper, it's a product launch** — but it is the single most important market signal in 2026 for Dan Glasses. Microsoft Scout is an always-on work agent built on OpenClaw. Project Solara is an Android-based OS for agent-first devices. Work IQ is the enterprise intelligence layer with memory + graph.

**Why it matters:**

1. **Microsoft Scout is built on OpenClaw.** The compliance wedge (os-toold v2 with OWASP AIUC-1, Agent 365, MXC, Apple Core AI) is open-source on the same runtime.
2. **Project Solara targets agent-first wearables.** The badge concept is the wearable reference. Open-source competition.
3. **Work IQ is GA June 16, 2026.** It is the enterprise memory + graph layer. Dan Glasses can integrate Work IQ as a context layer via MCP.

**What to do:**

- **Month 3**: os-toold v2 GA with OWASP + Agent 365 + Microsoft IQ + Apple Core AI compliance. Wedge against Microsoft Scout GA.
- **Month 1**: Read Work IQ docs, spike as a context layer for memoryd v2.

---

## Honorable Mention 5: LFM2-Audio-1.5B (Liquid AI, 2026) — pending public release

**Source:** Liquid AI roadmap. https://www.liquid.ai/

**Why this is on the list:**

LFM2-Audio-1.5B is a **single audio-language model for STT + reasoning + TTS**. Apache 2.0-equivalent. If it ships an ONNX/GGUF export, it eliminates the audiod + ttsd stack (2 services → 1 service).

**Why it matters:**

1. **Sub-1W wearable is achievable in 2026.** A single 1.5B model on GAP9 is more efficient than 2 separate services (whisper.cpp + KittenTTS).
2. **Lower latency.** End-to-end STT + reasoning + TTS in one model = no IPC between services.
3. **Larger context.** Audio events can be reasoned about in their full temporal context.

**What to do:**

- **Month 1**: Spike LFM2-Audio-1.5B in audiod + ttsd. If ONNX/GGUF export ships, **consolidate audiod + ttsd into one audiolangd service**.
- **Month 1**: Watch Liquid AI's public release calendar. Carry if not available.

---

## Reading schedule (for the next 4 weeks)

| Week | Papers | Effort | Output |
|---|---|---|---|
| **Week 1** | SIA (Paper 1) + OpenGlass (Paper 2) | 6 hours total | SIA-H fork plan + GAP9 dev kit order |
| **Week 2** | Mem0 (Paper 3) + Harness Updating (Paper 4) | 6 hours total | memoryd v2 design + SIA-W+H focal model choice (1.2B) |
| **Week 3** | VLMCache (Paper 5) | 3 hours | perceptiond v5 integration plan |
| **Week 4** | SkillOpt + Hindsight + LightGMEM | 4 hours | memoryd v2 v1.0 component list |
| **Async** | Microsoft Scout / Work IQ / Solara (Honorable Mention 4) | 2 hours | os-toold v2 compliance plan |

Total: ~21 hours over 4 weeks. One paper per workday.

---

## The 1-page summary

| # | Paper | Key claim | Danlab action |
|---|---|---|---|
| 1 | **SIA (Hexo Labs, May 2026)** | SIA-H +25% on legal; SIA-W+H 70.1% on LawBench. Harness + weights self-improvement. | Fork SIA-H into `danlab-multimodal` Month 1. SIA-W+H spike Month 3 with LFM2.5-1.2B-Thinking focal model. |
| 2 | **OpenGlass (arXiv 2606.07431)** | Sub-1W wearable: GAP9 + event camera, 11.8h on 200mAh, 78.3ms latency. | Buy GAP9 dev kit + event camera Month 1. Form factor decision Month 1. |
| 3 | **Mem0 (arXiv 2504.19413)** | 4-stage memory pipeline. 90% token cost reduction. LoCoMo SOTA. | Spike as memoryd v2 module Month 1. 6-core stack Month 3. |
| 4 | **Harness Updating Is Not Harness Benefit (arXiv 2605.30621)** | Harness gains ≠ weight gains. Train focal model to load its own harness. | Use 1.2B focal model (LFM2.5-1.2B-Thinking), not 4.6B evolver. PopuLoRA populations. Per-user-isolated weights. |
| 5 | **VLMCache (ACM 2026)** | 1.4-3.8× VLM speedup with <1% accuracy loss. Block-level visual KV-cache. | Integrate in perceptiond Month 2. Single highest-ROI upgrade. |

**These 5 papers directly inform the 24-month AGI roadmap in `dan2-agi-roadmap.md`.**

---

## Sources

- SIA: https://arxiv.org/html/2605.27276v2 (arXiv 2605.27276, May 2026)
- SIA GitHub: https://github.com/hexo-ai/sia
- Harness Updating: https://huggingface.co/papers/2605.30621
- OpenGlass: https://arxiv.org/abs/2606.07431
- Mem0: https://arxiv.org/abs/2504.19413
- Mem0 GitHub: https://github.com/mem0ai/mem0
- VLMCache: https://dl.acm.org/doi/abs/10.1145/3745756.3809243
- SkillOpt: https://openreview.net/forum?id=2ONrrPIFYi
- SkillsVote: https://openreview.net/forum?id=kj068rI9Uh
- CMM (Cognitive Memory Manager): https://openreview.net/forum?id=yCsHQnvvWY
- SkillCompiler: https://openreview.net/forum?id=baOeYyuxty
- The Living Wiki: https://openreview.net/forum?id=e64EcfHp8L
- HERO: https://openreview.net/forum?id=CFnfsORP7Y
- PAM: https://openreview.net/forum?id=ptIjkWmtl9
- TRACE: https://openreview.net/forum?id=p37UqCmcxG
- Meta-Harness: https://openreview.net/forum?id=2Tx03Dan7u
- AEL: https://openreview.net/forum?id=dtPo105y8x
- DPCM: https://openreview.net/forum?id=ywl53zPXu0
- LightGMEM: https://openreview.net/forum?id=FCQR2oceJ1
- Hindsight: https://github.com/vectorize-io/hindsight
- SuperLocalMemory V3.3: https://github.com/SuperLocalMemory/SuperLocalMemoryV3
- Tenure: https://arxiv.org/html/2605.11325v2
- VisualMem: https://arxiv.org/abs/2605.28806v1
- BitNet b1.58 (ENERZAi on QCS6490): https://www.edge-ai-vision.com/2026/06/running-bitnet-on-qualcomm-hexagon-with-custom-1-58-kernels
- Litespark: https://arxiv.org/html/2605.06485v2
- V5e-0: https://openreview.net/forum?id=GpFgbKW7PR
- BASTION: https://openreview.net/forum?id=uqeOxztSIS
- MineDraft: https://openreview.net/forum?id=UmTQ21h8HC
- TISA: https://openreview.net/forum?id=6kOo3YtMdu
- PRKV: https://openreview.net/forum?id=HbjaTsG8vU
- MI-Pruner: https://openreview.net/forum?id=Bc2DZoXBus
- QViD: https://openreview.net/forum?id=UgbjqumIWe
- R-APS: https://arxiv.org/abs/2606.04823v1
- DUAL-Bench: https://openreview.net/forum?id=SLaIKf46Dz
- DPCM: https://openreview.net/forum?id=ywl53zPXu0
- GRAM: https://openreview.net/forum?id=rzGvGnwVC7
- GraP-Mem: https://openreview.net/forum?id=AUPI1ifc4v
- MemoryArena / Mage: https://arxiv.org/html/2606.06090v1
- EMemBench: https://openreview.net/forum?id=zzndQeR4Ay
- Modality-Aware Long-Term Memory: https://dl.acm.org/doi/abs/10.1145/3812835.3814986
- LFM2.5-VL-450M: https://huggingface.co/LiquidAI/LFM2.5-VL-450M
- Brilliant Labs Halo: https://quasa.io/video/brilliant-labs-halo-open-source-ai-glasses-for-curious-minds
- Monako Glass: https://www.timesofai.com/news/monako-glass-custom-linux-computer-glasses/
- Apple Glasses N50: https://www.macrumors.com/2026/05/31/apple-glasses-late-2027-report/
- Apple Vision Air: https://www.macobserver.com/news/apple-delays-smart-glasses-again-vision-air-still-expected-by-2029/
- Microsoft Scout: https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/
- Work IQ: https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/
- Project Solara: https://arstechnica.com/gadgets/2026/06/microsofts-project-solara-is-an-android-os-designed-for-agents-instead-of-apps/
- Microsoft Scout "addicted users" memo: https://windowsforum.com/threads/microsoft-scout-always-on-work-agent-openclaw-governance-security-risks.421703
- METR Frontier Risk Report: https://metr.org/blog/2026-05-19-frontier-risk-report
- Anthropic Fable 5 / Mythos: https://www.linkedin.com/posts/kai-t-williams_this-week-anthropics-internal-think-tank-activity-7468690513249107968-hqua
- MIT Tech Review / DeepMind / Millions of Agents: https://www.technologyreview.com/2026/06/11/1138794/google-deepmind-is-worried-about-what-happens-when-millions-of-agents-start-to-interact
- OpenClaw 2026.6.5: https://github.com/openclaw/openclaw/releases/tag/v2026.6.5
- OpenClaw 2026.5.26: https://github.com/openclaw/openclaw/releases/tag/v2026.5.26
- OpenClaw 2026.5.28: https://github.com/openclaw/openclaw/releases/tag/v2026.5.28
- OpenClaw-node 0.11.0: https://github.com/heypinchy/openclaw-node/releases/tag/v0.11.0
- openclaw-mcp-adapter: https://github.com/kriptoburak/openclaw-mcp-adapter

*End of papers-to-read.*
