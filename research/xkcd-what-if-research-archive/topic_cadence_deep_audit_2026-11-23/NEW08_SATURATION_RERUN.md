# NEW-08 saturation re-run with the 464K video (2026-11-24)

Candidate: NEW-08 "What if light were as slow as a car (100 km/h)" (calendar slot 11). Status before: REPLACE, "strong-but-saturated". Nothing below changes a score, the order or the cadence.

## Method (same evidence, one addition)
- Base: the 36 unique videos from the NEW-08 search rows in TOPIC_RESEARCH_EVIDENCE.csv (2 queries, YouTube search, unpersonalised, US).
- Added: WhatIfAnimations TAsqnXcCqRI ("What If Light Kept Getting Slower and Couldn't Stop?"), taken from UPLOAD_INVENTORY.csv (463,676 views, published 2026-10-19 00:06 UTC; age 35.7 days at the 2026-11-23 fetch). It had 0 search rows, so it came only from the channel crawl. Total now 37.
- "Near premise" = titles that say light or the speed of light is slowed, slow, 100 km/h, 30 mph, car or bicycle. This is a keyword rule I applied, not a human judgement. Titles were not watched.
- Scanned the other 958 inventory rows for the same premise: no other upload matches. The channel's other light titles are different premises (sound slower, light moving backward, light faster).

## Result
| Set | Videos | Published last 30 d | Median age (d) | Median lifetime views | Max views |
|---|---|---|---|---|---|
| Old base (36) | 36 | 31 | 3 | 65 | 4,267,718 |
| Base + 464K video (37) | 37 | 31 | 3.3 | 97 | 4,267,718 |
| Near premise only (19) | 19 | 14 | 15.3 | 33 | 4,267,718 |

- The 464K video is 35.7 days old, so it is not in the last-30-days count; the count stays 31.
- Median views rose from 65 to 97 only because one more high-view video entered a small sample. It is not a sign of a less crowded topic.
- Near-premise videos with at least 10K views: 5 of 19. Worlds In Motion 4.27M (1,248 d old), What If 1.08M (2,700 d; this is a "speed of light and sound switched" premise, a looser match), WhatIfAnimations 464K (35.7 d), Ifverse 17.8K (2.2 d), Just Suppose? 11.0K (23.9 d).
- The other 14 near-premise videos have 0 to 501 views after 0 to 121 days (median 33 across all 19).

## Reading (OBSERVED unless marked)
- OBSERVED: the premise has real past demand twice: a 4.27M video in 2023 and a 464K video from a 3.8K-subscriber channel in Oct 2026.
- OBSERVED: at least 14 near-identical "light 100 km/h" style uploads appeared within 30 days of the fetch. Most have under 500 views so far.
- INFERENCE: the copy wave is likely a reaction to the visible success of the 464K video or the older one. The data cannot prove cause or order. Copy timing was not tested.
- INFERENCE: the low views of copies do not show the topic is dead. They are new, mostly tiny channels, and no CTR, retention or thumbnail data exists. No forecast is made.
- The original call holds: demand is real, the exact-title lane is crowded, and prior art includes Gamow 1940 and the MIT Game Lab (from earlier research).

## Decision impact
- NEW-08 stays REPLACE as written. The condition "needs a clearly distinct question, for example a car-speed road scene" stands.
- Add to the NEW-08 notes: WhatIfAnimations (2026-10-18) is prior art on a near-identical premise, so a title like "What If Light Were as Slow as a Car?" would be the third high-view version, not a new idea. Changing the angle matters more than changing the title.
- No score was recomputed. The scores are subjective 0-3 editorial values and the new evidence does not map to a dimension in a way I can defend.

## Limits
- Search was top-N by relevance with two queries; other relevant videos may exist. The inventory covers 959 uploads from the crawled channels only, so a similar video on an uncrawled channel would be missed.
- The keyword rule can miss titles that use other wording and can include loose matches (the 1.08M video).
- Views are lifetime at fetch time. Age differs between videos, so views are not comparable per day.
