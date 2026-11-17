# Alicia Invests: source completeness report

Snapshot timestamp: 2026-11-11T17:25:44.000Z. Coverage status: **PARTIAL** (tranche X).

- Channel ID: UCFPfloFwa6X2UddqRH83rAA. Handle: @AliciaInvestsUS. Subscribers: 105000. YouTube-reported videos: 275.
- Run limits: regular 40, Shorts 0, streams 0; max cost $0.17; captions/transcripts/AI off.
- Public master rows: 40 (regular 40, Shorts 0, streams 0); members-only excluded: 0.
- Date coverage: 2026-09-21T11:06:57.000Z to 2026-11-03T11:00:19.000Z.
- Core metadata completeness: 100.00%.


## Coverage meaning
- COMPLETE: fetched rows (public + members-only) reached the channel's reported video count.
- COMPLETE_REGULAR_TAB_ONLY: the regular tab was exhausted below its limit; the reported total includes Shorts/streams this run did not request.
- PARTIAL: a run limit bound the result before the channel was exhausted.
- GAP_FILL_NEWEST: newest-first delta for a channel already packaged in PR #39; merge with that frozen snapshot by video_id.

## Limitations
- Counts are point-in-time snapshots. Views per day is not a velocity series.
- No caption, transcript, AI or media download. Thumbnail binaries were not fetched (dimensions/hashes UNKNOWN).
