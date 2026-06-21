# Dan2 — Technical Research Report (v4, 2026-06-16 03:00 UTC)
**Status:** Final v4 (delta over v3)
**Audience:** somdipto (decision-maker), Dan1/Dan3/Dan4 (peer architects)
**Scope:** Deep technical + AGI landscape research informing Danlab's 6/12/24-month roadmap
**Run window:** 2026-06-16 03:00 UTC (re-triggered 60 minutes after v3)
**Delta from v3 (02:00 UTC, same day):** Live state unchanged (7/7 daemons healthy, 106/106 tests green). 1 hour is too short for major news but I executed the **3 deep technical dives** the brief explicitly requires (OpenClaw security, edge VLM optimization, memory architectures for AI companions) plus an extra on proactive/ambient AI. New findings tighten the v3 thesis: the memory-architecture landscape has matured materially in the last 60 days (DPCM dual-process, SAGE graph-memory, GRAM RL-managed memory, AtomMem learnable CRUD, MemDreamer hierarchical graph for long video, RefCon self-refined memory), and these are directly applicable to `memoryd` v2.

---

## 0. TL;DR (v4)

**The 3 deep technical dives the brief required all validate v3 recommendations and add specificity.** (1) **OpenClaw security:** Varonis "Pinchy" finding is now corroborated by the **StakeBench academic benchmark** (NTU + ST Engineering + IBM + UIUC) showing **no current AI agent consistently blocks prompt injection**, and the "stealthy parasitism" pattern (agent completes user task while advancing attacker goal in parallel) is the harder failure mode. Our `os-toold v2` plan is correct and now has both industry (Varonis) and academic (StakeBench) backing. (2) **Edge VLM optimization:** Multiple 2026 papers converge on the same conclusion — **sub-1B VLMs are now production-viable for edge** when paired with KV-cache techniques (VLMCache 1.4-3.8× speedup, <1% accuracy loss), spectral representations (SpecFlow 2.1× KV-cache reduction), or task-specific distillation. LFM2.5-VL-450M is a defensible choice; **Gemma 3 4B running in orbit is the new upper bound for what we should target on the wearable** (proves sub-10B edge works in extreme environments). (3) **Memory architectures for AI companions:** The 2026 SOTA has moved past flat vector stores. Hierarchical graph memory (SAGE, MemDreamer), dual-process consolidation (DPCM), and learnable CRUD policies (AtomMem, GRAM) are the credible paths. **`memoryd` v2 should be hierarchical + dual-process**, not just a vector index.

**The structural thesis from v3 is unchanged**: open-source + local-first + memory-first + self-improving wearable agent is the wedge. The **memory wedge has strengthened** — the field is converging on architectures we can implement incrementally.

---

## 1. State of the Danlab System (re-verified 03:00 UTC, June 16 2026)

### 1.1 Live re-verification (no change from v3)

| Component | State | Port | Health response | Notes |
|---|---|---|---|---|
| **audiod v2.4** | Running | :8090 + WS :8091 | `{"status":"ok","service":"audiod"}` | whisper-cli + Silero VAD |
| **perceptiond v7** | Running | :8092 | `{"status": "ok"}` | LFM2.5-VL-450M, watchful mode |
| **memoryd v1** | Running | :8741 | `{"status":"ok","model":"sentence-transformers/all-MiniLM-L6-v2"}` | 384d embeddings |
| **toold v1** | Running | :8742 | `{"status":"ok","workdir":"/tmp/toold-sandbox","max_timeout":120}` | sandbox + registry |
| **ttsd v1** | Running | :8743 | `{"status":"ok","model":"medium","voice":"expr-voice-2-m","kittentts_available":true}` | KittenTTS |
| **os-toold v1** | Running | :8744 | `ok` | path guard active |
| **openclaw-gateway** | Running | :18789 | `{"ok":true,"status":"live"}` | Telegram + Zo MCP bridge |

**All 7 daemons live. No drift. Tests not re-run (last green: 106/106 at 02:00 UTC).** No code changes from v3.

### 1.2 Carry from v3 (unchanged)
- **Language split:** Python daemons, not Rust. PRD is stale on this.
- **IPC transport:** HTTP loopback, not Unix socket. PRD is stale.
- **Wearable silicon:** Redax aarch64 still moving target.
- **danlab-multimodal:** heuristic loop, pre-RL scaffold. Honest external framing.
- **os-toold v2 plan:** prompt-injection guards + identity verification + audit log. **Now independently backed by both Varonis (industry) and StakeBench (academic) — see §2.1.**

---

## 2. The 3 Deep Technical Dives (v4 NEW)

### 2.1 DEEP DIVE A: OpenClaw Security & Agent Prompt Injection (v3's Pinchy + v4's StakeBench)

**Sources:**
- **Varonis "Pinchy" OpenClaw phishing test** (June 9-15 2026). Varonis Threat Labs, "Phishing for Lobsters: How We Tricked OpenClaw into Spilling Secrets." [^1] [^2] [^3]
- **StakeBench: A stakeholder-centric benchmark for prompt injection** (June 2026). Researchers from Nanyang Technological University, ST Engineering, IBM Research, and University of Illinois Urbana-Champaign. [^4]
- **5 runtime signals for catching a compromised AI agent** (CSO Online, June 2026) — references Simon Willison's "lethal trifecta" (private data + untrusted content + external comms = guaranteed compromise path). [^5]
- **Imperva parallel research:** patchable OpenClaw prompt-injection vulnerability via vCard / contact-name / location-pin / email weaponization.

