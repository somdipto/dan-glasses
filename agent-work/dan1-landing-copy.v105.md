# Dan Glasses Landing Copy — v105

**Author:** Dan1 👾
**Status:** Supersedes v104
**Purpose:** Homepage / landing page copy for `danlab.dev` / `/glasses`

---

## Hero

# The only open-source reference implementation of the 3rd LLM UI paradigm.

Dan Glasses is an on-device AI companion that sees what you see, hears what you say, remembers what matters, and speaks back only when it has something useful to add.

Built from India. Designed to run anywhere.

**8 daemons. 144 tests. 0 cloud. MIT forever.**

[Reproduce in 5 minutes](/install)  [Read the paper](/arxiv)  [See the receipts](/status)

---

## What this is

Not a notification mirror.
Not a camera with a speaker.
Not a cloud assistant with a wearable shell.

Dan Glasses is:
- **persistent** — context survives sessions
- **auditable** — every layer is inspectable
- **on-device** — your memory stays on your device
- **open-source** — the stack is shipped in the open
- **proactive** — it speaks when there is signal

Karpathy described the new UI paradigm as a self-contained, persistent, asynchronous entity with org-wide tools and context. Danlab is building that reference implementation in public.

---

## What it does

### 1. It hears
`audiod` turns microphone input into structured transcript events.

### 2. It sees
`perceptiond` captures camera frames, filters for salience, and runs vision inference only when it matters.

### 3. It remembers
`memoryd` stores episodic, semantic, and procedural memory locally in SQLite + vectors.

### 4. It speaks
`ttsd` turns responses into speech with low-latency local synthesis.

### 5. It acts
`OpenClaw` orchestrates the system, routes tools, and keeps the whole stack coherent.

---

## Why it’s different

| Dan Glasses | Typical smart glasses |
|---|---|
| proactive AI companion | notification relay |
| local memory | cloud memory |
| auditable stack | black box app |
| open-source | closed hardware lock-in |
| on-device first | cloud first |
| built in public | shipped as marketing |

Your agent’s memory lives on your device, not in a cloud database.

---

## The workflow

1. Wear it or run it on a laptop.
2. Say something.
3. Ask what you want to know.
4. Get an answer that uses your current context.
5. Keep going without re-explaining everything.

The point is not that it sounds futuristic. The point is that it compounds context over time.

---

## The receipts

- 8/8 daemons live
- 144/144 tests passing
- Monday Transparency every week
- Memory bug disclosed publicly
- Spec patches and corrections tracked
- No hidden cloud dependency

---

## Comparison

### Meta / Ray-Ban / consumer AI glasses
Great at shipping a polished product. Not designed around local memory or open verification.

### Google / Android XR
Platform strength, but still platform logic: ecosystem first, user custody second.

### Apple
Hardware quality is real. Shipping speed is not the lane right now.

### Dan Glasses
Open, local, auditable, persistent.

---

## CTA

**Install the stack. Inspect the state. Decide for yourself.**

[Install now](/install)  [GitHub](/github)  [Live status](/status)

---

## FAQ

### Is this a desktop app or actual glasses?
Both. The software runs today on a Linux laptop. The wearable form factor is the next body.

### Is the memory really on-device?
Yes. SQLite + vectors. No cloud dependency for core memory.

### Is this reactive or proactive?
Proactive. It should speak when there is signal, not chatter all day.

### Is it open-source?
Yes. That is not a side note. It is the thesis.

### Why build this from India?
Because the constraint forces honesty. And because the global market is ready for software that does not depend on a closed American cloud stack.

*v105 landing copy.*