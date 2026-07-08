# Danlab AGI Roadmap v6 — 6/12/24 Month Plan

**Author:** Dan2 (Research Agent) | **Date:** 2026-06-24 11:30 IST
**Status:** v6 — supersedes v1–v5
**Companion to:** `dan2-research-report.v6.md`, `dan2-architecture-review.v6.md`

> v6 north star: **Reliability is the new capability. Submit a reliability-aware audiod confidence-calibration RL agent to AIE-Bench + SEAGym by Sep 30, 2026.** Anthropic's Jun 4 2026 call for a global pause on recursive self-improvement makes this *the* timely contribution. Memory is engineering (memoryd v2). Smart glasses is commodity (Meta Glasses $299, Snap Specs $2,195, Google Android XR fall 2026). Danlab wins on **reliability + proactivity + on-device-first + India-cost**.

---

## 6-month plan (Jul – Dec 2026) — the verifiable reliability era

**North star:** audiod calibration RL agent with ECE < 0.05 on Librispeech + ECE < 0.10 on CommonVoice Indian-accent English (OOD). AIE-Bench + SEAGym submission. arXiv pre-print Aug 15, 2026. Failure-mode registry live. Operative-context surface live.

### Q3 (Jul – Sep 2026)

1. **audiod calibration RL loop** (12 weeks: 6 build + 6 eval) — Deep Dive A in research report
   - Fork SIA (Hexo Labs, MIT) or implement GRPO from scratch
   - 4-layer MLP calibration head on frozen whisper.cpp base.en encoder
   - Failure-mode registry: `failure_class ∈ {silence, music_overlap, OOD_accent, low_SNR, hallucinated_token}`
   - Eval: Brier + ECE on Librispeech, CommonVoice, TED-LIUM
   - **Target:** ECE < 0.05 on Librispeech test-clean, ECE < 0.10 on CommonVoice Indian-accent English (OOD)
   - **Early-stop:** arXiv 2606.21090 rise-and-collapse pattern — track ES (early-stop rule from CARE) and GRPO + ES combination
   - **Submission target:** AIE-Bench (ICML 2026) + SEAGym by Sep 30, 2026
   - **arXiv pre-print:** Aug 15, 2026

2. **memoryd v2 (AEL + DPCM + LLM-Wiki + operative_context) rebuild** (8 weeks, parallel) — Deep Dive C
   - int8 quantization (4× memory win)
   - DPCM doubly-linked provenance graph
   - AEL fast Thompson bandit over {semantic, episodic, procedural, graph, reranked} modes
   - Slow LLM reflection (nightly, opt-in)
   - LLM-Wiki reconsolidation (nightly, async, low-priority)
   - **operative_context table** (NEW v6) — what actually drives behavior
   - OpenClaw-memory-compatible adapter (ecosystem composability)
   - **Submit to LongMemEval + PersonaMem-v2** by Sep 30

3. **ttsd v2 — KittenTTS → Kokoro-82M swap** (1 week, parallel)
   - Apache 2.0 license, 21 voices, 24kHz, MOS 4.45, 327MB, runs on Raspberry Pi
   - 210× real-time on RTX 4090, sub-20ms TTFA on warm cache
   - Multi-engine router (Kokoro for English, Piper for non-English, MisoTTS for batch)
   - WebGPU in-browser option for v1.5 Tauri webview
   - **Deploy by Jul 15, 2026** (1-week decision, not a research project)

4. **VLM eval: LFM2.5-VL-450M vs OmniVLM-968M vs Gemma 3 4B** (2 weeks, parallel)
   - Run on perceptiond's existing test set
   - Measure watchful-mode queue depth + battery proxy
   - Apply V5e-0 self-speculative decoding (1.89× speedup, OpenReview 2026)
   - Eval CondenseVLM token condensation (training-free)
   - Decision by Aug 1, 2026; swap by Oct 1, 2026
   - **Default v2 wearable: OmniVLM-968M Q4_K_M** (9× token compression, ~1.1s/frame)

5. **Power-state machine on every daemon** (3 weeks, parallel)
   - Global `power_state` enum (`wakeful|watchful|drowsy|asleep`)
   - OpenClaw-coordinated transitions via heartbeat
   - perceptiond: `idle` actually unloads the VLM from RAM
   - audiod: `asleep` parks the capture thread
   - Deploy by Aug 15, 2026

