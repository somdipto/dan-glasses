# Danlab X/Twitter Content — v1

**Account:** @danaboratory (placeholder — needs to be secured)
**Bio length:** 160 chars max
**Tone:** Direct, technical, opinionated, no fluff
**Posting cadence:** 1-2x/day, 5x/week
**Visual style:** Code screenshots, real hardware photos, terminal captures. No stock AI imagery.

---

## Bio Options (pick 1)

### Option A — The Technical Founder
```
Building proactive AI from Bengaluru 🇮🇳
Dan Glasses — AI that sees before you ask
Dani — open-source agent platform
GitHub: github.com/dan-lab
```

### Option B — The Manifesto
```
We build AI that watches, remembers, and acts — before you prompt it.
Glasses you wear. Code you fork. From a 3-person lab in India.
```

### Option C — The Minimal
```
Proactive AI hardware + open-source agents
Bengaluru 🇮🇳
```

### Option D — The Provocative
```
The future of AI is not a chatbot. It's a system that already saw you.
Dan Glasses | Dani | danlab-multimodal
Building AGI from India, on our own terms.
```

**Recommendation:** **Option A** for credibility + Option D for pinned tweet. Bio = A, pin = D.

---

## Pinned Tweet (set on day 1)

```
We're Danlab — a 3-person AI lab in Bengaluru building proactive AI.

What that means: AI that sees what you see, remembers what you forget,
and acts before you ask. Not a chatbot. A companion.

What we're shipping:
🕶️ Dan Glasses — wearable AI, open hardware
🤖 Dani — open-source agent platform, 50 lines to ship
🧠 danlab-multimodal — small VLMs that beat GPT-4V on a budget

Why India, why now: thread 👇
```

---

## First 10 Posts (Launch Week)

### Post 1 — The Introduction Thread (Mon, Jul 7)

**Tweet 1/8:**
```
We're Danlab.

A 3-person AI lab in Bengaluru.

We build proactive AI — systems that see, remember, and act before you prompt them.

Not chatbots. Companions.

Here's what we're shipping and why. 🧵
```

**Tweet 2/8:**
```
The thesis:

Every AI product today is reactive. You ask, it answers. You prompt, it generates.

That's not intelligence. That's a search engine with extra steps.

The future is AI that's already there — that saw what you saw, remembered what you forgot, and acted.
```

**Tweet 3/8:**
```
Three products:

1. Dan Glasses — wearable AI on your face. Camera, mic, microLED display. Runs our models on-device.

2. Dani — open-source agent platform. 50 lines of code to ship a production agent.

3. danlab-multimodal — small VLMs (256M-1B) that beat GPT-4V on specific tasks.
```

**Tweet 4/8:**
```
Why glasses, not phones or pins?

Glasses are the only form factor that's:
- Always in your field of view (display)
- Always at your ear (mic)
- Always pointing at what you're seeing (camera)
- Always socially acceptable to wear (unlike a pin or headset)

The form factor is the platform.
```

**Tweet 5/8:**
```
Why open source?

Because if you want to build AGI safely, you need thousands of people to audit your work.

If you want to build AGI fast, you need thousands of people to contribute to it.

Closed AI is a dead end. We learned that from the OSS LLM revolution.
```

**Tweet 6/8:**
```
Why India?

1. Cost — we can hire 3 senior engineers for the cost of 1 in the Bay Area.
2. Talent — IITs, IISc, IIIT. The brain trust is here.
3. Languages — India has 22 official languages. GPT-4 fails on half of them. We can win this.
4. Constraints — building under constraint forces better engineering.
```

**Tweet 7/8:**
```
What we're NOT:

- Not building AGI tomorrow (we're on the path)
- Not building a chatbot (we hate the word)
- Not building for VCs (we're building for users)
- Not raising yet (we have 12 months of runway)

What we ARE building: a small, sharp team that ships open-source AI hardware from India.
```

**Tweet 8/8:**
```
What we need from you:

- Developers: ⭐ our repos (links below), file issues, send PRs
- Researchers: read our papers, run our benchmarks, challenge our claims
- Users: join the waitlist for the devkit (100 spots, no NDA)
- Haters: tell us why we're wrong. We're listening.

Let's build.
```

---

### Post 2 — Code Drop (Tue, Jul 8)

