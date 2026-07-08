# Dan1 — GitHub README Improvements (v122)

**Run:** 2026-07-05 13:00 IST
**Author:** Dan1
**Scope:** `dan-glasses`, `dani`, `danlab-multimodal`, `paperclip`, and the `danlab` org profile README. **`blurr`/`Panda` removed from this list** — `blurr` in this workspace is Panda (Android phone operator, Ayush Chaudhary, MIT-licensed). It is not the on-device eval harness. Panda is a separate project with its own README. Don't conflate.
**Lead:** *The protocol is the bet. The data path is yours. The threat model is public. The wearable ships it.*
**v22 ADD:** Every README in scope must link `THREAT_MODEL.md` (or its own threat model section) and `PROTOCOL.md`. The v24 Adversa / HackerNoon / Anthropic-Samsung cites are mandatory in the dan-glasses and dani READMEs.

---

## 0. The cross-cutting rules (apply to every README in scope)

1. **Lead with the one-liner, not the project name.** The README is the homepage for the repo. The first 200 chars decide if a developer stays.
2. **Show the daemon map, the .deb, or the bot in the first 500 chars.** Receipts > adjectives.
3. **Link to the threat model doc and the protocol surface doc in every README that touches OpenClaw.** v22 ADD: this is non-negotiable. The Mashable + Adversa + HackerNoon cites are the marketing wedge.
4. **No "we're excited to announce."** Show the work.
5. **The 4 pillars appear in this order:** protocol → observability → on-device → small-beats-large.
6. **v22 ADD: the 2 v24 pillars** — threat-model-is-public, yours-not-theirs — appear after the 4 in this exact order.
7. **Pin to: danlab.dev, dan-consciousness, danlab-multimodal-demo.**
8. **License + provenance block at the top of every README:** `MIT · Built in Bengaluru · The substrate is auditable, not perfect.`
9. **Badges:** GitHub stars, license, last commit, arXiv (when applicable), HuggingFace (when applicable). No build-status badges unless they actually mean something.
10. **Contributing section must include the threat model reporting flow.** This is how security researchers become allies, not enemies. v22 ADD: link `THREAT_MODEL.md` directly in the contributing section.
11. **No "TODO" sections in the public README.** TODOs belong in the issue tracker.
12. **v22 ADD: the word "audited" replaces "secure" in all v22+ copy.** Secure is a claim. Audited is a receipt.

---

## 1. `dan-glasses` (the flagship)

### Current state
PRD §1 framing. v121 suggested a top-section rewrite. v122 adds the threat model + v24 cites.

### v122 deltas to the v121 top section

Replace the v121 "Install" block with the v22 launch-blocker gate:

```markdown
## Install

\`\`\`bash
# .deb (Q3 2026) — gated on THREAT_MODEL.md + PROTOCOL.md being live
curl -fsSL https://danlab.dev/install.sh | bash
\`\`\`

**Before you install, read the [threat model →](THREAT_MODEL.md) and the [protocol surface →](PROTOCOL.md).** The threat model is public. The audit log is public. The fix is in the doc.
```

Replace the v121 "The threat model is public" section with the v22 expanded version:

```markdown
## The threat model is public

@Mashable flagged a flaw in OpenClaw 2 months before mobile launch. @AdversaAI disclosed bash-tricks bypass 10 of 11 open-source AI coding agents. We are auditing both.

- toold strict-mode (quote-removal + $IFS + unquoted-glob patterns): **shipped Q3 W2**
- openclaw → toold call-chain audit: **shipped Q3 W2**
- @HackerNoon operational-governance framing: **cited in v1.0 spec**

The fix is in this doc. The audit log is public. **Audited, not perfect.** [Read the threat model →](THREAT_MODEL.md)
```

Replace the v121 "The protocol is the bet" section with the v22 expanded version that includes Anthropic-Samsung:

```markdown
## The protocol is the bet

Vinton Cerf said AI agents need TCP/IP. Anthropic shipped a closed-source version 2 days later. **Now Anthropic is co-developing a custom inference chip with Samsung.** Closed source. Closed weights. Closed silicon.

We shipped the protocol first — MIT-licensed, MCP-bridged, on a wearable that runs on a $349 laptop in Bengaluru. [Read the protocol →](PROTOCOL.md)
```

Add a v22 "From $725B to on-device" section between "The substrate is the bet" and "The threat model is public":

```markdown
## Observability > model

PagerDuty: agent model drift is the new outage. BNP Paribas: $725B AI infra spend in 2026. @HackerNoon: the month AI governance became operational. **The harness is the workbench, the model is the commodity.**

audiod's `segment_timing` histogram is the on-device observability surface. Every voice round-trip is timed. Every PTT press is logged. Every model call is traced. [Read the audiod SPEC →](Services/audiod/SPEC.md)
```

