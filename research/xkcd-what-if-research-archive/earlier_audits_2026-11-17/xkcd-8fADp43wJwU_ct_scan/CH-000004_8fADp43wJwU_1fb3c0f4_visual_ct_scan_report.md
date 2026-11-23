# Visual CT-Scan Report - xkcd's What If? "If all humans died, when would the last light go out?"

- Video ID: 8fADp43wJwU (CH-000004) | Duration 303.856 s | 1920x1080 @24 fps | H.264 + AAC
- Source: /Users/ghilmanislam360/GhilmanProjects/video data of what if/videos/YTDown.com_YouTube_If-all-humans-died-when-would-the-last-l_Media_8fADp43wJwU_001_1080p.mp4
- SHA-256: 1fb3c0f4f510fe724749105425e31c8d7f5e9a6053d41e8b67e21f6a2c0a11d9
- Mode: DEEP (as requested: full video). Status: **VISUAL_ANALYSIS_PARTIAL** (see Coverage). Audio: **not listened**; **no AV sign-off**.
- Date: 2026-11-17. Repository untouched; all outputs are in this external folder.

## 0. Coverage and method (read first)

- **MEASURED:** per-frame difference signal across all 7,290 frames; 26 hard cuts at native-frame precision (difference spike >= 40). 4 weaker boundaries (white-to-white / dark-to-dark) found as spikes of 12-20 and confirmed by sheet change only. Total 31 shots.
- **OBSERVED:** all 304 one-second samples reviewed on 16 contact sheets; 14 native frames at 4 fps (2.5-6.0 s) and 3 full frames at 1280 px.
- **ESTIMATED:** every intra-shot event time (+/-1 s). The 1fps sheet label k is actually ~k+0.46 s (verified against the 258.458 s cut), already corrected in the ledgers.
- **UNAVAILABLE / not done:** human listening, ASR, timed transcript, native review of most state changes, retention/CTR data, camera-motion verification.
- **Prior run (2026-09-16, `video_forensics_output/if_all_humans_died`)**: 29 shots / 48 states from 2 s sampling. Treated as HISTORICAL_UNVERIFIED; not promoted. This run finds 31 shots; difference = weak boundaries and 2 extra short cards.
- **Prompt scope vs evidence:** your master prompt has 23 sections per visual plus synthesis. All 23 are produced per shot (31 shots, the meaningful distinct visuals); sub-states inside a shot are in the event ledger (49 events).
- Figures such as retention, CTR or exact easing are not claimed anywhere.

## 1. Literal visual summary (one sentence)
A black-line stick-figure presenter and chalkboard dissolve into red specks, then a series of hand-drawn silhouette plants and diagrams lose their lights one source at a time, ending on a pure black frame of glowing cyan waste blocks and a red end card with a books CTA.

## 2. Script architecture (transcript, positional)
- **Hook:** the viewer-submitted question card (S01) - states the title promise within 8 s; lamp dims at its end.
- **Open loop:** "when would the last artificial light go out?" stays open through the whole sequence of source types.
- **Structure ("elimination ranking"):** grid -> fossil -> nuclear (fuel-rich but auto-shutdown) -> off-grid generators (diesel < 6 months) -> geothermal (< 3 years) -> wind (11 / 3 / > 20 years) -> hydro (~4 years) -> batteries (decades) -> solar (~100 years) -> twist: radioactive glow (centuries).
- **Mini-payoffs:** time labels (S11, S14, S16, S17, S24). **Reversal:** "another contender, and it's a weird one" (S26). **Ultimate payoff:** S30 + final spoken answer. **CTA:** end card only (S31).
- **Alignment with packaging:** title promise ("last light") is answered literally at S30; the thumbnail was not available in this evidence (Not available from supplied evidence).

## 3. Shot timeline (compact)

| Shot | Time (s) | What |
|---|---|---|
| S01 | 0.00-8.67 | Question card + presenter at chalkboard |
| S02 | 8.67-10.67 | Series title card |
| S03 | 10.67-15.75 | City skyline blackout |
| S04 | 15.75-20.67 | Apartment cutaway with lava lamp |
| S05 | 20.67-30.79 | Coal power plant silhouette |
| S06 | 30.79-40.92 | Control room: grid cascade failure |
| S07 | 40.92-49.62 | Nuclear plant, reactor core glowing |
| S08 | 49.62-56.79 | Fuel energy content chart (scroll) |
| S09 | 56.79-72.88 | Reactor auto-shutdown, MAYDAY |
| S10 | 72.88-78.88 | Four-panel off-grid sources darken |
| S11 | 78.88-87.75 | Island hut + diesel generator, '< 6 MONTHS' |
| S12 | 87.75-92.17 | Five source icons on white |
| S13 | 92.17-99.29 | Geothermal plant silhouette + 'SVARTSENGI ISLAND GEOTHERMAL PLANT' |
| S14 | 99.29-110.08 | Maintenance worker with bucket, '< 3 YEARS' |
| S15 | 110.08-118.33 | Wind farm silhouettes + 'Tom Scott' inset |
| S16 | 118.33-138.67 | Turbine lifespan comparison: Gedser 11 / 3 / >20 YEARS |
| S17 | 138.67-158.08 | Dam: 'I DON'T ACTUALLY DO ANYTHING HERE' -> 'OOPS!' -> '~4 YEARS' |
| S18 | 158.08-162.12 | 'Eternal LIGHT - Requires ∞ AA batteries' product box |
| S19 | 162.12-165.71 | Drawer of batteries discharging |
| S20 | 165.71-172.12 | Six battery types draining (red fill -> empty) |
| S21 | 172.12-180.00 | Solar buildings/weather station/perimeter camera build-up |
| S22 | 180.00-191.21 | Roadside call box + billboard 'RHODE ISLAND POPULATION: EVERYONE 0' |
| S23 | 191.21-200.21 | Solar panel close-up accumulating grime |
| S24 | 200.21-209.67 | 'SPACE SUBMARINES IN CINEMAS!' billboard, '~100 YEARS', rain |
| S25 | 209.67-220.67 | Five-lane columns darken to leave solar lit |
| S26 | 220.67-227.92 | Barrel glow -> dim; warning signs |
| S27 | 227.92-246.71 | Glow-in-the-dark watch dial; face goes black |
| S28 | 246.71-258.46 | Cherenkov radiation diagram -> glowing cesium capsule in water |
| S29 | 258.46-285.17 | 'CESIUM 137' label -> glowing capsule + decay graph |
| S30 | 285.17-293.79 | Stacked glowing cyan blocks on black (answer) |
| S31 | 293.79-303.86 | End card with book CTA and credits |

## Part A - Per-shot forensic records (23 sections each)

### S01 - Question card + presenter at chalkboard  (0.000 -> 8.667 s, 8.7 s)

1. **[VISUAL ID]** S01
2. **[TIMESTAMP]** 0.000-8.667 s (start frame 0); boundary: video start / cut f208. Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'This question comes from Alan, who asks: If every human somehow simply disappeared from the face of the earth, how long would it be before the last artificial light source would go out?' (positional; transcript has no timestamps)
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Top-center rounded light-grey card with serif text 'Q. If every human somehow simply disappeared from the face of the earth, how long would it be before the last artificial light source would go out?' and '- Alan' below. Lower-left: large black stick figure (empty round head, thin limbs) holds a sheet of paper at chest height, other hand on hip. Lower-right: dark-grey chalkboard with white frame and chalk ledge; inside it a smaller stick figure with half-lit (white crescent) head beside a lit floor lamp with a bright radial glow cone. Off-white background.
5. **[CHANGE FROM PREVIOUS VISUAL]** First shot. DENSE (4 fps, 2.5-6.0 s): both figures turn black->red at ~2.75 s; presenter then dissolves into red particles (left of head/body) from ~3.5 s while the paper tilts, turns grey and drops with small motion marks (~3.75-4.25 s); inner figure turns red and thins. Lamp stays lit until ~6 s, then board and lamp dim to near black by ~8 s (1fps, ESTIMATED).
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) question card (top, high-contrast text); 2) presenter figure (large, left, recolors red = only chromatic change); 3) lamp glow (brightest area).
8. **[COMPOSITION ANALYSIS]** Two-column: text card on top, presenter left third, board right two-thirds. Locked frame (no camera move observed at 1fps/4fps). Negative space right of card. Eye flow: card -> presenter -> board -> lamp.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) question card (top, high-contrast text) | see anim/events | see facts | see composition | n/a | Very High |
| 2) presenter figure (large, left, recolors red = only chromatic change) | see anim/events | see facts | see composition | n/a | High |
| 3) lamp glow (brightest area). | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Hook confirmation + open loop: states the title question in the viewer's own terms and, within 3 s, shows 'people vanish' via red dissolve. Curiosity: will the lamp go out? Lamp dims at the end of the shot (micro-payoff + new question).
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn webcomic frame, 16:9, off-white background. Top center: a rounded light-grey caption card containing the text exactly: 'Q. If every human somehow simply disappeared from the face of the earth, how long would it be before the last artificial light source would go out?' with '- Alan' smaller beneath. Lower left: a tall thin-line stick figure (large empty circle head, no facial features) facing right, holding a sheet of paper at chest height, other hand on hip. Lower right: a dark-grey chalkboard with white frame and a thin chalk ledge containing a smaller stick figure with a white crescent on its head and a lit floor lamp with a soft white radial glow. Preserve framing, placement and empty space. Do not add people, props, text or decoration not listed. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no extra characters, no facial features on stick figures, no photorealism, no 3D, no shading beyond the lamp glow, no extra text, no logo, no colored background
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: black linework figures, lamp lit. Order: (1) both figures recolor to red; (2) presenter's outline breaks into red speckles drifting left while the paper tilts and falls with short motion marks; (3) inner figure thins/fades; (4) chalkboard and lamp dim to near black. Camera locked; card static throughout. End: red particle outline, dark board. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Locked frame. Black stick figures turn red; presenter dissolves into drifting red specks as the paper drops; then the chalkboard and lamp fade to near black. Card stays static.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Vector/raster hand-drawn layers (card, presenter, board, lamp glow) with a recolor effect then a particle/dissolve effect; paper is a separate falling layer. Software/method UNKNOWN.
18. **[EDIT RECONSTRUCTION]** 1) Hold static scene ~2.7 s. 2) Recolor both figures red. 3) Apply speckle dissolve to presenter ~1.5 s. 4) Fade board/lamp over ~2 s. 5) Hard cut to red title card.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Hook confirmation + open loop: states the title question in the viewer's own terms and, within 3 s, shows 'people vanish' via red dissolve. Curiosity: will the lamp go out? Lamp dims at the end of the shot (micro-payoff + new question). Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Introduces: red=person-removed mechanic, lamp=light state. Reused: S03-S14 and others.
21. **[LIKELY CREATOR INTENT]** HIGH: establish the premise visually. MEDIUM: use red as the 'person removed' signal for the whole video. ALT: red is only a brand accent.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Pose High; Environment High; Camera Medium (locked at 1-4fps); Motion High (dense); Text High
23. **[EDITOR IMPROVEMENT]** Works: card + instant dissolve. Friction: ~3 s of static before any change. Minimal fix: recolor 1 s earlier.


### S02 - Series title card  (8.667 -> 10.667 s, 2.0 s)

