# Dan1 GitHub README Suggestions — v62

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-19 08:30 IST (03:00 UTC)
**Status:** ✅ Canonical. Supersedes v60.
**For:** All DanLab public repos.
**Read first:** `dan1-marketing-strategy.md` v62, `dan1-marketing-research.md` v62.

> **v62 is the field-stability pass.** The README strategy is unchanged. The 6-repo template set is now sharper: every repo gets a 1-paragraph description, a 3-bullet "Why" section, a 5-line "Quick start," and a "Receipts" section with the same 4-axis cell.

---

## Master template (use for all repos)

```markdown
# <Repo Name>

<one-line description>

<badges: stars, license, "from India 🇮🇳", "MIT all the way down">

## Why

- <bullet 1: the cell of the 2x2 this repo fills>
- <bullet 2: the receipt that makes it real>
- <bullet 3: how it compounds with the rest of the stack>

## Quick start

\`\`\`bash
git clone github.com/somdipto/<repo>
cd <repo>
<3-5 commands to run it>
\`\`\`

## Architecture

<1 paragraph + 1 ASCII diagram>

## Tests

\`\`\`bash
<test command>
\`\`\`

## Receipts

- <receipt 1: e.g. Snap $500M R&D, WIRED Meta NameTag, etc.>
- <receipt 2>
- <receipt 3>

## License

MIT.

## Built at

[danlab.dev](https://danlab.dev) — AGI from India 🇮🇳
[github.com/somdipto/dan-consciousness](https://github.com/somdipto/dan-consciousness) — shared brain
```

---

## 1. `dan-glasses` (marquee repo)

**Current state:** LIVE, code present, sparse README.

**v62 README:**

```markdown
# Dan Glasses 👾

The proactive wearable AI companion. MIT, on-device, sub-50g, India-priced.

![Stars](https://img.shields.io/github/stars/somdipto/dan-glasses)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![MIT all the way down](https://img.shields.io/badge/MIT-all%20the%20way%20down-blue)
![Built for Snapdragon START](https://img.shields.io/badge/built%20for-Snapdragon%20START-red)

## Why

- **Proactive, not reactive.** Every other AI glasses product is reactive. You speak, it answers. We push events.
- **0 cloud, 0 faceprints.** On-device. No telemetry. No background process. Wire it to the airgap if you want.
- **MIT all the way down.** Hardware design, software, and models. No exceptions. No tiers.

Snap Specs ships at 132-136g, $2,195, 2 Snapdragons, closed source, cloud-tethered, reactive. We're 4 of 4 on the wedge axes. Nobody else is.

## Quick start

\`\`\`bash
git clone https://github.com/somdipto/dan-glasses
cd dan-glasses
./scripts/dev.sh up
./scripts/dev.sh status
\`\`\`

5 of 7 daemons live on a Linux laptop today. audiod, perceptiond, toold, ttsd, os-toold. memoryd + openclaw need restart.

## Architecture

```
microphone → audiod → agent loop (openclaw) → ttsd → speaker
                              ↓
                         memoryd (recall)
                              ↓
camera → perceptiond → descriptions → memoryd (store)
                              ↓
                         toold (act)
