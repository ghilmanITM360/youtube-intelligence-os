# Senior Health Acquisition Checkpoint

Updated: 2026-09-22

## Completed work

- Last completed channel: Dr. Okoro control acquisition
- Channel ID: `UCMJxAeBJ0d1JC937de1eZ0Q`
- Dataset: `DS-000028`
- Apify run ID: `4Jkn3vuO1nDp57HfT`
- Apify default dataset ID: `wcOVfRxeT5khIdk8O`
- Actor/build: `streamers/youtube-scraper` / `0.0.303`
- Result: `SUCCEEDED`, 1 regular video, 1 auto-generated YouTube subtitle
- Actual cost: `$0.004`, confirmed in Apify Console
- Cumulative senior-health acquisition spend recorded here: `$0.004`
- Git HEAD before this checkpoint commit: `27ae8d2bd7f94044e3fdf447d6c57c4d93791641`

## Validation

- `ingest-existing`: completed as `RUN-000025`; no partial registration found
- Inventory database: `PRAGMA integrity_check = ok`; `PRAGMA foreign_key_check` returned no rows
- Registered rows: 1 channel snapshot, 1 video, 1 video snapshot, 1 available transcript, 1 thumbnail-evidence row, 1 Apify source run
- Raw dataset: 23,770 bytes; SHA-256 `493caa1673a7d73d9659fe913c7f00a52b179bf43dfbb5e17b6966cb5101cb45`
- Transcript: 13,195 bytes; SHA-256 `a44706058e070033e3e63321ef1b1305eecbe8e70dcd27c664d961646fed8cda`
- Raw-retention verifier: `VERIFIED`
- Focused Channel-ID regression: 1 passed
- Full Apify-ingest module: 21 passed
- Console verification: run ID, target, build, input limits, result count, video identity, status, and `$0.004` cost match local evidence
- Billing detail: Console shows `$0.004`; the local cost-observation row remains non-final because charged-event API fields were unavailable and were not fabricated

## Dataset lineage decision

`DS-000028` is the Dr. Okoro acquisition lineage and currently contains one bounded control run. Existing schema and adapter support multiple run-scoped Apify acquisitions in one dataset through immutable raw payloads and append-only snapshots. A future approved full Dr. Okoro run may therefore remain in `DS-000028`, but it must use a new Apify run ID, its own retained raw JSON and hash, deduplicate by YouTube Video ID, and be described as a separate run. Current one-video control must never be described as a full-channel acquisition.

## Current boundary

- Proposed additional acquisition cap: `$4.80`
- Approval status: not approved in this conversation
- Apify usage display: `$0.14 / $5.00` in the sidebar and `$0.15 / $5.00` on Billing Limits; approximately `$4.85–$4.86` remains
- Actor price display: from `$4.00 / 1,000 videos` (`$0.004` per video)
- Next channel: Dr. Okoro full catalog, only after explicit cumulative-budget approval
- Next state: `AWAITING_TOTAL_ACQUISITION_BUDGET_APPROVAL`

## Durable and local-only files

Tracked for commit:

- `data/manifests/DS-000028.md`
- `data/manifests/apify/4Jkn3vuO1nDp57HfT.json`
- this checkpoint

Preserved local-only evidence:

- `data/raw/competitors/DS-000028/dataset.json`
- `data/raw/competitors/DS-000028/apify/4Jkn3vuO1nDp57HfT/evidence/actor_input.json`
- `data/raw/competitors/DS-000028/apify/4Jkn3vuO1nDp57HfT/evidence/run_metadata_console_observation.json`
- `data/raw/competitors/DS-000028/apify/4Jkn3vuO1nDp57HfT/transcripts/eD2OnCE8iKM.txt`
- `data/catalog/youtube_inventory.db`

No raw evidence or database binary will be staged.