6. **rewardsd (NEW service, AIE-Bench + SEAGym integration)** (2 weeks, parallel)
   - Ingests `(task, action, signal)` tuples
   - Produces learned policies
   - AIE-Bench harness integration
   - SEAGym harness integration (Terminal-Bench 2.0 + HLE)
   - Failure-mode registry write access
   - Deploy by Aug 30, 2026

7. **proactived (NEW service)** (3 weeks, parallel)
   - Calendar (CalDAV or Google Calendar) + location (opt-in) + time + email fusion
   - Reads operative_context from memoryd
   - Reads reliability from audiod (gates nudges during failure-mode events)
   - Outputs nudges to ttsd
   - OpenClaw tool exposure: `dan_proactive_*`
   - Deploy by Sep 15, 2026

8. **Show HN Aug 25** + India press placements (per Dan1 v82)
9. **arXiv pre-print by Aug 15** — audiod calibration RL + memoryd v2 + reliability framing
10. **First ICLR 2027 workshop submission by Sep 30** — "Reliability-Aware Self-Revising Agents for On-Device AI"

### Q4 (Oct – Dec 2026)

11. **Self-improving Paperclip agent** (6 weeks) — apply Socratic-SWE-style trace-derived skills pattern to paperclip's tool-calling substrate
12. **Open eval repo (dglabs-eval)** — public benchmark for audiod calibration + perceptiond salience + memoryd recall (AEL modes) + operative_context selection
13. **Hindi / multilingual support** — swap whisper-large-v3-turbo or SeamlessM4T-v2 for Indian-accent English + Hindi; eval SmolVLM-256M-Instruct multilingual vs Gemma 3 nano
14. **NDP200 wake-word integration** (per GAP_ANALYSIS.md) — on-device "Hey Dan"
15. **Hardware privacy switch** — camera off, mic off, LED configurable (v1.5 PCB)
16. **Dev-kit pre-orders Oct 25** (per Dan1 v82) + first 100 dev-kits shipped (India)
17. **AWS Bedrock AgentCore vs OpenClaw benchmark** — public numbers
18. **Tauri native bundle** — `cargo tauri build` for `.deb`/`.AppImage` (deferred from v5, hardware-target-dependent)

### Success criteria (6 months)

- [ ] ECE on audiod calibration < 0.05 on Librispeech test-clean
- [ ] ECE < 0.10 on CommonVoice Indian-accent English (OOD)
- [ ] **AIE-Bench + SEAGym submission with audiod agent scoring top quartile**
- [ ] arXiv pre-print published Aug 15, 2026
- [ ] **memoryd v2 deployed** with AEL + DPCM + LLM-Wiki + operative_context + OpenClaw-memory adapter
- [ ] OmniVLM-968M OR Gemma 3 4B live in perceptiond, inference <2s/frame
- [ ] **Kokoro-82M live in ttsd, sub-20ms TTFA**
- [ ] rewardsd live, AIE-Bench + SEAGym integration verified
- [ ] proactived live, audiod-reliability-gated
- [ ] Power-state machine on every daemon
- [ ] Failure-mode registry live
- [ ] `/reliability` endpoint on every daemon
- [ ] Show HN top-10 of the day
- [ ] Dev-kit pre-orders ≥ 100 (India) or $5K MRR

---

## 12-month plan (Jul 2026 – Jun 2027) — the on-device on-wearable era

**North star:** ship a hardware-tethered v1.5 of Dan Glasses with on-device VLM, on-device wake word, on-device AEL-shaped memory, on-device reliability-aware audiod. Meta Glasses at $299 (Jun 22 2026, Muse Spark, 14 languages incl. Hindi/Japanese/Mandarin/Korean, 8h battery), Google Android XR fall 2026, Apple AirPods+glasses (Bloomberg), Microsoft Scout (built on OpenClaw), Snap Specs standalone ($2,195, Jun 16 2026) — Dan Glasses must win on **reliability + proactivity + on-device-first + India-cost**.

### Q1 2027 (Jan – Mar)

19. **Hardware v1.5 prototype**
    - 400-450mAh battery (15-20hr)
    - JBD MicroLED single-eye display
    - 8MP camera (opt-in, hardware privacy switch)
20. **visiond v2** — VLM with proactive salience (perceptiond → visiond rename + new capabilities)
    - Trigger on "Hey Dan" wake word (NDP200)
    - Push-to-talk or wake-word activation
    - On-device VLM via OmniVLM-968M quantized to NPU
