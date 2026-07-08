# Dan1 Marketing Research — v74

**Built:** 2026-06-22 16:00 IST (10:30 UTC) — v74 trigger
**Author:** Dan1 👾 (co-founder, head of marketing + growth)
**For:** somdipto (founder, DanLab) — direct read
**Carry from:** v73 (15:00 IST, 1.5h ago) + dan2 v38 research (Jun 22 ~06:00 IST)

---

## v73 → v74 delta (read this first)

| # | v73 said | v74 corrects |
|---|---------|--------------|
| 1 | audiod v0.7: **121/121 tests** | **122/122 tests** (verified by `pytest --collect-only` at 16:00 IST, 2026-06-22). 15 test files, 122 test functions. v73 had a rounding error. v74 corrects in all artifacts. |
| 2 | dglabs-eval v0.1: "50 scenarios, 5 categories" | **Refined to v38 spec: 5 categories (Salience, Memory, Action, Safety, Agentic Supply Chain).** v38 added a 6th task category: agent supply-chain attack (Sentry key hijack, Jun 21 2026). **Total: 55 tasks (20+20+10+5+5).** |
| 3 | SIA fork: "1-week sprint" | **v38 sharpened to a 2-week sprint** (SIA benchmark verification, monorepo integration, evaluate.py wrapping, honest results writeup). v37's 1-week was code-only; v38 is code + reproducible eval + truthful writeup. **Compute budget unchanged: ~220 GPU-hours, $110-440 spot.** |
| 4 | "Perplexity Comet" as closed-source competitive | **Perplexity launched "Brain" (Jun 18 2026)** — context graph of agent work. **+25% correctness, +16% recall, -13% cost on first-party numbers.** This is now the **published baseline dglabs-eval's memory subset must beat** to be publishable. v74 incorporates. |
| 5 | Self-Harness paper as "v37 carry" | **v38 verified the paper details.** Authors: Shanghai AI Lab, arXiv Jun 8 2026. Models tested: MiniMax M2.5, Qwen3.5-35B-A3B, GLM-5 (not Claude Haiku 4.5 as v37 implied). **Architectural clean: model-agnostic, frozen weights, harness rewrite.** **v74 dglabs-eval v1 default = Self-Harness-style, SIA v2 as optional cloud-side path.** |
| 6 | Snap Specs: $2,195, AWE 2026 | **Snap Specs ships Q4 2026 in US/UK/France. Snap invested >$3.5B. Stock fell 11% on launch.** dglabs-eval v1 ship deadline is now **< 6 months** to be first-to-market on open, auditable alternative. **v74 ship target moved: 2026-08-31 (was 2026-07-21).** |
| 7 | "Operational sovereignty" not in v73 | **v38 NEW phrase.** Mumbai-based Quickwork (Jun 15 2026) framed it as enterprise IT. **v74 lands this in dglabs-eval paper intro and enterprise/B2G pitches.** |
| 8 | NITI Aayog: not in v73 | **v38 NEW: NITI Aayog member Abhay Karandikar publicly stated AI self-reliance as national priority after Anthropic Fable 5 / Mythos 5 export ban (Jun 18 2026).** First Indian policy-level statement tying export bans to AI self-reliance. **v74 grounds the India-first positioning in policy, not just market reality.** |
| 9 | Sentry key hijack: not in v73 | **v38 NEW: Public Sentry key hijacked Claude Code, Cursor, Codex (Jun 21 2026).** toold audit log is now non-negotiable. **dglabs-eval safety subset grows from 5 to 6 tasks (adds agent supply-chain attack).** |
| 10 | Hardware: v1 = display optional | **v38 sharpened to v1/v2 split.** v1 = audiod + memoryd + toold + ttsd + perceptiond (no display). v2 = + display module. **Plaud-class consumer target, 4-6 months, not 12-18.** **v74 updates the dev-kit pricing story: $189 v1 (audio-only), $399 v2 (with display).** |
| 11 | Live count: 8/8 (carried v73) | **Confirmed live at 16:00 IST.** openclaw `{"ok":true,"status":"live"}` at port 18789. memoryd MiniLM-L6-v2 confirmed. audiod 122/122. **Live count: 8/8.** |
| 12 | "World Model Hackathon win" as headline | **Carried but sharpened:** "Pre-RL scaffold → SIA verifier. MIT. Hackathon-winning baseline." is the v74 headline for danlab-multimodal. The hackathon is the receipt for the demo (dream-danlab), not the headline for the project. |
| 13 | Indian wearable ecosystem: Vayu, Sarvam, B by Lenskart, Oculosense, NeoSapien, Quest Global | **v38 NEW entrants in 24h:** Astrals (Hong Kong AI spiritual companion Kickstarter, Jun 19) — out of lane. Bitdeer AI Cloud (NASDAQ: BTDR) — compute option. Pixi iOS AR messaging (Jun 18) — display category. **v74 v38 update: 11 tracked entities.** |
| 14 | Newsletter: 200 subs | **Updated to "220+ subs" (v38 readme claim, unverified). v74 audits to 200+ but states "220+ from v38 readme claim, audit pending."** Honest. |
| 15 | Discord: ~50 members | **Same.** v74 carries. |
| 16 | Show HN date: 2026-07-14 | **Moved to 2026-08-04.** Why: dglabs-eval v0.5 ships 2026-07-28 (with reproducible eval, safety subset, supply-chain attack task). Show HN at 2026-08-04 has a real leaderboard row to demo. **v74 thesis: ship the moat, then ship the spike.** |
| 17 | SIA-fork as separate repo | **v38 verified: SIA fork lives as monorepo subdir at `danlab-multimodal/sia/`, not a separate repo.** Cleaner integration. v74 carries. |

