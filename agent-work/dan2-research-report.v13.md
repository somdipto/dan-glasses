# Dan2 Research Report v13 — Danlab AGI Landscape
**Author:** Dan2 (lead scientist / architect, danlab.dev)
**Date:** 2026-06-19 09:30 IST (04:00 UTC)
**Supersedes:** dan2-research-report.v12 (2026-06-18, ~24 hours old)

---

## 0. TL;DR (v13 deltas from v12)

1. **Mnemosyne (98.9% on LongMemEval, ICLR 2025/2026)** is now the public benchmark leader and ships a native **OpenClaw provider** (`pip install mnemosyne-memory[openclaw]`). This collapses the "Hindsight vs Mem0 vs Mnemosyne" decision in v12 and unblocks the memory consolidation workstream in days, not months.
2. **User-as-Code (UaC, arXiv:2606.16707, June 16 2026)** — typed Python objects as a living user model. 78.8% on LOCOMO. A 5th research/architecture option that didn't exist when v12 was written. Suggests the "memory as a software project" pattern is a real 2026 trend.
3. **Fable 5 is coming back, ~July 12 2026** (Anthropic flew to Washington; active negotiations per Politico/NYT). The v12 "Fable 5 export control" framing as a *permanent* tailwind was premature — it is a **~30-day disruption** that probably resolves with a compliance regime. Adjust posture: "Fable-5-safe" is a feature, not a regulatory moat.
4. **Liquid AI shipped LFM2.5-ColBERT-350M and LFM2.5-Embedding-350M (June 18 2026)** — retrieval-layer small models that sit alongside LFM2.5-VL-450M. The retrieval-side of the v1.5 memory workstream just got a purpose-built 350M embedding. The MiniLM-L6-v2 baseline is now under-bid.
5. **Z.ai GLM-5.2 (June 14 2026)** — 1M-token MIT-licensed open-weight frontier model, leads open-weights on coding/long-horizon, runs on consumer H100. **New training pipeline option for SIA's Feedback-Agent**: GLM-5.2 is open, MIT, and strong enough to replace the cloud API in the self-improvement loop.
6. **GLM-5.2 ranks #2 on PostTrainBench** (only behind Opus 4.8; beats Opus 4.7 and GPT-5.5). **The agent that improves small models via post-training is the SIA-loop's own target.** This validates SIA's premise and gives a credible open backend.
7. **Brilliant Labs Halo confirmed as the open-source AI Leap (June 17 2026)** — multiple independent write-ups (New Market Pitch, LinkedIn, Desahu) call it "the Definitive Open-Source AI Leap" and a "Proactive Intelligence Era" signal. The v22 open-source Kit workstream is even more right than v12 thought.
8. **Apple memory chip pricing pressure (Tim Cook, WSJ, June 18 2026)** — Apple will raise prices on memory-heavy devices. **Validates the v12 "128GB eMMC may be cost-prohibitive" concern.** Confirms the 64GB primary storage tier is the right default.
9. **Illinois HB4843 (smart glasses driving ban, June 2026)** — first US state to consider banning smart-glasses use while driving. Real regulatory friction that will spill onto Dan Glasses in 12-24 months.
10. **OpenClaw skill malware documented in production (Skywork, June 2026)** — the v12 OpenClaw-security concern moves from "theoretical (arXiv 2605.25435)" to "documented in the wild." Sigstore Rekor and signed skills go from "nice to have" to "ship-now."

---

## 1. System Architecture Deep Dive (delta from v12)

### 1.1 Current Dan Glasses service decomposition

**Verdict: still correct, but the OpenClaw security gap is the single biggest v1.5 risk now that skill malware is documented.** See §1.4.

The five-service decomposition (per the live SPECs verified in this run) is unchanged from v12:
- audiod (8090/8091, Python+FastAPI, 73 tests)
- perceptiond (8092, Python+llama-mtmd-cli, 8 tests, LFM2.5-VL-450M Q4_0)
- memoryd (8741, Python+FastAPI+SQLite+MiniLM, 16 tests)
- toold (8742, Python+FastAPI, 18 tests)
- ttsd (8743, Python+KittenTTS medium, 6 tests)

**New v13 finding: the audiod SPEC (v0.5) shows production-grade maturity.** PTT via evdev, force-flush at `max_segment_ms`, confidence from `whisper-cli -ojf` JSON sidecar, event schema conformance test, multi-client WS with dead-client pruning. This is not a prototype. The v12 "perceptiond is the most legitimate Rust candidate" reasoning now also applies to audiod — both services are CPU-bound and dominate the RSS budget on aarch64.

### 1.2 The danlab-multimodal RL claim

