# Source Discovery Report

Phase 0.5 read-only discovery pass over four external source folders. **No file in any of these folders was moved, renamed, deleted, modified, recompressed, or ingested into this repository.** All four remain outside the canonical repository, exactly as found. This report documents what they contain; `docs/source-discovery/SOURCE_DATASET_INVENTORY.md`, `SOURCE_DUPLICATE_REPORT.md`, and `SOURCE_INGESTION_RECOMMENDATIONS.md` carry the structured follow-on detail.

## Executive summary

All four target folders exist at their exact given paths. Combined they total roughly **77 MB** across **34 files** — far smaller than initially expected from the surrounding `~/Downloads` directory (34 GB, 676 items), because the four named folders are small, hand-curated result sets, not the raw multi-gigabyte video files that also live in `~/Downloads` but were out of scope for this task.

Four distinct, high-quality logical datasets were found:

1. **DISC-001** — a single-video AI-generated-slideshow forensic reconstruction (retirement-finance content), in `files (1)` (byte-identical to a second copy, `files`).
2. **DISC-002** — a structured competitor dataset: full scraped metadata + transcripts for 159 videos across two real YouTube channels, in `files (1)fulldata (1)`.
3. **DISC-003** — a curated corpus of 15 YouTube craft/strategy documents (hooks, algorithm mechanics, storytelling, AI-image/video prompting), in `all training data of youtube`.
4. **DISC-004** — 13 screenshots of a real competitor channel's YouTube page with a vidIQ analytics overlay, in `Dr. Adewale`.

Three of the four folders have byte-identical or near-identical zip-archive counterparts sitting alongside them in `~/Downloads` (outside the four named folders but directly relevant to duplicate/relationship analysis — see below).

## Source paths

| # | Requested path | Exists? | Resolved absolute path | Type |
|---|---|---|---|---|
| 1 | `/Users/ghilmanislam360/Downloads/files (1)` | Yes, exact match | same | Directory |
| 2 | `/Users/ghilmanislam360/Downloads/files (1)fulldata (1)` | Yes, exact match | same | Directory |
| 3 | `/Users/ghilmanislam360/Downloads/all training data of youtube` | Yes, exact match | same | Directory |
| 4 | `/Users/ghilmanislam360/Downloads/Dr. Adewale` | Yes, exact match | same | Directory |

No path required fuzzy-matching; all four names given in the task resolved exactly. Directly adjacent in `~/Downloads` (not one of the four requested paths, but relevant context found during discovery — see Relationships below):

- `files` (no suffix) — a directory, byte-identical to `files (1)`.
- `files.zip`, `files (1).zip` — byte-identical zip archives of the `files`/`files (1)` content.
- `files (2).zip`, `files (1)fulldata.zip`, `files (1)fulldata (1).zip` — three byte-identical zip archives, matching the content of `files (1)fulldata (1)`.
- `all training data of youtube 2.zip` — a zip archive containing the same 15 documents as `all training data of youtube`, plus macOS `__MACOSX` resource-fork cruft.
- `Dr. Adewale.zip` — a zip archive containing screenshots matching `Dr. Adewale` by size, plus `__MACOSX` cruft.

## Folder statistics

| Folder | Size | Files | Dirs (excl. self) |
|---|---|---|---|
| `files (1)` | 692 KB | 4 | 0 |
| `files (1)fulldata (1)` | 1.6 MB (Transcripts zip itself contains 3.4 MB uncompressed across 160 files) | 2 | 0 |
| `all training data of youtube` | 6.6 MB | 15 | 0 |
| `Dr. Adewale` | 69 MB | 13 | 0 |

All four folders are flat — no subdirectories, no nested archives beyond the two archive files already listed as their own items (`Transcripts_All_159_Videos.zip` inside DISC-002).

## What each folder actually contains

