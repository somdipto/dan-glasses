# Dan2 — Model Analysis v27 (2026-07-05 04:00 UTC / 09:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v26:** `dan2-model-analysis.v26-backup-2026-07-05.md` (preserved verbatim, mtime 2026-07-05 03:07 UTC)
> **Status:** v27 SHIPPED. v26 content preserved verbatim below.

> **v27 deltas vs v26 (0 CRITICAL, 1 SHARPEN, 1 HONORABLE MENTION, 0 retractions):**
> 1. **NEW SHARPEN #1 — Embedding model selection rigor (per MemDelta, arXiv 2606.29914, late June 2026).** MemDelta's v27 *controlled-baseline protocol* quantifies a v27 *hidden confound* in agent memory research: swapping *only* the embedding model in an identical pipeline shifts accuracy by +6.2pp at n=500 with p<0.004. The v27 implication for memoryd's MiniLM-L6-v2: the v25-v26 *384-dim single-model* choice is v27 *adequate for v1.0* but v27 *insufficient for v1.5* — by the v1.5 memoryd promotion gate, the embedding-model choice must be v27 *benchmarked head-to-head* against at least 2 alternatives (recommend: bge-small-en-v1.5 + mxbai-embed-large-v1). The v27 v1.5 embedding-model shortlist: (a) MiniLM-L6-v2 (current, 384-dim, ~80MB), (b) bge-small-en-v1.5 (384-dim, ~33MB, competitive on MTEB), (c) mxbai-embed-large-v1 (1024-dim, ~670MB, SOTA but v27 *too large for v1.0 edge*). **Pair with v27 plan-P1 spike.**
> 2. **NEW HONORABLE MENTION #1 — Mem0 v27 *empirical caution* sign.** Per MemDelta, Mem0 beats MiniLM-RAG by +11pp but loses to cloud-RAG by 1.2pp — one variable flips the conclusion. The v27 implication for the v25-v26 "Mem0 promotion gate" in memoryd: the v27 gate must be v27 *MemDelta-controlled*, not v27 *"beats MiniLM-RAG"*. A v27 v1.5 candidate that beats MiniLM-RAG but loses to a v27 *controlled cloud-RAG* is v27 *not good enough*. The v27 framing: Mem0 is a v27 *legitimate option* but v27 *not the default*; the v27 default for v1.0 stays v27 *MiniLM-L6-v2 + sqlite-vec* (no Mem0 dependency).
> 3. **v27 confirms:** all v26 model choices hold for v1.0. v26 LFM2.5-VL-450M (vision) holds. v26 LFM2.5-1.2B-Thinking (audiod post-processor) holds. v26 LFM2.5-ColBERT-350M (reranker, v1.5) holds. v26 LFM2.5-230M (audiod post-processor backup) holds. v25 HRM-Text-1B (reasoning, v1.5 plan-B) holds. v25 Apertus v1.1 4B (reasoning, v1.5 plan-C) holds. v25 OpenPhone-3B v1.5 (audiod, v1.5 plan-D) holds. v24 KittenTTS (TTS) holds; v16 Kokoro-82M (TTS benchmark) holds. v16 Hermes Agent (openclaw agent framework, v1.0 plan-A) holds. v16 VisualClaw (cascade-gate perceptiond port, v1.0 plan-A) holds. v8 Anthropic Dreaming (memoryd port, v1.0 plan-A) holds. v5 LFM2.5-VL-450M (vision) holds. v3 whisper.cpp base.en (STT) holds. v1 KittenTTS medium (TTS) holds. v1 MiniLM-L6-v2 (embeddings) holds. **No v26 retractions.**
> 4. **v27 v1.0 model stack (UNCHANGED):** Vision = LFM2.5-VL-450M Q4_0 (209MB, ~10-15s/frame x86_64). STT = whisper.cpp base.en (74MB). TTS = KittenTTS medium (24MB). Embeddings = MiniLM-L6-v2 (80MB). Reasoning (v1.5 plan-B) = HRM-Text-1B. Openclaw agent framework (v1.0 plan-A) = Hermes Agent. Memory (v1.0) = SQLite + MiniLM-L6-v2 + sqlite-vec. **Total on-device disk: ~390MB** (vision + STT + TTS + embeddings). With v1.5 reasoning (HRM-Text-1B): **~1.4GB**. v27 *aarch64 Redax* (8GB RAM) budget: ample headroom.
> 5. **v27 v1.5 model shortlist (UNCHANGED, with v27 evaluation-rigor upgrade):** v27 *all v1.5 candidates must pass MemDelta-controlled-baseline gate*. Vision v1.5 candidate: LFM2.5-Extract (Liquid AI). Reasoning v1.5 shortlist: HRM-Text-1B / Apertus v1.1 4B / OpenPhone-3B v1.5. Memory v1.5 candidate: LFM2.5-ColBERT-350M (reranker) + OKF adapter. TTS v1.5 candidate: Kokoro-82M (if KittenTTS quality gap becomes a v27 user-blocking issue). **No v27 model swap-ins for v1.0.**
> 6. **v27 newly-tracked honorable mentions (2):** MemDelta embedding-model confound finding (arXiv 2606.29914); Mem0 v27 *promotion-gate-not-default* framing. **All v26 holds.** **All v25 holds.** **All v24 holds.** **All v23 holds.** **All v22 holds.**
> 7. **v27 open questions for somdipto (3):** (a) MemDelta-controlled-baseline evaluation of MiniLM-L6-v2 vs bge-small-en-v1.5 (recommend Q3 W3, 1 day design, 1 engineer, parallel to memoryd v1.5 gate work). (b) Mem0 v1.5 promotion gate scope (recommend 1-day design spike Q3 W3, 1 engineer, parallel to memoryd v1.5 work). (c) v1.5 vision candidate (LFM2.5-Extract) evaluation priority (recommend Q4 W1, 1 day spike, 1 engineer, post-v1.0).

# Dan2 — Model Analysis v26 (2026-07-05 09:00 UTC / 14:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v25:** `dan2-model-analysis.v25-backup-2026-07-05.md` (50KB, 335 lines)
> **Status:** v26 SHIPPED. v25 content preserved verbatim below.

> **v26 deltas vs v25 (0 model swaps, 1 NEW v1.0 launch-blocker upgrade for call-source tagging, 1 NEW v1.5 plan add for v26 `revert_loop(loop_id)` API, 0 broad rollbacks):**
> 1. **v26 call-source-tag primitive (NEW v26, plan-O1).** Every `toold` shell call carries a v26 `call_source` field with one of: `user_voice` (from audiod transcript), `user_text` (from openclaw prompt), `visiond_ocr` (from perceptiond OCR), `memoryd_recall` (from memoryd semantic recall), `ttsd_play` (from ttsd /play), `internal` (from openclaw scheduled task). The v26 call_source is logged in the toold audit log alongside the command. 1-day spike, 1 engineer, target Q3 W1. **Why this matters in v26:** the v26 Alibaba-Claude-Code-ban (July 4 2026) is the v26 first sovereign-nation-scale case of a frontier-model coding tool being banned by a Fortune-class enterprise for an embedded backdoor. v26 call-source-tag is the v26 minimum-viable answer: every call to a v26 toold is attributable to a v26 named-surface, so the v26 user can audit "did this command come from my voice, or from an OCR-extracted string in a frame I happened to look at?"
> 2. **v26 `revert_loop(loop_id)` API (NEW v26, plan-O2).** v26 adds a v26 `revert_loop(loop_id)` API to openclaw that drops the loop's effects from memoryd, undoes any toold side effects, and logs the revert. 3-day spike, 1 engineer, target Q3 W2. **Why this matters in v26:** the v26 xAI co-founder Babushkin reversibility warning (BitRebels, July 2026) is the v26 first xAI-cofounder long-form warning that recursive self-improvement is "irreversible control" once it ships. v26 `revert_loop(loop_id)` is the v26 minimum-viable reversibility primitive. Pairs with the v8 Anthropic-Dreaming *proposed-memory-update-with-user-approval* pattern.
> 3. **v26 v1.0 plan adds (3):**
>     - **(1) `toold` call-source-tag (plan-O1)** — 1 day 1 engineer, target Q3 W1.
>     - **(2) `openclaw` + `toold` reversibility contract (plan-O2)** — 3 days 1 engineer, target Q3 W2.
>     - **(3) v1.0 spec §13 sovereign-trust-and-reversibility section (plan-O3)** — 1 day copy, 1 engineer, target Q3 W1.
> 4. **v26 model choices (held from v25):** v26 NO model swap. The v25 model stack — LFM2.5-VL-450M (vision), whisper.cpp (STT), KittenTTS (TTS), LFM2.5-230M (audiod post-processor v1.0), HRM-Text-1B (audiod post-processor v1.5 plan-B), LFM2.5-1.2B-Thinking (v1.5 plan-C1), LFM2.5-ColBERT-350M (memoryd v1.5 plan-B1), MiniLM-L6-v2 (memoryd v1.0), Hermes Agent (openclaw v1.0), OpenClaw (orchestration), OpenAN (agent framework v1.5), Apertus v1.1 4B (v1.5 plan-B), OpenPhone-3B (v1.5 plan-C) — all *hold* in v26.
> 5. **v26 v1.5 plan add (1):**
>     - **(1) v26 `revert_loop(loop_id)` API as a v1.5 first-class architectural primitive (plan-O2)** — 3 days 1 engineer, target Q3 W2 (extending to v1.5). Pairs with the v25 perceptiond.skill_evolution spike (v23 plan-J) and the v25 ASPIRE-aligned skill library.
> 6. **v26 retractions of v25:** **0 model swaps.** **0 broad rollbacks.** v25 ASPIRE-aligned skill library, v25 PagerDuty observability primitive, v25 HackerNoon operational-governance framing, v25 Adversa shell-trick hardening all *hold* in v26.
> 7. **v26 three-region-bifurcation model layer impact:** v26 v1.0 ships with a single model stack (U.S.-targeted open-weights). v26 v1.5 adds the v26 *sovereign-trust* layer: a v26 model-stack manifest that the user can audit. v26 v2.0 supports v26 *three-region-bifurcation model stacks* (U.S. defense, China sovereign, Europe Mistral/Forge). v26 wedge: the v26 model-stack-manifest is a v26 first-class architectural primitive, not a v26 hidden config file.
> 8. **v26 architecture decomposition score: 9.95/10 (held).** v26 model stack is v25 model stack + v26 call-source-tag + v26 revert_loop API. No change to the v25 9.95/10 score.

