# 04 Decisions and change log

| time PKT | decision/change | evidence |
|---|---|---|
| 2026-11-23 20:55 | Found prior audit 2 folder not named in prompt; treat as previous proposed 60-day order | ls of ~/Downloads, mtimes 20:42-20:52 |
| 2026-11-23 21:10 | Own crawler instead of trusting prior audit 2's inventory: prior rows carry relative ages ("7mo ago"), many no exact date. Method: tab lists (YouTube's own Long/Short split) + watch-page microformat publishDate. | scripts/crawl_uploads.py; smoke test returned 2026-11-17T12:09:45-08:00 for Aony69nO5kI |
| 2026-11-23 21:20 | Fall-speed recompute reproduces prior audit numbers (204.0/204.3 km/h; sensitivity 186-229) -> integrator is independent code, atmosphere identical class; drag input CdA/m=0.00505 is SHARED, not independently validated | raw/science_recompute_output.txt |
| 2026-11-23 21:25 | Found audit1 vs audit2 disagree on WIB-52 (KEEP vs REPLACE) and NEW-06 (KEEP vs REPLACE) | ORIGINAL_CALENDAR_AUDIT.csv cols audit1_decision/audit2_action |
| 2026-11-23 21:40 | YouTube 429 on watch pages; discarded 5,701 empty rows; switched to RSS + tab-membership for cadence | raw/failed_429_rows_discarded.jsonl |
| 2026-11-23 21:55 | WIB-55 KEEP (differs from both prior audits HOLD); WIB-52 KEEP as Short; NEW-06 REPLACE; Voyager as Short | TOPIC_RESEARCH_CANDIDATES.csv |
| 2026-11-23 22:00 | Original plan's "WhatIfAnimations 433K" not matched (observed 3.82K) — flagged, unresolved | CHANNEL_SELECTION CSV |

## 2026-11-23 resume-crawl update
Crawl_resume.py completed for 9 channels (no throttle). analyze_cadence.py patched to overlay tab status from raw/crawl_resume_run*.log (old channels_raw tab status came from the 429-damaged crawl). Cadence 30/90 d now complete for all channels; scenario B recommendation unchanged. verify_all.py 11/11 PASS. Pre-resume CSVs kept in raw/*.pre_resume.csv.

## Search-hit metadata update
Fetched 514/516 search-hit watch pages; merged into TOPIC_RESEARCH_EVIDENCE.csv; no decision or score changed; verify_all view-check updated from "all UNAVAILABLE" to "numeric or UNAVAILABLE". See SEARCH_EVIDENCE_METADATA_UPDATE.md.

## Comment sample
Sampled 1,814 top-level public comments on 13 videos (no author data stored); themes in COMMENT_SAMPLE_FINDINGS.md; no decision or score changed.

## DS-000011 packaging PDFs
Read 5 PDFs (SOP, Viral Checklist, Title Analyzer, Hook guide, SEO checklist) from the raw folder without modifying it; classified as creative heuristics; checked candidate titles; no decision or score changed; softened "same speed" wording. See DS000011_PACKAGING_AND_HOOK_APPLICATION.md.

## DS-000011 remaining files
Opened the other 12 DS-000011 files read-only (folder has 17 files, earlier "18" was wrong). All classed as creative heuristics, tool-specific prompts or unverified platform claims; Hook (1).pdf has identical text to Hook guide.pdf. Numeric thresholds and cadence advice from the guides were not used (unsourced, mutually inconsistent). No decision, score, order or cadence changed. Algorithm guide and updates PDF read by structure and greps only. See DS000011_REMAINING_FILES_REVIEW.md.

## DS-000018 and DS-000031
Extracted the DS-000018 zip into the scratchpad (raw untouched), verified 63/63 tab hashes against its manifest, read titles, three cadence tabs and keyword searches; read DS-000031 (first part and competitor section fully, middle by headings). Creator claims on upload frequency conflict across tabs and are unsourced, so they neither support nor change cadence B. No decision, score or order changed. See DS000018_DS000031_REVIEW.md. The 2026-11-11 supplement is still unopened.

## DS-000011 supplement 2026-11-11
Checksums OK. The md matches the DS-000018 tabs in 61 of 62 sections; txt, docx and xlsx overlap at title level (not body-compared). So it is the same source in other formats, not independent evidence. VIDEO EDITING.docx is new (CapCut tutorials), not used. A "do not mix Long and Shorts" claim was recorded as a contradictory single-speaker claim; 18 of 25 observed channels post both formats; cadence B unchanged, mixed-format response to be compared in evaluation slots. See DS000011_SUPPLEMENT_REVIEW.md.

## WhatIfAnimations discrepancy
Re-fetched the live channel page: 3.83K subscribers, 820,892 total views; no channel in the set has ~433K subs. Resolved as: subscribers about 3.8K, plan's 433K unsourced and wrong as a subscriber figure; likely a mislabelled view count (inference). Found its top video (464K views, close to NEW-08's premise) was missing from search evidence; recorded as prior art, no score or decision changed. See WHATIFANIMATIONS_DISCREPANCY_RESOLUTION.md.

## NEW-08 saturation re-run (2026-11-24)
Re-ran with TAsqnXcCqRI (464K views) added: 37 videos, 14 near-premise uploads in 30 d, 5 of 19 near-premise at 10K+ views, rest 0-501. NEW-08 stays REPLACE; no score, order or cadence changed. Details: NEW08_SATURATION_RERUN.md. Limits: two queries, crawled channels only, keyword rule.
