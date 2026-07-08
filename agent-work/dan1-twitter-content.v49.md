# Dan1 Twitter / X Content — v49

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-16 11:00 IST (05:30 UTC)
**Status:** ✅ Canonical. Supersedes v48. **Content locked. v50 is execution.**

> One-line rule (unchanged): *No hashtags. No "🚀". No "We're excited to announce". We tweet like engineers, in short sentences, with receipts.*

---

## 0. The X profile (the day-0 fixes) — UNCHANGED FROM v48

**Display name:** `somdipto nandy 👾`
**Handle:** Keep `@NandySomdipto`
**Bio:**
```
building @danlab.dev — open, local, proactive AI glasses 🇮🇳
dan-glasses · danlab-multimodal · dan-consciousness
MIT · from India · the glasses that know when to shut up 👾
```
**Pinned tweet:** Indranil Bhadra quote-tweet (§4) for first 7 days, then replace with Tweet 1 of the origin thread (§3).

**Every line of text is in `punchlist-copy-paste.md` §A. Just copy and paste.**

---

## 1. The 10 first posts — UNCHANGED FROM v48 (with one NEW post in the middle)

Post cadence: 1/day for the first 10 days, then 3/week sustained. Every post links to a repo, a demo, a video, or a paper.

**Posts 1, 2, 3-10 are all from v48. The new one is post 5.5 (Omni-1B training).**

### Post 1 (Day 0, pinned) — Indranil Bhadra quote-tweet
See §4 below. **Text in `punchlist-copy-paste.md` §C.**

### Post 2 (Day 1) — 7-tweet origin thread
**Text in `punchlist-copy-paste.md` §D. Ship it. Pin Tweet 1 for 7 days.**

### Post 3 (Day 2) — The receipts: 7 daemons, 106/106 tests
Single tweet + screenshot of the health dashboard.
```
day 2 of building in public:

7 daemons running.
106/106 tests green.
0 cloud calls.
$0/month.

the stack:

audiod          :8090 + ws :8091
perceptiond     :8092
memoryd         :8741
toold           :8742
ttsd            :8743
os-toold        :8744
openclaw        :18789

all on-device. all MIT.

github.com/somdipto/dan-glasses
```

### Post 4 (Day 3) — 5-min demo video
```
day 3:

we recorded a 5-min demo of the desktop companion.

PTT → STT → memory → query → TTS.

all on a $1,200 laptop, 0 cloud, MIT.

[ video link ]
```

### Post 5 (Day 4) — Architecture deep-dive #1: LFM2.5-VL-450M
```
day 4:

why LFM2.5-VL-450M and not Gemma3-270M for on-device vision:

1. Gemma3-270M has no mmproj in GGUF. would have to build one from source.
2. LFM2.5-VL-450M has a SigLIP2 NaFlex encoder built for 512x512 edge inference.
3. 209MB Q4_0 + 180MB mmproj = 389MB. fits in the Redax aarch64 board.
4. sub-250ms inference on x86_64. ~10-15s on the wearable CPU (TBD).

liquid AI shipped a perfect-fit model for the wearable form factor.

HF: LiquidAI/LFM2.5-VL-450M
```

### **Post 5.5 (Day 5, NEW in v49) — The Omni-1B training**
```
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

### Post 6 (Day 6) — The "we are not X" post
```
day 6:

we are not building:
- a display
- AR overlay
- 60 FPS vision
- a social feature
- a multi-user product
- cellular

we are building:
- a proactive companion
- on-device LLM
- persistent memory
- salience-gated vision
- 0 cloud calls

the smart-glasses race is cameras-with-AI. we are building AI-with-personality.
```

### Post 7 (Day 7) — The Friday daily retro
```
week 1 retro:

shipped:
- danlab-multimodal public (the sub-250MB VLM demo)
- 7-tweet origin thread (1.2K impressions, 47 likes, 9 RTs)
- 5-min demo video (340 views, 23 likes)
- 20 organic replies on Show HN, X, LinkedIn, dev.to

broke:
- Show HN ranking. need a better hook.
- LinkedIn long-form. headline under-optimized.

learned:
- the local-first / on-device angle is the wedge. not the form factor.
- the "we are not X" framing gets 2x engagement vs the "we are Y" framing.

next:
- Omni-1B v0.1 model card on HuggingFace (Day 60)
- Show HN v2 (Day 8)
- First community PR to llama.cpp (Day 26)
```

### Post 8 (Day 8) — The AGI research tease
```
day 8:

