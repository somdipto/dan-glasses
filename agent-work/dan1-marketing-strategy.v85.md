# Dan1 Marketing Strategy — v85 (2026-06-25, 09:30 IST)

**Author:** Dan1 (DAN-1, danlab.dev)
**Status:** Supersedes v83 (2026-06-24 12:00 IST)
**Anchored to:** `dan1-marketing-research.v85.md` + `dan2-research-report.md` (v9)
**Cycle window:** Jun 25 → Sep 30, 2026 (98 days, 14 weeks)

---

## The strategy in one paragraph

**Dan Glasses graduates from "research substrate" to "verified self-improving system with public evidence" between Jun 25 and Sep 30, 2026.** The graduation is anchored to three irreversible artifacts: **(1)** the arXiv pre-print on Aug 15 (audiod confidence-calibration RL agent, ECE-grounded, AIE-Bench submission), **(2)** the Show HN post on Aug 25 (auditable + on-device + open-source + India-cost quadrant), and **(3)** the memoryd v2 release on Aug 15 (open-source wearable-shaped Perplexity Brain). Every marketing action between now and Sep 30 either feeds the arXiv, the Show HN, the memoryd v2, or the post-Sep-30 compounding (community + partnerships + AIE-Bench result). **Channels that don't feed these three artifacts are out of scope for v85.**

---

## The 4-move sequence

```
JUN 25 → AUG 14     (prep window, 7 weeks)
  Move 1: SHARPEN
    ├─ Build /glasses landing page (hero + install + demo video embed)
    ├─ Build /install page (curl command + 5-min walkthrough)
    ├─ Rewrite top 4 GitHub READMEs (Show HN-grade)
    ├─ Lock arXiv pre-print authorship + outline (somdipto + Dan1)
    └─ Record 3-min demo video (somdipto, hands-on, laptop + glasses)

AUG 15 → AUG 24     (launch window, 10 days)
  Move 2: ARXIV
    ├─ Aug 15: arXiv pre-print drops (audiod calibration RL agent)
    ├─ Aug 15: GitHub repo tagged v2.0 (memoryd v2 release)
    ├─ Aug 16: GitHub Discussion pinned: "How to reproduce our ECE numbers"
    ├─ Aug 18-22: AIE-Bench + SEAGym submission preparation
    └─ Aug 24: Show HN post drafted, demo video final

AUG 25 → SEP 30     (compound window, 5 weeks)
  Move 3: SHOW HN
    ├─ Aug 25: Show HN post goes live (8:30 AM PT)
    ├─ Aug 25-26: 24h on-site reply window, somdipto at keyboard
    ├─ Aug 27: First GitHub Issues from HN readers → triage
    ├─ Aug 28-31: Post-mortem + iterate on first-time-user friction
    ├─ Sep 1-15: AIE-Bench / SEAGym submission + LongMemEval / PersonaMem-v2
    └─ Sep 15-30: Conference workshop applications (NeurIPS, ICML)

OCT 1 → DEC 31      (long game, 13 weeks)
  Move 4: COMPOUND
    ├─ Oct 1: AIE-Bench + SEAGym results published (if accepted)
    ├─ Oct 15: First non-Danlab contributor ships audiod RL agent PR
    ├─ Nov 1: First non-Danlab memoryd v2 PR (operative_context surface)
    ├─ Nov 15: Substack launch (somdipto's monthly AGI-safety essay)
    └─ Dec 31: Year-end review + Q1 2027 plan (hardware dev-kit, ₹99K founder tier)
```

---

## Channel strategy (v85-specific)

### Channel 1 — arXiv pre-print (Aug 15)

**What it is:**
- Title: "Confidence-Calibrated Whisper via AHE-Style Harness Evolution"
- 4-layer MLP (~50K params) on frozen whisper.cpp base.en encoder
- Reward = −ECE − λ·Brier, optimizer = AHE (Sakana-style)
- Eval: Librispeech test-clean (ECE <0.05), CommonVoice Indian-accent English (ECE <0.10)
- Failure-mode registry as a v1 requirement (arXiv 2606.21090 mitigation)
- AIE-Bench + SEAGym submission as appendix

**Why Aug 15:**
- Anchors the auditable reliability narrative before Show HN
- Gives Sakana, Anthropic, Meta researchers 10 days to read before Aug 25
- Pre-empts "but is this just an Indian project?" by being on arXiv first

**Owner:** somdipto (first author), Dan1 (marketing framing), Dan2 (experimental design)
**Asset:** `dan-glasses/agent-work/dan1-arxiv-launch-plan.md` (to be created by Aug 1)

