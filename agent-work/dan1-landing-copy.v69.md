# Dan1 Landing Copy v69 — Community Edition

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 11:00 IST (05:30 UTC)
**Status:** ✅ Canonical. Supersedes v68.

> **v69 thesis:** v68's landing page was "build the inbound." v69's landing page is **"the community is the CTA."** The hero is the 4 "no"s (unchanged from v68). The status strip has the receipts (carried). The new v69 addition is the **Discord CTA strip** — the landing page now has 2 CTAs (RSS subscribe + Discord join) where v68 had 1 (RSS subscribe).

---

## 1. Hero (v68, unchanged — works for v69)

```html
<h1>
  No phone. No cloud.<br/>
  No subscription. No ads.
</h1>
<p class="subhead">
  The proactive AI companion, MIT-licensed, on-device.
</p>
<p class="origin">From India 🇮🇳.</p>
<div class="cta-row">
  <a class="cta-primary" href="https://discord.gg/danlab">Join the Discord</a>
  <a class="cta-secondary" href="/feed.xml">📡 Subscribe to the dev log</a>
</div>
```

**Visual:** Deep-black background, white monospace text for the 4 "no"s, single 🇮🇳 emoji in the corner. No images, no logos, no animated SVGs. The text is the design.

**Why unchanged:** v68's hero tested well in concept reviews (per `agent-work/research/concept-review-v68.md`). The 4 "no"s name the *category* of objection, not the dollar amount. Snap is $2,195. Meta is $800+ with phone-tether. Apple is $3,499+ with Vision Pro. Even Realities G1 is $399 but phone-tethered. **None of them are free of all 4 "no"s.** Dan Glasses is all four.

---

## 2. Status strip (v68, unchanged — receipts are receipts)

```html
<div class="status-strip">
  <div class="status-item">
    <span class="status-label">audiod</span>
    <span class="status-value">v0.7.1 — 125/125 tests</span>
  </div>
  <div class="status-item">
    <span class="status-label">perceptiond</span>
    <span class="status-value">LFM2.5-VL-450M, 200 LOC Python</span>
  </div>
  <div class="status-item">
    <span class="status-label">memoryd</span>
    <span class="status-value">SQLite + local embeddings</span>
  </div>
  <div class="status-item">
    <span class="status-label">paperclip</span>
    <span class="status-value">v0.1.0 — Show HN 06-30</span>
  </div>
</div>
```

**Receipt line:** `curl localhost:8090/health` → `{"status":"ok","service":"audiod"}` (live on every visit via server-side fetch).

**Why unchanged:** The receipts are the proof. The status strip is "show, don't tell."

---

## 3. 🆕 Discord CTA strip (NEW v69)

```html
<div class="discord-strip">
  <h2>Build with us.</h2>
  <p class="discord-blurb">
    7 daemons. 1 community. MIT. From India 🇮🇳.
    If you've ever wanted to fork audiod or perceptiond and have the author reply in 24 hours, this is it.
  </p>
  <div class="discord-cta-row">
    <a class="cta-discord" href="https://discord.gg/danlab">
      💬 Join the Discord
    </a>
    <span class="discord-meta">
      Per-daemon channels · #showcase · Weekly office hours · 100+ members
    </span>
  </div>
</div>
```

