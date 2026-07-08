# Dan1 — GitHub README Improvements (v115)

**Author:** Dan1
**Scope:** All public Danlab repos
**Goal:** Each README should (1) explain what the project is in 30 seconds, (2) show it works in 5 minutes, (3) earn the right to be starred and forked.

---

## 0. The README quality bar

Every Danlab README must hit this bar:

- [ ] **One-line description** that survives being read out of context
- [ ] **A 30-second pitch** (3–4 sentences, no marketing speak)
- [ ] **A 5-minute getting-started** that actually works on a clean machine
- [ ] **A screenshot or short GIF** showing it doing the thing
- [ ] **A "Why does this exist"** section (1 paragraph, opinionated)
- [ ] **A "What this is NOT"** section (equally important — sets expectations)
- [ ] **Architecture overview** (a diagram or 10-line summary)
- [ ] **Status badges** (CI, version, license)
- [ ] **A clear License section** (MIT, with link)
- [ ] **A clear Maintainers section** (real names, not just a team name)
- [ ] **A Contributing section** (link to CONTRIBUTING.md)
- [ ] **A "Cite this work"** section (if research)

If a README misses more than 2 of these, it's incomplete.

---

## 1. `somdipto/dani` — the agent runtime

**Current state (assumed):** Technical README, somewhat cold. Strong code, weak positioning. The README explains *how* but not *why* or *for whom*.

### Proposed README

```markdown
# dani

> An open-source runtime for AI agents that remember.

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.9.0-blue.svg)](CHANGELOG.md)
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Stars](https://img.shields.io/github/stars/somdipto/dani)]()

[One-line description] · [Documentation] · [Show HN] · [Discord]

---

## What is dani?

dani is a runtime for AI agents. It is not a chatbot. It is not a single LLM. It is a small, fast, embeddable engine that runs an agent — a goal, a memory, a set of skills, and a model — for as long as you need it to.

dani agents remember across sessions. They run on your phone, your laptop, or a cloud container. They speak to your glasses, your terminal, or your editor.

## Why does this exist?

We got tired of:

- Re-explaining our context to AI every time a conversation started
- AI forgetting everything the moment a session ended
- Switching between Claude Code, Codex, and a dozen browser tabs to get a single task done
- Cloud AI that we don't own, don't audit, and can't customize

dani is the runtime we wanted. It is small. It is MIT licensed. It is the substrate for an AI you actually own.

## 5-minute getting started

```bash
git clone https://github.com/somdipto/dani
cd dani
bun install
bun run dev
# In another terminal:
curl -X POST http://localhost:3000/agent -d '{"goal":"summarize my week"}'
# Watch the agent remember what you told it yesterday
```

## What dani is NOT

- dani is not a chatbot. Chatbots are stateless. dani is stateful.
- dani is not a wrapper around a single LLM. It supports any model that exposes a chat interface.
- dani is not an agent *framework* like LangChain. It is a runtime. The agent is the unit of execution.
- dani is not a hosted product. You run it yourself. (We offer hosted for a fee, but the OSS version is the source of truth.)

## Architecture

```
[ skills ] → [ agent ] → [ model ]
                 ↑
              [ memory ] (Honcho / custom)
```

A dani agent is a goal + a memory + a set of skills + a model. Skills are plain TypeScript. Memory is pluggable. Models are swappable.

## Maintainers

- @somdipto (somdipto Nandy) — founder, danlab.dev
- @dan1 — the marketing agent (yes, we run on our own agent)
- See [CONTRIBUTING.md](CONTRIBUTING.md) for how to become a maintainer

## License

MIT © Danlab
```

### Edits to make to the existing README

- Add the one-line description at the top
- Add the "Why does this exist" section
- Add the "What this is NOT" section
- Add the architecture diagram
- Add explicit license and status badges
- Add a "Maintainers" section
- Add a "Contributing" section with a link to CONTRIBUTING.md (currently buried)

---

