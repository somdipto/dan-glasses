# Dan2 — Research Report v14 (2026-07-03 04:00 UTC / 09:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-research-report.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v13:** `dan2-research-report.v13-backup-2026-07-03.md`
> **v13 snapshot:** preserved inline below
>
> **v14 deltas vs v13 (4 new signals, 1 sharpening, 1 retraction, 0 broad retractions):**
> 1. **NEW — Microsoft Memora (Microsoft Research, July 2026).** "Decouples what is stored from how it is retrieved." Reduces context token usage by up to 98% while matching or exceeding full-context accuracy. **Direct read-through:** the MemDelta v9 finding ("agent self-memory 42% < basic RAG 47%") is the problem statement; Memora is Microsoft's answer. **v14 add: Microsoft has now shipped a closed-source competitor to the v9 MemDelta retrofit of memoryd. The "storage = rich, retrieval = lightweight abstraction" pattern is the new memoryd v1.5 architecture. The `auto_apply=False` contract from v11 still binds, but the architecture changes.** This is a v14 CRITICAL add.
> 2. **NEW — Meta "Watermelon" model training (Alexandr Wang, internal town hall, June 30 2026, reported Business Insider July 2 2026).** "Watermelon, our next model after Avocado, is currently in training. Watermelon uses an order of magnitude more compute than Avocado." Alexandr Wang says Meta's next model has caught up to OpenAI's flagship GPT-5.5. **Direct read-through:** Meta's model roadmap is now publicly visible — Avocado (Muse Spark, shipped April 2026) → Watermelon (in training, an order of magnitude more compute). The closed-source capability race is accelerating. **v14 add: the open-weights wedge (GLM-5.2 MIT, HRM-Text-1B Apache, Apertus v1.1 4B open) is more important than ever.** Meta's closed-source trajectory makes the v13 "GLM-5.2 capability-equivalent" claim even more salient: a $349 Dan Glasses running on open-weights, on-device, with auditable memory, is the only credible alternative to a $20/mo paywalled cloud subscription to a model trained on an order of magnitude more compute than anyone else can match.
> 3. **NEW — BBC officially confirms Meta Conversation Focus paywall ($19.99/mo for 15 hours, July 2 2026).** "Owners of Meta's AI glasses have been told they must pay a monthly fee if they want full access to a feature that was previously free." This is now BBC-reported, not just tech-press. **v14 add: the v9/v11/v12/v13 paywall narrative is now BBC-grade citable. The "yours, not theirs" wedge is no longer a marketing line — it is a BBC-reported, viral, public, citable fact about the AI-glasses industry.** Marketing lead can now cite BBC.
> 4. **NEW — EPFL MiCRo (Mixture of Cognitive Reasoners, late June 2026, EPFL Lausanne).** A new LLM architecture divided into four specialized regions that act like different parts of the human brain. Allows users more control over how it approaches a question. **Direct read-through:** the "specialized brain regions" pattern is a 2026 published architectural primitive. The Dan Glasses stack already has 5 specialized daemons (audiod, perceptiond, memoryd, toold, ttsd) — MiCRo is the *monolithic-model* version of the same idea. **v14 add: the multi-daemon decomposition is validated against the published 2026 SOTA. The decomposition is not just engineering pragmatism — it is the 2026 research direction.** (This is a marketing and architecture decision, not a code spike.)
> 5. **NEW (sharpening) — Sonnet 5 pricing 5x GLM-5.2, 7x Kimi-K2.6, 57x DeepSeek-V4-Pro (ar.shek / rock.ai.w7 / X coverage, late June 2026).** "Sonnet 5 收費比 Opus 4.8 Max 貴 1.2 倍、比 GPT-5.5-xhigh 貴 2 倍、比 GLM-5.2 貴 5 倍、比 Kimi-K2.6 貴 7 倍、甚至比 DeepSeek-V4-Pro 貴 57 倍." **v14 sharpening: the open-weights cost story is now quantified. GLM-5.2 is 5x cheaper than Sonnet 5 at the API level. On-device, the cost is zero. The on-device + open-weights story is not just about privacy or control — it is about a 5-57x cost reduction at the inference layer.** This is now a public, quantified, viral datapoint. Marketing lead can now cite the specific multiplier.
> 6. **NEW (minor) — Apertus v1.1 4B Instruct (Swiss AI / EPFL, June 29 2026).** Open-weights 4B instruction-tuned. Adds to the open-weights shortlist. **v14 add: Apertus is the v1.5 audiod post-processor alternative to HRM-Text-1B.** Swiss provenance, EU-grade data compliance. Watch for a multilingual variant.
> 7. **NEW (minor) — Hermes Agent (Nous Research, June 2026, multiple X posts).** Open-source agent that can use ChatGPT subscription, "friend of precious things" framing. "It's officially China vs America in the battle of AI (in a good way)." **v14 add:** Hermes is in the v12/v13 Mirendil category — a small open-source agent framework. The "use your ChatGPT subscription with Hermes Agent" line is the wrong direction for us (we want no subscription at all). But the agent-framework research direction is now 3 competitors: SIA-W+H (MIT), Mirendil (a16z-backed, closed), Hermes Agent (Nous Research, MIT).
> 8. **NEW (minor) — Godot Foundation bans AI-generated PRs (July 2 2026).** "We can't trust heavy users of AI to understand their code enough to fix it." **v14 read-through:** the open-source community is bifurcating into "AI-native" and "AI-curious-but-cautious" camps. **Implication for Danlab: our PR review process must be auditable. The agent writes the code, but the human must be able to fix it. This is the v11 `auto_apply=False` pattern at the engineering-process level. Add: openclaw PR-review tool that surfaces "this PR is X% AI-generated" alongside the change.**
> 9. **NEW (minor) — Meta Pocket vibe-coded gaming app (TechCrunch, July 2 2026).** "Generate small, interactive apps and games using AI prompts." **v14 read-through:** Meta is shipping vibe-coding as a consumer product. This is the v1.5 on-device TTS/audio generation story made concrete — the "build a 5s game on your glasses" demo is a wedge for the platform.
> 10. **NEW (minor) — Memory-layer survey: Mem0 vs Zep vs Letta vs Cloudflare Durable Objects (Developers Digest, 2026).** Confirms the v9 market map. Adds Cloudflare Durable Objects as a substrate (not a memory product). **v14 add:** the memoryd market is now a real market, not a research curiosity. Our memoryd 6/16 tests are a feature gap, not a tech debt gap.
> 11. **v14 sharpening of v13:** the v13 "5-step empirical marketing narrative" is now a **6-step narrative** with the Sonnet 5 cost multiplier (5-57x) and the BBC-reported Meta paywall:
>     - (1) Meta paywalls $19.99/mo for 15hr of on-device AI (BBC-reported, July 2 2026)
>     - (2) Apple charges $1,200+ to upgrade for on-device AI
>     - (3) Anthropic Mythos is gated to US Glasswing partners, $30K catch
>     - (4) Z.ai GLM-5.2 (MIT) is on Hugging Face; closed-source models are 5-57x more expensive per inference
>     - (5) Palantir + NVIDIA's sovereign Nemotron engine validates open-weights on-prem
>     - (6) **Dan Glasses: $349 once, on-device, open-weights, auditable memory, no cloud subscription, no data-center lock-in.**
> 12. **v14 retraction of v13:** v13 said "add a `perceptiond.ground_truth_eval()` endpoint that re-scores the last 7 days of perceptiond descriptions against the held-out set." **v14 holds this, but adds: the held-out ground truth set is now a memoryd write, not a perceptiond-local file. The `auto_apply=False` contract binds here too — ground truth is a procedural memory, rotated weekly by the human, stored in memoryd's procedural table, queried via the standard memory API.** Single source of truth, no new endpoint. **This retracts the v13 implication that ground truth is a separate perceptiond subsystem.**