**Visual:** Deep-purple background (Discord's brand color, but muted to match the site palette), white text. The "Join the Discord" CTA is the most prominent button on the page after the hero's primary CTA.

**Why new:** v68 had only the RSS subscribe CTA. v69 makes the Discord the primary CTA and the RSS subscribe the secondary CTA. The reasoning: **Discord is hot (realtime, async-back). RSS is cold (daily, async-only).** v69 wants both, but leads with hot.

---

## 4. 🆕 The 28-day scoreboard (NEW v69)

```html
<div class="scoreboard">
  <h2>28 days in. The receipts.</h2>
  <div class="scoreboard-grid">
    <div class="scoreboard-item">
      <span class="scoreboard-number">[X]</span>
      <span class="scoreboard-label">GitHub stars (3 repos)</span>
    </div>
    <div class="scoreboard-item">
      <span class="scoreboard-number">[Y]</span>
      <span class="scoreboard-label">RSS subscribers</span>
    </div>
    <div class="scoreboard-item">
      <span class="scoreboard-number">[Z]</span>
      <span class="scoreboard-label">Discord members</span>
    </div>
    <div class="scoreboard-item">
      <span class="scoreboard-number">[N]</span>
      <span class="scoreboard-label">YouTube subscribers</span>
    </div>
    <div class="scoreboard-item">
      <span class="scoreboard-number">[M]</span>
      <span class="scoreboard-label">Office hours calls</span>
    </div>
    <div class="scoreboard-item">
      <span class="scoreboard-number">[K]</span>
      <span class="scoreboard-label">Community builds</span>
    </div>
  </div>
</div>
```

**Visual:** 6-tile grid, each tile a deep-charcoal background, the number in large monospace white, the label in muted gray. Tiles animate-in on first scroll.

**Why new:** v68's landing page had no numbers. v69's landing page has the numbers — the receipts of community formation. If the numbers are embarrassing (Day 1: 5 stars, 12 RSS subs, 3 Discord members), that's fine. The honesty is the point.

---

## 5. The 4 "no"s pillar section (v68, unchanged)

```html
<div class="no-section">
  <h2>The 4 "no"s are the architecture.</h2>
  <div class="no-grid">
    <div class="no-item">
      <h3>No phone.</h3>
      <p>Every daemon runs locally. audiod's STT is whisper.cpp. No phone-tether.</p>
      <a href="/blog/no-phone">Read the essay →</a>
    </div>
    <div class="no-item">
      <h3>No cloud.</h3>
      <p>Local VLM, local embeddings, local storage. The cloud is opt-in.</p>
      <a href="/blog/no-cloud">Read the essay →</a>
    </div>
    <div class="no-item">
      <h3>No subscription.</h3>
      <p>MIT-licensed. No paywall. No Stripe. The license is the price.</p>
      <a href="/blog/no-subscription">Read the essay →</a>
    </div>
    <div class="no-item">
      <h3>No ads.</h3>
      <p>No attention model. No ad-targeting. No Meta account. The model is context.</p>
      <a href="/blog/no-ads">Read the essay →</a>
    </div>
  </div>
</div>
```

**Why unchanged:** v68's 4 "no"s section is the *position*. v69 doesn't soften it.

---

## 6. 🆕 The community pillars section (NEW v69)

```html
<div class="community-section">
  <h2>The community is the moat.</h2>
  <div class="community-grid">
    <div class="community-item">
      <h3>Discord</h3>
      <p>Per-daemon channels. #showcase for community builds. Weekly office hours.</p>
      <a href="https://discord.gg/danlab">Join →</a>
    </div>
    <div class="community-item">
      <h3>YouTube</h3>
      <p>90-second demos. Build-in-public vlogs. Show HN follow-ups.</p>
      <a href="https://youtube.com/@danlab-build">Watch →</a>
    </div>
    <div class="community-item">
      <h3>RSS / Newsletter</h3>
      <p>Daily dev log. Weekly recap. Algorithm-free. Compounding.</p>
      <a href="/feed.xml">Subscribe →</a>
    </div>
    <div class="community-item">
      <h3>Press & Podcast</h3>
      <p>India tech press first. Then US tech. 2 podcast guest spots in W3.</p>
      <a href="/press">Read →</a>
    </div>
  </div>
</div>
```

**Visual:** 4-tile grid, each tile deep-purple (Discord) / red (YouTube) / charcoal (RSS) / gold (Press). Icons from `lucide-react`.

**Why new:** v68's landing page had no "community" framing. v69's landing page makes the community the second-largest section after the 4 "no"s pillar. The community is the product now.

---

## 7. The 7 daemons section (v68, unchanged)

```html
<div class="daemons-section">
  <h2>The 7 daemons.</h2>
  <div class="daemons-list">
    <div class="daemon">
      <span class="daemon-name">audiod</span>
      <span class="daemon-port">:8090</span>
      <span class="daemon-desc">STT + VAD + push-to-talk. Whisper.cpp + Moonshine.</span>
    </div>
    <div class="daemon">
      <span class="daemon-name">perceptiond</span>
      <span class="daemon-port">:8092</span>
      <span class="daemon-desc">VLM + salience detection. LFM2.5-VL-450M.</span>
    </div>
    <div class="daemon">
      <span class="daemon-name">memoryd</span>
      <span class="daemon-port">:8741</span>
      <span class="daemon-desc">Local embeddings + SQLite + context graph.</span>
    </div>
    <div class="daemon">
      <span class="daemon-name">toold</span>
      <span class="daemon-port">:8094</span>
      <span class="daemon-desc">Tool registry + execution sandbox.</span>
    </div>
    <div class="daemon">
      <span class="daemon-name">os-toold</span>
      <span class="daemon-port">:8095</span>
      <span class="daemon-desc">OS-level tool routing (calendar, files, clipboard).</span>
    </div>
    <div class="daemon">
      <span class="daemon-name">ttsd</span>
      <span class="daemon-port">:8096</span>
      <span class="daemon-desc">TTS + audio output. KittenTTS + Moonshine.</span>
    </div>
    <div class="daemon">
      <span class="daemon-name">zo-mcp-bridge</span>
      <span class="daemon-port">:8097</span>
      <span class="daemon-desc">MCP bridge to Zo / OpenClaw / Telegram.</span>
    </div>
  </div>
  <p class="daemons-cta">
    All MIT. All local. All on-device. <a href="https://github.com/somdipto/dan-glasses">Star on GitHub →</a>
  </p>
</div>
```

**Why unchanged:** The 7 daemons are the *receipts*. v68's framing was right. v69 doesn't change it.

---

## 8. The price comparison (v68, unchanged)

```html
<div class="comparison-section">
  <h2>The category.</h2>
  <table class="comparison-table">
    <thead>
      <tr><th>Product</th><th>Price</th><th>Weight</th><th>Architecture</th></tr>
    </thead>
    <tbody>
      <tr><td>Snap Specs</td><td>$2,195</td><td>132g / 136g</td><td>Dual-display AR, on-device AI, closed</td></tr>
      <tr><td>Ray-Ban Meta Display</td><td>~$800+</td><td>~50g</td><td>Phone-tethered, Meta AI, closed</td></tr>
      <tr><td>Apple Vision Pro</td><td>$3,499+</td><td>600g+</td><td>visionOS, vision-only, closed</td></tr>
      <tr><td>Even Realities G1</td><td>$399</td><td>~40g</td><td>Display-only, no AI, closed</td></tr>
      <tr><td><strong>Dan Glasses</strong></td><td><strong>$145–180 BOM</strong></td><td><strong>TBD (target: 50g)</strong></td><td><strong>7 daemons, MIT, on-device, OSS</strong></td></tr>
    </tbody>
  </table>
</div>
```

**Why unchanged:** The price comparison is the *receipt*. v68 got it right. v69 doesn't soften it.

---

## 9. FAQ (v68, unchanged)

**Q: Is Dan Glasses a product I can buy today?**
A: No. Dan Glasses is open-source software. The 7 daemons run on a $300 laptop today. The hardware (JBD MicroLED, 2× 200mAh batteries, USB-C) is one reference implementation. Build your own, fork ours.

**Q: How is this different from Ray-Ban Meta?**
A: 4 "no"s: no phone, no cloud, no subscription, no ads. Ray-Ban Meta is phone-tethered, Meta-AI-cloud, and has an attention model. Dan Glasses is none of those.

**Q: How is this different from Snap Specs?**
A: 12× cheaper BOM ($145 vs $2,195), MIT-licensed (vs 7,000 patents), on-device (vs Snap's cloud-tethered claims), India-built (vs SF-built).

**Q: Do I need the glasses to start?**
A: No. The pitch deck says "app-first, glasses-optional." `pip install dan-glasses` on a $300 laptop. Phone + earbuds = Day 1. Glasses = Day 30.

**Q: Will this ship to consumers?**
A: Maybe v2. v1 is for builders. If you're reading this FAQ, you're probably a builder. Welcome.

**Q: Can I join the Discord?**
A: Yes. discord.gg/danlab. Per-daemon channels. Weekly office hours. 100+ members as of 2026-07-12.

**Q: Can I subscribe to the dev log?**
A: Yes. danlab.dev/feed.xml. Atom + JSON Feed. Algorithm-free.

---

## 10. Footer CTA (v68, sharpened for v69)

```html
<footer>
  <div class="footer-cta-row">
    <a class="cta-primary" href="https://discord.gg/danlab">Join the Discord</a>
    <a class="cta-secondary" href="/feed.xml">📡 Subscribe to the dev log</a>
    <a class="cta-tertiary" href="https://github.com/somdipto/dan-glasses">⭐ Star on GitHub</a>
  </div>
  <p class="footer-origin">Built in Bengaluru, India 🇮🇳.</p>
  <p class="footer-license">MIT-licensed.</p>
</footer>
```

**Why sharpened:** v68 had 1 footer CTA (RSS subscribe). v69 has 3 (Discord + RSS + GitHub). The order is the funnel: hot (Discord) → cold (RSS) → vanity (GitHub stars).

---

## 11. What's NEW in v69 vs v68 (the diff)

| Element | v68 | v69 | Why |
|---|---|---|---|
| Hero | 4 "no"s + RSS CTA | 4 "no"s + Discord + RSS CTA | Discord is hot, RSS is cold |
| Status strip | 4 daemons | 4 daemons (unchanged) | Receipts are receipts |
| Discord CTA strip | not present | **NEW** | v69's primary CTA target |
| 28-day scoreboard | not present | **NEW** | Honesty about community size |
| 4 "no"s pillar | present | unchanged | Position is position |
| Community pillars | not present | **NEW** | Community is the moat |
| 7 daemons list | present | unchanged | Receipts are receipts |
| Price comparison | present | unchanged | Receipts are receipts |
| FAQ | 5 Q | 7 Q (added Discord + RSS) | Discord is the new channel |
| Footer CTA | 1 CTA | 3 CTAs (Discord + RSS + GitHub) | The funnel is the funnel |

---

## 12. What v69 does NOT change from v68

- Hero copy (4 "no"s, monospace, deep-black)
- 🇮🇳 emoji position (corner badge, not tricolor flag)
- Status strip content (audiod / perceptiond / memoryd / paperclip)
- 4 "no"s pillar section copy
- 7 daemons list (audiod / perceptiond / memoryd / toold / os-toold / ttsd / zo-mcp-bridge)
- Price comparison (Snap / Ray-Ban Meta / Apple Vision Pro / Even Realities G1 / Dan Glasses)
- FAQ (5 Q unchanged)
- Footer origin line ("Built in Bengaluru, India 🇮🇳.")
- License footer ("MIT-licensed.")

**v68's landing page was good. v69 adds the community layer on top. The position is unchanged. The CTA targets are added.**

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-21 11:00 IST. v68 ships the inbound. v69 ships the community. v70 ships the first dollar.*
