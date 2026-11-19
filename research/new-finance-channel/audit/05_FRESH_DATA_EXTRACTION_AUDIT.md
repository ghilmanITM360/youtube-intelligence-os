# 05 Fresh Data Extraction Audit
Evidence checked today: 8 raw Apify JSON files in 05_FRESH_COMPETITOR_DATA/raw/ pass `shasum -a 256 -c` (all OK); run IDs are in the filenames; ingest script ingest/ingest_r1_r2_r3.py exists; DB has a video_snapshots table (820 rows) and 46 channel snapshots; DB latest scrape stamp 2026-11-18T17:18Z.
Raw items: 491 rows in 8 files (R1 59, R2 180, R3 252). Logged counts were R1 56 / R2 180 / R3 243 = 479; the 12-item gap is rows without a date or error rows (12 rows have no date). Explained but not individually reconciled: PARTIAL.
Cost log: $0.236 + $0.716 + $1.004 = $1.956 of $5.00, each run approved by the owner. VERIFIED from logs, not re-checked against the Apify console.
Freshness: 644 videos dated since 2026-10-19 across 52 of 72 channels; newest upload 2026-11-18. Upload date and extraction date are separate in the DB (published vs snapshot). 
Gaps: raw covers 23 channels only; the other 49 were not refreshed in this project (older Apify batches, latest dates mostly Aug-Sep 2026 = 2-3 months old). Not "fresh". Last-7-day coverage per channel not saved as a table. Broken-URL check not run. View counts are a point-in-time snapshot (2026-11-18).
Status: fresh data claim is TRUE for 23 channels (incl. all primary six), FALSE for the rest. PARTIAL.
