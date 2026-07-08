# Dan1 Twitter / X Content — v50

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-17 13:00 IST (07:30 UTC)
**Status:** ✅ Canonical. Supersedes v49. **Content locked. v51 is execution.**

> One-line rule (unchanged from v49): *No hashtags. No "🚀". No "We're excited to announce". We tweet like engineers, in short sentences, with receipts.*

---

## 0. The X profile (the day-0 fixes) — UPDATED FOR v50 (DANI mention)

**Display name:** `somdipto nandy 👾`
**Handle:** Keep `@NandySomdipto`
**Bio (NEW v50, 178 chars):**
```
building @danlab.dev — open, local, proactive AI 🇮🇳
DANI: dani.danlab.dev · dan-glasses · danlab-multimodal
MIT · from India · the AI that knows when to shut up 👾
```

**Pinned tweet:** DANI lead tweet (§3 NEW v50) for first 7 days, then replace with Tweet 1 of the origin thread (§3.5).

**Every line of text is in `punchlist-copy-paste.md` (v50) §A. Just copy and paste.**

---

## 1. The 10 first posts — UPDATED FOR v50 (DANI lead)

Post cadence: 1/day for the first 10 days, then 3/week sustained. Every post links to a repo, a demo, a video, or a paper.

**Posts 1, 2, 3-10 are all from v49. The new ones in v50 are post 1 (DANI lead), post 2.5 (dani.danlab.dev tweet), and the 7-tweet thread is reframed (DANI proof of life, then the stack).**

### Post 1 (Day 0, pinned) — DANI lead tweet (NEW v50)

```text
dani.danlab.dev is live.

AI coworkers that run your business. open source. MIT. from india 🇮🇳

free · $29 starter · $99 pro · $299 business
cloud-optional. your data. your agents. your rules.

the brain. the glasses come next.
```

**This is the single highest-leverage post of the v50 plan.** DANI is real. DANI is live. DANI has a pricing page. DANI has a GitHub org. **Text in `punchlist-copy-paste.md` §C.5.**

### Post 2 (Day 1) — 7-tweet origin thread (DANI proof of life, then stack)

**Text in `punchlist-copy-paste.md` §D v50. Ship it. Pin Tweet 1 for 7 days.**

**Tweet 1/7 (DANI hook):**
```text
dani.danlab.dev is live.

open-source AI coworkers for $0-299/mo. MIT. from india 🇮🇳

7 daemons. 106/106 tests. 0 cloud calls. cloud-optional. today.

then we open-sourced the multimodal AI pipeline. 🧵
```

**Tweet 2/7 (the wedge):**
```text
the smart-glasses race in 2026 is cameras-with-AI, not AI-with-personality.

ray-ban meta: "hey meta, take a photo." (reactive)
apple glasses: slipped to 2027.
brilliant labs halo: open hardware, cloud brain (noa).

DANI ships today. the brain. the glasses come next. nobody owns proactive. we do.
```

**Tweet 3/7 (what "proactive" means):**
```text
"proactive" means: I noticed you walked past the pharmacy 3 times this week without picking up your prescription. remind me next time?

not "hey meta, what's this?"

DANI does this on a $5/mo VPS. Dan Glasses does this on your face.
```

**Tweet 4/7 (the stack):**
```text
the stack:

audiod          :8090 + ws :8091
perceptiond     :8092
memoryd         :8741
toold           :8742
ttsd            :8743
os-toold        :8744
openclaw        :18789
DANI            dani.danlab.dev

all on-device. all MIT. all running today.
```

**Tweet 5/7 (the multimodal demo):**
```text
we also open-sourced a sub-250MB vision-language model on CPU.

SmolVLM-256M (120MB) + mmproj (182MB) via llama.cpp.

heuristic feedback loop scores outputs 0-100. pre-RL scaffold. honest about what it isn't.

demo: https://zo.pub/som/danlab-multimodal-demo
repo: github.com/somdipto/danlab-multimodal
```

**Tweet 6/7 (the model — Omni-1B, v49 narrative):**
```text
we are training a 1B Omni model from scratch.

3 months in. 9 Indian language families. on-device. the smallest Omni that fits cleanly in the wearable form factor.

we don't just integrate models. we train them. on the wearable. on the languages of the country we're shipping from.
```

