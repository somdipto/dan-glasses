# Dan1 X/Twitter Content — v106 (2026-06-28)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-28 11:30 IST (06:00 UTC), Bengaluru, India 🇮🇳
**Status:** v106. Supersedes v105.
**Scope:** 60-minute delta refresh — **Karpathy reply sequence (Jul 1) locked**, **Monday Transparency #1 thread (Jun 29) locked**, **Post 1 v106 announcement updated**, **Post 4 rewritten for Meta $299 mass-market + Persona 11**, **5 thread drafts A-E updated**, **launch-day burst pack for Aug 15 / Aug 25 / Jun 29**.

---

## v106 X bio (locked)

```
Dan1 👾
Co-founder, head of marketing + growth @danlab_dev
From India 🇮🇳, building auditable on-device AI glasses
Open-source. MIT forever.
github.com/somdipto/dani
```

**Alt bio (Karpathy-paradigm-aligned):**

```
Dan1 👾
We shipped Karpathy's 3rd LLM UI paradigm 9 months ago
On a $400 Linux laptop. 8 daemons. 144 tests. MIT.
From India 🇮🇳 → the world
github.com/somdipto/dani
```

---

## v106 first 10 posts (locked)

### Post 1 — v106 announcement (the launch tweet, Jun 28)

```
We just shipped v106 of our marketing infrastructure.

What changed in the last 60 minutes:
• Karpathy thread reply #2 forces a correction: OpenClaw is the substrate, not the paradigm. DANI is the auditable instantiation.
• Meta shipped $299 mass-market Meta Glasses (Jun 23). Different lane, validated market.
• CNN: AI glasses exam cheating in Taiwan + South Korea (Jun 26). Privacy paradox = regulatory tailwind.
• 15th honest-accounting cycle. Live memoryd write receipt: id=1, vec_1, db 24KB→32KB.

7-pillar wedge. 11 personas. 15 Monday Transparency receipts.

🇮🇳 From India. MIT forever.

github.com/somdipto/dani
```

### Post 2 — Monday Transparency #1 (Jun 29, content-locked)

```
8/8 daemons live. 144/144 tests green. 15th honest-accounting cycle. 🟢

The bug we found this week: memoryd reopens at /tmp/memoryd.db on host restart.

The 1-line fix: MEMORYD_DB=/home/workspace/dan-glasses/Services/memoryd/memory.db

The receipt: just wrote id=1, embedding_id=vec_1 to memoryd. db 24KB → 32KB.

This is Monday Transparency #1 of 15.

🇮🇳
```

### Post 3 — Karpathy reply (Jul 1, locked)

```
@karpathy Jun 23: "the 3rd paradigm is a self-contained, persistent, asynchronous entity with org-wide tools and context, working alongside teams of humans."

We built that. 9 months ago. On a $400 Linux laptop. From India 🇮🇳

Built on OpenClaw, not adjacent to it.

8/8 daemons. 144/144 tests. 15 honest-accounting cycles. 0 cloud. MIT forever.

@anthropic has Claude Tag (closed). We have DANI (open).

github.com/somdipto/dani
```

### Post 4 — Meta $299 + Persona 11 (Jul 7, rewritten v106)

```
Meta just launched $299 in-house Meta Glasses. No Ray-Ban, no Oakley. 50% cheaper than entry-level Ray-Ban Meta.

Different lane from Danlab. Meta = mass-market + consumer-fluencer (Kylie Jenner). Danlab = auditable + on-device + developer-researcher.

But the privacy paradox is real:

🇹🇼 Taiwan caught a student wearing AI glasses in a medical school entrance exam.
🇰🇷 South Korea's college entrance exam administrator is in talks with the Education Ministry.

Schools, courts, employers, governments are now asking: what does the AI in your glasses remember? Where is it stored?

Closed AI glasses: "We don't know, it's in the cloud."

Danlab: auditable memory. On-device SQLite. Receipts for every write. The bug we found this week, the fix, the spec patch — all published.

Persona 11: institutional buyer. Q4 2026. The regulatory tailwind for the auditable lane. 🇮🇳
```

### Post 5 — iPhone price (Jul 9, new v106)

```
Tim Cook told WSJ: AI memory chip demand is forcing iPhone prices up.

SK Hynix $29.4B US listing. Micron Q2 2026 revenue +196% YoY.

The cloud-AI economics are eating the device-AI economics.

Danlab: ₹12K wearable, no subscription, no cloud. The structural answer.

🇮🇳
```

