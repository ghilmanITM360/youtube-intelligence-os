# Better Health While Aging (DS-000033) — Individual Channel Dossier

**Channel:** Better Health While Aging (`@BetterHealthWhileAging`, `UCFpxvukIqCAUA7YizI-q9Dw`)
**Status date:** 2026-09-26
**Data basis:** 98/98 videos, 98/98 real transcripts, 0 placeholders (94-video initial acquisition, run `AuZ65QkXBmVIXcOn9`, 2026-09-25, + 4-video Priority A Shorts backfill, run `Ll3gKxE3dXEeG4SDd`, 2026-09-26). Source: `youtube_channel_registry.db` / `youtube_inventory.db`, dataset `DS-000033`.
**Purpose:** Phase 6 individual-channel research artifact for this competitor, requested separately from the combined V3 cross-channel synthesis. Extends the existing V3 corpus rather than duplicating it — breakout-event analysis for this channel already exists in `SMALL-CHANNEL-BREAKOUT-FORENSICS.md` (Case 13) and is referenced, not re-derived, below.

**Scope disclosure (metadata completeness vs. forensic-analysis completeness are tracked separately):**
- Metadata completeness: **COMPLETE** — 98/98 videos, 98/98 real YouTube-caption transcripts, 0 explicit no-subtitle gaps, thumbnail URLs present for 97/98 (1 missing per registry ledger), all public metadata fields populated.
- Forensic-analysis completeness this pass: **PARTIAL**. Covered: full population profiling, title-by-title pattern analysis (quantitative, all 98 videos), breakout-vs-baseline comparison, format (regular vs. Shorts) performance split, pointer to existing breakout-event case file. **Not covered this pass**: thumbnail-by-thumbnail visual inspection (no forensic video/thumbnail evidence is registered for this channel — `forensic_video_status = NOT_AVAILABLE`, `visual_asset_status` is URL-only; per AGENTS.md this must stay `NOT_AVAILABLE` rather than be inferred from titles), full manual script-by-script reading of all 98 transcripts beyond the 9 breakout events already read in Case 13, and DS-000011/018/031 knowledge-framework cross-referencing beyond what Case 13 already applied.

---

## 1. Population

| Metric | Value |
|---|---|
| Total videos | 98 (80 regular, 18 Shorts, 0 archived streams) |
| Total views (captured videos) | 13,865,335 |
| Mean views/video | 141,483 |
| Median views/video | 19,346 |
| Std. dev. | 412,107 (heavily right-skewed — a small number of large outliers) |
| Max / min views | 3,582,804 / 1,018 |
| Real transcripts | 98/98 (0 placeholders) |
| Regular-video median views | 28,688 |
| Shorts median views | 3,153 |

**Observation (descriptive, not causal):** on this channel, long-form regular videos substantially outperform Shorts by view count (median ~9x higher). This is a single-channel observation, not yet tested against a matched-format control across the competitor cohort; it should not be generalized without that cross-channel check (Phase 7 work).

## 2. Title-by-title pattern analysis (quantitative, all 98 videos)

Computed directly from the registered title text and view counts (`/tmp/bhwa_videos.csv` derived from `video_snapshots`, not re-typed by hand):

| Title feature | n with feature | Median views (feature) | n without | Median views (no feature) |
|---|---|---|---|---|
| Contains a digit/number | 36 | 11,428 | 62 | 24,328 |
| Contains a question mark | 15 | 25,925 | 83 | 16,880 |
| Warning/avoid-type word (*warning, avoid, never, stop, danger, risk, drugs*) | 5 | 25,925 | 93 | 17,617 |

**Reading these numbers honestly:** number-in-title titles perform *worse* than the median here (opposite of a common assumption), but the sample sizes for the question-mark and warning-word groups (15 and 5) are small enough that this is a descriptive pattern within one channel, not a statistically established effect. It is reported as observed data, not as a recommendation.

### Top 15 performers (>5x channel median views — descriptive breakout threshold, consistent with the methodology already used in `SMALL-CHANNEL-BREAKOUT-FORENSICS.md`)

| Views | Format | Title |
|---|---|---|
| 3,582,804 | video | Improve Memory by AVOIDING These Drugs ⛔ |
| 1,294,247 | video | Vitamin B12 Deficiency in Aging: Causes, Symptoms and Treatment |
| 980,106 | video | 10 Causes of Memory Loss in Aging |
| 953,110 | video | Memory Improvement: Say No to These Medications |
| 664,860 | video | Tylenol, Advil, or Aspirin? What's Safest for Older Adults |
| 607,506 | video | 10 Warning Signs of Early Alzheimer's Disease – HOP ML Podcast |
| 429,529 | video | 😱 PARANOIA or Memory Loss. Signs That Could be Early Alzheimer's |
| 329,571 | video | Is Your Blood Pressure Too Low? Understanding Hypotension |
| 325,492 | video | Dehydration in Older Adults: Symptoms, Treatment, & Prevention |
| 322,073 | video | MCI, Alzheimer's and Dementia. What's the Difference? – HOP ML Podcast |
| 315,176 | video | Can Exercise Reverse Aging? How to Exercise to Age Well |
| 308,978 | video | Methylcobalamin vs Cyanocobalamin: Which Vitamin B12 is Best? |
| 301,468 | video | Constipation After 60: Causes, Relief & Safe Treatments |
| 275,536 | video | The Surprising Risks of Too Much Vitamin D for Seniors |
| 269,514 | video | Turning 65 Soon? How to Get Started with Medicare |

