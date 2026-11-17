# Frozen rules v3 — Shorts colour + motion (targeted held-out v9; LOCAL ONLY)

**Freeze.** The rules are frozen at the `date -u` stamp in `FROZEN_RULES_v3.sha256`. That file hashes:
- this document;
- `heldout_v9_selection.json`;
- the measurement tools (`v2/colour_classes.py`, `v2/motion_classes.py`, `v3/camera_instances.py`).

No frame, sheet or measurement of either v9 Short was opened, ingested or run before this freeze.

**Scope.** Only the two Short rules that failed in v8 are revised.
- **Unchanged:**
  - v7 = 19/23;
  - v8 = 32/34 (FROZEN_RULES_v2);
  - long rules = v2.
- **zJNmUWZXj2M is now training data for v3.** The v3 changes were written from its failures, so zJNm cannot test v3.

## Changes from v2 (Shorts only)
1. **C2 colour, MAP_FILL.**
   - New condition: a hold tile classed PAINTED_PLATE also meets C2 when, on viewing, it is a **MAP_FILL**: a map, globe or geographic cross-section whose land, sea, population or climate zones are flat saturated fills.
   - Each PAINTED_PLATE tile is given a viewed sub-label, MAP_FILL or PLATE, before C2 is judged.
   - All other v2 C2 conditions stay as written.
2. **M1 motion, camera budget by device instance.**
   - **Numerator:** WHOLE_FRAME_CAMERA *instances* (`v3/camera_instances.py`). An instance is a maximal run of camera-labelled ACTIVITY segments with no non-camera ACTIVITY between them, and ≤3.0 s from the end of one to the start of the next. Holds between them are allowed.
   - **Denominator:** unchanged, all ACTIVITY segments.
   - **Limits:** unchanged, ORDINARY ≤ 0.13 and MAP_TOUR ≤ 0.45.
   - **Dev check before freeze** (`v3/dev_camera_instances.txt`):
     - all 17 dev Shorts give the same value as v2 (no merges); maximum ORDINARY 0.129 and MAP_TOUR 0.44;
     - zJNm (training) goes from 4 moves to 2 instances, 0.105.
   - The raw move share is reported alongside, not scored.

## Rules that are unchanged (as in FROZEN_RULES_v2)
- **C1:** 0 red full frames.
- **C3:** photographs only as an in-story camera or sensor image.
- **M0:** format label, viewed from the holds sheet and written before the labeller runs.
- **M3:** OBJECT_MOTION / all ≤ 0.33.
- **Tools:** the classifiers are the frozen v2 copies; the thresholds are unchanged.

## Feature presence (decides which results count as "feature-present")
- **F_MAP (viewed, before scoring, from the holds sheet):** at least one hold tile is a MAP_FILL (saturated) map. A pastel TINT-only map does **not** count.
- **F_SCROLL (measured, then viewed):** at least one camera instance contains ≥2 camera moves, **and** viewing the frames of that run shows a strip, axis, stack or ladder translating across the whole frame. A single pan does not count.
- **Reporting:**
  - The C2 result on F_MAP-present tiles and the M1 result on F_SCROLL-present instances are reported **separately** from the overall score.
  - If a pick lacks its intended feature, that is reported as a **coverage gap**, not as a pass of the revised rule.

## Scoring
- **Checks:** 2 Shorts × (C1, C2, C3, M1, M3) = **10 checks**.
- **Pass bar:**
  - a category holds at ≥90%, both colour (6 checks) and motion (4 checks);
  - overall ≥90% = 9/10.
- **Independence:** the parent overlap (title, and ASR/caption after ingest) is recorded for each Short. A Short whose parent is in a used set is reported as not independent.
- **Order of work:**
  1. ingest the Shorts;
  2. check the parents' ASR overlap;
  3. make the holds sheets, then view them for M0, F_MAP and the PAINTED sub-labels;
  4. write `heldout_v9/M0_F_labels.json`;
  5. run the labeller and the instance counter;
  6. view the frames of camera runs for F_SCROLL;
  7. view the non-default tiles for C2;
  8. score.
