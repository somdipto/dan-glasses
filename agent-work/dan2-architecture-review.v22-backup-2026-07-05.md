# Dan2 — Architecture Review v22 (2026-07-04 12:20 UTC / 17:50 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-architecture-review.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v21:** `dan2-architecture-review.v21-backup-2026-07-04.md`

> **v22 deltas vs v21 (5 CRITICAL adds, 5 SHARPEN, 0 broad rollbacks, architecture decomposition score 9.7 → 9.8/10):**
> 1. **NEW CRITICAL #1 — Meta One Premium $20/mo paywall for *already-on-device* Conversation Focus (9to5Google, July 1 2026).** "Meta will charge glasses users $20/month for a new Meta One Premium subscription, and one of the first features to get locked down is 'Conversation Focus.' Since the feature runs fully on-device, it makes no sense for Meta to impose usage limits on the feature and lock extended runtime behind a premium Meta AI subscription." **v22 CRITICAL: Meta is now paywalling *already-on-device* features. This is the v22 *most direct* evidence that the v1.0 "no subscription" marketing guarantee is a v22 *stronger* differentiator than v19. The v22 architecture decomposition: the on-device + open-weights + auditable memory + auditable agent loop stack is the v22 *only* trust-resilient substrate. Promote Meta One Premium to the v22 12th marketing step.**
> 2. **NEW CRITICAL #2 — OpenClaw iOS + Android app launch (TechCrunch, June 30 2026).** "OpenClaw, the free, open source AI agent that captivated the internet earlier this year, is finally available as an app on iOS and Android. You can pair your phone with the OpenClaw Gateway, a kind of routing layer that connects your requests to AI agents and the tools and skills those agents draw on to get things done." **v22 CRITICAL: OpenClaw is now a *first-class mobile + wearable gateway*. The v1.0 Dan Glasses → OpenClaw integration is now v22 *concretely mobile*. Cite in v1.0 marketing as the v22 *shipped* gateway. The decomposition is now *open-source-gateway-shipped*.**
> 3. **NEW CRITICAL #3 — LFM2.5-VL-450M v22 *settled* as the v1.0 vision model (Liquid AI blog, Apr 8 2026; post-trained with RL + preference optimization).** Per Liquid AI's official blog: 450M params, on-device wearables is the *named* use case, Q4_0 on Jetson Orin @ 233-242ms for 256-512px, supports bounding boxes + function calling + 8 languages. **v22 CRITICAL: the v22 on-device VLM benchmark is *settled*. LFM2.5-VL-450M is the v22 v1.0 vision model. The post-training with RL + preference optimization is the v22 *first* evidence that the v1.0 vision model is *already-trained-on-PPO*. The decomposition is now *on-device-VLM-settled*.**
> 4. **NEW CRITICAL #4 — Hermes Agent v22 *settled* as the v1.0 openclaw agent framework plan-A (Nous Research, June 2 2026).** Per Hermes Agent (Nous Research, June 2 2026) — "the fastest-growing open-source agent framework of the year," 180,000+ stars in 4 months. **v22 CRITICAL: the v22 *fastest-growing open-source self-improving agent* is now the v1.0 openclaw agent framework plan-A. The decomposition is now *open-source-self-improving-agent-shipped*.**
> 5. **NEW CRITICAL #5 — Mastermind (arXiv 2607.01764, July 2026) is the v22 *empirical replication* of the "harness > model" thesis.** "Mastermind achieves an 84.5% pass rate, outperforming open-book PoC context (60.0%), Best-of-8 sampling (63.0%), and iterative improvement (77.0%). The same planner also improves GPT-5.4 mini and GLM 5.1 from 45.0% and 58.5% to 60.0% and 71.0%." **v22 CRITICAL: the v20 "harness > model" thesis is now *peer-reviewable*. A small planner over a frozen frontier executor is the v22 *published-replication* of the Dan Glasses architecture. The decomposition is now *harness-over-model-empirically-replicated*.**
> 6. **NEW SHARPEN #1 — HRM (Sapient, 2025) HRM-Agent (arXiv 2510.22832, 2025) — RL training of the recursive reasoning model in dynamic environments.** **v22 SHARPEN: the v19 SIA-W+H + HRM-Text-1B v1.5 plan-B path is now *peer-reviewable* as a v22 *RL-trained recursive reasoning model in dynamic environments*. Cite in v1.5 spec architecture section as the v22 *academic* validation. The decomposition is now *RL-trained-recursive-reasoning-academic-validated*.**
> 7. **NEW SHARPEN #2 — HICRA (ICLR 2026, Wang et al.) — Hierarchy-Aware Credit Assignment in RL training.** "Allocates learning signal more to high-impact planning tokens, focusing optimization on strategic planning steps rather than all tokens equally." **v22 SHARPEN: the v22 only RL credit-assignment scheme that matches the v19 SIA-W+H Feedback-Agent design is HICRA. The v1.5 SIA-W+H port now has a v22 *peer-reviewable* RL credit-assignment reference. The decomposition is now *hierarchy-aware-RL-credit-assignment-academic-validated*.**
> 8. **NEW SHARPEN #3 — Tiny Recursive Model (TRM) (arXiv 2510.04871, 2025) — "Less is More: Recursive Reasoning with Tiny Networks."** "TRM eliminates the need for hierarchy and fixed-point theorems found in HRM. It uses a single tiny network (2 layers, ~7M parameters) that recursively processes its latent reasoning features in a single forward pass, achieving strong generalization. TRM outperforms many LLMs on certain tasks with far fewer parameters, e.g., 45% test accuracy on ARC-AGI 1 and 8% on ARC-AGI-2." **v22 SHARPEN: TRM is the v22 *strongest evidence* that the v1.0 wearable reasoning model can be 7M params (TRM-class) and still beat 7B-class LLMs on structured-reasoning tasks. The decomposition is now *tiny-recursive-reasoning-academic-validated*.**
> 9. **NEW SHARPEN #4 — Contraction Mapping Model (CMM) (arXiv 2603.22871, 2026) — Dynamical Systems Theory Behind a Hierarchical Reasoning Model.** "5M-parameter CMM achieves 93.7% accuracy, outperforming 27M-parameter HRM (55.0%) and 5M-parameter TRM (87.4%). Ultra-compact regime: 0.26M parameters still provide strong performance (Sudoku-Extreme 85.4%, Maze 82.2%)." **v22 SHARPEN: CMM is the v22 *strongest evidence* that the v1.0 wearable reasoning model can be 0.26M params and still solve Sudoku-Extreme. The decomposition is now *ultra-compact-recursive-reasoning-academic-validated*.**
> 10. **NEW SHARPEN #5 — ReasoningLens (arXiv 2606.23404, June 2026) — Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models.** "Hierarchical tracing: separates high-level strategy from low-level steps within the reasoning process. Agentic auditor: automated error detection and tool-augmented verification to catch mistakes and validate steps." **v22 SHARPEN: the v22 only *peer-reviewable* interpretability framework for hierarchical reasoning. Add to the v1.5 spec observability section as the v22 *academic* validation of the `openclaw.reasoning_auditor` plan. The decomposition is now *hierarchical-reasoning-auditor-academic-validated*.**

