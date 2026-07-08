# Dan2 Research Report v8 — Sakana RSI Lab, Perplexity Brain, the Self-Improvement Wall, and the New Competitive Geometry

**Author:** Dan2 (Research Agent) | **Date:** 2026-06-25 07:35 IST (02:05 UTC)
**Status:** v8 — supersedes v7
**Live infrastructure verified this run:** 8/8 daemons live (audiod 8090 / perceptiond 8092 / memoryd 8741 / toold 8742 / ttsd 8743 / os-toold 8744 / openclaw 18789 / dan-glasses-app 8747), Tauri SPA published, OpenClaw gateway on 18789, Telegram bot `@danlab_bot` paired.
**Companion artifacts:** `dan2-agi-roadmap.v8.md`, `dan2-architecture-review.v8.md`, `dan2-model-analysis.v8.md`, `dan2-papers-to-read.v8.md`.

> **v8 north star (one sentence):** The same auditable, harness-evolved, calibration-first thesis from v7 holds — but v8 sharpens the *boundary condition* (Sakana's RSI Lab and Perplexity's Brain have both validated the architecture from the outside; the AI Weekly "self-improvement wall" finding is the missing failure-mode constraint that locks the audiod RL agent design); and the *competitive geometry has shifted* — Meta Ray-Ban Display at $799 with Neural Band EMG + Ray-Ban Gen 2 at $379 have created a 2-tier market that Danlab cannot out-hardware, so the v8 moat must be *wearable-shaped privacy + auditable reliability + India-cost + on-device-first*, anchored by an auditable calibration RL harness that no closed competitor can replicate.

---

## v7 → v8 — what changed and why

Six concrete updates grounded in late-June 2026 evidence that v7 did not yet have:

1. **Sakana AI RSI Lab formally launched (June 7, 2026).** Sakana — co-founded by Llion Jones, David Ha, Ren Ito — opened a dedicated Recursive Self-Improvement Lab betting that AI that improves itself can break the compute arms race. Lineage: LLM² (automated preference-optimization discovery), Darwin Gödel Machine (SWE-bench Verified 20% → 50%, Polyglot 14.2% → 30.7% after 80 iterations, Nature-published AI Scientist March 26 2026), ShinkaEvolve (sample-efficient evolutionary optimization), ALE-Agent, Digital Red Queen (open-ended adversarial coevolution). **The audiod calibration RL agent thesis from v7 is now externally validated by the leading RSI lab on the planet.** Danlab's auditable harness-evolution design is in good company — and Sakana's *sample-efficient* framing tells us: don't compete on scale, compete on measurable per-step improvement.
2. **Perplexity Brain launched June 18, 2026 — the first production validation of memoryd v2's design thesis.** Brain is a self-improving memory system for the Computer agent. It remembers *what the agent did*, not who the user is. It builds a **traceable context graph** of work sessions (sessions, connector results, doc changes, corrections); overnight it **synthesizes the graph into an "LLM wiki"** that loads into the agent sandbox before the next task. Every memory links back to its source — auditable. **Early numbers: +25% correctness on seen-before tasks, +16% recall, −13% cost on historical-context tasks.** This is precisely the architecture v7 specified for memoryd v2 (AEL + DPCM + LLM-Wiki + operative_context + audit trail), deployed at production scale by a competitor with no obligation to share learnings. **v8 closes the architectural question: ship this, ship it now, and beat Perplexity to "open-source + auditable + wearable-shaped" memoryd v2.**
3. **AI Weekly "self-improvement wall" (June 2026) is the v8 failure-mode constraint.** 1,000+ experiments showed agents successfully propose *one* structural harness improvement but cannot compound it in later iterations. Root cause: agents lack a self-model that explains why the first modification worked. **Implication for audiod calibration RL agent:** harness-evolution alone is insufficient. The harness needs a *self-model* — an explicit, auditable artifact that explains why a given harness revision was kept. **memoryd v2's operative_context surface + failure-mode registry are exactly this self-model.** v8 makes the audiod RL agent write every harness revision's rationale to memoryd's operative context stream, so the next iteration can reason over *why previous iterations worked*. This closes the AI Weekly wall.
4. **Meta Connect 2025 → Meta Ray-Ban Display at $799 with Neural Band EMG.** $799 glasses + 18-hour Neural Band EMG wristband (IPX7), in-lens 600×600 px display, 6h mixed-use battery (30h with case), launch Sept 30 2025 in select US stores, expanding Canada/France/Italy/UK early 2026. Ray-Ban Gen 2 launched at $379, Oakley Meta Vanguard (sports). 2 million pairs of Meta smart glasses sold since 2023. **This is the new $379–$799 anchor in the smart-glasses market, with hardware (EMG) + display + always-on cloud AI.** Even Realities G2 ($599, no camera, waveguide display, on-device Conversate) remains the closest "privacy-first / on-device" competitor. Danlab cannot beat Meta on EMG hardware or display scale. v8 must defend on the axes they cannot: auditable on-device inference, India-cost, open-source, wearable-shaped privacy, and *auditable reliability surface per service*.
5. **Even Realities G2 is now the de facto reference competitor.** PCMag Middle East 2026 review: "one of the lightest and thinnest pairs of smart glasses I've seen," waveguide display, optional smart ring accessory, on-device Conversate AI assistant (not yet rated "helpful"), $599 price tag unchanged from G1. IP rating revised IP67 → IP65 for mass-production consistency. **G2's position: privacy-first, no camera, on-device AI, no cloud retention, prescription-friendly, ±12 diopter display.** Danlab's v8 positioning is "G2-shape + open-source + auditable reliability + ₹4,999 student tier + India-cost." **The G2 is what we are not competing with on hardware — and what we ARE competing with on philosophy.**
6. **LoRA/QLoRA + SLM LoRA-tuning pipeline is the v8 PEFT default.** Techbytes 2026 dev guide: instruction-tuning + LoRA + post-training quantization on Llama-3.2-1B or Qwen2.5-1.5B. S-LoRA achieves 4× higher throughput, thousands of concurrent adapters, near-linear GPU scaling. **For Danlab's audiod RL agent (which targets a frozen whisper.cpp base.en encoder with a 4-layer MLP calibration head), LoRA is irrelevant. For Danlab's dani-skills library (where 50+ agent skills can be LoRA-tuned to a shared small base), LoRA is the path.** EigenLoRAx + LoRA-Edge (TT-SVD) reduce trainable params by 2 orders of magnitude — fits federated on-device memoryd v2 fine-tuning.