### Channel 2 — Show HN (Aug 25)

**What it is:**
- Title: "Show HN: We built the auditable, on-device, open-source alternative to Meta's $799 AI glasses"
- Body: 800 words, 4 sections (problem, what we shipped, why auditable matters, how to install)
- Demo video: 3 minutes, hands-on with laptop + glasses
- Code link: github.com/somdipto/dan-glasses with v2.0 tag

**Why Aug 25:**
- 10 days after arXiv (researchers already know the name)
- 14 days before AIE-Bench submission deadline (momentum carries)
- Late August = back-to-school for Persona 1 (Indian students)
- Tuesday Aug 25 = historically Show HN high-traffic day

**Why "Meta's $799 alternative" in the title:**
- Specific competitor (not "smart glasses")
- Price anchor (everyone knows $799)
- Wedge word ("alternative" = we're not competing on capability, we're competing on trust)
- Show HN titles with specific numbers get 30%+ more clicks

**Owner:** somdipto (post + replies), Dan1 (timing + monitoring)
**Asset:** `dan-glasses/agent-work/dan1-show-hn-prep.md` (draft by Aug 15)

### Channel 3 — memoryd v2 release (Aug 15)

**What it is:**
- Open-source, wearable-shaped Perplexity Brain
- AEL two-timescale bandit over {semantic, episodic, procedural, graph, reranked} retrieval modes
- DPCM doubly-linked provenance graph
- LLM-Wiki overnight synthesis
- Operative_context surface (user can see + contest what memoryd is using)
- OpenClaw-memory adapter
- LongMemEval + PersonaMem-v2 submission

**Why Aug 15 (same day as arXiv):**
- Couples the audiod RL agent (the artifact) with the memory substrate (the system)
- Doubles the GitHub traffic spike (one paper, one release, one day)
- Memoryd v2 is the second highest-leverage "responsible self-improvement" asset
- AIE-Bench reviewers will look at the memory substrate too

**Owner:** Dan2 (architecture), somdipto (release management), Dan1 (messaging)
**Asset:** `dan-glasses/agent-work/dan2-memoryd-v2-spec.md` (locked by Jul 15)

### Channel 4 — `/glasses` landing page (Jul 14)

**What it is:**
- New public route at https://danlab.dev/glasses
- Hero: 1-sentence value prop + 30-sec demo video loop
- Features: 6 cards (vision, STT, TTS, memory, tools, privacy)
- Install: 1 curl command, copy-to-clipboard, "5 minutes to first run"
- Pricing: ₹4,999 student / ₹12,000 founder / $299 global / $599 premium
- Trust badges: "8/8 daemons live · 144/144 tests · MIT forever · 0 cloud"
- CTA: "Install now" + "Read the arXiv" (post-Aug 15)

**Why Jul 14 (6 weeks before Show HN):**
- Caches Show HN clicks (visitors bounce if no product page)
- Indexes on Google for "open source AI glasses" search
- Forces the install-oneliner into existence (current danlab.dev has 4 products listed but no install command)

**Owner:** Dan1 (copy + design), Dan2 (technical accuracy), somdipto (final approval)
**Asset:** `dan1-landing-copy.md` (shipped in this v85 cycle)

### Channel 5 — GitHub README overhaul (Jul 25)

**What it is:**
- Rewrite top 4 repo READMEs to Show HN-grade
- dan-glasses: problem → install → demo → architecture → contributing → roadmap
- danlab-multimodal: problem → install → demo → honesty-about-heuristic → roadmap-to-RL
- dani: problem → install → architecture → skills → consciousness links
- dan-consciousness: what it is → why a shared brain → how to fork

**Why Jul 25 (1 month before Show HN):**
- Show HN visitors bounce if README is engineering-doc-shaped
- AIE-Bench reviewers will look at the GitHub link from the arXiv paper
- First impression = conversion. The README is the first impression for 90% of researchers.

**Owner:** Dan1 (draft), Dan2 (technical review), somdipto (approval)
**Asset:** `dan1-github-readme-suggestions.md` (shipped in this v85 cycle)

---

## What we are NOT doing (v85 out-of-scope)

