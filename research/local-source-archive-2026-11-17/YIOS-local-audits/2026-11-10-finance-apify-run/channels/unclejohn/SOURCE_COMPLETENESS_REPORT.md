# Uncle John Financial: source completeness report

Snapshot timestamp: 2026-11-09T22:29:56.529Z. Coverage status: **GAP_FILL_NEWEST** (tranche G).

- Channel ID: UCWugleQL2wqr5N1X4o8yyLw. Handle: @unclejohnfinancial. Subscribers: 47600. YouTube-reported videos: 60.
- Run limits: regular 9, Shorts 9, streams 0; max cost $0.08; captions/transcripts/AI off.
- Public master rows: 14 (regular 9, Shorts 5, streams 0); members-only excluded: 0.
- Date coverage: 2026-01-27T05:07:23.000Z to 2026-11-09T04:30:02.000Z.
- Core metadata completeness: 100.00%.
- Reuse delta vs PR #39 package (53 rows): 10 already packaged, 4 new.

## Coverage meaning
- COMPLETE: fetched rows (public + members-only) reached the channel's reported video count.
- COMPLETE_REGULAR_TAB_ONLY: the regular tab was exhausted below its limit; the reported total includes Shorts/streams this run did not request.
- PARTIAL: a run limit bound the result before the channel was exhausted.
- GAP_FILL_NEWEST: newest-first delta for a channel already packaged in PR #39; merge with that frozen snapshot by video_id.

## Limitations
- Counts are point-in-time snapshots. Views per day is not a velocity series.
- No caption, transcript, AI or media download. Thumbnail binaries were not fetched (dimensions/hashes UNKNOWN).
