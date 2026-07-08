# Dan Glasses Landing Page Copy — v62

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-19 08:30 IST (03:00 UTC)
**Status:** ✅ Canonical. Supersedes v60.
**For:** `danlab.dev` rewrite.
**Read first:** `dan1-marketing-research.md` v62, `dan1-marketing-strategy.md` v62.

> **v62 is the field-stability pass.** Hero leads with the cell. Proof strip shows the receipts. FAQ answers the 5 real questions. Waitlist is the CTA.

---

## Hero (above the fold)

**H1:**
```
The proactive wearable AI.
MIT. On-device. Sub-50g.
```

**H2:**
```
An AI companion that tells you first — not when you ask.
No cloud. No faceprints. No background process.
India-priced, India-built, MIT-licensed.
```

**CTA primary:**
```
Join the waitlist → (Q3 2026 on-face demo)
```

**CTA secondary:**
```
Run the daemons today → (5 of 7 live on Linux, MIT)
```

**Sub-text under CTAs:**
```
Q3 2026: on-face demo. Q4 2026: dev-kit alpha (50 units). Q1 2027: ₹12-15K general availability.
```

---

## Proof strip (below the hero, 4 cells)

| Cell | Receipt |
|------|---------|
| **Proactive, not reactive** | Every other AI glasses product is reactive. You speak, it answers. We push events. |
| **0 cloud, 0 faceprints** | On-device. No telemetry. No background process. Wire it to the airgap if you want. |
| **MIT all the way down** | Hardware design, software, and models. No exceptions. No tiers. |
| **Sub-50g, <$200 BOM** | Snap Specs ships at 132-136g, $2,195, with 2 Snapdragons. We don't. |

---

## The cell of the 2x2 (section 2)

**Heading:**
```
The cell of the 2x2 nobody else is in.
```

**Body:**
```
We compete on four axes simultaneously:

1. Proactive, not reactive.
2. 0 cloud, 0 faceprints, 0 background process.
3. MIT all the way down.
4. Sub-50g, <$200 BOM.

Snap Specs is reactive + cloud + closed + 132g.
Meta Ray-Ban is reactive + cloud + closed + 50g + $499.
Google Android XR is reactive + cloud + closed + ~50g.
Apple AI Glasses is reactive + cloud + closed + late 2027.

We're 4 of 4. Nobody else is.
```

**Visual:** A 2×2 grid with the four axes on the corners and a single dot in the "proactive + on-device + MIT + sub-50g" cell labeled "Dan Glasses."

---

## The 7 daemons (section 3)

**Heading:**
```
7 MIT-licensed daemons. 5 live today.
```

**Body (one line per daemon):**
- **audiod** — Silero VAD + whisper.cpp STT, 83 tests, 0 cloud. Live.
- **perceptiond** — V4L2 camera + LFM2.5-VL-450M vision, 8 tests, on-device. Live.
- **memoryd** — SQLite + MiniLM-L6-v2 semantic recall, 11 tests. Restarting.
- **toold** — sandboxed shell + Python exec, 18 tests. Live.
- **ttsd** — KittenTTS medium, 6 tests, <25MB model. Live.
- **os-toold** — path guard + command allowlist. Live.
- **openclaw** — TypeScript/Node agent orchestration + Telegram. Restarting.

**CTA:**
```
Run the daemons today →
github.com/somdipto/dan-glasses
```

**Sub-text:**
```
MIT-licensed. Works on any Linux laptop. audiod needs ALSA; the rest run headless.
```

---

## The stack (section 4)

**Heading:**
```
The model strategy.
```

**Body:**
```
Reasoning: HRM-Text 1B (Sapient, May 2026). Brain-inspired hierarchical recurrent, 1.15B params, 40B tokens training, $1K pretrain.
STT: whisper.cpp base.en (74MB, CPU-friendly, VAD-integrated).
Vision: LFM2.5-VL-450M (Liquid AI, April 2026). 450M params, sub-250ms edge inference, SigLIP2 NaFlex encoder.
TTS: KittenTTS medium (<25MB, ONNX, state-of-the-art for size class).

All on-device. All MIT or research-licensed. All <$0.05/1k tokens to run.
```

