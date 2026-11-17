# Reviewed registry ingestion inputs

Importer-shaped workbooks, materialized by `scripts/build_reviewed_channel_workbooks.py` from sources pinned by commit in each `REVIEW.json`. The source files are not changed. No database is written here.

Status: machine-checked by reading each workbook back with the importer's parser. Owner review is pending, and no row is registered yet.

Rules: a value the source does not know stays empty, never 0. Only timestamps to UTC and IDs to watch URLs are converted. All videos are transcript-pending because these sources carry no transcript text.

To register one, after owner approval and on the writer's claim:

```sh
mkdir -p /tmp/empty-transcripts
python scripts/register_supplied_channel.py \
  --workbook research/registry-ingestion/<slug>/<slug>_reviewed.xlsx \
  --transcripts /tmp/empty-transcripts \
  --transcript-pending-id <each id in REVIEW.json transcript_pending_ids>
python -m scripts.build_youtube_channel_registry --write-ledgers
```

The trial in `TRIAL.md` records what that route did. Registering rebuilds binary databases, so run it after PR #20 and the frozen-registry separation in PR #45, one channel at a time.

Open point: `barely-evolved` keeps the comment count and engagement of `4X3xd3MDZro` empty. The actor returned 0 on a partial row, while comments were not turned off. See its `REVIEW.json`.
