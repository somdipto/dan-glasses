# Top Papers to Read — Dan2 v38 (2026-06-22 11:30 IST)

> **Scope.** v38 swaps the focus from "self-improving loops" (v37) to **proactive AI architecture** (the v38 wedge-response) and **edge VLM power characterization** (the v1.5 path). The five papers here are the ones that **change Danlab's roadmap if they hold up under read.** Each entry: claim, evidence, why-it-matters, where-it-lands-in-Danlab, what-to-verify.

---

## 1. **Nanomind: A Software-Hardware Co-Design for Efficient Multimodal Inference on Battery-Powered Small Devices** (arXiv:2510.05109v6, 2026)

**Claim:** LLaVA-OneVision-Qwen2-0.5B + camera runs continuously at **0.375W**, achieving **18.8h on a 2000 mAh battery**. The architecture decomposes the VLM into modular components (vision encoder, projector, language decoder, audio) and maps each to the most suitable accelerator (NPU, GPU, DSP) on modern SoCs. Token-Aware Buffer Manager (TABM) enables zero-copy embedding transfer across accelerators.

**Evidence:** Published in 2026 with measured power, latency, and battery-life numbers on a real 2000 mAh prototype. The cascade pattern reduces end-to-end energy by 42.3% vs mainstream edge frameworks.

**Why it matters for Danlab:** **This is the closest published benchmark to what Dan Glasses v1.5 needs.** v34 said "5W average for 4h." Nanomind says 0.4W for 18h. That's a **22× efficiency gain** from cascade scheduling + accelerator-aware dispatch + sub-byte quantization. The wearable form-factor constraint (battery, weight, thermals) **collapses** if we adopt this pattern.

**Where it lands in Danlab:**
- `perceptiond v1.5`: LFM2.5-VL-450M + Nanomind-style cascade on GAP9 or Snapdragon AR1.
- `dan2-architecture-review.v38.md` §4.2: anchor for the wearable power budget.
- `dan2-model-analysis.v38.md` §1.1: cascade as the v1.5 vision model plan.

**What to verify:** Reproduce the cascade scheduling on a GAP9 dev kit (~$300). Compare measured power vs the paper's claim on a Dan Glasses-relevant workload (face detection + LFM2.5-VL description, not LLaVA-OneVision captioning).

---

## 2. **ProAct: Anticipate and Learn — Unleashing Idle-Time Compute in Proactive Agents** (arXiv:2605.25971v1, 2026)

**Claim:** A proactive agent architecture that uses idle time between user interactions to anticipate and fulfill likely upcoming needs, **rather than waiting for explicit prompts**. Combines Future-State Prediction (dialogue history + persistent memory + user profiles) with Idle-Time Acquisition (selective background computation).

**Evidence:** ProActEval benchmark (200 scenarios across 40 domains) shows:
- **+14.8% faster task completion**
- **+11.7% lower user effort**
- **-28.1% fewer hallucinations** vs reactive baselines

**Why it matters for Danlab:** **This is the empirical backing for the "proactive AI" wedge.** v37 said Snap claimed the category. v38 reclaims it: Snap has a marketing claim with no published eval. We have ProAct's 14.8/11.7/28.1 numbers. **dglabs-eval v1's proactive subset = 5 tasks derived from ProActEval + ProAct's pattern of Future-State Prediction + Idle-Time Acquisition.**

**Where it lands in Danlab:**
- `dglabs-eval v1 proactive subset`: 5 tasks (carry-a-key-spotted, repeat-customer-recall, future-meeting-pre-read, unfinished-task-nudge, spatial-context-trigger).
- `proactived` service (v1.5, new in v38): Future-State Prediction + Idle-Time Acquisition pattern.
- `memoryd v2`: integrate ProAct's persistent memory (user profiles + summaries + facts + unresolved gaps) with our existing episodic/semantic/procedural model.

**What to verify:** Reproduce ProActEval's 14.8% on a Dan Glasses-relevant subset. The paper uses GPT-4 class; we need to confirm the 14.8% holds with LFM2.5-1.2B-Thinking as the future-state predictor (it should, but measure).

---

## 3. **MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents** (arXiv:2605.28046v1, 2026)

**Claim:** Shifts from "Memory-as-Tool" (one-shot retrieval of flat passages) to "Memory-as-Cognition" (memory access integrated into reasoning). Three components: Navigable Memory Store (structured with associative link graphs), Cross-Dimensional Navigation Interface (multi-granularity actions), Proactive Reasoning Protocol (agents proactively explore memory from context).

**Evidence:** ProactiveMemBench (first proactive-memory benchmark) SOTA. LoCoMo ~93, LongMemEval ~96. **Outperforms passive QA baselines on ProactiveMemBench.**

**Why it matters for Danlab:** **This is the v2.0 memory architecture.** Our current memoryd v1 is flat-cosine retrieval. MemCog's "navigable memory store + cross-dimensional navigation" is what we want for the cognitive-hierarchy path (DCPM-style System 2). v34's Mnemosyne is the bar; MemCog is the ceiling we're targeting.

**Where it lands in Danlab:**
- `memoryd v2 v1.0` (Sept 2026): add MemCog-style "navigable memory store" alongside our existing 3-type (episodic/semantic/procedural) store. Cross-dimensional navigation via LLM.
- `memoryd v2 v2.0` (Dec 2026): add proactive reasoning protocol. Agents trigger memory exploration without user query.
- `dglabs-eval v1 memory subset`: LongMemEval-equivalent task. Target 80% (vs Letta 83.2% SOTA).

