# 10 Validation: hypotheses, holdouts, failures (continuation, 2026-11-23)

Status: **machine tests plus same-model self-review. No independent reviewer exists (human or other model family).** "Holdout" here means a set of videos that did not take part in forming the hypothesis; where the numbers were formed on all videos the test is called a stability check.

## Hypotheses formed on examined material, tested on other videos
| ID | Hypothesis (formed on) | Test set | Result | Failures and exceptions |
|---|---|---|---|---|
| H1 | Most frames of an xkcd video are visual holds; one fully viewed video had 92.7% hold frames (pilot `9VG0yqq_PHM`) | 87 other videos, long 43 and Short 44 separately (`ct_scan_batch/BATCH_SUMMARY.csv`) | **Holds.** Median hold share: long 93.3% (IQR 86.2 to 95.4), Short 94.1% (IQR 89.1 to 96.8) | long min 31.1%, Short min 54.7%: the two continuous-motion videos (`oTzW-mTQd5w`, `ERieN5pee7A`) and a few others; hold share measured at the detector thresholds, not a judgement |
| H2 | Narration starts at frame 0 and the first visual event lands by about 2 s (campaign 44) | audit-ledger 44 videos, different detector | **Replicates.** First ASR segment starts at <= 0.5 s in 88 of 88; first event median 1.81 s (campaign) and 2.00 s (audit); within 3 s in 91% and 89% | latest first event 5.8 s (campaign), 7.6 s (audit) |
| H3 | Event gap about 2.1 s and 20 to 23 events per minute (campaign 44) | audit-ledger 44 | **Replicates** (`06_PACING_CORRECTION.md`): 2.15 vs 2.15 s long, 22.5 vs 21.8 events per min | same family of detector; shot medians do **not** replicate cleanly (8.44 vs 6.75 s long) |
| H4 | ASR clause starts and visual events are associated (campaign 44) | audit-ledger 44 and chance shifts | **Replicates**: 54 to 58% within 0.5 s in all four groups vs 33 to 37% under time shifts | segment-level provisional ASR; no listening |
| H5 | A red book-promo end card closes long videos (20 long checked) | all 44 long and 24 Shorts | **Holds** 44 of 44 long, 0 of 24 Shorts | |
| H6 | Script rules (attributed opening 41/43, no CTA 41/43, speech rate 3.6 w/s) formed on all 43 long | older 21 vs newer 22 (`05_PHASE5_VERIFICATION.md`) | opening, CTA and speech rate **stable**; length **not** (825 vs 632 words) | V015 label, V019, V020, V024 |
| H7 | Palette is achromatic with a sparing red accent (Phase 7 sample) | Phase 7 holdout (23 frames) vs coding sample (24) vs 7b (40) vs Shorts (38) | red accent in 46%, 30%, 30%, 24% of frames; thin-stroke median 6.0, 6.0, 7.6, 5.7 px; achromatic default holds everywhere | red share varies with the sample (46% to 24%), so "about a third" is a pooled figure (39 of 125 = 31%) with wide spread; stroke width is +-1 to 2 px |
| H8 | Spoken number appears on screen in about half of quantity moments (Phase 7) | holdout frozen before viewing: 9 of 18 vs 9 of 19 | **Holds** (checkpoint 3) | pooled 125-frame figure 53 of 105 |
| H9 | Measured shot boundaries are real cuts | 156 viewed shots (`06_LEDGER_REVIEW_METHOD_AND_COVERAGE.md`, batch 4 added 2026-11-23) | 119 of 156 true cuts (76%); 65% at strength < 0.3 vs 87% at >= 0.3 (v2: 83 of 108, 64% vs 89%) | camera moves over maps, content added, whole-frame dimming (`U4cONnQxgvo` 7 of 14 false boundaries in batch 3) |

## Phase 10 checklist against the directive
| # | Requirement | Status |
|---|---|---|
| 1 | reusable hypotheses from deeply examined videos | done (H1 to H9) |
| 2 | test on distinct, previously unexamined episodes | done for H1 to H6 and H9 as above; H7 and H8 tested on frozen or disjoint frame sets |
| 3 | long-form and Shorts separately | done for H1, H3, H4, H7, H9; H2 pooled |
| 4 | highly similar and structurally different topics | **partial**: split by era and format, not by topic family; no per-family test |
| 5 | record failures and exceptions | done (right-hand column) |
| 6 | check visual claims against actual frames | done for Phase 7 coding, the 108-shot sample, style masks (validation sheets) |
| 7 | recalculate numeric motion and editing metrics | done: pacing recomputed from ledgers and from probe durations; ASR segment counts; hold shares |
| 8 | validate transcript-to-video alignment | **partial**: ASR identity and duration checked for 88 of 88; sync **not** validated (no listening) |
| 9 | independently assess scientific diagrams | **partial**: 10 spoken claims recomputed (`07_SCIENCE_CLAIM_CHECKS.md`); diagram drawings not assessed for accuracy; not expert review |
| 10 | record missing media and inaccessible evidence | done: 4 videos without media; no Machine A data; no listening |
Overall: self-reviewed; independent QA UNAVAILABLE.

## Addendum 2026-11-23 (third pass): what each kind of check was
| Kind | What was done here | Not done |
|---|---|---|
| Preselected holdout | none new (the Phase 7 holdout of 23 frames and the 20-long and Short samples from checkpoint 16 stand) | no pre-registered test of the 23 rules |
| Later stability check | shot-boundary strength pattern re-tested on a fresh 48-shot draw (67% below 0.3, 83% at or above 0.3; overall 156 shots 65% vs 87%); era split of script length unchanged | no per-topic-family holdout |
| Automated detector validation | leading-silence detector (-45 dB) on 88 files; colour-share measure on 160 frames | none validated against a listener |
| Same-model self-review | all viewing, coding, physics recomputation and the 23-rule audit | this is not independent review |
| Independent human or expert review | none | UNAVAILABLE |

A rule-level finding from the audit: 7 of 23 rules needed qualification and 1 was not yet supported, which shows the draft overstated in places; the revisions are in `11_RULE_AUDIT_2026-11-23.csv` and the ledger columns `audit_label_2026_11_23` and `wording_change_2026_11_23`.
