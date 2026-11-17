# Held-out v8 results — targeted test of FROZEN_RULES_v2 (colour + motion/journey only; LOCAL ONLY)

## Setup
- **Rules:** frozen 2026-11-08T20:41:49Z (`../FROZEN_RULES_v2.sha256`). The eval script re-checked every frozen hash before running.
- **Format labels:** M0 was recorded at 20:4xZ (`M0_format_labels.json`), before the motion labeller ran.
- **Sources:** all 6 source SHAs matched.
- **Measurements:**
  - `measured.json`;
  - `motion_labels.csv`;
  - `colour_<id>.csv`.
- **Viewed sheets:**
  - `<id>_holds.jpg` (6 sheets, used for M0 and C3);
  - `<id>_nondefault.jpg` (Jpy5 and zJNm, used for C2).
- **v7 is unchanged:** 19/23 = 82.6%, FROZEN_SET_DOES_NOT_HOLD.
- **Scope:** this is a targeted v8 pass on two rule categories. It is **not** a fresh pass of the whole ruleset.

| Check | Jpy55EgMQgY (L, MAP_TOUR) | RgBYohJ7mIk (L) | saj7b5C6TCM (L) | PUtI3xoaHx0 (L) | zJNmUWZXj2M (S) | alBQCm0QpJg (S) |
|---|---|---|---|---|---|---|
| C1 red full frames (Shorts) | not scored (pre-measured; 288 = 48 + 240) | not scored (288) | not scored (288) | not scored (288) | PASS 0 | PASS 0 |
| C2 conditional colour (viewed) | PASS 14/14 (10 DARK_FIELD: ocean-floor sections and silhouettes; 4 "RED_SOLID": a thin red water-level line, a classifier misfire, used as a mark) | PASS (trivial, 0 non-default tiles) | PASS (trivial, 0) | PASS (trivial, 0) | **FAIL** 2/5 (G0017/G0019 dark cinema-audience silhouettes OK; G0021–G0025 saturated climate map classed PAINTED_PLATE, and "map" is not in the frozen PAINTED condition list) | PASS (trivial, 0) |
| C3 photographs (viewed) | PASS | PASS | PASS (G0107–G0113 grey city map) | PASS (G0055 ngram chart is typeset UI) | PASS | PASS |
| C4 red ink present | PASS | PASS | PASS | PASS | n/a | n/a |
| M1 whole-frame camera / all ACTIVITY | PASS 1/70 ≤ 0.20 | PASS 4/58 ≤ 0.13 | PASS 1/71 | PASS 1/70 | **FAIL** 4/19 = 0.21 > 0.13 (G0028–G0036: a genuine whole-frame film-strip scroll) | PASS 0/28 |
| M2 ruler ≥3 ⇔ JOURNEY_LADDER | PASS 0 | PASS 0 | PASS 0 | PASS 1 | n/a | n/a |
| M3 object motion / all | PASS 2/70 | PASS 2/58 | PASS 1/71 | PASS 2/70 | PASS 2/19 | PASS 0/28 |

## Verdicts
- **Colour verdict: 17/18 = 94.4% → HOLDS.** Three caveats:
  1. Four of the six C2 passes are **trivial**: those videos had no non-default tile. Only Jpy5 actually exercised the conditional rule.
  2. The one failure was caused by how I wrote the rule, not by new art. Saturated maps fall into PAINTED_PLATE, and dev WH4g had the same pattern (10% PAINTED, maps), which I missed when listing the conditions.
  3. zJNm is not independent of dev, because its art is reused from WH4g.
- **Journey/motion verdict: 15/16 = 93.8% → HOLDS for ORDINARY/MAP_TOUR only.** The **JOURNEY_LADDER arm is UNTESTED**: no v8 long was a journey or ladder video (0 ruler labels).
  - What v8 does support: ordinary and map longs stay within the whole-frame camera budget, and ruler scroll does not appear without a ladder.
  - The single failure is a Short using a new **film-strip scroll** device: a horizontal strip of frames scrolls past.
- **Overall: 32/34 = 94.1% → FROZEN_SET_v2_HOLDS (targeted).**
  - It is not a full-ruleset pass.
  - The 2026 long stratum is still not covered.
  - Hold stillness was not tested.

## New findings (n=1 each)
1. **Film-strip scroll device in Shorts** (zJNm G0027–G0039, about 44–56 s). A film strip with sprocket holes scrolls horizontally through 4 moves of 12–15 f, and it reads as a whole-frame camera move.
2. **Stepwise depth counter on a fixed map** (Jpy5 G0049–G0131, −50 m → −5000 m → DRAINED). A numeric progress header on a map that does not move, combined with red circle callouts.
   - This is a "ladder without camera": progression is shown by relabelling, not by scrolling.
   - Production use: in a scale story, a counter on a static frame is the default; a ruler scroll is optional.
3. **Classifier limits to carry forward:**
   - a thin horizontal red line can be classed RED_SOLID;
   - saturated maps cross the PAINTED_PLATE threshold.

   v3 should add "map" to the PAINTED condition list, or a separate MAP_FILL class, and use a minimum thickness for RED_SOLID.
4. **Card correction** (MEASURED, all 44 local longs; see `../FROZEN_RULES_v2.md`): what was called a "12.0 s red title card" is really two cards.
   - A **2.0 s opening title card**: 48 f in 43/44 longs.
   - A **10.0 s red end screen**: 240 f in 40/44 longs.
   - Every long has both: 44/44.
   - Their total is 288 f = 12.0 s in 40/44 longs (280–287 f in the other 4).
   - Shorts have neither.

## What a further sample would need to justify
- **JOURNEY_LADDER (untested):** the only remaining candidates are dev or v7 videos. No fresh journey long exists locally.
- **2026 long stratum:** no fresh local source exists.
- **Map Shorts:** the M0 25% map threshold misses Shorts whose camera moves sit in non-map scenes.
