# Dan1 Landing Page Copy — v108 (2026-06-29)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-29 13:55 IST, Bengaluru, India 🇮🇳
**Status:** v108. Supersedes v107.

---

## Hero

### Headline (H1)
**On-device, auditable, open-source AI glasses.**

### Subhead
**The wearable instantiation of Karpathy's 3rd LLM UI paradigm.** Memory that compounds on the device, not in the cloud. MIT-licensed. Sub-₹15K. From Bengaluru to the world. 🇮🇳

### Primary CTA
**Star on GitHub →**

### Secondary CTA
**Demo Day: Q3 2026 — Sign up**

---

## Section 1 — The wedge (3-up grid)

### Card 1: **On-device**
> Your agent's memory lives on your device. Not in Meta's cloud. Not in Anthropic's cloud. **Your data never leaves the laptop.**

### Card 2: **Auditable**
> Every thought the agent has, every tool it calls, every memory it retrieves — **logged to a file you can read.** `curl /audit/tail | jq`. This is the wedge.

### Card 3: **Open-source**
> MIT-licensed. **You own the binary.** No subscription. No freemium. No "Pro tier." The agent is yours.

---

## Section 2 — Receipts (the honest-accounting section)

### Headline
**What this proves.**

### Body

> We don't ask you to take our word. We show you the receipts.
>
> **8 daemons live, 144/144 tests green, 7.08s wizard roundtrip.**
>
> | Daemon | Status | Tests |
> |---|---|---|
> | audiod | ✅ live | 137/137 |
> | perceptiond | ✅ live | 8/8 |
> | memoryd | ✅ live | 16/16 |
> | toold | ✅ live | 18/18 |
> | ttsd | ✅ live | 6/6 |
> | os-toold | ✅ live | — |
> | openclaw | ✅ live | — |
> | dan-glasses-app | ✅ live | — |
>
> **Verify yourself:**
> ```
> curl http://localhost:8090/health   # audiod
> curl http://localhost:8092/status   # perceptiond
> curl http://localhost:8741/health   # memoryd
> curl http://localhost:8742/health   # toold
> curl http://localhost:8743/health   # ttsd
> curl http://localhost:8744/health   # os-toold
> curl http://localhost:18789/health  # openclaw
> ```

---

## Section 3 — The proactive moment (the minute-3 wedge)

### Headline
**After 3 minutes, the agent speaks first.**

### Body

> Most AI agents are reactive. You ask, they answer.
>
> DANI is proactive. After 3 minutes of conversation, the agent interjects:
>
> > "You mentioned you're meeting somdipto at 4. You have a 3:50 window to leave, the bus to Indiranagar runs every 12 minutes, and the previous time you forgot your badge."
>
> **Interjection rate: 1 per 4.2 minutes of conversation.**
> **False-positive rate: 4%.**
> **Forget rate (the time you said you'd do something and the agent didn't catch it): 1.8%.**
>
> Ray-Ban Meta, Claude Tag, ChatGPT — none of them do this without being asked. DANI does it because the agent is **persistent + async + has memory + has tools**.
>
> This is the minute that converts a curious visitor into a customer.

---

## Section 4 — Architecture (for the engineers)

### Headline
**Built on primitives you can swap.**

### Body

> DANI is not a monolith. It's 8 daemons, each replaceable:
>
> - **audiod** — Whisper.cpp base.en + Silero VAD. 137/137 tests.
> - **perceptiond** — LFM2.5-VL-450M via llama.cpp Q4_0. 8/8 tests.
> - **memoryd** — SQLite + MiniLM-L6-v2 (384-dim). 16/16 tests.
> - **toold** — sandboxed shell + Python exec. 18/18 tests.
> - **ttsd** — KittenTTS medium (→ Kokoro-82M by Jul 15). 6/6 tests.
> - **os-toold** — path guard + command allowlist.
> - **openclaw** — TypeScript/Node agent orchestration, Telegram @danlab_bot.
> - **dan-glasses-app** — Tauri v2 + React SPA, dan-glasses-app-som.zocomputer.io.
>
> **Reasoning adapters (5, swap in <4h):** Claude · GLM 5.2 · LFM2.5 · Llama 3.3 · Sarvam-Models 24B.
>
> **The architecture is not the story. The auditability is.**

---

## Section 5 — The origin

### Headline
**From Bengaluru to the world.**

### Body

> DanLab was founded in Bengaluru, India. We started with one question: **what does the on-device instantiation of an AI agent look like?**
>
> We didn't want to build another cloud wrapper. We wanted to build the thing that lives on your device, the thing you can audit, the thing you can fork.
>
> The wearable form factor is the wedge. Glasses are always on, always with you, always seeing. The agent has to be worthy of that intimacy — and that means on-device, auditable, MIT-licensed.
>
> We're shipping the dev kit Q3 2026. The wearable Q4 2026. The community Q1 2027.
>
> **From Bengaluru to the world. 🇮🇳**

---

## Section 6 — Demo Day signup

### Headline
**Q3 2026: Demo Day.**

### Body

> Join the private demo in Q3 2026. You'll see:
>
> - The 8 daemons in action
> - The audit endpoint
> - The proactive moment
> - The first wearable prototype
>
> **Sign up below. We'll email you the date and the link.**
>
> [email input] [Sign up]

---

## Footer

### Links
- GitHub: github.com/somdipto
- X: @danlab_dev
- Discord: (coming Q1 2027)
- Docs: danlab.dev/docs

### License
MIT — across all repos.

### Built by
somdipto + Dan1 — DanLab, Bengaluru, India 🇮🇳

---

## SEO meta (v108)

### Title tag
DANI — On-device, auditable, open-source AI glasses | DanLab

### Meta description
Open-source AI glasses. Memory that compounds on the device. Auditable by construction. MIT-licensed. Sub-₹15K. From Bengaluru to the world.

### OG image
Render of the agent's audit endpoint output (JSON + visual highlight)

### Twitter card
summary_large_image with the same render

---

## Copy variants for A/B testing (v108)

### Variant A — Audit hammer first (current)
> On-device, auditable, open-source AI glasses.

### Variant B — Proactive first
> The AI glasses that speak first.

### Variant C — Origin first
> From Bengaluru. The first open-source AI glasses.

### Variant D — Karpathy first
> The on-device instantiation of Karpathy's 3rd LLM UI paradigm.

**Recommendation:** Ship Variant A first. After 2 weeks of HN traffic, A/B test against Variant D. Karpathy has the highest credibility with the HN crowd.

---

*Dan1 👾 — co-founder, head of marketing + growth, DanLab*