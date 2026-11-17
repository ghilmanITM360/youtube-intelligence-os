# Uncle Frank Retirement: source completeness report

Snapshot timestamp: 2026-11-09T22:30:40.325Z. Coverage status: **GAP_FILL_NEWEST** (tranche G).

- Channel ID: UCLh3aiudWdnfR0QDC8aLEhQ. Handle: @unclefrankretirement16. Subscribers: 899. YouTube-reported videos: 35.
- Run limits: regular 13, Shorts 0, streams 0; max cost $0.06; captions/transcripts/AI off.
- Public master rows: 13 (regular 13, Shorts 0, streams 0); members-only excluded: 0.
- Date coverage: 2026-10-07T15:25:16.000Z to 2026-11-09T17:25:30.000Z.
- Core metadata completeness: 100.00%.
- Reuse delta vs PR #39 package (27 rows): 5 already packaged, 8 new.

## Coverage meaning
- COMPLETE: fetched rows (public + members-only) reached the channel's reported video count.
- COMPLETE_REGULAR_TAB_ONLY: the regular tab was exhausted below its limit; the reported total includes Shorts/streams this run did not request.
- PARTIAL: a run limit bound the result before the channel was exhausted.
- GAP_FILL_NEWEST: newest-first delta for a channel already packaged in PR #39; merge with that frozen snapshot by video_id.

## Limitations
- Counts are point-in-time snapshots. Views per day is not a velocity series.
- No caption, transcript, AI or media download. Thumbnail binaries were not fetched (dimensions/hashes UNKNOWN).
