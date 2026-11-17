# Neu: source completeness report

Snapshot timestamp: 2026-11-11T17:15:57.000Z. Coverage status: **COMPLETE** (tranche X).

- Channel ID: UChS4VG1jXDcxDnUvwcMcxtg. Handle: @neu-youtube. Subscribers: 40000. YouTube-reported videos: 56.
- Run limits: regular 60, Shorts 0, streams 0; max cost $0.23; captions/transcripts/AI off.
- Public master rows: 56 (regular 56, Shorts 0, streams 0); members-only excluded: 0.
- Date coverage: 2025-09-24T16:41:38.000Z to 2026-11-11T13:32:34.000Z.
- Core metadata completeness: 100.00%.


## Coverage meaning
- COMPLETE: fetched rows (public + members-only) reached the channel's reported video count.
- COMPLETE_REGULAR_TAB_ONLY: the regular tab was exhausted below its limit; the reported total includes Shorts/streams this run did not request.
- PARTIAL: a run limit bound the result before the channel was exhausted.
- GAP_FILL_NEWEST: newest-first delta for a channel already packaged in PR #39; merge with that frozen snapshot by video_id.

## Limitations
- Counts are point-in-time snapshots. Views per day is not a velocity series.
- No caption, transcript, AI or media download. Thumbnail binaries were not fetched (dimensions/hashes UNKNOWN).