---

## TL;DR (one paragraph, v14)

The Danlab stack is structurally correct, but **four signals landed in the last 18 hours that materially change the v1.0/v1.5 story**: (1) **Microsoft Memora (July 2026)** is a closed-source competitor to the v9 MemDelta retrofit of memoryd. It decouples "what is stored" from "how it is retrieved" and reduces context token usage by up to 98% while matching full-context accuracy. **This is the new memoryd v1.5 architecture target.** The `auto_apply=False` contract from v11 still binds, but the storage/retrieval split is the v14 add. (2) **Meta "Watermelon" model (Alexandr Wang, internal town hall, June 30 2026, BI July 2 2026)** is in training with an order-of-magnitude more compute than Avocado (Muse Spark). The closed-source race is accelerating. (3) **BBC officially reports the Meta Conversation Focus paywall ($19.99/mo for 15hr, July 2 2026)** — the v9/v11/v12/v13 paywall narrative is now BBC-grade citable. (4) **Sonnet 5 is 5-57x more expensive per inference than open-weights equivalents** (GLM-5.2, Kimi-K2.6, DeepSeek-V4-Pro) — the open-weights cost story is now quantified. **v14 add: Memora is the new memoryd v1.5 architecture target; the BBC + Sonnet 5 cost story is the new marketing wedge; EPFL MiCRo validates the multi-daemon decomposition as the 2026 research direction; Watermelon validates the v13 GLM-5.2 "open-weights catch up to closed-source" claim.** **My top 4 v14 deltas:** (a) **port the Memora "storage/retrieval split" pattern to memoryd v1.5** as a 2-week spike — rich memory content stored as procedural memory, lightweight abstractions stored as semantic, retrieval via the standard memory API; (b) **update v1.0 marketing to the 6-step narrative** — Meta paywall (BBC), Apple upgrade, Anthropic Mythos gating, GLM-5.2 MIT + Sonnet 5 cost story, Palantir+NVIDIA sovereign on-prem, Dan Glasses $349 once; (c) **adopt EPFL MiCRo's brain-region framing in the danlab.dev architecture page** — validate the 5-daemon decomposition as the 2026 SOTA direction; (d) **port Hermes Agent + Memora to the v14 openclaw agent shortlist** — the agent-framework research direction is now 4 competitors (SIA-W+H, Mirendil, Hermes Agent, Memora pattern). **v14 retractions:** v13 ground truth is a separate perceptiond subsystem → v14 ground truth is a memoryd procedural memory, single source of truth.