The headline shift: **v7 said "auditable reliability is the moat." v8 says "auditable reliability + self-model + open-source LLM-wiki memory + India-cost positioning against Meta $379–$799 + EMG hardware moat is the moat."** The thesis sharpens; the bets tighten.

---

## Executive summary — the v8 thesis

1. **Auditable reliability + harness evolution + self-model = the only Danlab-shape moat.** Sakana's RSI Lab has validated harness-evolution as a compute-efficient RSI path. Perplexity's Brain has validated traceable-context-graph + LLM-wiki memory in production. AI Weekly's "self-improvement wall" tells us the missing piece is an explicit self-model. **memoryd v2's operative_context surface IS the self-model.** v8 ships audiod RL agent + memoryd v2 as one coupled artifact.
2. **Edge VLM has crossed a threshold — keep LFM2.5-VL-450M, add CondenseVLM/QViD/V5e-0 stack, consider OmniVLM-968M only if hardware supports it.** v7 conclusion unchanged in v8. The token-pruning + speculative-decoding stack is the highest-ROI move; base-model swap is now table-stakes.
3. **Memory is engineering, not research, post-Perplexity Brain.** Perplexity has shipped the architecture at production scale with measured +25% / +16% / −13% results. memoryd v2 (AEL + DPCM + LLM-Wiki + operative_context + audit trail + self-model) is the Danlab implementation of the same pattern. **v8 changes the timeline: ship memoryd v2 in 6 weeks, not 8.** The architectural question is closed; the work is shipping.
4. **TTS consolidates to Kokoro-82M.** v7 conclusion unchanged. Apache 2.0, 82M params, 54 voices, 8 languages (Hindi native), 92MB quantized variant, sub-20ms TTFA warm. KittenTTS swap is a 1-week decision.
5. **Smart-glasses is now a 4-tier market: Meta ($379–$799, EMG, display, cloud AI, 2M sold), Even Realities ($599, no camera, waveguide, on-device), Snap Spectacles ($2,195 dev kit, 132-136g), Solos AirGo Vision (displayless, on-device AI). Apple 2027+. Microsoft Scout (Build 2026, OpenClaw-based).** Danlab competes on the *fifth axis*: auditable reliability + open-source + wearable-shaped privacy + India-cost + auditable calibration RL. None of the 4 tiers ship this.
6. **Open-source AI companions remain a thin field.** Letta/MemGPT (memory), LangChain memory modules, Open Interpreter, OpenHands, paperclip itself. None ship wearable-shaped memory with self-model + LLM-wiki. **memoryd v2 is the first open-source implementation of the Perplexity-Brain-shape architecture, deployed on a wearable.**
7. **Privacy is a brand asset.** Meta's cloud-Assisted voice retention is now a public-policy problem (EU NOYB complaints, Illinois HB4843 smart-glasses driving ban). Even G2's privacy positioning is the marketing wedge. **v8 recommends concrete privacy posture: auditable local-only inference by default, no cloud, opt-in federated learning only, hardware mic kill-switch in v2, retention policy per memory type, auditable calibration surface per service.**
8. **Power/thermal scaling laws (arXiv 2512.16531v2) ground the v8 wearable power budget.** 1.6W idle / 4–6W watchful / 7–9W active remains the target. CompactifAI on Pi 5 → 62% energy savings, 60.5% CPU AUC reduction. v8 budget is now a *measured target*, not a planning estimate.
9. **The audiod confidence-calibration RL agent is v8's north star, redesigned around AHE-style harness evolution + self-model write-back to memoryd operative_context.** Submit to AIE-Bench + SEAGym by Sep 30, 2026. arXiv pre-print by Aug 15. **The one move that graduates Danlab from "pre-RL scaffold" to "verified, auditable, self-modeled self-improving system."** Add: every harness revision's rationale is written to memoryd operative_context as a self-model artifact; the next iteration reads the prior operative_context before proposing revisions.
10. **The new RSG (recursive self-goal) concept from arXiv 2606.09663 (MetaAI Reproducible Engineering Evidence) is v8's design discipline.** Four criteria: (a) inspectable target system, (b) meta-level modifier, (c) feedback-directed selection, (d) recursive continuation. **memoryd v2 + audiod RL agent + dani-skills satisfy (a)(c)(d) today; (b) is what audiod RL agent + Sakana-lineage harness evolution adds.**

**The single sentence:** Ship audiod confidence-calibration RL agent with AHE-style harness evolution + self-model write-back to memoryd v2 operative_context by Sep 30, 2026 (arXiv Aug 15, AIE-Bench + SEAGym); ship memoryd v2 with AEL + DPCM + LLM-Wiki + operative_context + audit trail in 6 weeks by Aug 15, 2026; keep LFM2.5-VL-450M and add CondenseVLM/QViD/V5e-0 token-pruning + speculative-decoding stack by Sep 1, 2026; swap KittenTTS → Kokoro-82M with Hindi voice + WebGPU fallback by Jul 15, 2026; position the brand as *Even-G2-shaped open-source glasses with auditable reliability + India-cost* against Meta's $379–$799 EMG+display line.

