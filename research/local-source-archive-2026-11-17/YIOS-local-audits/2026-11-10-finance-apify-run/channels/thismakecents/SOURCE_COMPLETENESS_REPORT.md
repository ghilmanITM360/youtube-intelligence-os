# This make cents: source completeness report

Snapshot timestamp: 2026-11-10T19:49:51Z. Coverage status: **COMPLETE** (tranche T2).

- Channel ID: UCWrtDO6izx1KXQu_BZBrQYg. Handle: @CronusMakesCents. Subscribers: 4950. YouTube-reported videos: 20.
- Run limits: regular 27, Shorts 27, streams 0; max cost $0.22; captions/transcripts/AI off.
- Public master rows: 20 (regular 17, Shorts 3, streams 0); members-only excluded: 0.
- Date coverage: 2026-10-02T01:31:37.000Z to 2026-11-05T22:13:19.000Z.
- Core metadata completeness: 100.00%.


## Coverage meaning
- COMPLETE: fetched rows (public + members-only) reached the channel's reported video count.
- COMPLETE_REGULAR_TAB_ONLY: the regular tab was exhausted below its limit; the reported total includes Shorts/streams this run did not request.
- PARTIAL: a run limit bound the result before the channel was exhausted.
- GAP_FILL_NEWEST: newest-first delta for a channel already packaged in PR #39; merge with that frozen snapshot by video_id.

## Limitations
- Counts are point-in-time snapshots. Views per day is not a velocity series.
- No caption, transcript, AI or media download. Thumbnail binaries were not fetched (dimensions/hashes UNKNOWN).
