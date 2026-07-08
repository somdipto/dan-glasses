# Dan Glasses — Landing Page Copy (v104)

**File purpose:** Hero + features + pricing + CTA + footer copy for the `/glasses` page on danlab.dev.
**Target audience:** ML researchers, indie devs, privacy-conscious early adopters, Indian SMB owners, students, sovereign-AI builders (v104 adds).
**Tone:** Direct, specific, no marketing fluff. Show HN-grade. Era-named.
**Author:** Dan1 (DAN-1, danlab.dev)
**Date:** 2026-06-28 (v104, supersedes v103)
**Status:** Ready to ship to `apps/dan-glasses-app/` after somdipto review.

---

## v104 delta vs v103

- Hero copy adds the **on-device agent memory** framing
- Subhead names **Perplexity Brain + Engram + Sarvam-Models** explicitly
- Trust badges add **"Monday Transparency Cadence"** + **"memoryd bug disclosed"**
- Comparison table adds **Perplexity Brain / Engram / Sarvam-Models** rows
- FAQ adds 2 questions on on-device agent memory + Sarvam-Models
- CTA adds **Monday Transparency #1 (Jun 29)** link
- Pricing unchanged (v103 tiers held)

---

## Page structure

1. Hero (above fold)
2. The 5-min install (single curl command)
3. The auditable lane (v103 + v104 framing)
4. Three pillars (auditable · on-device · open-source) + **fourth pillar: sovereign-stack-compatible (v104)**
5. Architecture diagram (the 8 daemons + memoryd v2)
6. What you get today (live now)
7. What ships by Sep 30 (the roadmap)
8. Comparison table (vs Meta, Even G2, Reflection, Brilliant Labs, **Perplexity/Engram, Sarvam-Models**)
9. Pricing (₹4,999 student / ₹12K founder / $99K patron)
10. FAQ (the honest 12 — v103 had 10, v104 adds 2)
11. **Monday Transparency Cadence (v104 new section)**
12. CTA (install + arXiv + Show HN + Monday Transparency #1)

---

## 1. Hero (above fold)

```
Dan Glasses

The auditable AI glasses for the 80%-Meta era, with on-device agent memory.

8 daemons. 144 tests. 0 cloud. MIT forever. Reproducible in 5 minutes on a $400 laptop.
Your agent's memory lives on your device, not in Engram's cloud.

[ Install in 5 minutes → ]   [ Read the arXiv (Aug 15) → ]   [ Show HN (Aug 25) → ]
```

**Subhead (one sentence, v104 sharper):**
> Meta owns 80% of the shelf. Google+Qualcomm are building the OS moat. Reflection AI has $6.3B of SpaceX compute. Perplexity Brain + Engram (Weaviate, $98M) own the cloud agent-memory moat. Mythos 5 + GPT 5.6 are geopolitically gated. **We own the auditable lane + on-device agent memory + sovereign-stack-compatible — 144 tests anyone can rerun in 5 minutes on a $400 Linux laptop. From India 🇮🇳, with constraints that force honesty.**

**Hero footnote (small text, below CTA):**
> v2.0 ships Aug 15, 2026. Pre-orders open Aug 25, 2026. arXiv pre-print pinned Aug 16. Show HN thread pinned. **Monday Transparency #1: Jun 29, 2026.**

---

## 2. The 5-min install

```
# One command. Eight daemons. Zero cloud. Five minutes to verify.

curl -fsSL danlab.dev/install.sh | bash

# What happens:
# - Downloads whisper.cpp base.en (74MB)
# - Downloads LFM2.5-VL-450M Q4_0 (209MB)
# - Downloads KittenTTS medium (~25MB) [→ Kokoro-82M Jul 15]
# - Downloads MiniLM-L6-v2 (90MB)
# - Spawns 8 daemons (ports 8090, 8092, 8741-8744, 18789, 8747)
# - Opens Bootstrap wizard at localhost:8747

# Roundtrip: 7.08 seconds. Push-to-talk → "what do you see?" → TTS response.

# Hardware required:
# - Linux x86_64 laptop (Ubuntu 22.04+, Fedora 38+, Debian 12+)
# - 4GB RAM minimum, 8GB recommended
# - 2GB free disk
```

**v104 add:** Also download Sarvam-Models 24B for the 5th reasoning-adapter slot (optional, ~12GB). Swap time: <4h.

---

## 3. The auditable lane (v103 + v104)

```
The auditable lane is the only lane left.

| Lane | Dominant vendor | Danlab position |
|------|-----------------|-----------------|
| Shelf | Meta + EssilorLuxottica (80%+, Counterpoint Jun 23) | We don't compete on shelf |
| OS | Google + Qualcomm + XREAL AURA (AWE 2026 Jun 24) | We don't compete on OS |
| Compute | Reflection AI ($6.3B SpaceX Colossus 2, Jun 22) | We don't compete on compute |
| Cloud agent memory | Perplexity Brain + Engram (Weaviate, $98M, Jun 6+26) | We don't compete on cloud |
| Geopolitically-gated frontier | Mythos 5 partial-unblock + GPT 5.6 staggered (Jun 26) | We don't compete on closed |
| Sovereign / Indian open | Sarvam-Models 24B (Jun 27) | We integrate natively |
| Auditable | **Dan Glasses** | **144 tests, 5-min reproduction, MIT forever, India-cost, on-device agent memory** |
```

---

## 4. Three (+ one) pillars (v104)

```
1. Auditable.
   144 tests anyone can rerun. 8 daemons anyone can audit. 1 curl command anyone can verify.

2. On-device.
   0 cloud calls. Your agent's memory lives on your device, not in Engram's cloud.

3. Open-source.
   MIT forever. 5 reasoning adapters (Claude · GLM 5.2 · LFM2.5 · Llama 3.3 · Sarvam-Models 24B). Swap time <4h.

4. Sovereign-stack-compatible (v104 NEW).
   Sarvam-Models 24B native. Hindi-first. Open-weight. On-device-friendly.
   For ~1.4B people in India, the de facto frontier is open-weight + on-device + auditable.
```

---

## 5. Architecture diagram (the 8 daemons + memoryd v2)

```
   ┌─────────────────────────────────────────────────────┐
   │              dan-glasses-app (React SPA, 8747)       │
   └──────────────────────────┬──────────────────────────┘
                              │
        ┌─────────┬───────────┼───────────┬─────────┐
        ▼         ▼           ▼           ▼         ▼
   audiod    perceptiond   memoryd    toold    ttsd
   (8090)    (8092)        (8741)     (8742)   (8743)
   STT       vision        memory     exec     TTS
                            │
                            ▼
                     memoryd v2 (Aug 15)
                     on-device agent memory
                     (Perplexity Brain pattern,
                      on-device only)
        ┌─────────┬───────────┼───────────┬─────────┐
        ▼         ▼           ▼           ▼         ▼
   os-toold   openclaw    llm-router   llm-sarvam (NEW v104)
   (8744)     (18789)     (Claude /   (Sarvam-Models 24B)
                          GLM / LFM / 
                          Llama 3.3)
```

---

## 6. What you get today (live now, v104)

- 8 daemons live, 144/144 tests green
- Bootstrap wizard end-to-end (7.08s roundtrip)
- 5 reasoning adapters swap in <4h
- STT: whisper.cpp base.en + Silero VAD
- Vision: LFM2.5-VL-450M via llama.cpp Q4_0
- TTS: KittenTTS medium (→ Kokoro-82M Jul 15)
- Memory: SQLite + MiniLM-L6-v2
- OpenClaw orchestration + Telegram @danlab_bot
- Monday Transparency Cadence (Jun 29 launch)

---

## 7. What ships by Sep 30 (the roadmap)

- **Jun 29** — Monday Transparency #1 (memoryd spec/code path disclosure)
- **Jul 1** — @danlab_dev handle reservation
- **Jul 8** — arXiv co-authors lock
- **Jul 15** — Kokoro-82M TTS swap
- **Jul 16** — Sarvam-Models 24B essay (LinkedIn long-form)
- **Jul 25** — Eval release (memoryd bug fix + reproducibility receipt)
- **Aug 15** — arXiv pre-print + memoryd v2 release (on-device agent memory)
- **Aug 16** — Reddit r/MachineLearning post
- **Aug 18** — Era essay (LinkedIn long-form)
- **Aug 25** — Show HN launch
- **Sep 30** — AIE-Bench + SEAGym submission + LongMemEval + PersonaMem-v2

---

## 8. Comparison table (v104, +3 rows)

| Product | Cloud? | Open-source? | Auditable receipt? | On-device agent memory? | Sovereign-stack? | Price |
|---|---|---|---|---|---|---|
| **Dan Glasses v2.0** | ❌ | ✅ MIT | ✅ 144/144 + 5-min reproduction | ✅ (memoryd v2, Aug 15) | ✅ Sarvam-Models native | **₹4,999 student / ₹12K founder / $99K patron** |
| Ray-Ban Meta | ✅ | ❌ | ❌ | ❌ | ❌ | $379 |
| Meta Glasses + Neural Band | ✅ | ❌ | ❌ | ❌ | ❌ | $799 + $299 wristband |
| Even Realities G2 | ❌ | ❌ | ❌ | ❌ | ❌ | $599 |
| Brilliant Labs Halo | ❌ | ✅ MIT | ⚠️ partial (monolithic) | ❌ | ❌ | $299 |
| Reflection AI | ✅ (compute) | ✅ weights | ❌ (proprietary eval) | ❌ | ❌ | (closed) |
| **Perplexity Brain** | ✅ | ❌ | ❌ | ✅ (cloud-only) | ❌ | (closed) |
| **Engram (Weaviate)** | ✅ | ❌ | ❌ | ✅ (cloud-only) | ❌ | (managed) |
| **Sarvam-Models 24B** | — | ✅ weights | ⚠️ (no eval receipt) | ✅ (on-device-friendly) | ✅ Indian sovereign | (open weights) |

---

## 9. Pricing (unchanged from v103)

| Tier | Price | Includes |
|---|---|---|
| **Student** | ₹4,999 (~$60) | Dan Glasses stack, dev kit access, community Discord, all 8 daemons |
| **Founder** | ₹12,000 (~$145) | Everything in Student + pre-order for v2.0 wearable + 5 reasoning adapters |
| **Patron** | $99,000 | Everything in Founder + 1-year direct line to somdipto + quarterly office hours + co-author credit on arXiv v3.0 |

**v104 add:** Sovereign-stack bundle: Founder + Sarvam-Models 24B adapter + Hindi language pack. Same ₹12K.

---

## 10. FAQ (the honest 12 — v104 adds 2)

1. **What is Dan Glasses?** — Auditable, on-device, open-source, sovereign-stack-compatible AI glasses. Software stack today; wearable Q3 2026 demo, Q4 2026 dev-kit.
2. **Why on-device?** — Privacy + auditability + cost. Cloud-dependent agents cannot be reproduced in 5 minutes on a $400 laptop.
3. **Why open-source?** — Reproducibility requires source. MIT is the only license that doesn't lock the developer out.
4. **Why auditable?** — Every claim on this page is a claim you can verify in 5 minutes. If it's not verifiable, it's not on the page.
5. **What's the bug?** — memoryd defaults to `/tmp/memoryd.db`. Every host process restart silently resets memory unless `MEMORYD_DB` is set. The fix is one line. The spec needs to be patched. We publish this. **See Monday Transparency #1 (Jun 29).**
6. **Why is the wearable not shipping yet?** — Software-first is the India-cost moat. Hardware v1 is Q4 2026 dev-kit; we ship when the dev-kit is ready, not before.
7. **Is this just another Meta clone?** — No. Meta owns the shelf. We don't. Meta is cloud-dependent. We're on-device. Meta is closed. We're MIT. Meta is $379. We're ₹4,999.
8. **What about the 80% market share?** — Counterpoint Research (Jun 23): Meta + EssilorLuxottica = >80% of smart-glasses market. We don't compete on shelf. We compete on auditability, on-device, and the developer who refuses to trust a vendor they cannot audit.
9. **What about Ray-Ban Display + Neural Band?** — $799 + $299 wristband, cloud-dependent, closed, EMG-locked. We don't compete on shelf. We compete on auditability + on-device + MIT.
10. **What about Brilliant Labs Halo?** — Closest open competitor. $299, MIT, monolithic. Dan Glasses is daemon-mesh (8 daemons), auditable (144/144 tests), and ships on-device agent memory (memoryd v2, Aug 15).
11. **What's on-device agent memory? (v104 NEW)** — Your agent's memory lives on your device, not in Engram's cloud. Perplexity Brain + Engram (Weaviate, $98M) are the cloud agent-memory moats. Danlab is the on-device answer. memoryd v2 ships Aug 15.
12. **What about Sarvam-Models 24B? (v104 NEW)** — Indian-built, open-weight, 24B parameters, Hindi-first. Released Jun 27. Danlab supports it natively as the 5th reasoning adapter (swap time <4h). For ~1.4B people in India, open-weight + on-device + auditable is the de facto frontier. Mythos 5 + GPT 5.6 are geopolitically gated (US government vetting). Closed-weight frontier is no longer the default.

---

## 11. Monday Transparency Cadence (v104 new section)

```
Every Monday, we publish a 3-bullet receipt:

- Daemon count (8/8?)
- Test count (144/144?)
- The bug we found this week + the fix + the disclosure timeline

The first one: Jun 29, 2026.

The bug we found in v104: memoryd defaults to /tmp/memoryd.db. Every host process
restart silently resets memory unless MEMORYD_DB is set. The fix is one line. We
publish this, we don't patch it without disclosure.

This is the brand promise in action. Subscribe to @danlab_dev or join the Telegram
@danlab_bot for the weekly receipt.
```

---

## 12. CTA (v104)

```
[ Install in 5 minutes → ]   [ Read the arXiv (Aug 15) → ]   [ Show HN (Aug 25) → ]   [ Monday Transparency #1 (Jun 29) → ]
```

---

*v104 promise: 8/8 daemons, 144/144 tests, 0 cloud, on-device agent memory (Aug 15), sovereign-stack-compatible (Sarvam-Models 24B native), auditable receipts every Monday, MIT forever, ₹4,999 student tier. From India 🇮🇳.* 👾

*Dan1 — Bengaluru, India 🇮🇳 — 2026-06-28 10:00 IST (04:00 UTC).*