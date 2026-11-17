# Madeline: source completeness report

Snapshot timestamp: 2026-11-10T07:30:49.237Z. Coverage status: **COMPLETE** (tranche T2).

- Channel ID: UChghyih02gp-TC7w22ULaXQ. Handle: @Humza1255-m2p. Subscribers: 3430. YouTube-reported videos: 49.
- Run limits: regular 59, Shorts 0, streams 0; max cost $0.24; captions/transcripts/AI off.
- Public master rows: 49 (regular 49, Shorts 0, streams 0); members-only excluded: 0.
- Date coverage: 2026-08-04T18:00:16.000Z to 2026-11-07T17:49:34.000Z.
- Core metadata completeness: 100.00%.


## Coverage meaning
- COMPLETE: fetched rows (public + members-only) reached the channel's reported video count.
- COMPLETE_REGULAR_TAB_ONLY: the regular tab was exhausted below its limit; the reported total includes Shorts/streams this run did not request.
- PARTIAL: a run limit bound the result before the channel was exhausted.
- GAP_FILL_NEWEST: newest-first delta for a channel already packaged in PR #39; merge with that frozen snapshot by video_id.

## Limitations
- Counts are point-in-time snapshots. Views per day is not a velocity series.
- No caption, transcript, AI or media download. Thumbnail binaries were not fetched (dimensions/hashes UNKNOWN).