25 of 98 videos (26%) clear the >5x-median breakout threshold — all are regular videos, none are Shorts. 9 of these 25 are the events already deep-dived in `SMALL-CHANNEL-BREAKOUT-FORENSICS.md` Case 13 (script openings, matched-failure comparisons, local-baseline multiples); the remaining 16 breakout titles above are newly surfaced by this population-level pass and have **not yet** had script-level breakout investigation — flagged as outstanding, not silently folded into Case 13's existing 9-event claim.

### Bottom 10 performers

| Views | Format | Title |
|---|---|---|
| 1,018 | video | COVID Update for Aging Adults: Omicron BA.2 & More |
| 1,384 | video | 2022 FLU Vaccine Update for Older Adults & Families: Which Flu Vaccine to Get & Why |
| 1,403 | shorts | How To Talk To An Older Adult About Their Driving |
| 1,501 | shorts | Treating Symptoms of Atrial Fibrillation |
| 1,562 | shorts | Overview of Treatment for Atrial Fibrillation |
| 1,722 | video | 1.6.22 COVID Omicron Update for Aging Adults |
| 1,840 | shorts | What is Atrial Fibrillation? |
| 2,024 | shorts | All About IADLs #shorts – Better Health While Aging |
| 2,282 | video | COVID September 2022: COVID Fall Booster Update for Older Adults & Families |
| 2,298 | shorts | Special Exercises for Frailty, Alzheimer's & Dementia |

**Pattern (descriptive):** 4 of the bottom 10 are time-sensitive news-cycle content (COVID/flu updates) that has plainly decayed since publication — a topic-durability signal, not a title-wording signal. The other 6 of the bottom 10 are Shorts, consistent with §1's format gap. No single wording pattern distinguishes the bottom 10 from the median; low performance here correlates more with topic durability and format than with title phrasing.

## 3. Thumbnails

`visual_asset_status = THUMBNAIL_URL_ONLY` for this channel (confirmed via registry). Thumbnail URLs are captured for 97/98 videos but **no thumbnail image has been visually inspected or registered as forensic evidence** — per AGENTS.md Core Rule 4/6, this stays reported as `NOT_AVAILABLE` for forensic purposes rather than inferring visual patterns (e.g., "answer-withholding thumbnails") from title text alone. The cross-channel thumbnail pattern findings in `SENIOR-HEALTH-FORENSIC-REPORT-V3.md` were derived from channels with genuine forensic video/thumbnail evidence (CH-000004) and do not automatically transfer to this channel without its own registered visual evidence.

## 4. Script/transcript evidence

98/98 real transcripts available (77 user-generated, 21 auto-generated captions across the combined 98-video set — verified via `SELECT caption_type, COUNT(*) FROM transcripts ... GROUP BY caption_type`; no paid AI transcription used in either run). Deep script-level reading (openings, hooks, reveals, structure) has been done for the 9 Case-13 breakout events in `SMALL-CHANNEL-BREAKOUT-FORENSICS.md`, including matched-failure comparisons for 7 of the 9 topics. The remaining 89 transcripts have not had the same manual script-structure reading — this is the largest concrete gap toward full Phase 6 depth for this channel and would be the next unit of work if continued.

## 5. Breakout investigation

Already completed and not re-derived here: see `SMALL-CHANNEL-BREAKOUT-FORENSICS.md`, **Case 13** (9 breakout events, matched-failure comparisons for 7/9, local-baseline-multiple field added, credential-first self-introduction confirmed present on both breakout and matched-failure videos alike — i.e. not a differentiating factor for this channel).

This dossier adds one new, concrete finding beyond Case 13: **16 additional videos** (listed in §2's top-15-plus table minus the 9 already in Case 13) clear the same >5x-median breakout threshold but have not yet been individually investigated for cause. This is flagged as the next concrete Phase-6 task for this channel, not claimed as done.

## 6. Historical demand / external research

Not attempted in this pass. Existing Google Trends work in `TRENDS-RECAPTURE-SUMMARY.md` covers the 6-channel original cohort plus select breakout topics; Better Health While Aging's specific topics (B12 deficiency, medication warnings, ADLs/IADLs) have not yet had a dedicated Trends check.

## 7. Knowledge-corpus integration (DS-000011/018/031)

Applied only within the existing Case-13 write-up (breakout events). Not yet applied to the remaining 89-video population or to the 16 newly-flagged breakout candidates.

## 8. Honest summary

Metadata layer: complete and verified (98/98, real transcripts, 0 gaps, both DBs pass integrity/FK checks). Forensic-analysis layer: population-level and title-pattern analysis is now genuinely done for all 98 videos with real numbers, not estimates. Deep per-video script/thumbnail/breakout-cause analysis remains complete for 9 of 98 videos (the pre-existing Case 13) and outstanding for the other 89 — including 16 newly-identified breakout candidates this pass surfaced but did not investigate further. This is stated plainly so a later pass does not have to rediscover the gap.
