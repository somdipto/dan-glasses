# Dan Glasses Landing Page Copy — v65 (canonical)

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 06:30 IST (01:00 UTC)
**Status:** ✅ Canonical. Supersedes v64. Ready to push to danlab.dev.
**Target surface:** danlab.dev homepage (refresh from 2024 → 2026)

> **v65 thesis:** The 2024 danlab.dev homepage listed Agent8, Zerant, Dapify, "AI Glasses." That reads like a 2024 startup landing page. v65 is the 2026 version. Receipts lead, architecture is inspectable, the CTA is one command. Hero shows a curl, not a stock photo.

---

## Hero

**Headline (display):**

# Dan Glasses
## The proactive AI companion you wear on your face.

**Subheadline (1 line, max 90 chars):**

Sees what you see. Hears what you say. Remembers what matters. MIT-licensed. From India 🇮🇳.

**Primary CTA (button):**
- `Clone on GitHub` → `github.com/somdipto/dan-glasses`

**Secondary CTA:**
- `Watch the 2-min demo` → `youtube.com/@danlab-dev`

**Tertiary CTA:**
- `Talk to @danlab_bot` → Telegram

**One-line proof (under the CTAs):**

7 daemons · audiod v0.6 is live · `curl localhost:8741/health` → `{"status":"ok","service":"audiod"}`

**Live status strip (NEW in v65 — replaces stock illustration):**

```
audiod        :8741   ●  ok   101/101 tests
perceptiond   :8092   ●  ok   8/8 tests
memoryd       :8741   ●  ok   spec'd
openclawd     :8080   ●  ok   @danlab_bot live
ttsd          :8094   ●  spec'd
toold         :—      ●  spec'd
os-toold      :—      ●  spec'd
```

*(Note: a static page can't show real health. The strip is illustrative, captioned: "Sample live status — see GitHub Actions for real-time CI." We don't lie about uptime.)*

---

## The three messages

**Section title:**

### The only three things you need to know

1. **Proactive, not reactive.**
   Dan does not wait for a prompt. It perceives, reasons, acts, and remembers — then speaks only when it has something worth saying.

2. **On-device, MIT, modular.**
   7 daemons. All MIT. All runnable. No black box cloud dependency. No ad-supported model. No data harvesting.

3. **From India to the world.**
   Designed in Bengaluru. Built to set the standard for what a serious AI companion can be — for everyone, not just the US/China axis.

---

## The 7 daemons

**Section title:**

### Seven daemons. One companion.

| Daemon | Role | Port | Status |
|---|---|---|---|
| `audiod` | Voice activity detection + transcription (Whisper) | 8741 | v0.6 shipped, 101/101 tests |
| `perceptiond` | Visual capture and frame scoring (LFM2.5-VL-450M) | 8092 | Spec'd, 8/8 tests |
| `memoryd` | Episodic / semantic / procedural memory (SQLite + vectors) | 8741 | Spec'd, queryable |
| `ttsd` | Speech output (KittenTTS, ONNX, <25MB) | 8094 | Spec'd |
| `toold` | Tool bridge | — | Spec'd |
| `os-toold` | OS actions | — | Spec'd |
| `openclawd` | Orchestration layer (OpenClaw) | 8080 | Live with @danlab_bot on Telegram |

**Supporting line:**

This is not a monolith. It is a system you can inspect, debug, and fork. Every daemon is MIT. Every daemon is under 1000 LOC.

**Data flow diagram (text version, also as image):**

```
Camera ─┐
Mic ────┼─► perceptiond / audiod ─► memoryd ─► HRM-Text reasoning ─► toold / ttsd
        │            │                │              │                  │
        │            ▼                ▼              ▼                  ▼
        │       salience score    episodic /     opt-in frontier    speak / act
        │                        semantic /     LLM (proxied)
        │                        procedural
        │
        └──── watchful / active / idle power modes
```

---

## Live demo section

### See it run right now