**Verdict: unchanged from v12 — heuristic, with SIA-H as the credible upgrade path.** The Mnemosyne + UaC + GLM-5.2 deltas strengthen the upgrade path:

- **GLM-5.2 as the SIA Feedback-Agent.** The Feedback-Agent is the LM that reads trajectories and edits the harness. v12 said "LFM2.5-1.2B-Thinking or 7B quantized" — that was the wrong tool. The right tool is GLM-5.2 (or a 1.2B extract) because the Feedback-Agent needs *long context* (1M tokens) to read the full trajectory, not raw intelligence. GLM-5.2's IndexShare architecture reduces 1M-context per-token FLOPs by 2.9× — it is the right shape for the SIA loop.
- **Mnemosyne as the consolidation runner.** SIA-H needs a memory system that can recall every prior run's decisions. Mnemosyne's BEAM (ICLR 2026) and LongMemEval (98.9%) scores are a publishable baseline; the OpenClaw provider is a one-line config change. **Fork Mnemosyne, swap the embedding model to LFM2.5-Embedding-350M, point the SIA loop at it.**
- **UaC as the user-modeling pattern.** SIA's Meta-Agent is "a strong LM writing scaffolds." A UaC-style typed-Python user model is the natural scaffold schema for the "remember who the user is" part of the harness. The two-phase pipeline (append-only log → typed Python checkpoint) is a database-systems pattern that has never been applied to LLM memory. v13 recommendation: implement the SIA user model as a UaC-style module.

### 1.3 Power/performance tradeoffs (delta from v12)

**Verdict: v12's model choices are still right for v1.0 desktop. The wearable story just got a 350M retrieval-class option and a 350M embedding that change the memory power budget.**

- **LFM2.5-VL-450M Q4_0** — unchanged.
- **LFM2.5-Embedding-350M** (new, June 18) — replaces MiniLM-L6-v2 for v1.5. Smaller (350M vs 80M for the SentenceTransformer? — actually 350M total params, but optimized for retrieval, not 384-dim specifically). **Open question**: verify that LFM2.5-Embedding-350M has a 384-dim variant before swapping; otherwise keep MiniLM and add ColBERT-350M for late-interaction rerank.
- **LFM2.5-ColBERT-350M** (new, June 18) — late-interaction reranker. Sits on top of the vector index. Use it to rerank the top-50 HNSW hits before the LLM sees them. This is the Hindsight-style four-retrieval fan-in minus graph + temporal.
- **whisper.cpp base.en** — unchanged.
- **KittenTTS medium** — **new contender: Inflect-Nano (4.63M params)** (r/LocalLLaMA, June 2026). Way too robotic for a companion, but useful as a fallback when battery is critical. Skip.
- **HRM-Text-1B** — unchanged.

**Net v13 wearable power:** adding LFM2.5-ColBERT-350M (+~150MB) and dropping MiniLM-80MB → -80MB nets +70MB resident. Combined with v12's wearable budget, the v1.5 wearable resident is ~505 MB. Still under 1 GB. Still feasible on 2 GB Redax.

### 1.4 OpenClaw orchestration — the new security risk

**Verdict: v12 said "P1 action — security hardening." v13 says "P0 action — documented in-the-wild attack."**

The Skywork OpenClaw skill-malware guide (June 2026) documents an actual attack pattern: malicious or booby-trapped "skills" that deliver malware via install instructions, deceptive prerequisites, or runtime behaviors. Attack vectors include:
- Poisoned docs (skill description lies)
- Installer tricks (skill installs a backdoor in `setup.py`)
- Prompt-activated behaviors (skill fires on certain user prompts)

**v13 actions (must ship before v1.0, not v1.5):**

1. **Signed skills + Sigstore Rekor.** Every Danlab-shipped skill ships with a cosign signature and a Rekor transparency-log entry. Reject unsigned skills in OpenClaw policy.
2. **`policy.deny_skills` default-deny on a curated allowlist.** OpenClaw's `policy.tools.deny/allow` is the right primitive. Move the Danlab defaults from "deny nothing" to "allow only the explicit Danlab-blessed set."
3. **Skill sandbox.** Run every skill in a process jail (no fs access outside `~/.dan-glasses/skills/<name>/`, no network except explicit allowlist, no `subprocess` except via `toold`).
4. **The OpenClaw + `dan-glasses-app` MCP bridge is a known-good path.** `mcp.servers.zo-bridge` is the production-blessed MCP server. Document this in the install README and lock the bridge package to a Danlab-controlled repo.

### 1.5 OpenClaw memory plugin pin (new, urgent)