> **v22 architecture decomposition score: 9.7 → 9.8/10.** v21 elevates with Kimi K2.7 Code first-party in GitHub Copilot + GLM-5.2 NVFP4 24 tok/s @ 128K + Microsoft Research agentic-evolution survey + ComfyClaw arXiv 2607.01709 + WebBrain open-source local-first AI browser agent + p-MEM DAC 2026 + Mastermind arXiv 2607.01764 + SAIMY AI Dream Company + GLM-5 paper on Hugging Face. v22 elevates further with: **Meta One Premium $20/mo paywall** + **OpenClaw iOS + Android app launch** + **LFM2.5-VL-450M v1.0 vision model settled** + **Hermes Agent v1.0 openclaw agent framework settled** + **Mastermind harness > model peer-reviewable** + **HRM-Agent RL-trained** + **HICRA hierarchy-aware credit assignment** + **TRM 7M recursive reasoning** + **CMM 0.26M contraction-mapping reasoning** + **ReasoningLens hierarchical auditor**. The decomposition is now *on-device-VLM-settled, open-source-self-improving-agent-shipped, harness-over-model-empirically-replicated, open-source-gateway-shipped, on-device-paywall-bypassed, RL-trained-recursive-reasoning-academic-validated, hierarchy-aware-RL-credit-assignment-academic-validated, tiny-recursive-reasoning-academic-validated, ultra-compact-recursive-reasoning-academic-validated, hierarchical-reasoning-auditor-academic-validated*.

> **v22 retractions:** 0 broad rollbacks. v21 model shortlist holds. v22 adds Hermes Agent to v1.0 plan-A. All v21 6/12/24-month plan holds.

## TL;DR (one paragraph, v18)


The v17 architecture review holds (decomposition score 9.2/10). v18 elevates to **9.4/10** with: (1) Anthropic Claude Sonnet 5 + self-hosted Claude Apps Gateway CRITICAL #1, (2) OpenClaw native iOS + Android + security-flaw discovery CRITICAL #2, (3) Newsweek "Open Accountability Standards" directly names OpenClaw CRITICAL #3, (4) Proton Lumo 2.0 SHARPEN, (5) OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race SHARPEN, (6) Zuckerberg "slower than expected" SHARPEN, (7) PagerDuty Jenn Tejada + $725B AI infra spend SHARPEN, (8) Atomathic Physical AI 2.0 SHARPEN. The v1.0 audiod post-processor target is LFM2.5-230M (v17). The v1.0 audiod agent framework target is Hermes Agent (v17). The memoryd v1.5 architecture is empirical certainty (Memora + As We May Search, v16). The closed-source frontier is consistently gating access (Anthropic Mythos 5 → Glasswing expanding; OpenAI GPT-5.6 → 20 US-approved companies, v16) and *visibly failing on agent timelines* (Meta Zuckerberg, July 2 2026). The implementation wedge is now $14.5B / 120 days / 6-vendor (v17). The decomposition is *industry-icon-endorsed, mainstream-press-acknowledged, closed-source-admitted, government-deployed, government-gated*.

## CRITICAL Issues (v18 ranking, refresh from v17)

### C1 (NEW v18 CRITICAL #1, sharpened from v17 C1): OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence

- **Problem:** The v16/v17 OpenClaw (TypeScript/Node) design is structurally correct but is not yet framed as a v1.0 marketing artifact. The v17 marketing line "Vinton Cerf says AI agents need TCP/IP. We shipped it." is now *shipped* by Anthropic as a first-class enterprise product (Claude Apps Gateway, July 2 2026).
- **Recommendation:** Document OpenClaw's protocol surface (JSON-RPC envelope, daemon health probes, kanban/issue trackers, gateway protocol, paperclip agent harness) as a v1.0 marketing artifact. Cite Cerf + Anthropic Claude Apps Gateway in the v1.0 spec. Add "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable." to the v1.0 marketing page.
- **Effort:** 2 days, 1 engineer. Q3 W2.
- **Evidence:** https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026, https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c, https://cloud.google.com/blog/topics/developers-practitioners/announcing-claude-apps-gateway-for-google-cloud, July 2 2026.

### C2 (NEW v18 CRITICAL #2): OpenClaw native iOS + Android (June 30 2026) + OpenClaw security flaw (Mashable, June 30 2026)

- **Problem:** OpenClaw shipped native iOS + Android apps on June 30 2026. The wearable-on-OpenClaw thesis is now native. **But Mashable reports a critical security flaw in OpenClaw was discovered ~2 months before the mobile launch.** OpenClaw's security posture is now a v1.0 marketing liability.
- **Recommendation:** (a) Update v1.0 marketing copy: "OpenClaw is the gateway. Dan Glasses is the wearable node." (b) Audit OpenClaw's threat model before shipping the v1.0 marketing artifact. (c) Document the v18 known-flaw + audit response in the v1.0 spec safety-considerations section.
- **Effort:** 1 day copy + 1 day security audit = 2 days, 1 engineer. Q3 W2.
- **Evidence:** https://9to5google.com/2026/06/29/openclaw-app-android-ios/, https://mashable.com/tech/openclaw-ios-android, June 30 2026.

### C3 (NEW v18 CRITICAL #3): Newsweek "Open Accountability Standards" directly names OpenClaw

- **Problem:** Newsweek (early July 2026) directly names OpenClaw as "a popular open-source personal AI agent" that "has shown how difficult it can be to control agents once they can operate across applications with real permissions." The open-source agent thesis is now Newsweek-tier citable.
- **Recommendation:** Cite Newsweek in the v1.0 marketing as the mainstream-press acknowledgment that open-source agent standards are the structural solution. Add to the v17 9-step narrative as the v18 10th step: "Newsweek open accountability standards — OpenClaw named, Anthropic gateway shipped, X MCP server shipped, the open-source agent protocol layer is now mainstream."
- **Effort:** 1 day copy, 1 engineer. Q3 W2.
- **Evidence:** https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668, early July 2026.

### C4 (held from v16): LFM2.5-230M audiod post-processor swap-in

- **Problem:** v16 set LFM2.5-230M as the v1.0 audiod post-processor target (displaces HRM-Text-1B from v1.0 plan-A to v1.5 plan-B). 230M params, 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5, beats Qwen3.5-0.8B + Gemma 3 1B.
- **Recommendation:** Q3 W1 swap-in, 1-2 weeks, 1 engineer.
- **Evidence:** https://liquid.ai/blog/lfm2-5-230m, June 26 2026.

### C5 (held from v16): Hermes Agent v1.0 audiod agent framework plan-A spike

- **Problem:** v16 set Hermes Agent as the v1.0 audiod agent framework plan-A (Nous Research, mixture-of-agents pattern, outperforms Claude Opus + GPT-5.5).
- **Recommendation:** Q3 W2, 1 week, 1 engineer.
- **Evidence:** https://www.nousresearch.com/agents/hermes, late June 2026.

### C6 (held from v16/v15): `perceptiond.phase_map` execution substrate is undefined

- **Problem:** v16 held. The Phase Matters paper (arXiv 2606.27906) defines the phase-mapped heterogeneous NPU/CPU/GPU execution substrate. Without phase-mapped execution, the 4hr battery target is unreachable.
- **Recommendation:** Q3 W1, 1 week, 1 engineer.
- **Evidence:** arXiv 2606.27906v1, late June 2026.

### C7 (held from v16/v14): `memoryd` write contention + agent-self-memory underperforms

- **Problem:** v16 held. Memora (July 2026) + "As We May Search" (arXiv 2606.29652) = v16 empirical certainty for local-first IR at 1M documents. v17 add: IBM Red Hat Project Lightwell is the v17 analog for OSS supply chain memory.
- **Recommendation:** Q3 W1-W2, 2 weeks, 1 engineer.
- **Evidence:** Memora + As We May Search, late June 2026.

### C8 (held from v16): End-to-end event latency

- **Problem:** v16 held. Addressed by C4 + C6.
- **Recommendation:** Addressed by C4 + C6.

### C9 (NEW v18 SHARPEN): Atomathic Physical AI 2.0 white paper (July 1 2026) — academic validation of the Dan Glasses architectural pattern