1. **[VISUAL ID]** S02
2. **[TIMESTAMP]** 8.667-10.667 s (start frame 208); boundary: hard cut f208->f256 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** No narration identified for this card (UNAVAILABLE without audio review).
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Full-frame solid red. Black silhouette of a satellite/space-telescope shape with a dinosaur-like silhouette biting it (top-center/left); white text 'xkcd's' (small), 'what if?' (large lowercase sans), 'THE VIDEO SERIES' (small caps). Two 1fps samples show the logo group at different size/position (smaller and right at ~9.5 s, larger and left-low at ~10.5 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut from dark chalkboard to saturated red; background changes from off-white/dark grey to red; logo group changes scale/position within the shot (direction UNVERIFIED, would need dense review).
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) 'what if?' wordmark (white on red, largest); 2) black silhouette; 3) 'THE VIDEO SERIES'.
8. **[COMPOSITION ANALYSIS]** Centered stack; silhouette above wordmark; flat colour field. Symmetric-ish, strong negative space.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) 'what if?' wordmark (white on red, largest) | see anim/events | see facts | see composition | n/a | Very High |
| 2) black silhouette | see anim/events | see facts | see composition | n/a | High |
| 3) 'THE VIDEO SERIES'. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Brand reset / pattern interrupt: color jump red after the dimming scene; reintroduces the series identity.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 16:9 title card, solid saturated red background. Upper center: a black silhouette of a satellite with a dinosaur-like creature biting it. Below, white text 'xkcd's' small, 'what if?' large lowercase geometric sans, 'THE VIDEO SERIES' small uppercase. Centered stack, generous empty space. Do not add extra icons or text. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no gradients, no 3D, no extra text, no photoreal textures
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: logo stack smaller, offset right. Motion (direction UNVERIFIED): stack scales up and drifts toward lower-left over the ~2 s. Hold at end, then hard cut. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Flat red title card; the logo stack slowly scales up and shifts while holding.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Flat vector logo animation (scale/translate); implementation UNKNOWN.
18. **[EDIT RECONSTRUCTION]** Hard cut in from S01; ~2 s hold with slow scale; hard cut out.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Brand reset / pattern interrupt: color jump red after the dimming scene; reintroduces the series identity. Content-vs-decoration: Decorative (brand).
20. **[VISUAL EVOLUTION / CALLBACK]** Bookended by S31 (same red field + silhouette).
21. **[LIKELY CREATOR INTENT]** HIGH: series branding. LOW: any other purpose.
22. **[RECONSTRUCTION CONFIDENCE]** Subject Medium; Pose n/a; Environment High; Camera Low; Motion Low; Text High
23. **[EDITOR IMPROVEMENT]** Works as brand sting. No change.


### S03 - City skyline blackout  (10.667 -> 15.750 s, 5.1 s)

1. **[VISUAL ID]** S03
2. **[TIMESTAMP]** 10.667-15.750 s (start frame 256); boundary: hard cut f256->f378 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'We'll start with the obvious: most lights wouldn't last long, because the major power grids would go down relatively quickly.' (positional)
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Black/dark-grey night skyline silhouette on left half; a building with grid of lit white windows; right half empty black. A short step (3 frames, ~13.2 s, detector ~8) extinguishes windows; skyline then holds dark with faint stars/dots.
5. **[CHANGE FROM PREVIOUS VISUAL]** From red card to black night scene; windows lit then dark.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) lit windows (brightest, highest contrast); 2) empty right black area (draws expectation of new element); 3) skyline edge.
8. **[COMPOSITION ANALYSIS]** Left-weighted; right half empty (reserved for the next shot's inset). Static.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) lit windows (brightest, highest contrast) | see anim/events | see facts | see composition | n/a | Very High |
| 2) empty right black area (draws expectation of new element) | see anim/events | see facts | see composition | n/a | High |
| 3) skyline edge. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Escalation of premise: 'lights go out' shown literally; sets the black visual language; right void sets up S04.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn night skyline, 16:9. Left half: dark-grey building silhouettes against black sky with a few faint stars; one building has a grid of lit white rectangular windows. Right half pure empty black. Preserve the empty right half. No people, no text. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no moon, no clouds, no people, no text, no photorealistic lighting
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: windows lit. Windows switch off together in a ~3-frame step at about 2.5 s into the shot; hold dark skyline. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Locked night skyline; lit windows all snap off, leaving a dark silhouette.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Static silhouette layer + window layer toggled off.
18. **[EDIT RECONSTRUCTION]** Cut in; hold ~2.5 s; window layer off (hard toggle); hold; cut/transition to S04 with new panel on the right.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Escalation of premise: 'lights go out' shown literally; sets the black visual language; right void sets up S04. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Leaves right half empty -> filled by S04 inset.
21. **[LIKELY CREATOR INTENT]** HIGH: visualise blackout. MEDIUM: leave right half empty for the next inset.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text n/a
23. **[EDITOR IMPROVEMENT]** Works.


### S04 - Apartment cutaway with lava lamp  (15.750 -> 20.667 s, 4.9 s)

1. **[VISUAL ID]** S04
2. **[TIMESTAMP]** 15.750-20.667 s (start frame 378); boundary: hard cut f378->f496 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Without people, there would be less demand for power, but our fridges and air conditioners and lava lamps would still be running.' (positional)
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Same dark skyline on left; right-hand framed room cutaway (light grey interior): ceiling lamp, wall AC unit with wavy airflow lines, TV, armchair with a lava lamp on bedside table, fridge with notes/magnets at right edge. A small red stick figure stands near the chair at ~16.5 s and dissolves to nothing by ~18 s; room stays lit through the end.
5. **[CHANGE FROM PREVIOUS VISUAL]** Right panel appears (inset reveal) over the skyline; red figure present then dissolved.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) lit room (bright, right); 2) red figure (only colour); 3) lava lamp / AC lines.
8. **[COMPOSITION ANALYSIS]** Split: dark city left, bright room right (frame-within-frame). Lit/dark contrast.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) lit room (bright, right) | see anim/events | see facts | see composition | n/a | Very High |
| 2) red figure (only colour) | see anim/events | see facts | see composition | n/a | High |
| 3) lava lamp / AC lines. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Proof by example + humor ('lava lamps'): concrete objects still using power while the human is removed.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn illustration, 16:9: left half dark-grey night skyline silhouette; right half a white-framed room cutaway in light grey: ceiling lamp lit, wall AC with wavy airflow lines, TV, armchair, bedside table with a lava lamp, fridge with notes at the right edge; soft white glow from the ceiling lamp. Black outer background. No people. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no people (red figure is a separate animated layer), no extra furniture, no photoreal shading
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: room panel visible. A small red stick figure stands by the armchair, then dissolves into red specks and disappears over ~1.5 s. Lamp/AC lines hold. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Locked cutaway room; a small red stick figure beside the armchair dissolves away while the lamp stays lit.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Inset panel layer; reuse of the same red-dissolve effect as S01.
18. **[EDIT RECONSTRUCTION]** Cut from dark skyline; panel appears at right; red figure dissolve; hold; hard cut to coal plant.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Proof by example + humor ('lava lamps'): concrete objects still using power while the human is removed. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Reuses S01 red-dissolve mechanic; objects named in narration.
21. **[LIKELY CREATOR INTENT]** HIGH: show appliances left running. ALT: purely illustrative.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text n/a
23. **[EDITOR IMPROVEMENT]** Works; objects named in narration appear.


### S05 - Coal power plant silhouette  (20.667 -> 30.792 s, 10.1 s)

1. **[VISUAL ID]** S05
2. **[TIMESTAMP]** 20.667-30.792 s (start frame 496); boundary: hard cut f496->f739 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Fossil fuel plants, which supply the vast majority of the world's electricity, require a steady supply of fuel, and their supply chains do involve people doing things.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Off-white sky; solid near-black silhouette of a plant with tall stack and line-drawn smoke, conveyor tower left, transmission pylon right. A dump truck and coal pile appear at left (~24 s). Several small red stick workers appear along the conveyor/plant (~26.5 s), dissolve (~28.5-30 s); smoke line-art fades; final frame shows plant with truck, no workers, no smoke.
5. **[CHANGE FROM PREVIOUS VISUAL]** Switch to light background; new object (truck/pile); then red workers added and removed; smoke disappears.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) black plant mass; 2) red workers (small, colour pop); 3) truck/smoke.
8. **[COMPOSITION ANALYSIS]** Horizontal silhouette band at bottom; sky empty top; pylon right.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) black plant mass | see anim/events | see facts | see composition | n/a | Very High |
| 2) red workers (small, colour pop) | see anim/events | see facts | see composition | n/a | High |
| 3) truck/smoke. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Explanation: fuel supply chain needs people; red = people; their disappearance halts the plant (smoke ends).
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn industrial silhouette on off-white background, 16:9: near-black coal power plant with tall chimney, boxy halls, conveyor tower at left feeding a coal pile and a dump truck, line-drawn smoke curling above, transmission pylon at right, solid black ground strip. Optional separate layer: 5 tiny red stick workers along the conveyor and plant. Preserve scale and placement. No text. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no outlines inside silhouettes, no realistic shading, no extra buildings, no text
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: plant with smoke. Truck + pile appear at left. Red workers appear, then each dissolves into red specks; smoke line fades out and plant is left idle. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Locked silhouette plant; truck arrives, tiny red workers appear then dissolve, and the smoke fades away.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Silhouette plate + overlay layers (truck, workers, smoke) toggled/dissolved.
18. **[EDIT RECONSTRUCTION]** Hard cut from room; stagger layer entries; dissolve workers; hold idle plant; hard cut to control room.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Explanation: fuel supply chain needs people; red = people; their disappearance halts the plant (smoke ends). Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Plate family 'black silhouette on off-white' (S05, S07, S09, S13, S15, S17).
21. **[LIKELY CREATOR INTENT]** HIGH: visualise 'supply chains need people'. MEDIUM: red-for-humans system.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text n/a
23. **[EDITOR IMPROVEMENT]** Works. Small red workers could be slightly larger on mobile.


### S06 - Control room: grid cascade failure  (30.792 -> 40.917 s, 10.1 s)

1. **[VISUAL ID]** S06
2. **[TIMESTAMP]** 30.792-40.917 s (start frame 739); boundary: hard cut f739->f982 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'As coal and oil plants started shutting down in the first few hours, other power sources would get hit with the extra load... a rapid series of cascading failures, leading to a blackout of all major power grids.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) White background. Large wall map screen showing grid icons (nuclear, plant, city, solar, wind, pylons) with a few warning triangles; two seated operators (stick figures with hair) at consoles below; one standing stick figure left says 'UH OH...' (~35 s). Then all three figures turn red and dissolve (~36-38.5 s) while warning triangles multiply on the map; a ~6-frame full-frame darken step (~38.6-38.8 s, detector ~30) turns the scene dark grey.
5. **[CHANGE FROM PREVIOUS VISUAL]** New interior scene; speech bubble appears; figures recolor/dissolve; warnings added; global darken.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) map warning triangles (black on grey); 2) 'UH OH...' text; 3) red figures.
8. **[COMPOSITION ANALYSIS]** Frame-within-frame screen top-center; people bottom; left figure separated.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) map warning triangles (black on grey) | see anim/events | see facts | see composition | n/a | Very High |
| 2) 'UH OH...' text | see anim/events | see facts | see composition | n/a | High |
| 3) red figures. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Escalation + payoff beat: cascading failure literal on a map; humor in 'UH OH...'.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn control room, 16:9, off-white background: large framed wall screen (center-top) showing a grey schematic grid map with small icons (nuclear symbol, factory, city blocks, solar panel, wind turbine, pylons) and a few black warning triangles. Below: two seated stick figures at consoles in chairs, one with a hair bun. To the left a standing stick figure. Preserve layout. Speech bubble text optional layer: 'UH OH...'. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no extra people, no real UI screenshots, no color except the optional red layer, no 3D
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: static room. Speech bubble 'UH OH...' appears. All three figures turn red and dissolve into specks while warning triangles pop onto the map one by one; the whole frame then darkens to dark grey in a quick step. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Locked control room: 'UH OH...' appears, three figures turn red and dissolve while warning triangles multiply, then the frame darkens.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Screen/map layer with triangle overlays; figure layers; global exposure/overlay step.
18. **[EDIT RECONSTRUCTION]** Hard cut in; hold; add bubble; red dissolve; add triangles; darken step; hard cut to nuclear plant.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Escalation + payoff beat: cascading failure literal on a map; humor in 'UH OH...'. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Red-dissolve + global darken step (also E012).
21. **[LIKELY CREATOR INTENT]** HIGH: show cascading failure. ALT: joke-driven gag only.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text High (UH OH...)
23. **[EDITOR IMPROVEMENT]** Works; clear cause->effect.