### `files (1)` — DISC-001, forensic video reconstruction
- `FORENSIC_RECONSTRUCTION.md` (64 KB, ~1,150 lines) — a detailed, self-labeled-confidence forensic teardown of one specific YouTube video ("7 Things Wealthy Retirees Stopped Buying to Stay Rich"): shot-by-shot editing measurements (216 shots, cut timing, motion-preset parameters measured via SIFT/RANSAC), audio analysis, a reusable "visual DNA" image-prompt system, and reconstruction guidance. It explicitly separates measured fact (tagged `HIGH CONFIDENCE`) from things it could not verify (tagged `BLOCKED`/`NOT ATTEMPTED`, e.g. transcription — Whisper was network-blocked in the sandbox that produced this document).
- `EDL_216_shots.csv` (217 rows) — the row-level Edit Decision List backing the markdown: per-shot timecodes, duration, motion preset, and OCR'd (often garbled) baked-in text.
- `EVIDENCE_seven_title_cards.jpg`, `EVIDENCE_temporal_average.jpg` — supporting visual evidence, viewed directly and confirmed to match the markdown's claims (title-card grid; a heavily blurred temporal-average frame showing a screen-locked watermark badge).

### `files (1)fulldata (1)` — DISC-002, competitor YouTube dataset
- `YouTube_Master_Data.xlsx` — 5 sheets (Channel Overview, All Videos, Descriptions, Verification, Analysis). Header states its own provenance: *"Source: Apify streamers/youtube-scraper | Scraped 24 Aug 2026 | 159 videos, 158 transcripts, 159 descriptions"*, covering two real channels, **Matty Invests** (`@MattyInvests`) and **Mr. Finance** (`@misterfinanceyt`). Fields per video include title, URL, publish date/day, duration, views, likes, comments, engagement rate, views/day, transcript word count, description character count, hashtags, and thumbnail URL. A built-in "Verification" sheet cross-checks completeness (e.g. explicitly notes the one video with no available captions), and an "Analysis" sheet computes channel-vs-channel comparative metrics.
- `Transcripts_All_159_Videos.zip` — 160 files (an `INDEX.txt` plus 159 per-video `.txt` transcripts, organized into `MattyInvests/` and `MrFinance/` subfolders). Each transcript file has a metadata header (channel, title, video ID, URL, publish date, views, likes, comments, caption type, language, word count) followed by the full description and full transcript text. Caption type is consistently `auto_generated`.

### `all training data of youtube` — DISC-003, YouTube craft/strategy corpus
15 PDFs and DOCX files (mostly PDF, two native DOCX), covering: hook psychology and a 3-step hook formula; a YouTube algorithm/upload-sequencing strategy guide; a video-title analyzer prompt set; a script-analysis multi-model prompt set; a viral-content checklist (attributed to Codie Sanchez); a "Renae Creative Engine v2.5" unified storytelling/algorithm framework written in ChatGPT-conversational voice; an SEO checklist; AI image/video prompting guides (Nano-Banana, Google VEO 3); and a cinematic-psychological character/engine profile document. Content is a mix of curated third-party knowledge and AI-assisted compiled frameworks, sampled directly (not judged by filename alone).

### `Dr. Adewale` — DISC-004, competitor channel screenshots
13 PNG screenshots (2.5–6.3 MB each, ~69 MB total), all timestamped within a single minute-scale window (2026-08-16, 3:04–3:05 PM), all showing a Chrome browser with the vidIQ extension active, viewing `youtube.com/@Dr.Adewale`. Confirmed by direct visual inspection:
- Channel: **Dr. Adewale** (displayed name "Dr. Kevin Adewale"), described as a cardiovascular surgeon; 151K subscribers, 72 videos, not monetized.
- vidIQ overlay panel: views gained (7 days) +256,015 (+142.7%), est. monthly earnings ~US$2.1k, avg. video length 20 minutes, similar channels listed.
- Video grid entries legible with title, view count, age ("2 months ago" / "5 months ago"), and vidIQ-computed VPH (views-per-hour) and velocity-multiplier badges (e.g. one video at 2.7M views, 708 VPH, 21.9x).
- Not all 13 screenshots were individually inspected — 3 representative frames were viewed directly; the remaining 10 were confirmed present, correctly sized, and non-corrupt by listing/hash only (see Confidence & Sampling Limitations).

## Important files (read beyond filename)

