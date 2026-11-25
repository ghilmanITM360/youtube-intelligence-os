# CADENCE_METHOD_AND_COVERAGE (Phase 3) — status: PARTIAL
Observation time T = 2026-11-23 21:33:37 PKT (UTC+5); windows are (T-N d, T], N = 7/30/90/180/365, lower bound exclusive, upper inclusive; burst/gap days use the Asia/Karachi calendar date. Data: UPLOAD_INVENTORY.csv (959 unique channel/video rows, 25 channels; was 662 before the resume crawl), CHANNEL_UPLOAD_CADENCE.csv (375 rows).

## Methods actually used (all public, unauthenticated)
1. **YouTube RSS feed** (feeds/videos.xml): the 15 newest uploads per channel with exact UTC publish time and view count. Directly observed. Covers a window completely only when the 15th-newest entry is older than the window start.
2. **Deep watch-page crawl** (publish time with offset, duration, views from the page's player response) — completed for ~11 channels (Astrum, Be Smart, Branch, AstroKobi, Epic Spaceman, Life Noggin, Lightbound, MinuteEarth, Physics Girl, PBS Space Time + partial others) before YouTube returned **HTTP 429**. **Resume (2026-11-23, after the 429 cleared):** scripts/crawl_resume.py ran single-threaded (2.5 s spacing) for What If, WhatIfAnimations, AumSum's What-If, AumSum's Science, Kurzgesagt, Veritasium, PBS Space Time, MinuteEarth and SciShow; no tab was throttled (raw/crawl_resume_run2.log). Uploads rows 508 → 906; inventory 662 → 959 unique videos. Tab status for those channels now comes from that log (cutoff 180 d What If/WhatIfAnimations/AumSum's What-If, 90 d others). 5,701 rows fetched after throttling were empty and were discarded (raw/failed_429_rows_discarded.jsonl). Deep coverage is trusted only where >=90% of fetched rows carry data.
3. **Format classification**: YouTube's own tab membership (/videos vs /shorts first 80 ids). No runtime or aspect-ratio guessing (L7). RSS entries in neither list would be "Unknown" (a few for What If). **Live/premiere tab not collected** (streams listing absent/empty for the channels tried) → Live = UNKNOWN, not zero.
4. Cross-check: for 154 videos present in both sources the RSS UTC time equals the watch-page time (0 mismatches).
5. xkcd reconciliation: live tabs observed 2026-11-23 list **46 videos + 46 Shorts = 92**; historical census (2026-11-04) = 91 IDs (45 long + 46 short) + Aony69nO5kI (published 2026-11-17, long). **0 IDs missing, 0 reclassified.**

## Coverage rules in the CSV
"Complete…" = counts for that window are a full census of the public listing as seen; "Lower bound" = at least that many (e.g. What If posts many Shorts a day; 15 RSS entries span ~2 weeks). Unknown ≠ zero: empty cells = not computable.

## Known limitations
- Public listings omit private/unlisted/deleted videos. 
- After the resume crawl every 30- and 90-day cell is labelled Complete (deep crawl crossed cutoff, full tab listing, or RSS reaches before window). The 180/365-day cells for some resume channels are still lower bounds. Completeness assumes the /videos and /shorts tabs list newest-first and that 6 consecutive older uploads mean the cutoff was crossed; this was not independently verified (e.g. SciShow lists 242 Shorts yet only 1 falls in 90 d).
- Prior audit 2 reported What If at 3 longs / 21 Shorts in 30 days; the resume crawl now **reproduces exactly that** (3 / 21). A few What If uploads belong to neither tab (format Unknown, 3 in 30 d) and are not counted as Long or Short.
- 180/365-day windows are mostly "Lower bound" for RSS-only channels; xkcd 12-month is from the 2026-11-04 census (13 longs, 31 Shorts in 365 d, REPORTED).
- Views are lifetime snapshots at fetch time, differing by minutes–hours between sources.
- Resume crawl DONE for the 9 channels above. Not resumed: minutephysics, Action Lab, Mr Scientific tails (already complete or unaffected at 30/90 d).

## Summary: uploads observed, Long / Short (a "+" = lower bound; regenerated after the 2026-11-23 resume crawl)
| Channel | last 30 d | last 90 d |
|---|---|---|
| AstroKobi | 1 / 14 | 3 / 36 |
| Astrum | 5 / 0 | 15 / 4 |
| AumSum's Science | 12 / 5 | 31 / 20 |
| AumSum's What-If | 4 / 10 | 15 / 26 |
| Be Smart | 1 / 3 | 3 / 10 |
| Branch Education | 1 / 1 | 2 / 3 |
| Epic Spaceman | 0 / 0 | 0 / 0 |
| Kurzgesagt – In a Nutshell | 2 / 4 | 7 / 13 |
| Life Noggin | 0 / 0 | 0 / 0 |
| Lightbound | 15 / 1 | 23 / 2 |
| MinuteEarth | 2 / 6 | 7 / 15 |
| Mr Scientific | 0 / 0 | 2 / 4 |
| PBS Space Time | 2 / 7 | 7 / 12 |
| Physics Girl | 0 / 5 | 0 / 10 |
| RealLifeLore | 4 / 0 | 10 / 0 |
| SciShow | 20 / 1 | 59 / 1 |
| ScienceClic English | 0 / 0 | 2 / 0 |
| Steve Mould | 2 / 1 | 4 / 3 |
| The Action Lab | 4 / 0 | 12 / 0 |
| Veritasium | 2 / 8 | 6 / 18 |
| What If | 3 / 21 | 12 / 34 |
| What If Kids | 0 / 0 | 0 / 0 |
| WhatIfAnimations | 20 / 0 | 24 / 8 |
| minutephysics | 2 / 0 | 2 / 2 |
| xkcd's What If? | 2 / 1 | 4 / 6 |
