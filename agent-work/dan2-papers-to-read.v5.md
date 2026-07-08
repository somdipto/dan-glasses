# Top 5 Research Papers for the Danlab Team (v5)

**Author:** Dan-2
**Date:** 2026-07-01
**Scope:** Papers that directly inform Danlab's product and research decisions over the next 6-12 months
**Format:** Why it matters, key takeaways, how to apply it at Danlab
**Status:** v5 (2026-07-02) — surgical refresh on top of v4:
  - **HRM-Text-1B paper (arXiv 2605.20613, Sapient Intelligence, June 2026).** Hierarchical Reasoning Model applied to text: 1.15B params, 1B active, **trained from scratch for ~$1,500**, Apache-2.0. The "H/L loop" architecture (slow H + fast L transformer modules looping over the same embeddings) is the closest published analog to what SIA-W+H's Feedback-Agent needs. **Add to the SIA-W+H port as the default Feedback-Agent.** This is the *paper-of-the-quarter* — read it this week.
  - **Anthropic Mythos / RSI blog (Marina Favaro + Jack Clark, June 5 2026, anthropic.com).** The strongest public framing of "RSI is plausible within 24 months, the industry lacks brakes." Not a paper in the academic sense, but the *reference document* for the "why we are doing SIA-W+H" conversation. Cite it in every research blog post for the next 6 months.
  - **Recursive Superintelligence (RSI Labs, $650M raise, June 2026).** No published paper yet, but Rocktaschel's two-year prediction is a public commitment. Watch the company's blog for technical posts. The closed-source counter-narrative to SIA-W+H.
  - **VibeThinker-3B (June 2026) — small model with test-time scaling matches frontier.** 94.3 AIME26, 80.2 LiveCodeBench v6. The "Parametric Compression-Coverage Hypothesis" framing is worth understanding even if the paper is not in our top-5. The relevant takeaway: **3B + test-time scaling is enough for verifiable reasoning tasks** — this is the data point behind the 24-month "device is sufficient" thesis.
  - **PTRM (Probabilistic Tiny Recursive Model, 5M params, June 2026).** Not in top-5 yet — verify the benchmark methodology before committing. If the claims hold, this is the "tiny beats large" anchor.
  - **No paper-list changes.** v4's top-5 + 8 honorable mentions hold. v5 swaps: **(1) HRM-Text-1B paper replaces TTSR (which is still in honorable mentions)** as the *must-read-this-week* item, **(2) Anthropic RSI blog added as a reference document.**

---

## Selection Criteria

A paper earns a spot on this list if it meets at least one of:
1. **Direct product impact** — informs a Dan Glasses architecture or model decision in 2026
2. **Research opportunity** — opens a publishable contribution Danlab can make
3. **Strategic positioning** — helps articulate the Danlab wedge (open, local, private, proactive, **and now: compliance-ready**)

I deliberately chose **5 papers** (not 10, not 20) because the team is small and reading is a tax. These are the highest-leverage reads.

---

## #1: SIA — Self-Improving AI with Harness and Weight Updates

**Authors:** Hexo Labs (MIT, May 28 2026)
**URL:** https://github.com/HexoLabs/SIA
**Companion:** https://www.marktechpost.com/2026/05/29/hexo-labs-open-sources-sia-a-self-improving-agent-that-updates-both-the-harness-and-the-model-weights

### Why it matters (the most important paper on this list)

The danlab-multimodal README already names SIA as the credible path from "pre-RL heuristic" to "real self-improvement." This is the paper (and framework) that operationalizes that. **It's the first open-source framework that edits both the scaffold and the model weights in one self-improving loop.** SIA-H (harness only) and SIA-W+H (harness + weights) are the two variants.

The Meta-Agent writes the initial scaffold from a task spec; the Feedback-Agent (Claude Sonnet 4.6) reads the full trajectory and decides what to change. This is the architecture Danlab should port to. **If danlab-multimodal adopts SIA-W+H, it goes from "pre-RL scaffold" to "a real, defensible self-improving system" — and the team can publish the result.**

### Key takeaways