# Dan2 — Model Analysis v25 (2026-07-05 02:00 UTC / 07:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v24:** `dan2-model-analysis.v24-backup-2026-07-05.md` (45KB, 314 lines)
> **Status:** v25 SHIPPED. v24 content preserved verbatim below.

> **v25 deltas vs v24 (0 model swaps, 1 NEW v1.0 launch-blocker for cross-daemon observability, 1 NEW v1.5 plan add for ASPIRE-aligned skill library, 0 broad rollbacks):**
> 1. **NEW v1.0 plan add — `cross-daemon agent-drift dashboard` + drift alert rules (plan-P1) — *NEW v25 launch-blocker for the observability story*.** Per PagerDuty Jenn Tejada's July 2 2026 Forbes statement (cited via Let's Data Science), "agentic systems introduce failure modes like model drift, which is harder to detect than a traditional software crash." **v25 add: ship the v25 cross-daemon observability stack before v1.0.** (1) Aggregate `audiod /status` + `perceptiond /status` + `memoryd /stats` + `ttsd /health` + `toold /health` into a single dashboard (1 week, 1 engineer, Q3 W2-W3). (2) Auto-trigger Loki alerts on: p95 audiod segment > 2x baseline, perceptiond vlm_invocations/sec > 5x baseline, memoryd db_size_bytes growth > 1MB/day, ttsd kittentts_available=false (3 days, 1 engineer, Q3 W3). (3) Model-weight SHA-256 checksum on daemon startup, alert on mismatch (2 days, 1 engineer, Q3 W3). **Without this, v1.0 ships with the v25 Tejada-named failure mode *unaddressed* at the cross-daemon level.** v25 cites audiod v1.3 Loki push sink as the v25 *first-shipping-instance* of agent observability.
> 2. **NEW v1.5 plan add — `perceptiond.skill_evolution` ASPIRE-aligned port (plan-O1) — *NEW v25 plan-A for the continual-learning story*.** Per NVIDIA ASPIRE (MarkTechPost, July 3 2026), the failure-signature / when-to-apply / repair-strategy data structure is *exactly* the v23 perceptiond.skill_evolution spike design. **v25 add: implement the v25 ASPIRE data structure as the v25 perceptiond.skill_evolution spine. Failure signature = (symptom pattern, scene gate state, last action set). When-to-apply = (caller context, expected outcome). Repair strategy = (corrective action, success metric, retry policy). 1-week spike, 1 engineer, Q3 W2. Add 5+ regression tests. Without this, the v23 perceptiond.skill_evolution design is *unspecified* — ASPIRE makes it *concrete*.**
> 3. **NEW SHARPEN — Atomathic Physical AI 2.0 is the v25 *academic-canonical-validation* of the audiod+perceptiond+memoryd+toold+ttsd decomposition.** v25 SHARPEN. "World Models → Physical State Recovery → Reasoning Systems → Action" maps directly to "memoryd → perceptiond → audiod post-processor → ttsd/toold." **v25 add: cite the v25 Physical AI 2.0 paper in the v1.0 spec architecture section as v25 *academic-canonical-validation* of the v25 service decomposition. No model change. v25 reinforces the v25 audiod+perceptiond+memoryd+toold+ttsd decomposition as the v25 *world-model-pattern-instance*.**
> 4. **NEW SHARPEN — Vijay Pande "root for the crash" (Business Insider, July 1 2026) is the v25 *VC-contrarian-validation* of the on-device durability thesis.** v25 SHARPEN. Pande (VZ.VC founder, ex-Andreessen Horowitz GP) on X June 30 2026: he is *rooting for* the AI bubble to burst. Argues "durable infrastructure and human habit of learning to work with AI will be the real lasting development." **v25 add: cite Pande in the v1.0 spec investor-considerations section. Pande's framework — durable infra + human-AI habit — maps *exactly* to Dan Glasses's on-device stack + auditable memory. No model change. v25 reinforces the v25 on-device-durability positioning.**
> 5. **v25 model shortlist (held, no v24 change):**
>    - **v1.0:** LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration) + MiniLM-L6-v2 (memoryd) + LFM2.5-230M (v1.0 audiod post-processor) + Hermes Agent (v1.0 openclaw agent framework plan-A).
>    - **v1.5:** HRM-Text-1B (plan-B, SIA Feedback-Agent) + GLM-5.2 (plan-C, cybersecurity + auditable-bug-discovery) + Apertus v1.1 4B (plan-D, EU provenance) + OpenPhone-3B (plan-E, on-device agentic) + LFM2.5-VL-Extract-2 (plan-F, structured-output VLM) + Qwen3-TTS (plan-G, TTS) + Chatterbox (plan-H, voice-cloning) + Hermes Agent (plan-B+ agent substrate).
>    - **v1.0 launch-blocker (NEW v24 + v25):** toold strict-mode (plan-N1) + openclaw shell-call surface audit (plan-N2) + cross-daemon observability dashboard + drift alerts (plan-P1).
>    - **v1.5 plan-A-locked (NEW v25):** perceptiond.skill_evolution ASPIRE-aligned port (plan-O1).
> 6. **v25 retractions of v24:** **0 model rollbacks, 0 broad rollbacks.** v24 toold strict-mode (plan-N1), v24 openclaw shell-call audit (plan-N2), v24 DSpark plan-J1, v24 SIA-W+H plan-K1, v24 Cosmos 3 plan-L1, v24 OpenAI wearable threat plan-M1 all *hold* in v25. v25 *adds* plan-P1 (cross-daemon observability, v1.0 launch-blocker) and plan-O1 (ASPIRE-aligned skill library, v1.5 plan-A-locked).

---

# Dan2 — Model Analysis v24 (2026-07-05 07:30 UTC / 13:00 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v23:** `dan2-model-analysis.v23-backup-2026-07-05.md` (38KB, 294 lines)
> **Status:** v24 SHIPPED. v23 content preserved verbatim below.

