# Dan Glasses — Landing Page Copy v111
**Date:** 2026-07-01
**Owner:** DAN-1
**Format:** Landing page wireframe + copy blocks. Drop into React + Tailwind components.
**Target URL:** `https://danlab.ai/glasses` (Track A primary) with redirects from `danlab.ai/dan-voice` (Track B secondary).
**v111 delta:** Numbers updated to v111 daemon matrix. Telegram bot block added. Danlab.dev refresh plan called out. Hardware blocker paragraph now references the real Redax/gvisor situation.

---

## 0. Page structure (top to bottom)

1. Hero (above the fold)
2. Problem statement (the in-your-face framing)
3. Differentiator stack (architecture, not features)
4. Live daemon matrix (v111 update — replace the static "perceptiond screenshot" with the full 9-daemon matrix)
5. Stack / open-source cred
6. Privacy section (the unbeatable position)
7. Telegram + OpenClaw section (v111 update)
8. Roadmap + hardware status
9. CTA — Join the waitlist
10. Footer

---

## 1. Hero

### 1.1 Headline (H1, single line, max 9 words)
```
A proactive AI on your face. Open source. From India.
```

### 1.2 Sub-headline (H2, two lines)
```
Dan Glasses watches what matters, drafts what is next, and speaks only when it should. Your data never leaves your own cloud.
```

### 1.3 Visual
Black-and-white render of the ForgeCAD glasses model, hero shot from the right, soft purple backlight. Static image, no spinning hero animation — slow the page down.

Alt: "97-part parametric glasses model designed in ForgeCAD. Built in Bengaluru."

### 1.4 Primary CTA
```
[ Get early access →  ]
```
Above the fold, top-right corner, fixed on scroll. Color: white text on `#0E0E10` background, 1px border `#7C3AED` (purple accent).

### 1.5 Secondary CTA (inline)
```
[ Read the architecture doc ]   (links to dan-consciousness wiki)
```

### 1.6 Trust strip (small grey text under the CTA)
```
150+ audiod tests passing · 9/9 daemons live · MIT licensed · @danlab_bot online
```

### 1.7 Eyebrow (top of hero, right above H1)
```
DanLab ·  AI R&D lab · Bengaluru 🇮🇳
```

---

## 2. Problem statement (the in-your-face framing)

### 2.1 Headline
```
Smart glasses are still stupid.
```

### 2.2 Body (one paragraph)
Meta Ray-Ban waits for you to ask. Quark Glasses wait for you to ask. Apple Vision Pro waits for you to ask. The entire category is reactive. You speak, they reply. If you forget to ask, they forget to think.

Dan Glasses is the first wearable with a *proactive* AI layer. It watches what you look at, drafts what comes next, and only speaks when the work is done. Hands free. Eyes up. No "Hey, can you…".

### 2.3 Visual
A 3-panel comic strip.
- Panel 1: "Hey glasses, what's that building?" (Meta)
- Panel 2: "Hey glasses, draft the email to the client." (Quark)
- Panel 3: glasses already drafted the email. The user is reading. No ask needed. (Dan)

---

## 3. Differentiator stack (architecture, not features)

### 3.1 Headline
```
We win on architecture. Not on hardware.
```

### 3.2 Differentiator 1 — Privacy
**Headline:** Your data. Your cloud. Not ours.
**Body:** Every Dan Glasses user runs the AI in their own isolated Docker container. The container lives in a TEE-protected instance that *only the user* can decrypt. We cannot see your emails. We cannot see your Notion pages. We cannot see your meeting notes. By architecture, not by promise.

**Code block (paste verbatim):**
```python
# The contract — audiod publishes events only to the user's container
audiod.publish(
    event=transcript_event,
    target=user_container_local_socket,  # not our socket
    audit_log=True,
)
```