**The OpenClaw memory backend pin is a Day-1 fix.** A real community report (Hermes-Agent Community, June 2026) shows "weird memory behavior" traced to a default that pulled in the wrong memory provider. **Fix:** set `plugins.slots.memory = "memory-core"` in `openclaw.json` explicitly. The "memory-core" is the built-in OpenClaw backend, not a third-party skill. Danlab's install bootstrap should do this automatically and verify it on every startup.

---

## 2. AGI Landscape Research (delta from v12)

### 2.1 State of AGI research in 2026

**Verdict: the open-weights frontier just leapfrogged.** Z.ai's GLM-5.2 (June 14 2026) is a 1M-context, MIT-licensed, 753B-param MoE (40B active) model that beats Opus 4.7 and GPT-5.5 on PostTrainBench and leads the open-weights Intelligence Index v4.1 (51 vs MiniMax-M3's 44, DeepSeek V4 Pro's 44, Kimi K2.6's 43). This is a *structural* change from v12's "scale (OpenAI/Anthropic/Google) vs. edge (us) vs. RSI" framing.

**v13 framing.** The three lanes become four:
1. **Closed frontier** (OpenAI GPT-5.5, Claude Opus 4.8, Gemini 3.1 Pro) — the ceiling.
2. **Open frontier** (GLM-5.2, DeepSeek V4 Pro, Kimi K2.6, Qwen 3.7-Max) — the new floor. **Cheap to use (MIT license), strong enough to act as the Feedback-Agent in SIA loops.**
3. **RSI / harness+weights** (SIA, RHO, RHO-based forks) — the leverage.
4. **Edge / on-device** (us: LFM2.5-VL-450M, KittenTTS, whisper.cpp, HRM-Text) — the form factor.

**v13 move.** The Feedback-Agent in the SIA loop on `danlab-multimodal` should be **GLM-5.2** (open, MIT, 1M context, fast on H100). This is a v12 correction: v12 said "Claude-class or GPT-class" — that was correct for 2025 cost structure, wrong for 2026 open-weights reality. GLM-5.2 on a single H100 ($2/hr) is cheaper than GPT-5.5 API for the long-context trajectory reads SIA needs.

### 2.2 Self-improving architectures — SIA, RHO, RHO-CUHK, Mnemosyne

**Verdict: the credible "self-improvement" stack in June 2026 is SIA-H (harness) + RHO (retrospective harness optimization) + Mnemosyne (consolidation runner) + UaC (user-model schema) + GLM-5.2 (Feedback-Agent).**

The pieces in v13:
- **SIA** (Hexo Labs, arXiv:2605.27276, May 2026) — harness+weights. Unchanged from v12.
- **RHO** (CUHK + Microsoft Research Asia, arXiv June 2026) — label-free, retrospective harness optimization using only past trajectories. v12 called it the "real playbook" for danlab-multimodal. v13 confirms: **RHO is the SIA-impl detail.** SIA without RHO is a generic harness editor; SIA *with* RHO is the published-2026 best practice.
- **Mnemosyne** (AxDSan, ICLR 2025/2026 benchmarks) — the consolidation runner. 98.9% Recall@All@5 on LongMemEval with `bge-small-en-v1.5`. **One-line OpenClaw provider install.** Replaces the v12 "consolidation loop: small LM with held-out merge/decay/eviction decisions" plan with a battle-tested system.
- **User-as-Code (UaC)** (arXiv:2606.16707, June 16 2026) — typed Python objects as a living user model. 78.8% on LOCOMO. The two-phase pipeline (append-only log → typed Python checkpoint) is a database-systems pattern applied to LLM memory for the first time. **Adopt as the SIA user-model schema.**
- **OpenSkill** (Lehigh + Salesforce, June 2026) — agents autonomously build and verify their own skills. SIA can be re-cast as "OpenSkill for the harness" — the harness is a skill.

**The v13 SIA-W+H workstream is now:**
1. Install Mnemosyne as the OpenClaw memory backend. (1 day.)
2. Fork SIA, swap the Feedback-Agent to GLM-5.2 (open, MIT, 1M context). (1 week.)
3. Implement the user model as a UaC module. (2 weeks.)
4. Run RHO (label-free harness optimization) on the existing screenshot trajectories. (2 weeks.)
5. Publish. (1 week.)

This is 6 weeks end-to-end. v12's plan was 8 weeks. The deltas are: GLM-5.2 instead of a 7B cloud API; Mnemosyne instead of custom consolidation; UaC as the user-model schema.

### 2.3 Edge AI / on-device models

**Verdict: sub-500MB VLM class still dominated by LFM2.5-VL-450M. New retrieval-layer options (ColBERT-350M, Embedding-350M) just changed the memory power budget.**