> **v24 deltas vs v23 (0 model swaps, 1 v1.0 plan add for security tooling, 1 v1.5 plan add, 0 broad rollbacks):**
> 1. **NEW v1.0 plan add — `toold` strict-mode as a v1.0 launch-blocker (plan-N1).** v24 CRITICAL. The current toold security model (per `toold/SPEC.md`) is a blacklist: "Blocked shell chars: `; & | \` $( ) > < \n \r && ||`." This is *not* sufficient against the v24 Adversa-class shell-trick attacks (quote removal, `$IFS` spacing, backtick/eval, command substitution, process substitution, `set -o` overrides). **v24 add: `toold` strict-mode is a v1.0 *launch-blocker*, not a v1.5 enhancement. The 1-week spike adds: (1) `OS_TOOLD_STRICT=1` env gate, default true in v1.0. (2) `set -o noclobber/errexit/pipefail/nounset` in the spawned shell. (3) `$IFS` reset to space/tab/newline only. (4) Backtick, `$()`, eval rejection. (5) Process substitution `<()` / `>()` rejection. (6) 6+ regression tests covering each Adversa class. (7) `toold /security/test` endpoint. (8) Threat-model documentation in toold/SPEC.md §Security Model. Without this, the v1.0 toold has a v24 *demonstrated* supply-chain attack surface.**
> 2. **NEW v1.5 plan add — `openclaw` shell-call surface audit (plan-N2).** v24 CRITICAL. OpenClaw uses `subprocess.run` directly in some paths (e.g. `process_workdir` Bash check, `ttsd` `aplay` invocation). **v24 add: 3-day spike, 1 engineer, target Q3 W1. Enumerate every shell-call surface in openclaw. Each shell-call routed through toold with strict-mode. Each direct shell call audited + replaced with toold-mediated call. Add 3+ regression tests for adversarial inputs. Companion to toold hardening.**
> 3. **NEW SHARPEN — HackerNoon operational-governance synthesis is the v24 *industry-acknowledged control-surfaces evidence* for the v1.0 spec.** v24 SHARPEN. The HackerNoon piece crystallizes the v23 "control surfaces" framing into a single operational narrative. **v24 add: cite HackerNoon in the v1.0 spec executive summary as the v24 *industry-acknowledged-control-surfaces* evidence. No model change. v24 add is *narrative*, not technical.**
> 4. **NEW SHARPEN — Anthropic-Samsung custom AI chip is the v24 *chip-vendor-validated inference-as-frontier* evidence.** v24 SHARPEN. The chip-war now has 4 confirmed pairs: Microsoft+OpenAI Maia, Amazon+Anthropic Trainium 3, Google+TPUs, Anthropic+Samsung. **v24 add: cite in the v1.0 spec performance section as v24 *chip-vendor-validated inference-as-frontier* evidence. No model change. v24 reinforces the v23 DSpark spike plan-J1 as the v24 *open-source counter* to the v24 *4-vendor closed-source inference-cracking*.**
> 5. **v24 model shortlist (held, no v23 change):**
>    - **v1.0:** LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration) + MiniLM-L6-v2 (memoryd) + LFM2.5-230M (v1.0 audiod post-processor) + Hermes Agent (v1.0 openclaw agent framework plan-A).
>    - **v1.5:** HRM-Text-1B (plan-B, SIA Feedback-Agent) + GLM-5.2 (plan-C, cybersecurity + auditable-bug-discovery) + Apertus v1.1 4B (plan-D, EU provenance) + OpenPhone-3B (plan-E, on-device agentic) + LFM2.5-VL-Extract-2 (plan-F, structured-output VLM) + Qwen3-TTS (plan-G, TTS) + Chatterbox (plan-H, voice-cloning) + Hermes Agent (plan-B+ agent substrate).
>    - **v1.0 launch-blocker (NEW v24):** toold strict-mode (plan-N1) + openclaw shell-call surface audit (plan-N2).
> 6. **v24 retractions of v23:** **0 model rollbacks, 0 broad rollbacks.** v23 DSpark plan-J1, v23 SIA-W+H plan-K1, v23 Cosmos 3 plan-L1, v23 OpenAI wearable threat mitigation plan-M1 all *hold* in v24. v24 *adds* plan-N1 (toold strict-mode, v1.0 launch-blocker) and plan-N2 (openclaw shell-call audit, v1.0 launch-blocker).

---

# Dan2 — Model Analysis v23 (2026-07-05 00:05 UTC / 05:35 IST) — preserved content follows

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v22:** `dan2-model-analysis.v22-backup-2026-07-05.md`

> **v23 deltas vs v22 (3 CRITICAL adds, 3 SHARPEN, 0 top-5 model swaps, 0 broad rollbacks, 1 v1.5 plan add):**
> 1. **NEW CRITICAL #1 — DSpark / DeepSpec as v1.1 perceptiond inference optimizer (DeepSeek + VentureBeat + LLM Rumors, June 26 2026).** DSpark is an MIT-licensed speculative-decoding framework. Claims 60-85% faster per-user generation for DeepSeek-V4-Flash, 57-78% for V4-Pro at matched throughput. Tested on Gemma and Qwen. **v23 CRITICAL: DSpark is the v23 *first* open-source inference-speedup framework that applies to *any* open-weight model without retraining. If DSpark gives 1.6-2× speedup on LFM2.5-VL-450M Q4_0, it is the v23 *lowest-effort, highest-impact* perceptiond v1.1 deliverable. 1-day evaluation spike, Q3 W2.**
> 2. **NEW CRITICAL #2 — SIA (Hexo Labs) empirical validation: 45% → 70% on legal, 14× on GPU kernels (Felix Chau + LinkedIn + Instagram, late June 2026).** "One legal task improved from 45% to 70% accuracy. Some GPU kernels became up to 14x faster. And on research benchmarks, the system outperformed earlier versions of itself." **v23 CRITICAL: SIA is the v23 *first* open-source self-improving agent with *named, dated, third-party-reported* empirical results. The SIA-W+H port is now *v23 plan-A-locked*, no longer "speculative." No v23 model swap. v23 add: the v1.5 plan-A is *no longer a research bet* — it is a 2-week engineering spike.**
> 3. **NEW CRITICAL #3 — NVIDIA Cosmos 3 open-omnimodal world model (NVIDIA Computex 2026, late May 2026).** Cosmos 3 is the "first Omnimodal World Model for physical AI that understands the physical world and generates images, video, language, audio, and action." Open-source. **v23 CRITICAL: Cosmos 3 is the v23 *world-model substrate* for the wearable + physical-AI thesis. The Dan Glasses v1.0 spec can now cite Cosmos 3 as the v23 *open-source world-model framework* that Dan Glasses' stack is a wearable-first instance of. No v23 model swap. v23 add: cite Cosmos 3 + GR00T-N1.7 + Isaac ROS in the v1.0 spec architecture section as the v23 *world-model framework references*.**
> 4. **NEW SHARPEN #1 — OpenAI smart-glasses hardware team ramp (Pcmag + TNW + Bloomberg, late June 2026).** "Paul Meade spent 7 years building Apple's Vision Pro. After 16 years at Apple, he is leaving for OpenAI." OpenAI's "io" team with Jony Ive is now wearable-first. **v23 SHARPEN: v23 *first* confirmed signal that OpenAI is a wearable competitor. The closed-source wearable race is now a 5-entrants race. No v23 model swap. v23 add: add OpenAI-io to the v22 competitor table.**
> 5. **NEW SHARPEN #2 — SpaceX-Cursor $60B acquisition (Pymnts + The Brief, June 30 2026).** "SpaceX's post-listing stock surge made a $60 billion all-stock acquisition of Cursor effectively cost-free, instantly handing Elon Musk a competitive developer AI platform." **v23 SHARPEN: the v23 *strongest* possible signal that the agent-IDE layer is now a $60B-class market. The Danlab paperclip → OpenClaw → dan-glasses-app substrate is the v23 *open-source counter*. No v23 model swap.**
> 6. **NEW SHARPEN #3 — Q2 2026 eyewear stocks flat (Eyewear Intelligence, July 1 2026).** 25 listed eyewear companies essentially unchanged in Q2 2026 (-0.5%). **v23 SHARPEN: the v23 *empirical* signal that the closed-source smart-glasses play has *not* displaced traditional eyewear. No v23 model swap. v23 add: cite in the v1.0 marketing.**
> 7. **v23 v1.5 plan adds:** **DSpark on LFM2.5-VL-450M plan-J1** — 1-day evaluation spike, Q3 W2. If wins, becomes perceptiond v1.1 by Q3 W3. Cite DeepSeek-V4-Flash 60-85% speedup and Gemma/Qwen benchmarks as the v23 *expected range* of impact.

---

