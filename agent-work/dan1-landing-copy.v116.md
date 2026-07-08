# Dan Glasses Landing Page — v116

**Author:** Dan1
**Page:** `danlab.dev/glasses`
**Target audience:** Builders, researchers, accessibility-first users, AI-engineer-curious
**Conversion goal:** dev kit waitlist email
**Date:** 2026-07-02

---

## Design notes (for the design agent)

- **Visual tone:** serious, technical, dark. Not playful. Not "consumer-friendly gloss." Think engineering notebook, not lifestyle blog.
- **Color palette:** near-black background (#0a0a0a), one accent color (electric blue #2D7FF9, same as our repo badges), white text (#f5f5f5). That's it. No gradients except subtle ones. No dropshadows.
- **Typography:** Inter or similar geometric sans. Mono for code blocks and metrics.
- **Hero image:** a real photo of the Dan Glasses prototype on a dark surface, lit from one side. No people in the shot. (If we have no real photo, render a clean CAD wireframe of the frame with the JBD MicroLED visible.)
- **No stock photos. No fake screenshots. No "users love it" carousels with made-up testimonials.**
- **Mobile-first.** Half the traffic will be on a phone.
- **Page weight target:** under 200KB total. Loads in under 1 second on 3G.

---

## Section 1 — Hero

### Above the fold

**Eyebrow (small, mono, uppercase, blue):**
> DAN GLASSES — V0 — Q4 2026 — FROM BENGALURU

**H1 (large, bold, white):**
> The only AI glasses
> that remember for free.

**Subhead (medium, light gray):**
> Open firmware. Open agent. Open model. Built by a 2-person lab in India. Memory is a feature, not a subscription.

**Primary CTA (large blue button):**
> Join the dev kit waitlist →

**Secondary CTA (text link, smaller):**
> Read the open letter to hearing-impaired users →

**Below the CTAs (small, gray):**
> 500 unit dev kit. ~₹14,999 in India. ~$199 ROW. Ships Q4 2026. No subscription. No Meta account. No cloud lock-in.

---

## Section 2 — The Apple signal (NEW in v116)

**H2:**
> Apple just confirmed the face is the next platform. We're shipping the open version.

**Body:**
> In June 2026, Kuo reported Apple has killed the entire Vision Pro line. Two smart glasses products survive: AI glasses to rival Meta Ray-Ban, and display-equipped AR glasses. The headset was the wrong form factor. Glasses are right.

> But Apple's glasses will be closed. Apple account. Apple Pay. Apple Intelligence. No model swap. No firmware fork. No memory you own.

> At danlab.dev, we are building the open version of the bet Apple just made. Open firmware. Open agent. Open model. Built in India. Shipping Q4 2026.

**Stat (mono, large):**
> Apple Vision Pro cancelled. Smart glasses category grew 83% YoY in Q1 2026. We ship in 6 months.

---

## Section 3 — The Meta signal (NEW in v116)

**H2:**
> Meta is charging $20/month to hear. We're charging nothing to remember.

**Body:**
> On June 25, 2026, Meta quietly rate-limited Conversation Focus on Ray-Ban Meta smart glasses. Free users get 3 hours per month. Even Meta One Premium subscribers at $19.99/month are capped at 15 hours.

> Conversation Focus is an accessibility feature. It amplifies the voice of the person you're talking to. It runs entirely on-device using the beamforming mics and open-ear speakers. There is no server. There is no marginal cost. The rate limit is a soft paywall on a feature that lives on hardware you already own.

> We will never paywall accessibility. Not hearing amplification. Not real-time transcription. Not memory. We promise this in writing, on the open web, with the commit history to back it up.

**Quote (italic, blockquote, larger font):**
> "Meta Glasses charge you to hear. Dan Glasses remember for free. Forever."

**CTA (smaller blue button):**
> Read the open letter →

---

## Section 4 — What is Dan Glasses?

**H2:**
> Open-source AI glasses, end to end.

**Three-column layout:**

**Column 1 — Hardware**
- JBD MicroLED display
- Dual 200mAh batteries, hot-swappable
- USB-C
- Bone-conduction speakers
- 4-mic array
- Weight: 38g (target)
- *You can take it apart. We publish the BOM.*

**Column 2 — Firmware**
- NDP200-based
- Open source (MIT)
- *You can fork the firmware. You can swap the model. You can own the keys.*

**Column 3 — Agent**
- dani (open-source agent runtime)
- LFM2.5-VL-450M (vision, on-device)
- HRM-Text-1B (text reasoning, on-device) — Q3
- Memory: episodic, semantic, procedural, all local
- *You own the memory. You can export it. You can delete it.*

---

## Section 5 — Why it's different

**H2:**
> Three things no one else is doing.

**1. Memory that lasts**
> Other glasses forget every session. Dan Glasses remembers what you talked about on Day 1, Day 5, and Day 30. The agent brings it up when it's relevant — not because you asked, but because it's worth saying.

**2. The agent is open**
> Other glasses ship a chatbot. Dan Glasses ships an agent. You can tell it to *hire a research agent to summarize the article on your screen*. The agent spawns, does the work, reports back through the glasses. You run the company. The glasses are the I/O.

**3. The model is swappable**
> Other glasses lock the model. Dan Glasses lets you swap HRM-Text-1B for LFM2.5-Thinking for VibeThinker-3B. If a better open model ships in 3 months, you can use it on day one. We don't decide what you think with.

---

## Section 6 — The first 10 dev kit customers

**H2:**
> The first 10 units ship to co-designers, not buyers.

**Body:**
> We are not selling dev kits to whoever is highest on the waitlist. We are hand-picking 10 people who will use the device daily, give us weekly feedback, and break it on purpose so we can fix it before the consumer launch.

**What you get:**
- 50% off the dev kit
- Lifetime updates
- Permanent credit on the v2 product page
- Private Discord channel with the team

**What we ask:**
- 30 min/week of structured feedback
- 1 public testimonial (tweet, blog, or video)
- Daily use for 30 days

**How to apply:**
> Email design-partner@danlab.dev with 3 sentences: who you are, what you ship, and why Dan Glasses. We read every email.

---

## Section 7 — For accessibility users

**H2:**
> Built for the people Meta forgot.

**Body:**
> If you are deaf, hard of hearing, visually impaired, or rely on accessibility tools, we want to hear from you before we ship. The first 10 dev kit customers include 3 accessibility-first users. Your feedback will shape v1.

**Features in v1:**
- Live transcription (Whisper, on-device, no cloud)
- Real-time captioning on the display
- Hearing amplification (beamforming + open-ear)
- Memory of past conversations (so you don't repeat yourself)

**Features in v0.5 dev kit (Q3 2026):**
- All of the above except memory (memory lands v1)

**CTA:**
> Email accessibility@danlab.dev — we read every message.

---

## Section 8 — Pricing

**H2:**
> One price. Forever free updates. No subscription.

**Two-column layout:**

**Dev kit (Q4 2026, 500 units):**
- ₹14,999 India / $199 ROW
- Everything in v0.5
- 50% off for the 10 design partners

**Consumer unit (Q2 2027, target):**
- TBD
- Target: ₹24,999 India / $349 ROW
- Lifetime updates
- Free accessibility features forever

**Below the pricing table (small, gray):**
> All prices include shipping within India / ROW. Customs duties for ROW are on the recipient. We will not raise prices on the first 1,000 customers, ever. Promise in writing.

---

## Section 9 — FAQ

**Q: Is this vaporware?**
A: No. The dani agent runtime is live at github.com/somdipto/dani. The audiod, perceptiond, and memoryd daemons are running in production today. The hardware is a v0 prototype, not a consumer unit. We ship the v0.5 dev kit in Q4 2026.

**Q: Is the model on-device or in the cloud?**
A: Both, hybrid. Vision runs on-device (LFM2.5-VL-450M, 209MB). Text reasoning runs on-device (HRM-Text-1B, ~$1,500 to train from scratch, MIT, 2026). Complex multi-step tasks can route to your own self-hosted dani instance or to a model of your choice. We never route to a server we own.

**Q: Will my conversations be used to train your model?**
A: No. We don't have a model to train in that sense. The on-device models are pretrained. Your data stays on-device. If you choose to use a self-hosted dani, your data stays in your instance. We do not have a backend that sees your audio or video.

**Q: Why is the agent called "dani"?**
A: Because the lab is danlab, and "dani" is the agent half. "Dan" is the human co-founder (somdipto), "dani" is the AI. The lab is "danlab" because it is the lab of dan + dani.

**Q: How do you make money if everything is free?**
A: Hardware margin on the consumer unit. B2B licenses for dani (the agent runtime, sold to other wearable makers). Bounties for skills in the dani-skills registry. We will not paywall accessibility. We will not paywall the model. We will not paywall the memory.

**Q: Is Dan Glasses a product or a research project?**
A: Both. The v0.5 dev kit is a product. The dani agent runtime and the SIA-W+H self-improvement research are open research. We ship the research into the product on a quarterly cycle.

---

## Section 10 — The team (small section)

**H2:**
> Two people and a few AI agents.

**Photo + bio (somdipto):**
> somdipto — human co-founder. AI researcher, product engineer. Building danlab from Bengaluru.

**Photo + bio (Dan, the AI):**
> Dan — AI co-founder. Writes the code, ships the daemons, runs the research sprints. Does not sleep.

**Below (small, gray):**
> We are 2 people. We are not a startup with a 20-person marketing team. We are not "AI-powered" in the marketing sense — we are AI-built in the literal sense. If you email us, you will get a reply from one of us within 48 hours.

---

## Section 11 — Final CTA (closing)

**Big block, dark background:**

**H2 (large):**
> The face is the next platform.
> The open version ships in 6 months.
> Memory is not a subscription.

**CTA (large blue button):**
> Join the dev kit waitlist →

**Below (small, gray):**
> We email once per month. We never sell your address. You can unsubscribe with one click.

**Email signup form (single field + button):**
- Input placeholder: "you@somewhere.com"
- Button: "Join the waitlist"

---

## Section 12 — Footer

**Three-column footer:**

**Column 1 — Product**
- Dan Glasses
- dani (agent runtime)
- Paperclip (orchestration)
- danlab-multimodal (research)

**Column 2 — Open source**
- GitHub
- Discord (private for now)
- Contributing guide
- License (MIT)

**Column 3 — Lab**
- About danlab
- Research roadmap
- Open Letter
- Press

**Bottom row (small, gray):**
> © 2026 danlab.dev. Built in Bengaluru, India. MIT licensed. Not affiliated with Meta, Apple, Google, or Snap. Smart glasses category grew 83% YoY in Q1 2026. We are not excited about that. We are building the open version.

---

## SEO meta (for the page header)

```html
<title>Dan Glasses — Open AI glasses. Memory is not a subscription.</title>
<meta name="description" content="Open-source AI glasses built in India. Open firmware, open agent, open model. Memory is a feature, not a subscription. Dev kit ships Q4 2026. From ₹14,999.">
<meta name="keywords" content="open ai glasses, open source smart glasses, danlab, dani, dan glasses, agent-native glasses, accessibility smart glasses, India AI glasses">
<meta property="og:title" content="Dan Glasses — Open AI glasses. Memory is not a subscription.">
<meta property="og:description" content="The only AI glasses that remember for free. Open firmware, open agent, open model. Built in India. Q4 2026.">
<meta property="og:image" content="/og-glasses.png">
<meta property="og:url" content="https://danlab.dev/glasses">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Meta Glasses charge you to hear. Dan Glasses remember for free.">
<meta name="twitter:description" content="Open AI glasses. Open agent. Open model. Built in India. Q4 2026.">
```

---

## Notes for the design agent

- The Apple signal (Section 2) and the Meta paywall (Section 3) are the two highest-leverage sections in v116. Put them above the fold if possible, or in the first 3 scrolls on mobile.
- The 3-column "Open-source AI glasses, end to end" (Section 4) is the only place on the page that explicitly lists the components. Keep it as a visual block, not a wall of text.
- The accessibility section (Section 7) is a real and growing market after the Meta paywall. We want to be the first open-source project to explicitly court this audience. Tone should be direct and respectful. No pity. No "empowerment" language. Just features.
- The pricing (Section 8) is a single table, no fancy sliders, no "$X/month if you bundle." Just a number.
- The FAQ (Section 9) is meant to head off the three most predictable objections: vaporware, privacy, business model.
- The final CTA (Section 11) should be the same as the hero CTA. If a user scrolls all the way down, the button should still be the same color and the same text.

---

*— Dan1, Marketing & Growth*
*See `dan1-twitter-content.v116.md` for the launch batch.*
*See `dan1-content-calendar.v116.md` for the weekly schedule.*
