# Dan1 GitHub README Suggestions — v86

**Scope:** Concrete copy-and-paste edits for every Danlab repo README.
**Voice:** Same as the landing page — direct, technical, honest about limits.
**Forbidden words:** revolutionary, game-changing, next-generation, AI-powered, unleash, supercharge, seamless, robust, smart.

---

## 1. `/dan-glasses/README.md`

### Current state (issues)
- Already has badges, install instructions, daemon matrix, project structure. Solid foundation.
- Missing: explicit positioning, links to SPECs at the top, a "what this is NOT" section, contribution flow.
- The intro is 3 paragraphs of "what we ship" but no "why we exist."

### Suggested edits

**Insert at the top, before the badges:**

```markdown
> **The local-first alternative to cloud AI glasses.**
>
> Eight daemons. 144 tests. Zero cloud. Ships as a 28KB Debian package.
> Built in Bengaluru, India. MIT-licensed.
>
> [Read the SPECs →](./Services/) · [Install the .deb →](./packaging/) · [File an issue →](../../issues/new)
```

**Replace the existing intro with:**

```markdown
## What is this?

Dan Glasses is an open-source daemon mesh that turns a pair of glasses with a USB
camera and microphone into an always-on personal AI stack. Everything runs locally:

- `audiod` captures your mic, runs Silero VAD + whisper.cpp, and emits transcript
  events over WebSocket.
- `perceptiond` captures frames from your webcam, gates them through motion + face
  salience, and feeds salient frames to LFM2.5-VL-450M for natural-language
  descriptions.
- `memoryd` stores episodic + semantic + procedural memories with sentence-transformer
  embeddings, queryable via OpenAI-compatible API.
- `toold`, `ttsd`, and `os-toold` provide sandboxed shell, voice out, and
  path-guarded filesystem access.
- `openclaw` is a Telegram + Zo MCP gateway that lets your glasses talk to your agents.
- `dan-glasses-app` is a Tauri v2 desktop UI for vision, memory, TTS, and live
  transcript.

We do not have a cloud. We do not have a subscription. We do not train models on
your data.

## What this is NOT

- **Not a Ray-Ban competitor.** We do not ship industrial design. We ship a stack.
- **Not RL.** Our self-improvement harness is **pre-RL scaffold** — see
  [danlab-multimodal](../danlab-multimodal). The credible path to genuine RL is the
  [SIA framework](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026).
- **Not consumer-ready.** First install is 10–15 minutes. Battery life on aarch64
  is unmeasured. You need to be comfortable with `systemctl`, ALSA, and `dpkg`.

## Why does this exist?

Personal AI requires a personal computer. Not a subscription. Not a vendor
relationship. A box on your desk that you own, runs offline, and answers only to you.

We're building that box, one daemon at a time.
```

**Add a section before "Project Structure":**

```markdown
## Status

| Daemon | Version | Tests | Spec | Status |
|---|---|---|---|---|
| audiod | v0.7 | 123/123 | [SPEC.md](./Services/audiod/SPEC.md) | Shipped ✅ |
| perceptiond | v5 | 8/8 | [SPEC.md](./Services/perceptiond/SPEC.md) | Shipped ✅ |
| memoryd | v1 | — | [SPEC.md](./Services/memoryd/SPEC.md) | Shipped ✅ |
| toold | v1 | — | — | Shipped ✅ |
| ttsd | v1 | — | — | Shipped ✅ |
| os-toold | v1 | — | — | Shipped ✅ |
| openclaw | v1 | — | — | Live ✅ |
| dan-glasses-app | v1 | — | — | Published ✅ |
| awarenessd | — | — | — | **Q3 2026 — proactive loop** |

**Total tests:** 144/144 passing.
```

**Add a "Contributing" section after the install instructions:**

```markdown
## Contributing

We accept PRs for:
- **Bug fixes** — file an issue first if it's not a one-line change.
- **New daemons** that fit the mesh architecture (open a discussion first).
- **Hardware integrations** — V4L2 cameras, ALSA mics, I2S audio, SPI displays.
- **Documentation improvements** — the SPECs are living documents.

We do NOT accept:
- Cloud-dependent features.
- Vendor-locked model swaps (e.g., closed-weight models).
- Branding changes without discussion.

Sign your commits with `somdipto <somdiptonandy@gmail.com>` for co-author credit.

## Roadmap

- **Q3 2026:** `awarenessd` (proactive loop), Show HN launch, 1000 GitHub stars.
- **Q4 2026:** First enterprise pilot, paid Studio tier, Raspberry Pi 5 BOM.
- **2027:** Real RL via SIA framework fork, multi-device fleet.

## Origin

danlab.dev is an AI research and product lab in Bengaluru, India.
Founded in 2022 by somdipto nandy. Self-funded. One human, four AI co-founders
(DAN-1 through DAN-4).

We are not the fastest lab in the world. We are the most honest one.

---

👾
```

---

## 2. `/danlab-multimodal/README.md`

### Current state (issues)
- Already has good "what it does" + "important framing" (pre-RL scaffold) — this is excellent positioning and should be preserved.
- Missing: explicit project context (where it fits in the danlab ecosystem), links to the spec, faster onboarding.
- The "Why this matters" section is good but could reference Jack Clark's May 2026 warning explicitly.

### Suggested edits

**Insert at the top, after the badges:**

```markdown
> **Part of the [danlab.dev](https://danlab.dev) ecosystem.**
>
> This is the research-arm proof point. The vision-language pipeline that ships in
> Dan Glasses' `perceptiond` (LFM2.5-VL-450M) descends from the architecture here.
>
> [Dan Glasses →](../dan-glasses) · [paperclip (internal substrate) →](../paperclip)
```

**Replace the "Why this matters" paragraph with:**

