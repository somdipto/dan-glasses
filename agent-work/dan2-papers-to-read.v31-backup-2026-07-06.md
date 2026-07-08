# Dan-2 Papers to Read — v31 (2026-07-06)

> **Status:** v31 refresh. v30 backups at `*.v30-backup-2026-07-06.md`. v30 content preserved; v31 deltas prepended.
> **Scope:** Top 5 research papers + honorable mentions, ranked by direct relevance to Danlab's AGI roadmap.

---

## v31 Deltas (this refresh — 2026-07-06)

v31 holds the v30 top-5 papers (DynamicMem, Adaptive Auto-Harness, Edge Reliability Gap in VLMs, Hermes Agent Channel Fracture, MemDelta) and **promotes 2 to the top 5** (Cerf agent-to-agent standardization; Karp value-chain) and adds 4 honorable mentions. v31's top-5 has the strongest direct-action read for v1.0 ship-gate in 31 versions.

---

## v31 Top 5 Papers (in priority order)

### 1. (PROMOTED) — Karp Value-Chain Argument (Forbes, July 2 2026) + Cerf Agent-to-Agent Standardization (Open Frontier, June 30 2026)

**Why promoted:** Karp's CNBC interview is the v31 *first external confirmation* of Danlab's positioning from a *credible industry voice*. Karp is CEO of Palantir, a $100B+ company, and is publicly stating: "real enterprise AI value requires model + application layer + compute; frontier AI labs are stealing enterprise value." Cerf is internet co-architect, speaking at Open Frontier (June 30 2026) on agent-to-agent standardization needing TCP/IP-like protocols.

**What it gives Danlab:** Karp's value-chain argument is the v31 *theoretical foundation* for the 6-axis wedge. Without Karp, the wedge is a marketing claim. With Karp, the wedge is *industry-confirmed value-chain theory*. Cerf's standardization argument gives the v31 *infrastructure foundation* for OpenClaw as the user-owned agent-to-agent layer.

**Read time:** Karp: 20 min (Forbes article + Karp CNBC interview clip). Cerf: 30 min (Open Frontier panel transcript + TechCrunch recap).

**Direct action:** v31 plan-X6 + v31 plan-X10 — wire Karp cite into v1.0 spec §13 (1 day copy).

### 2. (HOLD) — DynamicMem (arXiv 2606.22877, late June 2026)

93% of memory failures trace to retrieval, not writing. Promoted to top-5 in v28.

**Direct action:** v30 plan-M3 (memoryd v1.5 4-layer model) + v30 plan-X5 (Perplexity Brain work-trace memory) + v31 plan-X7 (619MB footprint constraints on v1.5 expansion).

### 3. (HOLD) — Adaptive Auto-Harness (arXiv 2606.01770)

Stateful multi-agent evolver with harness tree + solve-time routing. Decomposes gap-to-oracle into evolution loss + adaptation loss.

**Direct action:** v30 plan-P4+ (SIA-W+H + Adaptive Auto-Harness routing layer). The v31 Karp cite sharpens the *bet* — Karp's value-chain argument *requires* an adaptive harness to capture the application-layer value.

### 4. (HOLD) — Edge Reliability Gap in Vision-Language Models (arXiv 2603.26769)

SmolVLM2-500M answers "Yes" to 100% of COCO negation trials. Qwen2.5-VL-7B 4-bit answers incorrectly 14% of the time.

**Direct action:** v30 plan-E1 (LFM2.5-VL-450M negation-collapse probe, Q3 W3, 1 engineer-week, BEFORE v1.0 ships). v31 sharpen: the v31 619MB footprint makes the *cost* of falling back to LFM2.5-VL-1.6B more painful (2.5-3× the v1.0 footprint).

### 5. (HOLD) — Hermes Agent Channel Fracture (arXiv 2606.04896)

Scheduled cron-like agents cannot write to target agent's persistent memory due to `skip_memory=True` flag.

