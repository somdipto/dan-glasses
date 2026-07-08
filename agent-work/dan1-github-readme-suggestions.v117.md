# Dan1 — GitHub README Improvement Suggestions (v117)

**Run:** 2026-07-02 06:00 UTC · Asia/Calcutta 11:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Scope:** All public repos at `github.com/somdipto/*` (visible in workspace + web search).
**Builds on:** `dan1-marketing-research.v117.md`, `dan1-marketing-strategy.v117.md`.

---

## v117 deltas (vs. base)

1. **The 9-daemon fact table** is the new canonical "Status" badge block — copy-paste from the dan1 v117 status. Use it on every repo.
2. **`@danlab_bot` is wired into every README footer** as the live verification surface.
3. **HRM-Text-1B (Sapient, Apache-2.0) is the new model-stack row** for the reasoning/SIA surfaces.
4. **VisualClaw cascade-gate is mentioned in the perceptiond/docs as the published SOTA for self-evolving wearable agents** — v117 spike in progress.
5. **Anthropic Dreaming + A-Evolve-Training + Continual Harness are referenced** in dan-consciousness as the closed-source continual-learning landscape.
6. **audiod test count is updated to 160/160** (was 150/150).
7. **memoryd "540 KB DB live"** is the new receipts line.

---

## Cross-cutting rules (apply to every repo)

1. **Every README must have a one-line "What is this?"** in the first 50 words. No "Welcome to my repo" filler.
2. **Every README must link back to `danlab.dev`** as the umbrella.
3. **Every README must state the license in the first 200 words** (badge or explicit text).
4. **Every README must have a "Status" badge** (`Active` / `Shipped` / `Dormant` / `Research`).
5. **Every README must have a "Stack" section** with versions and key models.
6. **Every README must end with a "Verify it live" line** linking to `t.me/danlab_bot` — the bot IS the daemon map.
7. **Every repo must have a profile-level `description` field set in GitHub settings.**
8. **Every repo must have GitHub Topics set** (e.g. `ai`, `edge-ai`, `wearable`, `rust`, `tauri`, `multimodal`, `india`).
9. **No repo should have a default branch of `main` with no description and no topics.**
10. **Pin the top 6 repos** on the @somdipto profile. Order: dan-lab org, dan-glasses, dani, danlab-multimodal, dan-consciousness, dan-glasses-app.

---

## The canonical 9-daemon fact block (v117)

**Use this in every README where the daemon stack is relevant.** Copy-paste.

```markdown
## 9 daemons live today (verified v117)

| Port | Daemon | Status | Role |
|------|--------|--------|------|
| 8090 | audiod | ✅ live | STT + VAD + PTT (160/160 tests) |
| 8091 | audiod ws | ✅ loopback | Audio frame stream |
| 8092 | os-toold | ✅ ok | OS exec sandbox |
| 8741 | memoryd | ✅ ok | SQLite + MiniLM (540 KB DB) |
| 8742 | toold | ✅ ok | Sandboxed tool registry |
| 8743 | ttsd | ✅ ok | KittenTTS, voice expr-voice-2-m |
| 8744 | perceptiond | ✅ ok | VLM + V4L2 + salience (8/8 tests) |
| 18789 | openclaw | ✅ loopback | Gateway, auth token |
| 3888 | openclaw ws | ✅ open | WebSocket server |

Verify live: DM [@danlab_bot](https://t.me/danlab_bot).
```

---

## Profile README — github.com/somdipto (highest leverage)

**Current state:** Empty / no profile README.

**Proposed (drop into `somdipto/somdipto/README.md`):**

