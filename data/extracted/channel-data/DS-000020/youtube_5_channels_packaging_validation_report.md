# Five-Channel YouTube Packaging Validation

- Dataset: DS-000020 — Five-Channel YouTube Apify Dataset Packages
- Generated: 2026-09-12
- Actor: streamers/youtube-scraper
- Source runs: gHdfrGgqKgaJTpQYf, p3YkBpvXTnFgK1Yzg, 3P6JmgeBgwcgwV1BU
- Source datasets: rHxW9HkEtoKL0ox0I, Gc7WCqaw61qPm5EfJ, H26eTQBhYOisHTDXd

## Description recovery

Targeted run 3P6JmgeBgwcgwV1BU succeeded: 14 records; 28 requests succeeded; 0 failed; cost $0.056. Actor returned no video-description text for all 14 targets. Live YouTube pages displayed "No description has been added to this video." for every target. Final status: 0 Recovered; 14 No public description; 0 unavailable; 0 Actor failures; 0 Unknown.

## Count reconciliation

| Channel | Videos | Regular | Shorts | Livestreams | Transcripts | No public description |
|---|---:|---:|---:|---:|---:|---:|
| Apesthetic | 22 | 21 | 1 | 0 | 22 | 1 |
| Primate Economics | 28 | 15 | 13 | 0 | 28 | 13 |
| Sonny Finance | 39 | 39 | 0 | 0 | 39 | 0 |
| Money Life POV | 20 | 20 | 0 | 0 | 20 | 0 |
| My Chaotic Stories | 23 | 23 | 0 | 0 | 23 | 0 |
| **Total** | **132** | **118** | **14** | **0** | **132** | **14** |

## Validation evidence

- Combined JSON, CSV, and XLSX: 132 records, 132 unique IDs, identical ID set and order.
- Channel counts: 22 + 28 + 39 + 20 + 23 = 132.
- Five workbook record counts sum to 132; package ID union equals combined-master ID set.
- Every video appears in exactly one channel package.
- All 132 records contain video ID, title, canonical URL, channel identity, publication date, public metrics, thumbnail URL, and transcript plaintext.
- Transcript ZIPs contain one UTF-8 video file per workbook row plus one INDEX.txt; workbook Transcript File values match exactly.
- 132/132 transcript files contain complete plaintext; no placeholders.
- 14 description gaps are verified uploader-absent descriptions. Channel descriptions were never substituted.
- All workbook formulas recalculated; formula-error scans found no unexpected Excel errors.
- Every workbook contains exactly five required sheets in required order; every sheet rendered to QA PNG.
- Raw source/destination SHA-256 values match exactly.
- Per-video location and transcript/SRT URLs remain unavailable; plaintext transcripts are complete.
- Reference files remained outside repository and unchanged. TPDossier_Master_Data.xlsx supplied workbook visual system.
- All 14 supplied format references were present, hashed, and structurally inspected; see data/manifests/DS-000020_FORMAT_REFERENCES.csv.
- Every file in both source output directories was inventoried; see data/manifests/DS-000020_SOURCE_ARTIFACTS.csv.
