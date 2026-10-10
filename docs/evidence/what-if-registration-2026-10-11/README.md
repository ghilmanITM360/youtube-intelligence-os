# What If verified identity registration

This unit materializes PR #18's reviewed identity packet into the existing supplied-channel workbook shape. The packet and original official evidence JSON remain unchanged. `registration-result.json` pins their hashes and records exact IDs, title, publish time, channel ownership and importer result. The input workbook and canonical raw copy have identical hashes and represent one evidence source, not two independent observations.

Published timestamps are converted deterministically from the evidenced original offsets to UTC; both forms are retained. The importer requires exact text timestamps, so exported XLSX relationship targets and timestamp cell serialization were normalized before validation/import. Other source values remain unchanged. Blank subscriber/metric/format/description/transcript cells mean unobserved, not zero. The workbook banner records the official evidence retrieval date (10 October 2026), not a new scrape claim. No caption text or file was fabricated; the transcript directory is intentionally empty.

Reproduction on the pre-registration main checkpoint uses the same normal importer:

```sh
mkdir -p /tmp/what-if-empty-transcripts
python scripts/register_supplied_channel.py \
  --workbook docs/evidence/what-if-registration-2026-10-11/Verified_What_If_Identities.xlsx \
  --transcripts /tmp/what-if-empty-transcripts \
  --transcript-pending-id 9VG0yqq_PHM \
  --transcript-pending-id X97DDWvxaqQ \
  --dataset-name 'What If — reviewed verified identities, transcripts pending'
python scripts/register_structured_source.py verify --dataset-id DS-000035
python -m scripts.build_youtube_channel_registry --write-ledgers
```

Do not rerun against the registered snapshot: duplicate source/video safeguards reject it. DS-000035 contains two videos and zero transcripts. Historical video/channel snapshots, source contracts and forensic stages remain unchanged. Two pending transcript gaps are explicit; absent observations also create their normal availability gaps. Updated validator control totals reflect measured registration counts, while real/placeholder transcript totals stay unchanged. The actual imported pending identities survive hook/script joins; a disposable pending-only report marks both transcripts unavailable and produces zero hook/script features without crashing.

No paid acquisition, API integration, raw media addition, canonical history rewrite or source crosswalk promotion occurred. This new PR requires separate owner review and is not approved for merge.

Historical intelligence artifact bytes and the committed freshness registry are preserved. The normal read-only refresh planner now reports affected CH-000004 topic/packaging/hook-script artifacts as REFRESH_REQUIRED; this is recorded in `pending-intelligence-refresh.json`, not silently cleared. The deterministic clean-baseline test constructs its baseline in memory so a legitimate pending refresh cannot force false generation provenance. No analytical refresh was performed as part of identity registration.