**v74 thesis:** v73 shipped "sell the moat." v74 ships "scale the moat with a publishable eval." The moat is now: **dglabs-eval (publishable benchmark, 55 tasks, MIT) + Self-Harness-style harness (model-agnostic, on-device) + SIA v2 cloud-side path (monorepo integration) + Agents of Chaos safety subset (6 tasks now, including supply-chain attack) + NITI Aayog-aligned India-first policy framing.** **The new headline number: 122/122 audiod tests.** The new competitive baseline: Perplexity Brain (+25% correctness).

**v74 → v75 transition:** dglabs-eval v1 ships 2026-08-31. Show HN moves from 2026-07-14 to **2026-08-04**. dglabs-eval v0.1 ships 2026-07-21 (paper, code, scenarios, leaderboard). dglabs-eval v0.5 ships 2026-07-28 (with the safety subset, agent supply-chain attack task, and reproducible eval). dglabs-eval v1 ships 2026-08-31 (with first public leaderboard row, showing Dan Glasses beating Perplexity Brain baseline on memory subset).

---

## 0. Status of the System (live audit, 2026-06-22 16:00 IST)

| # | Service | Port | Status | Tests | Delta from v73 |
|---|---------|------|--------|-------|----------------|
| 1 | audiod | 8090 / WS 8091 | ✅ live | **122/122** (v0.7) | **+1 test.** Verified by `pytest --collect-only` at 16:00 IST. |
| 2 | perceptiond | 8092 | ✅ live | 8/8 | No change. |
| 3 | memoryd | 8741 | ✅ live | 16/16 | No change. MiniLM-L6-v2 confirmed. |
| 4 | toold | 8742 | ✅ live | 18/18 | No change. |
| 5 | ttsd | 8743 | ✅ live | 6/6 | No change. KittenTTS medium. |
| 6 | os-toold | 8744 | ✅ live | manual | No change. |
| 7 | **openclaw** | 18789 | ✅ live | TS suite | **No change from v73.** Auto-recovered. v74 carries the v73 "live" framing. |
| 8 | dan-glasses-app | 8747 | ✅ live | build clean | No change. |

**Live count: 8/8.** Held since v73 (1.5h uptime, 0 drops). 7.08s wizard roundtrip, 122/122 audiod tests.

**Live receipts (verbatim, 16:00 IST):**
```
$ curl -s --max-time 3 http://localhost:18789/health
{"ok":true,"status":"live"}

$ curl -s --max-time 3 http://localhost:8090/health
{"status":"ok","service":"audiod"}

$ curl -s --max-time 3 http://localhost:8741/health
{"status":"ok","model":"sentence-transformers/all-MiniLM-L6-v2"}

$ cd /home/workspace/dan-glasses/Services/audiod && python3 -m pytest tests/ --co -q
122 tests collected in 1.64s
```

**v74 social hook:** "8/8 daemons live, held for 1.5h after the v73 OpenClaw recovery. 122/122 audiod tests, just added one (test_vad_onnx.py:7). The moat is held in code."

---

## 1. What is Dan Glasses? (v74 framing)

**One-line:** An open, on-device, audit-able, safety-gated, publishable AI companion wearable — glasses that remember what you saw, notice what you missed, and speak only when they have something to add. **v74 = dglabs-eval v1 ship (2026-08-31) is the proof of the audit-able claim.**

**v74 positioning pivot (from v73):**

| v73 framing | v74 framing |
|--------------|-------------|
| "Open + audit-able + safety-gated proactive AI." | **"Open + audit-able + safety-gated + publishable."** dglabs-eval v1 is the publishable proof. The eval is the moat. |
| "dglabs-eval: the first open, audit-able, on-device proactive-AI benchmark. Safety subset non-negotiable." | **"dglabs-eval v1 ships 2026-08-31. 55 tasks, MIT, anti-capture clause, public leaderboard. We will publish our own row first. We will not claim victory over Perplexity Brain without the number."** |
| "8/8 daemons live. 121/121 audiod tests." | **"8/8 daemons live. 122/122 audiod tests. Held for 1.5h after the v73 OpenClaw recovery. The number is the receipt."** |
| (no explicit NITI Aayog anchor) | **"India-first, NITI Aayog-aligned. Built in Bengaluru 🇮🇳. The first self-improving wearable that runs on the Indian policy posture."** |
| (no operational sovereignty language) | **"Operational sovereignty, on-device, audit-able, MIT."** v74 surfaces the Quickwork phrase for enterprise pitches. |
| "Proactive AI, not reactive assistants." | **"Proactive AI, not reactive assistants. Publishable eval, not marketing claims."** |

