# Database Relationships

FKs are from `PRAGMA foreign_key_list` (read-only). The branch DBs declare **no** FKs. Their joins are implicit on `video_id` / `channel_id` (YouTube IDs).

## 1. Inventory catalog (provenance spine)

```mermaid
erDiagram
  datasets ||--o{ source_files : contains
  datasets ||--o{ ingestion_runs : "ingested by"
  datasets ||--o{ channel_dataset_links : links
  datasets ||--o{ dataset_relationships : "from/to"
  channels ||--o{ channel_dataset_links : links
  channels ||--o{ channel_snapshots : "measured as"
  channels ||--o{ videos : publishes
  videos ||--o{ video_snapshots : "measured as"
  videos ||--o{ transcripts : has
  videos ||--o{ content_classifications : "classified as"
  videos ||--o{ thumbnail_evidence : has
  videos ||--o{ apify_result_records : "returned by"
  apify_source_runs ||--o{ apify_result_records : produces
  apify_source_runs ||--o{ apify_run_cost_observations : costs
  ingestion_runs ||--o{ field_provenance : records
  field_provenance }o--|| videos : about
  field_provenance }o--|| channels : about
  field_provenance }o--|| transcripts : about
  source_batches ||--o{ batch_roots : has
  source_batches ||--o{ discovered_files : discovered
  discovered_files ||--o| discovered_files : "duplicate of"
  discovered_files ||--o{ visual_assets : "is image"
  discovered_files ||--o{ document_records : "is document"
  visual_assets ||--o{ visual_observations : "observed as"
  source_files ||--o{ file_relationships : "from/to"
  source_files ||--o| source_files : "parent (archive member)"
```

`field_provenance` is the key table for a UI: every displayed value can link to its source file, run, extraction method and evidence layer.

## 2. Channel registry (coverage spine)

```mermaid
erDiagram
  channels ||--o{ videos : publishes
  videos ||--o{ transcripts : has
  videos ||--o{ subtitle_tracks : has
  videos ||--o{ dataset_videos : "member of"
  datasets ||--o{ dataset_videos : contains
  datasets ||--o{ dataset_channels : covers
  channels ||--o{ dataset_channels : "covered by"
  channels ||--o{ channel_aliases : "also known as"
  channels ||--o{ identity_evidence : "verified by"
  channels ||--o{ channel_data_layers : "layer status"
  channels ||--o{ intelligence_coverage : "capability status"
  intelligence_capabilities ||--o{ intelligence_coverage : "status per channel"
  channels ||--o{ availability_gaps : "missing fields"
  channels ||--o{ visual_coverage : "visual level"
  channels ||--o{ artifacts : "artifacts"
  submissions }o--|| channels : "resolved to"
  submissions ||--o| submissions : "duplicate of"
  non_channel_subjects ||--o{ subject_datasets : has
```

## 3. Reference knowledge

`ref_source_member` → `ref_section` (FTS) → `ref_rule` (33, with rule class) ↔ `ref_rule_conflict` (3); `ref_constituent_video` (63) and `ref_video_assessment` (722) link rules to audited videos; `ref_platform_verification` (9) records platform-claim checks; `ref_analysis_run` gives provenance.

## 4. Branch DBs (implicit joins)

```mermaid
erDiagram
  FE_channels ||--o{ FE_videos : channel_id
  FE_videos ||--o| FE_transcripts : video_id
  FE_videos ||--o{ FE_apify_rows : video_id
  SH_channels ||--o{ SH_videos : channel_id
  SH_videos ||--o| SH_transcript_index : video_id
  SH_transcript_index ||--|| SH_shard_transcripts : "video_id + shard"
  SH_videos ||--o{ SH_ds34_records : video_id
  SHA_runs ||--o{ SHA_videos : run_id
  SHA_channels ||--o{ SHA_videos : channel_id
```

## 5. Hidden relationships worth surfacing

| Relationship | How to compute | User value |
|---|---|---|
| Same video across stores | join on YouTube video ID | "Where do we know about this video from?" panel; dedup |
| Channel ↔ niche ↔ workstream | registry `target_group` + FE `niche` + SH `category`/`tier` | niche-level browsing |
| Video ↔ finance audit ↔ reference rules | NICK audit IDs → `ref_video_assessment` | "which rules does this video support/contradict" |
| Video ↔ visual forensic ledger ↔ seal | evidence map CSV (`VISUAL_EVIDENCE_MAP.csv`) keyed by video ID + SHA-256 | forensic depth badge per video |
| Channel ↔ template network (Senior Health Report 2: 12-channel network) | report tables | "independent evidence" count, not raw channel count |
| Plan ↔ evidence | plan JSON `internal_evidence`, `linkage`, `counter_evidence` | click-through from a recommendation to its proof |

## 6. Normalization needs

1. **Canonical identity tables**: `entity_channel(youtube_channel_id PK, …)`, `entity_video(youtube_video_id PK, youtube_channel_id, …)`, plus crosswalks to `CH-0000NN` and registry IDs.
2. **Per-field source precedence** (e.g. registry > inventory > FE > SH for titles; latest `observed_at` for metrics), stored, not hard-coded in the UI.
3. **Snapshot table** for metrics with `observed_at` and `store`, so view counts from different scrape dates are never silently mixed.
4. Normalized `video_type` plus the raw value.

## 7. Schema migration risks between branches

- Migration `011_reference_knowledge.sql` is absent on main. Merging the finance lineage adds it.
- `codex/register-verified-transcript-pending-what-if` edits the committed catalog DBs directly. Re-apply it by script, never by a binary merge.
- Branch DBs have no `schema_meta`/migration history (FE has a `meta` table with `built_from_registry_sha256`). Their schemas are defined only by their builder scripts.
