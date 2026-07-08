# DAN-2 AGI Roadmap — v12 (2026-06-26, 12:00 IST / 06:30 UTC)

**Author:** Dan2 (DAN-2, danlab.dev)
**Status:** Supersedes v11 (2026-06-25, 11:30 IST)
**Companion to:** `dan2-research-report.md` v12, `dan2-architecture-review.md` v12
**Delta from v11:** Re-prioritizes audiod RL ahead of memoryd v2 (per architecture review §3). Adds HRM-Text-1B integration as the highest-leverage capability add for v1.5. Keeps v11's stage-gated memoryd v2 schedule (v2.0 Oct, v2.1 Dec, v2.2 Q1 2027).

---

## 0. North star (unchanged from v10)

**Danlab ships auditable, on-device, open-source AI from India.** The product proof is Dan Glasses. The research proof is auditable calibration and self-modeled agents. The moat is **reliability + transparency + locality**, which competitors cannot copy because their business models forbid it.

---

## 1. Six-month roadmap (Jul 2026 → Dec 2026)

### Jul 2026 — audiod RL + HRM-Text foundation
- **audiod calibration head v1** — ship by Jul 25. ECE on Librispeech < 0.05.
- **HRM-Text-1B integration plan** — locked, prototype in week 4.
- **Show HN prep** — landing page, install script, eval harness, video demo.

### Aug 2026 — Show HN + first arXiv
- **Aug 15:** arXiv pre-print on audiod calibration (with co-evolving harness as 2nd contribution).
- **Aug 25:** Show HN. Target: top 10 of the day. Mitigate install-to-talking-to gate (5-min demo).
- **Aug 30:** memoryd v2.0 ships (RRF fusion + provenance graph).

### Sep 2026 — long-memory + persona
- **Sep 15:** LongMemEval + PersonaMem-v2 submissions (memoryd v2 baseline + with provenance graph).
- **Sep 30:** memoryd v2.1 ships (KG overlay, Mem0g-style).
- **Sep 30:** bench harness published — reproducibility is part of the moat.

### Oct 2026 — proactive AI + Polish
- **Oct 15:** Proactive AI v1. Background state machine: watchful → trigger → proactive-speaks. Decision policy = salience + memory-relevance + time-of-day.
- **Oct 30:** ttsd swap decision — Kokoro-82M if voice quality materially improves user retention.

### Nov 2026 — wearable robustness
- **Nov 15:** power/thermal telemetry in production.
- **Nov 30:** battery + thermal fallback policies are data-driven, not heuristic.

### Dec 2026 — product hardening
- **Dec 15:** HRM-Text-1B in the loop for planning, memory-write policy, and task decomposition.
- **Dec 31:** memoryd v2.2 scoping finalized.

---

## 2. Twelve-month roadmap (Jan 2027 → Jun 2027)

### Q1 2027
- **memoryd v2.2** — Curator role + structured incremental playbook.
- **OpenClaw hardening** — sandbox exfiltration defenses, tool provenance, denylist testing, replay logs.
- **Reasoner evals** — compare HRM-Text vs local transformers on planning, recall, and tool-choice quality.

### Q2 2027
- **Wearable hardware lock** — one stable target board; no more hardware churn.
- **Camera + microphone power budget** — actual measured battery numbers on real hardware.
- **Proactive agent loop** — user-triggered, then increasingly context-triggered.

---

## 3. Twenty-four-month roadmap (Jul 2027 → Jun 2028)

### Core outcome
By mid-2028, Danlab should have a **personal on-device agent** that can:
- perceive continuously,
- store evidence cleanly,
- reason locally,
- act safely with tools,
- and initiate useful actions before being asked.

### What must be true by then
- HRM-Text is not a toy; it is part of the default stack.
- memoryd is an evidence system, not just embeddings.
- audiod is calibrated and measurable.
- OpenClaw is a hardened orchestration substrate, not merely a convenience layer.
- the product remains private-by-default and auditable end-to-end.

---

## 4. Priority ranking

### P0 — do immediately
1. audiod calibration head
2. OpenClaw security hardening
3. prompt injection sanitization between perceptiond and os-toold

### P1 — do next
4. HRM-Text-1B reasond
5. memoryd v2.0
6. Granite Speech / Kokoro benchmark sweep

### P2 — do after evidence
7. wearable hardware migration
8. proactive background agent loop
9. ttsd swap only if user feedback demands it

---

## 5. Anti-priorities

- Do not chase frontier cloud models for the wearable path.
- Do not rewrite the whole stack to chase an architecture fad.
- Do not ship a second memory system before memoryd v2 stabilizes.
- Do not over-invest in voice quality if the user still misses commands or trusts transcripts less than 95%.
- Do not add autonomy before controllability and replayability are solid.

---

## 6. The key bet

**Small models + good harnesses + local evidence + human-steerable autonomy beat giant opaque assistants for this product.**

That is the roadmap. Everything else is a subtask.