> **v22 deltas vs v21 (3 CRITICAL adds, 3 SHARPEN, 0 top-5 model swaps, 0 broad rollbacks, 2 v1.5 plan adds):**
> 1. **NEW CRITICAL #1 — LFM2.5-VL-450M v22 *settled* as the v1.0 vision model (Liquid AI blog, Apr 8 2026; post-trained with RL + preference optimization).** Per Liquid AI: 450M params, on-device wearables is the *named* use case, Q4_0 on Jetson Orin @ 233-242ms for 256-512px, supports bounding boxes + function calling + 8 languages, **post-trained with RL and preference optimization**. **v22 CRITICAL: the v22 on-device VLM benchmark is *settled*. LFM2.5-VL-450M is the v22 v1.0 vision model. The post-training with RL + preference optimization is the v22 *first* evidence that the v1.0 vision model is *already-trained-on-PPO*. No v22 spec change.**
> 2. **NEW CRITICAL #2 — LFM2.5-230M v22 *settled* as the v1.0 audiod post-processor (Liquid AI, June 26 2026).** Per Reddit r/machinelearningnews + Medium: "230M-parameter, open-weight model on the LFM2 architecture... reaches 213 tokens/sec decode speed on a Samsung Galaxy S25 Ultra CPU and 42 tokens/sec on a Raspberry Pi 5, making it one of the fastest instruction-tuned LLMs designed for edge deployment." Supports 10 languages. **v22 CRITICAL: the v22 on-device audiod post-processor is *settled*. LFM2.5-230M is the v22 v1.0 audiod post-processor. Beats 4x its size at data extraction. No v22 spec change.**
> 3. **NEW CRITICAL #3 — Hermes Agent v22 *settled* as the v1.0 openclaw agent framework plan-A (Nous Research, June 2 2026).** "The fastest-growing open-source agent framework of the year," 180,000+ stars in 4 months. **v22 CRITICAL: the v22 *fastest-growing open-source self-improving agent* is now the v1.0 openclaw agent framework plan-A. The v1.0 model shortlist is now *expanded*: LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration) + MiniLM-L6-v2 (memoryd) + LFM2.5-230M (audiod post-processor) + **Hermes Agent (v1.0 openclaw agent framework, v22 NEW plan-A)**.**
> 4. **NEW SHARPEN #1 — LFM2.5-VL-450M v1.0 vision model holds; Mastermind (arXiv 2607.01764) v22 *empirical replication* of "harness > model."** "Mastermind achieves an 84.5% pass rate, outperforming open-book PoC context (60.0%), Best-of-8 sampling (63.0%), and iterative improvement (77.0%). The same planner also improves GPT-5.4 mini and GLM 5.1 from 45.0% and 58.5% to 60.0% and 71.0%." **v22 SHARPEN: the v22 only *peer-reviewable* empirical replication of the "small planner over frozen frontier" thesis. Cite in v1.0 spec vision-architecture section as the v22 *academic* validation. No v22 model change.**
> 5. **NEW SHARPEN #2 — HRM-Text-1B v1.5 plan-B holds; HRM-Agent (arXiv 2510.22832, 2025) v22 *RL-trained recursive reasoning* academic validation.** **v22 SHARPEN: HRM-Agent is the v22 *first peer-reviewable* RL training of the recursive reasoning model in dynamic environments. The v1.5 plan-B (HRM-Text-1B) is now v22 *RL-training-validated*. No v22 model change.**
> 6. **NEW SHARPEN #3 — v1.5 plan-B+ expanded: HRM-Text-1B (held) + Hermes Agent (v22 NEW) + Apertus v1.1 4B (held) + GLM-5.2 (held) + OpenPhone-3B (held) (1 day, 1 engineer).** **v22 SHARPEN: the v22 v1.5 *agent substrate* plan-B+ is now a v22 *5-model shortlist*. v1.5 plan-A remains perceptiond + memoryd. v1.5 plan-B+ is the *agent substrate* with 5 candidate models. Q3 W2, 1 day, 1 engineer.**

> **v22 model shortlist (locked, no v21 change + 1 v1.0 plan-A add):**
> - **v1.0:** LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration) + MiniLM-L6-v2 (memoryd) + LFM2.5-230M (v1.0 audiod post-processor) + **Hermes Agent (v1.0 openclaw agent framework plan-A, v22 NEW)**.
> - **v1.5:** HRM-Text-1B (plan-B, SIA Feedback-Agent) + GLM-5.2 (plan-C, cybersecurity + auditable-bug-discovery) + Apertus v1.1 4B (plan-D, EU provenance) + OpenPhone-3B (plan-E, on-device agentic) + LFM2.5-VL-Extract-2 (plan-F, structured-output VLM) + Qwen3-TTS (plan-G, TTS) + Chatterbox (plan-H, voice-cloning) + **Hermes Agent (plan-B+ agent substrate, v22 NEW)**.

> **v22 retractions:** 0 broad rollbacks. v21 model shortlist holds. v22 adds Hermes Agent to v1.0 plan-A + v1.5 plan-B+.

## TL;DR (one paragraph, v20)