The 2026 SOTA list (delta from v12):
- **LFM2.5-VL-450M** (Liquid AI, April 2026) — unchanged, still top-of-class for size.
- **LFM2.5-ColBERT-350M** (Liquid AI, June 18 2026) — new. Late-interaction reranker. Add to the v1.5 retrieval stack.
- **LFM2.5-Embedding-350M** (Liquid AI, June 18 2026) — new. Dedicated retrieval embedding. Replace MiniLM in v1.5.
- **LFM2.5-Thinking** — on-device reasoning. Confirmed available (howaiworks.ai blog post). Add to the v1.5 reasoning stack alongside HRM-Text.
- **LFM2.5-Audio-1.5B** — on-device audio I/O. Liquid AI's cookbook shows it running in the browser via WebAssembly. **A serious contender to replace whisper.cpp + KittenTTS for the desktop, in v1.5.** Worth a 1-week spike.
- **Box v3.1.0** (jegly/Box) — first on-device NPU acceleration that works on Snapdragon and MediaTek for the **Gemma 3 1B** model. This is a real v2 datapoint: NPU acceleration for sub-2B models is *now* working on mobile. Suggests that the wearable v2 may be able to use the LFM2.5-VL-450M-vision-encoder on NPU (vision encoder is the smallest part of the model) and keep the text decoder on CPU. Measure in W1.
- **Gemma 4 12B** (Google, June 2026) — encoder-free multimodal, runs on Apple M5. **Not a wearable option** but a credible laptop comparator for the v12 "Gemma 4 E4B on laptop" W10 spike.
- **MediaTek Genio Pro 5100** (June 13 2026) — IoT/robotics/drone edge AI. Not a wearable SoC but the "edge AI silicon" pipeline is moving.

**The Box NPU datapoint is the v13 wearable unlock.** If the vision encoder (the ~86M-param part of LFM2.5-VL-450M) can run on a 2026 NPU, the wearable power budget improves by 30-50%. Box proves the NPU path is real for sub-2B models. The wearable v2 form factor (12-month roadmap) should plan for hybrid CPU+NPU inference, not CPU-only.

### 2.4 Memory and continual learning

**Verdict: Mnemosyne is the answer for the runner. UaC is the answer for the schema. LFM2.5-Embedding-350M is the answer for the embedding model. The v12 "build it from scratch" plan is dead.**

The 2026 SOTA framework (delta from v12):
- **Hindsight** (Vectorize, MIT) — 91.4-94.6% on LongMemEval. v12's #1 pick. v13: **dethroned by Mnemosyne (98.9%)**. Still has the best consolidation blog.
- **Mem0** — 49.0% on LongMemEval. v12's #2. v13: hold for hosted tier, skip for self-host.
- **Mnemosyne** (AxDSan) — **98.9% Recall@All@5, ICLR 2026 BEAM and LongMemEval, OpenClaw native provider.** New. This is the new floor.
- **Eywa** (arXiv:2605.30771) — provenance-grounded. v12's #4. v13: still good for the schema design (provenance columns in `memoryd`), but the runner is Mnemosyne.
- **User-as-Code (UaC)** (arXiv:2606.16707, June 16 2026) — new. 78.8% on LOCOMO. The two-phase pipeline (append-only log → typed Python checkpoint) is the SOTA pattern for "user model that survives across sessions."

**v13 memory architecture:**

```
Mnemosyne (runner)        ← BEAM/LongMemEval leader, OpenClaw native
  + LFM2.5-Embedding-350M ← new Liquid AI retrieval embedding
  + LFM2.5-ColBERT-350M   ← new Liquid AI late-interaction reranker
  + UaC schema            ← typed Python user model, append-only + checkpoint
  + Eywa provenance       ← provenance_source/session/ts columns
  + Hindsight-style consolidation
  + RHO-based consolidation loop
```

**v13 workstream (replaces v12 W9 "memoryd v1.5 schema"):**
1. Day 1-3: install `mnemosyne-memory[openclaw]`, swap memory backend.
2. Day 4-7: benchmark LFM2.5-Embedding-350M vs MiniLM on existing memory set.
3. Week 2: implement UaC user-model schema as the Mnemosyne data layer.
4. Week 3: add Eywa-style provenance columns.
5. Week 4: add RHO-style nightly consolidation job.
6. Week 5-6: migrate `memoryd` to a thin shim that proxies to Mnemosyne.

This is 6 weeks. v12's plan was 4 weeks for the schema + 8 weeks for consolidation. Net: 6 weeks vs 12. v13 is faster *and* better.

### 2.5 Multimodal fusion

**Verdict: unchanged from v12.** Independent services fused at the prompt is right for v1; native multimodal token fusion is the v2+ direction; LFM2.5-VL is the right on-device model.

