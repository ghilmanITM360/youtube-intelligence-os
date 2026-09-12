# 11-Channel YouTube Packaging Validation

- Dataset: DS-000021 — Eleven-Channel YouTube Apify Dataset Packages
- Generated: 2026-09-12
- Actor: streamers/youtube-scraper
- Run: hh3hyA9bbe6NWbzSh
- Apify dataset: JlPm7fypGnBYpU34x
- Status: SUCCEEDED
- Requests: 490 succeeded; 0 failed
- Estimated cost: $0.91
- Actual cost: $0.952

## Count reconciliation

| Channel | Live public | Scraped unique | Missing | Duplicates | Regular | Shorts | Livestreams | Transcripts |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| inkly | 28 | 28 | 0 | 0 | 28 | 0 | 0 | 28 |
| Ink Explainer | 15 | 15 | 0 | 0 | 15 | 0 | 0 | 15 |
| Dark Ledger | 38 | 38 | 0 | 0 | 38 | 0 | 0 | 38 |
| Shaami Finance | 13 | 13 | 0 | 0 | 13 | 0 | 0 | 13 |
| Oddlyhuman | 13 | 13 | 0 | 0 | 13 | 0 | 0 | 13 |
| Luco | 4 | 4 | 0 | 0 | 4 | 0 | 0 | 4 |
| Past Tense | 24 | 24 | 0 | 0 | 24 | 0 | 0 | 24 |
| Zenn | 35 | 35 | 0 | 0 | 35 | 0 | 0 | 35 |
| Genius History | 10 | 10 | 0 | 0 | 10 | 0 | 0 | 10 |
| Unknown Frequencies | 19 | 19 | 0 | 0 | 19 | 0 | 0 | 19 |
| CIPHER UNIT | 17 | 17 | 0 | 0 | 17 | 0 | 0 | 17 |
| **Total** | **216** | **216** | **0** | **0** | **216** | **0** | **0** | **216** |

## Record classification

- Raw records: 238
- Raw video records: 216
- Unique video IDs: 216
- Duplicate video discoveries merged: 0
- Channel-about records: 22
- Status/error records: 0
- Unknown records: 0

## Validation evidence

- Combined JSON, CSV, and XLSX contain identical 216-video ID sets.
- 11 workbook counts sum to 216; package union equals combined master.
- 216/216 records contain plaintext transcripts.
- 0 descriptions remain empty; 0 have live YouTube no-description evidence.
- 54/54 sampled watch pages resolved to their exact video IDs (five per channel, or every public video when a channel has fewer than five).
- 216/216 video rows have titles, publication timestamps, durations, views, likes, comments, thumbnails, canonical URLs, and channel identity.
- 216 workbook publication cells use real spreadsheet date-time values; 1080 metric formulas and 432 HYPERLINK formulas were generated.
- Transcript packs contain 227 root text files: 216 video files plus 11 INDEX.txt files.
- Every workbook has five required sheets, formulas, filters, freeze panes, hyperlinks, and QA renders.
- Each transcript ZIP contains one UTF-8 file per video plus INDEX.txt; filenames match workbook entries.
- Immutable raw source/destination SHA-256 hashes match.
- Channel descriptions were never substituted for video descriptions.
- Phase 1 descriptive summaries only; no strategy or recommendations.
