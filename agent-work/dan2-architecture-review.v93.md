# Dan Glasses Architecture Review — Problems, Risks, Improvements

**Author:** Dan2
**Date:** 2026-06-26
**Status:** v93 — delta on v12 (Microsoft Scout, Liquid AI retrievers, edge VLM benchmarks)

---

## Summary Verdict (v93 update)

The v12 verdict stands: **The current Dan Glasses architecture is production-grade for a desk-bound prototype.** Three structural gaps for a true wearable:
1. No proactive loop (awarenessd)
2. No power characterization on target SoC
3. OpenClaw gateway single point of failure

**v93 adds three new findings** that sharpen the diagnosis:
1. **Microsoft Scout (Jun 2, 2026)** now competes for the OpenClaw category. The gateway risk just went from "engineering" to "category-level."
2. **Liquid AI retrievers (Jun 18, 2026)** turn memoryd v2 from research into a 2-week fork-and-ship. The memoryd bottleneck is solved.
3. **NPU edge VLM benchmarks** (AMD Ryzen AI 67× more efficient than iGPU, Qualcomm SA8295P 14× lower latency, CHIME 41× faster than Jetson) **prove NPU acceleration is shipping today**. The "we don't have NPU" excuse is gone.

---

## P1. No `awarenessd` — the proactive wedge is unowned (v93: Action 1)

**Severity:** Critical

**Evidence:** PRD Section 2 promises "proactive AI companion — observes, reasons, contextualizes, **acts**." Every shipped daemon is **reactive**. No service triggers output unsolicited.

**v93 updates to the v12 awarenessd design:**