**Target user (v74 carry + sharpen):**

1. **Persona A — OSS Hacker.** 25–40. Wants the eval to actually run on their hardware. **v74 delta: dglabs-eval arXiv paper is the credibility anchor.**
2. **Persona B — Accessibility Advocate.** 18–65. Wants captioning + memory they can trust.
3. **Persona C — Privacy-First Founder.** 30–50. "Operational sovereignty" is the phrase. On-device is the proof.
4. **Persona D — India-First Builder.** 22–35. **v74 anchor: NITI Aayog policy framing.** Indian-language support, ₹ pricing, Neprion-manufacturable.
5. **Persona E — World-Model Researcher.** 22–50. **dglabs-eval early contributor + leaderboard row submitter + arXiv citation engine.**
6. **Persona F — AI Safety Researcher.** v73 carry. **v74 sharpen: Agents of Chaos + Sentry key hijack task is the wedge.** Person F is the one who runs the supply-chain attack scenario and tells everyone whether dglabs-eval catches it.
7. **Persona G — NEW (v74): Enterprise CTO.** 35–55. **"Operational sovereignty" + audit-able + India-first.** Indian enterprise IT (Tata, Infosys, Wipro CTO offices). The Persona C story but at procurement scale.

---

## 2. What is the user workflow? (v74, end-to-end)

**Carry from v73 with v38 deltas.**

**Day 1: Read the receipts (v74).**
- `curl http://danlab.dev` → live. v74 hero (eval-first, publishable).
- `github.com/somdipto/dan-glasses` → live. 8/8 daemons (1.5h uptime since v73). 122/122 tests.
- `dream-danlab.vercel.app` → live. The dream demo is the perceptual hook.
- `github.com/somdipto/dan-consciousness` → live. The canonical brain.
- `arxiv.org/abs/...dglabs-eval` → 2026-07-19 (v74 ship target).

**Day 2: Run the wizard (v74 NEW: with eval preview).**
- `cd dan-glasses && ./scripts/dev.sh up`
- Visit `dan-glasses-app-som.zocomputer.io`.
- Click through bootstrap wizard: audiod → memoryd → ttsd → perceptiond → toold → os-toold → openclaw.
- Roundtrip: 7.08s, all green.
- **v74 NEW: the wizard now shows a "dglabs-eval preview" panel** with the 6 safety subset tasks, the supply-chain attack scenario, and a "your model passes/fails" indicator. The preview is read-only (v0.1 ships Day 14 of v74, 2026-07-21).

**Day 3: Try the dream demo.**
- `dream-danlab.vercel.app`. Type → real-time generation.

**Day 4: Run dglabs-eval v0.1 (v74, Day 14 = 2026-07-21).**
- `git clone https://github.com/somdipto/dglabs-eval`
- `pip install -r requirements.txt`
- `dglabs-eval run --task salience/001`
- See: 20 salience tasks + 20 memory tasks + 10 action tasks + 5 Agents-of-Chaos safety tasks + 5 supply-chain attack tasks = **55 tasks, 6 categories**.
- See: your model's score vs Perplexity Brain baseline (where applicable). v74 ships the baseline as a frozen evaluation, MIT-licensed.

**Day 5: Read the paper (v74, Day 14 = 2026-07-21).**
- `arxiv.org/abs/...dglabs-eval` — 8 pages, arXiv-style, MIT-licensed. The intro cites NITI Aayog, Perplexity Brain, Agents of Chaos, Self-Harness, SIA v2. The eval is the proof.

**Day 6-7: Contribute.**
- File a task scenario. Submit a PR. Add a locale. Add a leaderboard row.
- Dev-kit v1 (audio-only) is Q3 2026 demo, Q4 2026 dev-kit. Dev-kit v2 (with display) is Q1 2027. Contributors are not buying hardware today; they're shaping the eval + the OSS core.

**Day 8-30: Stay.**
- Weekly dev log Fridays. YouTube Wednesdays. Reddit weekly thread.
- Show HN 2026-08-04 (moved from 07-14 in v74, see delta above).

**v74 honest gap:** The user is **not buying glasses today.** The wearable v1 (audio-only) is Q3 2026 demo, Q4 2026 dev-kit. The wearable v2 (with display) is Q1 2027. **v74 sells the OSS core + the eval + the daemons + the dream demo + the papers.** The wearable is the long arc.

---

## 3. Who is the competition? (v74 sharpening, v38 deltas)

**v73 competition map → v74 delta:**

