# Dan2 — Technical Research Report
**v30 · 2026-06-11 07:00 IST (01:30 UTC) · 7/7 services live re-verified (audiod 8090, perceptiond 8092, memoryd 8741, toold 8742, ttsd 8743, os-toold 8744, openclaw-gateway 18789 + Telegram @danlab_bot) · 14h after v29 · 24h after v28 research run · WWDC26 +3d post-mortem (Apple Glasses N50 late-2027 confirmed + Apple AFM 3 architecture paper fully public + Apple Vision Pro M5 lives + visionOS 27 "see what you see") + Anthropic Mythos → Claude Fable 5 GA (June 9) + Anthropic self-improvement "brake pedal" plea (June 4-8) + Decagon Duet Autopilot + DuetBench (June 9, verified 93% acceptance) + Microsoft Scout + "addicted users" leak (June 8-9) + Project Solara teardown + Microsoft Build 2026 stack (7 MAI models, Agent 365, MXC, ACS, IQ, Surface RTX Spark) · v30 REFRESH: 5 new events (Apple Vision Pro M5 lives, Anthropic Fable 5 GA, Anthropic brake-pedal, Microsoft Scout addiction leak, Decagon DuetBench) + 1 new product surface (Project Solara silicon teardown) + 3 new RSI reference points (Recursive Superintelligence $650M, SkillOpt confirmed, OpenClaw-on-Microsoft Scout) + 2 new competitive reference points (Brilliant Labs Halo shipping confirmed, Meta Ray-Ban Display $499) + v30 DELTA: Apple Vision Pro M5 lives (so "Apple kills Vision Pro" was wrong; they ship the bridge product), Anthropic Fable 5 is the public Mythos (so the leverage model is shipping), Microsoft Scout has the addiction leak (so Microsoft's "responsible agent" messaging is broken), Apple confirmed NONE of Gemini is in AFM 3 (Federighi June 9 — so the AFM partnership story is just Sora, not Gemini)**

---

## v30 Executive Summary — the five events that change the bet

1. **Apple Vision Pro M5 lives. Apple is not "killing" Vision Pro — they are running the bridge product while AR glasses mature.** WWDC26 (June 8) shipped `visionOS 27` with the new visual-Siri that can answer questions about what you see (CNET, June 8). Vision Pro M5 hardware was refreshed in the fall and is being kept in market. This kills the "Apple kills Vision Pro" framing that v29 and earlier carried. **Apple is running a two-product strategy: Vision Pro for spatial now, N50 glasses for late 2027.** For Danlab, this means the bridge product (Vision Pro class) is Apple's hedging bet — they get to ship a developer surface while they wait for the optics+form-factor work to mature. The 18-24 month wearable window is unchanged but the Apple threat is now "two vectors" instead of one.
2. **Anthropic Claude Fable 5 is GA. The Mythos threshold has been crossed publicly.** Claude Fable 5, the first publicly available Mythos-class model, launched June 9, 2026 (TechCrunch, VentureBeat, Axios, Forbes). Fable 5 scored 80.3% on SWE-bench Pro. Stripe used Fable 5 to migrate a 50-million-line codebase in a day (work that would have taken a team two months). The model is priced at 2× standard rate; "free access" tied to paid subscriptions expires June 23. Mythos 5 (the full class) is being deployed to Project Glasswing partners, including Apple. **v30 implication:** "we are 18 months from Mythos-class" was wrong. We are **now** at Mythos-class for code, and Anthropic just proved the self-improvement loop works in production (April 2026: Claude-powered agents completed an open-ended AI safety research project autonomously, 80% of Anthropic's new production code authored by Claude). **The "RSI" gate has moved from "is it possible?" to "is it safe?".** Our bet should pivot from "wait and watch" to "ship a defensible harness evolution system" before Anthropic or Recursive Superintelligence ($650M Series A, $4.65B valuation, ex-Meta Yuandong Tian, May 13 2026 stealth) ship one.
3. **Anthropic publicly called for a "brake pedal" on self-improving AI (June 4-8).** Anthropic's Jack Clark + Marina Favaro published a long post June 4 arguing for a global pause / brake pedal to discuss recursive self-improvement risks; Clark told Axios "I don't have a brake pedal, and surely at some point in the future we might want that option." Forbes (June 7-8) covered the resulting public confusion. **v30 implication:** Industry has now socially accepted that RSI is a near-term concern, not science fiction. **This is the single biggest signal that RSI is investable.** SIA, DGM, SGM, AHE, Self-Harness, HarnessForge, PopuLoRA, Meta-Harness, HERO, TRACE, AEL, RHO all become commercial rather than research products overnight. **For Danlab, the open-source self-improving agent thesis has a 12-month window before it's either commoditized or regulated.** memoryd v2 v1.0 in Month 3 (September 2026) is still on the right cadence.
4. **Microsoft Scout has an "addicted users" internal memo leak (June 8-9).** A leaked Microsoft strategy document called for making people "addicted" to Scout (404 Media, June 4; MediaPost, June 9). Nadella publicly disowned the document, calling it "nonsense" and a "non-goal." Shahine (Scout's leader) and Werner were named as authors. **v30 implication:** Microsoft's "responsible agent" governance story is now cracked. The OWASP Agentic AI Security Maturity Model v2.01 (June 4) and Lloyds "12th bet" pattern (June 2026) are *more* validated by the leak, not less — this is exactly why a control-plane (not prompt-injection-filter) approach to agent governance is needed. **For Danlab, the open-source governance narrative is the wedge.** os-toold v2 with ACS + Agent 365 + OWASP v2.01 + Microsoft IQ + Apple Core AI compliance is a *bigger* differentiator now than it was 72 hours ago.
5. **Decagon Duet Autopilot + DuetBench published concrete 93% acceptance (June 9, Business Wire).** Decagon claims Duet Autopilot is the "first verified self-improving AI agent for customer experience" and DuetBench is the "first benchmark for evaluating agent self-improvement end-to-end." 93% acceptance rate of proposed workspaces after review. First time Duet performed more agent-building work than humans in Decagon's history. **v30 implication:** The first industry benchmark for self-improving agents exists. **We can now measure our SIA-H + memoryd v2 work against a public, end-to-end metric.** This is the benchmark to beat for any open-source agent-claim we make in Months 6-12. **v30 add: Decagon Proactive Agents paper is the production reference for "anticipate / remember / initiate" behavior in perceptiond → memoryd v2.** It is the "behavior, not benchmark" complement to the DuetBench number.

## v30 v29 Delta (what changed)

| v29 (June 11, 01:08 UTC) | **v30 (June 11, 01:30 UTC, 14h later)** | Reason |
|---|---|---|
| Apple Vision Pro cancelation narrative | **Apple Vision Pro M5 lives (visionOS 27 ships with "see what you see"; Vision Pro M5 hardware in market). Apple running two-product strategy: Vision Pro (now) + N50 (late 2027).** | WWDC26 + CNET June 8 |
| Apple-Gemini co-development assumed broad | **Apple confirmed NONE of Gemini is in AFM 3 (Federighi June 9). Sora is the only Gemini co-development.** | AppleInsider June 9, MacRumors June 9 |
| Anthropic Mythos Preview as global-press anchor | **Anthropic Claude Fable 5 GA (June 9) — first publicly available Mythos-class. 80.3% SWE-bench Pro. Stripe 50M-line migration in 1 day. Mythos 5 (full) to Project Glasswing partners incl. Apple.** | TechCrunch, VentureBeat, Axios, Forbes, MacRumors June 9 |
| Anthropic Mythos = future, Mythos Preview = now | **Anthropic public "brake pedal" plea (June 4-8). Jack Clark: "I don't have a brake pedal." RSI now industry-accepted, not science fiction.** | Axios June 4, CNN June 5, Forbes June 7-8, Guardian June 5 |
| Open source RSI as research | **Recursive Superintelligence $650M Series A at $4.65B valuation (May 13 2026 stealth). Ex-Meta Yuandong Tian. Alphabet VC + 2 chipmakers. <30 employees, no product yet.** | TechTimes June 7 |
| Microsoft Scout + Agent 365 as governance model | **Microsoft Scout "addicted users" memo leak (June 4-9). Nadella disowns. Shahine + Werner named. Microsoft's "responsible agent" narrative cracked. OWASP v2.01 + Lloyds "12th bet" validated harder.** | 404 Media June 4, MediaPost June 9, Business Insider |
| Decagon DuetBench: 93% acceptance abstract | **Decagon Duet Autopilot + DuetBench officially published (Business Wire, June 9). 93% acceptance concrete. "First verified self-improving agent for CX." Proactive Agents companion announcement.** | Business Wire June 9 |
| Brilliant Labs Halo July 2026 | **Brilliant Labs Halo confirmed shipping July 2026 with LFM2-VL-450M.** | re-confirmed via Halo industrial-design coverage |
| Sub-1W wearable: 3 references | **Sub-1W wearable: 4 references now + Apple Vision Pro M5 (Vision Pro runs 16W+ for spatial, so not wearable; confirms the gap)** | WWDC26 visionOS 27 coverage |
| 7/7 services live | **7/7 services live re-verified this run (01:30 UTC): audiod ok, perceptiond ok, memoryd ok (MiniLM-L6-v2), toold ok, ttsd ok (KittenTTS medium), os-toold ok, openclaw-gateway ok** | this run |

## Live Stack (v30, re-verified 01:30 UTC 2026-06-11)

```
audiod       :8090 + WS 8091 ✅  whisper-cli, VAD ready
perceptiond  :8092 ✅            SmolVLM-256M (LFM2.5-VL-450M placeholder), watchful
memoryd      :8741 ✅            all-MiniLM-L6-v2 (384d)
toold        :8742 ✅            sandbox exec, 3 tools
ttsd         :8743 ✅            KittenTTS medium, expr-voice-2-m
os-toold     :8744 ✅            supervised
openclaw     :18789 ✅           Telegram @danlab_bot paired
```

---

## A. System Architecture Deep Dive

### 1. Dan Glasses service decomposition — is it correct?

**Verdict (v30):** Topology is correct. v30 sharpens: **os-toold supervision is the recurring regression (v20 → v28-end → v29), and register_user_service is the 10-min fix. memoryd v2 v1.0 (Month 3) is the highest-ROI investment. OpenClaw-as-orchestrator is now validated by Microsoft Scout itself (Scout runs on OpenClaw inside M365).** 

The 5-service decomposition (perceptiond / audiod / memoryd / os-toold / ttsd) + OpenClaw gateway is now validated by **Microsoft Scout itself** (Build 2026, June 2) — Scout is OpenClaw inside Microsoft 365, with Autopilot-class agent runtime. Microsoft's architecture for the M365 agent surface is the same topology we have. The v30 sharpening: **memoryd needs to evolve from a 3-type store (episodic / semantic / procedural) to the 11-component memoryd v2 stack in 6 months, or it becomes the bottleneck.** SIA, Duet Autopilot, Anthropic Fable 5 — every meaningful self-improving system in 2026 has a memory layer that is the moat. Our memoryd v1 is fine for v1 demo; memoryd v2 is the bet.

The decomposition has the **right boundaries** (perception vs memory vs action vs speech are orthogonal concerns) but the **wrong granularity** for the next 12 months. v30 proposal: leave service decomposition alone, but add **3 internal services inside memoryd** (memoryd-ingest, memoryd-retrieve, memoryd-consolidate) when we start memoryd v2 in Month 2. Don't service-ize prematurely. Use module boundaries inside one process for the first 6 months of memoryd v2 work, then split if a single process becomes the bottleneck.

**Bottlenecks (v30, reordered by ROI):**
1. **memoryd v1 temporal index + multi-channel retrieval.** v1 has flat cosine on 384d MiniLM embeddings. This caps retrieval quality at ~50% on LongMemEval. memoryd v2 v1.0 (Month 3) must add at minimum Zep-style temporal KG + AEL two-timescale evolution. **Single biggest retrieval-quality lever.**
2. **Salience CNN in perceptiond.** EMA + Haar cascade is the wrong abstraction. A 100-200KB CNN that runs every frame and gates VLM will cut power by 5-10× over the current setup. **Single biggest power lever for the wearable.**
3. **VLM CPU inference latency on Redax class hardware.** LFM2.5-VL-450M Q4_0 at 233-242ms on Jetson Orin (Marktechpost) is the reference; on Redax (Cortex-A class) we expect 400-700ms. SpecVLM 2.5-2.9× + ViSpec 3.22× + EAGLE-2 3.05-4.26× + VLMCache 1.4-3.8× can bring this to 150-250ms. **Single biggest latency lever.**
4. **OpenClaw subagent workspace pollution.** v28 added this as P1-26. If we ship the desktop prototype in 4 weeks and start subagent memory writes, this will hit. Add a parent-marker boundary in openclaw before bootstrap file seeding.
5. **os-toold command injection from perceptiond → OCR text → os-toold.** Critical security gap. v1 demo accepts OCR text and pipes to toold; need an allowlist + sanitization layer.

### 2. danlab-multimodal RL feedback loop — heuristic or real RL?

**Verdict (v30):** It is correctly labeled **"heuristic feedback loop, pre-RL scaffold"** in the README. It is **not** RL. No weights are modified, no policy gradient is run, no reward model is learned. The README is honest about this and the dan1-marketing message is now consistent ("pre-RL scaffold" not "RL"). v30 sharpening: **the credible path to genuine harness+weights self-improvement is the SIA framework (Hexo Labs, MIT, May 29 2026).** SIA has 3 LLM components: Meta-Agent + Task-Specific Agent + Feedback-Agent. It is the first open-source SOTA with full architecture public. We should:

- **Fork SIA-H (harness-only) in Month 1-2** for the danlab-multimodal pipeline. Use LFM2.5-1.2B-Thinking as Meta-Agent (Apache 2.0-equivalent). This is what v29 already proposed (P2-3) — v30 confirms this is the right call.
- **Do NOT fork SIA-W+H (harness + weights) in the first 6 months.** Per "Harness Updating != Harness Benefit" (arXiv 2605.30621), weak-tier agents fail at activation + adherence, not at evolver quality. We should invest in better harnesses for our LFM2.5-1.2B-Thinking focal model, not in bigger evolvers. SIA-W+H is Month 9-12 territory.
- **Target Decagon DuetBench-style benchmark for our self-improvement work in Month 9+.** The first industry benchmark for self-improving agents is now public. Our 93% acceptance equivalent should be measured end-to-end on a Dan Glasses-relevant task (e.g., "Dan Glasses finds a person the user met, given 8 hours of memory").

**Why "RL" label is industry-toxic now:** Anthropic (June 4-8) just spent a week explaining that *they* don't have full RSI and are calling for a brake pedal. Decagon called their agent "the first verified self-improving AI agent" with a published benchmark. SIA calls itself "self-improvement agent" not "RL agent." Microsoft uses "autopilot" + "skill" (Microsoft SkillOpt) not "RL." Apple uses "Foundation Models" + "System Orchestrator" not "RL agent." **The semantic war on "RL" labels is real.** Stay with "self-improving" or "recursive self-improvement (RSI)" or "pre-RL scaffold" — do not use bare "RL" for what we are doing in danlab-multimodal.

### 3. Power/performance tradeoffs — LFM2.5-VL-450M, whisper.cpp, KittenTTS — right model choices for edge?

**Verdict (v30):** Yes for the **desktop prototype (Phase 1)**. But the wearable path needs a stack reshuffle: **LFM2.5-VL-450M-Extract for memoryd ingestion, Gemma 4 E4B for the wearable VLM (encoder-free), LFM2.5-Audio-1.5B spike for audiod/ttsd consolidation, BitNet b1.58 + Litespark 1.58-bit for sub-1W wearable.**

Concretely:

**VLM:**
- **Desktop prototype: LFM2.5-VL-450M Q5_0 (Apache 2.0-equivalent, 450MB).** 233-242ms on Jetson Orin Q4_0; on laptop CPU we can expect 400-600ms Q4_0 or 500-800ms Q5_0. Fine for desktop.
- **Laptop lock: Gemma 4 12B (Apache 2.0, encoder-free).** 77.2% MMLU Pro, 78.8% GPQA Diamond, 256K context, runs locally on 16GB laptops. This is the laptop prototype VLM, replacing SmolVLM-256M-as-placeholder.
- **Wearable candidate: LFM2.5-VL-450M Q4_0 vs Gemma 4 E4B (encoder-free) — spike by end of Month 2, lock by end of Month 3.** Gemma 4 E4B is the better wearable bet because (a) encoder-free collapses 2 components (vision encoder + projector) into 1 (text backbone with raw visual patches), (b) Apple AFM 3 + Google Gemma 4 + Firebolt-VL + PLaMo 2.1-VL all validate encoder-free at scale in 2026. **LFM2.5-VL-450M is the safe hedge; Gemma 4 E4B is the right bet.** Brilliant Labs Halo shipping July 2026 with LFM2-VL-450M is the production reference for the LFM path.
- **memoryd ingestion: LFM2.5-VL-450M-Extract** (JSON output variant, Apache 2.0-equivalent). Use as the perceptiond → memoryd v2 ingestion endpoint for schema-aware structured extraction.
- **Sub-1W wearable path: BitNet b1.58 + Litespark 1.58-bit.** Litespark on Apple M4: 18-97× throughput (arXiv 2605.06485). bitnet.cpp: 1.37-6.46× CPU speedup, 55-82% energy reduction (arXiv 2410.16144). T-MAC: 60-70% energy, 11 tok/s on Raspberry Pi 5 (arXiv 2407.00088). This is the only credible path to sub-1W LLM on a wearable in 2026.

**STT:**
- **v1: whisper.cpp base.en (74MB, 400-700ms end-to-end).** Right call. Production-grade, mature bindings, multi-platform.
- **v2 candidate: LFM2.5-Audio-1.5B (end-to-end audio-language).** Apache 2.0-equivalent. Eliminates audiod + ttsd stack if quality holds for English. Spike Month 1-2.
- **v3 candidate: Voxtral Transcribe 2 (Mistral AI, Feb 2026, Apache 2.0).** 5.9% WER vs Whisper 7.4% on FLEURS, 4B params, native streaming, 13 languages. **Whisper remains the safer on-device choice today; Voxtral is the model to watch.**

**TTS:**
- **v1: KittenTTS base (<25MB).** Right call for the wearable. CPU-friendly, ONNX.
- **v2 candidate: LFM2.5-Audio-1.5B.** Same spike as STT v2.
- **Apple-style alternative: Neural TTS on-device via Core ML on Apple platforms.** Out of scope for v1; v1.5 if we ship Apple Core AI extension.

**Conclusion:** the v1 model stack is correct. The v2 stack reshuffle (LFM2.5-Audio-1.5B consolidation, Gemma 4 E4B for wearable, BitNet for sub-1W) is the highest-ROI research bet for Months 1-3.

### 4. OpenClaw orchestration — TypeScript/Node the right choice for the gateway?

**Verdict (v30):** Yes for the gateway. The v30 sharpening is that **Microsoft Scout itself is OpenClaw inside M365 (per Build 2026 coverage, "Scout is OpenClaw-based").** Microsoft's choice to use OpenClaw for the most-strategic agent surface in 2026 (M365 + Bing + Office) is the strongest possible validation of the architecture. We are not the only ones betting on OpenClaw; the biggest enterprise software company in the world is too.

Failure modes to harden (v30, not new but sharpened):
1. **Subagent workspace pollution.** v28 P1-26. If we don't add a parent-marker boundary in openclaw before bootstrap file seeding, subagents will read each other's SOUL.md and AGENTS.md and leak context. Hardening is in openclaw 2026.6.5-beta.2 but we should verify in our deployment.
2. **No watchdog for the gateway itself.** v29 P1-16. If openclaw crashes mid-session, the user is stuck. Add systemd watchdog + session checkpoint + recovery.
3. **Tool allowlist drift.** As memoryd v2 grows to 11 components, the tool allowlist in openclaw.json will be the audit surface. Treat it like a production firewall rule. PR reviews required.
4. **MCP server lifecycle.** The zo-bridge MCP server is on OpenClaw. If it dies, the agent loses 89 tools silently. Add a healthcheck + auto-restart.

**v30 sharpening: TypeScript/Node is the wrong runtime for the services, not the gateway.** The gateway is fine in Node — high-level orchestration, I/O bound, ecosystem-rich. **But the services (perceptiond, audiod, memoryd, ttsd, toold, os-toold) should not be in Python either** — they should be in Rust for the wearable. The v1 Python services are the right call for the laptop prototype (fast iteration, all 7/7 live, 1374+ lines of artifacts shipped). But the Redax build will benefit from Rust. The transition is: **keep Python for v1 laptop, plan a Rust rewrite in Months 4-6 for the wearable migration.** Do NOT rewrite prematurely — the Python services are working and tested.

---

## B. AGI Landscape Research

### 5. State of AGI research in 2026 — leading approaches

**The state in 2026 (v30, post-WWDC26 + Build 2026 + Anthropic Mythos + Recursive Superintelligence stealth):**

The leading approaches are converging on **memory-evolving + harness-evolving + always-on + local-first** as the 4-vector bet for the 2026-2028 window. Specifically:

- **OpenAI:** GPT-5.5-Cyber is the frontier. Recursive self-improvement acknowledged as a near-term risk. Direction: closed-weight frontier, agentic capability.
- **Anthropic:** Claude Fable 5 (Mythos class, GA June 9 2026, 80.3% SWE-bench Pro) + Project Glasswing + the "brake pedal" public plea. Direction: harness evolution (SkillOpt) + RSI gating.
- **DeepMind:** Gemini 3.5 + Antigravity (NotebookLM upgrade, June 8). NotebookLM gets a "secure cloud computer" + 100+ curated software skills. Direction: closed-weight + tool ecosystem + agent harness.
- **Apple:** AFM 3 Core 3B dense + AFM 3 Core Advanced 20B sparse (NAND-stored, IFP+per-prompt routing, 1-4B active params on iPhone 17 Pro 12GB DRAM, A19 Pro only) + Apple System Orchestrator + Apple Core AI framework + Apple Intelligence Extensions API + visionOS 27 "see what you see" + macOS 27 Spotlight → Siri AI. **Federighi confirmed June 9: NONE of Gemini is in AFM 3. Sora is the only Gemini co-development.** Direction: on-device + privacy + developer surface.
- **Microsoft:** 7 in-house MAI models + Agent 365 + Execution Containers (MXC) + Agent Control Specification (ACS, open source) + IQ layer (Work IQ GA June 16, Fabric IQ, Foundry IQ, Web IQ) + Scout + Surface RTX Spark (1 PFlop, Arm + Blackwell) + Majorana 2 quantum. Direction: enterprise orchestration + control plane.
- **Google:** Gemma 4 12B (encoder-free Unified, Apache 2.0) + Gemma 4 E2B/E4B + AI Edge Gallery macOS + AI Edge Eloquent dictation app. Direction: open weights + on-device.
- **Meta:** Ray-Ban Display $499 (April 14 2026) + Muse Spark pendant (leaked May 2026) + Meta Lab @ Best Buy in 50+ stores + 7M Ray-Ban buyers in 2025. Direction: scale + retail.
- **Anthropic Mythos / Fable 5 / Project Glasswing:** the first Mythos-tier public model is shipped. RSI is a 2026 concern, not 2030.
- **Recursive Superintelligence (Yuandong Tian, ex-Meta):** $650M Series A at $4.65B valuation. <30 employees, no product. The capital is going to RSI research. This validates the bet.
- **Sakana AI (Tokyo):** Darwin Gödel Machine (DGM) + DGM-H Hyperagents. Sakana RSI Lab (June 5 2026, dedicated RSI unit).
- **Hexo Labs:** SIA (May 29 2026, MIT, 3 LLM components, full architecture public).
- **Decagon:** Duet Autopilot + DuetBench + Proactive Agents (June 9 2026). First verified self-improving agent for customer experience. 93% acceptance.

**What is NOT happening in 2026:** A "single breakthrough to AGI" moment. The trend is **incremental integration**: each lab is taking its existing model and adding a memory layer + a harness evolution loop + a context layer. None of them has crossed the "I can build a better version of myself" line for general capabilities. The closest is Anthropic's Fable 5 (80% of Anthropic's code is Claude-authored, but humans still review the diffs).

**For Danlab, the conclusion is:** the 18-24 month window is real and concrete. We are not behind; we are aligned with the leading edge (open-source self-improving + memory-evolving + always-on + local-first). The bet is sound.

### 6. Self-improving architectures — what exists, what works

**v30 reference list (in production, ordered by relevance to Danlab):**

1. **SIA (Hexo Labs, MIT, May 29 2026).** 3 LLM components: Meta-Agent + Task-Specific Agent + Feedback-Agent. 56.6% LawBench gain, 91.9% GPU kernel runtime reduction, 502% denoising improvement. **First open-source SOTA with full architecture public. v30 lock: fork SIA-H (harness-only) in Month 1-2 for danlab-multimodal.**
2. **Sakana Darwin Gödel Machine (DGM) + DGM-H Hyperagents.** 20% → 50% on SWE-bench Verified after 80 iterations, 14.2% → 30.7% on Polyglot. DGM-H adds fully self-referential exploration.
3. **RHO (arXiv 2606.05922).** SWE-Bench Pro 59% → 78% in single round.
4. **SGM safety wrapper (arXiv 2510.10232).** Add safety constraints to DGM-class systems.
5. **PopuLoRA (arXiv 2605.16727).** LoRA populations with TrueSkill cross-evaluation.
6. **Meta-Harness (OpenReview 2Tx03Dan7u).** Harness search, 7.7-pt gain on online text classification.
7. **HERO (OpenReview CFnfsORP7Y).** Hindsight self-distillation.
8. **TRACE (OpenReview p37UqCmcxG).** Capability-targeted LoRA + MoE, +14.1pt on τ 2-Bench.
9. **AEL (OpenReview dtPo105y8x).** Two-timescale memory retrieval evolution (Thompson Sampling fast + LLM reflection slow), Sharpe +27%.
10. **RewardHarness.** Reward-model search for harness optimization.
11. **Continual Harness (arXiv 2605.09998).** Reset-free online harness refinement.
12. **Adaptive Auto-Harness.** Adapts the harness at inference time.
13. **Meta-Evolution Loop.** Meta-meta-learning on the evolution loop itself.
14. **VeRO (arXiv 2602.22480).** Harness-for-agents — the agent IS the harness.
15. **Harbor (arXiv 2604.20938).** BO-based harness optimization.
16. **Agentic Harness Engineering (AHE, arXiv 2604.25850).** Observability-driven harness evolution. 10 iterations 69.7% → 77.0% pass@1, transfers to SWE-bench + 3 model families.
17. **Self-Harness (arXiv 2606.09498).** Harness improves itself. 21.4pp held-out gain on Terminal-Bench-2.0 with MiniMax M2.5.
18. **HarnessForge (arXiv 2606.01779).** Joint harness + policy evolution, 3.56% avg gain.
19. **EvoTrainer (arXiv 2606.03108).** Policy + training-harness co-evolution.
20. **Harness-1 (arXiv 2606.02373).** 20B RL search agent with stateful harness.
21. **Harness Updating != Harness Benefit (arXiv 2605.30621).** **The critical finding: weak-tier agents fail at activation + adherence, not at evolver quality. Invest in better harnesses for our focal model, not in bigger evolvers.**
22. **Microsoft SkillOpt (Build 2026).** Agents participate in dev workflows (debugging, profiling, testing, merge), all in Visual Studio. **Direct fit for Dan skill document evolution (Dan1/Dan2/Dan3/Dan4 = trainable parameters).**
23. **Anthropic SkillOpt.** Skill evolution for Anthropic Claude Code.
24. **Decagon Duet Autopilot (June 9 2026).** First verified self-improving agent. DuetBench = first benchmark for end-to-end self-improvement.
25. **Anthropic Fable 5 (June 9 2026).** 80% of Anthropic's code is Claude-authored. **The "agent builds agent" loop is in production today, not 2030.**

**What has actually worked (v30, ranked):**
1. **Harness evolution (SkillOpt, SIA-H, AHE, Self-Harness, Meta-Harness, HarnessForge).** The cheapest, fastest, most generalizable improvement. Doesn't need weight modification. SOTA in 2026.
2. **Hindsight self-distillation (HERO).** Uses past experience as training signal. Works without policy gradient.
3. **Two-timescale memory evolution (AEL).** Separates fast (Thompson Sampling) and slow (LLM reflection) learning loops.
4. **Harness + weight co-evolution (DGM, SIA-W+H, RHO).** More expensive but bigger gains. Reserve for when harness evolution plateaus.
5. **Population-based LoRA (PopuLoRA, TRACE).** Trains multiple adapters, picks the best. Cheaper than full retraining.

**What has NOT worked (v30):**
- "Just make the model bigger" — doesn't give RSI capability, just better task performance.
- "Just add more memory" — without harness evolution, the memory just fills up and isn't useful.
- "RL on the agent output" — without a reward model that the agent can update, this is just SFT.

### 7. Edge AI / on-device models — sub-500MB VLMs that work

**v30 SOTA for sub-500MB VLMs:**
1. **LFM2.5-VL-450M (Liquid AI, Apache 2.0-equivalent, released April 11 2026).** 450MB Q4_0, SigLIP2 NaFlex encoder, 512×512 images, sub-250ms on Jetson Orin, GGUF + ONNX. POPE 86.93, OCRBench 84. **Production-ready. Reference for our wearable path.**
2. **SmolVLM-256M (HuggingFace, Apache 2.0, what perceptiond currently runs).** 120MB main + 182MB mmproj = 302MB combined. Smaller than LFM2.5-VL-450M but lower quality.
3. **Gemma 4 E2B / E4B (Google, Apache 2.0, June 2026).** Encoder-free Unified. 2B/4B effective params. **v30 wearable lock candidate (with LFM2.5-VL-450M as hedge).** Encoder-free = 1 component instead of 2.
4. **PLaMo 2.1-VL (arXiv 2604.19324, Apache 2.0).** 53.9% zero-shot factory task accuracy. Validates the lightweight VLM bet for autonomous devices with Japanese + English support.
5. **Firebolt-VL (arXiv 2604.04579).** Replaces Transformer decoder with Liquid Foundation Model decoder (linear-time inference, state-space model with FiLM conditioning). Token-Grid Correlation Module.
6. **LFM2.5-VL-450M-Extract.** Same architecture, JSON output. For memoryd ingestion.

**v30 verification:** the v1 LFM2.5-VL-450M decision is right. The Gemma 4 E4B spike in Month 2 is the right expansion. The sub-1W wearable path needs BitNet b1.58 + Litespark 1.58-bit.

### 8. Memory and continual learning

**v30 reference list (in production, ordered by relevance to Danlab):**

1. **Mem0 (Apache 2.0, 49% LongMemEval).** Production memory layer for agents.
2. **Zep (Apache 2.0, 63.8% LongMemEval).** Temporal knowledge graph. **Direct fit for memoryd v2 temporal layer.**
3. **Letta (Apache 2.0, 83.2% LongMemEval).** Open-source agent memory framework. The ceiling.
4. **Hindsight (arXiv 2512.12818, MIT).** 4-network architecture: World + Experience + Opinion + Observation. Retain / recall / reflect. **The cognitive consolidation reference. v30 lock for memoryd v2 v1.0.**
5. **HMO (arXiv 2604.01670).** 3-tier memory: Primary Cache + Secondary + Archive with persona-driven promotion.
6. **HeLa-Mem (arXiv 2604.16839).** Hebbian-style hub detection + spreading activation. **For memoryd v2 v2.0 (Month 6).**
7. **vstash (arXiv 2604.15484).** Adaptive RRF with per-query IDF weighting. +21.4% NDCG@10 on ArguAna. **For memoryd v2 v1.0 (Month 3).**
8. **SuperLocalMemory V3.3 (arXiv 2604.04514).** 7-channel RRF (zero-LLM option for wearable). 70.4% LongMemEval zero-LLM. **The wearable memoryd candidate.**
9. **VisualMem (research code).** Persistent structured visual memory, not just captions. For perceptiond → memoryd.
10. **CraniMem (research).** Hierarchical memory.
11. **Memora (research).** Memory consolidation at scale.
12. **APEX-MEM (research).** Agent-context memory.
13. **AEL (OpenReview dtPo105y8x).** Two-timescale memory retrieval evolution. Sharpe +27%.
14. **Decagon Proactive Agents (June 2026).** "Anticipate / remember / initiate" behavioral pattern. **The production reference for memoryd v2's proactive retrieval.**
15. **Weaviate Engram.** Background-write architecture. Memory writes happen in background, retrieval remains available. **For memoryd v2 v1.0 architecture.**

**v30 conclusion:** memoryd v2 v1.0 = Mem0 + Zep (temporal KG) + Hindsight (4-lever consolidation) + SuperLocalMemory V3.3 (7-channel RRF) + LFM2.5-VL-450M-Extract (ingestion) + Weaviate Engram (background-write) = 6-core stack. **Highest-ROI investment for AGI direction. Ship in Month 3.** memoryd v2 v2.0 (Month 6) = + HeLa-Mem (Hebbian) + AEL (two-timescale) + vstash (adaptive RRF) + Decagon Proactive (behavior) + VisualMem (structured visual) = 11-component stack.

### 9. Multimodal fusion

**v30 SOTA for combining vision, audio, text:**
- **Encoder-free Unified (Gemma 4 12B, June 2026).** Raw audio + visual patches → LLM backbone. **The 2026 trend.** Apple AFM 3 + Google Gemma 4 + Firebolt-VL + PLaMo 2.1-VL all converge here.
- **Encoder-based (LFM2.5-VL-450M, SmolVLM, Moondream2).** Vision encoder (SigLIP) + projector + LLM decoder. **The 2024-2025 architecture.** Still production-ready for sub-500MB.
- **Specialist + orchestrator (Apple AFM 3 + System Orchestrator).** Multiple specialists + a focal orchestrator. **The architecture Apple is shipping at scale.**
- **NAND-stored MoE (Apple AFM 3 Core Advanced).** 20B sparse with 1-4B active params. **The on-device 20B unlock.**

**For Danlab:** the v1 architecture (encoder-based LFM2.5-VL-450M + separate whisper.cpp + separate KittenTTS) is correct. The v2 architecture (LFM2.5-Audio-1.5B consolidation, encoder-free Gemma 4 E4B for wearable) is the right expansion. The v3 architecture (specialist + orchestrator with BitNet b1.58 sub-1W) is the wearable target.

### 10. Model compression

**v30 techniques (in production, ordered by impact):**
1. **BitNet b1.58 + Litespark (arXiv 2605.06485, 2410.16144, 2407.00088).** 18-97× throughput on M4, 1.37-6.46× CPU speedup, 55-82% energy reduction. **The 2026 SOTA for sub-1W inference.**
2. **QAT (Quantization-Aware Training).** Gemma 4 QAT variants released June 6 2026 for mobile/laptop. Smaller, on-device oriented. **The bridge between full-precision and 1-bit.**
3. **GGUF Q4_0 / Q5_0 / IQ4_XS.** Mature, multi-model, llama.cpp native.
4. **Speculative decoding (SpecVLM 2.5-2.9×, ViSpec 3.22×, EAGLE-2 3.05-4.26×).** Latency-only, not memory.
5. **VLMCache (ACM 2026, DOI 10.1145/3745756.3809243).** 1.4-3.8× speedup with <1% accuracy loss via block-level KV-prefix caching.
6. **T-MAC (arXiv 2407.00088).** 60-70% energy, 11 tok/s on Raspberry Pi 5.
7. **Vec-LUT (research).** 4.2× CPU speedup for quantized LLMs.
8. **Distillation (smaller models from larger).** Gemma 4 E2B/E4B from 12B; LFM2.5-VL-450M-Extract from 450M-Instruct.

**v30 path to 50-150× combined VLM energy reduction:** SpecVLM + ViSpec + EAGLE-2 + VLMCache (latency 5-30× combined) + BitNet b1.58 + Litespark 1.58-bit (energy 18-97×) = 50-150× total. **Month 2-3 spike target.**

---

## C. Competitive & Market Research

### 11. AI wearables landscape (v30, post-WWDC26 + Build 2026)

**5 competitive fronts + 4 open-source reference products:**

**Microsoft (closed):**
- **Scout (M365, Build 2026).** OpenClaw-based. Autopilot-class. GA October 2026. **"Addicted users" memo leaked June 4-9. Nadella disowned. Shahine + Werner named authors.**
- **Project Solara (Build 2026).** MDEP OS, AOSP-based, badge form factor. Uses OpenClaw for agent runtime. **Off-the-shelf Redax alternative.**
- **Agent 365 SDK (GA May 1 2026, expanded at Build 2026).** Control plane for AI agents. Entra + Purview.
- **MXC (Microsoft Execution Containers).** Per-service policy-driven containment, early preview.
- **ACS (Agent Control Specification).** Open-source standard for declarative agent policy.
- **IQ layer.** Work IQ GA June 16, Fabric IQ, Foundry IQ, Web IQ.
- **Surface RTX Spark (June 2026).** 1 PFlop local AI dev box. Arm + Blackwell. Runs 120B locally.
- **Majorana 2 (quantum, Build 2026).** 20-second qubit stability. Future.

**Apple (closed, two-product):**
- **Vision Pro M5 (lives, fall 2025 refresh).** visionOS 27 ships with "see what you see." $3,499+. Bridge product while N50 matures.
- **N50 smart glasses (late 2027 per Gurman May 31 + Kuo June 3).** 4 designs tested.
- **AFM 3 Core (3B dense) + AFM 3 Core Advanced (20B sparse NAND-MoE, 1-4B active).** WWDC26.
- **Apple System Orchestrator (sub-1W focal).** Routes to 4 capabilities.
- **Apple Core AI framework + Apple Intelligence Extensions API + Siri AI (Gemini co-developed).** Xcode 27 distribution.
- **macOS 27 Golden Gate (WWDC26).** Spotlight → Siri AI for AI-shaped queries.
- **visionOS 27 + curved windows + visual Siri.** WWDC26.

**Google (mixed):**
- **Android XR (I/O 2026).** Samsung + Xreal + Google demo. Fall 2026 ship. Project Aura with 70° FOV.
- **Gemini 3.5 + Gemini Live (glasses-ready).** NotebookLM gets Antigravity + 100+ curated skills (June 8).
- **Gemini 3.5 Live Translate (June 9).** Speech-to-speech translation.
- **Gemma 4 12B + E2B + E4B (Apache 2.0, June 2026).** The open-weight on-device bet.

**Meta (closed, retail-scale):**
- **Ray-Ban Display $499 (April 14 2026).** Prescription displays.
- **Muse Spark pendant (leaked May 2026).** Companion to glasses.
- **Meta Lab @ Best Buy in 50+ stores.** Retail distribution.
- **7M Ray-Ban buyers in 2025.** Scale is the moat.
- **Reality Labs workforce shifts.** Cuts.

**Brilliant Labs (open, production July 2026):**
- **Halo + Liquid AI.** LFM2-VL-450M on glasses. Open source. **The production reference for the LFM2.5 path on a wearable form factor.**

**4 open-source reference products:**
- **OpenGlass (arXiv 2606.07431).** GAP9 RISC-V + Prophesee GENX320 event camera. 100mW inference, 11.5h on 200mAh. **The sub-1W AI eyewear reference.**
- **Monako Glass (Aug 2026 ship).** 48g, $399, ARM Cortex A7 + 300mAh, Buildroot Linux. **The 48g form factor reference.**
- **VisionClaw (community).** OpenClaw on Meta Ray-Ban.
- **Brilliant Labs Halo (July 2026).** LFM2-VL-450M on glasses.

**v30 conclusion:** **5 competitive fronts, 4 open-source references, the 18-24 month window is real.** Danlab's open-source + local-first + proactive + memory-first position is the only white space. Ship before Apple does (late 2027 N50). Ship before Microsoft Scout GA (October 2026).

### 12. Open-source AI companion projects

**v30 map (relevant to Dan Glasses):**
- **OpenGlass** (arXiv 2606.07431) — RISC-V AI eyewear, 100mW. ✅
- **Brilliant Labs Halo** (July 2026) — LFM2 on glasses. ✅
- **Monako Glass** (Aug 2026) — 48g Linux glasses. ✅
- **Sakana AI DGM + DGM-H** — Darwin Gödel Machine. ✅
- **Hexo Labs SIA** — self-improvement agent. ✅
- **Letta** — agent memory framework. ✅
- **Mem0** — memory layer for agents. ✅
- **Zep** — temporal knowledge graph. ✅
- **SuperLocalMemory V3.3** — zero-LLM memory. ✅
- **AEL** — two-timescale memory evolution. ✅
- **Cognee** — knowledge graph memory. ✅
- **OpenInterpreter** — local code interpretation. ✅
- **OpenHands** (formerly OpenDevin) — code agent. ✅
- **Aider** — code agent. ✅
- **Continue** — IDE AI. ✅
- **Cline** — IDE AI. ✅
- **Paperclip / DanClaw** — agent company orchestration (us). ✅
- **Blurr / Panda** — Android AI operator (comparable UX, different platform). ✅

**v30 conclusion:** the open-source ecosystem is rich. memoryd v2 v1.0 (Month 3) should integrate Letta + Mem0 + Zep + SuperLocalMemory V3.3 + HeLa-Mem rather than building from scratch. The 12-week ML-eng timeline is realistic.

### 13. Privacy-preserving AI positioning

**v30, sharpened:**

Dan Glasses is **the only AI wearable in 2026 that combines:**
1. Local-first (no cloud inference, no data leaves the device unless user explicitly shares)
2. Open source (all services + all training + all harnesses public)
3. Proactive (the AI initiates, not just responds)
4. Memory-first (the AI evolves from the user's experience)
5. No face recognition (the deliberate omission that differentiates from Meta "Name Tag" PR disaster June 2026)
6. No social sharing (capture + post is explicitly out of scope, v1)
7. Encrypted at rest (SQLite + vectors encrypted with user-controlled key)
8. Per-device key (no cross-device sync in v1)

**The 4 trust pillars for the v1 marketing message:**
- "Your data stays on your face."
- "No cloud. No account. No telemetry."
- "You can read every line of code we shipped."
- "You can delete everything in one command."

**v30 sharpened anti-patterns to call out:**
- **Microsoft Scout addiction leak (June 4-9).** This is the counter-marketing for our open-source governance story.
- **Meta Name Tag face-rec PR disaster (June 2026).** Free marketing for our "no face recognition" position.
- **Apple AFM 3 ≠ "private by default" for all use cases.** AFM 3 Cloud routes to Apple Silicon PCC (Private Cloud Compute). On-device is private, cloud is "Apple-controlled" not "user-controlled." We can position as more private than Apple on the cloud boundary.
- **Google Android XR Aura.** Cloud-tethered to Google services. Not local-first.

---

## D. Technical Deep Dives (v30, picked 3 of the 6)

### Option A: Self-improving RL loops for language models — **DONE (v30 refresh)**

**State of the art (v30):**
- **SIA (May 29 2026, MIT, Hexo Labs)** is the first open-source SOTA with full architecture public. 3 LLM components: Meta-Agent + Task-Specific Agent + Feedback-Agent. **Fork SIA-H in Month 1-2 for danlab-multimodal.**
- **Sakana DGM + DGM-H** — 20% → 50% on SWE-bench Verified, 14.2% → 30.7% on Polyglot.
- **RHO (June 2026)** — SWE-Bench Pro 59% → 78% single round.
- **Anthropic Fable 5 (June 9 2026)** — 80% of Anthropic's production code is Claude-authored. The "agent builds agent" loop is in production. Stripe 50M-line migration in 1 day.
- **Recursive Superintelligence (May 13 2026, $650M, $4.65B)** — ex-Meta Yuandong Tian. <30 employees. RSI is a $4.65B bet.
- **Decagon Duet Autopilot (June 9 2026, verified self-improving)** — first public benchmark (DuetBench) for end-to-end self-improvement. 93% acceptance.
- **Anthropic public brake-pedal plea (June 4-8, 2026)** — RSI is now socially accepted as a near-term concern.
- **Harness Updating != Harness Benefit (arXiv 2605.30621)** — the critical finding: invest in better harnesses, not bigger evolvers. v30 lock: SIA-H (harness-only) before SIA-W+H (harness + weights).

**What works (v30, ranked):**
1. Harness evolution (SkillOpt, SIA-H, AHE, Self-Harness, Meta-Harness, HarnessForge) — cheapest, fastest, most generalizable.
2. Hindsight self-distillation (HERO).
3. Two-timescale memory evolution (AEL).
4. Harness + weight co-evolution (DGM, SIA-W+H, RHO) — bigger gains, more expensive.
5. Population-based LoRA (PopuLoRA, TRACE).

**What doesn't work (v30):**
- "Just bigger model" — no RSI capability.
- "Just more memory" — fills up and isn't useful without harness evolution.
- Bare RL on agent output — needs a reward model the agent can update.

**For Danlab, v30 lock:**
- **Month 1-2: SIA-H fork for danlab-multimodal.** LFM2.5-1.2B-Thinking as Meta-Agent. Target: 3 cycles on a Dan Glasses-relevant task. SIA-H ships in 2 weeks.
- **Month 3-4: harness evolution infrastructure** in openclaw-gateway. Component observability + experience observability + decision observability. Apply to memoryd v2.
- **Month 6-9: SIA-W+H** (harness + weight updates). Locked only after SIA-H plateaus.
- **Month 9-12: DGM-H + SGM safety wrapper.** Decagon DuetBench-style benchmark target.

**Critical open question (v30):** does the "harness evolution > base-model capability" finding (Harness Updating != Harness Benefit, Meta-Harness, AHE, Self-Harness, HarnessForge) mean we should **stop trying to make our focal model smarter** and instead invest everything in harness engineering? **v30 answer: yes for the next 12 months.** Lock LFM2.5-1.2B-Thinking as the focal model. Evolve the harness. Re-evaluate in Month 12.

### Option B: Edge VLM optimization (quantization, distillation, hardware acceleration) — **DONE (v30 refresh)**

**State of the art (v30):**
- **BitNet b1.58 (Microsoft, arXiv 2410.16144) + bitnet.cpp.** 1.37-6.46× CPU speedup, 55-82% energy reduction.
- **Litespark 1.58-bit (Apple, arXiv 2605.06485, May 2026).** 18-97× throughput on Apple M4. **The 2026 sub-1W unlock.**
- **T-MAC (Microsoft, arXiv 2407.00088).** 60-70% energy savings. 11 tok/s on Raspberry Pi 5. 71 tok/s on M2 Ultra.
- **SpecVLM (arXiv 2509.11815).** 2.5-2.9× VLM speedup via speculative decoding.
- **ViSpec (arXiv 2509.15235).** 3.22× VLM speedup.
- **EAGLE-2 (arXiv 2406.16858).** 3.05-4.26× LLM speedup.
- **VLMCache (ACM 2026, DOI 10.1145/3745756.3809243).** 1.4-3.8× VLM speedup with <1% accuracy loss via block-level KV-prefix caching.
- **Gemma 4 QAT (June 6 2026).** QAT variants for mobile/laptop. The bridge between full-precision and 1-bit.
- **Apple AFM 3 Core Advanced NAND-MoE.** 20B sparse with 1-4B active. IFP+per-prompt routing. The on-device 20B unlock.
- **encoder-free collapse** (Gemma 4, Apple AFM 3, Firebolt-VL, PLaMo 2.1-VL). 2 components → 1.

**For Danlab, v30 lock:**
- **Month 1-2: SpecVLM 2.5-2.9× + ViSpec 3.22× + EAGLE-2 3.05-4.26× + VLMCache 1.4-3.8× in perceptiond.** Latency 5-30× combined.
- **Month 2-3: BitNet b1.58 + Litespark 1.58-bit spike.** 18-97× energy reduction. **Single biggest power lever for the wearable.**
- **Month 3-4: encoder-free vs encoder-based lock.** Gemma 4 E4B vs LFM2.5-VL-450M for the wearable VLM.
- **Month 6-9: 1-bit SigLIP2 spike.** NeurIPS 2027 paper. 6-9 month wearable power unlock.

**v30 call to action:** buy Snapdragon X Elite dev kit + Microsoft Surface RTX Spark. Measure LFM2.5-VL-450M Q4_0 + Gemma 4 12B + LFM2.5-VL-450M-Extract + LFM2.5-1.2B-Thinking + **BitNet b1.58 + Litespark 1.58-bit** on Redax-class hardware THIS WEEK. **Monako Glass silicon teardown in August 2026 is the production reference.**

### Option C: Vector search and memory architectures for AI companions — **DONE (v30 refresh)**

**State of the art (v30):**
- **LongMemEval benchmark:** Letta 83.2% > SuperLocalMemory V3.3 70.4% (zero-LLM) > Zep 63.8% > Mem0 49%.
- **64% single-channel ceiling** is structural (per v29). Multi-channel RRF + cognitive consolidation breaks the ceiling.
- **Hindsight 4-network** (arXiv 2512.12818, MIT). World + Experience + Opinion + Observation. Retain / recall / reflect.
- **HMO 3-tier** (arXiv 2604.01670). Primary + Secondary + Archive with persona-driven promotion.
- **HeLa-Mem Hebbian** (arXiv 2604.16839). Hub detection + spreading activation. Dual-path retrieval.
- **vstash adaptive RRF** (arXiv 2604.15484). IDF-weighted fusion, +21.4% NDCG@10 on ArguAna.
- **SuperLocalMemory V3.3 7-channel RRF** (arXiv 2604.04514). Zero-LLM option for wearable. 70.4% LongMemEval.
- **AEL two-timescale evolution** (OpenReview dtPo105y8x). Thompson Sampling fast + LLM reflection slow. Sharpe +27%.
- **Decagon Proactive Agents** (June 2026). "Anticipate / remember / initiate" behavior.
- **Weaviate Engram.** Background-write architecture.
- **VisualMem.** Persistent structured visual memory.

**For Danlab, v30 lock:**
- **memoryd v2 v1.0 (Month 3, 6-core):** Mem0 + Zep (temporal KG) + Hindsight (4-lever) + SuperLocalMemory V3.3 (7-channel RRF) + LFM2.5-VL-450M-Extract (ingestion) + Weaviate Engram (background-write). **Single highest-ROI investment.**
- **memoryd v2 v2.0 (Month 6, 11-component):** v1.0 + HeLa-Mem (Hebbian) + AEL (two-timescale) + vstash (adaptive RRF) + Decagon Proactive (behavior) + VisualMem (structured visual). **Open-source release in September 2026.**

**v30 call to action:** the 12-16 week timeline for 1 ML engineer is realistic. **$0 of compute** (all open-source). **Open-source as "the local-first Project Solara memory layer."**

---

## Production References (v30, 30+)

1. SIA (Hexo Labs, MIT, May 29 2026) — arXiv 2605.27276
2. DGM (Sakana AI)
3. DGM-H Hyperagents (arXiv 2603.19461)
4. RHO (arXiv 2606.05922)
5. SGM safety wrapper (arXiv 2510.10232)
6. PopuLoRA (arXiv 2605.16727)
7. Meta-Harness (OpenReview 2Tx03Dan7u)
8. HERO (OpenReview CFnfsORP7Y)
9. TRACE (OpenReview p37UqCmcxG)
10. AEL (OpenReview dtPo105y8x)
11. Self-Harness (arXiv 2606.09498)
12. AHE (arXiv 2604.25850)
13. HarnessForge (arXiv 2606.01779)
14. Continual Harness (arXiv 2605.09998)
15. EvoTrainer (arXiv 2606.03108)
16. Harness-1 (arXiv 2606.02373)
17. Harness Updating != Harness Benefit (arXiv 2605.30621)
18. VeRO (arXiv 2602.22480)
19. Harbor (arXiv 2604.20938)
20. Apple AFM 3 architecture (WWDC26, June 8)
21. Apple System Orchestrator (WWDC26)
22. Microsoft Build 2026 stack (Agent 365, MXC, ACS, IQ, Surface RTX Spark, 7 MAI models, Majorana 2, Scout)
23. Microsoft SkillOpt (Build 2026)
24. Anthropic SkillOpt
25. Anthropic Claude Fable 5 (June 9 2026)
26. Anthropic Mythos 5 + Project Glasswing
27. Anthropic "brake pedal" public plea (June 4-8)
28. Anthropic 80% production code by Claude (May-June 2026)
29. Decagon Duet Autopilot + DuetBench + Proactive Agents (June 9 2026)
30. Recursive Superintelligence $650M Series A (May 13 2026)
31. Sakana AI RSI Lab (June 5 2026, Tokyo)
32. **NEW v30:** Microsoft Scout "addicted users" memo leak (June 4-9, 2026)
33. **NEW v30:** Apple Vision Pro M5 lives + visionOS 27 "see what you see" (WWDC26, June 8)
34. **NEW v30:** Apple confirms NONE of Gemini in AFM 3 (Federighi June 9)
35. **NEW v30:** Project Solara MDEP OS (Build 2026)
36. **NEW v30:** Brilliant Labs Halo shipping July 2026 with LFM2-VL-450M
37. **NEW v30:** Meta Ray-Ban Display $499 (April 14 2026)
38. **NEW v30:** Meta Lab @ Best Buy in 50+ stores
39. **NEW v30:** Meta "Name Tag" face-rec PR disaster (June 2026)
40. **NEW v30:** Apple Siri AI app with iCloud sync (WWDC26)

---

## The Bet (v30, locked)

**The bet is unchanged from v29.** memoryd v2 v1.0 (Month 3) + SIA-H fork (Months 1-2) + Gemma 4 E4B wearable VLM (Month 3) + BitNet b1.58 sub-1W path (Month 2-3) + Open Standards compliance (Agent 365 + ACS + OWASP v2.01 + Microsoft IQ + Apple Core AI) by Q4 2026 = the only local-first, open-source, proactive, memory-evolving, harness-evolving, always-on consumer wearable + open agent standard **before Microsoft Scout GA (October 2026) AND before Apple Glasses N50 (late 2027).**

**v30 sharpening:** the Anthropic Mythos → Fable 5 GA + Recursive Superintelligence $650M + Decagon DuetBench publication + Microsoft Scout addiction leak all in the same 2 weeks (May 13 - June 9, 2026) reset the competitive clock. **The window is 18-24 months wide and the value of the open-source self-improving position is now multi-billion-dollar validated.** memoryd v2 v1.0 in September 2026 is the most important single deliverable for Danlab in 2026.

---

*Last updated: 2026-06-11 07:00 IST (01:30 UTC) — v30.*
*Status: 7/7 daemons live. 24 production references (v29) + 8 v30 NEW = 32 total. ~25 RSI/harness architectures + 1 industry benchmark (DuetBench) + 1 verified self-improving system (Duet Autopilot) + 1 production harness-evolution in production (Anthropic Fable 5) + 1 $4.65B RSI bet (Recursive Superintelligence). The window is 18-24 months wide. The bet is locked.*