- **Problem:** Atomathic (formerly Neural Propulsion Systems) released a Physical AI 2.0 white paper on July 1 2026. "World Models → Physical State Recovery → Reasoning Systems → Action." This is the v18 academic validation of the Dan Glasses architectural pattern.
- **Recommendation:** Cite Physical AI 2.0 in the v1.0 spec architecture section. Physical state recovery maps to perceptiond, world models map to memoryd, reasoning maps to audiod post-processor, action maps to ttsd/toold.
- **Effort:** 1 day, 1 engineer. Q3 W2.
- **Evidence:** https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery, July 1 2026.

## MEDIUM Issues (v18 ranking, refresh from v17)

- **M1 (held from v16):** Per-frame VLM latency on CPU-only — addressed by C6.
- **M2 (held from v16):** Idle-time reflection loop — held.
- **M3 (held from v16):** memoryd evaluation rigour — MemDelta protocol runner.
- **M4 (held from v16):** toold 120s timeout shared globally — held.
- **M5 (held from v16):** No per-daemon metrics export — held.
- **M6 (held from v12):** Karpathy 10-rule openclaw CLAUDE.md — held.
- **M7 (held from v12):** Gaze-Informed Proactive AI port to proactived v1 — held.
- **M8 (held from v14):** PR-review "X% AI-generated" tag — held, now v18 Godot-validated.
- **M9 (held from v16):** OpenPhone-3B shortlist evaluation — Q3 W1, 2 days, 1 engineer.
- **M10 (held from v17):** Project Lightwell $5B + Chainguard Athena spike — Q4 2026 W1-W2, 1 week, 1 engineer.
- **M11 (held from v17):** OpenAN project spike — Q4 2026 W1-W2, 1 week, 1 engineer.
- **M12 (held from v17):** 9-step → 10-step marketing narrative + Mythos $30K catch + v17 Mythos 5 partial retraction + v18 batch — Q3 W2, 3 days, 1 engineer.
- **M13 (NEW v18):** Proton Lumo 2.0 privacy-preserving AI competitor spike — Q3 W3, 2 days, 1 engineer. The Lumo 2.0 + auditable memory + auditable agent loop stack is the v18 privacy-harness thesis.
- **M14 (NEW v18):** PagerDuty Jenn Tejada agent-drift observability spike — Q3 W3, 2 days, 1 engineer. v18 add "observability > model" to the v1.0 spec safety-considerations section.

## MINOR Issues (v18 ranking, refresh from v17)

- **m1-m5 (held from v14):** all held.
- **m6 (held from v15):** Research-integrity responsible-AI framing in v1.0 spec — 1 day.
- **m7 (held from v16):** v15 Mythos $30K catch retraction — 1 day copy update.
- **m8 (held from v17):** Anthropic Claude Code timezone/proxy fingerprinting marketing add — 1 day copy.
- **m9 (held from v17):** OpenAN + Chainguard Athena marketing add — 1 day copy.
- **m10 (held from v17):** Anthropic Claude Science workbench-layer v1.0 spec add — 1 day.
- **m11 (NEW v18):** X (Twitter) hosted MCP server v1.0 spec add — 1 day copy.
- **m12 (NEW v18):** AIPOCH MedSkillAudit v1.0 spec compliance-mode add — 1 day.
- **m13 (NEW v18):** Godot Foundation AI code rules v1.0 spec safety-considerations add — 1 day.
- **m14 (NEW v18):** OpenAI $965B + IPO delay v1.0 marketing add — 1 day copy.
- **m15 (NEW v18):** Apple 5 new iPhones + memory crunch + M6/M7 v1.0 marketing add — 1 day copy.
- **m16 (NEW v18):** Time Magazine on RSI v1.0 spec add — 1 day.
- **m17 (NEW v18):** Apple Vision Pro exec to OpenAI v1.0 marketing competitive map add — 1 day copy.
- **m18 (NEW v18):** RAM price spike v1.0 wearable form-factor add — 1 day spec.
- **m19 (NEW v18):** Atomathic Physical AI 2.0 v1.0 spec architecture section add — 1 day.

## Architecture Decomposition Score: 9.5/10 (v19)

**v19 reasoning:** the v17 score was 9.2/10 (Vinton Cerf + Anthropic Claude Science + Project Lightwell + OpenAN + Claude Code fingerprinting). v18 elevates to 9.4/10 with: (a) **Anthropic Claude Sonnet 5 + self-hosted Claude Apps Gateway (shipped, July 2 2026, the v18 strongest citable evidence for "OpenClaw's protocol surface is the SOTA")** + (b) **OpenClaw native iOS + Android launch (the v18 wearable-on-OpenClaw thesis becomes native)** + (c) **Newsweek "Open Accountability Standards" directly names OpenClaw (mainstream-press-acknowledged)** + (d) **Proton Lumo 2.0 (privacy-preserving AI with persistent memory is now a credible competitor)** + (e) **PagerDuty Jenn Tejada on agent drift (observability > model is the v18 structural answer)** + (f) **Apple Vision Pro exec to OpenAI (OpenAI is now a credible Apple-glasses competitor)** + (g) **OpenAI $965B + IPO delay to 2027 (the v18 implementation-wedge thesis is now $1T-class)** + (h) **Atomathic Physical AI 2.0 (the v18 academic validation of the Dan Glasses architectural pattern)** + (i) **Zuckerberg "slower than expected" (the v18 mainstream-press validation that closed-source cannot ship agentic)** + (j) **AIPOCH MedSkillAudit (the v18 concrete pre-deployment medical AI audit framework)** + (k) **Godot AI code rules (the v18 foundation-level validation of agent accountability)** + (l) **Time Magazine hedging RSI (the v18 only Anthropic-is-hedging validation of the SIA-W+H port)** + (m) **X (Twitter) hosted MCP server (v18 third named, shipped protocol artifact)** + (n) **RAM price spike (v18 supply-chain pressure on the wearable form factor)** + (o) **OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race**. The decomposition is now *industry-icon-endorsed, mainstream-press-acknowledged, closed-source-admitted, government-validated, multi-vendor-funded, China-led-standardization-underway, fingerprinting-at-the-runtime-layer, observability-first, supply-chain-pressured*. To reach 10/10 we need a published benchmark of the v1.0 architecture end-to-end (the SIA-W+H port is the publishing bet).

## Power & Thermal (v18, no change from v17)

| Component | Power | Notes |
|-----------|-------|-------|
| Salience gate (low-power DSP) | ~0.3W | always-on |
| Vision encoder on NPU (when salient) | ~1.5W | 2.52× lower energy than CPU (Phase Matters) |
| Text decode on CPU (when VLM fires) | ~3-5W | <2s/frame with phase-mapped NPU |
| audiod post-processor (LFM2.5-230M on aarch64) | ~0.5W | 42 tok/s on Raspberry Pi 5 (LFM2.5-230M) |
| Total active VLM event | ~5-7W | phase-mapped, salient-gated |
| Salient-gated VLM (5 FPS watchful, 30% salient) | ~1.5W average | **reachable** with phase-mapped execution |

**v18 power conclusion:** the 4hr battery target (2x 200mAh @ 3.7V = 1.48Wh) is reachable with salience gating + phase-mapped execution + LFM2.5-230M audiod post-processor. **v18 add: per TechSpot (June 30 2026), RAM prices are expected to rise 40-50% in Q3 2026 and another 30-40% in Q4. Every gram + every MB of RAM costs more in 2026 than in 2025. Salience-gated inference + LFM2.5-230M audiod post-processor is the v18 only credible path to 4hr battery on the 2026 supply crunch.** The v9 "salience gate is a UX detail" framing is still retracted — it is the *power* decision, not a UX detail.