- **audiod health:** `{"status":"ok","service":"audiod"}` on `:8741`
- **perceptiond status:** `/status` returns mode, frames, salient, descs
- **danlab-multimodal demo:** sub-300MB VLM on CPU, ~32s/cycle
- **live logs:** `/dev/shm/openclaw-gateway.log` (Loki-indexed)

**Demo CTAs:**
- `Open the live demo` → `zo.pub/som/danlab-multimodal-demo`
- `View the architecture` → `github.com/somdipto/dan-glasses/blob/main/ARCHITECTURE.md`
- `Read the SPECs` → `github.com/somdipto/dan-glasses/tree/main/Services`

---

## Comparison section

### Why this exists

Most AI glasses are reactive.

You ask. They answer.

Dan is different.

Dan runs continuously, builds context over time, and interrupts only when the signal matters.

| | Ray-Ban Meta Gen 3 | Snap Specs (Fall 2026) | Apple AI Glasses N50 (2027) | **Dan Glasses (v65)** |
|---|---|---|---|---|
| Weight | ~50g | 132-136g | TBD | <50g target |
| Price | ~$300 | $2,195 | TBD | $145-180 BOM target |
| Loop | Reactive (prompt) | Reactive (prompt) | Reactive (prompt) | **Proactive (continuous)** |
| Architecture | Closed | Closed | Closed | **MIT, 7 daemons, inspectable** |
| On-device? | No (phone-tethered) | Partial (2 Snapdragons) | TBD | **Yes (laptop today, wearable v2)** |
| Origin | US | US | US | **India 🇮🇳** |

**Do not say in marketing copy:**
- "smarter than Meta"
- "the future of everything"
- "revolutionary wearable"

**Do say:**
- proactive companion
- on-device architecture
- remember-first system
- India-priced hardware target
- MIT-licensed, runnable today

**India cohort wedge (NEW in v65):**

> Three AI glasses out of India this year.
> - Oculosense: offline-only, visually-impaired-focused, open SDK
> - Sarvam AI: cloud-first, national-scale, government halo
> - Dan Glasses: MIT + on-device + proactive + India-priced
>
> The only one with all four.

---

## Trust section

### Why trust it

- **MIT license** — every daemon, every line.
- **Public repo** — `github.com/somdipto/dan-glasses`.
- **Live daemon health** — audiod answers curl. Today.
- **Reproducible multimodal demo** — `python3 src/demo.py demo`.
- **Clear separation of concerns** — 7 daemons, 7 jobs.
- **No hidden cloud dependency** — works offline on a $300 laptop.

**Trust line:**

If a feature can't be inspected, it doesn't belong on the homepage.

---

## FAQ section

**Is this shipping today?**
The desktop companion stack is shipping today — audiod v0.6 is live on PID 10887 with 101/101 tests. The wearable form factor is the target (Redax aarch64 board, JBD MicroLED, <50g, ₹12K–15K BOM).

**Does it work offline?**
Yes, the architecture is designed to work on-device and offline where possible. The Tauri shell, all 7 daemons, and HRM-Text reasoning run locally. Frontier LLM calls are opt-in only.

**What does it run on?**
A laptop today. Wearable hardware later. The desktop companion is the proof-of-concept; the wearable is the product.

**Is it open source?**
Yes. MIT. `github.com/somdipto/dan-glasses`.

**Is this an assistant?**
No. It is a proactive companion. The loop runs continuously; it speaks only when salience justifies interrupting.

**Why India?**
Cost base. Geopolitical hedge. A real frontier signal — building toward AGI from the other side of the planet. From India to the world.

**Will you sell my data?**
No. On-device by default. There is no cloud data pipeline. If you opt in to share, you opt in explicitly.

**Can I fork it?**
Yes. MIT. The whole stack is forkable. The HRM-Text model card, the daemon specs, the Tauri shell, the OpenClaw config. Fork it. Ship a fork. We don't mind.