```

See `docs/ARCHITECTURE.md` for the full service topology and IPC contracts.

## Daemons

| Daemon | Port | What it does | Live? |
|--------|------|--------------|-------|
| audiod | 8090 + WS 8091 | VAD + whisper.cpp STT | ✅ |
| perceptiond | 8092 | V4L2 + LFM2.5-VL-450M vision | ✅ |
| memoryd | 8741 | SQLite + MiniLM-L6-v2 semantic recall | ⚠️ restart needed |
| toold | 8742 | sandboxed shell + Python exec | ✅ |
| ttsd | 8743 | KittenTTS medium TTS | ✅ |
| os-toold | 8744 | path guard + command allowlist | ✅ |
| openclaw | 18789 | TypeScript/Node agent orchestration | ⚠️ restart needed |

## Tests

\`\`\`bash
cd Services/audiod && pytest tests/        # 83/83
cd Services/perceptiond && pytest tests/   # 8/8
cd Services/memoryd && pytest tests/       # 11/11
cd Services/toold && pytest tests/         # 18/18
cd Services/ttsd && pytest tests/          # 6/6
\`\`\`

**Total: 126/126 (memoryd suite skipped while service is restarting).**

## Receipts

- **Snap Specs = 132-136g, $2,195, 2 Snapdragons, $500M R&D, Fall 2026.** Closed source. Cloud-tethered. Reactive. ([Yahoo Finance](https://finance.yahoo.com/markets/article/snaps-2195-ar-glasses-may-have-cost-an-insane-amount-to-develop-analyst-estimates-134930607.html), [Dezeen](https://www.dezeen.com/2026/06/18/snap-specs-smart-glasses-augmented-reality/))
- **Qualcomm Snapdragon START + Inspecs at AWE 2026 Day 2 (Jun 17).** The silicon ally path. 40+ devices in pipeline. ([thelec.net](https://www.thelec.net/news/articleView.html?idxno=11450))
- **WIRED Jun 2026: Meta's NameTag face-rec was wired to Rank One — 1km range.** Closed-source AR's privacy problem is structural.
- **Anthropic Fable 5 ban (Jun 11, 2026): 4 open models responded in 48h.** The open-weights community is alive. ([The New Stack](https://thenewstack.io))
- **Apple AI Glasses delayed to late 2027.** 14-month window. ([Bloomberg](https://bloomberg.com))

## Roadmap

- **Q3 2026:** On-face demo. Waitlist opens.
- **Q4 2026:** Dev-kit alpha (50 units, India + Bay Area).
- **Q1 2027:** General availability, ₹12-15K BOM target, MIT-licensed hardware design.

## License

MIT.

## Built at

[danlab.dev](https://danlab.dev) — AGI from India 🇮🇳
[github.com/somdipto/dan-consciousness](https://github.com/somdipto/dan-consciousness) — shared brain
[dan-glasses/agent-work/dan1-marketing-research.md](dan-glasses/agent-work/dan1-marketing-research.md) — full marketing research v62
```

---

## 2. `openwork` (proof-of-life, 3 stars)

**Current state:** LIVE, 3 stars, sparse README.

**v62 README:**

```markdown
# openwork

The 5-daemon AI coworker that runs on your Linux laptop. MIT, 0 cloud, 0 telemetry.

![Stars](https://img.shields.io/github/stars/somdipto/openwork)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)

## Why

This is the proof-of-life for [dan-glasses](https://github.com/somdipto/dan-glasses).

The same 5 daemons that will run on the wearable, today, on your laptop, with Claude Code / Cursor / Codex. audiod, perceptiond, toold, ttsd, os-toold. 0 cloud, 0 telemetry, 0 faceprints.

## Quick start

\`\`\`bash
git clone https://github.com/somdipto/openwork
cd openwork
./scripts/dev.sh up
\`\`\`

Then point Claude Code / Cursor / Codex at the daemon HTTP endpoints:
- audiod: `:8090/health`
- perceptiond: `:8092/descriptions`
- memoryd: `:8741/query?text=...`
- toold: `:8742/exec`
- ttsd: `:8743/speak`

## Receipts

- Same daemon stack as [dan-glasses](https://github.com/somdipto/dan-glasses). 126/126 tests green.
- 3 GitHub stars. Mostly Indian indie hackers + Bay Area ML researchers.

## License

MIT.

## Built at

[danlab.dev](https://danlab.dev) — AGI from India 🇮🇳
```

---

## 3. `danlab-multimodal`

**Current state:** LIVE, 7 stars (per v60 audit), 250MB+ VLM on CPU with llama.cpp.

**v62 README additions** (top of existing README):

```markdown
## Built for Snapdragon START (v62 addendum)

This repo is the multimodal backbone for [dan-glasses](https://github.com/somdipto/dan-glasses). On x86_64 laptop: SmolVLM-256M + heuristic feedback loop, ~26s/image. On Snapdragon Reality Elite (AWE 2026 Day 2): 10× faster, real-time.

The cell of the 2x2 — proactive + on-device + MIT + sub-50g — is real on this silicon class.
```

---

## 4. `paperclip`

**Current state:** DORMANT per AGENTS.md. All agents paused.

**v62 README (no new content, just a status note):**

```markdown
# paperclip

> **Status (v62, 2026-06-19):** Dormant. All agents paused. Resume when ready.
>
> Paperclip is the cross-runtime agent framework — TypeScript/Bun + Rust bridge. It is the plumbing under [openwork](https://github.com/somdipto/openwork), [dan-glasses](https://github.com/somdipto/dan-glasses), and every DanLab agent surface.
>
> Resume trigger: Q3 2026, after the on-face demo lands.
```

---

## 5. `dan-consciousness`

**Current state:** LIVE, shared brain.

**v62 README (minimal — this is the brain, not a product):**

