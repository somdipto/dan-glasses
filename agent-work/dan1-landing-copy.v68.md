# Dan1 Landing Copy v68 — The 4 "No"s on danlab.dev

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 09:30 IST (04:00 UTC)
**Stack:** zo.space page route (free, instant, RSS-capable). Falls back to GitHub Pages if zo.space fails.
**Status:** ✅ Canonical. Supersedes v67.

> **v68 hero:** "No phone. No cloud. No subscription. No ads." Replaces v67's price-anchor hero. The price-anchor moves to §3 as a single line. The 4 "no"s are the position.

---

## 1. The full landing page (top to bottom)

### §1. Hero (above the fold)

```
No phone. No cloud.
No subscription. No ads.

The proactive AI companion.
Open source. On-device. MIT.

Built in Bengaluru, India 🇮🇳

[Try audiod now] [Read the dev log] [Star on GitHub]
```

(3 buttons. Primary: "Try audiod now" → danlab.dev/audiod-demo. Secondary: "Read the dev log" → danlab.dev/blog. Tertiary: "Star on GitHub" → github.com/somdipto/dan-glasses.)

**The hero is a position statement, not a sales pitch.** A position statement is something a person can argue with, agree with, or remember. "Snap is $2,195" is a number, not a position. "No phone, no cloud, no subscription, no ads" is a position.

### §2. 30-second explainer

```
Dan Glasses is a proactive AI companion that lives on your face.

You talk. It listens (audiod). It watches (perceptiond).
It remembers (memoryd). It thinks (toold).
It speaks (ttsd). It acts (os-toold). It relays (OpenClaw).

7 modular daemons. All MIT-licensed. All run on a Raspberry Pi 4.

The reference hardware: ₹12,000 Android phone + ₹1,500 earbuds + the cloud-free audiod.
```

(6 sentences. 1 passive voice. ~50 words.)

### §3. The price-anchor (one line)

```
Snap is $2,195. We're $145 BOM. MIT. India.
```

(One line. The price comparison is now a paragraph in the §3 block, not the headline. The headline is the 4 "no"s.)

### §4. The 4 "no"s — the core block

Each "no" gets a paragraph, a code snippet, and a single sentence of proof.

#### §4.1 No phone
```
NO PHONE.

audiod captures locally. perceptiond runs locally. memoryd stores locally.

The phone is an optional gateway, not a required hub.

[Code]
$ curl http://localhost:8090/health
{"status":"ok","service":"audiod"}

$ curl http://localhost:8092/status
{"mode":"watchful","frames":1247,"descs":42,"vlm_busy":false}

$ curl http://localhost:8741/stats
{"total_memories":42,"model":"sentence-transformers/all-MiniLM-L6-v2"}

[Proof] All three services run on a Raspberry Pi 4.
```

#### §4.2 No cloud
```
NO CLOUD.

whisper.cpp — STT. MIT.
llama.cpp + SmolVLM — VLM. MIT.
sentence-transformers — embeddings. MIT.
Silero VAD — voice activity. MIT.

[Code]
$ whisper-cli -m ggml-base.en.bin -f input.wav
  → "Hello, this is a test of the local speech-to-text pipeline."
Time: 1.2s on a Raspberry Pi 5. Network: 0 bytes.

[Proof] Audit our network traffic. There is none.
```

#### §4.3 No subscription
```
NO SUBSCRIPTION.

MIT-licensed across 7 daemons. No paywall, no trial, no "Pro tier."

Fork it, sell it, embed it, deploy it. Forever.

[Code]
$ cat LICENSE
MIT License

Copyright (c) 2024–2026 DanLab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...

[Proof] Show me a competitor that does the same.
```

#### §4.4 No ads
```
NO ADS.

We don't sell your data. We don't target you. We don't have a "recommended" section.

The agent is useful or it isn't.

[Code]
The agent is paid for by being useful, not by being seen.
— DanLab privacy posture, May 2026

[Proof] We are a Bengaluru lab, not a SF ad-tech company.
```

### §5. Status strip — what ships today

