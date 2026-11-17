# Database Inventory & Reconciliation

**Source:** `data/catalog/finance_economics_complete.db` on branch `data/finance-economics-complete-2026-11-11` @ `933f236e03429ad8b902c11077f53ac4b483c21a` (worktree `~/workprojects/yios-audit-fixes`), sha256 `fa6fd1b24d07da39870100168306b99d1e9b84f61831d97a9946ded49b8c9d20`, opened read-only. Tables: `channels`, `videos`, `transcripts`, `apify_rows`, `meta`.

## Reconciliation of the reported counts (checked 2026-11-12)

| Item | Reported in brief | Independently counted | Status |
|---|---|---|---|
| Channel records | 69 | 69 | MATCH |
| Channels with ≥1 video | 68 | 68 (Wealth Logic has 0) | MATCH |
| Unique videos | 3,634 | 3,634 (video_id is primary key) | MATCH |
| Distinct videos with transcript | 3,410 | 3,410 (`has_transcript`) | MATCH |
| Transcript rows | 3,450 | 3,450 rows over 3,410 videos (40 videos have 2 sources) | MATCH |
| Long-form | 3,412 | 3,412 | MATCH |
| Shorts | 222 | 222 — `video_type` is inconsistent (SHORT 214, Short 7, plus duration rule); Shorts sit on **8** channels: Casual Finance 173, MonkeyExplains 15, Primate Economics 13, Primitive Education 11, Uncle John Financial 5, This make cents 3, Business Decoded 1, Logical Money 1 | MATCH (count); earlier “201 Shorts across 3 channels” referred to a classified subset |
| Classified long-form (previous pipeline) | 3,056 / 60 channels | 3,056 long-form with a PI baseline across 60 channels; 356 long-form NOT_CLASSIFIED (too new <14 d, or channel has <12 comparable uploads) | MATCH |
| Videos with views | — | 3,624 (10 missing) | — |
| Likes / comments | — | 3,248 / 3,240 | PARTIAL |
| Descriptions | — | 3,148 non-empty | PARTIAL |
| Publish date | — | 3,442 (192 undated → channel-median baseline) | PARTIAL |
| Thumbnail URL captured vs derived | — | 3,089 captured; 545 derived from the standard `i.ytimg.com/vi/<id>/` pattern (marked UNVERIFIED) | — |
| Thumbnail image actually downloaded | — | 3,577 (57 failed; stored locally in `~/YIOS-local-audits/finance-viral-forensics-2026-11-12/thumbs/`, not committed) | — |
| Subscriber count | — | missing for 24 of 69 channel records | PARTIAL |

Transcript sources: YouTube auto captions 2,334; creator captions 173; registry DS-000001/20-24 auto captions 715; Whisper ASR 228 (199 flagged `ASR_UNCERTIFIED`). **All transcripts are untimed text** — first-5/15/30-second analysis uses word positions (≈13/38/75 words at ~150 wpm) and is labelled INFERRED.

## Important scope limitation
Most channels were collected as the **newest ≤100 uploads** (commit b96847f4 “capped 100 videos/channel”; 933f236e topped up 5 channels to 100). Several channels have only 2-30 videos. Reports therefore describe the *recent library in the database*, not the lifetime catalogue; “topics it stopped covering” can only be judged inside that window.

## Performance index used in every report
PI = video views ÷ median views of the 15 nearest-in-time uploads of the same channel and format (≥6 comparables; videos <14 days old excluded). Classes: Breakout ≥5, Successful ≥2, Average 0.5-2, Underperforming <0.5. This controls for channel size and upload era but **not** for traffic source, CTR, retention or promotion. Shorts are never compared with long-form.

## Investigation queue
`MASTER_TRACKER.csv` lists all 69 channels in investigation order: tier 1 = ≥40 classified long-form + complete metadata + ≥80% transcripts; tier 2 = ≥20 classified; tier 3 = ≥12 classified or high median views; tier 4 = few/unclassifiable videos; tier 5 = no videos. This is a data-availability order, **not** a quality ranking.
