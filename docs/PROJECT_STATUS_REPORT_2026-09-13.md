# YouTube Intelligence OS — Work Summary and Current Status

**Report date:** 2026-09-13 (Asia/Karachi)

**Repository:** `/Users/ghilmankhan/workprojects/youtube-intelligence-os`

**Scope:** Completed acquisition and packaging work through DS-000024, overall project capability status, current limitations, and remaining funded work.

## 1. Executive summary

The repository contains 24 durable dataset records, `DS-000001` through `DS-000024`. The YouTube Intelligence OS V1 intelligence capabilities are complete for the five canonical channels: Topic Opportunity, Packaging, Hook, Script, conditional Editing/Visual Intelligence, and unified evidence-traceable orchestration. Channel Strategy Intelligence is `GENERALIZED_WORKING` across two independent niches. First-party YouTube Analytics ingestion is ready for real exports, but no real first-party export has been ingested.

The recent funded acquisition work completed two of the three deterministic batches:

| Batch | State | Channels | Videos | Real transcripts | Actual cost | Git state |
|---|---|---:|---:|---:|---:|---|
| DS-000023 | Completed, validated, pushed | 5 | 110 | 110 | $0.440 | Remote-verified at `4fbdd57fd1975709a843ad9234ad27a080bbdb47` |
| DS-000024 | Completed, validated, pushed | 4 | 178 | 178 | $0.712 | Remote-verified at `57491326ec76c7763c9da7b0affcc473a962b7e7` |
| DS-000025 | Planned, not started | 3 | 230 expected | Not yet acquired | $0.944 estimated | No files, run, dataset, or commit yet |
| DS-000026 | Not defined in the canonical funded plan | Not assigned | Not assigned | Not applicable | Not estimated | Must not be invented or launched |

Funded batches DS-000023 and DS-000024 used $1.152 in total. The last authenticated post-run balance evidence records `$1.648` remaining. This is the recorded balance after DS-000024, not a fresh pre-DS-000025 authorization check.

## 2. Work completed

### 2.1 DS-000023 checkpoint confirmation

Before DS-000024, the DS-000023 checkpoint was verified against Git and repository evidence.

- Commit: `4fbdd57fd1975709a843ad9234ad27a080bbdb47`
- Local, upstream, and remote `main` matched at the checkpoint.
- Worktree was clean.
- Five channels were complete: Maximus, The Life Outline, Bro Pump, Crayon Capital, and Zoozle.
- Public and scraped counts reconciled at 110 videos.
- Content types: 110 regular videos, 0 Shorts, 0 livestreams.
- Transcript coverage: 110/110 real plaintext transcripts.
- Missing descriptions: 0.
- Packages: five five-sheet workbooks and five transcript ZIPs.
- Rendered workbook sheets reviewed: 25.
- Actor requests: 251 succeeded, 0 failed.
- Actual cost: `$0.440` versus `$0.480` estimate.
- Balance after run: `$2.36`.
- No DS-000020, DS-000021, or DS-000022 files were included in the DS-000023 commit.

Canonical evidence:

- [DS-000023 manifest](../data/manifests/DS-000023.md)
- [DS-000023 package validation](../data/extracted/channel-data/DS-000023/DS-000023_PACKAGE_VALIDATION_REPORT.md)
- [DS-000023 file ledger](../data/manifests/DS-000023_FILES.csv)

### 2.2 DS-000024 preflight and budget control

The exact allocation from the funded extraction plan was preserved. No channel was substituted and no previously packaged channel was scraped again.

| Channel | Canonical channel ID | Public regular videos | Public Shorts | Public livestreams | Conservative results | Estimated cost |
|---|---|---:|---:|---:|---:|---:|
| Hypothetically | `UC0L9hD7HMwWU7xuU5HRA6Iw` | 39 | 0 | 0 | 41 | $0.164 |
| Brimm. | `UC1GwXFBhh1fiLLuZxs8VRXA` | 44 | 0 | 0 | 46 | $0.184 |
| Lost Legacy | `UC96yqt8xjtShTpgdoIo0Lqg` | 45 | 0 | 0 | 47 | $0.188 |
| ago. | `UCJqZXjdkolPUgVcf6WBm8VA` | 50 | 0 | 0 | 52 | $0.208 |
| **Total** |  | **178** | **0** | **0** | **186** | **$0.744** |