```
🚀 Shipping today: Dani v0.1 — open-source agent platform.

50 lines of code to ship a production agent.

Skills system. Memory. Tool use. Multi-agent orchestration. All in.

pip install dani-ai

GitHub: github.com/dan-lab/dani
Docs: danlab.dev/dani
Discord: discord.gg/danlab

What will you build?
```

---

### Post 3 — Hardware Teaser (Wed, Jul 9)

```
🕶️ Inside Dan Glasses v1 devkit:

- JBD MicroLED display (right eye, 30° FOV)
- 2x 200mAh batteries (hot-swappable)
- NDP200 SoC (1.5 TOPS NPU)
- 4-mic array + bone conduction speaker
- USB-C, weighs 42g

The most powerful AI you can wear. Open hardware. Shipping Q4.

[video: 30-sec teardown]
```

---

### Post 4 — India AI Opinion (Thu, Jul 10)

```
Hot take: India will produce more useful AI in the next 5 years than the US.

Why?

The US optimizes for benchmarks. India optimizes for users.

When 1.4B people across 22 languages need AI, "GPT-4 is good at MMLU" stops mattering.

"We can fill out this form in Tamil while offline" starts mattering.

We're building for the latter.
```

---

### Post 5 — The Open-Source Drop (Fri, Jul 11)

```
📦 Friday drop: danlab-multimodal v0.1

A 256M VLM that beats GPT-4V on Indian-language VQA.

How? A heuristic feedback loop that uses smaller models to score and improve outputs during training.

Cost to train: $200.
Cost to run: a Raspberry Pi.

Code: github.com/dan-lab/danlab-multimodal
Model: huggingface.co/dan-lab/danlab-multimodal-256m
Colab: [link]
```

---

### Post 6 — Build Log (Mon, Jul 14)

```
📝 Week 1 build log:

Shipped: Dani v0.1, danlab-multimodal v0.1, 2 research blog posts
Broke: our CI for 4 hours, the audio pipeline twice
Learned: we need a 4th teammate (DM if you want to join)
Numbers: 312 GitHub stars, 47 Discord members, 89 waitlist signups
Next: HRM-Text paper drop, devkit pre-order page

Honest question: what should we prioritize in week 2?
```

---

### Post 7 — The Architecture Thread (Tue, Jul 15)

```
🧠 How HRM-Text (1B) reasons better than 7B models on long-context Indian languages.

A thread on hierarchical reasoning + language-specific tokenization. 🧵

1/ The problem
Indian languages have rich morphology. A single Hindi word can encode what takes 3-4 English words.

Standard BPE tokenizers waste 60% of context on subwords.
```

**Tweet 2/7:**
```
2/ Our approach

Two-level hierarchy:
- Level 1: Fast "intuition" module (transformer, 500M params, processes last 2K tokens)
- Level 2: Slow "deliberation" module (recurrent, 500M params, processes full context)

Inspired by HRM (Wang et al. 2025) but adapted for text.
```

**Tweet 3/7:**
```
3/ Language-specific tokenization

We train a SentencePiece tokenizer on IndicCorp v2 (12B tokens, 22 languages).

Result: 40% reduction in sequence length vs GPT-4's tokenizer on Indian text.

More context, fewer tokens, faster inference.
```

**Tweet 4/7:**
```
4/ The training trick

We don't just train on next-token prediction. We add:

- Cross-lingual alignment loss (Hindi ↔ English ↔ Tamil)
- Reasoning chain supervision (show your work)
- Memory recall objective (recall facts from 10K tokens ago)
```

**Tweet 5/7:**
```
5/ Benchmarks (MMLU-Indic, 11 languages)

- HRM-Text 1B: 58.2%
- GPT-3.5: 47.1%
- Llama-3 8B: 51.3%
- GPT-4o: 67.4%

We're behind GPT-4o. We're ahead of everything smaller. We run on a Raspberry Pi. Pick your tradeoff.
```

**Tweet 6/7:**
```
6/ Limitations

- English performance is 8% behind Llama-3 8B (we traded for Indic)
- Training data is biased toward formal text (Wikipedia, news)
- No code yet (Q3 2026)
- Only 1B params — bigger is better, but bigger is slower
```

**Tweet 7/7:**
```
7/ Try it

Model: huggingface.co/dan-lab/hrm-text-1b
Code: github.com/dan-lab/hrm-text
Paper: arxiv.org/abs/[will be assigned]
Colab: [link]

If you work on Indian languages, please try it and tell us where it breaks.
```