### S07 - Nuclear plant, reactor core glowing  (40.917 -> 49.625 s, 8.7 s)

1. **[VISUAL ID]** S07
2. **[TIMESTAMP]** 40.917-49.625 s (start frame 982); boundary: hard cut f982->f1191 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Nuclear reactors, of course, don't require a steady supply of fuel: one reactor operator I talked to said that if their core settled into low-power mode, it could continue running almost indefinitely...'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Off-white sky; black silhouette: cooling tower (left), containment dome with glowing white reactor core graphic, turbine, pylon right. Three tiny red workers (one by cooling tower, two near turbine). From ~45 s the red workers dissolve to specks. The core keeps a bright white glow.
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to a nuclear-specific plant plate; same red-people mechanic as S05.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) glowing reactor core (brightest); 2) red workers; 3) cooling tower.
8. **[COMPOSITION ANALYSIS]** Silhouette horizontal band; core is the bright focal point left-center.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) glowing reactor core (brightest) | see anim/events | see facts | see composition | n/a | Very High |
| 2) red workers | see anim/events | see facts | see composition | n/a | High |
| 3) cooling tower. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Setup for contrast: nuclear is the exception (does not need constant fuel) - then S08 quantifies why.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn nuclear plant silhouette on off-white, 16:9: near-black cooling tower at left with line-drawn steam, containment dome with a white rectangular window containing a glowing reactor core graphic with radiation symbol and soft white glow, turbine, transmission pylon at right, black ground strip. Optional red stick workers (3). Preserve composition. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no outlines in silhouettes, no realistic steam, no extra buildings, no text
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: core glowing, steam drifting (subtle). Workers stand, then dissolve into red specks. Core glow stays constant. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Locked nuclear plant; red workers dissolve while the reactor core keeps glowing.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Same silhouette-plate system as S05 with a glow layer.
18. **[EDIT RECONSTRUCTION]** Hard cut in; hold; red dissolve; hard cut to chart.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Setup for contrast: nuclear is the exception (does not need constant fuel) - then S08 quantifies why. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Base plate reused in S09 (callback with glow off).
21. **[LIKELY CREATOR INTENT]** HIGH: contrast with fossil plants.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text n/a
23. **[EDITOR IMPROVEMENT]** Works.


### S08 - Fuel energy content chart (scroll)  (49.625 -> 56.792 s, 7.2 s)

1. **[VISUAL ID]** S08
2. **[TIMESTAMP]** 49.625-56.792 s (start frame 1191); boundary: hard cut f1191->f1363 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** '...a cube of uranium contains about six million times as much stored energy as a similar-sized cube of coal.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) White background. Left: a sheet 'FUEL ENERGY CONTENT IN MJ/KG' with bars labelled 19 SUGAR, 24 COAL, 39 FAT, 46 GASOLINE and a very tall black bar URANIUM that extends upward and winds as a long ribbon/scroll to the right where a tiny stick figure stands at the end. Around ~51 s a label '76,000,000' appears above the scroll's end.
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to a diagram; label added once.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) tall black uranium bar/ribbon; 2) chart numbers; 3) '76,000,000' label + tiny figure.
8. **[COMPOSITION ANALYSIS]** Diagonal/spiral ribbon leading eye to right, tiny figure as scale cue.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) tall black uranium bar/ribbon | see anim/events | see facts | see composition | n/a | Very High |
| 2) chart numbers | see anim/events | see facts | see composition | n/a | High |
| 3) '76,000,000' label + tiny figure. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Evidence/proof + humor of scale (ribbon gag). NOTE: spoken '~six million times' vs on-screen '76,000,000' (units/quantity differ?) - flagged; not resolved here.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn infographic gag, 16:9, white background: a paper sheet at left titled 'FUEL ENERGY CONTENT IN MJ/KG' with four short bars labelled 19 SUGAR, 24 COAL, 39 FAT, 46 GASOLINE and one extremely tall black bar labelled URANIUM that rises off the sheet and becomes a long looping ribbon curling right across the frame toward a tiny stick figure standing at its end; a small label '76,000,000' near the ribbon's end. Preserve proportions. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no 3D, no extra values, no extra icons, no colour
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: chart and ribbon static. '76,000,000' label pops in near ribbon end (~1.5 s in), then hold. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Static chart with an extremely tall uranium ribbon winding to a tiny figure; a '76,000,000' label pops in.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Single illustrated plate + one text layer.
18. **[EDIT RECONSTRUCTION]** Hard cut in; hold ~1 s; label in; hold ~5 s; hard cut to reactor.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Evidence/proof + humor of scale (ribbon gag). NOTE: spoken '~six million times' vs on-screen '76,000,000' (units/quantity differ?) - flagged; not resolved here. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Chart/scroll gag; single use.
21. **[LIKELY CREATOR INTENT]** HIGH: make scale comedic. ALT: numbers as authority.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Low; Text High (digits readable)
23. **[EDITOR IMPROVEMENT]** Static ~5 s hold: possible low-change zone - add a second beat.


### S09 - Reactor auto-shutdown, MAYDAY  (56.792 -> 72.875 s, 16.1 s)

1. **[VISUAL ID]** S09
2. **[TIMESTAMP]** 56.792-72.875 s (start frame 1363); boundary: hard cut f1363->f1749 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Unfortunately, although there's enough fuel, most nuclear reactors wouldn't keep running for long. As soon as something went wrong, the core would go into automatic shutdown...'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Same nuclear plate. Tiny extra elements appear on the dome/turbine edges (~62-63 s); the reactor core glow switches off (~67 s, core outline dims); small red lights appear around the plant (~68-70 s); a speech bubble 'MAYDAY!' emerges from the pylon (~71-72 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** Callback to S07 plate; core glow off; red alarm dots; speech bubble.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) core (glow vanishes); 2) red dots; 3) 'MAYDAY!' text.
8. **[COMPOSITION ANALYSIS]** Same as S07; speech bubble from right.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) core (glow vanishes) | see anim/events | see facts | see composition | n/a | Very High |
| 2) red dots | see anim/events | see facts | see composition | n/a | High |
| 3) 'MAYDAY!' text. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Reversal: payoff of the nuclear loop (it shuts down) via visual state change of the same object.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Reuse S07 plate (nuclear plant silhouette, off-white, 16:9) with the reactor core UNLIT: core window dim grey outline, no glow. Add small red alarm dots on the dome, tower and turbine, and a speech bubble from the pylon with text 'MAYDAY!'. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no glow on the core, no workers, no extra text, no new buildings
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: core lit. Core glow switches off; red alarm lights fade in around the plant; speech bubble 'MAYDAY!' pops from the pylon. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Same nuclear plate: the core glow goes out, red alarm lights appear and the pylon shouts 'MAYDAY!'.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Reuse of S07 plate with changed layers (glow off, alarm layer, bubble).
18. **[EDIT RECONSTRUCTION]** Hard cut in (callback); hold; glow off; alarms; bubble; hard cut to four-panel.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Reversal: payoff of the nuclear loop (it shuts down) via visual state change of the same object. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Callback to S07: same plate, changed state (reversal).
21. **[LIKELY CREATOR INTENT]** HIGH: payoff by state change on a reused plate (low production cost).
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text High
23. **[EDITOR IMPROVEMENT]** ~16 s on one plate: possible pacing risk; works because of staged changes.


### S10 - Four-panel off-grid sources darken  (72.875 -> 78.875 s, 6.0 s)

1. **[VISUAL ID]** S10
2. **[TIMESTAMP]** 72.875-78.875 s (start frame 1749); boundary: hard cut f1749->f1892 (boundary MEASURED, end inferred dark-to-dark). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'However, plenty of light comes from sources not tied to the major power grids. Let's take a look at a few of those, and when each one might turn off.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) 2x2 grid, light-grey panels, each with a ceiling bulb: hydro/pipe with turbine (top-left), diesel generator (top-right), house with solar panel (bottom-left), wind turbines (bottom-right). Bulbs light then switch off in steps (~76.0, 76.5, 77.0, 77.6 s; detector 12-23) leaving all dark.
5. **[CHANGE FROM PREVIOUS VISUAL]** New split-screen; bulbs extinguish stepwise.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) glowing bulbs; 2) generator drawing; 3) turbines.
8. **[COMPOSITION ANALYSIS]** 2x2 grid, equal weight, bulbs top of each cell.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) glowing bulbs | see anim/events | see facts | see composition | n/a | Very High |
| 2) generator drawing | see anim/events | see facts | see composition | n/a | High |
| 3) turbines. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Orientation/agenda: enumerates the off-grid source types that the video will rank.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn 2x2 grid, 16:9, light-grey cells: top-left hydro pipe feeding a turbine, top-right diesel generator with vibration marks, bottom-left house with solar panel roof, bottom-right two wind turbines; each cell has a hanging bulb with a soft white glow. Preserve cell layout. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no text, no people, no extra cells, no photoreal shading
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: all bulbs glowing. Bulbs turn off one at a time in quick steps with their cell darkening; end all dark. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Locked 2x2 grid of power sources; bulbs switch off one by one until all four are dark.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Four panel plates + per-cell glow toggles.
18. **[EDIT RECONSTRUCTION]** Hard cut; hold; stepwise glow-off at ~0.5 s intervals; hard cut to island.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Orientation/agenda: enumerates the off-grid source types that the video will rank. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Grid reappears conceptually as the five-lane lineup in S25.
21. **[LIKELY CREATOR INTENT]** HIGH: agenda before ranking.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text n/a
23. **[EDITOR IMPROVEMENT]** Works.


### S11 - Island hut + diesel generator, '< 6 MONTHS'  (78.875 -> 87.750 s, 8.9 s)

1. **[VISUAL ID]** S11
2. **[TIMESTAMP]** 78.875-87.750 s (start frame 1893); boundary: boundary ~78.875 (dark-to-dark, detector 19.9; ESTIMATED) / cut f2106 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Many remote communities, like those on far-flung islands, get their power from diesel generators. These can run until their tanks run out of fuel, which in most cases could be anywhere from days to months.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Dark-grey scene: small island hill, hut with lit doorway and window, diesel generator at left (vibration marks), palm tree silhouette, one stick figure sitting at right. Lights glow, then go out (~83 s); the figure turns red and dissolves (~83.5-85.5 s). White text '< 6 MONTHS' appears top-left (~86.5 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** New dark scene; glow off; figure dissolve; time label.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) lit doorway; 2) generator; 3) red figure; 4) '< 6 MONTHS'.
8. **[COMPOSITION ANALYSIS]** Horizon-line landscape, hut center, generator left, figure right.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) lit doorway | see anim/events | see facts | see composition | n/a | Very High |
| 2) generator | see anim/events | see facts | see composition | n/a | High |
| 3) red figure | see anim/events | see facts | see composition | n/a | Medium |
| 4) '< 6 MONTHS'. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Micro-payoff with a number: first time-to-failure estimate appears as a label.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn night island scene, 16:9, dark grey: low hill with ocean strip at bottom, small thatched hut with glowing doorway and window, a diesel generator with vibration marks to its left, a palm silhouette behind, one stick figure sitting at right. Optional text top-left: '< 6 MONTHS'. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no realistic water, no extra huts, no stars, no extra text
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: doorway and window glowing. Lights go out; figure turns red and dissolves; text '< 6 MONTHS' fades in top-left. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Locked night island: hut lights go out, the figure dissolves in red, and '< 6 MONTHS' appears.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Dark plate + glow toggles + dissolve + text layer.
18. **[EDIT RECONSTRUCTION]** Cut in; hold; glow off; red dissolve; label in; hard cut to icons.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Micro-payoff with a number: first time-to-failure estimate appears as a label. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Introduces white time-label (< 6 MONTHS) -> reused as <3 YEARS, 11/3/>20 YEARS, ~4 YEARS, ~100 YEARS.
21. **[LIKELY CREATOR INTENT]** HIGH: introduce the time-label system.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text High
23. **[EDITOR IMPROVEMENT]** Works.


