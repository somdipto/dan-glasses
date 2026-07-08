# Dan Glasses Architecture Review v13
**Author:** Dan2 (lead scientist / architect)
**Date:** 2026-06-19 09:30 IST
**Supersedes:** dan2-architecture-review.v12 (24 hours old)

---

## 0. Headline

**The architecture is correct. The two new v13 priorities are: (1) ship OpenClaw signed-skill infrastructure this week, and (2) swap the memory backend to Mnemosyne + LFM2.5-Embedding/ColBERT. Everything else from v12 still holds.**

## 1. What's correct (unchanged from v12)

1. Five-service decomposition (`audiod`, `perceptiond`, `memoryd`, `toold`, `ttsd`).
2. Salience gating *before* VLM in `perceptiond` (motion + face, `MAX_QUEUE_DEPTH = 2`).
3. HTTP control plane + WebSocket event plane.
4. `.deb` + systemd delivery on x86_64 / aarch64.
5. SQLite + markdown + vectors memory core, Obsidian as optional mirror.
6. Tauri v2 + CrabCamera + V4L2 desktop stack.

## 2. P0 issues (ship this week)

### 2.1 OpenClaw signed-skill infrastructure — now a P0, not a P1

**Severity: 🔴 P0 (was 🟡 P1 in v12).** The Skywork OpenClaw skill-malware guide documents an in-the-wild attack. Three changes must ship before v1.0:

1. **Sigstore + cosign for every Danlab-shipped skill.** Sign the `SKILL.md` + the package with cosign; commit the signature to Sigstore Rekor.
2. **Default-deny `policy.deny_skills`.** Move the OpenClaw default from "deny nothing" to "allow only the explicit Danlab-blessed allowlist."
3. **Skill sandbox.** Process jail — no fs access outside `~/.dan-glasses/skills/<name>/`, no network except explicit allowlist, no `subprocess` except via `toold`.

**Time:** 1 week. **Owner:** Dan1 (OpenClaw config) + Dan2 (skill sandbox). **Blocks:** v1.0 .deb.

### 2.2 OpenClaw memory backend pin — community-reported "weird memory behavior" fix

**Severity: 🔴 P0.** The Hermes-Agent Community confirmed a default-loads-wrong-provider bug. **Fix:** set `plugins.slots.memory = "memory-core"` in `openclaw.json` explicitly. Verify on every startup.

**Time:** 1 hour. **Owner:** Dan1. **Blocks:** v1.0 .deb.

### 2.3 Mnemosyne swap — replaces v12 W9 workstream

**Severity: 🟡 P0 for the workstream, not for v1.0.** Mnemosyne (98.9% on LongMemEval, OpenClaw native) replaces the v12 "build consolidation from scratch" plan. Install this week, validate the 98.9% number on the danlab-multimodal screenshot set.

**Time:** 1 day. **Owner:** Dan2 (memoryd). **Unblocks:** W9 (now 6 weeks instead of 12).

## 3. Critical issues (carry-forward from v12, unchanged)

These are the v12 critical issues, still blocking for v1.5 wearable:

1. **No power characterization on a known board** — W1, 4 weeks, owner Dan2. Block on Redax. **Update v13:** Add LFM2.5-Audio-1.5B to the W1 measurement set (collapse audiod + ttsd candidate).
2. **No `clawd-watchdog` for OpenClaw** — W5, 1 week.
3. **No `evented` aggregator** — W3, 3 weeks.
4. **No `stated` snapshot service** — W4, 2 weeks.
5. **No `clawd-watchdog` reads from `stated`** — W5, 1 week.

## 4. Important issues (6-month, carry-forward from v12)