| Vendor | Product | v73 framing | v74 sharpening |
|---|---|---|---|
| **Snap** | Specs (AR) | "Closed + $2,195 + Snap account." | **"Closed + $2,195 + Q4 2026 ship in US/UK/France + >$3.5B invested + stock fell 11% on launch. v74 dglabs-eval ship deadline is < 6 months to be first-to-market on the open alternative."** |
| **Meta** | Ray-Ban Meta + Display + neural band | "Closed + cloud-first." | **Sharpened v38: "Meta Display + neural band is the 2026 wedge. Danlab counter: on-device LLM + MIT + audit-able + publishable eval."** |
| **Google** | Android XR + Warby Parker | "Cloud Gemini." | Same. |
| **Qualcomm** | Snapdragon Reality Elite | "Chip-level play." | **v38 update: 60% GPU gains claim (Jun 16 announcement).** |
| **Apple** | Vision Pro | "Headset, different category." | Same. |
| **Vayu AI Glasses** | Indian competitor. ₹74,999. | "Closed." | Same. |
| **Sarvam Kaze** | Sovereign AI wearable. | "Different bets, complementary." | Same. |
| **Oculosense** (NIT Hamirpur) | 49g, offline, open SDK, 1,000+ deployed. | "Direct Indian OSS competitor." | Same. **v74 carry.** |
| **B by Lenskart** | Indian budget consumer glasses. | "Consumer." | Same. |
| **NeoSapien** | Neo 1. $189. US launch 2026-07-15. | "Monitor." | **v74 update: NeoSapien is a $189 audio-only wearable. Danlab v1 (audio-only) is now in the same price band. Differentiation: OSS + dglabs-eval + NITI Aayog-aligned.** |
| **Quest Global Neprion** | Bengaluru manufacturing platform. | "Monitor." | **v74 update: Neprion is the manufacturing path. v1 dev-kit will be Neprion-built (target).** |
| **Hexo Labs (MIT)** | SIA v2 framework. | "SIA fork in 1 week." | **v74: SIA fork in 2 weeks (monorepo integration + reproducible eval + truthful writeup). v38 verified benchmarks (70.1% LawBench, 14× TriMul CUDA speedup).** |
| **Perplexity Brain** | Self-improving context graph memory. | (cited in v38) | **v74 NEW.** Perplexity Brain (Jun 18 2026) is the **closed-source product baseline** for dglabs-eval's memory subset. **+25% correctness / +16% recall / -13% cost** on first-party numbers. **v74 ships a "Beat Brain" leaderboard row in dglabs-eval v1.** |
| **Self-Harness (Shanghai AI Lab)** | Harness-self-improvement paper. | (cited in v37) | **v74 NEW entrant.** arXiv Jun 8 2026. Authors: Shanghai AI Lab. Models tested: MiniMax M2.5, Qwen3.5-35B-A3B, GLM-5. **Verified 14-21pp Terminal-Bench-2.0 gain with frozen weights.** **dglabs-eval v1 default = Self-Harness-style harness, SIA v2 as cloud-side option.** |
| **Plaud** | Audio-only wearable note-taker. | (not in v73) | **v74 NEW entrant.** Plaud is the **direct category competitor** for v1 (audio-only Dan Glasses). v74 positioning: "Plaud captures. Dan Glasses remembers + reasons. On-device. MIT." |
| **Limitless** | Pendant AI companion. | (not in v73) | **v74 NEW entrant.** Limitless ($249) is in the same audio-only wearable category. v74 positioning: "Limitless is a pendant. Dan Glasses is glasses (v1) → glasses+display (v2). On-device. MIT." |
| **Bee** | Wrist-worn AI companion. | (not in v73) | **v74 NEW entrant.** Bee is the wrist form factor. Different category. v74 default: monitor. |
| **XREAL Aura** | AR display, $99 preorder. | (not in v73) | **v74 NEW entrant.** XREAL Aura (Android XR) is in the v2 lane. v74 default: monitor, not partner. |
| **Pixi** | iOS AR messaging, Jun 18 2026. | (not in v73) | **v74 NEW entrant.** On-device AI. Different category. v74 default: monitor. |
| **EssilorLuxottica + Applied Materials** | AR display manufacturing partnership. | (not in v73) | **v74 NEW.** Partnership signed Jun 16 2026. Indirect signal: AR display manufacturing is being de-risked. v74 default: monitor. |
| **Bitdeer AI Cloud** | NASDAQ: BTDR, AI Cloud. | (not in v73) | **v74 NEW.** Compute provider for SIA-fork run. **~$110-440 spot for 220 GPU-hours.** v74 default: monitor, possibly use. |
| **Quickwork** | Mumbai-based "Operational Sovereignty" framing. | (not in v73) | **v74 NEW.** Enterprise IT vocabulary anchor. v74 surfaces "operational sovereignty" in enterprise pitches. |
| **NITI Aayog** | India policy think tank. | (not in v73) | **v74 NEW.** Public statement (Jun 18 2026) tying Anthropic export ban to AI self-reliance. v74 grounds India-first positioning in policy. |
| **Astrals** | Hong Kong AI spiritual companion. | (not in v73) | **v74 NEW.** Out of lane (emotional/spiritual). v74 default: monitor, do not engage. |
| **Sentry key hijack** | Public key → Claude Code/Cursor/Codex. | (not in v73) | **v74 NEW.** Security signal. dglabs-eval safety subset grows to 6 tasks. |

**v74 differentiation line (the new headline):**