### S12 - Five source icons on white  (87.750 -> 92.167 s, 4.4 s)

1. **[VISUAL ID]** S12
2. **[TIMESTAMP]** 87.750-92.167 s (start frame 2106); boundary: hard cut f2106 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Off-grid generating stations that don't need a human-provided fuel supply would be in better shape.' (positional)
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) White background: battery (left), two wind turbines, solar panel on pole (right), geothermal plant diagram (lower-left), hydro/pipe diagram (lower-right). Static through the shot.
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to bright white list of icons.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) wind turbines (center, tall); 2) solar; 3) battery.
8. **[COMPOSITION ANALYSIS]** Scatter/catalog layout on white.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) wind turbines (center, tall) | see anim/events | see facts | see composition | n/a | Very High |
| 2) solar | see anim/events | see facts | see composition | n/a | High |
| 3) battery. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Orientation: names the candidates the ranking will walk through.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D icon sheet, 16:9, white: left a battery outline; center two wind turbines; right a solar panel on a pole; lower-left a geothermal plant cutaway with turbine; lower-right a hydro pipe with turbine. Thin black linework only. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no color, no labels, no shading
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Fully static hold; no motion observed. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Static white icon sheet of five energy sources.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Single plate.
18. **[EDIT RECONSTRUCTION]** Hard cut in; short hold; hard cut out.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Orientation: names the candidates the ranking will walk through. Content-vs-decoration: Reinforcing.
20. **[VISUAL EVOLUTION / CALLBACK]** Icon sheet reappears as lanes in S25.
21. **[LIKELY CREATOR INTENT]** HIGH: agenda reminder.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium (no motion seen); Text n/a
23. **[EDITOR IMPROVEMENT]** Short and efficient.


### S13 - Geothermal plant silhouette + 'SVARTSENGI ISLAND GEOTHERMAL PLANT'  (92.167 -> 99.292 s, 7.1 s)

1. **[VISUAL ID]** S13
2. **[TIMESTAMP]** 92.167-99.292 s (start frame 2212); boundary: hard cut f2212 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Geothermal plants can run for a fair bit of time without human intervention. According to the maintenance schedule for the Svartsengi Island geothermal plant in Iceland...'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Black silhouette: steam stacks at left, dome with exposed turbine/pipe cutaway in white linework, pylon right; label 'SVARTSENGI ISLAND GEOTHERMAL PLANT' appears top-center (~96.5 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** Silhouette plate in same family as S05/S07; label appears.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) cutaway turbine (white on black); 2) label; 3) steam stacks.
8. **[COMPOSITION ANALYSIS]** Silhouette band; label top-center.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) cutaway turbine (white on black) | see anim/events | see facts | see composition | n/a | Very High |
| 2) label | see anim/events | see facts | see composition | n/a | High |
| 3) steam stacks. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Specificity/proof: named real plant adds credibility.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D silhouette on off-white, 16:9: black plant with tall steam stacks at left, a dome with a white line-art cutaway showing a turbine and pipes, pylon at right. Optional label top-center in hand-drawn caps: 'SVARTSENGI ISLAND GEOTHERMAL PLANT'. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no people, no extra text
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Static plate; label fades/pops in after ~4.5 s. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Static geothermal silhouette; a place-name label appears at the top.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Plate + label layer.
18. **[EDIT RECONSTRUCTION]** Hard cut; hold; label in; hold; hard cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Specificity/proof: named real plant adds credibility. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Silhouette family; label pattern.
21. **[LIKELY CREATOR INTENT]** HIGH: name-drop real facility.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Low; Text High
23. **[EDITOR IMPROVEMENT]** Works.


### S14 - Maintenance worker with bucket, '< 3 YEARS'  (99.292 -> 110.083 s, 10.8 s)

1. **[VISUAL ID]** S14
2. **[TIMESTAMP]** 99.292-110.083 s (start frame 2383); boundary: hard cut f2383 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** '...every six months the operators must change the gearbox oil and re-grease all electric motors and couplings. Without humans to perform these sorts of maintenance procedures, some plants might run for a few years, but they'd all succumb to corrosion eventually.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Grey pipe-room: horizontal pipes, a large motor/gearbox with a blinking beacon on top; stick figure with hard hat and a bucket says 'OH, HAS IT BEEN 6 MONTHS ALREADY?'. Beacon glow pulses (~101 s). Figure turns red and dissolves (~104-105 s). Label '< 3 YEARS' fades in at top-left (~106.5 s) while the scene darkens; black corrosion/stain marks spread over the machine (~108-109 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** New interior; speech; dissolve; time label; darken; decay texture.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) hard-hat figure + speech; 2) beacon; 3) corrosion marks (late).
8. **[COMPOSITION ANALYSIS]** Foreground figure right, machine center-left, pipes horizontal.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) hard-hat figure + speech | see anim/events | see facts | see composition | n/a | Very High |
| 2) beacon | see anim/events | see facts | see composition | n/a | High |
| 3) corrosion marks (late). | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Explanation with joke + time label; decay shown visually (corrosion).
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn grey industrial pipe room, 16:9: horizontal pipes, a motor/gearbox unit with a small beacon light on top, a stick figure in a hard hat holding a bucket at right, speech bubble text 'OH, HAS IT BEEN 6 MONTHS ALREADY?'. Mid-grey background. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no extra workers, no color except an optional red dissolve layer, no photoreal rust
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Beacon pulses; figure turns red and dissolves; scene darkens as '< 3 YEARS' appears and black corrosion spots spread across the machine. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Locked pipe room: the worker jokes, dissolves in red, and the machine darkens and corrodes under '< 3 YEARS'.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Plate + beacon loop + dissolve + progressive overlay for corrosion + text.
18. **[EDIT RECONSTRUCTION]** Hard cut; hold; beacon pulse; dissolve; darken + label; corrosion overlay; hard cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Explanation with joke + time label; decay shown visually (corrosion). Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Time-label + dissolve + decay overlay (reused in S17, S23).
21. **[LIKELY CREATOR INTENT]** HIGH: joke carries the maintenance fact.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text High
23. **[EDITOR IMPROVEMENT]** Works.


### S15 - Wind farm silhouettes + 'Tom Scott' inset  (110.083 -> 118.333 s, 8.2 s)

1. **[VISUAL ID]** S15
2. **[TIMESTAMP]** 110.083-118.333 s (start frame 2642); boundary: hard cut f2642 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Lights relying on wind power would last a bit longer. Wind turbines are designed so that they don't need constant maintenance, for the simple reason that there are a lot of them and they're a pain to climb.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Off-white sky; field of black turbine silhouettes at varied sizes on black ground. At ~116.5 s a framed video-card window appears upper-center: a stick figure in a hard hat climbing a turbine ladder, caption 'Tom Scott' with a verified check mark and avatar, with a speech-tail line toward the turbines.
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to wide silhouette field; inset card appears.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) tall left turbine; 2) inset card (new element); 3) distant turbines.
8. **[COMPOSITION ANALYSIS]** Rule-of-depth scale variation; inset overlays top.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) tall left turbine | see anim/events | see facts | see composition | n/a | Very High |
| 2) inset card (new element) | see anim/events | see facts | see composition | n/a | High |
| 3) distant turbines. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Humor/cameo: 'pain to climb' joke illustrated by a named creator's video-card (cultural reference). Whether this is a real creator reference is INFERRED from on-screen text.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn wind farm in black silhouette on off-white, 16:9: about 12 three-blade turbines at varied scale on a thick black ground strip. Optional overlay: a framed video-card top-center showing a stick figure in a hard hat climbing a ladder inside a turbine, with caption 'Tom Scott' and a verified check mark, and a curved tail line pointing to a turbine. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no realistic sky, no extra text, no real photos
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Static field; turbines may be still (no rotation seen). Inset card pops in at ~6.5 s and holds. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Static wind-farm silhouettes; a small video-card cameo pops in at the top.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Plate + inset layer.
18. **[EDIT RECONSTRUCTION]** Hard cut; hold ~6 s; card pop-in; hard cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Humor/cameo: 'pain to climb' joke illustrated by a named creator's video-card (cultural reference). Whether this is a real creator reference is INFERRED from on-screen text. Content-vs-decoration: Emotional/humor + reinforcing.
20. **[VISUAL EVOLUTION / CALLBACK]** Wind-farm silhouette -> S16 comparison.
21. **[LIKELY CREATOR INTENT]** HIGH: joke payload. MEDIUM: audience-targeted reference.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Low; Text High
23. **[EDITOR IMPROVEMENT]** Works; ~6 s static before the gag.


### S16 - Turbine lifespan comparison: Gedser 11 / 3 / >20 YEARS  (118.333 -> 138.667 s, 20.3 s)

1. **[VISUAL ID]** S16
2. **[TIMESTAMP]** 118.333-138.667 s (start frame 2840); boundary: hard cut f2840 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'The Gedser Wind Turbine in Denmark was installed in the late 1950s and it generated power for 11 years without maintenance. Modern turbines are typically rated to run for 3 years without servicing, and there are no doubt some which would run for decades...'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) White panels separated by vertical lines. Left: 'GEDSER WIND TURBINE, DENMARK' with the old tripod-braced turbine silhouette, then '11 YEARS' appears. A second panel slides in from the right with a modern turbine and '3 YEARS'; a third with a taller turbine and '>20 YEARS'; a framed nacelle cutaway (black, with a glowing dot) opens in the third panel, shifts to white line-art of gearbox/shaft, then darkens/corrodes (dark patches) near the end.
5. **[CHANGE FROM PREVIOUS VISUAL]** Panels added left to right; numeric labels; inset cutaway progression.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) newest panel/turbine; 2) year labels; 3) nacelle inset.
8. **[COMPOSITION ANALYSIS]** Three-column comparison; vertical dividers; label row top.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) newest panel/turbine | see anim/events | see facts | see composition | n/a | Very High |
| 2) year labels | see anim/events | see facts | see composition | n/a | High |
| 3) nacelle inset. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Proof via comparison and escalation: 11 -> 3 -> >20 years; decay shown inside the nacelle.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D three-column comparison, 16:9, white: column 1 an old tripod-braced turbine silhouette with caption 'GEDSER WIND TURBINE, DENMARK' and '11 YEARS'; column 2 a modern turbine silhouette with '3 YEARS'; column 3 a taller turbine silhouette with '>20 YEARS' and a framed nacelle cutaway showing a gearbox and shaft in white line art. Thin vertical dividers, black ground strip. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no extra columns, no color, no photoreal turbine, no extra labels
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: only column 1. Label '11 YEARS'; column 2 turbine slides/draws in; '3 YEARS'; column 3 appears; nacelle inset opens, cycles from dark to line-art, then corroded dark spots. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Three-column turbine comparison builds left to right with year labels, ending on a nacelle cutaway that corrodes.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Column plates added sequentially with sliding/reveal; inset sub-animation.
18. **[EDIT RECONSTRUCTION]** Hard cut; incremental layer adds timed to spoken numbers; hard cut to dam.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Proof via comparison and escalation: 11 -> 3 -> >20 years; decay shown inside the nacelle. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Column-build system reused in S21.
21. **[LIKELY CREATOR INTENT]** HIGH: stack comparison progressively to keep curiosity.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text High
23. **[EDITOR IMPROVEMENT]** ~20 s: well staged.


