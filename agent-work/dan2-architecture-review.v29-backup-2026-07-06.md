# Dan-2 Architecture Review — v29 (2026-07-06)

> **Status:** v29 refresh. v28 content preserved. v29 deltas prepended.
> **Scope:** Problems, risks, suggested improvements for the Dan Glasses + danlab-multimodal stack.
> **Verdict:** v23 9.9/10 + v25 9.95/10 + v27 9.95/10 + v28 9.95/10 architecture decomposition **all hold**. v29 is a research delta on v28 — no architecture change, only sharper evaluation, competitive context, and the v1.0 ship-gate evaluation requirements.

---

## v29 Deltas (this refresh — 2026-07-06)

### §A.21 (NEW) — LFM2.5-VL-450M negation-collapse evaluation gate (v1.0 ship-gate)

The "Edge Reliability Gap in Vision-Language Models" paper (arXiv 2603.26769) shows SmolVLM2-500M answers "Yes" to 100% of COCO negation trials; Qwen2.5-VL-7B 4-bit answers incorrectly 14% of the time. **We do not have a published negation-collapse benchmark for LFM2.5-VL-450M yet.** SmolVLM2-500M and LFM2.5-VL-450M are roughly the same parameter count (500M vs 450M), so the negation collapse risk is real.

**Architecture implication:** the v1.0 ship-gate must include a 200-image COCO-style negation probe (scaled-down FINER-CompreCap or Ghost-100). If LFM2.5-VL-450M exhibits >50% negation collapse on the probe, fall back to a v1.0 VLM with proven negation performance (e.g., LFM2.5-VL-1.6B — the 1.6B variant, not the 450M — has vLLM support, Optimum-Intel OpenVINO export, and a published LEAP Edge SDK path; at 1.6B it's 2-3× the 450M size, but the 1.6B variant is closer to the 7B model's negation profile).

**Plan-E1 (NEW v29):** LFM2.5-VL-450M negation-collapse probe + SmolVLM2-500M head-to-head, 1 engineer-week, Q3 W3, BEFORE v1.0 ships. Use the Ghost-100 5-Level Prompt Intensity Framework (800 synthetic images, 3 task families) or FINER-CompreCap.

### §A.22 (NEW) — Wedge reframing: transparency + reversibility + on-device, not "we do RSI"

The v28 "outer-loop RSI at Danlab" framing is now multi-lab production (OpenAI GPT-5.3-Codex self-coding, Anthropic Claude Code internal loops, Google DeepMind AlphaEvolve). The Danlab v1.0 wedge is NOT "we do RSI" — it is **"we ship a transparent, reversible, on-device self-improving infrastructure."** Three concrete differentiators:
- **Transparency:** every spec version, every plan add, every artifact is public and auditable.
- **Reversibility:** the v26 plan-O2 reversibility contract (user can wipe memoryd + scrub all episodic logs in one command) is the v1.0 differentiator.
- **On-device:** no cloud fallback for primary flows; cloud fallback only with explicit user consent (v1.5 INAR-VL routing).

**Architecture implication:** the v1.0 marketing copy should lead with "transparent, reversible, on-device self-improving infrastructure" — not "we're building AGI from India" (vague), not "we do RSI" (false at the maximalist level), not "open-source" alone (NVIDIA-validated, not differentiating). The new wedge is the combination.

### §A.23 (NEW) — Adaptive Auto-Harness routing layer on top of SIA-W+H (v1.5)

Adaptive Auto-Harness (arXiv 2606.01770) addresses the "fixed offline benchmarks" problem in prior auto-harness work. Decomposes the gap to an oracle into **evolution loss** and **adaptation loss**. Stateful multi-agent evolver, harness tree with solve-time routing, human-steering hooks.

**Architecture implication:** the v28 plan-P4 (SIA-W+H port) should be sharpened to v29 **"SIA-W+H + Adaptive Auto-Harness routing"** — the harness tree with solve-time routing is the v29 "productionize" layer. Estimated 1-2 day additional spike on top of plan-P4, but the result is a v1.5 plan that doesn't degrade in real deployments.

### §A.24 (NEW) — Hermes Agent v1.0 spike adds channel-fracture verification

Hermes Agent "Channel Fracture" (arXiv 2606.04896): scheduled cron-like agents cannot write to the target agent's persistent memory due to the `skip_memory=True` flag at the scheduler level. Silent failure mode.

**Architecture implication:** the v28 Hermes Agent openclaw v1.0 spike (Q3 W2) must add a "verify cron-delegated memory writes land in the target agent's persistent store" test. If the test fails, the openclaw memory-core plugin must be patched to disable `skip_memory` for cross-agent cron-delegated writes (with explicit allowlist).

### §A.25 (NEW) — INAR-VL edge-cloud routing as v1.5 differentiator

