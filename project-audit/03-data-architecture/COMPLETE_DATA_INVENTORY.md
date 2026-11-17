# Complete Data Inventory

All counts were measured read-only on 2026-11-17. Main-branch DBs were read from the working tree; `git diff origin/main -- data/catalog` is empty, so they match main. Branch DBs were read from `git show <branch>:<path>` copies in a scratch directory. Nothing was written to any database.

## 1. Structured stores

| Store | Location | Size | Tables | Key volumes | On main? |
|---|---|---:|---:|---|---|
| Inventory catalog | `data/catalog/youtube_inventory.db` | 52 MB | 27 | 10 channels, 667 videos, 668 transcripts, 26 datasets, 45,774 discovered files, 6,953 source files, 12,335 field provenance rows, 5,172 visual assets, 244 visual observations, 604 classifications, 479 thumbnail evidence rows, 9 Apify runs | yes (tracked) |
| Channel registry | `data/catalog/youtube_channel_registry.db` | 141 MB (LFS) | 21 | 75 channels, 2,303 videos, 2,303 transcripts (12 placeholders), 2,291 FTS rows, 2,455 subtitle tracks, 600 coverage cells, 825 data-layer cells, 216 gaps, 318 artifacts, 67 submissions, 142 aliases | yes (LFS) |
| Reference knowledge | `data/knowledge/reference_knowledge.db` | 5 MB | 10 used (+31 empty, debt D6) | 33 rules, 1,260 sections (FTS), 722 video assessments, 63 constituent videos, 9 platform verifications, 3 rule conflicts | **no** (finance lineage + current branch) |
| Finance complete | `data/catalog/finance_economics_complete.db` | 98 MB | 5 | 69 channels (finance 47, economics 14, other 8), 3,634 videos, 3,450 transcripts, 2,970 Apify rows | **no** (`data/finance-economics-complete-2026-11-11`) |
| Senior Health core | `data/catalog/senior_health/senior_health_core.db` | 67 MB | 4 | 159 channels (tiers: full package 8, Apify complete 21, per-video metadata 55, identity only 75), 5,802 videos, 5,007 DS-34 records, 2,433 transcript index rows | **no** (#50, exercise branch) |
| Senior Health transcripts | `senior_health_transcripts_{1,2,3}.db` | 43 + 8 + 4 MB | 1 each | shard 1: 1,794 transcripts | **no** |
| Senior Health Apify | `research/senior-health-apify-2026-11-11/senior_health_apify.db` | 6 MB | 3 | 21 channels, 501 videos, 3 runs | **no** |
| Frozen registry pointer | `research/finance-economics-intelligence/audit-baseline/youtube_channel_registry.frozen.db` | 134 B (LFS pointer) | — | pinned audit baseline | **no** (#45) |

**Cross-store identity overlap (unique YouTube video IDs):**

| | inventory | registry | finance | SH core | SH Apify |
|---|---:|---:|---:|---:|---:|
| inventory (667) | — | 667 | 159 | 425 | 0 |
| registry (2,303) | 667 | — | 726 | 460 | 0 |
| finance (3,634) | 159 | 726 | — | 0 | 0 |
| SH core (5,802) | 425 | 460 | 0 | — | 501 |
| SH Apify (501) | 0 | 0 | 0 | 501 | — |

**Union: 10,553 unique videos.** Inventory ⊂ registry, and SH Apify ⊂ SH core. Per AGENTS.md rule 9, overlapping rows are **not independent evidence**. Any aggregate across stores must dedupe on `youtube_video_id` and record which store each field came from.

## 2. File-based evidence

| Class | Location | Volume | Notes |
|---|---|---|---|
| Raw supplied evidence | `data/raw/` | 2,179 + 124 tracked files on main | immutable; ledger-pinned |
| Extracted evidence | `data/extracted/` | 152 files on main; ~1,029 on CF lineage | |
| Manifests / ledgers | `data/manifests/` | 107 files | DS-xxxxxx file lists + hashes |
| Normalized | `data/normalized/` | 3 files | |
| Intelligence artifacts | `data/intelligence/` | 72 files: channels 5 dirs, cross-channel 7, plans 10+2, system 8, blueprints 2, global 4 | JSON + MD, versioned by date |
| First-party analytics | `data/intelligence/first-party/` | gitignored; **0 real exports** | private |
| Research corpora | `research/**` | main: casually-finance 10, consolidation 8; branches: finance-economics-intelligence ~1,600, visual-forensics up to ~2,200, senior-health-forensics 101, CF editing forensics 992 | most volume is off main |
| Docs / research notes | `docs/research` 379, `docs/audits` 39 on main | | |
| Production packages | `productions/`, `projects/`, `finance-short-02-visual-calibration/` | 473 to 1,030 files per production branch | media in git |
| Local-only heavy evidence | `~/YIOS-local-audits` (~15 GB frames/audio), 454 MP4s (4.4 GB), stash branch (~843 MB thumbnails) | not on any remote | single copy |
| Untracked in working tree | `research/what-if-scripts/` (126 files), `docs/audit/` | | uncommitted |

## 3. Datasets registered in the inventory (26)

Semantic classes (`docs/DATA_CLASSIFICATION.md`): **A** global YouTube knowledge (DS-11, 18, 31), **B** competitor evidence (17 datasets: DS-1, 3-10, 17, 19, 28-30, 32-34), **C** forensic video intelligence (DS-2, 12-16). DS-20 to 27 are not in this DB; they appear in ledgers/registry (e.g. DS-27 was integrated by the remediation branch).

## 4. Status vocabularies (the data a UI must render honestly)

| Vocabulary | Values (counts) | Where |
|---|---|---|
| Evidence layer (design, `docs/Database.md`) | EXTRACTED_FACT, MEASURED_FACT, OBSERVATION, AI_INTERPRETATION, HUMAN_INTERPRETATION, HYPOTHESIS, RECOMMENDATION, SUSPECT | all records |
| Evidence layer (observed) | field_provenance: EXTRACTED_FACT 10,998 / MEASURED_FACT 1,333 / SOURCE_METADATA 4; classifications: MEASURED_FACT 302 / AI_INTERPRETATION 302; visual obs: OBSERVATION 122 / EXTRACTED_FACT 122 | inventory DB |
| Classification status | VERIFIED 302 (format), PROPOSED 302 (topic) | inventory DB |
| File disposition | TOOLING 35,462, SUPPORTING_EVIDENCE 5,181, EXACT_DUPLICATE 4,057, SUPERSEDED 802, INGEST 141, NOISE 95, HOLD 24, REFERENCE_ONLY 10 | inventory DB |
| Channel status | COMPLETE 32, COMPLETE_WITH_LIMITATIONS 14, IDENTITY_VERIFIED_DATA_NOT_EXTRACTED 29 | registry |
| Intelligence coverage | NOT_AVAILABLE 335, DATA_READY 235, VALIDATED 23, PARTIAL 7 (75 channels × 8 capabilities) | registry |
| Visual evidence level | NONE 31, THUMBNAIL_URL_ONLY 41, THUMBNAIL_EVIDENCE 2, FORENSIC_VIDEO_EVIDENCE 1 | registry |
| First-party analytics | SCHEMA_READY_NO_DATA 75/75 | registry |
| Workstream statuses | VISUAL_ANALYSIS_COMPLETE, ASR_UNCERTIFIED, SEMANTIC_REVIEW_PENDING, PARTIAL, BLOCKED | START_HERE, research ledgers |

## 5. Data quality issues

| ID | Issue | Evidence | Fix |
|---|---|---|---|
| Q1 | `video_type` has 5+ spellings across stores | registry: video 1,150, regular video 890, NULL 159, shorts 90, Short 14; SH core: videos 3,801, video 1,308, shorts 551, streams 107, regular video 35 | normalize to {LONG_FORM, SHORT, LIVE, UNKNOWN} in the read model; keep the raw value |
| Q2 | Three channel-ID schemes | `CH-0000NN`, registry `canonical_channel_id`, YouTube `UC…` | crosswalk table keyed on YouTube channel ID |
| Q3 | Overlapping video tables (§1) | 10,553 union vs 12,907 row sum | dedupe + per-field source precedence |
| Q4 | Point-in-time metrics without consistent snapshot dates across stores | `video_snapshots.observed_at` vs branch DBs' single scrape | always show "as of" dates |
| Q5 | 12 placeholder transcripts; ASR transcripts uncertified | registry `is_placeholder=1`; CF `ASR_UNCERTIFIED` | label the transcript source in the UI |
| Q6 | 4 CF visual seals fail verification | START_HERE | show seal status badge |
| Q7 | Reference DB carries 31 empty tables | prior audit D6 | apply only migration 011 |