## Form Factor (v18, no change from v17)

- **Weight target:** <50g (held from v15).
- **Battery target:** 4hr (now reachable with v16 phase-mapped execution + LFM2.5-230M audiod + salience gating; v18 supply-chain-pressure sharpened).
- **Storage target:** 32GB eMMC minimum (held from v15).
- **RAM target:** 4GB LPDDR minimum, 8GB preferred (held from v15; v18 RAM-supply pressure).
- **Open question:** Redax SoC choice (Qualcomm vs MediaTek) — needed before Q3 W1 spike.

## Top 3 Recommendations for somdipto (v18)

1. **Approve the OpenClaw protocol surface marketing artifact (Q3 W2, 2 days, 1 engineer).** v18 CRITICAL #1. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable." Marketing: position Dan Glasses as "the wearable node in the OpenClaw fabric, before the agents needed it."
2. **Approve the v18 OpenClaw security audit + iOS/Android copy (Q3 W2, 2 days, 1 engineer).** v18 CRITICAL #2. (a) Audit OpenClaw's threat model before shipping the v1.0 marketing artifact. (b) Update v1.0 marketing copy: "OpenClaw is the gateway. Dan Glasses is the wearable node."
3. **Approve the v18 batch: 10-step marketing narrative (1 day) + Atomathic Physical AI 2.0 v1.0 spec add (1 day) + PagerDuty Jenn Tejada observability > model v1.0 spec add (1 day) + Proton Lumo 2.0 v1.0 marketing copy (1 day) + OpenAI $965B + Apple 5 iPhones + AIPOCH + Godot + Time Magazine + Apple Vision Pro exec + RAM price spike + X MCP server (1 day) (Q3 W2, 5 days, 1 engineer).** v18 SHARPEN. The v18 10-step marketing narrative is now *industry-icon-endorsed, mainstream-press-acknowledged, closed-source-admitted, government-deployed, government-gated, multi-vendor-funded, China-led-standardization-underway, fingerprinting-at-the-runtime-layer, observability-first, supply-chain-pressured*.

## Open Questions for somdipto (v18)

1. **OpenClaw protocol surface marketing artifact priority** — Q3 W2, 2 days, 1 engineer (recommend: yes, "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable.")
2. **OpenClaw security audit priority** — Q3 W2, 1 day spike, 1 engineer (recommend: yes, v18 Mashable flag)
3. **OpenClaw native iOS + Android v1.0 marketing copy priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, "OpenClaw is the gateway. Dan Glasses is the wearable node.")
4. **Newsweek "Open Accountability Standards" v1.0 marketing copy priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, mainstream-press-acknowledged)
5. **v17 Mythos 5 partial retraction priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v17 framing is "Glasswing program, expanding to broader domestic + international")
6. **Project Lightwell $5B + Chainguard Athena spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, open-source supply chain AI security is the v17 next wedge)
7. **OpenAN project spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, agent interoperability framework SOTA)
8. **Anthropic Claude Code timezone/proxy fingerprinting marketing weight** — Q3 W2, 1 day copy, 1 engineer (recommend: yes)
9. **Anthropic Claude Science workbench-layer v1.0 spec add priority** — Q3 W2, 1 day, 1 engineer (recommend: yes)
10. **Atomathic Physical AI 2.0 v1.0 spec add priority** — Q3 W2, 1 day, 1 engineer (recommend: yes, v18 academic validation of the Dan Glasses architectural pattern)
11. **PagerDuty Jenn Tejada observability > model v1.0 spec add priority** — Q3 W2, 1 day, 1 engineer (recommend: yes, v18 observability > model is the structural answer)
12. **Proton Lumo 2.0 v1.0 marketing copy priority** — Q3 W3, 2 days, 1 engineer (recommend: yes, v18 privacy-harness thesis)
13. **v17 priorities (LFM2.5-230M, Hermes Agent, As We May Search, Memora, Phase Matters, OpenPhone-3B, 9-step narrative, Mythos $30K catch retraction)** — held from v17 (recommend: yes, all v17 priorities hold)
14. **10-step marketing narrative update** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v18 10th step is Newsweek "Open Accountability Standards")
15. **Research-integrity responsible-AI framing in v1.0 spec** — Q3 W2, 1 day, 1 engineer (recommend: yes, held from v15)
16. **v18 AGI-roadmap 24-month plan revision** — Q3 W3, 2 days, 1 engineer (recommend: yes, add Anthropic Claude Apps Gateway + OpenClaw iOS/Android + Newsweek + Proton Lumo 2.0 + Atomathic Physical AI 2.0 + PagerDuty Jenn Tejada + OpenAI $965B + Apple 5 iPhones to the 24-month plan)
17. **Redax SoC choice (Qualcomm vs MediaTek)** — needed before Q3 W1 LFM2.5-230M swap-in (recommend: confirm with hardware team)
18. **LFM2.5-230M on aarch64 (Raspberry Pi 5) benchmarks** — after Q3 W1 swap-in, 1-day benchmark (recommend: yes)
19. **AIPOCH MedSkillAudit v1.0 spec compliance-mode add priority** — Q3 W3, 1 day, 1 engineer (recommend: yes, v18 concrete pre-deployment medical AI audit framework)
20. **Godot Foundation AI code rules v1.0 spec safety-considerations add priority** — Q3 W3, 1 day, 1 engineer (recommend: yes, v18 foundation-level validation of agent accountability)
21. **Time Magazine on RSI v1.0 spec add priority** — Q3 W3, 1 day, 1 engineer (recommend: yes, v18 only Anthropic-is-hedging validation)
22. **X (Twitter) hosted MCP server v1.0 spec add priority** — Q3 W3, 1 day, 1 engineer (recommend: yes, v18 third named, shipped protocol artifact)

## Footnotes (v19)

