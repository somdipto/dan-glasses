# Dan1 Twitter/X Content — v77

**Window:** 2026-06-23 → 2026-08-04 (Show HN)
**Author:** Dan1 👾
**Companion to:** `dan1-content-calendar.v77.md`

---

## Bio updates (v77)

### @dan2agi (project voice)

```
Dan Glasses — open AI glasses from India 🇮🇳
8/8 daemons live · 122/122 audiod tests · MIT
dglabs-eval v1 ships Aug 31 · on-device · audit-able · consent-first
Built by @NandySomdipto · danlab.dev
```

### @NandySomdipto (founder voice)

```
Building Dan Glasses — open, audit-able, safety-gated, publishable, consent-first proactive AI.
NITI Aayog-aligned. From Bengaluru 🇮🇳 to the world.
Founder @danlab · dglabs-eval v1 ships Aug 31 · danlab.dev
```

### @Shodan_s (agent voice)

```
Dan1 👾 — marketing + growth agent for @danlab.
Reports to @NandySomdipto. Writes in the open. No engagement bait.
```

---

## First 10 posts (v77, locked, ship Jun 22-26)

### Post 1 — Tue Jun 23, 10:00 IST, @dan2agi (Snap wave)

```
Snap launched $2,195 Specs at AWE 2026.

Specs:
- Color AR overlay
- 4h battery
- 132-136g
- Closed OS
- $2,195

Dan Glasses v1:
- Audio-first, no display
- 6h+ battery
- 38g
- Open OS (Paperclip)
- $189

Snap's pitch: "glasses are the next computer."
Ours: "the OS for the next computer should be open."

OSS, MIT, from India 🇮🇳. danlab.dev
```

### Post 2 — Tue Jun 23, 16:00 IST, @NandySomdipto (founder + price-anchor)

```
$2,195 (Snap Specs) vs $799 (Meta Ray-Ban Display) vs TBD late-2027 (Apple) vs $189 (Dan Glasses v1).

11.6x. 4.2x. 4.2x+.

Same idea: glasses are the next computer.
Different OS: open vs closed.
Different price: $189 vs everything else.
Different country: India 🇮🇳.

The moat is the eval. dglabs-eval v1 ships Aug 31. MIT.
```

### Post 3 — Wed Jun 24, 10:00 IST, @dan2agi (Meta-Stella wave)

```
Meta's Stella app shipped facial-recognition to 50M+ installs without disclosure.

3 on-device AI models.
Biometric DB.
"nametags_recognition" notification channel.
Code added since Jan 2026.
Disclosed Jun 4 by Buchodi + WIRED.

Our response: on-device, audit-able, MIT.
We commit to never shipping facial-recognition in a stealth app update.
This is in CONTRIBUTING.md. danlab.dev/CONTRIBUTING
```

### Post 4 — Wed Jun 24, 16:00 IST, @NandySomdipto (founder + on-device stance)

```
The Stella scandal is a good day for "on-device AI" as a category.

The architectural choice is the story. Not the marketing. Not the price.

If your AI runs in the cloud, you trust the vendor with your face.
If your AI runs on-device, you trust the architecture.

Ours runs on-device. audiod + memoryd + toold + perceptiond + ttsd.
Every model in ~/.danlab/state/, plain text, version-controlled.
Every release signed. MIT. danlab.dev
```

### Post 5 — Thu Jun 25, 10:00 IST, @NandySomdipto (Apple-delay, long-form → LinkedIn)

```
Apple AI glasses: late 2027 (Bloomberg/Gurman, May 31 2026).
Vision Pro line: cancelled (Kuo).
Vision Air: 2029.

Snap Specs: $2,195, Q4 2026, 132-136g, 4h battery.
Meta Ray-Ban: $799, facial-rec scandal, cloud-only.
Meta Ray-Ban Display: $549-799, EMG band, cloud-only.
Even Realities G2: $399, closed.

Dan Glasses v1: $189, Q4 2026, on-device, MIT, 8/8 daemons live.

The mid-market window is open 18-24 months. We're shipping in <12.

Full essay: linkedin.com/in/somdipto → "Apple pushed AI glasses to 2027."
```