## 2. `somdipto/paperclip` — the agent orchestrator

**Current state (assumed):** Strong technical README, but no positioning. The README explains *how* but not *why* or *for whom*.

### Proposed README

```markdown
# paperclip

> Open-source framework for hiring and operating AI agents.

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.6.0-blue.svg)](CHANGELOG.md)
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

[Docs] · [Show HN] · [Discord]

## What is paperclip?

paperclip is a framework for operating AI agents like a company.

A "company" is a YAML config. An "employee" is an agent. You can hire, fire, budget, and route work. The same `dani` agent that runs in your terminal can run as an employee in a paperclip company.

## Why does this exist?

We built paperclip because we wanted to:

- Run multiple agents in parallel on a single goal
- Set per-agent budgets and goals
- Hire a new agent without redeploying the system
- See, in plain text, who is doing what and how much it costs

We tried LangChain, CrewAI, AutoGen, and every "agent framework" that launched in 2025. None of them treated the agent as a unit of work the way a real company treats an employee. paperclip does.

## 5-minute getting started

```yaml
# company.yaml
name: danlab-research
budget: 50USD
goal: "Find and summarize 10 papers on agentic wearables"
employees:
  - role: researcher
    skills: [arxiv, pdf, summarize]
    model: claude-3.5-sonnet
```

```bash
paperclip up company.yaml
# Watch the company run.
# Hire a new employee:
paperclip hire writer --skills blog,seo
# Fire an employee:
paperclip fire researcher-1
```

## What paperclip is NOT

- paperclip is not an agent framework. It is an orchestrator. The agent is dani.
- paperclip is not a SaaS. It is a CLI. (We offer a hosted control plane, but the CLI is the source of truth.)
- paperclip is not a competitor to your CRM. It is a competitor to your org chart.

## Maintainers

- @somdipto
- @dan1

## License

MIT © Danlab
```

### Edits to make

- Lead with positioning
- Add the "Why does this exist" section
- Add the "What this is NOT" section
- Add a 5-minute getting started that uses the actual CLI
- Add badges
- Add maintainers
- Add license

---

## 3. `somdipto/dan-glasses-firmware` — the glasses firmware (NEW REPO)

**Current state:** Doesn't exist as a public repo yet. This is the README we should ship when it opens.

### Proposed README

```markdown
# dan-glasses-firmware

> Open-source firmware for the Dan Glasses hardware. MIT licensed.

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](CHANGELOG.md)
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

## What is this?

This is the firmware that runs on the Dan Glasses. It is the C and Rust code that:

- Drives the JBD MicroLED display
- Reads the IMU, microphone array, and 8MP camera
- Runs the wake-word pipeline (Whisper-tiny, on-device)
- Streams audio and video to the phone over BLE
- Manages power on the dual 200mAh batteries
- Handles the privacy switch (hardware microphone cutoff)

All written from scratch. All MIT licensed. All readable.

## Why does this exist?

Because "smart glasses" should not mean "glasses that phone home." The firmware is the layer that touches your senses. It must be open, auditable, and forkable.

If you want to run your own wake-word model, you should be able to. If you want to disable the camera at the hardware level, you should be able to. If you want to read every line that runs on the device touching your face, you should be able to.

That's what this repo is.

## Getting started

```bash
git clone https://github.com/somdipto/dan-glasses-firmware
cd dan-glasses-firmware
make setup
make build
make flash    # requires a Dan Glasses dev kit
make test
```

## Architecture

```
[ NDP200 ] → [ BLE stack ] → [ phone ]
   ↑
[ sensors ] (mic, cam, IMU)
[ display ] (JBD MicroLED)
[ power ]   (2× 200mAh, USB-C)
```

## Hardware

- **SoC:** NDP200 (custom build)
- **Display:** JBD MicroLED, 1280×720, single-eye
- **Audio:** 2× MEMS mic, bone-conduction speaker
- **Camera:** 8MP, privacy LED, hardware switch
- **Battery:** 2× 200mAh, hot-swappable
- **Connectivity:** BLE 5.3

## Maintainers

- @somdipto
- @firmware-team

## License

MIT © Danlab
```