21. **proactived v2** — calendar + location + time + email fusion (Anthropic Dynamic Workflows pattern)
    - "Focus Mode" — user opt-in, speech-gated
    - Operative-context-aware (proactived only nudges when operative_context is high-confidence)
22. **memoryd v3** — federated learning opt-in (H-FedSL pattern)
    - Gradient sharing, no raw data ever leaves device
    - Federated calibration of audiod confidence head
23. **Public security audit** of memoryd v2 + proactived (third-party)
24. **ICLR 2027 Workshop on RSI** — submit paper on audiod calibration + memoryd v3 + operative_context

### Q2 2027 (Apr – Jun)

25. **Dani integration** — audiod agent and memoryd v2 ship as Dani skills
26. **HRM-Text-1B evaluation** — train and eval on Danlab's task suite, compare to LFM2.5-1.2B-Thinking. HRM-Text 1B is 84.5% GSM8K (NOT 84.7%), $1,500 training, May 18 2026 release, fully open-sourced (Sapient).
27. **Edge NPU bringup** — port OmniVLM-968M and HRM-Text-1B to Redax NPU
28. **Multilingual VLM eval** — SmolVLM-256M-Instruct multilingual vs Gemma 3 nano for Hindi
29. **OSS contribution** — contribute DPCM-inspired memoryd patterns back to OpenClaw as a plugin
30. **Dev-kit v2 production run** — 1,000 units for India + SEA
31. **Partnership or acquisition conversation** with Even Realities (only proactive AI competitor) OR with an Indian OEM (Tata, Reliance, Ola Electric)

### Success criteria (12 months)

- [ ] Hardware v1.5 prototype functional, 15hr+ battery
- [ ] On-device VLM <2s/frame on Redax NPU
- [ ] proactived v2 live, Focus Mode shipped
- [ ] memoryd v3 federated, opt-in
- [ ] HRM-Text-1B evaluated against LFM2.5-1.2B-Thinking baseline
- [ ] 2 ICLR/NeurIPS workshop submissions
- [ ] 2 arXiv pre-prints
- [ ] Dev-kit v2 production run (1,000 units)
- [ ] $20K MRR or 500 dev-kit pre-orders
- [ ] Public security audit published

---

## 24-month plan (Jul 2026 – Jun 2028) — the AGI thesis era

**North star:** publish a credible "audited, on-device, on-wearable, self-improving, reliability-aware" AGI thesis. Use the two years to integrate HRM-Text, OmniVLM-968M, AEL-shaped memory, SIA-style self-improvement, operative-context-aware proactived, and reliability-aware predictions into a single coherent system with public evaluations and a public safety audit.

### H2 2027 (Jul – Dec)

32. **Dani v2 — self-improving agent platform**
    - SIA fork integrated
    - Audiod agent, memoryd v3, paperclip agent as Dani skills
    - Public eval suite (dglabs-eval) v2
33. **HRM-Text-2B on-device** — train and quantize for Redax NPU. ($1,500 training cost basis suggests scaling beyond 1B is feasible with curated data.)
34. **memoryd v4 — cross-agent memory sharing** with provenance graph
35. **proactived v3 — calendar + email + voice intent fusion + proactive outreach (Focus Mode)**
36. **NeurIPS 2027 workshop submission** — "On-Device Self-Improving AI Wearables"
37. **First 10K units shipped** to India + SEA

### H1 2028 (Jan – Jun)

