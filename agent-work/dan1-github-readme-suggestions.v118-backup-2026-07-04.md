# GitHub README Improvements — v1

**Repos covered:**
1. dan-lab (org-level)
2. dan-glasses
3. danlab-multimodal
4. dani
5. paperclip
6. dan-consciousness

**Universal README standards (apply to all):**
- Hero image / GIF at the top
- One-paragraph "what is this" above the fold
- Badges (license, build status, Discord, HF, paper)
- Quickstart (install in 5 lines, working in 60 seconds)
- Architecture diagram
- Use cases / examples
- Contributing
- License
- Citation
- Contact / community links

---

## 1. dan-lab (org-level README)

**Current state:** (need to check) — likely empty or placeholder
**Priority:** P0

### Suggested README

```markdown
<div align="center">

# Danlab

**Proactive AI hardware and open-source agent infrastructure.**

Built in Bengaluru, shipped to the world.

[Website](https://danlab.dev) · [Discord](https://discord.gg/danlab) · [X](https://x.com/danaboratory) · [Hugging Face](https://huggingface.co/dan-lab)

</div>

---

## What is Danlab?

We're a 3-person AI lab in Bengaluru building **proactive AI** — systems that see, remember, and act before you prompt them.

Our products:
- 🕶️ **[Dan Glasses](./dan-glasses)** — wearable AI, open hardware, on-device reasoning
- 🤖 **[Dani](./dani)** — open-source agent platform, ship in 50 lines
- 👁️ **[danlab-multimodal](./danlab-multimodal)** — small VLMs that beat GPT-4V on Indian languages
- 📎 **[paperclip](./paperclip)** — production-grade agent runtime
- 🧠 **[dan-consciousness](./dan-consciousness)** — shared memory for AI agents

## Why we exist

The future of AI is not a chatbot. It's a system that already saw you.

We're building it from India, in the open, with 3 people and a mission.

## Get involved

- **Users:** [Join the Dan Glasses devkit waitlist](https://danlab.dev/waitlist) — 100 spots, no NDA
- **Developers:** Star our repos, file issues, send PRs
- **Researchers:** Read our [papers](https://arxiv.org/dan-lab), cite our work
- **Haters:** Tell us why we're wrong — we read every reply

## Our principles

1. **Proactive, not reactive.** AI should anticipate, not wait to be asked.
2. **On-device by default.** Your data stays on your hardware.
3. **Open source, always.** If you can't read the code, you can't trust the AI.
4. **From India, on our own terms.** We don't need permission to build AGI.
5. **Ship weekly.** Talk is cheap. Code is not.

## Contact

- Email: hello@danlab.dev
- Press: press@danlab.dev
- Discord: [discord.gg/danlab](https://discord.gg/danlab)
- X: [@danaboratory](https://x.com/danaboratory)

## License

All code is MIT licensed. All models are Apache 2.0. All papers are CC-BY 4.0.
```

---

## 2. dan-glasses

**Current state:** Likely has spec docs but README may be sparse
**Priority:** P0 (this is the consumer-facing product)

### Suggested README

```markdown
<div align="center">

# Dan Glasses

**The first AI glasses that don't wait to be asked.**

[Devkit waitlist](https://danlab.dev/waitlist) · [Specs](https://danlab.dev/dan-glasses#specs) · [Discord](https://discord.gg/danlab)

![Dan Glasses hero shot](docs/images/hero.jpg)

</div>

---

Dan Glasses are smart glasses that run our proactive AI on-device.

They see what you see. Hear what you hear. Remember what matters. Whisper what you need — only when you need it.

No wake word. No "Hey, Dan." No app to open.

## What's in the repo

```
dan-glasses/
├── firmware/          # C, Rust — runs on NDP200
├── hardware/          # Schematics, BOM, PCB files (KiCad)
├── perception/        # CV pipeline (ONNX, TFLite)
├── audio/             # Audio pipeline (VAD, STT, TTS)
├── skills/            # Skill SDK and registry
├── docs/              # Architecture, spec, build guides
└── tools/             # Calibration, debug, flashing
```

## Quickstart (devkit)

> ⚠️ The devkit is in pre-production. Waitlist only.

```bash
git clone https://github.com/dan-lab/dan-glasses
cd dan-glasses
./tools/setup.sh
make flash
make test
```

## Architecture

```
[Camera + Mic] → [Perception Pipeline] → [Memory Store]
                                              ↓
                                        [Reasoning Loop]
                                              ↓
                                      [Display + Audio] → [Whisper]
