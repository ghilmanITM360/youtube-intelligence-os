# Mark Invests: source completeness report

Snapshot timestamp: 2026-11-09T22:28:48.585Z. Coverage status: **GAP_FILL_NEWEST** (tranche G).

- Channel ID: UCcj_KU4ZN6bx6Ki68hNJWqw. Handle: @MarkBuildsUS. Subscribers: 19800. YouTube-reported videos: 98.
- Run limits: regular 22, Shorts 0, streams 0; max cost $0.09; captions/transcripts/AI off.
- Public master rows: 22 (regular 22, Shorts 0, streams 0); members-only excluded: 0.
- Date coverage: 2026-10-14T22:06:35.000Z to 2026-11-09T00:00:34.000Z.
- Core metadata completeness: 100.00%.
- Reuse delta vs PR #39 package (81 rows): 5 already packaged, 17 new.

## Coverage meaning
- COMPLETE: fetched rows (public + members-only) reached the channel's reported video count.
- COMPLETE_REGULAR_TAB_ONLY: the regular tab was exhausted below its limit; the reported total includes Shorts/streams this run did not request.
- PARTIAL: a run limit bound the result before the channel was exhausted.
- GAP_FILL_NEWEST: newest-first delta for a channel already packaged in PR #39; merge with that frozen snapshot by video_id.

## Limitations
- Counts are point-in-time snapshots. Views per day is not a velocity series.
- No caption, transcript, AI or media download. Thumbnail binaries were not fetched (dimensions/hashes UNKNOWN).
