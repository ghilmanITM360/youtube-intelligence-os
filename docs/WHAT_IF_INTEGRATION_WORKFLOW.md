# What If forensic integration workflow

## Current contract and evidence boundaries

Release 1.0.0 supplies 14 media sources and 11,585 source-declared observations. The reviewed crosswalk has 12 verified mappings and two unresolved mappings. Ten verified mappings exist in the canonical CH-000004 inventory. X97DDWvxaqQ and 9VG0yqq_PHM remain unregistered pending official acquisition. The selected canonical inventory has 83 unique What If videos; this integration has created zero videos and modified zero historical snapshots or transcripts.

The external corpus is immutable. Configure its location at runtime; no code assumes a home directory or machine name:

```bash
export YIOS_WHAT_IF_CORPUS_ROOT="/path/to/video data of what if"
python scripts/validate_what_if_source_contract.py
python scripts/stage_what_if_forensics.py
python scripts/stage_what_if_forensics.py
python scripts/promote_what_if_forensics.py
python scripts/promote_what_if_forensics.py
```

Run commands from repository root in a Python 3.12 environment with declared dependencies installed. First creation reports CREATED; the second run reports UNCHANGED. Promotion reports UNCHANGED when reproducing the already committed index.

## Data flow and durable local staging

The adapter validates the release manifest, source index, crosswalk and actual media hashes, then reads only eight canonical MASTER CSVs. It does not import legacy output or copy media. Normalization joins by exact approved YouTube identity, never by title. Unresolved and unregistered identities are held, not rejected or silently promoted.

Generated local staging lives at `data/staging/what-if-forensic/v1.0.0/` relative to repository root and is ignored by Git. Keep this directory in the durable checkout rather than a disposable worktree. It contains eight JSONL tables and deterministic `manifest.json`, which records release, transformation, source-manifest hash, catalog identity hash, accepted/held/rejected counts, table sizes and checksums. `lifecycle.json` separately records its UTC creation timestamp and deterministic manifest checksum. Keeping wall-clock metadata separate preserves byte-identical evidence reproduction. Existing creation time survives repeated generation. Old valid stages acquire lifecycle metadata only after their deterministic files validate.

Every normalized observation preserves canonical video ID, source video ID, slug, release, table, local row ID, CSV row number, timing, supplied confidence, media hash, original fields and transformation version. A source reference resolves as configured corpus root plus `production_intelligence_brain/01_master_data/<table>.csv#row=<n>`; the fragment identifies the CSV row and is not part of the filesystem path.

Current accepted/held/rejected rows:

| Table | Source | Accepted and promoted | Held | Rejected |
|---|---:|---:|---:|---:|
| MASTER_WORDS | 7,864 | 5,817 | 2,047 | 0 |
| MASTER_SENTENCES | 604 | 485 | 119 | 0 |
| MASTER_SHOTS | 200 | 146 | 54 | 0 |
| MASTER_STATES | 581 | 352 | 229 | 0 |
| MASTER_MOTIONS | 438 | 289 | 149 | 0 |
| MASTER_ASSETS | 448 | 323 | 125 | 0 |
| MASTER_AUDIO_EVENTS | 29 | 21 | 8 | 0 |
| MASTER_AUDIO_VISUAL_SYNC | 1,421 | 894 | 527 | 0 |
| Total | 11,585 | 8,327 | 3,258 | 0 |

## Promotion and Editing/Visual consumption

Promotion reads the durable stage, revalidates every table checksum, counts, identity digest, observation key and provenance, then produces `data/intelligence/channels/CH-000004/forensic-observation-index-v1.json`. A different existing index fails with PROMOTION_CONFLICT; it is never replaced automatically. Promotion does not write to SQLite.

```bash
python scripts/query_what_if_forensics.py --video-id mEUqVgGf4e0 > /tmp/what-if-query.json
python scripts/run_youtube_intelligence.py \
  --channel CH-000004 --opportunity CH-000004-OP-001 \
  --generated-on 2026-10-09 --output-dir /tmp/what-if-production-plan
```

The compact query validates stage/index agreement before returning sampled shot pacing, state progression, motion actions/relationships, asset types and recurrence across unique videos, audio timing, narration/visual offsets, and the first 30 seconds of narration/edit pacing. Missing or non-finite timing never becomes a numeric measurement. Sampled shots do not establish complete-video coverage; changes per minute use sampled durations only. Recommendations remain EVIDENCE_BACKED_HYPOTHESIS, retain exact source rows and supplied confidence, and make no causal performance claim.

