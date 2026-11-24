# 07c Science-visual pass on the Shorts (extends `07_` and `07b_`)

Status: **self-review, one coder, still frames only.** Same question: when the narration states a number or scale comparison, what is on screen at that moment? Describes devices; no artwork or script reproduced.

## 1. What was run

- **Scope:** 46 Shorts in the campaign matrix; 44 have media (2 do not: UNAVAILABLE); 38 of the 44 have a quantity moment and were sampled; 6 have none by the regex (`kNry0bf7eC0`, `pMMo3XvoKD4`, `n_KUCunjMwQ`, `oLoxdLfB6Gs`, `SLd4hnmeW_g`, `35KZm1yiyIE`) and are listed, not coded.
- **Timing source:** campaign faster-whisper ASR for 16 of the 38 frames, local whisper.cpp `small.en` for 22 (`scripts/phase7c_asr.py` -> `phase7c_asr/`, `07c_SHORTS_INVENTORY.csv`). Machine transcripts, not listening, uncertified; two engines.
- **Selection (changed from the long-video rule because Shorts are short):** **one** frame per Short: the ASR segment matching the quantity regex nearest the middle of the runtime, still frame at the segment midpoint, portrait 360x640 cells, 6 per sheet (`scripts/phase7c_sample.py`, `07c_SAMPLE_FRAMES.csv`, `phase7c_frames/sheet1-7.jpg`; frame order = CSV row order).
- **Scheme:** v1.1 as in 07b, unchanged. Coding `07c_SCIENCE_VISUAL_CODING_SHORTS.csv`; tally `scripts/phase7c_tally.py`.

## 2. Results (counts)

| | Shorts (38 frames, 38 Shorts) | Long, pooled 7 + 7b (87 frames) | All (125) |
|---|---|---|---|
| LABEL (v1-equiv; includes TITLE, EQUATION) | 15 (11 plain, 3 EQUATION, 1 TITLE) | 31 | 46 |
| MECH (v1-equiv; includes 6 SCENE in Shorts) | 11 | 19 | 30 |
| AXIS | 3 | 10 | 13 |
| MAP | 3 | 8 | 11 |
| SBS / OBJ / SCALEREF / TALLY | 2 / 2 / 2 / 0 | 6 / 6 / 6 / 1 | 8 / 8 / 8 / 1 |
| Frames with a spoken quantity | 35 | 70 | 105 |
| ...restated on screen (YES) | 16 (46%) | 37 (53%) | 53 (50%) |
| ...PARTIAL / NO / UNCLEAR | 8 / 10 / 1 | 16 / 14 / 3 | 24 / 24 / 4 |
| Person as SCALE / PRESENTER | 1 / 4 | 7 / 12 | 8 / 16 |
| Red accent | 12 | 30 | 42 |

**Reading:** Shorts look like the long videos on this measure: about half of spoken quantities are on screen at the moment they are spoken (46% against 53%; n 35 and 70, so the gap is within noise) and a numeral or unit label is the commonest device. Fewer presenter and scale-reference people are drawn, but counts are tiny.

## 3. What is specific to the Shorts (OBSERVED, small n)

1. **The art is mostly the same art as the long video.** By eye, at least 15 of the 38 frames show the same drawing as a frame of the long counterpart that I viewed in Phase 7 or 7b: the 60-nanosecond shell, the 9.17 kW/m2 laser beside rain, the 31 August 2010 diver, the Gale crater column, the weight-maximum diagram, the freezer of humans, the millions-of-degrees annotation, the 1000 km/h globe, the 7 km/s arrow, the 4 G track, the Niagara blackboard, the car and ice slab, the minus-N-metre drain map, the wise-men globe. This fits the script finding (38 of 40 Shorts are cuts of long scripts) and means **Short frames are not independent of the long-video frames**: pooling "125 frames" double-counts about 15 pieces of artwork. Not checked systematically.
2. **Recomposed for portrait, not cropped.** The landscape art is re-laid out vertically: the 4 G track drawn upright, a ruler running full height with a magnitude arrow, a presenter placed under a small board, art in a band with plain space above and below. (Frames show the art area often filling only part of the 9:16 frame.)
3. **Quantity labels carry over unchanged** (T=60 nanoseconds, LIMIT: 4 Gs, 7 km/s, ~100 population), including the **magnitude-ruler device with an arrow** used for two different earthquake sizes.
4. **The 10 NO frames** are again numbers the picture does not carry at that instant: lightning count, one metre, 10 times the distance, a spin duration, a passenger count, 0.5 percent, a 30 km circle, a hundred feet, 90 degrees, 15 or 20 hours.
5. **Question card shown** (the asker's text as a card) in at least 2 of 38 frames; a card text that contains the quantity counts as restated.
6. A depth label caught mid-change (-50 m on its way to -100 m) was coded UNCLEAR, a reminder that a still can land between two states of an animation.

## 4. Limits

- One coder; no second reviewer. Regex-selected quantity moments, one per Short, so the Short's mid-runtime only; stills only.
- Two ASR engines pooled (16 campaign, 22 whisper); not tested whether that matters.
- Frame and speech offsets uncertain; NO means "not on screen at that instant".
- 6 Shorts had no quantity hit; 2 Shorts have no media; the Short sample inherits the long-video families (see 3.1).
- **TARGETED_VISUAL, not DEEP_VISUAL.** No performance link. Nothing about voice or sync (listening blocked).

## 5. Use for an original channel (OWNER class)

If a long script is written with Short seams (playbook C), plan the **Short's quantity visuals as a vertical recomposition of the long's**, with the same numerals; do not assume the long frame fits a portrait frame. Re-run the storyboard checklist (07 section 5) per cut, and do not count a Short's frame as extra evidence of a separate style.
