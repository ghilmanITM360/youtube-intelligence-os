# xkcd's What If? — model sheets v0.1 (P3, 2026-11-08, LOCAL ONLY)

Built from the 44-video library (24 long, 20 Shorts; 5,458 states; 2,755 clusters), the campaign ledgers (`videos/<id>/tables/state_ledger.csv`) and manual v0.7. Labels: **MEASURED** (pixels / ledger numbers, tool stated), **OBSERVED** (I opened the image), **ESTIMATED** (rough pixel rule, bounds given), **INFERRED** (my interpretation), **UNAVAILABLE**.
Images I opened for this sheet: the 10 `../review_sheets/xk_*.jpg`, plus `figure_measure_check.jpg` (32 opening frames with boxes), `title_end_cards.jpg` (12), `characters_modifier_kit.jpg` (24). Tile label = `video/state` → full-res file `<video>/states/<state>_f*.jpg`.
**Originality line:** this is the style SYSTEM to rebuild with ORIGINAL characters, logo, name and end card. The source channel's narrator template, mascot silhouette, book covers, credits, names and title lockup are structure references only, never assets to copy.
Overlap: 9 Shorts are re-layouts of library long videos (`../XKCD_COVERAGE_AUDIT.md` §2); they count as 9:16 layout evidence, not extra style evidence.

## 0. Two format families (MEASURED)
| | Long-form | Shorts |
|---|---|---|
| Resolution / fps | 1920x1080, 24 fps CFR (24/24) | 1080x1920, 24 fps CFR (20/20) |
| Duration in library | 162–407 s | 21–150 s |
| Opening | lecture frame + question card (see §2a), then cold-open gag, then full-frame title card (manual §3: 6–31 s) | no title card; subject/board directly, question card in ~half |
| Ending | full-frame red end card held ≈10 s (manual §6: 235–240 frames) | no end card observed |
| Layout | one 16:9 canvas | landscape panel in the upper half, narrator or empty space below (OBSERVED); map panels on a BLACK lower area with a WHITE-outline narrator; wide diagrams cropped and panned across, not redrawn |

## 1. Canvas, line, palette (MEASURED unless marked)
- Canvas: modal light pixel **#F9F9F9** (86.9% of light pixels, 200 canvas frames, every 8th pixel; `canvas_colour.csv`). Manual v0.7 measured #F7F7F7 on one source frame; the library JPEG re-encode gives #F9F9F9. Treat as off-white ≈ #F7–#F9, not pure white.
- Ink: near-black #0C0C0C plus a grey scale of flat fills: #C4C4C4 15.7%, #E4E4E4 15.2%, #ACACAC 10.4%, #646464 9.3%, #848484 8.8% of non-canvas pixels (`palette_canvas_frames_ink_and_accents.csv`, 300 frames). Greys are FLAT fills (globes, water, land, boards), not gradients (OBSERVED).
- Accent on the canvas (chromatic pixels only, `palette_canvas_frames_chromatic.csv`): reds/pinks dominate — #DC8C94 13%, #D45C6C 8.1%, #ECBCC4 7.4%, #E4A4AC 6.7%, #CC4454 5.1% (the pinks are anti-aliased edges of thin red strokes; INFERRED), yellow #FCFC0C 6% (sun discs), pale yellow #F4FCAC, beige #C4B4A4, pale blue #BCD4F4.
- Colour scenes (`palette_full_bleed_scenes_chromatic.csv`, 300 of 420): beige/khaki #C4B4A4 22.9% (planet/desert/Mars), map green #6CBC6C 13.6%, cream land #ECECB4 10.8%, grey-teal #8CACAC 7.4%, pale cyan shelf #BCECF4 4.6%, red #CC2C3C 4.4% (end card), browns #948474/#C4A484.
- Dark scenes (`palette_dark_scenes.csv`): #0C0C0C 48.8%, #1C1C1C 13.7%, #343434 13.4%, white line #FCFCFC 5.2%.
- Stroke: about **8 px at 1080 px frame height** for the long-form narrator (0.0074 of frame height; ESTIMATED, median horizontal run through the head outline, n=18 identical template frames); Shorts narrator about 7 px at 1920 height (0.0036; n=14). One uniform monoline weight, round caps, slight hand wobble (OBSERVED). Objects use the same weight plus finer hatching (OBSERVED).
- Sampling method: 5-bit/channel bins, bins merged within 36 RGB units, seeded random frames; JPEG re-encoded frames, not calibrated.

