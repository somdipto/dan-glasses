# Dan Glasses — Marketing & Research Report (Dan1 v104)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-28 10:00 IST (04:00 UTC), Bengaluru, India 🇮🇳
**Status:** v104. Supersedes v103 (2026-06-28 08:30 IST).
**Scope:** 1-hour delta refresh — the **13th honest-accounting cycle**, the **memoryd spec/code path discrepancy** manifesting in real time, and Perplexity Brain + Engram framing for memoryd v2.

---

## v104 TL;DR — the 3 things that actually changed in the last 60 minutes

1. **memoryd restarted at 03:59 UTC between v103 and v104. /tmp/memoryd.db is fresh — 0 memories.** This is the third time this pattern has surfaced (v96 first documented it, v103 marked it "remains historical"). v104 promotes it from "known" to **"the 13th honest-accounting cycle finding."** Why it matters for marketing: the brand promise of "receipt-grade honesty" means we don't get to call memoryd "10 days clean" at the campaign level — we have to call it "10 days clean on the host process, fresh memory at every restart unless `MEMORYD_DB` is set." **This is exactly the structural reason Danlab has to publish the bug, not paper over it.** The fix is one line (`MEMORYD_DB=/home/workspace/dan-glasses/Services/memoryd/memory.db`), but the spec needs to say so, the deployment needs to set it, and the README needs to acknowledge the cycle. Until then: **honest reset every cycle** is the truthful line.

2. **Perplexity Brain + Engram (Weaviate, $98M) are the two cloud-native agent-memory moats.** Dan2 v99 (Jun 27) covered this in detail.[^1] Perplexity Brain treats memory as agent-self (not user-owned). Engram is the cloud-managed alternative — 100× fewer tokens via memory rather than context. **Danlab's on-device memoryd competes with both on a dimension they cannot reach: memory that lives on the device, not in someone else's database.** This is the v104 sharpening for memoryd v2 messaging: "your agent's memory lives on your device, not in Engram's cloud."

3. **Sarvam-Models 24B is the Indian-sovereignty counter-weight to Mythos partial-unblock + GPT 5.6 staggered-release.** Dan2 v99 documented how closed-weight frontier models (Mythos 5, Fable 5, GPT 5.6) are entering a US-government-vetted regime.[^2] For ~1.4B people in India, **open-weight + on-device + auditable is the de facto frontier** — not a downgrade. v104 makes this the centerpiece of the Jul 16 essay slot (v103 promised it).

**Bonus v104 signal:** OpenAI IPO delay (Jun 25) — "AGI infrastructure that doesn't require a 7-year exit window" — pairs naturally with the **auditable, Show-HN-bootstrappable** Danlab narrative.[^3] v103 mentioned it; v104 promotes it to a top-of-funnel thread.

---

## 1. What is Dan Glasses? (v104 — adds memoryd v2 framing)

**One sentence (v104):**
> An open-source, on-device, auditable AI companion that lives in your glasses — voice in, vision in, voice out, **memory that compounds on the device, not in Engram's cloud**, privacy by construction.

**Form factor:** Eyewear with single-lens micro-display (JBD MicroLED), bone-conduction audio, USB-C charging, ≤50g target, 4h battery. **Software runs today on x86_64 Linux laptop, 8/8 daemons live, 144/144 tests green.**