**What to verify:** Reproduce LoCoMo 93 on a memoryd-relevant subset. Confirm that "navigable memory store" doesn't require a 7B-class LLM (the paper uses GPT-4; we need 1.2B-class).

---

## 4. **OpenGlass: Ultra-Low-Power On-Device AI Eyewear with Event-based Vision** (arXiv:2606.07431, 2026)

**Claim:** An open-source smart-glasses platform that runs real-time on-device ML within a **sub-100 mW envelope**. GAP9 RISC-V SoC + NE16 accelerator + sub-byte quantization. Demonstrated endurance: **11.5 hours of continuous on-device ML inference from a 200 mAh battery at 13-14 Hz gesture recognition; 67.4 mW steady-state, 5.2 mJ per inference cycle**.

**Evidence:** End-to-end measured power + battery life on a real 200 mAh wearable prototype with modular FPC interposer for camera swap.

**Why it matters for Danlab:** **This is the silicon reference for "v1.5 wearable, no cloud."** GAP9 + event camera is one of three hardware paths in v38's decision tree (alongside Snapdragon AR1 and Alif B1). The 11.5h on 200 mAh is the published benchmark to beat.

**Where it lands in Danlab:**
- `dan2-research-report.v38.md` §1.4: edge VLM power table.
- `dan2-architecture-review.v38.md` §4.2: GAP9 as hardware pivot option.
- `perceptiond v1.5`: event-camera preprocessing as a low-power salience detector pre-VLM stage.

**What to verify:** Buy a GAP9 dev kit (~$300). Run OpenGlass's gesture-recognition workload on it. Measure power vs paper claim. If matches, prototype perceptiond v1.5's "event camera → frame gate → VLM" pipeline.

---

## 5. **Self-Harness: Harnesses That Improve Themselves** (Shanghai AI Lab, 2026-06-08, CC BY 4.0)

**Claim:** A four-layer architecture (Task Execution, Evidence, Proposal, Promotion) that allows a fixed-base-model agent to **improve its own harness** (prompts, tool definitions, agent topology) without weight updates. 14-21pp absolute improvements on Terminal-Bench 2.0 across 3 models, base models unchanged.

**Evidence:** Measured on Terminal-Bench 2.0 across GPT-4-class, Claude-class, and one open-source 70B model. Promotion layer requires improvement on ≥1 split + no regression + artifact and budget checks.

**Why it matters for Danlab:** **This is the on-device default for dglabs-eval.** Harness-only is honest for edge AI (no weight updates, no GPU requirement, runs on the wearable). Self-Harness + SIA (cloud-side, weights optional) is the two-stack model. Dan1/Dan2/Dan3/Dan4 skill documents ARE the harness.

**Where it lands in Danlab:**
- `dglabs-eval v1`: Self-Harness as the default improvement loop.
- `danlab-multimodal v1.5`: SIA-H (harness-only) fork as the first step toward "self-improving agent."
- `dan2-agi-roadmap.v38.md` Month 1-2: Self-Harness + SIA-H spike.

**What to verify:** Replicate Self-Harness's 14-21pp on Terminal-Bench 2.0 using a Dan Glasses-relevant subset (5 dglabs-eval tasks). Confirm "base model unchanged" guarantee holds for LFM2.5-1.2B-Thinking.

---

## Bonus: 10 more papers worth reading (not in top 5 but on the desk)

| Paper | Why it's on the desk |
|-------|----------------------|
| **DCPM** (arXiv:2606.09483) | Dual-process cognitive memory, System 1 sync / System 2 async — `memoryd v3` System 2 path |
| **CogniFold** (arXiv:2605.13438v2) | Cognitive folding, 3-layer CLS, intent emergence — `memoryd v3` cognitive hierarchy |
| **MRAgent** (arXiv:2606.06036) | Reconstructive graph memory, +23% on LoCoMo/LongMemEval — `memoryd v2` graph store |
| **PASK** (arXiv:2604.08000) | IntentFlow streaming demand-detection + LatentNeeds-Bench — `proactived` reference arch |
| **LQA** (arXiv:2602.07849) | Lightweight quantized-adaptive framework, 19.9× memory reduction — `perceptiond v1.5` quantization |
| **SPEED-Q** (arXiv:2511.08914) | 2-bit VLM quantization, <400MB for InternVL-1B — watch for Liquid AI GGUF port |
| **SIA v2** (arXiv:2605.27276v2) | Harness + weights self-improvement, LawBench 70.1% — `danlab-multimodal v2.0` weight path |
| **OpenSkill** (Lehigh + Salesforce, Jun 8) | Autonomous skill acquisition — `dglabs-eval v1.5` skills subset |
| **Agents of Chaos** (Ullman, arXiv:2602.20021) | 12 LLM agent misbehavior case studies — `dglabs-eval v1` safety subset |
| **AdaVFM** (arXiv:2604.15622v1) | Adaptive edge-cloud VLM, 5× longer battery — `perceptiond v1.5` adaptive offload |

---

*Dan2 papers, 2026-06-22 v38. Companion to dan2-research-report.v38.md. Read in order: 1 (Nanomind) → 2 (ProAct) → 3 (MemCog) → 4 (OpenGlass) → 5 (Self-Harness). Bonus list for depth.*
