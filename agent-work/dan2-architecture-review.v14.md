# Dan Glasses Architecture Review v14
**Author:** Dan2 (lead scientist / architect)
**Date:** 2026-06-19 10:30 IST
**Supersedes:** dan2-architecture-review.v13 (24 hours old)

---

## 0. Headline

**v13 P0 list is unchanged (signed skills, Mnemosyne swap, memory pin). v14 MAJOR add: `privacyd` is promoted from a daemon to a *compliance attestation product* with OSS / $99 / $999 tiers. The Lutnick-letter resolution this week is the unlock. W26, 4 weeks.**

## 1. What's correct (unchanged from v13)

1. Five-service decomposition (`audiod`, `perceptiond`, `memoryd`, `toold`, `ttsd`).
2. Salience gating *before* VLM in `perceptiond`.
3. HTTP control plane + WebSocket event plane.
4. `.deb` + systemd delivery on x86_64 / aarch64.
5. SQLite + markdown + vectors memory core.
6. Tauri v2 desktop stack.

## 2. P0 issues (ship this week)

### 2.1 OpenClaw signed-skill infrastructure

**Severity: 🔴 P0 (unchanged from v13).** Three changes must ship before v1.0:
1. Sigstore + cosign for every Danlab-shipped skill.
2. Default-deny `policy.deny_skills`.
3. Skill sandbox.

**Time:** 1 week. **Owner:** Dan1 + Dan2. **Blocks:** v1.0 .deb.

### 2.2 OpenClaw memory backend pin

**Severity: 🔴 P0.** Set `plugins.slots.memory = "memory-core"`. Verify on every startup.

**Time:** 1 hour. **Owner:** Dan1.

### 2.3 Mnemosyne swap

**Severity: 🟡 P0 (workstream, not v1.0).** 1 day. W9 unblock.

### 2.4 NEW v14: Snapdragon Start application

**Severity: 🟡 P0 (strategic, not blocking).** Apply this week. **Owner:** Somdipto (CEO sign-off) + Dan1 (technical writeup). **Why now:** Snapdragon Start is invite-style; first-mover window is open. **Time:** 3-5 days.

## 3. NEW v14: privacyd as compliance attestation product (W26)

### 3.1 The unlock

The Lutnick-letter framework being negotiated this week (June 18 2026) will formalize a **measurement regime** for jailbreak severity, not just a yes/no export license. Every AI deployment will need a machine-readable compliance attestation. Sigstore + cosign + Rekor are the right primitives.

**v14 architectural decision:** productize `privacyd` as a compliance attestation framework.

### 3.2 Architecture

```
Input: model weights, training data sources, jailbreak test results
  ↓
privacyd attest build
  ↓
SLSA provenance + in-toto attestation
  ↓
cosign sign → Sigstore Rekor
  ↓
Output: signed attestation artifact + Rekor log entry
  ↓
Webhook to compliance officer / Slack / Teams / auditor
```

### 3.3 Compliance profiles (v14 launch set)

- **fable-5-safe:** Anthropic Fable 5 compliance check.
- **mythos-5-safe:** Anthropic Mythos 5 compliance check.
- **eu-ai-act-art-9:** EU AI Act Article 9 (risk management).
- **dpdp-act-2023:** India Digital Personal Data Protection Act.
- **soc2-ai:** SOC2 for AI deployments.

### 3.4 Pricing tiers

- **OSS Community (free):** self-host, public Rekor, all profiles, no SLA.
- **Indie/SMB ($99/mo):** 100 attestations/mo, signed compliance reports, webhook, email support.
- **Enterprise ($999/mo):** unlimited, SSO, custom compliance profiles, audit log export, on-prem, SLA.

### 3.5 Why this is the v14 unlock

1. **Timing:** Lutnick-letter resolution days away. Compliance regime imminent.
2. **White space:** No open-source compliance attestation for AI deployments exists as a product.
3. **Infrastructure:** Sigstore is mature. We are not building infra; we are building AI-specific attestation framework on top.
4. **Convergence:** Privacy story + open-source story + regulatory tailwind.

### 3.6 Workstream W26

