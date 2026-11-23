# 03 Corpus completeness (v2, reconciled 2026-11-23 continuation)

Numbers come from `03_CHANNEL_MASTER_INVENTORY.csv` (v2, 92 rows), `03_ASR_VALIDATION.csv` (88 rows), `live_channel_ids_2026-11-23.json` and `scripts/reconcile_v2.py`. The v1 report is kept as `03_CORPUS_COMPLETENESS_REPORT_v1_2026-11-23T1043.md` (history of earlier conclusions; what changed is in section 5).

## 1. Catalog count (live recount done)
On 2026-11-23 the built-in browser opened `youtube.com/@xkcd_whatif/videos` and `/shorts` and scrolled until no new item loaded (no continuation element left). Result: **46 long videos + 46 Shorts = 92 distinct IDs, identical to the 92-row inventory** (0 IDs only live, 0 only in the inventory; format matches for all 92; `Aony69nO5kI` is a long video). Qualification: this is what the two public listing tabs show to a logged-out visitor on one day. It does not prove that no unlisted, private or removed video exists, and views/dates were not re-read (the views column stays the 2026-11-04 census value). 83 is the transcript count, not the channel count.

## 2. Counts (logical video IDs; one ID = one video whatever the encode)
| Measure | Count |
|---|---|
| Public videos listed live | 92 (46 long, 46 Shorts) |
| Full local media (library MP4, SHA-256 equals census hash) | 88 (44 long, 44 Shorts); missing: alkJ7xScBiw, NxVdO7M2YdM, XwJAbyn5uGY, Aony69nO5kI |
| Catalog transcript (untimed; 67 user-generated, 16 auto captions) | 83 (43 long, 40 Shorts) |
| Local whisper ASR (provisional, never a verified transcript) | 88 videos (44 from the campaign, 44 from this audit); 0 videos with media lack ASR |
| ASR identity confirmed against the catalog transcript (3-gram containment, duration) | 83 of 83 |
| ASR only, no catalog text | 5: 9VG0yqq_PHM, 35KZm1yiyIE, TIDHee_Q5Gk, X97DDWvxaqQ, alBQCm0QpJg |
| Any transcript (catalog or ASR) | **88 of 92** (v1 said 86; the two new ASR files are X97DDWvxaqQ and alBQCm0QpJg) |
| No transcript of any kind | 4 (the 4 without media) |

ASR validation of the two files the continuation had to check (`03_ASR_VALIDATION.csv`): `X97DDWvxaqQ` ASR ends at 99.76 s for a 100.84 s file; its text matches its title ("Could you power your computer by typing?") and 70% of its 8-grams occur in the catalog transcript of the long `0L44GEJ5pLE` (a Short extracted from that long video, consistent with the family table). `alBQCm0QpJg` ASR ends at 69.2 s for a 70.03 s file; the content is a run of viewer questions ("More weird and worrying questions"); only 2.7% of its 8-grams occur in any catalog transcript, so there is no text to cross-check against. Status for both: **ASR_PROVISIONAL, duration and title consistent**. Not a verified transcript, not listened to.

## 3. Evidence layers by logical ID (no double counting)
| Layer | IDs | Notes |
|---|---|---|
| Campaign (existing, hash-matched library files) with shot + event ledgers | 44 (24 long, 20 Shorts) | 43 `quality_gate = VISUAL_ANALYSIS_PARTIAL`, plus 9VG0yqq_PHM, which also has the audit pilot |
| Audit measured ledgers (this audit, machine, different detector) | 44 (20 long, 24 Shorts) | **disjoint from the campaign 44** (0 shared IDs); 719 shots, 2,160 events |
| Union of the two ledger layers | 88 = every video with media | |
| Brain (14 slugs, different encodes, 0 of 14 hash-equal) | 10 IDs resolved: 8 also in the campaign set, 2 (`UXA-Af-JeCE`, `e3uk7jU3RHo`) in the audit-ledger set | 4 slugs without a canonical ID; never pooled with the campaign (AGENTS rule 9) |
| CT_SCAN machine stage (every frame, full resolution) | 88 of 88 | measured, not viewed |
| Hold-residual runs viewed as stills | 88 of 88 (189 + 1,443 runs) | one coder family |
| Science frames viewed and coded | 82 videos (125 frames) | |
| Measured shots viewed and coded | 42 videos (60 shots) | |
| Every native frame viewed | 1 (`9VG0yqq_PHM`, 3,893 frames) | visual only |

## 4. Evidence tiers (directive scale; v2 rule)
Rule: DEEP_VISUAL needs every native frame viewed; TARGETED_VISUAL needs a model reviewer to have classified segments (campaign gate); STRUCTURAL_ONLY needs measured shot/event tables; processing alone never raises a tier. "machine measured", "sampled and viewed" and "deep visual review" are separate columns in the inventory.

| Tier | Count | Detail |
|---|---|---|
| DEEP_VISUAL | **1** | `9VG0yqq_PHM`: visual-only, one coder, no audio, changes under 15 px not examined. Not DEEP for audio or sync. The earlier "0 channel-wide" was too strict about this one video; channel-wide deep coverage is 1 of 92 |
| TARGETED_VISUAL | 43 (23 long, 20 Shorts) | campaign classified segments; native views partial |
| STRUCTURAL_ONLY | 44 (20 long, 24 Shorts) | audit measured ledgers + CT machine scan + sampled stills; 659 shots and the events of these videos are NOT_VIEWED beyond the 60-shot sample |
| TRANSCRIPT_ONLY / MEDIA_ONLY | 0 | v1 had 22 + 2; they now have measured ledgers |
| UNAVAILABLE | 4 | no media |

Unmet for all 92: audio listening; human-verified narration timing; independent review.

## 5. What changed since v1 (history kept in the `_v1_` files)
1. Live recount done (v1: not possible; RSS latest 15 only). 92 confirmed.
2. ASR: v1 said 64 videos; the real count of ASR files is 88 (44 campaign + 44 this audit). Any-transcript 86 -> 88 of 92.
3. Tier table: TRANSCRIPT_ONLY 22 and MEDIA_ONLY 2 became STRUCTURAL_ONLY because measured ledgers now exist; the 20 long structural-only videos gained a shot ledger; one DEEP_VISUAL video.
4. `shot_ledger = YES 44` in v1 meant campaign ledgers only; it is replaced by explicit layer columns.
5. Phase 4 attributes added: aspect ratio, live format, observation dates, audio availability, article-correspondence candidates (22 title-word candidates, 22 weak body-text candidates, 48 UNKNOWN; none verified against article text), legal status.
