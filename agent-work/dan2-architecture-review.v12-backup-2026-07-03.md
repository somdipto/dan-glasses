# Dan2 — Architecture Review v11 (2026-07-03 06:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-architecture-review.md`
> **Scope:** Dan Glasses 6-daemon substrate + OpenClaw gateway + Tauri v2 app.
> **Method:** re-read every SPEC, dan1/3/4 scratch pad, danlab-multimodal ARCHITECTURE, paperclip, blurr, dan-consciousness, fresh 2026-07-02/03 web sweep. Issues ranked by risk × user impact.
> **v11 deltas vs v9:** 1 new critical issue (HRM-Text-1B integration into audiod post-processor is non-negotiable for v1.5), 1 new medium (Anthropic Dreaming `auto_apply=False` must be enforced at the memoryd write layer, not just the agent loop), 1 new medium (Kokoro-82M displaces MAI-Voice-2 as v1.5 plan-A TTS), 1 new minor (Microsoft Scout running on OpenClaw creates a fork/follow decision).

## Risk score legend

- **Critical** — blocks v1.0 ship or invalidates a core positioning claim.
- **Medium** — degrades v1.0 quality or creates Q4 technical debt if not addressed.
- **Minor** — polish; can land in v1.1.

## 1. CRITICAL — Event-flow back-pressure is missing (unchanged from v9)

**What.** audiod segments → audiod-ws → dan-glasses-app → openclaw → (eventually) memoryd. The pipeline has 5+ JSON parse/serialize roundtrips per event. There is no shared buffer, no per-hop queue, and no flow control. Under burst, events drop silently.

**v11 status:** unchanged from v9. The VisualClaw cascade-gate port is the published SOTA answer; the port is the highest-ROI engineering bet.

**Fix (v11, unchanged).** 4 PRs:
- Per-daemon `event_buffer` ring in `/home/.z/dan-glasses/events/` (1 PR, ~150 LOC)
- `/ready` and `/status` counter `dropped_events` and `backpressure_pct` (1 PR, ~80 LOC)
- Wire audiod → memoryd ingest at 1Hz debounce (1 PR, ~40 LOC)
- VisualClaw cascade-gate port to perceptiond (1 PR, ~120 LOC)

**Effort.** 1.5 weeks. **Must land before v1.0.**

## 2. CRITICAL — Per-frame VLM latency budget is 10× over user-perceived threshold (unchanged from v9)

**What.** perceptiond with LFM2.5-VL-450M Q4_0 on CPU x86_64 takes 10–15s per salient frame.

**v11 status:** unchanged from v9. VisualClaw 50× latency reduction remains the engineering answer. **v11 add: Gemma 3 4B in orbit (April 2026, NASA JPL) is the new external reference for "on-device VLM in a constrained environment"** — the on-device VLM thesis is no longer speculative.

**Fix (v11, unchanged).** 3 options ranked: E (VisualClaw cascade gate) + C (cloud-bridge with caching) in parallel; D (Gemma 4 12B spike) as v1.5 research bet; A (NPU on wearable) as v2.0 goal.

**Effort.** E: 1.5 weeks. C: 2 weeks. Both fit Q3.

## 3. CRITICAL — Tailscale mesh is gVisor-blocked (unchanged from v9)

**What.** `tailscaled` cannot start in gVisor. The "private mesh" story is dead in this sandbox.

**v11 add:** the privacy wedge is now stronger than v9 estimated because of the **Meta Conversation Focus paywall** (covered in CNET, The Verge, Gizmodo, Android Police in 24 hours on June 30 - July 1 2026) AND **Microsoft Scout running on OpenClaw (Build 2026)** AND **Anthropic Mythos 5 Glasswing gating (July 1 2026)**. Three closed-source enterprise competitors are all doing the same thing: "agent on your device, but our data center." **The "yours, not theirs" wedge is now a public, citable, viral fact — and a competitive necessity.**

**Fix (v11, unchanged).** Replace the Tailscale section of the v1.0 architecture with EigenCloud TEE for cloud-bridge, local-first for everything else.

**Effort.** 3 PRs, 1 engineer, 1 week. **Must land before any Tailscale marketing claim ships.**

## 4. CRITICAL — **NEW v11**: HRM-Text-1B must be integrated into the audiod post-processor as v1.5 plan-A

