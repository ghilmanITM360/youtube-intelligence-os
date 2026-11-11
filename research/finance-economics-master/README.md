# Finance / investing / economics master data (2026-11-11)

One rebuildable SQLite DB with every Finance, investing and economics channel the repo knows: `data/catalog/finance_economics_complete.db`
(built by `scripts/build_finance_economics_complete_db.py build`; read-only on the frozen `youtube_channel_registry.db`).

Tables: `channels` (availability, data_category), `videos` (metadata, thumbnail_url, `thumbnail_source` = captured | derived_standard_pattern,
`metadata_level` FULL/PARTIAL/TITLE_ONLY), `transcripts` (one row per video+source; plain text; caption_type; status), `apify_rows` (raw actor rows), `meta`.

Sources (all under `sources/`): registry slice; Apify 2026-11-10 (24 ch) and 2026-11-11 (21 ch, $4.352 of the $5 cap; run ids in the batch CHANNEL_STATUS.csv);
Machine A research (expansion masters, universe, landscape, queue; commit in `machine_a/SOURCE_COMMIT.txt`); Casual Finance catalog + Whisper-base ASR
(`casual_finance/`, ASR_UNCERTIFIED, commit in `SOURCE_COMMIT.txt`; kept here as its own copy because that channel also carries visual-forensics data on its research branch).
Transcripts: YouTube creator/auto captions via free paced yt-dlp backfill (never translations; stops on bot-check). Timestamped copies: `sources/transcripts_*.tar.gz`; raw json3 stays local.

Known gaps: Wealth Logic removed by YouTube (UNAVAILABLE_OR_DELETED); Tom Lazy Investor, Ivan Invests, Mark Retired at 55, Alicia Invests, Tom Talks Money
captured only newest 40 each (full catalogs exceed the $5 budget); videos with no caption track stay without a transcript (status in the coverage CSVs).
Per-channel completeness: `CHANNEL_DATA_FINAL.csv`.

## Final state (2026-11-12)
- DB `data/catalog/finance_economics_complete.db` (89.3 MB, integrity ok): 67 channels, 3,332 videos, 3,148 transcripts (3,108 videos with transcript), 2,787 captured thumbnail URLs (rest derived).
- Cap rule: per channel 100 videos (newest 50, top-viewed 30, lowest-viewed older than 90d 20), 60 transcript targets (30/20/10). Casual Finance is exempt (full 206-video catalog + Whisper-base ASR transcripts, ASR_UNCERTIFIED, kept as separate copy too). 445 videos dropped by the cap; raw data remains in `sources/`.
- Channels by category: Finance 32 COMPLETE, 7 PARTIAL_TRANSCRIPTS, 7 PARTIAL_VIDEOS, 1 UNAVAILABLE_OR_DELETED (Wealth Logic); Economics 13 COMPLETE, 1 PARTIAL_TRANSCRIPTS; Machine A landscape 6 PARTIAL_TRANSCRIPTS, 2 METADATA_ONLY.
- Apify spend $4.352 of $5 cap. Caption backfill: 969 targets, 967 complete, 1 partial (64% coverage), 1 without usable captions; no bot-check.

## Update 2026-11-12 — newest-100 top-up for the 5 Apify-capped channels
Tom Lazy Investor, Ivan Invests, Mark Retired at 55, Alicia Invests and Tom Talks Money had only the newest 40 videos from Apify.
Videos 41-100 (302 videos) were added with free, paced yt-dlp (metadata + creator/auto captions, one request per video, no bot-check, 0 failures).
Source: `sources/ytdlp_2026-11-12/` (metadata.jsonl.gz, extract.py, run.log) + `sources/transcripts_ytdlp_2026-11-12.tar.gz`.
These 5 channels now keep the newest 100 videos (not the 50/30/20 mix) and are all COMPLETE (100 videos, 100 transcripts, 100 thumbnails).
DB totals: 67 channels, 3,634 videos, 3,450 transcripts, 3,410 videos with transcript, 3,089 captured thumbnails. DB size 97.8 MB (close to the 100 MB limit; next growth needs LFS or a split).
No additional Apify spend (total stays $4.352).