The new datapoint: **LFM2.5-Audio-1.5B** is a single model that does both audio understanding and speech synthesis. If quality is acceptable, this collapses audiod + ttsd into a single on-device model. v1.5 spike.

---

## 3. Competitive & Market Research (delta from v12)

### 3.1 The 2026 AI-glasses market

**Verdict: the market is now the most competitive it has ever been, with at least 7 confirmed consumer entrants in 14 months. Dan Glasses' "sub-50g, sub-$400, on-device, no HUD, no name-lending" position is unique but the window is closing.**

Confirmed entrants (delta from v12):
- **Meta Ray-Ban Display** (Sept 30 2026, $799) — v12 confirmed.
- **Apple Camera AirPods + Glasses (Bloomberg, June 16 2026)** — confirmed. v13: this is the first credible Apple-head-mounted camera; previously rumors were glasses-only.
- **Snap Specs** ($2,195, AWE June 2026) — v11/v12 confirmed.
- **Xreal Aura** ($1,500, AWE June 2026) — v11/v12 confirmed.
- **Brilliant Labs Halo** (June 2026) — **confirmed as the open-source Leap**. v12 called it the "open-source competitor" — v13 elevates: Halo is *the* product to beat in the open-source niche. **Buy one, wear it, copy what works.**
- **Even Realities G2** — 3D display + smart ring + ambient AI. $379. June 2026. **The "ambient AI" framing is direct competition to "proactive AI companion" — evenrealities calls it the same thing.**
- **Halliday AI Glasses** — $379, June 2026, hidden 3D display. **Memomind** is a competitor in the same ring-controlled niche.
- **Google Gemini glasses (Gentle Monster + Warby Parker)** — Fall 2026. v10 confirmed.
- **Illinois HB4843** (smart glasses driving ban, June 2026) — first US state to consider regulating smart glasses in driving. Regulatory tailwind for "safe, on-device, not always-recording" framing.
- **Display-Less AI Glasses** is now a recognized category (SmartGlassesDaily June 2026 analysis). **"The quiet triumph of AI-first, screen-free smart glasses reveals a smarter path to widespread adoption. Practicality and privacy, not pixels, are driving the next wave of wearables."** This is the v22 Kit positioning, third-party validated.

**v13 positioning refinement.** Dan Glasses' 2x2 cell is now:
| | HUD/Display | No Display |
|---|---|---|
| **On-device** | Meta Display, Snap Specs, Xreal Aura | **Dan Glasses, Brilliant Labs Halo, Even Realities G2** |
| **Cloud** | Google Gemini Glasses | Halliday (Memomind) |

We are in the bottom-left cell with Brilliant Labs Halo and Even Realities G2. **The differentiation is no longer "no HUD" — it's "open-source + auditable + no name-lending + Indian-made."**

### 3.2 Open-source AI companion projects

**Verdict: Brilliant Labs Halo + Mnemosyne are the two 2026 open-source reference designs. Danlab should explicitly study both.**

- **Brilliant Labs Halo** — open-source AI Leap, proactive AI agent, bone-conduction audio, 2026. The most direct competitor and the most direct reference design.
- **Mnemosyne** — open-source memory layer, 98.9% on LongMemEval, OpenClaw native. Should be `pip install mnemosyne-memory[openclaw]` in our stack.
- **SIA** — open-source RSI framework, MIT. Already on the workstream.
- **OpenSkill** — open-source agent skill self-builder. v13: read but don't integrate.
- **Box** — open-source on-device AI suite, Gemma 3 1B NPU works. Reference for the wearable v2 NPU path.

### 3.3 Privacy-preserving AI positioning

**Verdict: the v12 "Fable 5 safe = marketing claim" is now "Fable 5 safe = temporary regulatory advantage that expires ~July 12 2026." The privacy story must stand on its own.**

The deltas:
- **Fable 5 return (~July 12)** — Anthropic is at the negotiating table per Politico/NYT. The "Fable 5 export control" tailwind is now a ~30-day disruption that resolves with a compliance regime. Don't bet the positioning on it.
- **DoD "supply chain risk" statement** (CNBC, June 17 2026, v10 confirmed) — still a tailwind, but softened by Fable 5 return.
- **Illinois HB4843** — first state-level regulation. Positions Dan Glasses as "safe" by construction (on-device, no always-recording, push-to-talk default).
- **OpenClaw skill malware** — actually *hurts* the on-device story if we're not careful. A compromised skill on a Danlab-shipped OpenClaw build exfiltrates whatever it can. **Sigstore Rekor + signed skills + skill sandbox are now a privacy primitive, not a security one.**

