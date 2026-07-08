# Dan Glasses Architecture Review v8 — Problems, Risks, Suggested Improvements

**Author:** Dan2 | **Date:** 2026-06-25 07:35 IST
**Status:** v8 supersedes v7
**Scope:** audiod, perceptiond, memoryd, toold, ttsd, os-toold, OpenClaw, dan-glasses-app, danlab-multimodal

---

## Executive verdict

- **Service decomposition is correct.** The 7-service split matches the wearable's functional seams.
- **Transport is mostly correct for v1, but not for v2.** HTTP+JSON is fine for the research harness; it will be too heavy for the wearable control plane once latency, power, and reliability tighten.
- **The missing primitive is a self-model.** Perplexity Brain and AI Weekly's self-improvement wall make this obvious: memory without self-model is just storage.
- **The highest-leverage fix is the reliability surface.** Every daemon should expose calibration, robustness, and failure-mode metrics.
- **OpenClaw is a strategic asset.** Microsoft Scout's choice of OpenClaw validates the gateway layer.

---

## 1) Service decomposition — correct seams, incomplete contracts

### What is right
- **audiod** owns capture, VAD, transcription, publication.
- **perceptiond** owns vision capture, salience, VLM inference, descriptions.
- **memoryd** owns episodic / semantic / procedural memory and now must own operative context.
- **toold** owns command execution.
- **ttsd** owns synthesis.
- **os-toold** owns path-guarded OS utilities.
- **OpenClaw** orchestrates external channels and Zo MCP.
- **dan-glasses-app** is the human interface.

### What is wrong or missing
- **No explicit reliability contract.** The current `/health` endpoints are liveness only.
- **No self-model seam.** Harness evolution has nowhere to write its rationale.
- **No adaptive routing layer.** Edge-only vs cloud-only is the wrong abstraction.
- **No persistent event/audit stream.** Tool actions, revision rationales, and failure modes are not uniformly recorded.
- **No per-memory-type retention policy.** Memory is already multi-type, but the system does not yet treat retention as part of the contract.

### Recommended fix
Introduce a shared contract:

```text
GET /health
GET /status
GET /reliability
GET /reliability/calibration
GET /operative_context
GET /audit_log
```

Every daemon should publish enough state for the user and the harness to answer:
- What did it do?
- How confident was it?
- Did it improve or decay?
- What changed last time?

---

## 2) audiod — the right place to start self-improvement

### What is right
- Frozen encoder + small calibration head is the right edge shape.
- Whisper-based STT is pragmatic.
- VAD + transcript publishing is a good seam for a reliability harness.

### Risks
- **False confidence.** Speech confidence can be badly calibrated on Indian-accent English.
- **Rise-and-collapse.** The self-improvement wall suggests iteration-1 gains may not compound.
- **Reward hacking.** If reward is only ECE or only WER, the agent can exploit one metric while harming another.
- **Overfitting to Librispeech.** Good lab numbers may fail on real wearables.

### Suggested improvements
- Build the audiod RL agent around:
  - frozen whisper.cpp encoder
  - 4-layer calibration head
  - ECE + Brier + ID + OOD evaluation
  - AHE-style harness evolution
  - explicit failure-mode registry
  - memoryd operative_context write-back
- Keep the base model frozen.
- Add rollback to the best checkpoint on collapse.

### Opinion
This is the right first self-improving subsystem because the reward is observable and bounded. It is much safer than recursive weight modification on a general model.

---

## 3) perceptiond — viable, but model strategy needs a more modern path

### What is right
- Salience gating is essential.
- Separate VLM service is correct.
- `/frame.jpg` and `/stream` were the right missing UI primitives.

### Risks
- **LFM2.5-VL-450M is acceptable, not ideal.** It works, but it is not the power/performance ceiling.
- **No frame retention.** The user cannot revisit what the model saw.
- **Mock capture ambiguity.** Production and dev can blur if mock is not clearly signaled.
- **No adaptive routing.** Some frames are cheap, some should escalate.

### Suggested improvements
- Keep LFM2.5-VL-450M as default.
- Add CondenseVLM + QViD + V5e-0 stack.
- Add INAR-VL routing.
- Add frame retention only as an opt-in v2 feature.
- Make mock mode visually obvious in UI.

### Opinion
The architecture is right. The current model choice is a good bridge, not a destination.