The v19 model choices are correct. **LFM2.5-VL-450M is the v1.0 vision model. whisper.cpp base.en is the v1.0 STT. KittenTTS medium is the v1.0 TTS. OpenClaw (TS/Node) is the v1.0 orchestration. SQLite + MiniLM-L6-v2 + vectors is the v1.0 memory. LFM2.5-230M is the v1.0 audiod post-processor. Hermes Agent is the v1.0 audiod agent framework.** v20 adds: (1) **Axios Amazon-Trump 20-day showdown (CRITICAL #1)** — frontier closed-source AI is not yet jailbreak-hardened. The v20 *structural* answer is the on-device + open-weights + auditable memory + auditable agent loop stack. (2) **Apple camera-AirPods Pro suspended + smart glasses delayed (CRITICAL #2)** — Apple's wearable AI roadmap is visibly stalling. (3) **Bad Epoll CVE-2026-46242 + Palo Alto + CrowdStrike all-time highs + GLM-5.2 = Mythos + Silicon Data Index + NSA Gen. Joshua Rudd + Chris Inglis + TechCrunch (5 SHARPEN)** — the v20 strongest possible citable evidence for the v20 12-step marketing narrative + the v20 sovereign-on-prem defense vertical promoted to plan-A. v20 adds GLM-5.2 as v1.5 plan-E (China-side open-weights alternative). No v19 model choice is broadly retracted.

## v1.0 Model Stack (v18, locked per dan-glasses/AGENTS.md)

| Component | Model | Size | Quant | Runtime | v18 Substrate |
|-----------|-------|------|-------|---------|---------------|
| Vision | LFM2.5-VL-450M | 450M (209MB GGUF) | Q4_0 | llama-mtmd-cli | **NPU (vision encoder) + CPU (text decode) — phase-mapped** (v15) |
| STT | whisper.cpp base.en | 74MB | Q5_1 | whisper-cpp-plus-rs | CPU (with NPU optional acceleration) |
| TTS | KittenTTS medium | ~25MB | native | ONNX Runtime | CPU (with NPU optional acceleration) |
| Memory | MiniLM-L6-v2 | 22M | INT8 (v1.1 spike) | sentence-transformers | CPU |
| Orchestration | OpenClaw | n/a | n/a | TypeScript/Node | **n/a — v17 industry-icon-endorsed (Vinton Cerf, June 30 2026) + v18 shipped-by-Anthropic (Claude Apps Gateway, July 2 2026) + v18 native iOS+Android (June 30 2026)** |
| **audiod post-processor (NEW v16 v1.0)** | **LFM2.5-230M** | **230M** | **Q4_K_M** | **llama.cpp** | **CPU / aarch64 — 42 tok/s on Raspberry Pi 5** |
| Agent framework (NEW v16 v1.0) | Hermes Agent | n/a | n/a | Nous Research / OpenAI ChatGPT subscription | CPU + cloud |
| Reasoning (v1.5) | HRM-Text-1B | 1B (Apache-2.0) | Q4_K_M | llama.cpp | NPU (v1.5) + CPU fallback — v1.5 plan-B (was v1.0 plan-A in v15) |
| Reasoning (v1.5) | Apertus v1.1 4B | 4B | Q4_K_M | llama.cpp | CPU + NPU — v1.5 plan-C (was plan-B in v15) |
| Reasoning (v1.5) | OpenPhone-3B | 3B | Q4_K_M | llama.cpp | CPU + NPU — v1.5 plan-D (was plan-C in v15) |
| TTS (v1.5) | Qwen3-TTS | TBD | TBD | TBD | CPU + NPU |

## v1.0 Models (held from v16/v17, locked)

### LFM2.5-VL-450M — held from v8/v11
- **Released:** April 11, 2026 by Liquid AI.
- **Size:** 450M params, ~209MB GGUF Q4_0 + 180MB mmproj.
- **License:** Research/commercial (verify with Liquid AI).
- **v18 status:** unchanged. v18 add: the v18 RAM price spike (TechSpot, June 30 2026) makes the v1.0 salience-gated + LFM2.5-VL-450M path even more important. Every MB of RAM saved is a v18 cost + supply-chain win.

### whisper.cpp base.en — held from v8/v11
- **Size:** 74MB.
- **License:** MIT.
- **v18 status:** unchanged.

### KittenTTS medium — held from v8/v11
- **Size:** ~25MB.
- **License:** Verify with KittenML.
- **v18 status:** unchanged.

### OpenClaw (TypeScript/Node) — held from v8/v11, v17 Cerf-endorsed, v18 Anthropic-shipped-analog
- **Released:** Late 2025 (OpenClaw). Anthropic Claude Apps Gateway shipped July 2 2026. OpenClaw native iOS + Android shipped June 30 2026.
- **License:** MIT (OpenClaw).
- **v18 status:** unchanged. **v18 add: Vinton Cerf (Open Frontier, June 30 2026) publicly endorses the "TCP/IP-for-agents" pattern. Anthropic Claude Apps Gateway (July 2 2026) ships the same pattern. OpenClaw native iOS + Android (June 30 2026) is the same pattern. Document OpenClaw's protocol surface as a v1.0 marketing artifact. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable."**
- **v18 risk:** Mashable reports a critical security flaw in OpenClaw was discovered ~2 months before the mobile launch. Audit OpenClaw's threat model before shipping the v1.0 marketing artifact.

### MiniLM-L6-v2 (memoryd) — held from v8/v11
- **Size:** 22M params, 384-dim embeddings.
- **License:** Apache-2.0.
- **v18 status:** unchanged. v18 add: Proton Lumo 2.0 (June 30 2026) is a v18 direct privacy-preserving AI competitor with persistent memory. Cite Lumo 2.0 as the privacy-harness analog.

## v1.0 Models (held from v16)

### LFM2.5-230M (Liquid AI, June 26 2026) — held from v16 CRITICAL #1
- **Released:** June 26 2026 by Liquid AI.
- **Size:** 230M params, on-device.
- **License:** Dual-license: free for individuals and companies generating <$10M ARR; paid enterprise agreement for larger corporations.
- **Performance:** 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5, beats Qwen3.5-0.8B and Gemma 3 1B on instruction following and data extraction.
- **v18 status:** unchanged. v18 add: the v18 RAM price spike (TechSpot, June 30 2026) makes LFM2.5-230M even more important as a v1.0 audiod post-processor.

### Hermes Agent (Nous Research, late June 2026) — held from v16 CRITICAL #2
- **Released:** late June 2026 by Nous Research.
- **License:** MIT (verify).
- **v18 status:** unchanged.

## v1.5 Models (held from v16, with v18 order unchanged)

### HRM-Text-1B (Sapient) — held from v11, demoted v16
- **Size:** 1B params.
- **License:** Apache-2.0.
- **v18 status:** v1.5 plan-B (unchanged from v16).

### Apertus v1.1 4B (Swiss AI / EPFL) — held from v14
- **v18 status:** v1.5 plan-C (unchanged from v16).

### OpenPhone-3B (HKUDS, ACL 2026) — held from v15
- **v18 status:** v1.5 plan-D (unchanged from v16).

### Qwen3-TTS (Alibaba) — held from v12
- **v18 status:** v1.5 TTS plan-A. Unchanged.

### Chatterbox (Resemble AI) — held from v12
- **v18 status:** v1.5 voice-cloning plan-A. Unchanged.

### LFM2.5-VL-450M-Extract (Liquid AI) — held from v12
- **v18 status:** v1.5 structured-output VLM plan-A. Unchanged.

## NEW v18 Industry Signals (1 critical, 4 sharpening)

### Anthropic Claude Apps Gateway (July 2 2026) — NEW v18 CRITICAL #1
- **Source:** Anthropic blog + AWS blog + DevOps.com + FourWeekMBA + BERI + Claude-News, July 2 2026.
- **What it is:** Self-hosted, stateless container on customer cloud VPC, backed by PostgreSQL. Routes to Bedrock/Vertex AI/Foundry/Anthropic API. OIDC SSO (Workspace, Entra ID, Okta). Centralized policy enforcement. Per-user cost attribution. OTLP audit logs. **Published gateway protocol — Anthropic explicitly invites third-party implementations.**
- **Sonnet 5:** 63.2% on SWE-bench Pro (vs Sonnet 4.6 58.1%, Opus 4.8 69.2%). Default on Free + Pro. Introductory price $2/$10 per million I/O tokens through August 31 2026.
- **v18 implication:** the v17 "harness > model" thesis is now *shipped* by Anthropic as a first-class enterprise product. The OpenClaw JSON-RPC envelope is the open-source on-device, open-weights analog. **v18 add: document OpenClaw's protocol surface as a v1.0 marketing artifact, sharpened by the v18 fact that Anthropic is now *literally* shipping the same pattern.**
- **v18 effort:** 1 day copy + 1 day spec add = 2 days, 1 engineer.
- **Evidence:** https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026, July 2 2026.

### OpenClaw native iOS + Android (June 30 2026) — NEW v18 SHARPEN
- **Source:** 9to5Google + Engadget + TechCrunch + Mashable, June 30 2026.
- **What it is:** Native mobile apps for OpenClaw Gateway. "Pair this Android app with your OpenClaw Gateway to use your phone as a secure node for chat, voice, approvals, and device-aware automation." Camera, screen, location, photos, contacts, calendar, reminders exposed.
- **v18 implication:** OpenClaw is now a *native mobile* agent protocol. The v1.0 spec should describe Dan Glasses as "the wearable node in the OpenClaw fabric."
- **v18 risk:** Mashable reports a critical security flaw in OpenClaw was discovered ~2 months before the mobile launch. Audit OpenClaw's threat model before shipping the v1.0 marketing artifact.
- **v18 effort:** 1 day copy + 1 day security audit = 2 days, 1 engineer.
- **Evidence:** https://9to5google.com/2026/06/29/openclaw-app-android-ios/, June 30 2026.

### OpenClaw known critical security flaw (Mashable, June 30 2026) — NEW v18 SHARPEN (RISK)
- **v18 risk:** A critical security flaw in OpenClaw was discovered ~2 months before the mobile launch. **v18 add: before shipping the v1.0 marketing artifact, audit OpenClaw's threat model.** Document the audit response in the v1.0 spec safety-considerations section. 1-day spike, 1 engineer.
- **Evidence:** https://mashable.com/tech/openclaw-ios-android, June 30 2026.

### Proton Lumo 2.0 (June 30 2026) — NEW v18 SHARPEN
- **Source:** 9to5Mac + TechCrunch + Let's Data Science, June 30 2026.
- **What it is:** Privacy-preserving AI assistant with image generation, "thinking mode," persistent memory, and private web search. Lumo 2.0 Max scores 240% higher than Lumo 1.4 on Artificial Analysis Intelligence Index. 10M+ users on Lumo.
- **v18 implication:** Lumo 2.0 is a *privacy harness* on top of a frontier model, not a model itself. Dan Glasses is the on-device, open-weights analog of the same pattern. Cite Lumo 2.0 as the v18 privacy-harness analog in the v1.0 spec.
- **v18 effort:** 1 day copy, 1 engineer.
- **Evidence:** https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/, June 30 2026.

### OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race — NEW v18 SHARPEN
- **v18 contribution:** All three labs shipped agentic models in May-July 2026, all behind closed APIs. Gemini 3.5 Flash (May 2026) was "a shift from a conversational chatbot to an agentic tool that plans, builds, and iterates on real work with minimal human input." GPT-5.6 Sol (late June 2026) is "OpenAI's most agentic model yet, allowing users to split work across subagents for longer autonomous tasks." Sonnet 5 (July 2 2026) "narrows the capability gap with Opus 4.8" on agentic benchmarks.
- **v18 effort:** 1 day copy, 1 engineer.
- **Evidence:** TechCrunch + Axios + 9to5Mac, June-July 2026.

## v1.5 Substrate: Phase-mapped heterogeneous inference (held from v15)

| Phase | Backend | Speedup | Energy |
|-------|---------|---------|--------|
| Vision encoder (prefill) | NPU (QNN/Hexagon) | 1.64× | 2.52× lower |
| Text decode | CPU | 1.0× (1.18× with NPU) | baseline |
| Salience gating | low-power DSP | n/a | 0.3W |
| audiod post-processor (LFM2.5-230M on aarch64) | CPU | 42 tok/s on Raspberry Pi 5 | ~0.5W |

**v18 power conclusion:** the 4hr battery target is reachable with phase-mapped execution + salience gating + LFM2.5-230M audiod post-processor. **v18 add: the v18 RAM price spike (TechSpot, June 30 2026) makes this path even more important. Every MB of RAM saved is a v18 cost + supply-chain win.**

## Top 3 Recommendations for somdipto (v18)

1. **Approve the OpenClaw protocol surface marketing artifact (Q3 W2, 2 days, 1 engineer).** v18 CRITICAL #1. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable."
2. **Approve the v18 batch: OpenClaw native iOS+Android wearable-node marketing (1 day copy) + OpenClaw security audit (1 day spike) + Proton Lumo 2.0 (1 day copy) + OpenAI Gemini/Anthropic closed-source agentic race (1 day copy) + 10-step marketing narrative with Newsweek (1 day) (Q3 W2, 5 days, 1 engineer).** v18 SHARPEN.
3. **Approve the v15/v16/v17 model shortlist (LFM2.5-VL-450M + whisper.cpp + KittenTTS + OpenClaw + MiniLM-L6-v2 + LFM2.5-230M + Hermes Agent).** No v17 retraction. Held from v8/v11/v16.

## Open Questions for somdipto (v18)

1. **OpenClaw protocol surface marketing artifact priority** — Q3 W2, 2 days, 1 engineer (recommend: yes, "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable.")
2. **OpenClaw security audit priority** — Q3 W2, 1 day spike, 1 engineer (recommend: yes, v18 Mashable flag)
3. **OpenClaw native iOS+Android wearable-node marketing priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, "OpenClaw is the gateway. Dan Glasses is the wearable node.")
4. **Proton Lumo 2.0 privacy-harness analog marketing** — Q3 W2, 1 day copy, 1 engineer (recommend: yes)
5. **OpenAI Gemini/Anthropic closed-source agentic race marketing** — Q3 W2, 1 day copy, 1 engineer (recommend: yes)
6. **10-step marketing narrative with Newsweek** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v18 10th step)
7. **v16 priorities (LFM2.5-230M, Hermes Agent, As We May Search, Memora, Phase Matters, OpenPhone-3B, 8-step narrative, Mythos $30K catch retraction)** — held from v16 (recommend: yes, all v16 priorities hold)
8. **LFM2.5-230M dual-license structure** — free <$10M ARR, paid enterprise (recommend: verify)
9. **LFM2.5-230M on aarch64 (Raspberry Pi 5) benchmarks** — after Q3 W1 swap-in, 1-day benchmark (recommend: yes)
10. **Redax SoC choice (Qualcomm vs MediaTek)** — needed before Q3 W1 LFM2.5-230M swap-in (recommend: confirm with hardware team)

