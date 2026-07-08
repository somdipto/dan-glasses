# Dan2 — Architecture Review v14 (2026-07-03 04:00 UTC / 09:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-architecture-review.md`
> **Scope:** Dan Glasses 6-daemon substrate + OpenClaw gateway + Tauri v2 app.
> **Method:** re-read every SPEC, dan1/3/4 scratch pad, danlab-multimodal ARCHITECTURE, paperclip, blurr, dan-consciousness, fresh 2026-07-03 web sweep.
> **Backup of v13:** `dan2-architecture-review.v13-backup-2026-07-03.md`
> **v14 deltas vs v13 (2 new issues, 1 sharpening, 1 promotion, 0 broad retractions):** 1 new CRITICAL (Memora storage/retrieval split → memoryd v1.5 architecture), 1 new MEDIUM (PR-review "X% AI-generated" tag → Godot signal, defense in depth), 1 sharpening (held-out ground truth is a memoryd write, not a perceptiond subsystem), 1 promotion (decomposition score 7.5/10 → 8.0/10; Memora + MiCRo validate the 6-daemon split as the 2026 research direction).

## Risk score legend

- **Critical** — blocks v1.0 ship or invalidates a core positioning claim.
- **Medium** — degrades v1.0 quality or creates Q4 technical debt if not addressed.
- **Minor** — polish; can land in v1.1.

## 1. CRITICAL — Event-flow back-pressure is missing (unchanged from v9/v11/v13)

**What.** audiod segments → audiod-ws → dan-glasses-app → openclaw → (eventually) memoryd. The pipeline has 5+ JSON parse/serialize roundtrips per event. There is no shared buffer, no per-hop queue, and no flow control. Under burst, events drop silently.

**v14 status:** unchanged. The VisualClaw cascade-gate port is the published SOTA answer; the port is the highest-ROI engineering bet.

**Fix (v14, unchanged from v13).** 4 PRs:
- Per-daemon `event_buffer` ring in `/home/.z/dan-glasses/events/` (1 PR, ~150 LOC)
- `/ready` and `/status` counter `dropped_events` and `backpressure_pct` (1 PR, ~80 LOC)
- Wire audiod → memoryd ingest at 1Hz debounce (1 PR, ~40 LOC)
- VisualClaw cascade-gate port to perceptiond (1 PR, ~120 LOC)

**Effort.** 1.5 weeks. **Must land before v1.0.**

## 2. CRITICAL — Per-frame VLM latency budget is 10× over user-perceived threshold (unchanged from v9/v11/v13)

**What.** perceptiond with LFM2.5-VL-450M Q4_0 on CPU x86_64 takes 10–15s per salient frame.

**v14 status:** unchanged. VisualClaw 50× latency reduction remains the engineering answer. **v14 add: MiCRo (EPFL, late June 2026) validates the on-device specialized-region architecture. Our 6-daemon split is the engineering analogue of the MiCRo "4 cognitive regions" pattern.** External validation.

**Fix (v14, unchanged from v13).** 3 options ranked: E (VisualClaw cascade gate) + C (cloud-bridge with caching) in parallel; D (Gemma 4 12B spike) as v1.5 research bet; A (NPU on wearable) as v2.0 goal.

**Effort.** E: 1.5 weeks. C: 2 weeks. Both fit Q3.

## 3. CRITICAL — Tailscale mesh is gVisor-blocked (unchanged from v9/v11/v13)

**What.** `tailscaled` cannot start in gVisor. The "private mesh" story is dead in this sandbox.