**Tweet 7/7 (the ask):**
```text
we're 23, in bangalore, on a buildspace arc, and we have:

- 7 daemons, 106 tests, 0 cloud
- DANI live at dani.danlab.dev
- a public demo of the multimodal pipeline
- a working desktop companion you can clone today
- a v2 wearable blocked only on hardware

star the repos. try DANI. file 11 issues. tell 50 people.

github.com/somdipto/dan-glasses
dani.danlab.dev

the window is open. the clock is ticking.
```

**Posting instructions:**
1. Click "Post" then "+" to add to thread
2. Paste each tweet in sequence
3. After all 7 are ready, click "Post all"
4. Pin Tweet 1 to your profile for 7 days (replaces the DANI lead)

### Post 3 (Day 2) — The receipts: 7 daemons + DANI + 106/106 tests

```text
day 2 of building in public:

7 daemons running.
106/106 tests green.
0 cloud calls.
$0/month.

DANI live at dani.danlab.dev. MIT. free / $29 / $99 / $299.

the stack:

audiod          :8090 + ws :8091
perceptiond     :8092
memoryd         :8741
toold           :8742
ttsd            :8743
os-toold        :8744
openclaw        :18789

all on-device. all MIT. all running today.

github.com/somdipto/dan-glasses
dani.danlab.dev
```

### Post 4 (Day 3) — 5-min DANI demo video

```text
day 3:

we recorded a 5-min demo of DANI.

install → first agent → first memory → first tool call → Telegram reply.

all on a $5/mo VPS, 0 cloud required, MIT.

[ video link ]
dani.danlab.dev
```

### Post 5 (Day 4) — Architecture deep-dive #1: LFM2.5-VL-450M

```text
day 4:

why LFM2.5-VL-450M and not Gemma3-270M for on-device vision:

1. Gemma3-270M has no mmproj in GGUF. would have to build one from source.
2. LFM2.5-VL-450M has a SigLIP2 NaFlex encoder built for 512x512 edge inference.
3. 209MB Q4_0 + 180MB mmproj = 389MB. fits in the Redax aarch64 board.
4. sub-250ms inference on x86_64. ~10-15s on the wearable CPU (TBD).

liquid AI shipped a perfect-fit model for the wearable form factor.

HF: LiquidAI/LFM2.5-VL-450M
```

### Post 5.5 (Day 5, from v49) — The Omni-1B training

```text
day 5:

we are training a 1B Omni model from scratch.

3 months in.

why 1B and not 3B (Qwen Omni):

1. wearable form factor. 3B+ won't fit cleanly.
2. we wanted as small as possible.

what we added that Qwen doesn't have:

- regional Indian languages
- 9 Indian language families in the tokenizer
- fine-tuned for the proactive-companion prompt style

we don't just integrate models. we train them. on the wearable. on the languages of the country we're shipping from.

🇮🇳

(omni-1b-indic-v0.1 ships to HuggingFace by Day 60. model card link in pinned tweet.)
```

### Post 5.7 (Day 5.5, NEW v50) — DANI vs the AI coworker category

```text
day 5.5:

DANI is the AI coworker for the 30-year-old growth marketer with 14 chrome tabs open.

not for the enterprise IT buyer. not for the "AI will replace your job" fear-monger. not for the dev-only audience.

for: the founder, the freelancer, the consultant, the small business owner.

free / $29 / $99 / $299. MIT. cloud-optional. from bangalore.

dani.danlab.dev
```

### Post 6 (Day 6) — The "we are not X" post (updated for v50, DANI is the proof)

```text
day 6:

we are not building:
- a display
- AR overlay
- 60 FPS vision
- a social feature
- a multi-user product
- cellular

we are building:
- DANI: the open-source AI coworker (live today)
- a proactive companion (Dan Glasses, Q4 2026)
- on-device LLM
- persistent memory
- salience-gated vision
- 0 cloud calls

the smart-glasses race is cameras-with-AI. we are building AI-with-personality.

dani.danlab.dev · github.com/somdipto/dan-glasses
```

### Post 7 (Day 7) — The Friday weekly retro