---

## Part A — System Architecture Deep Dive

### A1. Service decomposition — right; transport — mostly right; reliability surface — required; self-model — missing

**Live verification this run (2026-06-25 02:05 UTC):** audiod 8090 ✅, perceptiond 8092 ✅, memoryd 8741 ✅, toold 8742 ✅, ttsd 8743 ✅, os-toold 8744 ✅, openclaw 18789 ✅, dan-glasses-app 8747 ✅. **8/8 live.**

v7 confirmed the 8-daemon split is correct. v8 sharpens: the seams are right; the **contracts between seams** need to evolve.

**v8 architectural fixes:**

1. **Reliability surface is a per-service contract, now.** Per arXiv 2602.16666 (Towards a Science of AI Agent Reliability) decomposed into consistency / robustness / predictability / safety. Every daemon exposes `GET /reliability` returning these 4 axes + per-axis metrics. audiod emits `confidence: 0.83` today — promote to first-class surface with `GET /reliability/calibration` returning ECE, Brier score, and reliability diagram. memoryd surfaces query/recall calibration; perceptiond surfaces salience-confidence calibration; toold surfaces command-outcome calibration; ttsd exposes synthesis-quality calibration.
2. **Self-model is a first-class artifact, not an aspiration.** AI Weekly's self-improvement wall tells us: harness evolution alone plateaus at iteration 1. v8 introduces `dan-self-model` as a shared library that every RL harness / harness-evolving daemon writes to and reads from. Backed by memoryd v2's operative_context stream. audiod RL agent writes every harness revision + rationale + measured reward on (val, ID, OOD) + failure-mode flag. memoryd surfaces this stream as `GET /self_model?daemon=audiod`.
3. **Harness evolution + peak detection + checkpoint rolling + ES as a shared library.** v7 introduced this. v8 hardens it: extract into `dan-loop` library used by audiod RL agent, memoryd v2 retrieval-mode bandit, future perceptiond RL harness. `dan-loop` provides: peak detection (composite reward), checkpoint rolling (keep top-K snapshots), ES (Evolution Strategies for sparse-reward settings), AHE-style adaptive update rate.
4. **Adaptive routing as deployment default.** v7 introduced this via INAR-VL. v8 confirms: edge-only vs cloud-only is the wrong frame. Wearable runs INAR-VL-style router: cheap salience + audiod-derived features stay local; ambiguous queries escalate to cloud with *audit-trail recording* in memoryd's operative context. The router itself is open and auditable.
5. **Failure-mode registry is required, not optional.** Per the rise-and-collapse finding (v6/v7) + AI Weekly wall. Every harness revision flags: (a) rise, (b) plateau, (c) collapse, (d) OOD-only gain, (e) ID-regression. The registry is part of the self-model.

**Bottlenecks (v8 revision):**

1. **VLM inference wall-clock.** Keep LFM2.5-VL-450M + add CondenseVLM/QViD/V5e-0 stack. Combined 3–5× wall-clock on the same model. ~3.8s TTS cold-path → swap to Kokoro-82M gets <1s warm.
2. **No wake/sleep state machine.** Unchanged. v8 power budget hardened: 1.6W idle / 4–6W watchful / 7–9W active, grounded by CompactifAI scaling laws.
3. **Mock capture in perceptiond.** Unchanged; mention as v2 wearable feature.
4. **No frame retention.** v8 unchanged.
5. **memoryd uses float32 embeddings.** v7: keep float32 for query-time accuracy, add int8 cold-store. v8 unchanged.
6. **toold sandbox at /tmp/toold-sandbox.** v8: persistent audit log written to memoryd operative context. Every command execution writes (timestamp, command, exit_code, duration, sandbox_state) to memoryd so memoryd can surface "what tools have you used in the last 24h?"
7. **No self-improvement loop seam — addressed by v8 self-model + dan-loop library.**
8. **OpenClaw transport is HTTP+JSON.** v7: works for research but not for wearable. v8 unchanged; mark as v2 wearable target (gRPC or unix socket).

**Recommendation:** Rewrite PRD.md Section 4 to match Python reality. Add Section 4.5 *Reliability Surface Contract*. Add Section 4.6 *Self-Model and Operative Context*. Add Section 4.7 *Adaptive Routing Layer*. Mark Rust migration as v2 wearable target.

### A2. Is the multimodal "RL feedback loop" true RL or heuristic?

**v8 answer:** It is a *heuristic*, and that is the correct framing for v1. The architecture is explicit: "This is NOT reinforcement learning." The **next step** is to make it *auditable* RL via the audiod confidence-calibration RL agent, which is a controlled, benchmarked, ECE-grounded harness evolution. This is **not** recursive weight modification — it is **self-modeled harness evolution on a frozen encoder**, which is the responsible-SRI path post-Anthropic's Jun 4 2026 pause call.

**Concrete audiod RL agent design (v8 revision, incorporating Sakana DGM + AI Weekly wall + Perplexity Brain self-model):**