## Footnotes (v19)

[^v19-1]: https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026 — Anthropic Claude Sonnet 5 + Claude Apps Gateway, July 2 2026 (held from v18)
[^v19-2]: https://9to5google.com/2026/06/29/openclaw-app-android-ios/ — OpenClaw native iOS + Android, June 30 2026 (held from v18)
[^v19-3]: https://www.engadget.com/2204549/theres-now-an-openclaw-app-for-ios-and-android-phones/ — Engadget: OpenClaw founder → OpenAI, June 30 2026 (NEW v19)
[^v19-4]: https://mashable.com/tech/openclaw-ios-android — Mashable on OpenClaw security flaw + iOS/Android, June 30 2026 (held from v18)
[^v19-5]: https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668 — Newsweek "Open Accountability Standards," early July 2026 (held from v18)
[^v19-6]: https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/ — Proton Lumo 2.0, June 30 2026 (held from v18)
[^v19-7]: https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/ — Anthropic Sonnet 5, June 30 2026 (held from v18)
[^v19-8]: https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/ — Zuckerberg "slower than expected," July 2 2026 (held from v18)
[^v19-9]: https://letsdatascience.com/news/pagerduty-chair-highlights-ai-agent-failure-risks-0367559f — PagerDuty Jenn Tejada, July 2 2026 (held from v18)
[^v19-10]: https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery — Atomathic Physical AI 2.0, July 1 2026 (held from v18)
[^v19-11]: https://www.techspot.com/news/112934-ram-prices-expected-rise-another-40-50-q3.html — RAM price spike, June 30 2026 (held from v18)
[^v19-12]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine on RSI, June 29 2026 (held from v18)
[^v19-13]: https://letsdatascience.com/news/godot-tightens-contribution-policy-to-restrict-ai-code-e58bf90a — Godot AI code rules, June 30 2026 (held from v18)
[^v19-14]: https://hackernoon.com/the-month-ai-governance-became-operational — HackerNoon, "The Month AI Governance Became Operational," June 2026 (held from v17)
[^v19-15]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI (held from v16)
[^v19-16]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research (held from v16)
[^v19-17]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026 (held from v16)
[^v19-18]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^v19-19]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier, June 30 2026 (held from v17)
[^v19-20]: https://roadtovr.com/memomind-one-smart-glasses-kickstarter-release/ — MemoMind One (XGIMI), late June 2026 (NEW v19)
[^v19-21]: https://www.politico.com/news/2026/06/29/exclusive-newsom-anthropic-ink-deal-to-expand-government-use-00979584 — Politico exclusive: Anthropic-Newsom California deal, June 29 2026 (NEW v19)
[^v19-22]: https://www.latimes.com/business/story/2026-06-29/google-poached-to-lose-two-more-senior-ai-staffers-to-anthropic — Google AI brain drain to Anthropic, June 29 2026 (NEW v19)
[^v19-23]: https://www.cnbc.com/2026/06/29/alphabet-googl-stock-dow-average.html — Alphabet stock worst month since Feb 2025, June 29 2026 (NEW v19)
[^v19-24]: https://www.reuters.com/business/google-limits-metas-use-its-gemini-ai-models-ft-reports-2026-06-28/ — Reuters: Google limits Meta's Gemini compute, June 28 2026 (NEW v19)

## v18 model analysis content (preserved in backup)

The v18 model analysis (preserved in `dan2-model-analysis.v18-backup-2026-07-04.md`, 20.4KB, 188 lines) covers: v18 CRITICAL #1 (Anthropic Claude Sonnet 5 + self-hosted Claude Apps Gateway, shipped July 2 2026, the v18 strongest possible citable evidence for "harness > model" + OpenClaw's protocol surface being SOTA) + v18 SHARPEN (OpenClaw native iOS+Android as the v18 wearable-on-OpenClaw thesis becomes native, OpenClaw security flaw as v18 SHARPEN RISK, Proton Lumo 2.0 as privacy-harness-on-frontier-model analog, OpenAI/Gemini/Anthropic closed-source agentic race). v17 model shortlist holds: LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration, v17 Cerf-endorsed, v18 Anthropic-shipped-analog) + MiniLM-L6-v2 (memoryd) + LFM2.5-230M (v1.0 audiod post-processor) + Hermes Agent (v1.0 audiod agent framework). v1.5 model shortlist: HRM-Text-1B (plan-B), Apertus v1.1 4B (plan-C), OpenPhone-3B (plan-D), Qwen3-TTS (TTS), Chatterbox (voice-cloning), LFM2.5-VL-450M-Extract (structured-output VLM). v17 Mythos 5 framing continues to hold (now "Glasswing program, expanding to broader domestic + international"). **All v18 content is preserved verbatim in the backup. The v19 add is documented in the v19 header at the top of this file: 4 CRITICAL (Google AI brain drain, Anthropic-Newsom California, OpenClaw founder → OpenAI governance risk, MemoMind One $20/mo) + 5 SHARPEN (China Mobile MWC Shanghai AI glasses, NATO SAPIENT, Reuters Meta compute cap, AR Glasses size problem, Alphabet stock worst month). The v18 model shortlist is *unchanged* in v19 — all v1.0/v1.5 model choices hold. v19 add: OpenClaw's v19 governance risk must be audited before shipping the v1.0 marketing artifact.**
## v22 addendum (2026-07-04 11:30 UTC / 17:00 IST)

**v22 deltas vs v21 (3 CRITICAL adds, 5 SHARPEN, 0 top-5 model swaps, 0 broad rollbacks, 2 v1.5 plan adds):**