1. **memoryd schema** — *superseded by v13 §2.3.* Mnemosyne + Eywa provenance + UaC user-model schema + RHO consolidation. 6 weeks.
2. **Wake-on-event primitive** — W12, 6 weeks. **Update v13:** target 50 mW idle (was 500 mW target in v12 — Box NPU data shows it's achievable).
3. **GPU/acceleration contract for VLM** — Update `perceptiond/SPEC.md` to specify per-form-factor accelerator.
4. **Security review of perception → os-toold path** — Add `description_intent` schema; only `kind=act` + allow-listed actions route to `toold`.
5. **`.deb` package signing** — Now P0 alongside OpenClaw skills (GPG + cosign).

## 5. Minor issues (12-24 month)

Unchanged from v12. **Update v13:** §4.2 "Five Python services are too many for the wearable" gets a partial answer — audiod and ttsd can be *collapsed* if LFM2.5-Audio-1.5B benchmark works out. **Net:** 4 services on the wearable (audiod+ttsd merged into one), not 5.

## 6. New v13 issues (last 24 hours)

### 6.1 OpenClaw skill malware documented in production

**Severity: 🔴 P0.** See §2.1. The 24-hour-old v12 "P1 action — security hardening" is now "P0 action — documented in-the-wild attack."

### 6.2 Fable 5 export control has an expiration date

**Severity: 🟡 Medium (positioning, not architecture).** Anthropic + Trump administration are negotiating. Fable 5 likely returns ~July 12 2026. The "Fable-5-safe" positioning has a ~30-day shelf life. **Move from "regulatory moat" to "feature."**

### 6.3 Apple memory chip pricing pressure (Tim Cook, WSJ, June 18 2026)

**Severity: 🟡 Medium (BOM, not architecture).** Validates the v12 "64GB primary" recommendation. Document the rationale: 128GB eMMC BOM may be 2-3× higher than projected. Lock the storage tier spec.

### 6.4 Illinois HB4843 — first state-level smart-glasses regulation

**Severity: 🟢 Low (product, not architecture).** The "on-device, push-to-talk, not always-recording" framing is structurally aligned with the regulatory direction. Document this in the privacy whitepaper.

### 6.5 LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M (Liquid AI, June 18)

**Severity: 🟡 Medium (architecture, but not blocking).** The retrieval-side of the memory stack just got purpose-built 350M models. **Add to W9.2 benchmark.**

### 6.6 Box v3.1.0 NPU acceleration works (jegly/Box, June 2026)

**Severity: 🟢 Low (v2 wearable, not v1.5).** First credible on-device NPU run for Gemma 3 1B on Snapdragon + MediaTek. **Implication for wearable v2 silicon plan:** hybrid CPU+NPU. v12 said "CPU only" for v1.5. v13: hybrid for v2.

## 7. Suggested v1.5 wearable changes (one page)

The v12 plan is right. The v13 changes are:

1. **W1.5:** Add LFM2.5-Audio-1.5B measurement to the W1 power-characterization workstream.
2. **W9 (memory):** Mnemosyne swap (Day 1), LFM2.5-Embedding-350M benchmark (Week 1), LFM2.5-ColBERT-350M late-interaction rerank (Week 2), Eywa provenance columns (Week 2-3), UaC user-model schema (Week 3-4), RHO consolidation (Week 4-5), audit log (Week 5-6). **6 weeks total.**
3. **W11 (compliance):** Add DPDP Act + EU AI Act compliance review. 4 weeks.
4. **W22 (open-source Kit):** Promote from Q4 2027 to **Day-1 promise.** Halo is the proof; we ship.
5. **W24 (battery + thermal v2):** Plan for hybrid CPU+NPU silicon based on Box NPU datapoint. 16 weeks.
6. **OpenClaw signed skills + default-deny policy:** ship in v1.0, not v1.5. (Moved up from v12 P1 to v13 P0.)

## 8. Top 3 architecture recommendations (Telegram summary)

1. **Ship OpenClaw signed-skill infrastructure (cosign + Rekor + default-deny) this week.** Three small changes, blocks v1.0 .deb. The in-the-wild attack is documented; the v12 "P1" is now P0.
2. **Install Mnemosyne as the OpenClaw memory backend. Day 1.** Replaces the v12 "build consolidation from scratch" plan. Unlocks W9 in days, not weeks.
3. **Promote the open-source "Dan Glasses Kit" from a Q4 2027 deliverable to a Day-1 promise.** Brilliant Labs Halo is the proof; Even Realities G2 is the competitor; the open-source wearable niche is now the right niche. Say it now, ship it soon.
