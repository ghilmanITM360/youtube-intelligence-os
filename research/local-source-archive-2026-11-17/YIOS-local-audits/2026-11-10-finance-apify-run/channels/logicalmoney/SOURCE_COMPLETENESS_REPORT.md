# Logical Money: source completeness report

Snapshot timestamp: 2026-11-09T22:32:23.768Z. Coverage status: **GAP_FILL_NEWEST** (tranche G).

- Channel ID: UCKhpM-cu2Cod-GyG6KngNYg. Handle: @LogicalMoney72. Subscribers: 28500. YouTube-reported videos: 26.
- Run limits: regular 11, Shorts 11, streams 0; max cost $0.09; captions/transcripts/AI off.
- Public master rows: 12 (regular 11, Shorts 1, streams 0); members-only excluded: 0.
- Date coverage: 2026-07-06T11:42:16.000Z to 2026-11-06T13:15:16.000Z.
- Core metadata completeness: 100.00%.
- Reuse delta vs PR #39 package (20 rows): 6 already packaged, 6 new.

## Coverage meaning
- COMPLETE: fetched rows (public + members-only) reached the channel's reported video count.
- COMPLETE_REGULAR_TAB_ONLY: the regular tab was exhausted below its limit; the reported total includes Shorts/streams this run did not request.
- PARTIAL: a run limit bound the result before the channel was exhausted.
- GAP_FILL_NEWEST: newest-first delta for a channel already packaged in PR #39; merge with that frozen snapshot by video_id.

## Limitations
- Counts are point-in-time snapshots. Views per day is not a velocity series.
- No caption, transcript, AI or media download. Thumbnail binaries were not fetched (dimensions/hashes UNKNOWN).
