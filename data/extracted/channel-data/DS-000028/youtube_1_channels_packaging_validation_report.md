# 1-Channel YouTube Packaging Validation

- Dataset: DS-000028 — Dr. Okoro Complete Channel Extraction
- Generated: 2026-09-22
- Actor: streamers/youtube-scraper
- Run: uLT4StERHwuiLthti
- Apify dataset: vvBzcGKPzEfKLnMrX
- Status: SUCCEEDED
- Requests: NOT_AVAILABLE succeeded; NOT_AVAILABLE failed
- Original estimated cost: $0.264
- Original actual cost: $0.264
- Recovery run: 4Jkn3vuO1nDp57HfT; dataset: wcOVfRxeT5khIdk8O
- Recovery records: 1; recovery-added video IDs: none
- Recovery actual cost: $0.004
- Total estimated cost: $0.264
- Total actual cost: $0.264

## Count reconciliation

| Channel | Live public | Scraped unique | Missing | Duplicates | Regular | Shorts | Livestreams | Transcripts |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Dr. Okoro | 66 | 66 | 0 | 0 | 65 | 1 | 0 | 66 |
| **Total** | **66** | **66** | **0** | **0** | **65** | **1** | **0** | **66** |

## Record classification

- Raw records: 66
- Raw video records: 66
- Recovery raw records: 1
- Recovery video records: 1
- Unique video IDs: 66
- Duplicate video discoveries merged: 0
- Channel-about records: 0
- Status/error records: 0
- Unknown records: 0

## Validation evidence

- Combined JSON, CSV, and XLSX contain identical 66-video ID sets.
- 1 workbook counts sum to 66; package union equals combined master.
- 66/66 records contain plaintext transcripts.
- 0 descriptions remain empty; 0 have live YouTube no-description evidence.
- 5/5 sampled watch pages resolved to their exact video IDs (five per channel, or every public video when a channel has fewer than five).
- 66/66 video rows have titles, publication timestamps, durations, views, likes, comments, thumbnails, canonical URLs, and channel identity.
- 66 workbook publication cells use real spreadsheet date-time values; 330 metric formulas and 132 HYPERLINK formulas were generated.
- Transcript packs contain 67 root text files: 66 video files plus 1 INDEX.txt files.
- Every workbook has five required sheets, formulas, filters, freeze panes, hyperlinks, and QA renders.
- Each transcript ZIP contains one UTF-8 file per video plus INDEX.txt; filenames match workbook entries.
- Immutable raw source/destination SHA-256 hashes match.
- Channel descriptions were never substituted for video descriptions.
- Phase 1 descriptive summaries only; no strategy or recommendations.
