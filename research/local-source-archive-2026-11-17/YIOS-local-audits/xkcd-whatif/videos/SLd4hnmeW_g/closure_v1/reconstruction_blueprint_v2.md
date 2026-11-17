# Reconstruction blueprint v2 — SLd4hnmeW_g (closure v1; rv1 blueprint unchanged)
Use A = internal evidence-matched test only (source art, script, voice, names and branding are not reusable). Use B = ORIGINAL transfer: new subject and drawings, PROMPT_PACK_v2 locks and original branding; never the source logo, title lockup, creator name or recurring characters.
Global: 1080x1920, 24 fps CFR, 1139 f. Near-white LINE_ART canvas; seated desk figure lower half in most states; light-grey rounded question card with round Q badge at top (typeset serif question + sans attribution); cloud thought bubble; red only for the thermometer; full-frame grey TV-static as transition.

| State | Frames | Enter (event @frame, length) | Image prompt (rv1 description verified on native/half-scale view; corrections applied) |
|---|---|---|---|
| VS001 | 0–25 | first frame | Off-white canvas; grey rounded question card upper with Q icon and text 'Would it be possible to get your teeth to such a cold temperature that they would shatter upon drinking a hot cup of coffee?' and '- Shelby'. Lower-left: black-ink stick figure seated at desk with monitor holding a mug. Middle empty. |
| VS002 | 27–55 | POP_ON_OBJECT @f26, 1 f | Card; thought bubble with intact row of teeth; seated figure with mug. No thermometer. |
| VS003 | 57–63 | POP_ON_OBJECT @f56, 1 f | Bubble with thermometer (red mercury) at left and intact teeth; figure with mug. |
| VS004 | 78–91 | WRITE_ON_LINE @f64, 14 f | Thermometer with short red mercury column near bulb; intact teeth; figure with mug. |
| VS005 | 93–107 | STATE_SWAP_DAMAGE @f92, 1 f | Shattered teeth in bubble; thermometer; figure with mug. |
| VS006 | 109–153 | POP_ON_OBJECT @f108, 1 f | Bubble: thermometer left, shattered teeth middle, steaming mug right. Figure still holds mug. |
| VS007 | 155–212 | POSE_SWAP @f154, 1 f | Same as G0012 final: figure head down, small mug flying at lower-left, bubble with thermometer, shattered teeth and tilted steaming mug. |
| VS008 | 228–235 | NOISE_TRANSITION_TO_BLANK @f213, 15 f | Blank canvas with only desk, monitor and seated figure lower-left; encoder artifact frames flagged. |
| VS009 | 237–291 | POP_ON_OBJECT_AND_LABEL @f236, 1 f | Hat figure with hand mirror and speech text 'HOW MANY MIRRORS REFLECTING (SUN)LIGHT WOULD IT TAKE TO KILL, OR AT LEAST, INJURE SOMEONE?'; seated figure at desk. |
| VS010 | 293–312 | SCENE_SWAP @f292, 1 f | Card for Jeff upper; empty middle; seated figure lower-left. |
| VS011 | 314–357 | POP_ON_OBJECT @f313, 1 f | Bubble with machine apparatus left and two tiny figures right; Jeff card; seated figure. |
| VS012 | 359–415 | POP_ON_OBJECT @f358, 1 f | Bubble with machine, glowing star with rays, two tiny figures at right. |
| VS013 | 417–457 | SCENE_SWAP_WITHIN_BUBBLE @f416, 1 f | Bubble with single large standing stick figure at left; otherwise empty. |
| VS014 | 459–493 | POP_ON_LABEL @f458, 1 f | Large figure with '...MAYBE' speech in bubble. |
| VS015 | 495–506 | SCENE_SWAP_WITHIN_BUBBLE @f494, 1 f | Figure holding 'SUN OBLITERATOR' device in bubble; Jeff card; desk figure. |
| VS016 | 523–535 | NOISE_TRANSITION_SCENE_SWAP @f507, 16 f | Tomasz card upper; empty middle; seated desk figure lower-left; encoder artifact frames at start. |
| VS017 | 537–583 | POP_ON_OBJECT @f536, 1 f | Bubble with detailed dormant volcano; Tomasz card; seated figure. |
| VS018 | 585–652 | POP_ON_OBJECT @f584, 1 f | Volcano with bomb falling above summit. |
| VS019 | 654–656 | STATE_SWAP_DAMAGE @f653, 1 f | Volcano erupting with scattered debris specks; short 3-frame hold. |
| VS020 | 658–674 | STATE_SWAP_DAMAGE @f657, 1 f | Volcano with large mushroom cloud in bubble; Tomasz card; seated figure. |
| VS021 | 691–704 | NOISE_TRANSITION_SCENE_SWAP @f675, 16 f | AJ card upper; empty middle; seated figure; encoder artifact frames at start. |
| VS022 | 706–717 | POP_ON_OBJECT @f705, 1 f | Bubble with Chernobyl site and radiation sign. |
| VS023 | 719–804 | POP_ON_LABEL @f718, 1 f | Chernobyl with 'ANTIMATTER' label and arrow; long hold. |
| VS024 | 806–832 | STATE_SWAP_DAMAGE @f805, 1 f | Explosion/destruction drawing in bubble; trefoil sign tilted at left. |
| VS025 | 834–839 | SCENE_SWAP @f833, 1 f | Certificate 'AJ' with trefoil and rosette; figure with raised hand. |
| VS026 | 841–924 | WRITE_ON_TYPE @f840, 1 f | Certificate `AJ & TOMASZ` with radiation sign, bomb icon and rosette (same position as VS027) |
| VS027 | 926–976 | TEXT_ADD_WITH_REPOSITION @f925, 1 f | VS026 + `FOR GOD'S SAKE, WHAT WERE YOU THINKING?!` (THINKING underlined); certificate not moved |
| VS028 | 991–1005 | NOISE_TRANSITION_SCENE_SWAP @f977, 14 f | Karl card upper; empty middle; seated figure. |
| VS029 | 1007–1078 | POP_ON_OBJECT @f1006, 1 f | Crying figure in puddle in bubble. |
| VS030 | 1080–1099 | SCENE_SWAP @f1079, 1 f | Karl card; '...KARL' speech above seated figure. |
| VS031 | 1101–1133 | WRITE_ON_TYPE @f1100, 1 f | Karl card; speech '...KARL, IS EVERYTHING OK?'; seated figure; brighter white card background. |

Motion: Mostly 1-frame pops. Thermometer column falls steadily over 14 f (f64–77). Four question changes use 5-f full-frame TV static, new card complete on the 6th frame (encoder recovery afterwards is not animation). Video ends on 5 f of static.
Continuity: desk figure, desk and chair fixed in every desk state; question card fixed at top until the next static transition; thought-bubble content builds in place per question.
QA: (1) use A frame compare per state at native res; (2) every onset within ±1 frame of the ledger; (3) pops change on exactly 1 frame, multi-frame events match the measured curve (activity_curves.csv); (4) holds still (<0.1% changed px excluding grain); (5) all text exactly as transcribed in CLOSURE.md and legible at 320 px width; (6) use B originality check.
Not done: per-video render test (not required by contract v1).
