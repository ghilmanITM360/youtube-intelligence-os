# Source Dataset Inventory

Discovery-ID-level inventory of the logical datasets found across the four Phase 0.5 source folders. Discovery IDs (`DISC-00N`) are temporary identifiers for this discovery pass only — they are **not** production Dataset IDs (`docs/DATA_INVENTORY.md`'s ID scheme is assigned only at actual ingestion time).

---

## DISC-001 — Forensic Video Reconstruction: "7 Things Wealthy Retirees Stopped Buying"

- **Source Folder:** `files (1)` (byte-identical duplicate at `files`)
- **Source Path:** `/Users/ghilmanislam360/Downloads/files (1)`
- **Description:** A single-video forensic teardown of an AI-generated-slideshow YouTube video — shot-by-shot editing measurements, motion-preset analysis, audio characteristics, and a reusable illustration-style "visual DNA" prompt system, backed by a full 216-row shot-level CSV and two supporting evidence images.
- **Semantic Class:** C (Forensic Video Intelligence), with D (Raw Forensic Evidence) and E (Visual Reference Assets) elements.
- **Evidence Layer:** Mixed — `MEASURED_FACT` for frame-differencing/SIFT-RANSAC measurements; `AI_INTERPRETATION` for narrative/structural claims; explicitly `NOT ATTEMPTED`/`BLOCKED` where the source itself could not verify (transcription).
- **Associated Channel:** Unnamed in the source (the video's own channel is referenced only via a watermark avatar, not identified by name/handle).
- **Associated Competitor:** Not established — no channel name/handle given.
- **Associated Video:** "7 Things Wealthy Retirees Stopped Buying to Stay Rich" (source file `7_Things_Wealthy_Retirees_Stopped_Buying_to_Stay_Rich.mp4`, referenced but not present in this folder).
- **File Count:** 4
- **Approximate Size:** 692 KB
- **Canonical Candidate Files:** `FORENSIC_RECONSTRUCTION.md`, `EDL_216_shots.csv`
- **Supporting Evidence:** `EVIDENCE_seven_title_cards.jpg`, `EVIDENCE_temporal_average.jpg`
- **Duplicate Status:** Folder-level exact duplicate exists (`files`); zip-archive exact duplicates exist (`files.zip`, `files (1).zip`) — see `SOURCE_DUPLICATE_REPORT.md`.
- **Revision Status:** No revision detected within this dataset.
- **Quality:** High — internally consistent, self-labels confidence, backs narrative claims with a full measurement CSV.
- **Future Ingestion Priority:** P1 — High Value (a strong worked example of the forensic-evidence model in `docs/Database.md`, but scoped to one unnamed video with no channel/competitor link, limiting immediate reuse).
- **Notes:** The source video referenced by filename (`7_Things_Wealthy_Retirees_Stopped_Buying_to_Stay_Rich.mp4`) is not present in this folder or the other three; only the analysis artifacts are.

---

## DISC-002 — Competitor Dataset: Matty Invests & Mr. Finance (159 videos)

- **Source Folder:** `files (1)fulldata (1)`
- **Source Path:** `/Users/ghilmanislam360/Downloads/files (1)fulldata (1)`
- **Description:** A structured, scraper-sourced (Apify `streamers/youtube-scraper`) export covering two real YouTube channels' full video catalogs as of 24 Aug 2026: per-video metadata (views, likes, comments, duration, publish date, description, hashtags) in a 5-sheet spreadsheet, plus full transcripts for 158 of 159 videos in a companion zip.
- **Semantic Class:** B (Competitor Evidence).
- **Evidence Layer:** `RAW_SOURCE` (the zip/xlsx as supplied) and `EXTRACTED_FACT` (individual scraped fields — YouTube-sourced counts, dates, text). Auto-generated-caption transcripts are `EXTRACTED_FACT` with a caveat: known auto-caption error rates.
- **Associated Channel:** N/A (both are competitor channels, not the owned channel).
- **Associated Competitor:** **Matty Invests** (`@MattyInvests`, channel ID `UCkqzov98m_7niJOXwbRQgBA`) and **Mr. Finance** (`@misterfinanceyt`, channel ID `UC6AwWrRKNrwt83CMJqeTUzw`).
- **Associated Video:** All 159 videos across both channels (per-video IDs and titles enumerated in the source; not reproduced here in full).
- **File Count:** 2 top-level (161 total counting the 160 files inside `Transcripts_All_159_Videos.zip`).
- **Approximate Size:** 1.6 MB (xlsx 167 KB + transcripts zip 1.46 MB; 3.4 MB uncompressed inside the transcripts zip).
- **Canonical Candidate Files:** `YouTube_Master_Data.xlsx` (metadata of record), `Transcripts_All_159_Videos.zip` (full-text corpus).
- **Supporting Evidence:** The xlsx's own "Verification" sheet (completeness self-check) and "Analysis" sheet (computed channel comparison).
- **Duplicate Status:** Likely zip-level duplicates exist for this folder (`files (2).zip`, `files (1)fulldata.zip`, `files (1)fulldata (1).zip`) — see `SOURCE_DUPLICATE_REPORT.md` for confidence level.
- **Revision Status:** None detected; single scrape date (24 Aug 2026), no prior version found.
- **Quality:** High — internally self-verifying, clearly labeled provenance and scrape date, matches YouTube's own channel video counts per the source's own completeness check.
- **Future Ingestion Priority:** **P0 — Critical.** The strongest, most immediately usable competitor dataset found: fully structured, two full real channels, transcripts included, provenance stated by the source itself.
- **Notes:** This is the highest-value dataset found in this discovery pass.

---

## DISC-003 — YouTube Craft & Strategy Training Corpus

- **Source Folder:** `all training data of youtube`
- **Source Path:** `/Users/ghilmanislam360/Downloads/all training data of youtube`
- **Description:** A 15-document curated corpus covering YouTube algorithm mechanics, hook psychology, storytelling/script-analysis frameworks, a viral-content checklist, SEO, and AI image/video prompting guides. A mix of human-curated reference material and AI-assisted compiled "creative engine" frameworks.
- **Semantic Class:** A (Global YouTube Knowledge).
- **Evidence Layer:** Mixed — `HUMAN_INTERPRETATION` for attributed/curated material (e.g. the Viral Checklist credits Codie Sanchez); `AI_INTERPRETATION` for documents visibly written in AI-conversational voice (e.g. `Renae_Creative_Engine_v2.5_Unified_Intelligence_Blueprint.pdf` opens mid-conversation, "Got it — you're asking for..."). None of it is `RAW_SOURCE` evidence about any specific channel/video.
- **Associated Channel:** None — this is general knowledge, not channel-specific.
- **Associated Competitor:** None.
- **Associated Video:** None.
- **File Count:** 15
- **Approximate Size:** 6.6 MB
- **Canonical Candidate Files:** All 15 are individually candidate reference documents; no single file is "the" canonical one. Highest apparent density of reusable, structured guidance: `Renae_Creative_Engine_v2.5_Unified_Intelligence_Blueprint.pdf`, `Hook guide.pdf`, `Script Analyzer.pdf`.
- **Supporting Evidence:** N/A (this dataset is itself reference/supporting material for future prompt/analysis work, not evidence about a specific channel).
- **Duplicate Status:** A likely archive duplicate of this whole folder exists (`all training data of youtube 2.zip`). Within the folder, `Hook (1).pdf` and `Hook guide.pdf` are a probable revision/related pair, not exact duplicates — see `SOURCE_DUPLICATE_REPORT.md`.
- **Revision Status:** `Hook (1).pdf` / `Hook guide.pdf` flagged as possible revision pair; not resolved.
- **Quality:** High for the 5 documents directly sampled; Unknown for the remaining 10 (present, correctly typed, not content-read in this pass).
- **Future Ingestion Priority:** P1 — High Value, as reusable Global Knowledge (Class A) input for future Phase 4 intelligence extraction — but lower urgency than DISC-002 because it is general craft knowledge, not channel/competitor-specific evidence with a decay date.
- **Notes:** Per-document FOUNDATIONAL/HIGH VALUE/SUPPORTING/REDUNDANT/OUTDATED assessment for all 15 documents is deferred — only 5 were read in enough depth to judge; see `SOURCE_DISCOVERY_REPORT.md` sampling limitations. Do not treat the 10 unread documents as characterized.

---

## DISC-004 — Competitor Channel Screenshots: Dr. Adewale

- **Source Folder:** `Dr. Adewale`
- **Source Path:** `/Users/ghilmanislam360/Downloads/Dr. Adewale`
- **Description:** 13 full-browser screenshots of the YouTube channel page for "Dr. Adewale" (displayed name "Dr. Kevin Adewale"), captured with the vidIQ browser extension active, showing channel stats, video grid, titles, view counts, upload age, and vidIQ-computed velocity metrics (VPH, multiplier badges).
- **Semantic Class:** B (Competitor Evidence), with E (Visual Reference Assets) overlap.
- **Evidence Layer:** `RAW_SOURCE` (the screenshots themselves) and `OBSERVATION` (any value read off them — e.g. "151K subscribers" — since it is manually/visually transcribed, not independently corroborated via API).
- **Associated Channel:** None (competitor only).
- **Associated Competitor:** **Dr. Adewale** / "Dr. Kevin Adewale" (`@Dr.Adewale`), 151K subscribers, 72 videos, health/cardiology content, not monetized per the captured vidIQ panel.
- **Associated Video:** Multiple video thumbnails/titles visible in the video-grid screenshots (e.g. "7 Common Medications That Silently Damage an Older Heart", "NEVER Agree to This: 5 Deadly Surgeries for Seniors" at 2.7M views/708 VPH); not exhaustively transcribed in this pass.
- **File Count:** 13
- **Approximate Size:** 69 MB
- **Canonical Candidate Files:** None singularly canonical — each screenshot is an independent evidence frame of the same channel session.
- **Supporting Evidence:** N/A (self-contained visual evidence).
- **Duplicate Status:** A likely archive duplicate of this whole folder exists (`Dr. Adewale.zip`) — see `SOURCE_DUPLICATE_REPORT.md`.
- **Revision Status:** None — all 13 captured within a single ~1-minute session on one date (2026-08-16).
- **Quality:** High for the 3 screenshots directly viewed (legible, information-dense); Unknown for the remaining 10 (present, correctly sized, not visually confirmed).
- **Future Ingestion Priority:** P1 — High Value as competitor evidence, but P2/Useful for any value derived from vidIQ's own computed estimates (subscriber-rank, estimated earnings) since those are third-party estimates, not YouTube-reported facts — must be tagged `OBSERVATION`, never `EXTRACTED_FACT`, if ingested.
- **Notes:** Screenshots mix true YouTube UI data (titles, view counts, upload dates) with vidIQ overlay estimates (earnings, "similar channels," rank) in the same frame — any future extraction prompt must be able to separate the two sources within one image.