Every text-bearing file under roughly 5,000 words was read in full or in substantial excerpt: `FORENSIC_RECONSTRUCTION.md` (full), `EDL_216_shots.csv` (header + full row count + sample rows), the `YouTube_Master_Data.xlsx` shared-string table (sheet names, column headers, sample data rows, full Notes/Verification text), one sample transcript and the transcript-pack `INDEX.txt`, and the first two pages of five representative PDFs from `all training data of youtube` (`Renae_Creative_Engine_v2.5...`, `YouTube algorithm guide...`, `Hook guide.pdf`, `Script Analyzer.pdf`, `Viral Checklist.pdf`). The remaining 10 documents in that folder were confirmed present and correctly typed by `file`/size/hash but not individually read in full — see sampling limitations below.

## Important documents

The two standout documents by density of directly usable intelligence: `FORENSIC_RECONSTRUCTION.md` (a complete, reusable production-grammar extraction for one real video, including a copy-paste "Master Style Block" and "Master Character Block" image-prompt system) and `YouTube_Master_Data.xlsx` (a complete, structured, provenance-labeled competitor dataset across two channels).

## Visual assets

`EVIDENCE_seven_title_cards.jpg` and `EVIDENCE_temporal_average.jpg` (DISC-001) are forensic-analysis outputs, not raw screenshots — Class D/E material. The 13 `Dr. Adewale` PNGs are raw competitor screenshots — Class B/E material, with third-party tool (vidIQ) overlay data mixed into the same frame as the underlying YouTube UI; any future extraction must be able to attribute which numbers came from YouTube's own UI versus vidIQ's computed estimates.

## Competitor evidence

Two independent, non-overlapping competitor evidence sets were found: DISC-002 (Matty Invests / Mr. Finance — retirement and business-economics content, full metadata + transcripts, no screenshots) and DISC-004 (Dr. Adewale — cardiology/senior-health content, screenshots only, no transcripts or structured metadata). They do not reference each other and appear to have been gathered independently, at different times, by different methods (a scraper export vs. manual browser screenshots).

## Training knowledge

DISC-003 is the entire training-knowledge corpus found. It covers: YouTube algorithm mechanics, hook psychology, storytelling/script analysis, viral-content checklists, SEO, and AI image/video prompt engineering. It does not cover editing/visual-production grammar as a standalone topic — that material instead exists uniquely inside DISC-001's forensic document, which was produced by a different process (direct video measurement) than DISC-003's curated/compiled documents.

## Forensic / raw evidence

DISC-001 is the only forensic-analysis dataset found among the four folders. It is unusually rigorous for an AI-generated document: it distinguishes measured values (frame-differencing, SIFT/RANSAC residuals) from narrative interpretation, and explicitly marks what it could not determine rather than inventing it (e.g. §6.1, transcription blocked by a sandbox network restriction).

## Relationships