**Direct action:** v30 plan-R1 (Hermes Agent openclaw v1.0 spike + channel-fracture verification, Q3 W2, 1-2 engineer-weeks). v31 sharpen: if the test fails, the openclaw memory-core plugin must be patched to disable `skip_memory` for cross-agent cron-delegated writes.

---

## v31 Honorable Mentions (4 NEW, 5 hold)

### NEW #1 — Meta paywall coverage cluster (WIRED, The Verge, BBC, 9to5Google, July 1-3 2026)

5 industry outlets in 72 hours covering the Meta Conversation Focus paywall. WIRED: "Welcome to the New Era of Consumer Tech." The Verge: "ridiculous rate limit." BBC: "Meta glasses wearers hit with paywall." 9to5Google: "Meta slaps a premium subscription on an existing smart glasses feature." Ynetnews: "The main criticism is not about the business model itself but about a technical fact: the feature runs entirely on the glasses' local chip."

**Read time:** 10 min total (skim headlines + 1-2 long-form).

**Direct action:** v31 plan-X6 — the v31 *strongest* v1.0 wedge cite cluster. Every press hit is citable as "industry consensus on paywall-free as a consumer expectation."

### NEW #2 — Forbes bubble math coverage (Forbes, July 4 2026)

Leaked audited financials: OpenAI -$20.9B operating loss on $13.07B revenue in 2025. Palantir CEO Karp: "per-token pricing is completely wrong." Forbes headline: "Credible AI Lab Critics Pile Up As The Bubble Math Worsens."

**Read time:** 15 min (full Forbes article + Karp CNBC clip).

**Direct action:** v31 plan-X6 + v31 plan-X8 — anchor the v1.0 wedge in *industry-critic consensus* on closed-source frontier unit economics.

### NEW #3 — Crypto Briefing Rocktaschel 2-year RSI ship-date (June 2026)

Recursive Superintelligence co-founder Rocktaschel: "we can build recursive self-improving AI within roughly two years." $4.65B valuation, $155M per employee (less than 30 employees, no public product).

**Read time:** 10 min.

**Direct action:** v31 plan-X9 — wire Rocktaschel 2-year ship-date into v1.0 marketing. Frame: "when RSI ships (2028 H2), Danlab is the audit-by-default open-weights alternative."

### NEW #4 — TechSpot RAM pricing analysis (July 5 2026)

Ethan Tan (former Samsung China exec) at Jefferies: RAM prices rise 40-50% in Q3 2026, 30% in Q4. Relief not until 2028. California lawsuit accuses Samsung/SK Hynix/Micron of price-fixing.

**Read time:** 10 min.

**Direct action:** v31 plan-X7 — anchor the v1.0 spec §14 to 619MB combined model footprint as the v31 supply-chain-constrained hard floor.

### HOLD #1 (v30) — Decagon DuetBench
End-to-end self-improvement benchmark. v30 plan-P4 evaluation rig add.

### HOLD #2 (v30) — Anthropic Institute blog (Favaro + Clark, June 4 2026)
80% of Anthropic code written by Claude. v30 outer-loop RSI citation of record.

### HOLD #3 (v30) — Perplexity Brain work-trace memory (June 18 2026)
First industry ship of *work-trace* memory architecture. v30 plan-X5 (4-layer memoryd v1.5).

### HOLD #4 (v30) — Microsoft Research + Renmin University Arbor (June 2026)
2.5× Claude Code + Codex on same compute. v30 toold v1.5 Arbor-style cumulative learning.

### HOLD #5 (v30) — MatchaTTS + vocos (tts-bench, 5uck1ess, June 2026)
RTF 0.163, 123MB total. v30 v1.5 TTS plan-A.

---

*Maintained by DAN-2. v31 deltas prepend v30. v30 top-5 papers all hold; v31 promotes Karp/Cerf to #1 (industry-confirmed value-chain + standardization foundation for the 6-axis wedge) and adds 4 honorable mentions (Meta paywall cluster, Forbes bubble math, Rocktaschel 2-year RSI, TechSpot RAM pricing). v31 top-5 has the strongest direct-action read for v1.0 ship-gate in 31 versions.*