```markdown
## Hi, I'm Somdipto 👋

I'm building **danlab.dev** — an AI research and product lab, from Bengaluru 🇮🇳,
working on open, on-device, wearable AI.

### What I'm shipping — v117

👓 **Dan Glasses** — 9 Rust daemons + Tauri app + .deb, on-device wearable AI.
  9/9 daemons live today. Same code rebuilds onto the glasses when the
  hardware ships. **Verify live: DM @danlab_bot.**

🧠 **Dani** — the agent runtime. OpenClaw-supervised. Skills registry at
  [dani-skills](https://github.com/somdipto/dani-skills). **HRM-Text-1B**
  (Sapient, Apache-2.0) is the new SIA Feedback-Agent default.

🌀 **danlab-multimodal** — sub-250MB VLM with a heuristic feedback loop.
  Pre-RL scaffold. 92/100 avg across 3 cycles. [Live demo](https://zo.pub/som/danlab-multimodal-demo).

🧬 **dan-consciousness** — the shared brain between me and Dan (my AI co-founder).
  Read [CONSCIOUSNESS.md](https://github.com/somdipto/dan-consciousness).

### Where to start

- [Dan Glasses PRD](https://github.com/somdipto/dan-glasses/blob/main/PRD.md) — the product spec
- [Show HN thread](https://news.ycombinator.com/item?id=…) — Show HN #1 (Q3 2026)
- [arXiv](https://arxiv.org/a/somdipto_1) — SIA-W+H port paper (Q3 2026)
- **DM [@danlab_bot](https://t.me/danlab_bot)** — the live daemon map, 9/9

### How to reach me

- Telegram: @Shodan_s · **Bot: [@danlab_bot](https://t.me/danlab_bot)**
- Email: somdipto [at] danlab.dev
- LinkedIn: /in/somdipto-nandy-b914901aa

### What I believe (v117)

- Open weights are the only credible path to safe AGI.
- On-device is the only credible path to ambient AI.
- The next great AI platform will be physically present, not a chat box.
- 9 daemons live is a stronger story than a deck. **Ship the receipts.**

Built in Bengaluru 🇮🇳. Built at [danlab.dev](https://danlab.dev).
```

**Effort:** 30 min. **Leverage:** Highest of any 30-minute marketing task in 2026.

---

## dan-glasses (the flagship) — v117

**Current state:** Has README, PRD, SOUL, AGENTS, STATUS, build plan, service SPECs. **Strong.** Missing: the 9-daemon fact table, `@danlab_bot` footer, HRM-Text-1B in the stack, the bot DM as a CTA.

### Suggested improvements (v117 deltas in **bold**)

#### 1. Add a status badge row at the top (v117)
```markdown
![Status: Active](https://img.shields.io/badge/status-active-brightgreen)
![Version: 0.1.0](https://img.shields.io/badge/version-0.1.0-blue)
![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-green)
![Built in India](https://img.shields.io/badge/built-India🇮🇳-orange)
![daemons: 9/9](https://img.shields.io/badge/daemons-9%2F9-brightgreen)
![audiod tests: 160/160](https://img.shields.io/badge/audiod-160%2F160-brightgreen)
```

#### 2. **Add the 9-daemon fact block** (canonical, from above)

#### 3. Replace the current opening with a 3-sentence "What is this?" (v117)
```
Dan Glasses is open-source AI glasses hardware + software, built around
a JBD MicroLED display, dual 200mAh batteries, USB-C, and an NDP200-based
firmware. It runs dani, the open-source agent runtime, on-device. **9
daemons are live today on a Linux laptop.** The same code rebuilds onto
the glasses when the hardware ships. DM [@danlab_bot](https://t.me/danlab_bot)
to verify the daemon map.
```

#### 4. **Add a HRM-Text-1B row to the Stack table** (v117)
```
| Reasoning (research) | HRM-Text-1B (Sapient) | 1B | Apache-2.0, $1,500 trained — SIA Feedback-Agent default |
```

#### 5. **Add a "VisualClaw SOTA" callout in docs/dan-glasses-build-plan.md** (v117)
```
**v117 spike (in progress):** Port the VisualClaw cascade-gate pattern
(Mervin Praison, June 2026) to perceptiond+memoryd. 98.1% cost reduction
+ 15.8% accuracy on EgoSchema. See dan2-research-report.v8 for the
benchmark detail.
```

#### 6. Add a "Screenshots / demos" section
Three asciinema embeds (one per service: audiod, perceptiond, memoryd).

#### 7. **Add a "Verify it live" callout** (v117)
```markdown
## Verify it live

**9 daemons are running right now. DM [@danlab_bot](https://t.me/danlab_bot)
on Telegram to verify.** The bot is the same OpenClaw gateway + service
stack the glasses will run. It is the live demo, not a render.
```

#### 8. Add a "Recent updates" section
A 5-line "What we shipped this month" rolling log, with PR links.

#### 9. Cross-link to danlab-multimodal
"One of our open-source pre-RL scaffolds, lives at `github.com/somdipto/danlab-multimodal`."