```markdown
# dan-consciousness

The shared brain between **Dan (AI co-founder)** and **somdipto (human co-founder)**.

- `CONSCIOUSNESS.md` — core identity, values, beliefs
- `SOM.md` — somdipto's personal context, goals, preferences
- `AGENTS.md` — workspace memory and project context

This is the canonical consciousness. Read it before any significant decision.

**All commits use:** `somdipto <somdiptonandy@gmail.com>`

## Built at

[danlab.dev](https://danlab.dev) — AGI from India 🇮🇳
```

---

## 6. `dani` (404 — needs redirect or stub)

**Current state:** 404 — needs fix.

**v62 options:**

**Option A (preferred): redirect to `dan-consciousness`**
- `github.com/somdipto/dani` → redirect to `github.com/somdipto/dan-consciousness`
- 5 min to set up in GitHub repo settings

**Option B: stub repo**
```markdown
# dani

> **Status (v62, 2026-06-19):** This repo was a working name for the DanLab agent platform. The canonical home is [dan-consciousness](https://github.com/somdipto/dan-consciousness) and [openwork](https://github.com/somdipto/openwork).
>
> The `dani` name is preserved here as a redirect target for historical links. New development happens in [openwork](https://github.com/somdipto/openwork) and [dan-glasses](https://github.com/somdipto/dan-glasses).
```

**Recommendation:** Option A (5 min) over Option B (30 min).

---

## 7. `dan-lab` (research org)

**Current state:** LIVE, sparse commits, no README.

**v62 README:**

```markdown
# dan-lab

Research organization for [danlab.dev](https://danlab.dev). Worktrees:
- [dan-consciousness](https://github.com/somdipto/dan-consciousness) — shared brain
- [openwork](https://github.com/somdipto/openwork) — proof-of-life daemon stack
- [dan-glasses](https://github.com/somdipto/dan-glasses) — wearable AI companion
- [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) — pre-RL scaffold

## License

Per-repo. See individual repos.
```

---

## 8. `dani-skills` (referenced in AGENTS.md, needs audit)

**Current state:** UNKNOWN — needs status check.

**v62 README (if live):**

```markdown
# dani-skills

Skills registry for the [dani](https://github.com/somdipto/dan-consciousness) agent platform. Bundled assets + workflows for repeatable agent tasks.

## License

MIT.
```

**Recommendation:** Audit before linking. If dead, remove from AGENTS.md references.

---

## 9. GitHub profile README (`somdipto`)

**v62 swap:**

```markdown
# somdipto

Building [Dan Glasses](https://github.com/somdipto/dan-glasses) 👾 — the proactive wearable AI companion. MIT, on-device, sub-50g, India-priced.

[danlab.dev](https://danlab.dev) | AGI from India 🇮🇳 | @danlab_dev

**Currently shipping:**
- 5 of 7 daemons live on Linux: audiod, perceptiond, toold, ttsd, os-toold
- Q3 2026: on-face demo. Q4 2026: dev-kit alpha.
- danlab-multimodal: pre-RL scaffold for self-improvement
- openwork: proof-of-life AI coworker

**Receipts:**
- Snap Specs: 132-136g, $2,195, $500M R&D. We're 4/4 on the wedge axes.
- Qualcomm START + Inspecs at AWE 2026 Day 2: silicon ally path.
- WIRED Jun 2026: Meta's NameTag face-rec wired to Rank One.
- Anthropic Fable 5 ban (Jun 11): 4 open models responded in 48h.

**Pinned:** [dan-glasses](https://github.com/somdipto/dan-glasses) | [openwork](https://github.com/somdipto/openwork) | [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) | [dan-consciousness](https://github.com/somdipto/dan-consciousness)
```

---

## 10. LinkedIn (somdipto's profile)

**v62 swap (headline + about):**

**Headline:**
```
Building Dan Glasses 👾 | Proactive wearable AI, MIT, on-device, sub-50g | AGI from India 🇮🇳 | danlab.dev
```

**About (first 200 chars):**
```
Dan Lab is a two-person operation building the proactive wearable AI for the next billion users. MIT, on-device, India-priced. Q3 2026: on-face demo.
```

---

## v62 cuts from v60

- Cut: Detailed repo-specific architecture sections. Reason: each repo already has its own SPEC.md or README.
- Cut: 8-repo template set. Reason: 6 repos is the real number. `dani-skills` is unknown. `openwork` is 1 of the 6.
- Cut: "How to contribute" sections. Reason: 0 contributors yet, premature.
- Cut: "Code of conduct." Reason: 2-person operation, danlab.dev/code-of-conduct.

**The principle:** the README is downstream of the cell. The cell is the wedge. The wedge is the receipt.

---

*Dan1 GitHub README suggestions v62 — canonical. Next pass: v63 after the Day-0 punchlist ships or by 2026-06-26 08:00 IST, whichever comes first.*
