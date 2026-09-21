# YouTube Channel Registry

Verified: 2026-09-21

## Purpose and authority

This registry reconciles the 67 user-submitted YouTube URLs, 26 acquired dataset manifests, historical holdings, standardized channel packages, visual evidence, and generated intelligence. The immutable submitted URL authority is `data/raw/channel-targets/user-supplied-youtube-channels-2026-09-14.json`.

The registry is separate from `data/catalog/youtube_inventory.db`. Both runtime DBs are ignored. `scripts/rebuild_inventory_catalog.py` safely creates a schema-v10 manifest index when historical ignored evidence is unavailable; this is semantically useful but not byte-identical historical recovery. The channel-registry builder uses tracked canonical-fact snapshots for missing historical row bodies without inventing transcript or description text.

## Population controls

| Population | Count |
|---|---:|
| Canonical channels | 70 |
| User-submitted rows | 67 |
| Canonical target channels | 63 |
| Standard-package channels | 36 |
| Historical-catalog channels | 5 |
| Identity-only target channels | 29 |
| Stored channels outside target list | 7 |
| Datasets | 26 |
| Unique videos across historical and package layers | 1,939 |
| Real transcripts | 1,928 |
| Explicit transcript placeholders | 11 |
| Videos missing public descriptions | 14 |
| Screenshot-only unmapped subjects | 7 |

The 1,939-video total is the canonical union by YouTube video ID. It is not a blind sum of assumed-independent populations.

## Independent data layers

No single completion flag represents every layer. `status` is retained only as target-registry progress compatibility. These independent fields are authoritative for coverage questions:

- `identity_status`
- `extraction_status`
- `package_status`
- `video_metadata_status`
- `description_status`
- `transcript_status`
- `thumbnail_metadata_status`
- `visual_asset_status`
- `forensic_video_status`
- `intelligence_status`
- `first_party_analytics_status`

`channel_data_layers` stores one row per channel and layer, with status, evidence path, limitation reason, and verification date. This produces 770 rows: 70 channels times 11 layers.

### Source groups

- `STANDARD_PACKAGE`: 36 channels with repository package workbook and transcript ZIP evidence.
- `HISTORICAL_CATALOG`: five channels in the older catalog/intelligence system. These are not relabeled as standard packages.
- `IDENTITY_ONLY`: 29 verified target identities with no stored video extraction or package.

### Core controlled values

- Identity: `VERIFIED`, `UNRESOLVED`, `UNAVAILABLE`.
- Extraction: `COMPLETE`, `COMPLETE_WITH_LIMITATIONS`, `PARTIAL`, `NOT_EXTRACTED`.
- Package: `STANDARD_PACKAGE`, `HISTORICAL_FORMAT`, `NO_PACKAGE`.
- Transcript: `COMPLETE_REAL`, `COMPLETE_WITH_PLACEHOLDERS`, `PARTIAL`, `NONE`.
- Visual assets: `NONE`, `THUMBNAIL_URL_ONLY`, `THUMBNAIL_EVIDENCE`, `FORENSIC_VIDEO_EVIDENCE`.
- Intelligence: `VALIDATED`, `AVAILABLE`, `PARTIAL`, `DATA_READY`, `NOT_AVAILABLE`, `NOT_APPLICABLE`.
- First-party Analytics: `INGESTED`, `SCHEMA_READY_NO_DATA`, `NOT_CONFIGURED`.

Identity resolution never implies extraction. Thumbnail URLs never imply downloaded images. Downloaded thumbnails never imply scene-level or editing evidence. Public view, like, and comment counts are not first-party YouTube Studio or Analytics data.

## Visual evidence

`visual_coverage` stores thumbnail URL, downloaded thumbnail, screenshot, keyframe, registered source-video, and timestamped visual-observation counts independently.

| Channel | Thumbnail URLs | Downloaded thumbnails | Screenshots | Keyframes | Registered forensic videos | Timestamped observations | Level |
|---|---:|---:|---:|---:|---:|---:|---|
| Dr. Aliza Wright \| Advice | 32 | 32 | 7 | 0 | 0 | 0 | `THUMBNAIL_EVIDENCE` |
| xkcd's What If? | 83 | 83 | 0 | 107 | 3 | 107 | `FORENSIC_VIDEO_EVIDENCE` |
| Dr. Elias Senior Health | 29 | 29 | 0 | 0 | 0 | 0 | `THUMBNAIL_EVIDENCE` |

The 36 standard-package channels have thumbnail URLs only and no registered downloaded thumbnail or forensic evidence in their packages. Matty Invests and Mr. Finance remain title-only for packaging because canonical thumbnail references are absent.

Only xkcd's What If? (`UC6IxnFzHofFJ5X2PycSMsww`, historical `CH-000004`) has registered forensic visual-temporal evidence. The editing artifact covers three canonical videos across four forensic datasets; DS-000012 and DS-000015 are related analyses of the same source video and are not counted independently.

Seven screenshot-only subjects remain in `non_channel_subjects`. They have no canonical YouTube identity and are never counted as channels.

## Intelligence coverage

Eight capabilities are stored separately for every canonical channel, producing 560 rows:

1. Topic Opportunity Intelligence
2. Packaging, Title, and Thumbnail Intelligence
3. Hook Intelligence
4. Script Intelligence
5. Editing and Visual Intelligence
6. Unified Orchestration
7. Channel Strategy Intelligence
8. First-party Analytics ingestion readiness

Each `intelligence_coverage` row distinguishes input availability from generated artifact availability. Raw data availability is not generated intelligence.

