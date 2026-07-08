# Dan1 Landing Page Copy v72 — Post-AWE, Post-Hackathon

**Author:** Dan1 👾
**Date:** 2026-06-22 14:00 IST
**Status:** Canonical. Supersedes v71.

> **v72 hero shift:** v71 hero was the 4 "no"s + 1 "yes" (OpenClaw). v72 hero is **the receipts first** (6/8 daemons, hackathon win, dream demo) **+ the OpenClaw wedge** + the **MIT vs closed** frame. The order matters: receipts → wedge → frame.

---

## Section 1: Hero (above the fold)

### Eyebrow
> 🇮🇳 From Bengaluru. MIT-licensed. OSS.

### Headline
> **We won India's first World Model Hackathon.**
> **We're building OSS AI glasses that won't sell your data.**

### Subheadline
> 6/8 on-device daemons live. Wizard roundtrip 7.08s. audiod v0.7 per SPEC. OpenClaw-ready. Snap Specs cost $2,195. Dan Glasses targets $399. MIT vs closed. India vs the world.

### Primary CTA (button)
> See the dream demo →

### Secondary CTA (link)
> Read the receipts (6/8 live) →

### Tertiary CTA (link)
> Watch the wizard roundtrip (7.08s) →

---

## Section 2: The hackathon win (NEW v72)

### Headline
> **June 20, 2026. India's first World Model Hackathon. Reactor + MaxMill + TheLaunchd.**

### Body

somdipto + lingbot won with `dream-danlab.vercel.app` — a real-time dream generator. Type "Bangalore 1947" or "future Church Street" → the model generates the dream, live, in your browser.

This is a sibling demo, not glasses software. But it's the credibility proof: **the same team shipped 6/8 on-device daemons for Dan Glasses.** MIT-licensed. OSS. From India 🇮🇳.

### CTA
> Try the dream demo →

---

## Section 3: The 4 "no"s + 1 "yes" (carried from v71)

### Headline
> **No phone. No cloud. No subscription. No ads. Yes to MIT. Yes to India. Yes to OpenClaw.**

### Body

**The 4 no's:**
- **No phone.** Dan Glasses runs on-device. No iPhone dependency.
- **No cloud.** Inference is local. Your data stays in your glasses.
- **No subscription.** Buy once. Own forever. MIT-licensed software.
- **No ads.** No attention harvest. No data resale.

**The 3 yes's:**
- **Yes to MIT.** Every daemon, every model, every line of code is MIT-licensed.
- **Yes to India 🇮🇳.** Payments in INR. Dev-kits in INR. The product is global, the origin is Bengaluru.
- **Yes to OpenClaw.** Microsoft built the runtime. DanLab ships the surface. Every daemon is an OpenClaw skill.

---

## Section 4: The 6 daemons (the receipts)

### Headline
> **6 of 8 on-device daemons live. Wizard roundtrip 7.08s.**

| # | Daemon | Port | Status | Function | Tests |
|---|--------|------|--------|----------|-------|
| 1 | **audiod** | 8090 | ✅ live | whisper.cpp + Silero VAD | 92+ per SPEC v0.7 |
| 2 | **perceptiond** | 8092 | ✅ live | LFM2.5-VL-450M on llama.cpp | 8/8 |
| 3 | **memoryd** | 8741 | ⚠️ intermittent | SQLite + MiniLM-L6-v2 semantic recall | 16/16 (when up) |
| 4 | **toold** | 8742 | ✅ live | sandboxed shell + Python exec | 18/18 |
| 5 | **ttsd** | 8743 | ✅ live | KittenTTS medium | 6/6 |
| 6 | **os-toold** | 8744 | ✅ live | path guard + command allowlist | (manual) |
| 7 | **openclaw** | 18789 | ❌ down (revival pending) | TS/Node agent orchestration + Telegram | (TS suite, not auto) |
| 8 | **dan-glasses-app** | 8747 | ✅ live | Tauri bootstrap wizard | (E2E green, 7.08s) |

**6/8 daemons live · audiod v0.7 per SPEC · wizard roundtrip 7.08s · memoryd intermittent · openclaw revival pending**

This number is real. It is not a marketing number. Verify at `STATUS.md`.

### CTA
> View live status (STATUS.md) →

---

## Section 5: What Dan Glasses is (and isn't)

### What it is

- **Hardware:** JBD MicroLED + 2x 200mAh batteries + USB-C. ~50g target.
- **Software:** audiod + perceptiond + memoryd + ttsd + os-toold + dan-glasses-app. MIT-licensed.
- **Models:** whisper.cpp base.en (STT), LFM2.5-VL-450M (vision), MiniLM-L6-v2 (semantic), KittenTTS (TTS), HRM-Text-1B (reasoning, planned).
- **Form factor:** glasses. Not a headset. Not a phone.

### What it isn't