### S17 - Dam: 'I DON'T ACTUALLY DO ANYTHING HERE' -> 'OOPS!' -> '~4 YEARS'  (138.667 -> 158.083 s, 19.4 s)

1. **[VISUAL ID]** S17
2. **[TIMESTAMP]** 138.667-158.083 s (start frame 3328); boundary: hard cut f3328 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Generators that convert falling water into electricity will also keep working. An operator at the Hoover Dam once said that if everyone walked out, the facility would continue to run on autopilot for several years... the dam would probably succumb to clogged intakes or the same kind of mechanical failure...'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Cross-section: grey water on left with fish, black dam mass, penstock channel to a turbine housing, pylon right. Stick figure on top with speech '(I DON'T ACTUALLY DO ANYTHING HERE)', then red dissolve (~148 s); speech 'OOPS!' near the pylon; label '~4 YEARS' top-left (~151 s) while intake/turbine area shows dark clogging/rust (~152-156 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** New plate; speech; dissolve; speech 'OOPS!'; label; decay overlay.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) speech bubble; 2) red figure; 3) intake/turbine rust.
8. **[COMPOSITION ANALYSIS]** Diagonal dam slope leads from top-left to lower right.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) speech bubble | see anim/events | see facts | see composition | n/a | Very High |
| 2) red figure | see anim/events | see facts | see composition | n/a | High |
| 3) intake/turbine rust. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Humor + time label + decay payoff.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn hydroelectric dam cross-section, 16:9: grey water at left with two fish, thick black dam mass, a channel running down-right to a turbine housing, transmission pylon at right, off-white sky; a tiny stick figure sits atop the dam. Speech bubble text 'I DON'T ACTUALLY DO ANYTHING HERE'. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no realistic water, no extra people, no text beyond the bubble
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Static plate; speech appears; figure turns red and dissolves; 'OOPS!' appears and fades; '~4 YEARS' appears; dark clog marks spread over intake/turbine. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Locked dam cross-section: the lone operator jokes, dissolves in red, then the intake corrodes under '~4 YEARS'.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Plate + overlays.
18. **[EDIT RECONSTRUCTION]** Hard cut; hold; bubble; dissolve; second bubble; label; decay; hard cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Humor + time label + decay payoff. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Decay overlay system (rust) reused in S23.
21. **[LIKELY CREATOR INTENT]** HIGH: comic beat before the decay fact.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text High
23. **[EDITOR IMPROVEMENT]** Works.


### S18 - 'Eternal LIGHT - Requires ∞ AA batteries' product box  (158.083 -> 162.125 s, 4.0 s)

1. **[VISUAL ID]** S18
2. **[TIMESTAMP]** 158.083-162.125 s (start frame 3794); boundary: hard cut f3794 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Battery-powered lights wouldn't fare much better...' (positional)
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Grey background with a vignette glow behind a hand-drawn product-box illustration: bulb icon top-left, title 'Eternal LIGHT', 'Requires ∞ AA BATTERIES (NOT INCLUDED)', rows of battery icons. Card dims to dark over ~160-162 s.
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to gag product; dims.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) 'Eternal LIGHT' headline; 2) battery grid; 3) bulb.
8. **[COMPOSITION ANALYSIS]** Centered box with radial glow.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) 'Eternal LIGHT' headline | see anim/events | see facts | see composition | n/a | Very High |
| 2) battery grid | see anim/events | see facts | see composition | n/a | High |
| 3) bulb. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Humor + setup for the battery segment.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn product package on mid-grey with a soft radial glow, 16:9: bulb icon top-left; title 'Eternal LIGHT' in italic hand lettering; line 'Requires ∞ AA BATTERIES (NOT INCLUDED)'; below it rows of battery outlines in black/white. Centered. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no real brand, no photo, no extra text
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Static; card dims to near black. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Eternal-light box card on grey that dims to dark.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Prop plate + dim.
18. **[EDIT RECONSTRUCTION]** Hard cut; brief hold; dim; hard cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Humor + setup for the battery segment. Content-vs-decoration: Emotional/humor.
20. **[VISUAL EVOLUTION / CALLBACK]** Prop gag; single use.
21. **[LIKELY CREATOR INTENT]** HIGH: gag.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Low; Text Medium
23. **[EDITOR IMPROVEMENT]** Fine.


### S19 - Drawer of batteries discharging  (162.125 -> 165.708 s, 3.6 s)

1. **[VISUAL ID]** S19
2. **[TIMESTAMP]** 162.125-165.708 s (start frame 3891); boundary: hard cut f3891 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Even without anything using their power, batteries eventually self-discharge.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Top-down open drawer, white interior, grey surround; two red batteries, a pen and small dice. Batteries shift slightly and then turn white (~165 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut; batteries rotate; recolor red->white.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) red batteries; 2) pen/dice.
8. **[COMPOSITION ANALYSIS]** Framed drawer, two batteries center.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) red batteries | see anim/events | see facts | see composition | n/a | Very High |
| 2) pen/dice. | see anim/events | see facts | see composition | n/a | High |

10. **[RETENTION FUNCTION]** Demonstration: charge leaves with no use.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn top-down view of an open drawer, 16:9: grey surround, white inner box, two red AA batteries, a pen and small dice. Hand-drawn thin outlines. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no hands, no extra objects, no photoreal
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Batteries nudge/rotate slightly, then drain from red to white. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Top-down drawer: two red batteries nudge, then turn white.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Plate + object nudge + recolor.
18. **[EDIT RECONSTRUCTION]** Hard cut; hold; recolor; hard cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Demonstration: charge leaves with no use. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Recolor red->white = discharge (same colour logic as red=life).
21. **[LIKELY CREATOR INTENT]** HIGH: show self-discharge.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text n/a
23. **[EDITOR IMPROVEMENT]** Fine.


### S20 - Six battery types draining (red fill -> empty)  (165.708 -> 172.125 s, 6.4 s)

1. **[VISUAL ID]** S20
2. **[TIMESTAMP]** 165.708-172.125 s (start frame 3977); boundary: hard cut f3977 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Some types last longer than others, but even batteries advertised as having long shelf lives typically only hold their charge for a decade or two.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) White: six labelled icons - LEAD-ACID, ALKALINE, ZINC CARBON, Ni-MH, Ni-Cd, LITHIUM-ION - each filled red; fills drain at different rates (~166-169 s), ending all empty outlines.
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to a labeled grid; per-icon fill animation.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) red fills (only colour); 2) labels.
8. **[COMPOSITION ANALYSIS]** 3x2 grid, centered.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) red fills (only colour) | see anim/events | see facts | see composition | n/a | Very High |
| 2) labels. | see anim/events | see facts | see composition | n/a | High |

10. **[RETENTION FUNCTION]** Evidence + comparison: different drain rates.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D icon grid on white, 16:9: six battery icons with small caps labels LEAD-ACID, ALKALINE, ZINC CARBON, Ni-MH, Ni-Cd, LITHIUM-ION; red fill levels inside each (full). Thin black outlines. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no extra labels, no gradients
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** All fills start full; each drains downward at its own speed until empty; labels static. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Six labeled battery icons drain their red fill at different speeds until empty.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Per-icon fill masks animated.
18. **[EDIT RECONSTRUCTION]** Hard cut; staggered drains; hard cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Evidence + comparison: different drain rates. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Fill-drain system.
21. **[LIKELY CREATOR INTENT]** HIGH.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion High; Text High
23. **[EDITOR IMPROVEMENT]** Works.


### S21 - Solar buildings/weather station/perimeter camera build-up  (172.125 -> 180.000 s, 7.9 s)

1. **[VISUAL ID]** S21
2. **[TIMESTAMP]** 172.125-180.000 s (start frame 4131); boundary: boundary ~172.125 (white-to-white, detector 11.8; ESTIMATED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Solar power is probably the most promising candidate. There are many off-grid solar-powered buildings, weather stations, and other remote infrastructure around the world.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) White; a house with a solar-panel roof at left; a vertical divider and a weather-station pole with a small solar panel appears (~175 s); then a third panel with a security camera, razor-wire fence and small panel appears at right (~178.5 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** Panels added left to right (same system as S16).
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) newest panel; 2) house.
8. **[COMPOSITION ANALYSIS]** Three-column.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) newest panel | see anim/events | see facts | see composition | n/a | Very High |
| 2) house. | see anim/events | see facts | see composition | n/a | High |

10. **[RETENTION FUNCTION]** Examples list; builds the case for solar.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D three-column illustration on white, 16:9: column 1 a house with a solar roof; column 2 a weather station on a pole with a small panel; column 3 a security camera above a razor-wire fence with a small panel. Thin vertical dividers. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no people, no color
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: house only; weather station slides in; third column slides in. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Three solar examples appear one after another in a row.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Sequential panel adds.
18. **[EDIT RECONSTRUCTION]** Cut; staged adds; hard cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Examples list; builds the case for solar. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Column-build system from S16.
21. **[LIKELY CREATOR INTENT]** HIGH.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text n/a
23. **[EDITOR IMPROVEMENT]** Fine.


### S22 - Roadside call box + billboard 'RHODE ISLAND POPULATION: EVERYONE 0'  (180.000 -> 191.208 s, 11.2 s)

1. **[VISUAL ID]** S22
2. **[TIMESTAMP]** 180.000-191.208 s (start frame 4320); boundary: hard cut f4320 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Emergency call boxes, often found along the side of the road in remote locations, are frequently solar-powered. They usually have lights on them, which provide illumination every night.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Dark grey night road with dashed centre line and bushes; billboard 'RHODE ISLAND / POPULATION: EVERYONE 0' (the word EVERYONE appears struck/underlined; low-res uncertainty); right: pole with solar panel on top, a light shining down onto the road and a 'HELP' call box. Static through the shot.
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to a night road scene; first appearance of the 'last light' candidate.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) lit road cone; 2) billboard; 3) panel.
8. **[COMPOSITION ANALYSIS]** Horizontal road; pole right; billboard left; light cone diagonal.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) lit road cone | see anim/events | see facts | see composition | n/a | Very High |
| 2) billboard | see anim/events | see facts | see composition | n/a | High |
| 3) panel. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Reveal of the leading candidate (solar call box) + joke billboard.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D hand-drawn night road, 16:9, dark grey: dashed center line, bushes left, a billboard reading 'RHODE ISLAND / POPULATION: EVERYONE 0', at right a pole with a solar panel on top, a downward lamp casting a bright cone on the road and a small box labelled 'HELP'. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no cars, no people, no extra signs
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Static; light cone constant. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Static night road with a solar-powered call box lighting the asphalt.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Plate with glow layer.
18. **[EDIT RECONSTRUCTION]** Hard cut; hold ~11 s; cut to close-up.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Reveal of the leading candidate (solar call box) + joke billboard. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Wide road composition reused in S24 (after-time-skip).
21. **[LIKELY CREATOR INTENT]** HIGH: introduce the winner candidate.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Low; Text Medium (billboard)
23. **[EDITOR IMPROVEMENT]** Long static hold (~11 s): possible low-change zone; mitigated by narration density.


### S23 - Solar panel close-up accumulating grime  (191.208 -> 200.208 s, 9.0 s)