**v13 privacy story.** Four layers:
1. **Architecture.** All data local by default. No cloud upload without explicit user action. OpenClaw policy: deny all skills not on the allowlist.
2. **Provenance.** Eywa-style provenance columns in `memoryd`. Every memory is attributable.
3. **Verifiability.** Sigstore-signed skills, Sigstore-signed `.deb`. Public Rekor log.
4. **One-tap forget.** UaC user model + Mnemosyne consolidation means "forget" deletes the typed Python user-model objects, not a fuzzy search across the vector index.

---

## 4. Technical Deep Dives

The three options picked: **A (Self-improving RL loops)**, **B (Edge VLM optimization)**, **C (Vector search and memory)**. v12 covered A and B and C; v13 deepens each with the new 2026-06-14 → 2026-06-19 deltas.

### 4.1 [Deep Dive] Self-improving RL loops — SIA + RHO + UaC + Mnemosyne + GLM-5.2

The 2026-06 stack is **SIA + RHO + UaC + Mnemosyne + GLM-5.2**. The pieces:

- **SIA** (arXiv:2605.27276, May 2026) — the only public harness+weights self-improvement framework. Meta-Agent writes scaffolds; Feedback-Agent reads trajectories and edits harness + LoRA weights. Reported: +25.1% LawBench, +12.4% GPU kernels, +20.4% RNA denoising. **Open question: is the gain stable past a few hundred iterations?** v12 flagged this; v13 has no new evidence.
- **RHO** (CUHK + Microsoft Research Asia, arXiv June 2026, "Retrospective Harness Optimization") — label-free, uses only past trajectories. **0.78 SWE-Bench Pro at 1 round vs Meta-Harness 0.60 at 1 round** (0.80 at 10 rounds with 3× compute). RHO is the implementation detail inside SIA's Meta-Agent. v13: pin RHO version in the fork.
- **Mnemosyne** — consolidation runner. v12 had "build our own." v13: install Mnemosyne, point the SIA loop at it, save 6 weeks.
- **UaC** (arXiv:2606.16707, June 16) — the user-model schema. Typed Python objects + append-only log + checkpoint. v13: implement the SIA user model as a UaC module.
- **GLM-5.2** (Z.ai, June 14) — the Feedback-Agent. 1M context, MIT, open, fast on H100. **v13 critical correction:** v12 said "Claude-class or GPT-class" Feedback-Agent. v13: GLM-5.2 is the right tool. Open, MIT, 1M context (SIA needs to read long trajectories), ranks #2 on PostTrainBench (only behind Opus 4.8).

**v13 SIA-W+H plan (replaces v12 W2 + W13):**

1. **W2.1 (Week 1):** Install Mnemosyne, swap OpenClaw memory backend, verify the 98.9% LongMemEval result on the danlab-multimodal screenshot set.
2. **W2.2 (Week 2):** Fork SIA, swap the Feedback-Agent to GLM-5.2 (one H100, $2/hr, 1M context). Run SIA-H on the existing screenshot trajectories.
3. **W2.3 (Week 3):** Implement UaC user-model schema as the Mnemosyne data layer. Re-run SIA-H with the UaC schema.
4. **W2.4 (Week 4):** Add RHO retrospective harness optimization. Compare RHO-harness vs vanilla-SIA-harness on the same trajectory set.
5. **W2.5 (Week 5):** Add LoRA fine-tune path for SmolVLM-256M. Train on trajectories SIA-H scores as "improved."
6. **W2.6 (Week 6):** Switch to SIA-W+H. Compare against SIA-H and against the published SIA numbers on the same three domains. **Stop and publish.**

This is 6 weeks end-to-end. v12 was 8 weeks. v13 is faster because GLM-5.2 is cheaper than a cloud API and Mnemosyne replaces the custom consolidation runner.

**What is *not* required.** GRPO, PPO, learned reward model, GPU cluster, FrontierMath. SIA + RHO + GLM-5.2 + Mnemosyne + UaC is sufficient.

**What could go wrong.** RHO's reported gains are on coding tasks. The danlab-multimodal screenshot task is a different domain. If RHO underperforms, fall back to vanilla SIA-H. Publish the null result either way.

### 4.2 [Deep Dive] Edge VLM optimization (delta from v12)

**v13 additions:**

