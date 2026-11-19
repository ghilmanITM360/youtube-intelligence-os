# 03 New Branch Structure Audit
Path: research/new-finance-channel/ (git branch data/apify-monkey-economics-primate-science-2026-11-18; commit 13138e04, nothing pushed).

| Folder | Files | Verdict |
|---|---:|---|
| 01 PROJECT_OVERVIEW | 2 | OK |
| 02 MASTER_INVENTORY | 2 | OK (csv + md) |
| 03 PRIMARY_REFERENCE | 4 | OK; one combined matrix |
| 04 ADDITIONAL | 1 | thin |
| 05 FRESH_DATA | 14 (16.6 MB) | OK, SHA-256 verified |
| 06 VIDEO_TRANSCRIPTS | 0 | EMPTY (transcripts exist only inside the DB: 3,617 rows / 3,577 videos) |
| 07 THUMBNAIL_LIBRARY | 68 | 61 images only |
| 08 VISUAL_STORYTELLING | 0 | EMPTY, FAIL |
| 09 TOPIC_DISCOVERY | 4 | OK |
| 10 SUB_NICHE | 6 | OK, inferred |
| 11 TRENDS_AND_NEWS | 1 | thin |
| 12 SEARCH_AND_SUGGESTED | 2 | thin |
| 13 WINNING_TITLE_MODELS | 0 | EMPTY duplicate of 13_TITLE_MODELS (5 files) |
| 14 WINNING_THUMBNAIL_MODELS | 0 | EMPTY (thumbnail briefs sit in Phase E file) |
| 15 SCRIPT_AND_HOOK | 0 | EMPTY (hook work sits in 13_TITLE_MODELS) |
| 16-24 | 1-2 each | present; single-file phases |

Result: 24/24 folders exist, 19 hold content, 5 empty. Empty folders are not deliverables. Index links: all 114 backticked file references checked; 18 looked missing by script, all but 3 are bare filenames that exist in subfolders (verified by find); 3 point into the older project (`research/finance-economics-channel-forensics/...`, exist) and one points to `01_CHANNEL_REPORTS/071_paperbillionstv/raw/...json` (not verified). No dead link confirmed. Status: PARTIAL.