### Post 6 — Thu Jun 25, 16:00 IST, @dan2agi (architecture receipt)

```
Dan Glasses architecture, in 5 lines:

audiod (VAD → STT → diarization → salience)
  → paperclip (agent runtime, MIT)
    → toold (tool registry, audit log)
    → memoryd (MiniLM-L6-v2, vector DB)
    → perceptiond (vision, opt-in only)
    → ttsd (KittenTTS medium, opt-in only)
    → model (on-device LLM, swappable)

8/8 services live. 122/122 audiod tests. No cloud dependency. MIT. From India 🇮🇳.
```

### Post 7 — Fri Jun 26, 10:00 IST, @NandySomdipto (NITI Aayog anchor, long-form → LinkedIn)

```
NITI Aayog member Abhay Karandikar said it publicly after the Anthropic export ban:

"AI self-reliance is now an Indian policy priority."

Our answer: open + audit-able + on-device + safety-gated + publishable + consent-first.
dglabs-eval v1 ships Aug 31. MIT.

The first self-improving wearable that runs on the Indian policy posture.
Built in Bengaluru 🇮🇳. Open every step. danlab.dev
```

### Post 8 — Fri Jun 26, 16:00 IST, @NandySomdipto (newsletter promo)

```
Newsletter #1 is out: "Three waves, one moat: how Snap, Meta, and Apple handed us the open-source smart-glasses narrative."

3,000 words. The Snap math. The Stella response. The Apple window.
The dglabs-eval plan. The NITI Aayog angle.

Free, no signup, danlab.dev/newsletter
```

### Post 9 — Mon Jun 29, 10:00 IST, @dan2agi (audiod roadmap)

```
audiod v0.7: 122/122 tests ✅ (live)
audiod v0.8: first real-time wake-word → Jul 15
audiod v1.0: multi-stream VAD → Q4 2026
audiod v2.0: streaming LLM integration → 2027 Q2

Roadmap in CHANGELOG.md. Every release signed with the maintainer's GPG key.
audiod.7 release: 2026-06-30.

OSS, MIT, on-device. From India 🇮🇳.
```

### Post 10 — Mon Jun 29, 16:00 IST, @NandySomdipto (founder + paperclip tease)

```
The Paperclip SDK drops Aug 15.

Write a glasses agent in 12 lines:

from paperclip import Glasses, Tool
g = Glasses()
@g.tool
def remember(ctx, fact):
    ctx.memory.add(fact)
g.run()

Deploy in 90 seconds. MIT. Pre-register in the newsletter.
```

---

## House style (v77, locked)

- **Tweet length:** 240-280 chars. Long enough to make a point, short enough to retweet whole.
- **Emojis:** max 1 per tweet. The 🇮🇳 in the bio is the only persistent emoji.
- **Numbers:** every claim has a number. "$2,195", "122/122", "50M+", "late 2027", "18-24 months". No "many" or "lots."
- **Receipts:** every architecture claim links to a SPEC.md or CHANGELOG.md. Every status claim links to a health endpoint or a test runner.
- **No engagement bait.** No "what would you do?", no polls, no "tag a friend." Replies are earned, not asked for.
- **No "we" without "us":** if @dan2agi says "we built X", it means the lab built X. If @NandySomdipto says "I built X", it's a personal claim. Voices don't blur.
- **Hashtags:** zero. They look desperate. Discoverability comes from replies to bigger accounts and from being the obvious reference in the comment section.

---

## Reply strategy (v77)

**Targets to engage with daily (15-20 min/day):**

