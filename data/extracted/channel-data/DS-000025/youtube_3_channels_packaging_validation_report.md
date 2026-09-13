# 3-Channel YouTube Packaging Validation

- Dataset: DS-000025 — Funded Master Channel Extraction — Batch 3
- Generated: 2026-09-13
- Actor: streamers/youtube-scraper
- Run: HLqdr5AbPI0c1iYfN
- Apify dataset: 24ZtWCc6BjC7EX34V
- Status: SUCCEEDED
- Requests: 476 succeeded; 0 failed
- Original estimated cost: $0.944
- Original actual cost: $0.928
- Recovery run: fgU7aFRXEXiBF9qQJ; dataset: WcCerWihH19NyUQUU
- Recovery records: 1; recovery-added video IDs: 0IBXm8QtsZg
- Recovery actual cost: $0.004
- Total estimated cost: $0.948
- Total actual cost: $0.932

## Count reconciliation

| Channel | Live public | Scraped unique | Missing | Duplicates | Regular | Shorts | Livestreams | Transcripts |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Stickly | 75 | 75 | 0 | 0 | 75 | 0 | 0 | 75 |
| Mack | 76 | 76 | 0 | 0 | 76 | 0 | 0 | 76 |
| Explain In Paint | 82 | 82 | 0 | 0 | 82 | 0 | 0 | 82 |
| **Total** | **233** | **233** | **0** | **0** | **233** | **0** | **0** | **233** |

## Record classification

- Raw records: 232
- Raw video records: 232
- Recovery raw records: 1
- Recovery video records: 1
- Unique video IDs: 233
- Duplicate video discoveries merged: 0
- Channel-about records: 0
- Status/error records: 0
- Unknown records: 0

## Validation evidence

- Combined JSON, CSV, and XLSX contain identical 233-video ID sets.
- 3 workbook counts sum to 233; package union equals combined master.
- 233/233 records contain plaintext transcripts.
- 0 descriptions remain empty; 0 have live YouTube no-description evidence.
- 15/15 sampled watch pages resolved to their exact video IDs (five per channel, or every public video when a channel has fewer than five).
- 233/233 video rows have titles, publication timestamps, durations, views, likes, comments, thumbnails, canonical URLs, and channel identity.
- 233 workbook publication cells use real spreadsheet date-time values; 1165 metric formulas and 466 HYPERLINK formulas were generated.
- Transcript packs contain 236 root text files: 233 video files plus 3 INDEX.txt files.
- Every workbook has five required sheets, formulas, filters, freeze panes, hyperlinks, and QA renders.
- Each transcript ZIP contains one UTF-8 file per video plus INDEX.txt; filenames match workbook entries.
- Immutable raw source/destination SHA-256 hashes match.
- Channel descriptions were never substituted for video descriptions.
- Phase 1 descriptive summaries only; no strategy or recommendations.