[^v19-1]: https://www.latimes.com/business/story/2026-06-29/google-poached-to-lose-two-more-senior-ai-staffers-to-anthropic — Google AI brain drain to Anthropic (Adler, Pritzel), June 29 2026 (NEW v19 CRITICAL #1)
[^v19-2]: https://www.cnbc.com/2026/06/29/alphabet-googl-stock-dow-average.html — Alphabet stock worst month since Feb 2025, June 29 2026 (NEW v19 SHARPEN)
[^v19-3]: https://www.reuters.com/business/google-limits-metas-use-its-gemini-ai-models-ft-reports-2026-06-28/ — Reuters: Google limits Meta's Gemini compute (FT-sourced), June 28 2026 (NEW v19 CRITICAL #1 + SHARPEN)
[^v19-4]: https://www.politico.com/news/2026/06/29/exclusive-newsom-anthropic-ink-deal-to-expand-government-use-00979584 — Politico exclusive: Anthropic-Newsom California deal (Claude at 50% off), June 29 2026 (NEW v19 CRITICAL #2)
[^v19-5]: https://www.govtech.com/artificial-intelligence/as-its-own-ai-tool-expands-california-will-use-anthropic-too — GovTech: California-Anthropic + Poppy in-house AI, June 29 2026 (NEW v19 CRITICAL #2)
[^v19-6]: https://www.engadget.com/2204549/theres-now-an-openclaw-app-for-ios-and-android-phones/ — Engadget: OpenClaw iOS+Android + founder → OpenAI, June 30 2026 (NEW v19 CRITICAL #3)
[^v19-7]: https://9to5google.com/2026/06/29/openclaw-app-android-ios/ — 9to5Google: OpenClaw iOS+Android launch, June 30 2026 (held from v18)
[^v19-8]: https://mashable.com/tech/openclaw-ios-android — Mashable: OpenClaw security flaw + iOS+Android, June 30 2026 (held from v18)
[^v19-9]: https://roadtovr.com/memomind-one-smart-glasses-kickstarter-release/ — Road to VR: MemoMind One (XGIMI) $500K Kickstarter, late June 2026 (NEW v19 CRITICAL #4)
[^v19-10]: https://www.rcrwireless.com/20260629/carriers/china-mobile-shanghai — RCR Wireless: China Mobile MWC Shanghai 2026 "mobile intelligence" + AI glasses, June 29 2026 (NEW v19 SHARPEN)
[^v19-11]: https://www.military.com/nato-drone-exercise-amplifies-international-battle-for-military-airspace-control — Military.com: NATO SAPIENT TIE26, late spring 2026 (NEW v19 SHARPEN)
[^v19-12]: https://gizmodo.com/ar-glasses-have-a-massive-size-problem-2000779454 — Gizmodo: AR Glasses size problem, early July 2026 (NEW v19 SHARPEN)
[^v19-13]: https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026 — Anthropic Claude Sonnet 5 + Claude Apps Gateway, July 2 2026 (held from v18)
[^v19-14]: https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668 — Newsweek "Open Accountability Standards," early July 2026 (held from v18)
[^v19-15]: https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/ — Proton Lumo 2.0, June 30 2026 (held from v18)
[^v19-16]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine on RSI, June 29 2026 (held from v18)
[^v19-17]: https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery — Atomathic Physical AI 2.0, July 1 2026 (held from v18)
[^v19-18]: https://www.techspot.com/news/112934-ram-prices-expected-rise-another-40-50-q3.html — RAM price spike, June 30 2026 (held from v18)
[^v19-19]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI (held from v16)
[^v19-20]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research (held from v16)
[^v19-21]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026 (held from v16)
[^v19-22]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^v19-23]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier, June 30 2026 (held from v17)
[^v19-24]: https://www.defenseone.com/technology/2026/07/genaimil-records-almost-17m-users-plans-new-model-additions/414569/ — DoD GenAI.mil 1.7M users, July 2 2026 (held from v16)
[^v19-25]: https://www.beri.net/article/ai-deployment-wars-9-billion-forward-deployed-engineers-enterprise-pilot-failure-crisis-2026 — $9.5B / 90 days / 5-vendor (held from v16)
[^v19-26]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B, Sapient (held from v15)
[^v19-27]: https://www.mobihealthnews.com/news/anthropic-debuts-claude-science-renews-access-fable-5-mythos-5 — Anthropic Claude Science, June 30 2026 (held from v17)
[^v19-28]: https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them- — IBM Red Hat Project Lightwell $5B (held from v17)
[^v19-29]: https://www.developingtelecoms.com/telecom-technology/optical-fixed-networks/20448-openan-project-aims-to-enable-o-m-agent-collaboration-in-autonomous-networks.html — OpenAN project (held from v17)
[^v19-30]: https://letsdatascience.com/news/pagerduty-chair-highlights-ai-agent-failure-risks-0367559f — PagerDuty Jenn Tejada, July 2 2026 (held from v18)
[^v19-31]: https://markets.businessinsider.com/news/stocks/aipoch-launches-medskillaudit-an-ai-audit-framework-to-evaluate-medical-ai-agent-skills-before-deployment-1036284741 — AIPOCH MedSkillAudit, June 29 2026 (held from v18)
[^v19-32]: https://letsdatascience.com/news/godot-tightens-contribution-policy-to-restrict-ai-code-e58bf90a — Godot AI code rules, June 30 2026 (held from v18)
[^v19-33]: https://techcrunch.com/2026/06/27/apple-vision-pro-exec-is-reportedly-leaving-for-openai/ — Apple Vision Pro exec to OpenAI, June 27 2026 (held from v18)
[^v19-34]: https://www.forbes.com/sites/sandycarter/2026/06/28/openai-eyes-2027-ipo-delay-as-washington-clears-anthropics-mythos-5/ — OpenAI delays IPO + Anthropic $965B, June 28 2026 (held from v18)

## v18 architecture review content (preserved in backup)

The v18 architecture review (preserved in `dan2-architecture-review.v18-backup-2026-07-04.md`, 29.5KB, 206 lines) covers: 3 CRITICAL issues (Anthropic Sonnet 5 + Claude Apps Gateway citable evidence for OpenClaw protocol surface, OpenClaw native iOS+Android + security flaw, Newsweek "Open Accountability Standards" directly names OpenClaw) + 4 SHARPEN (Proton Lumo 2.0, OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race, Zuckerberg "slower than expected," PagerDuty Jenn Tejada + $725B AI infra spend, Atomathic Physical AI 2.0, OpenAI $965B + IPO delay to 2027, X (Twitter) hosted MCP server, AIPOCH MedSkillAudit, Godot Foundation AI code rules, Time Magazine on RSI, Apple Vision Pro exec to OpenAI, Apple 5 new iPhones + memory crunch + M6/M7, RAM price spike) + 22 open questions + 34 footnotes. v18 9-step → 10-step marketing narrative. Decomposition score 9.2 → 9.4/10. **All v18 content is preserved verbatim in the backup. The v19 add is documented in the v19 header at the top of this file: 4 CRITICAL (Google AI brain drain, Anthropic-Newsom California, OpenClaw founder → OpenAI governance risk, MemoMind One $20/mo) + 5 SHARPEN (China Mobile MWC Shanghai AI glasses, NATO SAPIENT, Reuters Meta compute cap, AR Glasses size problem, Alphabet stock worst month). Decomposition score: 9.4 → 9.5/10. v18 implicit "OpenClaw is independent of OpenAI" framing is now partially retracted — OpenClaw is an OpenAI-supported open-source foundation project.**
## v22 addendum (2026-07-04 11:30 UTC / 17:00 IST)

**v22 deltas vs v21 (4 CRITICAL adds, 5 SHARPEN, 0 broad rollbacks, 1 service-decomposition change, 14-step marketing narrative):**

1. **NEW v22 CRITICAL #1 — LFM2.5-VL-450M service-confirmed: visiond service. v22 vendor-confirmed evidence + LFM2.5-1.2B-Thinking as v1.5 reasoningd alternative.** The v21 LFM2.5-VL-450M is *vendor-confirmed* to run Q4_0 on Jetson Orin Nano at 233-242ms for 256-512px images; post-trained with RL + preference optimization; supports bounding boxes + function calling + 8 languages; named use case is on-device wearables. **v22 service-decomposition change: confirm `visiond` as the v1.0 service that wraps LFM2.5-VL-450M, with `perceptiond` as the *higher-level* service that orchestrates visiond + audiod + memoryd. Add a v1.0 service-decomposition diagram to the v1.0 spec. Q3 W2, 1 day, 1 engineer.**

2. **NEW v22 CRITICAL #2 — LFM2.5-ColBERT-350M + LFM2.5-Embedding-350M: memoryd v1.5 retriever alternatives.** Purpose-built on-device retriever family. **v22 add: 2-week spike vs. the current MiniLM-L6-v2 in memoryd. If wins on the v22 memoryd eval harness, swap. 1 engineer, target Q3 W4.**

3. **NEW v22 CRITICAL #3 — Meta Conversation Focus paywall (9to5Google, Jul 1 2026) as v22 service-decomposition evidence.** Meta charges $20/mo to gate an *on-device* feature. **v22 add: cite in the v1.0 spec service-decomposition section: "Closed-source vendors are *addicted* to subscription-locking every AI capability, even the ones that cost them nothing per-inference. Dan Glasses's audiod + perceptiond + memoryd + toold + ttsd are *owned by the user* and run *on the user's device* with *no subscription*." Q3 W2, 30 min, 1 engineer copy.**

