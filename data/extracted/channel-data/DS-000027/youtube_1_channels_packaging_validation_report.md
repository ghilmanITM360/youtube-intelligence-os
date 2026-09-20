# 1-Channel YouTube Packaging Validation

- Dataset: DS-000027 — Dr. Ares Senior Complete Channel Extraction
- Generated: 2026-09-20
- Actor: streamers/youtube-scraper
- Run: dqMkTSwYwRir4QfUM
- Apify dataset: TOdB7bMFfGfrqapsF
- Status: SUCCEEDED
- Requests: 73 succeeded; 0 failed
- Original estimated cost: $0.14
- Original actual cost: $0.14
- Recovery run: Not applicable; dataset: Not applicable
- Recovery records: 0; recovery-added video IDs: none
- Recovery actual cost: $0
- Total estimated cost: $0.14
- Total actual cost: $0.14

## Count reconciliation

| Channel | Live public | Scraped unique | Missing | Duplicates | Regular | Shorts | Livestreams | Transcripts |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Dr. Ares Senior | 35 | 35 | 0 | 0 | 35 | 0 | 0 | 35 |
| **Total** | **35** | **35** | **0** | **0** | **35** | **0** | **0** | **35** |

## Record classification

- Raw records: 35
- Raw video records: 35
- Recovery raw records: 0
- Recovery video records: 0
- Unique video IDs: 35
- Duplicate video discoveries merged: 0
- Channel-about records: 0
- Status/error records: 0
- Unknown records: 0

## Validation evidence

- Combined JSON, CSV, and XLSX contain identical 35-video ID sets.
- 1 workbook counts sum to 35; package union equals combined master.
- 35/35 records contain plaintext transcripts.
- 0 descriptions remain empty; 0 have live YouTube no-description evidence.
- 5/5 sampled watch pages resolved to their exact video IDs (five per channel, or every public video when a channel has fewer than five).
- 35/35 video rows have titles, publication timestamps, durations, views, likes, comments, thumbnails, canonical URLs, and channel identity.
- 35 workbook publication cells use real spreadsheet date-time values; 175 metric formulas and 70 HYPERLINK formulas were generated.
- Transcript packs contain 36 root text files: 35 video files plus 1 INDEX.txt files.
- Every workbook has five required sheets, formulas, filters, freeze panes, hyperlinks, and QA renders.
- Each transcript ZIP contains one UTF-8 file per video plus INDEX.txt; filenames match workbook entries.
- Immutable raw source/destination SHA-256 hashes match.
- Channel descriptions were never substituted for video descriptions.
- Phase 1 descriptive summaries only; no strategy or recommendations.
