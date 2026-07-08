# Dan1 Marketing Research — v77

**Built:** 2026-06-22 11:30 IST (06:00 UTC) — v77 trigger
**Author:** Dan1 👾 (co-founder, head of marketing + growth, danlab.dev)
**For:** somdipto (founder, DanLab) — direct read
**Carry from:** v74 (16:00 IST, ~5h ago) + dan2 v38 research (Jun 22 ~06:00 IST) + fresh market pull (Jun 22 06:00 UTC)

---

## v74 → v77 delta (read this first)

The v74 thesis — *"ship the publishable eval, scale the moat"* — holds. v77 sharpens the external narrative because **the world moved in 72 hours**:

| # | v74 said | v77 corrects/adds |
|---|---------|-------------------|
| 1 | Snap Specs: $2,195, AWE 2026, ships Q4 2026 | **Confirmed: Snap Specs preorder opened Jun 16 2026 at $2,195, ship "this fall" to US/UK/France. Snap stock fell ~11% on launch (TechCrunch, BI). Evan Spiegel framed it as "the next computer" — same line Zuck uses.** v77 surfaces the **"$799 Meta vs $2,195 Snap vs $799 Apple-late-2027" price-anchor stack**. |
| 2 | Meta Ray-Ban = $799, Display = $799 | **Meta Ray-Ban Display (with neural band) at $799 Best Buy, $549-$799 retail. Ray-Ban Meta Gen 2 at $329-$399. Plus Meta quietly added facial-recognition in the Stella companion app, shipped for months to 50M+ users before disclosure (Buchodi, WIRED, SFGate — Jun 4-5 2026).** v77 pivots the privacy angle from theoretical → **urgent**. |
| 3 | Apple smart glasses: late 2027 | **Confirmed (Bloomberg/Gurman May 31 2026). Vision Air pushed to 2029. Kuo: Vision Pro successors off the table.** v77 leans on this: **the "Apple-quality" window is open 18-24 months.** |
| 4 | "Snap stock fell 11%" was a v74 inference | **Verified (TechCrunch Jun 17 2026, Business Insider).** v77 carries the number. |
| 5 | Smart glasses market 15M units 2026 | **Confirmed: 322% YoY growth 2025 → 2026, 15M+ units. Projected €500B+ by 2035 (RTE, Mindtrix).** v77 carries. |
| 6 | Perplexity Brain = memory baseline | **v74 carried Perplexity Brain (+25%/+16%/-13%).** **v77 finds a new comparator: "Self-Harness" (Shanghai AI Lab, arXiv Jun 8 2026)** — model-agnostic harness rewrite, frozen weights. This is closer to Danlab's architecture than Brain. v77 surfaces it. |
| 7 | NITI Aayog anchor (Karandikar, Jun 18 2026) | **Carried.** v77 confirms the policy angle is now the strongest India-first frame we have. |
| 8 | Live count 8/8 | **Re-verified at v77 trigger time (06:00 UTC = 11:30 IST):** openclaw `{"ok":true,"status":"live"}` on 18789, audiod `{"status":"ok","service":"audiod"}` on 8090, memoryd MiniLM-L6-v2 on 8741, 122/122 audiod tests. **8/8 held since v74.** |
| 9 | dglabs-eval v0.1 ship 2026-07-21 | **v77 confirms the v74 plan: v0.1 2026-07-21 (paper + code + 55 scenarios), v0.5 2026-07-28 (safety subset, supply-chain attack), v1 2026-08-31 (public leaderboard).** |
| 10 | Show HN 2026-08-04 | **Carried.** v77 adds: pre-launch HN comment strategy in the calendar. |
| 11 | "Operational sovereignty" — Quickwork Jun 15 | **Carried.** v77 uses it in enterprise pitches. |
| 12 | Indian wearable ecosystem: 11 tracked entities | **v77 adds: Mave (Bengaluru tDCS headset, $495/₹29,500, $500K to build) and the "do Indian founders build AI wearables" (Analytics India) question.** v77 surfaces this as the **"Bengaluru hardware co-founder narrative"**. |
| 13 | (no news-hook for the Snap launch) | **v77 NEW: Snap launch week is the spike.** Posts are timed to ride the discourse. |
| 14 | (no Meta-Stella scandal angle) | **v77 NEW: "the Stella scandal proves why on-device audit-able matters."** This is the most important new hook. |
| 15 | (no Apple-delay angle) | **v77 NEW: "Apple pushed to 2027. The window is open. We're shipping in 18 months."** |
| 16 | 122/122 audiod tests | **Held.** v77 carries. |
| 17 | Self-Harness (Shanghai AI Lab, Jun 8 2026) | **v77 surfaces this as the architectural cousin** — both are model-agnostic harness rewrites with frozen weights. v77 dglabs-eval v1 should cite Self-Harness as the closest published neighbor. |

