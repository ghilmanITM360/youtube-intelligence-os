# 05 Cross-video script synthesis (D4): xkcd What If?, 83 transcripts

Status: **self-review**. No independent reviewer. Source = repo `research/what-if-scripts/` (83 audits, `matrix.jsonl`, `inventory.json`) plus this audit's recomputation (`scripts/phase5_corpus.py`, `05_*.csv`). The 83 are the transcripts the catalog holds, **not the channel count** (channel = 91 in census, 92 with Aony69nO5kI).

## 0. Verification of the 83 audits (done before synthesis)

| Check | Result |
|---|---|
| `locate.py check` (every ¶N and wA-B cited in 83 audits exists) | **ok** |
| `inventory.json` / `matrix.jsonl` / `coverage_ledger.json` | 83 / 83 / 83, same VID set, IDs agree, 83 audits DONE, 0 missing files |
| Word counts: my whitespace count vs inventory | **83 of 83 equal** |
| Core headings present in all 83 audits | A, B, D, E, H, J, K and the framework check. C, F, G, I, L vary in title or are absent in 2–43 files (heading drift, not missing content: the long audits use "Opening beats", Shorts "Opening beats (Short)", etc.) |
| Families | recomputed **45** (8-gram containment >= 0.30, union of Short to long parent): 43 long roots, 38 derived Shorts in 28 families with a long, 2 independent Shorts (V065, V080). Reproduces the repo's "about 45". |
| Derived Shorts | containment of Short in best parent: median 0.895, min 0.54, max 1.0. Parent with most Shorts: V023 (4). 15 of 43 long videos have no Short. |

Limit: I verified structure and counts, **not** each audit's prose judgments. Those remain the prior audit's self-review plus mine.

## 1. Corpus facts (MEASURED, recomputed)

| Metric | Long (n=43) | Short (n=40) |
|---|---|---|
| Words, median (range) | **680** (569 to 1,414) | 282 (79 to 492) |
| Duration, median (range) | **3:16** (2:39 to 6:47) | 1:15 (0:21 to 2:12) |
| Words per second, median | 3.59 | 3.77 |
| Paragraphs, median | 25 (some auto-captions are 1 block) | n/a |
| Question marks, median | 2 | n/a |
| Numerals per 100 words, median | 2.4 | n/a |
| Second person ("you") per 100 words, median | 1.0 | n/a |

Opening by audit (manual, authoritative): attributed viewer question in **41 of 43** long videos (exceptions V019, V024); only **4 of 40** Shorts keep such a line (V056, V058, V062, V076). A loose regex gives 42/43 (counts V019's "comes from me") and flags V040 among Shorts; the audit's manual judgement stands.

**Derivation:** 38 of 40 Shorts add no substantive new content: they are contiguous excerpts or abridgements of a long script. This is the channel's real production model: **a long script is written once, then cut at structural seams into Shorts**. For a new channel this is a *script architecture* requirement (design each long script with seams), not just a distribution habit.

## 2. What recurs (OBSERVED in the audits; counts are keyword-tagged on `matrix.structure`, approximate)

| Pattern | Long videos | Note |
|---|---|---|
| Attributed question, then a **reframe in beat 2** (misconception fix, answer-first with withheld mechanism, deflation, flash-forward) | 41 | every audited long, 10 of 10 in batch 1 |
| Ladder or escalation spine (scale, time, constraint, cost) | ~13 | most common spine |
| Frame or idiom spine (proverb, literal idiom) | ~6 | |
| Consequence cascade (by timescale, region, depth) | ~5 | |
| Feasibility audit / limits list | ~4 | |
| Anticlimax or deflection first | ~4 | |
| Elimination tournament | ~2 | |
| **No CTA** | 38 of 43 | one book promo (V019), one playful real-world action (V020); no subscribe, Patreon, sponsor wording anywhere |
| Dry-humour and absurd-bureaucracy beats | recurring | comic frame is often dropped in the Short cut, the physics chain is kept |
| Serial callbacks | V014, V018, V019, V063, V080 | small; a "channel is a universe" signal, not a rule |

Endings are almost always a **button** (reframe, deadpan advice, aphorism, callback, P.S.), never a summary and never a CTA (audits' ending-type lists, V001 to V083).

## 3. Conflicts and confounds (the part the playbook must not ignore)

1. **Era confound.** Long-video views at the 2026-11-04 snapshot fall with upload date (Spearman rho -0.72). Older videos are also longer (median words 695 in 2023, **849 in 2024**, 635 in 2025, 632 in 2026). Raw "longer = more views" (rho +0.61 for words, +0.66 for duration) is therefore partly age.
2. **Within-year check.** Controlling by year, words vs views is still positive: **2024 rho +0.56 (n=17), 2025 rho +0.62 (n=14)**; duration vs views +0.56 and +0.69. Correlational, n small, topic not controlled, no retention data. Question marks, numerals and "you" density show **no** relationship (|rho| <= 0.11).
3. **Tension with the strategy.** `03`/`05` and the Day 1 and Day 3 cuts reasoned toward matching xkcd's *median* length (680 words, 3:16). The data above says the **median** is not the performance-winning region: 2024 longs ran about 850 words and drew the highest median views. This does not prove that length drives views, but it **removes length-cutting as an evidence-backed priority**. It remains an owner production choice. Status: **INFERRED conflict, not CONTRADICTED**; flagged for the owner at the next strategy edit.
4. **Rules for Shorts and long are different objects.** 38 Shorts are cuts. Any "Short hook" statistic is a statistic about a *cut point*, not a written hook. Per-video counts over 83 double-count about 45 content families.
5. **Abridgement can break logic** (V037 loses a step, V038's figures contradict, V041 "too slow" unquantified, V076 cut reversal). A Short-from-long workflow needs a logic check, not just a clean seam.

## 4. Things the 83 scripts cannot tell us (UNAVAILABLE here)

- Retention, CTR, watch time: none. Every audience effect is speculative.
- Timing inside the video: transcripts have no timestamps. "First 30 seconds" is opening beats only. The campaign's per-video frame tables supply timing for 64 videos (Phase 5b below).
- On-screen payoffs (maps, "this many", diagrams) that the text assumes.
- Fact accuracy of the scripts' science (arithmetic consistency only).
- Thumbnails.

## 5. Where the three layers agree and where they do not

See `06_LAYER_RECONCILIATION.md` (visual layers) and `01_STRATEGY_GAPS_AND_CONFLICTS.md` (G3).