- `files` (folder, no suffix) is **byte-identical** to `files (1)` (folder) — confirmed by SHA-256 across all 4 member files.
- `files.zip` and `files (1).zip` are **byte-identical to each other**, and their uncompressed member sizes exactly match `files (1)`'s four files — confirmed by `unzip -l` listing. This is an archive → extracted-folder relationship: the zip is the compressed form of the same DISC-001 content.
- `files (2).zip`, `files (1)fulldata.zip`, and `files (1)fulldata (1).zip` are **byte-identical to each other** (same SHA-256). Given the matching name pattern and comparable size to `files (1)fulldata (1)`, these are almost certainly archive copies of that same DISC-002 folder, though member-by-member size verification (as was done for `files.zip`) was not performed for this pair — see sampling limitations.
- `all training data of youtube 2.zip` contains the same 15 real filenames as the `all training data of youtube` folder (plus `__MACOSX` noise), with at least two filenames matching folder sizes exactly (`Hook guide.pdf` at 682,682 bytes in both places; `Hook (1).pdf` at 682,676 bytes in both places). Archive → extracted-folder relationship, high confidence.
- `Dr. Adewale.zip` lists 13 screenshot entries (plus `__MACOSX` noise) whose visible sizes match several `Dr. Adewale` folder files exactly (e.g. 5,700,829 and 5,880,720 bytes appear in both). Archive → extracted-folder relationship, high confidence, not individually hash-verified for every one of the 13.
- Within `all training data of youtube`, **`Hook (1).pdf`** (682,676 bytes) and **`Hook guide.pdf`** (682,682 bytes) are near-identical in size but **not** byte-identical (different SHA-256). This is a probable revision/related pair, not a confirmed duplicate — content was not diffed line-by-line. See `SOURCE_DUPLICATE_REPORT.md`.
- DISC-001 and DISC-002 are otherwise unrelated to each other in subject matter (a finance-content forensic teardown vs. a different pair of finance/business channels' scraped data) despite both being finance-adjacent content — no shared channel, video, or filename links them.

## Data quality problems

- **Ambiguous authoritative revision:** `Hook (1).pdf` vs. `Hook guide.pdf` — two non-identical files, unclear which (if either) supersedes the other. Flagged, not resolved.
- **OCR unreliability already self-documented:** `EDL_216_shots.csv`'s `BAKED_TEXT_OCR` column contains frequently garbled text (e.g. `"Oly Sog"`, `"Set ARS"`) — this is expected OCR noise on stylized illustration text, already flagged as low-confidence in the source markdown itself. Any future extraction must not treat this column as reliable ground truth.
- **One video with no transcript:** DISC-002 is explicitly missing a transcript for one of its 159 videos (`oBJZxDwKgAU`, no YouTube captions exist at all) — correctly recorded as missing by the source rather than silently omitted or fabricated.
- **Redundant zip/folder pairs:** three of the four target folders have a byte-identical or near-identical zip archive elsewhere in `~/Downloads`, doubling apparent storage without adding evidentiary value — relevant to future storage decisions, not a defect in the evidence itself.
- **macOS resource-fork cruft:** every inspected zip (`all training data of youtube 2.zip`, `Dr. Adewale.zip`) carries a parallel `__MACOSX/` tree of `._*` AppleDouble metadata files — noise, not evidence.
- No corrupted, empty, or unreadable files were found among the items actually inspected.

## Unknowns

- Which of `Hook (1).pdf` / `Hook guide.pdf` is authoritative, and what specifically differs between them.
- Whether `files (2).zip` / `files (1)fulldata.zip` / `files (1)fulldata (1).zip` are byte-for-byte archives of `files (1)fulldata (1)` (name/size pattern strongly suggests yes; not hash-verified member-by-member).
- The provenance/authorship of the DISC-003 documents beyond what's stated in-document (e.g. "Codie Sanchez" is credited by the document itself for the Viral Checklist; not independently verified).
- The full content of the 10 DISC-003 documents not individually read in this pass, and of the 10 `Dr. Adewale` screenshots not individually viewed.
- Whether any additional logical datasets exist inside the un-sampled DISC-003 documents (e.g. whether `Engine-by-Engine Personality & Lens...pdf` is a companion to `Renae_Creative_Engine_v2.5...pdf` or independent — plausible given naming, not confirmed by content).

## Confidence & sampling limitations

This was a manual, single-pass inspection, not exhaustive:

- **Full-content read:** `FORENSIC_RECONSTRUCTION.md`, `EDL_216_shots.csv` (structure + full row count), the `YouTube_Master_Data.xlsx` string table, one full transcript, the transcript-pack index.
- **Excerpt read (first ~2 pages):** 5 of 15 DISC-003 documents.
- **Listed but not content-read:** the remaining 10 DISC-003 documents (confirmed present, correctly typed, hashed).
- **Directly viewed:** 2 of 2 DISC-001 images; 3 of 13 DISC-004 screenshots.
- **Hashed but not visually confirmed:** the remaining 10 DISC-004 screenshots and 10 DISC-003 documents.
- All SHA-256 hashes in this report and in `SOURCE_DUPLICATE_REPORT.md` were computed directly against the files as found; no hash was estimated or assumed.
- No file, in any of the four folders or their adjacent zip variants, was modified, moved, renamed, or deleted during this discovery pass.