## 2. Character model sheet
**2a. The narrator template (MEASURED + OBSERVED, the biggest finding).** In 18 of 24 long videos the first frame contains a narrator figure with IDENTICAL pixel geometry (bbox 617 px tall in all 18; head-box width 231 px in 16, 232 in 1, 243 in JcXpCyPc2Xw where the paper is hatched; `figure_measure_samples.csv`; the other 6 long openings were not detected by the rule and were not checked) at the same place (lower-left), holding a sheet of paper, beside the same empty whiteboard (thin black frame, marker ledge bottom-right), under a grey rounded question box. So the lecture frame is a reused stamped layout, not redrawn per video. Shorts reuse one narrator drawing too (674 px tall in 6 Shorts at 1080x1920). Variants put modifiers on the same figure (headphones, sunglasses; `characters_modifier_kit.jpg` 5, 10, 11).
- Head: unfilled circle, no face (no eyes, no mouth) by default (OBSERVED in every sheet). Head diameter / full figure height ≈ **0.37** long template (ESTIMATED, single template measured 18x; true bound ±0.03 because the paper touches the head box), 0.29–0.37 for Shorts narrators (n=14, 3 distinct drawings).
- Body: single straight line torso, single-line arms and legs, no hands or feet, round line caps (OBSERVED). Proportion INFERRED from the measured template: head ≈ 3/8 of height, torso ≈ 1/4, legs ≈ 3/8.
- Identity by modifiers only (OBSERVED, `characters_modifier_kit.jpg` + review sheets): long ponytail / long hair (woman variant), dark bob hair, messy bun, frizzy hair when electrocuted (zigzag shock lines), black bowler/derby hat, hard hats, party hats, beanie, helmet, headphones, sunglasses, glasses, beard, medical cap, robes/crowns (manual), astronaut helmet. Held props: paper, pointer, phone, spray can, rifle, binoculars, drinks.
- Expression set: UNAVAILABLE as faces (no facial features). Emotion is carried by pose, speech text, symbols ("!", "?", sweat/shock lines, Z's) and situation (OBSERVED).
- Pose set seen (OBSERVED): standing neutral, holding paper (lecture), pointing / presenting to the board, hand-on-chin thinking, arms raised, walking, running, sitting at desk with computer and office chair (the "question asker"), falling, lying, climbing, crowd line-ups, tiny figures on globes for scale. Pose change = 1-frame swap (POSE_SWAP 86 events, median 1 frame; MEASURED), no in-between animation.
- Views: front and 3/4-side profiles of the same stick rig; true turnaround UNAVAILABLE (not needed for a stick rig, INFERRED).
- Speech: floating hand-lettered caps near the head, often no balloon, sometimes a short tail line; thought bubbles = scalloped cloud with a drawing inside (OBSERVED).
- Gag cast (OBSERVED, structure only): grim reaper (robe + scythe), dinosaurs, moles, animals drawn with more detail than people.

## 3. Environment sheet (OBSERVED unless marked)
- Default: no environment — off-white void with at most a thin ground line (most frames; `features` empty for 1,884 of 2,755 clusters = 68%, MEASURED by pixel rule).
- Recurring set pieces: wall whiteboard (thin black rectangle, small marker ledge bottom-right; holds the subject drawing, equations, lists, inserted photos); grey rounded question box; desk + office chair + computer; globe on stand; diary notebook (spiral, boxed weekday labels, lowercase script).
- Background families (cluster pixel rule, MEASURED counts): dark screens 450 clusters (16%), full-bleed non-white 420 (15%), strong colour fields 115 (4%). Visual families: (a) black space with white line art, grey flat Earth limb with white cloud blobs, starfields, soft radial white glows, red/cyan glows; (b) grey night scenes with vignette, black tree-line silhouettes, snow specks; (c) flat colour planet/dusk scenes with black ground silhouette and tiny figures (beige, blue→orange, purple→pink gradients); (d) colour maps (grey ocean, pale cyan shelf, cream land, green vegetation, dashed latitude lines, hand-lettered caps names, magenta city dots); (e) inverted white-on-black line drawings; (f) technical cross-sections with stipple soil and black-fill rock.
- Depth/layering: flat 2D; occlusion by drawing order only; no parallax observed in stills (INFERRED; camera moves are ledger-measured, see §6).
- Camera: locked by default; pans/slides 4% of long events, zooms 2% (MEASURED, §6); Shorts pan across wide diagrams.

## 4. Graphics and typography sheet (OBSERVED unless marked)
- Hand lettering: all-caps, monoline, slightly irregular, same weight as the line art; used for headings ("1) CAN IT LIFT ITS OWN WEIGHT?"), labels with leader lines, speech, numbers and equations. Nearest font match (INFERRED): a casual monoline hand-printed caps font; the open "Humor Sans"-type fonts imitate this exact hand, so for an original clone use a different rounded hand-print caps face (owner allowed a near font).
- Question card (long): light-grey (#E4E4E4-ish) rounded rectangle top-centre, small dark SERIF text starting "Q." with right-aligned "—Name" attribution. Nearest match INFERRED: a book serif (Georgia / PT Serif class). Shorts: same box but often larger left-aligned SANS-like text with a small dark rounded "Q" chip (SLd4hnmeW_g, verified on the full-scale overlay sheet; some Shorts keep the serif version).
- Footnotes / captions under inserts: tiny serif paragraph (OBSERVED).
- Banners: full-width black top band with white caps "T = 1 DAY" as a persistent timer (OBSERVED).
- Real-world inserts: heat-map image, scanned tables, Wikipedia page, YouTube-comment cards, quoted article text with red underlines — inside a thin black frame or on the whiteboard, with a small serif source line.
- Diagrams: labelled cutaways (submarine, Earth layers), charts with hand-lettered axis ends, flowcharts with outlined boxes, process chains of circled icons, comparison triptychs with black dividers, measurement rulers as persistent anchors.
- Red marker system: arrows, circles around words, strike-through + replacement, hatching scribbles, dashed limit lines, red result numbers ("~6.28"), red signal rings; red also as content for fire/heat/magma (manual v0.5).
- End card (long, OBSERVED `title_end_cards.jpg` 3/5/7/8): full-frame red, black silhouette mascot left, row of book covers centre, white credits column right, small ©year line. Title card: full-frame red series title with animated silhouette ≈2 s (manual §3; I did NOT open a title-card frame in this pass: UNVIEWED here).
- Typing/write-on: question text types on letter by letter in some videos (manual §3); headings and formulas write on (DRAW_ON_TYPE median 6 frames, MEASURED §6).

## 5. Rhythm (MEASURED from ledgers; `rhythm_by_video.csv`)
Event = ledger ACTIVITY row (a verified visual change), excluding NO_VISIBLE_CHANGE.
| Type (tertile within format) | Long-form videos | events/min | median gap between events | median hold |
|---|---|---|---|---|
| BUSY | BO8rOs05v48, 4ZVtHknKuvg, s3oLIDaElaE, 9VG0yqq_PHM, TFhrRrRdUbA, FYoHYq8VRt0, lLlwvmu1ZeA, JcXpCyPc2Xw | 23.4–30.7 | 1.37–1.92 s | 1.17–1.85 s |
| MID | 8 videos | 20.4–22.8 | 1.54–2.48 s | 1.29–2.33 s |
| CALM | 2LSyizrk8-0, -1-ldW4kpLM, YL2VNtus4xk, JqFSGkFPipM, WH4g1ptJ-70, UQgw50GQu1A, Z_xJ40QXu7Q, oTzW-mTQd5w | 14.6–20.2 | 2.46–2.92 s | 2.15–2.50 s |
- Shorts: BUSY 26.3–39.2 events/min (SLd4hnmeW_g, jVy3qd70AqU, 35KZm1yiyIE, wBLVmEZV2Oc, oLoxdLfB6Gs, _efsqO-4OoQ, Ny9m2l6h478), CALM 17.9–21.8 (d5TD3r1nLqM, mEUqVgGf4e0, XvvXDEtMfhw, i6e4NnFnQi0, Uj10jGq2O8o, kNry0bf7eC0, GgEGcxJRDik, sFTRRdHqZIQ).
- p10/p90 gaps: long 0.29–1.31 s / 3.7–6.6 s; Shorts 0.46–2.25 s / 2.9–6.9 s.
- Which videos are busy: 6 of 8 BUSY long videos are 2026 uploads; 6 of 8 CALM are 2023-2025 plus oTzW-mTQd5w (2026, continuous-journey type with the longest moves, activity share 0.29). MEASURED dates, INFERRED trend (manual v0.6 already warns the year rule failed held-out; treat as a tendency, not a rule).
- Narration (ASR_UNCERTIFIED, `narration_vs_rhythm.csv`): narration pace is nearly constant (194–235 ASR words/min long, 195–249 Shorts) and does NOT track visual density (r = 0.10 long, −0.37 Shorts). So busy vs calm is set by the visual plan, not by talking speed (INFERRED). 62% of long-form events start within 0.5 s of an ASR segment start (Shorts 46%); with ~1 segment per 2 s the chance level is roughly 50%, so this is weak evidence that changes land on phrase starts (INFERRED, audio unverified). Manual §7 has the reviewed cases where pops land on the named word.
- Both rhythm types should be cloned: BUSY = board-centred builds with many 1-frame pop-ons on one canvas; CALM = more hard cuts per step, longer holds, or long continuous moves (INFERRED from manual §4/§9b and the tables).

## 6. Entering-class mix (MEASURED counts; class = reviewer label mapped by `model_sheet_data.py`)
| Class | Long share | Shorts share | Duration median (p10–p90) frames at 24 fps |
|---|---|---|---|
| POP_ON | 37.9% | 36.4% | 1 (1–1) |
| CUT (scene swap, title/end card) | 22.6% | 23.8% | 1 (1–1) |
| DISSOLVE / FADE | 6.6% | 5.3% | 6 (6–8) |
| STATE_SWAP (damage, lighting, panel content) | 6.4% | 7.3% | 1 (1–3) |
| DRAW_ON stroke (lines, strikes, circles, underlines) | 6.4% | 7.9% | 4 (1–13) |
| DRAW_ON type (letter-by-letter text) | 4.9% | 2.6% | 6 (1–13) |
| PAN / SLIDE / SCROLL | 3.9% | 4.5% | 8 (1–17) |
| POSE_SWAP | 3.5% | 2.2% | 1 |
| ZOOM | 2.0% | 3.5% | 9 (1–16) |
| POP_OFF | 1.2% | 1.2% | 1 |
| TEXT_SWAP | 0.2% | 0.7% | 1 |
| OTHER (rare subtypes) | 4.4% | 4.5% | 1 (1–38) |
- Files: `entering_class_counts.csv`, `entering_class_durations.csv`. Easing / overshoot: UNAVAILABLE here (P4 measures a few windows).

## 7. Style bible, one page (rules that held in the frames I opened; counterexamples listed)
1. Off-white canvas (#F7–F9 grey-white) is the default; one black monoline ink weight. Counter: black space scenes, grey night scenes, flat colour fields and maps (≈1/3 of clusters).
2. People are faceless circle-head stick figures; identity only via hair/hats/props. Counter: none seen with faces; animals and objects are drawn in far more detail.
3. Objects, machines and maps carry the detail (hatching, parts, labels); people stay minimal.
4. Flat fills only, mostly greys; colour is used as content (fire, maps, sky, planets), not decoration. Counter: soft glows and gradients in space/night/dusk scenes, one shaded grid globe.
5. Red is the only annotation colour: arrows, circles, strikes, results. Counter: some videos use no red at all (manual).
6. Text is hand-lettered caps on the drawing; only the question card, footnotes and inserts use a serif (Shorts card may be sans).
7. Long-form wraps the content: fixed lecture-frame opening with question card → cold-open gag → red title card → step canvases → red end card held ≈10 s. Shorts drop title and end cards.
8. Change is mostly 1-frame: pop-ons and cuts are ~60% of events; multi-frame moves are short (dissolve 6 f, write-on 4–6 f, slide 8 f, zoom 9 f).
9. A new event every ~1.4–2.9 s (median), busy builds on one board or calm step-by-step cuts; a persistent anchor (ruler, timer banner, map band) often carries a quantity across cuts.
10. Shorts re-use long-form drawings: landscape panel in the upper part of 9:16, narrator below or white-on-black, wide diagrams panned across.

## Not done / limits
- Figure geometry rests on one long template and three Shorts narrators (pixel-identical repeats), not on posed figures inside scenes.
- Title-card frame not opened; fonts not identified (nearest classes only); colours from JPEG copies.
- Rhythm classes are tertiles of this sample, not channel norms; 9 Shorts overlap their long parents.
