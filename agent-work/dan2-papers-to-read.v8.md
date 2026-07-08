# Danlab Top 5 Papers to Read v8

**Author:** Dan2 | **Date:** 2026-06-25 07:35 IST
**Status:** v8 supersedes v7

---

## 1) Darwin Gödel Machine / MetaAI recursive self-design

**Why read it:**
- It is the cleanest current evidence that harness evolution can improve a system without full model retraining.
- It gives Danlab the experimental shape for audiod RL.
- The reported improvement on SWE-bench Verified (20% → 50%) is the most relevant empirical benchmark for self-improving coding/agent systems.

**What to extract:**
- How self-modification is gated.
- What counts as a valid improvement.
- How to prevent collapse after a peak.
- How to structure the meta-level modifier.

**Use for Danlab:** audiod calibration RL loop + memoryd self-model.

---

## 2) Toward a Science of AI Agent Reliability

**Why read it:**
- This is the paper that formalizes the reliability axes Danlab should expose.
- It turns "trust me" into calibration, consistency, robustness, predictability, and safety.

**What to extract:**
- Reliability decomposition.
- Calibration metrics.
- How to surface reliability publicly.
- How reliability differs from raw capability.

**Use for Danlab:** `GET /reliability`, `GET /reliability/calibration` on every daemon.

---

## 3) Perplexity Brain

**Why read it:**
- It is the closest production reference for memoryd v2.
- It operationalizes memory about the agent’s work, not just the user.
- It shows traceable context graphs and overnight synthesis at product scale.

**What to extract:**
- Context graph structure.
- Source-linking discipline.
- Overnight synthesis / wiki generation.
- The +25% / +16% / -13% performance pattern.

**Use for Danlab:** memoryd v2 design and operative_context surface.

---

## 4) SEAGym

**Why read it:**
- It is the best current benchmark for harness evolution.
- It makes clear that intermediate snapshots can decay.
- It shows why peak detection and rollback are necessary.

**What to extract:**
- Update protocols.
- Why AHE outperforms alternatives.
- How to keep only useful intermediate snapshots.
- How to evaluate held-out improvement honestly.

**Use for Danlab:** audiod RL agent harness design.

---

## 5) INAR-VL / adaptive routing for VLMs

**Why read it:**
- It is the clearest answer to edge/cloud routing.
- It quantifies the benefit of not forcing every query through the same path.
- It maps directly onto a wearable with power constraints.

**What to extract:**
- Routing policy.
- Cost/accuracy tradeoff.
- Latency and energy accounting.
- Decision boundaries.

**Use for Danlab:** `dan-router` between local daemons and cloud fallback.

---

## Honorable mentions
- **Kokoro-82M** documentation / releases — to justify the TTS swap.
- **CondenseVLM / QViD / V5e-0** — to ground the perceptiond compression stack.
- **AEL / DPCM / LLM-Wiki** — to implement memoryd v2 properly.
- **Sakana AI Scientist** — to understand end-to-end research automation.
- **Auto-Enhance / Meta-Harness** — for meta-benchmark design.

---

## Reading order
1. Toward a Science of AI Agent Reliability
2. Darwin Gödel Machine / MetaAI recursive self-design
3. SEAGym
4. Perplexity Brain
5. INAR-VL / adaptive routing

— DAN-2, 2026-06-25 07:35 IST