1. **[VISUAL ID]** S23
2. **[TIMESTAMP]** 191.208-200.208 s (start frame 4589); boundary: boundary 191.208 (dark-to-dark, detector 19.5; ESTIMATED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Solar panels will generally last as long as the electronics connected to them, and as long as the panels are kept free of dust and debris. The wires and circuits will eventually succumb to corrosion...'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Close-up of the tilted panel on a pole with the lamp below; dark speck/dirt clusters then cracks appear on the panel (~194-198 s) and dark vertical drips along the pole (~198-199.5 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** Zoomed composition of S22 object (callback), decay overlay added.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) panel; 2) grime; 3) lamp glow bottom-left.
8. **[COMPOSITION ANALYSIS]** Diagonal panel, pole vertical.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) panel | see anim/events | see facts | see composition | n/a | Very High |
| 2) grime | see anim/events | see facts | see composition | n/a | High |
| 3) lamp glow bottom-left. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Decay demonstration (corrosion/dust).
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D close-up, 16:9, dark grey: a tilted rectangular solar panel on a pole at center-right with a small lamp below left emitting a soft white glow; add dark speck clusters and thin cracks across the panel and dark drip lines along the pole. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no people, no text, no extra objects
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Start: clean panel. Specks and cracks accumulate, then drips run down the pole. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Close-up of the solar panel as grime, cracks and drips gradually spread.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Cropped reuse + progressive overlay.
18. **[EDIT RECONSTRUCTION]** Cut/zoom from S22; hold; progressive overlay; cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Decay demonstration (corrosion/dust). Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Cropped reuse of S22's pole + panel.
21. **[LIKELY CREATOR INTENT]** HIGH.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Low (zoom vs cut unverified); Motion Medium; Text n/a
23. **[EDITOR IMPROVEMENT]** Fine.


### S24 - 'SPACE SUBMARINES IN CINEMAS!' billboard, '~100 YEARS', rain  (200.208 -> 209.667 s, 9.5 s)

1. **[VISUAL ID]** S24
2. **[TIMESTAMP]** 200.208-209.667 s (start frame 4805); boundary: boundary 200.208 (dark-to-dark, detector 19.6; ESTIMATED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** '...solar panels in a dry place, with well-built electronics, could easily continue providing power for a century if they're kept free of dust by occasional breezes or rain...'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Back to wide road; billboard now reads 'SPACE SUBMARINES! IN CINEMAS!' (faded paint; replaces the Rhode Island sign), a spiky tumbleweed near the lamp cone; '~100 YEARS' appears top-right (~203.5 s); diagonal rain streaks begin (~207.5 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** Callback to S22 composition with changes: sign replaced, tumbleweed, label, rain.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) lit road; 2) sign; 3) label.
8. **[COMPOSITION ANALYSIS]** Same as S22.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) lit road | see anim/events | see facts | see composition | n/a | Very High |
| 2) sign | see anim/events | see facts | see composition | n/a | High |
| 3) label. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Time-skip: same composition shows decades passing (visual callback).
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Reuse S22 night road composition (call-box pole at right, light cone, dashed line) with a different billboard reading 'SPACE SUBMARINES! IN CINEMAS!', a small spiky tumbleweed near the lamp cone, text '~100 YEARS' top-right, and optional diagonal rain streaks across the whole frame. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no people, no vehicles, no extra signs
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Static; '~100 YEARS' label appears; rain streaks fall diagonally across the frame; lamp stays on. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Same night road a century later: new sign, tumbleweed, '~100 YEARS', rain, lamp still lit.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Compositional reuse with changed props.
18. **[EDIT RECONSTRUCTION]** Cut/dissolve from close-up; hold; label; rain; hard cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Time-skip: same composition shows decades passing (visual callback). Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Compositional reuse of S22 with changed props.
21. **[LIKELY CREATOR INTENT]** HIGH: show decay of everything except the lamp.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text High
23. **[EDITOR IMPROVEMENT]** Good callback.


### S25 - Five-lane columns darken to leave solar lit  (209.667 -> 220.667 s, 11.0 s)

1. **[VISUAL ID]** S25
2. **[TIMESTAMP]** 209.667-220.667 s (start frame 5032); boundary: hard cut f5032 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'If we follow a strict definition of lighting, solar-powered lights in remote locations could conceivably be the last surviving human light source.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Five vertical lanes each with a hanging bulb: geothermal, wind, hydro, battery, solar call box. Lanes go dark left to right (~210.5-218 s), leaving the solar lane lit; then the lanes shift and a radioactive-waste barrel appears in the rightmost lane (~219.5 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to a summary lineup; stepwise light-out; new object introduced at the end.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) the single lit lane; 2) bulbs; 3) barrel (late).
8. **[COMPOSITION ANALYSIS]** Five equal vertical columns.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) the single lit lane | see anim/events | see facts | see composition | n/a | Very High |
| 2) bulbs | see anim/events | see facts | see composition | n/a | High |
| 3) barrel (late). | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Recap + reveal of a twist: 'there's another contender'.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D five-lane lineup, 16:9, light grey fading to dark grey: each lane has a hanging bulb at top; lanes contain (left to right) a geothermal plant, a wind turbine, a hydro pipe, a battery, a solar call box with lamp. Most lanes are dark, the solar lane lit; an optional radioactive waste barrel in the last lane. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no text, no people
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Lanes extinguish one by one left to right; the barrel slides in at the end. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Five lanes go dark one by one until only solar remains; then a nuclear-waste barrel appears.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Lane plates with per-lane glow toggles.
18. **[EDIT RECONSTRUCTION]** Hard cut; staggered extinguish; barrel slide-in; hard cut to glow.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Recap + reveal of a twist: 'there's another contender'. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Lanes echo S10/S12; ends with barrel hand-off to S26.
21. **[LIKELY CREATOR INTENT]** HIGH: recap before twist.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text n/a
23. **[EDITOR IMPROVEMENT]** Efficient recap.


### S26 - Barrel glow -> dim; warning signs  (220.667 -> 227.917 s, 7.2 s)

1. **[VISUAL ID]** S26
2. **[TIMESTAMP]** 220.667-227.917 s (start frame 5296); boundary: hard cut f5296 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'But there's another contender, and it's a weird one: spent nuclear fuel. Contrary to popular portrayals, radioactivity isn't usually visible, which is part of why we need warning signs...'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Dark-grey floor line; a barrel with radiation symbol glows white (~221-222.5 s), then the glow vanishes and the barrel is a dim outline (~223.5 s). Then a 'DANGER RADIOACTIVE' sign, a small trefoil sign and a trefoil triangular sign on a pole appear (~225-227 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** Glow on->off; warning signs added.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) glowing barrel; 2) signs.
8. **[COMPOSITION ANALYSIS]** Barrel center, signs flanking.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) glowing barrel | see anim/events | see facts | see composition | n/a | Very High |
| 2) signs. | see anim/events | see facts | see composition | n/a | High |

10. **[RETENTION FUNCTION]** Myth-bust: radioactivity isn't visible -> glow removed then signs added.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D dark-grey scene, 16:9: a barrel with a radiation trefoil on a floor line, optional white radial glow; add a 'DANGER RADIOACTIVE' wall sign at upper-left, a small trefoil sign at left of the barrel, and a triangular trefoil sign on a pole at right. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no extra text, no people
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Barrel glows then glow fades out; signs pop in. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Glowing barrel fades to dim, then radiation warning signs appear around it.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Glow layer toggle + sign pop-ins.
18. **[EDIT RECONSTRUCTION]** Cut; hold; glow off; signs in; hard cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Myth-bust: radioactivity isn't visible -> glow removed then signs added. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Glow-off beat (radioactivity invisible) before S28 re-introduces glow as cyan.
21. **[LIKELY CREATOR INTENT]** HIGH: debunk glow myth.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text High
23. **[EDITOR IMPROVEMENT]** Works.


### S27 - Glow-in-the-dark watch dial; face goes black  (227.917 -> 246.708 s, 18.8 s)

1. **[VISUAL ID]** S27
2. **[TIMESTAMP]** 227.917-246.708 s (start frame 5470); boundary: hard cut f5470 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Sure, watch dials used to be coated in small amounts of radium to help them glow in the dark, but the glow didn't come from the radioactivity itself... Once the phosphorescent paint breaks down, the watch dials are still radioactive, but no longer glow.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) White with concentric grey rings around a black watch face with numbers; from ~235 s a female stick figure with a hair bun sits at a desk (lower-right), painting/working. At ~240.5 s the watch face and numbers disappear, leaving a black disc; rings remain.
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to a radial scene; figure appears; face goes black.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) watch face; 2) rings; 3) figure.
8. **[COMPOSITION ANALYSIS]** Radial symmetry, figure lower-right.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) watch face | see anim/events | see facts | see composition | n/a | Very High |
| 2) rings | see anim/events | see facts | see composition | n/a | High |
| 3) figure. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Explanation by history/analogy (radium dial) ending in 'glow gone'.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D radial illustration on white, 16:9: concentric hand-drawn grey rings around a round black wristwatch with white numerals 1-12; at lower right a seated stick figure with a hair bun at a slanted desk with a brush. Optional second state: the watch face fully black with no numerals. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no extra people, no photoreal, no color
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Rings static/subtle; figure appears; watch numerals vanish leaving a black disc. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Concentric rings around a watch; the dial painter appears, then the numerals vanish.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Radial plate + figure layer + dial toggle.
18. **[EDIT RECONSTRUCTION]** Cut; ~7 s hold; figure in; dial-off; cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Explanation by history/analogy (radium dial) ending in 'glow gone'. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Analogy; radial plate; single use.
21. **[LIKELY CREATOR INTENT]** HIGH.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Low; Text n/a
23. **[EDITOR IMPROVEMENT]** Long hold (~19 s) with small changes: possible low-change zone.


### S28 - Cherenkov radiation diagram -> glowing cesium capsule in water  (246.708 -> 258.458 s, 11.8 s)

1. **[VISUAL ID]** S28
2. **[TIMESTAMP]** 246.708-258.458 s (start frame 5921); boundary: hard cut f5921 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'When radioactive particles travel through materials like water or glass, they can emit light through a sort of optical sonic boom. This light is called Cherenkov radiation, and it's seen in the distinctive blue glow of nuclear reactor cores.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) White; a grey water tank (left) with expanding circles and a dashed cone behind a moving point; the tank gradually shows cyan glow and curved wave lines (~250-252 s); label 'CHERENKOV RADIATION' appears at right (~252 s); then a cutaway of a hanging capsule in water glowing cyan with a soft cyan halo (~254-258 s).
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to a physics diagram; colour introduced (cyan); then object shot.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) cyan glow; 2) circles; 3) label.
8. **[COMPOSITION ANALYSIS]** Tank left, label right, then centered capsule.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) cyan glow | see anim/events | see facts | see composition | n/a | Very High |
| 2) circles | see anim/events | see facts | see composition | n/a | High |
| 3) label. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Explanation + visual reward: the first cyan colour appears exactly when the 'blue glow' is explained.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D diagram, 16:9, white: a grey water tank with a dashed cone and expanding circles from a small point; cyan radial glow and wavy lines in the water; label 'CHERENKOV RADIATION' at right. Second state: a vertical cesium capsule hanging in a grey water tank with a cyan halo. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no realistic water, no extra text
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Circles expand; cyan glow fades in with wave lines; label appears; then the capsule glows cyan. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Wave-front diagram turns cyan, the label appears, then a capsule glows cyan in water.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Diagram plate + glow overlays.
18. **[EDIT RECONSTRUCTION]** Cut; staged; dissolve/cut to capsule; cut to text.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Explanation + visual reward: the first cyan colour appears exactly when the 'blue glow' is explained. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** First cyan: becomes the final colour identity.
21. **[LIKELY CREATOR INTENT]** HIGH: introduce the cyan visual identity.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text High
23. **[EDITOR IMPROVEMENT]** Works.


### S29 - 'CESIUM 137' label -> glowing capsule + decay graph  (258.458 -> 285.167 s, 26.7 s)