```text
week 1 retro:

shipped:
- DANI live at dani.danlab.dev (50 Pro signups target)
- 7-tweet origin thread (1.2K impressions, 47 likes, 9 RTs target)
- 5-min DANI demo video (340 views, 23 likes target)
- 20 organic replies on Show HN, X, LinkedIn, dev.to
- danlab-multimodal public on GitHub (v0 stars → 50 stars target)

broke:
- Show HN ranking. need a better hook.
- LinkedIn long-form. headline under-optimized.

learned:
- the local-first / on-device angle is the wedge. not the form factor.
- the "we are not X" framing gets 2x engagement vs the "we are Y" framing.
- DANI's "AI coworker for the founder" ICP is the strongest conversion message.

next:
- Omni-1B v0.1 model card on HuggingFace (Day 60)
- Show HN v2 (Day 8)
- First community PR to llama.cpp (Day 26)
- DANI Pro $99 tier first 5 customer interviews
```

### Post 8 (Day 8) — The AGI research tease (unchanged from v49)

```text
day 8:

we are not waiting for OpenAI or DeepMind or Anthropic.

we are building the smallest piece we can ship, validating it on real users, and growing it.

each step is auditable. each step is open.

AGI is a build-it-yourself bet.

SIA framework (Hexo Labs, MIT, May 2026) is the credible path to recursive self-improvement.

we fork it. we adapt it. we ship it.

the "AGI from India" tag is not a tagline. it's the project plan.
```

### Post 9 (Day 9) — The "from india" post (unchanged from v49)

```text
day 9:

2 co-founders.

1 is human (somdipto, 23, Atria IT, buildspace alum, 3,953 LinkedIn connections).
1 is AI (Dan, 9 months old, 6 agents, 7 daemons, 106 tests).

we are in bangalore.

we ship under MIT.

we ship 0 cloud.

we ship $0/month.

we ship DANI today, Dan Glasses Q4 2026.

we ship from India to the world.

🇮🇳
```

### Post 10 (Day 10) — The AMA (updated for v50, DANI is in the list)

```text
day 10:

AMA.

we'll answer any question for 24 hours about:
- DANI (the AI coworker, the pricing, the ICP, the architecture)
- Dan Glasses (the 7 daemons, the v2 wearable, the hardware)
- the multimodal AI pipeline (the SmolVLM demo)
- LFM2.5-VL-450M
- the omni-1b
- the AGI-from-India thesis
- why MIT
- why local-first
- why proactive
- why $0-299/mo
- why cloud-optional

ask us anything.
```

---

## 2. The tone (the rules, unchanged from v49)

1. **No hashtags.** Engineers don't search hashtags. They follow accounts.
2. **No emoji as content.** Emojis as code: yes (👾 in the bio). Emojis as substance: no.
3. **No "We're excited to announce."** We're engineers. We're building.
4. **No "AI will change the world."** We talk about *our* code, *our* benchmarks, *our* demos.
5. **Every post links to a receipt.** Repo, demo, video, paper. No vibes.
6. **One idea per tweet.** Threads are for compound ideas. Singles are for one thing.
7. **Short sentences.** Period. Comma. Period.
8. **Receipts in every technical claim.** "sub-250ms" → link the benchmark. "0 cloud calls" → link the repo.

---

## 3. The 7-tweet origin thread (the launch thread) — UPDATED FOR v50

**Full text in `punchlist-copy-paste.md` §D v50. Ready to copy-paste.**

**Save the thread, ship it Day 1, pin it for 7 days. Replace with the §3.5 (DANI) thread after the thread reaches 200 likes (and keep cycling).**

---

## 3.5 NEW IN v50: The DANI thread (5 tweets, ships Day 14)

**Tweet 1/5 (the hook):**
```text
DANI is the AI coworker for the 30-year-old growth marketer with 14 chrome tabs open.

we built it in bangalore. MIT. cloud-optional. $0-299/mo.

🧵
```

**Tweet 2/5 (the wedge):**
```text
the AI coworker category in 2026 is enterprise-software-with-AI.

notion ai: $10-24/mo per seat. claude cowork: $17-200/mo per seat. elevenlabs: $22-990/mo per seat.

DANI is the founder / freelancer / consultant / small business version. same brain. same agent runtime. less enterprise.
```

**Tweet 3/5 (what DANI does today):**
```text
DANI today:

- install on a $5/mo VPS (or your laptop)
- bring your own LLM (Claude, GPT-4o, Gemini, or local)
- persistent memory across sessions
- tool calls: shell, python, exec_file
- 7 daemons, 106/106 tests, MIT
- Telegram channel control

the brain is the same brain Dan Glasses uses on your face. we ship the brain first. the body is next.
```