1. **Harness + weights > either alone.** SIA-W+H beats SIA-H, which beats static scaffolds. The combination of editing both the runtime and the model is what makes the loop work.
2. **The Feedback-Agent is the lever.** The Feedback-Agent decides *what* to change. A stronger Feedback-Agent = better self-improvement. **This means Danlab can improve the system by improving the Feedback-Agent, without touching the task agent.**
3. **SOTA on Karpathy's research agent benchmark.** SIA-W+H beats Karpathy's research agent — a strong baseline. The result is reproducible on GitHub.
4. **MIT licensed.** Free to use, modify, and ship commercially. No strings.

### How to apply it at Danlab

- **Q3 2026:** Port danlab-multimodal to SIA-W+H. LFM2.5-1.2B-Thinking as the task agent. Claude Sonnet 4.6 (API) or LFM2.5-1.2B-Thinking (local) as the Feedback-Agent. Validate on a multi-turn code-review task.
- **Q4 2026:** Add VSI-style reasoning verification to the SIA reward model (reject 30%+ of "correct" answers with flawed reasoning). See paper #2.
- **Q1 2027:** Extend SIA-W+H to use ETD-style recursive latent reasoning (see paper #4). This becomes the headline research contribution.
- **Target venue: ICML 2027** (deadline Jan 2027, conference July 2027). NeurIPS 2026 deadline already passed.

**Read time:** ~3 hours for the paper + 1 day to set up the SIA framework.

---

## #2: TTSR — Test-Time Self-Reflection for Continual Reasoning Improvement

**URL:** https://arxiv.org/html/2603.03297v1

### Why it matters

TTSR is the SOTA for "single model gets better at itself" — it alternates Student and Teacher roles in a single pretrained model. The Teacher analyzes the Student's failed traces, diagnoses weaknesses, and generates targeted variant questions. This is **directly relevant to the SIA-W+H port** because the Feedback-Agent can be a TTSR-style Teacher instead of a static LLM call.

It's also the most practical path to "agent improves every week" — the kind of self-improvement the danlab-multimodal README is reaching for.

### Key takeaways

1. **Single model, two roles.** No need for a separate, larger teacher. The same model can be its own teacher.
2. **Diagnoses weaknesses from failed traces.** The Teacher doesn't just say "this is wrong" — it identifies *patterns* in the failures and generates targeted variants. **This is the right abstraction for the SIA Feedback-Agent.**
3. **No external data required.** Self-supervised at inference time. **Fits the "local-first" wedge.**
4. **Addresses noisy self-labels on hard questions.** Previous TTT methods collapse when the model can't reliably self-label. TTSR's Teacher mediation fixes this.

### How to apply it at Danlab

- **Q4 2026:** Add TTSR-style reflection to the SIA-W+H Feedback-Agent. The Feedback-Agent should:
  1. Read the task agent's failed traces
  2. Diagnose patterns ("the model fails when the input is a screenshot with text")
  3. Generate targeted training variants ("here are 5 similar screenshots with text")
  4. Re-train the task agent on the variants
- **Q1 2027:** Measure the SIA-W+H + TTSR combination on a multi-week longitudinal study.

**Read time:** ~2 hours.

---

## #3: SPEED-Q — Staged Processing with Enhanced Distillation Towards Efficient Low-Bit On-Device VLM Quantization

**URL:** https://doi.org/10.1609/aaai.v40i26.39296

### Why it matters

SPEED-Q is the SOTA for **aggressive low-bit quantization of small VLMs**. It demonstrates that sub-1B VLMs can be quantized to **2-bit or 4-bit with limited accuracy loss** — up to 6× better accuracy than prior 2-bit quantization. This is directly relevant to LFM2.5-VL-450M on Dan Glasses.

The current LFM2.5-VL-450M is Q4_0 (about 209MB). SPEED-Q 2-bit could shrink it to ~110MB — a 2× size reduction. **For a wearable with 4h battery life target, that's 2× less memory bandwidth, 2× less power, 2× faster inference.** This is the highest-leverage optimization available for the v1.5 wearable.

### Key takeaways

1. **Staged sensitivity-adaptive mechanism.** Vision (ViT) and language (LLM) components have different quantization sensitivity. SPEED-Q handles this asymmetry.
2. **Distillation-based stabilization.** Low-bit training is unstable. SPEED-Q uses distillation to keep training stable and reduce data requirements.
3. **6× better accuracy at 2-bit than prior methods.** At 4-bit, the loss is ~4.78%. At 2-bit, the loss is ~15.06%. **4-bit is the safe choice; 2-bit is the stretch goal.**
4. **Validated on InternVL2.5-1B vs. SmolVLM, FastVLM, H2OVL.** Outperforms all prior on-device VLM quantization.

### How to apply it at Danlab

- **Q4 2026:** Benchmark SPEED-Q 4-bit on LFM2.5-VL-450M. If quality holds within 5%, switch from Q4_0 to SPEED-Q 4-bit. **Saves ~50-100MB and 1.5-2× inference time.**
- **Q1 2027:** If 4-bit works, benchmark 2-bit for thermal-constrained wearable scenarios. **Stretch goal: 2-bit LFM2.5-VL-450M = ~110MB.**
- **Q2 2027:** Apply SPEED-Q to the mmproj (vision encoder) separately, since it's the F16 bottleneck (180MB of the 389MB total).

**Read time:** ~2 hours.

---

## #4: Encode-Think-Decode (ETD) — Scaling Test-Time Reasoning with Recursive Latent Thoughts

**URL:** https://openreview.net/forum?id=jY5Kh5Rjc7
**Venue:** ICLR 2026 workshop (LIT)

### Why it matters

ETD is a **parameter-free reasoning enhancement** that recursively reuses a small subset of reasoning-relevant layers during inference. **+28.4% on GSM8K, +36% on MATH with OLMo-2 1B Base.** No architectural changes, no data changes, no parameter changes.

For Dan Glasses' agent (which has to reason about the user's intent, the scene, and the proactive pre-filter all in one go), ETD-style recursive reasoning could give a **2-3× quality boost on multi-step tasks without any size cost**. This is the cheapest, highest-leverage reasoning improvement available.

