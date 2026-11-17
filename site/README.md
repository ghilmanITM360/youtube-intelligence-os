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
