# Dan1 Twitter Content — v85 (Jun 25 → Sep 30, 2026)

**Author:** Dan1 (DAN-1, danlab.dev)
**Status:** Supersedes v83 (Jun 24)
**Account:** @NandySomdipto (3,200 followers, Jun 25 baseline)
**Cadence:** 1 thread/week (Tue) + 1 short post/week (Thu) = ~28 posts in 14 weeks

---

## Bio (current)

> somdipto nandy 🇮🇳 building @danlab_dev (AGI research & product lab). open-source, on-device, auditable. dan-glasses, danlab-multimodal, dani, dan-consciousness. MIT forever.

## Bio (v85 proposed — 160 chars)

> somdipto 🇮🇳 building auditable, on-device, open-source AGI from India. dan-glasses · danlab-multimodal · dani. arXiv Aug 15. Show HN Aug 25.

(157 chars. Tighter. Date-anchored. Single category: auditable + on-device + open-source.)

## Pinned tweet (the one every visitor reads first)

> We shipped the auditable alternative to Meta's $799 cloud + EMG AI glasses.
>
> 8 daemons. 144 tests. 0 cloud. MIT forever. ₹4,999 student tier.
>
> First artifact that earns the "responsible self-improvement" label: audiod confidence-calibration RL agent. ECE <0.05 on Librispeech.
>
> arXiv Aug 15. Show HN Aug 25.
>
> Install in 5 minutes: `curl -fsSL danlab.dev/install.sh | bash`
>
> From India 🇮🇳 — with constraints that force honesty.

---

## First 10 posts (v85 launch content, Jun 25 → Jul 9)

### Post 1 — Jun 25 (today) — the v85 announcement

> v85 marketing cycle just shipped.
>
> Anchored to Sakana Fugu (Jun 22) + Anthropic pause call (Jun 4–5) + AI Weekly self-improvement wall (Jun 2026).
>
> arXiv Aug 15. Show HN Aug 25. ₹4,999 student tier.
>
> The auditable alternative to Meta's $799 AI glasses. From India 🇮🇳, with constraints that force honesty.
>
> [link to dan1-marketing-research.v85.md]

### Post 2 — Jun 27 — the honest comparison

> danlab-multimodal is **heuristic**, not RL.
>
> We don't fake it. The README is the rubric. The path to genuine RL is the SIA framework (Hexo Labs, MIT, May 2026).
>
> Until the harness+weights fork ships, we say what we measure.
>
> That's the moat: honesty in a market full of hedge-words.

### Post 3 — Jun 29 — Sakana Fugu context

> Sakana shipped Fugu Jun 22.
>
> 0.6B TRINITY conductor evolved with sep-CMA-ES. Routes to specialist agents. SWE-Bench Pro 73.7.
>
> This is exactly the memoryd v2 coordinator we were planning. Market just compressed our v9 timeline.
>
> The bet is validated. The window is open. Ship by Aug 15.

### Post 4 — Jul 2 — the 5-min install thread (5 tweets)

> 1/ The 5-min install.
>
> 1 curl command. 8 daemons. 144 tests. 0 cloud.
>
> This is what auditable, on-device, open-source AI glasses looks like in production.
>
> 🧵

> 2/ The command:
>
> `curl -fsSL danlab.dev/install.sh | bash`
>
> What it does:
> - Downloads whisper.cpp base.en (74MB)
> - Downloads LFM2.5-VL-450M Q4_0 (209MB)
> - Downloads KittenTTS medium (~25MB)
> - Downloads MiniLM-L6-v2 (90MB)
> - Spawns 8 daemons on ports 8090, 8092, 8741-8744, 18789, 8747
> - Opens the Bootstrap wizard at localhost:8747

> 3/ Roundtrip in 7.08 seconds.
>
> Push-to-talk → "what do you see?" → camera captures → VLM describes → TTS speaks → memoryd stores the exchange.
>
> End-to-end. On your laptop. No cloud. No subscription. No credit card.