Pre-launch controls:

- Authenticated plan: Apify Free plan.
- Actor price: `$4.00` per 1,000 videos written to the dataset.
- Starting balance: `$2.36`.
- Estimated balance after run: `$1.616`.
- Minimum reserve: `$0.30`.
- Budget decision: `SAFE_TO_LAUNCH`.
- Paid date, AI-description, AI-summary, and speech-to-text add-ons remained disabled.
- Existing Apify credits were used. No credit purchase, plan upgrade, or payment approval occurred.
- Exact Actor input SHA-256: `a1cfad21e72e0d0d04abb28392861392a2d9b313fba767ebdb4a618e823abe4f`.

Preflight evidence:

- [DS-000024 preflight record](../data/manifests/DS-000024_PREFLIGHT.json)
- [Authenticated budget evidence](../data/raw/channel-data/DS-000024/preflight/authenticated_apify_budget_evidence.json)
- [Authenticated pricing evidence](../data/raw/channel-data/DS-000024/preflight/authenticated_pricing_evidence.json)
- [Authenticated balance evidence](../data/raw/channel-data/DS-000024/preflight/authenticated_balance_evidence.json)
- [Actor input](../data/raw/channel-data/DS-000024/preflight/actor_input.json)
- [Actor schema evidence](../data/raw/channel-data/DS-000024/preflight/actor_input_schema_evidence.json)

### 2.3 DS-000024 Actor run