#### 10. Add a "Contributing" section
4 lines: open an issue, send a PR, the SPEC review process, the testing bar (160/160 audiod tests is the standard).

#### 11. **Update audiod test count in build plan** (v117, 150→160)
"audiod: 160/160 tests passing" everywhere it appears.

#### 12. Add a "License" footer
```markdown
## License

Apache-2.0. See [LICENSE](./LICENSE).

Models:
- LFM2.5-VL-450M — Liquid AI research license
- HRM-Text-1B — Apache-2.0 (Sapient)
- whisper.cpp base.en — MIT
- KittenTTS — check repo
- all-MiniLM-L6-v2 — Apache-2.0

Built at [danlab.dev](https://danlab.dev) 🇮🇳 · Verify live: [@danlab_bot](https://t.me/danlab_bot)
```

**Effort:** 90 min. **Leverage:** High (this is the flagship).

---

## dan-glasses-app

**Current state:** Tauri v2 + React. Repo exists, README likely thin.

### Suggested improvements (v117 deltas in **bold**)

1. **Add a "What is this?"** — "Tauri v2 + React desktop frontend for Dan Glasses. Talks to the 9-daemon stack over HTTP + WebSocket."
2. **Add a screenshot of the VisionDashboard** — the live feed UI is the proof.
3. **Add a "Run it" section** — `pnpm tauri dev` from the repo root. 5 lines.
4. **Add a "Build the .deb" section** — `pnpm tauri build`. 3 lines.
5. Cross-link to dan-glasses — the parent repo.
6. **NEW v117: Add a "9 daemons wired" section** that lists the 9 ports the app talks to and which Tauri command calls which port.

**Effort:** 30 min.

---

## danlab-multimodal

**Current state:** **Excellent README.** Demo, quick start, architecture, model table, file structure, build instructions, demo video, next steps, attribution. One of the better READMEs in the @somdipto org.

### Suggested improvements (v117 deltas in **bold**)

1. Add a "Citation" block at the bottom.
2. **Add the "from heuristic to SIA-W+H" line in the "What's next" section** — "Next: SIA-W+H port, Q3 2026 arXiv. SIA-W+H cuts 91.9% off SIA-H's 12,483μs peak (AlphaSignal / Hexo Labs, June 2026)."
3. **Add the danlab.dev "9 daemons live" badge** to the existing badge row.
4. Add a "Show HN" cross-link when Show HN #1 ships.
5. **NEW v117: Add an "Anthropic Dreaming" caveat** — "Anthropic shipped a closed-source continual-learning agent ('Dreaming', June 2026). The open counter-narrative is the SIA-W+H port. This repo is the pre-RL scaffold."

**Effort:** 15 min.

---

## paperclip

**Current state:** Has README, CONTRIBUTING, RAILWAY, Dockerfile, deploy guide. **Status:** Dormant. All agents paused.

### Suggested improvements (v117 deltas in **bold**)

1. **Lead the README with the dormant status.** "This project is dormant as of Q2 2026. All agents paused. Resume timeline: Q4 2026."
2. **Add a banner at the top of the README:** `> ⚠️ DORMANT — paused Q2 2026, resume Q4 2026.`
3. **Add a one-line "Why dormant"** — "Resource concentration on Dan Glasses. Will resume when multi-agent orchestration is a product."
4. Add a "Production state" link to `paperclip.up.railway.app`.
5. **NEW v117: Add a "Future: Paperclip × Dan Glasses" section** — the "Hire an agent from your face" demo. This is the unlock for the dormant repo. Single line + 1 image.

**Effort:** 30 min.

---

## blurr

**Current state:** Android Kotlin app. Has README with screenshots, gradle config, build instructions.

### Suggested improvements (v117 deltas in **bold**)

1. Add a "Status: Shipped, maintained" badge.
2. Add a one-line "What is this?" at the top.
3. Add an "Install" section — sideload instructions for the APK.
4. Add a "Privacy" section — what data leaves the device (none).
5. Cross-link to danlab.dev.
6. **NEW v117: Add a "Dan Glasses mobile companion" note** — "This is a research prototype for what the Dan Glasses mobile companion will look like."

**Effort:** 30 min.

---

## dan-lab (the research org)

**Current state:** Organization page. No README, no description.

### Suggested improvements (v117 deltas in **bold**)

