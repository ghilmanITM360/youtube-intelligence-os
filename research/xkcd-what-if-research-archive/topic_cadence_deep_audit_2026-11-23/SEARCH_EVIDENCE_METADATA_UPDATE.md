# SEARCH_EVIDENCE_METADATA_UPDATE (2026-11-23, after the 429 cleared)
**What was done:** scripts/fetch_search_hit_meta.py fetched the watch page of every unique search-hit video (516 ids) single-threaded; 514 returned exact publish date (with offset) and lifetime views, 2 failed (removed/unavailable → UNAVAILABLE, not zero). scripts/merge_search_meta.py wrote them into TOPIC_RESEARCH_EVIDENCE.csv (678 of 681 rows; pre-merge copy raw/TOPIC_RESEARCH_EVIDENCE.pre_meta.csv) and produced TOPIC_SEARCH_SATURATION_STATS.csv. Views are lifetime snapshots at fetch time (views_fetched_at_utc), not velocity (L6).

**Sampling caveat (important):** most queries used YouTube's "this week / this month / today" filters, so the sample is biased toward recent uploads (e.g. 34 of 39 NEW-06 hits are <30 days old). Counts of recent same-title videos measure *supply* in that sample, not total supply. Search relevance is also noisy: many high-view hits are older or off-premise (e.g. Red Bull space-jump, steak recipes), so max views per topic is NOT demand for the planned video. Medians of recent uploads are the more honest descriptive figure, and still say nothing about CTR or retention.

**What it adds (descriptive, OBSERVED):**
- Saturated and weak: NEW-06 (Moon vanished) 34 uploads in 30 d, median lifetime views of recent uploads 10; NEW-08, WIB-11, WIB-22, NEW-07 show the same pattern (many recent copies, medians 7–16 views). Supports the earlier REPLACE/saturation calls; it does not prove no audience.
- Voyager one light-day: top hits 627K views (8.9 d old, Today in the Space), 188K (3.8 d, Anton Petrov); 15 recent uploads, median ≈13K. Demand around the news is observed, but so is competition and a fast-decaying hook — consistent with keeping it a Short, not a long.
- Higher fall (WIB-36): 37 hits in 30 d, median recent ≈64 views; the very large numbers are old space-jump videos (BBC/Red Bull), a different premise. So "fall from space" interest exists in YouTube history, but that does not show demand for this specific comparison; keep Medium confidence.
- WIB-18 (steak): high-view hits are cooking recipes, not the space premise → no demand evidence for the premise; REPLACE stands.

**Decision impact:** no decision or score changed. The new metadata strengthens the saturation reading and the Voyager timing logic; it adds no CTR/retention evidence. Confidence levels unchanged.