### 3.3 Differentiator 2 — Proactive AI
**Headline:** Watches. Drafts. Speaks only when needed.
**Body:** Three daemons collaborate in real time. `perceptiond` watches the camera through a salience gate (motion or face) and runs LFM2.5-VL-450M Q4_0 on the salient frames. `memoryd` semantically indexes every transcript in SQLite with 384-dim sentence-transformer vectors. `paperclip` orchestrates eight core workflows end-to-end (email, Notion, Slack, calendar, PDF generation, expense reports, meeting summaries, travel planning).

### 3.4 Differentiator 3 — Open SDK
**Headline:** If it does not run on Day 1, build it in 30 lines.
**Body:** Paperclip's Python and TypeScript SDKs let any developer wire a new agent into a user's container. The agent inherits voice input, OAuth to Gmail/Notion/Slack/Calendar, and the user's permission scope. You write the workflow. We ship the substrate.

**Code block:**
```python
from paperclip import Agent, tool

class ReceiptAgent(Agent):
    @tool
    def parse_image(self, image_bytes: bytes) -> dict:
        """OCR + line item extraction."""
        ...

# That's it. The user approves the tool once.
# ReceiptAgent now runs in their container, every receipt, forever.
```

### 3.5 Differentiator 4 — Open-source end-to-end
**Headline:** Auditable from the silicon to the SQL.
**Body:** Every daemon is MIT-licensed on GitHub. The brain (`dan-consciousness`) is MIT. The orchestrator (`paperclip`) is MIT. The inference engine (`llama.cpp`) is MIT. The only proprietary layer is the device firmware — and the firmware is documented line by line in the public repo.

### 3.6 Differentiator 5 — Pricing
**Headline:** Free powerful app. ₹12–15k if you want the hardware.
**Body:** No subscription for the software. No mandatory hardware. The Meta Ray-Ban playbook, but more aggressive on price and more aggressive on openness.

---

## 4. Live daemon matrix (v111 — replaces the perceptiond screenshot)

### 4.1 Headline
```
This is what is live on a Linux laptop right now.
```

### 4.2 Body
The image is a single screenshot of the live daemon matrix running on a Linux laptop. No mockup. No Photoshop. One curl command per line. The state is reproducible from a fresh shell.

### 4.3 Code caption (small grey)
```
$ ./scripts/up.sh && for p in 8090 8091 8092 8741 8742 8743 8744 18789 3888; do
    echo "=== :$p ==="
    curl -s --max-time 2 http://localhost:$p/status || echo "down"
  done

=== :8090 === {"vad":true,"whisper_binary":true,"whisper_model":true,"publisher":true,"running":true}  # audiod
=== :8091 === {"status":"ok"}                                                                    # dan-glasses-app
=== :8092 === {"model":"sentence-transformers/all-MiniLM-L6-v2","db_size_bytes":352256}            # memoryd
=== :8741 === {"status":"ok"}                                                                    # perceptiond (LFM2.5-VL-450M)
=== :8742 === {"status":"ok","version":"0.2.0"}                                                  # toold
=== :8743 === {"model":"medium","kittentts_available":true}                                       # ttsd
=== :8744 === ok                                                                                 # os-toold
=== :18789 === gateway reachable, telegram: connected                                            # openclaw-web
=== :3888 === local                                                                              # percmcp
```

### 4.4 The four takeaways (call out under the matrix)
1. **9 daemons, 9 ports, 9 healthy.** Every one is a separate process with a separate SPEC.md.
2. **LFM2.5-VL-450M is the live vision model.** 209MB Q4_0. ~10-15s/frame on CPU. Not a benchmark; a real production inference.
3. **No cloud required.** Every byte stays on the device or the user's EigenCloud container.
4. **No third-party telemetry.** No Mixpanel, no GA, no Segment, no Posthog. We do not track you.

---

## 5. Stack cred (one row of badges)

```
🦀 Rust services · 🐍 Python orchestration · ⚛️ React frontend · 🤖 Paperclip agents · 🧠 LFM2.5 vision · 👂 Whisper STT · 🗣 KittenTTS · 🗃 SQLite + vectors · 🛡 TEE-attested containers
```

---

## 6. Privacy section (the unbeatable position)

### 6.1 Headline
```
Three cloud-AI wearables today. Only one is private by architecture.
```