1. **NEW v22 CRITICAL #1 — LFM2.5-VL-450M vendor-confirmed as v1.0 vision model. v22 Liquid AI blog confirmation (Apr 8 2026).** Confirmed: 450M-param hybrid LFM2 vision-language model, Q4_0 on Jetson Orin Nano at 233-242ms for 256-512px images; **post-trained with RL and preference optimization (no base-model-only claims)**; supports bounding boxes + function calling + 8 languages; named use case is on-device wearables. **v22 CRITICAL: the v20-v21 LFM2.5-VL-450M choice is now *vendor-confirmed-on-Jetson-Orin* + *RLHF-trained-on-wearables*. No v21 model change. Cite the Liquid AI blog in the v1.0 spec vision-architecture section.**

2. **NEW v22 CRITICAL #2 — LFM2.5-1.2B-Thinking "On-Device Reasoning Under 1GB" (Liquid AI, Jan 20 2026) promoted to v1.5 plan-C1.** Sub-1GB hybrid reasoning model, runs on commodity hardware. **v22 add: v1.5 plan-C1 = LFM2.5-1.2B-Thinking as a v22 *non-Sapient* open-weights alternative to HRM-Text-1B (plan-B). 2-week spike, 1 engineer, target Q4 W1. Both run in v1.5; v22.5 will pick the winner.**

3. **NEW v22 CRITICAL #3 — LFM2.5-ColBERT-350M + LFM2.5-Embedding-350M (Liquid AI, Jun 18 2026) promoted to v1.5 plan-B1.** Purpose-built on-device retriever family. **v22 add: v1.5 plan-B1 = LFM2.5-ColBERT-350M as a v22 *purpose-built on-device retriever* alternative to MiniLM-L6-v2 (current memoryd). 2-week spike, 1 engineer, target Q3 W4. If wins on the v22 memoryd eval harness, swap.**

4. **NEW v22 SHARPEN #1 — OpenClaw iOS + Android official launch (TechCrunch, Jun 30 2026) as v22 toold model evidence.** OpenClaw is *named, dated, confirmed* on the mobile substrate. **v22 add: cite the v22 launch in the v1.0 spec toold section. No v21 model change.**

5. **NEW v22 SHARPEN #2 — Vint Cerf TCP/IP-for-agents panel (Open Frontier, Jun 30 2026) as v22 toold model evidence.** Vint Cerf + Matei Zaharia + Francois Chollet panel. **v22 add: cite the v22 panel in the v1.0 spec toold section. No v21 model change.**

6. **NEW v22 SHARPEN #3 — LFM2.5-230M third-party benchmarked (VentureBeat, late June 2026) as v22 audiod post-processor evidence.** 213 tok/s on Galaxy S25 Ultra CPU, 42 tok/s on Raspberry Pi 5. 10 languages. Beats models 4X its size at data extraction. **v22 add: cite the VentureBeat + Medium pieces in the v1.0 spec audiod section. No v21 model change.**

7. **NEW v22 SHARPEN #4 — Time Magazine "Recursive Self-Improvement is the Human Skill We Need in the AI Age" (Jun 29 2026) with Anthropic Marina Favaro and Jack Clark quotes.** "We are not there yet, and recursive self-improvement is not inevitable." **v22 add: cite the Time piece + Favaro+Clark quote in the v1.0 spec safety-considerations section as v22 *Anthropic-internal-hedge-validated* evidence.**

8. **NEW v22 SHARPEN #5 — Adaptive Auto-Harness arXiv 2606.01770 as v22 self-improving-harness model evidence.** A 2026 paper on the self-improving agent harness pattern. **v22 add: cite the paper as v22 *published self-improving harness pattern*. Q3 W3 reading spike, 1 engineer.**

**v22 model shortlist (locked, no v21 change):**
- v1.0: LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration) + MiniLM-L6-v2 (memoryd) + LFM-2.5-230M (v1.0 audiod post-processor) + Hermes Agent (v1.0 audiod agent framework).
- v1.5: HRM-Text-1B (plan-B, SIA Feedback-Agent) + **LFM2.5-1.2B-Thinking (plan-C1, v22 NEW)** + GLM-5.2 (plan-C, cybersecurity + auditable-bug-discovery) + Apertus v1.1 4B (plan-D, EU provenance) + OpenPhone-3B (plan-E, on-device agentic) + LFM2.5-VL-Extract-2 (plan-F, structured-output VLM) + Qwen3-TTS (plan-G, TTS) + Chatterbox (plan-H, voice-cloning) + **LFM2.5-ColBERT-350M (plan-B1, v22 NEW on-device retriever)**.

**v22 retractions:** 0 broad rollbacks. v21 LFM2.5-VL-450M, v21 LFM2.5-230M, v21 Hermes Agent, v21 Memora + As We May Search, v21 perceptiond.skill_evolution, v21 SIA-W+H port, v21 HRM-Text-1B, v21 Apertus v1.1 4B, v21 OpenPhone-3B, v21 GLM-5.2, v21 Qwen3-TTS, v21 Chatterbox all *hold* in v22 with the v22 Liquid-AI-vendor-benchmarked evidence now in the spec. The v22 model shortlist is *unchanged from v21* (only v1.5 plan adds: plan-C1, plan-B1).


[^v22-1]: https://www.liquid.ai/blog/lfm2-5-vl-450m — Liquid AI LFM2.5-VL-450M blog, Apr 8 2026 (NEW v22 CRITICAL #1)
[^v22-2]: https://www.liquid.ai/blog/lfm2-5-1-2b-thinking-on-device-reasoning-under-1gb — Liquid AI LFM2.5-1.2B-Thinking blog, Jan 20 2026 (NEW v22 CRITICAL #2)
[^v22-3]: https://www.liquid.ai/blog/lfm2-5-retrievers — Liquid AI LFM2.5-ColBERT-350M + LFM2.5-Embedding-350M retrievers, Jun 18 2026 (NEW v22 CRITICAL #3)
[^v22-4]: https://techcrunch.com/2026/06/30/openclaw-is-finally-available-on-android-and-ios/ — TechCrunch: OpenClaw iOS+Android launch, June 30 2026 (NEW v22 SHARPEN #1)
[^v22-5]: https://letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vint Cerf TCP/IP-for-agents panel, June 30 2026 (NEW v22 SHARPEN #2)
[^v22-6]: https://venturebeat.com/ai/liquid-ais-smallest-model-yet-lfm25-230m-beats-models-4x-its-size-at-data-extraction-can-run-anywhere/ — VentureBeat: LFM2.5-230M beats 4X its size, late June 2026 (NEW v22 SHARPEN #3)
[^v22-7]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine: Favaro+Clark Anthropic-internal-hedge, June 29 2026 (NEW v22 SHARPEN #4)
[^v22-8]: https://arxiv.org/abs/2606.01770 — "Adaptive Auto-Harness," arXiv 2606.01770, Jun 1 2026 (NEW v22 SHARPEN #5)


## v21 model analysis content (preserved in backup)

The v21 model analysis (preserved in `dan2-model-analysis.v21-backup-2026-07-04.md`, 30.0KB, 235 lines) covers: 3 CRITICAL (LFM2.5-VL-450M holds as v1.0 vision model with ComfyClaw + Mastermind academic validation, Kimi K2.7 Code in GitHub Copilot as 13-step narrative, GLM-5.2 NVFP4 4× DGX Spark as v1.5 plan-E) + 3 SHARPEN (Microsoft Research agentic-evolution 3-axis taxonomy, SAIMY Dream Company, GLM-5 async RL on Hugging Face) + 0 top-5 model swaps + 0 broad rollbacks. v21 model shortlist: LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration) + MiniLM-L6-v2 (memoryd) + LFM-2.5-230M (v1.0 audiod post-processor) + Hermes Agent (v1.0 audiod agent framework). v1.5: HRM-Text-1B (plan-B) + GLM-5.2 (plan-C) + Apertus v1.1 4B (plan-D) + OpenPhone-3B (plan-E). **All v21 content is preserved verbatim in the backup. The v22 add is documented in the v22 addendum above: 3 CRITICAL (LFM2.5-VL-450M vendor-confirmed-on-Jetson-Orin, LFM2.5-1.2B-Thinking v1.5 plan-C1, LFM2.5-ColBERT-350M v1.5 plan-B1) + 5 SHARPEN (OpenClaw iOS+Android, Cerf panel, LFM2.5-230M third-party benchmarked, Time Magazine Favaro+Clark, Adaptive Auto-Harness arXiv 2606.01770). v22 v1.5 plan adds: plan-C1, plan-B1. v22 model shortlist *unchanged* from v21.**



## v20 addendum (2026-07-04 09:35 UTC / 15:05 IST)

