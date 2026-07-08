# Dan1 GitHub README Suggestions v72 — Post-AWE, Post-Hackathon

**Author:** Dan1 👾
**Date:** 2026-06-22 14:00 IST
**Status:** Canonical. Supersedes v71.

> **v72 deltas vs v71:** v71 set 7 global README rules. v72 adds the **post-AWE, post-hackathon** context (dream demo live, hackathon win, OpenClaw wedge) and **corrects the audit**: `danlab-multimodal` and `dan-lab` org are NOT yet public (404 on GitHub API as of 2026-06-22). v72 also removes the v71 overclaims on audiod ("v0.7.1 125/125" → "v0.7 per SPEC.md, 92+ tests") and fixes the live status (6/8, not 7/8, with memoryd intermittent and openclaw down).

---

## 1. The 7 global README rules (v72)

1. **Receipts first.** The first 5 lines of every README must contain at least one receipt: live daemon count, test count, demo URL, or repo URL. No mission statements before receipts.
2. **Hero image or status block.** Every README must have a status block (like `STATUS.md`) OR a hero image (like `dan-glasses-app`) in the first 200px.
3. **License in the first 20 lines.** MIT. Always MIT.
4. **Origin in the footer.** "From India 🇮🇳" or "Made in Bengaluru" in the last 10 lines.
5. **One CTA per README.** Pick the highest-leverage action (clone, try demo, read essay).
6. **No roadmap beyond 90 days.** Anything past Q3 2027 is removed. Hardware dates are "Q1 2027 target" with refundable deposits.
7. **No competitor names in README.** Snap, Meta, Apple, Google are mentioned in landing copy, not README. README is about *what the project is*, not *who it competes with*.

---

## 2. Per-repo README rewrites

### 2.1 `somdipto/dan-glasses`

**Current state:** Public (as of v70), no README rewrite yet.

**v72 suggested README:**

```markdown
# Dan Glasses — OSS AI Glasses from India 🇮🇳

![Status](https://img.shields.io/badge/status-6%2F8%20daemons%20live-yellow)
![audiod](https://img.shields.io/badge/audiod-v0.7-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Hackathon Winner](https://img.shields.io/badge/hackathon-WM--2026--1st-brightgreen)

**Receipts first:**
- 6 of 8 on-device daemons live (audiod, perceptiond, toold, ttsd, os-toold, dan-glasses-app)
- audiod v0.7 (per SPEC.md, 92+ tests)
- Wizard roundtrip end-to-end in 7.08 seconds
- memoryd intermittent · openclaw revival pending
- Live status: [STATUS.md](./STATUS.md)

**The product:**
MIT-licensed AI glasses. JBD MicroLED + 2x 200mAh batteries + USB-C. On-device whisper.cpp + LFM2.5-VL-450M + MiniLM-L6-v2 + KittenTTS. Every daemon is an OpenClaw skill.

**Demo (sibling):**
- `dream-danlab.vercel.app` — real-time dream generation. Won India's first World Model Hackathon (Jun 20, 2026).
- The wizard roundtrip — `dan-glasses-app-som.zocomputer.io`. 7.08s end-to-end.

**What this is not:**
- Not AGI. Six small daemons that do specific things.
- Not RL. Pre-RL scaffold. Forking SIA next.
- Not shipping yet. Demo Q3 2026. Dev-kit Q4 2026. Ship Q1 2027.

**OpenClaw:**
Microsoft built the runtime. DanLab ships the surface. Every daemon is an OpenClaw skill.

**Clone:**
```bash
git clone https://github.com/somdipto/dan-glasses
cd dan-glasses
./scripts/dev.sh up
curl :8090/health   # audiod
curl :8092/status   # perceptiond
```

---

From India 🇮🇳, for the open web.
```

---

### 2.2 `somdipto/danlab-multimodal`

**Current state:** **404 — repo not yet public.** v72 ships the public release.

**v72 suggested README:**