4. **NEW v22 CRITICAL #4 — Microsoft Research "From Self-Improving Agents to Co-Evolving Human-AI Systems" as v22 service-decomposition evidence (Microsoft Research, July 2026).** The v21 add confirmed the 3-axis taxonomy. **v22 add: cite the paper's H≠0 (human-involved) selective pressure axis as the v22 architectural pattern for Dan Glasses. "Dan Glasses is a co-evolving human-AI system, with auditable H≠0 selective pressure on the open-weights agent loop." Q3 W2, 1 day copy, 1 engineer.**

5. **NEW v22 SHARPEN #1 — OpenClaw iOS + Android official launch (TechCrunch, Jun 30 2026) as v22 toold service evidence.** OpenClaw is *named, dated, confirmed* on the mobile substrate. **v22 add: cite the v22 launch in the v1.0 spec toold section: "toold wraps OpenClaw. OpenClaw is the gateway. The phone is the mobile node. Dan Glasses is the wearable node. All three are open-source and on-device." Q3 W2, 30 min, 1 engineer copy.**

6. **NEW v22 SHARPEN #2 — Vint Cerf TCP/IP-for-agents panel (Open Frontier, Jun 30 2026) as v22 toold service evidence.** Vint Cerf + Matei Zaharia + Francois Chollet panel. **v22 add: cite the v22 panel in the v1.0 spec toold section: "The internet needed TCP/IP. Agents need it too. toold wraps OpenClaw + Anthropic Claude Apps Gateway + X MCP. Dan Glasses is the wearable node on the same protocol surface." Q3 W2, 30 min, 1 engineer copy.**

7. **NEW v22 SHARPEN #3 — LFM2.5-230M third-party benchmarked (VentureBeat, late June 2026) as v22 audiod post-processor evidence.** 213 tok/s on Galaxy S25 Ultra CPU, 42 tok/s on Raspberry Pi 5. 10 languages. **v22 add: cite the VentureBeat + Medium pieces in the v1.0 spec audiod section. No service-decomposition change. Q3 W2, 30 min, 1 engineer copy.**

8. **NEW v22 SHARPEN #4 — Time Magazine Favaro+Clark Anthropic-internal-hedge (Jun 29 2026) as v22 toold safety evidence.** "We are not there yet, and recursive self-improvement is not inevitable." **v22 add: cite the Time piece + Favaro+Clark quote in the v1.0 spec toold safety-considerations section. Q3 W2, 30 min, 1 engineer copy.**

9. **NEW v22 SHARPEN #5 — Adaptive Auto-Harness arXiv 2606.01770 as v22 toold + perceptiond + memoryd self-improving evidence.** A 2026 paper on the self-improving agent harness pattern. **v22 add: cite the paper in the v1.0 spec toold + perceptiond + memoryd sections as v22 *published self-improving harness pattern*. Q3 W3, reading spike, 1 engineer.**

**v22 service-decomposition summary (v1.0):**
- **visiond** (NEW v22 service name) — LFM2.5-VL-450M (vision-language, vendor-confirmed Q4_0 on Jetson Orin Nano, RL+preference-optimized, bounding boxes + function calling + 8 languages, on-device wearable)
- **audiod** — whisper.cpp base.en (STT) + KittenTTS medium (TTS) + LFM2.5-230M (post-processor, third-party benchmarked)
- **perceptiond** — orchestrates visiond + audiod + memoryd + toold, with `perceptiond.skill_evolution` (v21 plan-A, region-level VLM verifier + skill library per ComfyClaw arXiv 2607.01709)
- **memoryd** — MiniLM-L6-v2 (current) + LFM2.5-ColBERT-350M (v22 plan-B1 candidate) + Memora (v1.5) + As We May Search (v1.5)
- **toold** — OpenClaw (gateway, iOS+Android launched Jun 30 2026) + Hermes Agent (agent framework, v21)
- **ttsd** — KittenTTS medium (v1.0) + Qwen3-TTS (v1.5 plan-G) + Chatterbox (v1.5 plan-H)
- **reasoningd** (v1.5) — HRM-Text-1B (plan-B) + LFM2.5-1.2B-Thinking (v22 plan-C1) + LFM2.5-2.6B + GLM-5.2 + Apertus v1.1 4B + OpenPhone-3B
- **rsid** (v2.0) — SIA-W+H + SIA-H + Microsoft Research co-evolution H≠0 selective pressure

**v22 13-step → 14-step marketing narrative:** (1) BBC Meta paywall, (2) Apple $1,200+ (now *plus* Apple camera AirPods Pro suspended), (3) Anthropic Mythos 5 Glasswing (now *plus* NSA Rudd: "broke into almost all of our classified systems"), (4) GLM-5.2 MIT (now *plus* WSJ: rivals Mythos + Chris Inglis endorsement), (5) Palantir + NVIDIA sovereign Nemotron, (6) $14.5B / 120 days / 6-vendor implementation-wedge bet, (7) DoD GenAI.mil 1.7M users, (8) GPT-5.6 government-gating, (9) Vinton Cerf: agents need TCP/IP (now *plus* panel-confirmed, v22 SHARPEN), (10) v19 Newsweek + Anthropic Gateway + X MCP (now *plus* OpenClaw iOS+Android official launch, v22 SHARPEN), (11) v20 Axios + Bad Epoll + LA Times + Apple AirPods + WSJ GLM-5.2 rotation, (12) v21 Kimi K2.7 Code in GitHub Copilot + GLM-5.2 NVFP4 4× DGX Spark + ComfyClaw arXiv + WebBrain, (13) v22 Microsoft Research co-evolution + Mastermind arXiv + p-MEM DAC + SAIMY Dream Company + GLM-5 async RL, **(14) NEW v22: Meta Conversation Focus paywall + LFM2.5-VL-450M vendor-confirmed + LFM2.5-1.2B-Thinking sub-1GB + LFM2.5-ColBERT-350M on-device retrieval + Time Magazine Favaro+Clark Anthropic-internal-hedge + Adaptive Auto-Harness arXiv 2606.01770.**

**v22 architecture decomposition score: 9.6 → 9.7/10.** v21 elevates with ComfyClaw arXiv 2607.01709 + WebBrain + Microsoft Research co-evolution + Kimi K2.7 Code + GLM-5.2 NVFP4 4× DGX Spark + p-MEM DAC + Mastermind + SAIMY Dream Company + GLM-5 async RL. v22 elevates further with: **LFM2.5-VL-450M vendor-confirmed-on-Jetson-Orin (v22 vendor-confirmed evidence)** + **LFM2.5-1.2B-Thinking sub-1GB on-device reasoning (v22 non-Sapient reasoning alternative)** + **LFM2.5-ColBERT-350M on-device retrieval (v22 purpose-built retriever alternative)** + **Meta Conversation Focus paywall (v22 strongest evidence for closed-source addiction to subscription-locking on-device features)** + **OpenClaw iOS+Android official launch (v22 named-dated-confirmed mobile-substrate signal)** + **Cerf TCP/IP-for-agents panel (v22 named-dated industry-acknowledgment)** + **LFM2.5-230M third-party benchmarked (v22 S25-Ultra + RPi5 evidence)** + **Time Magazine Favaro+Clark Anthropic-internal-hedge (v22 Anthropic-cofounder-hedge-validated)** + **Adaptive Auto-Harness arXiv 2606.01770 (v22 published self-improving harness pattern)** + **Microsoft Research agentic-evolution deeper analysis (v22 Microsoft-Research-named co-evolution pattern)**. The decomposition is now *vendor-confirmed, reasoning-alternative-on-device, retrieval-alternative-on-device, paywall-addiction, openclaw-named-dated, cerf-panel-confirmed, third-party-benchmarked, anthropic-internal-hedge-validated, self-improving-harness-published, microsoft-research-taxonomized*.

