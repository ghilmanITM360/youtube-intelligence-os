# 5-Channel YouTube Packaging Validation

- Dataset: DS-000023 — Funded Master Channel Extraction — Batch 1
- Generated: 2026-09-13
- Actor: streamers/youtube-scraper
- Run: YlTuIQD7ejSlxe2Ox
- Apify dataset: dDiWWR0m3YHwEBL0Z
- Status: SUCCEEDED
- Requests: 251 succeeded; 0 failed
- Estimated cost: $0.48
- Actual cost: $0.44

## Count reconciliation

| Channel | Live public | Scraped unique | Missing | Duplicates | Regular | Shorts | Livestreams | Transcripts |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Maximus | 5 | 5 | 0 | 0 | 5 | 0 | 0 | 5 |
| The Life Outline | 15 | 15 | 0 | 0 | 15 | 0 | 0 | 15 |
| Bro Pump | 21 | 21 | 0 | 0 | 21 | 0 | 0 | 21 |
| Crayon Capital | 30 | 30 | 0 | 0 | 30 | 0 | 0 | 30 |
| Zoozle | 39 | 39 | 0 | 0 | 39 | 0 | 0 | 39 |
| **Total** | **110** | **110** | **0** | **0** | **110** | **0** | **0** | **110** |

## Record classification

- Raw records: 110
- Raw video records: 110
- Unique video IDs: 110
- Duplicate video discoveries merged: 0
- Channel-about records: 0
- Status/error records: 0
- Unknown records: 0

## Validation evidence

- Combined JSON, CSV, and XLSX contain identical 110-video ID sets.
- 5 workbook counts sum to 110; package union equals combined master.
- 110/110 records contain plaintext transcripts.
- 0 descriptions remain empty; 0 have live YouTube no-description evidence.
- 25/25 sampled watch pages resolved to their exact video IDs (five per channel, or every public video when a channel has fewer than five).
- 110/110 video rows have titles, publication timestamps, durations, views, likes, comments, thumbnails, canonical URLs, and channel identity.
- 110 workbook publication cells use real spreadsheet date-time values; 550 metric formulas and 220 HYPERLINK formulas were generated.
- Transcript packs contain 115 root text files: 110 video files plus 5 INDEX.txt files.
- Every workbook has five required sheets, formulas, filters, freeze panes, hyperlinks, and QA renders.
- Each transcript ZIP contains one UTF-8 file per video plus INDEX.txt; filenames match workbook entries.
- Immutable raw source/destination SHA-256 hashes match.
- Channel descriptions were never substituted for video descriptions.
- Phase 1 descriptive summaries only; no strategy or recommendations.