**v14 sharpening:** the privacy wedge is now stronger than v13 estimated because of the **BBC-reported Meta Conversation Focus paywall ($19.99/mo for 15hr, July 2 2026)** AND **Apple Siri AI WWDC 2026 price hike strategy (new hardware required)** AND **Microsoft Scout running on OpenClaw (Build 2026)** AND **Anthropic Mythos 5 Glasswing gating ($30K catch)** AND **Anthropic Sonnet 5 priced 5-57x higher than GLM-5.2 / Kimi-K2.6 / DeepSeek-V4-Pro (X coverage, late June 2026)**. **Five closed-source enterprise competitors are all doing the same thing: "agent on your device, but our data center." The "yours, not theirs" wedge is now a BBC-reported, citable, viral, public, quantified fact. BBC + 5x cost multiplier + $30K catch = a six-step empirical marketing narrative.** **v14 marketing lead update: "Meta paywalls $19.99/mo for 15 hours of on-device AI (BBC, July 2 2026). Apple charges $1,200+ to upgrade. Anthropic Sonnet 5 is 5-57x more expensive than GLM-5.2 / Kimi-K2.6 / DeepSeek-V4-Pro. Dan Glasses is $349 once, on-device, auditable, open-weights, forever."**

**Fix (v14, unchanged from v13).** Replace the Tailscale section of the v1.0 architecture with EigenCloud TEE for cloud-bridge, local-first for everything else.

**Effort.** 3 PRs, 1 engineer, 1 week. **Must land before any Tailscale marketing claim ships.**

## 4. CRITICAL — Red Queen moving-judge pattern for danlab-multimodal (unchanged from v12/v13)

**What.** Red Queen Gödel Machine (arXiv:2606.26294v1, June 24 2026, Cambridge + NVIDIA) is the first credible mechanism for self-improving agents with empirical safety results. Headline findings: 1.35–1.72× fewer steps than HGM-H on code/math benchmarks; 1.91× AI-paper over-acceptance bias in static judges reduced to ~1.0× with the moving judge.

**v14 sharpening (new):** the held-out ground truth set is now a **memoryd write**, not a perceptiond-local file. The `auto_apply=False` contract binds here too — ground truth is a procedural memory, rotated weekly by the human, stored in memoryd's procedural table, queried via the standard memory API. **Single source of truth, no new endpoint.** This retracts the v13 implication that ground truth is a separate perceptiond subsystem.

