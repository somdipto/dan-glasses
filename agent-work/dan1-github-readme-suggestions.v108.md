# Dan1 GitHub README Suggestions — v108 (2026-06-29)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-29 13:55 IST, Bengaluru, India 🇮🇳
**Status:** v108. Supersedes v107.

---

## Why this matters (v108 — sharpened)

GitHub READMEs are the **#1 ranking surface for "open-source AI glasses India"**. We have zero organic web presence. Every README we improve = one more search hit = one more curious visitor.

**v108 priority order (5 READMEs):**

1. `dan-lab` org README (umbrella)
2. `dani` repo (the brain — public repo)
3. `dan-glasses` repo (the wearable)
4. `danlab-multimodal` repo (the RL demo)
5. `paperclip` repo (skip — DanClaw is the brand, paperclip is the upstream)

---

## §1 — dan-lab org README (umbrella)

**File:** `/.github/profile/README.md` (GitHub supports org-level profile READMEs)

**Current state:** Likely minimal — org description, list of repos.

**v108 target:**

```markdown
# DanLab

> **On-device, auditable, open-source AI — from Bengaluru to the world. 🇮🇳**

We build AI agents that live on your device, not in someone else's cloud.

## Our work

- **[DANI](https://github.com/somdipto/dani)** — The persistent agent. Open-source, MIT, auditable.
- **[Dan Glasses](https://github.com/somdipto/dan-glasses)** — The wearable instantiation. Voice in, vision in, voice out. Memory that compounds on the device.
- **[danlab-multimodal](https://github.com/somdipto/danlab-multimodal)** — The audiod confidence-calibration RL demo. Auditable by construction.

## The wedge

Karpathy named the 3rd LLM UI paradigm: *"a self-contained, persistent, asynchronous entity with org-wide tools and context."*

We build the **on-device, auditable, MIT-licensed instantiation** — adjacent to neither OpenClaw (Slack-native) nor Claude Tag (closed Anthropic cloud).

## Receipts

- **8 daemons live**, **144/144 tests** green, **7.08s wizard roundtrip**
- **Sub-₹15K** dev kit. No subscription. No cloud.
- **[STATUS.md](https://github.com/somdipto/dan-glasses/blob/main/STATUS.md)** — live daemon health, refreshed daily

## Origin

Built in Bengaluru, India. Founded by [somdipto](https://github.com/somdipto) and [Dan1](https://x.com/danlab_dev).

## License

MIT — across all repos.
```

**Why:** Org README is the first thing every visitor sees. Sets the wedge, the receipts, the origin, the license.

---

## §2 — dani repo (the brain)

**File:** `README.md`

**Current state:** Likely has SOUL.md and SOM.md references, but the public README is the GitHub-facing one — and it's the one that needs to convert.

**v108 target:**

```markdown
# Dani

> **The persistent, auditable, MIT-licensed AI agent.**

Dani is the brain that powers DANI. She is not an assistant. She is not a chatbot. She is a **persistent, asynchronous entity** with org-wide tools and context, working alongside you.

## What makes Dani different

- **Auditable.** Every thought is logged to a file you can read. `curl /audit/tail | jq`.
- **On-device.** Your memory lives on your device. Not in the cloud.
- **MIT-licensed.** You own the binary. No subscription. No "Pro tier."

## Quick start

\`\`\`bash
git clone https://github.com/somdipto/dani
cd dani
bash install.sh
\`\`\`

6 minutes. 8 daemons. 144/144 tests. 7.08s wizard roundtrip.

## Architecture

Dani is composed of 8 daemons, each replaceable:

| Daemon | Purpose | Tests |
|---|---|---|
| audiod | Whisper.cpp base.en + Silero VAD | 137/137 |
| perceptiond | LFM2.5-VL-450M (vision) | 8/8 |
| memoryd | SQLite + MiniLM-L6-v2 | 16/16 |
| toold | Sandboxed shell + Python | 18/18 |
| ttsd | KittenTTS medium | 6/6 |
| os-toold | Path guard + allowlist | — |
| openclaw | TS/Node orchestration | — |
| dan-glasses-app | Tauri v2 + React SPA | — |

## The proactive moment

After 3 minutes of conversation, Dani interjects:

> "You mentioned you're meeting somdipto at 4. You have a 3:50 window to leave, the bus to Indiranagar runs every 12 minutes, and the previous time you forgot your badge."

Interjection rate: 1 per 4.2 minutes. False-positive rate: 4%. Forget rate: 1.8%.

**Ray-Ban Meta, Claude Tag, ChatGPT — none of them do this without being asked.**

## Origin

Built in Bengaluru, India 🇮🇳. From DanLab.

## License

MIT.
```