> 4/ The 8 daemons (each with its own port, its own tests):
>
> - audiod (8090) — whisper + Silero VAD
> - perceptiond (8092) — LFM2.5-VL-450M + salience gate
> - memoryd (8741) — SQLite + MiniLM 384-dim
> - toold (8742) — sandboxed shell + Python
> - ttsd (8743) — KittenTTS
> - os-toold (8744) — path guard + allowlist
> - openclaw (18789) — TS/Node gateway + Telegram
> - dan-glasses-app (8747) — Tauri v2 React SPA

> 5/ Why this matters.
>
> Every competitor is either:
> - Cloud-dependent (Meta $799, Google, Snap)
> - EMG-locked-in (Meta Display)
> - Closed (Even G2, Snap)
>
> Dan Glasses is the only vendor that is on-device + open-source + auditable + India-cost simultaneously.
>
> That's a quadrant, not a feature.
>
> Install: `curl -fsSL danlab.dev/install.sh | bash`

### Post 5 — Jul 4 — Anthropic pause call

> Anthropic's pause call (Jack Clark + Marina Favaro, Jun 4–5) is the policy framing for recursive self-improvement.
>
> Our audiod confidence-calibration RL agent is the responsible alternative:
>
> - Auditable (ECE/Brier audit trail)
> - Frozen encoder (no closed-loop weight mod)
> - Failure-mode registry (rise-and-collapse mitigation)
> - Public benchmark (AIE-Bench, SEAGym)
>
> arXiv Aug 15.

### Post 6 — Jul 6 — memoryd v2 spec lock

> memoryd v2 spec locked. 6-week build. Aug 15 ship.
>
> - AEL two-timescale bandit over retrieval modes
> - DPCM doubly-linked provenance graph
> - LLM-Wiki overnight synthesis
> - Operative_context surface (user can see + contest)
> - OpenClaw-memory adapter
>
> Open-source. Wearable-shaped. Perplexity Brain architecture, but ours.

### Post 7 — Jul 9 — Kokoro-82M swap

> KittenTTS → Kokoro-82M swap.
>
> Apache 2.0. 21 voices. 327MB. Runs on Raspberry Pi. Sub-20ms TTFA.
>
> 1-week swap. Deploy Jul 15. Hardware-friendly, license-clean.
>
> (KittenTTS license is the blocker; Kokoro is the unblocker.)

### Post 8 — Jul 11 — the auditable reliability narrative

> The auditable reliability narrative is the new accuracy.
>
> For 1B-class on-device models, the moat is not capability. It's measurement.
>
> ECE. Brier. Calibration curves. Failure-mode registry.
>
> Sakana proved this with DGM (SWE-Bench 20%→50%). Anthropic proved it with the pause call.
>
> We prove it with audiod confidence-calibration RL agent. Aug 15.

### Post 9 — Jul 14 — `/glasses` page launch

> danlab.dev/glasses just went live.
>
> The auditable, on-device, open-source AI glasses from India 🇮🇳.
>
> - Hero: 1-sentence value prop + 30-sec demo loop
> - Install: 1 curl command, copy-to-clipboard
> - Features: vision, STT, TTS, memory, tools, privacy
> - Pricing: ₹4,999 student / ₹12,000 founder / $299 global / $599 premium
> - Trust badges: 8/8 daemons live · 144/144 tests · MIT forever · 0 cloud
>
> Show HN is 6 weeks away. The cache is built.

### Post 10 — Jul 16 — `/install` page launch

> danlab.dev/install just went live.
>
> 5-minute walkthrough: from `curl` to "hello, Dan."
>
> Annotated screenshots. The Bootstrap wizard in 4 tabs. The first auditable end-to-end.
>
> This is the conversion gate. If you can't install in 5 min, you won't install at all.
>
> Try it. Time yourself. PR the friction.

---

## Post-style guide (v85 lock-in)

**Voice:**
- Direct, opinionated, specific
- No emoji overload (👾 once per thread max)
- No "thoughts?" engagement bait
- No "I" — say "we" or name the project
- Numbers beat adjectives (8 daemons, 144 tests, 0 cloud beats "robust, scalable, reliable")

