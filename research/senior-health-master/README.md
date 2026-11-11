# Senior Health — master index (all data, zero to date, 2026-11-11)

Single in-repo home for the senior-health niche. Everything here is derived read-only from files already in the repo; the raw evidence stays where it is (never moved or modified). Rebuild: `python3 research/senior-health-master/build_master.py`.

## Totals

| Tier | Channels | Videos | What exists |
|---|---:|---:|---|
| 1. Full package (registry) | 8 | 460 | metadata + descriptions + 459 real transcripts + thumbnail URLs (`data/catalog/youtube_channel_registry.db`, datasets DS-000028/29/30/32/33 …) |
| 2. Apify metadata, complete catalog | 21 | 501 | titles, views, likes, comments, dates, durations, descriptions, thumbnails — NO transcripts (`research/senior-health-apify-2026-11-11/`, PR #50) |
| 3. Public per-video metadata only | 55 | 4,513 | title/duration/keywords/description from DS-000034 (`data/raw/competitors/DS-000034`); only 15 of 5,007 records playable, no views, no transcripts |
| 4. Identity only | 75 | 0 | channel ID/handle/category known from discovery, no video data |
| **Total** | **159** | **5,370 unique video IDs** | **459 transcripts total** |

(Some tier 1/2 videos are also in DS-000034, so tier counts add to slightly more than the unique total.)

## Files
- `MASTER_CHANNELS.csv` — one row per channel with tier and per-source counts.
- `senior_health_master.db` — tables `channels`, `videos` (one row per unique video ID, `sources` lists where it appears).
- `build_master.py` — rebuild script. `SHA256SUMS.txt` — checksums.

## Where the underlying data lives
| Source | Path |
|---|---|
| Registry (transcripts) | `data/catalog/youtube_channel_registry.db` (Git LFS) |
| Apify 2026-11-11 run | `research/senior-health-apify-2026-11-11/` (raw/, per-channel JSONL, DB) |
| DS-000034 | `data/raw/competitors/DS-000034/` |
| Discovery inventory (143 leads) | `docs/research/senior-health-2026-09-25/forensic-v3/SENIOR-HEALTH-MASTER-INVENTORY-2026-09-28.*` |

## Not done
- Tier 2 and 3 channels are not in the registry DB; no transcripts for them yet.
- Registry was not modified.