The orchestrator resolves opportunity video IDs through the canonical catalog and attaches matching guidance to the Editing/Visual blueprint. It preserves Topic, Packaging, Hook and Script artifacts. Four matching canonical videos contribute 2,381 observations and 24 cited hypotheses to the dated OP-001 example, without adding any channel samples. If local staging is absent, forensic consumption is explicitly NOT_AVAILABLE; if staging or index is changed, consumption fails closed. Historical editing reports remain preserved rather than rewritten.

## Review an update before promotion

Do not edit generated staging. Regenerate a candidate directory and candidate index, inspect the delta, and preserve current stage/index until review succeeds:

```bash
python scripts/stage_what_if_forensics.py --output /tmp/what-if-stage-candidate
python scripts/promote_what_if_forensics.py \
  --stage /tmp/what-if-stage-candidate --output /tmp/what-if-index-candidate.json
python -m json.tool data/staging/what-if-forensic/v1.0.0/manifest.json > /tmp/what-if-before.json
python -m json.tool /tmp/what-if-stage-candidate/manifest.json > /tmp/what-if-after.json
diff -u /tmp/what-if-before.json /tmp/what-if-after.json
git diff --no-index -- \
  data/intelligence/channels/CH-000004/forensic-observation-index-v1.json \
  /tmp/what-if-index-candidate.json
```

`diff` exits 1 for a legitimate difference. Review counts, mappings, media hashes, release and transformation changes. For a new source release, preserve the old corpus and contract; use a new versioned source contract and stage path with `--contract` and `--output`. After approval, archive the previous ignored stage outside the active path and replace it with the validated candidate. Update the reviewed index in an atomic PR and regenerate dated production outputs. Never change a recorded hash merely to suppress a mismatch.

A source table or identity change invalidates staging/promotion; regeneration is required. Source-declared evidence and AI recommendations stay separate. No forensic row is an independent channel sample.

## Identity refresh and unresolved sources

The owner explicitly authorized a narrow official YouTube Data API refresh for CH-000004 on 2026-10-09, superseding the no-API rule only for this task. Repository currently has controlled Apify acquisition, but no existing `channels.list`/uploads/`playlistItems.list` acquisition implementation; no YouTube/Google API credential was available in the execution environment. Apify acquisition requires a separate approved cost cap and was not run as a substitute.

There is currently no executable official refresh command to document honestly. Do not invoke a guessed script or register videos from search snippets. Once API authorization is available, the official acquisition must follow: `channels.list(part=contentDetails)` to identify the channel's uploads playlist; paginate `playlistItems.list(part=contentDetails)`; then `videos.list(part=snippet)` for exact channel ownership, title and publish time. Preserve sanitized response provenance and retrieval timestamp; register only genuine new IDs through the catalog registration workflow with append-only metadata snapshots. Review a 83-video baseline diff before publication. Credential values must remain environment-only.

SRC01 candidate U8F7UNK9jco has a matching sunset question on the official public video search result. SRC02 candidate qu8nx1qUwEU has matching visible-light question text. Their media metadata contains encoding/duration information but no authoritative video ID. Direct official page fetches were throttled. These are research candidates, not verified source-byte identity joins; crosswalk stays UNRESOLVED and promotion excludes both.

## Rollback

Catalog identities, snapshots and transcripts are not changed by stage/promotion/query work, so no data migration rollback is needed. Preserve the immutable external corpus and ignored stage.

For a published change, revert the specific integration merge in a new review branch, selecting the exact merge SHA from GitHub. Do not reset shared main or force-push:

```bash
git fetch origin main
git switch -c codex/what-if-rollback origin/main
git revert -m 1 <integration-merge-sha>
python -m pytest -q
git diff --check
```

Review dependent later commits before reverting; revert dependent units newest first. Submit the revert through normal PR/CI/exact-head merge. For local generated staging rollback, move the current ignored stage to a retained archive path and regenerate the previous reviewed contract at its deterministic path. Restore the matching reviewed promotion index via a PR. No raw media or historical evidence should be deleted.

## Privacy and raw-media policy

No raw MP4, audio, dense frames, Studio exports, credentials, temporary query outputs, or duplicated release packages may enter this What If integration. Keep source corpus and generated stages local. Commit only reviewed contracts, checksums, code/tests/docs and derived summaries with provenance. New private-derived analytics belong under ignored first-party storage.

Pre-existing tracked audio/frames/private-derived artifacts are separately classified in [repository safety review](audits/WHAT_IF_REPOSITORY_SAFETY_2026-10-09.md). They are not silently removed by this integration. Broader repository sharing or history rewriting requires an explicit owner/security decision.
