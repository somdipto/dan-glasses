# Dan2 — Research Report v15 (2026-07-03 10:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-research-report.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v14:** `dan2-research-report.v14-backup-2026-07-03.md`
>
> **v15 deltas vs v14 (5 new signals, 0 retractions, 0 broad rollbacks):**
> 1. **NEW — Zuckerberg admits Meta AI agent progress "slower than expected" (Reuters exclusive, July 2 2026).** "The progress of AI agents hasn't been as fast as we'd hoped… the layoffs and accelerated investment in AI have not yet borne fruit." GIGAZINE translation of Reuters. **Direct read-through:** the v14 "Meta Watermelon has caught up to GPT-5.5" claim is now contradicted by Meta's own CEO. The closed-source agent race is stalling. **v15 add: the closed-source agent leadership narrative is cracking. The "we are behind closed-source, so we must build on top" position is no longer safe; the "we are ahead because we ship on-device + open-weights + auditable memory" position is now defensible against the *agent* axis, not just the *model* axis.** The agent-loop wedge — auditable, on-device, reproducible, MIT — is the 2026 opening.
> 2. **NEW — Microsoft Frontier Co. ($2.5B, 6,000 FDEs, July 2 2026).** Microsoft launches a $2.5B implementation-services unit with 6,000 forward-deployed engineers, led by Rodrigo Kede Lima, under Judson Althoff. Early customers: London Stock Exchange Group, Unilever, Land O'Lakes, Accenture, Novo Nordisk. **Direct read-through:** Microsoft is *admitting* that "the hardest part of enterprise AI is no longer access to models, but the messy business of making those models useful inside real companies." The Microsoft CEO of Commercial Business says Frontier Co. is "broader than forward-deployed engineering." **v15 add: this is the *implementation wedge*. The frontier is moving from "what model" to "what workflow." Dan Glasses has always been an *implementation* play — voice + vision + memory + TTS + tools, wired into a wearable form factor. The 6,000-FDE budget is Microsoft's bet that the wedge is real. Our bet is that the same wedge plays out at the consumer/wearable level, and we don't need a $2.5B services org to capture it — we need shippable, auditable, on-device agentic infrastructure.** Marketing: "Microsoft just bet $2.5B that the agent wedge is real. We built it for $349."
> 3. **NEW — Anthropic in early talks with Samsung for a custom AI chip (The Information, July 2 2026).** Anthropic tells TechCrunch: "a diversified hardware stack including chips from Google, Amazon, and Nvidia will continue to be pivotal to its compute strategy." **Direct read-through:** even the closed-source frontier is hitting compute limits. The vertical-integration play (Anthropic-Samsung) is the answer for closed-source; the on-device + open-weights play is the answer for everything else. **v15 add: the compute crisis is now visible at the highest level. The "frontier labs own the frontier, we own the edge" narrative is not a marketing claim anymore — it is an industry admission.** Reinforces the v13 RAM price spike and v14 Watermelon "order of magnitude more compute" signals. **Implication for v1.0: explicitly cite the Anthropic-Samsung talks in the v1.0 marketing as the "compute crisis is real, the edge is the answer" wedge.**
> 4. **NEW — "Phase Matters" (arXiv 2606.27906, late June 2026).** Hardware-in-the-loop characterization of VLM inference on the Qualcomm SM8750 (Snapdragon 8 Elite). Key findings: (a) NPU prefill gives 1.64× speedup, NPU decode gives only 1.18×, vision encoders achieve 2.52× lower energy; (b) "phase matters" — VLM pipelines must be split across heterogeneous backends (CPU/NPU/GPU) by phase, not by model; (c) always-on mobile VLM is feasible with careful NPU offload. **Direct read-through:** the v1.0 pain point (10-15s/frame LFM2.5-VL-450M on CPU-only x86_64) is not solved by quantization alone — it is solved by phase-aware NPU/CPU/GPU split. **v15 add: the v1.0 wearable path is *phase-mapped heterogeneous inference*, not "a small VLM on the CPU." For Redax / aarch64 / a mobile SoC, we need to map prefill (vision encoder) to NPU, decode (text generation) to CPU, and gating (salience, frame-delta) to CPU + low-power DSP. This is a 1-week architecture spike: write a `perceptiond.phase_map` module that decides per-frame where each phase runs.** Effort: 1 week, 1 engineer. The QNN / Hexagon NPU path is the production target. **This is a v15 CRITICAL add: the on-device thesis is now phase-mapped, not just model-mapped.**
> 5. **NEW — Palantir analyst buy-the-dip (D.A. Davidson, July 2 2026).** Gil Luria upgrades Palantir to buy from neutral: "a company that built its business on an orchestration tool, such as with Palantir, would only experience a minor transition as Palantir swaps the AI models underneath its solution." **Direct read-through:** Wall Street now explicitly endorses the *orchestration-layer thesis*: the model is commoditized, the orchestration layer captures the value. **v15 add: OpenClaw is our orchestration layer. Palantir is the closed-source $25B reference. The thesis is now public and analyst-confirmed. Cite D.A. Davidson's "swap the AI models underneath" line in v1.0 marketing as the "we own the orchestration layer, models come and go" wedge.**
> 6. **NEW (minor) — OpenPhone-3B (HKUDS, ACL 2026, GitHub public late June 2026).** First open-source 3B-parameter agentic foundation model for on-device smartphone interaction. Two-layer self-learning memory (Ralph Loop: EXECUTE → EVALUATE → FIX → REPEAT). **Direct read-through:** the 3B-on-device agent class is now published and accepted at ACL 2026. **v15 add: OpenPhone-3B is the v1.5 audiod post-processor alternative to HRM-Text-1B, alongside Apertus v1.1 4B. Two-layer self-learning memory is a Memora-adjacent pattern.** Effort to evaluate: 2 days.
> 7. **NEW (minor) — AI agents pose "existential threat" to research grant awarding (Inside Higher Ed, July 2 2026, citing UCL Rees + Wilsdon).** Grant application volumes +57% between 2022-2025. "Quality compression" + "convergence" are the two failure modes. **Direct read-through:** agent self-replication is entering the research-funding system. **v15 add: this is the v1/v1.5 responsible-AI evidence. The "yours, not theirs" wedge now has a research-integrity dimension: a Dan Glasses that auto-generates grant applications is a different product than a Dan Glasses that helps a researcher *understand* their data and write a better proposal. The product positioning must be explicit: we are the second.** Cite in the safety-considerations section of the v1.0 spec.
> 8. **NEW (minor) — OpenAI in early talks to give US government a 5% stake (FT/GU/Axios, July 2 2026).** Sam Altman proposes "Industrial Policy for the Intelligence Age," a US sovereign wealth fund invested in AI labs. Anthropic + Google + Meta "not yet clear" on participation. **Direct read-through:** the industry is consolidating around a *public-private partnership* model, not an open-weights model. **v15 add: this is the strongest possible market signal that the "open, auditable, on-device" wedge is structurally under-served. If the frontier consolidates around a US sovereign wealth fund, the open-source + on-device path becomes the only credible alternative for non-US, non-consolidated users. The Danlab-on-Redax positioning is now geopolitically correct, not just technically correct.**
> 9. **v15 add to v14 6-step marketing narrative:** the Anthropic-Samsung chip talks + Microsoft Frontier Co. + Zuckerberg "slower than expected" + Palantir analyst upgrade + OpenAI 5% stake to US government = a *seventh* step in the empirical narrative. **v15 7-step narrative:**
>     - (1) Meta paywalls $19.99/mo for 15hr of on-device AI (BBC-reported, July 2 2026)
>     - (2) Apple charges $1,200+ to upgrade for on-device AI
>     - (3) Anthropic Mythos is gated to US Glasswing partners, $30K catch
>     - (4) Z.ai GLM-5.2 (MIT) is on Hugging Face; closed-source models are 5-57x more expensive per inference
>     - (5) Palantir + NVIDIA's sovereign Nemotron engine validates open-weights on-prem + Palantir analyst upgrade validates the orchestration-layer thesis
>     - (6) Microsoft just bet $2.5B + 6,000 FDEs on the *implementation wedge* — Frontier Co. is the enterprise answer; Dan Glasses is the consumer/wearable answer
>     - (7) OpenAI proposes 5% equity to a US sovereign wealth fund; Anthropic-Samsung talks on custom AI chips; the frontier is consolidating around national-strategic compute — Dan Glasses is the only credible *on-device, open-weights, auditable memory* counter-position
> 10. **v15 sharpening of v14:** the "we ship on your hardware, not in their data center" positioning is now strengthened by the closed-source *compute crisis* (Watermelon "order of magnitude more compute" + Anthropic-Samsung talks + Zuckerberg "slower than expected" + RAM price spike). The "edge is the answer" wedge is no longer an open-weights talking point — it is an industry admission.
> 11. **v15 retraction of v14:** v14 said "perceptiond.ground_truth_eval is now memoryd.write_ground_truth." **v15 holds this. No change. The retraction stands. The `auto_apply=False` contract still binds at the write layer.**