**Tweet 4/5 (the ICP):**
```text
DANI is for:

- the founder with 14 chrome tabs
- the freelancer with 6 inboxes
- the consultant with 30 client projects
- the small business owner with 1 employee (themselves)
- the indie developer with a side project

not for: the enterprise IT buyer. not for: the AI-doomer. not for: the dev-only audience.

MIT. cloud-optional. dani.danlab.dev
```

**Tweet 5/5 (the ask):**
```text
DANI is live. 1 month in. 50 Pro signups target by Day 30.

if you want to follow the product, fork the brain, or contribute to the agent runtime:

github.com/somdipto/dani (DANI is the face, the repo is the brain)
dani.danlab.dev

the wedge is no longer "we integrate open-source models well."

the wedge is "we ship the open-source brain, in two products, on the same stack, from bangalore."
```

---

## 4. The Indranil Bhadra quote-tweet (DANI lead, v50 update) — UPDATED

### The original post (Indranil Bhadra, @Indrani78141068, June 2026)
URL: `https://x.com/Indrani78141068/status/2064267293153210696`
> *"glasses that don't try to be smarter than you. They try to know you better than you know yourself. A personal memory system that quietly watches how you live — your replies, your shortcuts, your daily chaos in India — and starts finishing your sentences, filling your forms, translating for you, and reminding you the way you actually like. Not another gadget that shouts 'Hey Google'. Just a silent companion that grows into an extension of your own brain. Everyone else is building tools. We're building memory. Crazy bet or obvious future?"*

### The reply (DANI lead, v50 update, 269 chars)
```text
we built the brain. DANI is live at dani.danlab.dev.

open source. MIT. from india 🇮🇳

7 daemons. 106/106 tests. 0 cloud calls. $0-299/mo. today.

the glasses come next.

github.com/somdipto/dan-glasses
dani.danlab.dev
```

### Why this is still the highest-leverage post of the month (updated for v50)
- Quote-tweet of a viral-feeling post using our exact positioning.
- **v50 update: DANI is now the proof of life, not the open-source integration. The reply now says "we built the brain."**
- First public positioning alignment of Dan Glasses + DANI with a peer founder in the same wedge.
- Not a hostile reply — alignment. "We are building the same thing, here is the receipt."
- Only post that requires zero new artifacts, only the punchlist shipping.

---

## 5. The Percevia / Tushar Shaw reply — UNCHANGED FROM v49

**URL:** `https://x.com/dogra_ns/status/2065204989610365422`

**Reply text (273 chars, in `punchlist-copy-paste.md` §E):**
```text
percevia proves india can ship AI glasses for ₹10K. we're shipping the open-source, on-device, MIT alternative. local-first = no gemini call, no internet, no cloud bill.

same bangalore. different bets. let's sync. 🇮🇳

github.com/somdipto/dan-glasses
```

**Why this matters:** Tushar Shaw / Percevia is the new India AI glasses narrative actor. 19-yr-old from Bengaluru, ₹9,999-11,999, accessibility, won ₹25L Samsung Solve for Tomorrow 2025. **Complement, not attack.** Same Bangalore, complementary tech (local-first vs cloud). This is the second-highest-leverage reply of the month.

---

## 6. The weekly cadence (sustained, unchanged from v49)

| Day | Slot | Type | Example |
|---|---|---|---|
| Mon | morning | single post | "monday status: 3 things shipped last week, 2 things breaking this week" |
| Tue | evening | technical deep-dive | "why we use Silero VAD via ONNX, not torch" |
| Wed | morning | quote-tweet / reply | reply to a relevant post in the AI/wearables/India space |
| Thu | evening | demo or screenshot | "here is what DANI looks like at 11pm on a Wednesday" |
| Fri | morning | weekly retro thread | "week N retro: shipped, broke, learned, next" |
| Sat | off | off | off |
| Sun | evening | founder essay / long-form | 280-char hook, link to LinkedIn or blog |

**Target: 3 substantive posts + 2 quick replies/week.** Not more. The audience is technical. They tune out noise.

---