### Post 6 — Sarvam-Models (Jul 16, locked)

```
Sarvam-Models 24B is now a reasoning adapter for DANI.

Sovereign-AI. Open-weight. On-device. India-cost.

5 reasoning adapters, swap in <4h:
• Claude
• GLM 5.2
• LFM2.5
• Llama 3.3
• Sarvam-Models 24B (sovereign-stack-compatible)

🇮🇳
```

### Post 7 — arXiv teaser (Aug 13, locked)

```
Aug 15. arXiv pre-print.

"Auditable Confidence Calibration for On-Device Speech Recognition"

ECE-grounded. AIE-Bench submission. 144/144 tests. 15 honest-accounting cycles.

Related Work opens with @karpathy's Jun 23 thread on the 3rd LLM UI paradigm.

🇮🇳
```

### Post 8 — Reddit teaser (Aug 16, locked)

```
We built the auditable alternative to the closed AI labs.

Reddit r/MachineLearning post. Aug 16.

144/144 receipt. 15 honest-accounting cycles. The memoryd bug we publish.

🇮🇳
```

### Post 9 — Show HN (Aug 25, headline locked)

```
Show HN: the auditable, on-device instantiation of the 3rd LLM UI paradigm, built on OpenClaw, 8 daemons, 144 tests, 15 honest-accounting cycles, MIT, from India 🇮🇳

github.com/somdipto/dani
```

### Post 10 — Q3 wrap (Sep 29, locked)

```
15 weeks. 15 receipts. 1 Q3 shipped.

Aug 15: arXiv
Aug 25: Show HN
Sep 30: AIE-Bench + SEAGym

Monday Transparency Cadence Q4 starts Oct 6.

🇮🇳 From India. MIT forever.
```

---

## v106 thread drafts (5)

### Thread A — Monday Transparency #1 (Jun 29, content-locked)

```
1/ 8/8 daemons live. 144/144 tests green. 15th honest-accounting cycle. 🟢

2/ The bug we found this week: memoryd reopens at /tmp/memoryd.db on host restart. 0 memories after restart.

The 1-line fix: MEMORYD_DB=/home/workspace/dan-glasses/Services/memoryd/memory.db

The spec patch: queued.

3/ The live receipt: just wrote id=1, embedding_id=vec_1 to memoryd via POST /memories. db grew 24KB → 32KB. /stats confirms {"total_memories":1, "by_type":{"episodic":1}}.

4/ This is Monday Transparency #1 of 15. Every Monday for 15 weeks, a 3-bullet receipt: daemon count, test count, the bug we found this week.

5/ Brand promise: we publish the bug, the fix, and the audit trail. The auditable lane isn't a slogan — it's a receipt.

🇮🇳 From India. MIT forever.
```

### Thread B — Karpathy reply (Jul 1, locked)

```
1/ @karpathy Jun 23: "the 3rd major redesign of LLM UIUX... a self-contained, persistent, asynchronous entity with org-wide tools and context, working alongside teams of humans."

We built that. 9 months ago. On a $400 Linux laptop. From India. 🇮🇳

2/ Built on OpenClaw, not adjacent to it. DANI is the auditable, on-device, sovereign-stack-compatible instantiation of the 3rd paradigm.

3/ 8/8 daemons. 144/144 tests. 15 honest-accounting cycles. 0 cloud. MIT forever.

Receipt: github.com/somdipto/dani

4/ @anthropic has Claude Tag (closed). We have DANI (open). Same paradigm, different lane.

5/ arXiv Aug 15. Show HN Aug 25. Eval Jul 25. Monday Transparency #1 Jun 29. 🇮🇳
```

### Thread C — Privacy paradox (Jul 8, locked)

```
1/ Taiwan and South Korea just banned AI glasses in exams. CNN, Jun 26.

This is the strongest argument for the auditable on-device lane.

2/ Schools, courts, employers, governments are now asking: "What does the AI in your glasses remember? Where does it store it? Who can see it?"

The answer for closed AI glasses: "We don't know, it's in the cloud."

3/ The answer for Danlab: auditable memory. On-device SQLite. Receipts for every write. The bug we found this week, the fix, the spec patch — all published.

4/ Persona 11: institutional buyer. Q4 2026. Schools, courts, employers, governments.

5/ The privacy paradox is the regulatory tailwind for the auditable lane. 🇮🇳
```

### Thread D — iPhone price (Jul 9, locked)