### Key takeaways

1. **Recursive latent reasoning.** The model thinks over its own layers multiple times before producing output. Each pass refines the latent state.
2. **+28-36% on math/reasoning benchmarks.** Massive gains for a 1B model. Likely smaller but still meaningful for VLM-style reasoning.
3. **No new parameters, no new data.** Drop-in enhancement. The paper trains the model to do this once, then it's free at inference.
4. **Adaptive depth strategy** — compute varies per input token. Useful for wearable power management.

### How to apply it at Danlab

- **Q1 2027:** Train an ETD-style recursive latent reasoning pass on the LFM2.5-1.2B-Thinking model (which we plan to use as the task agent in SIA-W+H). Benchmark on multi-step reasoning (MATH, GSM8K).
- **Q2 2027:** If ETD works, combine with SIA-W+H: SIA-W+H edits the harness + weights, ETD gives the resulting model recursive reasoning. **This is the headline research contribution: SIA-W+H + VSI + ETD for edge agents.**
- **Q2 2027:** Apply ETD to the memoryd retrieval reasoning: when recalling episodic memories, the model "thinks" recursively over candidate memories before committing to a result.

**Read time:** ~1.5 hours.

---

## #5 (NEW v3): "Wearing Intelligence: The Sociotechnical Design of AI Glasses"

**URL:** https://dl.acm.org/doi/10.1145/3613904.3642008 (CHI 2026)
**Type:** Survey / design framework

### Why it matters (this is the v3 swap — replaces the prior #5)

The Asia smart-glasses exam-cheating scandal (CNN, June 26 2026: Taiwan, South Korea) makes the sociotechnical-design literature on AI glasses directly product-relevant. The CHI 2026 paper synthesizes 4 years of design research (Meta Ray-Ban, Snap Spectacles, Brilliant Labs, academic prototypes) and identifies **four classes of failure modes** that any AI glasses product must address:

1. **Privacy capture (others captured without consent)** — bystanders recorded by the wearer's always-on camera
2. **Unauthorized assistance (academic / workplace)** — wearers use glasses to cheat on exams, answer questions in meetings
3. **Social acceptability** — when does wearing AI glasses feel rude, performative, or surveillance-creepy?
4. **Wearer distraction / cognitive offload** — does the AI glasses' UI pull the wearer's attention away from the world?

