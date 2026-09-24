# 1-Channel YouTube Packaging Validation

- Dataset: DS-000030 — Senior Health Hub Complete Channel Extraction
- Generated: 2026-09-23
- Actor: streamers/youtube-scraper
- Run: ai1C2ifFj7SPFkINt
- Apify dataset: H8G42VGbBdemNvMlu
- Status: SUCCEEDED
- Requests: 250 succeeded; 0 failed
- Original estimated cost: $0.488
- Original actual cost: $0.488
- Recovery run: Not applicable; dataset: Not applicable
- Recovery records: 0; recovery-added video IDs: none
- Recovery actual cost: $0
- Total estimated cost: $0.488
- Total actual cost: $0.488

## Count reconciliation

| Channel | Live public | Scraped unique | Missing | Duplicates | Regular | Shorts | Livestreams | Transcripts |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Senior Health Hub | 122 | 122 | 0 | 0 | 120 | 2 | 0 | 122 |
| **Total** | **122** | **122** | **0** | **0** | **120** | **2** | **0** | **122** |

## Record classification

- Raw records: 122
- Raw video records: 122
- Recovery raw records: 0
- Recovery video records: 0
- Unique video IDs: 122
- Duplicate video discoveries merged: 0
- Channel-about records: 0
- Status/error records: 0
- Unknown records: 0

## Validation evidence

- Combined JSON, CSV, and XLSX contain identical 122-video ID sets.
- 1 workbook counts sum to 122; package union equals combined master.
- 122/122 records contain plaintext transcripts.
- 2 descriptions remain empty; 2 have live YouTube no-description evidence.
- 5/5 sampled watch pages resolved to their exact video IDs (five per channel, or every public video when a channel has fewer than five).
- 122/122 video rows have titles, publication timestamps, durations, views, likes, comments, thumbnails, canonical URLs, and channel identity.
- 122 workbook publication cells use real spreadsheet date-time values; 610 metric formulas and 244 HYPERLINK formulas were generated.
- Transcript packs contain 123 root text files: 122 video files plus 1 INDEX.txt files.
- Every workbook has five required sheets, formulas, filters, freeze panes, hyperlinks, and QA renders.
- Each transcript ZIP contains one UTF-8 file per video plus INDEX.txt; filenames match workbook entries.
- Immutable raw source/destination SHA-256 hashes match.
- Channel descriptions were never substituted for video descriptions.
- Phase 1 descriptive summaries only; no strategy or recommendations.