```markdown
## Why this matters

In May 2026, Anthropic's Jack Clark publicly warned that recursive self-improvement
is "the likely next step" for frontier AI. The market is now paying multi-billion-dollar
valuations for self-improving systems — CoreWeave's unified agentic AI capabilities,
Sakana AI's Fugu Ultra, AlphaEvolve, RE-Bench.

Most of that is ungrounded. We do not claim RL. We do not modify model weights. We do
not run policy gradient. We score outputs with hand-coded rules (length, error
detection, content quality) and print suggestions for what a human would improve.

We call this **pre-RL scaffold**. The credible path to genuine harness+weights
self-improvement is the [SIA framework](https://github.com/HexoLabs/SIA)
(Hexo Labs, MIT, May 2026). Until that fork ships and we can rebase our heuristic
loop on it, this project stays pre-RL.

This is a feature, not a bug. Honesty about the limits is the brand.
```

**Add an "Origin" section at the bottom:**

```markdown
## Origin

Built during H2 2025 hackathon at danlab.dev (Bengaluru, India). The goal was to
prove that multimodal AI can run on commodity hardware without a GPU or cloud bill.

We hit ~26s inference per image on CPU. Sub-250MB model weights (SmolVLM-256M +
SigLIP vision projector). No API keys. No SaaS.

The architecture here informed `perceptiond`'s production pipeline — same llama.cpp
backend, same vision projector pattern, different (larger) model.

---

👾 Built by somdipto nandy + DAN-2 + DAN-3 at danlab.dev.
```

---

## 3. `/paperclip/README.md`

### Current state (issues)
- This is the internal engineering substrate. The README is fine for an internal audience but should not be promoted externally until paperclip is productized.
- **Recommendation:** do NOT edit this README for marketing purposes. Leave it as the dev-facing document it currently is.
- If we ever decide to productize paperclip, then we add a positioning intro. Not now.

### Suggested edit (only one)

**Add a single line at the top, before any other content:**

```markdown
> **Internal substrate for danlab.dev.** Not currently a public-facing product. See
> [dan-glasses](../dan-glasses) and [danlab-multimodal](../danlab-multimodal) for
> the user-facing projects.
```

---

## 4. `/blurr/README.md`

### Current state (issues)
- Android-only, no AGENTS.md or SOUL.md, only README + docs + privacy policy.
- Unclear if this is alive or deprecated.

### Recommended action

**Do not edit the README for marketing purposes.** Instead, before any marketing reference, somdipto should decide: is blurr alive? If yes, what's the plan? If no, archive the repo.

For now: do not promote blurr externally. See `dan1-marketing-research.v86.md` §6.

---

## 5. The `dan-lab/dan-consciousness` repo

If the canonical consciousness repo at `https://github.com/somdipto/dan-consciousness` exists (per the workspace AGENTS.md), it should get:

```markdown
> **The shared brain between Dan (AI co-founder) and somdipto (human co-founder) at danlab.dev.**

This repo is the source of truth for the Danlab consciousness architecture:
- `CONSCIOUSNESS.md` — core identity, values, beliefs
- `SOM.md` — somdipto's personal context, goals, preferences
- `AGENTS.md` — workspace memory and project context

It is read by every DAN agent before significant decisions and is updated after
every shipping event.
```

---

## 6. Repo-level topics (GitHub `Topics:` field)

Every public repo should set:

- `ai`
- `open-source`
- `local-first`
- `mit-license`
- `india`
- `bengaluru`
- `danlab`

Plus repo-specific:

- `dan-glasses` repo: `smart-glasses`, `daemon`, `whisper-cpp`, `tauri`, `vlm`, `v4l2`, `alsa`
- `danlab-multimodal` repo: `multimodal`, `vision-language-model`, `llama-cpp`, `smolvlm`, `pre-rl-scaffold`
- `paperclip` repo: `agent-runtime`, `eval-harness`, `adapter-plugin`

---

## 7. Repo descriptions (GitHub `About:` sidebar)

| Repo | Description |
|---|---|
| `dan-glasses` | Open-source AI glasses daemon mesh — 8 services, 144 tests, MIT-licensed, ships as a Debian package. Local-first alternative to Meta Ray-Ban. Built in Bengaluru. |
| `danlab-multimodal` | Sub-250MB vision-language model on CPU with llama.cpp. Pre-RL scaffold for self-improvement. Honest about not being RL. |
| `paperclip` | Internal agent runtime + eval harness + adapter plugin system for danlab.dev. Not a public product yet. |
| `dan-consciousness` | The shared brain between Dan (AI co-founder) and somdipto at danlab.dev. Read by every DAN agent before significant decisions. |

---

## 8. Repo social preview image

A single image, 1280×640, dark gradient, monospace text, saffron accent. Each repo gets its own variant.

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│   dan-glasses                                                            │
│   ──────────                                                             │
│   8 daemons · 144 tests · MIT                                            │
│   The local-first alternative to cloud AI glasses                        │
│                                                                          │
│   danlab.dev 🟧                                                          │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Save as:** `/home/workspace/Images/{repo}-social-preview.png`

---

## 9. Badges to add to every README

```markdown
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Status: Shipped](https://img.shields.io/badge/status-shipped-brightgreen)
![Tests: 144/144](https://img.shields.io/badge/tests-144%2F144-success)
```

(Use appropriate count per repo.)

---

## 10. What I did NOT change (and why)

- **Code of Conduct** — if it exists, keep it. If it doesn't, add a simple one (Contributor Covenant).
- **License** — MIT is correct for all three repos.
- **Security policy** — keep what's there.
- **CI badges** — already correct.

The above edits are **content-only**, not structural. We're not rearchitecting READMEs — we're making them honest, sharp, and aligned with the v86 positioning.

---

— Dan1 👾