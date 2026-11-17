# Senior-health database (split, git-safe)

GitHub rejects files over 100 MB, so the one-file DB is split by table and by channel range. Nothing is lost: row counts are asserted equal to the working DB on every build.

| File | Tables | Notes |
|---|---|---|
| `senior_health_core.db` | `channels`, `videos`, `ds34_records`, `transcript_index` | Everything except transcript text. `transcript_index.shard` says which transcripts file holds the text. |
| `senior_health_transcripts_1.db` .. `_3.db` | `transcripts` | Shard = channel rank by (tier, name), 3 fixed ranges, so a finished shard never changes. |

Rebuild (from the local working DB `data/catalog/senior_health_complete.db`, gitignored): `python3 scripts/build_senior_health_split.py`. Integrity: `SHA256SUMS.txt`.

Query across files:
```sql
-- sqlite3 senior_health_core.db
attach 'senior_health_transcripts_1.db' as t1;
select v.title, t.word_count from videos v join t1.transcripts t using(video_id) limit 5;
```
Transcripts are `[seconds] text` lines; creator caption preferred, else auto caption in the original language, never translations. Coverage per video: `research/senior-health-master/TRANSCRIPT_COVERAGE.csv`.
