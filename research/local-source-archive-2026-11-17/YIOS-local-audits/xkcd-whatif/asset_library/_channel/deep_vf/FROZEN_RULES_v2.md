# Frozen rules v2 — targeted held-out v8 (colour + motion/journey only; LOCAL ONLY)

Frozen at the `date -u` stamp in `FROZEN_RULES_v2.sha256`. That file also hashes this document, the selection file `heldout_v8_selection.json` (seed 20261110) and the two measurement tools. No v8 frame, sheet or motion label was opened or run before this freeze.

**Scope.** This is a targeted test. It covers only the two categories that failed in v7:
- colour/red usage;
- camera share in the journey format.

A v8 pass is NOT a fresh pass of the whole ruleset. The v7 result stays **19/23 = 82.6%, FROZEN_SET_DOES_NOT_HOLD**, unchanged.

## Exposure statement
- **v8 longs** (Pop-6, quant-only before this pass):
  - Jpy55EgMQgY (2024H1)
  - RgBYohJ7mIk (2024H2)
  - saj7b5C6TCM (2025H1)
  - PUtI3xoaHx0 (2025H2)
- **What was already seen or measured for them before the freeze:**
  - frame 3 (opening study);
  - automated 1-frame share;
  - saturation share (`colour_mode_share.csv`);
  - red full-frame run lengths (`v2/title_card_durations.csv`, computed this pass for all 44 longs).
- **Partial visual exposure through Short excerpts in the reviewed library:**
  - Jpy55EgMQgY has the child Short aMshLs0YCTQ (DEV);
  - saj7b5C6TCM has the child Short jVy3qd70AqU (HELDOUT1).
  - These two longs are therefore not visually independent of the dev set.
- **v8 Shorts:**
  - zJNmUWZXj2M: never ingested or viewed. Its caption matches dev long WH4g1ptJ-70, so its art is probably reused from a dev video, and it is **not independent of dev**.
  - alBQCm0QpJg: never ingested or viewed, and no caption match. It is the most independent pick.
- **Coverage gap:** no 2026 long exists outside prior use. Pop-6 has no 2026 upload, so the 2026 long stratum is **not covered** by v8.
- **The tools were sanity-checked on v7 videos only:**
  - RULER_SCROLL detection on e3uk7jU3RHo gave 13 labels, against 0 on the other three v7 longs.
  - All thresholds below come from DEV videos only.

## Corrected title/end-card fact (from `v2/title_card_durations.csv`, MEASURED, all 44 local longs)
- The red full frames (mean R>150, G<110, B<110) in every long form **two separate runs**:
  - an **opening title card**: 48 f = 2.0 s in 43/44 longs (p2M8Y0z9Rl0: 45 f), starting at 6–30 s;
  - a **closing red end screen** (credits and books): 240 f = 10.0 s in 40/44 longs (jgafb8G7i4o 232, UQgw50GQu1A 236, DiWFXv9N0Vs 239, p2M8Y0z9Rl0 241), running to the last frame.
- The earlier claim "a 12.0 s red title card in 44/44" summed these two cards. 288 frames is the **total** red-card time in 40/44 longs (280–287 f in the other 4).
- The cards were checked by viewing frames 175, 4800 and 4984 of 2LSyizrk8-0.
- Shorts have neither card: 0 red full frames in 20/20 dev Shorts.

## Colour rules (colour verdict)
**Measurement.**
- Each automated HOLD is represented by its middle frame, decoded natively in colour at 320×180 (Shorts 180×320).
- Each frame is classed by `colour_classes.classify` as one of: LINE_ART, RED_MARK, COLOUR_ACCENT, TINT_REGION, RED_SOLID, GLOW_DARK (read as **DARK_FIELD**), PAINTED_PLATE or TITLE_CARD.
- Dev class shares come from the library state JPGs (`v2/colour_<id>.csv`, 44 videos). Exemplar sheets for each class were viewed.

**Dev findings that make v1 wrong:**
- RED_SOLID already occurs in dev: magma (4ZVt), fire (TFhr), a red can (9VG0), heat regions on maps (WH4g) and a laser (JqFS).
- DARK_FIELD (space/night) makes up 0–78% of states.
- 2LSyizrk8-0 G0038/G0070 contain blurred photographs (a "camera resolution" demo).

- **C1 (MEASURED; Shorts only).** Zero red full frames.
  - For the v8 longs this was already measured before the freeze, so C1 is reported but **not scored** for them.