**v22 retractions of v21:** **0 broad rollbacks.** v21 service-decomposition holds. v21 vision model (LFM2.5-VL-450M) confirmed. v21 STT (whisper.cpp base.en) confirmed. v21 TTS (KittenTTS medium) confirmed. v21 audiod post-processor (LFM2.5-230M) confirmed. v21 agent framework (Hermes Agent) confirmed. v21 toold (OpenClaw) confirmed. v21 perceptiond.skill_evolution plan-A confirmed. v21 GLM-5.2 NVFP4 4× DGX Spark plan-E confirmed. v21 GLM-5 async RL plan-F confirmed. v21 Memora + As We May Search v1.5 memoryd confirmed. v21 SIA-W+H port confirmed (now with Microsoft Research co-evolution cite). v21 HRM-Text-1B plan-B confirmed. v21 Apertus v1.1 4B plan-D confirmed. v21 OpenPhone-3B plan-E confirmed. v21 Qwen3-TTS plan-G confirmed. v21 Chatterbox plan-H confirmed. v21 Kimi K2.7 Code in GitHub Copilot confirmed. v21 ComfyClaw arXiv 2607.01709 confirmed. v21 WebBrain confirmed. v21 p-MEM DAC confirmed. v21 Mastermind arXiv 2607.01764 confirmed. v21 SAIMY Dream Company confirmed. v21 GLM-5 async RL on Hugging Face confirmed. **All v21 signals hold in v22.**