- W26.1 (Week 1): Re-architecture `privacyd` as a cosign/Rekor-aware service. SLSA provenance generation.
- W26.2 (Week 2): Implement Fable-5-safe profile. Score: params, training data, jailbreak-test results, model hash.
- W26.3 (Week 3): Web UI for compliance officers.
- W26.4 (Week 4): Documentation + danlab.dev/privacyd launch.

**Owner:** Dan1 (UI) + Dan2 (core). **Cost:** ~$50/mo H100 for Rekor.

## 4. Critical issues (carry-forward from v13)

These are the v12 → v13 carry-forwards, still blocking for v1.5 wearable:

1. **No power characterization on a known board** — W1, 4 weeks, owner Dan2.
2. **No `clawd-watchdog` for OpenClaw** — W5, 1 week.
3. **No `evented` aggregator** — W3, 3 weeks.
4. **No `stated` snapshot service** — W4, 2 weeks.
5. **No `clawd-watchdog` reads from `stated`** — W5, 1 week.

## 5. NEW v14 critical issues

### 5.1 Apple 2027 = biggest product year in history (Gurman)

**Severity: 🟡 Medium (strategic, not architecture).** Six new iPhones, multiple AI wearables, M6 Macs. **The Apple-window may compress to 12-14 months.** v14 update: revisit v12's 14-month window quarterly. If Apple ships a wearable at WWDC 2027 (June 2027), our v1.5 ship window is the Q1 2027 deadline.

### 5.2 OpenAI Shazeer → consumer-companion architecture research

**Severity: 🟢 Low (validating, not new).** OpenAI is signaling post-transformer architecture for consumer AI companion. Our LFM2.5 + HRM + Mnemosyne stack is non-transformer. **Validation, not new work.**

### 5.3 Qualcomm + Inspecs partnership (June 17)

**Severity: 🟡 Medium (supply chain).** Snapdragon Start + Inspecs = integrated AI glasses supply chain. Danlab needs to be in this. **See §2.4.**

### 5.4 Snap Specs cost: $500M/yr dev, $2,195 price

**Severity: 🟢 Low (positioning, not architecture).** Validates our $400 BOM target as a moat.

## 6. Important issues (6-month, carry-forward from v13)

1. **memoryd schema** — Mnemosyne + Eywa + UaC + RHO. 6 weeks. v13 W9.
2. **Wake-on-event primitive** — W12, 6 weeks. Sub-50 mW idle target.
3. **GPU/acceleration contract for VLM** — Update `perceptiond/SPEC.md`.
4. **Security review of perception → os-toold path** — `description_intent` schema.
5. **`.deb` package signing** — GPG + cosign.

## 7. Minor issues (12-24 month)

Unchanged from v13.

## 8. Suggested v1.5 wearable changes (one page)

The v13 plan is right. v14 changes:

1. **W1.5:** Add LFM2.5-Audio-1.5B measurement to W1 power-characterization.
2. **W9 (memory):** Mnemosyne swap (Day 1), LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M (Week 1-2), Eywa provenance (Week 2-3), UaC schema (Week 3-4), RHO consolidation (Week 4-5). **6 weeks.**
3. **W11 (compliance):** DPDP Act + EU AI Act.
4. **W22 (open-source Kit):** Day-1 promise.
5. **W24 (battery + thermal v2):** Plan for hybrid CPU+NPU silicon. v14 update: **Snapdragon Start path is now parallel to Redax.**
6. **OpenClaw signed skills + default-deny policy:** ship in v1.0.
7. **NEW v14 W26 (privacyd as product):** 4 weeks. Compliance attestation framework with OSS / $99 / $999 tiers. Blocks: Lutnick-letter resolution this week.

## 9. Top 5 architecture recommendations (Telegram summary)

1. **Ship OpenClaw signed-skill infrastructure (cosign + Rekor + default-deny) this week.** P0. Blocks v1.0 .deb.
2. **Install Mnemosyne as OpenClaw memory backend. Day 1.** W9 unblock.
3. **Apply to Qualcomm Snapdragon Start program this week.** Turnkey silicon path. Inspecs partnership.
4. **Productize `privacyd` as compliance attestation framework (W26).** OSS / $99 / $999 tiers. The Lutnick-letter resolution this week is the unlock. 4 weeks.
5. **Promote open-source "Dan Glasses Kit" to Day-1 promise.** Brilliant Labs Halo is the proof. The 2x2 cell has us with Halo and Even Realities G2.