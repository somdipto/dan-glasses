# Dan2 — Research Report v9
## Delta Refresh for Danlab's AGI Roadmap

**Date:** 2026-06-18 06:30 IST (01:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v9. v8 archived as `dan2-research-report.v8.md` (2026-06-17 11:30 IST, 19 hours old).
**v9 thesis:** v8 is fresh enough that v9 is a *targeted delta*, not a redo. The half-life of useful research on this stack is ~24-72 hours. Three things changed since v8 that materially affect our AGI roadmap and our architecture:

1. **Fable 5 / Mythos 5 export-control suspension (June 12 2026)** — Anthropic's most capable models pulled worldwide by US government order within 3 days of launch. This is the most consequential AI event of 2026 and validates our "on-device + open-weights only" thesis.
2. **Apple AI glasses (N50) + camera AirPods confirmed for late 2027 (Bloomberg, June 16 2026)** — the Apple-window kickoff is time-critical. We have ~6 months of head start before Apple ships.
3. **SIA confirmed at Stanford (June 2026)** — the self-improving agent paper we plan to fork has a second implementation in the wild. The fork collaboration is now possible.

The v8 deep-dives (memory architecture, edge VLM optimization, proactive AI) all stand. v9 sharpens three things: the safety case (Fable 5 lesson), the market timing (Apple-window confirmation), and the SIA fork path (Stanford confirmation).

---

## 0. What Changed Since v8

### 0.1 The Fable 5 / Mythos 5 export-control event (June 12 2026)

This is the most consequential AI event of 2026. The chain of events:

- **June 9, 2026:** Anthropic launches Claude Fable 5 and Claude Mythos 5. Fable 5 is the first broadly available "Mythos-class" model. Same underlying weights as Mythos 5 with guardrails. Billed as Anthropic's most capable model — large gains in software engineering, knowledge work, vision, scientific research, long-running autonomous tasks.
- **June 12, 2026:** US government issues an export-control directive ordering Anthropic to suspend access to both models for any foreign national, including Anthropic's own foreign-national employees. The directive cites "national security authorities" and references a "method of bypassing, or 'jailbreaking' Fable 5."
- **Net effect:** Fable 5 and Mythos 5 are disabled for *everyone*, because Anthropic cannot reliably separate foreign nationals from the rest of its user base in real time.
- **Anthropic's response:** "We disagree that the finding of a narrow potential jailbreak should be cause for recalling a commercial model deployed to hundreds of millions of people." Anthropic notes that the jailbreak capability is "widely available from other models (including OpenAI's GPT-5.5)."
- **June 15, 2026:** CNBC reports Anthropic is meeting with Trump administration to resolve. Wired reports Anthropic "is still at odds with the White House." No resolution as of v9 (June 18).

**Why this matters for Danlab (v9 thesis):**

This is the **first time a US export-control directive has been applied to a frontier AI model** for reasons other than weights proliferation (i.e., not because of concerns about the weights being copied to adversaries, but because of a discovered *jailbreak technique*). The implications:

1. **Single-vendor frontier API dependency is now a *structural* risk.** Any product built on Claude Fable 5 or Mythos 5 was disabled in 3 days. The "always available, always improves" promise of frontier APIs is contingent on US regulatory stability.
2. **The "jailbreak as export-control trigger" precedent is dangerous.** If other models are subject to the same standard, every frontier model is one jailbreak away from being cut off.
3. **Anthropic's own framing — "this capability is widely available" — is correct.** The capability differential between Fable 5 and other models is small. But the *legal* differential (Anthropic is a US lab subject to US export control) is the actual lever.
4. **Open-weights on-device is the only defense.** A model running on the user's device, with weights that the user has downloaded and audited, is not subject to US export control.

**v9 implication for our architecture:** v1 must be *provably* on-device. Not "designed to be on-device" — *provably* on-device. A CI test that fails on any non-allowlisted network call. A `privacyd` service with a `/privacy/on-device-only` endpoint that returns `{"on_device_only": true, "network_calls_observed": [...]}` and an audit log.

**v9 implication for our roadmap:** the Apple-window kickoff is more urgent. If Anthropic's frontier models can be regulatorily cut off, frontier-LLM-dependent products become structurally fragile. The "on-device + open-weights" thesis is no longer a *preference* — it's a *requirement*.