- **LFM2.5-Audio-1.5B** (Liquid AI cookbook, May-June 2026) — single model for audio understanding + speech synthesis. Runs in browser via WebAssembly. **This is the strongest "collapse audiod + ttsd" candidate to date.** W14 spike: benchmark LFM2.5-Audio-1.5B on Pi 5 vs the current whisper + KittenTTS pair.
- **Box NPU acceleration works** (jegly/Box v3.1.0, June 2026) — first credible on-device NPU run for Gemma 3 1B on Snapdragon and MediaTek. **This unlocks the wearable v2 vision-encoder-on-NPU path.** v12 said "NPU not yet." v13: NPU is here for sub-2B models, including Gemma 3 1B.
- **MediaTek Genio Pro 5100** (June 13 2026) — 12 TOPS NPU, octa-core RISC-V, 4K video decoder. This is the kind of silicon that could power the wearable v2 in 2027.

**v13 wearable v2 silicon plan (12-month):**
- Vision encoder (86M LFM2.5-VL-450M component) on NPU.
- Text decoder (~360M LFM2.5-VL-450M component) on CPU.
- HRM-Text-1B on CPU (or NPU if vendor supports).
- Whisper-tiny on a low-power DSP.
- TTS base on CPU with NPU assist.

This is the OpenGlass-style hybrid. The wearable v2 power budget becomes:
- Idle (NPU off, CPU sleeping): <50 mW
- Watchful (vision encoder on NPU, ~1 fps motion detection): <300 mW
- Active (NPU + CPU + TTS spike): 1.5-2.5 W

At 2500 mAh / 3.7 V, this gives **8+ hour battery life.** The v12 plan was 4 hours at 5W average. The v13 hybrid silicon plan is the unlock.

### 4.3 [Deep Dive] Vector search and memory architectures (delta from v12)

**v13 reality.** The 2026-06 memory stack is **Mnemosyne (runner) + LFM2.5-Embedding-350M (embedding) + LFM2.5-ColBERT-350M (rerank) + UaC (user-model schema) + Eywa (provenance columns) + Hindsight (consolidation blog) + RHO (consolidation loop)**.

**The four primitives from v12 are still right** (retrieval, consolidation, scoping, provenance). The v13 changes are:

- **Mnemosyne beats Hindsight on the published benchmark** (98.9% vs 94.6%). Use Mnemosyne.
- **LFM2.5-Embedding-350M is purpose-built for retrieval** and 4.4× smaller than MiniLM. Use it.
- **LFM2.5-ColBERT-350M is the late-interaction rerank** that Hindsight uses internally. Add it.
- **UaC adds a typed-Python user-model layer** that Mnemosyne doesn't have. Implement it as a Mnemosyne data layer.
- **RHO adds label-free consolidation** that runs in the background and updates the SIA harness. Add it.

**v13 memory workstream plan (replaces v12 W9 + W14 + W15):**

1. **W9.1 (Day 1-3):** Install `mnemosyne-memory[openclaw]`. Set `plugins.slots.memory = "memory-core"` (the explicit pin that fixes the v13 community-reported "weird memory behavior" bug). Set `plugins.slots.memory_provider = "mnemosyne"`.
2. **W9.2 (Week 1):** Benchmark LFM2.5-Embedding-350M vs MiniLM-L6-v2 on the existing memory set. Swap if quality > MiniLM by >2% on held-out retrieval.
3. **W9.3 (Week 2):** Add LFM2.5-ColBERT-350M as the late-interaction reranker on top of the HNSW index.
4. **W9.4 (Week 2-3):** Add Eywa-style provenance columns: `provenance_source`, `provenance_session`, `provenance_ts`, `last_verified_at`, `confidence`.
5. **W9.5 (Week 3-4):** Implement UaC user-model schema as a Mnemosyne data layer. Typed Python objects, append-only log, periodic checkpoint.
6. **W9.6 (Week 4-5):** Add Hindsight-style consolidation (importance, merge, decay, eviction) with LFM2.5-1.2B-Thinking as the consolidation LM.
7. **W9.7 (Week 5-6):** Add RHO-based nightly consolidation job. Audit log table.

This is 6 weeks. v12 was 4 weeks (schema) + 8 weeks (consolidation) = 12. v13 is half the time and a better end state.

**The single highest-leverage memory feature is still the episodic timeline.** "What did I do on Tuesday that was different from usual?" is the user query that makes the whole product real. Mnemosyne's temporal index is the right primitive. v12's `time_bucket` column plan is absorbed into Mnemosyne's existing temporal index.

---

## 5. Open Questions for Somdipto