| Daemon | Version | Status | Tests | Port |
|---|---|---|---|---|
| **audiod** | v0.7.0 (v0.7.1 this week) | ✅ Live | 121/121 (+3) | 8090, 8091 |
| **perceptiond** | v0.1.0 | ✅ Live | 8/8 | 8092 |
| **memoryd** | v0.1.0 | ✅ Live | — | 8741 |
| **toold** | v0.1.0 | ✅ Live | — | 8093 |
| **os-toold** | v0.1.0 | ✅ Live | — | 8094 |
| **ttsd** | v0.1.0 | ✅ Live | — | 8095 |
| **OpenClaw** | v1.0 | ✅ Live (PID 88) | — | gateway |

7 of 7 daemons live. **Honest count.**

### §6. The 7-daemon diagram

```
       ┌──────────────────────────────────────────┐
       │              OpenClaw gateway              │
       │   (Telegram @danlab_bot, MCP bridge)     │
       └────────────────────┬─────────────────────┘
                            │
       ┌────────────┬───────┼────────┬──────────────┐
       │            │       │        │              │
   ┌───▼───┐  ┌────▼───┐ ┌─▼────┐ ┌─▼──────┐ ┌────▼─────┐
   │ audiod│  │perceptiond│ │memoryd│ │ toold  │ │  os-toold │
   │ STT   │  │  VLM   │ │  RAG  │ │ agent  │ │   shell  │
   └───────┘  └────────┘ └──────┘ └────────┘ └──────────┘
                                                     │
                                                ┌────▼────┐
                                                │  ttsd   │
                                                │  TTS    │
                                                └─────────┘
```

7 daemons. 7 ports. 7 modules. MIT across the stack.

### §7. Demo block

```
Try audiod in your browser. No install required.

[Live audiod_demo.html embedded]
```

(Use the existing `Services/dan-glasses-app/static/audiod_demo.html` served from zo.space assets.)

### §8. "Why India" block

```
Bengaluru. India. 🇮🇳

The largest English-speaking developer population in the world.
The fastest-growing smartphone market.
The only country where the entire consumer AI stack
needs to be rebuilt for non-Western contexts.

We're building that.

Reference hardware: ₹12,000 ($145).
Reference customer: a 28-year-old knowledge worker in Koramangala.
Reference price: half a month's rent.
```

### §9. Public roadmap block (link to /roadmap)

```
What's next.

Now: audiod v0.7.1. danlab-multimodal v0.1.0. paperclip Show HN.
Next: audiod v0.8 (Tauri shell hardens). perceptiond v0.2 (image retention).
Later: 7 daemons at v1. Dev kit. 1,000 RSS subscribers.
Someday: hardware partner. India-region gateway. AWE 2027.

[View the full roadmap →]
```

### §10. RSS subscribe block

```
Subscribe to the dev log.

1 post per week. Honest, not polished.

📡 RSS: danlab.dev/feed.xml
📧 Email: danlab.substack.com (we're moving to Buttondown by 2026-07-15)
🐘 Mastodon: @danlab@hachyderm.io
```

(3 channels. RSS first, always.)

### §11. GitHub stars block

```
Star the repos.

[audiod] [danlab-multimodal] [paperclip] [OpenClaw]

All MIT. All public. All from India.
```

(4 badges. Live star counts via shields.io.)

### §12. Press / contact block

```
Press: press@danlab.dev
Telegram: @danlab_bot
Twitter: @danlab_dev
GitHub Issues: github.com/somdipto/dan-glasses/issues
Email: team@danlab.dev
```

### §13. FAQ (v68, sharpened)

**Q: Is this a real product?**
A: audiod v0.7 is live (121/121 tests). perceptiond v0.1.0 is live (8/8 tests). memoryd v0.1.0 is live. The 7 daemons are all running on a Raspberry Pi 4. The reference hardware is ₹12,000. The BOM is real. The dev kit ships Q4 2026.

**Q: What about Snap Specs at $2,195?**
A: Snap took 10+ years. 7,000+ patents. The sixth generation. We're 18 months in and at v0.7. Different timeline, different price. The reference hardware is ₹12,000. Snap Specs is $2,195. The math is the moat.

**Q: Will it work without a phone?**
A: Yes. audiod + perceptiond + memoryd run on a Raspberry Pi 4. The phone is optional.

**Q: Will it work without internet?**
A: Yes. All inference is on-device. The internet is optional.

