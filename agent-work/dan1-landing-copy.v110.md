# Dan Glasses — Landing Page Copy v110
**Date:** 2026-06-29
**Owner:** DAN-1
**Format:** Landing page wireframe + copy blocks. Drop into React + Tailwind components.
**Target URL:** `https://danlab.ai/glasses` (Track A primary) with redirects from `danlab.ai/dan-voice` (Track B secondary).

---

## 0. Page structure (top to bottom)

1. Hero (above the fold)
2. Problem statement (the in-your-face framing)
3. Differentiator stack (architecture, not features)
4. Live demo (perceptiond dashboard screenshot)
5. Stack / open-source cred
6. Privacy section (the unbeatable position)
7. Roadmap + hardware status
8. CTA — Join the waitlist
9. Footer

Approx scroll depth at each break: 100vh / 80vh / 120vh / 100vh / 100vh / 100vh / 120vh / 50vh.

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
137+ tests passing · 9 daemons live · MIT licensed · github.com/somdipto/dan-glasses
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
**Body:** Three daemons collaborate in real time. `perceptiond` watches the camera through a salience gate (motion or face). `memoryd` semantically indexes every transcript. `paperclip` orchestrates eight core workflows end-to-end (email, Notion, Slack, calendar, PDF generation, expense reports, meeting summaries, travel planning).

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

## 4. Live demo — Perceptiond dashboard

### 4.1 Headline
```
This is what the daemon sees.
```

### 4.2 Body
A real screenshot of the VisionDashboard panel from `dan-glasses-app`. Capture every 2 seconds. Show one salient event arriving per minute on average. No narration. The number on screen (event count) is real.

### 4.3 Code caption (small grey)
```
$ curl localhost:8092/status
{"mode": "watchful", "frames": 1247, "salient": 23, "descs": 21, "vlm_busy": false, "queue_depth": 0}
```

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

## 7. Roadmap + hardware status

### 7.1 Headline
```
We're shipping in waves.
```

### 7.2 Timeline

**Now → Q3 2026 — Dan Voice (no hardware)**
- Android-first app
- EigenCloud container per user
- 8 Paperclip workflows live
- Whisper STT + ElevenLabs TTS
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
- REDAX 03W board for offline heavy tasks

### 7.3 Honest status note
```
Hardware is currently blocked on the Redax 03W board. Software ships on Linux laptops today (Track A). The wearable form factor rebuilds onto Redax when the board is final. We do not hide this.
```

---

## 8. CTA — Join the waitlist

### 8.1 Headline
```
Ready when you are.
```

### 8.2 Body
Be among the first 1,000 to get Dan Voice access. Android-first. India-first. Waitlist opens July 1, 2026.

### 8.3 Form (simple)
- Email input (required)
- Country dropdown (helps us with regulatory)
- Single opt-in checkbox: "Send me the monthly digest. No spam."
- Submit: `[ Request access → ]`

### 8.4 Post-submit page
```
You're #247. We'll email you when access opens.
In the meantime: github.com/somdipto/dan-glasses · 9 daemons live today.
```

### 8.5 Footer of waitlist section
```
No card. No commitment. We delete the waitlist the day we open access.
```

---

## 9. Footer

### 9.1 Three columns

**Column 1 — Product**
- Dan Glasses
- Dan Voice
- Paperclip
- danlab-multimodal

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

### 9.2 Bottom strip
```
© 2026 DanLab · Built with ❤️ and 🦀 in Bengaluru 🇮🇳 · MIT licensed
```

---

## 10. Implementation notes

### 10.1 Tech stack (per frontend-design skill)
- React + Vite + Tailwind CSS 4
- shadcn components (`Button`, `Input`, `Dialog`)
- `lucide-react` icons
- Animate-on-scroll with `framer-motion` (small bundle, well-supported)
- Hero image: black-frame ForgeCAD render exported as `public/hero.png`

### 10.2 Performance budget
- First contentful paint < 1.5s on 4G India (Jio / Airtel)
- Largest contentful paint < 2.5s
- Total page weight < 1MB (no video autoplay, only static hero)
- No third-party trackers (no GA until we can A/B test on our own infra)

### 10.3 SEO
- Title: "Dan Glasses — Proactive AI wearable, open source, from India"
- Description: "A proactive AI on your face. Watches what matters, drafts what is next, and speaks only when it should. Your data never leaves your own cloud."
- OG image: `/og.png` — the hero render + a tagline in white-on-black
- Twitter card: `summary_large_image` with the same OG image

### 10.4 Tracking / analytics
First 30 days: NONE. We will read the logs ourselves. After 30 days we add Plausible self-hosted (no cookies, no PII).

---

## 11. Copy anti-pattern audit (self-check before shipping)

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

*Landing copy complete. Companion artifacts: [research](./dan1-marketing-research.v110.md), [strategy](./dan1-marketing-strategy.v110.md), [calendar](./dan1-content-calendar.v110.md), [Twitter](./dan1-twitter-content.v110.md), [READMEs](./dan1-github-readme-suggestions.v110.md).*
