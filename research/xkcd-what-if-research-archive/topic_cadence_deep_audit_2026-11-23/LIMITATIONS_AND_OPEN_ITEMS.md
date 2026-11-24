# LIMITATIONS_AND_OPEN_ITEMS
1. **YouTube HTTP 429**: bulk watch-page crawl was throttled; 5,701 empty rows discarded. Effect: search-result publish dates/views now FETCHED for 514 of 516 videos (see SEARCH_EVIDENCE_METADATA_UPDATE.md; filter-biased recent sample). **Update 2026-11-23:** the 429 cleared and the competitor resume crawl was completed for 9 channels (RESOLVED for 30/90-day cadence); 180/365-day cells and the search-hit metadata remain open.
2. **Google Trends**: reached via an unofficial endpoint (12 terms, web+YouTube, 12-mo + 3-mo, Worldwide, category 0, retrieved 2026-11-23 ~21:00-21:45 PKT). Single-term indices are self-normalised (not comparable across terms); broad concept terms, not the video questions. Topic-level volumes UNAVAILABLE. One series (moon tides, YouTube, 3-mo) failed.
3. **4-hour / 24-hour data**: only YouTube's "last hour"/"today" filter titles; no exact timestamps → not used for decisions.
4. **Book**: What If? text not available (OCR is private; only SHA-256 list). What If? 2 unchecked. Crosswalk = REPORTED question bank.
5. **Competitor metrics**: public lifetime views only; no CTR/retention/impressions; comments sampled only lightly (13 videos, 1,814 top-sorted comments; COMMENT_SAMPLE_FINDINGS.md), no first-party comments.
6. **First-party analytics**: none (channel unlaunched); Day-14/30/60 are plans.
7. **Science**: no expert review; drag input shared with prior audits; WIB-22/24/NEW-07/Apophis detail not recomputed; Artemis II distance claims in earlier audits not re-verified.
8. **Knowledge resources**: all 17 DS-000011 files opened (the folder has 17, not 18): 5 read in detail (DS000011_PACKAGING_AND_HOOK_APPLICATION.md), 12 reviewed in DS000011_REMAINING_FILES_REVIEW.md; the 117-page algorithm guide and 45-page updates PDF were read by structure and keyword search only, not line by line. DS-000018 snapshot (63 tabs, hashes match manifest; read by titles, three tabs and keyword search) and DS-000031 (partly line-read) now opened, see DS000018_DS000031_REVIEW.md; the 2026-11-11 supplement is also opened (DS000011_SUPPLEMENT_REVIEW.md: duplicate of DS-000018 content, not independent; txt/docx/xlsx compared by title only) (PARTIAL).
9. **Prior audits**: audit 1/2 only partly read; audit 2 provenance unknown. Machine B repo path absent on this Mac. Strategy-branch files 01-08 reports not read (only data files).
10. **Capacity**: no real production-hours data; workloads are assumptions.
11. **Search bias**: unpersonalised US-server results, top-N only; keyword-overlap column in TOPIC_RESEARCH_EVIDENCE.csv is a crude heuristic (not used for decisions; decisions were made by reading titles).
12. **Resolved 2026-11-24**: WhatIfAnimations has ~3.8K subs; "433K" is unsourced and not its subscribers or total views (see WHATIFANIMATIONS_DISCREPANCY_RESOLUTION.md). Origin of 433K stays unproven (likely a mislabelled view count of its 464K-view top video; inference). NEW-08 saturation not re-run with that video.
13. Live/premiere formats not collected (UNKNOWN, not zero).
14. Day-1 video status unknown: no record exists that the Day-1 video is produced.

13. **Done 2026-11-24**: NEW-08 saturation re-run with the 464K video (see NEW08_SATURATION_RERUN.md). Result: still REPLACE; demand real, exact-title lane crowded. Limits: two queries, crawled channels only, keyword rule for near premise.