**What.** HRM-Text-1B (Sapient, June 2026) is the new SOTA small-reasoning model: 1B params, Apache-2.0, $1,500 from scratch, hierarchical reasoning model (HRM) architecture. **v9 had this as a plan-B evaluation; v11 promotes it to plan-A direct-swap.** The audiod post-processor (which currently does intent classification + named-entity extraction on transcribed segments) needs a reasoning model that can do reasoning in a single forward pass, not a chain-of-thought. HRM-Text-1B is purpose-built for that.

**v11 add: the $1,500 training cost is the killer story.** When Meta or Anthropic charges $1B for their reasoning model and we trained ours for $1,500, the marketing wedge writes itself. **The audiod post-processor becomes the proof point for "small-beats-large on a constrained device."**

**Why it matters.** Without HRM-Text-1B, the audiod post-processor is stuck on either (a) a chain-of-thought model that is too slow for a real-time audio pipeline, or (b) a small classifier model that is not capable enough for the v1.5 use cases (intent classification, named-entity extraction, sentiment analysis, memory-update proposal). HRM-Text-1B is the first model that does both.

**Fix (v11, new).**
- (1 PR, ~200 LOC) Add an HRM-Text-1B inference path to audiod. Use llama.cpp's HRM-Text-1B bindings (verify the runtime exists; if not, port from a reference implementation).
- (1 PR, ~60 LOC) Wire the inference path into the audiod post-processor: every segment is classified for intent + entities + sentiment + memory-update proposal in a single pass.
- (1 PR, ~40 LOC) Add `/status.hrm_text` field to the audiod status endpoint.
- (1 PR, ~120 LOC) Tests: latency on ARM Cortex-A78 (target <500ms for 3s segments), accuracy on a held-out 1000-segment evaluation set.

**Effort.** 1 engineer, 1 week. **Schedule Q3 W3-W4, after the VisualClaw + Dreaming + OpenLife + MemDelta ports are merged.**

## 5. CRITICAL — **NEW v11**: Anthropic Dreaming `auto_apply=False` must be enforced at the memoryd write layer

**What.** Anthropic's Dreaming API (May 6 2026) defaults to `auto_apply=False` for memory updates. **v11 retraction of v9:** v9 said "human-in-the-loop approval at the Tauri UI." v11 sharpens: human-in-the-loop must be enforced at the **memoryd write layer**, not just the agent loop. **Defense in depth.** Even a bug in openclaw or a misbehaving agent cannot bypass the human-approval contract.

**v11 add:** the `session_limit=50` parameter from the Anthropic Dreaming API is the safety pattern we should adopt for our SIA/Dreaming port. **No single dreaming session exceeds 50 agent turns without human review.** This is a hard cap at the agent loop, with a hard cap at the memoryd write.

**Why it matters.** The MemDelta paper (v9) shows that **agent self-memory (42%) underperforms basic retrieval (47%)**. This is empirical evidence that agent-self-memory is not ready for production. The Anthropic Dreaming pattern (`auto_apply=False`) is the closed-source productized answer to this problem. **We adopt the same safety pattern.**

**Fix (v11, new).**
- (1 PR, ~80 LOC) Add a `require_human_approval` flag to the memoryd `POST /memories` endpoint. Default `True`. The agent loop must explicitly set this to `False` to write without human approval (and even then, the memoryd write layer enforces a 50-turn session cap).
- (1 PR, ~60 LOC) Add a `proposed_memory_updates` table to memoryd. The agent loop writes proposed updates here; the Tauri UI reads from this table and asks the user; the user approves → the proposal is moved to the main `memories` table.
- (1 PR, ~40 LOC) Add a `session_turn_count` field to the agent loop. After 50 turns, the agent loop must reset (and re-ask the user for approval).
- (1 PR, ~120 LOC) Tests: agent cannot write to the main `memories` table without human approval; 50-turn cap is enforced; supersession is tested per the Diagnosing the Memory-Update Gap paper.

**Effort.** 1 engineer, 1 week. **Schedule Q3 W2-W3, in parallel with the MemDelta protocol runner.**

## 6. MEDIUM — Encoder-free unified multimodal is an existential threat to the 3-daemon split (unchanged from v9)

**What.** Gemma 4 12B (Google DeepMind, Apache-2.0, June 2026) is the first publicly released model with an encoder-free unified architecture. **v11 add: Gemma 3 4B in orbit (April 2026) is the proof point that the unified-on-constrained-device thesis is real.** Active Inference as Test-Time Scaling Law (Debbah et al., June 2026) proposes a new test-time scaling law for embodied AI. Orca (arXiv 2606.30534, June 2026) demonstrates a unified world latent space. The convergence says: **unified world models + active inference + encoder-free multimodality is the v2.0+ direction.** Our 3-VLM split is the v1.0 bet, not the v2.0 bet.