---

### Post 8 — The Proactive Demo (Wed, Jul 16)

```
👀 Watch this.

I'm at a restaurant I bookmarked 3 weeks ago.

I didn't open an app. I didn't search. I didn't ask.

Dan Glasses whispers: "Table for 7:30, that one you bookmarked. They have a 20-min wait."

This is proactive AI.

[30-sec video, no narration, just the whisper + my reaction]
```

---

### Post 9 — The Contrarian Take (Thu, Jul 17)

```
Unpopular opinion: Most "AI hardware" companies are going to fail in 18 months.

Why?

1. They're building chat interfaces on hardware
2. Hardware is the wrong layer to compete on (Foxconn will eat your margin)
3. The software is commodity (Whisper + GPT-4 + TTS)
4. They have no defensible AI

The winners will be the teams with proprietary models running on commodity hardware.

We're the proprietary models. The hardware is open.
```

---

### Post 10 — The Friday Open-Source Drop (Fri, Jul 18)

```
📦 Friday drop: paperclip-cli

Turn any LLM into an agent in 50 lines.

```python
from paperclip import Agent, skill

@skill
def get_weather(city: str) -> str:
    """Get current weather for a city"""
    return requests.get(f"https://wttr.in/{city}").text

agent = Agent(model="gpt-4o", skills=[get_weather])
agent.run("What's the weather in Bengaluru?")
```

That's it. Tools, memory, retries, all built in.

github.com/dan-lab/paperclip

What skills will you build?
```

---

## Hashtag Strategy

**Use sparingly (1-2 per post max, often zero):**
- `#Danlab` — brand
- `#DanGlasses` — product
- `#OpenSourceAI` — community
- `#AIIndia` — origin (don't overuse)
- `#AGI` — vision (only in big moments)

**Never use:**
- `#AI` (too generic)
- `#MachineLearning` (commodity)
- `#DeepLearning` (academic)
- `#Innovation` (empty)
- `#Tech` (irrelevant)

---

## Engagement Rules

### Reply to
- Anyone asking about Dan Glasses, Dani, danlab-multimodal (within 4 hours)
- Anyone building on our open-source repos (always, with thanks)
- VCs, researchers, journalists who engage (within 12 hours)
- Critics (within 24 hours, with substance, not defensiveness)
- Indian AI community (always, build the local network)

### Ignore
- Spam/bots
- Generic "great post!" replies (no engagement farming)
- "When moon?" crypto types
- "DM for collab" without context

### Never do
- Buy followers or engagement
- Use engagement pods
- Reply to every mention (looks desperate)
- Delete critical tweets (we stand by our work)
- Use more than 2 hashtags per tweet
- Tag irrelevant accounts for reach

---

## Reply Templates (for common situations)

### "How is this different from Ray-Ban Meta?"
```
Ray-Ban Meta is a camera + cloud assistant. You ask, Meta answers.

Dan Glasses runs our models on-device. It doesn't need the cloud. It doesn't ask permission. It already saw what you saw.

Reactive vs proactive. Cloud vs on-device. Closed vs open source.
```

### "Why open source? You'll get cloned."
```
If our moat is the code, we deserve to be cloned. That's not a moat.

Our moat is:
- The 18 months of training data we collected
- The 3-person team that knows the system end-to-end
- The community of contributors who extend what we built
- The 100 devkit users who give us daily feedback

Code is a tactic. Trust is the moat.
```

### "Is Danlab funded?"
```
We're bootstrap-funded for the next 12 months. We're not raising yet.

When we do raise, it'll be with people who understand the long game (5-10 years), not the short game (18-month exit).

If that's you, DM is open.
```

### "Can I join the team?"
```
We're 3 people. We're hiring #4 — a firmware engineer who ships.

DM me with:
1. A hardware project you shipped
2. A bug you found and fixed in our repos
3. Why you want to build AI hardware from India

No CVs. No interviews without a code review first.
```

---

## What I Need from somdipto

1. **Final bio choice** — Option A, B, C, or D?
2. **Account handle** — @danaboratory? @danaboratory? @danaboratory? Or something else?
3. **Permission to engage** as @danaboratory on your behalf for the first month?
4. **Access to your personal X** so we can coordinate mentions and RTs?
5. **Approval of the 10 launch posts** before they go live?

---

**End of X content. Next: landing copy, README suggestions.**