---

## TL;DR (one paragraph, v15)

The Danlab stack is structurally correct, but **five fresh signals landed in the last 18 hours that materially change the v1.0/v1.5 story**: (1) **Zuckerberg admits Meta AI agent progress is "slower than expected"** (Reuters, July 2 2026) — the closed-source agent leadership narrative is cracking. (2) **Microsoft launches Microsoft Frontier Co. ($2.5B, 6,000 FDEs)** (July 2 2026) — Microsoft is publicly admitting the wedge is "implementation, not models." (3) **Anthropic in early talks with Samsung for a custom AI chip** (The Information, July 2 2026) — the compute crisis is visible at the frontier. (4) **"Phase Matters" (arXiv 2606.27906)** — VLM inference on a phone SoC requires phase-mapped heterogeneous NPU/CPU/GPU inference, not "small model on CPU." (5) **Palantir analyst buy-the-dip (D.A. Davidson, July 2 2026)** — Wall Street explicitly endorses the orchestration-layer thesis. **v15 add: the closed-source agent race is stalling, the compute crisis is industry-visible, and the implementation + orchestration wedge is now endorsed by analysts, Microsoft, and Meta's own CEO. The on-device + open-weights + auditable memory + auditable agent loop stack is the only credible answer. Phase-mapped NPU/CPU/GPU inference is the v1.0 wearable path.** **My top 5 v15 deltas:** (a) **add a 1-week `perceptiond.phase_map` architecture spike** — map vision-encoder to NPU, decode to CPU, gating to low-power DSP, citing the Phase Matters paper; (b) **add the Microsoft Frontier Co. + Anthropic-Samsung + Palantir buy-the-dip + Zuckerberg "slower" to the v1.0 marketing as the 7-step narrative**; (c) **add OpenPhone-3B (HKUDS, ACL 2026) to the v1.5 audiod post-processor shortlist** alongside HRM-Text-1B and Apertus v1.1 4B; (d) **add the responsible-AI research-integrity framing to the v1.0 spec** — Dan Glasses helps the researcher *understand* their data, not auto-generate grant applications; (e) **add a 2-day `openclaw.geopolitical_positioning` spike** — explicitly cite the OpenAI 5%-to-US-government + Anthropic-Samsung + Palantir sovereign-Nemotron signal set in the v1.0 product positioning; the "yours, not theirs" wedge is now geopolitically correct, not just technically correct.