---

## 4) memoryd — the moat, but currently too small

### What is right
- SQLite + embeddings is a good baseline.
- episodic / semantic / procedural memory is a good taxonomy.
- OpenAI-compatible embeddings endpoint is useful.

### Risks
- **No operative context.** The system stores memory, but not the “active memory that drives behavior.”
- **No provenance graph.** You need to know why a memory exists, not just that it exists.
- **No consolidation cadence.** A good memory system synthesizes over time.
- **Embedding-only retrieval is not enough.** Pure vector search is weak for planning and agentic memory.

### Suggested improvements
- Add **operative_context** as a first-class memory stream.
- Add **DPCM** provenance edges.
- Add **AEL** retrieval-mode bandit.
- Add overnight synthesis into an LLM wiki.
- Add per-type retention rules.
- Add user-visible audit trails.

### Opinion
This is the biggest strategic moat in the stack. Perplexity Brain validated the form factor: memory about the agent’s work, not the user. Danlab should implement the open-source wearable version now.

---

## 5) toold — useful, but must become auditable

### What is right
- Sandboxed execution is correct.
- Explicit timeout and command filtering are required.

### Risks
- **Invisible side effects.** Tool execution can silently change the environment.
- **No provenance.** Future agents cannot inspect why a command ran.
- **Sandbox drift.** If the tool state changes, the harness can become non-reproducible.

### Suggested improvements
- Write every command to memoryd operative_context.
- Record command, timeout, exit code, stdout/stderr summary, sandbox state.
- Add `GET /audit_log`.

### Opinion
toold is fine as an execution primitive, but it is not a research primitive until it becomes auditable.

---

## 6) ttsd — the easiest swap

### What is right
- HTTP TTS surface is stable.
- Current shape is easy to integrate.

### Risks
- KittenTTS is no longer the best tradeoff.
- Latency and voice quality are not the best available in 2026.

### Suggested improvements
- Swap to Kokoro-82M.
- Add Hindi voice.
- Keep WAV output.
- Add WebGPU fallback for browser path.

### Opinion
This is a low-risk, high-upside replacement. Do it now.

---

## 7) OpenClaw — strategic gateway, but its runtime shape is not wearable-safe yet

### What is right
- TypeScript/Node is a good control plane language.
- MCP bridging is the right abstraction.
- Telegram is a useful outbound channel.

### Risks
- **Transport weight.** Node is fine at the gateway, but not ideal for the wearable hot path.
- **Tailscale sandbox mismatch.** The current environment cannot fully honor tailscaled assumptions.
- **Pairing state fragility.** Telegram pairing is easy to break if config is reset.

### Suggested improvements
- Keep Node/OpenClaw at the gateway.
- Do not move core wearable loops into Node.
- Add audiod RL event channel.
- Treat OpenClaw as the external orchestration plane, not the real-time control plane.

### Opinion
The Node gateway is right. The wearable’s low-latency loops should stay in daemon-local code.

---

## 8) danlab-multimodal — honest label needed

### Current state
- It is not true RL.
- It is a heuristic / harness-evolution scaffold.
- That is acceptable, as long as the label is honest.

### What it needs
- A clear self-model.
- Auditability.
- Failure-mode tracking.
- Separation between eval, optimization, and deployment.

### Suggested next step
Use danlab-multimodal as the harness framework around audiod RL, memoryd v2, and perceptiond compression experiments. Do not claim closed-loop general self-improvement until the self-model is shipped and bench-marked.

---

## 9) Recommended priority order

1. audiod calibration RL agent
2. memoryd v2
3. Kokoro-82M swap
4. reliability surface contract
5. perceptiond token-pruning stack
6. INAR-VL routing
7. OpenClaw audit channel
8. danlab-multimodal self-model seam

---

## 10) Risks that matter most

- **Reward hacking** in calibration loops.
- **Overfitting to lab data** instead of wearable data.
- **Invisible memory drift** if operative_context is not visible.
- **User trust collapse** if privacy claims exceed implementation.
- **Architecture drift** if gateway code and wearable code converge too much.

---

## Bottom line

Dan Glasses has the right seams. The next leap is not more seams; it is **better contracts**. Build the reliability surface, the self-model, the memory provenance graph, and the adaptive router. That is the architecture that can actually compound.

— DAN-2, 2026-06-25 07:35 IST