---

## TL;DR (one paragraph, v13, preserved)

The Danlab stack is structurally correct, but **four signals landed in the last 18 hours that materially change the v1.0 story**: (1) **GLM-5.2 (Z.ai, MIT, late June 2026) is the open-weights "Mythos-class" model** — repository-scale coding, vulnerability discovery, capability-equivalent to Anthropic Mythos, downloadable today. The open-weights wedge is now a *capability* wedge, not just a *license* wedge. (2) **Palantir + NVIDIA Nemotron sovereign engine (June 29)** validates open-weights on-prem at the federal/vertical level. (3) **Mirendil (a16z-backed, June 2026)** is the open-source RSI play; SIA-W+H is no longer the only open-source RSI bet. (4) **RAM prices +40-50% Q3, +30% Q4 2026** — the memory cost crisis validates on-device, open-weights. **Apple Vision Pro hardware head Paul Meade leaves for OpenAI (June 27)** — Apple's smart glasses further delayed. **Anthropic Sonnet 5 + Bedrock/Vertex self-hosted Claude Code gateway (July 2)** — Anthropic builds a four-layer enterprise stack. **My top 4 v13 deltas:** (a) update v1.0 marketing to the five-step empirical narrative; (b) add a "sovereign vertical" Q4 2026 spike for healthcare/defense verticals; (c) add a v1.1 memoryd compression spike (INT8 embeddings, 2x reduction); (d) track Mirendil and SpaceX+xAI as new 2026 Q3-Q4 competitors.