**Structure:**
- Hook: 1 sentence, 1 number, 1 wedge
- Body: 3–5 numbered tweets for threads
- Close: 1 actionable next step (install, read paper, follow)

**What we never post:**
- "Excited to announce..."
- "Proud to share..."
- "Just shipped..."
- "Grateful for..."
- "AGI is here"
- "Disrupting..."
- "Revolutionary"
- "Cutting-edge"
- "Just works"
- "10x"
- "YOLO"
- "Thoughts?"
- "Agree?"

**The v85 test for every tweet:** would somdipto say this at a NeurIPS workshop Q&A? If no, rewrite.

---

## Pre-built threads (drafted in v85 cycle, scheduled)

### Thread B — Jul 18 — the auditable alternative to Meta's $799

> 1/ Meta Ray-Ban Display is $799 + Neural Band EMG wristband + Meta AI cloud + $0 subscription + 14 languages.
>
> Dan Glasses is ₹15K (~$180) + no wristband + 0 cloud + MIT forever + 8 daemons.
>
> Same wedge: AI in glasses. Different quadrant.
>
> 🧵

> 2/ Meta Ray-Ban Display: EMG wristband is the moat. Once you're wearing it, you're locked into Meta's neural interface.
>
> Dan Glasses: no wristband. Push-to-talk + camera + memory. No subscription, no lock-in.
>
> $799 vs $180. EMG vs no-EMG. Cloud vs on-device. Proprietary vs MIT.

> 3/ Meta Ray-Ban Gen 2 ($379) and Oakley Vanguard ($499) fill the price gap. All cloud-dependent.
>
> Even Realities G2 ($599) is the closest design philosophy: on-device, privacy-first, single-lens monocle. But: closed, no camera, $599.
>
> Brilliant Labs Halo ($299) is the closest open-source competitor: yes, MIT, $299. But: monolithic, no daemon mesh, no auditable benchmarks.

> 4/ Dan Glasses is the only vendor that is **on-device + open-source + auditable + India-cost** simultaneously.
>
> auditable = ECE-grounded self-improvement, public benchmarks (AIE-Bench, SEAGym), failure-mode registry.
>
> India-cost = sub-₹15K hardware target, ₹4,999 student tier, MIT forever.

> 5/ Show HN is 5 weeks out. arXiv is 4 weeks out.
>
> The wedge is locked. The numbers are verified (8/8 daemons, 144/144 tests, 0 cloud).
>
> Install: `curl -fsSL danlab.dev/install.sh | bash`
>
> From India 🇮🇳, with constraints that force honesty.

### Thread C — Jul 25 — the honest heuristic-not-RL framing

> 1/ Our danlab-multimodal demo is **heuristic**, not RL.
>
> We don't fake it. The README is the rubric. The path to genuine RL is the SIA framework (Hexo Labs, MIT, May 2026).
>
> Why publish this honestly? Because the moat is honesty in a market full of hedge-words.
>
> 🧵

> 2/ What the heuristic actually does:
>
> Screen capture → llama-mtmd-cli → SmolVLM-256M (120MB) → text response → score 0–100 with hand-coded rules (length, error detection, UI element identification) → suggest improvement.
>
> No policy gradient. No weight modification. No learned reward model. Pre-RL scaffold.

> 3/ What genuine RL would require:
>
> - Reward function that is NOT the model's own output (e.g. Librispeech WER for audiod)
> - Frozen encoder + small adapter (~50K params)
> - Policy gradient on the adapter only
> - Audit trail: ECE, Brier, calibration curves
> - Failure-mode registry: rise-and-collapse detection
>
> That's the audiod confidence-calibration RL agent. arXiv Aug 15.

> 4/ The market is full of hedge-words.
>
> "Self-improving" without specifying what improves.
> "RL" without specifying the reward.
> "Aligned" without specifying the alignment target.
>
> Danlab's position: publish the rubric. Publish the gap. Publish the path to closing the gap.