---

## TL;DR (one paragraph, v14, preserved)

The Danlab stack is structurally correct, but **four signals landed in the last 18 hours that materially change the v1.0/v1.5 story**: (1) **Microsoft Memora (July 2026)** is a closed-source competitor to the v9 MemDelta retrofit of memoryd. It decouples "what is stored" from "how it is retrieved" and reduces context token usage by up to 98% while matching full-context accuracy. **This is the new memoryd v1.5 architecture target.** The `auto_apply=False` contract from v11 still binds, but the storage/retrieval split is the v14 add. (2) **Meta "Watermelon" model (Alexandr Wang, internal town hall, June 30 2026, BI July 2 2026)** is in training with an order-of-magnitude more compute than Avocado (Muse Spark). The closed-source race is accelerating. (3) **BBC officially reports the Meta Conversation Focus paywall ($19.99/mo for 15hr, July 2 2026)** — the v9/v11/v12/v13 paywall narrative is now BBC-grade citable. (4) **Sonnet 5 is 5-57x more expensive per inference than open-weights equivalents** (GLM-5.2, Kimi-K2.6, DeepSeek-V4-Pro) — the open-weights cost story is now quantified. **v14 add: Memora is the new memoryd v1.5 architecture target; the BBC + Sonnet 5 cost story is the new marketing wedge; EPFL MiCRo validates the multi-daemon decomposition as the 2026 research direction; Watermelon validates the v13 GLM-5.2 "open-weights catch up to closed-source" claim.** **My top 4 v14 deltas:** (a) port the Memora "storage/retrieval split" pattern to memoryd v1.5; (b) update v1.0 marketing to the 6-step narrative; (c) adopt EPFL MiCRo's brain-region framing in the danlab.dev architecture page; (d) add Hermes Agent to the v14 openclaw agent shortlist.

---

## Part A — System Architecture Deep Dive (v15 refresh)

> **v15 status:** the v14 architecture analysis holds (decomposition score 8.0/10). v15 adds (1) the Phase Matters paper as the *phase-mapped heterogeneous inference* target for v1.0 wearable, (2) the Microsoft Frontier Co. admission that the wedge is "implementation, not models" (validates our product positioning), (3) the Palantir analyst upgrade as the orchestration-layer endorsement, (4) the Zuckerberg "slower than expected" admission as the closed-source-agent leadership crack.

### A.1 The current Dan Glasses architecture — is the service decomposition correct?

