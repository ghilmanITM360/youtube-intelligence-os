# YIOS data browser

Read-only local website over the canonical DB. Python stdlib only, no install, no build step.

```bash
git pull && git lfs pull          # source DBs are tracked (the registry one via LFS)
python3 site/server.py            # first run builds data/catalog/yios_canonical.db (~1 min), then serves
# open http://127.0.0.1:8020
```

- The canonical DB is gitignored and rebuilt from the tracked source DBs, so every machine builds its own identical copy
  (`logical_sha256` in `data/manifests/yios-canonical-sources.json` proves it).
- Files only preview if they exist in your checkout; media outside git (see `docs/LOCAL_MEDIA_AVAILABILITY.md`) shows "not present".
- Viewers: `.md` rendered, `.csv/.tsv` sortable table, `.json/.jsonl` table or tree, `.gz` shown decompressed, images/audio/video inline.
- Another port: `--port 8030`. Another DB: `YIOS_CANONICAL_DB=/path/to.db`.

## What each page shows
- **Overview**: totals, uploads per year, biggest channels, how complete each field is.
- **Channels**: a scatter of every channel (videos vs typical views) and a sortable table with a per-channel uploads sparkline.
- **Channel report** (six tabs, with a dropdown to jump between channels): *Overview* (numbers, views-over-time chart, heat map, thumbnails), *Videos* (every video, sortable), *Titles* (which words and title features go with more views, long-form only), *Transcripts* (what the channel talks about, search and read inside the page), *Analyses & files* (every report, table, JSON and image about the channel, opened inline), *Data & sources* (completeness, source names, disagreements).
- **Videos**: filters (channel, type, year, transcript, specific file), title search and full-text search inside transcripts.
- Results are cached in memory per DB version and sent gzip-compressed, so every page after the first load answers in about a millisecond.