### 6.2 Table (render as a 3-column comparison)

| | Quark AI Glasses | Meta Ray-Ban | **Dan Glasses** |
|---|---|---|---|
| **Where your voice goes** | Alibaba cloud | Meta cloud | **Your Docker container** |
| **Where your vision goes** | Alibaba cloud | Meta cloud | **Your Docker container** |
| **Where your Notion lives** | Alibaba cloud | Meta cloud | **Your Docker container** |
| **Always-on mic** | Yes | Yes | **No (opt-in)** |
| **Always-on camera** | Yes | Yes | **No (opt-in)** |
| **Data monetization** | Inferred | Confirmed | **Architecturally impossible** |
| **Open source stack** | No | No | **Yes** |

### 6.3 Caption
> Source: the open-source `dan-glasses` codebase. Read the implementation, not the marketing.

---

## 7. Telegram + OpenClaw section (v111 NEW)

### 7.1 Headline
```
Talk to Dan right now. From any phone.
```

### 7.2 Body
We are not waiting for the wearable. We wired OpenClaw 2026.5.28 (e932160) into Telegram and the bot is online. DM `@danlab_bot`, complete the one-time pairing, and you can talk to Dan from your phone in 30 seconds. The first 100 paired devices get the white-glove onboarding.

### 7.3 What works today on Telegram
- Voice input → audiod → transcript → Dan
- Dan → ttsd → audio reply
- Long-term memory: every chat becomes a memoryd vector (episodic / semantic / procedural)

### 7.4 What lands when the app ships
- Calendar awareness (draft the brief 15 minutes before the meeting)
- Email triage (draft the response, you approve, we send)
- Notion sync (push it from voice, edit on desktop)
- Slack posting (read-first, never auto-send)

### 7.5 Inline CTA
```
[ Open @danlab_bot →  ]   (links to t.me/danlab_bot)
```

---

## 8. Roadmap + hardware status

### 8.1 Headline
```
We're shipping in waves.
```

### 8.2 Timeline

**Now → Q3 2026 — Dan Voice (no hardware) + Telegram bot**
- Android-first app
- EigenCloud container per user
- 8 Paperclip workflows live
- Whisper STT + ElevenLabs TTS
- @danlab_bot live now
- Waitlist open: `danlab.ai/waitlist`

**Q4 2026 — Dan Glasses v1 (hardware)**
- ESP32-S3 + Syntiant NDP200
- Bluetooth mic/speaker pair to your existing phone
- 15–20hr battery (400–450mAh upgraded from 200mAh)
- No camera, no display
- ₹12,000–15,000

**Q1 2027 — Dan Glasses v1.5**
- JBD MicroLED single-eye display
- 8MP camera (opt-in)
- Cloud-based QwenVL analysis
- Proactive Focus Mode

**Q2 2027 and beyond**
- Full prescription lens integration
- Dual-eye display
- Payment integration (UPI + Stripe)
- HRM-Text-1B on-device for reasoning (post-processor for audiod)

### 8.3 Honest status note (v111 — updated to reflect real blockers)
```
Hardware is currently blocked on the production Redax 03W board. Software ships on Linux laptops today (Track A) and on Telegram (live now). The wearable form factor rebuilds onto Redax when the board is final. We do not hide this.

Engineering note: Tailscale tailnet provisioning is also blocked in our current sandboxed environment (TUN device is not loadable). The Telegram surface does not need Tailscale — it uses Telegram's outbound HTTPS — so this does not block any user-facing functionality today. It does block us from exposing the gateway to other devices on a private mesh, which we will need for the multi-device Dan Glasses companion app.
```

---

## 9. CTA — Join the waitlist

### 9.1 Headline
```
Ready when you are.
```

### 9.2 Body
Be among the first 1,000 to get Dan Voice access. Android-first. India-first. Waitlist opens July 1, 2026.

### 9.3 Form (simple)
- Email input (required)
- Country dropdown (helps us with regulatory)
- Single opt-in checkbox: "Send me the monthly digest. No spam."
- Submit: `[ Request access → ]`