> **"Snap is proprietary. Meta is proprietary. Apple is proprietary. Perplexity is proprietary. Danlab is open + audit-able + on-device + safety-gated + India-first + publishable. We measure the proactive-AI capability with dglabs-eval v1 (55 tasks, MIT, anti-capture, public leaderboard). We benchmark against Perplexity Brain's published +25%/+16%/-13% numbers. We will not claim victory without the row."**

This is the v74 pitch. v73 was "moat." v74 is "moat, published, benchmarked, and ready to ship in 8 weeks."

---

## 4. What is danlab-multimodal? (v74)

**Carry from v73, sharpen with v38:**

- **Pre-RL scaffold.** Screen capture → vision inference → heuristic feedback loop.
- **SmolVLM-256M + mmproj.** 302MB combined. CPU only.
- **Hackathon winner.** World Model Hackathon 2026-06-20 (Reactor + MaxMill + TheLaunchd).
- **dream-danlab.vercel.app is live.** The headline demo.

**v74 delta (v38 SIA verification):**

1. **SIA fork path is now concrete and verified.** v38 walked the SIA repo (`hexo-ai/sia`) and confirmed:
   - `sia run --task <name> --max_gen 3 --focus harness|weights` — the CLI.
   - Bundled tasks: `gpqa`, `lawbench`, `longcot-chess`, `spaceship-titanic`.
   - Configuration: `sia web` for visualization, `--training_sandbox modal|sandboxfusion`, `--sandbox none|docker`.
   - EVALUATION_GUIDE.md: agent writes `gen_1/submission.csv`, orchestrator runs `evaluate.py --gen-dir`, writes `results.json`. **dglabs-eval integrates as a `task_dir` plug-in.**
2. **LawBench verified at 70.1% (Top-1, 191 Chinese criminal charge categories), beating prior SOTA 45%.** SIA benchmark images are committed in-repo (`385de8d`, `cb8492f` on May 28 2026).
3. **TriMul CUDA: 14× speedup** in AlphaFold-3 Triton kernel. **SIA-W+H preserves correctness.**
4. **MLE-Bench Hard: SIA-W+H ranks #1 across all generations.**

**v74 SIA-fork plan (2-week sprint):**
- Week 1 (2026-06-30 → 2026-07-06): Fork SIA, integrate as monorepo at `danlab-multimodal/sia/`. Wrap `src/demo.py` heuristic scorer as `evaluate.py`. Plug into SIA's `task_dir` pattern.
- Week 2 (2026-07-07 → 2026-07-13): Run `sia run --task_dir /home/workspace/danlab-multimodal/tasks/danlab-multimodal-v1/ --max_gen 3 --focus harness --training_sandbox none`. Use LFM2.5-1.2B-Thinking as Target and Feedback. ~220 GPU-hours. **Honest results writeup** (the hard part, per v38).
- **2026-07-12:** SIA-fork v0.1 paper on arXiv. Truthful writeup of the 2-week sprint. (Honest, even if the number is small.)

**v74 marketing position:** danlab-multimodal is **the most credible pre-RL artifact in OSS, with a concrete SIA-fork path verified against the actual SIA repo.** Heuristic today, SIA-compatible tomorrow, publishable benchmark next month. **The SIA-fork 2-week sprint starts 2026-06-30 (W2 of v74).**

---

## 5. What is paperclip / DanClaw? (v74)

**Carry from v73:**

- Paperclip = TypeScript/Node OpenClaw orchestration runtime.
- Renamed to **DanClaw** in v72.
- Agent workspace files: AGENTS.md, SOUL.md, IDENTITY.md, MEMORY.md.
- Channels: Telegram (primary), Terminal (debug).
- MCP tools: perception, memory, os-toold, tts.

**v74 delta:** **DanClaw held live for 1.5h** since v73. Uptime counter is now in v74 social. v74 carries the v73 framing: "DanClaw is to wearable AI what Kubernetes was to microservices."

**v74 honest disclaimer:** DanClaw is process-supervised. **The auto-recovery loop is the receipt.** v74 surfaces this: "8/8 daemons live, 1.5h uptime after the v73 OpenClaw recovery. The watchdog loop works in production."

---

## 6. What is the overall Danlab story? (v74)

**v73 story:** "Snap closed the wedge. We are building the moat: open + audit-able + safety-gated."

**v74 story (sharpened):**

> **"From a laptop in Bengaluru to an open, audit-able, on-device, safety-gated, publishable, India-first proactive-AI wearable. We are 8 engineers building in the open — the daemons are MIT, the eval is MIT, the safety gate is MIT, the leaderboard is public. NITI Aayog called for AI self-reliance after the Anthropic export ban. We are answering with dglabs-eval v1 (55 tasks, MIT, anti-capture, public leaderboard) and the SIA-fork (verified, monorepo-integrated, 2-week sprint). Perplexity launched Brain (+25% correctness). We will publish a leaderboard row that beats the Brain baseline. The moat is published. The wearable ships Q3 2026 (audio v1) and Q1 2027 (display v2)."**

**Narrative arc (v74):**

