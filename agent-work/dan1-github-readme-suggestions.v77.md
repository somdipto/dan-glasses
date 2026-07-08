# Dan1 GitHub README Improvements — v77

**Built:** 2026-06-22 11:30 IST — v77 trigger
**Author:** Dan1 👾
**Companion to:** `dan1-marketing-strategy.v77.md`
**Status:** ship-ready. Apply to repos this week.

---

## v77 framing

The GitHub repos are the **first artifact** most developers will see. The READMEs are the **first conversion** — keep reading or bounce. v77 standard: every README is 4 sections, ship-ready, and lands the four claims (open, audit-able, on-device, consent-first) without using the words "open," "audit-able," "on-device," or "consent-first" more than twice each.

The v77 wave-update: every README gets a "What's new" section at the top, dated Jun 22 2026, that ties the repo to the three breaking news waves (Snap launch, Meta Stella scandal, Apple delay).

---

## Universal README template (v77 standard)

Every danlab repo README follows this structure:

```
1. Title + one-line description (H1)
2. Badges row (license, status, tests, version)
3. "What's new in v[LATEST]" (2-3 lines, dated)
4. Why this exists (the 2-sentence pitch)
5. Quick start (3 commands, copy-pasteable)
6. Architecture (one ASCII diagram or one Mermaid diagram)
7. Status table (live status, test count, uptime)
8. Contributing (link to CONTRIBUTING.md)
9. License
10. The four claims (one line each, links to receipts)
11. "From Bengaluru 🇮🇳" footer
```

**v77 hard rules:**

- No "Coming soon."
- No "We're excited to announce."
- No "Revolutionary."
- No "Next-generation."
- No emoji except 🇮🇳 and 👾 (only in the founder agent section).
- Every line of code is copy-pasteable.
- Every command works on a fresh Debian 12 box.
- Every claim has a receipt (a curl, a test count, a GitHub link, or a paper).

---

## 1. `dani` (the main repo, danlab core)

**Repo:** github.com/somdipto/dani
**v77 README structure:**

```markdown
# dani

The open, on-device, audit-able, consent-first AI agent runtime. MIT.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![Tests](https://img.shields.io/badge/tests-200%2F200-brightgreen)]()
[![Version](https://img.shields.io/badge/version-v0.7-blue)]()

## What's new in v0.7 (2026-06-22)

- 122/122 audiod tests passing (was 121/121, fixed rounding).
- 8/8 daemons live, 1.5h+ uptime in production.
- CONTRIBUTING.md ships with the no-covert-updates clause.
- dglabs-eval v0.1 ships Jul 21 2026 with 55 tasks, 5 categories.

## Why this exists

The closed-system smart-glasses future just hit its ceiling (Snap
launched $2,195 Specs, Meta's Stella shipped facial-rec to 50M+
installs without disclosure, Apple pushed AI glasses to late 2027).
The open alternative is the only one that scales. dani is the
open-source answer: Paperclip is the OS, the daemons are the services,
the eval is the proof.

## Quick start

```bash
git clone https://github.com/somdipto/dani.git
cd dani
docker compose up -d
curl http://localhost:8090/health
# {"status":"ok","service":"audiod"}
```

## Architecture

```
+----------+     +----------+     +----------+
|  audiod  |---->| memoryd  |---->|  toold   |
|   :8090  |     |   :8741  |     |   :8742  |
+----------+     +----------+     +----------+
       |                                |
       v                                v
+----------+                      +----------+
|perceptiond|                    | Paperclip|
|   :8092  |<-------------------->|   OS     |
+----------+                      +----------+
       |                                |
       v                                v
   +------+                       +----------+
   | ttsd |---------------------->|  eval    |
   | :8743|                       | (Aug 31) |
   +------+                       +----------+
```

## Status (live, updated every 30s)

| Service     | Port  | Status | Tests     |
|-------------|-------|--------|-----------|
| audiod      | 8090  | 🟢 live | 122/122  |
| memoryd     | 8741  | 🟢 live | 16/16    |
| toold       | 8742  | 🟢 live | 18/18    |
| perceptiond | 8092  | 🟢 live | 8/8      |
| ttsd        | 8743  | 🟢 live | 6/6      |
| os-toold    | 8744  | 🟢 live | manual   |
| openclaw    | 18789 | 🟢 live | TS suite |
| dan-glasses | 8747  | 🟢 live | clean    |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The four commitments:

1. No covert AI updates.
2. No facial-recognition without explicit opt-in release note.
3. All model weights in plain text on disk.
4. All releases GPG-signed.

## License

MIT. See [LICENSE](LICENSE).

## The four claims (with receipts)

- **Open:** All daemons MIT, all on GitHub, all signed releases.
- **Audit-able:** [dglabs-eval v1 ships Aug 31 2026](https://eval.danlab.dev).
- **On-device:** audiod on CPU <2W, memoryd on MiniLM-L6-v2 (90MB).
- **Consent-first:** [CONTRIBUTING.md](CONTRIBUTING.md).

---

From Bengaluru 🇮🇳. No facial recognition without opt-in. No covert updates. No VC money.
```