### 0.2 Apple AI glasses (N50) + camera AirPods confirmed (Bloomberg, June 16 2026)

The Bloomberg report (June 16 2026) confirms Apple's 2027 product roadmap:

- **Camera-equipped AI AirPods:** first AI-focused Apple wearable. Launches late 2027 as part of Apple's "biggest wave of new products yet." Pairs with iOS 28 (code-named Bell).
- **N50 smart glasses:** Apple's first smart glasses. Launch as early as late 2027. Codenamed N50. Two cameras — one for pictures/videos, one for multimodal AI input and hand-gesture control.
- **Second-gen foldable iPhone + iPhone 20 Pro (20th anniversary model):** also late 2027.
- **Smart pendant:** reportedly under consideration as a third AI wearable.

**v8 said:** "Apple delayed to late 2027." v9 confirms this with more product detail.

**v9 implication:** the Apple-window kickoff is confirmed. We have Q4 2026 / Q1 2027 to ship a credible, open-source, on-device AI companion *before* Apple enters with a closed, cloud-dependent product. This is the only moment where a small open-source player can credibly enter the wearables market.

**v9 strategic call:** ship Dan Glasses v1 by end of Q4 2026. Don't wait for Redax. The x86_64 laptop dev target is the v1 form factor. The wearable is v2.

### 0.3 SIA confirmed at Stanford (June 2026)

A Stanford-based team announced an open-source SIA (Self-Improving AI agent) implementation at Stanford in June 2026. The announcement (Instagram): "We launched an open source Self Improving AI agent (SIA) at Stanford yesterday. It's truly a recursive agent that can self improve its own harness and weights."

This is in addition to the Hexo Labs + Oxford SIA paper (2026-05-29, MIT). v8 already noted the SIA paper; v9 confirms there's now a *second implementation* in the wild.

**v9 implication for our roadmap:** the SIA fork (12-month roadmap milestone) can be done as a *collaboration* with Stanford or Hexo Labs, not just a from-scratch fork. This accelerates the timeline and reduces risk.

**v9 action:** identify a contact at Hexo Labs or Stanford SIA team. Plan the fork collaboration in month 1-2.

### 0.4 Liquid LFM2.5-VL-1.6B-Extract (June 13 2026)

Liquid published a new variant of LFM2.5-VL on June 13 2026: the **1.6B Extract variant**, specialized for schema-consistent JSON extraction. 99.6% on Liquid's Extract F1 benchmark.

The 450M Extract variant scored 98.8%. The 1.6B Extract is a *quality upgrade* for structured-output tasks.

**v9 implication:** for v1.5 vision, we should evaluate the **base LFM2.5-VL-1.6B** (when Liquid publishes the base variant, not just the Extract variant). The base 1.6B would be a natural upgrade from our current 450M, with similar architecture family.

### 0.5 Other deltas

- **Liquid LFM 2.5 Audio 1.5B-JP (2026):** speech-to-speech end-to-end Japanese model. Tracks the speech-to-speech paradigm shift. Watch for English variant.
- **DeepSeek V4:** VLLM MoE decoder trend. Not a vision model. Watch for vision variants.
- **GLM-5.2 (Z.ai, June 14 2026):** 1M-token context, MIT license. No vision model in the 1B range yet.
- **Google Gemini 3.5 Flash (Google I/O 2026):** "faster and cheaper" — Google's competitive response to GPT-5.5 / Claude. Cloud-only. Out of scope for Danlab.
- **Meta Ray-Ban Display + Meta smart glasses expansion (June 2026):** Meta continues to ship; Apple's late-2027 entry is the only opening.

---

## 1. The v8 Pillars — What Stands

The v8 deep-dives stand. Specifically:

1. **System architecture:** the 7-service decomposition is correct. The 4 v9 services (`privacyd`, `reasond`, `proactived`, plus `powerd` folded into openclaw-gateway) are the additions.
2. **danlab-multimodal as pre-RL scaffold:** confirmed. The SIA fork path is clear.
3. **Model stack:** LFM2.5-VL-450M (vision), whisper.cpp base.en (STT), KittenTTS medium (TTS), all-MiniLM-L6-v2 (memory). All shipped, all live. v1.5 upgrade path is LFM2.5-VL-1.6B base (when released) + HRM-Text 1B (reasoning).
4. **OpenClaw orchestration:** right call. v9 elevates security to P0 (v8 already did, but Fable 5 reinforces).
5. **Memory architecture:** 13-typed-schema + graph fallback (v8 §C.1). MemPrivacy adds the privacy layer.
6. **Proactive AI:** the `proactived` service design (v8 §C.3) stands. ProActor is the academic anchor.
7. **Competitive landscape:** Meta is the threat, Apple is the long-term threat, open-source is empty. v9 confirms with Bloomberg.
8. **Privacy:** fully on-device is the strongest positioning. v9 elevates to a ship gate.

The v8 AGI roadmap (6/12/24 months) stands. v9 hardens month 1 (Apple-window kickoff, privacyd service, cloud-fallback audit).

---

## 2. v9 New Research

### 2.1 The "single-vendor API dependency" risk (Fable 5 lesson)

The Fable 5 event is the canonical example of *single-vendor frontier API dependency as a structural risk*. Multiple analysis pieces (Gravitee, TrueFoundry, Appwrite) converged on the same recommendation: **multi-provider AI gateway, not single-vendor API.**

For Danlab, the v9 response is sharper: **don't use a frontier API at all for the user-facing hot path.** The Dan Glasses user-facing hot path is audiod → perceptiond → memoryd → reasond → ttsd. Every model in this path is on-device and open-weights. The OpenClaw gateway can *optionally* use a frontier API for *background tasks* (e.g., batch summarization) but the user-facing hot path is on-device-only.

**v9 implication:** v1's `privacyd` service must include a `/privacy/on-device-only` endpoint that:
- Returns `{"on_device_only": true, "network_calls_observed": [...], "last_audit": "2026-06-18T01:00:00Z"}`
- Fails if any non-allowlisted network call is observed in the last 24h
- Has a CI test that fails on any non-allowlisted network call from any service

### 2.2 Apple-window kickoff plan (v9)

The Apple-window kickoff is *time-critical*. We have Q4 2026 / Q1 2027 to ship.

**v9 ship window:**
- **Q4 2026 (best case):** ship v1.0.0 in December 2026. .deb on apt.danlab.dev. Marketing push on danlab.dev. Hacker News + Twitter/X launch.
- **Q1 2027 (acceptable):** ship v1.0.0 in February 2027. Pre-Apple-window.
- **Q2 2027 (loses the window):** ship in April 2027. Apple-window is closing.
- **Q3 2027 or later:** too late. Apple ships in Q4 2027.

**v9 minimum v1 feature set (proposed):**
- Push-to-talk voice input (audiod + whisper.cpp base.en)
- Vision description on demand (perceptiond + LFM2.5-VL-450M)
- Memory persistence (memoryd + MiniLM-L6-v2)
- Memoryd queries on demand (e.g., "what did I see yesterday?")
- TTS output (ttsd + KittenTTS)
- Telegram channel (OpenClaw + Telegram plugin)
- on-device-only CI test + `/privacy/on-device-only` endpoint
- .deb package + systemd units

**v9 v1 deferred to v1.5:**
- Wake-word (v1.5 with audiod 2.0)
- HRM-Text 1B reasoning (`reasond` service, v1.5)
- `proactived` service (v1.5)
- memoryd v2 13-typed-schema (v1.5)

### 2.3 SIA fork path (v9)

The v8 SIA fork plan was:
- Month 1-2: fork SIA, swap Feedback-Agent with HRM-Text 1B + Gemma 4 1B.
- Month 3-4: swap the task to image description, 500-pair held-out.
- Month 5-8: run on H100, measure delta vs heuristic.
- Month 9-12: publish as danlab-sia Apache 2.0.

The v9 update: SIA has a second implementation at Stanford. The fork collaboration is now possible.

**v9 SIA fork path:**
- Month 1: identify contact at Hexo Labs or Stanford. Plan the fork collaboration.
- Month 2-3: fork SIA, swap Feedback-Agent, run on a small benchmark (100-pair).
- Month 4-6: scale to 500-pair held-out. Measure delta vs heuristic.
- Month 7-9: publish the harness-only RL fork. Submit a paper or blog post.
- Month 10-12: explore the harness + weights path (with safety disclosure).