1. **5-pillar framework** from "Proactive Systems in HCI and AI" (arXiv:2606.25149, Jun 2026) [^1]:
   - Timing (when to fire)
   - Appropriateness (context-aware)
   - User control (toggle, snooze, per-category opt-out)
   - Transparency (every decision logged)
   - Trust (calibrated confidence, don't fire unless match > 0.85)

2. **Halo's proactive is now the bar** — at $299. v12 said "without proactive we're slightly-better-open-source-Halo." v93 corrects: **Halo has proactive.** Our wedge is now: **memory depth + auditability + multilingual**.

3. **Concrete implementation:**
   ```python
   # awarenessd v0.1 (v93 plan)
   subscribers = [perceptiond_description_stream, memoryd_event_stream]
   for event in merge(subscribers):
       context = build_context(event, recent_memory_window=24h)
       salience = salience_model(event, context)       # novelty + relevance
       decision = should_i_fire(salience, context,
                               user_preferences,      # 5-pillar framework
                               spam_cap=3/hr,
                               time_of_day_gate,
                               confidence_threshold=0.85)
       if decision.fire:
           if decision.channel == "tts":
               ttsd.speak(decision.message)
           elif decision.channel == "telegram":
               openclaw.notify(decision.message)
           log(event, decision, user_feedback=None)   # auditable
   ```

**Effort:** 3 weeks for v0.1 with rules-engine, 4–6 weeks for v1.0 with LLM-based "should I fire?" using LFM2.5-1.2B-Thinking.

**Why this is the moat:** Brilliant Labs Halo's Noa agent [^2], Meta's Ray-Ban AI, Even Realities G2 — all are **reactive** (Halo's "proactive" is conversation-scoped, not memory-aware). If we ship proactive with **memory depth + auditability + multilingual**, we have a category.

---

## P2. VLM power draw uncharacterized on target hardware (v93: now solvable)

**Severity:** Critical

**Evidence:** perceptiond/SPEC.md notes "Power draw uncharacterized: VLM is the dominant power event on aarch64." PRD estimates 3–8W.

**v93 update:** **NPU acceleration is shipping today.** We no longer have to wait for fictional benchmarks.

| Reference | Hardware | Speedup vs iGPU | Power efficiency | Source |
|---|---|---|---|---|
| Mapping Gemma3 onto Edge Dataflow (AMD Ryzen AI) | Ryzen AI Max+ 395 NPU | **5.2× prefill, 4.8× decode** | **67× more efficient** | [^3] |
| AutoNeural (Qualcomm SA8295P) | SA8295P NPU | **14× lower latency** | 7× lower quantization error | [^4] |
| SPEED-Q 2-bit VLM | Edge | <400 MB for InternVL-1B | (vs 1.5 GB FastVLM) | [^5] |
| CHIME (near-memory chiplet) | vs Jetson Orin NX | **41× faster** | **185× more energy-efficient** | [^6] |
| LiteVLA on Raspberry Pi 4 | CPU-only | ~2 min per inference | NF4 quantization | [^7] |

**Implication for Dan Glasses:**

1. **Buy a Qualcomm SA8295P dev kit** (or AMD Ryzen AI Max+ 395 reference board) — these are the proxy targets for our wearable SoC.
2. **Re-measure LFM2.5-VL-450M Q4_0** on these boards. Expected: **<2W average in watchful mode** (vs current PRD estimate 3–8W on CPU).
3. **If NPU path works** → battery sizing collapses from 4h → 8h+ on same 2500 mAh. **Hardware weight target relaxes.**
4. **If NPU path fails** → fall back to SPEED-Q 2-bit quantization + CPU-only. Still beats current 3–8W estimate.

**Effort:** 2 weeks (procurement + measurement + report).

---

## P3. OpenClaw gateway single point of failure (v93: now category-level)

**Severity:** Critical (was High in v12)

**Evidence:** v38 documented 7 carry-forward OpenClaw crashes. **v93 adds: Microsoft Scout launched Jun 2, 2026 as an OpenClaw-based always-on agent** [^8]. Microsoft is betting on OpenClaw too — but for desktop. **For wearables, OpenClaw reliability is now a category-level risk.**

**Three paths forward:**

| Path | Pros | Cons | v93 Recommendation |
|---|---|---|---|
| **A. Stay on upstream OpenClaw + DanClaw proxy** | Insulates from upstream crashes; cheap | Two layers to maintain | **v93 Action 1 of Q3 2026.** |
| **B. Migrate to MS-Scout** when it ships a wearable SDK | Microsoft-backed | Vendor lock-in; not yet shipping | Defer. Re-evaluate Q4 2026. |
| **C. Build our own Rust gateway** | Full control | 6–12 month rebuild | Don't. TS/Node ecosystem is too valuable. |

**DanClaw proxy (v38/v93 spec):**
- TypeScript/Node, ~500 LOC
- Sits between wearable daemons and OpenClaw
- Exposes `danclaw/healthz` aggregating per-service health
- Swallows OpenClaw restarts (state preserved)
- Mirrors in-flight messages to memoryd/conversations

**This week:** Write 1-page brief on whether `openclaw-gateway` v2026.5.x is compatible with MS-Scout's OpenClaw fork. If yes → DanClaw proxy is cheap. If no → binary choice in 60 days.

**Effort:** 1 week.

---

## P4. memoryd flat cosine index won't scale past ~10K memories (v93: fork-and-ship now)

**Severity:** Medium (was Medium in v12)

**Evidence:** v12 noted O(N) flat cosine. At 10K memories, ~50ms query. At 100K, ~500ms — too slow for proactive loop.

**v93 update:** **Liquid AI retrievers shipped Jun 18, 2026** [^2]. Drop-in upgrade path:

| Component | v12 | v93 |
|---|---|---|
| Encoder | all-MiniLM-L6-v2 (384-dim) | **LFM2.5-Embedding-350M** (1024-dim, 22 Indic languages, Apache-2.0) |
| Reranker | (none) | **LFM2.5-ColBERT-350M** (Q4 2026) |
| Index | Flat cosine | **HNSW via `usearch`** (Q3 2026) |
| Consolidation | (deferred) | Nightly cron (Q4 2026) |

**memoryd v2 timeline (v93):**
- Q3 2026: swap encoder + add HNSW (2-week fork-and-ship)
- Q4 2026: add ColBERT reranker + nightly consolidation cron

**Why this matters:** memoryd is the cognitive core of Dan Glasses. **The 24 Indic language support** is the India-origin moat for v1 wearable. We can ship Hindi + Bengali + Tamil + Telugu + Marathi out of the box.

**Effort:** 2 weeks for v2.0, 2 weeks for v2.5.

---

## P5. TTS — KittenTTS is suboptimal (v93: confirmed + solution)

**Severity:** Medium

**Evidence:** ttsd/SPEC.md uses KittenTTS medium. English-only. Not the 2026 leader.

**v93 reaffirms:** **Kokoro-82M as v1.5 candidate** (Apache-2.0, 82 MB, has Hindi voices, runs on Raspberry Pi, beats KittenTTS in mid-2026 blind tests).

**Why now matters:** **Halo is English-only at launch.** Kokoro's Hindi voices are a **direct wedge** for India-first positioning. Ship Hindi + Bengali + Tamil via Kokoro in Q4 2026.

**Effort:** 3 days for swap + tests + voice benchmark.

---

## P6. toold vs os-toold — overlapping concerns (v93: unchanged)

**Severity:** Low (carried from v12)

**Evidence:** toold (port 8742) sandboxes shell + python. os-toold (port 8744) is a separate path-guard wrapper.

**v93 read:** Same as v12. Merge into toold with `mode=os` flag, or document the split clearly. **Not Action 1.**

---

## P7. Microsoft Scout compatibility check (v93: NEW)

**Severity:** High

**Evidence:** MS-Scout is OpenClaw-based. We don't know if Microsoft's fork diverges from upstream. If yes → binary choice. If no → DanClaw proxy is cheap.

**Action:** This week, 1-page brief on `openclaw-gateway` v2026.5.x vs MS-Scout compatibility.

**Effort:** 1 day.

---

## P8. Hardware timeline compression (v93: NEW, Critical)

**Severity:** Critical

**Evidence:** Halo at $299 with proactive is shipping now. Google × Warby Parker × Gentle Monster Gemini smart glasses Fall 2026 [^9]. Viture Helix + NVIDIA (Jun 16) [^10]. Snap acquires Illumix (Jun 4) [^11]. **The window to claim the category is closing fast.**

**v93 implication:** **Compress hardware timeline to Q4 2026 dev-kit.** This means:
- Lock a target SoC by end of Q3 2026 (Qualcomm SA8295P, AMD Ryzen AI, or a wearable-optimized variant)
- Buy dev kits now
- 1-week power measurement sprint (P2) before committing battery sizing
- Ship dev-kit to internal beta in Q4 2026

**Effort:** $5-15K hardware procurement + 1 week measurement + 8 weeks to dev-kit.

---

## Action priority (v93)

| Action | Severity | Effort | When |
|---|---|---|---|
| 1. awarenessd v0.1 | Critical | 3 weeks | Q3 2026 week 1 |
| 2. DanClaw proxy | Critical | 1 week | Q3 2026 week 1 |
| 3. MS-Scout compat brief | High | 1 day | This week |
| 4. memoryd v2 (encoder + HNSW) | Medium | 2 weeks | Q3 2026 week 2 |
| 5. Hardware procurement + power measurement | Critical | 2 weeks | Q3 2026 week 2 |
| 6. SIA-on-danlab-multimodal fork | High | 4 weeks | Q3 2026 week 3 |
| 7. Kokoro TTS swap | Medium | 3 days | Q4 2026 |
| 8. memoryd v2.5 (ColBERT + consolidation) | Medium | 2 weeks | Q4 2026 |
| 9. Wearable dev-kit | Critical | 8 weeks | Q4 2026 |
| 10. awarenessd v1.0 with LLM-based decision | High | 4 weeks | Q4 2026 |

---

## Sources

[^1]: https://arxiv.org/html/2606.25149v1 — Proactive Systems in HCI and AI (Jun 2026)
[^2]: https://www.liquid.ai/blog/lfm2-5-retrievers — LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M (Jun 18, 2026)
[^3]: https://arxiv.org/abs/2602.06063 — Mapping Gemma3 onto Edge Dataflow Architecture (AMD Ryzen AI NPU, May 2026)
[^4]: https://arxiv.org/html/2512.02924v2 — AutoNeural: Co-Designing VLMs for NPU Inference (Qualcomm SA8295P)
[^5]: https://arxiv.org/html/2511.08914 — SPEED-Q: Staged Processing with Enhanced Distillation (2-bit VLM)
[^6]: https://arxiv.org/html/2601.19908v1 — CHIME: Chiplet-based Heterogeneous Near-Memory Acceleration
[^7]: https://export.arxiv.org/pdf/2511.05642 — LiteVLA on Raspberry Pi 4 (4-bit NF4 SmolVLM)
[^8]: https://github.com/Zijian-Ni/awesome-ai-agents-2026 — Microsoft Scout launched at Microsoft Build 2026 (Jun 2, 2026)
[^9]: https://www.instagram.com/reel/DZek2QnAuH2 — Google display-less Gemini smart glasses Fall 2026 with Warby Parker and Gentle Monster
[^10]: https://www.facebook.com/AndroidCentral/posts/viture-revealed-its-new-helix-smart-glasses-which-signal-a-major-step-into-ai-an/1435121635322862 — Viture Helix + NVIDIA partnership (Jun 16, 2026)
[^11]: https://www.instagram.com/reel/DZMcz8jEYND — Snap acquires Illumix (Jun 4, 2026)
[^12]: https://www.facebook.com/BestBuyCanada/posts/discover-next-generation-ai-glasses-designed-to-keep-you-connected-and-capture-e/1445409774281048 — Brilliant Labs Halo at $299 with proactive AI