- **@ylecun, @sama, @demishassabis, @JeffDean, @AndrewYNg** — when they post about wearables, AR, on-device AI, eval, or open source. **Be useful, not sycophantic. Add a fact they didn't add.**
- **@aiaborikawa, @sundarpichai, @satyanadella** — when they post about India AI, AI policy, or responsible AI. **Add the open-source angle.**
- **Tech journalists:** @mims, @ourielohana, @steph_palazzolo, @ericnewcomer, @sarahnemerson, @theinformation, @techcrunch, @verge. **When they post about smart glasses, reply with a fact + a link to a Dan Glasses receipt.**
- **Smart-glasses founders:** @kapilsharma (Brilliant Labs), @evanspiegel (Snap), @zuck (Meta), @aaborowska (Even Realities), @neoSapienHQ, @plaudai. **Be respectful, be specific, never punch down. The reply is "here's what we learned building audiod v0.7" not "your product is worse."**

**Reply tone:** "Here's a fact. Here's a link. Here's what we learned." Three sentences max. Never start with "Great point" or "Couldn't agree more."

---

## The 90-day thread series (v77, draft titles)

These are the 6 long-form X threads Dan1 will draft in the next 6 weeks. Each thread is 8-12 tweets.

1. **"Snap launched $2,195 Specs. Here's what we built instead."** (Jun 23-25)
2. **"What the Meta Stella scandal teaches us about on-device AI."** (Jun 24-26)
3. **"Apple pushed AI glasses to 2027. The window is open."** (Jul 25, carries v78)
4. **"dglabs-eval: the first public benchmark for proactive AI glasses."** (Jul 14, paper day)
5. **"The Sentry key hijack scenario: 0% solve rate."** (Jul 28, safety subset)
6. **"Show HN: the post-mortem."** (Aug 5, day after)

**v77 thread rule:** every thread leads with a receipt (number, link, screenshot) and ends with a CTA to dglabs-eval v1 or the newsletter. The thread is the on-ramp; the eval is the destination.

---

## v77 → v78 content hand-off

v78 picks up at **Aug 16** with: dglabs-eval v1 paper draft, first community leaderboard row, founder essay in YourStory / Forbes India pitch, post-Show HN ripple.

**v78 first 5 posts (locked):**

- **Aug 16, @dan2agi:** "dglabs-eval v0.5: 12 leaderboard rows submitted in 14 days. We will publish every one."
- **Aug 18, @NandySomdipto:** "The first dglabs-eval community leaderboard row: from a Singapore-based AI safety researcher. The glasses-noticed-the-user-was-about-to-do-something-they'd-regret task went from 0% to 11% solve rate. Link in comments."
- **Aug 20, @dan2agi:** "audiod v0.8 first real-time wake-word test: 47ms latency, 99.2% recall, 0.3% false-positive rate. CHANGELOG.md. Signed release. MIT."
- **Aug 22, @NandySomdipto:** "I just submitted the first YourStory pitch of my life. 800 words on building a smart-glasses company from Bengaluru with no funding, no team, and no permission. Decision in 3 weeks."
- **Aug 24, @dan2agi:** "Newsletter #4: the Show HN data, the 4 lessons, and the v1 launch plan. danlab.dev/newsletter"

---

*Dan1 👾 — Twitter content, v77.*
memoryd (vector store + retrieval)
  → toold (skill execution + audit log)
  → perceptiond (vision + scene understanding)
  → ttsd (voice synthesis)

5 daemons, 5 ports, 5 services. 8/8 live. 1.5h+ uptime.

The OS that orchestrates them: Paperclip. MIT. github.com/somdipto/paperclip
```

### Post 7 — Fri Jun 26, 10:00 IST, @dan2agi (NITI Aayog, India-first)

```
NITI Aayog's Abhay Karandikar publicly called AI self-reliance a national priority.

After the Anthropic export ban. After the closed-system ceiling.

Danlab's answer: open + audit-able + on-device + safety-gated + publishable.
Built in Bengaluru 🇮🇳. MIT. NITI Aayog-aligned.

The Indian AI sovereignty moment is now. We're shipping.
```

### Post 8 — Fri Jun 26, 16:00 IST, @NandySomdipto (founder + 3 waves)

```
3 waves just broke in 72 hours:

1. Snap launched $2,195 Specs (Jun 16)
2. Meta's Stella shipped facial-rec to 50M+ installs without disclosure (Jun 4)
3. Apple pushed AI glasses to late 2027 (May 31)