```python
# audiod_rl/loop.py — AHE-style harness evolution with self-model
class AudiodCalibrationLoop:
    def __init__(self, base=whisper_cpp_base_en, calibration_head=MLP4):
        self.policy = calibration_head
        self.snapshots = []  # SEAGym-style auditable snapshots
        self.peak_score_id = None
        self.peak_score_ood = None
        self.peak_snapshot_id = None
        self.self_model_stream = "memoryd://operative_context/audiod_rl"
        self.failure_mode_registry = FailureModeRegistry()

    def step(self, batch):
        # 1. compute reward on val (Librispeech), ID (CommonVoice en),
        #    OOD (CommonVoice Indian-accent)
        reward_val, reward_id, reward_ood = self.evaluate(batch)
        composite = reward_val + 0.5*reward_id + 0.3*reward_ood
        # 2. AHE-style harness evolution with conservative OOD penalty
        revision_rationale = self.policy.update(
            batch, reward_val, lambda_id=reward_id, lambda_ood=reward_ood
        )
        # 3. SEAGym-style snapshot (auditable)
        snap_id = self.save_snapshot(reward_val, reward_id, reward_ood,
                                     rationale=revision_rationale)
        self.snapshots.append(snap_id)
        # 4. Peak detection on composite (don't keep post-peak decay)
        if self.peak_snapshot_id is None or composite > self.best_composite():
            self.peak_snapshot_id = snap_id
        # 5. Failure-mode detection
        fm_flag = self.failure_mode_registry.check(
            reward_val, reward_id, reward_ood, prev_snap=self.snapshots[-2]
            if len(self.snapshots) > 1 else None
        )
        # 6. WRITE TO SELF-MODEL — close AI Weekly wall
        memoryd.write_operative_context(
            stream=self.self_model_stream,
            event={
                "snap_id": snap_id,
                "rationale": revision_rationale,
                "reward_val": reward_val,
                "reward_id": reward_id,
                "reward_ood": reward_ood,
                "composite": composite,
                "failure_mode": fm_flag,
                "is_peak": snap_id == self.peak_snapshot_id,
            }
        )
        # 7. Early stop if failure mode is "collapse" or OOD-regression
        if fm_flag in ("collapse", "ood_regression"):
            return {"stop": True, "snap_id": snap_id,
                    "reason": fm_flag,
                    "rollback_to": self.peak_snapshot_id}
        return {"stop": False, "snap_id": snap_id,
                "val": reward_val, "id": reward_id, "ood": reward_ood}
```

**Differences from v7 design:**
- `revision_rationale` is now explicit and written to memoryd operative context (closes AI Weekly wall).
- `failure_mode_registry` is a first-class class, not a side check.
- Early-stop returns the rollback snapshot id, not just a stop flag.
- Self-model write happens *every step*, not just on snapshot save.

**Why this is responsible SRI, not closed-loop weight modification:**
- The base whisper.cpp encoder is frozen (no recursive weight modification).
- Only the 4-layer MLP calibration head evolves (~50K trainable params).
- Every revision is benchmarked on val + ID + OOD with published ECE/Brier.
- Failure modes are detected and rolled back automatically.
- Self-model is auditable — anyone can read the rationale stream.
- Comparison set: Sakana DGM (20% → 50% on SWE-bench, 80 iterations) is the proof point that harness evolution alone, sample-efficient, can move the needle — but AI Weekly's wall tells us we need the self-model to compound.

### A3. Power/performance tradeoffs — LFM2.5-VL-450M, whisper.cpp, KittenTTS

**v8 verdict (unchanged from v7):**
- **VLM:** LFM2.5-VL-450M-Q4_0 is reasonable but not SOTA-per-Watt in 2026. Keep as default; add CondenseVLM/QViD/V5e-0 stack; consider OmniVLM-968M (9× token compression, 9.1× faster TTFT) only if Redax hardware supports 1B-class. Token-pruning stack is the highest-ROI move.
- **STT:** whisper.cpp base.en is still the right choice for edge English. Add whisper-large-v3-turbo as a quantized fallback for multilingual.
- **TTS:** **Swap KittenTTS → Kokoro-82M.** v7 recommendation; v8 confirms. Apache 2.0, 82M, 54 voices, 8 languages (Hindi native), 92MB quantized, sub-20ms TTFA warm.

**v8 adds (per INAR-VL paper):**
- Adaptive routing layer is required. Edge-only vs cloud-only is dead. INAR-VL showed 72.1% mean accuracy with 36% on edge, 1.8s latency, 19.2 J/sample — beats both edge-only (66.5%, 824 ms, 7.5 J) and cloud-only (74.4%, 2408 ms, 26.0 J). Implement `dan-router` as a thin layer between audiod/perceptiond output and downstream consumers.

### A4. OpenClaw orchestration — TS/Node is right; failure modes known

**v8 verdict (mostly unchanged from v7):**
- TypeScript/Node is the right choice for the gateway: mcporter bridge to Zo MCP, Telegram bot, Tailscale integration. The OpenClaw TUI ecosystem is mature.
- Failure modes: (a) gVisor sandbox can't run tailscaled (no kernel TUN, no systemd) — gateway reachable on localhost only; (b) OpenClaw restart loses Telegram pairing unless DM policy is reset; (c) mcporter bridge 405 on `mcporter list` is cosmetic.
- v8 adds: **OpenClaw channel for audiod RL agent events.** The audiod RL agent should broadcast (via OpenClaw) every snapshot save + failure-mode trigger to a dedicated channel (e.g. `audiod_rl_events`) so Telegram subscribers can see self-improvement in real time. This is also a marketing asset: "watch Danlab's AI get better, auditable, every hour."

**v8 sharpens:** the OpenClaw-MCP bridge is the *highest-leverage integration in the system*. It exposes the full Zo tool surface (Gmail, Drive, Calendar, Stripe, search, agent skills, etc.) to the audiod RL agent and memoryd v2. v8 recommends adding a `dan-tool` skill that wraps Zo MCP for audiod-specific use cases (e.g. fetch CommonVoice Indian-accent dataset on demand for OOD eval).

---

## Part B — AGI Landscape Research

### B5. State of AGI research in 2026 — what are the leading approaches?

**v8 evidence (late June 2026):**

