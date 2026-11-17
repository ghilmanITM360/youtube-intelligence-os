# YIOS Data Inventory Report — 2026-11-12 (read-only; no data modified)
Method: sqlite3 read-only (mode=ro) counts on 4 catalog DBs + file counts under data/ research/ docs/. No performance conclusions.

## DBs
| DB | Location | Channels | Videos | Transcripts (text>0) | Thumb URLs |
|---|---|---|---|---|---|
| finance_economics_complete.db | yios-audit-fixes worktree, branch data/finance-economics-complete-2026-11-11 | 69 (68 w/ videos) | 3,634 | 3,450 rows / 3,410 videos | 3,634 |
| senior_health_complete.db | main checkout (uncommitted modification present) | 159 (84 w/ videos) | 5,513 | 1,936 | 807 |
| youtube_channel_registry.db | main checkout | 75 (29 identity-only, not extracted) | 2,303 | 2,291 real + 12 placeholders | 1,907 |
| youtube_inventory.db | main checkout | 10 | 667 | 666 available, 2 unavailable | 478 evidence rows |
Union by video_id across all 4: 10,264 unique videos; ~176 distinct channel ids (upper bound, overlap/handle-vs-id not fully reconciled).
## Gaps
- Senior health: 75 of 159 channels have zero videos; only 961 of 5,513 have likes/comments; 1,936/5,513 transcripts.
- Finance: 386 videos metadata_level PARTIAL; 199 transcripts ASR_UNCERTIFIED; 1 PARTIAL; 1 channel UNAVAILABLE_OR_DELETED; likes ~3,248, keywords only 446.
- Registry: 29 channels not extracted; transcript_status NONE for 29.
- Real thumbnail IMAGE files are scarce: only thumbnail URLs for most; ~56 thumbnails in DS-000032 plus evidence rows. 1,390 jpg + 129 png under data/research are mostly forensic frames.
## Files
data/raw 1.3G total data; competitors 952 files/597M; forensic-analysis 1,314/220M; channel-data 88; first-party 70 (no real analytics ingested); global-youtube-knowledge 20 (DS-000011/18/31); docs 462; research 83.
## Knowledge resources
DS-000011 (Hook guides, Packaging SOP, Viral checklist, algorithm guides, Intro/Script analyzers), DS-000018 (2026 algorithm update snapshot), DS-000031 corpus; docs/research senior-health 2026-09-25; ~71 forensic folders in ~/YIOS-local-audits. Not yet properly inspected: DS-000031, DS-000018 zip, many DS-0000xx competitor sets, vidIQ screenshots (DS-000032).
## Access
- yt-dlp: used earlier this session (free, works); not in project venv.
- Chrome browser: works; youtube.com navigation BLOCKED by tool policy.
- vidIQ web app: logged in (verified, feed loads). Account data shown belongs to owner's own channel, not the research niches.
- Google Trends: reachable in Chrome (classic Explore page loads, no login). pytrends not installed.
