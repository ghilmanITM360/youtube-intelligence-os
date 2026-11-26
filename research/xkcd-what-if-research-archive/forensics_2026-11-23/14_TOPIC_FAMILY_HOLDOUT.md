# 14 Topic-family stability check: result (2026-11-23)

Preregistration: `14_TOPIC_FAMILY_PREREGISTRATION.md` (SHA-256 `92fb7383864a281b3cb12748063fee3e8df38228150350618d7f2d430015c9f2`, written before the metrics were computed; self-recorded, not independently witnessed). Code `scripts/phase14_topic_family.py`; per-family numbers `14_TOPIC_FAMILY_RESULTS.csv`. Families were assigned mechanically from titles (4 families; 45 long and 46 Short classified videos).

| Test | Rule | Result |
|---|---|---|
| P1 words per total second within +-15% of the other families | K04 | **8 of 8 family x format cells PASS** (long 3.58 to 3.65 vs rest 3.59 to 3.60; Short 3.67 to 3.88 vs rest 3.74 to 3.84) |
| P2 attributed opening >= 80% (long) | K01 | **4 of 4 PASS** (HUMAN_BODY 5/5, SPACE 11/12, EARTH_WATER 13/13, MACHINE_OTHER 13/13) |
| P3 hold share within +-5 points of the other families | K09 | **8 of 8 PASS** (lowest long family EARTH_WATER 90.2 vs 93.6, a 3.4-point gap; Short 92.8 to 96.6) |

No failure was recorded. **What this is:** a stability check of three machine/script measures across four crude topic strata. **What it is not:** an independent holdout (the rules were formed on these same videos; titles are a weak topic proxy; a long video and its Shorts share a topic, so format cells are not independent; one coder family; the minimum family size is 5). It does not test the visual rules (K10 to K16, K20) or any rule needing viewing, which remain untested per topic family; the EARTH_WATER family is where the colour-fill exceptions of K10 concentrate.