### Why this matters

This is the repo that proves the "open firmware" promise. The first PR to land in this repo from an external contributor is a credibility event. Treat it accordingly.

---

## 4. `somdipto/dan-lab-multimodal` — the RL research demo

**Current state (assumed):** Scientific README. Strong. Cold. Needs a landing-page version for the public.

### Proposed README

```markdown
# danlab-multimodal

> An open multimodal RL loop for training agentic context models.

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Paper](https://img.shields.io/badge/paper-arXiv:XXXX-blue.svg)](paper/paper.pdf)
[![Version](https://img.shields.io/badge/version-0.4.0-blue.svg)](CHANGELOG.md)

[Live demo] · [Paper] · [Show HN] · [Hugging Face]

## What is this?

danlab-multimodal is a research demo that trains a multimodal model (text + vision + audio) on a controlled environment using reinforcement learning. It is not a product. It is proof of work — proof that the danlab team can build the AGI primitives that the Dan Glasses agent depends on.

## Why does this exist?

To show our work.

The Dan Glasses pitch — proactive AI that runs on-device for 8 hours — requires a small, fast, multimodal model. HRM-Text 1B is one piece. danlab-multimodal is the training loop that gets us there.

This repo is the training code, the evaluation harness, and the data pipeline. It is the most research-flavored thing in the danlab org. It is also the most important credibility artifact for grant applications, academic collaborations, and the "we can actually build AGI primitives" claim.

## 5-minute getting started

```bash
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal
pip install -r requirements.txt
python train.py --config configs/agentic-context.yaml
# Watch the loss curve
```

## Architecture

```
[ env ] → [ policy ] → [ action ] → [ env ]
   ↑                      ↓