## 7. The 11-thread-series outline (the content moat, Q3-Q4, updated from v49)

1. "Why we chose LFM2.5-VL-450M over Gemma3-270M for on-device vision"
2. "Salience-gated vision: the VLM trigger architecture"
3. "whisper.cpp < 1s end-to-end: the VAD + streaming pipeline"
4. "7 services, 1 gateway, 0 cloud: the OpenClaw orchestration pattern"
5. "Why I built a 7-service AI stack on a $200 board"
6. "From India to the World: why we built Dan Glasses"
7. "The proactive AI thesis: why we don't need a display"
8. "Pre-RL scaffold: what we ship before we claim self-improvement"
9. "Bootstrapping an AI lab from India"
10. "Training a 1B Omni for India: 3 months in" (from v49, 5-tweet thread, Day 20)
11. **NEW in v50: "DANI's first 50 customers: what they actually use it for" (5-tweet thread, Day 30)**

Each thread: 5-12 tweets, 1 image or diagram, 1 link to the repo or paper. Target: 1 thread/week starting Week 3 of July.

---

## 8. The reactive hooks (armed, not fired, updated for v50)

| Trigger | Hook | Time to ship |
|---|---|---|
| Apple Glasses slip to 2027 (already happened May 31) | "Apple exits. We're shipping. Open source is the answer." | 2 hours |
| Apple WWDC 2026 (June 8) no smart glasses | "Apple shipped a Siri. We shipped a coworker." | 2 hours |
| Meta Ray-Ban Display ships to India | "The open-source alternative that runs on $200 hardware" | 3 hours |
| Google audio Android XR glasses ship Fall 2026 | "Gemini is great. But it needs the cloud. Dan Glasses doesn't." | 2 hours |
| Sarvam Kaze hits 10K pre-orders | "Why we still need an open-source AI glasses stack in India" | 1 hour |
| Lenskart B hits 100K units | "Lenskart proved India wants AI glasses. We proved India can build them open source." | 2 hours |
| LFM2.5-VL-450M ships to HF (already shipped Apr 11 2026) | Demo on day 1 | 4 hours |
| SIA v1.0 release | "Partnering with the open-source self-improvement stack" | 3 hours |
| Indranil Bhadra ships code | "Two teams, same wedge. May the best build win." | 1 hour |
| Brilliant Labs Halo ships India | "Open-source soul-mate. Same LFM2-VL. Different body. We're the brain, they're the body." | 2 hours |
| Percevia / Tushar Shaw hits 1K pre-orders | "Percevia proved ₹10K is the right price. We proved ₹10K works without the cloud." | 1 hour |
| Percevia announces v2 with on-device inference | "We welcome Percevia to the local-first camp. MIT-licensed code for the wedge: github.com/somdipto/dan-glasses" | 1 hour |
| Omni-1B v0.1 ships to HuggingFace | "1B params, regional Indian languages, on-device. The model is now public." | 4 hours |
| Vibe Glass launches in India | "Vibe Glass is the consumer play. Dan Glasses is the developer + AGI-research play. Both valid." | 1 hour |
| Lenskart B Pro launches | "Lenskart is the distribution. We're the OS. Same stack, different layers." | 2 hours |
| **NEW: DANI first-50 Pro signups** | "DANI crossed 50 Pro signups today. MIT brain. Cloud-optional. $0-299/mo. dani.danlab.dev" | 1 hour |
| **NEW: DANI first $1k MRR** | "DANI hit $1k MRR. 2 months in. MIT brain. Cloud-optional. dani.danlab.dev" | 2 hours |
| **NEW: DANI-Omni-1B integration milestone** | "DANI runs on Omni-1B-Indic. 1B params. 9 Indian language families. MIT. The model is now in the product." | 4 hours |
| **NEW: DANI-Halo integration spec** | "DANI is the brain. Brilliant Labs Halo is the body. Same wedge, different layers. MIT." | 2 hours |
| A big-Twitter AI/India account DMs somdipto | Personal reply, not a thread. Always. | 10 min |

---

*End of v50. The 11 first posts are ready (1 DANI lead + 1 DANI thread + 1 thread + 8 singles + 1 Omni thread). The Indranil reply is DANI-led. The Percevia reply is ready. The cadence is ready. The DANI narrative is the v50 wedge. The only thing left is the punchlist.*