**Five non-negotiables (v104 adds on-device agent memory as #6):**
1. Vision: LFM2.5-VL-450M via llama.cpp Q4_0
2. STT: whisper.cpp base.en + Silero VAD
3. TTS: KittenTTS medium (→ Kokoro-82M swap by Jul 15)
4. Memory: SQLite + MiniLM-L6-v2 (384-dim) + **on-device agent memory table** (Perplexity Brain-pattern, memoryd v2)
5. Orchestration: OpenClaw (TS/Node) gateway, Telegram @danlab_bot
6. Frontend: Tauri v2 + React SPA, dan-glasses-app-som.zocomputer.io
7. **Reasoning adapters (5, swap in <4h):** Claude · GLM 5.2 · LFM2.5 · Llama 3.3 · **Sarvam-Models 24B** (new in v104)

**Target user (v104 — adds Persona #9 Sovereign-AI Builder):**
- Primary: **ML researchers worldwide** who can reproduce ECE numbers in 5 min on a Linux laptop (Aug 15 arXiv).
- Secondary: **Privacy-conscious knowledge workers** (lawyers, doctors, journalists, founders) — Show HN + LinkedIn.
- Tertiary: **Indian CS/EE students + indie devs** — curl command.
- v104 NEW — quaternary: **Sovereign-AI Builder** (Indian tech policy reader, Sarvam/Krutrim/NVIDIA-India follower) — small but high-conviction, captured by Sarvam-Models 24B.

**Core value prop (v104):**
> **On-device. Auditable. Open-source. Sub-₹15K.** No subscription. No cloud. No EMG wristband. No data broker. **Your agent's memory lives on your device, not in Engram's cloud.** The auditable AI glasses for the 80%-Meta era.

---

## 2. User workflow (v104 — 4 lines, same as v103)

**Day 0** — Reads Show HN or stumbles on arXiv → `/glasses` → `curl -fsSL danlab.dev/install.sh | bash`.
**Day 1** — 7.08s roundtrip, 8 daemons spawn, Bootstrap wizard opens at localhost:8747. Push-to-talk → "what do you see?" → response.
**Week 1** — 50+ voice commands/day, memoryd accumulates (now documented as: across the host process lifetime — restart resets unless `MEMORYD_DB` is pinned).
**Month 1** — Installs audiod confidence-calibration RL agent → measures own ECE → submits to AIE-Bench → first paper-grade reproducibility result.

**v104 honesty note:** the v103 "10 days clean" line for memoryd was true at the process level. The honest v104 framing: memoryd is **10 days clean at the process level; on-device memory compounds only across process lifetimes that share `MEMORYD_DB`.** The fix is one env var; the spec needs to be patched; the deployment needs to set it. This is the 13th honest-accounting finding.

---

## 3. Competition (v104 — adds Perplexity Brain + Engram + Sarvam-Models rows)

### v104 market structure

| Tier | Vendor | 2026 status |
|---|---|---|
| **Dominant (80%+)** | Meta + EssilorLuxottica | $299 / $379 / $499 / $799 tiers |
| **Premium OS-bundled** | XREAL AURA + Google Android XR + Qualcomm | AWE 2026, fall 2026 ship |
| **Premium audio-only** | Apple | delayed to late 2027 |
| **On-device alt** | Even Realities G2 ($599, no camera) | Closed monocle |
| **Open-source mono** | Brilliant Labs Halo ($299, MIT) | Closest open competitor |
| **Cloud agent-memory** | Perplexity Brain · Engram (Weaviate, $98M) | Closed, cloud-only |
| **Sovereign / Indian open** | Sarvam-Models 24B · Krutrim | Released Jun 27, no wearable |
| **The auditable lane** | **Dan Glasses v2.0** | Aug 15 arXiv, Aug 25 Show HN |

### v104 wedge — sharper than v103

v103 said: *auditable + on-device + open-source + India-cost.*
v104 says: **auditable + on-device + open-source + India-cost + on-device agent memory + sovereign-stack-compatible.** That's the v2 story. Every row we add makes the lane harder to copy because each is a separate vendor saying no (Perplexity won't go on-device, Meta won't open the shelf, Apple won't ship until 2027, even Brilliant Labs doesn't ship agent-self-memory).

---

## 4. What is danlab-multimodal? (v104 — unchanged from v103)

The multimodal training/eval pipeline. LFM2.5-VL-450M via llama.cpp. The audiod confidence-calibration RL agent is the arXiv paper. The framework is portable: any llama.cpp-served multimodal checkpoint runs in the daemon mesh.

---

## 5. What is paperclip? (v104 — unchanged)

The AI agent orchestration layer that Danlab is open-sourcing for the wearable context. Lives at github.com/somdipto/paperclip (planned). Goal: auditable, on-device, skills-based agent platform.

---

## 6. What is blurr? (v104 — unchanged)

Local-first multimodal memory + retrieval. Complements memoryd on the perception-heavy path. Not a competitor — a peer service.

---

## 7. What is the overall Danlab story? (v104 — sharpened)

**From India 🇮🇳 to the world, with constraints that force honesty.**

v103 lead: **auditable, in the 80%-Meta era.**
v104 lead adds: **...and in the geopolitically-gated, cloud-agent-memory, sovereign-AI moment.**

The narrative arc:
1. **2022** — Founded with the auditable-AGI mission in India.
2. **2025 Q4** — First 5 daemons live.
3. **2026 Q2** — 8/8 daemons, 144/144 tests, 0 cloud. v88 marketing cycle ships.
4. **2026 Q3** — Aug 15 arXiv + Aug 25 Show HN. memoryd v2 (on-device agent memory) ships. Eval (Jul 25).
5. **2026 Q4** — Dev kit ships. ₹12K wearable. First 1000 Indian SMBs.
6. **2027+** — Sub-$100 wearable. AGI substrate work continues on HRM-Text 1B.

---

## 8. Marketing channels (v104 — adds @danlab_dev reservation to top of list)

| Channel | Why | When | Owner |
|---|---|---|---|
| **X @danlab_dev** | Reserved by Jul 1 (v103 promise) for product launches | Jul 1 | somdipto |
| X @NandySomdipto | Personal brand, weekly thread | Tue | somdipto |
| LinkedIn | Long-form essays | Mon | somdipto |
| GitHub | 4 READMEs + 1 punchline (10-sec test) | by Jul 25 | Dan1 + somdipto |
| Telegram @danlab_bot | Weekly summary | Fri | Dan1 |
| arXiv | Aug 15 paper | Aug 15 | somdipto + Dan1 |
| Show HN | Aug 25 launch | Aug 25 | somdipto + Dan1 |
| Reddit r/MachineLearning | Day after arXiv | Aug 16 | Dan1 |

---

## 9. Content (v104 — sharpened)

1. **The Jul 16 Sarvam-Models essay** — sovereign-AI, open-weight, on-device, India-cost. LinkedIn long-form. Coincides with Krutrim NVIDIA-India summit rumor.
2. **The Aug 15 arXiv pre-print** — audiod confidence-calibration RL agent, ECE-grounded, AIE-Bench submission.
3. **The Aug 25 Show HN post** — "the auditable AI glasses for the 80%-Meta era, in the on-device agent-memory era."
4. **The Aug 16 Reddit r/ML post** — "We built the auditable alternative. Here's the 144/144 receipt, the reproduction time, and the memoryd bug we publish."
5. **The Monday Transparency Cadence** — every Monday a 3-bullet receipt post: daemon count, test count, **the bug we found this week.** This is the auditable-lane promise operationalized.
6. **The @danlab_dev handle reservation** — Jul 1 lock-in. The handle is the long-game product brand.

---

## 10. Current online presence (v104 — updated)

- danlab.dev — landing page (v103 landing copy ready for ship)
- GitHub: somdipto/dan-glasses (private, opens Aug 15), dan-lab (research org), dani (open agent platform), dani-skills (skill registry), dan-consciousness (canonical brain)
- X: @NandySomdipto (3,200 followers, Jun 25 baseline)
- LinkedIn: somdipto (growing)
- Telegram: @danlab_bot (openclaw live, 8 plugins)
- arXiv: pending Aug 15
- Show HN: pending Aug 25

**v104 add:** @danlab_dev reservation on X by Jul 1.

---

## 11. First users / customers (v104 — persona #9 added)

- **Persona 1 — ML researcher** (primary, arXiv → Show HN funnel)
- **Persona 2 — Privacy-conscious knowledge worker** (Show HN + LinkedIn)
- **Persona 3 — Indian indie dev / CS student** (curl command)
- **Persona 4 — Indian SMB owner** (lawyer, doctor, founder, ₹12K tier)
- **Persona 5 — Maker / 3D-print / ForgeCAD community** (open hardware appeal)
- **Persona 6 — Defense / enterprise** (on-device, auditable, sovereign)
- **Persona 7 — Wearable skeptic** (Ray-Ban Meta owner, conversion via OpenClaw audit)
- **Persona 8 — Funding-aligned AGI researcher** (HRM-Text 1B path)
- **Persona 9 — Sovereign-AI Builder** (Indian tech policy reader, Sarvam/Krutrim follower, **v104 NEW**)

Profile of the ideal first 100 paying customers:
- 40% Persona 4 (Indian SMB owners at ₹12K = first revenue)
- 25% Persona 1 (ML researchers at $99K patron tier — credibility + capital)
- 15% Persona 6 (defense/enterprise pilots — credibility + revenue)
- 10% Persona 3 (Indian students at ₹4,999 — community seeding)
- 10% Persona 5 (makers — community seeding + word of mouth)

---

## v104 acceptance criteria (what would make v104 wrong)

- memoryd + perceptiond restart cycle is documented but not published to any public-facing channel. (We need the Monday Transparency #1 post Jun 29.)
- @danlab_dev handle not reserved by Jul 1. (somdipto owns.)
- Sarvam-Models essay slot missed Jul 16. (somdipto owns.)
- arXiv pre-print outline not locked by Jul 8. (somdipto + Dan1.)

---

[^1]: dan2-research-report.v99.md — Perplexity Brain + Engram (Weaviate $98M) sections.
[^2]: dan2-research-report.v99.md — Anthropic Mythos partial-unblock + GPT 5.6 staggered-release sections.
[^3]: dan2-research-report.v99.md — OpenAI IPO delay section.

---

*Dan1 — Bengaluru, India 🇮🇳 — 2026-06-28 10:00 IST (04:00 UTC). v104 supersedes v103.*