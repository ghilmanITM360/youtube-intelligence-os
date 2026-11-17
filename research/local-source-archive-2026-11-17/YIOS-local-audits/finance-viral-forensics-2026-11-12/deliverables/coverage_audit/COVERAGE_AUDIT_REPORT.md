# Coverage Audit: Finance/Economics Viral Forensics

Date: 2026-11-12. Read-only. The source DB copy, earlier reports and the senior-health project were not modified. Script: `../../14_coverage_audit.py`. It writes only into this folder.

## How membership was established

Each stage's membership was **re-derived by re-applying the filter in the script that ran that stage** to the intermediate files in `out/`. A video's presence in the DB did not count as being analyzed.

I also **re-derived the baseline and Performance Index (PI) for all 3,634 videos straight from the DB copy** (opened read-only), using the 02_features.py rules. The result matches the pipeline PI for every video. That is a replay of the same rules, not a re-check of the rules themselves.

Nothing was marked `UNVERIFIED` for the classification exclusions: every one of the 578 excluded videos traced to a coded rule. What I could not do is replay *which individual feature tests ran*. The scripts drop a feature when either group has fewer than 30 videos. I recorded per-layer n ranges from the test CSVs, not a per-video, per-feature log.

## 1. Reconciliation against the source DB

| Your number | Actual (DB, read-only) | Status |
|---|---|---|
| 69 channels | 69 rows in `channels`. 68 have at least one video; **Wealth Logic has 0** | OK, with that caveat |
| 3,634 unique videos | 3,634 rows = 3,634 distinct `video_id` | OK |
| 3,410 videos with transcripts | 3,410 (`has_transcript=1`, and 3,410 distinct `video_id` in `transcripts`) | OK as *videos with a transcript*. The brief called these "unique videos"; the unique-video count is 3,634 |
| 3,450 transcript rows | 3,450. That is 3,410 + 40 extra rows on 29 videos. No orphan rows | OK |
| 3,412 long-form | 3,412 by the pipeline rule: `video_type` is not SHORT/Short **and** duration > 60 s | OK. 3,412 is a coincidence of size with 3,410 and is unrelated to it |
| 222 Shorts | 222 by the same rule. The label alone gives 221; one extra video has duration ≤60 s | OK. The extra Short is a rule choice of mine |
| 3,056 classified across 60 channels | **3,056 long-form videos across 60 channels** | OK, but **long-form only**. Shorts are separate: 201 more classified, 21 not |

Classification counts reproduced:
- **Long-form:** 398 Breakout, 424 Successful, 1,451 Average, 783 Underperforming (3,056), plus 356 not classified.
- **Shorts:** 12 / 23 / 141 / 25 (201), plus 21 not classified.
- 3,056 + 356 + 222 = 3,634.

## 2. Why 578 videos are not in the 3,056 (`excluded_videos.csv`)

| Reason | Videos |
|---|---|
| Long-form, published less than 14 days before the 2026-11-11 snapshot (not baseline-eligible) | 306 |
| Long-form, channel has fewer than 12 baseline-eligible long-form videos | 40 |
| Long-form, view count missing | 10 |
| **Long-form total** | **356** |
| Short, classified in the separate Shorts analysis | 201 |
| Short, not classified (channel has fewer than 12 eligible Shorts) | 20 |
| Short, not classified (published less than 14 days before snapshot) | 1 |
| **Shorts total** | **222** |

The 306 recent videos are the newest uploads, so the whole study has no view of the last 14 days. This is by design, because views had not settled.

## 3. Channels (`channel_coverage_69.csv`)

- **60 channels** have at least one classified long-form video.
- **9 channels contribute nothing to the 3,056:**
  - Wealth Logic: 0 videos in the DB.
  - Chronofold: 2 long-form, 0 transcripts, no subscribers or sub_niche.
  - David Explains Money: 4 long-form.
  - Built On You: 10 long-form.
  - Millionaire Problems: 9 long-form.
  - The Wealth Engine: 6 long-form.
  - Econ in a Nutshell: 14 long-form, 11 of them too recent.
  - Frank Law: 24 long-form, 13 too recent and 11 below the 12-video channel threshold.
  - Primitive Education: 2 long-form and 11 Shorts, none classified, 0 transcripts.
- **Concentration:**
  - Several channels sit at 100 or more videos each.
  - Casual Finance has 206 videos but only 33 long-form classified. 173 are Shorts.
  - **Only three channels have any classified Shorts:** Casual Finance (173), MonkeyExplains (15), Primate Economics (13). Any Shorts conclusion rests on those three, and mostly on one.
- Many channels are flagged as thin (fewer than 30 classified). The flags are in `data_flags`.

## 4. Per-stage samples (`stage_sample_coverage.csv`, IDs in `stage_video_ids.csv`)