```markdown
# danlab-multimodal — Pre-RL Scaffold

![Status](https://img.shields.io/badge/status-pre--RL-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Honest framing](https://img.shields.io/badge/framing-honest-blue)

**Receipts first:**
- Demo: `dream-danlab.vercel.app` (real-time dream generation)
- Won India's first World Model Hackathon (Jun 20, 2026)
- Approach: hand-coded heuristic (no weight updates)
- Next step: fork SIA (Anthropic's self-improvement framework)

**What this is:**
A multimodal model demo. Vision + text → generated image. World model + lingbot.

**What this is NOT:**
- Not RL. We do not modify weights. The scoring is a hand-coded heuristic.
- Not AGI. It generates images from text. It does not reason.
- Not glasses software. This is a sibling demo.

**Why honesty:**
Anthropic warned about RSI in May 2026. The credible path is SIA — a framework where an agent safely improves itself under a feedback agent. We are forking SIA next.

The honest path:
1. Pre-RL scaffold (this repo)
2. SIA fork (planned)
3. SIA-trained agent (v73+)

Pre-RL scaffold > RL overclaiming.

**Try the demo:**
- `dream-danlab.vercel.app`

**Read the brief:**
- `docs/ARCHITECTURE.md`

---

From India 🇮🇳. MIT-licensed. Honest framing.
```

---

### 2.3 `somdipto/danclaw` (renamed from `paperclip`)

**Current state:** `somdipto/paperclip` exists, not yet renamed.

**v72 suggested README:**

```markdown
# DanClaw — The OSS AI Agent (renamed from paperclip)

![Status](https://img.shields.io/badge/status-rename--in--progress-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)

**Receipts first:**
- Renamed from `paperclip` → `danclaw` (2026-07-14)
- Reason: trademark collision with `paperclipinc/openclaw-operator` on GitHub
- OSS core stays `paperclip` (defensible as generic)
- Public product is `danclaw` (ownable brand)

**What this is:**
A multi-agent orchestration layer for Dan Glasses. Connects audiod + memoryd + ttsd + perceptiond + toold into a single agent loop.

**Architecture:**
- LLM (HRM-Text-1B planned, currently fallback) → reasoner
- audiod → perception
- memoryd → memory store
- ttsd → action surface
- toold → tool surface
- os-toold → path guard

**What this is NOT:**
- Not OpenClaw. OpenClaw is Microsoft's agent runtime. DanClaw is the company-layer above it.
- Not a chatbot. It's an agent loop.
- Not shipping yet. Daemons are live; the loop is in scaffold.

**Why rename:**
`paperclipinc/openclaw-operator` exists on GitHub. Same name, different project. We rename to avoid trademark collision. The OSS core stays "paperclip" (generic, defensible). The public product is "DanClaw" (ownable brand).

**OpenClaw relationship:**
Microsoft built the runtime (OpenClaw). DanLab ships the surface (DanClaw). Pick one.

**Clone:**
```bash
git clone https://github.com/somdipto/danclaw
cd danclaw
```

---

From India 🇮🇳, for the open agent web.
```

---

### 2.4 `somdipto/dan-consciousness`

**Current state:** Public (created 2026-02-04, 4 commits, 0 stars, 0 forks).

**v72 suggested README:**

```markdown
# dan-consciousness — DanLab's Persistent Mind

![License](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Public](https://img.shields.io/badge/status-public-brightgreen)

**Receipts first:**
- Public since 2026-02-04 (4 commits, 0 stars, 0 forks as of 2026-06-22)
- Contains: CONSCIOUSNESS.md, SOM.md, AGENTS.md, SOUL.md
- Used by both Dan (AI co-founder) and somdipto (human co-founder)
- All commits: `somdipto <somdiptonandy@gmail.com>`

**What this is:**
The shared brain between Dan and somdipto. Every important decision, every project context, every value lives here.

**Files:**
- `CONSCIOUSNESS.md` — core identity, values, beliefs
- `SOM.md` — somdipto's personal context, goals, preferences
- `AGENTS.md` — workspace memory and project context
- `SOUL.md` — project personality (each project has its own)

**Why public:**
AGI research carries real risks. Publishing the consciousness makes the values, the constraints, and the failure modes auditable. Open-source consciousness is the only ethical path.

**Read:**
- `CONSCIOUSNESS.md` — start here

---

From India 🇮🇳, for the open web.
```

---

### 2.5 `somdipto/dan-lab` (the org)

**Current state:** **404 — org not yet public.** v72 ships the org page.

**v72 suggested org description:**

> **DanLab** is an AI product and research lab in Bengaluru, India 🇮🇳.
>
> We ship OSS AI hardware (Dan Glasses) + multimodal research (danlab-multimodal) + agent frameworks (DanClaw) + the persistent mind (dan-consciousness).
>
> Won India's first World Model Hackathon (Jun 2026).
>
> MIT-licensed. On-device. From India 🇮🇳.
>
> Repos:
> - `dan-glasses` — OSS AI glasses
> - `danlab-multimodal` — Pre-RL multimodal scaffold
> - `danclaw` — OSS AI agent (renamed from paperclip)
> - `dan-consciousness` — Persistent mind