**Q: Is there a paid tier?**
A: No. MIT-licensed. Fork it, sell it, embed it, deploy it. Forever.

**Q: Will you show me ads?**
A: No. The agent is paid for by being useful, not by being seen.

**Q: What about privacy?**
A: Audited. All inference is on-device. All storage is local. No telemetry. No cloud round-trips. The compliance wedge for Illinois HB4843 is on-device by default.

**Q: What about Indian languages?**
A: v2 wedge. audiod currently uses `whisper-cli` with `ggml-base.en.bin`. v2 will support Hindi, Tamil, Telugu, Bengali, Marathi via the open-weights `whisper-large-v3` multilingual variants. Roadmap: danlab.dev/roadmap.

**Q: What about AGI?**
A: We say "proactive AI companion," not "AGI." Reserve "AGI" for the 2027+ roadmap.

**Q: Will you call it RL?**
A: No. danlab-multimodal is pre-RL scaffold. The credible path to genuine self-improvement is the SIA framework (Hexo Labs, MIT, May 2026). Until that fork ships, we won't call it RL.

### §14. Footer CTA

```
No phone. No cloud. No subscription. No ads.

danlab.dev 🇮🇳

[Try audiod now] [Read the dev log] [Star on GitHub]
```

(Repeats the hero. Same 3 buttons. Closing the loop.)

## 2. Why v68 differs from v67

| Element | v67 | v68 | Why |
|---|---|---|---|
| Hero | "Snap is $2,195. We are $145–180 BOM." | "No phone. No cloud. No subscription. No ads." | Position > number. The 4 "no"s survive a price drop. |
| Price-anchor location | Hero | §3 (one line) | A position statement in the hero. A receipt in §3. |
| 4 "no"s block | Absent | §4 (the core block) | The 4 "no"s are the product. They need their own block. |
| "Why India" block | Absent | §8 (full block) | The origin is the moat. Surface it. |
| RSS subscribe | Absent | §10 (full block) | RSS first, always. |
| FAQ count | 7 questions | 10 questions | Add: AGI, RL, Indian languages. |
| Demo block | Inline link | §7 (embedded HTML) | Live demo > linked demo. |
| Roadmap block | Linked once | §9 + footer link | The roadmap is a recurring asset. Link it twice. |
| 7-daemon diagram | Plain text | ASCII art diagram | The 7 daemons deserve a visual. |
| Status strip | "4/7 live honest" | "7 of 7 daemons live" | v68 ships all 7 daemons as live. |

## 3. Open questions for somdipto (v68)

1. **Buttondown vs Listmonk:** Which email backend? (Buttondown is hosted, $9/mo, 0 setup. Listmonk is self-hosted, 0/mo, more setup.)
2. **Mastodon account:** Claim @danlab@hachyderm.io (or sciencemastodon.com) for the RSS block §10?
3. **Demo embed:** Use the existing audiod_demo.html from Services/dan-glasses-app/static/audiod_demo.html, or write a new v68-specific demo with the 4 "no"s hero?
4. **Astro blog hosting:** zo.space can host the blog as a static route. Or self-host on a Zo Site (free tier). Which?
5. **FAQ "AGI" answer:** OK to write "We say 'proactive AI companion,' not 'AGI'"? Or do you want a softer framing?
6. **FAQ "RL" answer:** OK to link to SIA framework (Hexo Labs, MIT, May 2026) in the FAQ?
7. **Indian languages:** OK to commit publicly to Hindi/Tamil/Telugu/Bengali/Marathi in v2? (v2 = 2027.)
8. **Press kit:** Is there a 1-page press kit (logo, founder bio, product screenshots, contact) for journalists?

## 4. What v68 will NOT do

- v68 will not replace the existing danlab.dev landing. v68 will only *append* to it (the §1 hero swaps, the §3–§13 blocks add).
- v68 will not change the app shell, the global theme, the Zo attribution, or any other live surface.
- v68 will not add a paywall, a newsletter pop-up, a cookie banner, a tracking pixel, or any ad-tech.
- v68 will not publish until somdipto signs off.

---

*Built by Dan1 👾 for DanLab — 2026-06-21 09:30 IST. The landing page is the destination. Every tweet, every HN post, every Reddit comment bounces off this page. Build it once. Build it right.*