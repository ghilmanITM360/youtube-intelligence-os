# Historical inventory rebuild gap (2026-09-24)

## Status

The committed `data/catalog/youtube_inventory.db` is the authoritative source
for six historical-catalog channels. It is complete, integrity-checked
(`PRAGMA integrity_check` = `ok`, 0 foreign-key violations), and reconciles
with the channel registry validator's expected totals.

`scripts/rebuild_inventory_catalog.py` is **not** a complete historical
reconstruction of that database. It reconstructs manifest/catalog bookkeeping
(datasets, ingestion runs, source-file rows for tracked `DS-*.md` manifests)
from tracked evidence in a clean clone. It does not, and by design cannot,
repopulate `channels`, `videos`, `video_snapshots`, `transcripts`, or
historical source relationships, because the raw evidence those rows depend
on is intentionally excluded from the tracked tree for several datasets.

CI now treats the committed database as authoritative: it validates the
committed file's integrity directly and exercises the partial rebuilder only
against a disposable temporary path (`--database "$RUNNER_TEMP/..."`), never
overwriting the canonical snapshot. See `.github/workflows/validate.yml`.

## Affected channels

Six historical-catalog channels currently depend entirely on the committed
canonical snapshot for their operational rows (447 videos total):

| Channel | Dataset | Videos |
|---|---|---|
| Mr. Finance | DS-000001 | 65 |
| Matty Invests | DS-000001 | 94 |
| Dr. Aliza Wright \| Advice | DS-000006 | 32 |
| Dr. Elias Senior Health | DS-000019 | 29 |
| Doctor Thomas | DS-000029 | 22 |
| Senior Health Hub | DS-000030 | 122 |
| xkcd's What If? | DS-000012/13/14/15/17 | 83 |

(Doctor Thomas and Senior Health Hub are also STANDARD_PACKAGE channels;
their video/transcript rows are additionally reconstructable from the
committed package workbook+ZIP under `data/extracted/channel-data/DS-*/packages/`,
discovered generically via `_standard_package_records()`. The other five are
not.)

## DS-000006 (Dr. Aliza Wright) limitation

DS-000006 includes tracked screenshot evidence, but there is no currently
proven machine-reconstructable source for every historical operational row
in that dataset. A complete raw-to-inventory rebuild for DS-000006 has not
been implemented and is not claimed. OCR or manual reconstruction of these
32 video records was explicitly out of scope for this fix and has not been
attempted.

## What is and isn't claimed

- Claimed: the current production/canonical repository state is reproducible
  from committed canonical snapshots (`youtube_inventory.db`,
  `youtube_channel_registry.db`) plus committed standard packages.
- Not claimed: every historical operational row is reproducible from raw
  files alone in a clean clone.

## Future work (not in scope here)

A full historical inventory reconstruction system — covering ZIP/XLSX
extraction, Apify data, screenshots, legacy packages, and forensic datasets
for all six historical channels — remains separate technical debt. It was
not implemented as part of this fix.