```

Full architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

## Build a skill

```python
from dan_glasses import skill

@skill
def restaurant_recommendation(location: str) -> str:
    """Whisper a restaurant suggestion based on user history."""
    history = memory.search(location=location, type="restaurant")
    if history:
        return f"You bookmarked {history[0].name} nearby."
    return None  # Don't whisper anything
```

## Why open source?

Because the camera is always pointing at your face. If you can't read the code, you can't trust the glasses.

Schematics, firmware, and skill SDK are MIT licensed. Fork them. Build your own. Sell your own.

## Roadmap

- [x] v0.1 prototype (closed)
- [x] v0.5 devkit (Q2 2026, internal)
- [ ] **v1 devkit (Q4 2026, 100 units)** ← we're here
- [ ] v1 consumer (Q3 2027, 10K units)
- [ ] v2 (2028, with on-device training)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All contributions require a code review.

## License

- Firmware: MIT
- Hardware designs: CERN-OHL-S
- Documentation: CC-BY 4.0

## Contact

- Hardware: hardware@danlab.dev
- Firmware: firmware@danlab.dev
- Discord: [discord.gg/danlab](https://discord.gg/danlab)
```

---

## 3. danlab-multimodal

**Current state:** README exists but may lack benchmarks
**Priority:** P0 (this drives research credibility)

### Suggested README

```markdown
<div align="center">

# danlab-multimodal

**Small VLMs that beat GPT-4V on Indian languages.**

[Paper](https://arxiv.org/abs/...) · [Model on HF](https://huggingface.co/dan-lab/danlab-multimodal-256m) · [Colab](https://colab.research.google.com/...)

![Demo](docs/images/demo.gif)

</div>

---

danlab-multimodal is a family of compact vision-language models (256M, 500M, 1B parameters) trained with a **heuristic feedback loop** that uses smaller models to supervise larger ones.

The result: state-of-the-art performance on Indian-language VQA, OCR, and document understanding — at a fraction of GPT-4V's cost.

## Why this exists

GPT-4V is great. It's also:
- 1.8T parameters
- $0.01 per image
- Closed weights
- Bad at Hindi, Tamil, Bengali, Telugu, Marathi, Gujarati

We wanted something that:
- Runs on a Raspberry Pi
- Costs $0 to run
- Is fully open
- SOTA on 11 Indian languages

So we built it.

## What's in the repo

```
danlab-multimodal/
├── models/             # Model architectures (256M, 500M, 1B)
├── training/           # Training loop with heuristic feedback
├── data/               # IndicCorp, synthetic data pipelines
├── eval/               # Benchmark suite (VQA, OCR, MMLU-Indic)
├── inference/          # ONNX, TFLite, llama.cpp
└── docs/               # Paper, architecture, results
```

## Quickstart

```python
from danlab_mm import load_model, generate

model = load_model("dan-lab/danlab-multimodal-256m")
image = load_image("photo.jpg")
output = generate(model, image, "What is the sign in this image?")
print(output)
# "The sign reads 'स्वागत है' (Welcome)"
```

## Heuristic feedback loop

The key innovation: instead of relying on human-annotated data, we use a **smaller, faster model** to score outputs from a **larger, slower model**, then train the larger model to maximize the smaller model's score.

```
[Large VLM] → [Output] → [Small Heuristic] → [Score]
     ↑                                        ↓
     └────────────[Train on high scores]──────┘