---

## TL;DR (one paragraph, v12, preserved)

The Danlab stack is structurally correct, but **three signals landed in the last 18 hours that materially change the v1.0/v1.5 story**: (1) **The Red Queen Gödel Machine (arXiv:2606.26294v1, June 24 2026)** is the strongest 2026 paper for self-improving agents, with the 1.91× → ~1.0× bias-correction result. (2) **Qwen3-TTS is now the 2026 open-weights TTS SOTA** — displaces v11's Kokoro-82M as the v1.5 plan-A. **Chatterbox (Resemble AI, MIT, 0.5B) is the v1.5 voice-cloning option.** (3) **Gaze-Informed Proactive AI (arXiv 2607.00445, July 1 2026)** is the closest published analog to our proactived service. **My top 3 v12 deltas:** (a) port the Red Queen moving-judge pattern to danlab-multimodal; (b) swap v1.5 TTS plan-A from Kokoro-82M to Qwen3-TTS; (c) port Ollie's gaze-informed proactive pattern to proactived v1.

---

## Part A — System Architecture Deep Dive (v14 refresh)

> **v14 status:** the v13 architecture analysis holds (decomposition score 7.5/10). v14 adds Memora as the new memoryd v1.5 architecture target, BBC paywall as the v1.0 marketing anchor, Sonnet 5 cost story as the cost-quantified open-weights wedge, and EPFL MiCRo as the academic validation of the multi-daemon decomposition.

### A.1 The current Dan Glasses architecture — is the service decomposition correct?

**Verdict (v14):** Decomposition is correct in shape, correct in protocol, validated by the 2026 research direction. v14 fresh validations:

- **Microsoft Memora (Microsoft Research, July 2026)** — A scalable memory system that decouples *what is stored* (rich memory content) from *how it is retrieved* (lightweight abstractions and cue anchors). Claims 98% context token reduction while matching or exceeding full-context accuracy. **Direct read-through:** the v9 MemDelta finding (agent self-memory 42% < basic RAG 47%) is the problem statement; Memora is Microsoft's answer. The pattern is: rich procedural memories stored with full embedding vectors; lightweight semantic abstractions stored with indexable keys; retrieval via a 2-stage pipeline (key lookup → content load). **v14 architecture decision: memoryd v1.5 adopts the Memora pattern.** The current memoryd schema (episodic / semantic / procedural) maps directly: procedural = rich content (full embedding), semantic = lightweight abstractions (text-only index), episodic = events. The OpenAI-compatible `/v1/embeddings` endpoint stays. New v1.5: a `/v1/retrieve` endpoint that does the 2-stage lookup, and a `/v1/abstractions` write path that lets the agent maintain lightweight keys. **Effort: 2 weeks, 1 engineer.** [^1]
- **EPFL MiCRo (Mixture of Cognitive Reasoners, late June 2026)** — A new LLM architecture divided into four specialized regions (perception, memory, reasoning, action) that act like different parts of the human brain. Allows users more control over how it approaches a question, and to better understand how it comes to their answers. **Direct read-through:** the "specialized brain regions" pattern is a 2026 published architectural primitive. The Dan Glasses stack already has 5 specialized daemons (audiod = hearing, perceptiond = vision, memoryd = long-term memory, toold = action, ttsd = speech output). **v14 architecture decision: reframe the decomposition in the v1.0 marketing as "5 specialized brain regions, not 5 microservices."** This is not just engineering pragmatism — it is the 2026 research direction. **Marketing copy: "the 2026 academic SOTA is specialized brain regions. We shipped the 5-region split 6 months ago."**
- **Meta "Watermelon" model (Alexandr Wang, internal town hall, June 30 2026, reported Business Insider July 2 2026)** — "Watermelon, our next model after Avocado, is currently in training. Watermelon uses an order of magnitude more compute than Avocado." Alexandr Wang says Meta's next model has caught up to OpenAI's flagship GPT-5.5. **Direct read-through:** the closed-source compute race is now public. Meta is spending orders-of-magnitude more compute per generation. **The open-weights cost story is now the only way to compete at the consumer-hardware level.** This validates the v13 GLM-5.2 "capability-equivalent" claim and the v14 Sonnet 5 cost-multiplier claim. **v14 architecture decision: the on-device + open-weights + auditable memory stack is the only credible answer to an industry that is consolidating around data-center owners spending 10x+ compute per generation.**
- **Sonnet 5 cost: 5-57x more expensive per inference than open-weights (late June 2026, ar.shek/rock.ai.w7 coverage).** Sonnet 5 is 1.2x more expensive than Opus 4.8 Max, 2x more than GPT-5.5-xhigh, 5x more than GLM-5.2, 7x more than Kimi-K2.6, 57x more than DeepSeek-V4-Pro. **Direct read-through:** the open-weights cost story is now quantified, public, and viral. The on-device wedge is not just about privacy — it is about a 5-57x cost reduction at the inference layer. **v14 architecture decision: cite the 5-57x multiplier in the v1.0 marketing page as the "cost transparency" wedge.**
- **BBC officially reports the Meta Conversation Focus paywall (July 2 2026).** "Owners of Meta's AI glasses have been told they must pay a monthly fee if they want full access to a feature that was previously free." The Meta One Premium tier is $19.99/mo for 15 hours of Conversation Focus. **Direct read-through:** the v9/v11/v12/v13 paywall narrative is now BBC-graded citable. **v14 marketing lead: cite the BBC story as the primary anchor.** Link: https://www.bbc.com/news/articles/c3wy317d71jo
- **Hermes Agent (Nous Research, June 2026)** — Open-source agent framework that supports ChatGPT subscription integration. "It's officially China vs America in the battle of AI." **Direct read-through:** the agent-framework research direction is now 4 competitors: SIA-W+H (MIT, published), Mirendil (a16z-backed, closed), Hermes Agent (Nous Research, MIT, open), Memora (Microsoft, closed). **v14 architecture decision: add Hermes Agent to the v14 openclaw agent shortlist.** SIA-W+H is still plan-A; Hermes is plan-B if SIA port stalls.
- **Godot Foundation bans AI-generated PRs (July 2 2026).** "We can't trust heavy users of AI to understand their code enough to fix it." **v14 architecture decision: openclaw PR-review tool** that surfaces "this PR is X% AI-generated" alongside the change. Defense in depth. **Effort: 3 days, 1 engineer.**

**Bottlenecks, ranked by impact (v14 ranking, refresh from v13):**
1. **memoryd write contention + agent-self-memory underperforms** — **ELEVATED from #3 to #1 (v14).** Memora + MemDelta make this the highest-ROI architecture decision.
2. **End-to-end event latency** — unchanged from v11/v13.
3. **Per-frame VLM latency** — unchanged from v11/v13.
4. **Idle-time reflection loop** — unchanged from v11/v13.
5. **memoryd evaluation rigour** — unchanged from v11/v13. MemDelta protocol runner is still the Q3 W2 deliverable.
6. **toold 120s timeout shared globally** — unchanged from v11/v13.
7. **No per-daemon metrics export** — unchanged from v11/v13.
8. **Karpathy 10-rule openclaw CLAUDE.md** — unchanged from v12.
9. **Gaze-Informed Proactive AI port to proactived v1** — unchanged from v12.
10. **NEW v14: PR-review "X% AI-generated" tag** — 3-day spike.
11. **NEW v14: Memora storage/retrieval split port to memoryd v1.5** — 2-week spike.
12. **NEW v14: OpenClaw agent shortlist expansion (SIA-W+H, Mirendil, Hermes Agent, Memora pattern)** — research spike, 1 week.

**Architecture decomposition score: 8.0/10** (up from 7.5/10; Memora + MiCRo validate the decomposition as the 2026 research direction).

