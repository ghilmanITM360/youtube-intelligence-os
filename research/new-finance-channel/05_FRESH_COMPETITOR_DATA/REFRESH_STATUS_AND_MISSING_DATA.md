# Fresh data: status, missing data, refresh proposal (2026-11-18)

Labels: VERIFIED (read from DB/files today) / INFERRED / UNKNOWN. No paid run was made for this document. Nothing was scraped today for this branch.

## 1. Refresh status per primary channel

| Channel | In DB | Latest in DB | Needs | Status |
|---|---|---|---|---|
| Monkey Economics (@MonkeyEconomic, 224K subs) | 60 of 60 (19 long + 41 Shorts), 60 transcripts | 2026-11-09 | nothing | FRESH (Apify run 2026-11-18, merged to main via PR #62) |
| Casual Finance | 206 of 220 reported, 206 transcripts | 2026-10-10 | everything after 10-10; 14 videos missing; no local thumbnail files | STALE (39 days) |
| MonkeyExplains | 63 of 63, 60 transcripts | 2026-10-18 | after 10-18; 3 missing transcripts | STALE (31 days) |
| Crayon Capital | 30 of 30 | 2026-09-09 | after 09-09 | STALE (70 days; may have stopped uploading, UNKNOWN) |
| Capital Case (11.7K subs) | 13 | 2026-11-02 | after 11-02 | 16 days old |
| PaperBillionsTV (14.1K subs, 4 videos on channel) | 0 (not in DB) | 2026-11-13 (spot scrape) | transcripts, thumbnails, Shorts check, DB ingest | LOW: only 4 view snapshots |

PaperBillionsTV raw JSON (`01_CHANNEL_REPORTS/071_paperbillionstv/raw/apify_youtube_scraper_JsyvS0PVokzdfwCAb.json`) holds 5 rows: 1 channel-info row plus 4 videos (views 144K to 2.1M, 14 to 20 min), no subtitles. The 11-12 CSV has 3 of them with likes/comments. Joined 2022-09; channel page says 4 videos. VERIFIED from the files.

Name check (VERIFIED from DB handles): **Monkey Economics = @MonkeyEconomic (224K)**, and **Primate Economics = @Primateeconomics (577K)** is a different channel. Both are in the inventory.

## 2. Time windows today

The DB stops at 2026-11-11, so the 7/30/60/90-day windows are partly empty. Windows with data (from `MASTER_INVENTORY.csv`): last-30-day counts exist for only Monkey Economics 2, Capital Case 1, PaperBillionsTV 4, Primate Economics 1. Casual Finance, MonkeyExplains, Crayon Capital: 0. A fresh pull is needed before any "recent performance" claim.

## 3. Missing-data report

| Gap | Size | Fix | Paid? |
|---|---|---|---|
| Videos after DB cut-off for 5 primary channels | est. 60 to 100 items | Apify delta scrape | yes, small |
| **Publish dates missing** on 192 videos: Economics Explained, How Money Works, Money & Macro, Patrick Boyle, Modern MBA, PensionCraft (30 each) plus ~12 others. These came from the Videos tab with rounded views and derived thumbnail URLs | 192 | Apify re-scrape (dates, exact views, real thumbnails) | yes |
| Transcripts missing | 224 of 3,694 (3,470 present). Includes MonkeyExplains 3, Tom Lazy Dividend 40, Finance Simplified 40, Max Invests 40, Rick Finance 40, Wise Future 33 | check for existing caption files first; else Apify subtitles; or local whisper-cli (installed 2026-11-14, free) | partly |
| Casual Finance local thumbnails | 0 files (206 URLs) | download from `i.ytimg.com` URLs (free, public) | no |
| 14 Casual Finance videos not in DB | 14 | delta scrape | yes, small |
| Wealth Logic channel unavailable/deleted | 1 | none; keep as UNAVAILABLE | no |
| Studio CTR, retention, impressions for any channel | all | owner's own channel only; competitors' are UNKNOWN permanently | n/a |
| Likes/comments for most Shorts and older videos | many | Apify | yes |

Free first: (a) local transcripts via whisper-cli for the missing ones where audio can be obtained legitimately, (b) public thumbnail downloads, (c) Trends, News and YouTube search in the browser. None of these cost money.

## 4. Paid refresh proposal (needs your approval; nothing run)

Price evidence (VERIFIED, 2026-11-18 run notes): actor `streamers/youtube-scraper`, about $0.004 per video row with English subtitles (19 rows $0.072, 41 rows $0.164). Per-run cap $0.30 is the convention used so far.

| Batch | Scope | Est. rows | Est. cost |
|---|---|---:|---:|
| R1 primary delta | Casual Finance (since 10-10, incl. 14 missing), MonkeyExplains (since 10-18), Crayon Capital, Capital Case, PaperBillionsTV (all 4 + Shorts tab) | about 100 | about $0.40 |
| R2 date repair | the 6 undated channels, latest 30 each | 180 | about $0.72 |
| R3 additional explainers | about 12 P1 channels (Neu, Business Decoded, Nostalgic Wheels, Built On You, The Expensive Part, Econ in a Nutshell, Finance ANALYST, Mr. Ranks, Primate Economics, Penny Explains Finance, etc.), last 90 days | about 300 | about $1.20 |
| Total | | about 580 | **about $2.3, cap $3.00** |

Expected benefit: a real last-7/30/60/90 view of the six primary channels, usable publish dates for the six largest economics channels (the most relevant for our positioning), current view counts for the topic scoring. Earlier you set a $5.00 cumulative Apify cap for the Finance batch (2026-11-10); spend on record since then is about $2.44 + $0.08 + $0.27, so R1+R2+R3 would sit near that cap. Please confirm whether the cap is still $5.00. Run R1 first and stop to review.

Not proposed: re-scraping data already held (Monkey Economics, all 60 rows), and the 71 per-channel history.

## 5. R1 RESULT (executed 2026-11-18, owner-approved, new Apify account, free plan $5.00)

Two runs of `streamers/youtube-scraper`, subtitles on (`ALWAYS_SUBTITLES`), newest first. Total **$0.236** (run x8dELGyWu8l9Ufzhe $0.148, 77 requests; run DRAGcutlIUr24oUmJ $0.088, 45 requests), 0 failed. Estimate was about $0.40. Raw JSON (unchanged) and `SHA256SUMS.txt` in `raw/`; flat table `R1_FRESH_VIDEOS_2026-11-18.csv` (56 videos). Snapshot date 2026-11-18, public views only. DB `data/catalog/` was NOT modified; ingest is a separate step.

| Channel | Rows | Not in DB | Newest | 7d | 30d | 90d | Subs now | Transcripts | Note |
|---|---:|---:|---|---:|---:|---:|---:|---:|---|
| Paper Billions | 6 | 6 | 11-17 | 3 | 6 | 6 | 23,600 (14,100 on 11-13) | 6 | all videos on channel (no Shorts); 3 new since 11-13 |
| Casual Finance | 30 (15 long + 15 Shorts) | 17 | 11-17 | 2 | 13 | 25 | 440,000 | 30 | cap reached, so counts are lower bounds |
| MonkeyExplains | 10 (5+5) | 10 | 11-14 | 5 | 10 | 10 | 261,000 | 8 | cap reached; 2 are Member Edition (no views, no transcript) |
| Crayon Capital | 5 | 5 | 11-14 | 1 | 3 | 5 | 319,000 | 5 | **NOT stale: the DB was behind** (earlier "70 days old" label was wrong) |
| Capital Case | 5 | 0 | 11-02 | 0 | 1 | 4 | 12,000 | 5 | nothing new; about 1 video a month |

What changed: Casual Finance posts roughly 13 items in 30 days (mostly housing/real-estate-crisis Shorts plus a long video about every 5 to 10 days, long videos at 0.7M to 1.4M views). MonkeyExplains is now 100% on the AI bubble (long video 2.66M views on 11-01, Shorts about 9K to 17K). Crayon Capital's NVIDIA video (11-14) has 553K views in 4 days. Paper Billions' top video reached 3.24M views (was 2.10M on 11-13). Public views only; they are not CTR or retention.

Still open: R2 (192 undated videos) and R3 are not run. Spent so far on this account: $0.236 of $5.00.

## 6. R2 RESULT (executed 2026-11-18, owner-approved): date repair for 6 economics channels

Two runs, 30 newest long videos each, no Shorts, no subtitles (transcripts already in DB). Cost **$0.716** (R2a 8pZsatgjxninGb5h9 $0.360; R2b Lh3aocZMhPPaVLXfc $0.356), 192 requests, 0 failed. Raw JSON + checksums in `raw/`; flat table `R2_DATE_REPAIR_2026-11-18.csv` (180 rows, real publish dates and exact views). Total spent on this Apify account: $0.952 of $5.00 (about $4.05 left). `data/catalog/` not modified; matching to the 30 undated DB rows per channel by video_id is still to do (143 of 180 fresh ids already exist in the DB, so the undated rows can be dated by join).

| Channel | Subs now | Newest | Oldest in sample | 7d | 30d | 60d | 90d | Median views (30 newest) |
|---|---:|---|---|---:|---:|---:|---:|---:|
| Economics Explained | 2.89M | 11-17 | 05-11 | 2 | 6 | 12 | 16 | 579,750 |
| How Money Works | 1.77M | 11-17 | 04-26 | 1 | 4 | 8 | 11 | 830,048 |
| Money & Macro | 681K | 11-05 | 02-02 | 0 | 5 | 6 | 8 | 245,376 |
| Patrick Boyle | 1.37M | 11-15 | 04-25 | 1 | 4 | 9 | 13 | 1,527,601 |
| Modern MBA | 848K | 10-31 | 2024-12-15 | 0 | 1 | 2 | 3 | 293,546 |
| PensionCraft | 219K | 11-14 | 05-09 | 1 | 4 | 9 | 14 | 41,862 |

Reading (INFERRED, public views only): these big channels post about 1 video a week (Modern MBA far less). The first four have 7-day-to-30-day views already in the hundreds of thousands, so they are strong benchmarks for what a trending topic does at scale, not for a new channel's starting point. Dates are now usable for Phase D topic-recency checks. R3 (about 12 channels, about $1.20) is not run.

## 7. R3 RESULT (executed 2026-11-18, owner-approved): 12 additional explainer channels, last ~90 days

Four runs, each 3 channels, up to 20 long + 5 Shorts per channel, subtitles on. Cost **$1.004** (A XoDF6Brpp3oT1kLh0 $0.260; B 3ala8emOPEkjfhSbU $0.228; C 4fyGVqKzZG61uIzFQ $0.268; D GMObwEwtkQtGH1UiR $0.248), 512 requests, 0 failed. Raw JSON + checksums in `raw/`; table `R3_ADDITIONAL_CHANNELS_2026-11-18.csv` (243 videos, flag `already_in_db`). **Apify total on this account: about $1.956 of $5.00 (about $3.04 left).** `data/catalog/` not modified.

| Channel | Rows | In DB | Newest | 7d | 30d | 90d | Subs now | Median long views |
|---|---:|---:|---|---:|---:|---:|---:|---:|
| Neu | 20 | 17 | 11-18 | 4 | 10 | 20 | 40,700 | 40,933 |
| Primate Economics | 22 (5 Shorts) | 22 | 10-27 | 0 | 1 | 3 | 577,000 | 459,347 |
| PENNY (Penny Explains Finance) | 22 (5 Shorts) | 0 | 11-17 | 5 | 21 | 22 | 9,060 | 13,796 |
| Built On You | 14 | 10 | 11-17 | 4 | 9 | 14 | 16,600 | 22,648 |
| Business Decoded | 20 | 14 | 11-17 | 6 | 18 | 20 | 6,330 | 4,706 |
| Nostalgic Wheels, now named "The Wealth Cortex" | 20 | 18 | 11-17 | 2 | 10 | 16 | 29,200 | 434 |
| Econ in a Nutshell | 25 (5 Shorts) | 14 | 11-17 | 12 | 25 | 25 | 6,330 | 1,573 |
| The Expensive Part | 20 | 19 | 11-15 | 1 | 5 | 8 | 4,920 | 2,137 |
| Brimm. | 20 | 18 | 09-20 | 0 | 0 | 5 | 21,500 | 9,431 |
| Finance ANALYST | 20 | 20 | 11-01 | 0 | 5 | 20 | 3,250 | 3,416 |
| Mr. Ranks | 20 | 19 | 11-12 | 1 | 8 | 19 | 32,000 | 15,400 |
| Mr. Finance | 20 | **0** | 11-18 | 7 | 20 | 20 | 83,100 | 1,300 |

Flags (INFERRED, check before relying on them):
- **Mr. Finance (UC6AwWrR...)**: none of the 20 fresh videos exist in the DB (DB has 65 videos up to 08-24), 83K subs and median 1,300 views, 7 uploads in 7 days. Probably a repurposed, renamed or very different channel under the same ID, or a mass-upload channel. Do not use it as a benchmark until opened by hand.
- **Nostalgic Wheels** now appears as "The Wealth Cortex" (handle @thewealthcortexx), so rename or pivot; median long views 434.
- **Business Decoded and Econ in a Nutshell** both show exactly 6,330 subs; coincidence is possible, but verify.
- **Primate Economics has gone quiet**: 1 upload in 30 days, 3 in 90, last 10-27 (577K subs). Its older hits (e.g. Shorts at millions of views) are not recent evidence.
- **PENNY** (9K subs, 21 uploads in 30 days, median 13.8K views) is the closest new-channel-scale benchmark besides Paper Billions (23.6K subs, 6 videos).

Reading: the channels with strongest recent numbers at small scale are Neu (40K subs, 41K median), Built On You (22.6K median at 16.6K subs) and PENNY. Public views only; not CTR/retention.

## 8. INGEST into `data/catalog/finance_economics_complete.db` (2026-11-18, owner-approved)

Script: `05_FRESH_COMPETITOR_DATA/ingest/ingest_r1_r2_r3.py` (idempotent; batch tag `apify_2026-11-18_R123`). Pre-ingest copy of the DB kept outside the repo (scratchpad; SHA-256 `9b5bf2d0...ee52d0`, equals git HEAD blob). Result: 479 fresh rows = **138 new videos + 341 existing videos updated** (no duplicates; 3,832 video rows, all unique), **2 new channels** (Paper Billions, PENNY; DB now 72 channels), 107 new transcripts (existing transcripts untouched), **152 undated videos now dated**, integrity check ok. Updated rows keep their old values in new table `video_snapshots` (batch `PRE_...`) beside the fresh values; channel subscriber history in new table `channel_snapshots`. Newest video now 2026-11-18. Remaining undated: 28 older videos outside the 30-newest window (Economics Explained 7, How Money Works 5, Money & Macro 5, Patrick Boyle 5, PensionCraft 5, Modern MBA 1). Nostalgic Wheels got an `availability_note` about the new name. The DB file is modified in the working tree and NOT committed. `MASTER_INVENTORY.csv/.md` still show the pre-ingest snapshot and need regenerating.