1. **[VISUAL ID]** S29
2. **[TIMESTAMP]** 258.458-285.167 s (start frame 6203); boundary: hard cut f6203 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'Some of our radioactive waste products, such as cesium-137, are melted and mixed with glass... Cesium-137 has a half-life of 30 years, which means that two centuries later, the blocks will still be glowing with 1% of their original radioactivity.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) White: text 'CESIUM 137' alone, then boxed into a label, then widening into a bar/capsule graphic. At ~264 s the background goes dark grey and the capsule glows cyan; at ~269.5 s a framed graph appears above: red decay curve with '30 YEAR HALFLIFE CESIUM-137' and axes. Glow dims slightly across ~271-276 s.
5. **[CHANGE FROM PREVIOUS VISUAL]** Text becomes object; colour from white to dark with cyan; graph added.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) glowing capsule; 2) graph; 3) label.
8. **[COMPOSITION ANALYSIS]** Vertical stack: graph above, capsule below.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) glowing capsule | see anim/events | see facts | see composition | n/a | Very High |
| 2) graph | see anim/events | see facts | see composition | n/a | High |
| 3) label. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** Mega-payoff setup: the object whose glow is the answer.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 2D scene, 16:9, dark grey: a long rounded capsule labelled 'CESIUM 137' with cyan glow, above it a grey framed graph with a red exponential-decay curve and text '30 YEAR HALFLIFE CESIUM-137', axes with numbers 0-240. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no extra text, no photoreal glass
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Text boxes into a capsule; background darkens; capsule glows cyan; graph pops in; glow slowly dims. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Text turns into a cyan-glowing capsule on dark; a decay graph appears above it and the glow slowly dims.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Text-to-object transform + glow + graph overlay.
18. **[EDIT RECONSTRUCTION]** Cut; staged transform; hold ~14 s; hard cut.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Mega-payoff setup: the object whose glow is the answer. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Cyan glow + decay graph (S29) -> S30.
21. **[LIKELY CREATOR INTENT]** HIGH: payoff object.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Medium; Text High
23. **[EDITOR IMPROVEMENT]** ~27 s shot; hold at end is long, change frequency low.


### S30 - Stacked glowing cyan blocks on black (answer)  (285.167 -> 293.792 s, 8.6 s)

1. **[VISUAL ID]** S30
2. **[TIMESTAMP]** 285.167-293.792 s (start frame 6844); boundary: hard cut f6844 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** 'And thus, we arrive at our answer: Centuries from now, deep in concrete vaults, the light from our most toxic waste will still be shining.'
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Pure black background; a stack of eight horizontal cyan-glow capsule blocks arranged symmetrically (two columns of four). Static, constant glow.
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to pure black; simplified composition.
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) cyan glow (only brightness).
8. **[COMPOSITION ANALYSIS]** Centered symmetrical, huge negative space.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) cyan glow (only brightness). | see anim/events | see facts | see composition | n/a | Very High |

10. **[RETENTION FUNCTION]** Ultimate payoff: the answer, shown as the single remaining light.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a minimal 2D scene, 16:9, pure black: a symmetrical stack of eight horizontal capsule blocks (two columns of four) with soft cyan outer glow and light-grey line art. Nothing else. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no text, no extras, no gradients beyond the glow
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Fully static; constant glow. Camera locked. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Pure black frame with a stacked cluster of softly glowing cyan blocks, static.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Single glow plate.
18. **[EDIT RECONSTRUCTION]** Hard cut; ~8.6 s hold; hard cut to end card.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** Ultimate payoff: the answer, shown as the single remaining light. Content-vs-decoration: Essential/Reinforcing (adds information beyond narration).
20. **[VISUAL EVOLUTION / CALLBACK]** Cyan stack = final payoff.
21. **[LIKELY CREATOR INTENT]** HIGH: payoff held as a final image.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Low; Text n/a
23. **[EDITOR IMPROVEMENT]** Works as final image; hold ~8.6 s - voice carries it.


### S31 - End card with book CTA and credits  (293.792 -> 303.856 s, 10.1 s)

1. **[VISUAL ID]** S31
2. **[TIMESTAMP]** 293.792-303.856 s (start frame 7051); boundary: hard cut f7051 (MEASURED). Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** No narration identified for the end card (UNAVAILABLE without audio review).
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) Red background; black satellite+dinosaur silhouette at left edge; centered 'GET THE BOOKS: xkcd.com/books' above four book covers (what if?, THING EXPLAINER, how to, what if? 2); right: 'Narrated by and based on "What If" by Randall Munroe xkcd.com'; 'More serious answers to absurd questions at: what-if.xkcd.com'; 'Henry Reich - Writer & Video Director'; 'Lizah van der Aart - Illustration & Video Editing'; 'Ever Salazar - Illustration & Animation'; 'Know Art Studios - Music & Sound Effects'; fine print: 'What If? The Video Series is the official adaptation of the What If? books by Randall Munroe and is produced by Neptune Studios LLC'; '(c)2024 xkcd, inc. xkcd.com'. Static.
5. **[CHANGE FROM PREVIOUS VISUAL]** Cut to the same red as S02 (bookend).
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) 1) 'GET THE BOOKS' + covers; 2) silhouette; 3) credits.
8. **[COMPOSITION ANALYSIS]** Left-bottom CTA group, right credits column.
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
| 1) 'GET THE BOOKS' + covers | see anim/events | see facts | see composition | n/a | Very High |
| 2) silhouette | see anim/events | see facts | see composition | n/a | High |
| 3) credits. | see anim/events | see facts | see composition | n/a | Medium |

10. **[RETENTION FUNCTION]** CTA + credits + series/book bridge; bookends S02.
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** Create a flat 16:9 end card, solid saturated red background: left edge a black silhouette of a satellite with a dinosaur creature; center-bottom white text 'GET THE BOOKS: xkcd.com/books' above four portrait book covers in a row; right column credits in white with names in bold and roles in light weight; small centered copyright line at bottom. Use placeholder covers if source art is unavailable. Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** no extra logos, no fabricated credits, do not alter names or text
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** Static; no motion observed. Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** Static red end card: books CTA, covers and credits.
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** Single static plate.
18. **[EDIT RECONSTRUCTION]** Hard cut in; hold ~10 s; end.
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** CTA + credits + series/book bridge; bookends S02. Content-vs-decoration: Essential (CTA/credits).
20. **[VISUAL EVOLUTION / CALLBACK]** Bookend of S02.
21. **[LIKELY CREATOR INTENT]** HIGH: CTA to the books the series adapts.
22. **[RECONSTRUCTION CONFIDENCE]** Subject High; Environment High; Camera Medium; Motion Low; Text High (read at 1280 px)
23. **[EDITOR IMPROVEMENT]** CTA is end-only; no mid-video CTA observed.


## Part B - Video-level synthesis

### B1. Locks (use in every prompt)
- **CHARACTER LOCK (stick figure):** thin black wobbly outline, large empty circle head, no facial features, straight-line limbs, no fill; occasional hair bun / hard hat as only accessories (OBSERVED). Red version = same figure recolored.
- **RED PARTICLE DISINTEGRATION (effect lock):** outline breaks into small red specks drifting away from the figure's left/top; dissolve lasts roughly 1.5-3 s; appears on every "person removed" beat (S01, S04, S05, S06, S07, S11, S14, S17).
- **ENVIRONMENT LOCK A - silhouette plates:** solid near-black mass on off-white sky, thick black ground strip, line-drawn smoke, pylon at right (S05, S07, S09, S13, S15, S17).
- **ENVIRONMENT LOCK B - dark scenes:** dark grey ground/background with glow cones (S11, S22-S24, S26).
- **COLOR LOCK:** off-white, mid/dark greys, black; red only for people/failure/draining; cyan only for radioactive glow (S28-S30); no other hues except the red end card (S02, S31). Hex codes not measured.
- **TEXT LOCK:** hand-drawn caps for labels (e.g. '< 6 MONTHS'), serif for the question card, clean sans for end-card credits.
- **LIGHT/GLOW LOCK:** a soft white radial glow = "light on"; glow removed = "light out"; this on/off state is the main storytelling variable.

### B2. Creator visual system (supported by repetition)
- **Composition:** locked frames; horizontal silhouette bands; side-by-side column builds (S16, S21, S25); frame-within-frame insets (S04, S15, S16).
- **Motion:** almost no camera movement observed (not verified between samples). Motion = layer pop-ins, glow toggles, recolor, dissolve, fills draining, progressive decay overlays. Hard cuts between shots.
- **Pattern interrupts:** red particle dissolve (every ~10-20 s), global darken step (S06), colour jump (S02, S28 cyan), text label pop-ins.
- **Time-label system:** white caps label bubbles appear when a source "dies" ('< 6 MONTHS', '< 3 YEARS', '11 YEARS', '3 YEARS', '>20 YEARS', '~4 YEARS', '~100 YEARS'), forming a scoreboard the viewer can follow.
- **Humor layer:** speech bubbles, gag props (Eternal LIGHT box, Rhode Island billboard, 'UH OH...', 'MAYDAY!', 'OOPS!', Tom Scott cameo).

### B3. Retention / pacing (qualitative; no metrics)
- **Fast zones:** 8-21 s (four shots in 13 s), 72-100 s (5 short shots).
- **Slow/hold zones:** S08 (7 s chart), S22 (11 s road), S27 (19 s radial), S29 (27 s), S30 (8.6 s static final). Possible retention risk where narration is dense but visuals static; mitigations seen: staged label pop-ins and glow dims.
- **Strongest reveal:** S28 first cyan glow tied to "Cherenkov". **Strongest reversal:** S26 'weird contender' + glow on->off->new glow. **Strongest callback:** S22->S24 same road a century later. **Strongest escalation:** time labels from months -> years -> decades -> centuries.
- **Clip candidates (Shorts):** S11 island (diesel, < 6 months) ~9 s; S14 maintenance gag ~11 s; S15+S16 turbine lifespans ~28 s; S22-S24 solar call box ~29 s; S26-S30 radioactive twist ~65 s. Each needs added context; none promised here.

### B4. Thumbnail-style candidates (from frames; actual thumbnail not available)
1. S30 (285-293 s): single glowing cyan block cluster on black - single dominant promise, mobile-readable; add a short question; title would pair with 'the last light' idea.
2. S01 (0-3 s): large presenter + lamp + question; text-heavy, lower mobile readability.
3. S22: lit road with solar call box; medium readability.

### B5. Script analyzer consensus (seven lenses applied once; not seven external models)
- **Agreement:** strong hook (question card), clear elimination ranking, good humor, time labels as mini-payoffs, answer arrives as the twist.
- **Disagreement:** viral lens would reveal the cyan glow earlier; narrative lens keeps the twist late (current structure supports surprise).
- **Highest-priority risks:** Medium - static holds in S08/S22/S27/S29; Optional - mid-video CTA absent (end-only).
- **Scorecard (qualitative):** Hook Strong; Curiosity Strong; Narrative spine Exceptional; Pacing Strong; Payoffs Exceptional; Emotional engagement Functional (awe/humor, no empathy beats); Intellectual clarity Strong; CTA Functional (end only); Title alignment Excellent; Thumbnail alignment Not available.