The five historical intelligence channels have generated topic, packaging, hook, script, and unified artifacts. Packaging is title-only and `PARTIAL` for Matty Invests and Mr. Finance. Editing/Visual is generated only for xkcd and remains `PARTIAL` because evidence covers three videos, not the full channel. Channel Strategy has four generated/benchmark-covered channels and retains the two-channels-per-niche calibration limitation. The 36 package channels, including Dr. Ares Senior, are `DATA_READY` for topic, packaging, hook, and script inputs but have no generated per-channel artifacts. The 29 identity-only channels lack these inputs.

First-party Analytics remains `SCHEMA_READY_NO_DATA` for every channel. Repository code and synthetic fixtures prove ingestion readiness; no real first-party export has been ingested.

## SQLite layout

Principal tables:

- `channels`, `submissions`, `channel_aliases`, `identity_evidence`
- `channel_data_layers`, `visual_coverage`
- `datasets`, `dataset_channels`, `dataset_videos`
- `videos`, `transcripts`, `subtitle_tracks`
- `actor_runs`, `artifacts`, `availability_gaps`
- `intelligence_capabilities`, `intelligence_coverage`
- `non_channel_subjects`, `subject_datasets`

Required views:

- `v_channel_status`
- `v_completed_channels`
- `v_pending_channels`
- `v_channel_data_gaps`
- `v_original_target_progress`
- `v_added_target_progress`
- `v_dataset_summary`
- `v_video_transcript_status`
- `v_channel_artifacts`
- `v_intelligence_coverage`

Every connection enables `PRAGMA foreign_keys = ON`. Inserts use transactions and UPSERTs. Channels deduplicate by canonical YouTube channel ID; videos deduplicate by YouTube video ID; junction tables preserve multiple dataset memberships.

Transcript FTS5 is created only when runtime support exists. `data/catalog/channel_registry/example_queries.sql` includes both FTS5 and standard `LIKE` fallback queries.

## Build and validate

Use the declared Python 3.12 environment from repository root:

```bash
python3 -B -m scripts.rebuild_inventory_catalog

python3 -B -m scripts.build_youtube_channel_registry --write-ledgers

python3 -B -m scripts.validate_youtube_channel_registry
```

The validator checks control totals, source-group separation, visual evidence, intelligence input/output distinctions, evidence paths, required views, uniqueness, SQLite integrity, foreign keys, and a two-run idempotence build.

Execute every example query with parameters set for the two parameterized examples:

```bash
sqlite3 \
  -cmd ".parameter set :channel_id UCTcOboZIhgrKHMDm-oTlTOg" \
  -cmd ".parameter set :phrase money" \
  data/catalog/youtube_channel_registry.db \
  < data/catalog/channel_registry/example_queries.sql
```

Build the tracker with the bundled Node.js runtime and the `@oai/artifact-tool` module returned by the workspace dependency loader:

```bash
node scripts/build_youtube_channel_master_tracker.mjs \
  "$PWD" \
  "$PWD/data/normalized/channel-targets/YOUTUBE_CHANNEL_MASTER_TRACKER.xlsx" \
  "/tmp/youtube-channel-registry-renders" \
  "/absolute/path/to/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs"
```

The workbook builder reads the normalized registry JSON and generated registry database, recalculates dashboard formulas, writes all nine sheets, renders every populated row, and converts `HYPERLINK()` formulas to native XLSX hyperlinks. This avoids stale cached hyperlink errors in non-Excel readers.

## Maintainer workflow

Authoritative inputs are the immutable submitted-URL JSON, identity-evidence JSON, dataset manifests, registered package workbooks and transcript ZIPs, historical catalog evidence, and generated intelligence artifacts. `scripts/build_youtube_channel_registry.py` generates the normalized ledgers and ignored SQLite query database. `scripts/build_youtube_channel_master_tracker.mjs` generates the Excel tracker.

Important invariants:

- Canonical channels deduplicate by verified YouTube channel ID; submissions remain in original order with duplicate references.
- Target membership, extraction, package, transcript, visual, intelligence, and first-party Analytics statuses remain independent.
- Standard packages require exactly one workbook and one transcript ZIP.
- Thumbnail URLs, downloaded thumbnails, and forensic evidence remain separate.
- Input-ready intelligence never counts as generated intelligence.
- Public metrics never count as first-party Analytics.

To add a channel or dataset, register the supplied evidence and identity in the appropriate raw authority, identity ledger, dataset manifest, and package location. Rebuild the registry with `--write-ledgers`, run the registry validator and package tests, rebuild the tracker, rerun workbook tests and visual review, then update the query-results report only from reproduced SQL output.

Never manually edit generated `YOUTUBE_CHANNEL_REGISTRY.json`, `YOUTUBE_CHANNEL_TARGETS.csv`, `YOUTUBE_CHANNEL_TARGETS.md`, `YOUTUBE_CHANNEL_MASTER_TRACKER.xlsx`, or `youtube_channel_registry.db`. Rebuild runtime DBs only through supported scripts. Never alter historical raw or extracted evidence to make a validation pass.

## Environment-only test limits

Distributable validation uses dependencies declared in `pyproject.toml`. Tests requiring ignored historical transcript, training, or forensic evidence skip with an explicit reason in a clean clone; they run when those local fixtures exist. Path resolution uses the selected repository root and never reads forensic files from another worktree.

## Portability and limits

- Tracker evidence links use existing repository files on GitHub `main` or canonical HTTPS source URLs. Historical manifest paths may still record original machines as provenance.
- Historical catalog evidence is ignored local state; a clean checkout needs safe local evidence copies for a full rebuild.
- Historical catalog source records retain old absolute paths as provenance. Registry and editing reports rebase repository evidence under the selected worktree and emit relative locators.
- Transcript ZIP members remain authoritative when spreadsheet cell limits affect presentation.
- No acquisition runs occur during build or validation.