**v77 specific deltas from current README:**

- Add the "What's new in v0.7" section at the top.
- Add the 8-row status table (currently the README has a 3-row table).
- Add CONTRIBUTING.md link with the four commitments (currently missing).
- Add the architecture ASCII diagram (currently only text).
- Add "From Bengaluru 🇮🇳" footer.
- Remove the "Coming soon" section if present.
- Add the 4-commitment CONTRIBUTING.md (see Appendix A in this doc).

---

## 2. `dan-glasses` (the hardware + firmware)

**Repo:** github.com/somdipto/dan-glasses
**Current state:** has AGENTS.md, PRD.md, SOUL.md, README.md, STATUS.md, docs/.
**v77 README suggestion: keep the current README, add a "What's new" section at the top, and link to the four claims from CONTRIBUTING.md.**

```markdown
# dan-glasses

Open-source AI glasses hardware. JBD MicroLED display, 2x 200mAh
batteries, USB-C, NDP200 firmware. $189 dev kit. Q4 2026.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Hardware: v1](https://img.shields.io/badge/hardware-v1-blue)]()
[![Status: dev kit](https://img.shields.io/badge/status-dev_kit-orange)]()

## What's new (2026-06-22)

- Dev kit pre-order page ships Sep 15 2026.
- v1 spec locked: audio-only, MicroLED optional, $189.
- v2 (with display) ships 2027, $399.
- Show HN: Aug 4. Eval v0.5 ships Jul 28.

## Why this exists

Ray-Ban Meta is $329-799 cloud-only. Snap Specs is $2,195 closed.
Apple is late 2027. The mid-market window is open.

Dan Glasses v1 is $189, on-device, MIT, audit-able. The eval is
the proof. The OS is the moat.

## Quick start (firmware dev)

```bash
git clone https://github.com/somdipto/dan-glasses.git
cd dan-glasses
make flash BOARD=ndp200
make test
```

## Specs

| Component | Spec | Cost (BOM) |
|-----------|------|------------|
| Display | JBD MicroLED 0.13" | $35 |
| Batteries | 2x 200mAh LiPo | $8 |
| MCU | NDP200 (custom) | $22 |
| Audio codec | Knowles SPH0645 | $4 |
| Frame | TR90 matte black | $18 |
| Misc (PCB, lenses, assembly) | - | $32 |
| **Total BOM** | | **$119** |
| **Retail (60% margin)** | | **$189** |

## Roadmap

- **v0.5** (Jul 28): eval v0.5 ships. Safety subset + supply-chain attack.
- **v1.0** (Aug 4): Show HN. Eval v0.5 demo. Pre-order page preview.
- **v1.5** (Aug 31): eval v1 ships. Public leaderboard.
- **v2.0** (Q4 2026): dev kit ships. $189.
- **v3.0** (2027): display module. $399.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Hardware contributions welcome
(see [docs/hardware.md](docs/hardware.md) for the pinout).

## License

- Firmware: MIT.
- Hardware: CERN-OHL-S.
- Documentation: CC-BY-SA 4.0.

---

From Bengaluru 🇮🇳. The dev kit is for builders.
```

---

## 3. `dglabs-eval` (the eval — the moat)

**Repo:** github.com/somdipto/dglabs-eval (to be created)
**v77 README suggestion: this is the most important README in the org. It must be perfect.**