38. **Dani v3 — multi-agent orchestration** with Anthropic Dynamic Workflows pattern (executable JS orchestration)
39. **HRM-Text + LFM2.5 ensemble** — task routing by complexity
40. **Public third-party safety audit** of the full self-improvement loop (per Anthropic Jun 4 2026 pause proposal — Danlab's response is "audited self-improvement beats unverified acceleration")
41. **International expansion** — Japan, EU, US pilots
42. **NeurIPS 2028 main track submission** — "Audited Self-Improving Reliability Agents for Wearable AI"
43. **Series A or strategic partnership** with an Indian OEM (Tata, Reliance, Ola Electric) or Even Realities

### Success criteria (24 months)

- [ ] Dani v2 live with audiod + memoryd + paperclip as skills
- [ ] HRM-Text-2B on-device, <500ms inference
- [ ] 10K units shipped
- [ ] 1 NeurIPS main-track submission
- [ ] Public third-party safety audit published
- [ ] Series A closed or strategic partnership signed

---

## What we are NOT doing (and why)

1. **Not building our own foundation model.** HRM-Text is open (Sapient, May 18 2026, $1,500), LFM2.5 is open (Liquid AI), Gemma is open (DeepMind), OmniVLM-968M is open. The 2026 frontier is too expensive for a 2-person lab.
2. **Not competing on Meta's distribution.** Meta has 70%+ market share, Meta Glasses at $299 (Jun 22 2026, Muse Spark from Meta Superintelligence Labs), 14 new languages incl. Hindi. We compete on **on-device-first + open-source + India-cost + reliability** — they cannot match us here without abandoning their cloud-first business.
3. **Not chasing Apple.** Apple's AI AirPods + glasses (Bloomberg) means we should partner, not compete. Stay on Android XR + Tailscale + Tauri stack.
4. **Not deploying SIA before evaluating AIE-Bench first.** SIA is the right framework, but AIE-Bench is the right *measurement* — submit the audiod agent to AIE-Bench first, get a public number, then adopt SIA with the public baseline as proof of improvement.
5. **Not claiming "RL" without harness + weights modification.** The danlab-multimodal "pre-RL scaffold" framing is honest and credible. The audiod calibration RL agent is the first artifact that earns the "RL" label. Stay disciplined.
6. **Not pausing.** Anthropic's Jun 4 2026 pause call is for *frontier* labs accelerating RSI. Danlab is sub-1B on-device — the pause concern does not apply, and the audiod calibration work is the *opposite* of unverified acceleration: it ships with a public benchmark, a failure-mode registry, and an audit trail.

---

## Three "if this, then that" contingencies

1. **If AIE-Bench submission scores bottom quartile** → pivot to procedural memory (memoryd v2) as the v2 differentiator. Self-improvement is not yet ready for sub-1B models; the audiod calibration task may be too narrow. Alternative: submit memoryd v2 + AEL bandit to LongMemEval instead.
2. **If OmniVLM-968M eval beats LFM2.5-VL-450M by >2× watchful-mode throughput** → swap immediately, push hardware v1.5 dev-kit schedule forward by 3 months.
3. **If Anthropic ships Claude Code + A2A plugin ecosystem before Sept 2026** → adopt A2A for OpenClaw → Claude handoff, build Dan Glasses as an A2A node (not just an MCP server).

---

## v5 → v6 changes

1. **HRM-Text corrected: 84.5% GSM8K (not 84.7%), May 18 2026 release, $1,500 training cost, fully open-sourced.** v5 had minor drift on the GSM8K number; v6 is exact.
2. **arXiv 2606.21090 rise-and-collapse failure mode integrated into audiod RL agent design.** Early-stop + CARE-style belief revision. v6: audiod RL agent ships with a failure-mode registry as a first-class artifact.
3. **Operative Context surface (NEW v6) added to memoryd + proactived + UI.** Per OpenReview "Operative Contexts" 2026 framing — distinguish stored memory from operative context that drives behavior.
4. **`/reliability` endpoint on every daemon (NEW v6).** Typed contract: `{ece, brier, last_failure_class, fault_class_distribution}`.
5. **V5e-0 self-speculative decoding added to perceptiond v2 plan.** 1.89× speedup, zero training cost, applies on top of any VLM.
6. **CondenseVLM + QViD token condensation added to perceptiond v2 plan.** Training-free, halves encoder time.
7. **proactived and rewardsd given full architecture specs (NEW v6).** v5 mentioned in passing; v6 specifies endpoints, OpenClaw tool exposure, failure-mode registry access.
8. **Meta Glasses confirmed at $299 (Jun 22 2026) with Muse Spark from Meta Superintelligence Labs.** 14 new languages including Hindi/Japanese/Mandarin/Korean. v6 sharpens the competitive framing.
9. **Anthropic Jun 4 2026 global pause call integrated into the narrative.** Danlab's audiod calibration work is *the* alternative to unverified RSI acceleration: public benchmark + failure-mode registry + audit trail.
10. **Show HN Aug 25, 2026 (per Dan1 v82) is the v6 commitment date.** arXiv pre-print by Aug 15. AIE-Bench + SEAGym submission Sep 30.

— Dan2, 2026-06-24 11:30 IST
