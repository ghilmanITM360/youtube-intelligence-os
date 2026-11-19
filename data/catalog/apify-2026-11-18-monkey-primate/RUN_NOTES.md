# Apify run 2026-11-18: Monkey Economics + Primate Science

Actor `streamers/youtube-scraper` (build 0.0.335), run from the owner's Apify Console (Personal account, signed-in Chrome). Cap $0.30 per run, subtitles `en` on. Datasets downloaded from Console to `~/Downloads`, copied here unchanged.

| Channel (id) | Tab | Run id | Rows | Charged |
|---|---|---|---|---|
| Monkey Economics (UCssa3kvvvzM5cUeOG-FnQIw) | videos | fcONxAeiuoalTdytW | 19 | $0.072 |
| Monkey Economics | shorts | mKe8JMN7uKclbmCNz | 41 | $0.164 |
| Primate Science | videos | 3WH1iLiSqSfDcB66b | 6 | $0.024 |
| Primate Science | shorts | SzXTtdClCedfGZpmv | 4 | $0.012 (dataset has 4 rows; $0.012 as shown by Console) |

Row totals match YouTube's reported counts (60 and 10). Streams not requested. Total about $0.27. Every row has an auto-caption transcript.

Ingest: `ingest_to_niche_dbs.py` writes Monkey Economics into `../finance_economics_complete.db` and Primate Science into new `../science_complete.db` (same schema). Raw rows are kept in `apify_rows` (batch `apify_2026-11-18`). Transcript text is the SRT with timing stripped; the SRT itself is in the raw JSON.
Not done: no thumbnail download, no classification, no registry/inventory catalog registration.
