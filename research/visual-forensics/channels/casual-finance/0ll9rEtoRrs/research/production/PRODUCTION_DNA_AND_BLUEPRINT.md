# Video 004 — Production DNA and Original Reconstruction Blueprint (PARTIAL)

Video `0ll9rEtoRrs` "The World's Safest Market Is Breaking", 1280×720, 24 fps, 24,298 frames (16.87 min).
Source SHA-256 `8fd0c2bfd7b89d46e49280b7329626b7656dca7f5f2fd98c8046998af0c95b73`. Identity `HIGH_CONFIDENCE_NEEDS_REVIEW`.

**Scope and status.** Built only from `integrated_v2/` (status `SECOND_PASS_INTEGRATED_STRUCTURE_ONLY_NOT_SEMANTICALLY_CERTIFIED`). This is NOT a CT_SCAN_COMPLETE package. Statistics: `dna_statistics.json`, `composition_family_specs.csv`.
Labels: MEASURED = computed from ledgers; OBSERVED = seen in frames/evidence; INFERRED = my reading; UNAVAILABLE = not done.

Known limits on every number below:
- 807 CONFIRMED candidates were not second-passed (first-pass only).
- 143 unowned intervals (3,012 frames, 12.4%) are classified but not absorbed into states; 13 of them end on a hard cut.
- Child states from splits inherit parent descriptions; `S0466P` description is pending.
- Audio not verified; no ASR/script alignment was run, so no claim map or narration timing exists.

## 1. Editing DNA (MEASURED)
| Metric | Value |
|---|---|
| States | 530 (31.4 per min); median 1.12 s, mean 1.67 s, p10 0.29 s, p90 3.79 s, max 13.12 s |
| Edit events (excl. not-a-change/codec) | 996 (59 per min); 853 inside states, 143 inside unowned gaps |
| Additive entry | 262 (26.3%) |
| Full replace (hard cut) | 247 (24.8%) |
| Highlight added | 118 (11.8%) |
| Draw-on / reveal | 93 (9.3%) |
| Text change + number/label change | 80 (8.0%) |
| Pan/scroll, object motion, character animation, zoom/scale, wipe/fade (+ renamed motion/transition) | 120 (12.0%) |
| Pose/expression/element swap | 46 |

INFERRED reading: the rhythm is "cut to a new drawn composition, then build it up piece by piece". A new composition roughly every 1.1 s with items popping in and highlights drawn on is the main attention device; true camera-style motion is the minority.

## 2. Visual DNA (MEASURED families, OBSERVED look)
Share of state frames by family: F5 screenshot+character 26.9%, F2 character+prop 16.4%, F4 full-bleed screenshot/document 14.9%, F3 object/icon cluster 12.7%, F1 character-only 11.5%, F6 chart 7.0%, F11 composite 5.4%, F9 full-bleed drawn scene 2.8%, F10 title/end card 1.1%, F8 dark-UI capture 0.6%, F7 text card 0.3%.
OBSERVED: white canvas; flat hand-drawn stick-figure presenters (black marker outline, skin-tone head), green country characters with faces, money-bag and bond-certificate doodles; red handwritten emphasis text; third-party charts, PDFs, web pages and film/TV clips placed as rectangles inside the drawn scene.
Colours/typeface were not sampled for this video: UNAVAILABLE (do not reuse Video 003 values).

## 3. Motion DNA
- MEASURED: unowned frames by class: motion within a composition 1,712; embedded video 658 (INFERRED label; includes screen-recorded PDF/browser scrolls); continuous animation 515; fade/transition 74; distinct composition 50; uncertain 3.
- OBSERVED: laptop scenes with scrolling PDF/web pages, red arrows travelling along charts, timelines growing right, objects entering one at a time.
- INFERRED: easing/curves not measured; none stated here.

## 4. Pacing and story
Pacing metrics are in section 1. Story/claim structure, hook, scorecard and script-to-visual alignment: UNAVAILABLE (no ASR alignment performed for this video).

## 5. Original reconstruction blueprint (do not copy; build new assets)
Goal: reproduce the *system*, with original art and original or licensed material.
1. **Canvas/layout system.** White 1280×720 (or 1920×1080) canvas, one drawn composition per beat. Build a small kit of original presenters (2–3 poses/expressions each) and original character/icon sets in a new hand-drawn style. Do not trace or reuse the source's characters, country mascots or doodles.
2. **Beat grammar.** For each narration sentence: cut to a clean composition, then add 2–5 elements at 0.3–1.5 s spacing, then one emphasis (underline/box/highlight or red handwritten number). Target median composition length about 1.1 s with a few 3–6 s holds for data or punchlines (matches measured median/p90).
3. **Data scenes.** Use your own charts built from cited public data, with the source named on screen. Zoom/pan into the chart region, then draw a highlight. Never paste another creator's screenshot.
4. **Embedded footage.** The source places third-party film/TV clips and website captures. Replace with original drawings, licensed stock, or short clips used with a documented fair-use or licence basis. Do not copy them.
5. **Motion kit.** Build once and reuse: pop-in (scale+fade, 4–6 frames at 24 fps), draw-on stroke, slide-in, scroll within a screen frame, arrow travel along a series, pose swap (1-frame hold).
6. **QA.** Check cut rate per minute against 31 ± 6 compositions; check no composition lacks a clear focal element; check every on-screen number has a source line; check licence record for every third-party asset.

## 6. Per-composition-family specs
Table with family, share, median duration and the most frequent entry events is in `composition_family_specs.csv`. Use each family as a template (layout, entry style, hold time) and fill it with new original assets. Child states from splits (`S0089.*`, `S0097.*`, `S0116.*`, `S0475.*`) and `S0466P` still need their own descriptive review before individual specs are written.

## 7. Not done / needed before this can be called complete
Shot count and ASR alignment; second pass of the 807 CONFIRMED candidates; absorbing or ruling on the 143 unowned intervals and 161 merge flags; colour/type sampling; human listening and AV sign-off; identity check against live YouTube metadata; claim map and scorecard.