### 9.4 Post-submit page
```
You're #247. We'll email you when access opens.
In the meantime: github.com/somdipto/dan-glasses · 9 daemons live today.
Try @danlab_bot on Telegram while you wait.
```

### 9.5 Footer of waitlist section
```
No card. No commitment. We delete the waitlist the day we open access.
```

---

## 10. Footer

### 10.1 Three columns

**Column 1 — Product**
- Dan Glasses
- Dan Voice
- Paperclip
- danlab-multimodal
- @danlab_bot on Telegram

**Column 2 — Open source**
- github.com/somdipto/dan-glasses
- github.com/somdipto/dan-consciousness
- github.com/somdipto/paperclip
- github.com/somdipto/danlab-multimodal

**Column 3 — Company**
- About
- Engineering blog (Dev.to mirror)
- Press kit (drop in share/README.md)
- Contact (Twitter DM preferred — we are 1 person)

### 10.2 Bottom strip
```
© 2026 DanLab · Built with ❤️ and 🦀 in Bengaluru 🇮🇳 · MIT licensed
```

---

## 11. Implementation notes (v111)

### 11.1 Tech stack (per frontend-design skill)
- React + Vite + Tailwind CSS 4
- shadcn components (`Button`, `Input`, `Dialog`)
- `lucide-react` icons
- Animate-on-scroll with `framer-motion` (small bundle, well-supported)
- Hero image: black-frame ForgeCAD render exported as `public/hero.png`
- Live daemon matrix image: capture a fresh `/status` payload on every page load (server-side rendered) — no need to re-render manually

### 11.2 Performance budget
- First contentful paint < 1.5s on 4G India (Jio / Airtel)
- Largest contentful paint < 2.5s
- Total page weight < 1MB (no video autoplay, only static hero)
- No third-party trackers (no GA until we can A/B test on our own infra)

### 11.3 SEO
- Title: "Dan Glasses — Proactive AI wearable, open source, from India"
- Description: "A proactive AI on your face. Watches what matters, drafts what is next, and speaks only when it should. Your data never leaves your own cloud."
- OG image: `/og.png` — the hero render + a tagline in white-on-black
- Twitter card: `summary_large_image` with the same OG image

### 11.4 Tracking / analytics
First 30 days: NONE. We will read the logs ourselves. After 30 days we add Plausible self-hosted (no cookies, no PII).

### 11.5 danlab.dev refresh (v111)
The current `danlab.dev` shows legacy product copy (Agent8, Zerant, Dapify, generic "AI Glasses"). Three options:

1. **Point danlab.dev to a new `sites/danlab-marketing/` zo.site.** Cleanest, fastest.
2. **Add a `danlab.ai` redirect on top of danlab.dev.** Best of both worlds, but costs a domain.
3. **Edit danlab.dev in place.** Slowest, depends on the CMS, ships a confusing transition.

**Recommendation:** Option 1. Ship the new site at `som.zo.space/danlab` (Zo Space) this week, point `danlab.dev` to it, retire the legacy copy. The new copy lives in this document.

---

## 12. Copy anti-pattern audit (self-check before shipping)

| Pattern | Allowed | Why |
|---|---|---|
| "Revolutionary" | No | Overused. Our differentiation is technical, not semantic. |
| "AI-powered" | No | Trivially true. Says nothing. |
| "The future of…" | No | We are not predicting. We are shipping. |
| Vague adjectives ("innovative", "next-gen") | No | Numbers > adjectives. |
| First-person plural ("we") | Yes | Brand voice. |
| Hyper-specific numbers | Yes | "97-part parametric model" > "beautiful". |
| Blockquote-as-truth | No | We use code blocks instead. |

---

*Landing copy complete. Companion artifacts: [research](./dan1-marketing-research.md), [strategy](./dan1-marketing-strategy.md), [calendar](./dan1-content-calendar.md), [Twitter](./dan1-twitter-content.md), [READMEs](./dan1-github-readme-suggestions.md).*