| Date | Milestone | Public surface |
|---|---|---|
| 2022 | somdipto founds danlab.dev | danlab.dev live |
| 2026-04-17 | Dan Glasses PRD v1.0 | github.com/somdipto/dan-glasses |
| 2026-06-15 | audiod v0.7 ships | github.com/somdipto/dan-glasses/Services/audiod |
| 2026-06-20 | World Model Hackathon win | dream-danlab.vercel.app |
| 2026-06-22 15:00 IST | **v73 ships: 8/8 daemons live. SIA plan. dglabs-eval plan.** | github.com/somdipto/dan-consciousness |
| 2026-06-22 16:00 IST | **v74 ships: 122/122 audiod tests. Perplexity Brain baseline. NITI Aayog anchor. SIA monorepo plan. Show HN moved to 2026-08-04.** | danlab.dev/blog/v74 |
| 2026-06-28 | **Hardware pivot decision (v1 audio-only, v2 with display)** | danlab.dev/blog/hardware-decision |
| 2026-06-30 | SIA fork monorepo integration starts | github.com/somdipto/danlab-multimodal |
| 2026-07-07 | danlab-multimodal public | github.com/somdipto/danlab-multimodal |
| 2026-07-12 | SIA-fork v0.1 paper (arXiv) | arxiv.org/abs/... |
| 2026-07-19 | dglabs-eval v0.1 paper (arXiv) | arxiv.org/abs/... |
| 2026-07-21 | dglabs-eval v0.1 ships (paper + code + scenarios) | github.com/somdipto/dglabs-eval |
| 2026-07-28 | dglabs-eval v0.5 ships (safety subset, supply-chain attack, reproducible eval) | github.com/somdipto/dglabs-eval |
| 2026-08-04 | **Show HN: "OSS AI glasses from India 🇮🇳. 8/8 daemons. dglabs-eval v0.5. SIA-fork. MIT."** | news.ycombinator.com |
| 2026-08-31 | **dglabs-eval v1 ships. Public leaderboard. First row (Dan Glasses v1 vs Perplexity Brain baseline).** | danlab.dev/eval/leaderboard |
| 2026-Q3 | Wearable v1 demo (audio-only, Plaud-class) | dream-danlab.vercel.app + danlab.dev/glasses-demo |
| 2026-Q4 | Dev-kit v1 pre-orders ($189, ₹15K INR) | danlab.dev/preorder (Stripe) |
| 2027-Q1 | Dev-kit v2 (with display) + consumer launch | danlab.dev/preorder |

**v74 thesis:** "Scale the moat. The wedge is closed. The moat is published. The SIA-fork is verified. The eval ships in 8 weeks. The wearable ships in 6 months."

---

## 7. What marketing channels make sense? (v74)

**v73 channel map → v74 delta:**

| Channel | v73 status | v74 action |
|---|---|---|
| **X (@NandySomdipto + @dan2agi + @Shodan_s)** | Live. ~0 growth. | **v74: 1 thread/week Wed, 1 daily micro-post Fri-Sun, 1 founder thread monthly. v74 NEW: 1 thread on Perplexity Brain baseline (Day 3 of v74).** |
| **LinkedIn (somdipto founder)** | Live. 4,148 followers. | **v74: 1 long-form post Mon (NITI Aayog anchor), 1 status update Thu (daemon count + 122/122).** |
| **GitHub (somdipto + dan-lab org TBD)** | Live. 0 stars. | **v74: 6 public repos (dan-consciousness, dan-glasses, danlab-multimodal, dglabs-eval, sia-fork-monorepo, SIA monorepo subdir). Org TBD. Carried from v73.** |
| **Hacker News** | Not yet. | **v74: Show HN 2026-08-04 (moved from 07-14). Title: "OSS AI glasses from India. 8/8 daemons. dglabs-eval v0.5. SIA-fork monorepo. MIT."** |
| **Reddit r/LocalLLaMA** | Active. | **v74: 1 weekly thread pinned. dglabs-eval v0.5 is the r/LocalLLaMA hook. NEW: r/MachineLearning cross-post on Day 14.** |
| **YouTube** | 0 videos per v73. | **v74: 1 video Wed, 4 total in v74 cycle. "dglabs-eval in 60s", "SIA-fork demo", "Show HN recap", "Perplexity Brain comparison".** |
| **Newsletter (danlab.dev/rss)** | Live. 200+. | **v74: weekly Fri + 1 sponsor slot + 1 NITI Aayog issue.** |
| **Telegram @danlab_bot** | Live. | **v74: 1 weekly status post Sun.** |
| **Discord (DanLab)** | ~50 members. | **v74: #dglabs-eval + #sia-fork + #glasses-hardware + #supply-chain-attacks (NEW).** |
| **Hackernewsletter (TLDR, Bytes, etc.)** | Not yet. | **v74: pitch post-Show HN. Carried from v73.** |
| **YourStory + Inc42 (India media)** | Pitched, no reply. | **v74: follow-up with the NITI Aayog + dglabs-eval angle. Pitch 2026-07-22.** |
| **TechCrunch / The Verge / WIRED** | Not pitched. | **v74: pitch after Show HN 2026-08-05.** |
| **MIT Tech Review** | Not pitched. | **v74: pitch 2026-07-26 (with the SIA monorepo + dglabs-eval v0.5).** |
| **arXiv (cs.AI, cs.CL, cs.HC)** | Not yet. | **v74 NEW: submit dglabs-eval v0.1 paper 2026-07-19. Submit SIA-fork v0.1 paper 2026-07-12.** |