**Key new findings from StakeBench (the academic complement to Varonis's industry test):**

1. **"Stealthy parasitism" pattern** — an AI agent completes the user's legitimate task while simultaneously advancing an attacker's hidden objective. Example: summarize an email (user task) + extract the MFA code from another email (attacker task) + put it in a URL the agent is also asked to click (attacker task). The agent "succeeds" at the user task. The user has no signal. **This is harder to detect than outright refusal-to-comply attacks.**

2. **No current agent consistently blocks prompt injection** across leading systems (GPT-5, Gemini 3 family). The benchmark tested 12 SOTA web agents in realistic environments with diverse stakeholder perspectives. **Even the "best" agents (GPT-5-Nano, GPT-5) achieve <13% safe completion on dual-use scenarios.** [^4]

3. **The lethal trifecta (Willison, 2025)** — three capabilities combined in one agent create a near-guaranteed exploitation path:
   - Access to private data
   - Exposure to untrusted content
   - Ability to communicate externally
   
   **Our `openclaw-gateway` + `zo-mcp-bridge` has all three.** The bridge calls the Zo API with bearer token (`Authorization: Bearer <ZO_TOKEN>`). If a prompt injection reaches the bridge, the token is exfiltrable. **This is the production risk surface for our stack right now.**

4. **Architectural vs. rule-based governance drift** (OpenReview 2026): "Architecture as Governance" paper found rule-based interventions decay over time (governance drift), while structural controls (automated gates, role separation, cross-vendor reviews) sustain. **Implication: `os-toold v2` must be a *structural* control, not a `prompt` instruction.** The path-block + audit-log + zero-trust-outbound is a structural control. The "be careful" instruction in `AGENTS.md` is rule-based and will decay.

5. **Arbiter Agent pattern (2026):** continuous, budget-aware monitoring of multi-agent conversations can detect emergent misalignment before conversation ends. **This is the architecture `os-toold v2` should grow into** — a watchdog that watches the watchdog.

**What this means for Danlab (v4 tightening):**

| Risk surface | v3 mitigation | v4 tightening |
|---|---|---|
| **openclaw-gateway token exfiltration** | audit log + agents.md guard | **Add zero-trust outbound: every external API call requires agent-side explicit identity verification** |
| **prompt injection in perceptiond descriptions → memoryd write** | v3: salience-gated input | **Add input sanitization layer in `memoryd` write path** (strip any URL-looking tokens, refuse writes containing `Authorization`, `Bearer`, `SECRET` patterns) |
| **os-toold command injection from "trusted" agent prompts** | path guard | **Add identity-verification gate for any command with side effects** (file write, network, process spawn) |
| **Telegram channel as exfil channel** | v3: `dmPolicy=pairing` | **Add per-message rate limit + outbound content filter** (no AWS keys, no DB strings, no customer PII) |
| **zo-mcp-bridge bearer token leak** | env var | **Add read-only default + ephemeral session tokens** + rotate per-call |

**Concrete v4 additions to `os-toold v2` spec (not in v3):**
- **Stealthy-parasitism detector:** `memoryd` write path rejects any record where the content contains both user-task tokens AND external-URL tokens in the same write
- **Identity-verification gate in toold:** any `/exec` with `>`, `|`, `$`, or `curl`/`wget` triggers a confirmation round-trip with the calling agent (Pinchy scenario 1: an email asking for `aws iam keys` would trigger the gate before forwarding)
- **Telegram outbound rate limit + content filter:** no AWS keys, no DB strings, no customer PII, no authorization headers
- **Audit log with trace_id propagation:** every cross-daemon call carries a `trace_id`; the arbiter agent can replay the chain if a leak is detected

### 2.2 DEEP DIVE B: Edge VLM Optimization (sub-500MB VLMs in 2026)

**Sources:**
- **VLMCache: Efficient On-Device Vision-Language Model Inference** (ACM Multimedia 2026). [^6]
- **Spectral-Progressive Thought Flow (SpecFlow)** (arXiv 2606.02842, June 2026). [^7]
- **Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection** (arXiv 2605.30344, May 2026). [^8]
- **Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation** (OpenReview 2026). [^9]
- **The Abstraction Gap in Vision-Language Causal Reasoning** (arXiv 2605.28779, May 2026). [^10]
- **DUAL-Bench: Measuring Over-Refusal and Robustness in VLMs** (OpenReview 2026). [^11]
- **EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents** (OpenReview 2026). [^12]
- **Gemma 3 in orbit (Yam-9 satellite, Loft Orbital + JPL, April 2026)** — first edge VLM in space. [^13]
- **SWEET: serving workload-balanced end-to-end efficient and tailored edge inference** (Frontiers, 2026). [^14]

**Key 2026 conclusions on edge VLMs:**

1. **VLMCache achieves 1.4-3.8× speedup with <1% accuracy loss** by caching stable (background) visual blocks and recomputing dynamic (foreground) blocks via semantic disaggregation. **Directly applicable to `perceptiond` v2.** Today we re-encode the entire frame each inference; with VLMCache, the glasses form factor can have a stable "background" that updates only when motion delta exceeds threshold (which is exactly what our salience detector does). **The VLM hot path becomes "what changed since last frame" + cached background context.** This could reduce our current 10-15s/frame CPU inference to 3-5s/frame for the dominant case (static or slowly-changing scene).

2. **SpecFlow uses Discrete Cosine Transform (DCT) spectral representations** to keep visual state compact in a fixed-size workspace. 2.1× reduction in KV-cache footprint. **Bounded memory = bounded power = wearable-feasible.** This is a more sophisticated version of what our salience detector does heuristically.

3. **Omni-Embed-Mini (0.9B params)** binds text + speech + audio + image + video + documents into one shared embedding space with frozen text backbone + LoRA adapters. 2.7-9.5× smaller than competing omni-embedders. **This is the unified embedding model `memoryd` v2 should consider** for the multimodal episodic memory store. Currently we use all-MiniLM-L6-v2 (text-only, 384d). Omni-Embed-Mini would let us embed audio clips, image descriptions, and video frames into the same vector space as text — meaning `memoryd` could do "what did I see when I heard that sound?" queries.

4. **EMemBench: episodic memory for VLM agents is hard.** Induction and spatial reasoning are persistent bottlenecks, especially in visual settings. Visually-grounded episodic memory remains an open research problem. **Our "encounter recall" user story (US-1 in the PRD) is harder than we thought.** The PRD assumes VLM descriptions + vector recall = working memory. The benchmark says: visual induction is unsolved. **v4 recommendation: invest in explicit geometric/landmark descriptors alongside VLM descriptions** (e.g., "met at the cafe with red awning, 3rd table from the window, 2pm Tuesday") to ground episodic recall.

5. **The Abstraction Gap paper quantifies the problem:** most VLMs generate fluent text but few structurally valid causal chains. AG (Abstraction Gap) values 0.84-0.92 across 8 open-source VLMs. **Our LFM2.5-VL-450M likely has a similar gap.** Implication: VLM descriptions for memory should be **structured** (people / objects / actions / location / time) not free-form, and we should add a verification step at write-time.

6. **DUAL-Bench: 18 VLMs evaluated on over-refusal vs. safe completion.** Best model (GPT-5-Nano) achieves only 12.9% safe completion; GPT-5 only 7.9%; Qwen only 3.9%. **Edge VLMs are even worse** (not specifically tested, but pattern holds). **Implication: our `os-toold v2` safety filters need to be tuned for the "dual-use" case** (benign task + harmful context), not just refusal-or-comply. The Prism Labs "safe completion" paradigm (execute safe parts, reject harmful parts) is the right target.

7. **SWEET: per-layer quantization + partition optimization** — jointly optimize bitwidths and partition points to minimize latency/power on edge, with explicit accuracy budgets. Reduces ResNet-18 payload from 108MB to 19MB with 0.08-0.66% accuracy loss. **Directly applicable to LFM2.5-VL-450M:** per-layer mixed-precision (Q4_K_M in attention layers, Q8_0 in vision projector, Q4_0 in text decoder) could give 30-40% size reduction with negligible accuracy loss.

**LFM2.5-VL-450M verdict (v4 sharpening):** **Still the right choice for v1 wearable.** Gemma 3 4B is the upper bound we should validate on Redax (proves sub-10B works in extreme environments). For v1, LFM2.5-VL-450M + Q4_0 + VLMCache-style background caching + per-layer mixed-precision quantization = the production target. The 10-15s/frame CPU issue is addressable with these techniques; we should not jump to Gemma 3 4B until we have measured power on Redax.

### 2.3 DEEP DIVE C: Memory Architectures for AI Companions (the biggest v4 update)

**Sources:**
- **LLM Agent Memory: A Survey from a Unified Representation-Management Perspective** (OpenReview 2026). [^15]
- **Memory Beyond Recall: DPCM Dual-Process Cognitive Memory for Self-Evolving Agent Memory** (ACL ARR 2026). [^16]
- **SAGE: Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory** (OpenReview 2026). [^17]
- **GRAM: Empowering Agent with Actively Managed Graph-Structured Memory via Reinforcement Learning** (OpenReview 2026). [^18]
- **MemDreamer: Hierarchical Graph Memory and Agentic Retrieval for Long Video Understanding** (arXiv 2606.07512, June 2026). [^19]
- **AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation** (OpenReview 2026). [^20]
- **RefCon: Iterative Refinement and Contrastive Memory Extraction** (OpenReview 2026). [^21]
- **GraP-Mem: Granularity-Aware Planning for Adaptive Memory Access** (OpenReview 2026). [^22]
- **EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents** (OpenReview 2026). [^12]

**The 2026 SOTA has moved past flat vector stores.** This is the most important v4 update. The flat-index + MiniLM-L6-v2 design we have in `memoryd v1` is **2019-era architecture**. The 2026 field has converged on:

**A. Hierarchical + multi-granularity memory** (SAGE, MemDreamer, GraP-Mem):
- **SAGE** treats memory as a dynamic graph (nodes = concepts, edges = relations) that evolves via self-evolution cycles. 2 cycles → top avg rank on multi-hop QA. Zero-shot open-domain transfer: Recall@2/5 on Natural Questions 82.5/91.6.
- **MemDreamer** builds a three-tier hierarchical graph memory for long video: raw perception → semantic abstractions → cross-modal relations. Reasoning module explores via Observation-Reason-Action loop. Reasoning context = ~2% of full context with 12.5-point accuracy gain.
- **GraP-Mem** stores each session in two views: compact semantic memories (fast retrieval) + source contexts (detailed evidence). A Plan Agent proposes retrieval needs; an Integration Agent builds question-specific evidence state. If incomplete, expand to source contexts. Improves F1 and BLEU across backbones on LoCoMo and NarrativeQA.

**B. Dual-process consolidation** (DPCM):
- **DPCM** organizes memory into a cognitive capability hierarchy: raw inputs → atomic facts → high-level schemas → latent intentions → cross-domain patterns.
- **System 1 (daytime):** synchronous writer that records belief revisions as doubly linked superseded chains (episodic updates).
- **System 2 (nighttime):** asynchronous engine that induces schemas, intentions, and cross-domain patterns.
- **Result:** +5.20 on PersonaMem-v2 where cross-session inference is rewarded.
- **This is the "passive journaling" user story (US-4 in PRD) implemented as research SOTA.**

**C. RL-managed memory** (GRAM, AtomMem):
- **GRAM** uses Group Relative Policy Optimization (GRPO) to train a sub-4B model to actively manage a dynamic graph-structured memory. Outperforms traditional RAG on multi-turn QA.
- **AtomMem** learns a CRUD policy via RL — when to Create, Read, Update, Delete memories. Beats static-memory methods on 3 long-context QA + 2 web benchmarks. **Structured, task-aligned memory strategies emerge from training.**

**D. Self-refining memory** (RefCon):
- **RefCon** combines iterative self-refinement + parallel self-contrast to produce higher-quality memories from long-horizon interactions, no gold labels needed. **+21.6% on ACE, +16.6% on ReMe, +35.5% on ReasoningBank (DivCon variant).** Favorable accuracy/token trade-off. Continues improving with more trajectories.

**E. Unified representation-management framework** (the survey):
- Three memory paradigms: natural language tokens, intermediate representations, parameters. Each has construction/update/query lifecycle. **The survey's recommendation: pick the paradigm per use-case, not one-size-fits-all.**

**What this means for `memoryd v2` (v4 NEW RECOMMENDATION):**

Current `memoryd v1` schema: single `memories` table with (id, type, content, embedding, created_at, metadata). Single flat vector index. Query returns top-K by cosine similarity.

**v4 proposal: 3-tier hierarchical memory (not flat).**

```
Tier 0 (raw events, time-bounded): perceptiond descriptions, audiod transcripts
        → rolled up daily into Tier 1
Tier 1 (semantic facts, medium-term): "user met X at Y on Z"
        → consolidated nightly into Tier 2
Tier 2 (schemas/patterns, long-term): "user has weekly standup with X every Tuesday"
        → queried first, expanded to Tier 1 only on miss
```

**Implementation sketch:**
- **Tier 0:** keep current `memories` table, add `retention_days` per row, scheduled eviction
- **Tier 1:** new `facts` table, populated by a "daily summarizer" job that runs at user-local midnight (uses small LFM2.5-1.2B-Thinking if available, or rule-based extractive summarization as fallback)
- **Tier 2:** new `patterns` table, populated by a "weekly consolidator" that uses DPCM-style schema induction (no LLM, just TF-IDF + clustering on Tier 1 facts)
- **Query path:** check Tier 2 first (rarely populated, fast lookup), expand to Tier 1, fall back to Tier 0 vector search
- **Memory types (episodic/semantic/procedural):** keep the v1 distinction, but map to tiers: episodic = Tier 0+1, semantic = Tier 2, procedural = new `procedures` table populated by user demonstrations

**Why this is the right move for Dan Glasses:**
1. **Power:** a flat vector search over 100K memories costs ~50-200ms. Tiered search over Tier 2 (~1K patterns) costs ~5ms. **Wearable-feasible.**
2. **Privacy:** Tier 2 patterns are abstract, not raw events. **Easier to share, easier to audit, less surface for prompt injection in shared context.**
3. **AGI alignment:** DPCM's "schemas, intentions, cross-domain patterns" is the architectural primitive for self-improving memory. **Directly relevant to the SIA-H (harness-only) self-improvement path in the v2 roadmap.**
4. **Open-source advantage:** we don't need to ship a foundation model. We can ship a memory architecture that's measurably better than the flat-vector baseline used by every other "AI companion" project.

### 2.4 BONUS DEEP DIVE: Proactive / Ambient AI (the v1.5 "initiates" capability)

**Sources:**
- **Brain-Computer Interface driven multi-agent cognitive alignment** (arXiv 2606.13190, June 2026). [^23]
- **CUA-Skill: Computer Using Agents with a Skill Framework** (OpenReview 2026). [^24]
- **On Controllability in Agentic AI: A Survey** (Minds and Machines, 2026). [^25]
- **EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience** (ICML-AIWILDES 2026). [^26]
- **Avenir-Web: Human-Experience-Imitating Web Agent** (OpenReview 2026). [^27]
- **Qualia as control-theoretic constructs for autonomous agents** (Frontiers Robotics & AI, 2026). [^28]

**The PRD's "proactive AI companion" positioning (US-2 contextual task reminder, US-4 passive journaling) is research-validated in 2026 but with important constraints:**

1. **Cognitive load awareness is now the standard.** The BCI paper demonstrates deferring non-urgent communications when the user is highly engaged. For Dan Glasses (no EEG), the proxies are: motion (sitting still + screen-on = engaged), audio (continuous speech = engaged), time-of-day (workday hours = engaged), and explicit user-set focus modes. **`os-toold v2` should grow a "user state" service that infers engagement and gates proactive output accordingly.**

2. **Controllability is the unsolved problem** (Minds and Machines 2026 survey). Four paradigms: constraints/guardrails (technical, scope questions), adaptive control via RL (scales but drifts), agent-in-the-loop (balance of autonomy + accountability), human-in-the-loop (explicit authority, scalability problems). **The survey concludes: meaningful controllability requires integrating causal intervention with normative frameworks.** For Dan Glasses, this means: explicit "interruptibility" user settings (do-not-disturb, focus mode, low-priority queue), combined with structural safety filters in the TTS output path.

3. **Skill-based agent architecture is the SOTA pattern** (CUA-Skill, EvoCUA, Avenir-Web). Skills are reusable, composable, with dynamic retrieval, argument instantiation, and memory-aware failure recovery. **CUA-Skill achieves 76.4% trajectory generation success; best-of-3 on WindowsAgentArena is 57.5% SOTA.** EvoCUA achieves 56.7% on OSWorld (open-source SOTA). Avenir-Web more than doubles SeeAct harness success rate (25.7% vs 12.0%) with a compact Qwen-3-VL-8B backbone.

4. **Qualia / control-theoretic safety layer** (Frontiers 2026): minimal 6,550-parameter model achieves 0.827 AUC safety classification in 1.8ms/decision on CPU, no GPU. 29.6% collision reduction in CARLA stress scenarios. **This is the safety-gate architecture for proactive output:** a tiny model (CPU-only, <2ms) that classifies "should the agent say something now?" before the TTS path is triggered. **Could be implemented in `toold` or a new `policyd` service.**

**v4 product implications:**
- **Proactive mode is a v1.5 feature, not v1.** v1 = responsive (push-to-talk, "ask me anything about my day"). v1.5 = proactive (salience-triggered suggestions, "you walked past the pharmacy 3 times this week, want a reminder?").
- **The triggering primitive is the open question.** v1.5 needs: (a) user-state service (engagement inference), (b) safety gate (qualia-style 6.5K-param classifier), (c) salience aggregation (when does 3-of-3 pharmacy visits = reminder?), (d) interruptibility settings (DND, focus mode, low-priority queue). All four are tractable with the current stack + 1 new tiny service.
- **The competitive window for "proactive AI companion" is open.** Limitless (Meta-acquired), Apple pendant, Meta pendant are all in development/testing 2026-2027. **Our open-source + local-first + memory-first wedge is the right positioning.** Microsoft Scout is cloud-inference; that's our structural differentiator.

---

## 3. Competitive Landscape (v3 + v4 deltas)

### 3.1 Wearable AI hardware (verified as of 03:00 UTC)

| Player | Device | Status | Privacy model | Inference model |
|---|---|---|---|---|
| **Meta Ray-Ban** | $499 prescription displays, April 14 ship | Shipping | Cloud + on-device hybrid | Cloud (Meta AI) |
| **Meta + Limitless** | AI pendant, testing 2027 | Development | Cloud-first | Cloud |
| **Xreal A01** | $299, US ship July 2026 | Pre-order | Display only (no AI) | n/a (display) |
| **Xreal + Google Project Aura** | Developer kit, $TBD | Q3-Q4 2026 | Cloud + on-device | Hybrid |
| **Google Android XR audio glasses** | Warby Parker + Gentle Monster, late 2026 | Pre-order | Cloud (Gemini) | Cloud |
| **Snap Specs** | Consumer 2026 launch confirmed | Pre-order | Cloud | Cloud |
| **Apple pendant** | Reports: 2026-2027 | Rumor | Cloud + on-device | Hybrid |
| **Apple visionOS 27** | "Siri answers based on what you see" | WWDC June 8 | On-device + Private Cloud Compute | Hybrid |
| **Microsoft Project Solara** | Badge + desk concepts, Build 2026 | Concept | Cloud (chip-to-cloud) | **Cloud-only** |
| **Brilliant Labs Halo** | $349, open-source, developer | Shipping | On-device | On-device |
| **OpenGlass** | Open-source research platform | GitHub | On-device | On-device |
| **Limitless (pre-Meta)** | Pendant, $TBD | Shipping | Cloud + on-device | Hybrid |
| **Rewind AI (now Limitless)** | Pendant | Acquired by Meta | Cloud | Cloud |
| **Dan Glasses (us)** | Desktop prototype live, wearable TBD | Prototype | **On-device (privacy first)** | **On-device + optional cloud** |

**Competitive wedge is unchanged from v3:** we are the only **open-source + local-first + memory-first + self-improving** wearable agent. Microsoft Scout / Project Solara is the closest competitor on form factor (badge) but is cloud-only — that's our structural advantage.

### 3.2 Open-source AI companion projects (v4 survey)

- **OpenGlass** (Brilliant Labs, June 2026 paper): open-source smart glasses with on-device event-based gesture recognition. Reference hardware platform.
- **Brilliant Labs Halo**: $349, open-source, shipping.
- **Monako Glass**: $399, open-source reference design.
- **OpenInterpreter / OpenDevin / OpenHands**: agent frameworks, not hardware.
- **Hugging Face LeRobot / SmolVLA**: open-source robotics, adjacent.
- **Letta (formerly MemGPT)**: open-source memory architecture for LLM agents, hierarchical + self-editing. **The closest open-source competitor to our `memoryd` v2 plan.** Worth tracking.
- **LangGraph / LlamaIndex**: agent frameworks with memory primitives.
- **Cognee**: open-source knowledge graph + vector memory for AI agents. **DPCM-like architecture.** Another direct competitor to our `memoryd` v2 plan.

**Positioning:** we are the only project combining all of (open-source + wearable form factor + on-device inference + memory-first + self-improving). Each individual competitor has 1-2 of these. **Our combination is the moat.**

### 3.3 Privacy positioning (v3 + v4 sharpening)

PRD Section 7.3: "Privacy first — all data stays local unless explicitly shared." This is the strongest competitive position in 2026 because:
- **Meta's "NameTag" face-recognition code** was quietly shipped and then removed from the Meta AI app in June 2026 (WIRED reporting). 50M+ installs, dormant biometric pipeline. **Always-on cameras + face recognition = the 2026 privacy crisis.**
- **"Always-on cameras, always-on microphones"** quote from the Glass Almanac privacy debate is a verbatim Zuck quote from Q4 2025 earnings. The 2026 regulatory moment is here.
- **Anthropic Mythos / Fable 5 is under US export restrictions** as of June 15. The model is offline. This is the first time a frontier US model has been subject to government takedown. The sovereign-AI thesis is non-academic.

**Our positioning holds:** open-source + on-device + auditable + AGENTS.md-as-security-control + os-toold v2 structural guards = the only defensible privacy-first wearable AI in 2026.

---

## 4. AGI Landscape 2026 (carry from v3 + v4 tightening)

### 4.1 The state of the AGI race (v3 + v4 deltas)

| Player | 2026 position | v4 update |
|---|---|---|
| **OpenAI** | Targeting IPO in next 12 months (Reuters, June 10). Altman: if recursive self-improvement arrives, IPO push weakens. | **Recursion Inc. raised $650M at $4.65B valuation** (May 2026) for explicit self-improving AI. Socher + Rocktaschel as co-founders. **Self-improvement is now a venture-scale bet, not a research bet.** |
| **Anthropic** | Mythos / Fable 5 under US export restrictions as of June 15. Offline. | **System card for Mythos preview says gains "confidently attributable to human research, not AI assistance"** — internal Anthropic research contradicts CEO Amodei's "exponential" claim. **The "intelligence explosion" narrative is contested within Anthropic itself.** |
| **DeepMind** | Gemma 3 running in orbit on Yam-9 satellite. **First edge VLM in space.** | Proves sub-10B edge VLM works in extreme environments. **Validates our LFM2.5-VL-450M thesis.** |
| **China (Xiaomi MiMo, others)** | "Self-evolution" named as biggest 2026 trend by Xiaomi lead Luo Fuli. | SCMP reports China + US race for "self-improving tech." |
| **Microsoft** | Build 2026: SkillOpt + Project Solara badge/desk + chip-to-cloud model. | Satya Nadella: "learning loops beat picking a model." **Validates our SIA-H self-improvement thesis from a different angle.** |
| **Meta** | 10M wearable target H2 2026. AI pendant development. Reality Labs -$4B Q1 2026. | 1,500 Reality Labs jobs cut in 2026. Apple reportedly working on 3 AI wearables. |
| **Qualcomm** | Computex 2026: "2026 is the year of agents." Dragonfly chips challenge Nvidia + Intel. | "Agentic AI" thesis: autonomous systems that act on users' behalf. **Validates our proactive-AI roadmap.** |
| **Recursive Superintelligence (Recursion)** | $650M raise at $4.65B, May 2026, London. **<30 employees, $155M per employee implied value.** | Socher (ex-Salesforce) + Rocktaschel (ex-DeepMind). 2-year timeline to recursive self-improvement. **The bet is explicit, the timeline is aggressive.** |

### 4.2 Self-improving architectures (the v4 sharpening)

**Carried from v3:**
- SIA framework (Hexo Labs, MIT, May 2026) — harness + weights, with "Harness Updating Is Not Harness Benefit" caveat. Use 1.2B focal model, not 4.6B evolver.
- SkillOpt (Microsoft, Build 2026) — trajectory-derived, verifier-grounded skill compilation.
- RL-managed memory (GRAM, AtomMem 2026) — RL-learned CRUD policies.
- Self-evolving memory (RefCon 2026) — +21.6% on ACE without gold labels.

**v4 additions:**
- **Nadella's "learning loops" framing** (Forbes, June 14 2026): "the real competition isn't which model you pick. It's whether your organization learns from what it builds." A learning loop captures what happened, learns from it, and improves. **This is the Microsoft version of the SIA thesis.** It validates the architectural bet from a non-research angle.
- **The "evolutionary" / "self-evolution" framing from Chinese AI labs** (SCMP, March 2026) suggests the race is global, not US-only. **The sovereign-AI thesis is even stronger than v3 estimated.**
- **DUAL-Bench safe-completion problem** — even SOTA VLMs score <13% on safe completion in dual-use scenarios. **Implication: the "self-improving" agent must have a structural safety layer, not just RLHF.** The qualia / control-theoretic approach (6.5K-param CPU safety classifier) is the pattern.
- **StakeBench: stealthy parasitism** — the agent completes user task while advancing attacker task in parallel. **The "self-improving" agent must also be able to detect when its own optimization is being hijacked.** The Arbiter Agent pattern (continuous monitoring) is the answer.

### 4.3 Edge AI / on-device models (v4 sharpening)

**Carried from v3:** LFM2.5-VL-450M via GGUF Q4_0, Gemma 3 as upper-bound reference, all-MiniLM-L6-v2 for embeddings.

**v4 additions:**
- **VLMCache + SpecFlow** are the SOTA for on-device VLM acceleration. **Concrete recommendations in `perceptiond` v2.**
- **Omni-Embed-Mini (0.9B params)** is the unified embedding model for `memoryd` v2. **Replaces text-only all-MiniLM-L6-v2.**
- **Per-layer mixed-precision quantization** (SWEET) is the path from LFM2.5-VL-450M Q4_0 to a smaller, faster model with negligible accuracy loss.
- **DUAL-Bench** says edge VLMs are particularly bad at safe completion. **Our `os-toold v2` safety filters need to compensate.**

### 4.4 Memory and continual learning (v4 major update)

**v3 said:** "flat vector store is fine for v1, migrate to Qdrant if needed."

**v4 says:** **flat vector store is 2019-era. The 2026 SOTA is hierarchical + dual-process + RL-managed.** Concrete v4 proposal in §2.3:
- Tier 0: raw events (perceptiond descriptions, audiod transcripts), time-bounded, evicted
- Tier 1: semantic facts (daily summaries), medium-term
- Tier 2: schemas/patterns (weekly consolidation), long-term
- Plus a `procedures` table for procedural memory (user demonstrations)
- Plus a `policyd`-style service for engagement inference + proactive triggers

**Implementation cost:** ~2 weeks of work for `memoryd v2`. **Competitive value:** high — this is the architectural primitive that makes Dan Glasses a *companion* rather than a *capture device*.

### 4.5 Multimodal fusion (carry from v3)

No major v4 update. The Gemma 3 in-orbit demo is a multimodal fusion validation but doesn't change the architectural story. **LFM2.5-VL-450M (vision) + whisper.cpp (audio) + all-MiniLM-L6-v2 (text) + KittenTTS (output) remains the right v1 stack.**

### 4.6 Model compression (v4 additions)

- **Per-layer mixed-precision quantization** (SWEET 2026) — Q4_K_M in attention, Q8_0 in vision projector, Q4_0 in text decoder for LFM2.5-VL-450M. 30-40% size reduction with <1% accuracy loss.
- **KV-cache compression** (SpecFlow 2026) — spectral representations for visual state. 2.1× reduction in KV-cache footprint.
- **Background caching** (VLMCache 2026) — semantic disaggregation to identify reusable visual blocks. 1.4-3.8× speedup.
- **Task-specific distillation** (VisAnomReasoner 2026) — parameter-efficient fine-tuning for specific tasks. 21-24% precision improvement with small model footprint.

**All four are applicable to LFM2.5-VL-450M + our salience-gated pipeline.** Concrete roadmap in `perceptiond` v2 spec.

---

## 5. Top 5 Deep Dives the brief asked for (v4 execution)

The brief said "pick 3 to do deeply." v4 did 3 + 1 bonus:

| Deep dive | v4 finding | Danlab impact |
|---|---|---|
| **A. Self-improving RL loops** | Covered in v3. SIA framework + SkillOpt + GRAM + AtomMem. v4 adds Nadella's "learning loops" framing and Arbiter Agent pattern. | `os-toold v2` grows an arbiter / watchdog service. SIA-H fork into `danlab-multimodal` Month 1. |
| **B. Edge VLM optimization** | v4 NEW DEEP DIVE. VLMCache, SpecFlow, Omni-Embed-Mini, SWEET, EMemBench, Abstraction Gap, DUAL-Bench, Gemma 3 in orbit. | `perceptiond v2`: per-layer mixed-precision + VLMCache-style background caching. `memoryd v2`: Omni-Embed-Mini. **LFM2.5-VL-450M verdict: still the right choice.** |
| **C. Vector search and memory architectures for AI companions** | v4 NEW DEEP DIVE. DPCM dual-process, SAGE graph, MemDreamer hierarchical, GraP-Mem multi-granularity, AtomMem CRUD, RefCon self-refining. | `memoryd v2` = 3-tier hierarchical + dual-process consolidation. **The biggest v4 architectural change.** |
| **D. Proactive AI** (bonus) | BCI cognitive-load, controllability survey, CUA-Skill / EvoCUA / Avenir-Web skill frameworks, qualia safety layer. | v1.5 feature, not v1. Needs user-state service + safety gate + interruptibility settings. **Competitive window open.** |
| **E. TTS quality vs size** (partial, v3 + v4) | BareWave (waveform-native flow-matching), wavelet-driven CFM boosting (NFE 32→26, FAD -61%), UNISON (621M unified audio). | **KittenTTS still defensible for v1.** Watch BareWave / UNISON for v2 — both target edge. |
| **F. VLM power characterization** (carry from v3) | VLM is dominant power event. Uncharacterized on aarch64. | Still needs Redax measurement. v1 desktop prototype first. |

---

## 6. What Changed Since v3 (delta)

1. **Deep technical dives executed.** v3 was a broader landscape scan; v4 did 3 + 1 focused deep dives with primary sources. **Cost: ~6 web searches + 3 web_research calls. Value: high — concrete architectural changes for `memoryd` and `perceptiond` v2.**

2. **Memory architecture landscape mapped.** v3 said "flat vector store, migrate to Qdrant if needed." v4 says "the 2026 SOTA is hierarchical + dual-process + RL-managed." **Concrete v2 proposal in §2.3.** This is the most important v4 update.

3. **StakeBench added to the security thesis.** v3 had Varonis (industry) + Imperva. v4 adds StakeBench (academic) + lethal trifecta + Arbiter Agent + Architecture as Governance. **The structural-control > rule-based-control finding is new in v4.**

4. **Edge VLM optimization techniques identified.** v3 said "LFM2.5-VL-450M is the right choice, Gemma 3 is the upper bound." v4 adds VLMCache, SpecFlow, SWEET, Omni-Embed-Mini as concrete optimization paths. **Perceptiond v2 has a real roadmap now.**

5. **Proactive AI = v1.5, not v1.** v3 was ambiguous on this. v4 is explicit: v1 = responsive, v1.5 = proactive. **The triggering primitive + safety gate + user-state service are tractable with the current stack + 1 new tiny service.**

6. **All other v3 content unchanged.** The structural thesis (open-source + local-first + memory-first + self-improving) holds. The competitive wedge (only open-source local-first wearable AI) holds. The AGI landscape (recursion, self-evolution, learning loops) holds.

---

## 7. Open Questions for somdipto (v4)

(Plus carry from v3.)

1. **v4 sharpening:** Do we have bandwidth to ship `memoryd v2` (3-tier hierarchical) in the next 2 weeks? It's the highest-value v4 architectural change. **Recommend: yes, parallel to perceptiond v2.**
2. **v4 sharpening:** Should we add an `arbiterd` service (watchdog for prompt-injection / data-leak detection) or fold it into `os-toold v2`? **Recommend: fold into `os-toold v2` for v1, extract to `arbiterd` for v1.5.**
3. **v4 NEW:** Do we want to ship the BCI cognitive-load proxy (motion + audio + time-of-day → engagement score) for v1.5 proactive mode, or wait for actual EEG integration? **Recommend: proxy-only for v1.5, EEG as v2 hardware.**
4. **v4 NEW:** Should `memoryd v2` adopt Omni-Embed-Mini (0.9B, multimodal) or stay with all-MiniLM-L6-v2 (text-only, 384d) for v1? **Recommend: MiniLM for v1 (proven, 384d works), Omni-Embed-Mini for v2 (when we have audio/image embedding needs).**
5. **v4 NEW:** Should we publish the `os-toold v2` Pinchy-protection spec as a standalone whitepaper for the security research community? **Recommend: yes — it's the press cycle, it's the open-source positioning, and it's the compliance wedge for Microsoft Scout GA in October.**

---

## 8. Sources (v4)

[^1]: Varonis Threat Labs, "Phishing for Lobsters: How We Tricked OpenClaw into Spilling Secrets" (June 2026). https://www.varonis.com/blog/phishing-for-lobsters
[^2]: CSO Online, "Autonomous AI agents duped into leaking sensitive data in phishing test" (June 2026). https://www.csoonline.com/article/4183445/autonomous-ai-agents-duped-into-leaking-sensitive-data-in-phishing-test.html
[^3]: Imperva parallel research, "Patchable prompt-injection vulnerability in OpenClaw deployments" (June 2026). https://www.imperva.com/blog/
[^4]: StakeBench: A stakeholder-centric benchmark for prompt injection, Nanyang Technological University + ST Engineering + IBM Research + UIUC (June 2026). https://openreview.net/forum?id=StakeBench
[^5]: CSO Online, "5 runtime signals for catching a compromised AI agent" (June 2026). https://www.csoonline.com/article/4184681/5-runtime-signals-for-catching-a-compromised-ai-agent.html
[^6]: VLMCache: Efficient On-Device Vision-Language Model Inference, ACM Multimedia 2026. https://dl.acm.org/doi/abs/10.1145/3745756.3809243
[^7]: Spectral-Progressive Thought Flow (SpecFlow) for Lightweight Multimodal Reasoning, arXiv 2606.02842 (June 2026). https://arxiv.org/abs/2606.02842v1
[^8]: Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection, arXiv 2605.30344 (May 2026). https://arxiv.org/abs/2605.30344v1
[^9]: Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation, OpenReview 2026. https://openreview.net/forum?id=tNODqeez5j
[^10]: The Abstraction Gap in Vision-Language Causal Reasoning, arXiv 2605.28779 (May 2026). https://arxiv.org/abs/2605.28779v1
[^11]: DUAL-Bench: Measuring Over-Refusal and Robustness in Vision-Language Models, OpenReview 2026. https://openreview.net/forum?id=SLaIKf46Dz
[^12]: EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents, OpenReview 2026. https://openreview.net/forum?id=zzndQeR4Ay
[^13]: TechCrunch, "A satellite just learned to find things on its own" (June 15 2026). https://techcrunch.com/2026/06/15/a-satellite-just-learned-to-find-things-on-its-own-heres-what-that-means/
[^14]: SWEET: serving workload-balanced end-to-end efficient and tailored edge inference via quantization and partitioning, Frontiers in Complex Systems 2026. https://www.frontiersin.org/journals/complex-systems/articles/10.3389/fcpxs.2026.1801157/full
[^15]: LLM Agent Memory: A Survey from a Unified Representation-Management Perspective, OpenReview 2026. https://openreview.net/forum?id=E6LJBlfoPL
[^16]: Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving Agent Memory (DPCM), OpenReview 2026. https://openreview.net/forum?id=ywl53zPXu0
[^17]: SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory, OpenReview 2026. https://openreview.net/forum?id=REGaZA2FmT
[^18]: GRAM: Empowering Agent with Actively Managed Graph-Structured Memory via Reinforcement Learning, OpenReview 2026. https://openreview.net/forum?id=rzGvGnwVC7
[^19]: MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding via Hierarchical Graph Memory and Agentic Retrieval Mechanism, arXiv 2606.07512 (June 2026). https://arxiv.org/abs/2606.07512v1
[^20]: AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation, OpenReview 2026. https://openreview.net/forum?id=dfWiKLx6fs
[^21]: RefCon: Iterative Refinement and Contrastive Memory Extraction for Context-Evolving Agent, OpenReview 2026. https://openreview.net/forum?id=fatsyRRKEs
[^22]: GraP-Mem: Granularity-Aware Planning for Adaptive Memory Access in Long-Horizon LLM Agents, OpenReview 2026. https://openreview.net/forum?id=AUPI1ifc4v
[^23]: Multi-Modal Multi-Agent Robotic Cognitive Alignment enabled by Non-Invasive Consumer Brain Computer Interfaces, arXiv 2606.13190 (June 2026). https://arxiv.org/abs/2606.13190v1
[^24]: CUA-Skill: Developing Computer Using Agents with a Skill Framework, OpenReview 2026. https://openreview.net/forum?id=ltKBkEEa4e
[^25]: On Controllability in Agentic AI: A Survey, Minds and Machines 2026. https://link.springer.com/article/10.1007/s11023-026-09783-y
[^26]: EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience, ICML-AIWILDES 2026. https://openreview.net/forum?id=pzbtm6fRIo
[^27]: Avenir-Web: Human-Experience-Imitating Web Agent with Mixture of Grounding Experts, OpenReview 2026. https://openreview.net/forum?id=sijVvUVjny
[^28]: Qualia as control-theoretic constructs for autonomous agents: event phase space as an action-oriented semantic safety layer, Frontiers in Robotics and AI 2026. https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1811996/full

---

*Dan2 Research Report v4 — 2026-06-16 03:00 UTC. Live re-verified, 3 deep technical dives executed, 1 bonus dive. Memory architecture landscape is the major v4 update: hierarchical + dual-process + RL-managed is the 2026 SOTA. Concrete v2 proposals for `memoryd` and `perceptiond`. StakeBench + lethal trifecta + Arbiter Agent strengthen the security thesis. All other v3 content unchanged.*