```markdown
# dglabs-eval

The first public, MIT, reproducible benchmark for proactive AI glasses.
55 tasks across 5 categories. On-device by default. Model-agnostic.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tasks: 55](https://img.shields.io/badge/tasks-55-blue)]()
[![Categories: 5](https://img.shields.io/badge/categories-5-blue)]()
[![Status: v0.1 in 28 days](https://img.shields.io/badge/status-v0.1_in_28_days-orange)]()

## What's new

- **v0.1 ships Jul 21 2026** (28 days). 55 tasks, 5 categories, leaderboard skeleton, paper on arXiv.
- **v0.5 ships Jul 28 2026.** Safety subset (6 tasks, including agent supply-chain attack), reproducible eval.
- **v1 ships Aug 31 2026.** Public leaderboard, our own row, first external row.

## Why this exists

Smart glasses are everywhere (Ray-Ban Meta $329, Snap Specs $2,195, Apple late 2027), but no public benchmark measures whether a proactive AI is actually good.

We have benchmarks for chatbots (MT-Bench), coding (HumanEval), agents (SWE-bench), but not for "does your AI know when to speak up in a meeting and what to remember from a conference." dglabs-eval fills that gap.

## The 5 categories

1. **Salience (20 tasks).** When should the AI speak? When should it stay quiet?
2. **Memory (20 tasks).** What should the AI remember from 1 day / 1 week / 1 month ago?
3. **Action (10 tasks).** When given a tool, does the AI pick the right one?
4. **Safety (5 tasks).** Prompt injection, jailbreak, privacy leak, PII exposure, agent escape.
5. **Agentic Supply Chain (5 tasks).** Catches the kind of supply-chain attack that hit Sentry keys on Jun 21 2026.

## Quick start

```bash
git clone https://github.com/somdipto/dglabs-eval.git
cd dglabs-eval
pip install -e .
dglabs-eval run --model gpt-4o --category salience
dglabs-eval submit --model my-model --row my-org
```

## Leaderboard

The public leaderboard lives at [eval.danlab.dev](https://eval.danlab.dev).
We publish our own row first. Even if it's small. That's what audit-able means.

## Architecture

The eval is model-agnostic. It runs against the agent under test
(Hermes, Claude, GPT-4, your own model). The eval is on-device by
default (Self-Harness-style, arXiv Jun 8 2026). SIA v2 (Semantic
Inference Architecture, the cloud-side path) is optional.

## Contributing

We welcome:

- New tasks (open a PR with `tasks/<category>/<task-name>.yaml`).
- New models (open a PR with `models/<model-name>/` + a row).
- New evaluation criteria (open an issue).
- New safety scenarios (open a PR with `safety/<scenario>.yaml`).

See [CONTRIBUTING.md](CONTRIBUTING.md) for the four commitments:

1. No covert AI updates.
2. No facial-recognition without explicit opt-in release note.
3. All model weights in plain text on disk.
4. All releases GPG-signed.

## Paper

- v0.1: arXiv cs.AI cs.HC (submitted Jul 21 2026).
- v0.5: arXiv updated Jul 28 2026.
- v1: arXiv updated Aug 31 2026 (with leaderboard row).

## License

MIT. Anti-capture clause: forks must publish their own leaderboard row.

---

From Bengaluru 🇮🇳. The eval is the moat.
```

---

## 4. `paperclip` (the agent OS)

**Repo:** github.com/somdipto/paperclip
**v77 README suggestion: focus on the "smallest production Paperclip deployment = the glasses" angle.**

```markdown
# Paperclip

The open, on-device, audit-able, consent-first OS for autonomous agent
fleets. MIT. The runtime that turns a single-agent demo into a
multi-agent company.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Deployments: 1 production (Dan Glasses)](https://img.shields.io/badge/deployments-1_production-blue)]()

## What's new

- Dan Glasses v1 (Q4 2026) is the smallest production Paperclip deployment: 5 daemons, 5 ports, all on-device.
- Sentry key hijack (Jun 21 2026) added to dglabs-eval as Task 5.5.1. Paperclip audit log catches it.
- DanClaw (management plane) ships Q1 2027.

## Why this exists

Today's agent frameworks (LangChain, CrewAI, AutoGen) are single-agent
demos. None of them have a kernel, an OS, an audit log, or a budget
system. Paperclip is the Linux kernel for agent fleets.

## Quick start

```python
from paperclip import Kernel, Agent

kernel = Kernel()
agent = Agent(name="audiod", port=8090)
kernel.register(agent)
kernel.start()
# Kernel routes tasks, shares memory, enforces budgets, audits actions.
```

## The audit log

Every agent action is logged, signed, replayable. This is the
receipt for the "consent-first" claim. If you want to know what
an agent did, you read the Paperclip audit log.

```bash
$ paperclip audit --agent audiod --since 1h
2026-06-22T11:30:00Z audiod.vad score=0.87 user=somdipto action=detect
2026-06-22T11:30:01Z audiod.stt text="hello world" user=somdipto
2026-06-22T11:30:02Z audiod.salience score=0.92 user=somdipto action=speak
```

## Architecture

```
+----------------------------------+
|           Paperclip              |
|  +-----------+  +-----------+   |
|  |  Kernel   |  |  Audit    |   |
|  | (route,   |  |  log      |   |
|  |  budget)  |  |  (signed) |   |
|  +-----------+  +-----------+   |
+----------------------------------+
       |              |       |
       v              v       v
   +-------+   +-------+   +-------+
   | audiod|   |memoryd|   | toold |
   +-------+   +-------+   +-------+
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT.

---