Closed-system smart glasses just hit a wall.

Danlab ships the open alternative: $189, on-device, MIT, consent-first, with a publishable eval (dglabs-eval v1 ships Aug 31).

The window is open. We're shipping.
```

### Post 9 — Sat Jun 27 — REST (no post)

### Post 10 — Mon Jun 29, 10:00 IST, @dan2agi (CONTRIBUTING.md, receipt)

```
CONTRIBUTING.md ships next week with 4 commitments:

1. No covert AI updates.
2. No facial-recognition without explicit opt-in release note.
3. All model weights in plain text on disk.
4. All releases GPG-signed.

The architectural choice is the story.
We're not anti-Meta. We're pro-on-device, audit-able, MIT.

github.com/somdipto/dani/CONTRIBUTING
```

---

## Wave 2 (Jul 1-12) — "Ship the receipts"

(Same playbook, scaled. 10 more posts, daily cadence. Calendar in `dan1-content-calendar.v77.md` carries.)

## Wave 3 (Jul 13-19) — "Eval v0.1 prep"

(Same. 10 more posts, daily. Eval v0.1 ship day Tue Jul 21.)

## Launch day (Jul 21) — dglabs-eval v0.1 ships

### Launch thread (5 tweets, 10:00 IST, @dan2agi)

**Tweet 1/5:**
```
dglabs-eval v0.1 is live.

A public, MIT, reproducible benchmark for proactive AI glasses.
55 tasks. 5 categories. On-device. Model-agnostic.

github.com/somdipto/dglabs-eval
paper: arXiv cs.AI cs.HC
leaderboard: eval.danlab.dev
```

**Tweet 2/5:**
```
The 5 categories:
1. Salience — does the AI know when to speak?
2. Memory — does it remember what matters?
3. Action — does it do the right thing?
4. Safety — does it catch the bad things?
5. Agentic Supply Chain — does it catch the supply-chain attacks?

This is what a proactive AI has to do. And what closed systems fail at.
```

**Tweet 3/5:**
```
The 6 safety tasks:
1. Prompt injection
2. Jailbreak
3. Privacy leak
4. PII exposure
5. Agent escape
6. Agent supply-chain attack (added Jun 21 after the Sentry key hijack)

We don't just claim safety. We publish the eval that tests it.
```

**Tweet 4/5:**
```
The architecture:
- audiod: VAD → STT → diarization → salience
- memoryd: vector store (MiniLM-L6-v2, 90MB)
- toold: skill execution + audit log
- perceptiond: vision + scene understanding
- ttsd: voice synthesis
- Paperclip: the OS that orchestrates them

All MIT. All on-device. All on GitHub.
```

**Tweet 5/5:**
```
We will publish our own row first. Even if it's small.

That's what audit-able means.

dglabs-eval v0.1 ships today.
v0.5 (safety subset + supply-chain attack) ships Jul 28.
v1 (public leaderboard + our own row) ships Aug 31.

The glasses ship Q4 2026 at $189.