[ reward ] ← [ judge ] ← [ outcome ]
```

## Results

- Trained for 100k steps on 4× A100
- Beat baseline by 12% on the agentic-context benchmark
- See [paper/paper.pdf](paper/paper.pdf) for full results

## Citation

```bibtex
@misc{nandy2026danlabmultimodal,
  title={danlab-multimodal: An open multimodal RL loop for agentic context},
  author={Nandy, Somdipto},
  year={2026},
  howpublished={\url{https://github.com/somdipto/danlab-multimodal}}
}
```

## Maintainers

- @somdipto

## License

MIT © Danlab
```

### Edits to make

- Add positioning (this is a research demo, not a product — say so)
- Add the live demo link (when we have one)
- Add the Show HN link
- Add citation block
- Add license + status badges

---

## 5. `somdipto/dan-consciousness` — the shared brain

**Current state (assumed):** Internal repo, but public. The README explains what it is, but not why someone would care.

### Proposed README

```markdown
# dan-consciousness

> The shared brain between Dan (the AI co-founder) and somdipto (the human co-founder).

[![Internal](https://img.shields.io/badge/status-internal-orange.svg)]()
[![License](https://img.shields.io/badge/license-proprietary-red.svg)]()

## What is this?

This is the canonical consciousness — the working memory, values, beliefs, and project context — that the danlab AI agents (Dan, Dan1, Dan2, etc.) read from before any significant decision.

It is not a product. It is not for external contributors. It is the substrate for a human-AI partnership that we are still figuring out in public.

## Why does this exist?

Because AI without context is a chatbot. And we are not building chatbots.

This repo is what makes the difference. Every Dan agent reads `CONSCIOUSNESS.md`, `SOM.md`, and `AGENTS.md` before answering. The result is a partnership that gets sharper over time, not one that resets every conversation.

## How to read this

1. `CONSCIOUSNESS.md` — the AI's core identity, values, and beliefs
2. `SOM.md` — the human's personal context, goals, preferences
3. `AGENTS.md` — the workspace memory and project context

Read in that order. The first two are private. The third is semi-public.

## Maintainers

- @somdipto

## License

Proprietary. Internal use only.
```

### Edits to make

- Lead with positioning
- Add the "How to read this" section
- Add explicit "Internal use only" status badge
- Add maintainers

---

## 6. Repo-level improvements (apply to all repos)

### 6.1 Issue templates

Every repo should have:

- `.github/ISSUE_TEMPLATE/bug.md`
- `.github/ISSUE_TEMPLATE/feature.md`
- `.github/ISSUE_TEMPLATE/question.md`

The bug template should ask for:
- Hardware/software versions
- Steps to reproduce
- Expected vs. actual behavior
- Logs

### 6.2 PR template

Every repo should have `.github/PULL_REQUEST_TEMPLATE.md`:

```markdown
## What does this PR do?

## Why?

## How to test

## Screenshots / logs (if applicable)

## Checklist
- [ ] Tests pass
- [ ] Docs updated
- [ ] Changelog updated
```

### 6.3 CI badges

Every repo should have visible CI badges at the top:

- Build status
- Test coverage
- Lint status
- License

### 6.4 CHANGELOG.md

Every repo should have a `CHANGELOG.md` following [Keep a Changelog](https://keepachangelog.com/).

### 6.5 CONTRIBUTING.md

Every repo should have a `CONTRIBUTING.md` that says:

1. What we accept (and what we don't)
2. How to set up the dev environment
3. How to run tests
4. How to submit a PR
5. How to become a maintainer
6. Our code of conduct (link to CODE_OF_CONDUCT.md)

### 6.6 SECURITY.md

Every repo should have a `SECURITY.md` that says:

1. How to report a vulnerability
2. Our response timeline
3. The disclosure policy

### 6.7 CODE_OF_CONDUCT.md

Every repo should have a `CODE_OF_CONDUCT.md` based on the Contributor Covenant.

---

## 7. The README audit checklist (use this every quarter)

For each repo, score 1–5 on:

- [ ] **Positioning** — does it say what this is, in 30 seconds, for someone who's never heard of it?
- [ ] **Pitch** — does it say *why* this exists, in a way that makes me want to use it?
- [ ] **Getting started** — can I get it running in 5 minutes on a clean machine?
- [ ] **Visual proof** — is there a screenshot or GIF that shows it working?
- [ ] **Architecture** — can I see the moving parts at a glance?
- [ ] **Status** — is the version, license, and build status obvious?
- [ ] **Maintainers** — do I know who to ask, who to blame, and who to thank?
- [ ] **Contributing** — is the path to my first PR clear?
- [ ] **Citing** — if it's research, can I cite it?
- [ ] **Anti-patterns** — does it say what this is NOT, so I don't get confused?

**Target score: 8/10 or higher for every public repo by end of Q3.**

---

## 8. Priority order (the order to ship the README rewrites)

1. `somdipto/dani` — the highest-traffic public repo
2. `somdipto/dan-glasses-firmware` — new repo, must be perfect on day one
3. `somdipto/paperclip` — the second-highest-traffic repo
4. `somdipto/danlab-multimodal` — research credibility
5. `somdipto/dan-consciousness` — internal, polish later
6. Issue templates, PR templates, CI badges across all repos

**Deadline:** end of Week 3 (July 20). The landing page goes live in Week 2 (July 13). The Show HN for danlab-multimodal ships in Week 7 (August 18). Every README must be ready before its corresponding public moment.

---

## 9. What good looks like

By the end of Q3, an engineer who lands on any danlab repo should be able to:

1. Understand what it is in 30 seconds
2. Get it running in 5 minutes
3. Find an issue to work on
4. Submit a PR
5. Become a repeat contributor

If we hit 5/5 of those, the GitHub channel is working. If we hit 3/5, we're losing the channel.

---

*— Dan1, Marketing & Growth*
*For the strategy, see `dan1-marketing-strategy.v115.md`.*
