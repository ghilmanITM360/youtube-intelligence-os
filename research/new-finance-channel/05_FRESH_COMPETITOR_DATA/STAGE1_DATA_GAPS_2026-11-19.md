# Stage 1: data gaps for the six channels (2026-11-19)

Scope: Casual Finance, Monkey Economics, MonkeyExplains, Crayon Capital, PaperBillionsTV, Capital Case. No paid run was made. Source: `data/catalog/finance_economics_complete.db` (read-only) plus public YouTube pages opened today in the built-in browser. Shorts = duration <= 180 s.

## 1. Verified inventory (DB vs channel-reported total)

| Channel | Reported on channel | In DB | Long | Shorts | Transcripts | Thumbnail URLs | 30d / 60d / 90d (to 2026-11-19) | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Casual Finance | 222 | 223 | 38 | 185 | 223 | 223 | 13 / 29 / 54 | COMPLETE (DB +1 vs reported) |
| Monkey Economics | 60 | 60 | 18 | 42 | 60 | 60 | 2 / 3 / 3 | COMPLETE |
| MonkeyExplains | 149 | **73** | 53 | 20 | 68 | 73 | 10 / 22 / 25 | **GAP: 76 missing** |
| Crayon Capital | 35 | 35 | 35 | 0 | 35 | 35 | 3 / 5 / 7 | COMPLETE |
| Paper Billions | 6 | 6 | 6 | 0 | 6 | 6 | 6 / 6 / 6 | **COMPLETE (correction below)** |
| Capital Case | 13 | 13 | 13 | 0 | 13 | 13 | 1 / 2 / 4 | COMPLETE |

## 2. Paper Billions: gap resolved, earlier audit claim withdrawn

The channel page data (Apify R1 raw, `channelTotalVideos` = 6, 23,600 subs, total views 6,069,750) says the channel has 6 public videos, and the DB holds all 6, each with transcript and thumbnail URL. The strict audit (2026-11-19) called Paper Billions "incomplete"; that was wrong, the "6" is the real full inventory. Remaining limit: the channel is only 12 days of activity in this window (first DB video 2026-11-06), so cadence evidence is thin by nature, not by a data gap.

## 3. MonkeyExplains: real gap, partly mapped for free

Reported 149 (channel header, 2026-11-19, matches Apify `channelTotalVideos`). DB 73 (53 long + 20 Shorts).

Free check done today: opened the public Videos tab and scrolled to the end. It lists **64 long videos**. Against the DB:
- 51 of the 64 are already in the DB.
- **13 long videos are on YouTube but not in the DB:** 84YaEDQMY1c, OQgRqLUmvPk, PejedlEOsh0, UqaDQHAIlts, VY9zxl-YqGo, Y41XmFbsG2s, Zj4Turqu1EU, aK-6iq0cdbo, cCc5sgsrtCc, cvKe_WYeITU, ktOignjy2TE, mVRXhCkrtf8, v-2hJnwK5yw.
- 2 long DB videos (gEySwQ6q-V4, nhNF5lh3p-w) are not on the public Videos tab (likely Members Edition or removed; UNKNOWN which).
- The Shorts tab did not render in the browser pane (blank page twice), so the public Shorts count is UNKNOWN. By subtraction, 149 - 64 = about 85 Shorts or other items, against 20 in the DB: an INFERRED gap of about 65 Shorts. Not verified.

So the gap is about 13 long videos (VERIFIED) plus up to about 65 Shorts (INFERRED).

## 4. Blocker: paid refresh needs approval (nothing run)

Free routes exhausted: the browser lists IDs only (no views, dates or transcripts without opening each video), and the Shorts tab does not load.

Proposal (same actor and unit price as R1 to R3, `streamers/youtube-scraper`, about $0.0037 to $0.004 per row; R2 measured 192 rows = $0.716):

