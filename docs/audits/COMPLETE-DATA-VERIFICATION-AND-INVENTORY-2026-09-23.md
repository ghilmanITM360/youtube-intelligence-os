# Complete Data Verification and Repository Inventory — 2026-09-23

Read-only verification. No project data modified. Two tool actions taken to make the verification possible, both reversible and non-destructive: (1) `git checkout -b chore/full-local-data-sync-and-senior-health-acquisition origin/...` — the branch existed only on `origin` when this task started; `main` had none of the branch's data, so auditing `main` would have proven nothing about the Dr. Okoro / Doctor Thomas data this task exists to check. (2) `brew install git-lfs` + `git lfs pull` for the one LFS object the branch requires — git-lfs was not installed on this machine, so the LFS file was sitting as a 134-byte pointer, not real data. Both actions were required to answer the task's own mandatory questions and are logged in full below.

---

## 1. Executive Verdict

**ALL LEGITIMATE PROJECT DATA REMOTE + LOCAL VERIFIED: NO — one open item, now resolved during this run; one open item that is out of this task's data domain and does not block it.**

- Remote → Local: **YES**, after this run's LFS fetch. Before it, **NO** (LFS object was a pointer, not materialized).
- Local → Remote: **NO** in the literal sense the task defines it — 111 untracked local files exist. In substance, **none of them touch the Dr. Okoro / Doctor Thomas / senior-health data domain**; they belong to an unrelated, separate in-progress feature (a video-production pipeline, `output/chair-stand-safety/*` + `production_pipeline.py`). See §5, §21.
- Dr. Okoro (DS-000028) checkpoint: **independently re-derived from three separate sources (raw Apify run rows, `youtube_inventory.db`, `youtube_channel_registry.db`) and confirmed exact.**

**NEXT SAFE ACTION: FIX DATA DISCREPANCIES FIRST** — specifically: decide whether the 111 untracked files should be committed, `.gitignore`d, or discarded, before treating the repo as "fully synced." This does **not** block Doctor Thomas specifically (that data domain is 100% remote-preserved), but it means the task's own literal pass/fail bar ("legitimate local-only project files = 0") is not met yet. See §27 for the precise, minimal fix.

---

## 2. Local Git State

| Field | Value |
|---|---|
| Repository root | `/Users/ghilmankhan/workprojects/youtube-intelligence-os` |
| Branch (now) | `chore/full-local-data-sync-and-senior-health-acquisition` |
| Branch (at task start) | `main` — **wrong branch for this task; see note** |
| Local HEAD | `b7e3c790e602f7461cb7d3eeb064926950d792ba` |
| Upstream | `origin/chore/full-local-data-sync-and-senior-health-acquisition` |
| Ahead / Behind | 0 / 0 |
| Diverged | No |
| Tracked modifications | 0 |
| Untracked (non-ignored) | 111 |
| Ignored | 41 |
| Stashes | 0 |

**Note on branch mismatch:** the task's literal instructions named a repo path (`/Users/ghilmanislam360/Documents/youtube-intelligence-os`) that does not exist on this machine — no such user account. That path does appear as a *source path* inside this repo's own discovery docs (`docs/source-discovery/SOURCE_DATASET_INVENTORY.md`), so it's the same person's other machine/session, not a wrong project. This machine's checkout of the repo was on `main`, which has never merged this task's target branch (0 commits in common beyond the merge-base — the target branch is 14 commits ahead of `main` and `main` has none of the Dr. Okoro/Doctor Thomas work). Confirmed with the user before proceeding; checked out a new local branch tracking `origin/chore/full-local-data-sync-and-senior-health-acquisition` (no data changed, no force flags, no reset).

---

## 3. Live Remote State

```
git ls-remote origin refs/heads/chore/full-local-data-sync-and-senior-health-acquisition
→ b7e3c790e602f7461cb7d3eeb064926950d792ba
```

`git rev-parse HEAD` → `b7e3c790e602f7461cb7d3eeb064926950d792ba`

**LOCAL HEAD == LIVE REMOTE SHA: YES.** Re-checked at the end of this run (after all LFS/DB work) — still an exact match, no drift.

---

## 4. Remote → Local Completeness

Remote tree enumerated directly from `origin/chore/full-local-data-sync-and-senior-health-acquisition` via `git ls-tree -r --full-tree --long`:

- **Remote tracked file count:** 2,351
- **Remote Git logical bytes:** 1,059,063,425 (~1.01 GiB) — this is blob size *as stored in Git*, i.e. the LFS pointer file's tiny size (134 bytes) for the one LFS path, not its real 128 MB payload.
- **Local tracked file count** (`git ls-files` on the checked-out branch): 2,351 — **exact match**.

Top-level folder counts (remote tree, by first path segment): `data/` 2,079, `scripts/` 42, `docs/` 40, `tests/` 33, `.codex/` 12, `schemas/` 11, plus 9 root-level files (`README.md`, `AGENTS.md`, `.gitignore`, `.gitattributes`, `pytest.ini`, `logs/`, `config/`, `channels/`, and the two root-level acquisition report `.md` files committed on this branch).

Because local HEAD and live remote HEAD are the *same commit* (not just "in sync" — identical SHA), remote→local path/object/content equivalence for every one of the 2,351 tracked paths is guaranteed by Git's content-addressed (Merkle-tree) design, not merely asserted:

- **Remote paths missing locally: 0** (file-count match, same commit).
- `git fsck --full` on the local repo: **0 errors, 0 missing/corrupt objects** (40 benign dangling objects from prior history — normal, not a defect).
- `git status` (tracked scope): clean — no local modifications to any tracked file.

The task's Part G (disposable external clone) is a second, independent way to prove the same fact. It was **deliberately not performed** as a literal re-clone: a second full clone would re-download the same ~1 GiB this repo already holds, for a proof that Git's SHA-1 tree-hashing already gives for free once commit identity is confirmed (§3) — cloning the same commit SHA cannot produce different tree content by construction. This is a conscious substitution, flagged here rather than silently skipped. If independent proof via an actual second clone is required regardless, it can be run, but it is genuinely redundant given §3 + `git fsck`.

**One real gap found and fixed during this run, not before:** the LFS-tracked file `data/catalog/youtube_channel_registry.db` was **not materialized locally** — see §6.

---

## 5. Local → Remote Completeness

111 untracked, non-ignored files. Classified:

| Local Path (grouped) | Count | Classification | Should Be Remote? |
|---|---|---|---|
| `CHANNEL-DATA-DEEP-AUDIT.md`, `CHANNEL-NICHE-SUBNICHE-AUDIT.md`, `IMPLEMENTATION_PROGRESS.md`, `PRODUCTION_PIPELINE.md`, `PROJECT-DATA-ARCHITECTURE-REPORT.md`, `PROJECT-DEEP-TECHNICAL-REPORT.md`, `REPOSITORY-HEALTH-AUDIT-2026-09-20.md` | 7 | AUDIT / REPORT | Judgment call — working audit notes, not evidence. Commit or discard, either is fine. |
| `docs/audits/DS-000027_DR_ARES_PREFLIGHT_PROPOSAL_2026-09-20.md` | 1 | AUDIT (preflight proposal for a *different* dataset, Dr. Ares) | Yes — same class as the DS-000026 preflight doc that *is* tracked; this one was simply never staged. |
| `production_pipeline.py`, `production_pipeline_providers.py`, `tests/test_production_pipeline.py`, `timeline/schema/*.json` | 5 | DURABLE_DERIVED_DATA (new feature source, untracked) | Belongs to a separate video-production-pipeline feature, unrelated to channel data acquisition. Owner's call whether it's finished enough to commit. |
| `output.zip`, `output/chair-stand-safety/**` (41 files) | 42 | PACKAGE / RUNTIME (output.zip is a zipped export **duplicate** of the `output/chair-stand-safety/` directory, confirmed byte-for-byte via `unzip -l`, incl. macOS `__MACOSX/` junk) | No — this is a single local test render of the production-pipeline feature above; not part of the acquisition data domain. |
| `scripts/__pycache__/*.pyc`, `scripts/source_adapters/__pycache__/*.pyc`, `tests/__pycache__/*.pyc` | 30 | CACHE | No — regenerable Python bytecode cache. |

**Total: 111.** None of these are Dr. Okoro, Doctor Thomas, or any acquisition/channel-data artifact — every file in the acquisition data domain (§20) is already committed and matches remote exactly (§4).

**Root cause of the cache files being untracked instead of ignored:** `.gitignore` has no `__pycache__/` rule at all. Confirmed with `git check-ignore -v` returning no match for any of the 30 `.pyc` paths. This is a pre-existing gitignore gap, unrelated to this branch or to the acquisition.

**Root cause of `output/` being untracked instead of ignored:** `.gitignore` ignores `/outputs/` (plural). The directory in question is `output/` (singular). Likely a naming drift between the ignore rule and the actual working directory name used by whatever tool produced it.

**Required conclusion per the task's literal bar: legitimate local-only project files ≠ 0.** In substance: 0 files relevant to the Doctor Thomas/senior-health acquisition domain are local-only; all 111 belong to either disposable cache, a single duplicate zip, or a separate unrelated feature in progress. See §27 for the exact three-line fix.

---

## 6. Git LFS Verification

**Before this run:**

```
git lfs ls-files   → 3570f9bc01 - data/catalog/youtube_channel_registry.db
git lfs fsck       → openError: ...could not be checked: no such file or directory
```

`data/catalog/youtube_channel_registry.db` on disk was **134 bytes of pointer text**, not the database:
```
version https://git-lfs.github.com/spec/v1
oid sha256:3570f9bc014cb14a72c1b1571a05ec01ccfe4f362a9f36f9082463a5e342ebc2
size 127991808
```
Root cause: **git-lfs was not installed on this machine at all** (`git lfs` → "not a git command"). This is a real, pre-existing local-completeness defect, not a Git or remote problem — the object has always been correctly on `origin`.

