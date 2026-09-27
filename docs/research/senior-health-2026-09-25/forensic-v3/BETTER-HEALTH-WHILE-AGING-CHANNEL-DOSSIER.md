# Better Health While Aging (DS-000033) — Individual Channel Dossier

**Channel:** Better Health While Aging (`@BetterHealthWhileAging`, `UCFpxvukIqCAUA7YizI-q9Dw`)
**Status date:** 2026-09-27
**Data basis:** 98/98 videos, 98/98 real transcripts, 0 placeholders (94-video initial acquisition, run `AuZ65QkXBmVIXcOn9`, 2026-09-25, + 4-video Priority A Shorts backfill, run `Ll3gKxE3dXEeG4SDd`, 2026-09-26). Source: `youtube_channel_registry.db` / `youtube_inventory.db`, dataset `DS-000033`.
**Purpose:** Phase 6 individual-channel research artifact for this competitor, requested separately from the combined V3 cross-channel synthesis. Extends the existing V3 corpus rather than duplicating it — breakout-event analysis for this channel already exists in `SMALL-CHANNEL-BREAKOUT-FORENSICS.md` (Case 13) and is referenced, not re-derived, below.

**Scope disclosure (metadata completeness vs. forensic-analysis completeness are tracked separately):**
- Metadata completeness: **COMPLETE** — 98/98 videos, 98/98 real YouTube-caption transcripts, 0 explicit no-subtitle gaps, 98/98 source thumbnail URLs. The earlier 97/98 registry result was a derived-data defect: `16n80OQCVSM` had a real URL in both immutable raw datasets and the standard workbook, but the registry kept an older snapshot row whose thumbnail field was blank. Duplicate video evidence now fills missing fields from later package evidence; multi-run thumbnail coverage now unions unique video IDs rather than taking the largest single run (94 vs. 4). Raw evidence was not changed.
- Forensic-analysis completeness: **PARTIAL**. Automated structural transcript analysis now covers 98/98 videos in `BETTER-HEALTH-WHILE-AGING-TRANSCRIPT-STRUCTURE.json`, with actual opening text and explicitly estimated 15/30/60-second windows. This is separate from deep investigation. Case 13 contains prior narrative review for 9 breakouts, but those nine still require acceptance-level re-verification against every criterion in the resumed assignment; 89/98 videos remain without deep manual review. Thumbnail visual inspection, dedicated historical-demand work, complete DS-000011/018/031 application, and medical verification remain open.

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

### Complete 25-video breakout-candidate inventory (>5x all-video median)

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
| 209,917 | video | Atrial Fibrillation in Older Adults: Watchman, Medications, & Other Treatment Options |
| 200,502 | video | How to Treat Urinary Incontinence in Older Women |
| 173,658 | video | UTIs in Older Adults: Symptoms & Prevention |
| 173,598 | video | Anemia in Aging: Symptoms and Solutions |
| 158,064 | video | Osteoporosis Medications Explained: What to Know Before You Start |
| 156,943 | video | COVID and Flu Vaccines 2026 What Older Adults Need to Know |
| 134,842 | video | High Blood Pressure in Aging: When to Treat & Why It Matters |
| 110,997 | video | 10 Causes of Memory Loss in Old Age – HOP ML Podcast |
| 100,825 | video | Slow Heart Rates in Aging: Pacemakers and other Treatments |
| 99,834 | video | Boosting Bone Density: Best Ways to Prevent Fractures as You Age |

25 of 98 videos (26%) clear the >5x-median candidate threshold — all regular videos, no Shorts. IDs and cohort membership are canonical in `BETTER-HEALTH-WHILE-AGING-TRANSCRIPT-STRUCTURE.json`: 25 unique IDs, 9 `ORIGINAL_NINE`, 16 `REMAINING_SIXTEEN`. This 5x candidate screen is intentionally broader than Case 13's 15x breakout-event rule. Case 13's nine are previously reported investigations, not newly accepted without re-verification. Remaining 16 have automated structure records but no deep case investigation.

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

`visual_asset_status = THUMBNAIL_URL_ONLY` for this channel. Source URLs exist for 98/98 videos after correction, but URL availability is not visual inspection. No candidate thumbnail is yet registered as inspected forensic evidence. Cross-channel thumbnail findings do not transfer automatically.

## 4. Script/transcript evidence