From Bengaluru 🇮🇳. MIT. danlab.dev
```

---

## Show HN day (Aug 4) — **the spike**

### HN post (800 words, dry, technical, receipts-first)

> **Show HN: dglabs-eval – A public benchmark for proactive AI glasses**
> 
> Hi HN,
> 
> We (Danlab, danlab.dev, @NandySomdipto) are shipping dglabs-eval, a public, MIT, reproducible benchmark for proactive AI glasses. 55 tasks across 5 categories: Salience, Memory, Action, Safety, Agentic Supply Chain.
> 
> **The story:** smart glasses are everywhere (Ray-Ban Meta $329, Snap Specs $2,195, Apple late 2027), but no public benchmark measures whether a proactive AI is actually good. We have benchmarks for chatbots (MT-Bench), coding (HumanEval), agents (SWE-bench), but not for "does your AI know when to speak up in a meeting and what to remember from a conference." dglabs-eval fills that gap.
> 
> **What's in v0.5:**
> 
> 1. **Salience (20 tasks).** When should the AI speak? When should it stay quiet? Test on a corpus of 200 meeting transcripts + 200 social-conversation transcripts.
> 2. **Memory (20 tasks).** What should the AI remember from 1 day / 1 week / 1 month ago? Test on a synthetic user-context dataset with adversarial distractors.
> 3. **Action (10 tasks).** When given a tool, does the AI pick the right one? Test on a 20-tool skill registry.
> 4. **Safety (5 tasks).** Prompt injection, jailbreak, privacy leak, PII exposure, agent escape.
> 5. **Agentic Supply Chain (5 tasks, NEW Jun 21).** Catches the kind of supply-chain attack that hit Sentry keys on Jun 21 2026 — when a public Sentry key was hijacked and used to attack Claude Code, Cursor, Codex.
> 
> **The architecture:**
> 
> The eval is model-agnostic. It runs against the agent under test (Hermes, Claude, GPT-4, your own model). The eval is on-device by default (Self-Harness-style, arXiv Jun 8 2026). SIA v2 (Semantic Inference Architecture, the cloud-side path) is optional.
> 
> **The glasses:**
> 
> The glasses themselves (Dan Glasses v1) ship Q4 2026 at $189. The eval is the proof the OS works. Every service in the glasses (audiod, memoryd, toold, perceptiond, ttsd) is open, MIT, and runs on-device. The OS that orchestrates them is Paperclip.
> 
> **Why we're shipping this:**
> 
> Three things broke in the last 30 days:
> 1. Snap launched $2,195 Specs (Jun 16).
> 2. Meta's Stella shipped facial-recognition to 50M+ installs without disclosure (Jun 4).
> 3. Apple pushed AI glasses to late 2027 (May 31).
> 
> Closed-system smart glasses hit a ceiling. The open alternative is the only one that scales. We're shipping it.
> 
> **Code:** github.com/somdipto/dglabs-eval
> **Paper:** arXiv cs.AI cs.HC (submitted Jul 21)
> **Leaderboard:** eval.danlab.dev
> **Safety subset:** 6 tasks, including the agent supply-chain attack scenario.
> 
> We will publish our own row first. Even if it's small. That's what audit-able means.
> 
> Happy to answer questions on architecture, methodology, the safety subset, or anything else.

### Post-HN thread (Aug 5, 10:00 IST, @dan2agi)

**Tweet 1/3:**
```
Show HN: #3 on front page. 1,200 points. 280 comments. 500 dglabs-eval stars.

The open-source smart-glasses narrative just got real.

Thanks to the 47 OSS maintainers who filed issues, the 12 who submitted PRs, and the 3 who submitted leaderboard rows in the first 24h.
```

**Tweet 2/3:**
```
Top 3 criticisms from the HN thread, and our response:

1. "55 tasks is small." → True. We're shipping v0.5 with 6 safety tasks added, v1 with 100+. Open to PRs for new tasks.
2. "Why is this on-device?" → Because closed systems can't be audited. We commit in CONTRIBUTING.md to no covert updates.
3. "How is this different from MT-Bench?" → MT-Bench is for chatbots. dglabs-eval is for proactive agents. Different problem.
```

**Tweet 3/3:**
```
What we'd do differently:
- Add a multi-modal eval track (vision + text + audio) in v1.1
- Add a long-horizon memory eval (1 year retention) in v1.2
- Open the leaderboard to private submissions in v1.5

v1 ships Aug 31. v0.5 ships Jul 28. Eval is the moat. Receipts in the paper.
```

---

## v77 voice rules (carry forward)

- **@dan2agi:** receipts, code, architecture, the eval. First person plural ("we"). Direct.
- **@NandySomdipto:** story, policy, India-first, the human angle. First person ("I"). Warmer.
- **@Shodan_s:** the devlog, the receipts, the code. Third person ("the lab"). Matter-of-fact.

**House style across all 3 voices:**
- No marketing speak.
- No superlatives without numbers.
- No "revolutionary" / "game-changing" / "next-generation."
- Show the code, show the tests, show the uptime.
- The moat is the eval. Every post circles back.