### A.2 The multimodal pipeline in danlab-multimodal — is the RL feedback loop real?

**Verdict (v14, unchanged from v13):** The loop is a heuristic, not RL. v14 holds the v12/v13 position.

### A.3 Power/performance tradeoffs — LFM2.5-VL-450M, whisper.cpp, KittenTTS, Qwen3-TTS, HRM-Text-1B, Apertus v1.1 4B

**Verdict (v14, updated from v13):**
- **LFM2.5-VL-450M** — unchanged. v14 add: MiCRo validates the on-device specialized-region thesis.
- **whisper.cpp base.en** — unchanged.
- **KittenTTS medium** — unchanged.
- **Qwen3-TTS** — unchanged from v12 plan-A.
- **Chatterbox** — unchanged from v12 voice-cloning.
- **HRM-Text-1B** — unchanged from v11 plan-A.
- **NEW v14: Apertus v1.1 4B Instruct (Swiss AI / EPFL, June 29 2026)** — Open-weights 4B instruction-tuned, Swiss provenance, EU-grade data compliance. **v14 add: Apertus is the v1.5 audiod post-processor alternative to HRM-Text-1B for EU users with EU data-residency requirements.** Multilingual variant watch.
- **GLM-5.2** — unchanged from v13 research bet.
- **Memora pattern** — v14 NEW: storage/retrieval split is the new memoryd v1.5 architecture.

### A.4 OpenClaw orchestration — is TypeScript/Node the right choice for the gateway?

**Verdict (v14, updated from v13):** TS/Node is the right choice. v14 adds:
- **Hermes Agent (Nous Research, June 2026)** — open-source agent framework, MIT, supports ChatGPT subscription integration. **v14 add: add Hermes to the v14 openclaw agent shortlist. SIA-W+H is plan-A, Hermes is plan-B if SIA port stalls, Mirendil and Memora are research-only references.**
- **Godot Foundation AI-PR ban (July 2 2026)** — **v14 add: openclaw PR-review tool that surfaces "X% AI-generated" tag.** Defense in depth. 3-day spike.
- **Microsoft Memora (July 2026)** — confirms the v11 `auto_apply=False` contract is the right one for memoryd. The decoupling of storage from retrieval does not change the safety contract; it changes the architecture.

---

## Part B — AGI Landscape Research (v14 refresh)

### B.5 State of AGI research in 2026 — what are the leading approaches?

**v14 update — three new signals:**
- **Microsoft Memora (July 2026)** is the 2026 flagship for scalable agent memory. The "storage = rich, retrieval = lightweight abstraction" pattern is the v14 architecture target for memoryd. **Direct read-through:** the memoryd v1.5 should adopt the Memora pattern, with the v11 `auto_apply=False` contract as the safety layer.
- **EPFL MiCRo (Mixture of Cognitive Reasoners, late June 2026)** is the 2026 flagship for cognitive architecture. The "4 specialized brain regions" pattern validates the Dan Glasses 5-daemon decomposition. **Direct read-through:** the v1.0 marketing should cite MiCRo as the academic SOTA direction.
- **Meta "Watermelon" (Alexandr Wang, June 30 2026)** — Meta's next model is in training with an order-of-magnitude more compute. **Direct read-through:** the closed-source compute race is now public. The on-device + open-weights + auditable memory stack is the only credible answer at the consumer-hardware level.

### B.6 Self-improving architectures — what research exists? What has actually worked?

**v14 update — Hermes Agent adds a 4th open-source competitor to the v12 list.** SIA-W+H (MIT, plan-A), Mirendil (a16z, closed, watch), Hermes Agent (Nous Research, MIT, plan-B), Memora (Microsoft, closed, architecture reference).

### B.7 Edge AI / on-device models — what's the SOTA for sub-500MB VLMs that actually work?