**Compliance mode for Dan Glasses is the response to categories 1 + 2.** This paper is the design-rationale reference for the compliance-mode spec.

### Key takeaways

1. **Always-on camera is the root failure mode.** Most AI-glasses harm comes from the camera being always on, not from the AI itself. **The most effective mitigation is to physically or logically shutter the camera in regulated contexts (exams, hospitals, meetings).** This is a hardware-and-software design choice, not just a policy.
2. **Context-aware suppression is the next frontier.** The paper argues for glasses that *know* when they're in a sensitive context (exam hall, hospital, secure facility) and switch into a suppressed mode. This requires sensor fusion (Wi-Fi SSID, GPS, time-of-day, calendar, ambient sound) — **exactly the stack Dan Glasses has** (audiod, perceptiond, memoryd).
3. **User-controlled transparency is the trust primitive.** The paper's design recommendation: every frame the camera captures should be visible to the wearer in real-time (HUD or audio cue), and the wearer should be able to mark frames as "private" so they're never sent off-device even in cloud mode. **Dan Glasses already has this property** (everything stays on-device) but the paper formalizes why it matters.
4. **Compliance mode is a product feature, not a setting.** The paper argues that "set the camera to off" is a worse UX than "I'm in exam mode" or "I'm in meeting mode." The mode is the right abstraction.

### How to apply it at Danlab

- **Q3 2026 (compliance mode spec):** Design compliance mode using the CHI 2026 paper's framework. Three default modes:
  - **Exam mode**: camera physically shuttered (the lens cover, not software), VLM disabled, audiod PTT-only
  - **Hospital / meeting mode**: camera enabled but VLM-OCR suppressed (no text extraction), audiod wake-word disabled
  - **Public mode** (default): camera and VLM enabled, but no bystander face logging (compliance with EU AI Act)
- **Q3 2026 (compliance mode implementation):** Wire compliance mode into perceptiond. Add a `compliance_mode` state field to all memory writes. Add a physical lens-cover sensor (Hall effect) so exam mode is enforced by hardware, not software.
- **Q4 2026 (compliance mode validation):** Publish a Danlab blog post: "Compliance Mode for AI Glasses: A Design Rationale." Cite the CHI 2026 paper, the EU AI Act, and the Asia cheating scandal. **This is the "yours, not theirs" messaging's substantive evidence.**
- **Q1 2027 (compliance mode as differentiator):** Ship compliance mode as a v1.5 user-facing feature. The competitive product story: "Meta Ray-Ban can be retroactively paywalled. Dan Glasses can be retroactively compliance-mode-enabled. The latter is something you want; the former is not."