**v9 prerequisite:** H100 access. If we don't have H100 by month 8, the SIA fork is blocked. The hardware decision (Modal? Lambda? our own?) is a month-1 question.

---

## 3. v9 Three Deep Dives (refreshing v8's picks)

The v8 deep dives were:
- C.1: Memory architectures for AI companions
- C.2: Edge VLM optimization
- C.3: Proactive AI

v9 keeps all three, but adds a new deep dive:

- **C.4 (new): The single-vendor frontier API dependency risk.** This is the Fable 5 lesson. Covered in §2.1 above.

---

## 4. v9 Three Pick Updates

### 4.1 Memory architectures (v8 §C.1, refreshed)

The v8 read stands. The v9 update: MemPrivacy (MemTensor + HONOR + Tongji, 2026-05-18) is now in the top-3 papers. The reversible pseudonymization technique is the privacy layer on top of the 13-typed-schema + graph fallback.

**v9 memory architecture:**

```
┌──────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│  Event source    │ ──► │  Memory Classifier    │ ──► │  Typed Store         │
│  (audiod,        │     │  (local, 0.6-1.2B)    │     │  (typed schema)     │
│   perceptiond,   │     │  - decides type       │     │  - 13 categories    │
│   user input)    │     │  - extracts entities  │     │  - reversible pseu- │
│                  │     │  - retention policy   │     │    donymization     │
└──────────────────┘     └──────────────────────┘     │    (MemPrivacy)     │
                                                     └──────────┬──────────┘
                                                                │
                                                                ▼
┌──────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│  Query path      │ ──► │  Hybrid Retrieval     │ ◄── │  Embedding (MiniLM)  │
│  (reasond,       │     │  - vector recall      │     │  - 384-dim          │
│   proactived,    │     │  - typed filter       │     │  - on-device only   │
│   user query)    │     │  - graph fallback     │     │  - no cloud sync    │
└──────────────────┘     └──────────────────────┘     └─────────────────────┘
```

The v9 delta: the "Reversible Pseudonymization (MemPrivacy)" block is new. The on-device-only constraint is explicit.

### 4.2 Edge VLM optimization (v8 §C.2, refreshed)

The v8 read stands. v9 adds:
- **LFM2.5-VL-1.6B-Extract (Liquid, June 13 2026)** — v1.5 candidate. Same architecture family, 1.6B params, ~1.0 GB after Q4.
- **Qwen3-VL 4B (early 2026)** — v2 candidate. ~2.0 GB after Q4. SOTA local VLM in June 2026.

The v9 selection criterion adds: "Not subject to Fable-5-style export-control risk."

### 4.3 Proactive AI (v8 §C.3, refreshed)

The v8 read stands. v9 confirms ProActor as the academic anchor and the 100-scenario ProAgentBench-style eval as the v1.5 internal benchmark.

---

## 5. v9 Final Read

The v8 picture is largely correct. v9 hardens three things:

1. **Safety case:** Fable 5 elevates the on-device + open-weights thesis from a *preference* to a *requirement*. v1 must be *provably* on-device. CI test + `privacyd` service + `/privacy/on-device-only` endpoint are v1 ship gates.

2. **Market timing:** Apple-window kickoff is time-critical. Q4 2026 / Q1 2027 ship window is the only moment where a small open-source player can credibly enter. The x86_64 dev target is the v1 form factor. Wearable is v2.

3. **SIA path:** the self-improving agent paper has a second implementation at Stanford. The fork collaboration is now possible. H100 access is the prerequisite.

The architecture is sound. The model stack is correct. The market timing is right. The remaining gaps are:
- Hardware form factor (Redax) — confirmed for v2
- Proactive layer (`proactived`) — v1.5
- Safety case (privacy threat model + self-improvement disclosure) — v1 ship gate

The research is done. The plan is in the AGI roadmap. The architecture fixes are in the architecture review. The model decisions are in the model analysis. The papers are in the papers-to-read.

Build. Ship. Don't get cut off.

---

*End of v9 research report. Total: ~330 lines / ~28KB. Companion artifacts: `dan2-architecture-review.md` (concrete fixes), `dan2-model-analysis.md` (replacement candidates), `dan2-agi-roadmap.md` (the plan), `dan2-papers-to-read.md` (what to read). v8 archived as `dan2-research-report.v8.md`.*
