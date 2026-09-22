# Senior Health Acquisition Checkpoint

Updated: 2026-09-22

## Completed work

- Last completed channel: Dr. Okoro catalog acquisition
- Channel ID: `UCMJxAeBJ0d1JC937de1eZ0Q`
- Dataset: `DS-000028`
- Apify runs: control `4Jkn3vuO1nDp57HfT`; catalog `uLT4StERHwuiLthti`
- Apify datasets: control `wcOVfRxeT5khIdk8O`; catalog `vvBzcGKPzEfKLnMrX`
- Actor/build: `streamers/youtube-scraper` / `0.0.303`
- Catalog result: `SUCCEEDED`, 66 raw records, 66 unique videos (65 regular, 1 Short, 0 streams)
- Catalog subtitles: 66 available (64 auto-generated, 2 user-generated); 0 unavailable
- Catalog cost: `$0.264`; new-campaign cumulative cost: `$0.264 / $4.50`
- Historical control cost: `$0.004`; combined acquisition cost: `$0.268`
- Remaining approved campaign budget: `$4.236`
- Ending Apify free credit: `$4.59`
- Git HEAD before this checkpoint commit: `f9bac0039328af9c485ca40ebce3fe5893156c69`

## Validation

- Catalog `ingest-existing`: completed as `RUN-000026` / `APIFYRUN-000004`
- Inventory database: `PRAGMA integrity_check = ok`; `PRAGMA foreign_key_check` returned no rows
- Catalog-run rows: 66 video snapshots, 66 available transcripts, 66 thumbnail-evidence rows
- Deduplication: control video `eD2OnCE8iKM` overlapped once; canonical video identity remains unique; catalog run added 65 new video identities
- Coverage: 65 regular videos, 1 Short, 0 public archived streams; matches precheck
- Catalog raw dataset: 2,038,742 bytes; SHA-256 `1d55bcf8a429a8619bb7238cea58f0310770c01ad05e69f40f135fbaa9139dc1`
- Raw dataset: 23,770 bytes; SHA-256 `493caa1673a7d73d9659fe913c7f00a52b179bf43dfbb5e17b6966cb5101cb45`
- Transcript: 13,195 bytes; SHA-256 `a44706058e070033e3e63321ef1b1305eecbe8e70dcd27c664d961646fed8cda`
- Raw-retention verifier: `VERIFIED`
- Focused Channel-ID regression: 1 passed
- Full Apify-ingest module: 21 passed
- Console verification: run ID, target, build, input limits, result count, video identity, status, and `$0.004` cost match local evidence
- Billing detail: Console shows `$0.004`; the local cost-observation row remains non-final because charged-event API fields were unavailable and were not fabricated

## Dataset lineage decision

`DS-000028` remains the Dr. Okoro acquisition lineage. Control and catalog runs retain separate immutable raw evidence and append-only snapshots. One overlapping control video was logically deduplicated by YouTube Video ID; original control evidence remains unchanged.

## Current boundary

- Approved additional acquisition cap: `$4.50`
- New-campaign actual spend: `$0.264`; remaining: `$4.236`
- Apify subscription: Free plan; `$5.00` monthly free platform usage; no payment method configured
- Apify current-period usage after catalog run: `$0.41 / $5.00`; `$4.59` remains
- Actor price display: from `$4.00 / 1,000 videos` (`$0.004` per video)
- Actor/build: `streamers/youtube-scraper` / latest observed successful build `0.0.303`
- Catalog-run maximum cost setting: `$0.30`; actual cost `$0.264`
- Next channel: Doctor Thomas (`UCFuGMi0idGeyXl6wYK9hg7Q`), after usage capacity recovers
- Next state: `CODEX_USAGE_CHECKPOINT_90_PERCENT`

## New-campaign ledger

| Run | Channel | Content Type | Results | Max Charge | Actual Cost | Cumulative Actual |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `uLT4StERHwuiLthti` | Dr. Okoro | regular + Shorts | 66 | `$0.300` | `$0.264` | `$0.264` |

Historical control remains separately recorded at `$0.004`.

## 90% usage checkpoint

- Codex weekly usage reached 90% after successful ingestion. No further Actor run started.
- Inventory DB: integrity `ok`; foreign-key violations `0`; SHA-256 `247294558d26b38d02d056cdbe52cc1009ea206c18c4106008a3fe5aa859c5d2`
- Registry DB: integrity `ok`; foreign-key violations `0`; unchanged SHA-256 `e8cacdccedca566b4d9c2c5a2bcb86ed07bdf3915aff2a41d5c9a227cffc47e6`
- Registry rebuild attempted after ingestion but stopped on `sqlite3.IntegrityError: FOREIGN KEY constraint failed`; transaction left registry DB unchanged and healthy. Diagnose before rebuilding next session.
- Full standard package generation deferred: mandatory 90% checkpoint forbids starting a large packaging job.

## Zero-spend Dr. Okoro precheck

- Public channel identity reconfirmed: `UCMJxAeBJ0d1JC937de1eZ0Q`, `@drmarcusokoro`
- Public channel header: 66 videos
- Regular-video catalog: 65 items observed across the complete public Videos tab
- Shorts catalog: 1 item (`PSukpB1Io-o`)
- Archived streams: 0 publicly exposed; no Live tab is present and the `/streams` route resolves to the Videos catalog
- Existing control video: `eD2OnCE8iKM`; retain and deduplicate by YouTube Video ID if a full run is approved
- Current Actor schema exposes separate limits for regular videos, Shorts, and streams
- Subtitle mode available: existing subtitles only; language `Any`; plaintext output
- AI video analysis remains off; no paid AI transcription is authorized
- No new Actor run or charge was started during this precheck

## Durable and local-only files

Tracked for commit:

- `data/manifests/DS-000028.md`
- `data/manifests/apify/4Jkn3vuO1nDp57HfT.json`
- this checkpoint

Remote-preservation set:

- `data/raw/channel-data/DS-000026/preflight/29_channel_public_counts.json`
- `data/raw/channel-data/DS-000026/preflight/29_channel_registry_export.json`
- `data/raw/competitors/DS-000028/dataset.json`
- `data/raw/competitors/DS-000028/apify/4Jkn3vuO1nDp57HfT/evidence/actor_input.json`
- `data/raw/competitors/DS-000028/apify/4Jkn3vuO1nDp57HfT/evidence/run_metadata_console_observation.json`
- `data/raw/competitors/DS-000028/apify/4Jkn3vuO1nDp57HfT/transcripts/eD2OnCE8iKM.txt`
- `data/raw/competitors/DS-000028/apify/uLT4StERHwuiLthti/raw/dataset.json`
- `data/raw/competitors/DS-000028/apify/uLT4StERHwuiLthti/evidence/actor_input.json`
- `data/raw/competitors/DS-000028/apify/uLT4StERHwuiLthti/evidence/run_metadata_console_observation.json`
- `data/raw/competitors/DS-000028/apify/uLT4StERHwuiLthti/transcripts/` (66 files)
- `data/manifests/apify/uLT4StERHwuiLthti.json`
- `data/catalog/youtube_inventory.db`
- `data/catalog/youtube_channel_registry.db` (Git LFS)

Correction (2026-09-22): owner policy requires remote preservation of canonical
raw evidence and valid project database snapshots. DS-000028 acquisition
evidence, existing DS-000026 preflight evidence, `youtube_inventory.db`, and
`youtube_channel_registry.db` passed integrity, secret, and size review for
remote preservation. SQLite WAL/SHM files, caches, temporary files, secrets,
and exact duplicate staging copies remain excluded.