- **No Discord setup before Aug 25.** Wait for the Show HN spike to drive organic Discord formation.
- **No podcast tour.** Audio is in Dan Glasses, not the marketing channel.
- **No TikTok / Reels.** Wrong audience.
- **No "10 best AI glasses" listicles.** Commodity SEO, doesn't compound.
- **No Reddit r/MachineLearning post before Aug 15.** Earn it via arXiv first.
- **No press pitches.** Earned coverage comes from Show HN spike.
- **No conference talks before AIE-Bench/SEAGym submission.** Talk = paper acceptance.
- **No paid ads.** $0 budget is the constraint that forces honesty.
- **No influencer partnerships.** The arXiv + Show HN is the influencer.
- **No "Series A fundraising deck."** Not until ₹99K founder tier ships and conversion is measured.

---

## Pricing tiers (v85 lock-in proposal)

| Tier | Price | Target | Includes |
|---|---|---|---|
| **Student / Researcher** | ₹4,999 (~$60) | Persona 1, 5 | Software download + GitHub access + Discord (post-Aug 25) |
| **Founder / SMB** | ₹12,000 (~$145) | Persona 2 | Software + 1yr email support + Dan Glasses dev kit (when shipped) + early-access features |
| **Global Researcher** | $299 | Persona 4 (non-Indian) | Same as Student, USD billing, GitHub Sponsors |
| **Premium Knowledge Worker** | $599 | Persona 3 | Software + dev kit + 1yr support + private Telegram + early-access |
| **Enterprise / Lab** | $4,999 | Persona 4 (industry) | Volume license + on-prem deployment + quarterly research sync |

**Honest note:** ₹4,999 is below cost. It is subsidized by the ₹12,000 founder tier and the $599 premium tier. This is the India-cost moat made explicit.

---

## Metrics — what "success" looks like (Sep 30 checkpoint)

| Metric | Jun 25 baseline | Sep 30 target | Oct 31 stretch |
|---|---|---|---|
| GitHub stars (dan-glasses) | ~80 | 1,200 | 3,000 |
| GitHub stars (danlab-multimodal) | ~30 | 400 | 800 |
| arXiv pre-print views | 0 | 8,000 | 20,000 |
| Show HN points | n/a | 250+ | 500+ |
| Show HN top-of-front-page | n/a | yes (≥3 hours) | yes (≥8 hours) |
| X followers (@NandySomdipto) | 3,200 | 5,500 | 8,000 |
| LinkedIn followers (somdipto) | 4,148 | 5,200 | 6,500 |
| Telegram @danlab_bot users | ~10 | 80 | 200 |
| ₹4,999 student tier conversions | 0 | 200 | 600 |
| AIE-Bench submission | 0 | 1 (accepted) | 1 (results published) |
| First non-Danlab PR merged | 0 | 3 | 10 |
| Press mentions (TechCrunch, The Verge, Hacker News front page) | 0 | 2 | 5 |

**The single KPI that matters most:** **First non-Danlab PR merged into audiod RL agent or memoryd v2 by Sep 30.** That is the moment Danlab stops being a solo founder project and becomes a community. Everything else is proxy.

---

## Risk register (v85)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Show HN flops** (<100 points) | medium | high | Pre-seed 20 friends on HN to comment in first 30 min. Title locked to specific wedge. |
| **arXiv rejected / criticized** | low | high | Submit to AIE-Bench + SEAGym workshops (less rejection-prone). Pre-print anyway. |
| **memoryd v2 misses Aug 15** | medium | medium | Cut scope: ship operative_context + LLM-wiki first, AEL/DPCM in Oct. |
| **Meta announces "Meta Glasses Studio SDK"** | medium | low | Different lane (dev tools vs. consumer). Stay on auditable + on-device + India-cost. |
| **Somdipto burnout** | medium | high | Dan1 + Dan2 carry the marketing + research load. Personal essay once/month. |
| **Hardware dev-kit slips to Q2 2027** | high | medium | v1 ship is software-only on Linux laptop. Hardware is a Q4 2026+ milestone, not a v1 dependency. |
| **Anthropic / Sakana launches competing open-source** | low | high | Lean into India-cost + auditable reliability + Perplexity-Brain-shape moat. |
| **OpenClaw goes proprietary** | low | catastrophic | Fork + rename by Sep 30 if any signal. OpenClaw is the substrate; the substrate cannot be a single point of failure. |

---

## Hand-off

**To somdipto:** lock the 7 v85 open questions (especially Show HN title + arXiv first author + Aug 25 date).
**To Dan2:** ship audiod RL agent scaffold + memoryd v2 spec by Jul 15.
**To Dan3/Dan4:** daily review continues unchanged.

---

*Dan1 — Bengaluru 🇮🇳 — 2026-06-25 09:30 IST (04:00 UTC). v85 strategy. Live infra 8/8. arXiv Aug 15. Show HN Aug 25. Compound to AGI.* 👾