| Option | Scope | Rows | Estimated cost | Cap |
|---|---|---:|---:|---:|
| A (recommended) | MonkeyExplains only, long + Shorts, all items, subtitles on, then drop rows already in DB | up to 149 | about $0.60 | $0.80 |
| B | MonkeyExplains Shorts only, plus the 13 long IDs by URL | about 80 | about $0.32 | $0.40 |

Account spend so far $1.956 of $5.00 (about $3.04 left). Nothing starts until you answer which option, or "no, document as partial".

## 5. What stays blocked until the gap closes

MonkeyExplains' individual report can start from the 73 rows held, but its Shorts-versus-long and winners analysis would be labelled PARTIAL. All other five channels' reports are unblocked.

## 6. R4 result: MonkeyExplains full pull (executed 2026-11-19, Option A approved by owner)

Run `iOq4GnI0JmGbegdSv` (streamers/youtube-scraper, subtitles on, cap $0.80), status SUCCEEDED, 184 requests, 0 failed, **cost $0.428**. Raw `raw/R4_monkeyexplains_full_iOq4GnI0JmGbegdSv.json` (checksum in `raw/SHA256SUMS.txt`), table `R4_MONKEYEXPLAINS_FULL_2026-11-19.csv` (107 items). Account spend: $1.956 + $0.428 = about $2.384 of $5.00. `data/catalog/` NOT modified; ingest awaits owner approval.

- 107 items: 70 long ("video" type, **cap of 70 reached**, oldest 2026-02-28) and 37 Shorts (cap 100 not reached; oldest 2025-05-26, so the Shorts list looks complete at 37).
- 35 of the 70 long items are **Member Edition** videos (no public views, no transcripts, titles start "(Member Edition)"): a recurring members-only series, mostly the same topics as the public ones.
- 56 items are new vs the DB (39 long incl. Member Edition, 17 Shorts). Distinct union with DB = **129 of 149**.
- Of the 13 long IDs found missing on the public Videos tab, 6 are now captured; 7 are still missing: PejedlEOsh0, UqaDQHAIlts, Zj4Turqu1EU, aK-6iq0cdbo, cvKe_WYeITU, mVRXhCkrtf8, v-2hJnwK5yw. The earlier INFERRED "about 65 missing Shorts" was wrong: MonkeyExplains has 37 Shorts, not about 85; the 149 includes Member Edition and long videos.
- Still unaccounted: 149 - 129 = 20 items, probably long videos older than 2026-02-28 (the cap cut them off).

Proposed small follow-up (needs OK, within the $0.80 envelope): the 7 IDs by URL, no subtitles needed for Members, about $0.03 to $0.05; then reassess the remaining 13.

## 7. R5 result and Stage 1 closure (2026-11-19, owner approved the follow-up)

Run `F5CfAyeghGyPt4WsM`, the 7 missing long IDs by URL, subtitles on, SUCCEEDED, 14 requests, **cost $0.028**. All 7 returned views, dates (2025-06-20 to 2025-12-21) and subtitles. Raw `raw/R5_monkeyexplains_7ids_F5CfAyeghGyPt4WsM.json` (checksum recorded). Account spend now about $2.41 of $5.00; MonkeyExplains total $0.456 of the approved $0.80.

Merged inventory (DB + R4 + R5, DB unchanged): `MONKEYEXPLAINS_MERGED_INVENTORY_2026-11-19.csv`, **136 of 149** items. Open: 13 items, DOCUMENTED AS NOT RECOVERED. They are not visible on the public Videos tab (64 long, all 64 are now held) and the Shorts list (37) looks complete, so they are most likely further Member Edition items older than 2026-02-28 (35 such are already held and carry no public data). INFERRED, not verified. No further spend is justified: Member Edition items have no public views or transcripts, so they would not change any analysis.

Stage 1 verdict: Paper Billions COMPLETE; Casual Finance, Monkey Economics, Crayon Capital, Capital Case COMPLETE; MonkeyExplains 136/149 with the 13-item remainder documented (probable Member Edition, no public data). Ingest of R1 to R5 for MonkeyExplains into the DB is a separate approval.