- **C2 (VIEWED; conditional colour).** Every hold tile whose class is PAINTED_PLATE, RED_SOLID, TINT_REGION or DARK_FIELD must show its referent:
  - PAINTED_PLATE: sky, sunlight, sunset, night sky, aurora, fire, explosion, lava, plasma, a glowing light source, or a degraded photo-like image framed as what a camera or sensor sees.
  - RED_SOLID: an object or region that is red, hot, burning or dangerous in the story (fire, magma, laser, a heat or danger zone on a map, a red-coloured prop). Never a decorative background panel.
  - TINT_REGION: map land, sea or climate zones, terrain, a diagram fill, or flat pastel sky or ground.
  - DARK_FIELD: space, night, underground or deep water, darkness, silhouettes.
  - **Pass** when ≥90% of the video's non-default tiles meet their condition. A video with 0 non-default tiles passes trivially, and that is recorded.
- **C3 (VIEWED; photographs, revises S6/L2).** Photographic material appears only as a degraded or blurred in-story camera or sensor image. Everything else is line art or flat fill.
- **C4 (MEASURED; longs).** Red ink exists: at least one hold tile is classed RED_MARK or RED_SOLID. Dev: 22/22 library longs.

## Motion / journey rules (journey verdict)
**Measurement.**
- `motion_classes.py` runs on automated segments_v1 ACTIVITY segments longer than 6 f. It uses Farneback flow on edge pixels and labels each segment WHOLE_FRAME_CAMERA, RULER_SCROLL, OBJECT_MOTION or NO_TRANSLATION.
- Validation against the dev reviewed subtypes (PAN/ZOOM/SCROLL): camera precision 0.92, recall 0.77 (54 TP, 5 FP, 16 FN; 263 segments over 22 dev longs). The labeller under-counts slow or partial moves.
- All shares below use **all** automated ACTIVITY segments as the denominator. This is the same denominator as v7's "7–9 of 75".
- The v1 limit of 6% did not match the dev distribution under this measure: dev longs range 0–0.176.

- **M0 (VIEWED, recorded BEFORE the labeller runs).** The format label is read from the holds sheet:
  - **JOURNEY_LADDER**: a persistent measurement axis, ruler, altitude or scale ladder is visible across ≥3 holds, or the spine is a continuous traversal through one space;
  - **MAP_TOUR**: maps fill ≥25% of hold tiles;
  - otherwise **ORDINARY**.
  - Dev labels:
    - JOURNEY_LADDER: oTzW-mTQd5w (continuous ascent) and Z_xJ40QXu7Q (persistent height axis);
    - MAP_TOUR: WH4g1ptJ-70 (and Short GgEGcxJRDik);
    - all others ORDINARY.
- **M1 (MEASURED).** WHOLE_FRAME_CAMERA / all ACTIVITY must stay within these limits:

  | Format | Longs | Shorts |
  |---|---|---|
  | ORDINARY | ≤ 0.13 (dev max 0.127, 2LSy) | ≤ 0.13 (dev max 0.129) |
  | MAP_TOUR | ≤ 0.20 (dev 0.176) | ≤ 0.45 (dev 0.44) |
  | JOURNEY_LADDER | ≤ 0.13 | — |

  The JOURNEY_LADDER limit encodes the claim that a journey's extra motion is axis/ruler scroll, not more whole-frame camera. Dev: Z_xJ 0.061, oTzW 0.000.
- **M2 (MEASURED + VIEWED; longs only).** RULER_SCROLL count ≥3 **if and only if** M0 = JOURNEY_LADDER. ORDINARY and MAP_TOUR longs have ≤2 (dev max 1).
  - Not applied to Shorts: the portrait side band is not validated, and dev wBLVmEZV2Oc gave 4 false positives.
- **M3 (MEASURED).** OBJECT_MOTION / all ACTIVITY must be:
  - longs ≤ 0.25 (dev max 0.239);
  - Shorts ≤ 0.33 (dev max 0.32).
- **Not tested:** hold stillness. A single still tile cannot show idle motion. It is dropped from L3 and left as an open item.

## Scoring
- **Colour verdict:**
  - longs C2 + C3 + C4 = 12 checks;
  - Shorts C1 + C2 + C3 = 6 checks;
  - 18 in total.
- **Journey/motion verdict:**
  - longs M1 + M2 + M3 = 12 checks;
  - Shorts M1 + M3 = 4 checks;
  - 16 in total.
- **Thresholds:**
  - each category HOLDS if ≥90% of its checks pass;
  - the overall v8 score holds if ≥90% of all 34 checks pass;
  - otherwise the failing rule is listed and only that category gets more samples.
- **Order of work:**
  1. ingest the Shorts;
  2. decode the hold sheets and view them for M0;
  3. write M0 to `heldout_v8/M0_format_labels.json`;
  4. run the colour classifier and the motion labeller;
  5. view the non-default colour tiles;
  6. score.