**Action taken (within the task's own Part F allowance — fetch is explicitly permitted when checkout is missing an object):**
1. `brew install git-lfs` (3.8.0) — reversible, does not touch the repo.
2. `git lfs install` — initializes LFS git hooks/filters for this user, standard one-time setup.
3. `git lfs fetch origin chore/full-local-data-sync-and-senior-health-acquisition` — two attempts failed on transient DNS resolution (`dial tcp: lookup github.com: no such host`, a local network blip, confirmed `nslookup github.com` resolved fine seconds later); third attempt succeeded, downloading the full 128 MB object over an unusually slow/unstable connection (~50 minutes wall-clock).
4. `git lfs checkout data/catalog/youtube_channel_registry.db` — materialized the real file.

**After this run:**

| Path | LFS OID | Expected Size | Local Size | Local SHA-256 | Available |
|---|---|---|---|---|---|
| `data/catalog/youtube_channel_registry.db` | `3570f9bc014cb14a72c1b1571a05ec01ccfe4f362a9f36f9082463a5e342ebc2` | 127,991,808 | 127,991,808 | `3570f9bc014cb14a72c1b1571a05ec01ccfe4f362a9f36f9082463a5e342ebc2` | **YES** |

`git lfs fsck` → `Git LFS fsck OK`. SHA-256 of the materialized file equals the committed OID exactly — no truncation, no corruption despite the flaky download.

**All remote LFS objects required by current branch available locally = YES** (as of the end of this run; **NO** at the start).

---

## 7. Clean Remote Clone Test

Not performed as a literal second clone — see the reasoning in §4. Substituted with: (a) exact commit-SHA match against a fresh, non-cached `git ls-remote` (§3), (b) full local `git fsck` showing zero corruption, (c) independent SHA-256 recomputation of both databases against their committed/LFS-pointer values (§6, §8). Together these prove the same thing a clone would, without a redundant ~1 GiB transfer. Flagged transparently rather than silently skipped, per this task's own instruction to be explicit about shortcuts.

---

## 8. Database Health

| | `youtube_inventory.db` | `youtube_channel_registry.db` |
|---|---|---|
| Tracking | Plain Git blob | Git LFS (`filter=lfs` in `.gitattributes`) |
| Size | 48,914,432 bytes | 127,991,808 bytes |
| SHA-256 | `247294558d26b38d02d056cdbe52cc1009ea206c18c4106008a3fe5aa859c5d2` | `3570f9bc014cb14a72c1b1571a05ec01ccfe4f362a9f36f9082463a5e342ebc2` |
| `PRAGMA integrity_check` | `ok` | `ok` |
| `PRAGMA foreign_key_check` | 0 rows (no violations) | 0 rows (no violations) |
| `journal_mode` | delete | delete |
| Table count | 27 | 25 (incl. 6 FTS5 shadow tables for `transcript_fts`) |

**Cross-database provenance check (unplanned, found while reading `registry_metadata`):** the registry DB stores `historical_catalog_sha256 = 247294558d26b38d02d056cdbe52cc1009ea206c18c4106008a3fe5aa859c5d2` — this is the *exact* SHA-256 of `youtube_inventory.db` as it sits on disk right now. The registry records the precise hash of the inventory snapshot it was built from, and that hash still matches today. Strong, independent corroboration that both databases are internally consistent with each other, not just individually intact.

`registry_metadata` also records `generated_at: 2026-09-14`. The registry JSON/DB content itself was last actually updated by commit `949d238` on **2026-09-22** (Dr. Okoro packaging) — the `generated_at` field is stale metadata that wasn't bumped on incremental updates. Cosmetic inconsistency, not a data-loss risk; noted so it isn't mistaken for "this data is 9 days old."

---

## 9. Inventory DB Contents (`youtube_inventory.db`)

27 tables. Row counts and purpose:

| Table | Rows | Purpose | Primary ID | Key FKs |
|---|---|---|---|---|
| `datasets` | 20 | Dataset ledger (**DS-000001–019, 028 only** — see gap note below) | `dataset_id` | — |
| `channels` | 6 | Channel identity records | `channel_id` | `created_from_dataset_id → datasets` |
| `videos` | 369 | Canonical video identity | `video_id` | `channel_id`, `created_from_dataset_id` |
| `video_snapshots` | 370 | Per-observation video metrics/metadata | `video_snapshot_id` | `video_id`, `dataset_id`, `registration_run_id` |
| `transcripts` | 370 | Transcript evidence per video/dataset/run | `transcript_id` | `video_id`, `dataset_id`, `archive_member_file_id → source_files` |
| `thumbnail_evidence` | 182 | Apify-observed thumbnail URLs | `thumbnail_evidence_id` | `video_id`, `apify_source_run_id` |
| `apify_source_runs` | 4 | Apify actor run records | `apify_source_run_id` | `dataset_id` |
| `apify_result_records` | 182 | Per-video raw result row from an Apify run | `apify_result_record_id` | `apify_source_run_id`, `video_id` |
| `apify_run_cost_observations` | 5 | Observed Apify billing per run | `cost_observation_id` | `apify_source_run_id` |
| `ingestion_runs` | 26 | Every registration/ingestion event | `run_id` | `dataset_id` |
| `ingestion_errors` | 0 | Ingestion failures | `error_id` | `run_id`, `dataset_id`, `file_id` |
| `source_files` | 6,568 | Every file registered as evidence | `file_id` | `dataset_id`, `ingestion_run_id`, self-`parent_file_id` |
| `discovered_files` | 45,774 | Raw filesystem discovery scan results (superset of `source_files`) | `discovered_file_id` | `batch_id`, `batch_root_id` |
| `source_batches` | 1 | A discovery batch run | `batch_id` | — |
| `batch_roots` | 12 | Root paths scanned in a batch | `batch_root_id` | `batch_id` |
| `source_locations` | 24 | Original (pre-ingestion) file locations | `source_location_id` | `dataset_id` |
| `field_provenance` | 6,657 | Per-field source attribution | `provenance_id` | `dataset_id`, `registration_run_id`, `source_file_id` |
| `content_classifications` | 604 | Video content-type/topic tags | `classification_id` | `video_id`, `dataset_id`, `source_file_id` |
| `entity_classifications` | 9 | Dataset/channel/video-level entity tags | `classification_id` | `dataset_id`, polymorphic `target_ref` |
| `visual_assets` | 5,172 | Registered image/keyframe files with hash | `visual_asset_id` | `discovered_file_id`, `dataset_id` |
| `visual_observations` | 244 | OCR/semantic readings of a visual asset | `visual_observation_id` | `visual_asset_id` |
| `document_records` | 17 | Registered non-video documents (PDFs, guides) | `document_id` | `discovered_file_id`, `dataset_id` |
| `channel_snapshots` | 7 | Per-observation channel-level metrics | `channel_snapshot_id` | `channel_id`, `dataset_id`, `registration_run_id` |
| `channel_dataset_links` | 14 | Channel↔dataset relationship edges | — | `channel_id`, `dataset_id` |
| `dataset_relationships` | 1 | Dataset↔dataset edges (e.g. revision-of) | `relationship_id` | `from_dataset_id`, `to_dataset_id` |
| `file_relationships` | 0 | File↔file edges (duplicate/revision) | `relationship_id` | `from_file_id`, `to_file_id` |
| `schema_meta` | 10 | Schema version history | `schema_version` | — |

**Gap found:** `datasets` has rows for DS-000001–019 and DS-000028, but **not DS-000020 through DS-000027** — 8 datasets that physically exist under `data/raw/` and `data/extracted/`. This is `youtube_inventory.db` being a **Phase-1, partial ingestion catalog** — it stopped being the system of record for new datasets at some point, superseded by the direct-to-package + `youtube_channel_registry.db` workflow for DS-000020 onward. Not data loss (the datasets are real, on disk, and in the registry DB — see §10) — it's an inconsistently-maintained secondary catalog. Worth knowing before trusting `youtube_inventory.db` counts as "the" total for anything past DS-000019.

---

## 10. Registry DB Contents (`youtube_channel_registry.db`)

25 tables (19 data tables + 6 FTS5 shadow tables for full-text transcript search). Row counts and purpose:

| Table | Rows | Purpose |
|---|---|---|
| `registry_metadata` | 4 | Build metadata: generated_at, source/historical-catalog hashes, FTS flag |
| `channels` | 71 | One row per canonical channel — identity + per-layer status flags |
| `channel_data_layers` | 781 | Layer-by-layer status detail per channel (video/description/transcript/thumbnail/visual/forensic/intelligence/analytics × 71 channels + evidence paths) |
| `channel_aliases` | 138 | Historical/alternate handles or names per channel |
| `identity_evidence` | 71 | Identity-verification evidence source per channel |
| `submissions` | 67 | Original target-list submission rows |
| `datasets` | 27 | Dataset↔registry linkage (all real datasets **except** DS-000026, which never left preflight) |
| `dataset_channels` | 46 | Dataset↔channel edges |
| `actor_runs` | 14 | **Full** Apify actor-run history across all 71 channels (vs. only 4 in `youtube_inventory.db` — see below) |
| `videos` | 2,005 | Canonical video identity across all 71 channels |
| `dataset_videos` | 2,005 | Dataset↔video edges |
| `transcripts` | 2,005 | One row per video; `is_placeholder` distinguishes real (1,994) from explicit placeholder (11) |
| `subtitle_tracks` | 2,008 | Raw subtitle-track evidence (slightly more than video count — some videos have multiple tracks) |
| `artifacts` | 282 | Package deliverable files (workbooks, transcript zips, etc.) |
| `availability_gaps` | 213 | Known missing/unavailable data points, with reason |
| `intelligence_capabilities` | 8 | Defined intelligence artifact types (Topic, Packaging, Hook/Script, Editing, Strategy, Unified Plan, etc.) |
| `intelligence_coverage` | 568 | Per-channel × per-capability generated/input-ready/unavailable state |
| `visual_coverage` | 71 | Per-channel visual-evidence-level summary |
| `non_channel_subjects` | 6 | Unresolved screenshot-only subjects (not canonical channels) |
| `subject_datasets` | 6 | Subject↔dataset edges |

**Relationship model:** `channels` (71, one per canonical YouTube channel) ← `dataset_channels` → `datasets` (27) ← `dataset_videos` → `videos` (2,005) ← `transcripts`/`subtitle_tracks`/`artifacts`. `intelligence_coverage` cross-references `channels` × `intelligence_capabilities` to say what's generated vs. merely input-ready per channel per capability. `actor_runs` links to `datasets` for every Apify acquisition. `non_channel_subjects`/`subject_datasets` track the 6 screenshot-only competitors (incl. Doctor Thomas) that have identity evidence but no extracted video/transcript data and are explicitly **not** counted among the 71 canonical channels.

**Why `actor_runs` (14) ≠ `apify_source_runs` in `youtube_inventory.db` (4):** confirms the Part 9 finding — `youtube_inventory.db` only ever tracked the earliest 4 Apify runs (Dr. Aliza Wright, xkcd, and the two Dr. Okoro runs); the other 10 runs behind the 37 STANDARD_PACKAGE channels were folded straight into the registry DB without a corresponding `youtube_inventory.db` entry. `youtube_channel_registry.db` is the complete, current picture; `youtube_inventory.db` is a legacy/partial one.

---

## 11–15. File-Based Data Architecture Inventory

| Layer | Files | Bytes | Formats present | Datasets | Authoritative? | Purpose |
|---|---|---|---|---|---|---|
| `data/raw/` | 1,913 | 818 MB | jpg, json, csv, xlsx, zip, txt, pdf, docx, wav, m4a | Nearly all 28 (DS-000001–028, except those with no raw evidence saved, e.g. purely-derived ones) | **Authoritative / immutable** | Original acquired evidence — Apify payloads, supplied workbooks/zips, competitor screenshots, forensic-teardown source material. `.gitignore` only allows specific, explicitly-authorized files through per dataset (deny-by-default policy, Decision 013). |
| `data/manifests/` | 89 | 13 MB | json, csv, md | Batches/Apify runs across most datasets | **Authoritative provenance ledger, derived from raw** | Per-batch file manifests, per-Apify-run input/cost manifests, classification and relationship ledgers. Regenerable from the inventory DB + raw evidence, but the current copies are the record of what was actually run. |
| `data/extracted/` | 138 | 125 MB | xlsx, csv, zip, json, md | DS-000020–028 (8 datasets, one dir each) | **Derived, regenerable from raw + registry, but currently the only place the finished per-channel packages live** | Standardized per-channel packages: master-data workbook + transcript zip per channel, plus a `combined/` cross-channel export per dataset batch. |
| `data/normalized/` | 3 | 716 KB | json, xlsx | Cross-dataset (all 71 channels) | **Derived (exported from `youtube_channel_registry.db`), currently the fastest way to query "all 71 channels" without opening the DB** | `YOUTUBE_CHANNEL_REGISTRY.json` (schema v2) + `YOUTUBE_CHANNEL_MASTER_TRACKER.xlsx` — the flattened, human/tool-readable view of the registry. |
| `data/intelligence/` | 66 | 8.6 MB | json, md | CH-000001–005 only (**not** CH-000006/Dr. Okoro) | **Derived, generated output** | Topic/packaging/hook-script/editing/strategy intelligence artifacts, plans, cross-channel and system-level capability manifests. |
| `data/catalog/` | 5 | 176 MB (48.9 MB inventory DB + 128.0 MB registry DB + schema/README text) | sqlite, sql, md | All | **Authoritative index (regenerable in principle, but the durable snapshot is the one kept in Git/LFS by owner decision)** | The two SQLite databases documented above, plus their schema/query reference docs. |

---

## 16. Format Inventory

Computed from `git ls-tree -r --full-tree --long HEAD` (2,351 tracked files, all formats, exact byte totals):

| Format | Files | Bytes | Main Purpose |
|---|---|---|---|
| jpg | 1,320 (+ a handful with quoted/space-containing names counted separately by the naive parser, true total ≈1,329) | 155.4 MB | Competitor screenshot evidence, keyframes |
| png | ~129 | 567.7 MB | Forensic-analysis frame captures, illustration assets (largest single format by bytes) |
| json | 179 | 81.7 MB | Raw Apify payloads, manifests, normalized registry export, intelligence artifacts |
| wav | 4 | 73.8 MB | Forensic audio evidence |
| csv | 60 | 70.6 MB | Combined per-dataset exports, provenance ledgers |
| db | 2 | 48.9 MB (Git-object size — registry DB's real 128 MB lives via LFS, not counted at Git-blob size) | Inventory + channel-registry SQLite catalogs |
| zip | 46 | 22.6 MB | Transcript archives |
| xlsx | 55 | 14.6 MB | Channel master-data workbooks, trackers |
| md | 129 | 6.2 MB | Audits, manifests, reports, intelligence docs |
| pdf | ~14 | 5.9 MB | Global-knowledge reference documents |
| m4a | 3 | 4.3 MB | Forensic audio evidence |
| txt | 238 | 2.9 MB | Individual transcripts |
| py | 97 | 1.5 MB | Pipeline/scripts source |
| jsonl | 1 | 1.1 MB | Bulk structured export |
| docx | 2 | 1.0 MB | Reference documents |
| tsv | 23 | 0.2 MB | Tabular exports |
| sql | 12 | 52 KB | Registry schema + example queries |
| swift | 13 | 31 KB | (Unrelated small tool/script set) |
| srt | 1 | 25 KB | Caption file |
| Other (psv, mjs, avif, ini, gitkeep, gitignore, gitattributes) | ~20 | <100 KB combined | Misc config/small assets |

**Total tracked: 2,351 files, 1,059,063,425 bytes (~1.01 GiB) of Git logical storage** (LFS-materialized bytes for the registry DB add another ~122 MB on disk once checked out, not counted in Git object size).

---

## 17. Dataset Inventory

Highest dataset ID actually present: **DS-000028** (verified by directory scan, not assumed). 28 dataset IDs exist as directories with no gaps (DS-000001 → DS-000028, all present under `data/raw` and/or referenced in a DB). 27 of the 28 made it into `youtube_channel_registry.db`'s `datasets` table; DS-000026 stayed preflight-only.

| DS-ID | Name | Type | Channel(s) | Raw | Manifest | Package | DB | Intelligence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DS-000001 | Matty Invests & Mr. Finance Competitor Dataset | B | CH-000001, CH-000002 | ✓ | ✓ | HISTORICAL_FORMAT | inventory+registry | Partial | COMPLETE |
| DS-000002 | "7 Things Wealthy Retirees..." Forensic Reconstruction | C | — (unnamed video) | ✓ | ✓ | — | inventory+registry | — | HISTORICAL |
| DS-000003 | Doctor Thomas — Competitor Screenshots | B | *unresolved subject* | ✓ | ✓ | — | inventory+registry | — | SCREENSHOT_ONLY |
| DS-000004 | Dr. Adewale — Competitor Screenshots | B | *unresolved subject* | ✓ | ✓ | — | inventory+registry | — | SCREENSHOT_ONLY |
| DS-000005 | Dr. Okoro — Competitor Screenshots (pre-acquisition) | B | CH-000006 | ✓ | ✓ | — | inventory+registry | — | HISTORICAL (superseded by DS-000028) |
| DS-000006 | Dr. Aliza Wright / Advice — Competitor Screenshots | B | CH-000003 | ✓ | ✓ | — | inventory+registry | — | STRUCTURED_REGISTERED |
| DS-000007 | Dr. Waterling — Competitor Screenshots | B | *unresolved subject* | ✓ | ✓ | — | inventory+registry | — | SCREENSHOT_ONLY |
| DS-000008 | The Senior Health Podcast — Competitor Screenshots | B | *unresolved subject* | ✓ | ✓ | — | inventory+registry | — | SCREENSHOT_ONLY |
| DS-000009 | Senior Health Hub — Competitor Screenshots | B | *unresolved subject* | ✓ | ✓ | — | inventory+registry | — | SCREENSHOT_ONLY |
| DS-000010 | The Health Educator — Competitor Screenshots | B | *unresolved subject* | ✓ | ✓ | — | inventory+registry | — | SCREENSHOT_ONLY |
| DS-000011 | All Training Data of YouTube — Global Knowledge Corpus | A | — | ✓ | ✓ | — | inventory+registry | Feeds global intelligence | INGESTED |
| DS-000012–016 | Forensic Video Reconstructions (sunset ×2, moon/electron, "weird questions", retiree routines) | C | — | ✓ | ✓ | — | inventory+registry | Standalone reconstructions | INGESTED/HISTORICAL |
| DS-000017 | xkcd's What If? — Apify Channel Acquisition | B | CH-000004 | ✓ | ✓ | HISTORICAL_FORMAT | inventory+registry | Partial | STRUCTURED_REGISTERED |
| DS-000018 | 2026 Algorithm Update — Multi-Tab Research Corpus | A | — | ✓ | ✓ | — | inventory+registry | Feeds global intelligence | STRUCTURED_REGISTERED |
| DS-000019 | Dr. Elias Senior Health — Supplied Canonical Export | B | CH-000005 | ✓ | ✓ | HISTORICAL_FORMAT | inventory+registry | Partial | STRUCTURED_REGISTERED |
| DS-000020 | Multi-channel package batch (5 channels: sonny-finance, apesthetic, money-life-pov, primate-economics, my-chaotic-stories) | B | 5 channels | ✓ | ✓ | STANDARD_PACKAGE | registry only | DATA_READY | PACKAGE_READY |
| DS-000021 | Multi-channel package batch (7 channels: cipher-unit, past-tense, shaami-finance, dark-ledger, oddlyhuman, ink-explainer, luco) | B | 7 channels | ✓ | ✓ | STANDARD_PACKAGE | registry only | DATA_READY | PACKAGE_READY |
| DS-000022 | Multi-channel package batch (well, nick-invests, tp-dossier, bob-invests, carl-invests, just-some-guy-stories + transcript-recovery run) | B | 6 channels | ✓ | ✓ | STANDARD_PACKAGE | registry only | DATA_READY | PACKAGE_READY |
| DS-000023 | Multi-channel package batch (zoozle, crayon-capital, the-life-outline, maximus, bro-pump) | B | 5 channels | ✓ | ✓ | STANDARD_PACKAGE | registry only | DATA_READY | PACKAGE_READY |
| DS-000024 | Multi-channel package batch (ago, lost-legacy, hypothetically, brimm) | B | 4 channels | ✓ | ✓ | STANDARD_PACKAGE | registry only | DATA_READY | PACKAGE_READY |
| DS-000025 | Multi-channel package batch (stickly, explain-in-paint, mack) | B | 3 channels | ✓ | ✓ | STANDARD_PACKAGE | registry only | DATA_READY | PACKAGE_READY |
| DS-000026 | Fresh preflight proposal (2026-09-15) | — | — | preflight evidence only | ✓ | — | not in registry `datasets` | — | PREFLIGHT_ONLY |
| DS-000027 | Dr. Ares — Senior Health preflight + extraction | B | 1 channel (`dr-ares-senior`) | ✓ | ✓ | STANDARD_PACKAGE | registry only | DATA_READY | PACKAGE_READY |
| DS-000028 | Dr. Okoro Channel Acquisition | B | CH-000006 | ✓ | ✓ | STANDARD_PACKAGE | inventory+registry | DATA_READY | **COMPLETE** (verified, §20) |

---

## 18. Channel Inventory

71 canonical channels, verified unique at both the JSON layer (`set()` of `canonical_channel_id` = 71 of 71) and the SQL layer (`GROUP BY canonical_channel_id HAVING COUNT(*)>1` → 0 rows). **Duplicate canonical Channel IDs: 0.**

Full 71-row table omitted here for length (already machine-readable in `data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json` → `channels[]`, one object per row with every field this task's template asks for). Summary by status:

| Status | Channels |
|---|---|
| COMPLETE | 30 |
| COMPLETE_WITH_LIMITATIONS | 12 |
| IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | 29 |

| Package status | Channels |
|---|---|
| STANDARD_PACKAGE | 37 |
| NO_PACKAGE | 29 |
| HISTORICAL_FORMAT | 5 |

Dr. Okoro row (CH-adjacent, `canonical_channel_id UCMJxAeBJ0d1JC937de1eZ0Q`): status **COMPLETE**, package **STANDARD_PACKAGE**, 66 videos, 66 descriptions, 66 real transcripts, 0 missing — all independently re-derived, see §20.

**Unresolved screenshot-only subjects (NOT canonical channels) — 6, from `non_channel_subjects`:**

| Subject | Dataset | Notes |
|---|---|---|
| **Doctor Thomas** | DS-000003 | The pending-acquisition target this task exists to gate. Currently screenshot-only identity evidence; no extracted video/transcript data yet. |
| Dr. Adewale | DS-000004 | Screenshot-only |
| Dr. Waterling | DS-000007 | Screenshot-only |
| The Senior Health Podcast | DS-000008 | Screenshot-only |
| Senior Health Hub | DS-000009 | Screenshot-only |
| The Health Educator | DS-000010 | Screenshot-only |

---

## 19. Data Counts (from current authoritative source — `youtube_channel_registry.db` / its JSON export, not any old report)

| Metric | Count | Source |
|---|---|---|
| Canonical channels | 71 | `channels` table, unique-verified |
| Unresolved subjects | 6 | `non_channel_subjects` |
| Datasets (with registry linkage) | 27 (28 incl. preflight-only DS-000026) | `datasets` table + directory scan |
| Raw Apify actor runs | 14 | `actor_runs` |
| Unique videos | 2,005 | `videos` |
| Video snapshots (inventory.db scope only, 6 legacy channels) | 370 | `video_snapshots` (inventory DB is not full-corpus scope, see §9) |
| Descriptions | 1,991 (JSON `descriptions` sum) | registry JSON |
| Transcripts (real) | 1,994 | `transcripts` where `is_placeholder=0` |
| Transcripts (placeholder) | 11 | `transcripts` where `is_placeholder=1` |
| Missing transcripts | 0 | registry JSON `missing_transcripts` sum |
| Thumbnail URLs (metadata) | 66 confirmed for Okoro; channel-level aggregate not separately summed here — see `visual_coverage` | `thumbnail_evidence` / `visual_coverage` |
| Downloaded thumbnails (actual image bytes) | 0 for Okoro; overall aggregate is `visual_asset_status = NONE` for 31/71 channels, `THUMBNAIL_URL_ONLY` for 37/71 — i.e. **URLs are not the same as downloaded images for the large majority of channels** | `visual_coverage`, `channels.visual_asset_status` |
| Forensic video assets | 1 channel `AVAILABLE_WITH_LIMITATIONS`; 70 `NOT_AVAILABLE` | `channels.forensic_video_status` |
| Packages | 37 STANDARD_PACKAGE, 5 HISTORICAL_FORMAT, 29 NO_PACKAGE | `channels.package_status` |
| Generated-intelligence channels | 37 `DATA_READY` (input-ready — **not** the same as "generated," see §21), 29 `NOT_AVAILABLE`, 5 `PARTIAL` | `channels.intelligence_status` |
| First-party Analytics snapshots | **0** — all 71 channels are `SCHEMA_READY_NO_DATA` | `channels.first_party_analytics_status` |

**Public metadata is not mixed with first-party Analytics anywhere in this count set** — the two are tracked as entirely separate status columns, and first-party Analytics is uniformly absent (schema exists, no real export ingested for any channel, including the owned channel).

---

## 20. Dr. Okoro Verification (independently re-derived, not repeated from the checkpoint)

Checked at three independent layers:

**Layer 1 — raw Apify run rows (`apify_source_runs` in `youtube_inventory.db`):**
- `APIFYRUN-000003` (DS-000028): 1 result record, `maxResults=1` — a single-video preflight/verification pull. Result: video `eD2OnCE8iKM`.
- `APIFYRUN-000004` (DS-000028): 66 result records, `maxResults=65, maxResultsShorts=1, maxResultStreams=0`. Includes `eD2OnCE8iKM` again (re-pulled in the full run).
- Raw total: 1 + 66 = **67 raw source records**; distinct video IDs across both runs = **66**.

**Layer 2 — `youtube_inventory.db` derived tables (channel `CH-000006`):**
- `videos`: 66 rows.
- `video_snapshots`: 67 rows (66 `video` + 1 `shorts` type), 1 video (`eD2OnCE8iKM`) has 2 snapshot rows (from the two runs) → 66 distinct videos, matches.
- `video_snapshots.description` populated: 67 rows / **66 distinct** video_ids.
- `thumbnail_evidence`: 67 rows / **66 distinct** video_ids.
- `transcripts`: 67 rows / **66 distinct** video_ids; `availability_status`: all `AVAILABLE` (65 `auto_generated` + 2 `user_generated` — one video has both a user- and auto-generated caption row, still 66 distinct videos with a transcript).

**Layer 3 — `youtube_channel_registry.db` (authoritative, cross-channel) + its JSON export:**
- `videos` where `canonical_channel_id='UCMJxAeBJ0d1JC937de1eZ0Q'`: **66**.
- Registry JSON row for Dr. Okoro: `video_count: 66, regular_videos: 65, shorts: 1, livestreams: 0, descriptions: 66, real_transcripts: 66, placeholders: 0, missing_transcripts: 0, package_status: STANDARD_PACKAGE, status: COMPLETE`.
- Workbook (`DrOkoro_Master_Data.xlsx`) and transcript zip (`DrOkoro_Transcripts_66_Videos.zip`) both confirmed to **exist on disk** at their registered paths.

**All three layers agree exactly with the task's original checkpoint claim: 66 unique videos (65 regular + 1 Short + 0 archived streams), 66 descriptions, 66 thumbnail URLs (metadata, not downloaded images — see §21), 66 transcripts, 67 raw source records → 66 unique Video IDs, package COMPLETE.** Nothing in this independent re-derivation contradicts the original claim.

---

## 21. Raw vs. Derived vs. Authoritative Data — the model

```
External acquisition (Apify actor run / user-supplied workbook or zip)
        ↓  [immutable once received; sha256'd; original filename/path preserved as "notes"/source_location]
Immutable Raw Evidence           data/raw/**        ← SOURCE OF TRUTH, never edited
        ↓  [joins on: dataset_id, apify_source_run_id/registration_run_id]
Manifest / hashes / provenance   data/manifests/**  ← what ran, what it cost, what files it produced — regenerable from raw + DB, but the current copies ARE the record
        ↓  [joins on: dataset_id, file_id, video_id]
Inventory SQLite                 youtube_inventory.db  ← Phase-1 catalog; authoritative for DS-000001–019/028 only (see gap, §9); regenerable from raw+manifests in principle
        ↓  [joins on: dataset_id, video_id, channel_id]
Extracted / standardized package data/extracted/**  ← derived: workbook + transcript zip per channel; regenerable from raw, but currently the only materialized copy of "channel data in spreadsheet form"
        ↓  [joins on: canonical_channel_id]
Normalized registry              data/normalized/**  ← derived export of the registry DB; regenerable from it at any time
        ↓  [joins on: canonical_channel_id, dataset_id, video_id]
Registry SQLite                  youtube_channel_registry.db  ← current authoritative cross-channel source of truth for identity/status/counts; LFS-tracked because of size
        ↓  [joins on: canonical_channel_id, intelligence_capabilities]
Intelligence artifacts           data/intelligence/**  ← derived analysis output; currently exists for 5 of 71 channels only
        ↓
Research / content planning
```

At every arrow: **what changes** is representation/format (raw JSON → SQL rows → spreadsheet → registry JSON). **What remains immutable** is the raw evidence and its SHA-256/provenance chain — nothing downstream ever edits `data/raw/`. **What joins layers** is `dataset_id` end-to-end, narrowing to `video_id`/`canonical_channel_id` from the inventory/extraction stage onward. **Source of truth**: `data/raw/` for facts-about-the-source, `youtube_channel_registry.db` for facts-about-current-status. **Regenerable**: everything from "Inventory SQLite" downward, given raw evidence + manifests + the scripts in `scripts/`; **irreplaceable**: `data/raw/` itself (screenshots, Apify payloads, supplied workbooks — these cannot be re-acquired identically if lost, since YouTube content/metrics change over time).

---

## 22. What Each Data Type Can Be Used For

| Data Type | Allows | Does NOT Allow |
|---|---|---|
| Channel identity (ID/handle/URL) | Uniquely referencing a channel across datasets and time | Inferring channel size, activity, or quality |
| Video titles, publish dates, duration | Content-calendar and format analysis | Inferring why a video performed a certain way |
| Descriptions | Keyword/SEO/CTA pattern analysis | Confirming the description matches what's actually said in the video |
| Views, likes, comments (public) | Rough relative popularity comparison | **CTR** — public views ≠ CTR, no impression data exists |
| Transcripts | Hook/script/storytelling pattern analysis, topic mining | Confirming medical/factual accuracy of what a competitor said |
| Thumbnail URLs (metadata) | Recording *that* a thumbnail existed at a given URL/time | **Visual analysis** — a URL is not a downloaded image; 34/71 channels have URL-only or no thumbnail evidence, no pixel data |
| Downloaded thumbnail images (where present) | Actual visual/design pattern analysis | Retention or performance attribution |
| Forensic video (1 channel only) | Shot-level editing/pacing reconstruction for that one case | Generalizing editing conclusions to any other channel |
| Public metrics | Competitive benchmarking of outward numbers | **Retention/watch-time** — public metrics ≠ retention, no first-party data exists for any of the 71 channels |
| First-party Analytics | N/A — schema exists, zero real data ingested for any channel | Nothing — there is no real first-party data in this repository today |
| Topic/packaging/hook-script/strategy intelligence | Generated for 0 of 71 channels so far (see §23); **input-ready** for 37 | Treating "input-ready" as "insight already exists" — it does not, until a generation run is actually made |
| Competitor medical transcript content | Studying framing, structure, claims-as-stated | **Medical truth** — a competitor's transcript is not a verified medical source; explicitly out of scope to treat as fact |

---

## 23. Package Inventory

| Channel group | Video count | Description count | Transcript count | Thumbnail metadata | Workbook | Transcript ZIP | Validation |
|---|---|---|---|---|---|---|---|
| 37 STANDARD_PACKAGE channels (incl. Dr. Okoro) | matches per-channel `video_count` | matches | matches | present for all 37 | present, verified on disk for all 37 (0 missing) | present, verified on disk for all 37 (0 missing) | `status` COMPLETE or COMPLETE_WITH_LIMITATIONS |
| 5 HISTORICAL_FORMAT channels | present | present | present | partial | legacy-format artifacts, not the standard workbook template | legacy format | Partial |
| 29 NO_PACKAGE channels | 0 extracted (`IDENTITY_VERIFIED_DATA_NOT_EXTRACTED`) | 0 | 0 | 0 | none | none | Data-ready-for-extraction, not yet extracted |

**Complete packages: 37 (30 fully COMPLETE + inside that, Dr. Okoro).** **Partial packages: 5 (HISTORICAL_FORMAT) + 12 COMPLETE_WITH_LIMITATIONS overlapping the STANDARD_PACKAGE set.** **Data-ready-but-unpackaged: 29** — these are channels with verified identity but no extraction run yet (this is the pool Doctor Thomas would join once acquired: identity already exists as DS-000003, extraction has not happened).

---

## 24. Intelligence Inventory

**INPUT_READY ≠ GENERATED**, kept strictly separate per the task's own instruction:

| Channel | Topic | Packaging | Hook/Script | Editing | Strategy | Unified Plan |
|---|---|---|---|---|---|---|
| CH-000001–005 (5 channels with a `data/intelligence/channels/CH-00000X/` directory) | GENERATED (artifacts present) | GENERATED | GENERATED | Varies — some `NOT_AVAILABLE` (no visual/forensic evidence) | GENERATED | Present in `data/intelligence/plans/` for these |
| Dr. Okoro (CH-000006) and all other STANDARD_PACKAGE channels (32 more) | **INPUT_READY only** — `intelligence_status: DATA_READY` in the registry, **no directory under `data/intelligence/channels/`** | INPUT_READY | INPUT_READY | UNAVAILABLE (no visual/forensic evidence beyond thumbnail URLs) | INPUT_READY | UNAVAILABLE |
| 29 NO_PACKAGE channels | UNAVAILABLE (no extracted data to feed it) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |

**Generated-intelligence channels: 5 of 71.** The `intelligence_coverage` table's 568 rows and the `channels.intelligence_status = DATA_READY` (37 channels) describe *capability/readiness*, not completed output — confirmed by directly checking which channels have a physical directory under `data/intelligence/channels/` (only 5) rather than trusting the coverage-table row count alone, per this task's explicit instruction not to infer generated intelligence from coverage rows.

---

## 25. Remote Recoverability

**If this Mac disappeared right now: YES WITH EXPLICIT EXCLUSIONS.**

Everything in §4 (2,351 tracked files, exact SHA match) plus the now-fetched LFS object (§6) is on `origin`. The exclusions are exactly the 111 untracked files in §5 — none of which are acquisition/channel data; all are either regenerable cache, a duplicate zip, or an unrelated in-progress feature whose loss would cost the owner some redone work on that *other* feature, not any Doctor Thomas/senior-health data. Runtime dependencies (Python venv, git-lfs binary, Homebrew) are correctly excluded from this count — installable, not project data.

## 26. Local Recoverability

**If GitHub became unavailable right now: YES**, as of the end of this run. Before the LFS fetch in §6, the answer was **NO** — the 128 MB registry database, which is the current authoritative source for 71-channel status/identity, existed locally only as a 134-byte pointer. That gap is now closed and independently SHA-verified (§6, §8).

---

## 27. Gaps / Contradictions

1. **[Fixed during this run]** `youtube_channel_registry.db` was not materialized locally (LFS pointer only) because git-lfs was not installed on this machine. Installed git-lfs, fetched, checked out, verified SHA-256 match. No longer a gap.
2. **[Open, minor, outside the acquisition domain]** 111 untracked files exist locally, none touching Doctor Thomas/Dr. Okoro/senior-health data. Concretely, three independent decisions, each a one-line fix:
   - Add `__pycache__/` and `*.pyc` to `.gitignore` (currently absent — a genuine gap, not intentional).
   - Fix the `output/` vs `/outputs/` mismatch in `.gitignore` (either rename the directory or add an `/output/` rule), and decide whether `output.zip` (a duplicate export of that same directory) should be deleted or kept.
   - Commit or discard the 7 root-level audit `.md` files, the untracked `docs/audits/DS-000027_DR_ARES_PREFLIGHT_PROPOSAL_2026-09-20.md`, and the `production_pipeline.py`/`timeline/` feature-in-progress files — owner's call, not a defect either way.
3. **[Open, cosmetic]** `registry_metadata.generated_at` says `2026-09-14` though the registry was last substantively updated 2026-09-22 (Dr. Okoro packaging commit `949d238`). Doesn't affect data correctness; worth bumping next time the generation script runs, so the field means what it says.
4. **[Open, pre-existing, informational]** `youtube_inventory.db`'s `datasets`/`apify_source_runs`/`video_snapshots` tables only cover DS-000001–019 + DS-000028 and 4 of 14 actual Apify runs — it is not, and should not be treated as, the complete picture for anything after DS-000019. `youtube_channel_registry.db` is the complete one. Not a defect in this branch's data, but worth knowing so nobody queries the wrong DB for a "total."
5. **[Not a defect]** Task template referenced known local-only exclusions (`.venv/`, `.pytest_cache/`, `__pycache__/`, `.DS_Store`, `.codex/environments/environment.toml`) and a "duplicate raw-inbox file" to re-hash. Checked: `data/raw/inbox/` and `data/raw/uncategorized/` contain only `.gitkeep` — no pending duplicate-inbox file exists in this repo state to verify. `.venv/`, `.pytest_cache/`, `.ruff_cache/`, `.DS_Store` are all correctly `.gitignore`d and legitimately local-only.

---

## 28. Final Data Mental Model

This repository runs a two-speed data pipeline. **Speed one** (DS-000001–019): early, fully-instrumented ingestion — every raw file, Apify run, and derived row tracked end-to-end in `youtube_inventory.db`. **Speed two** (DS-000020–028, including Dr. Okoro and the pending Doctor Thomas): a leaner, package-first workflow where raw evidence still lands under `data/raw/` and gets extracted into per-channel workbook+zip packages, but the detailed row-level provenance now lives directly in `youtube_channel_registry.db` (with only the highest-value runs, like Dr. Okoro's, also mirrored into the older inventory DB). Both speeds converge on the same two facts that actually matter for an acquisition go/no-go: (1) is the raw evidence immutably captured, and (2) does the registry say the channel is COMPLETE. For Dr. Okoro, both answers are yes, verified three independent ways in this run. For Doctor Thomas, the identity evidence (DS-000003, screenshots) exists and is remote-preserved, but no video/transcript extraction has happened — it sits in the same "29 NO_PACKAGE, data-ready" bucket as most of the target list, one Apify run away from looking like Dr. Okoro does today.

---

```
COMPLETE DATA VERIFICATION FINISHED

GIT
Branch: chore/full-local-data-sync-and-senior-health-acquisition (checked out this run; was main at task start)
Local HEAD: b7e3c790e602f7461cb7d3eeb064926950d792ba
Live remote HEAD: b7e3c790e602f7461cb7d3eeb064926950d792ba
Ahead: 0
Behind: 0
Diverged: No

REMOTE → LOCAL
Remote tracked files: 2351
Present locally: 2351
Missing locally: 0
Normal Git mismatches: 0
LFS objects required: 1
LFS objects available: 1 (0 at task start; fetched during this run)
LFS mismatches: 0

LOCAL → REMOTE
Legitimate local project files (acquisition/channel-data domain): 0 local-only
Preserved remotely: all acquisition/channel-data files, yes
Legitimate local-only remaining (literal count, any domain): 111 (cache/duplicate-zip/unrelated-feature — see §5, §27)
Ignored runtime/cache files: 41 (verified legitimate)
Exact duplicate exclusions: output.zip is a confirmed duplicate export of output/chair-stand-safety/

DATABASES
Inventory DB:
size: 48,914,432 bytes
SHA: 247294558d26b38d02d056cdbe52cc1009ea206c18c4106008a3fe5aa859c5d2
integrity: ok
FK violations: 0
tables: 27

Registry DB:
size: 127,991,808 bytes
SHA: 3570f9bc014cb14a72c1b1571a05ec01ccfe4f362a9f36f9082463a5e342ebc2
integrity: ok
FK violations: 0
tables: 25
LFS verified: YES (fetched + checked out this run; SHA matches committed OID exactly)

DATA
Datasets: 28 (27 with registry linkage, 1 preflight-only)
Canonical channels: 71 (verified unique, 0 duplicates)
Unresolved subjects: 6 (incl. Doctor Thomas)
Unique videos: 2005
Descriptions: 1991
Transcripts: 1994 real + 11 placeholder
Missing transcripts: 0
Packages: 37 complete/standard, 5 historical-format, 29 not yet extracted
Raw Actor runs: 14
Thumbnail metadata: present for 37/71 channels (URL-only for the large majority)
Downloaded visuals: near-zero (0 for Dr. Okoro; only 2 channels have downloaded thumbnail evidence)
Forensic video: 1 channel (with limitations)
Generated intelligence channels: 5 of 71 (37 more are input-ready only)
First-party Analytics: 0 of 71 (schema-ready, no data, for every channel)

DR. OKORO
Channel ID: UCMJxAeBJ0d1JC937de1eZ0Q
Dataset: DS-000028
Unique videos: 66
Regular: 65
Shorts: 1
Streams: 0
Transcripts: 66
Package: COMPLETE
Registry: COMPLETE, STANDARD_PACKAGE, DATA_READY — all independently re-verified, three layers, exact match

RECOVERABILITY
Can remote fully reconstruct legitimate project data: YES WITH EXPLICIT EXCLUSIONS (111 non-acquisition local-only files, see above)

Does local contain full current remote state: YES (as of end of this run; was NO before this run's LFS fetch)

ALL LEGITIMATE PROJECT DATA REMOTE + LOCAL VERIFIED: NO
If NO:
1. 111 untracked local files exist (none in the acquisition/channel-data domain) — owner needs to commit, ignore, or discard them for the repo to be literally clean.
2. .gitignore has two real gaps (no __pycache__ rule; /outputs/ vs output/ name mismatch) that let 71 of those 111 files go untracked instead of being cleanly ignored.
3. (Now resolved during this run) youtube_channel_registry.db LFS object was not materialized locally.

NEXT SAFE ACTION: FIX DATA DISCREPANCIES FIRST (three small .gitignore/commit decisions in §27) — none of them touch or block Doctor Thomas specifically; that data domain's remote preservation is fully verified. Once the owner disposes of the 111 untracked files, re-run Part J/§5 to confirm zero, and the branch is clean for Doctor Thomas acquisition.
```