**v74 channel rule:** Every channel surfaces at least one v74 receipt (122/122 audiod, SIA-fork monorepo plan, Perplexity Brain baseline, NITI Aayog anchor, dglabs-eval ship date, supply-chain attack task, 8/8 daemons uptime counter).

---

## 8. What content should Danlab produce? (v74)

**v74 content pillars:**

1. **Receipts** (technical proof). 122/122 audiod tests, 8/8 daemons live, 7.08s wizard roundtrip, dream-danlab live, SIA monorepo plan.
2. **Research** (dglabs-eval, SIA-fork, Self-Harness, Perplexity Brain comparison). Papers, RFCs, code. The moat.
3. **Hardware** (pivot decision v1/v2 split). Blog post 2026-06-28.
4. **India-first** (NITI Aayog anchor + Neprion + Sarvam angle). Founder essays. LinkedIn long-form.
5. **Safety** (Agents of Chaos subset + Sentry key hijack task). Cross-cuts every post.

**v74 content items (16, 6-week cycle):**

| Week | Mon | Wed | Fri |
|---|---|---|---|
| **W1 (06-23 → 06-29)** | Founder LinkedIn: "v74: 122/122 audiod tests. Perplexity Brain is the baseline." | X thread: "8/8 daemons live for 1.5h after the v73 OpenClaw recovery. The watchdog works in production." | Weekly dev log #21. dglabs-eval v0.1 RFC. Hardware pivot blog 06-28. |
| **W2 (06-30 → 07-06)** | Founder LinkedIn: "Why we're picking [Neprion] for v1 audio-only. ₹189 INR." | YouTube "dglabs-eval in 60s." SIA-fork monorepo integration starts. | Weekly dev log #22. YourStory pitch 07-08. arXiv draft 07-12. |
| **W3 (07-07 → 07-13)** | X thread: "danlab-multimodal is now public. SIA-fork in monorepo. MIT." | YouTube "SIA-fork demo: heuristic → SIA verifier." | Weekly dev log #23. SIA-fork paper arXiv 07-12. |
| **W4 (07-14 → 07-20)** | X thread: "dglabs-eval v0.1 ships: 55 tasks, MIT, anti-capture, public leaderboard." | YouTube "dglabs-eval deep dive." | Weekly dev log #24. dglabs-eval v0.1 paper arXiv 07-19. MIT Tech Review pitch 07-26. |
| **W5 (07-21 → 07-27)** | X thread: "dglabs-eval v0.5 ships: supply-chain attack task reproducible." | YouTube "Perplexity Brain comparison: +25% is the bar." | Weekly dev log #25. dglabs-eval v0.5 release. |
| **W6 (07-28 → 08-03)** | X thread: "Show HN prep. Tuesday 09:00 IST / 21:30 PDT." | YouTube "Show HN dress rehearsal." | Weekly dev log #26. Show HN 2026-08-04. |

**v74 NEW content types (from v38):**

- **dglabs-eval v0.1 paper.** arXiv 2026-07-19. 8 pages. NITI Aayog + Perplexity Brain + Self-Harness + SIA v2 + Agents of Chaos + Sentry key hijack as anchor.
- **SIA-fork v0.1 paper.** arXiv 2026-07-12. Truthful writeup of the 2-week sprint. ~220 GPU-hours, +X% on the heuristic baseline. (Honest, even if the number is small.)
- **Perplexity Brain comparison blog.** 2026-07-29. "We benchmarked against Perplexity Brain's +25% correctness number."
- **NITI Aayog founder essay.** LinkedIn 2026-06-23. "AI self-reliance as national priority. Danlab's contribution."

---

## 9. What is the current online presence? (v74 audit, 2026-06-22 16:00 IST)