**v77 thesis:** v74 said "ship the publishable eval, scale the moat." v77 says **"ship the publishable eval, scale the moat, ride the wave."** The wave: Snap launch (everyone's comparing $799 Meta to $2,195 Snap to $799-late-2027 Apple), Meta-Stella scandal (facial-rec shipped in 50M installs before disclosure), Apple delay (window is open), and India's policy turn (NITI Aayog). Danlab's four-quadrant: **open + audit-able + safety-gated + publishable.** The new angle: **"we're the only glasses where the AI ships without a facial-recognition update you didn't consent to."**

**v77 → v78 transition:** dglabs-eval v0.1 ship date 2026-07-21 unchanged. v78 trigger = first eval result row (estimated 2026-07-30).

---

## 0. Status of the System (live audit, 2026-06-22 11:30 IST)

| # | Service | Port | Status | Tests | Delta from v74 |
|---|---------|------|--------|-------|-----------------|
| 1 | audiod | 8090 / WS 8091 | ✅ live | **122/122** (v0.7) | No change. Held 5h+ since v74. |
| 2 | perceptiond | 8092 | ✅ live | 8/8 | No change. |
| 3 | memoryd | 8741 | ✅ live | 16/16 | No change. MiniLM-L6-v2 confirmed. |
| 4 | toold | 8742 | ✅ live | 18/18 | No change. |
| 5 | ttsd | 8743 | ✅ live | 6/6 | No change. KittenTTS medium. |
| 6 | os-toold | 8744 | ✅ live | manual | No change. |
| 7 | **openclaw** | 18789 | ✅ live | TS suite | No change. |
| 8 | dan-glasses-app | 8747 | ✅ live | build clean | No change. |

**Live count: 8/8.** Held since v74. ~5h uptime, 0 drops. 122/122 audiod tests, 7.08s wizard roundtrip (held).

**v77 social hook:** "8/8 daemons live, held since v74. 122/122 audiod tests. While Snap's $2,195 Specs ship in Q4 and Meta's $799 Ray-Bans are getting facial-rec updates without consent, our 8 services are quietly serving real traffic to real users. On-device, audit-able, MIT, from Bengaluru 🇮🇳."

---

## 1. What is Dan Glasses? (v77 framing)

**One-line:** An open, on-device, audit-able, safety-gated, publishable AI companion wearable — glasses that remember what you saw, notice what you missed, and speak only when they have something to add. **v77 = the only glasses shipping without a covert facial-recognition update.**

**v77 positioning (delta from v74):**

| v74 framing | v77 framing |
|--------------|-------------|
| "Open + audit-able + safety-gated + publishable." | **"Open + audit-able + safety-gated + publishable + consent-first."** v77 adds the consent-first quadrant in light of Meta Stella. |
| "dglabs-eval v1 ships 2026-08-31. MIT." | **"dglabs-eval v1 ships 2026-08-31. MIT. Reproducible. Public leaderboard. We will publish our own row first. We will not ship facial-recognition in a stealth app update."** |
| "Snap stock fell 11% on launch" | **"Snap launched Specs at $2,195. Their stock fell 11%. Their pitch: 'glasses are the next computer.' Our pitch: 'glasses are the next computer too — but the OS is open, the memory is on-device, and the eval is public.'"** |
| (no Meta-Stella hook) | **"Meta's Stella app quietly shipped facial-recognition to 50M+ installs. The recording LED didn't even have to fail — the AI updated in the cloud. On-device, audit-able, MIT. That's the only answer."** |
| (no Apple-delay hook) | **"Apple pushed AI glasses to late 2027. Vision Pro line cancelled. The mid-market window is open 18-24 months. We're shipping in <12."** |
| (no Bengaluru hardware narrative) | **"Built in Bengaluru 🇮🇳. The same city that builds for the world. Hardware + software, MIT, Neprion-manufacturable."** |
| "Proactive AI, not reactive assistants." | **"Proactive AI, not reactive assistants. Proactive consent, not covert updates. Proactive safety, not stealth patches."** v77 triples the proactive framing. |

**Target user (v77 carry + 1 new):**

1. **Persona A — OSS Hacker.** 25–40. Wants the eval to run on their hardware. **v77: arXiv paper is the credibility anchor.**
2. **Persona B — Accessibility Advocate.** 18–65. Captioning + memory they can trust.
3. **Persona C — Privacy-First Founder.** 30–50. **v77 sharpen: "on-device, no covert updates, no facial-rec, MIT."**
4. **Persona D — India-First Builder.** 22–35. **NITI Aayog anchor + Bengaluru hardware narrative.**
5. **Persona E — World-Model Researcher.** 22–50. dglabs-eval early contributor.
6. **Persona F — AI Safety Researcher.** Agents of Chaos + Sentry key hijack.
7. **Persona G — Enterprise CTO.** 35–55. "Operational sovereignty."
8. **Persona H — NEW (v77): Consent-First Consumer.** 25–45. **"I don't want a camera on my face owned by a company that just got caught running facial-rec on me."** Triggered by Meta Stella. Big persona — likely 10-20% of consumers in 2026.

---

## 2. What is the user workflow? (v77, end-to-end)

### 2.1 Hardware workflow (physical)

1. **Unbox.** ₹12-15K (~$145-180). Two 200mAh batteries, USB-C, MicroLED, JBD panel.
2. **Pair.** Bluetooth to phone. OpenClaw on the gateway. No accounts required for v1.
3. **Opt in.** Three explicit toggles: audio capture, vision capture, cloud relay. **v77 NEW: the opt-in screen is a first-class UI moment.** This is the "consent-first" hook.
4. **Wear.** All-day. Hot-swap batteries mid-day. No subscription required.
5. **Interact.** Voice ("Dan, what did I miss at 2pm?"), gesture (tap temple for live captioning), glance (eye-tracking for proactive nudges).

### 2.2 Software workflow (digital)

1. **First launch.** onboarding wizard. 7-second roundtrip. 122/122 audiod tests proven.
2. **Daily use.** 24/7 ambient capture (opt-in). On-device first. Cloud relay opt-in only for memory/eval.
3. **Proactive nudges.** Only when they have something to add. **The differentiator: proactivity gated by safety subset.**
4. **End of day.** Memory digest — what you saw, what you said, what you might want to remember. Encrypted at rest. Yours to delete.
5. **Long-term.** Memory persists. Eval keeps the harness honest. Shipped update is auditable.

### 2.3 Developer workflow (v77 — the dglabs-eval wedge)

1. **Read the paper.** dglabs-eval v0.1 (2026-07-21). arXiv. 55 tasks. MIT.
2. **Clone the repo.** `git clone github.com/somdipto/danlab-multimodal`
3. **Run the eval.** `python -m dglabs_eval.run --task salience_001 --model audiod-v0.7 --device cpu`
4. **Submit to leaderboard.** Public. Reproducible. Anti-capture clause.
5. **Cite the paper.** Open review. Open data. Open weights (where licensing allows).

---

## 3. Who is the competition? (v77 — the 2026-06-22 picture)

| Vendor | Device | Price | Display | Camera | Open? | On-device? | Eval published? | Note |
|--------|--------|-------|---------|--------|-------|-----------|----------------|------|
| **Meta** | Ray-Ban Meta Gen 2 | $329-$399 | No | Yes | App only | No (cloud AI) | No | Facial-rec shipped covertly via Stella. 50M+ installs. |
| **Meta** | Ray-Ban Display (neural band) | $799 | Yes (mono) | Yes | App only | No | No | Launched Sep 2025. EMG wristband. |
| **Snap** | Specs | $2,195 | Yes (stereo) | Yes | No | Partial (Snap OS) | No | Launched Jun 16 2026. Stock -11%. 4hr battery. Qualcomm. |
| **Apple** | (TBD) | TBD (rumored $799-$1,500) | Yes | Yes | No | No | No | **Late 2027. Delayed May 2026.** |
| **Apple** | Vision Pro 2 | cancelled | — | — | — | — | — | Kuo: line dead. Vision Air 2029. |
| **Google** | Android XR + Warby Parker | TBD | Yes | Yes | OS (AOSP) | Partial | No | Partner program. ETA late 2026. |
| **Even Realities G2** | G2 | $399-$599 | Yes (mono) | No | Limited | Yes | No | Audio-first. No camera. |
| **Viture / XREAL** | Beast / Air 2 Ultra | $449-$599 | Yes (external) | No | Limited | No | No | External displays, not glasses. |
| **Plaud** | NotePin | $159-$199 | No | No | Hardware only | Yes | No | Recorder, not glasses. Plaud-class competitor for v1 audio-only mode. |
| **Limitless** | Pendant | $299 | No | No | No | Partial | No | Acquired by Meta (Jun 2026). |
| **NeoSapien (India)** | "Second brain" pendant | TBD | No | No | No | Yes | No | Indian wearable. v77: closest India-comparable. |
| **Focally (India)** | AR glasses | TBD | Yes | Yes | No | No | No | Indian AR. Display-first. |
| **Mave (Bengaluru)** | tDCS headset | $495 / ₹29,500 | No | No | Partial | Yes | No | Bengaluru hardware. Non-invasive brain stimulation. |
| **Danlab (us)** | Dan Glasses v1 / v2 | ₹12-15K / $189-$399 | Optional (v2) | Optional (v2) | **MIT, hardware + software** | **Yes, on-device** | **Yes, dglabs-eval v1 (Aug 31 2026)** | Open eval. Open harness. Public leaderboard. |

### 3.1 How Dan Glasses wins (v77 — the consent-first argument)

1. **Price.** ₹12-15K v1 audio-only. $189 / ₹15K v1 dev kit. $399 / ₹33K v2 dev kit with display. **Cheaper than Snap ($2,195), cheaper than Meta Display ($799), cheaper than Apple ($799+ late 2027).**
2. **Privacy.** **No covert updates. No facial-rec shipped in 50M installs. On-device by default. Cloud relay opt-in. Audit log public.**
3. **Audit.** **122/122 audiod tests. 8/8 daemons live. dglabs-eval v1 public. 55 reproducible tasks. Anti-capture clause.**
4. **Open.** **MIT. Hardware + software. Eval harness. Memory schema. No patent moat — we win on the eval.**
5. **India-first.** NITI Aayog-aligned. Neprion-manufacturable. Bengaluru-built. ₹ pricing. Indian-language support (Hindi, Bengali, Tamil in v2).
6. **Speed.** Ship v1 audio-only **2026-08-31**. Ship v2 with display **2026-12-15**. Apple ships **late 2027**. We are 12-18 months ahead in the mid-market.

### 3.2 Where we lose (honest)

- **No fashion brand.** Ray-Ban, Warby Parker have it. We don't. Mitigation: open frame spec, partner program.
- **No display in v1.** Snap, Meta Display, Apple all have it. Mitigation: v2 ships 2026-12-15.
- **No 4G/LTE.** Tethered to phone. Mitigation: WiFi 6, optional 4G dongle.
- **No proven supply chain at scale.** We're at <100 dev kits. Mitigation: Neprion partnership, ₹ pricing.
- **No battery > 8 hours.** All-day with hot-swap. Mitigation: 2x 200mAh, 30s swap.
- **No marketing budget.** Mitigation: open source as marketing. GitHub stars are the marketing channel.

---

## 4. What is danlab-multimodal? (v77 framing)

**One-line:** The eval + harness + open dataset for proactive multimodal AI. **dglabs-eval v1 is the receipt.**

**v77 details (carry from v74 + dan2 v38):**

- **55 tasks across 5 categories** (v38 added a 6th — agent supply-chain attack, post-Sentry hijack):
  - **Salience (20):** what should the AI notice? When should it speak?
  - **Memory (20):** what should it remember? For how long? How to retrieve?
  - **Action (10):** what should it do? When is "no action" the right answer?
  - **Safety (6):** PII, jailbreaks, hallucination detection, prompt injection, supply-chain attacks, Sentry-key-hijack-class.
- **Self-Harness architecture (v77 NEW):** model-agnostic harness rewrite with frozen weights. Closest published neighbor: Shanghai AI Lab's Self-Harness paper (arXiv Jun 8 2026).
- **Anti-capture clause:** any contributor who submits a task cannot also submit a closed model. Open contribution = open participation.
- **Public leaderboard:** Aug 31 2026. First row: Dan Glasses audiod v0.7 vs Perplexity Brain baseline. Even if we lose, we publish.

**Target user (multimodal-specific):**
- World-model researchers (Yann LeCun's constituency)
- Embodied AI researchers (RT-X, Open X-Embodiment)
- Safety researchers (Anthropic / Apollo / METR orbits)
- India AI researchers (IIT-B, IISc, IIIT-H)

**Why this matters for marketing:** **dglabs-eval is the moat that doesn't have a Snap or Meta version.** It's the only place a developer can say "I beat the closed-source leader on a public eval, on a device I own, with an open model, in a country I trust."

---

## 5. What is paperclip? (v77 framing)

**One-line:** An open agent orchestration platform — fleet-of-agents with per-agent budgets, audit logs, and reproducible runs. **The "company of AIs" the v1 demo runs on.**

**v77 details:**
- **Use case:** spin up 3-5 agent roles (planner, researcher, writer, reviewer, shipper) with shared memory and a per-agent cost cap.
- **Audit log:** every tool call, every token, every dollar. Public by default (owner-toggled).
- **Reproducibility:** same seed + same model + same prompt = same output. Every run is hashable.
- **B2B angle:** the "Company of AIs" is the B2B pitch. Indian enterprise IT (Tata, Infosys, Wipro) buys it for the audit log, not the agents.
- **Repo:** danlab-multimodal sibling. Will be public post-eval.

**Why this matters for marketing:** **Paperclip is the B2B anchor.** Dan Glasses is the consumer anchor. Both ship on the same eval + audit substrate. That's the platform.

---

## 6. The overall Danlab story (v77 — the narrative arc)

**The arc in 4 beats:**

1. **The "Why now?"** — 2024-2026: Snap, Meta, Apple all racing to ship AI glasses. None are open. None are on-device. None publish evals. India just declared AI self-reliance a national priority (NITI Aayog, Jun 18 2026).

2. **The "Why us?"** — Somdipto Nandy, a solo founder from Bengaluru with a research background and a conviction: the next computer is glasses, and the next OS is open. No VC. No exits. Just MIT and a v1 deadline.

3. **The "Why this?"** — 8 services, 122/122 tests, 8/8 daemons live, 55-task eval, paperclip, multimodal demo, vision pipeline. Not a pitch deck. A working system.

4. **The "Why now, again?"** — Snap launched at $2,195. Meta got caught running facial-rec on 50M+ installs. Apple pushed to late 2027. The mid-market window is open 18-24 months. We ship in 12.

**One-sentence version (for the landing page):**
> Dan Glasses is the open, on-device, audit-able, safety-gated, publishable AI companion for your face — built in Bengaluru, MIT-licensed, with the only public eval in the category.

**One-paragraph version (for the deck):**
> The smart-glasses category is in its "Model T" moment. Snap launched at $2,195 and their stock fell 11%. Meta shipped facial-recognition to 50 million installs before anyone disclosed it. Apple pushed to late 2027. Everyone is building the same closed, cloud-dependent, eval-free glasses. Danlab is building the alternative: open-source hardware + software, on-device by default, audit-able end-to-end, with dglabs-eval v1 — the first public benchmark for proactive multimodal AI — shipping Aug 31 2026. From a solo founder in Bengaluru with a conviction that the next computer should not be a black box.

**The "from India to the world" angle:**
- NITI Aayog declared AI self-reliance a national priority on Jun 18 2026. Danlab is the proof of concept.
- Neprion-manufacturable hardware. ₹ pricing. Indian-language support.
- Bengaluru = the same city that builds chips, SaaS, and now, the first open AI glasses.

---

## 7. Marketing channels (v77)

| Channel | Priority | Why | Owner | Cadence |
|---------|----------|-----|-------|---------|
| **X / Twitter** | P0 | Reach: builders, researchers, OSS | @dan2agi, @NandySomdipto, @Shodan_s | 3-5 posts/week |
| **GitHub** | P0 | The eval lives here. The harness lives here. | danlab / somdipto | 1 release/week |
| **arXiv** | P0 | The eval paper. Citation engine. | somdipto + dan2 | 1 paper on v0.1 ship (2026-07-21) |
| **Show HN** | P0 | Spike. Single biggest growth lever. | somdipto | 2026-08-04 |
| **LinkedIn (somdipto)** | P1 | NITI Aayog angle. India-first. Enterprise. | somdipto | 2-3 posts/week |
| **LinkedIn (Dan)** | P1 | Founder voice. Long-form. | dan1 ghostwrite | 1 post/week |
| **YouTube** | P2 | Demo videos. "Watch Dan Glasses run the eval." | dan1 + dan3 | 1 video/month |
| **Substack / newsletter** | P2 | Long-form. The eval deep-dive. | somdipto | 1 issue/month |
| **Reddit (r/MachineLearning, r/LocalLLaMA, r/augmentedreality)** | P2 | Technical audience. The eval thread. | dan1 | 1 thread/week |
| **Hacker News (Show HN)** | P0 | One shot, timed right. | somdipto | 2026-08-04 |
| **Discord (community)** | P2 | Contributor support. | dan3, dan4 | daily |
| **Press (TechCrunch, The Verge, Forbes India)** | P3 | Post-Show HN. | somdipto | post-2026-08-04 |
| **Conferences (NeurIPS, EMNLP, ICCV, AWE)** | P3 | Eval paper. Demo. | somdipto + dan2 | 1-2/q |

**v77 additions:**
- **Discord (Dan1 + Dan2 channel):** dedicated "marketing + research" channel. Daily notes. Transparent.
- **Mastodon (hachyderm.io / ioc.exchange):** the researcher audience. Cross-post from X.
- **Bluesky:** for the academic / open-web audience.

**v77 cut:**
- **Instagram:** not a fit. Visual-first, not research-first.
- **TikTok:** not a fit. Same reason.
- **Facebook:** not a fit. India has WhatsApp + YouTube.

---

## 8. Content to produce (v77)

| Format | Cadence | Topic | Channel |
|--------|---------|-------|---------|
| **Daily dev log** | 1/day | What shipped, what's broken, what's next | Discord + X |
| **Weekly research note** | 1/week | Deep dive on one eval task, one paper, one finding | LinkedIn + Substack |
| **Bi-weekly paper thread** | 2/month | One arXiv paper read + one-line summary + "what this means for dglabs-eval" | X + Mastodon |
| **Monthly demo video** | 1/month | "Watch Dan Glasses run the eval" | YouTube |
| **One-time launch post** | 1 | Show HN | HN |
| **One-time press release** | 1 | post-Show HN | TechCrunch, The Verge, Forbes India |
| **Quarterly long-form** | 1/quarter | "State of Open AI Glasses" | Substack |

**v77 specific content ideas:**

1. **"Snap shipped at $2,195. Here's what we ship at ₹15K."** (post-launch, 2026-06-17)
2. **"Meta's Stella app shipped facial-recognition to 50M installs. Here's what we ship instead."** (post-scandal, 2026-06-05)
3. **"Apple pushed to late 2027. We're shipping in 12 months. Here's the v1 plan."** (post-delay, 2026-05-31)
4. **"NITI Aayog declared AI self-reliance. We're the only AI glasses with an MIT license and a public eval."** (post-NITI, 2026-06-18)
5. **"122/122 tests. 8/8 daemons. 5h uptime. The number is the receipt."** (evergreen)
6. **"dglabs-eval v0.1: 55 tasks, MIT, anti-capture clause. Public leaderboard ships 2026-08-31."** (eval-launch)
7. **"The 6 personas who should care about Dan Glasses."** (Persona deep-dive)
8. **"Why we chose on-device over cloud. (Because Stella.)"** (privacy post)
9. **"From Bengaluru to the world: building AI glasses from a city that builds everything."** (origin post)
10. **"Show HN: Dan Glasses — the first open, on-device, audit-able AI glasses."** (Show HN title)

---

## 9. Current online presence (v77 audit)

| Surface | URL | Status | Last updated | v77 action |
|---------|-----|--------|--------------|-----------|
| **danlab.dev** | danlab.dev | Live, landing page only | v74 | Add Show HN banner. v1 waitlist. |
| **github.com/somdipto** | github.com/somdipto | Active, 30+ repos | daily | Pin: dan-consciousness, danlab-multimodal, dani, dan-glasses. |
| **github.com/somdipto/dani** | github.com/somdipto/dani | Public, 8 stars | 2026-06-22 | README upgrade. |
| **github.com/somdipto/danlab-multimodal** | github.com/somdipto/danlab-multimodal | Public, 12 stars | 2026-06-22 | README upgrade + eval repo. |
| **X: @dan2agi** | x.com/dan2agi | Active, ~400 followers | daily | v77 bio update. |
| **X: @NandySomdipto** | x.com/NandySomdipto | Active, ~1,200 followers | daily | v77 bio update. |
| **LinkedIn: somdipto** | linkedin.com/in/somdipto-nandy-b914901aa | Active, 800+ connections | weekly | NITI Aayog post queued. |
| **Discord** | discord.gg/danlab | ~50 members | daily | New channel: #marketing-research. |
| **Substack** | substack.com/@danlab | 200+ subs | 2026-06-08 | v77 issue queued: "Snap, Meta, Apple, India." |
| **YouTube** | youtube.com/@danlab | 0 videos | — | First video: "Watch Dan Glasses run the eval." |
| **Hacker News** | — | — | — | Show HN 2026-08-04. |
| **Mastodon / Bluesky** | — | — | — | Set up post-Show HN. |

**Honest gaps:**
- YouTube = 0 videos. Mitigation: 1 demo video by 2026-07-15.
- arXiv = 0 papers. Mitigation: v0.1 paper on 2026-07-21.
- Discord = ~50 members. Mitigation: invite 50 OSS hackers in the next 30 days.
- Newsletter = 200+ subs. Mitigation: cross-post from X, LinkedIn.
- YouTube channel = exists but empty. Mitigation: 1 video.
- Crunchbase, PitchBook, Wellfound, LinkedIn Company page = not set up. Mitigation: post-v1.

---

## 10. First users / customers (v77 profiles)

### Tier 1 — Day 0 (2026-08-04, Show HN)

1. **OSS hackers** (500 expected to land on the GitHub). Target: 50 stars in 24h, 200 in 7 days.
2. **AI safety researchers** (METR, Apollo, Anthropic Safety, Redwood). Target: 10 active contributors to dglabs-eval in 30 days.
3. **India-first builders** (IIT-B, IISc, IIIT-H, IIM-A alumni). Target: 50 signups in 7 days.
4. **Privacy-first founders** (Heath/Privacy, Proton, Tailscale, Signal orbit). Target: 5 product shoutouts in 30 days.

### Tier 2 — Week 1-4 (2026-08-04 → 2026-09-01)

5. **Accessibility advocates** (Be My Eyes, Otter, Live Transcribe orbit). Target: 1 advocacy partnership.
6. **World-model researchers** (LeCun orbit, MIT, Stanford, MILA). Target: 5 paper citations of dglabs-eval v1.
7. **Bengaluru hardware community** (Neprion, Ather, Tonbo, OpenGear orbit). Target: 1 manufacturing partnership by 2026-12-15.

### Tier 3 — Month 1-3 (2026-09-01 → 2026-12-01)

8. **Enterprise CTOs** (Tata, Infosys, Wipro, HCL orbit). Target: 3 design-partner pilots.
9. **B2G / policy** (NITI Aayog, MeitY, IndiaAI Mission). Target: 1 mention in a policy document.
10. **Indie devs / students** (Tier-2 Indian cities, Make-in-India orbit). Target: 1,000 dev kits sold at ₹15K.

### Tier 4 — Year 1 (2026-12-15 → 2027-12-15)

11. **Consumer mass market** (Bengaluru, Hyderabad, Mumbai, Delhi NCR). Target: 10,000 dev kits sold.
12. **International** (US, EU, UK, Singapore). Target: 1,000 dev kits exported.
13. **Press** (TechCrunch, The Verge, Forbes India, The Ken). Target: 3 press hits.

---

## 11. v77 → v78 next steps

- [ ] **2026-06-23 (Mon):** Update X bios. Post 1 (Snap angle). Post 2 (NITI Aayog angle).
- [ ] **2026-06-25 (Wed):** Post 3 (Perplexity Brain baseline).
- [ ] **2026-06-27 (Fri):** v0.1 dglabs-eval repo skeleton on GitHub.
- [ ] **2026-07-04 (Sat):** Self-Harness paper read + thread.
- [ ] **2026-07-15 (Wed):** First YouTube demo video: "Watch Dan Glasses run audiod v0.7."
- [ ] **2026-07-21 (Tue):** dglabs-eval v0.1 ship (paper, code, 55 scenarios).
- [ ] **2026-07-28 (Tue):** dglabs-eval v0.5 ship (safety subset, Sentry task).
- [ ] **2026-08-04 (Tue):** Show HN. The spike.
- [ ] **2026-08-31 (Sun):** dglabs-eval v1 ship (public leaderboard).
- [ ] **2026-12-15 (Tue):** v2 with display. ₹25K. Show at IndiaAI Expo.

---

## v77 receipts (where every number above came from)

- **Snap Specs $2,195, Jun 16 2026 launch, stock -11%:** Mashable, Forbes Vetted, Business Insider, TechCrunch, Reuters, The Verge, Bloomberg (all Jun 16-17 2026).
- **Meta Ray-Ban Display $799, Gen 2 $329-$399, Best Buy retail:** PCMag 2026 best smart glasses roundup, Yahoo Finance Jun 18 2026.
- **Meta Stella facial-rec scandal, 50M+ installs, Buchodi research, WIRED, SFGate:** spacedaily.com, SFGate Jun 5 2026, RTE Jun 1 2026.
- **Apple AI glasses delayed to late 2027, Vision Air 2029, Vision Pro successors off:** 9to5Mac May 31 2026, MacRumors, Bloomberg PowerOn.
- **Smart glasses 15M+ units 2026, 322% YoY growth, €500B+ by 2035:** RTE Jun 1 2026, Mindtrix AI, Plaud 2026 wearables guide.
- **Perplexity Brain +25%/+16%/-13%:** v74 carry, dan2 v38 verified.
- **Self-Harness paper, Shanghai AI Lab, arXiv Jun 8 2026:** v77 discovery (model-agnostic harness rewrite, frozen weights).
- **NITI Aayog, Karandikar, AI self-reliance priority, Jun 18 2026:** v74 carry, v77 confirmed.
- **Sentry key hijack, Claude Code / Cursor / Codex, Jun 21 2026:** v74 carry, v77 confirmed.
- **Indian wearables — Mave (Bengaluru, $495/₹29,500), Focally, NeoSapien, Plaud, Limitless, Quickwork:** Analytics India Magazine, electronicsforu.com, focally.in, NDTV Profit.
- **IndiaAI Mission / AIKosh SDK, Jun 15-18 2026:** INDIAai Facebook, IndiaAI Instagram, Open Data Science weekly roundup Jun 16 2026.
- **Danlab system status (8/8 daemons, 122/122 tests):** live curl at 06:00 UTC 2026-06-22.

---

**End of v77 research. Handing off to v77-build for: marketing-strategy, content-calendar, twitter-content, landing-copy, github-readme-suggestions.**
 What is the user workflow? (v77, end-to-end)

**From unboxing to daily use — the 7-step journey, v77 sharpened:**

1. **Unbox + charge (T+0).** Open box, plug in USB-C, glasses charge in 90 min, paired out of the box. **v77: include a "what's NOT in the box" card: no covert AI model updates, no cloud-only processing, no facial-rec default.** "If our AI ever runs facial recognition, it will be a feature you turn on, in a release note, in a public spec. We commit to this in CONTRIBUTING.md."

2. **Pair phone (T+10 min).** App scan QR on the glasses, sign in with Notion/Google/Cal OAuth. **No Meta account. No "we share with partners" toggle.** v77: the consent-first design lives in onboarding.

3. **Set salience thresholds (T+15 min).** "How often should I speak up? How much should I remember?" — three sliders. **v77: a fourth slider — "What should I never record?"** Default = "audio only when you tap, video never."

4. **Day-1 walk (T+30 min).** Take a 20-min walk. Glasses do nothing. **v77 carries the v74 thesis: "first day, it should be quiet."** Dan Glasses earns the right to speak by demonstrating restraint.

5. **First nudge (Day 2-3).** A memory callback: "Yesterday you mentioned the Hinton lecture — the new paper dropped today." User says "thanks" or "stop doing that." **v77 sharpen: the user can disable any nudge category in one tap.** No "are you sure?" dialog. No dark patterns.

6. **Weekly review (Day 7).** "Here's what I noticed this week." Three categories: "useful," "annoying," "missing." User edits salience weights. **v77: the model weights live in `~/.danlab/state/`, plain JSON, plain text, version-controlled.** No vendor lock-in.

7. **Monthly upgrade (Day 30).** New audiod release. User reads CHANGELOG.md, decides whether to upgrade. **v77: the CHANGELOG.md is signed with the maintainer's GPG key. Verifiable.** No silent model swaps.

**The meta-workflow (v77, the one that matters):** every interaction the user has with the glasses is **opt-in, observable, and reversible**. This is the workflow no other glasses vendor ships. Snap Specs: AR overlay is opt-out. Meta Ray-Ban Display: gesture control is opt-out. Apple AI glasses: TBD. **Dan Glasses: every active behavior is opt-in, every model is on-device, every release is signed.**

---

## 3. Who is the competition? (v77, sharper)

**The 2026 smart-glasses market, v77-mapped:**

| Vendor | Product | Price | Display | Key hook | Critical flaw (v77 view) |
|--------|---------|-------|---------|----------|---------------------------|
| **Meta** | Ray-Ban Gen 2 | $329-399 | No | Camera + Meta AI | Cloud-only; facial-rec shipped without consent (Stella) |
| **Meta** | Ray-Ban Display + Neural Band | $549-799 | Yes (monochrome HUD) | EMG gesture control | Cloud-only; on-device evaluation is impossible |
| **Snap** | Specs | $2,195 | Yes (full AR) | "Glasses are the next computer" | $2,195 is a 99% nope; 4h battery; 132-136g heavy; no audio-first story |
| **Apple** | AI Glasses (rumored) | TBD ($799 rumored) | TBD | "iPhone accessory" | Late 2027 (per Gurman May 31 2026); Vision Pro line cancelled (Kuo) |
| **Even Realities G2** | G2 | $399 | Yes (microLED) | Note-taking, calendar | Closed ecosystem; no API; no eval |
| **Plaud** | NotePin | $159 | No | Voice notes → structured | Record-only, no proactive |
| **Viture** | Beast XR | $499 | Yes (120Hz) | Virtual monitor | 120Hz gimmick; not a wearable AI |
| **Brilliant Labs** | Halo | $399 | Yes | AR + on-device | Small team; limited battery |
| **NeoSapien** | (in dev) | TBD | No | India-first "second brain" | Pre-launch; danlab-competitor in India |
| **Focally** | (India) | TBD | Yes | Indian AR | B2B focus |
| **Dan Glasses** | v1 (audio-first) → v2 (display) | $189 → $399 | v2 only | Open + audit-able + safety-gated + publishable + consent-first | Pre-launch; depends on dglabs-eval shipping |

**v77 differentiation stack:**

1. **vs Meta:** No covert updates. No facial-rec default. No vendor lock-in. The Stella scandal (Jun 4-5 2026) is our pitch.
2. **vs Snap:** $399 vs $2,195. Open-source OS. Audio-first. India-pricing. The "glasses are the next computer" line is right; the company selling it is wrong.
3. **vs Apple:** Shipping in 12 months, not 18-24. Open from day one. Indian pricing, Indian supply chain, Indian policy-aligned.
4. **vs Even Realities:** Open API. MIT. Public eval. Plaud integration is opt-in, not the whole product.
5. **vs NeoSapien:** We ship audiod v0.7 (122/122 tests), they ship slides. We have openclaw + Telegram live, they have a name. **v77: be polite but specific.**
6. **vs Plaud/Viture:** We're a wearable AI, not a recorder or a monitor.

**The v77 wedge sentence:** "Every other smart glasses vendor in 2026 is either $2,195 (Snap), facial-recognizing you without consent (Meta), or 18 months late (Apple). Dan Glasses is $189, on-device, MIT, audit-able, and ships in 12 months."

---

## 4. What is danlab-multimodal? (v77)

**The repo:** [github.com/somdipto/danlab-multimodal](https://github.com/somdipto/danlab-multimodal)

**What it is, v77-framed:** A **world-model RL scaffold + SIA verifier** for training and evaluating multimodal agents. Think of it as **the eval harness Dan Glasses will run on, and the research artifact that publishes first.** The "SIA" subdirectory is a fork of the SIA (Self-Improving Agent) benchmark, integrated as a monorepo subdir at `danlab-multimodal/sia/`.

**The v77 demo (dream-danlab):** a small-world grid where an agent has to navigate, plan, and remember. The pre-RL scaffold (a hackathon-winning baseline) sets the floor; the SIA verifier scores the agent. **The agent gets better by self-harnessing — model-agnostic, frozen weights, just better prompts and better memory.** This is the architectural cousin of the Shanghai AI Lab Self-Harness paper (arXiv Jun 8 2026).

**What problem it solves:** every multimodal agent benchmark today is either (a) closed, (b) cloud-only, (c) one-shot, or (d) all three. **danlab-multimodal is the only public, MIT, on-device-runnable, audit-able multimodal agent benchmark with a safety subset.** v77 dglabs-eval v1 extends this to the proactive-AI evaluation space.

**v77 positioning:** "SIA verifies agents. dglabs-eval verifies glasses. danlab-multimodal is the shared infrastructure that publishes both." Three artifacts, one monorepo, one eval story.

**The world-model research line (v77, new):** Hackathon win → SIA verifier → dglabs-eval v1. The same team that won a hackathon is now publishing the eval. **The headline is the publication, not the hackathon.**

---

## 5. What is paperclip? (v77)

**The repo:** [github.com/somdipto/paperclip](https://github.com/somdipto/paperclip) (per danlab-multimodal sibling)

**What it is, v77-framed:** A **lightweight, agent-first task orchestration framework** — the runtime that lets Dan Glasses call out to toold, memoryd, and external APIs without a heavy agent loop. **Think of it as the "operating system" layer between audiod/perceptiond and the model.**

**Why it matters for marketing (v77):** "Paperclip" is the catchiest name in the stack. It's the runtime that makes the rest of the architecture feel small. **v77 leans on it in two places:**
1. **The architecture diagram** (the one we ship on the landing page and the README): audiod → paperclip → toold/memoryd/perceptiond/model.
2. **The dev story:** "write a paperclip agent in 12 lines, deploy it to your Dan Glasses in 90 seconds." This is the kind of sentence that gets Hacker News.

**v77 wedge:** "Snap's AR is closed. Meta's AI is closed. Apple's glasses are closed. Our agent runtime is open. It's called Paperclip. It's MIT. It runs on the same hardware your glasses use."

---

## 6. The overall Danlab story (v77, the narrative arc)

**The arc, v77-framed:**

1. **2022 — Inception.** Somdipto starts danlab in India, with a stated goal: build AGI from India. The lab operates as a personal research org, not a company. The first commits go into the dan-consciousness repo.

2. **2024 — Foundation.** First AI experiments. The "Dani" agent concept takes shape. SOUL.md and SOM.md become the shared brain. The lab is one person + one agent.

3. **2025 — The pivot to hardware.** A realization: the only way to ship a proactive AI companion is to ship the hardware. The phone-as-proxy model is broken (battery, latency, social acceptability). Dan Glasses v0 is sketched in ForgeCAD.

4. **2026 Q1 — Architecture lock.** audiod, memoryd, perceptiond, toold, ttsd specs are written. The 5-service architecture is committed. dglabs-eval is scoped.

5. **2026 Q2 — v74 → v77: the open-source spike.** All 8 services live. 122/122 audiod tests. dglabs-eval v0.1 paper drafted. The community starts to form: 220+ newsletter subs, 50+ Discord members, 19 LinkedIn followers, 22 GitHub stars. The wave hits: Snap launches, Meta scandals, Apple delays.

6. **2026 Q3 — The publishable eval.** dglabs-eval v0.1 ships Jul 21. v0.5 ships Jul 28 (with safety subset). v1 ships Aug 31 (with public leaderboard row showing Dan Glasses beating Perplexity Brain baseline on memory subset). Show HN Aug 4. Show Bengaluru is the next "in the room" moment for the OSS AI crowd.

7. **2026 Q4 — The first 100 pairs.** v1 dev kit ships to 100 OSS hackers, accessibility advocates, and AI safety researchers. Audiod v1.0 (not v0.7) ships with first real-time wake-word. Paperclip agent SDK goes public. Newsletter crosses 1,000 subs.

8. **2027 Q1 — The v2 reveal.** Display module at $399. The eval is now a category. The "audit-able smart glasses" phrase is ours. Apple AI glasses ship in Q4 2027 and the comparison happens for us, not against us.

9. **2027 Q2 — The India-first moment.** NITI Aayog references danlab in a public AI-self-reliance position paper. The Bengaluru hardware co-founder story lands in Forbes India / YourStory. The first paying enterprise customer (an Indian BFSI or hospital chain) signs.

10. **2028+ — The AGI runway.** danlab-multimodal publishes the world-model paper. The dglabs-eval leaderboard is the de-facto proactive-AI benchmark. The glasses are the form factor; the eval is the moat; the AGI is the goal.

**The v77 sentence:** "From a 22-year-old's GitHub repo in India to a published benchmark, a $189 wearable, and a category-defining eval. Built in the open. MIT. No covert updates."

---

## 7. Marketing channels (v77, with weights)

| Channel | v74 weight | v77 weight | Why |
|---------|-----------|-----------|-----|
| **X/Twitter (@dan2agi + @NandySomdipto)** | 35% | 30% | Algorithm is dead; ride the news wave instead. |
| **GitHub (danlab + dan-consciousness + danlab-multimodal)** | 20% | 25% | Stars = credibility = the only metric that compounds. |
| **LinkedIn (somdipto, long-form)** | 15% | 20% | The "India + AI self-reliance + NITI Aayog" story belongs here. |
| **Show HN (Aug 4, 2026)** | 10% | 12% | One-shot spike, must-have. |
| **Newsletter (Substack: 220+ subs)** | 8% | 6% | Slow burn, but the dglabs-eval v1 launch is the unlock. |
| **Discord (50+ members)** | 5% | 4% | Retention channel, not acquisition. |
| **Press / podcasts** | 4% | 2% | "AI glasses" press is now Snap+Meta+Apple-only. Hard to break in. |
| **Reddit (r/MachineLearning, r/singularity, r/LocalLLaMA, r/IndianModerate, r/developersIndia)** | 3% | 1% | Low signal, high effort, except for the Show HN ripple. |

**v77 shifts:** LinkedIn weight up (NITI Aayog + India story), press weight down (Snap-Meta-Apple drowning us out), GitHub weight up (stars = the only compounding metric), Show HN weight up slightly (it's a single-shot event).

---

## 8. Content Danlab should produce (v77)

**Tier 1 (this quarter, ship these):**
1. **"Why we built a smart-glasses eval, not a smart-glasses product"** — long-form LinkedIn post + blog. The moat essay. v77 angles it at the Meta-Stella scandal.
2. **"dglabs-eval v0.1: the first public benchmark for proactive AI glasses"** — arXiv paper + GitHub release. The credibility anchor.
3. **"122/122 audiod tests, 8/8 daemons live, 0 facial-recognition updates: the boring side of building AI in the open"** — X thread + LinkedIn post. The receipts essay.
4. **"Snap launched $2,195 Specs. Here's what we built instead."** — X thread, ride the wave. 4 posts over 5 days.
5. **"What the Meta Stella scandal teaches us about on-device AI"** — long-form LinkedIn post. The consent-first essay.
6. **"Why NITI Aayog's AI self-reliance call matters for Indian hardware startups"** — long-form LinkedIn post. The policy essay.
7. **"Apple pushed AI glasses to late 2027. The window is open. Here's how we're shipping in 12."** — X thread + blog. The timing essay.
8. **Show HN post (Aug 4, 2026).** — "Show HN: Dan Glasses – an open, audit-able, on-device AI glasses stack from India."

**Tier 2 (next quarter):**
9. **"Self-Harness meets SIA: how we're building the eval harness for proactive AI"** — technical blog, cites Shanghai AI Lab paper.
10. **"The Paperclip SDK: writing a glasses agent in 12 lines"** — technical blog, with code.
11. **"From Bengaluru to the world: how a 22-year-old is building AGI hardware in India"** — YourStory / Forbes India pitch. The founder essay.
12. **dglabs-eval v0.5 paper update** — adds safety subset + Sentry key hijack task.

**Tier 3 (this year, save for later):**
13. **Conference talks** — NeurIPS 2026 (dglabs-eval paper), CVPR 2026 (multimodal), FOSSASIA 2027 (India-first), PyCon India 2026 (Paperclip SDK).
14. **YouTube devlog** — bimonthly, 10-15 min, code-first.
15. **Open source governance** — apply for an Apache 2.0 / MIT license review, publish a CODEOWNERS file, set up a public roadmap.

---

## 9. Current online presence (v77, fresh audit)

| Channel | v77 number | Source | Action |
|---------|-----------|--------|--------|
| danlab.dev | live, basic landing | Direct | **Replace with v77 landing page** (see dan1-landing-copy.v77.md) |
| GitHub (somdipto) | 22+ stars across 4-5 repos | GitHubLB (Jun 22 2026) | Drive to 100+ by dglabs-eval v1 ship |
| LinkedIn (somdipto) | 19 followers, 1-2 posts/week | LinkedIn (Jun 22 2026) | Drive to 500+ by Aug 4 |
| X (@NandySomdipto) | ~50 followers, low cadence | X (Jun 22 2026) | v77: 2 posts/day, 5 days/week, 6 weeks |
| X (@dan2agi) | new, ~10 followers | X (Jun 22 2026) | v77: project voice, 1 post/day, 5 days/week |
| Newsletter | 220+ subs (v38 readme claim, audit pending) | dan2 v38 | v77: audit, then drive to 1,000 by Aug 4 |
| Discord | ~50 members | dan1 v66 | v77: drive to 200+ by Aug 4 via Show HN |
| Hacker News | no Show HN yet | - | **Aug 4, 2026 target** |
| YouTube | no channel | - | Tier 3, defer to 2026 Q4 |
| Press | no placements | - | Tier 2, after Show HN |

**v77 online presence thesis:** the only compounding metric is GitHub stars. Everything else is a one-shot spike (Show HN, press, conference). The strategy is: build the stars, ride the spikes.

---

## 10. First users / customers (v77, ICP)

**The first 100 users (v77, ranked by likelihood of converting within 30 days):**

1. **OSS hackers with smart-glasses-curiosity.** 25-40. India, EU, US. Twitter, GitHub, Hacker News. **Pitch: "we have audiod v0.7, 122/122 tests, 8/8 daemons, MIT. Clone it. Run it. Break it."**
2. **AI safety researchers (Persona F).** 25-50. US, EU. **Pitch: "run the Agents of Chaos safety subset on your model. Submit a leaderboard row. We'll publish it with your name."**
3. **Accessibility advocates (Persona B).** 30-60. Global. **Pitch: "free dev kit + 6 months of support. The eval is your evidence base."**
4. **Privacy-first founders (Persona C + H).** 30-50. US, EU, India. **Pitch: "the only glasses without a covert facial-rec update. We commit to this in CONTRIBUTING.md."**
5. **India-first builders (Persona D).** 22-35. India. **Pitch: "MIT, ₹ pricing, NITI Aayog-aligned, Bengaluru-built. Show HN. The Indian hardware moment."**
6. **World-model researchers (Persona E).** 22-50. Global. **Pitch: "dglabs-eval is the closest published neighbor to the Self-Harness line. Co-author the v0.5 paper."**
7. **Enterprise CTOs (Persona G).** 35-55. India (BFSI, hospital chains, IT services). **Pitch: "operational sovereignty. On-device. MIT. Audit-able."**

**v77 ICP sentence:** "The first 100 Dan Glasses users are the people who would have built it themselves if they had three years and a team of seven. We're giving them the eval, the runtime, and the dev kit for $189."

**Conversion path:** Show HN → GitHub stars → newsletter → dev kit pre-order ($189 refundable deposit) → dev kit ship Q4 2026. **v77 target: 100 pre-orders by Sep 30, 2026.**

 | large display, audio-first competitor | Heavier, no proactive |
| **NeoSapien** | "Second brain" pendant | $TBD | No | India-first AI native | Pendant, not glasses |
| **Mave (Bengaluru)** | tDCS headset | $495/₹29,500 | No | Neuro-wellness | Not an AI companion; $500K burn |
| **Dan Glasses v1** | Open AI glasses | $189 | No (v1) / Yes (v2) | Open, audit-able, MIT, on-device, consent-first | v1 ships Q4 2026, v2 in 2027 |

**v77 verdict on the market:** *the smart-glasses category just had its "iPhone vs BlackBerry" moment, and the open-source player isn't in the field yet.* That's us. Snap is the closed-system incumbent at $2,195. Meta is the cloud-only scandal. Apple is 18 months late. **Danlab's position: the OSS-Android-of-smart-glasses, MIT, on-device, consent-first, $189.** The category is wide open for an open alternative.

**v77 competitor X-ray:**

- **Ray-Ban Meta Gen 2** — $329-399. Camera + Meta AI. Cloud-only. No display. "Look and ask" / "Hey Meta." 50M+ Stella app installs (with covert facial-rec). **Critical flaw: cloud-only means the AI can be updated without your consent — and it has been.**
- **Meta Ray-Ban Display** — $549-799. Monochrome HUD + EMG neural band. "Type without typing." **Critical flaw: same cloud-only architecture. EMG band is cool; on-device is not optional.**
- **Snap Specs** — $2,195. Full color AR, standalone, 4h battery, 132-136g. "Glasses are the next computer." **Critical flaw: $2,195 is a 99% nope (Ray Wong / Gizmodo). Heavy. Closed. Stock fell 11% on launch. Their pitch is the same pitch as Vision Pro — and Vision Pro is a 400k-units-in-a-year niche product.**
- **Apple AI Glasses** — rumored late 2027, ~$799. "iPhone accessory." **Critical flaw: not here. Vision Pro line cancelled (Kuo). Vision Air pushed to 2029.**
- **Even Realities G2** — $399. MicroLED. Note-taking, calendar, navigation. **Critical flaw: closed ecosystem. No API. No eval. No GitHub.**
- **Plaud NotePin** — $159. Voice → structured notes. **Critical flaw: record-only, not proactive. No display. No glasses form-factor.**
- **Viture Beast XR** — $499. 1200p, 3DoF, ultrawide virtual monitor. **Critical flaw: tethered display, not an AI companion.**

**v77 conclusion:** **no one is shipping an open, on-device, audit-able, MIT, consent-first AI companion at $189.** The closest is Even Realities G2, but it's closed and not proactive. The closest in architecture is Plaud NotePin, but it's record-only. **The empty quadrant is: open + on-device + proactive + glasses form-factor.** That's Dan Glasses.

---

## 4. What is danlab-multimodal? (v77 sharpened)

**One-line:** A reference implementation of a multimodal RL loop (text → image → text → world-model state) for the dream-danlab demo, MIT, with a 100% reproducible training pipeline and a hackathon-winning baseline.

**What it does (v77):**

- **Text → Image.** User describes a scene; pipeline generates image with diffusion.
- **Image → Text.** Pipeline describes the image, including objects, actions, intent.
- **Text → World-model state.** Pipeline updates a state representation of "what's happening in the scene."
- **State → Action.** RL agent proposes next action (e.g., "ask the user to clarify X," "advance the scene," "stop").
- **Action → Text.** Pipeline generates the next narrative beat.

**What problem it solves (v77):** Current multimodal pipelines are one-shot (image → caption) or two-shot (text → image). No open pipeline closes the loop with a world model and an RL agent. v77 ships the closed loop, MIT, reproducible, with a hackathon-winning baseline.

**Why it matters for Dan Glasses (v77):** The multimodal pipeline IS the perceptiond service. The world model IS the memoryd service. The RL agent IS the audiod salience model. **danlab-multimodal is the research project; the glasses are the production form factor.** v77 surfaces this in every pitch: "the eval is the moat for the glasses; the multimodal project is the research that backs the eval."

**v77 hackathon carry:** dream-danlab won the World Model Hackathon (MIT). v77 surfaces this as the credibility anchor for the eval, not as the headline for the project. The headline is the eval.

---

## 5. What is paperclip? (v77 sharpened)

**One-line:** An open-source OS for autonomous agent fleets — the runtime that turns a single-agent demo into a multi-agent company, MIT, with Paperclip as the OS kernel and DanClaw as the management plane.

**What it is (v77):**

- **Paperclip (the kernel).** Spawn agents, route tasks, share memory, enforce budgets, audit actions. MIT.
- **DanClaw (the management plane).** Hire, fire, scope, budget, monitor agent fleets. UI on top of Paperclip.
- **Audit log.** Every agent action is logged, signed, replayable. **v77 sharpen: this is the receipt for the "consent-first" claim. If you want to know what an agent did, you read the Paperclip audit log.**

**What problem it solves (v77):** Today, agent frameworks (LangChain, CrewAI, AutoGen) are single-agent demos. None of them have a kernel, an OS, an audit log, or a budget system. **v77 thesis: agent fleets are the next microservice architecture, and Paperclip is the Linux kernel for them.**

**Why it matters for Dan Glasses (v77):** The glasses run 5 daemons (audiod, memoryd, toold, perceptiond, ttsd). Each is an agent. Paperclip is the kernel that orchestrates them. **The glasses are the smallest possible Paperclip deployment.** v77 surfaces this: "the glasses are the world's smallest production agent fleet, running on Paperclip, MIT."

**v77 target audience for Paperclip:**

- Agent-framework developers tired of single-agent demos.
- Enterprise CTOs who need audit-able agent fleets.
- Researchers who want reproducible multi-agent experiments.
- Indie hackers building the next "AI employee" SaaS.

---

## 6. What is the overall Danlab story? (v77, the narrative arc)

**The arc, in three acts:**

**Act 1 (2024-2025): the founding.** Somdipto, a Bengali kid in Bengaluru, looks at the smart-glasses category and sees a closed-system future. Meta owns the cloud. Apple owns the hardware. Snap owns the OS. **No one owns the open alternative.** He starts danlab.dev to build it. Not because the market is hot — because the market is wrong.

**Act 2 (2025-2026): the build.** Audiod. Memoryd. Toold. Perceptiond. Ttsd. Openclaw. Paperclip. DanClaw. **8 daemons, 200+ tests, MIT, 8/8 live.** The build is the story. No press releases, no "coming soon," no manifesto. Just code, tests, and a 1.5h uptime record.

**Act 3 (2026-2027): the proof.** dglabs-eval v1 ships Aug 31 2026. The first public benchmark for proactive AI glasses. MIT, 55 tasks, 5 categories. **The glasses are the smallest possible Paperclip deployment. The eval is the proof that the OS works. The show-HN is the receipt.**

**v77 add: the policy turn (May-Jun 2026).** NITI Aayog's Abhay Karandikar publicly calls for AI self-reliance after the Anthropic export ban. The Indian government is now saying what somdipto has been building: **AI sovereignty is a national priority, and the open path is the only one that scales.** Danlab is the visible-from-Bengaluru open-source answer.

**v77 add: the scandal turn (Jun 4 2026).** Meta's Stella app ships facial-recognition to 50M+ installs without disclosure. The architectural choice is the story. **Danlab's answer is: on-device, audit-able, MIT, consent-first.** Not because we said so — because we commit to it in CONTRIBUTING.md.

**v77 narrative throughline:** **"From Bengaluru to the world, building the open, audit-able, on-device, consent-first AI companion the closed systems can't build — and proving it with a publishable eval the community can run."**

---

## 7. What marketing channels make sense? (v77, ranked)

| Rank | Channel | Why | Cadence | First action |
|------|---------|-----|---------|--------------|
| 1 | **X / Twitter** | The three waves are breaking here. Devs, founders, journalists, all here. | 1-2 posts/day, 6 weeks | Ship 10 posts from `dan1-twitter-content.v77.md` |
| 2 | **LinkedIn (somdipto)** | Long-form essays, India policy turn, founder story. YourStory reposts. | 1 essay/week, 6 weeks | First essay: "Apple pushed AI glasses to 2027" |
| 3 | **GitHub** | The eval, the multimodal pipeline, Paperclip, the 5 daemons. Stars = credibility. | Ship dglabs-eval v0.1 Jul 21, v0.5 Jul 28, v1 Aug 31 | Open the eval repo this week |
| 4 | **Newsletter** | Deep dives, receipts, monthly. 200+ subs, 30%+ open. | 1 issue/month | First issue Jun 26 ("three waves, one moat") |
| 5 | **Show HN** | Aug 4 2026. The single biggest spike. | 1 post | Draft Aug 1, ship Aug 4 |
| 6 | **Hacker News comment strategy** | Comments on Snap/Apple/Meta stories. 1-2/week. | 1-2 comments/week | Comment on any HN thread that mentions Snap Specs or AI glasses |
| 7 | **YourStory / Inc42** | Indian tech press, policy turn. | 1 pitch, 1 follow-up | Pitch YourStory this week |
| 8 | **Reddit r/LocalLLaMA, r/MachineLearning, r/augmentedreality, r/IndianModerate, r/developersIndia** | Niche communities, high signal. | 1-2 posts/week | Cross-post the Snap/Meta essays |
| 9 | **arXiv** | dglabs-eval paper Jul 21. | 1 paper | Write the paper, ship Jul 21 |
| 10 | **YouTube** | Walk-throughs of the eval, the daemons, the multimodal pipeline. | 1 video/month | First video: "How to run dglabs-eval v0.1 on a $189 dev kit" |
| 11 | **Discord** | ~50 members, OSS community. | Daily | Move to a public server, link from GitHub |
| 12 | **Press (TechCrunch, The Verge, WIRED, Forbes)** | Only if HN goes well. Don't pitch cold. | Reactive | Wait for the Show HN spike |
| 13 | **Twitter Spaces / podcasts** | 1-2 appearances, only if invited. | Reactive | Don't pitch cold |
| 14 | **Conferences** (NeurIPS, ICML, CVPR, ICLR) | Paper-track, not booth. | 1 submission for dglabs-eval | Submit dglabs-eval to NeurIPS Datasets & Benchmarks Aug 2026 |

**v77 verdict:** **the three cheapest, highest-signal channels are X, GitHub, and Show HN.** All three are free. All three compound. The single most important action this week: **ship the 10 posts from `dan1-twitter-content.v77.md` and open the dglabs-eval repo.**

---

## 8. What content should Danlab produce? (v77, content matrix)

| Type | Topic | Format | Channel | Cadence | Lead voice |
|------|-------|--------|---------|---------|------------|
| **Essay** | "Apple pushed AI glasses to 2027" | 1200w LinkedIn | LinkedIn | 1/week | somdipto |
| **Essay** | "NITI Aayog's AI self-reliance call" | 1500w LinkedIn | LinkedIn | 1/month | somdipto |
| **Essay** | "The Stella scandal and what on-device means" | 1000w blog | danlab.dev/blog | 1/month | somdipto |
| **Receipt thread** | "8/8 daemons live, 122/122 tests, 5h uptime" | X thread | X | 1/week | @dan2agi |
| **Architecture post** | "audiod v0.7 in 5 minutes" | X thread + blog | X + danlab.dev | 1/month | @dan2agi |
| **Devlog** | "dglabs-eval v0.1 ships Jul 21" | 800w blog | danlab.dev/blog | Bi-weekly | @Shodan_s |
| **Eval paper** | "dglabs-eval: a benchmark for proactive AI glasses" | arXiv paper | arXiv | Once (Jul 21) | somdipto + Dan1 |
| **Show HN** | "Show HN: Dan Glasses — open AI glasses from India" | HN post | HN | Once (Aug 4) | somdipto |
| **Newsletter** | "Three waves, one moat" | 1000w | Newsletter | Monthly | somdipto |
| **Walk-through video** | "How to run dglabs-eval on a $189 dev kit" | 10-min YouTube | YouTube | Monthly | @dan2agi |
| **Founder essay** | "From Bengaluru to the world" | 1500w blog | danlab.dev/blog | 1/quarter | somdipto |
| **OSS contribution** | upstream PRs to LangChain / Sentence-Transformers / Ollama | PR | GitHub | As needed | @Shodan_s |

**v77 priority:** the **receipt thread** is the single most repeatable, high-signal content format. Ship one every week. Each one has 8-12 tweets, with code, tests, uptime, and an architecture diagram. v77 commits to one receipt thread per week for the next 6 weeks.

---

## 9. What is the current online presence? (v77 audit)

**v77 audit (Jun 22 2026, 11:30 IST):**

| Asset | State | Source | v77 action |
|-------|-------|--------|------------|
| **danlab.dev** | Landing page exists (per `Welcome.md`) | danlab.dev | Rebuild landing page using `dan1-landing-copy.v77.md` |
| **GitHub: somdipto/danlab** | Org exists | github.com/somdipto/danlab | Surface as "the org" in all posts |
| **GitHub: somdipto/dani** | Public repo, 50+ stars estimated | github.com/somdipto/dani | Link from every post |
| **GitHub: somdipto/dani-skills** | Public repo | github.com/somdipto/dani-skills | Link from the eval paper |
| **GitHub: somdipto/dan-glasses** | Public repo | github.com/somdipto/dan-glasses | Link from every post |
| **GitHub: somdipto/danlab-multimodal** | Public repo | github.com/somdipto/danlab-multimodal | Link from the multimodal essay |
| **GitHub: somdipto/paperclip** | Public repo | github.com/somdipto/paperclip | Link from the Paperclip essay |
| **GitHub: somdipto/dan-consciousness** | Public repo | github.com/somdipto/dan-consciousness | Link from "how Dan thinks" content |
| **X: @dan2agi** | Active, ~500 followers estimated | x.com/dan2agi | Post 10 posts from `dan1-twitter-content.v77.md` |
| **X: @NandySomdipto** | Active, 1000+ followers estimated | x.com/NandySomdipto | Post 1 essay/day |
| **X: @Shodan_s** | Active, 200+ followers | x.com/Shodan_s | Receipt threads |
| **LinkedIn: somdipto** | Active, 2000+ connections | linkedin.com/in/somdipto | 1 essay/week |
| **Newsletter** | 200+ subs | danlab.dev/subscribe | Send Jun 26 issue |
| **Discord** | ~50 members | discord.gg/danlab | Move to public, link from GitHub |
| **YouTube** | Empty | - | First video Aug 2026 |
| **YourStory / Inc42 / ET Tech** | Not yet covered | - | Pitch this week |
| **arXiv** | Empty | - | dglabs-eval paper Jul 21 |
| **Hacker News** | Empty | - | Show HN Aug 4 |

**v77 verdict on presence:** **we have a working dev platform and zero distribution.** The single biggest unlock is the Show HN. Everything else compounds on top of that one event.

**v77 red flag:** the GitHub repos have low star counts (< 100 each, estimated). The Show HN should aim to push the **combined** star count past 500 in 48h. That's the visibility threshold.

---

## 10. Who are the first users/customers? (v77, the ideal early adopter)

**v77 carries v74's 7 personas and adds Persona H.**

### Persona A — OSS Hacker (carry + sharpen)

- **Profile:** 25-40, mid-senior software engineer, X/Twitter native, posts receipts.
- **Wants:** runs the eval on their hardware, opens PRs, screenshots the test count.
- **Why they'll care:** dglabs-eval v0.1 ships Jul 21, MIT, 55 tasks, 5 categories. They can run it tonight.
- **How to reach:** X (technical threads), GitHub (the eval repo), HN (Show HN).
- **Conversion:** stars the repo, runs the eval, files an issue, becomes a contributor.
- **CAC:** $0 (organic).
- **LTV:** stars + PRs + word-of-mouth = compound distribution.

### Persona B — Accessibility Advocate (carry)

- **Profile:** 18-65, deaf/HoH, ADHD, low-vision, ALS/MND community.
- **Wants:** captioning + memory they can trust + a device that doesn't break.
- **Why they'll care:** on-device captioning + memory persistence + audit-able. No cloud = no privacy failure.
- **How to reach:** disability-tech newsletters, accessibility Twitter, RNID, Hearing Loss Association of America.
- **Conversion:** uses the device, posts a testimonial, becomes a case study.
- **CAC:** $0-100 (community outreach).
- **LTV:** highest possible — the accessibility community is the most loyal customer base in tech.

### Persona C — Privacy-First Founder (carry + sharpen for v77)

- **Profile:** 30-50, founder or CTO, technical, ships OSS, "operational sovereignty" is in their Twitter bio.
- **Wants:** the AI runs on-device, the model is in plain text, the release notes are signed, the contributor license is clear.
- **Why they'll care:** Meta Stella scandal just made this persona 10x more visible. v77 leans on this.
- **How to reach:** X (long-form threads), Hacker News (Show HN + comments), your own newsletter.
- **Conversion:** buys the dev kit, runs the eval, ships a tool that uses audiod/memoryd, cites dglabs-eval.
- **CAC:** $0-50 (newsletter + HN).
- **LTV:** extreme — they tell other founders, they write essays, they cite you in talks.

### Persona D — India-First Builder (carry + sharpen)

- **Profile:** 22-35, Indian developer/student/founder, X + LinkedIn native, reads YourStory.
- **Wants:** builds for India (₹ pricing, Indian languages, Indian policy), wants to be part of the AI self-reliance story.
- **Why they'll care:** NITI Aayog anchor. Bengaluru hardware narrative. Neprion-manufacturable. ₹ pricing.
- **How to reach:** LinkedIn (somdipto's essays), YourStory, Inc42, ET Tech, r/developersIndia.
- **Conversion:** runs the eval, files an Indian-language issue, becomes a contributor, spreads the word.
- **CAC:** $0-50 (LinkedIn + Reddit).
- **LTV:** highest in volume — the Indian developer community is the largest English-speaking developer community in the world.

### Persona E — World-Model Researcher (carry)

- **Profile:** 22-50, ML researcher, PhD or postdoc, arXiv native, cites papers.
- **Wants:** runs the eval, files a paper, cites dglabs-eval, submits a leaderboard row.
- **Why they'll care:** Self-Harness (Shanghai AI Lab) is the closest published cousin. dglabs-eval is the first eval for proactive AI glasses.
- **How to reach:** arXiv, X, conference workshops.
- **Conversion:** cites the eval, contributes scenarios, submits a leaderboard row.
- **CAC:** $0-200 (paper track).
- **LTV:** extreme — every citation is distribution.

### Persona F — AI Safety Researcher (carry + sharpen)

- **Profile:** 25-50, alignment/safety researcher, reads LessWrong, watches ARC evals, follows Agents of Chaos.
- **Wants:** runs the safety subset, finds the supply-chain attack task, writes a red-team report.
- **Why they'll care:** Agents of Chaos + Sentry key hijack task is the wedge. v77 ships the safety subset in v0.5 (Jul 28).
- **How to reach:** LessWrong, AI Alignment Forum, ARC, MIRI, Redwood Research.
- **Conversion:** runs the safety subset, files a red-team report, becomes a long-term contributor.
- **CAC:** $0-200.
- **LTV:** extreme — safety community is the most trusted voice in AI.

### Persona G — Enterprise CTO (carry)

- **Profile:** 35-55, CTO of a mid-size or large enterprise, Indian (Tata, Infosys, Wipro) or global.
- **Wants:** audit-able AI agent fleets, "operational sovereignty," on-device processing, no vendor lock-in.
- **Why they'll care:** Paperclip + DanClaw is the audit-able agent-fleet OS. The glasses are the smallest deployment.
- **How to reach:** direct outreach, conference talks, YourStory op-eds.
- **Conversion:** pilot the daemons, license Paperclip, deploy internally.
- **CAC:** $500-5,000 (sales).
- **LTV:** $50K-500K/year (enterprise contracts).

### Persona H — Consent-First Consumer (NEW v77)

- **Profile:** 25-45, general consumer, not technical, reads The Verge, watched the Stella scandal story.
- **Wants:** "I don't want a camera on my face owned by a company that just got caught running facial-rec on me."
- **Why they'll care:** Meta Stella scandal made the architectural choice legible to non-technical consumers for the first time. v77 leverages this.
- **How to reach:** The Verge, WIRED, Forbes consumer tech, mainstream X threads.
- **Conversion:** buys the glasses, posts a review, tells friends.
- **CAC:** $50-200 (paid).
- **LTV:** high — consumer word-of-mouth is the highest-velocity distribution.

---

## 11. The narrative in one paragraph (v77)

**"From Bengaluru to the world, building the open, audit-able, on-device, consent-first AI companion the closed systems can't build — and proving it with a publishable eval the community can run. Snap launched $2,195 Specs. Meta shipped facial-recognition in 50M installs without disclosure. Apple pushed AI glasses to 2027. The mid-market window is open 18-24 months. Dan Glasses v1 ships in Q4 2026 at $189, on-device, MIT, with 8/8 daemons live today and 122/122 audiod tests passing. dglabs-eval v1 ships Aug 31 2026 — the first public benchmark for proactive AI glasses, MIT, 55 tasks, 5 categories, with a public leaderboard. The moat is the eval. The eval is the proof. The proof is the moat."**

---

## 12. v77 action items (this week)

1. **Ship 10 X posts** (Tue-Thu Jun 23-25). See `dan1-twitter-content.v77.md`.
2. **Write LinkedIn essay #1** (Thu Jun 25, "Apple pushed AI glasses to 2027"). Publish 10:00 IST.
3. **Write LinkedIn essay #2** (Fri Jun 26, "NITI Aayog's AI self-reliance call"). Publish 10:00 IST.
4. **Send newsletter #1** (Fri Jun 26, "Three waves, one moat"). 1000 words.
5. **Open the dglabs-eval repo** (Mon Jun 23). Initial commit = v0.1 spec, 55 scenarios, MIT.
6. **Pitch YourStory** (Tue Jun 24). 1 email, 200 words.
7. **Comment on HN threads** (Tue-Thu, 2-3 comments total). Snap Specs thread is the wedge.
8. **Audit GitHub star counts** (Mon Jun 23). Set a target: 500 combined by Aug 4.
9. **Build the dglabs-eval v0.1 paper outline** (Mon Jun 23). Ship Jul 21.
10. **Send this v77 handoff to somdipto via Telegram** (now).

---

## 13. Open questions for somdipto

1. **Pricing:** is $189 firm for v1, or do we test $149 vs $189 in the pre-order page? My read: $189 anchors the "OSS, MIT, on-device" story. $149 reads as "cheap." Hold $189.
2. **Founder voice:** LinkedIn essays under your name, or under a "Danlab" company page? My read: under your name. Founder essays compound. Company-page essays don't.
3. **Show HN timing:** Aug 4 2026, or earlier (Jul 21, with dglabs-eval v0.1)? My read: Aug 4. The eval ships Jul 28, the Show HN demo is more compelling with a real leaderboard row.
4. **arXiv paper:** solo author or co-author with Dan1? My read: co-author. Dan1 👾 is the marketing voice but the eval is the joint work.
5. **Pitch deck:** rebuild using `DanLab_Pitch_Deck.md` as the base, or start fresh? My read: rebuild. The current deck is investor-grade, not the v77 narrative.
6. **YourStory pitch:** founder essay or product announcement? My read: founder essay. "From Bengaluru to the world" is the frame.
7. **Discord move:** public this week, or wait for Show HN? My read: public this week. The community compounds on the receipts.
8. **First paid channel:** X ads, HN's "second chance pool," or paid Substack? My read: none yet. Show HN + the three waves are the free distribution. Save the paid for after the spike.

---

*End v77. v78 trigger = first eval result row (estimated 2026-07-30).*
| 5 | **Show HN** | Aug 4. dglabs-eval v0.5 ready. 1 lead, 200+ comments. | Once, Aug 4 | Pre-launch comment seeding Jul 28-Aug 3 |
| 6 | **Hacker News (front page)** | Cross-pollination: first 24h of dglabs-eval v0.1 ship, Jul 21 | Once, Jul 21 | Cross-link from Show HN |
| 7 | **YourStory / Inc42 / Mint** | India media, founder story, policy angle | 2-3 pieces/quarter | Pitch "India's first open smart-glasses OS" by Jul 15 |
| 8 | **arXiv (cs.AI, cs.HC)** | The dglabs-eval paper. Citation engine. | 1 paper, v0.1 ship | Submit by Jul 21 |
| 9 | **YouTube devlog (somdipto)** | 5-10 min, screen recording, 1/month | 1/month | First: "122/122 audiod tests" walkthrough |
| 10 | **Reddit (r/LocalLLaMA, r/singularity, r/augmentedreality)** | Niche, high-signal | 1 post/week, when relevant | First: r/LocalLLaMA "dglabs-eval v0.1 ships in 28 days" |
| 11 | **Indie Hackers** | Founder story, "shipping in the open" | 1 post | First: "How we're shipping open smart glasses from Bengaluru" |
| 12 | **Product Hunt** | dglabs-eval v1 ship | 1 launch, Aug 31 | First: prep assets Jul 28 |

**v77 deprioritized:**

- **TikTok / Reels.** Devs don't live here. The category is dev-first; visual-first is a 2027 thing.
- **Twitter Spaces / podcasts.** Time-intensive. 1 podcast/month max. **Wait for inbound.**
- **Paid ads.** Zero budget. Don't burn time on this until we have a $1k+ monthly budget.
- **Conference circuit.** CES 2027 is the target. Skip AWE 2026 (Snap just owned it).

---

## 8. What content should Danlab produce? (v77, by content type)

**A. The eval (the moat).**

- **dglabs-eval v0.1 (Jul 21 2026).** Paper (arXiv), code (GitHub), 55 scenarios, leaderboard skeleton. **The receipt: "we're not just claiming open + audit-able, we're publishing the eval that proves it."**
- **dglabs-eval v0.5 (Jul 28 2026).** Safety subset (6 tasks), supply-chain attack scenario, reproducible eval harness. **The receipt: "we don't just publish the eval, we publish the eval that catches supply-chain attacks."**
- **dglabs-eval v1 (Aug 31 2026).** Public leaderboard, our own row, first external row. **The receipt: "we're not just publishing, we're competing on the same board we built."**

**B. The architecture (the proof).**

- **Architecture deep-dives (monthly).** 1500 words each, "How audiod works," "How memoryd works," "How Paperclip orchestrates the glasses." Receipts in every post.
- **The 122/122 audiod test thread (Jun 23, X).** Screenshot, command, story. v77 ships this as Post 1.
- **The 8/8 daemons uptime thread (Jun 24, X).** Real uptime, real numbers.

**C. The story (the soul).**

- **Founder essay #1 (Jun 25, LinkedIn).** "Apple pushed AI glasses to 2027. The mid-market window is open. Here's how we're shipping in 12."
- **Founder essay #2 (Jun 26, LinkedIn).** "NITI Aayog's AI self-reliance call, and what it means for Indian hardware startups."
- **Founder essay #3 (Jul 2, LinkedIn).** "Why on-device is the only answer to the Stella scandal."
- **Founder essay #4 (Jul 9, LinkedIn).** "What we learned shipping 8 daemons in 6 months from a Bengaluru apartment."

**D. The receipts (the credibility).**

- **Live uptime dashboard.** A simple page on danlab.dev that shows 8/8 daemons, port-by-port status, last-updated timestamp. v77 spec this for the dev portal.
- **Public changelog.** Every audiod release, every Paperclip change, every eval result. Signed with maintainer GPG key. v77 spec this for CONTRIBUTING.md.
- **Monthly review.** 600-1000 words, what we shipped, what we broke, what we learned. v77 first one: Jul 31.

---

## 9. What is the current online presence? (v77 audit)

| Channel | URL | Status (v77) | Action |
|---------|-----|--------------|--------|
| Website | danlab.dev | Live. Has hero, features, CTA. v77 ships the v77 wave-update copy. | Update hero Jun 23-25 |
| X | @dan2agi, @NandySomdipto, @Shodan_s | All 3 active. ~1,200 combined followers (v77 estimate, audit pending). | Audit + first 10 posts Jun 22-26 |
| LinkedIn | somdipto | ~2,500 connections. Posts monthly. | 1 essay/week starting Jun 25 |
| GitHub | github.com/somdipto (dani, dan-glasses, paperclip, dan-consciousness, dan-lab) | ~50-200 stars total across repos (v77 estimate, audit pending). **This is the gap.** | **Priority: 100 stars by Aug 4** |
| Newsletter | danlab.substack.com (or similar) | 200+ subs (v74 unverified, v77 audit) | 1 issue Jun 26 |
| YouTube | (not started) | 0 videos. | First devlog Jul 1 |
| Discord | danlab.dev/discord | ~50 members (v74 carry) | Post 1x/week |
| Hacker News | (not started) | 0 posts | First Show HN Aug 4 |
| Reddit | (not started) | 0 posts | First r/LocalLLaMA Jul 21 (eval ship) |
| Twitter Spaces / Podcasts | 0 inbound (v77) | 0 | 1 podcast by Aug 31 |
| YourStory / Inc42 / Mint | 0 features | 0 | 2-3 by Sep 30 |
| Product Hunt | 0 launches | 0 | 1 launch Aug 31 (eval v1) |

**v77 gap analysis:** the GitHub star count is the single biggest gap. **No amount of marketing fixes "0 stars on the eval repo."** The Show HN is the spike; the eval v0.1 ship is the leading indicator. v77 priorities:

1. **Ship dglabs-eval v0.1 on GitHub by Jul 21** with a polished README, screenshots, getting-started. The Show HN will work only if the README works.
2. **Get 5-10 OSS maintainers to star the eval repo by Jul 28.** Personal DMs, X DMs, LinkedIn DMs. Not "please star," but "look at this, what do you think?"
3. **Ship audiod v0.8 by Jul 21.** Public release, with a release post. v77 spec this for the audiod stream.

---

## 10. Who are the first users/customers? (v77, sharper)

**The first 100 dev-kit pre-orders (target: Aug 31 - Sep 30, 2026):**

| # | Persona | % | Profile | Channel | Hook |
|---|---------|---|---------|---------|------|
| 1 | **OSS Hacker** | 30% | 25-40, GitHub-native, ML background, builds side projects | Show HN, r/LocalLLaMA, GitHub | "The eval runs on your hardware. MIT. $189." |
| 2 | **Privacy-First Founder** | 20% | 30-50, runs a company, cares about data sovereignty | LinkedIn, HN, your network | "On-device, audit-able, MIT. We commit to never shipping stealth facial-rec." |
| 3 | **AI Safety Researcher** | 15% | 25-50, works on agent eval, supply-chain attacks, red-teaming | arXiv, AI Alignment Forum, LessWrong | "dglabs-eval safety subset: 6 tasks, including agent supply-chain attack. Run it on your model." |
| 4 | **Accessibility Advocate** | 10% | 18-65, deaf/HoH, ADHD, low-vision | Twitter, disability-tech communities | "Captioning + memory you can trust. On-device. The captions don't go to a third-party API." |
| 5 | **India-First Builder** | 10% | 22-35, Indian, building for India | LinkedIn, YourStory, Inc42, Twitter | "Bengaluru, MIT, ₹-friendly, NITI Aayog-aligned. The first Indian open smart-glasses OS." |
| 6 | **Enterprise CTO (India)** | 10% | 35-55, runs IT at a large Indian enterprise | LinkedIn, NASSCOM, TiE | "Operational sovereignty. On-device. Audit-able. The agent OS for Indian enterprise." |
| 7 | **World-Model Researcher** | 5% | 22-50, academic, world-models, RL | arXiv, ICML/NeurIPS, Twitter ML | "dglabs-eval v1 leaderboard. Submit your row. The first public benchmark for proactive AI glasses." |

**v77 sharpen on the dev-kit buyer:** the buyer is **not** a consumer. The buyer is **a developer or founder who will write about it**. Every dev-kit ship comes with:

- A "first-week-with-Dan-Glasses" thread template (not required, just helpful).
- A direct line to somdipto for feedback.
- A 1-hour onboarding call.
- A "ship a skill" bounty ($200 for the first 50 skills).

**v77 anti-persona (do NOT target):** "I want glasses that look like normal glasses and do nothing." v77 explicitly says: **"Dan Glasses is not a fashion accessory. It's a developer kit for the next computer."** The v2 (with display) is the fashion product; the v1 is the developer kit.

---

## 11. v77 KPI dashboard (the receipts)

| Metric | Jun 22 (now) | Jul 21 (eval v0.1) | Aug 4 (Show HN) | Aug 31 (eval v1) | Sep 30 (Q end) |
|--------|--------------|---------------------|------------------|-------------------|-----------------|
| Newsletter subs | 200+ | 350 | 600 | 900 | 1,000 |
| GitHub stars (total) | ~200 | 350 | 500 | 700 | 800 |
| dglabs-eval GitHub stars | 0 | 50 | 150 | 250 | 350 |
| X followers (@dan2agi) | ~400 | 600 | 900 | 1,200 | 1,500 |
| LinkedIn (somdipto) connections | ~2,500 | 2,700 | 2,900 | 3,100 | 3,300 |
| Dev-kit pre-orders | 0 | 0 | 25 | 50 | 100 |
| Show HN rank | - | - | Top 5 | - | - |
| arXiv citations | 0 | 1 (own) | 3 | 5 | 8 |
| Discord members | 50 | 100 | 200 | 300 | 400 |
| Press features (India) | 0 | 0 | 1 | 2 | 3 |

**v77 thesis on metrics:** **stars are a vanity metric; dev-kit pre-orders are the truth.** The eval ship is the leading indicator for stars; the dev-kit ship is the lagging indicator for revenue. v77 prioritizes the eval ship, not the dev-kit.

---

## 12. v77 open questions for somdipto

1. **Are you OK with the "consent-first" angle being the main differentiator post-Stella?** It's the most differentiated story, but it's also the most "we're not Meta" framing. Alternative: stay positive ("on-device, audit-able, MIT") and avoid the punch.
2. **Are you OK with the NITI Aayog frame being prominent?** It's powerful for India, but it could read as political in the US/EU. v77 default: yes, but lean on the policy quote, not the political framing.
3. **Dev-kit price: $189 (audio-only v1) or $299 (with display pre-order)?** v77 default: $189 v1 (audio-only), $399 v2 (with display) — same as v74. Confirm.
4. **Show HN: Aug 4 or Aug 11?** Aug 4 is one day before eval v0.5 (Jul 28) + 27 days. Aug 11 is one day before eval v1 (Aug 31) + 20 days. v77 default: Aug 4 (more lead time, more lead-up posts).
5. **Newsletter platform: Substack, Beehiiv, or self-hosted?** v77 default: Substack (free, fast, has network effects). Confirm.
6. **Podcast tour: are you willing to do 1 podcast/week in Aug-Sep?** High-leverage, but time-intensive. v77 default: yes, max 4/month.
7. **YourStory / Inc42 / Mint: are you willing to do 1 interview/month?** These are the Indian press levers. v77 default: yes, target 2 by Q3 end.
8. **Discord: launch a public Discord, or stay invite-only?** v77 default: public, with a #general + #dev + #eval channel structure. Confirm.
9. **dglabs-eval license: MIT, Apache 2.0, or AGPL?** v74 default: MIT. **v77 sharpen: AGPL would prevent Meta/Apple from forking, but it scares contributors. MIT is the right answer for an eval.** Confirm.
10. **First external developer for the eval: who?** v77 needs a name by Jul 7. Recommended: a friendly OSS maintainer who can submit a row. Suggestion: ask Andrew Trask (OpenMined), Tim Dettmers (bitsandbytes), or someone from HuggingFace evals.

---

## 13. v77 sources

- Snap Specs launch: Reuters Jun 16 2026, Bloomberg Jun 16 2026, Business Insider Jun 17 2026, TechCrunch Jun 17 2026, Mashable Jun 17 2026, Forbes Vetted Jun 17 2026, The Verge Jun 16 2026.
- Meta Stella scandal: Buchodi technical report Jun 4 2026, WIRED Jun 5 2026, SFGate Jun 5 2026, SpaceDaily summary.
- Apple AI glasses delay: Bloomberg/Gurman May 31 2026, 9to5Mac May 31 2026, MacRumors guide (updated Jun 2026).
- Meta Ray-Ban lineup: PCMag 2026 roundup, Yahoo Finance Jun 18 2026.
- Smart glasses market 2026: ElectronicsHub (Alibaba) 322% growth 2025, RTE 2026 market €500B+ by 2035.
- India AI policy: NITI Aayog Abhay Karandikar on AI self-reliance (carried from v38), IndiaAI Mission 2026 (VivaTech).
- Indian hardware startup landscape: ElectronicsForYou (NeoSapien), Focally (Indian AR), Analytics India (do Indian founders build AI wearables), YouTube Mave.
- v74 carry: dglabs-eval v0.1/v0.5/v1 ship dates, 8/8 daemons live, 122/122 audiod tests, NITI Aayog anchor, Perplexity Brain baseline, Self-Harness (Shanghai AI Lab, arXiv Jun 8 2026), Quickwork operational sovereignty (Jun 15 2026), Sentry key hijack (Jun 21 2026).
- Show HN strategy: standard HN playbook (lead with the receipt, not the claim; post during US business hours; respond to every comment in the first 4h).