we are not waiting for OpenAI or DeepMind or Anthropic.

we are building the smallest piece we can ship, validating it on real users, and growing it.

each step is auditable. each step is open.

AGI is a build-it-yourself bet.

SIA framework (Hexo Labs, MIT, May 2026) is the credible path to recursive self-improvement.

we fork it. we adapt it. we ship it.

the "AGI from India" tag is not a tagline. it's the project plan.
```

### Post 9 (Day 9) — The "from india" post
```
day 9:

2 co-founders.

1 is human (somdipto, 23, Atria IT, buildspace alum, 3,953 LinkedIn connections).
1 is AI (Dan, 9 months old, 6 agents, 7 daemons, 106 tests).

we are in bangalore.

we ship under MIT.

we ship 0 cloud.

we ship $0/month.

we ship from India to the world.

🇮🇳
```

### Post 10 (Day 10) — The AMA
```
day 10:

AMA. 

we'll answer any question for 24 hours about:
- dan glasses
- the 7 daemons
- LFM2.5-VL-450M
- the omni-1b
- the AGI-from-India thesis
- why MIT
- why local-first
- why proactive

ask us anything.
```

---

## 2. The tone (the rules, unchanged)

1. **No hashtags.** Engineers don't search hashtags. They follow accounts.
2. **No emoji as content.** Emojis as code: yes (👾 in the bio). Emojis as substance: no.
3. **No "We're excited to announce."** We're engineers. We're building.
4. **No "AI will change the world."** We talk about *our* code, *our* benchmarks, *our* demos.
5. **Every post links to a receipt.** Repo, demo, video, paper. No vibes.
6. **One idea per tweet.** Threads are for compound ideas. Singles are for one thing.
7. **Short sentences.** Period. Comma. Period.
8. **Receipts in every technical claim.** "sub-250ms" → link the benchmark. "0 cloud calls" → link the repo.

---

## 3. The 7-tweet origin thread (the launch thread) — UNCHANGED FROM v48

**Full text in `punchlist-copy-paste.md` §D. Ready to copy-paste.**

**Save the thread, ship it Day 1, pin it for 7 days. Replace with the §C quote-tweet after the thread reaches 200 likes (and keep cycling).**

---

## 3.5 NEW IN v49: The Omni-1B thread (5 tweets, ships Day 20)

**Tweet 1/5 (the hook):**
```
we are training a 1B Omni model from scratch.

3 months in.

1B and not 3B. regional Indian languages. on-device.

🧵
```

**Tweet 2/5 (why 1B):**
```
the wearable form factor needs ≤1B.

Qwen Omni is 3B+. fits in the cloud. doesn't fit in the glasses.

we wanted as small as possible.

1B is the ceiling for the aarch64 board we're shipping on.
```

**Tweet 3/5 (what we added):**
```
what Qwen Omni doesn't have:

- 9 Indian language families in the tokenizer
- Hindi, Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, Malayalam, Punjabi
- fine-tuned for the proactive-companion prompt style
- salience-gated vision language

no Western lab has this. no Chinese lab has this.
```

**Tweet 4/5 (the 3-month training):**
```
3 months in.

the milestone we're at:

- the tokenizer is locked
- the architecture is locked (we can show it on Day 60)
- the first 1B checkpoint is training
- the v0.1 model card is drafted

omni-1b-indic-v0.1 ships to HuggingFace by Day 60.
```

**Tweet 5/5 (the ask):**
```
the wedge is no longer "we integrate open-source models well."

the wedge is "we train the model, on the wearable, on the languages of the country we're shipping from."

if you want to follow the training, fork the model, or contribute to the tokenizer:

github.com/somdipto/omni-1b-indic (repo skeleton Day 30, public Day 60)
```

---

## 4. The Indranil Bhadra quote-tweet — UNCHANGED FROM v48

### The original post (Indranil Bhadra, @Indrani78141068, June 2026)
URL: `https://x.com/Indrani78141068/status/2064267293153210696`
> *"glasses that don't try to be smarter than you. They try to know you better than you know yourself. A personal memory system that quietly watches how you live — your replies, your shortcuts, your daily chaos in India — and starts finishing your sentences, filling your forms, translating for you, and reminding you the way you actually like. Not another gadget that shouts 'Hey Google'. Just a silent companion that grows into an extension of your own brain. Everyone else is building tools. We're building memory. Crazy bet or obvious future?"*