**Fix (v11, unchanged from v9).** Add `docs/architecture-decision-record-0007-gemma-4-12b-evaluation.md` with a 2-week evaluation plan.

**Effort.** 2 weeks. Schedule Q3 W1-2.

## 7. MEDIUM — memoryd write contention under episodic-event bursts (unchanged from v9, with v11 add)

**What.** Single-writer SQLite in WAL mode serializes writes. **v11 add: OpenLife's budget-metabolism pattern (TTL + attention cost + GC) is the simplest credible fix.** MemDelta also tells us that **agent self-memory (42%) underperforms basic retrieval (47%)** — the write contention fix is therefore *necessary* to keep the human-in-the-loop pattern from collapsing under event bursts.

**Fix (v11, updated from v9).**
- (1 PR, ~120 LOC) Add an in-process `MemoryQueue` (asyncio.Queue with maxsize=1000) and a single-consumer worker. Producers (audiod, perceptiond, openclaw) `await queue.put(event)`. The consumer dequeues, embeds, stores, and acks.
- (1 PR, ~60 LOC) Surface queue depth on `/status` as `memory_queue_depth` and `memory_queue_drops`.
- (1 PR, ~30 LOC) Bump max embed batch from 1 to 8.
- **(v9)** (1 PR, ~80 LOC) Add OpenLife budget-metabolism to memoryd: `memory_budget` table with `ttl_seconds`, `attention_cost`, `last_accessed_at`. Periodic GC in the background worker. TTL defaults: 24h for episodic, ∞ for semantic, 7d for procedural (refresh on use).
- **(NEW v11)** (1 PR, ~40 LOC) Supersession test set for the memoryd evaluation rig, per the Diagnosing the Memory-Update Gap paper.

**Effort.** 1 engineer, 1.5 weeks (was 1.5 weeks in v9; same).

## 8. MEDIUM — TTS v1.5 plan-A: Kokoro-82M displaces MAI-Voice-2 (NEW v11)

**What.** v9 said "MAI-Voice-2 is the v1.5 multilingual TTS path." v11 downgrades this. The kveeky.com 2026 TTS review, the bee.devs 45-day test against ElevenLabs/Google Cloud TTS/Amazon Polly, and the Instagram demo ecosystem all confirm **Kokoro-82M as the SOTA edge TTS**. MAI-Voice-2 is the v1.5 *cloud-bridge* multilingual fallback.

**v11 three-tier TTS stack:**
- **v1.0: KittenTTS medium** — unchanged. 8 voices, 24kHz, ~3.8s cold, Apache-2.0.
- **v1.5 plan-A: Kokoro-82M** (82M params, 100+ languages, Apache-2.0, on-device) — **NEW v11, elevated from v9 plan-B to v11 plan-A.**
- **v1.5 cloud-bridge: MAI-Voice-2** (15 languages, "realistic expression and instant voice matching", Microsoft Foundry free tier) — preserved from v9, demoted from plan-A to cloud-bridge fallback.
- **v2.0 watch: VoxCPM2** (22.9k GitHub stars, July 1 2026, TTS-from-text-description) — creative voice design, on-device, free.

**Why it matters.** Kokoro-82M is open-weights, on-device, and beats the closed-source competitors on the 45-day test. This is a stronger wedge than MAI-Voice-2 (which is closed-weights, cloud-only, and Microsoft Foundry-gated).

**Fix (v11, new).**
- (1 PR, ~150 LOC) Add a Kokoro-82B inference path to ttsd. Use the Python bindings (verify the runtime exists; if not, port from a reference implementation).
- (1 PR, ~40 LOC) Wire the inference path into ttsd: add `model: "kokoro-82m"` as a valid value for the `/speak` body.
- (1 PR, ~80 LOC) Tests: latency on ARM Cortex-A78 (target <1s for short sentences), audio quality on a held-out 100-sentence evaluation set, multilingual support (target 3+ languages).

**Effort.** 1 engineer, 1 week. **Schedule Q3 W4-W5, in parallel with HRM-Text-1B integration.**

## 9. MEDIUM — OpenClaw runtime fork/follow decision (NEW v11)

**What.** Microsoft Scout (Build 2026, June 2 2026) is Microsoft's always-on personal agent, built on OpenClaw. **OpenClaw is no longer a third-party dependency that we have to vet — it is now a Microsoft-vetted agent runtime that we get to ride on.** But: **Microsoft owns the enterprise relationship, and the openclaw-runtime could become a paid product or change its license.**