98/98 real transcripts available (73 labeled user-generated, 21 labeled auto-generated, 4 real-caption transcripts whose source record omits caption type; no paid AI transcription). Earlier `77 user-generated` wording silently treated the 4 unspecified records as user-generated and is corrected here. `BETTER-HEALTH-WHILE-AGING-TRANSCRIPT-STRUCTURE.json` now records 98/98 automated structural analyses: actual opening/promise text; estimated 15/30/60-second windows; hook labels; five-part script excerpts; narrative progression; information-density measures; authority/evidence cues; curiosity and revelation proxies; recommendation cues; and conclusion/CTA evidence. Every row states `AUTOMATED_STRUCTURAL_ANALYSIS_COMPLETE` and separately records deep-investigation state. Timing is `ESTIMATED_FROM_WORD_POSITION_PLAINTEXT_CAPTIONS`; it is not represented as exact caption timing.

## 5. Breakout investigation

Already completed and not re-derived here: see `SMALL-CHANNEL-BREAKOUT-FORENSICS.md`, **Case 13** (9 breakout events, matched-failure comparisons for 7/9, local-baseline-multiple field added, credential-first self-introduction confirmed present on both breakout and matched-failure videos alike — i.e. not a differentiating factor for this channel).

This dossier adds one new, concrete finding beyond Case 13: **16 additional videos** (listed in §2's top-15-plus table minus the 9 already in Case 13) clear the same >5x-median breakout threshold but have not yet been individually investigated for cause. This is flagged as the next concrete Phase-6 task for this channel, not claimed as done.

## 6. Historical demand / external research

Not attempted in this pass. Existing Google Trends work in `TRENDS-RECAPTURE-SUMMARY.md` covers the 6-channel original cohort plus select breakout topics; Better Health While Aging's specific topics (B12 deficiency, medication warnings, ADLs/IADLs) have not yet had a dedicated Trends check.

## 7. Knowledge-corpus integration (DS-000011/018/031)

Applied only within the existing Case-13 write-up (breakout events). Not yet applied to the remaining 89-video population or to the 16 newly-flagged breakout candidates.

## 8. Honest summary

Metadata layer: 98/98 videos, 98/98 real transcripts, 98/98 source thumbnail URLs. Automated structural analysis: 98/98. Deep forensic acceptance: still **PARTIAL**; earlier Case 13 work covers nine candidates but requires criterion-by-criterion verification, while remaining 89 videos need deep review. No thumbnail inspection, dedicated historical-demand pass, complete knowledge-framework application, or medical-claim review is claimed complete.

## 9. Resumed-assignment phase audit

| Phase | Status | Evidence / gap |
|---|---|---|
| 1. Recover progress | VERIFIED COMPLETE | Current branch and remote at `655db99`; dossier, V3 reports, 41-sheet workbook, Case 13, evidence registers, raw DS-000033 evidence, package, and scripts located. |
| 2. Data corrections | PARTIAL | 25 unique IDs and 9/16 split verified; full inventory restored; missing thumbnail cause fixed; 98 transcript provenance rows verified; regular/Short baselines distinct. Full regression suite and regenerated workbook still pending. |
| 3. Structural transcript analysis | VERIFIED COMPLETE | `BETTER-HEALTH-WHILE-AGING-TRANSCRIPT-STRUCTURE.json`, 98 unique records. Automated status remains separate from deep review. |
| 4. Deep 25-breakout investigation | PARTIAL | Case 13 contains prior work for 9; acceptance re-verification and remaining 16 outstanding. |
| 5. Thumbnail inspection | NOT STARTED | 98 URLs available; 0 images registered as visually inspected. |
| 6. Historical research | NOT STARTED | Existing general Trends corpus does not provide dedicated BHWA topic research. |
| 7. Apply DS-000011/018/031 | PARTIAL | Prior Case 13 usage reported; full video-level support/counterexample matrix absent. |
| 8. Medical verification | NOT STARTED | Existing cohort medical file is not a BHWA 98-video claim review. |
| 9. Complete channel population | PARTIAL | Population statistics and automated structure complete; deep review incomplete. |
| 10. Update dossier/workbook | PARTIAL | Dossier updated in place; existing 41-sheet workbook not yet regenerated with resumed findings. |
| 11. Recoverable batches | PARTIAL | Batch A artifacts and tests exist; checkpoint/commit pending. |
| 12. Validation/preservation | PARTIAL | Full suite passed (393 tests); registry integrity/FK checks and focused workbook QA passed. Commit and push pending; V3 workbook integration remains open. |
| 13. Mandatory progress report | PARTIAL | Current numbers recorded here; final report waits for remaining phases. |