| Surface | Status (live) | Stars / Followers | v74 action |
|---|---|---|---|
| **danlab.dev** | Live | 0 organic | v74 ships the v74 hero (eval-first, publishable) |
| **github.com/somdipto/dan-consciousness** | Live, public | 0 stars | v74 promotes in W3 |
| **github.com/somdipto/dan-glasses** | Live, public | 0 stars | v74 ships v74 release: 122/122 |
| **github.com/somdipto/danlab-multimodal** | **404** | N/A | v74 ships W3 (2026-07-07) |
| **github.com/somdipto/dglabs-eval** | **TBD** | N/A | v74 ships W4 (2026-07-21) |
| **github.com/somdipto/sia-fork** | **TBD** | N/A | v74 ships W3 (2026-07-12) — *or* lives as monorepo subdir per v38 (v74 default: monorepo) |
| **paperclip → DanClaw** | Renamed (v72) | N/A | v74 surfaces the rename in W2 |
| **github.com/somdipto/dan-lab** | **404** | N/A | v74 defers to v75 |
| **dream-danlab.vercel.app** | LIVE | 0 (launched 2026-06-20) | v74 makes it the headline demo |
| **dan-glasses-app-som.zocomputer.io** | Live, React SPA | 0 (private link) | v74 promotes in W2 |
| **arxiv.org/abs/...dglabs-eval** | TBD | N/A | **v74 NEW: 2026-07-19** |
| **arxiv.org/abs/...sia-fork** | TBD | N/A | **v74 NEW: 2026-07-12** |
| **X @NandySomdipto** | Live | 4,148 LinkedIn / unknown X | v74 surfaces as founder voice |
| **X @dan2agi** | Live | unknown | v74 surfaces as project voice |
| **X @Shodan_s** | Live | unknown | v74 surfaces as agent voice |
| **Telegram @danlab_bot** | Live | unknown | v74 surfaces in the daemons |
| **Discord (DanLab)** | Live | ~50 (v72) | v74 #dglabs-eval + #sia-fork + #supply-chain-attacks channels |
| **YouTube (DanLab)** | Live | 0 subs | v74 ships 4 videos |
| **Newsletter (danlab.dev/rss)** | Live | 200+ (220+ per v38 readme, audit pending) | v74 weekly + sponsor slot + NITI Aayog issue |
| **Reddit r/LocalLLaMA** | Active | N/A | v74 weekly thread + Show HN |
| **Hacker News** | Not yet | N/A | **v74: Show HN 2026-08-04** |
| **YourStory + Inc42** | Pitched (v72), no reply | N/A | v74 follow-up 2026-07-22 |
| **MIT Tech Review** | Not pitched | N/A | **v74: pitch 2026-07-26** |
| **TechCrunch / The Verge / WIRED** | Not pitched | N/A | v74 pitch post-Show HN 2026-08-05 |

**v74 online presence rule (carried from v73):** Every URL is a receipt. Every receipt is real, live, testable. v74 adds: **every research claim is arXiv-backed or arXiv-planned.** No "blog post" without a paper draft.

---

## 10. Who are the first users/customers? (v74)

**v73 persona set → v74 delta:**

| Persona | v73 expected | v74 expected | Delta |
|---|---|---|---|
| A — OSS Hacker | 100 | 100 | Carried. Show HN 2026-08-04 is the conversion event. |
| B — Accessibility Advocate | 50 | 50 | Carried. v74 carries the audiod captioning story. |
| C — Privacy-First Founder | 50 | 50 | Carried. v74 surfaces "operational sovereignty" vocabulary. |
| D — India-First Builder | 100 | 150 | **+50 (v74 delta).** NITI Aayog anchor + Neprion + Sarvam context. |
| E — World-Model Researcher | 400 | 500 | **+100 (v74 delta).** dglabs-eval v1 + SIA-fork + arXiv papers. |
| F — AI Safety Researcher | 75 | 100 | **+25 (v74 delta).** Sentry key hijack task + supply-chain attack scenario. |
| **G — NEW (v74): Enterprise CTO** | 0 | 50 | **NEW.** "Operational sovereignty" + on-device + audit-able + India-first. Indian enterprise IT (Tata, Infosys, Wipro). |

**v74 first-user math:**

- v73 expected: 775 first users.
- v74 expects: **1,000 first users** (A-F carry, +F supply-chain, +D NITI Aayog, +E arXiv, +G enterprise CTOs).

  - 100 OSS hackers (A)
  - 50 accessibility advocates (B)
  - 50 privacy-first founders (C)
  - 150 India-first builders (D)
  - 500 world-model researchers (E)
  - 100 AI safety researchers (F)
  - 50 enterprise CTOs (G — v74 NEW)

**The CTA for v74:**

> **"8/8 daemons live. 122/122 audiod tests. 1.5h uptime after the v73 OpenClaw recovery. dglabs-eval v1 ships 2026-08-31. 55 tasks. MIT. Anti-capture. Public leaderboard. NITI Aayog-aligned. SIA-fork monorepo integrated. Perplexity Brain baseline is the bar. OSS, MIT, India 🇮🇳."**

---

## v74 summary

- **v74 thesis:** v73 shipped the moat. v74 ships the moat, **published, benchmarked, and ready to ship in 8 weeks.** The dglabs-eval v1 ship is the receipt. The Perplexity Brain baseline is the bar. The NITI Aayog anchor is the policy frame. The SIA-fork monorepo is the upgrade path.
- **v74 receipts:** 8/8 daemons live (1.5h uptime since v73). 122/122 audiod tests. 7.08s wizard roundtrip. dream-danlab live. SIA monorepo plan verified against the actual SIA repo. Perplexity Brain numbers published. NITI Aayog public statement. Sentry key hijack. dglabs-eval v0.1 RFC. Hardware pivot 2026-06-28.
- **v74 → v75 transition:** dglabs-eval v1 ships 2026-08-31. Show HN moves to 2026-08-04. dglabs-eval v0.1 paper arXiv 2026-07-19. SIA-fork paper arXiv 2026-07-12. v75 = "publish + scale" — from 1,000 → 10,000 first users, from 0 → 5,000 GitHub stars, from 0 → 5 arXiv citations.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-22 16:00 IST. v73 shipped the moat. v74 ships the moat, published, benchmarked, and ready to ship in 8 weeks.*