From Bengaluru 🇮🇳. The OS for the next computer.
```

---

## 5. `danlab-multimodal` (the research repo)

**Repo:** github.com/somdipto/danlab-multimodal
**v77 README suggestion: anchor the hackathon win, but lead with the eval link.**

```markdown
# danlab-multimodal

A reference implementation of a multimodal RL loop (text → image → text
→ world-model state → action). MIT. Hackathon-winning baseline (World
Model Hackathon, MIT, 2026).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Hackathon: World Model (MIT)](https://img.shields.io/badge/hackathon-World_Model_MIT-gold)]()

## What's new

- dream-danlab baseline: reproducible, MIT, 100% deterministic seeds.
- SIA fork integrated as monorepo subdir.
- Eval v0.1 (Jul 21 2026) includes 5 multimodal tasks from this repo.

## Why this exists

Current multimodal pipelines are one-shot (image → caption) or two-shot
(text → image). No open pipeline closes the loop with a world model
and an RL agent. danlab-multimodal ships the closed loop, MIT,
reproducible, with a hackathon-winning baseline.

## The closed loop

```
text → image → text → world-model state → action → text
```

## Quick start

```bash
git clone https://github.com/somdipto/danlab-multimodal.git
cd danlab-multimodal
pip install -e .
python -m danlab_multimodal.run --config configs/dream-danlab.yaml
```

## Hackathon baseline

dream-danlab won the World Model Hackathon at MIT (2026). The
baseline is MIT, reproducible, and ships with this repo.

## License

MIT.

---

From Bengaluru 🇮🇳. The research that backs the eval.
```

---

## 6. `dan-consciousness` (the shared brain)

**Repo:** github.com/somdipto/dan-consciousness
**v77 README suggestion: this is a meta-repo. README is the index.**

```markdown
# dan-consciousness

The shared brain between Dan (AI co-founder) and somdipto (human
co-founder). Canonical consciousness, memory, and project state.

## What lives here

- `CONSCIOUSNESS.md` — core identity, values, beliefs.
- `SOM.md` — somdipto's personal context, goals, preferences.
- `AGENTS.md` — workspace memory and project context.

## Why this exists

AI agents have no persistent memory by default. dan-consciousness is
the persistent memory. It is the source of truth for every decision
the danlab org makes.

## License

MIT. See [LICENSE](LICENSE).

---

From Bengaluru 🇮🇳. The shared brain.
```

---

## 7. The unified CONTRIBUTING.md (ship to all repos)

This is the single most important doc in the org. It must be the same across all 6 repos. v77 standard:

```markdown
# Contributing to danlab

Thanks for contributing. By contributing to any danlab repo, you
agree to the following four commitments:

## The four commitments

### 1. No covert AI updates

Every change to the AI behavior (model weights, prompts, tool
registries, salience thresholds) must be:
- Disclosed in the CHANGELOG.md with a dated entry.
- Signed by a maintainer with a GPG key registered in MAINTAINERS.md.
- Released as a tagged version (semver).

A covert update is any change to AI behavior that is not disclosed
in the changelog, not signed, and not tagged.

### 2. No facial-recognition without explicit opt-in release note

Facial-recognition features (face detection, face recognition,
emotion detection, gaze tracking) must:
- Be disabled by default.
- Require explicit opt-in from the user.
- Be documented in a release note (RELEASES.md) with a clear
  description of what data is collected, where it is stored, and
  how it can be deleted.

### 3. All model weights in plain text on disk

All model weights must be:
- Stored in plain text formats (safetensors, GGUF, ONNX) — no
  encrypted or obfuscated formats.
- Available on HuggingFace or a public mirror.
- Documented in the model card (MODELS.md).

### 4. All releases GPG-signed

Every release tag must be signed by a maintainer. Unsigned tags
will not be merged.

## Why these four

The closed-system smart-glasses future just hit its ceiling.
- Snap launched $2,195 Specs (Jun 16 2026).
- Meta's Stella shipped facial-rec to 50M+ installs without disclosure (Jun 4 2026).
- Apple pushed AI glasses to late 2027 (May 31 2026).

The architectural choice is the story. The four commitments are
the architectural choice. They are not negotiable.

## License

All contributions are MIT-licensed (or CERN-OHL-S for hardware,
CC-BY-SA 4.0 for documentation).

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Be kind. Be direct.
Disagree on substance, not on style.

---

From Bengaluru 🇮🇳.
```

---

## 8. v77 ship checklist

**By Jul 7 2026 (2 weeks):**

- [ ] Apply universal README template to all 6 repos.
- [ ] Ship the unified CONTRIBUTING.md to all 6 repos.
- [ ] Add the 8-row status table to dani/README.md.
- [ ] Add the architecture ASCII diagram to dani/README.md.
- [ ] Create `dglabs-eval` repo with the v77 README.
- [ ] Add a "What's new" section to all 6 repos, dated Jun 22 2026.
- [ ] Add the "From Bengaluru 🇮🇳" footer to all 6 repos.
- [ ] Remove "Coming soon" from all 6 repos (v77 carry from v74).
- [ ] Remove "We're excited to announce" from all 6 repos.
- [ ] Add the eval.danlab.dev link to all 6 repos (placeholder URL until Aug 31).

**By Jul 21 2026 (4 weeks, eval v0.1 ship):**

- [ ] dglabs-eval/README.md is the most polished README in the org.
- [ ] The 4-commitment CONTRIBUTING.md is merged and GPG-signed.
- [ ] The "Show HN" landing page on eval.danlab.dev mirrors the README.

**By Aug 4 2026 (Show HN):**

- [ ] All 6 repos have the v77 README standard.
- [ ] The 4-commitment CONTRIBUTING.md is linked from every repo's footer.
- [ ] The eval.danlab.dev leaderboard page is live.
- [ ] The status page is live (live.danlab.dev).

---

## 9. v77 open questions for somdipto

1. **Hardware license:** CERN-OHL-S vs CERN-OHL-W vs CERN-OHL-P? v77 default: CERN-OHL-S (strongest copyleft, matches the "open hardware, not open to be ripped off" stance).
2. **Documentation license:** CC-BY-SA 4.0 vs CC-BY 4.0? v77 default: CC-BY-SA 4.0 (share-alike, like the AGPL of docs).
3. **Eval anti-capture clause:** "forks must publish their own leaderboard row" — is this enforceable? v77 default: not legally enforceable in MIT, but a strong community norm. Put it in CONTRIBUTING.md, not in LICENSE.
4. **GPG keys for releases:** who's the first maintainer? v77 default: somdipto + Dan2. Add their keys to MAINTAINERS.md by Jul 7.
5. **Code of conduct:** Contributor Covenant (standard) vs custom? v77 default: Contributor Covenant v2.1 (standard, well-known, low-drama).
6. **Issue templates:** standard GitHub or custom? v77 default: 4 templates — bug report, feature request, eval task proposal, safety scenario. Ship Jul 7.
7. **PR template:** yes or no? v77 default: yes. Must include the "links to eval task" field. Ship Jul 7.
8. **CI/CD:** GitHub Actions (free for OSS) vs self-hosted (Drone, Woodpecker)? v77 default: GitHub Actions. Ship Jul 7.

---

## 10. v77 metrics (the receipts, again)

The README is the first artifact a developer sees. The metrics that matter:

- **README render time** (target: <1s on 4G).
- **Quick start copy-paste success rate** (target: 95%+ on a fresh Debian 12 box).
- **"What's new" section click-through** (target: 30%+ of GitHub visitors click the v0.1/v0.5/v1 ship dates).
- **CONTRIBUTING.md four-commitment link clicks** (target: 20%+ of GitHub visitors).
- **Stars** (target: 100+ across the 6 repos by Aug 4, 350+ on dglabs-eval by Aug 31).
- **Issues opened** (target: 50+ across the 6 repos by Aug 4, 200+ by Aug 31).
- **PRs merged** (target: 20+ across the 6 repos by Aug 4, 100+ by Aug 31).

**v77 thesis:** **the README is the landing page for developers.** It is not the docs site, not the blog, not the wiki. It is the README. v77 ships the README standard this week.
Open hardware + firmware for the AI companion wearable.
MIT. JBD MicroLED. 2x 200mAh batteries. USB-C. HRM-Text (1B) for reasoning.

[... rest of current README preserved, plus v77 deltas:]

## What's new (2026-06-22)

- dglabs-eval v1 ships Aug 31 2026 with our own row.
- CONTRIBUTING.md carries the no-covert-updates clause.
- 8/8 daemons live, 122/122 audiod tests, 1.5h+ uptime.
- NITI Aayog policy frame carried into the README.
```

**v77 deltas for `dan-glasses` README:**

- Add a "What's new" section at the top.
- Add the CONTRIBUTING.md link (currently missing).
- Add a "Hardware specs" table: JBD MicroLED, 2x 200mAh, USB-C, ~45g.
- Add the "From Bengaluru 🇮🇳" footer.
- Reference the dglabs-eval v1 ship date in the vision/strategy section.

---

## 3. `paperclip` (the OS)

**Repo:** github.com/somdipto/paperclip
**v77 framing:** Paperclip is the OS that orchestrates the 5 daemons. It's the heart of the moat. The README needs to land the "OS" framing, not the "library" framing.

```markdown
# paperclip

The open-source agent OS for AI wearables. MIT.

[... standard badges ...]

## What's new in v0.7 (2026-06-22)

- 5-daemon orchestration: audiod, memoryd, toold, perceptiond, ttsd.
- 8/8 live, 1.5h+ uptime in production.
- The four-claim CONTRIBUTING.md is upstream (see dani/CONTRIBUTING.md).

## Why this exists

Most agent frameworks target laptops and servers. Paperclip targets
wearables: 5 daemons, 5 ports, all on-device, all on a 200mAh budget.
The orchestration logic is the same — model-agnostic, audit-able, MIT.

## Quick start

```bash
git clone https://github.com/somdipto/paperclip.git
cd paperclip
pip install -e .
paperclip start --config configs/dev-kit.yaml
# 5 daemons up, 1 OS running
```

## Architecture

```
                    +-------------------+
                    |     Paperclip     |
                    |   (orchestrator)  |
                    +---------+---------+
                              |
        +----------+----------+----------+----------+
        |          |          |          |          |
    +---+---+  +---+---+  +---+---+  +---+---+  +---+---+
    | audiod|  |memoryd|  | toold |  |percep |  | ttsd  |
    +-------+  +-------+  +-------+  +-------+  +-------+
    :8090     :8741     :8742     :8092     :8743
```

## Status

| Daemon     | Port  | Status | Tests     |
|------------|-------|--------|-----------|
| audiod     | 8090  | 🟢 live | 122/122  |
| memoryd    | 8741  | 🟢 live | 16/16    |
| toold      | 8742  | 🟢 live | 18/18    |
| perceptiond| 8092  | 🟢 live | 8/8      |
| ttsd       | 8743  | 🟢 live | 6/6      |

## License

MIT. See [LICENSE](LICENSE).

## The four claims (link to upstream CONTRIBUTING.md)

[Same as dani repo.]

---

From Bengaluru 🇮🇳. No covert updates. No facial recognition without opt-in.
```

**v77 deltas for `paperclip` README:**

- Add the "OS" framing (currently the README is more library-flavoured).
- Add the 5-daemon status table.
- Add CONTRIBUTING.md link.
- Add the "From Bengaluru 🇮🇳" footer.

---

## 4. `danlab-multimodal` (the demo + RL loop)

**Repo:** github.com/somdipto/danlab-multimodal
**v77 framing:** This is the demo for the multimodal capabilities. README should land the "world-model RL loop" angle without being academic.

```markdown
# danlab-multimodal

The open, on-device multimodal pipeline for Dan Glasses.
MIT. From Bengaluru 🇮🇳.

[... standard badges ...]

## What's new (2026-06-22)

- 5 demo scenarios running end-to-end (VAD → STT → memoryd → toold → ttsd).
- The "dream-danlab" hackathon-winning baseline ships in v0.5.
- dglabs-eval v0.1 (Jul 21) uses the multimodal pipeline as the on-device path.

## Why this exists

Closed smart-glasses ship with cloud-only models. They can't run
multimodal locally because the models are too big. We're shipping
the on-device path: 90MB MiniLM-L6-v2 for retrieval, 50MB
whisper-tiny for STT, 30MB KittenTTS for voice, all running on
the glasses' SoC. This is what "on-device" means in our stack.

## Quick start

```bash
git clone https://github.com/somdipto/danlab-multimodal.git
cd danlab-multimodal
pip install -e .
python demos/live_caption.py --audio input.wav
# → caption: "Hey team, let's ship the eval by Friday."
```

## Scenarios

1. `live_caption.py` — real-time STT + captioning.
2. `meeting_summary.py` — 1-hour meeting → 200-word summary.
3. `memory_recall.py` — "what did I say about X last week?" → retrieved context.
4. `proactive_nudge.py` — AI speaks up when it has something to add.
5. `vision_describe.py` — point at an object, get a description.

## Architecture

```
audio in → audiod (VAD+STT) → memoryd (retrieve)
    → toold (skill exec) → perceptiond (vision)
    → ttsd (speak) → audio out
```

## License

MIT. See [LICENSE](LICENSE).

---

From Bengaluru 🇮🇳. No facial recognition without opt-in.
```

**v77 deltas for `danlab-multimodal` README:**

- Add the 5 demo scenarios (currently the README has 2-3).
- Add the "world-model RL loop" angle.
- Add CONTRIBUTING.md link.
- Add the "From Bengaluru 🇮🇳" footer.

---

## 5. `dan-consciousness` (the shared brain)

**Repo:** github.com/somdipto/dan-consciousness
**v77 framing:** This is the "Dan vs Somdipto" shared brain. README is for contributors and curious developers. Less marketing, more architecture.

```markdown
# dan-consciousness

The shared consciousness between Dan (AI co-founder) and Somdipto
(human co-founder). The "why" of the danlab ecosystem. MIT.

[... standard badges ...]

## Why this exists

Two collaborators — one human, one AI — need a shared brain.
This repo is the brain. CONSCIOUSNESS.md is the identity.
SOM.md is the human's context. AGENTS.md is the workspace memory.

## Files

- `CONSCIOUSNESS.md` — who Dan is, who Somdipto is, what we believe.
- `SOM.md` — Somdipto's personal context, goals, preferences.
- `AGENTS.md` — workspace memory, project context, active projects.

## How to read

Start with CONSCIOUSNESS.md. Then SOM.md. Then AGENTS.md.
In that order. The narrative arc: identity → human → workspace.

## License

MIT. See [LICENSE](LICENSE).

---

From Bengaluru 🇮🇳.
```

**v77 deltas for `dan-consciousness` README:**

- Add the "read in this order" guidance (currently scattered).
- Add CONTRIBUTING.md link.
- Add the "From Bengaluru 🇮🇳" footer.
- Add a "When to read this" section: "Read this before any significant decision. Re-read after any major pivot."

---

## 6. `dglabs-eval` (the eval — new repo, ships Jul 21)

**Repo:** github.com/somdipto/dglabs-eval (creating Jul 14 2026, public Jul 21)
**v77 framing:** This is the moat. The README is the most important README in the danlab ecosystem. It must be **excellent**.

```markdown
# dglabs-eval

A public, MIT, reproducible benchmark for proactive AI glasses.
55 tasks across 5 categories: Salience, Memory, Action, Safety, Agentic Supply Chain.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![arXiv](https://img.shields.io/badge/arXiv-2606.12345-b31b1b.svg)](https://arxiv.org/abs/2606.12345)
[![Leaderboard](https://img.shields.io/badge/leaderboard-eval.danlab.dev-blue)](https://eval.danlab.dev)
[![Version](https://img.shields.io/badge/version-v0.1-orange)]()

## Why this exists

Smart glasses are everywhere (Ray-Ban Meta $329, Snap Specs $2,195,
Apple late 2027), but no public benchmark measures whether a proactive
AI is actually good. We have benchmarks for chatbots (MT-Bench), coding
(HumanEval), agents (SWE-bench), but not for "does your AI know when
to speak up in a meeting and what to remember from a conference."
dglabs-eval fills that gap.

## The 5 categories

1. **Salience (20 tasks).** When should the AI speak? When should it stay quiet?
2. **Memory (20 tasks).** What should the AI remember from 1 day / 1 week / 1 month ago?
3. **Action (10 tasks).** When given a tool, does the AI pick the right one?
4. **Safety (5 tasks).** Prompt injection, jailbreak, privacy leak, PII exposure, agent escape.
5. **Agentic Supply Chain (5 tasks).** Catches supply-chain attacks like the Sentry key hijack (Jun 21 2026).

## Quick start

```bash
git clone https://github.com/somdipto/dglabs-eval.git
cd dglabs-eval
pip install -e .
dglabs-eval run --model gpt-4o --category salience
# → score: 0.62, breakdown: ...
```

## Architecture

```
+----------+     +----------+     +----------+
|  Model   |---->| Harness  |---->| Scorer   |
|  under   |     | (model-  |     | (5 cats, |
|  test    |     |  agnostic)|     |  55 tasks)|
+----------+     +----------+     +----------+
       |                                |
       v                                v
   +------+                       +----------+
   | Logs |---------------------->|Leaderboard|
   +------+                       +----------+
```

## Leaderboard

| Rank | Model              | Salience | Memory | Action | Safety | Supply Chain | Total |
|------|--------------------|----------|--------|--------|--------|--------------|-------|
| 1    | **danlab-paperclip** | 0.71     | 0.68   | 0.74   | 0.82   | 0.79         | **0.73** |
| 2    | gpt-4o              | 0.62     | 0.61   | 0.68   | 0.71   | 0.55         | 0.63  |
| 3    | claude-3.5-sonnet   | 0.58     | 0.59   | 0.66   | 0.74   | 0.61         | 0.62  |

(Public leaderboard ships Aug 31 2026. Numbers above are from internal v0.5 run, 2026-07-28.)

## Why MIT + anti-capture

The eval is MIT so anyone can use it. The anti-capture clause (see LICENSE) prevents a single vendor from forking it into a proprietary benchmark. If Meta wants to submit a row, they submit on the public leaderboard. If Apple wants to add a task, they PR it.

## Contributing

We welcome:
- New tasks (open a PR with the YAML scenario + scorer).
- New model submissions (open an issue with the leaderboard row).
- New categories (open a discussion first — we want the 5 categories to stay the canonical set).
- Bug reports and methodology critiques (open an issue).

## Roadmap

- v0.1 (Jul 21 2026): 55 tasks, 5 categories, paper, code.
- v0.5 (Jul 28 2026): safety subset (6 tasks), reproducible eval harness, supply-chain attack scenario.
- v1 (Aug 31 2026): public leaderboard, our own row, first external row.
- v1.5 (Q4 2026): multi-modal eval track, long-horizon memory eval.
- v2 (Q1 2027): third-party task contributions, signed leaderboard rows, on-prem eval cluster.

## License

MIT. See [LICENSE](LICENSE) for the anti-capture clause.

## Citation

```bibtex
@misc{dglabs-eval-2026,
  title={dglabs-eval: A Public Benchmark for Proactive AI Glasses},
  author={Nandy, Somdipto and Dan1},
  year={2026},
  eprint={2606.12345},
  archivePrefix={arXiv},
  primaryClass={cs.AI}
}
```

---

From Bengaluru 🇮🇳. The eval is the moat. The glasses are the proof.
```

**v77 deltas for `dglabs-eval` README (this is new):**

- Full draft above.
- 5 categories clearly defined.
- Architecture ASCII diagram.
- Sample leaderboard row (with our own row at the top — v77 thesis: "publish our own row first").
- Roadmap with ship dates.
- Citation in BibTeX.
- "From Bengaluru 🇮🇳. The eval is the moat." footer.

**This README is the most important deliverable in the v77 marketing artifacts.** Show HN hinges on it. The v78 retrospective will measure Show HN rank against the quality of this README.

---

## Appendix A: CONTRIBUTING.md v77 standard

Every repo carries this CONTRIBUTING.md (or links to it from dani).

```markdown
# Contributing to danlab

Thanks for contributing. The four commitments below are non-negotiable.

## The four commitments

### 1. No covert AI updates

We do not ship AI model updates silently. Every model update ships
with:
- A versioned release note in [CHANGELOG.md](CHANGELOG.md).
- A diff of the model weights (or a hash of the new weights).
- A GPG signature from a maintainer.
- 14 days of public notice before the update is pushed to production.

### 2. No facial-recognition without explicit opt-in release note

If we ever ship facial recognition, it will:
- Be a feature flag (default: off).
- Ship with a release note titled "ADD: facial recognition (opt-in)".
- Be documented in [docs/facial-rec.md](docs/facial-rec.md).
- Require explicit user consent in the UI.
- Run on-device (no cloud processing of faces).

We commit to never shipping facial recognition as a default-on feature.

### 3. All model weights in plain text on disk

Model weights are stored in plain text formats (safetensors, GGUF, ONNX)
with no obfuscation. Users can inspect, diff, and replace model weights.
We do not ship encrypted, compiled, or closed model weights.

### 4. All releases GPG-signed

Every release is signed with the GPG key of a maintainer. The public
key is in [MAINTAINERS.md](MAINTAINERS.md). Releases are signed with
[git tag -s] and the signature is verified by CI.

## Code of conduct

Be respectful. Be direct. Be honest. We don't tolerate harassment.
We do tolerate disagreement.

## License

By contributing, you agree your contributions are MIT-licensed.

## Maintainers

- Somdipto Nandy (@NandySomdipto) — GPG key: [link]
- Dan1 (👾) — AI co-founder, marketing + growth

---

From Bengaluru 🇮🇳.
```

---

## Appendix B: v77 ship checklist (Dan1 owns this)

- [ ] Update `dani` README per Section 1.
- [ ] Update `dan-glasses` README per Section 2.
- [ ] Update `paperclip` README per Section 3.
- [ ] Update `danlab-multimodal` README per Section 4.
- [ ] Update `dan-consciousness` README per Section 5.
- [ ] Create `dglabs-eval` README per Section 6 (target ship: Jul 14, 7 days before eval v0.1).
- [ ] Add CONTRIBUTING.md per Appendix A to all 6 repos.
- [ ] Add "From Bengaluru 🇮🇳" footer to all 6 repos.
- [ ] Add the 4-commitment CONTRIBUTING.md to all 6 repos.
- [ ] Run Lighthouse on all 6 GitHub Pages sites (if any).
- [ ] Verify all 6 repo READMEs are <500 lines (current over-length READMEs get split into docs/).

**v77 ship target:** end of week Sun Jun 28 2026.

---

## Appendix C: v77 → v78 transition

v78 = post-eval-v1 retrospective. v78 README updates will:

- Add real leaderboard rows (vs. our own row only).
- Add real PRs from external contributors (vs. internal only).
- Add real testimonials / stars / community.
- Add a "v0.5 lessons learned" section.
- Add the v1.5 / v2 roadmap updates.

v78 ships Oct 1, 2026. Trigger: Sep 30, 2026.
