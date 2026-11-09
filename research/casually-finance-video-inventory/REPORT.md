# Casual Finance — Complete Video Download Inventory (2026-10-19)

Channel: **Casual Finance** `@CasuallyFinance` — https://www.youtube.com/@CasuallyFinance — `UCrNfRFWnLC3tCy1TnyhVQ7g` (registry-verified 2026-09-14). Not Casual Economics / Casually Explained.

| Result | Value |
|---|---|
| Public videos enumerated (/videos 34 + /shorts 176; no /streams tab) | **210** (34 regular, 176 Shorts, 0 livestreams) |
| DOWNLOADED_VERIFIED | **48** (ffprobe + full decode + SHA256) |
| ZIP_ONLY_VERIFIED | 0 — every ZIP entry is byte-identical to a loose file in `Downloads/CasuallyFinance/` (counted once) |
| NOT_DOWNLOADED | **162** (24 regular + 138 Shorts) |
| Downloaded by type | 10 of 34 regular, 38 of 176 Shorts |
| Other (audio/transcript-only, unverified, uncertain, unavailable) | 0 |
| Download completion | 22.9% (48/210) |
| Metadata coverage (10 core fields) | 93.6% — gap is YouTube `language` (not exposed for 134 videos) |
| Local media files scanned | 54 folder + 54 ZIP entries; 0 unmatched |
| New since Oct-11 forensic enumeration (206 IDs) | 4 (`9eBM5IF_bco`, `7bm7XYssqlU`, `ffIiiPLDFdM`, `Es5c2MKzbDg`); 0 historical/absent |

Enumeration: complete for public tabs (0 failed IDs). Unlisted/private/members-only items cannot be seen from public tabs.

## Identity caveat
Local filenames contain **no YouTube ID**. A file is matched only when normalized title (exact, or SnapYT-truncated prefix ≥ 8 chars) **and** ffprobe duration (±2 s) agree; 17 files also match SHA256s already ID-verified in the Oct-11 forensic branch (`codex/casually-finance-forensic-research`). Title alone is never accepted. Strong, not cryptographic, proof.

## Files
- `CASUALLY_FINANCE_COMPLETE_VIDEO_DOWNLOAD_INVENTORY.xlsx` (6 sheets), `CASUALLY_FINANCE_VIDEO_INVENTORY.csv/.json`
- `LOCAL_MEDIA_SCAN.csv`, `VERIFICATION.json`, `metadata_receipt.jsonl`, `receipts/*.jsonl` (tab enumerations)
- `build_inventory.py` — reproducible; needs the raw yt-dlp output dir (see docstring). Re-run after any acquisition.

## Verification (all pass, see VERIFICATION.json)
unique IDs = rows; status counts sum to 210; downloaded/missing disjoint & exhaustive; every downloaded row has valid decode + 64-hex SHA256; URLs match IDs; ZIP copies not double-counted; CSV = JSON = workbook ID order; source files' size/mtime unchanged.
Not verified: workbook opened in Excel/LibreOffice (neither installed); formulas carry cached values and were checked structurally with openpyxl.

## Notes
- Per-video metadata used yt-dlp `mweb` client after the default client was bot-blocked. No cookies/credentials used. No media downloaded.
- Duration column is HH:MM as requested (Shorts read 00:00); `Duration (sec)` is added right of the table.
- Missing-video priority: HIGH = long-form or views ≥ 75th pct of missing; LOW ≤ 25th pct.
- Oct-11 workdir `/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research` is absent on this machine; only its branch copy was used.