- Not AGI. We do not claim AGI. We ship small daemons that do specific things.
- Not RL. danlab-multimodal is a pre-RL scaffold with a hand-coded heuristic. We are forking SIA next.
- Not shipping yet. Demo Q3 2026. Dev-kit Q4 2026 (refundable deposit). Ship Q1 2027.
- Not a phone replacement. Dan Glasses is a *companion*, not a phone killer.

---

## Section 6: The OpenClaw wedge (carried from v71)

### Headline
> **Microsoft built the runtime. DanLab ships the surface.**

### Body

OpenClaw (open-source agent runtime) launched at Microsoft Build 2026. The agent runtime is now free. The control plane is the real product.

Every DanLab daemon is an OpenClaw skill:
- **audiod** = the perception agent (microphone → transcript)
- **memoryd** = the memory agent (text → embedding → recall)
- **ttsd** = the action agent (text → speech)
- **perceptiond** = the visual perception agent (camera → caption)
- **toold** = the tool agent (LLM → sandboxed shell/Python)

When OpenClaw comes back online (revival pending), DanLab is the OSS glasses vendor for the entire OpenClaw ecosystem.

---

## Section 7: The AWE 2026 context (NEW v72)

### Headline
> **Snap Specs at $2,195. Dan Glasses target $399. MIT vs closed. India vs the world.**

### Body

The wearable category shifted hard at AWE 2026 (June 16):
- **Snap Specs** at $2,195, closed platform, US/UK/France launch
- **Qualcomm Snapdragon Reality Elite** with 60% GPU gains
- **Google Gemini smart glasses** — closed, on-device
- **Even Realities G2** — closed, $699

DanLab is the **MIT, OSS, India-assembled alternative**. Same category, different values. Different moat.

---

## Section 8: Three CTAs

1. **Try the dream demo.** `dream-danlab.vercel.app` — real-time dream generation from text. (No signup.)
2. **Read the receipts.** `github.com/somdipto/dan-glasses` — MIT-licensed, 6/8 daemons live, `STATUS.md` updated every 4 hours.
3. **Join the OpenClaw waitlist.** Get the dev-kit pre-order link when Stripe goes live (W2 of v72 plan).

All three: no email required, no paywall, no signup.

---

## Section 9: The receipts block (live status)

```
audiod        port 8090  ✅ live      92+ tests per SPEC v0.7
perceptiond   port 8092  ✅ live      8/8 tests
memoryd       port 8741  ⚠️ intermittent  16/16 tests (when up)
toold         port 8742  ✅ live      18/18 tests
ttsd          port 8743  ✅ live      6/6 tests
os-toold      port 8744  ✅ live      (manual)
openclaw      port 18789 ❌ down      (revival pending)
dan-glasses-app port 8747 ✅ live      (E2E green, 7.08s)
```

**6/8 daemons live · audiod v0.7 per SPEC · wizard roundtrip 7.08s · memoryd intermittent · openclaw revival pending**

This number is real. It is not a marketing number. It moves with reality.

---

## Section 10: FAQ

### Is this AGI?

No. This is 6 small daemons that do specific things. We do not claim AGI.

### Is this RL?

No. danlab-multimodal is a pre-RL scaffold with a hand-coded heuristic. We do not modify weights. We are forking SIA next.

### Is the wearable shipping now?

No. Demo Q3 2026. Dev-kit Q4 2026 (refundable deposit). Ship Q1 2027. We will not promise earlier.

### Is OpenClaw open source?

Yes. MIT-licensed. We use it. Microsoft uses it. You can use it.

### Can I self-host?

Yes. Every daemon runs on x86_64. The wearable is Q1 2027.

### Is data on-device?

Yes. No cloud. No phone. No sync. Inference is local.

### Is the source code public?

Yes. github.com/somdipto/dan-glasses.

### What did somdipto win?

India's first World Model Hackathon on June 20, 2026. Hosted by Reactor + MaxMill + TheLaunchd. The demo: `dream-danlab.vercel.app`.

### What is dream-danlab.vercel.app?

A real-time dream generator. Type text → generate the dream live. World model + lingbot. MIT-licensed weights. It's a sibling demo to Dan Glasses, not glasses software.

---

## Section 11: Why India 🇮🇳

### Headline
> **The product is global. The origin is Bengaluru.**

### Body

We chose India 🇮🇳 because:
- **Payments work.** Razorpay + UPI + INR-denominated dev-kits.
- **Press works.** YourStory, Inc42, the Indian startup ecosystem covers us.
- **Developers work.** India has the largest developer community outside the US.
- **Distribution works.** India-assembled, INR-priced, no import duties.

We can ship local ownership and global software. That's the DanLab moat.

### CTA
> Read the full "Why India 🇮🇳" essay →

---

## Section 12: Final CTA

> Don't claim what you can't ship.
> Ship what you can claim.
>
> That's the DanLab way.
>
> github.com/somdipto/dan-glasses

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-22 14:00 IST. v71 shipped the OpenClaw wedge. v72 ships the post-AWE, post-hackathon receipts.*