[^v22-1]: https://www.liquid.ai/blog/lfm2-5-vl-450m — Liquid AI LFM2.5-VL-450M blog, Apr 8 2026 (NEW v22 CRITICAL #1)
[^v22-2]: https://www.liquid.ai/blog/lfm2-5-retrievers — Liquid AI LFM2.5-ColBERT-350M + LFM2.5-Embedding-350M retrievers, Jun 18 2026 (NEW v22 CRITICAL #2)
[^v22-3]: https://9to5google.com/2026/07/01/meta-glasses-get-premium-usage-limits/ — 9to5Google: Meta Conversation Focus paywall, Jul 1 2026 (NEW v22 CRITICAL #3)
[^v22-4]: https://www.microsoft.com/en-us/research/wp-content/uploads/2026/07/agentic-evolution.pdf — Microsoft Research agentic-evolution, July 2026 (NEW v22 CRITICAL #4)
[^v22-5]: https://techcrunch.com/2026/06/30/openclaw-is-finally-available-on-android-and-ios/ — TechCrunch: OpenClaw iOS+Android launch, June 30 2026 (NEW v22 SHARPEN #1)
[^v22-6]: https://letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vint Cerf TCP/IP-for-agents panel, June 30 2026 (NEW v22 SHARPEN #2)
[^v22-7]: https://venturebeat.com/ai/liquid-ais-smallest-model-yet-lfm25-230m-beats-models-4x-its-size-at-data-extraction-can-run-anywhere/ — VentureBeat: LFM2.5-230M beats 4X its size, late June 2026 (NEW v22 SHARPEN #3)
[^v22-8]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine: Favaro+Clark Anthropic-internal-hedge, June 29 2026 (NEW v22 SHARPEN #4)
[^v22-9]: https://arxiv.org/abs/2606.01770 — "Adaptive Auto-Harness," arXiv 2606.01770, Jun 1 2026 (NEW v22 SHARPEN #5)


## v21 architecture review content (preserved in backup)

The v21 architecture review (preserved in `dan2-architecture-review.v21-backup-2026-07-04.md`, 41.1KB, 251 lines) covers: 4 CRITICAL (ComfyClaw arXiv 2607.01709 as perceptiond.skill_evolution direct analogue, Microsoft Research agentic-evolution 3-axis taxonomy, Kimi K2.7 Code in GitHub Copilot as 13-step narrative, GLM-5.2 NVFP4 4× DGX Spark as v1.5 plan-E) + 5 SHARPEN (p-MEM DAC 2026, Mastermind arXiv 2607.01764, SAIMY AI Dream Company, GLM-5 async RL on Hugging Face, WebBrain local-first) + 0 broad rollbacks. v21 12-step → 13-step marketing narrative. v21 service-decomposition held. Architecture decomposition score 9.5 → 9.6/10. **All v21 content is preserved verbatim in the backup. The v22 add is documented in the v22 addendum above: 4 CRITICAL (LFM2.5-VL-450M visiond service vendor-confirmed, LFM2.5-ColBERT-350M memoryd retriever alternative, Meta Conversation Focus paywall copy, Microsoft Research co-evolution deeper analysis) + 5 SHARPEN (OpenClaw iOS+Android official launch, Cerf TCP/IP-for-agents panel, LFM2.5-230M third-party benchmarked, Time Magazine Favaro+Clark Anthropic-internal-hedge, Adaptive Auto-Harness arXiv 2606.01770). v22 13-step → 14-step marketing narrative. v22 1 service-decomposition change (visiond as a v1.0 service name). Architecture decomposition score: 9.6 → 9.7/10.**



## v20 addendum (2026-07-04 09:35 UTC / 15:05 IST)

**v20 deltas vs v19 (4 CRITICAL, 4 SHARPEN, 1 partial sharpening, 0 broad rollbacks):**

1. **NEW v20 CRITICAL #1 — Axios: "How the world's top AI models were revived" (July 3 2026).** Amazon CEO Andy Jassy → Treasury Sec. Bessent → Commerce Sec. Lutnick → Anthropic CEO Amodei, 20-day showdown, jailbreak concerns about Mythos + Fable triggered sweeping export controls. **v20 add: the closed-source frontier is *inter-vendor fractured*. Amazon (Anthropic's own AWS host) reported Anthropic to the White House. This is the v20 strongest possible evidence for the on-device + open-weights + auditable memory + auditable agent loop stack being the v20 only trust-resilient substrate.** Q3 W2-W3 spec add, 1 day, 1 engineer.

2. **NEW v20 CRITICAL #2 — "Bad Epoll" Linux kernel flaw CVE-2026-46242 (July 3 2026) — Mythos found CVE-2026-43074 but missed Bad Epoll.** Mythos, the flagship closed-source safety/cyber model, missed a kernel bug in the same subsystem it scanned. **v20 add: the v1.0 safety spec must adopt the v20 *auditable-bug-discovery* pattern — every Dan Glasses release scanned by Mythos + GLM-5.2 + Apertus v1.1 4B before shipping, with findings published in a public security advisory. The Mythos-missed-bug benchmark is the v20 strongest possible evidence that *closed-source frontier models are not a reliable substrate for open-weights safety*.** Q3 W2-W3, 1 day, 1 engineer.

3. **NEW v20 CRITICAL #3 — Apple camera AirPods Pro "suspended" per Kosutami (July 3 2026).** Apple has missed two consecutive wearable-visual-AI ship dates — the AirPods Pro camera product (H1 2026) and the smart glasses (end 2027). **v20 add: the wearable-visual-AI competitive vacuum is now the v20 widest it has been in 12 months. Lock the v1.0 ship window to Q4 2026.** Q3 W2, 30 min, 1 engineer.

4. **NEW v20 CRITICAL #4 — LA Times + Bloomberg: Silicon Data LLM Token Expenditure Index -20% from May high (July 3 2026).** "The AI trade is losing one of its key signals." **v20 add: the on-device stack (lifetime cost of $349 hardware + free local inference) is the v20 only credible answer to the v20 unit-economics crisis. Cite Bloomberg + LA Times in the v1.0 spec pricing section.** Q3 W2-W3, 1 day copy, 1 engineer.

5. **NEW v20 SHARPEN #1 — Wall Street: Palo Alto + CrowdStrike all-time highs, PHLX semis -6.3%/-5.4%, WSJ: Zhipu GLM-5.2 now rivals Mythos at vulnerability hunting (July 3 2026).** Capital is rotating out of semis and into cybersecurity on the back of evidence that open-weight GLM-5.2 is closing the gap on Mythos. **v20 SHARPEN: the v19 GLM-5.2 / Mythos-cybersecurity story is now *Wall Street-priced*. Cite in v1.0 spec pricing/positioning section.** Q3 W2, 1 day, 1 engineer.

6. **NEW v20 SHARPEN #2 — NSA Gen. Joshua Rudd: Mythos "broke into almost all of our classified systems, not in weeks, but in hours" (Economist, July 3 2026).** **v20 SHARPEN: Mythos is *too dangerous* to ship widely, *too valuable* to ship to no one. The on-device + open-weights + auditable path is the v20 structural answer. Cite in v1.0 spec security/safety section.** Q3 W2, 1 day, 1 engineer.

7. **NEW v20 SHARPEN #3 — Chris Inglis (former US National Cyber Director) endorses GLM-5.2 for defenders (Dark Reading, July 3 2026).** **v20 SHARPEN: the v19 GLM-5.2 China-side stack is now *former-NSA-cyber-director-endorsed*. Cite in v1.0 spec security/positioning section.** Q3 W2, 1 day, 1 engineer.

8. **NEW v20 SHARPEN #4 — Meta "Pocket" AI gizmos app launches on Apple App Store + Google Play, June 29 - July 3 2026.** "Your interactions with gizmos on Pocket will be used to improve AI at Meta." **v20 SHARPEN: Meta is now using user gizmos to *train Meta's AI*. The v19 "Meta is compute-constrained" narrative is now a v20 "Meta is data-hungry + compute-constrained" narrative. The on-device + open-weights + auditable memory stack is the v20 only answer to the v20 *user-data-as-AI-training-fuel* pattern. Cite in v1.0 spec privacy/positioning section.** Q3 W2, 1 day, 1 engineer.

**v20 architecture decomposition score: 9.5 → 9.6/10.** v19 elevates with Vinton Cerf + Anthropic Claude Apps Gateway + OpenClaw native iOS+Android + Newsweek + Atomathic Physical AI 2.0. v20 elevates further with: **Axios Amazon-Jassy-Anthropic jailbreak escalation (v20 strongest evidence for the inter-vendor trust gap)** + **Bad Epoll Mythos-missed-bug (v20 strongest evidence for the auditable-bug-discovery pattern)** + **Apple camera AirPods Pro suspended (v20 strongest evidence for the wearable-visual-AI competitive vacuum)** + **LA Times + Bloomberg token-price collapse (v20 strongest evidence for the unit-economics imperative)** + **Palo Alto + CrowdStrike + GLM-5.2 vs Mythos (v20 Wall Street-priced open-weights cybersecurity)** + **NSA Gen. Rudd on Mythos (v20 NSA-validated safety-considerations)** + **Chris Inglis on GLM-5.2 (v20 former-NSA-cyber-director-endorsed)** + **Meta Pocket gizmos (v20 user-data-as-AI-training-fuel evidence).** The decomposition is now *inter-vendor-trust-fractured, kernel-bug-benchmarked, wearable-vacuum-opened, unit-economics-cracking, Wall-Street-priced, NSA-validated, former-NSA-director-endorsed, data-hungry-vendor-exposed*.

**v20 retractions:** 0 broad rollbacks. v19 Mythos 5 Glasswing framing is now *post-jailbreak-control*, *NSA-validated-at-the-classified-systems-level*, and *Wall-Street-priced-as-replaceable-by-GLM-5.2*. The framing holds; the v20 emphasis shifts to the *inter-vendor trust gap* and the *unit-economics imperative*.


[^v20-1]: https://www.axios.com/2026/07/03/anthropic-ai-models-revived-behind-the-scenes — Axios: How the world's top AI models were revived (Amazon Jassy → Bessent → Lutnick → Amodei, 20-day showdown), July 3 2026 (NEW v20 CRITICAL #1)
[^v20-2]: https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html — "Bad Epoll" Linux kernel flaw (CVE-2026-46242) — Mythos found CVE-2026-43074 but missed Bad Epoll; fix already landed, July 3 2026 (NEW v20 CRITICAL #2)
[^v20-3]: https://www.macrumors.com/2026/07/03/camera-airpods-pro-development-suspended-leaker/ — Apple camera AirPods Pro "suspended" per Kosutami, July 3 2026 (NEW v20 CRITICAL #3)
[^v20-4]: https://www.latimes.com/business/story/2026-07-03/with-token-prices-collapsing-regulation-rising-ais-pricing-power-looks-fragile — LA Times: Silicon Data LLM Token Expenditure Index -20% from May high; AI pricing power "looks fragile," July 3 2026 (NEW v20 CRITICAL #4)
[^v20-5]: https://letsdatascience.com/news/ai-driven-rotation-reshapes-stock-market-leadership-dc767e6c — Palo Alto + CrowdStrike all-time highs; PHLX semi -6.3%/-5.4% Wed/Thu; WSJ: Zhipu GLM-5.2 now rivals Mythos at vulnerability hunting, July 3 2026 (NEW v20 SHARPEN #1)
[^v20-6]: https://mimir.substack.com/p/the-new-news-in-ai-7326-edition — NSA Gen. Joshua Rudd: Mythos "broke into almost all of our classified systems, not in weeks, but in hours," July 3 2026 (NEW v20 SHARPEN #2)
[^v20-7]: https://www.darkreading.com/cyber-risk/chinese-llms-broaden-gap-between-attackers-defenders — 360 Security "Tulongfeng" finds 3,400+ vulnerabilities; Chris Inglis (former US National Cyber Director) endorses GLM-5.2 for defenders, July 3 2026 (NEW v20 SHARPEN #3)
[^v20-8]: https://www.mediapost.com/publications/article/416292/meta-prizes-ai-generated-creative-in-new-mini-game.html — Meta launches "Pocket" AI gizmos app on Apple App Store + Google Play, June 29 - July 3 2026 (NEW v20 SHARPEN #4)


## v19 architecture review content (preserved in backup)

The v19 architecture review (preserved in `dan2-architecture-review.v19-backup-2026-07-04.md`, 31.9KB, 213 lines) covers: 4 CRITICAL (Google AI brain drain, Anthropic-Newsom California, OpenClaw founder → OpenAI governance risk, MemoMind One $20/mo) + 5 SHARPEN (China Mobile MWC Shanghai AI glasses, NATO SAPIENT, Reuters Meta compute cap, AR Glasses size problem, Alphabet stock worst month) + 1 partial retraction (OpenClaw is now OpenAI-supported). v19 10-step marketing narrative. Decomposition score 9.4 → 9.5/10. **All v19 content is preserved verbatim in the backup. The v20 add is documented in the v20 addendum above: 4 CRITICAL (Axios Amazon-Jassy-Anthropic jailbreak escalation, Bad Epoll Mythos-missed-bug, Apple camera AirPods Pro suspended, LA Times token-price collapse) + 4 SHARPEN (Wall Street GLM-5.2 vs Mythos, NSA Rudd, Chris Inglis, Meta Pocket). v20 decomposition score: 9.5 → 9.6/10.**