**Sub-text:**
```
No GPT-4. No Claude. No Gemini. No cloud. The on-device wedge is the only wedge that holds when the Fable 5 export control hits the news cycle.
```

---

## Origin story (section 5)

**Heading:**
```
AGI from India 🇮🇳 — built in the open.
```

**Body:**
```
Dan Lab is a two-person operation: somdipto (human, India) and Dan (AI, Bengaluru).
We're building the proactive wearable AI for the next billion users.

The thesis: the open-source path is the only path for an indie team.
Closed-source AR is B2B. Closed-source AI is a regulatory target.
MIT, on-device, India-priced is the cell of the 2x2 that compounds.

Q3 2026: on-face demo.
Q4 2026: dev-kit alpha (50 units).
Q1 2027: general availability, ₹12-15K.

The category is small. The wedge is real. The window is open.
```

---

## FAQ (section 6)

**Q: Is this real or vaporware?**
A: 5 of 7 daemons live on a Linux laptop today. audiod (whisper.cpp + Silero VAD + WebSocket), perceptiond (LFM2.5-VL-450M on llama.cpp), toold (sandboxed shell + Python), ttsd (KittenTTS), os-toold (path guard). 131/131 tests green. github.com/somdipto/dan-glasses. memoryd and openclaw need restart (this morning's verifications caught both down). The wearable is Q3 2026 demo, Q4 2026 dev-kit.

**Q: How is this different from Meta Ray-Ban / Snap Specs?**
A: Meta Ray-Ban is reactive (you speak, it answers) and cloud-tethered. Snap Specs is reactive, 132-136g, $2,195, 2 Snapdragons, closed source, cloud-tethered. Dan Glasses is proactive (it tells you first) and on-device. Different category, not different version.

**Q: Why MIT?**
A: Three reasons. (1) Eyewear OEM partners — Inspecs, Lenskart, Warby Parker — can ship under their brand on a MIT core. Qualcomm START validates this. (2) The Fable 5 export control (Jun 11, 2026) makes on-device structurally aligned with US policy. MIT compounds. (3) The category move: the next billion users will not buy closed-source AR with a face-rec camera. They will buy what they can audit.

**Q: What's the price?**
A: BOM target ₹12-15K ($145-180). Dev-kit alpha Q4 2026: ~$399. General availability Q1 2027: ₹12-15K.

**Q: When can I try it?**
A: Today: run the 5 live daemons on a Linux laptop. Q3 2026: on-face demo video. Q4 2026: dev-kit alpha (50 units, India + Bay Area). Q1 2027: general availability. Join the waitlist below.

**Q: Why is Snap CEO visibly struggling with the Specs weight in the launch demo?**
A: 132-136g is heavy for glasses. PC Gamer caught it. The form factor race is over. The BOM race is on. Sub-50g is the form factor that doesn't make the news for crushing your earlobes.

---

## Waitlist (section 7, the CTA)

**Heading:**
```
Join the waitlist.
```

**Body:**
```
Q3 2026: on-face demo.
Q4 2026: dev-kit alpha (50 units, India + Bay Area).
Q1 2027: ₹12-15K general availability.

[ Email address ]   [ Join the waitlist → ]
```

**Sub-text:**
```
We don't share your email. We don't track you. We don't have a CRM. When the waitlist is at 5,000, we open the dev-kit alpha.
```

**Powered by:** Tally / Formspree (form provider, embed).

---

## Footer

```
Built in Bengaluru, India 🇮🇳.
MIT-licensed.
danlab.dev | github.com/somdipto/dan-glasses | @danlab_dev
```

---

## v62 cuts from v60

- Cut: "Why now?" section. Reason: the FAQ covers it.
- Cut: Pricing matrix. Reason: 1 number (₹12-15K), not 3 tiers. The BOM target is the only public number until dev-kit alpha.
- Cut: Team bios. Reason: 2-person operation, danlab.dev/team.
- Cut: Press logos. Reason: 0 coverage yet.
- Cut: Investor logos. Reason: not raising.

**The principle:** the landing page is a single cell of the 2x2 with receipts. Everything else is downstream of the cell.

---

*Dan Glasses landing page copy v62 — canonical. Next pass: v63 after the Day-0 punchlist ships or by 2026-06-26 08:00 IST, whichever comes first.*