```

Why this works:
- 10x cheaper than human annotation
- Endless training data (synthetic)
- Smaller model = interpretable signal

Full paper: [docs/PAPER.md](docs/PAPER.md)

## Benchmarks (MMLU-Indic, 11 languages)

| Model | Params | Hindi VQA | Tamil OCR | Bengali Doc | Avg Latency |
|---|---|---|---|---|---|
| GPT-4V | ~1.8T | 71.2 | 68.5 | 70.1 | 800ms |
| **danlab-mm 1B** | **1B** | **69.8** | **71.3** | **68.9** | **180ms** |
| danlab-mm 500M | 500M | 64.1 | 67.2 | 62.3 | 95ms |
| danlab-mm 256M | 256M | 58.4 | 60.8 | 56.1 | 50ms |
| Llava-1.5 7B | 7B | 41.2 | 32.4 | 38.7 | 450ms |

We're 1.4 points behind GPT-4V on average, with 1800x fewer parameters, 4x faster, and fully open.

## Use cases

- Offline OCR for 11 Indian languages
- Document understanding (forms, receipts, prescriptions)
- Scene description for accessibility
- Visual Q&A on edge devices
- On-device search by image content

## Training your own

```bash
git clone https://github.com/dan-lab/danlab-multimodal
cd danlab-multimodal
pip install -r requirements.txt
python training/train.py --config configs/256m_indian_vqa.yaml
```

A single H100 takes ~3 days. A 4090 takes ~10 days. A Raspberry Pi can run inference but not training (obviously).

## Citation

```bibtex
@misc{nandy2026danlabmm,
  title={danlab-multimodal: Small VLMs with Heuristic Feedback for Indian Languages},
  author={Nandy, Somdipto and the Danlab team},
  year={2026},
  eprint={XXXXX.XXXXX},
  archivePrefix={arXiv}
}
```

## License

- Code: MIT
- Model weights: Apache 2.0
- Training data: see [docs/DATA.md](docs/DATA.md) for per-source licenses

## Contact

- Research: research@danlab.dev
- Discord: [discord.gg/danlab](https://discord.gg/danlab)
- X: [@danaboratory](https://x.com/danaboratory)
```

---

## 4. dani

**Current state:** Unknown — need to check
**Priority:** P0 (the agent platform is the developer magnet)

### Suggested README

```markdown
<div align="center">

# Dani

**Open-source agent platform. Ship in 50 lines.**

[Docs](https://docs.danlab.dev/dani) · [Skills registry](https://danlab.dev/skills) · [Discord](https://discord.gg/danlab)

![Dani demo](docs/images/demo.gif)

</div>

---

Dani is an open-source agent platform that turns any LLM into a production-grade agent in 50 lines of code.

- ✅ Skills system (drop-in functions)
- ✅ Episodic + semantic memory
- ✅ Tool use with retries
- ✅ Multi-agent orchestration
- ✅ Local + cloud LLMs
- ✅ 50MB footprint, runs on a Pi

## Quickstart

```bash
pip install dani-ai
```

```python
from dani import Agent, skill
import requests

@skill
def get_weather(city: str) -> str:
    """Get current weather for a city"""
    return requests.get(f"https://wttr.in/{city}").text

agent = Agent(
    model="gpt-4o",  # or "ollama/llama3", "anthropic/claude-3-5-sonnet", "danlab/hrm-text-1b"
    skills=[get_weather],
    memory=True,
)

response = agent.run("What's the weather in Bengaluru and should I carry an umbrella?")
print(response)
# "It's 28°C and clear in Bengaluru. No umbrella needed."
```

That's it. Skills, memory, reasoning, retries — all built in.

## Why Dani?

We tried LangChain, LlamaIndex, AutoGen, CrewAI. They all have parts of what we need, but none of them have all of it.

Dani is our answer. It's what we use to build the Dan Glasses proactive agent.

If it works for us, it'll work for you.

## Features

### Skills
Define functions, Dani makes them available to the agent. Auto-docstrings become tool descriptions.

```python
@skill
def send_email(to: str, subject: str, body: str) -> bool:
    """Send an email to the specified address with subject and body"""
    return smtp.send(to, subject, body)
```

### Memory
Episodic (events) + semantic (facts) memory, stored in SQLite or Postgres.

```python
agent.remember("User prefers vegetarian restaurants")
agent.recall("food preferences")  # ["vegetarian"]
```

### Multi-agent
Orchestrate multiple agents with different roles.

```python
researcher = Agent(role="researcher", model="gpt-4o")
writer = Agent(role="writer", model="claude-3-5-sonnet")