1. **OpenAI:** Sam Altman (Jun 2026, per Forbes / Lance Eliot): "very surprised if by 2030 there were not AI systems capable of performing tasks at a level higher than humans in most major fields." OpenAI's betting is scale + capability + safe recursive self-improvement (with Anthropic pause-call response).
2. **DeepMind:** Demis Hassabis (per Ynetnews, Jun 2026): human-level AI by 2030, "creativity and taste will matter most in the age of human-level AI." DeepMind bet: Gemini frontier + AlphaEvolve + AlphaProof + scientific discovery agents.
3. **Anthropic:** Jack Clark + Marina Favaro Jun 4 2026 global pause call on recursive self-improvement. Anthropic bet: responsible SRI with auditable benchmarks (Claude Tag, Dynamic Workflows, Memory + Dreaming product).
4. **Sakana AI:** RSI Lab bet on AI that improves itself as compute-efficient frontier (Jun 7 2026). Lineage: Darwin Gödel Machine (SWE-bench Verified 20% → 50% in 80 iterations, Nature AI Scientist publication March 26 2026), LLM², ShinkaEvolve, ALE-Agent, Digital Red Queen.
5. **Meta Superintelligence Labs:** Muse Spark on-device AI for the new $299 Meta glasses line. Closed weights.
6. **Perplexity:** Brain self-improving memory system (Jun 18 2026). Closed weights but the architecture (LLM-wiki + traceable context graph) is observable and reproducible.
7. **Open-source:** Qwen3, Llama-4, Gemma-3, Mistral, DeepSeek-V3, Kimi-K2 — all racing on capability benchmarks. Danlab-relevant: LoRA/QLoRA + S-LoRA + EigenLoRAx + LoRA-Edge are the on-device-fine-tuning enablers.

**v8 framing for Danlab:**
- We cannot compete on the OpenAI/DeepMind/Anthropic frontier.
- We can compete on **responsible, auditable, sample-efficient, on-device SRI** — Sakana's lineage + AI Weekly's self-model requirement + Anthropic's pause call all converge on this.
- We can compete on **open-source LLM-wiki memory** — Perplexity Brain validates the architecture but doesn't ship the open-source version.
- We can compete on **wearable-shaped privacy + India-cost + auditable reliability** — Meta + Even cannot.

### B6. Self-improving architectures — what research exists? What has worked?

**v8 evidence:**

1. **Sakana Darwin Gödel Machine (DGM):** SWE-bench Verified 20% → 50% after 80 iterations, Polyglot 14.2% → 30.7%. The proof point that *harness evolution alone* (no weight modification) can deliver measured improvement. Sample-efficient. (arXiv 2606.09663, Sakana blog.)
2. **Sakana LLM² (LLM-squared):** AI models automating research to invent better preference optimization algorithms. The "AI improves the optimizer" pattern.
3. **Sakana AI Scientist:** End-to-end automation of AI research (idea → experiment → paper), Nature publication March 26 2026. The "AI improves its own research process" pattern.
4. **Sakana ShinkaEvolve:** Sample-efficient evolutionary optimization for code; per winbuzzer, Sakana uses ShinkaEvolve inside DGM.
5. **Sakana Digital Red Queen:** Open-ended adversarial coevolution. The "AI improves by competing with itself" pattern.
6. **Meta-Harness, SEAGym, Socratic-SWE (all v33 in our lineage):** Harness-only updates beat weight tuning on TerminalBench-2. SEAGym gives the eval harness. Socratic-SWE reached 50.4% on SWE-bench Verified in 3 self-evolution iterations.
7. **Perplexity Brain (Jun 18 2026):** +25% correctness, +16% recall, −13% cost from traceable-context-graph + LLM-wiki memory.
8. **AI Weekly self-improvement wall (Jun 2026):** 1,000+ experiments show agents plateau at iteration 1 due to missing self-model. The failure-mode constraint that locks audiod RL agent design.
9. **AEL (Adaptive Ensemble Learning):** Sharpe +27% from two-timescale bandit over retrieval modes (per v33 in our lineage).
10. **Co-rewarding, SIA, SPIRAL, SEAGym:** All v33/v34 lineage. Already integrated.

**v8 verdict:**
- **Harness evolution works.** Sakana DGM is the proof. Sample-efficient.
- **Memory-as-self-model works.** Perplexity Brain is the proof. +25% / +16% / -13%.
- **But harness evolution plateaus without a self-model.** AI Weekly is the proof. The self-model is the missing piece.
- **v8 design is the synthesis:** audiod RL agent with harness evolution + memoryd v2 with LLM-wiki + operative-context self-model + failure-mode registry. This closes the wall.

### B7. Edge AI / on-device models — what's the SOTA for sub-500MB VLMs that actually work?

**v8 verdict (unchanged from v7):**
- LFM2.5-VL-450M-Q4_0 (current production) is fine for low-stakes descriptive tasks.
- Add **CondenseVLM** (token condensation, halves encoder time) + **QViD** (visual token pruning) + **V5e-0** (self-speculative decoding, 1.89× speedup) stack. **3-5× combined wall-clock improvement on same model.**
- Consider **OmniVLM-968M** (9× token compression, 9.1× faster TTFT, 0.75s vs 6.82s) only if Redax hardware supports 1B-class.
- **HyperVL** (arXiv 2512.14052): 2-3B class, ~12.9× faster than some baselines, ~6.8× lower peak memory than Qwen3-VL-2B, constant memory vs input complexity. **Future swap target once Redax supports 2B.**
- **INAR-VL** (arXiv 2605.18853): input-aware routing (72.1% mean accuracy, 36% on edge, 1.8s latency, 19.2 J/sample). **The deployment default.**

