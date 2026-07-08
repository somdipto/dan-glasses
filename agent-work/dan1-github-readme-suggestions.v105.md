# Dan1 GitHub README Suggestions — v105

**Author:** Dan1 👾
**Status:** Supersedes v104
**Audience:** Maintainers of all Danlab public-facing repos

---

## Goal

Every README on the Danlab org should signal the same five things:

1. **What this is**
2. **What it does today**
3. **What it doesn’t do yet**
4. **How to verify it**
5. **Why it matters**

Keep it tight. Cut anything that is fluff.

---

## Universal README skeleton (v105)

```markdown
# <project-name>

<one-line description: what it does and why it exists>

## Status
- ✅ live: <version + date>
- ✅ tests: <N>/<N>
- 🛠️ known issues: <link to Monday Transparency>

## What it does
<3-5 bullets>

## What it doesn't do
<honest list>

## How to verify
<the minimal curl command or test invocation>

## Why it matters
<one short paragraph tying the project to the auditable on-device wedge>

## License
MIT

## Maintainers
@dan1 @<project-lead>
```

---

## Per-repo suggestions

### dan-glasses (umbrella repo)

- Replace the current intro with a one-liner: "The auditable on-device AI companion stack."
- Add a single `curl` command in the README header.
- Add a `## Receipts` section that links to the live status page and the Monday Transparency archive.
- Cut the long architecture description. Link to the architecture doc instead.

### dan-glasses-app

- Lead with: "Tauri v2 React frontend for the Dan Glasses stack."
- Document the four daemon calls in a single table: audiod, perceptiond, memoryd, ttsd.
- Replace the "Quick Start" placeholder with the actual smoke test command.

### Services/audiod

- Lead with the spec sheet, not prose. Spec is the source of truth.
- Keep `## Failure modes` as the second section after status.

### Services/perceptiond

- Lead with the live `/status` snapshot.
- Add a one-line note about the watchful vs active gating.
- Document the mock-capture fallback explicitly.

### Services/memoryd

- Lead with the `MEMORYD_DB` env var. This is the bug disclosed in Monday Transparency #1.
- Note the on-disk repo DB is shadow unless the env var is set.

### Services/toold, Services/os-toold

- Lean on the sandbox model. State the workdir in the README.

### Services/ttsd

- Document the model swap path (KittenTTS → Kokoro-82M by Jul 15).

### paperclip

- Lead with the DanClaw framing ("If OpenClaw is the employee, DanClaw is the company").
- Keep the Docker and Railway quick start at the top.
- Add a status badge linking to the live instance (if available).

### danlab-multimodal

- Lead with the model name: SmolVLM-256M.
- Add a clear statement: heuristic loop, not RL.
- Link to the v2 upgrade path (SIA framework).

### blurr

- Lean on the local-first framing.
- State the data locality invariant: no outbound network for retrieval.

---

## Per-project README improvements checklist

For every repo, verify:

- [ ] Status block at the top: live or not.
- [ ] One-line description.
- [ ] 3–5 bullets on what it does.
- [ ] Honest "what it doesn't do" section.
- [ ] A command that verifies it works in under 60 seconds.
- [ ] License (MIT).
- [ ] Maintainers listed.
- [ ] No marketing fluff.

---

## Voice and tone guidance

- Direct.
- Technical.
- Honest about what is shipped and what is not.
- No emojis in headings. Emojis in lists are fine.
- No "revolutionary" / "game-changing" / "10x" language.

---

## v105 specific additions

- Add a `## Monday Transparency` link to every repo that touches the live stack.
- Add a `## Known issues` section to memoryd, perceptiond, and audiod (the daemons with published receipts).
- For memoryd, add a one-liner: "This service restarts on host process restart with a fresh SQLite DB unless `MEMORYD_DB` is set."

---

## v103 no-covert-updates clause (preserved as law)

> Every change to a public-facing README must be visible in git history. No silent edits. No "polish" without a commit message that says what was changed and why.

If a marketing change is needed, ship it as its own PR with a one-line rationale.

---

## Verification pattern for any README claim

If the README says "live," there must be a CI check or a curl-able endpoint that proves it.

If the README says "X tests," there must be a way to run them locally.

If the README says "auditable," there must be a link to the spec or the source that backs the claim.

*v105 README suggestions.*