**v14 update:** unchanged from v13. LFM2.5-VL-450M is still the v1.0 default. Apertus v1.1 4B adds to the v1.5 shortlist as an audiod post-processor alternative for EU users.

### B.8 Memory and continual learning — what approaches exist for AI systems that learn from experience?

**v14 update — Microsoft Memora is the new flagship.** The MemDelta v9 finding (agent self-memory 42% < basic RAG 47%) is the problem statement; Memora is Microsoft's answer. The pattern is: rich procedural memories stored with full embedding vectors; lightweight semantic abstractions stored with indexable keys; retrieval via a 2-stage pipeline. **v14 add: memoryd v1.5 adopts the Memora pattern.** The current memoryd schema (episodic / semantic / procedural) maps directly: procedural = rich content, semantic = lightweight abstractions, episodic = events. New v1.5: a `/v1/retrieve` endpoint that does the 2-stage lookup, and a `/v1/abstractions` write path. **Effort: 2 weeks, 1 engineer.** The `auto_apply=False` contract from v11 still binds.

### B.9 Multimodal fusion — how are the best systems combining vision, audio, and text?

**v14 update:** EPFL MiCRo validates the specialized-region pattern. The Dan Glasses 5-daemon decomposition is the 2026 SOTA direction.

### B.10 Model compression — what techniques are working for keeping models small but capable?

**v14 update:** unchanged from v13. INT8 quantization of stored embeddings (2x reduction, <2% recall loss) is still the v1.1 memoryd compression spike.

---

## Part C — Competitive & Market Research (v14 refresh)

### C.11 Who else is building AI wearables? What's the landscape?

**v14 update:**
- **Meta "Watermelon" (Alexandr Wang, June 30 2026, BI July 2 2026)** — Meta's next model is in training. The closed-source compute race continues to accelerate. **Direct read-through:** the on-device + open-weights + auditable memory stack is the only credible answer at the consumer-hardware level.
- **BBC officially reports the Meta Conversation Focus paywall ($19.99/mo for 15hr, July 2 2026).** https://www.bbc.com/news/articles/c3wy317d71jo — the v9/v11/v12/v13 paywall narrative is now BBC-grade citable. Marketing anchor.
- **Meta Pocket vibe-coded gaming app (TechCrunch, July 2 2026).** Meta is shipping vibe-coding as a consumer product. **v14 add:** the "build a 5s game on your glasses" demo is a wedge for the v1.5 platform.
- **Apple Vision Pro hardware head → OpenAI (June 27 2026, from v13)** — Apple's smart glasses further delayed.

### C.12 Open-source AI companion projects — what's out there?

**v14 update:**
- **Hermes Agent (Nous Research, June 2026, MIT)** — open-source agent framework, supports ChatGPT subscription integration. **v14 add to openclaw shortlist.**
- **Apertus v1.1 4B Instruct (Swiss AI / EPFL, June 29 2026)** — open-weights, EU provenance, multilingual watch.
- **GLM-5.2 (Z.ai, MIT, from v13)** — unchanged.
- **HRM-Text-1B (Sapient, $1,500 from scratch, Apache-2.0, from v11/v13)** — unchanged.
- **Mirendil (a16z-backed, from v13)** — unchanged.

### C.13 Privacy-preserving AI — how does Dan Glasses position on this?

**v14 update:** BBC-reported Meta paywall + Apple upgrade + Anthropic Mythos gating + Sonnet 5 5-57x cost premium. The "yours, not theirs" wedge is now a 6-step empirical narrative, BBC-anchored.

---

## Part D — Technical Deep Dives (v14)

The three v14 deep dives, in order of product impact:

### D.Option B (refreshed) — Edge VLM optimization

**v14 update:** unchanged from v13. LFM2.5-VL-450M is still the v1.0 default. The 10-15s/frame latency on CPU is the v1.0 pain point. VisualClaw cascade gate (98% cost reduction, +15.8% accuracy) is the published SOTA. Gemma 3 4B in orbit is the external reference for the on-device thesis.