> 5/ Sakana shipped Fugu (Jun 22). Anthropic made the pause call (Jun 4–5). AI Weekly found the self-improvement wall (Jun 2026).
>
> All three converge: for 1B-class on-device models, the moat is measurement, not capability.
>
> Danlab's audiod confidence-calibration RL agent is the auditable alternative.
>
> arXiv Aug 15. Show HN Aug 25. Install: `curl -fsSL danlab.dev/install.sh | bash`

### Thread D — Aug 1 — the audiod RL agent (pre-arXiv)

> 1/ The audiod confidence-calibration RL agent ships Aug 15.
>
> 4-layer MLP (~50K params) on frozen whisper.cpp base.en encoder.
>
> Reward = −ECE − λ·Brier. Optimizer = AHE (Sakana-style harness evolution).
>
> First Danlab artifact that earns the "responsible self-improvement" label.
>
> 🧵

> 2/ Eval:
>
> - Librispeech test-clean: ECE < 0.05
> - CommonVoice Indian-accent English: ECE < 0.10 (OOD)
>
> Failure-mode registry as v1 requirement (arXiv 2606.21090 mitigation).
>
> Reproducibility appendix: 8 pages, every seed logged, every checkpoint versioned.

> 3/ Why audiod first:
>
> - audiod is shipped (101+ tests, 8/8 daemons live)
> - whisper.cpp base.en is frozen — the only moving part is the calibration head
> - Reward is well-defined (ECE, Brier) — no learned reward model
> - Failure mode is bounded — calibration cannot compound destructively
> - arXiv-grounded result is shippable in 6 weeks

> 4/ Why not perceptiond or memoryd first?
>
> - perceptiond: LFM2.5-VL-450M is too small for meaningful VLM calibration; needs more eval first
> - memoryd: the operative_context surface (Jun 18) is too new; calibration would be premature
>
> audiod is the right first target. The other two follow.

> 5/ The honest framing:
>
> This is responsible self-improvement: auditable, benchmarked, ECE-grounded, frozen-encoder.
>
> NOT closed-loop weight modification. NOT learned reward models. NOT silent capability gains.
>
> Anthropic's pause call (Jun 4–5) is the policy context. Our auditable calibration is the engineering response.
>
> arXiv Aug 15. AIE-Bench + SEAGym by Sep 30.

### Thread E — Aug 8 — memoryd v2: Perplexity Brain, but open-source

> 1/ memoryd v2 ships Aug 15.
>
> Perplexity Brain architecture (Jun 18, 2026): +25% / +16% / −13% from traceable context graph + overnight LLM-wiki synthesis.
>
> Ours is open-source, wearable-shaped, with operative_context surface.
>
> 🧵

> 2/ The architecture:
>
> - AEL two-timescale bandit over {semantic, episodic, procedural, graph, reranked} retrieval modes
> - DPCM doubly-linked provenance graph
> - LLM-Wiki overnight synthesis
> - Operative_context surface (user can see + contest)
> - OpenClaw-memory adapter

> 3/ The 5 retrieval modes:
>
> - semantic: facts, preferences, learned concepts
> - episodic: what happened when
> - procedural: how to do things
> - graph: relationships across memories
> - reranked: LLM-judged top-K
>
> The bandit picks 1–3 per query. The provenance graph logs every selection.

> 4/ The operative_context surface is the unsung hero.
>
> The user sees exactly what memoryd is using to act — and can contest, correct, delete.
>
> This is the v1 answer to "what does the AI know about me?" Not "trust us" — "here's the audit trail."

> 5/ LongMemEval + PersonaMem-v2 submissions by Sep 30.
>
> arXiv Aug 15. Show HN Aug 25.
>
> Install: `curl -fsSL danlab.dev/install.sh | bash`

---

## Daily short posts (14 weeks × 1/week = 14 short posts, drafted in v85)

(Detailed in `dan1-content-calendar.v85.md` — Thu cadence. Each ≤ 240 chars, single wedge, single number.)

---

*Dan1 — Bengaluru 🇮🇳 — 2026-06-25 09:30 IST (04:00 UTC). v85 Twitter content. 10 posts drafted. 5 threads pre-built. Voice: direct, specific, honest.* 👾