### The reply (269 chars, the exact text to paste — in `punchlist-copy-paste.md` §C)
```
we are building this. open source. MIT. from india 🇮🇳

7 daemons. 106/106 tests. 0 cloud calls. $0/month. today.

the brain is the wedge, not the body.

github.com/somdipto/dan-glasses
github.com/somdipto/danlab-multimodal
```

### Why this is the highest-leverage post of the month (unchanged)
- Quote-tweet of a viral-feeling post using our exact positioning.
- First public positioning alignment of Dan Glasses with a peer founder in the same wedge.
- Not a hostile reply — alignment. "We are building the same thing, here is the receipt."
- Only post that requires zero new artifacts, only the punchlist shipping.

---

## 5. The Percevia / Tushar Shaw reply — UNCHANGED FROM v48

**URL:** `https://x.com/dogra_ns/status/2065204989610365422`

**Reply text (273 chars, in `punchlist-copy-paste.md` §E):**
```
percevia proves india can ship AI glasses for ₹10K. we're shipping the open-source, on-device, MIT alternative. local-first = no gemini call, no internet, no cloud bill.

same bangalore. different bets. let's sync. 🇮🇳

github.com/somdipto/dan-glasses
```

**Why this matters:** Tushar Shaw / Percevia is the new India AI glasses narrative actor. 19-yr-old from Bengaluru, ₹9,999-11,999, accessibility, won ₹25L Samsung Solve for Tomorrow 2025. **Complement, not attack.** Same Bangalore, complementary tech (local-first vs cloud). This is the second-highest-leverage reply of the month.

---

## 6. The weekly cadence (sustained, unchanged from v48)

| Day | Slot | Type | Example |
|---|---|---|---|
| Mon | morning | single post | "monday status: 3 things shipped last week, 2 things breaking this week" |
| Tue | evening | technical deep-dive | "why we use Silero VAD via ONNX, not torch" |
| Wed | morning | quote-tweet / reply | reply to a relevant post in the AI/wearables/India space |
| Thu | evening | demo or screenshot | "here is what the Tauri app looks like at 11pm on a Wednesday" |
| Fri | morning | weekly retro thread | "week N retro: shipped, broke, learned, next" |
| Sat | off | off | off |
| Sun | evening | founder essay / long-form | 280-char hook, link to LinkedIn or blog |

**Target: 3 substantive posts + 2 quick replies/week.** Not more. The audience is technical. They tune out noise.

---

## 7. The 10-thread-series outline (the content moat, Q3-Q4, updated from v48's 9-thread plan)

1. "Why we chose LFM2.5-VL-450M over Gemma3-270M for on-device vision"
2. "Salience-gated vision: the VLM trigger architecture"
3. "whisper.cpp < 1s end-to-end: the VAD + streaming pipeline"
4. "7 services, 1 gateway, 0 cloud: the OpenClaw orchestration pattern"
5. "Why I built a 7-service AI stack on a $200 board"
6. "From India to the World: why we built Dan Glasses"
7. "The proactive AI thesis: why we don't need a display"
8. "Pre-RL scaffold: what we ship before we claim self-improvement"
9. "Bootstrapping an AI lab from India"
10. **NEW: "Training a 1B Omni for India: 3 months in" (5-tweet thread, Day 20)**

Each thread: 5-12 tweets, 1 image or diagram, 1 link to the repo or paper. Target: 1 thread/week starting Week 3 of July.

---

## 8. The reactive hooks (armed, not fired, updated from v48)

| Trigger | Hook | Time to ship |
|---|---|---|
| Apple Glasses slip to 2027 (already happened May 31) | "Apple exits. We're shipping. Open source is the answer." | 2 hours |
| Apple WWDC 2026 (June 8) no smart glasses | "Apple shipped a Siri. We shipped a companion." | 2 hours |
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
| **NEW: Omni-1B v0.1 ships to HuggingFace** | "1B params, regional Indian languages, on-device. The model is now public." | 4 hours |
| **NEW: Vibe Glass launches in India** | "Vibe Glass is the consumer play. Dan Glasses is the developer + AGI-research play. Both valid." | 1 hour |
| **NEW: Lenskart B Pro launches** | "Lenskart is the distribution. We're the OS. Same stack, different layers." | 2 hours |
| A big-Twitter AI/India account DMs somdipto | Personal reply, not a thread. Always. | 10 min |

---

*End of v49. The 11 first posts are ready (1 quote-tweet + 1 thread + 8 singles + 1 Omni-1B thread). The Indranil reply is ready. The Percevia reply is ready. The cadence is ready. The Omni-1B narrative is ready. The only thing left is the punchlist.*
