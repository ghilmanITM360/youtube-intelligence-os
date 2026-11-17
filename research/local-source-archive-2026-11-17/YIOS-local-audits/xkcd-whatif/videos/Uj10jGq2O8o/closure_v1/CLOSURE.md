# Uj10jGq2O8o: visual-only closure (contract v1; LOCAL ONLY)

## Evidence base
- **Source:** sha re-computed = manifest (checks.json V1, 5a9f6249…). 2731 frames. Every frame is measured and covered once (V2).
- **Reused:** the rv1 ledger (73 segments, 37 holds) and its measurements. rv1 left 6 segments unviewed (128 frames).
- **New in closure_v1/:**
  - native frames;
  - holds_01..10.jpg: all 37 holds, viewed;
  - activity_grid.jpg: all 117 frames of G0032 at 1/8 scale, viewed;
  - strips of every frame of G0002, G0008, G0010, G0014, G0018, G0042, G0060, G0068 and G0072, viewed;
  - residue_crops.png;
  - per-frame change series;
  - checks.json.

## V4/V5 resolutions
| Seg | rv1 | Resolution |
|---|---|---|
| G0002 f40–47 | — | `0.9c (604,000,000 mph)` typed over 8 f. |
| G0008 f246–251 / G0010 f305–310 | PAN | 6-f **whole-canvas horizontal slides** with blur. NORMAL PHYSICS leaves and PARANORMAL PHYSICS (black panel, white line-art wizard, balls) enters, then the slide reverses. These are camera/canvas instances. |
| G0014 f427 | MEDIUM | **1-frame swap**: the blurred grey cup, bag and particles become crisp black line art (next frame 1 px). Resolved. |
| G0018 f485 | MEDIUM | **1-frame swap**: blurred grey ovals become crisp tadpole molecule marks (next frame 2 px). Resolved. |
| G0032 f982–1098 | MEDIUM, 111 f unviewed | Cut to the grey GLOW version of the dome scene (`PLASMIZED AIR`, `DEVELOPING FIREBALL`). Then a **slow continuous pan/zoom-out** (~117 f): the dome drifts left and shrinks slightly while `UNSUSPECTING BATTER` enters from the right edge (from ~f1046). The hold-pair shift is ≤96 px. This is one slow camera instance. |
| G0042 f1508 | MEDIUM | **1-frame pop**: red `DISINTEGRATING` appears over a struck-through `UNSUSPECTING`, the batter re-renders as dissolving, and `T = 60` becomes `T = 63 NANOSECONDS` (next frame 0). Resolved. |
| G0060 f2347–2352 | HIGH | 6-f fireball to mushroom-cloud growth (stem rises, cap billows). |
| G0068 f2492 | MEDIUM | **1-frame pop** of the red dashed radius circle (next frame 0). |
| G0072 f2599–2604 | — | 6-f cross-dissolve: the line-art cloud fades and a dark grey crater/glow appears over the map. |

**Hold residue:**
- f55 and f336: low-amplitude whole-drawing edge shimmer (max diff 45/43, largest component 53/29 px). The crops show no visible change, so these are encoder residue (NOISE by viewing).
- **f2262–2287 inside G0057** (after the G0056 white flash): a **sub-threshold glow decay**. 250–860 px/frame, max diff ≤23 except f2269–2271 (≤52); f2273 has a 21 px component; f2278 is a 15.9k px step (component 960 px) on the skyline, fireball and gradient. Viewed crops show gradient-banding rings and edge brightness changes only, not a drawn object. Classified as GLOW_DECAY (an intended post-flash fade below the segmenter threshold) and recorded as a hold sub-event, not a ledger miss.
- f504, f817, f1265, f1585, f1841 and f2375: NOISE.

## V6 creative (text read from native holds)
- **Text:**
  - `0.9c (604,000,000 mph)`;
  - `NORMAL PHYSICS` / `PARANORMAL PHYSICS`, `~0c (80 mph)`;
  - `~1,000 mph`, `604,000,000 mph`;
  - `PARTIAL VACCUUM` (sic), `FUSION ZONE`;
  - `DISINTEGRATING PITCHER`, `BALL`, `T = 30 / 60 / 63 / 75 NANOSECONDS`;
  - `PLASMIZED AIR`, `DEVELOPING FIREBALL`;
  - `UNSUSPECTING BATTER` → red `DISINTEGRATING` with the old word struck through, red `1c` sine wave;
  - `DISINTEGRATED PITCHER / BATTER / CATCHER / REFEREE`, `UNSUSPECTING BACKSTOP`.
- **Colour:**
  - off-white with black line art;
  - a black DARK_FIELD panel (PARANORMAL);
  - grey GLOW plates (dome, flash, crater);
  - grey skyline and ground fills;
  - a grey street map (achromatic, **not** MAP_FILL) with a red pin and a red dashed circle;
  - red only for marks and labels.
  - No photographs and no full-frame red.
- **INFERRED rv1 claims tested:**
  - G0032 "CUT_TO_GREY_THEN_PAN_RIGHT" is confirmed (pan plus slight zoom-out).
  - The G0016 "ZOOM" is not re-tested; it remains as rv1 recorded it.
- **Originality flag:** the wizard (pointed hat, long beard, staff) resembles a well-known film character. Use a generic, distinct design.

## V7
- `reconstruction_blueprint_v2.md`: per-state prompts, motion, continuity, QA and originality.
- **Format:** ORDINARY escalation Short with two canvas-slide instances and one slow pan.
- The two 6-f slides are separate instances, 54 f apart. They count as a merged multi-move instance under FROZEN_RULES_v3 (≤3.0 s gap, no non-camera activity between) **only if** no non-camera ACTIVITY lies between them. None does (G0009 is a HOLD).
- So this is a **dev-library candidate F_SCROLL-like pair**, but it is a panel slide back and forth, not a strip/axis/ladder translation. Under the frozen F_SCROLL definition it would need a viewed strip/stack translation, which a two-panel A/B slide is not. It is recorded as an observation only: it was already in the dev library and is not a test.

## Status
**VISUAL_ANALYSIS_COMPLETE** (visual-only contract v1). visual_script_mapping, audio and AV are out of scope and remain unsigned.