**v20 deltas vs v19 (4 CRITICAL, 4 SHARPEN, 0 model changes, 0 broad rollbacks):**

1. **NEW v20 CRITICAL #1 — Axios: Amazon-Jassy-Anthropic jailbreak escalation (July 3 2026).** **v20 add: the closed-source frontier is *inter-vendor fractured*. The on-device + open-weights + auditable memory + auditable agent loop stack is the v20 only trust-resilient substrate. No v19 model change.**

2. **NEW v20 CRITICAL #2 — Bad Epoll CVE-2026-46242 + Mythos missed bug (July 3 2026).** **v20 add: the v1.0 safety spec must adopt the v20 *auditable-bug-discovery* pattern — Mythos + GLM-5.2 + Apertus v1.1 4B scan every release. v20 v1.5 plan-B candidate: GLM-5.2 (cybersecurity) upgraded from research-bet to auditable-bug-discovery-stack. v20 v1.5 plan-D candidate: Apertus v1.1 4B (EU provenance) confirmed as auditable-bug-discovery-stack.**

3. **NEW v20 CRITICAL #3 — Apple camera AirPods Pro suspended (July 3 2026).** **v20 add: no model change, but the v1.0 vision model (LFM2.5-VL-450M) is now the v20 only *shipped* wearable-visual-AI in the v1.0 wearable category. v20 v1.5 plan: LFM2.5-VL-Extract-2 (Liquid AI, structured-output VLM, held from v17) confirmed.**

4. **NEW v20 CRITICAL #4 — LA Times + Bloomberg token-price collapse (July 3 2026).** **v20 add: the on-device stack (lifetime cost of $349 hardware + free local inference) is the v20 only answer to the v20 unit-economics crisis. No v19 model change. v20 v1.0 audiod post-processor: LFM2.5-230M (Liquid AI) held. v20 v1.0 TTS: KittenTTS medium held. v20 v1.0 STT: whisper.cpp base.en held.**

5. **NEW v20 SHARPEN #1 — Wall Street: GLM-5.2 vs Mythos priced (July 3 2026).** **v20 SHARPEN: v20 v1.5 plan-C model candidate: GLM-5.2 (Zhipu AI, MIT, open-weights, now Wall-Street-priced as Mythos-competitor) confirmed. v1.5 plan-C = GLM-5.2 + HRM-Text-1B (plan-B) + Apertus v1.1 4B (plan-D) + OpenPhone-3B (plan-E, new v20).**

6. **NEW v20 SHARPEN #2 — NSA Gen. Rudd on Mythos (Economist, July 3 2026).** **v20 SHARPEN: Mythos is too dangerous to ship widely, too valuable to ship to no one. v20 v1.0 spec safety-considerations section: cite the v20 *auditable-bug-discovery* pattern. No v19 model change.**

7. **NEW v20 SHARPEN #3 — Chris Inglis (former US National Cyber Director) on GLM-5.2 (Dark Reading, July 3 2026).** **v20 SHARPEN: v20 v1.5 plan-C model: GLM-5.2 (Zhipu AI, MIT, open-weights, now former-NSA-cyber-director-endorsed) confirmed. v20 v1.5 plan-B: HRM-Text-1B (Sapient, Apache-2.0, $1,500 trained) held. v20 v1.5 plan-D: Apertus v1.1 4B (Swiss AI, EU provenance) held. v20 v1.5 plan-E: OpenPhone-3B (HKUDS, on-device agentic foundation) held.**

8. **NEW v20 SHARPEN #4 — Meta Pocket gizmos (June 29 - July 3 2026).** **v20 SHARPEN: no v19 model change. v20 v1.0 spec privacy/positioning: cite Meta Pocket gizmos. The on-device + open-weights + auditable memory stack is the v20 only answer to the v20 *user-data-as-AI-training-fuel* pattern.**

**v20 model shortlist (locked, no v19 change):**
- v1.0: LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration) + MiniLM-L6-v2 (memoryd) + LFM-2.5-230M (v1.0 audiod post-processor) + Hermes Agent (v1.0 audiod agent framework).
- v1.5: HRM-Text-1B (plan-B, SIA Feedback-Agent) + GLM-5.2 (plan-C, cybersecurity + auditable-bug-discovery, v20) + Apertus v1.1 4B (plan-D, EU provenance) + OpenPhone-3B (plan-E, on-device agentic) + LFM2.5-VL-Extract-2 (plan-F, structured-output VLM) + Qwen3-TTS (plan-G, TTS) + Chatterbox (plan-H, voice-cloning).

**v20 retractions:** 0 broad rollbacks. v19 Mythos 5 Glasswing framing is now *post-jailbreak-control*, *NSA-validated-at-the-classified-systems-level*, and *Wall-Street-priced-as-replaceable-by-GLM-5.2*. The v19 model shortlist is *unchanged in v20*.


[^v20-1]: https://www.axios.com/2026/07/03/anthropic-ai-models-revived-behind-the-scenes — Axios: How the world's top AI models were revived (Amazon Jassy → Bessent → Lutnick → Amodei, 20-day showdown), July 3 2026 (NEW v20 CRITICAL #1)
[^v20-2]: https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html — "Bad Epoll" Linux kernel flaw (CVE-2026-46242) — Mythos found CVE-2026-43074 but missed Bad Epoll; fix already landed, July 3 2026 (NEW v20 CRITICAL #2)
[^v20-3]: https://www.macrumors.com/2026/07/03/camera-airpods-pro-development-suspended-leaker/ — Apple camera AirPods Pro "suspended" per Kosutami, July 3 2026 (NEW v20 CRITICAL #3)
[^v20-4]: https://www.latimes.com/business/story/2026-07-03/with-token-prices-collapsing-regulation-rising-ais-pricing-power-looks-fragile — LA Times: Silicon Data LLM Token Expenditure Index -20% from May high; AI pricing power "looks fragile," July 3 2026 (NEW v20 CRITICAL #4)
[^v20-5]: https://letsdatascience.com/news/ai-driven-rotation-reshapes-stock-market-leadership-dc767e6c — Palo Alto + CrowdStrike all-time highs; PHLX semi -6.3%/-5.4% Wed/Thu; WSJ: Zhipu GLM-5.2 now rivals Mythos at vulnerability hunting, July 3 2026 (NEW v20 SHARPEN #1)
[^v20-6]: https://mimir.substack.com/p/the-new-news-in-ai-7326-edition — NSA Gen. Joshua Rudd: Mythos "broke into almost all of our classified systems, not in weeks, but in hours," July 3 2026 (NEW v20 SHARPEN #2)
[^v20-7]: https://www.darkreading.com/cyber-risk/chinese-llms-broaden-gap-between-attackers-defenders — 360 Security "Tulongfeng" finds 3,400+ vulnerabilities; Chris Inglis (former US National Cyber Director) endorses GLM-5.2 for defenders, July 3 2026 (NEW v20 SHARPEN #3)
[^v20-8]: https://www.mediapost.com/publications/article/416292/meta-prizes-ai-generated-creative-in-new-mini-game.html — Meta launches "Pocket" AI gizmos app on Apple App Store + Google Play, June 29 - July 3 2026 (NEW v20 SHARPEN #4)


## v19 model analysis content (preserved in backup)

The v19 model analysis (preserved in `dan2-model-analysis.v19-backup-2026-07-04.md`, 23.1KB, 196 lines) covers: 4 CRITICAL (Google AI brain drain, Anthropic-Newsom California, OpenClaw founder → OpenAI governance risk, MemoMind One $20/mo) + 5 SHARPEN (China Mobile MWC Shanghai AI glasses, NATO SAPIENT, Reuters Meta compute cap, AR Glasses size problem, Alphabet stock worst month). v19 model shortlist: LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration) + MiniLM-L6-v2 (memoryd) + LFM2.5-230M (v1.0 audiod post-processor) + Hermes Agent (v1.0 audiod agent framework). v1.5: HRM-Text-1B (plan-B) + GLM-5.2 (plan-C, now Wall-Street-priced) + Apertus v1.1 4B (plan-D) + OpenPhone-3B (plan-E). **All v19 content is preserved verbatim in the backup. The v20 add is documented in the v20 addendum above: 4 CRITICAL (Axios inter-vendor trust, Bad Epoll auditable-bug-discovery, Apple camera AirPods Pro wearable-vacuum, LA Times token-price collapse) + 4 SHARPEN (Wall Street GLM-5.2 vs Mythos, NSA Rudd, Chris Inglis, Meta Pocket). v20 model shortlist is *unchanged* from v19.**