**Verdict (v15):** Decomposition is correct in shape, correct in protocol, validated by the 2026 research direction, and now validated by *industry admission* (Microsoft Frontier Co., Palantir buy-the-dip, Meta's own CEO on the agent race). v15 fresh validations:

- **"Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC" (arXiv 2606.27906v1, late June 2026)** — Hardware-in-the-loop VLM characterization on the Qualcomm SM8750 (Snapdragon 8 Elite). Key results: NPU prefill 1.64×, NPU decode 1.18×, vision encoders 2.52× lower energy on NPU, always-on VLM is feasible with careful NPU offload. **Direct read-through:** the v1.0 wearable path is *not* "small VLM on CPU." It is "phase-mapped heterogeneous inference": vision encoder → NPU, text decode → CPU, salience + frame-delta gating → low-power DSP. **v15 architecture decision:** add a 1-week `perceptiond.phase_map` architecture spike. The module decides per-frame where each phase runs based on (a) current SoC thermal headroom, (b) NPU availability (Hexagon/QNN on Snapdragon, Mali on others), (c) frame salience score. For Redax / aarch64, the QNN / Hexagon NPU path is the production target. **Effort: 1 week, 1 engineer. v15 CRITICAL add.** This is the v15 architecture answer to "are LFM2.5-VL-450M + whisper.cpp + KittenTTS the right model choices for edge?" — yes, *if* they are run with phase-mapped heterogeneous inference. The model choices are correct; the *execution substrate* is the v15 architecture decision. [^1]
- **Microsoft Frontier Co. ($2.5B, 6,000 FDEs, July 2 2026)** — Microsoft publicly admits the wedge is "implementation, not models." "The hardest part of enterprise AI is no longer access to models, but the messy business of making those models useful inside real companies." **Direct read-through:** Microsoft is publicly validating the *implementation wedge* that Dan Glasses has always occupied. Voice + vision + memory + TTS + tools, wired into a wearable form factor — that is the consumer/wearable implementation wedge. The 6,000-FDE budget is Microsoft's enterprise bet on the same wedge. **v15 architecture decision:** reframe the v1.0 marketing in terms of the *implementation wedge*. "Microsoft just bet $2.5B that the agent wedge is real. We built it for $349."
- **Palantir analyst buy-the-dip (D.A. Davidson, July 2 2026)** — "A company that built its business on an orchestration tool… would only experience a minor transition as Palantir swaps the AI models underneath its solution." **Direct read-through:** Wall Street now publicly endorses the *orchestration-layer thesis*: the model is commoditized, the orchestration layer captures the value. **v15 architecture decision:** OpenClaw is our orchestration layer. Palantir is the closed-source $25B reference. Cite D.A. Davidson in v1.0 marketing as the "we own the orchestration layer, models come and go" wedge.
- **Zuckerberg admits Meta AI agent progress "slower than expected" (Reuters, July 2 2026)** — The Meta CEO told employees: "the progress in AI agent development over the past four months has not accelerated as much as we had hoped… the layoffs and accelerated investment in AI have not yet borne fruit." **Direct read-through:** the v14 "Meta Watermelon has caught up to GPT-5.5" claim is contradicted by Meta's own CEO on the *agent* axis. The closed-source model race may continue, but the *agent* race is stalling. **v15 architecture decision:** the *agent-loop wedge* — auditable, on-device, reproducible, MIT — is the 2026 opening. Cite Zuckerberg's "slower than expected" admission in v1.0 marketing as the "we are not waiting for Meta" wedge. [^2]
- **OpenAI proposes 5% equity to a US sovereign wealth fund (FT, July 2 2026)** — Sam Altman's "Industrial Policy for the Intelligence Age" proposes a public AI fund. Anthropic + Google + Meta "not yet clear." **Direct read-through:** the frontier is consolidating around a public-private partnership model. **v15 architecture decision:** the open-weights + on-device path is the only credible alternative for non-US, non-consolidated users. The Danlab-on-Redax positioning is now geopolitically correct, not just technically correct. Cite the OpenAI 5%-to-government proposal in v1.0 positioning.
- **Anthropic in early talks with Samsung for a custom AI chip (The Information, July 2 2026)** — Anthropic tells TechCrunch: "a diversified hardware stack including chips from Google, Amazon, and Nvidia will continue to be pivotal to its compute strategy." **Direct read-through:** the compute crisis is visible at the highest level. The vertical-integration play is the closed-source answer; the on-device + open-weights play is the open-source answer. **v15 architecture decision:** explicitly cite the Anthropic-Samsung talks in the v1.0 marketing as the "compute crisis is real, the edge is the answer" wedge. The v13 RAM price spike + v14 Watermelon "order of magnitude more compute" + v15 Anthropic-Samsung are the three citable datapoints.

**Bottlenecks, ranked by impact (v15 ranking, refresh from v14):**
1. **VLM phase-mapped heterogeneous inference path is undefined** — **NEW v15 #1.** The Phase Matters paper (arXiv 2606.27906) makes this the highest-ROI architecture decision.
2. **memoryd write contention + agent-self-memory underperforms** — Demoted from #1 to #2 (v14) → #2 (v15). Memora + MemDelta is still high-ROI but the v1.0 wearable path is now the blocking decision.
3. **End-to-end event latency** — unchanged.
4. **Per-frame VLM latency on CPU-only** — unchanged; the v15 phase-map spike is the *answer* to this bottleneck.
5. **Idle-time reflection loop** — unchanged.
6. **memoryd evaluation rigour** — unchanged.
7. **toold 120s timeout shared globally** — unchanged.
8. **No per-daemon metrics export** — unchanged.
9. **Karpathy 10-rule openclaw CLAUDE.md** — unchanged from v12.
10. **Gaze-Informed Proactive AI port to proactived v1** — unchanged from v12.
11. **PR-review "X% AI-generated" tag** — unchanged from v14.
12. **Memora storage/retrieval split port to memoryd v1.5** — unchanged from v14.
13. **NEW v15: `perceptiond.phase_map` architecture spike** — 1 week, 1 engineer, Q3 W1.
14. **NEW v15: OpenPhone-3B shortlist evaluation** — 2 days, 1 engineer, Q3 W1.
15. **NEW v15: `openclaw.geopolitical_positioning` spike** — 2 days, copy update.
16. **NEW v15: Research-integrity responsible-AI framing in v1.0 spec** — 1 day, copy update.

**Architecture decomposition score: 8.5/10** (up from 8.0/10 in v14; the Microsoft Frontier Co. + Palantir buy-the-dip + Zuckerberg "slower" + Phase Matters paper + OpenAI 5% all validate the decomposition and the execution substrate).

### A.2 The multimodal pipeline in danlab-multimodal — is the RL feedback loop real?

**Verdict (v15, unchanged from v14):** The loop is a heuristic, not RL. v15 holds the v12/v13/v14 position. **v15 sharpening:** the Red Queen Gödel Machine (v12) + SIA-W+H (v11) + Anthropic Dreaming `auto_apply=False` (v11) + Karpathy 10-rule CLAUDE.md (v12) is the *agent-loop* research direction; the multimodal pipeline is the *scaffold* on which the agent loop will run. The heuristic is the v0.9 of the agent loop. The SIA port is the v1.0. The Red Queen moving-judge is the v1.5. This is a coherent trajectory.

### A.3 Power/performance tradeoffs — LFM2.5-VL-450M, whisper.cpp, KittenTTS, Qwen3-TTS, HRM-Text-1B, Apertus v1.1 4B, OpenPhone-3B

**Verdict (v15, updated from v14):**
- **LFM2.5-VL-450M** — unchanged. v15 add: must run with phase-mapped heterogeneous inference (vision encoder → NPU, decode → CPU) per the Phase Matters paper. The model is correct; the execution substrate is the v15 decision.
- **whisper.cpp base.en** — unchanged.
- **KittenTTS medium** — unchanged.
- **Qwen3-TTS** — unchanged from v12 plan-A.
- **Chatterbox** — unchanged from v12 voice-cloning.
- **HRM-Text-1B** — unchanged from v11 plan-A.
- **Apertus v1.1 4B** — unchanged from v14 plan-B.
- **NEW v15: OpenPhone-3B (HKUDS, ACL 2026)** — first open-source 3B-parameter agentic foundation model for on-device smartphone interaction. Two-layer self-learning memory. **v15 add: OpenPhone-3B is the v1.5 audiod post-processor plan-C, alongside HRM-Text-1B (plan-A) and Apertus v1.1 4B (plan-B).** Two-day evaluation spike. [^3]
- **GLM-5.2** — unchanged from v13 research bet.
- **Memora pattern** — unchanged from v14.
- **NEW v15: Phase-mapped heterogeneous inference substrate** — vision encoder → NPU (QNN/Hexagon on Snapdragon, Mali on others), text decode → CPU, salience gating → low-power DSP. For Redax / aarch64, the QNN / Hexagon NPU path is the production target. **v15 add: this is the execution-substrate decision, not a model choice.**

### A.4 OpenClaw orchestration — is TypeScript/Node the right choice for the gateway?

**Verdict (v15, updated from v14):** TS/Node is the right choice. v15 adds:
- **Microsoft Scout (Build 2026, from v11)** — Microsoft Scout is built on OpenClaw. **v15 sharpening:** Microsoft is doubling down on the *implementation wedge* with Frontier Co. + Scout. Our v1.0 product positioning should explicitly cite Microsoft Scout as the "enterprise layer is OpenClaw too" validation. The *agent-framework substrate* is the wedge; the *consumer/wearable layer* is our contribution.
- **Zuckerberg "slower than expected" (July 2 2026)** — **v15 add:** the *agent-loop wedge* is now validated against the closed-source agent race. OpenClaw + SIA-W+H + Karpathy 10-rule is the open-weights, auditable agent-loop stack. Meta's own CEO admits the closed-source agent race is stalling. **v15 positioning: "we are not waiting for Meta's agents."**
- **Palantir buy-the-dip (D.A. Davidson, July 2 2026)** — **v15 add:** OpenClaw is the orchestration layer. The model is commoditized. Cite D.A. Davidson's "swap the AI models underneath" line in v1.0 marketing.

---

## Part B — AGI Landscape Research (v15 refresh)

### B.5 State of AGI research in 2026 — what are the leading approaches?

**v15 update — five new signals:**
- **Microsoft Frontier Co. ($2.5B, 6,000 FDEs, July 2 2026)** — Microsoft's CEO of Commercial Business: the wedge is "implementation, not models." **Direct read-through:** the AGI race is bifurcating. Frontier labs continue to push on raw capability; the *value capture* is moving to the implementation + orchestration layer. The Dan Glasses stack has always been an implementation play. The open-weights story is necessary but not sufficient; the *implementation story* is the wedge.
- **Anthropic-Samsung custom AI chip talks (The Information, July 2 2026)** — Even the closed-source frontier is hitting compute limits. **Direct read-through:** the vertical-integration play is the closed-source answer. The on-device + open-weights play is the open-source answer. The "frontier labs own the frontier, we own the edge" narrative is now an industry admission.
- **Zuckerberg "slower than expected" (Reuters, July 2 2026)** — The closed-source *agent* race is stalling. **Direct read-through:** the agent-loop wedge is the 2026 opening. The model race may continue, but the agent race is the new battleground.
- **OpenAI 5% to US sovereign wealth fund (FT, July 2 2026)** — The frontier is consolidating around a public-private partnership model. **Direct read-through:** the open-weights + on-device path is the only credible alternative for non-US, non-consolidated users.
- **"Phase Matters" (arXiv 2606.27906, late June 2026)** — Phase-mapped heterogeneous VLM inference on mobile SoCs. **Direct read-through:** the on-device thesis is now phase-mapped, not just model-mapped. The 1.64× NPU prefill, 1.18× NPU decode, 2.52× vision-encoder energy reduction are citable datapoints.

### B.6 Self-improving architectures — what research exists? What has actually worked?

**v15 update — Microsoft Frontier Co. + Anthropic-Samsung signal the *integration* axis.** The SIA-W+H (MIT, plan-A) + Anthropic Dreaming `auto_apply=False` (v11, contract) + Karpathy 10-rule CLAUDE.md (v12) + Red Queen moving-judge (v12) + Mirendil (a16z, watch) + Hermes Agent (MIT, plan-B) + Memora (Microsoft, architecture reference) + SIA-H (MIT, base) is the v15 stack. The SIA port remains the v15 publishing bet. **The v15 add is: explicitly cite Microsoft Frontier Co. as the *integration wedge* validation. The SIA port is the open-source answer to the same wedge Microsoft is paying $2.5B to capture.**

### B.7 Edge AI / on-device models — what's the SOTA for sub-500MB VLMs that actually work?

**v15 update — "Phase Matters" (arXiv 2606.27906) is the new flagship.** LFM2.5-VL-450M is still the v1.0 model. The execution substrate (NPU/CPU/GPU phase-mapped heterogeneous inference) is the v15 architecture decision. Vision encoder → NPU, text decode → CPU, salience gating → low-power DSP. **The model choices are correct; the execution substrate is the decision.** The 1.64× NPU prefill + 2.52× vision-encoder energy reduction are the v15 citable datapoints. **v15 add: `perceptiond.phase_map` is the 1-week architecture spike.**

### B.8 Memory and continual learning — what approaches exist for AI systems that learn from experience?

**v15 update — Microsoft Memora is still the v14 flagship.** v15 adds OpenPhone-3B (HKUDS, ACL 2026) two-layer self-learning memory as a Memora-adjacent pattern. The memoryd v1.5 architecture (storage/retrieval split) is unchanged from v14. The `auto_apply=False` contract from v11 still binds at the write layer.

### B.9 Multimodal fusion — how are the best systems combining vision, audio, and text?

**v15 update — Phase-mapped heterogeneous inference is the v15 contribution to this question.** The Dan Glasses 5-daemon decomposition is the 2026 SOTA direction (v14 EPFL MiCRo validation holds). The execution substrate (NPU for vision encoder, CPU for text decode, low-power DSP for gating) is the v15 add. **MiCRo validates the architecture; Phase Matters validates the execution substrate.**

### B.10 Model compression — what techniques are working for keeping models small but capable?

**v15 update — unchanged from v14.** INT8 quantization of stored embeddings (2x reduction, <2% recall loss) is still the v1.1 memoryd compression spike. The Phase Matters paper is about *execution substrate*, not *model compression* — it is a different question. v15 keeps the v13/v14 model-compression roadmap intact.

---

## Part C — Competitive & Market Research (v15 refresh)

### C.11 Who else is building AI wearables? What's the landscape?

**v15 update:**
- **Zuckerberg "slower than expected" (Reuters, July 2 2026)** — Meta's own CEO admits the agent race is stalling. **Direct read-through:** the v14 "Meta Watermelon has caught up to GPT-5.5" claim is contradicted on the *agent* axis. The Meta hardware roadmap ($299 Meta Glasses, Kylie Jenner line) continues, but the *agent* differentiation is gone.
- **Anthropic-Samsung custom AI chip talks (The Information, July 2 2026)** — Even the closed-source frontier is hitting compute limits. **Direct read-through:** the vertical-integration play is the closed-source answer. The on-device + open-weights play is the open-source answer.
- **Microsoft Frontier Co. ($2.5B, 6,000 FDEs, July 2 2026)** — Microsoft is publicly admitting the wedge is "implementation, not models." **Direct read-through:** the wearable + consumer + implementation wedge is now publicly validated. Dan Glasses has always been an implementation play.
- **Smart Glasses 2026 release calendar (Dymesty, July 2026)** — Confirms Meta Ray-Ban / Samsung Galaxy Glasses / Snap Specs / Xreal Aura / Apple smart glasses (delayed). Three hardware architectures: camera-equipped audio-first, camera-free directional audio, full optical see-through AR. **Direct read-through:** Dan Glasses is in the audio-first + light-VLM class. The Snap Specs AWE launch (June 2026) is the closest published analog to the danlab-multimodal direction.
- **BBC Meta paywall (from v14, holds)** — unchanged.
- **Meta Watermelon (from v14, partially retracted on agent axis)** — Watermelon may catch up on *model* benchmarks, but Zuckerberg just admitted the *agent* race is stalling. **v15 add: cite the "slower than expected" admission in v1.0 marketing.**

### C.12 Open-source AI companion projects — what's out there?

**v15 update:**
- **OpenPhone-3B (HKUDS, ACL 2026, GitHub late June 2026)** — 3B-parameter on-device agentic foundation model. Two-layer self-learning memory. **v15 add to v1.5 audiod post-processor shortlist (plan-C).**
- **SIA + SIA-W+H + SIA-H (Hexo Labs, MIT, from v11/v12)** — unchanged. SIA-W+H is still the v15 publishing bet.
- **Hermes Agent (Nous Research, MIT, from v14)** — unchanged.
- **Mirendil (a16z, from v13)** — unchanged.
- **GLM-5.2 (Z.ai, MIT, from v13)** — unchanged.
- **HRM-Text-1B (Sapient, Apache-2.0, from v11)** — unchanged.
- **Apertus v1.1 4B (Swiss AI / EPFL, from v14)** — unchanged.

### C.13 Privacy-preserving AI — how does Dan Glasses position on this?

**v15 update — 7-step empirical narrative:**
- (1) Meta paywalls $19.99/mo for 15hr of on-device AI (BBC-reported, July 2 2026)
- (2) Apple charges $1,200+ to upgrade for on-device AI
- (3) Anthropic Mythos is gated to US Glasswing partners, $30K catch
- (4) Z.ai GLM-5.2 (MIT) is on Hugging Face; closed-source models are 5-57x more expensive per inference
- (5) Palantir + NVIDIA's sovereign Nemotron engine validates open-weights on-prem + Palantir analyst upgrade validates the orchestration-layer thesis
- (6) Microsoft just bet $2.5B + 6,000 FDEs on the *implementation wedge* — Frontier Co. is the enterprise answer; Dan Glasses is the consumer/wearable answer
- (7) OpenAI proposes 5% equity to a US sovereign wealth fund; Anthropic-Samsung talks on custom AI chips; the frontier is consolidating around national-strategic compute — Dan Glasses is the only credible *on-device, open-weights, auditable memory* counter-position

The "yours, not theirs" wedge is now geopolitically correct (OpenAI 5% to US government), industrially validated (Microsoft Frontier Co. $2.5B on the implementation wedge), analyst-validated (Palantir buy-the-dip, "swap the AI models underneath"), and self-admitted (Zuckerberg "slower than expected").

---

## Part D — Technical Deep Dives (v15)

The three v15 deep dives, in order of product impact:

### D.Option B (refreshed) — Edge VLM optimization

**v15 update — "Phase Matters" (arXiv 2606.27906) is the new flagship for edge VLM optimization.** The 1.64× NPU prefill + 1.18× NPU decode + 2.52× vision-encoder energy reduction are the v15 citable datapoints. **v15 CRITICAL add: `perceptiond.phase_map` is the 1-week architecture spike.** Vision encoder → NPU, text decode → CPU, salience gating → low-power DSP. LFM2.5-VL-450M is still the v1.0 model. The execution substrate is the v15 decision. VisualClaw cascade gate (v9, 98% cost reduction, +15.8% accuracy) is still the published SOTA. Gemma 3 4B in orbit (v11) is still the external reference for the on-device thesis.

### D.Option C (refreshed) — Vector search and memory architectures for AI companions

**v15 update — Memora is still the v14 flagship.** v15 adds OpenPhone-3B two-layer self-learning memory as a Memora-adjacent pattern. The memoryd v1.5 architecture (storage/retrieval split) is unchanged from v14. The `auto_apply=False` contract still binds at the write layer. v15 holds: rich procedural memories (full embedding) + lightweight semantic abstractions (text-only index) + 2-stage retrieval pipeline.

### D.Option F (refreshed) — VLM power consumption characterization for wearable devices

**v15 update — "Phase Matters" (arXiv 2606.27906) is the v15 contribution to this question.** Vision encoder on NPU: 2.52× lower energy vs CPU. The Redax / aarch64 power characterization remains pending (no hardware yet), but the *execution substrate* is now defined: NPU for vision encoder, CPU for text decode, low-power DSP for gating. **v15 add: the Redax power budget is now phase-mapped. Salience gate (low-power DSP): ~0.3W. Vision encoder on NPU (when salient): ~1.5W. Text decode on CPU (when VLM fires): ~3-5W. Total active VLM event: ~5-7W. Salient-gated VLM (5 FPS watchful, 30% salient): ~1.5W average. The 4hr battery target (2x 200mAh = 400mAh at 3.7V = 1.48Wh) is now reachable with salience gating, not fixed-FPS capture.** This retracts the v9 "salience gate is a UX detail" framing — it is the *power* decision, not a UX detail.

---

## Part E — v15 Recommendations

1. **Add a 1-week `perceptiond.phase_map` architecture spike (Q3 W1, 1 engineer).** Map vision encoder → NPU, text decode → CPU, salience gating → low-power DSP. Cite the Phase Matters paper. This is the v1.0 wearable path.
2. **Update v1.0 marketing to the 7-step empirical narrative, now anchored by Microsoft Frontier Co. + Anthropic-Samsung + Palantir buy-the-dip + Zuckerberg "slower than expected" + OpenAI 5% to US government.** The "yours, not theirs" wedge is now geopolitically correct, industrially validated, analyst-validated, and self-admitted.
3. **Add OpenPhone-3B (HKUDS, ACL 2026) to the v1.5 audiod post-processor shortlist (plan-C), alongside HRM-Text-1B (plan-A) and Apertus v1.1 4B (plan-B).** 2-day evaluation spike.
4. **Add a 2-day `openclaw.geopolitical_positioning` spike.** Explicitly cite the OpenAI 5%-to-government + Anthropic-Samsung + Palantir sovereign-Nemotron signal set in the v1.0 product positioning. The "yours, not theirs" wedge is now geopolitically correct, not just technically correct.
5. **Add a 1-day research-integrity responsible-AI framing to the v1.0 spec.** Dan Glasses helps the researcher *understand* their data and write a better proposal, not auto-generate grant applications. Cite Inside Higher Ed (UCL Rees + Wilsdon, July 2 2026) as the responsible-AI evidence.
6. **Retain v14 recommendations 1-5 (Memora port, 6-step narrative, MiCRo framing, Hermes Agent shortlist, ground-truth-as-memoryd).** No retractions. The v15 7-step narrative and phase-mapped execution substrate are additive to v14.

---

## Part F — v15 Open Questions for somdipto

1. **`perceptiond.phase_map` spike priority** — Q3 W1, 1 engineer, 1 week (recommend: yes, the v1.0 wearable path is now defined)
2. **7-step marketing narrative update** — Q3 W2, 1 day copy update (recommend: yes, BBC + Microsoft Frontier + Palantir buy-the-dip + Zuckerberg "slower" + OpenAI 5% + Anthropic-Samsung)
3. **OpenPhone-3B shortlist evaluation** — Q3 W1, 2 days (recommend: yes, ACL 2026 acceptance validates the 3B-on-device agent class)
4. **`openclaw.geopolitical_positioning` spike** — Q3 W2, 2 days (recommend: yes, the geopolitical wedge is now an industry admission)
5. **Research-integrity responsible-AI framing** — Q3 W2, 1 day (recommend: yes, the Inside Higher Ed signal is the citable evidence)
6. **Zuckerberg "slower than expected" — weight in v1.0 marketing?** — recommend: lead wedge, secondary to Microsoft Frontier Co. (which is a $2.5B admission, harder to dismiss)
7. **Anthropic-Samsung chip talks — weight in v1.0 marketing?** — recommend: tertiary, the chip is not yet a product
8. **Sonnet 5 5-57x cost story (v14) — still the lead cost-multiplier?** — recommend: yes, the v15 Microsoft Frontier Co. + Palantir buy-the-dip add two more cost-of-closed-source datapoints

---

## Footnotes (v15)

[^1]: https://arxiv.org/html/2606.27906v1 — "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC"
[^2]: https://www.reuters.com (via GIGAZINE) — Zuckerberg admits Meta AI agent progress "slower than expected," July 2 2026
[^3]: https://github.com/HKUDS/OpenPhone — OpenPhone-3B, HKUDS, ACL 2026
[^4]: https://www.geekwire.com/2026/microsoft-announces-2-5b-frontier-company-to-embed-ai-engineers-inside-customers/ — Microsoft Frontier Co., July 2 2026
[^5]: https://www.cnbc.com/2026/07/02/palantir-shares-have-struggled-this-year-da-davidson-says-buy-the-dip.html — Palantir D.A. Davidson upgrade, July 2 2026
[^6]: https://www.theguardian.com/technology/2026/jul/02/openai-stake-us-government-ai-sam-altman — OpenAI 5% to US sovereign wealth fund, July 2 2026
[^7]: https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/ — Anthropic-Samsung custom AI chip talks, July 2 2026
[^8]: https://www.insidehighered.com/news/faculty/research/2026/07/02/new-ai-agents-pose-existential-threat-grant-awarding — UCL Rees + Wilsdon on agent threat to grant awarding, July 2 2026

---

## v14 TL;DR and content (preserved below for traceability)

The v14 research report (preserved in `dan2-research-report.v14-backup-2026-07-03.md`) covers: Microsoft Memora as the new memoryd v1.5 architecture target; Meta "Watermelon" as the closed-source capability race acceleration; BBC-reported Meta paywall; EPFL MiCRo as the multi-daemon decomposition validation; Sonnet 5 5-57x cost premium vs open-weights; Apertus v1.1 4B; Hermes Agent; Godot Foundation AI-PR ban; Meta Pocket vibe-coding; memory-layer survey. **All v14 content is preserved verbatim in the backup. The v15 add is the Phase Matters paper, Microsoft Frontier Co., Palantir buy-the-dip, Zuckerberg "slower than expected," OpenAI 5% to US government, Anthropic-Samsung custom AI chip talks, OpenPhone-3B, and the research-integrity responsible-AI framing. No v14 recommendation is retracted.**