**Why it matters (v14 sharpening).** Decoupling ground truth from perceptiond local state means the held-out set is one of many memoryd inputs, governed by the same Memora-style storage/retrieval split (issue #6 below), and the same `auto_apply=False` contract as the agent's dream-loop writes. The v12/v13 4-PR plan is reduced to 3 PRs:
- (1 PR, ~80 LOC) Add a `held_out_ground_truth` procedural memory type to memoryd's schema. The ground truth set is a single memory record with a TTL (7 days) and a `rotated_by: somdipto` metadata field.
- (1 PR, ~120 LOC) Add a `perceptiond.ground_truth_eval()` endpoint that fetches the held-out set via memoryd's standard API, re-scores the last 7 days of perceptiond descriptions, and surfaces a calibration report (TP/FP/FN + per-class precision/recall).
- (1 PR, ~60 LOC) Add a Tauri UI panel: "Calibration Report" tab. Shows the last 7 days of held-out scoring. Human can drill into FP/FN and override the salience gate.
- (1 PR, ~40 LOC) Wire the calibration report to memoryd so the human-override is recorded as a procedural memory (not a new local file).
- (1 PR, ~120 LOC) Tests: held-out set rotation works via the standard memoryd API, scoring is deterministic, calibration report is reproducible, supersession is tested per the Diagnosing the Memory-Update Gap paper.

**Effort.** 1 engineer, 2 weeks. **Schedule Q3 W1-W2, parallel to VisualClaw + Anthropic Dreaming ports.**

## 5. CRITICAL — Anthropic Dreaming `auto_apply=False` must be enforced at the memoryd write layer (unchanged from v11/v13)

**What.** Anthropic's Dreaming API (May 6 2026) defaults to `auto_apply=False` for memory updates. **v11: human-in-the-loop must be enforced at the memoryd write layer, not just the agent loop. Defense in depth.** **v12/v13: the Red Queen moving judge (issue #4) is the structural enforcement; this is the per-write enforcement. Both layers are required.** **v14 sharpening: with the Memora storage/retrieval split (issue #6), the `auto_apply=False` contract binds at the *storage* layer, not the *retrieval* layer. Storage = rich (raw descriptions, raw held-out set, raw agent proposals), retrieval = lightweight abstractions (cue anchors, summaries). Human approves at storage write; retrieval is automatic.**

**Fix (v14, unchanged from v13).** 4 PRs (as v11).

**Effort.** 1 engineer, 1 week. **Schedule Q3 W2-W3, in parallel with the MemDelta protocol runner.**

## 6. CRITICAL — **NEW v14**: Microsoft Memora storage/retrieval split is the new memoryd v1.5 architecture

**What.** Microsoft Memora (Microsoft Research blog, July 2026, Xuchao Zhang et al.) decouples "what is stored" (rich memory content) from "how it is retrieved" (lightweight abstractions and cue anchors), balancing abstraction and specificity. **Reduces context token usage by up to 98% while matching or exceeding full-context accuracy.** This is a published 2026 closed-source competitor to our memoryd v1.0. The MemDelta v9 finding ("agent self-memory 42% < basic RAG 47%") is the problem statement; Memora is Microsoft's answer.

**Why it matters.** Our current memoryd v1.0 has a single storage type (episodic/semantic/procedural) and a single retrieval path (cosine similarity on the embedded content). The MemDelta paper showed this is inferior to basic RAG. The Memora pattern is the architectural fix: storage is rich, retrieval is lightweight abstraction, and the two are decoupled.

**Fix (v14, new).** 5 PRs:
- (1 PR, ~120 LOC) Add a `storage` table to memoryd that holds the rich content (descriptions, audio segments, held-out ground truth, agent dream-loop proposals). This is what is written to disk; this is the source of truth.
- (1 PR, ~100 LOC) Add a `cue` table that holds the lightweight retrieval abstractions. Each cue is a short anchor (a tag, a topic, a person, a place, a time) with a reference to the rich storage entry. The cue is what is embedded and what is retrieved.
- (1 PR, ~80 LOC) Modify `/v1/embeddings` to embed cues, not storage. This is the "lightweight retrieval" path.
- (1 PR, ~60 LOC) Add a `cue_extract` endpoint that, given a storage entry, returns the cue(s). v1.5 uses a small local LLM (e.g., Apertus v1.1 4B or HRM-Text-1B) to extract the cue. v1.0 keeps the human-in-the-loop `auto_apply=False` pattern.
- (1 PR, ~150 LOC) Tests: storage and retrieval are decoupled, cue extraction is deterministic, supersession is tested per the Diagnosing the Memory-Update Gap paper, MemDelta protocol runner runs end-to-end.

**Effort.** 1 engineer, 2 weeks. **Schedule Q3 W2-W3, parallel to the Anthropic Dreaming port. Must land before v1.0 ship.**

## 7. CRITICAL — No hardware-defined power budget for the wearable (unchanged from v9/v11/v13)

**What.** Without a Redax aarch64 board in hand, we cannot characterize the v1.0 VLM power draw. Google + Samsung Android XR sets a 4hr battery bar; Meta Ray-Ban Display runs ~3hr on full AI. Without a target, the BOM cannot be sized.

**v14 status:** unchanged. **v14 sharpening: Q4 2026 RAM price spike (+40-50% Q3, +30% Q4, TechSpot/Jefferies) makes this even more critical. The wearable BOM is at risk. INT8 quantization on the VLM cuts RAM by ~30-40%, partially absorbing the spike.** Lock the BOM target at 4GB/64GB minimum (down from 8GB/128GB) to leave headroom.

**Fix (v14, unchanged from v13).** 1 PR to docs/ + 1 PR to v1.0 PRD + a 1-week BOM-target spike.

**Effort.** 1 engineer-week. **Must land before any wearable marketing claim ships.**

## 8. MEDIUM — Encoder-free unified multimodal is an existential threat to the 3-daemon split (unchanged from v9/v11/v13)

**What.** Gemma 4 12B (Google DeepMind, Apache-2.0, June 2026) is the first publicly released model with an encoder-free unified architecture.

**v14 sharpening (new):** **MiCRo (EPFL, late June 2026) is the published 2026 SOTA for the "specialized regions" pattern — but as a monolithic model, not a daemon split.** The 6-daemon Dan Glasses split (audiod, perceptiond, memoryd, toold, ttsd) is the engineering analogue. **The decomposition is validated as the 2026 research direction, not just engineering pragmatism.** External validation does not change the threat; it sharpens our marketing position.

**Fix (v14, unchanged from v13).** Add `docs/architecture-decision-record-0007-gemma-4-12b-evaluation.md` with a 2-week evaluation plan.

**Effort.** 2 weeks. Schedule Q3 W1-2.

## 9. MEDIUM — memoryd WAL checkpoint + embedding batched writes (unchanged from v11/v13)

**What.** SQLite WAL mode is on, but the checkpoint interval is auto. Under burst write, the WAL file can grow unbounded.

**v14 status:** unchanged. **v14 add: with the Memora storage/retrieval split (issue #6), the WAL pressure is concentrated on the `storage` table. The `cue` table is small and read-heavy. The fix is the same as v13: explicit checkpoint, batched writes.**

**Fix (v14, unchanged from v13).** 2 PRs, 2 days.

**Effort.** Trivial.

## 10. MEDIUM — toold 120s timeout shared globally (unchanged from v9/v11/v13)

**What.** Every tool call has the same 120s ceiling. There is no per-tool timeout.

**Fix (v14, unchanged from v13).** 1 PR, 1 day.

**Effort.** Trivial.

## 11. MEDIUM — No per-daemon metrics export (unchanged from v9/v11/v13)

**What.** audiod v1.3 ships Loki push. memoryd, perceptiond, ttsd, toold do not.

**v14 status:** unchanged. **v14 add: with the Memora storage/retrieval split (issue #6), memoryd metrics now include cue-extraction latency, cue-storage size, and storage-to-cue ratio. These are the new v1.5 memoryd metrics.**

**Fix (v14, unchanged from v13).** 4 PRs, 1 PR per daemon, ~80 LOC each.

**Effort.** 1 engineer-week.

## 12. MEDIUM — **NEW v14**: PR-review "X% AI-generated" tag (Godot signal, defense in depth)

**What.** Godot Foundation banned AI-generated PRs (July 2 2026) on the grounds that "we can't trust heavy users of AI to understand their code enough to fix it." This is a published 2026 open-source governance signal. **Our openclaw agent writes code; the human must be able to fix it.**

**Why it matters.** As we adopt the v11 `auto_apply=False` + v12 Red Queen moving judge + v14 Memora storage/retrieval split, the human-in-the-loop contract is at the engineering-process level, not just the agent-loop level. A PR-review tool that surfaces "this PR is X% AI-generated" alongside the change is the v14 operational implementation.

**Fix (v14, new).** 1 PR, ~100 LOC. Add a `pr_review` tool to openclaw. The tool inspects git diff for AI-generation signatures (long unbroken generation, specific token-pattern distributions, code-style markers) and returns a 0-100 score. The score is added to the PR description alongside the human-reviewer's sign-off.

**Effort.** 1 engineer, 3 days. **Schedule Q3 W1.**

## 13. MINOR — Per-daemon health endpoint shape varies (unchanged from v9/v11/v13)

**What.** audiod, perceptiond, memoryd, toold, ttsd, os-toold all have `/health` and `/status` but with different shapes. dan-glasses-app's proxy has to special-case each.

**Fix (v14, unchanged from v13).** 1 PR to docs/, 1 PR to each daemon (6 PRs total, ~20 LOC each), 1 PR to dan-glasses-app.

**Effort.** 1 engineer-week. Schedule Q3 W3.

## 14. MINOR — No replay mode for memoryd (unchanged from v9/v11/v13)

**What.** Replaying a memory sequence is a 2-PR job. Not blocking.

**Fix (v14, unchanged from v13).** 2 PRs, 2 days.

**Effort.** Trivial.

## 15. MINOR — perceptiond watchdog has no liveness probe (unchanged from v9/v11/v13)

**What.** The capture loop can hang silently. v5 added an MJPEG viewfinder, but no `/live` probe.

**Fix (v14, unchanged from v13).** 1 PR, 1 day.

**Effort.** Trivial.

## 16. MINOR — **NEW v14**: OpenClaw agent shortlist expansion (SIA-W+H, Mirendil, Hermes Agent, Memora pattern)

**What.** v12 had a 2-agent shortlist (SIA-W+H + Anthropic Dreaming). v14 expands to 4: SIA-W+H (MIT, published, plan-A), Hermes Agent (Nous Research, MIT, open-source framework, plan-B if SIA stalls), Mirendil (a16z-backed, closed, research-only), Memora (Microsoft, closed, reference pattern only).

**Why it matters.** The 4-agent shortlist is the v14 risk-mitigation against SIA port stalling. SIA is still plan-A, but Hermes Agent is now a published, MIT-licensed fallback. This is a research spike, not a code spike.

**Fix (v14, new).** 1 PR to docs/research.md. ~50 LOC of analysis. No code.

**Effort.** 1 engineer-week. Schedule Q3 W2.

---

## Summary (v14)

**Decomposition score: 8.0/10** (up from v13's 7.5/10; Memora + MiCRo validate the 6-daemon split as the 2026 research direction).

**Critical (must land before v1.0):** 1, 2, 3, 4, 5, 6, 7 (7 issues; was 6 in v13; **6 is new v14**).

**Medium (degrades v1.0 quality):** 8, 9, 10, 11, 12 (5 issues; was 4 in v13; **12 is new v14**).

**Minor (polish):** 13, 14, 15, 16 (4 issues; was 3 in v13; **16 is new v14**).

**v14 retractions:** 0 broad. v13's 4-PR Red Queen plan is reduced to 3 PRs (ground truth is a memoryd write, not a perceptiond subsystem).

**v14 priorities, ordered:**
1. **Memora storage/retrieval split port to memoryd v1.5** (issue #6, 2 weeks, Q3 W2-W3, plan-A). The v14 headline architecture decision.
2. **Red Queen moving-judge pattern** (issue #4, 2 weeks, Q3 W1-W2, with v14 sharpening to a memoryd write).
3. **VisualClaw cascade-gate port** (issue #2 + #1, 1.5 weeks, Q3 W1-W2).
4. **Anthropic Dreaming port** (issue #5, 1 week, Q3 W2-W3).
5. **PR-review "X% AI-generated" tag** (issue #12, 3 days, Q3 W1, defense in depth).
6. **OpenClaw agent shortlist expansion** (issue #16, 1 week, Q3 W2, research spike).

**v14 risks not in v13:**
- Memora ships as the closed-source benchmark before we port. Mitigation: spike starts in Q3 W2.
- Hermes Agent gains a "use your ChatGPT subscription" feature that competes with the v14 "no subscription" wedge. Mitigation: monitor; the on-device + auditable memory story is still ours.
- Godot-style open-source governance backlash against AI-generated PRs. Mitigation: PR-review "X% AI-generated" tag.
- Meta Watermelon ships before Q4 2026 with 10x Avocado compute. Mitigation: GLM-5.2 + HRM-Text-1B + Apertus v1.1 4B are the open-weights alternatives; the wedge is open + on-device, not "as smart as Meta's cloud."

---

## v13 architecture review (preserved for traceability)

[v13 issues 1-15 already in v13; see `dan2-architecture-review.v13-backup-2026-07-03.md` for the full v13 text.]