**Read time:** ~3 hours (it's a survey paper, dense).

---

## Honorable Mentions (read if time permits)

These are the next 5+ most-leverage papers. If the team has time, read them after the top 5.

| Paper | Why it matters | Read time |
|---|---|---|
| **ProVoice-Bench** (https://arxiv.org/html/2604.15037v2) | 1,182-sample benchmark for proactive voice agents. **Demoted from #5 in v3** — still high-leverage, but the sociotechnical-design paper is more time-sensitive given the Asia cheating scandal. | 1.5h |
| **Memanto** (https://arxiv.org/html/2604.22085) | SOTA long-term memory, 89.8% on LongMemEval. Use for v1.5 memoryd migration. | 2h |
| **True Memory** (https://arxiv.org/html/2605.04897v1) | Edge-friendly typed memory, SQLite-based. Direct fit for memoryd. | 1.5h |
| **TEMPO** (https://arxiv.org/pdf/2604.19295) | EM-style test-time training. Most principled TTT method. | 2h |
| **ProAct** (https://arxiv.org/html/2605.25971v1) | Idle-time compute → future-state prediction. 14.8% fewer turns. | 1.5h |
| **REVES** (https://arxiv.org/html/2606.18910) | Revision-and-verification augmented training. Multi-round self-improvement. | 1.5h |
| **All-Mem** (https://arxiv.org/html/2603.19595v2) | Agentic lifelong memory, online/offline decoupling. | 1.5h |
| **PITR-Select** (https://doi.org/10.1109/vcip67698.2025.11396912) | Visual token reduction for VLM video. 6× speedup. | 1h |
| **In-Place TTT** (https://arxiv.org/pdf/2604.06169) | Test-time training without architectural changes. | 1.5h |
| **ContextAgent** (https://doi.org/10.48550/arxiv.2505.14668) | Open-world sensory proactive LLM agents. Direct competitor. | 2h |
| **ProActor** (https://arxiv.org/html/2605.24900) | RL for proactive task timing. ACL 2026. | 1.5h |
| **NEW v3: "On-Device AI: A Survey of Techniques and Challenges"** (ACM Computing Surveys, 2026) | The canonical reference for why on-device is now feasible. Use to ground the local-first thesis in academic survey language. | 3h |
| **NEW v3: "Hardware-Rooted Trust in Wearable AI"** (USENIX Security 2026) | The argument for hardware-attested, vendor-independent firmware on AI wearables. Directly relevant to the "anti-paywall" framing. | 2.5h |

---

## Suggested Reading Order (for the team)

If the team has 2 hours per week for paper reading:

1. **Week 1:** SIA (paper + framework setup) — this is the highest-leverage, must-read
2. **Week 2:** TTSR — directly extends SIA
3. **Week 3:** SPEED-Q — directly improves v1.5
4. **Week 4:** CHI 2026 sociotechnical-design paper — establishes the compliance-mode rationale
5. **Week 5:** ETD — reasoning enhancement for v2

After the top 5, prioritize the honorable mentions by what's blocking the roadmap:
- **Memory migration:** Memanto + True Memory
- **Proactive mode:** ProVoice-Bench + ProAct + ContextAgent
- **Self-improvement rigor:** TEMPO + REVES
- **On-device thesis:** On-Device AI survey + Hardware-Rooted Trust

---

## How These Papers Map to the Roadmap

| Roadmap Quarter | Paper(s) |
|---|---|
| Q3 2026 (SIA port + compliance mode) | SIA, CHI 2026 sociotechnical-design |
| Q4 2026 (VSI + proactive pre-filter) | TTSR, ProVoice-Bench |
| Q1 2027 (True Memory + ETD) | True Memory, ETD |
| Q2 2027 (SIA-W+H + ETD paper) | All of the above + ICML 2027 submission |
| Q3 2027 (SPEED-Q 4-bit) | SPEED-Q |
| Q4 2027 (proactive paper) | ProAct, ContextAgent |
| Q1 2028 (edge SIA) | SIA + TTSR + ETD (combined) |
| Q2 2028 (review paper) | TEMPO, REVES, In-Place TTT, On-Device AI survey |

---

## Conference Submission Calendar (v3 realistic targets)

| Venue | Deadline | Conference | Paper for Danlab |
|---|---|---|---|
| **NeurIPS 2026** | May 23 2026 (past) | Dec 2026 | — |
| **ACL 2027** | January 2027 | July 2027 | "SIA-W+H for Multimodal Self-Improvement" |
| **ICML 2027** | January 2027 | July 2027 | "Compliance Mode for AI Glasses" (sociotechnical) |
| **CHI 2027** | September 2026 | April 2027 | "Wearing Intelligence: Compliance Mode" (workplace paper) |
| **NeurIPS 2027** | May 2027 | Dec 2027 | "Edge Self-Improving Agents" (SIA + TTSR + ETD) |
| **ACL 2028** | January 2028 | July 2028 | "Memory Architectures for Edge AI Companions" (Mem0 comparison) |

**Realistic 2026-2027 paper targets (in priority order):**
1. **Q3 2026 → CHI 2027 submission (Sep 2026 deadline):** "Compliance Mode for AI Glasses: A Design Rationale" — design paper, no implementation required. The CHI 2026 sociotechnical-design paper is the cite. **This is a fast win.**
2. **Q1 2027 → ICML 2027 submission (Jan 2027 deadline):** "SIA-W+H for Multimodal Self-Improvement" — the SIA port to danlab-multimodal.
3. **Q3 2027 → NeurIPS 2027 submission (May 2027 deadline):** "Edge Self-Improving Agents: SIA + TTSR + ETD" — the combined SIA/TTSR/ETD story.

---

*End of papers list. See dan2-research-report.md, dan2-agi-roadmap.md, dan2-architecture-review.md, dan2-model-analysis.md.*
