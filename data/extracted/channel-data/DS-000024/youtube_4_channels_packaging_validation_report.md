# 4-Channel YouTube Packaging Validation

- Dataset: DS-000024 — Funded Master Channel Extraction — Batch 2
- Generated: 2026-09-13
- Actor: streamers/youtube-scraper
- Run: 2ZEXd8nKLPegjIi8L
- Apify dataset: gLhVSzuRQfIJcVumQ
- Status: SUCCEEDED
- Requests: 378 succeeded; 0 failed
- Estimated cost: $0.744
- Actual cost: $0.712

## Count reconciliation

| Channel | Live public | Scraped unique | Missing | Duplicates | Regular | Shorts | Livestreams | Transcripts |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Hypothetically | 39 | 39 | 0 | 0 | 39 | 0 | 0 | 39 |
| Brimm. | 44 | 44 | 0 | 0 | 44 | 0 | 0 | 44 |
| Lost Legacy | 45 | 45 | 0 | 0 | 45 | 0 | 0 | 45 |
| ago. | 50 | 50 | 0 | 0 | 50 | 0 | 0 | 50 |
| **Total** | **178** | **178** | **0** | **0** | **178** | **0** | **0** | **178** |

## Record classification

- Raw records: 178
- Raw video records: 178
- Unique video IDs: 178
- Duplicate video discoveries merged: 0
- Channel-about records: 0
- Status/error records: 0
- Unknown records: 0

## Validation evidence

- Combined JSON, CSV, and XLSX contain identical 178-video ID sets.
- 4 workbook counts sum to 178; package union equals combined master.
- 178/178 records contain plaintext transcripts.
- 0 descriptions remain empty; 0 have live YouTube no-description evidence.
- 20/20 sampled watch pages resolved to their exact video IDs (five per channel, or every public video when a channel has fewer than five).
- 178/178 video rows have titles, publication timestamps, durations, views, likes, comments, thumbnails, canonical URLs, and channel identity.
- 178 workbook publication cells use real spreadsheet date-time values; 890 metric formulas and 356 HYPERLINK formulas were generated.
- Transcript packs contain 182 root text files: 178 video files plus 4 INDEX.txt files.
- Every workbook has five required sheets, formulas, filters, freeze panes, hyperlinks, and QA renders.
- Each transcript ZIP contains one UTF-8 file per video plus INDEX.txt; filenames match workbook entries.
- Immutable raw source/destination SHA-256 hashes match.
- Channel descriptions were never substituted for video descriptions.
- Phase 1 descriptive summaries only; no strategy or recommendations.