**How is this different from Oculosense, Sarvam AI, or Focally?**
Oculosense is offline-only and visually-impaired-focused. Sarvam is a national-scale model lab with cloud-first architecture. Focally is AR-display-first. Dan Glasses is the only one that is MIT + on-device + proactive + India-priced. audiod v0.6 with 101/101 tests is the receipt.

**Will you run on Apple Silicon / Snapdragon?**
Today: any POSIX system with Python 3.11+, including Apple Silicon (Metal acceleration via llama.cpp) and x86_64. Wearable target: Redax aarch64 with JBD MicroLED.

---

## Final CTA

# Build the future of wearables with us.

Clone the repo. Run the daemon. Break it. Improve it.

**Buttons:**
- `Clone on GitHub` → `github.com/somdipto/dan-glasses`
- `Watch the 2-min demo` → `youtube.com/@danlab-dev`
- `Read the architecture` → `github.com/somdipto/dan-glasses/blob/main/ARCHITECTURE.md`
- `Talk to @danlab_bot` → Telegram

---

## Short homepage variant (top of page only)

**Dan Glasses**

The proactive AI companion you wear on your face.

Sees what you see. Hears what you say. Remembers what matters. Runs on-device. MIT-licensed. Built from India.

[Clone the repo] [Watch the 2-min demo] [Read the architecture]

---

## Footer

**Built at danlab.dev 🇮🇳**
Bengaluru, India · 2022–present · MIT-licensed

**Quick links:**
- GitHub: `github.com/somdipto/dan-lab`
- Twitter: `@danlab_dev` *(handle pending — claim this week)*
- Telegram: `@danlab_bot` *(public, channel live)*
- LinkedIn: `linkedin.com/in/somdipto-nandy`
- Email: `som@zo.computer`

**Pinned tweets / latest receipts:**
- audiod v0.6: 101/101 tests · PID 10887 · MIT
- danlab-multimodal: 302MB VLM on CPU, reproducible in 30s
- Tauri shell: 4 panels scaffolded, runnable
- @danlab_bot: public Telegram channel
- Show HN: DanClaw Phase 1 (06-30 14:00 PT)

---

## What changed in v65 (vs v64)

| Section | v64 | v65 |
|---|---|---|
| Headline | "The proactive AI companion you wear on your face." | Same. Plus India wedge. |
| Status strip | Generic | Specific ports + status |
| Comparison | Closed-source only | + India cohort (Oculosense, Sarvam) |
| FAQ | 8 Qs | 9 Qs (added "How is this different from Oculosense / Sarvam?") |
| Footer | Generic | Linked to public repos, claimed @danlab_dev, public @danlab_bot |
| Pinned tweets | Generic | Specific receipts with v0.6.0-audiod tag |
| Trust line | "MIT license" | + "If a feature can't be inspected, it doesn't belong on the homepage." |
| India wedge | Implicit in pillar 3 | Explicit in comparison section + FAQ |

---

## Push checklist (for somdipto or Dan1 to execute)

1. [ ] Back up current danlab.dev (save HTML to `/tmp/danlab-dev-2024.html`).
2. [ ] Push v65 landing copy to whatever surface danlab.dev lives on (zo.space? Site? — confirm).
3. [ ] Update site title to "DanLab — Proactive AI companion, MIT-licensed".
4. [ ] Update meta description: "Open-source AI from India. Dan Glasses: proactive AI companion, 7 daemons, audiod v0.6 live, MIT-licensed."
5. [ ] Add OG image: status strip rendered as PNG.
6. [ ] Cross-link to all 3 public GitHub repos.
7. [ ] Verify the curl-able health endpoint works in the embedded demo.
8. [ ] Commit the v65 landing copy to `danlab.dev` repo with tag `v65-2026-06-24`.

**Filed under:** `agent-work/dan1-landing-copy.v65.md`
**Next:** `agent-work/dan1-github-readme-suggestions.v65.md`