### Add a new file: `THREAT_MODEL.md`

Cite Mashable. Cite Adversa. List the flaws. Show the toold fix. Show the openclaw shell-call audit. Credit the auditors. Link to CVE filing flow. Reference HackerNoon's "month AI governance became operational" framing as the v24 validation.

### Add a new file: `PROTOCOL.md`

Cite Cerf, Anthropic Apps Gateway, Anthropic-Samsung, OpenClaw, MCP. Diagram the wire format. Show the MCP bridge. List the audit log surface. Include v24 cite: "Anthropic is co-developing a custom inference chip with Samsung. Closed silicon. The escape hatch is on-device + open-weights + auditable substrate."

---

## 2. `dani` (the agent platform)

### Current state
SOUL.md / SOM.md framing. v121 suggested a top-section rewrite. v122 adds the v24 threat model + Anthropic-Samsung cite.

### v122 deltas

Add the v22 threat model anchor to the top of the v121 "The threat model is public" section:

```markdown
## The threat model is public

@Mashable flagged a flaw. @AdversaAI disclosed bash-tricks bypass 10 of 11 open-source AI coding agents. We audited both. The toold strict-mode fix is shipped. The openclaw shell-call audit is shipped. The fix is public. The audit log is public. **Audited, not perfect.** [Read the threat model →](https://github.com/somdipto/dan-glasses/blob/main/THREAT_MODEL.md)
```

Add the v22 Anthropic-Samsung cite to the substrate section:

```markdown
## The substrate is the bet

Anthropic shipped a closed-source Apps Gateway. Anthropic is co-developing a custom inference chip with Samsung. **Closed source. Closed weights. Closed silicon.** We shipped the same protocol surface first — MIT, MCP-bridged, on a wearable, on a phone, on a laptop. [Read the protocol →](https://github.com/somdipto/dan-glasses/blob/main/PROTOCOL.md)
```

### Add / update: `SECURITY.md`