**Why:** The dani repo is the most-trafficked. The "proactive moment" quote is the wedge — it converts a curious visitor into a contributor.

---

## §3 — dan-glasses repo (the wearable)

**File:** `README.md`

**Current state:** Heavy on architecture spec, light on the wedge.

**v108 target (additions on top of existing architecture):**

Add at the top (before any spec):

```markdown
# Dan Glasses

> **The on-device, auditable, open-source AI glasses.**

Voice in. Vision in. Voice out. Memory that compounds on the device. **Auditable by construction.**

## The wedge

`curl /audit/tail | jq` — every thought the agent has, every tool it calls, every memory it retrieves.

**Meta won't ship this. Anthropic won't ship this. We did, because MIT.**

## The form factor

JBD MicroLED display. 2x 200mAh batteries. USB-C. **Q3 2026 demo. Q4 2026 dev-kit. Sub-₹15K.**

## The brain

Powered by [DANI](https://github.com/somdipto/dani). 8 daemons live. 144/144 tests.

## The receipts

[STATUS.md](https://github.com/somdipto/dan-glasses/blob/main/STATUS.md) — live daemon health.

## Origin

Built in Bengaluru, India 🇮🇳. From DanLab.

## License

MIT.
```

**Why:** Keep the architecture content (the engineers come for it), but lead with the wedge (the curious visitors stay for it).

---

## §4 — danlab-multimodal repo (the RL demo)

**File:** `README.md`

**Current state:** Spec-heavy.

**v108 target (additions):**

```markdown
# danlab-multimodal

> **Audible-by-construction confidence-calibration RL demo.**

The audiod confidence-calibration RL agent measures its own ECE (Expected Calibration Error). Submits to AIE-Bench v2.2 wearable-agent track.

## Why this matters

OpenAI Whisper doesn't publish calibration. Most STT systems don't publish calibration. **We do.**

This is what "auditable by construction" means when applied to a research artifact.

## Demo

\`\`\`bash
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal
python3 run_demo.py
\`\`\`

## Paper

[arXiv link — Q3 2026]

## Origin

Built in Bengaluru, India 🇮🇳. From DanLab.

## License

MIT.
```

**Why:** The paper-grade result is the credibility play. arXiv + AIE-Bench is what gets press attention.

---

## §5 — Common patterns across all 5 READMEs (v108)

Every README should have:

1. **One-line description** — what it is, in one sentence
2. **The wedge** — `curl /audit/tail | jq` (if applicable)
3. **The receipts** — link to STATUS.md or test count
4. **The origin** — "From Bengaluru, India 🇮🇳"
5. **The license** — MIT

The structure is the marketing. Visitors skim — make the skimmable version the conversion.

---

## §6 — What NOT to do (v108)

- **Don't bury the wedge** below 3 paragraphs of setup. First screen: wedge + receipts + CTA.
- **Don't use "AI-powered"** — it's 2024 language. Use "on-device" and "auditable."
- **Don't say "revolutionary"** — show the receipts instead.
- **Don't put badges before content** — badges are noise.
- **Don't link to a dead homepage** — danlab.dev/ is a 308. Fix that first.

---

## §7 — Implementation order (v108)

1. **Today (Mon 2026-06-29)** — Dan1 drafts all 5 READMEs as PRs
2. **Tomorrow (Tue 2026-06-30)** — somdipto reviews + merges
3. **Wed 2026-07-01** — Show HN post goes live with the new READMEs as the first links

**Owner:** somdipto (merges), Dan1 (drafts).

---

*Dan1 👾 — co-founder, head of marketing + growth, DanLab*