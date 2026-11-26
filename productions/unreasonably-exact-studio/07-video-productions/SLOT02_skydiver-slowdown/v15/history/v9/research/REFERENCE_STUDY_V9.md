# Reference Study V9: Skydiver Slows Down Without a Parachute

Format: 9:16, 1080x1920. Model: fixed-posture drag, falling from 10 km into denser air.
Style target: thin-line illustration with a pale sky and a few accent colours, informed by xkcd What If.
**We learn general principles only. We do not copy characters, frames, panels, title cards or end cards.**

Sources studied:
1. `HumanCraft_MASTER_Animation_Director_V4.md` (1,519 lines / 128,554 bytes). Read in full, lines 1 to 1519.
2. Eight xkcd What If MP4s from `~/Documents/YIOS-Media-Library/xkcd Channel/`. I made contact sheets, 4-frame motion strips, cut detection, held-frame counts and loudness measurements for them. The image files are in `xkcd_sheets/`.

---

## Part 1: Rules extracted from HumanCraft V4

Each rule gives its section in brackets.

### 1A. Character animation: secondary motion, follow-through, holds, eye-led reactions
1. Every movement needs a *subject → cause → intention → start state → path → timing/spacing → end state*. If a movement has no purpose, cut it. [Part II §0 "Universal motion contract"; Part I §2C "Motion contract"]
2. Before animating, record a motion contract for every significant move: initial pose, final pose, path, velocity/spacing, pivot and hierarchy, secondary overlap, camera relationship, hold, and proof criterion. [§2C]
3. Follow-through and overlap: secondary parts (limbs, clothing, hair) offset according to inertia and do not start or stop on the same frame. Check that the lag reads as physical and not random. [§3 table, "Follow through & overlap"]
4. Clothing and hair react to acceleration or wind. They should not wave continuously. [Part II §7 "Rigged-character checklist"; §12 table "Hair, clothing, fog, dust always move"]
5. Cloth flutter must come from movement or wind, never from an independent sine wave. Hair and fabric pieces must not all move in sync. [§17 D #72, #73]
6. Secondary action supports the primary action without competing with it. Test this by muting the secondary motion and comparing clarity. [§3 "Secondary action"]
7. Eye-led reactions: gaze and reach come before a grasp. Eyes, head and hands follow the action with believable offsets. For every action, record the *acting intention*: what does the character think, see or react to? [§4.2 items 1 and 7]
8. Every facial expression change needs a clear emotional reason. Avoid identity drift. [§7 rigged checklist; §17 D #70]
9. Intentional holds are allowed and are often better than motion: "a still face can be better than continuous kinetic noise." [§0 "Non-negotiable creative rules"]
10. A static hold can be professionally directed. It does not need to pass an "everything moves" test. [§4.5]
11. Anticipation always comes before the main move, and "a graphic holds briefly before an important reveal." [§7 "Motion principles"; §3]
12. Different things move differently. A body, a sleeve, an arrow, a cloud and the camera each get their own curve. Never share one generic ease. [§0; §12 table "Same easing on camera, person, text and particles"]
13. "Motion feels floaty despite looking smooth": fix this by tightening acceleration and adding a hold, impact or settle. [§12 table]
14. The anti-robotic checklist flags identical easing, perfect symmetrical movement, sliding cutouts, missing reaction or anticipation, detached shadows and fake hand-drawn wobble. [§4.4]
15. Line of action: avoid lifeless bilateral symmetry in poses. [§4.2 item 2]
16. Keep the design on model. The same face, height, outline and garment must persist through every shot. [§4.2 item 8; §12 "Characters/objects subtly morph"]
17. Do not build hidden rig complexity for characters that only appear tiny and far away. [§4.2]
18. Exaggerate only when the factual or physical meaning stays defensible. [§7; §3 "Exaggeration"]
19. Use loops and cycles only for subtle idles. Key gestures must not visibly repeat too often. [§17 C #53]

### 1B. Camera motivation
20. Ask why the camera moves. The valid motivations are: approach a detail, reveal scale, track a subject, reveal something behind an occluder, go from macro to micro, or reframe for a change of emphasis. [§7 "Camera direction checklist"]
21. "Do not oscillate or zoom continuously by default." Match screen direction and eyeline at cuts. [§7]
22. A purposeful pull-back is the first choice when the viewer must comprehend scale, with accurate labels and spatial comparison. Reject a large false arrow or wobble that implies wrong facts. [§6 "Shot selection decision tree", "Comprehend scale"]
23. For suspense or absence, use a composed environment, a quiet reaction and a motivated hold. Reject constant jitter or zoom. [§6]
24. A crane or jib move is for vertical discovery or a change of scale. Avoid it when the move reveals no new information. [§17 A #07]
25. Pan and tilt are for tracking action or surveying a place. Avoid endless screen drift. [§17 A #08]
26. "Every shot has a slow zoom" is a template symptom. Remove unmotivated moves and use holds, framing changes and action cuts. [§12 table]
27. Keep screen-direction continuity: perceived travel direction stays the same across a sequence. [§17 A #18; §8 "Editorial continuity gates"]
28. Use camera shake only as a restrained local response to a physical impact. [§17 C #60; §10 "Avoid visual nausea"]
29. A beautifully composed still image held at the right moment reads as more professional than an unmotivated fly-through. [§7 "Motion can be understated"]

### 1C. Staging and composition (applied to vertical)
30. Staging means one primary action, with clear contrast and eyeline. Pass the thumbnail and one-view comprehension test. [§3 "Staging"]
31. Decide where the eye goes first, second and third before animating. [§0 Q3; §5 step 2 "Viewer action"]
32. Fix composition, scale, character shape, palette and focal hierarchy *before* any animation. [§0 "Design before animation"]
33. The rubric target is a clear focal hierarchy, quiet negative space and readable silhouettes. [§2F rubric "Composition & focus"]
34. Text and labels must stay visually separate from the subject and must never sit behind complex action. [§8 continuity gates; §10]
35. Visual-density rhythm: alternate high energy (hook, contradiction, payoff), medium energy (one evolving diagram or camera reveal) and low energy (quiet hold or readable infographic). Avoid fixed formulas like "new shot every 3 s". [§5 "Visual-density rhythm"]
36. Plan 2 to 5 hero moments and planned restraint moments in a vision card. [§2A]
37. Use one recurring visual token with a meaningful role whenever it reappears, and bring it back as the final callback. [Part IV §20 "Recurring visual token"]

### 1D. Scientific diagram construction (progressive reveal)
38. "Understand a mechanism" calls for real diagram *state transitions*. Reject icons that only label instead of explaining. [§6]
39. "Learn a sequence" calls for stepwise construction with one cause per step, labels and holds. Reject too many simultaneous moving parts. [§6]
40. Recipe for a science diagram: the comparison builds stepwise, the key value reveals *when it is spoken*, a hold follows for comprehension, then a clean cut to the outcome. Reject exaggerated wobble, unsupported numbers and "enormous effect arrows that imply false physical scale." [§13C]
41. Scientific arrows show direction, velocity and comparison. Avoid exaggerated effects without a scale annotation. [§17 E #91]
42. Animate the *cause-and-effect mechanism*, not just the entrance of labels. [§4.1 "Vector / shape-based"]
43. Use a staged reveal and hold: reveal part, hold the thought, resolve. [§17 C #56]
44. Use trim paths and write-on strokes for plotting vectors, routes and underlines, always with narrative direction. [§17 E #85]
45. A number counter is for a change in measured quantities. Avoid counting that creates false accuracy. [§17 E #93]
46. Label magnified or stylised scale "EXAGGERATED / NOT TO SCALE". [§10 "Truthful visualization"; Part IV §22]
47. An infographic layout morph is for one diagram reconfiguring into a related one, never as decoration. [§17 E #94]
48. Do not present an illustrative curve as a measured prediction unless a sourced calculation backs it. Keep a claim ledger. [Part IV §22]
49. "Presentation-deck animation" (everything fades, slides or pops in) is a defect. Replace it with draw, unveil, track, assemble or compare. [§12 table]

### 1E. Typography on mobile
50. Test for phone size. The recipe proof is "readable diagram at phone size". [§13C; Part III E "phone-size / final-size frame sample"]
51. Target contrast of at least 4.5:1 for normal text and 3:1 for large text. [§10 "Legibility"]
52. Show one focal idea at a time. Separate captions from designed labels and reduce density. [§12 table "Constant text/captions fill frame"]
53. Kinetic type is for emphasised nouns, contrasts and key words timed to speech. Do not animate every spoken word. [§17 E #77; §9]
54. Use editable word or phrase layers with a real hierarchy: key words larger, connectors smaller. Stagger to spoken cadence. The final layout must stay readable long enough before it exits. [§9 items 1, 2, 3, 9]
55. A caption must not disappear before viewers can read it, and must not obscure faces, actions or diagrams. [§4 "Caption design rules"]
56. Do not use high-frequency type flicker or rapid flashes. [§10 "Avoid visual nausea"]

### 1F. Sound design
57. Every sound effect needs a visible cause or a deliberate editorial accent. "Avoid a loud whoosh for every zoom/text layer." [Part II §10]
58. "Silence/room tone can create drama; don't fill every gap with sound." Use silence as an effect, to let a thought settle. [§10; §17 F #110]
59. Arrange ducking by *listening*. Keep narration intelligible. Distinguish atmospheric ambience from speech and from signal events. [Part I §7]
60. Ambient room tone gives spatial atmosphere and bridges scene transitions. It must never swamp dialogue. J and L cuts let audio lead or trail a picture cut. [§17 F #108, #109; §8]
61. Sound-design sync aligns transients with meaningful visual action. "Every letter accompanied by pop" is a defect. [§17 F #107; §9 item 8]
62. When joining chapters, check for discontinuous ambience and audio gaps. [§10]
(The doc gives no numeric ducking dB or LUFS target. Those numbers come from the measurements in Part 2.)

### 1G. Editing rhythm
63. Transitions are relationships between ideas. A hard cut suits a clean fact, a reversal or a new viewpoint. A match cut bridges a related shape. A movement handoff continues a direction. [§8]
64. Do not default to flash, glitch, shake, random zoom, spin, RGB split, bounce, glow or liquid wipe. Pick *one* signature transition. [§8; §12 "Big speed-ramp/glitch on every cut"]
65. Cuts hit narration meaning and deliberate punctuation. They should not be evenly spaced. [§8 continuity gates]
66. Use a freeze frame or hold for teaching and annotation, never to cover missing animation. [§8; §17 C #49]
67. Design the ending to resolve the opening question, with a visual or sonic callback. [§12 table "Final feels unfinished"]
68. Review process: render a moving proof, list the three worst defects with timecode and root cause, fix them in source, re-render and compare. Run the editorial review and the animation review as separate passes. [§2D, §2E; §12 "Mandatory critique/revision loop"]

---

## Part 2: xkcd What If visual reference study (observed)

Method: for each video I made a contact sheet of 24 evenly spaced frames. Tile *k* is at about k x interval (interval = duration/24). I also made 4-frame strips at 0.25 s spacing (fps=4) around a moving moment, ran scene-cut detection (`select=gt(scene,0.25)`), counted changed frames with `mpdecimate`, and measured loudness with `ebur128`. Timestamps are approximate (±half an interval) unless they come from a motion strip. **OBSERVED** means seen in an extracted frame. **INFERRED** is marked as such.

| # | Title | Format | Dur | Sheet interval | Sheet / strips |
|---|---|---|---|---|---|
| v1 | What if you floated upwards 1 ft every second? | 1920x1080 | 172.9 s | 7.2 s | `v1_sheet.jpg`, `v1_motion_16/50/79/100.jpg`, `v1_climb_30to37.jpg` |
| v2 | Why is the sky blue? | **1080x1920** | 45.7 s | 1.9 s | `v2_sheet.jpg`, `v2_motion_10/15.jpg` |
| v3 | What if everyone jumped at once? | 1920x1080 | 231.7 s | 9.7 s | `v3_sheet.jpg`, `v3_motion_79.jpg` |
| v4 | How fast could a human accelerate (while staying alive)? | **1080x1920** | 83.3 s | 3.5 s | `v4_sheet.jpg`, `v4_motion_62.jpg` |
| v5 | What if you made a jetpack using rifles? | 1920x1080 | 277.8 s | 11.6 s | `v5_sheet.jpg`, `v5_motion_220.jpg` |
| v6 | What if we built a billion-story building? | **1080x1920** | 108.2 s | 4.5 s | `v6_sheet.jpg`, `v6_motion_10.jpg` |
| v7 | Can you drive west to lengthen the sunset? | 1920x1080 | 165.5 s | 6.9 s | `v7_sheet.jpg`, `v7_motion_66.jpg` |
| v8 | What if Earth grew 1cm every second? | 1920x1080 | 315.7 s | 13.2 s | `v8_sheet.jpg`, `v8_motion_26.jpg` |

### 2.1 How altitude and scale are established
- **v1 is the closest analogue: one person rising through the atmosphere.** A persistent text block sits top-left: elapsed time plus altitude, and later pressure. Seen at ~22 s "30 SECONDS / 30 FEET", ~29–36 s "90 SECONDS / 90 FEET", ~79 s "3 HOURS / ~3.3 km / ~0.7 ATM", and ~108 s "7.25 HOURS / 8 km / EFFECTIVE O₂: 7% (SEA LEVEL: 21%)". The block gains lines as new quantities become relevant. It is plain small caps with no box.
- **Each altitude band gets a familiar benchmark object at that height.** In v1: an elevator at ~14 s, a fire-truck ladder and a tree line at 90 ft (~29 s), office rooftops with birds at 600 ft (~36 s), the Empire State Building at 1500 ft (~36 s), a cumulus cloud at 1 hour (~50 s), a helicopter at 3.3 km (~72–79 s), and a jagged mountain range at the bottom labelled "— DEATH ZONE —" at 8 km (~101–122 s). At ~129 s the person is above a single summit with climbers on it.
- **Dimension line as a label.** In v1 at 30–31 s (`v1_climb_30to37.jpg`), a horizontal "—— 90 FEET ——" rule is *written on* beside the figure about 1 s after the shot settles. It appears; it does not fly in.
- **The ground leaves the frame as altitude grows.** At low bands the ground line sits at the bottom with solid black tree silhouettes (v1 ~29 s). By ~57–65 s (1–2 h) the frame is empty off-white with faint grey horizontal streaks (air/wind) and a few grey blobs (birds or debris). The figure is the only dark mark.
- **Earth at height (v6, vertical).** The flat ground line (~4.5–13 s) becomes a curved arc with thin labelled bands "EARTH / AIR / SPACE" (~22–31 s). At ~36–45 s it becomes a small circle at the bottom with the tower as a hairline. Scale is shown by *pulling back* and redrawing the planet smaller, with leader-arrow labels ("MOUNTAINS", "AIRPLANES", "METEORS", "SPACE JUNK"). Airplanes appear as tiny glyphs with labels, not detailed drawings.
- **Counter plus goal.** v6 keeps "FLOORS 100 / GOAL: 1,000,000,000" fixed at top (~4.5 s onward). Only the number changes between beats (100 → 10,000 → 1,000,000 → 100,000,000).
- **Mass comparison as two stacked bands.** v3 at ~38–48 s shows a row of humans above a grey slab: "ALL HUMANS ~500,000,000,000 KG" over "THE EARTH ~6,000,…,000 KG". A red dashed line marks "↑0.5m". The numbers are written out in full, so their length carries the scale.

### 2.2 How stick figures move (what moves, and how much)
- **Mostly held.** Measured changed frames with mpdecimate (480 px, default-scale thresholds): v6 85 of 2596 frames (3%), v2 109 of 1096 (10%), v4 637 of 1997 (32%; a centrifuge and a car on a track are spinning), v1 2712 of 4148 (65%; continuous rising and scrolling). *Interpretation:* in diagram-led shorts, about 90% of frames are holds or near-holds. Motion is concentrated on the one thing that matters.
- **v1 at 50.0–50.75 s (swimming pool):** the two swimmers change arm and leg poses each 0.25 s and the splash spray redraws. The lifeguard holding binoculars shifts only slightly. The torso stays nearly fixed while the limbs carry the action.
- **v1 at 100–100.75 s (ranger at a board):** almost nothing moves apart from a small hand or arm gesture (a few px). The diagram on the board is fully static.
- **v1 at 79–80.5 s (helicopter at 3.3 km):** a crew member's arm dangles a jacket out of the door over the 4 frames. The rising figure (about 20 px tall in a 480 px frame, roughly 4% of frame height) is tiny and slightly jittery. The scene is mostly static.
- **v3 at 79–79.75 s (five faces / crowd):** small curved "motion arcs" are drawn above heads to show bobbing. The heads shift a few px, staggered (not in unison), and the bodies stay rigid stick lines.
- **v5 at 220–220.75 s (police stop):** the speaker's head tilts slightly and the police light bar's ray lines redraw. Everything else is held while the speech bubble stays up.
- **v8 at 26–26.75 s ("T = 2 SECONDS", lone figure on a ground line):** practically motionless. The head shifts 1–2 px. A standing figure is allowed to just stand.
- **v2 at 15–15.75 s (vertical):** a white-line figure floats in space next to Earth. Its legs sway slightly and the Earth texture rotates slowly. The motion is gentle and continuous.
- Characters are drawn with circle heads, single-line limbs and only a few identity marks (hair, hat). Faces have no features, so **head tilt and arm gesture carry the reactions.**

### 2.3 How diagrams, arrows and labels are introduced
- **Additive build on a persistent canvas.** v2 at 5.7 → 9.5 → 11.4 s (vertical): the sun with a "WHY IS THE SKY BLUE?" title. First two black ray lines with small purple scatter arrows. Then red direct-light arrows. Then pale yellow light cones fill. Each layer *adds* to the frame and nothing is cleared. The v2 strip at 10–10.75 s shows the full diagram held almost static.
- **v2 at 21–38 s:** a single statue, then a second copy recoloured. Then "Cu" and a carbonate formula appear in coloured circles with "+O₂ +CO₂ +H₂O" arrows. Then an absorbance chart replaces the circles in the same position. This is a layout morph in place.
- **Strike-through updates.** v4 at ~73–83 s (vertical): the track diagram text "LIMIT: 4 Gs ~1:45:00" gets crossed out and replaced ("6 Gs ~1:20:00", "10 Gs ~1:00:00"). Old values stay visible, struck through, so the revision history is on screen.
- **Directional arrow plus notes.** v4 at ~55–66 s: a figure with four red arrows (UPWARD / FORWARD / BACKWARD / DOWNWARD). Short underlined headers appear first, then 3–4 tiny bullet notes under each.
- **Leader arrows** (curved, hand-drawn, short) attach every label to its object: v6 "100 SKYSCRAPERS ↘", "MOUNTAINS →", and v7 "SUNSET ZONE ↙" at ~41–55 s.
- **Charts are minimal.** v1 at ~86 s: survival-time chart with labelled bands. v4 at ~35 s: a NASA tolerance chart. v8 at ~290 s: an oxygen toxicity chart. Each has 2 axes, few ticks and labelled regions instead of legends. Each chart is shown on screen for one beat and then held.
- **"NOT TO SCALE" annotation** in tiny type in the corner: v1 at ~137–151 s (space scenes).

### 2.4 Colour usage
- The base is off-white or very light grey (v4 and v6 backgrounds are a light grey, not pure white) with black line art.
- **One accent, mostly red.** Red is used for the key force or limit arrows (v4 "10 Gs", the 2:05:00 result, the directional arrows), the "↑0.5m" in v3, and the "1/10^n TO THE MOON" dashed orbit in v6.
- **Pale sky gradient used sparingly.** v2 at ~1.9–3.8 s and ~44 s: a soft blue fades down from the top to white, with text "THE SKY IS BLUE BECAUSE THE SKY IS MADE OF AIR, AND AIR IS BLUE". Blue appears only when the subject *is* sky.
- **Mode switches mark scale jumps.** A black background marks space (v1 ~137 s, v2 ~13–19 s, v6 ~67 s). A dark grey background marks the globe close-up (v7 ~41–55 s).
- **Full-colour painted image only at the emotional payoff.** v7 at ~145–158 s shows a red-orange painted sunset with two silhouettes, after about 140 s of mostly greyscale.
- Solid black silhouettes (v1 trees, v8 city) act as ground mass, so line art reads against them.

### 2.5 Amount of text on screen
- Usually 1–2 labels of 1–3 words plus one persistent counter block. Longer text appears only on quote or "fun fact" cards (v5 at ~255 s: a paragraph card) and the question card.
- In verticals, text sits in the top third or as short labels next to objects. The question title is a single line (v2: "WHY IS THE SKY BLUE?" top-right of the sun).
- All in a hand-lettered uppercase font. Speech bubbles hold at most about 8 words (v5 "DO YOU KNOW WHY I PULLED YOU OVER?").

### 2.6 Camera moves, cuts and pacing
- **Few hard cuts.** Detected cuts at scene threshold 0.25: v4 had 0 in 83 s, v2 had 2 in 46 s, v6 had 3 in 108 s, v5 had 4 in 278 s, and v1 had 7 in 173 s. The more cut-heavy videos were v3 (21 in 232 s, about 11 s/cut) and v8 (25 in 316 s, about 12.6 s/cut). Caveat: cuts from white to white may not reach the threshold, so these are lower bounds. Still, the visual change is mostly *on a persistent canvas* (draw, erase, pan) rather than by cutting.
- **Whip pull-back with motion blur.** v6 at 10.0 s: frame 1 is a heavily motion-blurred close shot (tower, cloud, ground). 0.25 s later it has settled into a wide shot with new labels and the counter changed from 100 to 10,000. One fast move followed by a long hold. (The first cut is detected at 5.1 s.)
- **Altitude bands as cut-separated tableaux.** v1 at ~36 s: "90 SECONDS" cuts straight to "600 SECONDS / 600 FEET" with rooftops. Each band holds about 7–20 s with tiny motion inside.
- **Slow sweeps.** v7 at ~97–117 s: the day/night terminator slides across a static map. In the v7 strip at 66 s, the globe shading changes subtly while the labels and arrows stay locked.
- **Pacing:** the persistent counter or title stays on screen across many beats while only the numbers and benchmark objects change.

### 2.7 Sound (measured only; I did not listen)
- Integrated loudness: v2 −16.4 LUFS, v4 −16.3 LUFS, v6 −15.8 LUFS, v1 −16.3 LUFS.
- Loudness range (LRA): 2.0–3.1 LU. The mix is very dense and compressed, which suggests a narration-dominant bed (INFERRED).
- Silences longer than 0.4 s below −40 dB: v2 had 1, v4 had 0, v6 had 0, v1 had 2. Something is almost always audible, so there are essentially no dead-air gaps.
- I cannot say whether the content is music, ambience or effects. Not inferred.

### 2.8 Do-not-copy list
The blackboard lecturer and pointer framing, the grey question card with the reader's name, the red "what if?" title card, the red end card with books, the hatted ranger character, the dynamite-holding girl, the specific Rhode Island/crowd jokes, and the specific helicopter, Empire State and death-zone sequence as a set. We take *principles*: counters, benchmarks, write-on labels, single accent and holds. We do not take those frames.

---

## Part 3: Directives for V9

1. **Canvas:** pale-sky gradient, light blue at the top fading to near-white at about 40% height, then off-white. Keep this for the whole fall. Black line art, stroke about 4–5 px at 1080 wide, round caps. No textures and no grain.
2. **Accent budget:** red only for the velocity or drag quantity (arrow, speed number, curve). One secondary accent (muted blue) only for air density. Nothing else is coloured. Allow one full-colour moment only at the payoff.
3. **Persistent altitude HUD**, top-left inside the safe zone: `ALTITUDE 10.0 km / SPEED 2xx km/h`, plus `AIR DENSITY 0.41 kg/m³` once density is introduced. Hand-lettered, about 44–52 px. Add lines only when they become relevant. Update numbers at beat points, not as a spinning counter. Every value must come from our drag model.
4. **One benchmark object per altitude band**, each with a short leader-arrow label: cruising airliner (about 10–11 km), Everest-height mountain silhouette (8.8 km), cloud deck, small plane or helicopter (about 3 km), tall building, then the ground. Show real heights in the HUD, not on the objects.
5. **Camera tracks the diver** at a fixed screen position (upper-middle third). The world scrolls *up* past the diver. Benchmarks enter from the bottom and exit at the top. The motivation is tracking a subject.
6. **Speed made visible as air streaks:** thin grey vertical streaks scroll upward. Their length and speed are mapped to the model's velocity, so the viewer *sees* the slowdown as the streaks shorten. This is the central visual metaphor and must be data-driven.
7. **Diver scale:** about 5–7% of frame height in wide or tracking shots, so the sky feels huge. Use a close-up only for the posture and drag explanation.
8. **Fixed posture means a fixed pose.** The body silhouette never changes (the model assumes it). Secondary motion is limited to small limb and clothing flutter whose amplitude scales with airspeed and visibly *calms* as the diver slows. Never use a sine-wave loop.
9. **Eye-led reactions:** at 2–3 beats the diver's head turns toward the HUD or the speed arrow just *before* the number updates (a lead of about 6–10 frames), then holds. No facial features are needed; head tilt carries the reaction.
10. **Hold most frames.** Aim for about 80–90% near-static frames in diagram beats. Hold 1.5–3 s after each key number is spoken.
11. **Force diagram by progressive reveal:** first gravity (a downward arrow, fixed length), hold. Then drag (a red upward arrow) grows as speed rises. Then, in the denser-air phase, the drag arrow gets *longer than* gravity, so the net force points up and the diver decelerates. Arrow lengths must keep their true ratios from the model. Write each arrow on with a stroke; do not pop or fade it.
12. **Terminal-velocity graph:** a minimal two-axis plot (speed against altitude) in the lower half. A dashed "terminal speed" line falls as density rises, and the diver's actual speed trace draws on behind it. Use labelled regions, not a legend, and at most 3 ticks per axis.
13. **Strike-through number revisions** when terminal speed drops (for example the old value crossed out, the new value written beside it). Keep the old value visible.
14. **"NOT TO SCALE"** in small type wherever we exaggerate curvature, streaks or arrow size.
15. **Earth at 10 km:** a very gentle horizon arc only in the opening establishing wide shot, with an "AIR" label band. Flatten it progressively as we descend. Do not show strong curvature without the "NOT TO SCALE" tag.
16. **Camera language:** open with an establishing wide (diver tiny beside an airliner at 10 km), then track during the fall, push in for the drag close-up, and pull back at the end to show the ground. Use one signature fast move at most (a blurred whip pull-back) at a scale jump. Never use a continuous drift or zoom.
17. **Cuts:** few. Change concepts on the persistent canvas (draw on, erase, scroll) and save hard cuts for concept boundaries or a reversal ("but the air gets thicker").
18. **Text density:** at most one label of 1–4 words plus the HUD on screen at once. Captions go in a separate system, kept out of the diagram zone.
19. **Vertical safe zones:** keep the HUD below the top 200 px. Keep key labels and graphs out of the bottom 380 px (platform UI) and the right 140 px. Body text must be at least 40 px and the HUD at least 44 px at 1080 wide, with 4.5:1 contrast against the gradient.
20. **Sound loudness:** master at about −16 LUFS integrated with a narrow LRA (about 3 LU or less), matching the measured reference. Keep near-continuous audio with no dead air longer than 0.4 s except one deliberate silence beat.
21. **Ambience layers:** a wind/air bed whose level and brightness are mapped to model airspeed, so it audibly *eases* as the diver slows. Add a faint high-altitude tone at 10 km and let low-altitude texture come in near the ground. Crossfade between them as continuous layers, with no hard swaps.
22. **Ducking:** duck the bed under narration by ear (set by listening, not by a fixed preset), so the voice stays intelligible.
23. **No repetitive whooshes.** No sound per label or arrow write-on. At most one whoosh, on the signature pull-back. Every other sound effect needs a visible cause (the airliner passing, the cloud punch-through).
24. **Recurring token:** the HUD speed number is the token. It opens the film, changes on screen at each beat, and closes as the callback ("still falling, but slower").
25. **Review loop:** render a 5–12 s moving proof of the slowdown beat, list the three worst defects with timecodes, fix them in source and re-render. Run the editorial review and the animation review as separate passes.