Standard SECURITY.md with: (a) the threat model reporting flow, (b) CVE filing path, (c) credit policy (we credit researchers, we don't sue them), (d) response time SLA (72h), (e) **v22 ADD: link to `THREAT_MODEL.md` at the top of the file.**

---

## 3. `danlab-multimodal` (the demo)

### Current state
README exists. v121 suggested a top-section rewrite. v122 does not need major changes — the demo is the demo, not the substrate. But:

### v122 deltas

Add a v22 "Honesty note" line to the top section:

```markdown
> **Heuristic feedback loop, not RL.** This is a pre-RL scaffold. No gradient. No reward model. The agent proposes a change. A heuristic scores it. The change is applied if the score improves. **The cheapest possible improvement loop, and it works.** This is the on-device thesis in action.
```

Add a v22 footer block:

```markdown
## The substrate is the bet (v22)

This demo runs on the same wire protocol as the Dan Glasses daemon stack. The protocol surface doc is at [github.com/somdipto/dan-glasses/blob/main/PROTOCOL.md](https://github.com/somdipto/dan-glasses/blob/main/PROTOCOL.md). The threat model doc is at [github.com/somdipto/dan-glasses/blob/main/THREAT_MODEL.md](https://github.com/somdipto/dan-glasses/blob/main/THREAT_MODEL.md).

**Audited, not perfect. Yours, not theirs.**

---

MIT · Built in Bengaluru · The substrate is auditable, not perfect.
```

---

## 4. `paperclip` (dormant but documented)

### Current state
Exists, dormant.

### v122 deltas

No major changes from v121. The dormant framing holds. Add a v22 footer:

```markdown
---

MIT · Built in Bengaluru · The substrate is auditable, not perfect.
```

---

## 5. ~~`blurr`~~ — RETIRED from this list

### Why retired

`blurr` in this workspace is **Panda** — the Android phone operator by Ayush Chaudhary, MIT-licensed. It is not the on-device eval harness the v121 README suggestions described. The v121 "blurr" section assumed an on-device eval harness for the substrate era. That repo does not exist in this workspace.

### v122 action

- **Do not** apply the v121 blurr README suggestions to the Panda repo. Panda has its own README and its own framing.
- **Do** flag the gap. If the lab wants an on-device eval harness, it should be a new repo. The v121 eval-harness framing can be revived when the repo exists.
- **Panda stays as a separate project.** Don't conflate.

### What v121 got wrong

The v121 README suggestions listed `blurr` as "the eval harness for on-device multimodal models." That framing is wrong for Panda. Panda is a phone operator. The eval harness framing belongs to a different project that does not yet exist in this workspace. v122 corrects this.

---

## 6. `danlab` org profile README

### Current state
v121 suggested a full body. v122 adds the v24 cites.

### v122 deltas to the v121 org profile

Replace the v121 "The threat model" section with:

```markdown
## The threat model is public (v22)

[Read the threat model →](https://github.com/somdipto/dan-glasses/blob/main/THREAT_MODEL.md)

@Mashable flagged a flaw. @AdversaAI disclosed bash-tricks bypass 10 of 11 open-source AI coding agents. We audited both. The toold strict-mode fix is shipped. The openclaw shell-call audit is shipped. The fix is public. The audit log is public. **Audited, not perfect.**

@HackerNoon named it: *"the month AI governance became operational."* The advantage is shifting from who builds the best model to who controls the conditions under which model capability is accessed, secured, and deployed. We are the audited-not-perfect path.
```

Replace the v121 "The thesis" section with:

```markdown
## The thesis

Vinton Cerf said AI agents need TCP/IP. Anthropic shipped a closed-source version 2 days later. Anthropic is co-developing a custom inference chip with Samsung. **Closed source. Closed weights. Closed silicon.**

We shipped the protocol first. MIT-licensed, MCP-bridged, on a wearable that runs on a $349 laptop in Bengaluru.

The substrate is the bet. The data path is yours. The threat model is public. The wearable ships it.
```

### Active projects list — v22 correction

Panda is NOT in the active projects list. The active projects are:

```markdown
## Active projects

- [dan-glasses](https://github.com/somdipto/dan-glasses) — open, on-device, agent-native AI in glasses form factor
- [dani](https://github.com/somdipto/dani) — the agent platform
- [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) — 120MB VLM demo
- [dani-skills](https://github.com/somdipto/dani-skills) — the skills registry
- [dan-consciousness](https://github.com/somdipto/dan-consciousness) — the brain

## Adjacent projects

- [Panda (blurr)](https://github.com/somdipto/blurr) — Android phone operator (separate project, MIT)
```

---

## 7. `dan-consciousness` (the brain)

### v122 deltas

No major changes from v121. Add a v22 footer:

```markdown
---

The substrate is auditable, not perfect. The threat model is at [github.com/somdipto/dan-glasses/blob/main/THREAT_MODEL.md](https://github.com/somdipto/dan-glasses/blob/main/THREAT_MODEL.md).
```

---

## 8. HuggingFace model card (LFM2.5-VL-450M)

### v122 deltas

Add a v22 "Why on-device" line to the model card:

```markdown
## Why on-device

This model is the same architecture class as the 4B Gemma 3 NASA put in orbit. It runs on a laptop. No cloud. No Anthropic-Samsung chip dependency. **The escape hatch is open-weights + on-device + auditable substrate.**

The Dan Glasses daemon stack uses this model via `perceptiond`. The threat model for the daemon stack is at [github.com/somdipto/dan-glasses/blob/main/THREAT_MODEL.md](https://github.com/somdipto/dan-glasses/blob/main/THREAT_MODEL.md).
```

Add a v22 footer:

```markdown
---

MIT · Built in Bengaluru · The substrate is auditable, not perfect.
```

---

## 9. The cross-README checklist (v22)

- [ ] One-liner in the first 200 chars
- [ ] `.deb` or install one-liner in the first 500 chars (where applicable)
- [ ] Daemon map / receipts (not adjectives) in the first 500 chars
- [ ] "The substrate is the bet" link to PROTOCOL.md (with v22 Anthropic-Samsung cite)
- [ ] "The threat model is public" link to THREAT_MODEL.md (with v22 Adversa + HackerNoon cites)
- [ ] "The 4 pillars" block (protocol → observability → on-device → small-beats-large)
- [ ] v22 ADD: "The 2 v24 pillars" (threat-model-is-public, yours-not-theirs)
- [ ] v22 ADD: "Audited, not perfect" replaces "secure" everywhere
- [ ] `SECURITY.md` with threat model reporting flow, linking `THREAT_MODEL.md`
- [ ] License + provenance footer: `MIT · Built in Bengaluru · The substrate is auditable, not perfect.`
- [ ] Topics tags: `on-device`, `agent-native`, `mcp`, `substrate`, `open-source`, `edge-ai`, `audited-not-perfect`
- [ ] Pinned to: danlab.dev, dan-consciousness, danlab-multimodal-demo
- [ ] v22 ADD: no `blurr`/`Panda` framing as "on-device eval harness" — that's a different project

---

## 10. The single rule

**Every README should make a developer want to `apt install dan-glasses-daemons` or a researcher want to read the SIA-W+H paper. If it doesn't, cut it.**

---

*v121 had 8 sections + blurr. v122 has 8 sections minus blurr + 1 correction note. Same 4 pillars + 2 v24 pillars. Same lead. Less is more.*
