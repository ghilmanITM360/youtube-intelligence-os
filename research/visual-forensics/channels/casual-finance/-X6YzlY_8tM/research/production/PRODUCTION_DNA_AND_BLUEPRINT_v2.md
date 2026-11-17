# Video 005 — Production DNA and Original Reconstruction Blueprint (PARTIAL)

Video `-X6YzlY_8tM` "The SpaceX IPO... It's Worse Than You Think", 1280×720, 24 fps, 21,410 frames (14.9 min). Source SHA-256 `adff66768f5545cdd6f6bd2d2ddac9392c127adbc54fac4799b29f294b1463ec` re-verified against the manifest. Identity `HIGH_CONFIDENCE_NEEDS_REVIEW`.

**Status: `VIDEO_005_PARTIAL_STRUCTURE_SECOND_PASSED`. NOT `CT_SCAN_COMPLETE`.** Built from `integrated_v2/` (structure only, not semantically certified). Labels: MEASURED = computed from ledgers/frames; OBSERVED = reviewer saw it in frames (first-pass descriptors, mostly not re-verified); INFERRED = reading; UNAVAILABLE = not done; ORIGINAL_CREATIVE_INSTRUCTION = new guidance for your own video, not derived from the source.

## Known limits on every number
- Second pass covered 821 items: 402 candidates, 109 disputes, 109 unowned gaps, 200 merge flags. 429 of 831 candidates are still first-pass only. The CONFIRMED sample is n=143 of 572 (137 confirmed, 3 reclassified, 3 unverified), not all 572.
- 302 of the 821 second-pass items are SAMPLED (evidence jpgs / downscaled tiles); only 176 were viewed at native resolution. All 109 gaps are SAMPLED. Gaps are kept as separate segments (13.1% of frames), not absorbed into states.
- Merge rulings (194 accepted, 6 kept separate) accepted additive-element reveals as the same composition; a stricter rule would split many.
- 13 SPLIT proposals: 5 are supported by measured hard cuts (EP0188, 0206, 0211, 0212, 0229); 8 are reviewer multi-event claims not confirmed by measurement.
- Audio never heard: `AUDIO_NOT_VERIFIED`, `AV_CERTIFICATION_BLOCKED`. Machine ASR only.

## 1. Editing DNA (MEASURED)
- 478 states (32.1/min); median 1.21 s, mean 1.62 s, p10 0.33 s, p90 3.33 s, max 15.71 s.
- 284 compositions after merge rulings (19.1/min).
- 802 edit events (53.9/min), final types after second pass where reviewed:

| Type | Count |
|---|---|
| FULL_REPLACE | 216 |
| ADDITIVE_ENTRY | 188 |
| POSE_SWAP | 71 |
| OBJECT_MOTION | 61 |
| OTHER | 52 |
| CHARACTER_ANIMATION | 45 |
| TEXT_CHANGE | 34 |
| HIGHLIGHT_ADD | 30 |
| DRAW_ON_OR_REVEAL | 29 |
| WIPE_OR_FADE | 19 |
| EXPRESSION_CHANGE | 11 |
| PARTIAL_REPLACE | 11 |
| ELEMENT_SWAP | 11 |
| ZOOM_OR_SCALE | 10 |
| ELEMENT_EXIT | 9 |
| PAN_OR_SCROLL | 4 |
| PROGRESS_BAR_OR_COUNTER | 1 |

INFERRED: the rhythm is a hard cut to a clean drawn composition, then elements enter one at a time, then a pose swap or emphasis. About 27% of events are full replaces and 23% additive entries; character pose/expression/animation is about 16%.

## 2. Visual DNA
MEASURED share of state frames by layout family (first-pass family labels):

| Family | Frames | States | Median |
|---|---|---|---|
| F3 object/icon cluster | 22.0% | 114 | 1.1 s |
| F2 character+prop | 19.1% | 118 | 0.85 s |
| F1 character-only | 16.6% | 101 | 1.21 s |
| F5 screenshot+character | 16.1% | 42 | 2.21 s |
| F11 other composite | 7.8% | 28 | 1.44 s |
| F6 chart/graph | 7.0% | 27 | 1.12 s |
| F4 full-bleed screenshot/document | 5.1% | 22 | 0.81 s |
| F7 text card | 2.8% | 14 | 1.27 s |
| F10 title/end card | 1.9% | 6 | 1.25 s |
| F9 full-bleed drawn scene | 1.2% | 4 | 2.65 s |
| F12:blank-canvas | 0.2% | 1 | 1.83 s |
| F12:black-beat | 0.2% | 1 | 1.21 s |

OBSERVED (first pass, not re-measured): near-white flat canvas (mean luma about 248 MEASURED), stick-figure host with changing pose/expression, teacher/board scenes with chalk-style capitals, company wordmarks and news cards as rectangles, money-bag and rocket doodles, hand-lettered marker captions, third-party clips and a podcast clip placed inside the scene. Exact colours, typefaces and easing: UNAVAILABLE.

## 3. Motion grammar
- MEASURED: 321 of 478 states are described as static 2D; remaining states add leg/pose loops, embedded footage or host jitter (first-pass descriptor counts).
- MEASURED hard cuts: measured changed-fraction above 25% at f4712, f5067, f5278, f5310, f6237 and others; slow satellite drift (about f8261-8408) is one continuous drift, not many events.
- INFERRED: transitions are mostly hard cuts; 19 WIPE_OR_FADE events are the minority.

## 4. Reconstruction blueprint (ORIGINAL_CREATIVE_INSTRUCTION)
1. Canvas: near-white 16:9 canvas, one composition per beat, original presenter kit (3 poses, 3 expressions) in your own drawn style. Do not trace the source host, mascots, doodles or wordmark layouts.
2. Beat grammar: per narration sentence, cut to a clean composition (about 1.2 s median), add 2-5 elements at 0.3-1.5 s spacing, then one emphasis (underline, circle, or handwritten number). Allow a few 3-6 s holds for a data point or punchline.
3. Data scenes: build your own charts from cited public data with the source on screen; zoom/pan and draw a highlight. Never paste another creator's screenshot.
4. Company or news cards: use your own neutral typographic cards; use third-party logos or clips only with a documented licence basis.
5. Motion kit to build once: pop-in (scale+fade 4-6 frames), draw-on stroke, slide-in, zoom-to-region, pose swap (1-frame hold), arrow travel.
6. QA: cut rate near 32.1 ± 6 states per minute; one clear focal element per frame; source line for every on-screen number; licence record for every third-party asset.

## 5. Not done
Full semantic certification; second pass of 429 candidates; native checks of the 109 gaps; colour/typeface sampling; human listening and AV sign-off; live YouTube identity check; script-wide claim verification.

Files: `dna_statistics_v2.json`, `per_state_specs_v2.csv` (478 states), `composition_family_specs_v2.csv`.