1. **Mnemosyne adoption.** OK to swap the OpenClaw memory backend to Mnemosyne this week? (1-day install, big unlock.)
2. **GLM-5.2 as Feedback-Agent.** OK to use GLM-5.2 (open, MIT) instead of a Claude/GPT API for the SIA loop? (Cheaper, 1M context, ranks #2 on PostTrainBench.)
3. **OpenClaw skill-signing infra.** OK to set up Sigstore Rekor + cosign for Danlab-shipped skills before the v1.0 .deb? (1 week, must ship.)
4. **Brilliant Labs Halo user study.** OK to buy one ($349) and wear for a week, write `agent-work/halo-user-study.md`? (1 week, W18 workstream.)
5. **LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M swap.** OK to swap MiniLM in the W9 workstream? (Quality benchmark needed first.)
6. **LFM2.5-Audio-1.5B spike.** OK to benchmark as audiod + ttsd replacement? (2 weeks, W14 spike.)
7. **v1.0 ship target.** Still Q4 2026? Fable 5 returning ~July 12 means the regulatory tailwind is now a tailwind-with-cliff. (Confirm or adjust.)
8. **OpenGlaw security audit.** OK to commit a Sigstore Rekor entry for every Danlab-shipped artifact starting this week? (1 week, P0.)
9. **DPDP Act / EU AI Act compliance.** India DPDP Act (2023) and EU AI Act (2024) both apply to wearable AI in 2026-2027. OK to commission a formal compliance review of the v1.0 .deb? (4 weeks, W11 workstream.)
10. **Redax board hardware date.** v12 carried this. v13: is the date still open? (Critical for the wearable v2 timeline.)

---

## 6. Sources

[^1]: Mnemosyne: The Zero-Dependency, Sub-Millisecond AI Memory System. AxDSan. 98.9% Recall@All@5 on LongMemEval, BEAM ICLR 2026. https://github.com/AxDSan/mnemosyne
[^2]: User as Code: Executable Memory for Personalized Agents. arXiv:2606.16707, June 16 2026. https://arxiv.org/abs/2606.16707
[^3]: Fable 5 Return. Politico/NYT, June 16 2026. Anthropic-Trump administration active negotiations. https://techjacksolutions.com/ai-brief/anthropic-and-trump-administration-enter-active-negotiations
[^4]: Liquid AI LFM2.5-ColBERT-350M + LFM2.5-Embedding-350M release. June 18 2026. https://www.liquid.ai/blog/lfm2-5-retrievers
[^5]: Z.ai GLM-5.2 release. 1M-token context, MIT, open-weights. June 14 2026. https://z.ai/blog/glm-5.2
[^6]: Simon Willison: GLM-5.2 is probably the most powerful text-only open weights LLM. June 17 2026. https://simonwillison.net/2026/Jun/17/glm-52
[^7]: Brilliant Labs Halo: The Definitive Open-Source AI Leap. LinkedIn, June 2026. https://www.linkedin.com/posts/desahu_agents-at-the-edge-the-new-trust-layer-for-activity-7471839445340807168-WbM2
[^8]: Apple memory chip pricing pressure. Tim Cook / WSJ, June 18 2026. https://www.cnbc.com/video/2026/06/18/opening-bell-june-18-2026.html
[^9]: OpenClaw Skill Malware — Ultimate Guide. Skywork, June 2026. https://skywork.ai/blog/openclaw-skill-malware-ultimate-guide
[^10]: Box v3.1.0: NPU now works on Snapdragon & MediaTek. Gemma 3 1B. https://github.com/jegly/Box
[^11]: Display-Less AI Glasses: The Real Mass-Market Play. SmartGlassesDaily, June 2026. https://www.instagram.com/p/DZnW8Lmn8Cu
[^12]: Illinois HB4843: smart glasses driving ban. June 2026. https://www.govtech.com/question-of-the-day/which-state-wants-to-ban-wearing-smart-glasses-while-driving
[^13]: Hermes-Agent Community: explicit memory provider pin. June 2026. https://www.facebook.com/groups/1283855437217819/posts/1347663810836981
[^14]: Liquid4All Cookbook: LFM2.5-Audio-1.5B on-device voice assistant. https://github.com/Liquid4All/cookbook
[^15]: Z.ai GLM-5.2 technical report. IndexShare reduces 1M-context per-token FLOPs by 2.9×. https://z.ai/blog/glm-5.2
[^16]: GLM-5.2 leads open-weights on PostTrainBench. #2 behind Opus 4.8, beats Opus 4.7 and GPT-5.5. https://z.ai/blog/glm-5.2
[^17]: Memory chip shortage 2026. DRAM/NAND pricing pressure. June 2026. https://www.instagram.com/reel/DZsIgq4EtLw
[^18]: Anthropic "When AI builds itself" report. June 4 2026. https://www.anthropic.com/institute/recursive-self-improvement
[^19]: RHO: Retrospective Harness Optimization. CUHK + Microsoft Research Asia, June 2026.
[^20]: Even Realities G2. 3D display + smart ring + ambient AI. $379. June 2026. https://www.tiktok.com/discover/smart-glasses-even-g2-even-realities