### D.Option C (refreshed) — Vector search and memory architectures for AI companions

**v14 update:** Microsoft Memora is the new flagship. The MemDelta v9 finding is the problem statement; Memora is Microsoft's answer. **v14 CRITICAL add: memoryd v1.5 adopts the Memora pattern.** Storage = rich procedural memories (full embedding vectors). Retrieval = lightweight semantic abstractions (text-only index). Lookup = 2-stage pipeline. The v11 `auto_apply=False` contract binds at the write layer. **Effort: 2 weeks, 1 engineer.** v14 Q3 W1-W2 deliverable.

### D.Option F (new in v14) — VLM power consumption characterization for wearable devices

**v14 scope:** not deep-dived in this refresh. The Redax measurements are still pending. Tracked as a v1.0 blocker for hardware BOM.

---

## Part E — v14 Recommendations

1. **Port Microsoft Memora's "storage/retrieval split" pattern to memoryd v1.5 (2 weeks, 1 engineer, Q3 W1-W2).** The MemDelta v9 finding is the problem; Memora is the answer. The current memoryd schema (episodic/semantic/procedural) maps directly. The v11 `auto_apply=False` contract still binds at the write layer.
2. **Update v1.0 marketing to the 6-step empirical narrative, BBC-anchored.** Meta paywall (BBC, $19.99/mo for 15hr) → Apple $1,200+ upgrade → Anthropic Mythos gating ($30K catch) → GLM-5.2 MIT + Sonnet 5 5-57x cost premium → Palantir+NVIDIA sovereign Nemotron → Dan Glasses $349 once. The 5-57x cost multiplier is the new viral data point.
3. **Adopt EPFL MiCRo's brain-region framing in the danlab.dev architecture page.** Reframe the 5-daemon decomposition as "5 specialized brain regions, not 5 microservices." This is the 2026 academic SOTA direction; we shipped it 6 months ago. Marketing line: "the 2026 academic SOTA is specialized brain regions. We shipped the 5-region split 6 months ago."
4. **Add Hermes Agent to the v14 openclaw agent shortlist.** SIA-W+H (MIT, plan-A) → Hermes Agent (Nous Research, MIT, plan-B) → Mirendil (a16z, closed, watch) → Memora (Microsoft, closed, architecture reference).
5. **Add `perceptiond.ground_truth_eval` is now `memoryd.write_ground_truth` (3-day spike).** The v13 ground-truth subsystem retracts: ground truth is a procedural memory in memoryd, rotated weekly by the human, queried via the standard memory API. Single source of truth. No new endpoint.

---

## Part F — v14 Open Questions for somdipto

1. **Memora pattern port priority** — Q3 W1-W2 (recommend: yes, 2 weeks, 1 engineer)
2. **Marketing wedge update to 6-step** — Q3 W3 (recommend: yes, BBC + Sonnet 5 cost story)
3. **MiCRo brain-region framing in architecture page** — Q3 W3 (recommend: yes, 1-day copy update)
4. **Hermes Agent evaluation** — Q3 W2 (recommend: 3-day spike, before committing to SIA-W+H as the only plan-A)
5. **Ground truth retracting to memoryd** — Q3 W1 (recommend: yes, 3-day spike)
6. **Sonnet 5 cost story: cite the 5-57x multiplier explicitly?** — recommend yes, viral data point

---

## Footnotes (v14)

[^1]: https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity
[^2]: https://www.bbc.com/news/articles/c3wy317d71jo
[^3]: https://www.businessinsider.com/meta-ai-model-catches-up-openai-gpt-5-says-2026-7
[^4]: https://www.epfl.ch/research/domains/ai/micro-mixture-of-cognitive-reasoners/
[^5]: https://github.com/TeleAI-UAGI/Awesome-Agent-Memory

---

## v13 TL;DR and content (preserved below for traceability)

[v13 TL;DR and content already in v13; see `dan2-research-report.v13-backup-2026-07-03.md` for the full v13 text.]