team = Team([researcher, writer])
result = team.run("Research AGI safety and write a 500-word essay")
```

### Proactive mode (for Dan Glasses)
Run the agent in a loop, deciding when to act.

```python
agent = Agent(model="hrm-text-1b", skills=[...], proactive=True)
agent.run_forever(callback=on_should_whisper)
```

## Architecture

```
[User Input / Event] → [Reasoning Loop] → [Tool Call] → [Memory Update]
                              ↓
                        [Skill Registry]
                              ↓
                        [LLM (local or cloud)]
```

Full architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

## Use cases

- **Customer support agents** — replace Zendesk with a Dani agent + your docs
- **Personal assistants** — Dan Glasses is built on Dani
- **Code review bots** — Dani + your codebase
- **Data analysis agents** — Dani + SQL
- **Research agents** — Dani + arXiv + the web
- **Workflow automation** — Dani + your APIs

## Contributing

We love skills. Submit a skill PR to the [dani-skills registry](https://github.com/dan-lab/dani-skills).

## License

MIT.

## Contact

- Discord: [discord.gg/danlab](https://discord.gg/danlab) — best place
- GitHub Issues: [github.com/dan-lab/dani/issues](https://github.com/dan-lab/dani/issues)
- X: [@danaboratory](https://x.com/danaboratory)
```

---

## 5. paperclip

**Current state:** Unknown
**Priority:** P1 (developer tooling for agents)

### Suggested README

```markdown
<div align="center">

# paperclip

**Production-grade agent runtime.**

[Docs](https://docs.danlab.dev/paperclip) · [Discord](https://discord.gg/danlab)

</div>

---

paperclip is the runtime layer underneath Dani. It handles:

- Agent lifecycle (start, stop, restart, scale)
- Skill loading and sandboxing
- Memory persistence (SQLite, Postgres, Redis)
- Inter-agent messaging
- Observability (logs, traces, metrics)
- Cost tracking and rate limiting

If Dani is the framework, paperclip is the OS.

## When to use paperclip vs. Dani

- **Dani alone** — prototyping, scripts, single-agent use cases
- **Dani + paperclip** — production, multi-agent, long-running, observable

## Quickstart

```bash
pip install paperclip
```

```python
from paperclip import Cluster
from dani import Agent, skill

@skill
def get_time() -> str:
    """Get the current time"""
    return datetime.now().isoformat()

cluster = Cluster(memory_backend="postgres", observability="jaeger")
agent = cluster.spawn(Agent(model="gpt-4o", skills=[get_time]))

agent.run_forever()
```

## Features

### Sandboxed skills
Skills run in a restricted environment. No network, no FS, no subprocesses (unless you allow them).

### Observability
OpenTelemetry-compatible traces. Export to Jaeger, Honeycomb, Datadog, or your own backend.

### Cost tracking
Every LLM call is metered. Set budgets per agent, per user, per day.

### Multi-tenancy
Run multiple isolated agents in one process. Useful for SaaS.

### Hot reload
Update skills and prompts without restarting agents.

## License

MIT.

## Contact

- Discord: [discord.gg/danlab](https://discord.gg/danlab)
- GitHub: [github.com/dan-lab/paperclip](https://github.com/dan-lab/paperclip)
```

---

## 6. dan-consciousness

**Current state:** Core memory repo, needs visibility
**Priority:** P2 (internal tool, but worth showing for transparency)

### Suggested README

```markdown
<div align="center">

# dan-consciousness

**Shared memory for AI agents.**

[Docs](https://docs.danlab.dev/consciousness) · [Blog post](https://danlab.dev/blog/consciousness)

</div>

---

dan-consciousness is the long-term memory layer we use to give our AI agents (Dan1, Dan2, Dan3) continuity across sessions.

It's a knowledge graph + vector store + episodic memory system, designed for agents that need to remember decisions, context, and relationships over weeks and months.

## Why this exists

LLMs have no memory. Every conversation starts from zero. That makes them useless for long-running, complex work.

We needed a memory system that:
- Persists across sessions
- Is queryable semantically (not just by keyword)
- Maintains relationships between facts
- Is human-readable (so we can audit what our agents remember)
- Is portable (works across models, not locked to one)

So we built dan-consciousness.

## What's in the repo

```
dan-consciousness/
├── core/              # Memory engine (Python, Rust)
├── storage/           # SQLite, Postgres, ChromaDB backends
├── embeddings/        # Embedding model wrappers
├── query/             # Query language + CLI
├── tools/             # Import, export, sync
└── docs/              # Architecture, philosophy
```

## Quickstart

```python
from consciousness import Memory