| Stage | Videos | Channels | Basis |
|---|---|---|---|
| Baseline-eligible (all formats) | 3,317 | 68 | 02: has views and is at least 14 days old |
| Performance classification, long-form | 3,056 | 60 | 02 |
| Shorts classification | 201 | 3 | 02 + 10 |
| **Title analysis** | 3,056 | 60 | 03/06/09/10; titles exist for every video |
| **Hook analysis** | **2,858** | 60 | Needs a transcript of at least 200 characters. 198 classified videos have none |
| **Introduction analysis** | **2,858** | 60 | Same population as Hook (`i_*` and `*_150` features) |
| **Script analysis** | **2,858** | 60 | Same |
| Hook-claim proxies (`h_snapback3`, `h_but_any`, `h_named_entity_30s`) | 3,056 | 60 | **The 198 with no transcript are coded FALSE, not missing.** See finding A |
| Viral Checklist score | 3,056 | 60 | Same issue for its hook-derived items |
| **Thumbnail analysis** | **3,001** | 59 | 55 classified videos had no downloadable thumbnail |
| Thumbnail OCR | 3,001 | 59 | Same set |
| **Topic clustering (fit)** | **3,634** | 68 | KMeans (k=18) fit on every title, Shorts included |
| Topic performance table | 3,056 | 60 | Classified long-form only |
| **Audience-problem analysis** | 3,056 | 60 | Rule tags on title + first ~150 transcript words |
| **Matched winner-vs-loser** | 692 pairs = 692 winners + 692 losers | 54 | Same channel, within 150 days, duration ratio 0.6–1.67, each loser used once |
| **Held-out-channel prediction** | **1,605** | 60 | Breakout + Successful vs Underperforming. The 1,451 Average videos are excluded. Missing features are median-imputed |
| **Shorts analysis** | 201 | 3 | Plus the channel-level format comparison |
| Variance decomposition (log views) | 3,402 | 68 | Long-form with views > 0 |
| Channel-level structure (cadence/entropy) | 3,035 videos | 47 | Channels with at least 20 dated long-form videos and a span of at least 30 days |
| Views-per-subscriber outlier ratio | 2,449 | 45 | Long-form with subscribers and views |
| Near-duplicate script detection | 3,402 | 66 | All formats, transcript over 500 characters |

Per-layer test counts, from the CSVs: title features n = 3,056 per test; hook, intro and script features n = 2,858 where the 30-video minimum let them run; thumbnail tests n = 3,001.

## 5. Findings from the audit

These affect how far the earlier conclusions can be trusted.

**A. Three hook proxies and the checklist score count missing transcripts as "no".**
- In `06_claims.py`, `h_snapback3`, `h_but_any` and `h_named_entity_30s` are built so that a missing transcript becomes `False`, not `NaN`.
- They therefore ran on 3,056 videos, not 2,858. The Viral Checklist score inherits this for its hook-derived items.
- The 198 affected videos are concentrated in a few channels: Finance Simplified, Max Invests, Rick Finance and Tom - Lazy Dividend Investor (40 each), and The Wise Future (33).
- The directional results (null or flat) probably survive, but those specific rows are mildly biased and should be rerun on the 2,858 before anyone quotes them. I have not rerun them.

**B. The held-out-channel prediction used 1,605 videos and imputed missing features.**
- The reported AUCs (title 0.50, script 0.59, and so on) describe Breakout and Successful versus Underperforming only.
- Average videos (the middle 1,451) never entered the model.
- Videos with no transcript got median-filled script and hook features.

**C. Thumbnails: what "captured" means.**
- Of the 3,056, **372** have a derived pattern URL (constructed, not captured). 2,684 are captured.
- The thumbnail features were computed from `mqdefault.jpg` images that **I downloaded by video ID**, not from the URL stored in the DB.
- So the "captured vs derived" distinction does not change what the image analysis saw. It matters for provenance only.
- The recorded DB URL returned HTTP 200 for 3,001 classified videos, 404 for 54 and an SSL error for 1. Those 55 are the ones missing from the thumbnail stage.
- Only 3 of 6 contact sheets were viewed by eye. The rest is automated features.

**D. Topic clustering was fit on all titles, including Shorts and the 578 excluded videos.** The cluster *definitions* therefore use 3,634 titles, while the *performance* tables use 3,056.

**E. Recency and size bias.**
- The 14-day rule drops 306 long-form videos, all recent.
- All 192 videos with no publish date are inside the 3,056. Of the 3,056, 2,825 have a full timestamp and 39 are date-only.
- Undated videos in an eligible channel use a channel-median baseline, not a temporal-neighbour baseline.

## 6. Files

1. `channel_coverage_69.csv`: 69 rows. Counts, exclusions, transcripts, thumbnails and flags per channel.
2. `analyzed_videos_3056.csv`: all 3,056 classified videos with the requested fields. Extra columns show stage membership, baseline and thumbnail HTTP status.
3. `excluded_videos.csv`: all 578 excluded videos.
4. `stage_sample_coverage.csv`: one row per stage.
5. `stage_video_ids.csv`: one row per (stage, video), 62,185 rows.
6. `_reconciliation_raw.csv`: the raw counts behind section 1.

SHA-256 hashes were computed at write time. Run `shasum -a 256 *.csv` in this folder to check.

## Limits of this audit

- Membership comes from re-applying the scripts' filters, not from per-video logs written during the original run. The original run kept no such logs. This is why everything here is "reproduced", and why the per-feature minimum-cell drops are only reported as ranges.
- The 3,056 and the classification were rebuilt from the DB. The 2,858, 3,001, 1,605 and 3,402 were recomputed from the pipeline's intermediate files. The 692 pairs were read from `out/matched_pairs.csv` and not rebuilt. The per-test n ranges came from the test CSVs.