- Actor: `streamers/youtube-scraper`
- Actor ID: `h7sDV53CddomktSi5`
- Build: `0.0.300` using `latest`
- Run ID: `2ZEXd8nKLPegjIi8L`
- Dataset ID: `gLhVSzuRQfIJcVumQ`
- Status: `SUCCEEDED`
- Start: 2026-09-13 13:19:17 Asia/Karachi
- Finish: 2026-09-13 13:24:32 Asia/Karachi
- Runtime: 315 seconds
- Results: 178 video records
- Requests: 378 succeeded, 0 failed
- Actual cost: `$0.712`
- Ending balance: `$1.65` displayed, `$1.648` calculated
- [Actor run](https://console.apify.com/actors/h7sDV53CddomktSi5/runs/2ZEXd8nKLPegjIi8L)
- [Actor dataset](https://console.apify.com/storage/datasets/gLhVSzuRQfIJcVumQ)

Result reconciliation:

| Channel | Public count | Scraped count | Regular | Shorts | Livestreams | Plaintext transcripts | Missing descriptions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Hypothetically | 39 | 39 | 39 | 0 | 0 | 39 | 0 |
| Brimm. | 44 | 44 | 44 | 0 | 0 | 44 | 0 |
| Lost Legacy | 45 | 45 | 45 | 0 | 0 | 45 | 0 |
| ago. | 50 | 50 | 50 | 0 | 0 | 50 | 0 |
| **Total** | **178** | **178** | **178** | **0** | **0** | **178** | **0** |

Transcript handling followed the required evidence rule. All 178 videos contained subtitle plaintext across 188 subtitle tracks. `transcriptionUrl` was absent for all videos, and the separate `transcript` field was absent or null, but neither condition was classified as transcript-missing because complete subtitle plaintext existed. Genuine missing transcripts: 0. No recovery run was needed.

### 2.4 Raw evidence preservation

Raw evidence was stored at the canonical non-duplicated path:

`data/raw/channel-data/DS-000024/apify/2ZEXd8nKLPegjIi8L/`

Preserved files:

- `actor_input.json`
- `authenticated_post_run_balance_evidence.json`
- `raw_evidence_manifest.json`
- `run.log.txt`
- `run_metadata.json`
- `youtube_actor_raw.json`

Integrity facts:

- Raw JSON size: 3,479,388 bytes.
- Raw JSON SHA-256: `f267b75300f5dc2e447be1e277417755b442f6d4964ee500431eb3676cffa408`.
- Raw JSON matched the downloaded source byte-for-byte.
- Run log size: 64,755 bytes across 511 lines.
- Run log SHA-256: `63755bc405472c0c86d0eac05eb758ba278b5ab250c28db7d5da47816a725d43`.
- No nested duplicate path such as `.../<RUN_ID>/apify/run/<RUN_ID>/` was created.
- Raw checkpoint commit: `9f5e41d8e95c0cf87d065d0f1d4e3e7f9183d7fe` (`data: preserve DS-000024 raw extraction evidence`).

Canonical evidence:

- [Run metadata](../data/raw/channel-data/DS-000024/apify/2ZEXd8nKLPegjIi8L/run_metadata.json)
- [Raw evidence manifest](../data/raw/channel-data/DS-000024/apify/2ZEXd8nKLPegjIi8L/raw_evidence_manifest.json)

### 2.5 DS-000024 packaging

Combined package files:

- [Clean normalized JSON](../data/extracted/channel-data/DS-000024/combined/youtube_4_channels_clean.json)
- [Combined master JSON](../data/extracted/channel-data/DS-000024/combined/youtube_4_channels_master.json)
- [Combined master CSV](../data/extracted/channel-data/DS-000024/combined/youtube_4_channels_master.csv)
- [Combined master workbook](../data/extracted/channel-data/DS-000024/combined/youtube_4_channels_master.xlsx)
- [Channel summary CSV](../data/extracted/channel-data/DS-000024/combined/youtube_4_channels_channel_summary.csv)

Per-channel packages:

| Channel | Five-sheet workbook | Transcript ZIP |
|---|---|---|
| Hypothetically | [Hypothetically_Master_Data.xlsx](../data/extracted/channel-data/DS-000024/packages/hypothetically/Hypothetically_Master_Data.xlsx) | [Hypothetically_Transcripts_39_Videos.zip](../data/extracted/channel-data/DS-000024/packages/hypothetically/Hypothetically_Transcripts_39_Videos.zip) |
| Brimm. | [Brimm_Master_Data.xlsx](../data/extracted/channel-data/DS-000024/packages/brimm/Brimm_Master_Data.xlsx) | [Brimm_Transcripts_44_Videos.zip](../data/extracted/channel-data/DS-000024/packages/brimm/Brimm_Transcripts_44_Videos.zip) |
| Lost Legacy | [LostLegacy_Master_Data.xlsx](../data/extracted/channel-data/DS-000024/packages/lost-legacy/LostLegacy_Master_Data.xlsx) | [LostLegacy_Transcripts_45_Videos.zip](../data/extracted/channel-data/DS-000024/packages/lost-legacy/LostLegacy_Transcripts_45_Videos.zip) |
| ago. | [Ago_Master_Data.xlsx](../data/extracted/channel-data/DS-000024/packages/ago/Ago_Master_Data.xlsx) | [Ago_Transcripts_50_Videos.zip](../data/extracted/channel-data/DS-000024/packages/ago/Ago_Transcripts_50_Videos.zip) |

Each workbook uses the required sheet order:

1. Channel Overview
2. All Videos
3. Descriptions
4. Verification
5. Analysis

### 2.6 DS-000024 validation and delivery

Recorded package validation:

- Four channel packages validated.
- 178 workbook rows and 178 unique video IDs.
- 178 transcript files and 0 placeholders.
- 182 ZIP members, including four `INDEX.txt` files.
- Workbook and ZIP IDs reconcile exactly.
- 1,286 formula cells contain usable cached values.
- No Excel formula errors detected.
- No missing descriptions or required metric fields.
- Formula, hyperlink, ZIP integrity, manifest path, checksum, raw-source byte comparison, duplicate-ID, and credential scans passed.
- All 20 channel workbook sheets were rendered and visually reviewed.
- Twenty browser sample URLs were verified.
- Video-ID overlap with DS-000020 through DS-000023: 0.
- Fresh focused tests on this report date: 11 tests run, 11 passed.

Validation evidence:

- [Package validation report](../data/extracted/channel-data/DS-000024/DS-000024_PACKAGE_VALIDATION_REPORT.md)
- [Packaging validation detail](../data/extracted/channel-data/DS-000024/youtube_4_channels_packaging_validation_report.md)
- [Video-ID overlap report](../data/extracted/channel-data/DS-000024/DS-000024_VIDEO_ID_OVERLAP_REPORT.csv)
- [File checksum ledger](../data/manifests/DS-000024_FILES.csv)
- [Source artifact ledger](../data/manifests/DS-000024_SOURCE_ARTIFACTS.csv)
- [Browser sample verification](../data/manifests/DS-000024_VIDEO_SAMPLE_VERIFICATION.json)

Git delivery:

- Raw-evidence checkpoint: `9f5e41d8e95c0cf87d065d0f1d4e3e7f9183d7fe`.
- Final DS-000024 commit: `57491326ec76c7763c9da7b0affcc473a962b7e7`.
- Commit message: `data: add DS-000024 funded channel extraction`.
- Local `HEAD`, `origin/main`, and live remote `refs/heads/main` were freshly verified at `57491326ec76c7763c9da7b0affcc473a962b7e7` before this report file was created.
- The baseline worktree was clean before this report was added.
- DS-000020, DS-000021, DS-000022, and DS-000023 files were not modified by the DS-000024 final commit.

## 3. Current package coverage

The following totals describe the recent channel-package layer, not the smaller five-channel canonical intelligence catalog in SQLite.

| Dataset | Channels | Videos | Real transcripts | Explicit placeholders | Missing public descriptions |
|---|---:|---:|---:|---:|---:|
| DS-000020 | 5 | 132 | 132 | 0 | 14 |
| DS-000021 | 11 | 216 | 216 | 0 | 0 |
| DS-000022 | 7 | 732 | 722 | 10 | 0 |
| DS-000023 | 5 | 110 | 110 | 0 | 0 |
| DS-000024 | 4 | 178 | 178 | 0 | 0 |
| **Total** | **32** | **1,368** | **1,358** | **10** | **14** |

The ten placeholders are documented Lucas Grant members-only videos from DS-000022. A targeted Actor recovery and live browser audit confirmed that captions were unavailable. No transcript text was fabricated. The 14 missing descriptions are DS-000020 videos for which the Actor and YouTube both confirmed no public description.

## 4. Overall project status

### 4.1 Data and provenance foundation

- Phase 0, Phase 0.5, and Phases 1A through 1D are complete.
- Phase 2 Data Classification and Provenance is closed.
- The durable inventory contains 24 datasets.
- Phase 1C recorded 45,774 discovered files with 100% disposition coverage.
- The canonical catalog contains 303 content items across five canonical channels and 604 classification rows.
- Raw evidence remains distinct from extracted, normalized, and intelligence layers.
- The local SQLite catalog is regenerable and gitignored. It may lag the newest manifests until a controlled rebuild.

### 4.2 V1 intelligence capabilities

| Capability | Current status | Evidence limitation |
|---|---|---|
| Topic Opportunity Intelligence | Complete for all five canonical channels | None recorded at capability level |
| Packaging Intelligence | Complete for all five canonical channels | CH-000001 and CH-000002 are title-only because canonical thumbnail references are absent |
| Hook Intelligence | Complete for all five canonical channels | Some timings are positional approximations when timestamps are unavailable |
| Script Intelligence | Complete for all five canonical channels | Opportunity linkage may be `PARTIAL` where authored blueprints do not exist |
| Editing/Visual Intelligence | Complete but conditional | Available only for CH-000004 because it is the only channel with registered forensic video evidence; others correctly report `NOT_AVAILABLE` |
| Unified orchestration | Complete | Degrades gracefully when an evidence layer is unavailable |
| Channel Strategy Intelligence | `GENERALIZED_WORKING` | Validated across health and finance; only two channels per niche, so no heuristic yet qualifies as a robust cross-niche pattern |
| First-party Analytics ingestion | Ready | No real YouTube Studio export has been ingested |

### 4.3 Explicitly out of scope or not built

No production UI, dashboard, API, RAG/vector store, embeddings layer, MCP server, custom agent workflow, scheduled research automation, YouTube API integration, or alternative scraper has been introduced. V2 work does not begin automatically.

### 4.4 Documentation state

`AGENTS.md` and the current status sections in `docs/Phases.md` are the authoritative capability summary. `README.md` and `docs/PROJECT_SCOPE.md` still contain older wording that describes the repository mainly as an ingestion foundation, while later text acknowledges completed V1 intelligence work. Formal phase numbering and top-level messaging should be reconciled in a separate documentation-only task.

## 5. Current verification status

Fresh checks performed while preparing this report:

- Local `HEAD`: `57491326ec76c7763c9da7b0affcc473a962b7e7`.
- Upstream `origin/main`: `57491326ec76c7763c9da7b0affcc473a962b7e7`.
- Live remote `main`: `57491326ec76c7763c9da7b0affcc473a962b7e7`.
- Baseline worktree before adding this report: clean.
- Focused workbook/package test modules: 11 tests, all passed.
- Full repository suite: 238 tests run; 17 known environment-dependent errors recur.

The 17 full-suite errors are not DS-000024 package failures. They arise from three known local-environment gaps:

1. The gitignored canonical SQLite database is absent, so database-backed intelligence tests cannot open it.
2. The local DS-000011 raw training-evidence directory is absent.
3. `pytest` is absent from the bundled Python runtime, so the first-party analytics test module cannot import it.

The focused DS-000024-relevant tests pass in the configured bundled Python runtime. Running them with macOS system Python fails because that interpreter lacks `openpyxl`; this is an interpreter-selection issue, not an artifact failure.

## 6. Remaining funded work

### 6.1 DS-000025

Canonical allocation:

- Stickly
- Mack
- Explain In Paint

Planned totals:

- Public uploads: 230.
- Conservative expected results: 236.
- Estimated cost: `$0.944`.
- Last recorded balance: `$1.648`.
- Projected balance after DS-000025: `$0.704`.
- Required reserve: at least `$0.30`.

DS-000025 is not started. There is no run ID, dataset ID, raw evidence, package, validation report, or commit. Before launch, the authenticated balance, Actor schema, pricing, exact channel counts, and reserve calculation must be refreshed. The batch must stop before launch if the complete three-channel allocation no longer fits safely.

### 6.2 DS-000026 and deferred channels

The canonical funded plan defines DS-000023, DS-000024, and DS-000025 only. It does not assign channels or a budget to DS-000026. Therefore:

- DS-000026 is not started.
- No channel may be assigned to DS-000026 by assumption.
- The 22-channel preflight and the approved 12-channel allocation imply ten channels remain outside the funded plan, but their exact names are not recorded in the canonical funded plan file.
- Any DS-000026 work requires an explicit deterministic allocation, live cost calculation, and reserve decision before launch.

Canonical plan: [Funded Master-Channel Extraction Plan](superpowers/plans/2026-09-13-funded-master-channel-extraction.md)

## 7. Risks and limitations

- Apify balance `$1.648` is the last authenticated post-DS-000024 evidence, not a current pre-run check.
- Public video metrics and channel catalog sizes are point-in-time observations and may change.
- Six combined-workbook transcript cells across DS-000023 and DS-000024 exceed Excel's 32,767-character cell display limit. Full text remains preserved in JSON, CSV, raw Actor output, and transcript ZIPs.
- DS-000022 user-provided packages did not include their original Actor raw JSON, inputs, run IDs, or dataset IDs. Only the targeted Lucas Grant recovery has complete Actor evidence.
- The local SQLite catalog may need a controlled rebuild before all database-backed tests can run.
- Cross-niche strategy confidence remains evidence-limited: two channels per niche are insufficient to establish robust cross-niche heuristics.
- Formal roadmap numbering and top-level documentation wording are partially stale relative to completed V1 work.

## 8. Recommended next actions

1. Reconcile `README.md`, `docs/PROJECT_SCOPE.md`, and formal phase numbering with the authoritative V1 status in `AGENTS.md` and `docs/Phases.md`.
2. If DS-000025 is authorized, re-check authenticated Apify balance and pricing, verify the exact three-channel public counts, preserve input evidence, and launch only if the complete batch preserves the reserve.
3. Rebuild the local SQLite catalog and restore the DS-000011 local raw fixture when a clean full-suite run is required.
4. Install `pytest` only if the user authorizes dependency changes; do not change the environment merely to make the current report appear cleaner.
5. Define DS-000026 explicitly before any launch. Record exact channels, counts, estimated cost, and reserve treatment.
6. Ingest a real first-party YouTube Studio export when available to move own-channel diagnostics from readiness to production evidence.

## 9. Source-of-truth hierarchy used for this report

1. Repository `AGENTS.md` and documented project rules.
2. Dataset manifests and file/checksum ledgers.
3. Immutable raw Actor evidence and preserved authenticated pricing/balance evidence.
4. Validation reports and fresh verification commands.
5. Git history and live remote branch verification.

No model memory, inferred channel allocation, or fabricated transcript content was used as authoritative evidence.