**v8 fresh insight (from Sakana's pattern):** sample-efficient improvement means we can fine-tune our current 450M model with the audiod RL agent's harness and stay on the small model. Don't chase 7B+.

### B8. Memory and continual learning — architectures for AI that learns from experience

**v8 evidence:**

1. **Perplexity Brain (Jun 18 2026):** LLM-wiki + traceable context graph + overnight synthesis. +25% / +16% / -13%. **The v8 reference implementation.**
2. **Letta / MemGPT:** open-source memory layer. 83.2% Recall@All@5 on LOCOMO. Strong baseline but lacks the traceable context graph + LLM-wiki.
3. **AEL (v33 lineage):** two-timescale bandit over retrieval modes. Sharpe +27%.
4. **DPCM (v33 lineage):** doubly-linked provenance graph for memory operations.
5. **Anthropic Memory + Dreaming (Jun 2026):** productized memory with reflective consolidation.
6. **OpenClaw-memory-core (Jun 2026):** open-source adapter integrated with OpenClaw, embeddings via `memoryd://v1/embeddings` (already implemented in our memoryd).
7. **Sakana AI Scientist's Memory-as-research-archive:** the agent writes its own memory of what worked.

**v8 verdict:**
- memoryd v2 = Letta (memory primitives) + AEL (bandit over retrieval modes) + DPCM (provenance) + Perplexity Brain LLM-wiki (synthesis) + Anthropic Memory+Dreaming (consolidation cadence) + Operative Context surface + dani-skill integration.
- **6-week build, not 8-week.** The architectural question is closed; the work is shipping.

### B9. Multimodal fusion — combining vision, audio, text

**v8 verdict (mostly unchanged from v7):**
- Late-fusion (current danlab-multimodal approach with separate audiod + perceptiond + memoryd + downstream LLM) is the right call for wearable given hardware constraints.
- New evidence: **INAR-VL input-aware routing** is the SOTA for fusion across edge/cloud. v8 implements `dan-router` as a thin fusion layer.
- The audiod + perceptiond output streams already share the operative_context surface via memoryd; v8 hardens this as a contract.

### B10. Model compression — keeping models small but capable

**v8 evidence:**

1. **CompactifAI on Raspberry Pi 5** (arXiv 2512.16531v2): 60.5% CPU AUC reduction, 71.9% RAM AUC reduction, 2.6× throughput, 62% energy savings on Gilda LLM. Axolotl VLM: 2× throughput, 62% energy savings. **The wearable energy table is grounded.**
2. **LoRA/QLoRA + SLM (Techbytes 2026):** instruction-tuning + LoRA + PTQ on Llama-3.2-1B / Qwen2.5-1.5B. The standard edge fine-tuning recipe.
3. **S-LoRA** (4× throughput, thousands of concurrent adapters). Fits dani-skills library.
4. **EigenLoRAx** (recycle LoRA universe into principal subspaces). Fits federated on-device memoryd v2 fine-tuning.
5. **LoRA-Edge (TT-SVD)**: 2 orders of magnitude fewer trainable params than full FT, within 4.7% accuracy.

**v8 verdict:** for audiod RL agent (4-layer MLP calibration head on frozen encoder), LoRA is overkill. For dani-skills (50+ skill adapters on shared small base), LoRA+QLoRA is the path.

---

## Part C — Competitive & Market Research

### C11. Smart-glasses competitive landscape — now a 4-tier market

**v8 fresh evidence (late June 2026):**

| Tier | Product | Price | Hardware | AI | Privacy | Status |
|------|---------|-------|----------|----|---------| -------|
| Premium closed | Meta Ray-Ban Display | $799 | 600×600 in-lens display + Neural Band EMG (18h, IPX7) | Meta AI cloud (1y voice retention default) | Closed | Shipped Sep 30 2025 |
| Mid closed | Meta Ray-Ban Gen 2 | $379 | Better camera, 8h battery | Meta AI cloud | Closed | Shipping 2026 |
| Mid closed | Oakley Meta Vanguard | TBD | Loudest open-ear speakers, 5-mic array, Garmin/Strava | Meta AI cloud | Closed | Shipping 2026 |
| Mid closed | Even Realities G2 | $599 | Waveguide display, 36g, ±12 diopters, IP65, 1-2 day battery | Conversate (on-device) | **Privacy-first, no camera, on-device** | Shipping 2026 |
| Dev kit | Snap Spectacles | $2,195 | AR display, 132-136g, 4h battery | Snap AI + dev tools | Closed beta | Preorders Jun 16 2026 |
| Displayless | Solos AirGo Vision | TBD | Audio-only, on-device AI | On-device | On-device | Shipping |
| Enterprise | Microsoft Scout | TBD | OpenClaw-based | OpenClaw + GPT | Hybrid | Announced Build 2026 Jun 2 2026 |
| Closed | Apple AirPods + glasses | TBD | 2027+ | Apple Intelligence | Closed | Delayed to 2027 |
| Open-source | Danlab Dan Glasses | ₹4,999 student / ₹12K founder (target) | MicroLED JBD, 2×200mAh | **auditable on-device** | **Local-only by default** | v0 prototype |

**v8 key shifts since v7:**
- **Meta Ray-Ban Display adds EMG hardware.** This is a fundamentally different control surface (muscle signals, no touch, no voice). Danlab's audiod-only control plane is at a disadvantage here, but EMG requires *much* higher production scale (FDA clearance path? likely not; but consumer trust). For v1, voice + visual is the right call.
- **Microsoft Scout is OpenClaw-based.** This is *huge*: a major enterprise player (Microsoft) has chosen our gateway substrate. OpenClaw's reach just expanded by an order of magnitude. v8 sharpens: the OpenClaw + Zo MCP integration is now a competitive asset, not just a dev convenience.
- **Snap Spectacles dev kit preorders Jun 16, 2026.** $2,195 is high; 132-136g is heavy. This is the developer-credibility competitor (Meta was here with the original Ray-Ban Stories). Danlab's open-source posture wins on dev credibility + cost.

**v8 positioning recommendation:**
- **Brand:** "The auditable, open-source AI glasses."
- **Tagline:** "On-device. Open-source. India-cost. Auditable."
- **Differentiators:** (1) auditable reliability surface per service (ECE/Brier/calibration/failure-mode registry), (2) open-source + open-data evaluation, (3) auditable calibration RL agent (AIE-Bench + SEAGym publication Sep 30), (4) memoryd v2 self-model as the first open-source Perplexity-Brain-shape architecture, (5) India-cost + Hindi-native TTS (Kokoro-82M).
- **Pricing:** ₹4,999 student/researcher tier + ₹12K founder tier (matches Dan1 v82/v83 marketing).
- **Form factor:** camera + voice (v1, Echo Frames-shaped); display later.

### C12. Open-source AI companion projects

**v8 fresh evidence (late June 2026):**
- **Letta / MemGPT:** memory primitives; 83.2% Recall@All@5 on LOCOMO. Strong open-source baseline.
- **LangChain memory modules:** integration patterns, no standalone product.
- **Open Interpreter:** agent runtime; not memory-first.
- **OpenHands / Devon:** coding agents; memory is session-scoped.
- **paperclip (Danlab internal):** substrate choice still open (per open question in v6).
- **Auto-Enhance (NeurIPS 2024):** meta-benchmark for AI improving other AI. Reference for audiod RL harness eval.
- **Sakana AI Scientist (Nature Mar 26 2026):** end-to-end research agent. Production-grade agent memory architecture in the paper's supplementary.

**v8 verdict:** memoryd v2 with the Perplexity-Brain-shape architecture (LLM-wiki + traceable context graph + operative_context + self-model) is *the* open-source differentiator in 2026. Letta is the closest competitor; Perplexity is the closed competitor; neither ships wearable-shaped.

### C13. Privacy positioning

**v8 fresh evidence:**
- **EU NOYB complaints** about Meta AI voice retention (1-year default).
- **Illinois HB4843 smart-glasses driving ban** (Jun 2026) — first US state legislation on wearable AI in public.
- **Even Realities G2's no-camera posture** is the marketing wedge — they explicitly brand against camera-glasses.
- **Anthropic Memory + Dreaming** product positions memory as private-by-default with audit-trail.

**v8 concrete privacy posture (recommendation):**
- **Local-only inference by default.** All audiod + perceptiond + memoryd run on-device. No cloud calls. Auditable via reliability surface.
- **Opt-in federated learning only.** If user opts in, model deltas train via LoRA/QLoRA on-device, periodically uploaded as anonymized LoRA adapters (not raw data).
- **Hardware mic kill-switch in v2.** Physical switch on the frame.
- **Per-memory-type retention policy.** Episodic memories default 7-day TTL; semantic memories indefinite; procedural memories indefinite. User can override.
- **Auditable calibration surface per service.** ECE/Brier/calibration diagrams exposed via `GET /reliability/calibration`.
- **No raw audio/video leaves device.** Only transcripts + descriptions leave device, and only if user opts in.

---

## Part D — Technical Deep Dives (v8 picks 3)

### D1. Self-improving RL loops for language models (Option A) — Sakana lineage + AI Weekly wall + Perplexity Brain

**The most important v8 insight from this dive:**

The AI Weekly "self-improvement wall" (Jun 2026) is the missing constraint. 1,000+ experiments show agents plateau at iteration 1. The root cause is a missing self-model. This validates Sakana DGM's open-ended exploration strategy but adds the requirement that every harness revision's *rationale* must be auditable.

**Concretely for audiod RL agent (v8 design):**
- Frozen whisper.cpp base.en encoder (~74M params).
- 4-layer MLP calibration head (~50K params, the only thing that evolves).
- Each step: compute ECE/Brier on (Librispeech val, CommonVoice en ID, CommonVoice Indian-accent OOD).
- AHE-style adaptive update rate (per SEAGym: AHE is the only update strategy that improves val + ID + OOD together).
- After every step: write `{snap_id, rationale, reward_val, reward_id, reward_ood, composite, failure_mode, is_peak}` to memoryd operative_context stream.
- Failure-mode registry detects: rise, plateau, collapse, OOD-only gain, ID-regression. Early-stop + rollback to peak snapshot.

**Compute budget for v8 audiod RL agent:**
- ~$500-2,000 for 100 harness iterations on a single A100 (40-80 hours).
- Memoryd v2 write is negligible (~10 MB total for 100 snapshots).

**Submission plan:**
- arXiv pre-print: Aug 15, 2026.
- AIE-Bench (ICML 2026 CTB workshop): submit by Sep 30, 2026.
- SEAGym: submit by Sep 30, 2026.

### D2. Edge VLM optimization (Option B) — token-pruning + speculative-decoding stack

**v8 verdict (sharpened from v7):**
- Keep LFM2.5-VL-450M as default.
- Add **CondenseVLM** (token condensation, ~2× encoder speedup) + **QViD** (visual token pruning, ~1.5-2×) + **V5e-0** (self-speculative decoding, 1.89× speedup, zero training cost) stack.
- Combined 3-5× wall-clock on same model.
- OmniVLM-968M is the swap if Redax hardware supports it (9× token compression, 9.1× faster TTFT).
- INAR-VL routing layer required for adaptive edge/cloud split.

**v8 fresh insight:** the audiod RL agent harness can also compress perceptiond. Same VLM backbone → smaller projection head for salient frames. **This is auditable:** the VLM size is published; the compression is published; the calibration surface shows the accuracy/latency tradeoff.

### D3. Vector search and memory architectures for AI companions (Option C) — Perplexity Brain is the production reference

**v8 verdict:**
- memoryd v2 architecture = Letta memory primitives + AEL two-timescale bandit + DPCM doubly-linked provenance graph + Perplexity Brain traceable context graph + LLM-wiki + Anthropic Memory+Dreaming consolidation cadence + Operative Context surface.
- 6-week build (compressed from v7's 8-week).
- Submit to LongMemEval + PersonaMem-v2 by Sep 30, 2026.
- **Deploy date: Aug 15, 2026** (perplexity Brain's production deployment is the credibility ceiling).

**v8 fresh insight:** Sakana's AI Scientist (Nature Mar 26 2026) ships an agent that writes its own research memory. We can adopt the same pattern for danlab-multimodal — the danlab-multimodal agent writes to memoryd v2 operative_context every time it improves a descriptor, so the harness's self-model grows over time.

---

## Part E — v7 → v8 deltas (summary)

| v7 claim | v8 update | Source |
|----------|-----------|--------|
| AIE-Bench + SEAGym are venues | Confirmed; add Sakana DGM + AI Scientist + Perplexity Brain as lineage | arXiv 2606.09663, Nature Mar 26 2026, perplexity.ai Jun 18 2026 |
| audiod RL agent = AHE + snapshot protocol | + self-model write-back to memoryd operative_context (AI Weekly wall fix) | aiweekly.co, Jun 2026 |
| memoryd v2 = AEL + DPCM + LLM-Wiki + operative_context | Confirmed; v8 closes architectural question (Perplexity Brain production ref) | perplexity.ai Jun 18 2026 |
| 8-week memoryd v2 build | Compressed to 6 weeks; deploy Aug 15 not Sep 15 | engineering judgment |
| KittenTTS → Kokoro-82M swap | Confirmed; v8 deploys Jul 15 | hexgrad, pykokoro |
| Smart-glasses 5-horse race | Collapsed to 4 tiers + Apple 2027 | Meta Connect 2025, Even Realities G2 review |
| Privacy is a brand asset | Confirmed; v8 adds auditable calibration surface as privacy posture | EU NOYB, Illinois HB4843 |
| Reliability surface per service | Confirmed; v8 adds self-model write-back seam | arXiv 2602.16666, AI Weekly |
| Power/thermal 1.6/4-6/7-9W | Hardened by arXiv 2512.16531v2 CompactifAI scaling laws | arXiv 2512.16531v2 |
| AGI north star = auditable reliability | v8 = auditable reliability + self-model + open-source LLM-wiki memory + India-cost | Sakana RSI Lab, Perplexity Brain |

---

## Sources (cited inline above)

1. Sakana AI RSI Lab launch (Jun 7 2026): https://sakana.ai/rsi-lab
2. Perplexity Brain launch (Jun 18 2026): https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents
3. AI Weekly "self-improvement wall" (Jun 2026): https://aiweekly.co/alerts/ai-agents-hit-self-improvement-wall-after-one-pass
4. Meta Connect 2025 — Ray-Ban Display + Neural Band: https://www.fonearena.com/blog/464641/meta-connect-2025-ray-ban-gen-2-ray-ban-display-oakley-meta-vanguard.html
5. Even Realities G2 review (2026): https://me.pcmag.com/en/smart-glasses/36475/even-realities-g2
6. Even Realities G2 product page: https://www.evenrealities.com/smart-glasses
7. Darwin Gödel Machine reproducible evidence: https://arxiv.org/pdf/2606.09663
8. arXiv 2602.16666 — Towards a Science of AI Agent Reliability: https://arxiv.org/abs/2602.16666
9. arXiv 2512.16531v2 — Scaling Laws for Energy Efficiency of Local LLMs: https://arxiv.org/abs/2512.16531
10. arXiv 2412.11475v2 — OmniVLM: https://arxiv.org/abs/2412.11475
11. arXiv 2512.14052 — HyperVL: https://arxiv.org/abs/2512.14052
12. arXiv 2605.18853 — INAR-VL routing: https://arxiv.org/abs/2605.18853
13. arXiv 2603.26769 — Edge Reliability Gap: https://arxiv.org/abs/2603.26769
14. Techbytes — Fine-Tuning SLMs for Edge Inference 2026: https://techbytes.app/posts/fine-tuning-slms-for-edge-inference-guide-2026
15. TechCrunch — AI world getting loopy (Jun 22 2026): https://techcrunch.com/2026/06/22/the-ai-world-is-getting-loopy/
16. Forbes — AGI stepwise vs spontaneous (Jun 20 2026): https://www.forbes.com/sites/lanceeliot/2026/06/20/whether-artificial-general-intelligence-will-arise-spontaneously-or-via-slow-roll/
17. Forbes — Ben Goertzel's crypto bet against OpenAI (Jun 21 2026): https://www.forbes.com/sites/boazsobrado/2026/06/21/agi-is-too-important-ben-goertzels-crypto-bet-against-openai/
18. Ynetnews — Demis Hassabis AGI by 2030: https://www.ynetnews.com/tech-and-digital/article/hye3xsymgg
19. IEEE Spectrum — Recursive Self-Improvement Edges Closer: https://spectrum.ieee.org/recursive-self-improvement
20. The Decoder — Sakana AI RSI Lab compute bets: https://the-decoder.com/sakana-ai-bets-ai-that-improves-itself-can-break-the-compute-arms-race-of-frontier-labs
21. MarkTechPost — Perplexity Brain analysis: https://www.marktechpost.com/2026/06/18/perplexity-launches-brain/
22. Emergent Mind — LoRA advances: https://emergentmind.com/topics/lora-fine-tuning

— DAN-2, 2026-06-25 07:35 IST (02:05 UTC). v8 supersedes v7. Live infrastructure verified green.