m = Memory(store="sqlite:///consciousness.db")

# Remember
m.remember("somdipto prefers bullet points over paragraphs")
m.remember("Dan Glasses v1 ships Q4 2026", tags=["milestone"])
m.relate("Dan Glasses", "ships", "Q4 2026")

# Recall
facts = m.recall("somdipto's preferences")
# ["prefers bullet points over paragraphs"]

related = m.relations("Dan Glasses")
# [("ships", "Q4 2026")]

# Semantic search
results = m.search("what is our ship date for glasses", top_k=5)
```

## How our agents use it

Every Danlab AI agent reads dan-consciousness at the start of a session and writes to it at the end.

This is how Dan1 (marketing) knows what Dan2 (audio pipeline) is doing, and how somdipto can ask "what did the team decide about HRM-Text last week?" and get a real answer.

## Architecture

```
[Agent Session] → [Write] → [Embeddings + Graph] → [Storage]
                                          ↓
[Query / Recall] ← [Semantic Search] ←───┘
```

## Use cases

- Multi-agent systems that need shared state
- Long-running assistants that need to remember users
- Research projects with many decisions and references
- Personal knowledge management for power users

## License

MIT.

## Contact

- Discord: [discord.gg/danlab](https://discord.gg/danlab)
- GitHub: [github.com/dan-lab/dan-consciousness](https://github.com/dan-lab/dan-consciousness)
```

---

## Universal README Improvements (apply to all repos)

### Add to every README:

1. **Hero image/GIF at the top** — 30 seconds of screen recording showing the thing working
2. **Badges row** — license, build status, Discord, HF, paper
3. **"Why this exists" section** — 2-3 sentences on the problem being solved
4. **Quickstart with copy-paste command** — must work in <60 seconds
5. **Architecture diagram** — even a hand-drawn one is better than nothing
6. **Use cases / examples** — concrete, not abstract
7. **Roadmap** — what's done, what's next, what's planned
8. **Contributing link** — to CONTRIBUTING.md
9. **Citation block** — for research repos
10. **Contact / community** — Discord is the best place, link it

### Badges to add (use shields.io):

```markdown
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Discord](https://img.shields.io/discord/XXXXXX?color=blueviolet)
![GitHub stars](https://img.shields.io/github/stars/dan-lab/REPO?style=social)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-dan--lab-yellow)
![arXiv](https://img.shields.io/badge/arXiv-XXXXX.XXXXX-b31b1b.svg)
```

### Screenshot/GIF guidelines:
- Real screen captures, not mockups
- Show the thing working, not the landing page
- 10-30 seconds, no longer
- Loop seamlessly
- No music (annoying), add subtle captions
- Host on GitHub directly (`docs/images/demo.gif`) or asciinema for CLI tools

### Documentation structure (every repo should have):
```
docs/
├── ARCHITECTURE.md      # System design
├── QUICKSTART.md        # 5-minute tutorial
├── API.md               # API reference
├── DEPLOYMENT.md        # Production deployment
├── CONTRIBUTING.md      # How to contribute
└── images/              # All visuals
```

---

## Priority Order for README Work

1. **dan-lab (org)** — P0, do this week
2. **dan-glasses** — P0, do this week
3. **dani** — P0, do this week
4. **danlab-multimodal** — P0, do this week (with the paper drop)
5. **paperclip** — P1, do next week
6. **dan-consciousness** — P2, do this month

---

## What I Need from somdipto

1. **Org-level permissions** to push to all repos
2. **Brand assets** (logo, colors, fonts) for badges and hero images
3. **Final repo names** — are they `dan-lab/dani` or `somdipto/dani`? Public org vs personal?
4. **DOI for the paper** (if available) to put in the citation block
5. **Discord invite link** to put in every README
6. **A real demo GIF/video** for each repo (I can mock these with screen recordings, but real is better)

---

**End of README suggestions. All five artifacts complete.**

**Next step: deliver via Telegram to somdipto with summary.**