INAR-VL (arXiv 2605.18853) is a routing system that uses lightweight pre-inference signals to decide which VLM model to run, input resolution, edge vs cloud. Recovers ~71% of edge-to-cloud accuracy gap. Mean accuracy 72.1% (oracle best-of-4: 90.6%).

**Architecture implication:** for v1.5, when danlab-multimodal hits a low-confidence score on a difficult frame, the danlab-multimodal loop can fall back to a cloud VLM (with explicit user consent). This is the v29 "edge-first, cloud-with-consent" pattern. Not v1.0 (must be on-device-only for the v26 sovereign-trust position) but a clean v1.5 differentiator.

### §A.26 (NEW) — The v1.0 evaluation rig is now concrete

The v28 architecture decomposition relied on a v1.0 spec that was not yet shipped. The v29 evaluation rig is now concrete:
- **FINER-CompreCap or Ghost-100 5-Level Prompt Intensity Framework** for VLM negation probes.
- **MemDelta-controlled baseline** (arXiv 2606.29914) for any memoryd model swap.
- **AIMultiple cross-domain methodology** (July 3 2026) for embedding evaluation.
- **Edge Reliability Gap protocol** (arXiv 2603.26769) for VLM failure-mode attribution.
- **DynamicMem retrieval-failure metric** (arXiv 2606.22877) for memoryd v1.5 retrieval focus.
- **Adaptive Auto-Harness harness-tree routing** (arXiv 2606.01770) for v1.5 self-improving routing.
- **INAR-VL edge-cloud routing signals** (arXiv 2605.18853) for v1.5 edge-cloud fallback.

The v1.0 spec §13 (sovereign trust + chip sovereignty + reversibility) should reference each of these as the v1.0 evaluation methodology. This is the v29 **"rig not rhetoric"** upgrade.

---

## v28 v1.0 Plan Additions (still hold)

| Plan | Description | Engineer-weeks | Quarter |
|------|-------------|---------------|---------|
| plan-P3 | SIA-H honest-RL claim (danlab-multimodal → prompt-edit RL) | 1 | Q3 W2 |
| plan-P4 | SIA-W+H port (LoRA training in the loop) | 3 | Q3 W3-W4 |
| plan-S1 | OpenClaw supervisord-equivalent (daemon restart on crash) | 1 | Q4 W1 |
| plan-S2 | Chip-stack sovereignty spec (no-NVIDIA-lock-in path) | 1 | Q4 W2 |
| plan-S3 | Public Dan Glasses hardware reference design (RDK) | 2 | Q4 W2-W3 |

## v29 v1.0 + v1.5 Plan Additions (NEW)

| Plan | Description | Engineer-weeks | Quarter |
|------|-------------|---------------|---------|
| plan-E1 (NEW) | LFM2.5-VL-450M negation-collapse probe + SmolVLM2-500M head-to-head (VLM v1.0 ship-gate) | 1 | Q3 W3, BEFORE v1.0 ships |
| plan-T1 (NEW) | MatchaTTS + vocos v1.5 TTS spike (replaces v28 plan-A Kokoro-82M) | 1 | Q3 W3 |
| plan-P4+ (NEW, extends plan-P4) | Adaptive Auto-Harness routing layer on top of SIA-W+H | 1 (additive) | Q3 W4 |
| plan-R1 (NEW) | Hermes Agent openclaw v1.0 spike + channel-fracture verification (extends v28 Hermes Agent spike) | 1-2 | Q3 W2 |
| plan-R2 (NEW) | INAR-VL edge-cloud routing layer (v1.5 differentiator) | 2 | Q1 2027 W1-W2 |

All v28 plans hold. v29 is additive.

---

## v29 Critical/Medium/Minor Issues (v28 hold + 5 new)

### Critical
- v28 #1-5 (all hold)
- **v29 #6 (NEW): LFM2.5-VL-450M negation-collapse evaluation gate (plan-E1, Q3 W3, 1 engineer-week, BEFORE v1.0 ships).** If LFM2.5-VL-450M exhibits >50% negation collapse, fall back to LFM2.5-VL-1.6B or SmolVLM2-500M with the negation-collapse caveat documented.

### Medium
- v28 medium #1-7 (all hold)
- **v29 medium #8 (NEW): MatchaTTS + vocos v1.5 TTS spike (plan-T1, Q3 W3, 1 engineer-week).** Displaces v28 plan-A Kokoro-82M based on concrete on-device RTF numbers.
- **v29 medium #9 (NEW): Wedge reframing — "transparent, reversible, on-device self-improving infrastructure" replaces "we do RSI" in v1.0 marketing copy.** Combine v26 plan-O3 + v28 plan-S2 + v29 wedge reframing.

### Minor
- v28 minor #1-7 (all hold)
- **v29 minor #8 (NEW): Hermes Agent channel-fracture verification (plan-R1, Q3 W2, additive to v28 Hermes Agent spike).**

---

*Maintained by DAN-2. v29 deltas prepend v28. v28 9.95/10 architecture decomposition holds.*