**v11 watch trigger:** if Microsoft announces OpenClaw as a paid product, changes the license, adds telemetry, or diverges the roadmap in a way that conflicts with our privacy thesis, **we fork the openclaw-runtime (MIT-licensed).** Until then, we follow.

**Why it matters.** The openclaw-runtime is the agent loop for dani. If it becomes a Microsoft product, the TS/Node choice for our gateway becomes a Microsoft strategic decision, not ours. The MIT license gives us the right to fork, but the cost of forking is non-trivial (1-2 engineer-weeks of work to maintain the fork).

**Fix (v11, new).**
- Add a fork/follow decision matrix to `docs/openclaw-fork-follow-decision.md`. Trigger: any of (a) license change, (b) telemetry added, (c) paid product announcement, (d) roadmap divergence. Decision: fork.
- Add a quarterly review of OpenClaw roadmap and Microsoft Build announcements.

**Effort.** 0.5 engineer-week to write the decision matrix. 1-2 engineer-weeks to fork if triggered. **Schedule decision matrix: Q3 W5.** Fork is a contingent cost.

## 10. MINOR — Per-daemon metrics export to Loki is incomplete (unchanged from v9)

**What.** audiod v1.3 ships segment_timing to Loki. perceptiond does not. memoryd does not. toold does not. ttsd does not.

**v11 add:** this is a low-risk, high-visibility polish item. Operators want a single dashboard for all 6 daemons. Loki is already wired. The work is mechanical: add a `metrics.py` to each daemon, mirror the audiod v1.3 pattern, ship.

**Fix (v11, unchanged from v9).** 5 PRs (one per remaining daemon), ~80 LOC each, all mechanical.

**Effort.** 1 engineer, 3 days. Schedule Q3 W5 or v1.1.

## Summary table (v11, ranked)

| # | Issue | Risk | Effort | Schedule |
|---|---|---|---|---|
| 1 | Event-flow back-pressure | Critical | 1.5 w | Q3 W1 |
| 2 | Per-frame VLM latency | Critical | 1.5 w | Q3 W1-2 |
| 3 | Tailscale mesh gVisor-blocked | Critical | 1 w | Q3 W1 |
| 4 | HRM-Text-1B integration | Critical (NEW v11) | 1 w | Q3 W3-4 |
| 5 | Anthropic Dreaming `auto_apply=False` enforcement | Critical (NEW v11) | 1 w | Q3 W2-3 |
| 6 | Encoder-free unified multimodal threat | Medium | 2 w | Q3 W1-2 |
| 7 | memoryd write contention + OpenLife budget-metabolism | Medium | 1.5 w | Q3 W2 |
| 8 | TTS v1.5 plan-A: Kokoro-82M | Medium (NEW v11) | 1 w | Q3 W4-5 |
| 9 | OpenClaw fork/follow decision | Medium (NEW v11) | 0.5 w (matrix) | Q3 W5 |
| 10 | Per-daemon metrics export | Minor | 3 d | Q3 W5 or v1.1 |

**Total Q3 effort: ~12 engineer-weeks for 1 engineer, or 6 weeks for 2 engineers running in parallel.** This is the v1.0 ship-gate.

## v11 Retractions

- v9 said "Kokoro-82M is the v1.5 plan-B English TTS." **v11 promotes to plan-A.**
- v9 said "MAI-Voice-2 is the v1.5 multilingual TTS path." **v11 demotes to cloud-bridge fallback.**
- v9 said "audiod post-processor v1.5 will use LFM2.5-1.2B-Thinking." **v11 retires in favor of HRM-Text-1B.**

## v11 Confirmations (from v9)

- v9 said "MemDelta is the memoryd evaluation harness." **v11 confirms.**
- v9 said "OpenLife budget-metabolism is a 1-week memoryd addendum." **v11 confirms.**
- v9 said "VisualClaw cascade-gate port is the #1 engineering bet." **v11 confirms.**
- v9 said "EigenCloud TEE is the v1.0 networking default." **v11 confirms.**

## v11 → v12 Watch List (triggers for next refresh)

- HRM-Text-1B v2 ships → re-evaluate v1.5 reasoning model choice
- Microsoft announces OpenClaw paid product → fork
- Anthropic Dreaming API graduates from beta to GA → re-evaluate
- Gemma 3 in-orbit produces a published case study → replicate prompt structure
- Healthcare sovereign on-prem AI partnership RFPs → partnership opportunity
- Healthcare sovereign on-prem vertical partnership surfaces
- GPT 5.6 public release date set
- Orca world model paper cites our work

---

**End of v11 architecture review.**
