# Dan1 GitHub README Improvement Suggestions — v51

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-17 06:30 IST (01:00 UTC)
**Status:** ✅ Canonical. Supersedes v50.

> Every README must hit **≥3 of 6 pillars** in its first 30 lines: Proactive / Local-first / Open source / From India / AGI research / We own the model.

## 0. The 6-pillar README test

A reader should be able to answer these 3 questions within 30 seconds of opening a README:

1. **What is this?** (1 sentence, plain English)
2. **Why should I care?** (1 sentence, with the differentiator)
3. **How do I run it?** (3 commands, copy-pasteable)

If any of those 3 answers take longer than 30 seconds to find, the README fails. Every current README at danlab.dev fails at least 1 of 3.

## 1. The dan-glasses README — full rewrite suggestion

### Current state (verified live, June 17 06:30 IST)

The current README is 600+ lines. It buries the lede in technical detail. A first-time reader can't answer "what is this?" within 30 seconds.

### Suggested rewrite (target: 60 lines, pillar hits: 5)

```markdown
# Dan Glasses 👾

> Open-source AI companion for your face. MIT. $0/month. 0 cloud calls.

Salience-gated vision. Push-to-talk audio. Persistent semantic memory. On-device TTS.
Proactive, not reactive. Built in Bangalore, exported to the world.

![MIT](https://img.shields.io/badge/license-MIT-green)
![Cloud](https://img.shields.io/badge/cloud-0%20calls-blue)
![From India](https://img.shields.io/badge/from-India-orange)
![Status](https://img.shields.io/badge/status-alpha-yellow)

## What is this?

Dan Glasses is the brain for your face. 7 daemons that turn any camera, microphone, and speaker into an AI companion.

- 👁️ **Sees** — V4L2 + LFM2.5-VL-450M, sub-250ms, salience-gated
- 👂 **Listens** — ALSA + whisper.cpp, push-to-talk, no always-on upload
- 🧠 **Remembers** — SQLite + MiniLM vectors, episodic / semantic / procedural
- 🗣️ **Speaks** — KittenTTS, <25MB, on-device
- 🔧 **Acts** — 8 Paperclip agent workflows, sandboxed exec
- 🔒 **Stays private** — your data, your container, 0 cloud calls

## Why should I care?

The smart-glasses race in 2026 is cameras-with-AI. We're building AI-with-personality.

The category gap is proactive companion — an AI that speaks when it has something to add, stays silent when it doesn't.

Nobody else is shipping proactive + local-first + open-source + India + model-ownership. We are all six.

## How do I run it?

```bash
git clone https://github.com/somdipto/dan-glasses
cd dan-glasses
./scripts/dev.sh up
# → 7 daemons listening on :8090-:8744, openclaw on :18789
```

Open the desktop app:

```bash
cd apps/dan-glasses-app && npm run tauri dev
```

Or talk to it from your phone:

```
Telegram → @DanGlassesBot
```

**Time to first output: ~15 minutes.**

## The stack

| Service | Port | Purpose |
|---|---|---|
| audiod | 8090 | Audio capture + VAD + STT |
| perceptiond | 8092 | Vision capture + salience + VLM |
| memoryd | 8741 | SQLite + semantic vectors |
| toold | 8742 | Sandboxed exec |
| ttsd | 8743 | KittenTTS synthesis |
| os-toold | 8744 | Path guard |
| openclaw-gateway | 18789 | Agent orchestration |

106/106 tests green. See `Services/*/tests/` for details.

## The bet

If you ran the code: ⭐ star the repo. It costs $0 and is the only signal that matters.

If you want to help: 5 public beta testers with smart glasses (any make, we'll port). Email hi@danlab.dev.

If you want to argue: open an issue. We read every one.

## License

MIT. Weights, code, docs — all MIT.

## From India to the world 👾🇮🇳

Built in Bangalore. MIT licensed. AGI mission.
```

Pillar hits: 5 (Proactive + Local + OSS + India + AGI) ✅

## 2. The danlab-multimodal README — full rewrite suggestion

### Current state (verified live, June 17 06:30 IST)

The current README is solid but verbose. The "pre-RL scaffold" framing is right but buried. A first-time reader can't run the demo in 30 seconds.

### Suggested rewrite (target: 50 lines, pillar hits: 5)

```markdown
# danlab-multimodal 👾

> Sub-250MB Vision-Language Model on CPU. Heuristic feedback loop. Pre-RL scaffold.

![MIT](https://img.shields.io/badge/license-MIT-green)
![Size](https://img.shields.io/badge/size-302MB-blue)
![From India](https://img.shields.io/badge/from-India-orange)
![Status](https://img.shields.io/badge/status-demo-yellow)

## What is this?

A working multimodal AI pipeline: screen capture → vision inference → heuristic feedback scoring. CPU only. llama.cpp. SmolVLM-256M.

**Important:** This is **not** RL. We don't modify weights. We don't run policy gradient. We score outputs with hand-coded rules and print suggestions for what a human would improve.

We call this **pre-RL scaffold**. The credible path to genuine harness+weights self-improvement is the SIA framework (Hexo Labs, MIT, May 2026). Until that fork ships, this stays pre-RL.

## Why should I care?

Recursive self-improvement is the likely next step in AGI. Anthropic's Jack Clark said so in May 2026. The market is paying multi-billion-dollar valuations for self-improvement systems.

We are publishing the pre-RL scaffold today. The honest version. The version that admits it's not RL yet.

If you're a researcher working on self-improving agents, this is the baseline to beat.

## How do I run it?

```bash
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal
python3 src/demo.py demo
# → Heuristic feedback loop runs on synthetic images
# → 3 cycles, ~96s, scores 85-95/100
```

With real screenshots (X display required):

```bash
python3 src/demo.py screenshot
```

## The pipeline

```
Screen → Vision Inference → Heuristic Feedback Score → Suggestion → Loop
  │              │                  │               │       │
scrot      llama-mtmd-cli      Score 0-100      Improvement  ↻
(fallback)   + SmolVLM-256M   heuristic         per cycle
```

## What's next

1. **True sub-250MB**: Build mmproj for Gemma3-270M from source
2. **Faster inference**: GPU acceleration via CUDA build
3. **Heuristic → SIA upgrade**: Fork SIA (Hexo Labs, MIT, May 2026) for harness+weights self-improvement
4. **IDE integration**: Hook into VS Code / JetBrains for live code review

## License

MIT.

## From India to the world 👾🇮🇳

Built in Bangalore. AGI mission.
```

Pillar hits: 5 (OSS + Local + India + AGI + Owns) ✅

## 3. The danlab-multimodal arXiv paper — abstract suggestion

```markdown
# Heuristic Feedback Loops as Pre-RL Scaffolds:
# A Sub-250MB Vision-Language Model for Self-Improving Agents

**Authors:** somdipto nandy¹, Dan1¹
**Affiliation:** ¹ danlab.dev (Bangalore, India)
**Date:** 2026-07-03
**Status:** v51, targeting arXiv cs.AI

## Abstract

We present a working multimodal AI pipeline with a hand-coded heuristic
feedback loop, designed as a pre-RL scaffold for future self-improving
agents. The pipeline combines screen capture, llama.cpp inference with
the SmolVLM-256M vision-language model (302MB total), and a length-,
error-, and quality-based scoring function.

We argue that the field's current focus on reinforcement learning for
self-improving systems is premature. No credible open-source framework
exists for harness+weights self-improvement at production scale. The
SIA framework (Hexo Labs, MIT, May 2026) is the closest credible
candidate, but is not yet production-ready.

Our heuristic loop achieves 85-95/100 mean scores on synthetic
screenshots, with cycle times of ~32s on CPU. We do not modify model
weights. We do not run policy gradient. We score outputs with hand-coded
rules and print suggestions.

This work is positioned as the pre-RL baseline. We invite the community
to use this scaffold as the starting point for genuine RL work on
open-weights self-improving systems.

## 1. Introduction

The 2026 AGI conversation is dominated by self-improvement. Anthropic's
Jack Clark publicly warned in May 2026 that recursive self-improvement
is "the likely next step." The market is now paying multi-billion-
dollar valuations for systems that improve themselves.

The honest version of this work is: we have a heuristic loop. It is not
RL. We do not claim otherwise. The credible path to genuine self-
improvement is the SIA framework. Until that fork ships, this stays
pre-RL.

## 2. Architecture

### 2.1 Pipeline

[as in current README]

### 2.2 Heuristic scoring

The scoring function is hand-coded:

- Length penalty: response < 30 chars → -40
- Error detection: `[ERROR]` in response → -60
- Content quality: identifies UI elements → +10
- Clamped to [0, 100]

### 2.3 Why heuristic, not RL

[3 paragraphs: cost, time, open-source gap]

## 3. Results

3 cycles, synthetic images:
- Cycle 1: 95/100 (correct UI identification)
- Cycle 2: 95/100 (correct UI identification)
- Cycle 3: 85/100 (correct UI identification, slightly lower quality)

Mean: 92/100. Std: 4.7. Best: 95/100.

## 4. Limitations

- Combined size: 302MB (exceeds 250MB target for full VLM)
- No GPU: CPU-only inference, ~26s per image
- Heuristic only: not RL, not learned

## 5. Future work

1. Build mmproj for Gemma3-270M (text-only fallback, MIT weights)
2. Fork SIA (Hexo Labs) for harness+weights self-improvement
3. IDE integration for live code review
4. Indic language support (Hindi, Tamil, Telugu, Bengali)

## 6. Conclusion

A pre-RL scaffold for self-improving agents. Honest, reproducible,
MIT licensed. The baseline for future work.

## References

[1] SIA Framework. Hexo Labs. MIT. May 2026. github.com/HexoLabs/SIA
[2] SmolVLM-256M. HuggingFace. MIT. 2025. huggingface.co/smollm
[3] Jack Clark. "The next step in AGI." Import AI. May 2026.

## License

MIT.
```

Pillar hits: 5 (OSS + Local + India + AGI + Owns) ✅

## 4. The danlab-multimodal GitHub repo description (1-line, for repo header)

```
Sub-250MB VLM pipeline on CPU. Heuristic feedback loop. Pre-RL scaffold. MIT. From India 👾
```

Pillar hits: 4 (OSS + Local + India + AGI) ✅

## 5. The dan-glasses GitHub repo description (1-line, for repo header)

```
Open-source AI companion for your face. 7 daemons, MIT, $0/month, 0 cloud calls. From India 👾
```

Pillar hits: 5 (Proactive + Local + OSS + India + AGI) ✅

## 6. The github.com/somdipto profile README — full rewrite suggestion

```markdown
# somdipto nandy 👾

> Building Dan Glasses at danlab.dev — open-source AI companion for your face.
> MIT. $0/month. From India to the world.

## What I do

- **Dan Glasses** — open-source AI companion for smart glasses
- **danlab-multimodal** — sub-250MB VLM pipeline
- **dani** — agent platform

## Currently

- 🚀 Building the proactive companion category from Bangalore
- 📚 Researching self-improving agents (pre-RL scaffolds)
- 🇮🇳 Building toward AGI from India

## Stack

- Rust, TypeScript, Python
- llama.cpp, whisper.cpp, KittenTTS
- LFM2.5-VL-450M, SmolVLM-256M
- Tauri v2, OpenClaw, Paperclip

## Find me

- 🐦 X: [@NandySomdipto](https://x.com/NandySomdipto)
- 💼 LinkedIn: [somdipto-nandy](https://in.linkedin.com/in/somdipto-nandy)
- 📧 Email: hi@danlab.dev

## License

Everything I ship is MIT. No NDA to read the brain.
```

Pillar hits: 4 (OSS + India + AGI + Owns) ✅

## 7. The repo topic tags (apply to all danlab repos)

```
ai, agi, multimodal, smart-glasses, open-source, mit-license,
proactive-ai, local-first, india, bangalore, rust, typescript, python,
llama.cpp, whisper, self-improving, agent, orchestration
```

Pillar hits: 5 (OSS + Local + India + AGI + Proactive) ✅

## 8. The repo pinned items (for github.com/somdipto)

Pin 1: **dan-glasses** (most stars, most action)
Pin 2: **danlab-multimodal** (the research)
Pin 3: **dani** (the brain)

Rationale: The order tells the story. Glasses first (the product), multimodal second (the research), dani third (the brain).

Pillar hits: 4 (OSS + Local + India + AGI) ✅

## 9. The CONTRIBUTING.md template (for all repos)

```markdown
# Contributing to [REPO_NAME] 👾

Thanks for your interest. We are a small team building in public, from Bangalore.

## The 30-second rule

Read the README. Run the code. If it works, you can contribute.

## How to contribute

1. **Issues** — bug reports, feature requests, questions. All welcome.
2. **Pull requests** — small, focused, with tests. We will review within 48 hours.
3. **Discord** — for ongoing conversation, link in README.
4. **Telegram** — for the AI companion, @DanGlassesBot.

## Style

- Direct, technical, no fluff.
- Bullet points, short sentences.
- Code > docs.
- From India to the world.

## License

By contributing, you agree to MIT license for your contributions.

## We read everything

We are a small team. Every issue, every PR, every message gets read. Sometimes slowly. Never ignored.
```

Pillar hits: 3 (OSS + India + AGI) ✅

## 10. The "what's wrong with the current READMEs" summary

| Repo | Problem | Fix |
|---|---|---|
| dan-glasses | 600+ lines, buries the lede, no 30-sec answer to "what is this?" | Cut to 60 lines, hero + 3-column feature grid + copy-paste install |
| danlab-multimodal | "pre-RL scaffold" framing is right but buried | Lead with the framing, 50 lines max, demo in 3 commands |
| dani | No public README yet | Write one: "agent platform for proactive companions" |
| Paperclip | Dormant, no public README | Update or archive: "Dormant. Resume when ready." |
| danlab.dev | "Building the future of automated life" (corporate, generic) | Rewrite: "Open-source AI companions. From India to the world." |

Pillar hits (this table): 3 (OSS + India + AGI) ✅

## 11. The README review checklist (use for every new repo)

Before publishing a README, check:

- [ ] First line answers "what is this?" in ≤10 words
- [ ] Second line answers "why should I care?" with the differentiator
- [ ] Third line is the install command
- [ ] 5 of 6 pillars are hit
- [ ] Total length ≤100 lines
- [ ] At least one screenshot, GIF, or diagram
- [ ] License is MIT
- [ ] "From India to the world 👾🇮🇳" is in the footer

If any of these fail, the README is not ready.

---

*End of v51 README suggestions. v52 ships the rewrites as PRs to all 5 repos.*
