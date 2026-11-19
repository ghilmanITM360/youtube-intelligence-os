# 20 Audit Evidence Index
- DB: data/catalog/finance_economics_complete.db (queries: totals, per-channel coverage, 30/60/90-day windows, duplicates, availability; run 2026-11-18)
- Raw: 05_FRESH_COMPETITOR_DATA/raw/*.json + SHA256SUMS.txt (8 files, `shasum -a 256 -c` all OK, 491 items)
- Link check script output: 114 backticked refs, 18 flagged, all resolved by find except one old-project raw path (unverified)
- Folder listing: file counts per folder (see 03)
- Git: commit 13138e04 on data/apify-monkey-economics-primate-science-2026-11-18; untracked files unrelated
- Prior reports: 09_, 10_, 13_TITLE_MODELS, 16_, 17_, 18_, 19_, 20_, 21_, 22_, 23_ phase files
- Not inspected in this audit: original master prompt text re-read, Apify console, YouTube Studio, old project's 71 reports, Playbook PDF.