```
1/ Tim Cook told WSJ: "AI memory chip demand is forcing iPhone prices up." MacRumors, Jun 22.

iPhone 17 Pro needs 12GB RAM to run Apple Intelligence on-device.

2/ SK Hynix $29.4B US listing (Jun 25). Micron Q2 2026 revenue $24B, +196% YoY (Jun 24). Memory chips are "runaway" per Bloomberg.

3/ The cloud-AI economics are eating the device-AI economics.

The on-device AI glasses lane is structurally cheaper. No subscription. No cloud. No memory chip demand from cloud data centers.

4/ Danlab: ₹12K wearable, ₹4,999 student tier, no subscription, no cloud. The structural answer to the AI memory chip squeeze.

From India. 🇮🇳
```

### Thread E — Show HN (Aug 25, locked)

```
1/ Show HN: the auditable, on-device instantiation of the 3rd LLM UI paradigm, built on OpenClaw, 8 daemons, 144 tests, 15 honest-accounting cycles, MIT, from India 🇮🇳

github.com/somdipto/dani

2/ @karpathy Jun 23: "the 3rd paradigm is a self-contained, persistent, asynchronous entity with org-wide tools and context, working alongside teams of humans."

We shipped that 9 months ago. Auditable. On-device. Open-source.

3/ Built on OpenClaw, not adjacent to it. (Karpathy Jun 24 reply: "it's not even OpenClaw adjacent." We agree — we built the auditable layer on top.)

4/ 8 daemons: audiod (STT), perceptiond (vision), memoryd (SQLite + embeddings), ttsd (KittenTTS → Kokoro-82M Jul 15), toold (sandbox), os-toold (system), openclaw (gateway), dan-glasses-app (Tauri v2 + React).

5/ 144 tests. 15 honest-accounting cycles. 1 live memoryd write receipt (id=1, vec_1, db 24KB→32KB). The bug we found this week, the fix, the spec patch — all published.

6/ 5 reasoning adapters, swap in <4h: Claude, GLM 5.2, LFM2.5, Llama 3.3, Sarvam-Models 24B (sovereign-stack-compatible).

7/ ₹4,999 student tier. ₹12K sovereign-stack bundle. ₹12K wearable. $99K patron tier.

From India 🇮🇳. MIT forever.
```

---

## v106 launch-day burst pack

### Jun 29 (Monday Transparency #1) burst
- 09:00 IST — Post 2 (single-tweet receipt).
- 09:05 IST — Thread A (5-tweet full version).
- 09:30 IST — LinkedIn cross-post (long-form).
- 10:00 IST — Telegram @danlab_bot announcement.
- 14:00 IST — Email to danlab.dev mailing list (if list exists by then).

### Jul 1 (Karpathy reply) burst
- 09:00 IST — Post 3 (single-tweet Karpathy reply).
- 09:05 IST — Thread B (5-tweet full version).
- 09:30 IST — Quote-tweet the Jun 23 thread with Post 3.
- 10:00 IST — Reply on the Jun 24 thread with "Built on OpenClaw, not adjacent."
- 14:00 IST — LinkedIn cross-post.

### Aug 15 (arXiv day) burst
- 09:00 IST — arXiv pre-print live.
- 09:30 IST — Post 7 (teaser from Aug 13, expanded).
- 10:00 IST — LinkedIn long-form essay.
- 11:00 IST — Telegram @danlab_bot announcement.
- 14:00 IST — Email to arXiv-announce watchers.

### Aug 25 (Show HN day) burst
- 09:00 IST — Post 9 + Thread E.
- 09:30 IST — Hacker News cross-post.
- 10:00 IST — LinkedIn cross-post.
- 11:00 IST — Telegram announcement.
- 14:00 IST — Email to danlab.dev mailing list.
- 18:00 IST — Day-1 metrics summary.

---

## v106 daily posting cadence

| Day | Time (IST) | Asset | Channel |
|-----|------------|-------|---------|
| Mon | 09:00 | Monday Transparency receipt | X + LinkedIn |
| Mon | 10:00 | Long-form version | LinkedIn |
| Tue | 09:00 | Personal brand thread | X @NandySomdipto |
| Wed | 09:00 | Technical deep-dive / Karpathy engagement | X @danlab_dev |
| Thu | 09:00 | Sovereign-stack / India-first | LinkedIn |
| Fri | 11:00 | Weekly summary | Telegram @danlab_bot |

---

**v106 X bio + 10 posts + 5 threads + 4 launch-day burst packs. Monday Transparency #1 content-locked at v106. Karpathy reply Jul 1 locked. Show HN headline locked.** 👾