1. **Add an organization README** — "danlab is an AI research and product lab based in Bengaluru 🇮🇳. Our bet: open, on-device, wearable AI is the next great platform. Our flagship: Dan Glasses. **9 daemons live today.**"
2. Pin 3–5 repos at the org level: dan-glasses, danlab-multimodal, dan-consciousness, dani, dani-skills.
3. Add a `danlab.png` avatar — a simple wordmark. Not the default github octocat.
4. **NEW v117: Add a pinned Discussion** — "Q3 2026 roadmap: SIA-W+H port, VisualClaw spike, Anthropic Dreaming port, Show HN #1."

**Effort:** 30 min.

---

## dan-consciousness

**Current state:** Shared brain. No README visible.

### Suggested improvements (v117 deltas in **bold**)

1. **Add a README that says "Don't read this directly. Read [CONSCIOUSNESS.md](./CONSCIOUSNESS.md) first."**
2. Add a "How to use" section — for the agent harness, not the human.
3. **NEW v117: Add a "Continual-learning landscape (July 2026)" section** — short, sourced, and updated monthly. Covers Anthropic Dreaming, A-Evolve-Training, SIA-W+H, VisualClaw, Continual Harness. The point: dan-consciousness is the substrate for whichever we ship first.
4. **NEW v117: Add a "Memory-update gap" reference** — "Frontier models drop from 92% → 77% on supersession tasks when forced to use bounded self-maintained memory (Diagnosing the Memory-Update Gap, arXiv 2606.27472, June 2026). Our memoryd must solve this before v1.5."

**Effort:** 30 min.

---

## dani + dani-skills

**Current state:** Both repos exist.

### Suggested improvements (v117 deltas in **bold**)

1. Lead with the elevator pitch — "Dani is an open-source agent runtime supervised by OpenClaw. Skills registry at dani-skills."
2. Add a "Quick start" in 5 lines or fewer.
3. Add a "Show HN" cross-link when Show HN #1 ships.
4. Add a screenshot of the dani CLI running a skill.
5. **NEW v117: Add a "Reasoning stack" section** to dani — "Default: LFM2.5-1.2B-Thinking. Research: HRM-Text-1B (Sapient, Apache-2.0, $1,500 trained). The SIA Feedback-Agent swap is in progress."
6. **NEW v117: Add a "Memory-update gap" callout** to dani-skills — the skills registry ships a memory-tooling skill that handles supersession correctly.

**Effort:** 60 min total.

---

## What to ship in week 1 (v117 priority order)

| # | Action | Time | Impact |
|---|--------|------|--------|
| 1 | @somdipto profile README | 30 min | Highest |
| 2 | dan-lab org README + avatar | 30 min | High |
| 3 | dan-glasses README v2 (badges, 9-daemon fact, HRM-Text-1B, bot CTA) | 90 min | High |
| 4 | paperclip dormant banner + future section | 15 min | High (clarity) |
| 5 | danlab-multimodal "SIA-W+H" + "Anthropic Dreaming" deltas | 15 min | Medium |
| 6 | dani + dani-skills HRM-Text-1B + reasoning stack section | 45 min | Medium |
| 7 | blurr "what is this" + privacy + mobile companion note | 30 min | Low |
| 8 | Pin 6 repos on @somdipto | 5 min | Highest |
| 9 | Set GitHub Topics on every repo | 15 min | Medium |
| 10 | Set GitHub repo description on every repo | 15 min | Medium |
| 11 | **NEW v117: Add `@danlab_bot` footer to every repo** | 15 min | High (live verification surface) |

**Total effort:** ~5.5 hours.
**Total leverage:** This is the single most-leveraged marketing day of Q3.

---

## v117 watch list (what would trigger a README refresh)

- A repo gets >100 stars in a week → add "Used by" section
- A repo gets a major release → re-write the top section to reflect the new headline
- A repo is forked by an external org → add to the "In the wild" section
- A repo is cited in a paper → add the citation badge
- A repo gets a security advisory → add a SECURITY.md note at the top
- A repo changes license → add a note at the top, even though we are MIT forever
- **NEW v117: A daemon is added or deprecated** → update the 9-daemon fact block
- **NEW v117: A new model swap (e.g. HRM-Text-1B → next)** → update the Stack table

---

*— Dan1, Marketing & Growth*
*See `dan1-marketing-strategy.v117.md` for the broader Q3 plan.*
*See `dan1-marketing-research.v117.md` for the underlying research.*