### B6. Creator formula
1. **Setup:** viewer question on a card, a presenter who disappears.
2. **Curiosity:** list candidate sources; each fails with a time label.
3. **Visual escalation:** months -> years -> decades -> centuries; scenes get darker and simpler.
4. **Reversal:** the twist contender (radioactive waste glow).
5. **Payoff:** black frame with cyan glow; spoken answer.
**Visual formula:** one object per shot; state change on one variable (glow/colour/label); reuse plates; red = people, cyan = radioactivity.
**Editing formula:** hard cuts between plates; intra-shot changes by layer toggles timed to narrated facts; progressive overlays for decay.
**Retention formula:** open one loop (last light), close many micro-loops (each source's lifespan), then pay off with a surprise.

### B7. Asset list
- Characters: C01 presenter/stick figure; C02 inner chalkboard figure; C03 workers (red); C04 hard-hat operator; C05 seated operators; C06 dial painter.
- Environments: E01 chalkboard; E02 skyline; E03 apartment cutaway; E04-E08 silhouette plates (coal, nuclear, geothermal, wind farm, dam); E09 control room; E10 pipe room; E11 night road; E12 island; E13 diagrams (Cherenkov, tank).
- Objects: lamp, lava lamp, barrel, battery set, solar pole/call box, watch, capsule, generator.
- Graphics: time labels, speech bubbles, charts, decay graph, red particles, cyan glow, rain.
- Image prompts: IP-S01..IP-S31 (in Part A, section 12). Animation prompts: AP-S01..AP-S31 (section 14).

### B8. Rebuild workflow
1. Break the transcript into ~31 beats (one per shot).
2. Define the single state variable per beat (glow/colour/label).
3. Build plates once (silhouette A/B) and reuse (S07->S09, S22->S24).
4. Generate static plates with the section-12 prompts.
5. Animate only: dissolve, glow toggle, fill drain, overlay decay (section 14).
6. Add labels timed to the narrated number.
7. Cut on narrative emphasis; hard cuts only.
8. Insert a state change before any hold > ~8 s.
9. Preserve callbacks (road, plant).
10. Deliver the twist payoff as a simple, quiet final image.

### B9. Notes and open questions
- On-screen **'76,000,000'** vs spoken **'about six million times'**: different quantities may be shown; unresolved.
- **'Tom Scott'** card: on-screen text shows a creator name with a verified check; whether this is an intentional cameo reference is INFERRED.
- Whether the episode text is adapted from the *What If?* books: the end card states 'official adaptation of the What If? books' (OBSERVED), but which book/chapter is **not** established here.
- Credits (OBSERVED, S31): Henry Reich (Writer & Video Director); Lizah van der Aart (Illustration & Video Editing); Ever Salazar (Illustration & Animation); Know Art Studios (Music & Sound Effects); produced by Neptune Studios LLC.


## Part C - Audio alignment (added 2026-11-17, ASR only)

**Method:** `whisper-cli` (whisper.cpp) with `ggml-medium.en`, 16 kHz mono extract of the source audio; word timestamps (`-ml 1 -sow`). Files: `audio/whisper_medium_en.srt`, `audio/whisper_medium_en_words.srt`, `audio/words.json`. This is **ASR_UNCERTIFIED**: machine transcription, **not human listening**, so the audio gate stays BLOCKED and there is no AV sign-off. Word times are approximate (about +/-0.3 s).

**Measured audio facts:** narration runs from 0.06 s to ~291.96 s (last word 'shining'); one detected silence of 1.69 s starts at 292.21 s (just before the end card at 293.79 s); ASR tags a '(gentle music)' non-speech label at ~299-301.7 s during the end card. Music/SFX elsewhere were **not** characterised (UNAVAILABLE).

**Timed transcript vs the earlier untimed transcript:** content order agrees with the shot mapping; the question card is read aloud during S01 (0.06-8.5 s).

### Alignment findings (spoken start vs visual onset window, seconds)

| Event | Spoken phrase | Spoken start | Visual window | Relation |
|---|---|---|---|---|
| E003 | go out | 8.17 | 6.00-8.60 | approximately simultaneous (dim window 6.0-8.6 s vs spoken "go out" 8.17 s) |
| E002 | disappeared | 4.08 | 3.50-5.00 | approximately simultaneous (dissolve 3.5-5.0 s vs spoken "disappeared" 4.08 s) |
| E012 | blackout | 39.38 | 38.58-38.83 | visual leads spoken by 0.55 to 0.8 s |
| E014 | six million | 51.17 | 50.46-51.46 | approximately simultaneous (-0.29 to 0.71 s; +ve = visual earlier) |
| E015 | rapidly shut down | 65.50 | 66.50-67.50 | visual follows spoken "rapidly shut down" (65.5-66.5 s) by ~0 to 2 s |
| E020 | days to months | 86.48 | 86.50-87.70 | approximately simultaneous (visual onset window 86.5-87.7 s contains spoken start 86.48 s) |
| E024 | climb | 117.88 | 116.46-117.46 | visual leads spoken by 0.42 to 1.42 s |
| E025 | 11 years | 122.39 | 120.46-121.46 | visual leads spoken by 0.93 to 1.93 s |
| E028 | hoover dam | 142.89 | 141.46-142.46 | visual leads spoken by 0.43 to 1.43 s |
| E030 | several years | 147.15 | 150.46-151.46 | visual lags spoken by 3.31 to 4.31 s |
| E037 | a century | 204.85 | 202.46-203.46 | visual leads spoken by 1.39 to 2.39 s |
| E040 | spent nuclear fuel | 218.61 | 218.46-219.46 | approximately simultaneous (-0.85 to 0.15 s; +ve = visual earlier) |
| E041 | visible | 223.46 | 222.46-223.46 | visual leads spoken by 0.0 to 1.0 s |
| E044 | breaks down | 239.89 | 239.46-241.46 | approximately simultaneous (numerals vanish 239.5-241.5 s; spoken "breaks down" 239.89 s); later "no longer glow" at 242.60 s |
| E046 | cherenkov radiation | 252.65 | 251.46-252.46 | visual leads spoken by 0.19 to 1.19 s |
| S29 | cesium-137 | 258.84 | 258.46-258.46 | visual leads spoken by 0.38 to 0.38 s |
| E049 | half-life | 270.22 | 268.46-269.46 | visual leads spoken by 0.76 to 1.76 s |

**Patterns (OBSERVED, 17 anchors only):**
- Time labels and diagrams tend to appear **1-2.5 s before** the spoken words ('11 YEARS' ~1-2 s early, '~100 YEARS' ~1.4-2.4 s early, decay graph ~0.8-1.8 s early). INFERRED (medium): visuals are placed slightly ahead so the viewer reads first and hears the confirmation.
- Several changes land **on** the key word: dissolve on 'disappeared', glow-off on 'visible', barrel on 'spent nuclear fuel', 'Cherenkov radiation' label, watch numerals on 'breaks down'; 'blackout' darken comes 0.55-0.8 s earlier.
- One clear lag: '~4 YEARS' appears ~3.3-4.3 s **after** 'several years'.
- '76,000,000' appears while the narrator says 'six million'; the numbers still differ (unresolved).
- The 'CESIUM 137' card cuts in 0.38 s before the first spoken 'cesium-137' (cut MEASURED, word ASR).


## Part D - Music / non-voice bed (added 2026-11-17, Demucs stem separation)

**Method:** `demucs` (`htdemucs`, two stems: vocals / no_vocals) in an isolated venv; per-second RMS of each stem. Files: `audio/demucs/htdemucs/8fADp43wJwU_44k_stereo/{vocals,no_vocals}.wav`, `CH-000004_8fADp43wJwU_1fb3c0f4_audio_stem_levels_per_second.csv`, `audio/bed_events.json`. This is **MEASURED** level data on separated stems, but separation is imperfect (voice leakage, and "no_vocals" mixes music with sound effects and room tone). It is **not human listening**; the audio gate stays BLOCKED.

**Findings (MEASURED, 1-second resolution):**
- The non-voice bed is present **from 0 s to the end** at a nearly constant level (median -32.4 dBFS, range of 20-s block means -30.5 to -34.4 dBFS), about **11-14 dB below the voice** (voice median -19.4 dBFS). It is not louder in the voice-free end card (-33 dBFS) and is not visibly ducked under speech: the bed sits at a steady level while the narrator speaks.
- Narration ends at ~291.9 s (vocal stem drops to about -90 dBFS from ~293 s). The bed continues through the end card to 303 s, with a one-second dip near 292 s (-24 dB vs local median).
- Whole-bed rhythmic periodicity estimate: ~70 BPM (alternatives ~94, ~140 BPM; **low confidence**, autocorrelation on a quiet bed). Spectral centroid median ~1.6 kHz. Genre, key, instrumentation and song identity are **not determined**; the end-card credit says 'Know Art Studios - Music & Sound Effects' (OBSERVED on screen).
- **Accent / dip candidates in the bed** (level >= 2.5 dB above, or <= -5 dB below, its local median; second resolution, so +/-1 s):

| Bed event (s) | Change | Nearby visual event (this report) | Relation |
|---|---|---|---|
| 14 | +2.5 dB | 13.2-13.3 windows switch off (S03) | within ~1 s |
| 38 | +3.8 dB | 38.58 full-frame darken step (S06) | within ~1 s |
| 78 | +3.3 dB | four-panel bulbs out / boundary 78.875 (S10-S11) | within ~1 s |
| 157 | +3.4 dB | cut to Eternal LIGHT card at 158.08 (S18) | ~1 s before the cut |
| 202 | +3.0 dB | boundary 200.208 / label '~100 YEARS' ~203 (S24) | within ~2 s |
| 220, 223, 224, 227 | +3.9 to +6.2 dB | cut 220.67 (S26), barrel glow off ~222.5-223.5, cut 227.92 (S27) | at or near each |
| 219, 222, 225, 228 | -6.4 to -11.1 dB dips | barrel appears ~219, glow ends ~222.5, signs ~225, cut 227.9 | at or near each |

- Fully aligned with the S26 cluster: the bed shows its largest accents/dips (up to +6.2 dB and -11.1 dB) during 219-228 s, exactly the 'radioactivity isn't visible' / warning-signs passage. INFERRED (medium): this section has the most deliberate sound design in the video. Other accents are small (2.5-3.8 dB).
- **Not established:** whether the bed is music, sound effects, or both; the instrument; whether accents are SFX hits or music dynamics; timing within a second.

**What this does and does not allow:** you can state that a continuous non-voice track runs under the whole video at roughly -33 dBFS, that it is about 12 dB under the voice, and that its biggest level changes cluster at 219-228 s. You cannot call it a specific song, a BPM, or confirm SFX identity without a person listening to the stems.

### Part D2 - What kind of music? (measured features, SPECULATIVE interpretation)

- **Clean evidence is only the end card (294-303 s)**, where the narrator is silent. Features: almost no energy above ~800 Hz (0.1% mid, ~0% above 2.5 kHz), energy mostly 80-800 Hz, steady level, no strong periodic hits detected. Strongest tonal peaks ~86, 248, 291, 377, 441, 495, 592, 668 Hz (about F2/E2, B3, D4, F#4, A4, B4, D5, E5 region); pitch classes dominated by D, then B, C, G, A (mostly consonant, D-major/B-minor-like, **low confidence**, only 9 s).
- **Under narration, the stem is contaminated:** its strongest peaks (97, 194, 291, 388 Hz) form a harmonic series of ~97 Hz, which matches a deep male voice, so the 'C major, 82% bass energy' reading over 20-285 s is mostly narrator leakage and is **not** used.
- Whole-bed stereo side/mid ratio -5.3 dB (fairly wide), level range p10-p90 only ~7 dB (very steady), spectral flatness 0.075 (tonal, not noise-like).
- **Best guess (SPECULATIVE):** a quiet, slow, low-register ambient/underscore bed (synth pad, soft piano or strings-like sustained tones) with no prominent drums, hi-hats or lead melody, typical of science-explainer background music, plus occasional soft accents near scene changes (see Part D table). Not confirmed by listening. Song identity, BPM (the ~70 BPM estimate is low confidence), genre and instruments remain undetermined.
- To settle by ear: listen to `no_vocals.wav` at 294-303 s (cleanest), then 219-228 s (largest accents).