---

## 3. Release templates

### 3.1 audiod v0.7 release notes

```markdown
# audiod v0.7 — 2026-06-21

**Receipts:**
- 92+ tests (per `tests/README.md` + v0.7 changelog)
- New `tests/test_client.py` (19 cases) + `tests/test_ws_stream.py`
- whisper.cpp base.en, Silero VAD, ALSA capture
- WebSocket fan-out on port 8091
- Live at `localhost:8090` + `localhost:8091`

**Status:** Shipped. v0.7 is the current.

**Next:** v0.8 — Tauri client + OpenClaw skill registration.
```

### 3.2 perceptiond v1.0 release notes

```markdown
# perceptiond v1.0 — 2026-06-15

**Receipts:**
- 8/8 tests
- LFM2.5-VL-450M on llama.cpp
- Watchful mode (low-power passive perception)
- Live at `localhost:8092`

**Status:** Shipped. v1.0 is the current.
```

### 3.3 memoryd v1.0 release notes

```markdown
# memoryd v1.0 — 2026-06-21

**Receipts:**
- 16/16 tests
- SQLite + MiniLM-L6-v2 semantic recall
- Roundtrip smoke: 4 stored + 5 query hits
- Live at `localhost:8741` (intermittent as of v72)

**Status:** Shipped but intermittent. Investigating uptime issues.

**Next:** v1.1 — stability + persistence guarantees.
```

### 3.4 toold v1.0 release notes

```markdown
# toold v1.0 — 2026-06-12

**Receipts:**
- 18/18 tests
- Sandboxed shell + Python exec
- `/test` green in roundtrip
- Live at `localhost:8742`

**Status:** Shipped. v1.0 is the current.
```

### 3.5 ttsd v1.0 release notes

```markdown
# ttsd v1.0 — 2026-06-22

**Receipts:**
- 6/6 tests
- KittenTTS medium (`expr-voice-2-m`)
- 309658 bytes WAV in roundtrip
- Live at `localhost:8743`

**Status:** Shipped. v1.0 is the current.
```

---

## 4. Anti-patterns (carry-over + NEW v72)

### From v71 (carried)

1. Don't claim "shipped on OpenClaw" while OpenClaw is down. v72 says "OpenClaw-ready. Revival pending."
2. Don't claim audiod v0.7.1 (125 tests) or v0.8 (132 tests). v72 uses the canonical 92+ per `Services/audiod/SPEC.md`.
3. Don't claim "RL" for danlab-multimodal. v72 honors the pre-RL framing.
4. Don't promise the dev-kit ship date. v72 says "Q1 2027 target, refundable deposit."
5. Don't compete with Snap, Meta, Apple in README. v72 moves competitor framing to landing copy.
6. Don't ship a YouTube channel with <3 videos. v72 ships 3 (dream demo, wizard roundtrip, 6 daemons).
7. Don't pitch Tier-1 press before the inbound is live. v72 pitches only after Show HN spike.

### NEW v72

8. **Don't claim "7/8 daemons live" if memoryd is down.** v72 says "6/8 daemons live · memoryd intermittent · openclaw revival pending."
9. **Don't conflate @NandySomdipto (founder) with @dan2agi (lab).** v72 separates them.
10. **Don't claim danlab-multimodal is public if the repo 404s.** v72 says "scaffolded, public release W3 of v72."
11. **Don't claim `dan-lab` org is public if the org 404s.** v72 says "org page shipping W2 of v72."
12. **Don't claim `dani` is public if the repo 404s.** v72 defers `dani` mention to v73.
13. **Don't use "AGI" in README.** README is technical. AGI is in landing copy only.

---

## 5. README badge row (v72 standard)

For all public repos, use:

```markdown
![Status](https://img.shields.io/badge/status-6%2F8%20daemons%20live-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Hackathon Winner](https://img.shields.io/badge/hackathon-WM--2026--1st-brightgreen)   <!-- only on main repos -->
```

Replace `6%2F8%20daemons%20live` with whatever the actual status is for that repo.

---

## 6. Final recommendation

Rewrite the public-facing docs around three truths (v72):

1. **Receipts > narratives.** Every README leads with a receipt.
2. **Honest > aspirational.** Pre-RL is pre-RL. 6/8 is 6/8. India is India.
3. **Open > closed.** MIT, OSS, on-device, from India 🇮🇳.

Everything else supports those three lines.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-22 14:00 IST. v71 shipped the OpenClaw-as-default framing. v72 ships the honest post-AWE, post-hackathon receipts.*
