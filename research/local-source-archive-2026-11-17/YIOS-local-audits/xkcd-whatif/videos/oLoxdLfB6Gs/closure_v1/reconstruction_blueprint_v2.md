# Reconstruction blueprint v2 — oLoxdLfB6Gs (closure v1; rv1 blueprint unchanged)
Use A = internal evidence-matched test only (source art, script, voice, names and branding are not reusable). Use B = ORIGINAL transfer: new subject and drawings, PROMPT_PACK_v2 locks and original branding; never the source logo, title lockup, creator name or recurring characters.
Global: 1080x1920, 24 fps CFR, 1096 f. Near-white canvas with optional blue speckled sky gradient; black monoline; story colour: yellow sun/light beams, blue scatter arrows, red direct-light arrows, verdigris green and copper brown statues; one DARK_FIELD space state with colour Earth.

| State | Frames | Enter (event @frame, length) | Image prompt (rv1 description verified on native/half-scale view; corrections applied) |
|---|---|---|---|
| VS001 | 0–3 | first frame | White canvas; black-ink outline sun with rays upper-left; black stick figure (round head, no face) lower-right. Nothing else. |
| VS002 | 24–63 | WRITE_ON_CHART @f4, 20 f | Sun upper-left; complete chart lower-left with purple decaying curve titled 'RAYLEIGH SCATTERING'; stick figure lower-right; white background. |
| VS003 | 70–97 | FADE_IN_SKY_GRADIENT @f64, 6 f | Blue gradient sky background; sun with yellow fill and orange glow upper-left; 'WHY IS THE SKY BLUE?' right of sun; Rayleigh chart lower-left; stick figure lower-right. |
| VS004 | 99–127 | POSE_SWAP @f98, 1 f | Same as G0005 but figure has one arm bent up toward the chart. |
| VS005 | 129–166 | SCENE_SWAP @f128, 1 f | White speckled canvas; sun upper-left with 'WHY IS THE SKY BLUE?'; black beam wedge diagonal down to figure; four purple scatter arrows with dashed bursts; figure lower-right; black diagonal line lower-right. |
| VS006 | 168–184 | POP_ON_OBJECT @f167, 1 f | As G0009 plus two parallel red arrows pointing down-right along the beam. |
| VS007 | 186–225 | POP_ON_GLOW @f185, 1 f | As G0011 plus yellow glow wedge lower-right behind figure. |
| VS008 | 227–270 | POP_ON_MULTIPLE_OBJECTS @f226, 1 f | Dense ray diagram: sun upper-left; black beams; red arrows (top, down-right, left-down); purple scatter arrows converging on yellow-tinted head of figure lower-right; yellow glow patches; title 'WHY IS THE SKY BLUE?' under top red arrow. |
| VS009 | 272–331 | POSE_SWAP @f271, 1 f | Same ray diagram as G0015; figure now with both arms up in shrug. |
| VS010 | 333–401 | SCENE_SWAP @f332, 1 f | Black space; Earth lower-centre; white helmeted stick figure upper-left; white label 'AIR' with arrow to Earth rim. |
| VS011 | 422–439 | WRITE_ON_TYPE_LABELS @f402, 20 f | Black space; Earth; helmeted figure upper-left; five white labels around Earth: RAYLEIGH SCATTERING, SOLAR BLACKBODY SPECTRUM, RELATIVE COLOR, TRICHROMATIC VISUAL SYSTEM, PLANCKIAN LOCUS. |
| VS012 | 441–511 | POSE_SWAP @f440, 1 f | Same as G0021 with space figure's arm raised. |
| VS013 | 513–524 | SCENE_SWAP @f512, 1 f | White canvas; cropped stick figure upper-left with speech line and 'WHY IS THE STATUE OF LIBERTY GREEN?'; empty below. |
| VS014 | 540–621 | POP_ON_OBJECT_THEN_COLOR_FILL @f525, 15 f | Statue of Liberty, verdigris green fill, lower right (drawn on stroke by stroke then painted top-down f525–539) |
| VS015 | 628–635 | WRITE_ON_TYPE @f622, 6 f | Green statue lower-right with label 'COPPER' + right arrow at its left; title upper-left. |
| VS016 | 642–666 | FADE_IN_OBJECTS @f636, 6 f | Brown-red statue left, green statue right, label '<-COPPER->' between; brown-red circle labelled 'Cu' on a string above left statue. |
| VS017 | 673–689 | FADE_IN_OBJECTS @f667, 6 f | Cu brown circle -> arrow with +O2 +CO2 +H2O +SO3 -> teal-green circle 'Cu2CO3(OH)2' above the two statues; title upper-left. |
| VS018 | 696–836 | FADE_IN_FOOTNOTE @f690, 6 f | Same reaction diagram with asterisk and footnote; long hold ~5.8 s. |
| VS019 | 838–943 | POP_ON_REPLACE_CHART @f837, 1 f | Cu / Cu2CO3(OH)2 absorption chart above the two statues; title and cropped figure upper-left. |
| VS020 | 945–984 | SCENE_SWAP @f944, 1 f | White canvas; single stick figure mid-right with one hand raised; nothing else. |
| VS021 | 991–1039 | FADE_IN_TEXT_AND_SKY @f985, 6 f | Faint blue speckles; two-line black text 'THE SKY IS BLUE BECAUSE THE SKY IS MADE OF AIR,' top; stick figure lower-centre. |
| VS022 | 1046–1095 | FADE_IN_TEXT_AND_SKY @f1040, 6 f | Blue gradient (deep at top, white at bottom) with speckles; three-line text 'THE SKY IS BLUE BECAUSE / THE SKY IS MADE OF AIR, / AND AIR IS BLUE.'; stick figure lower-centre with one hand raised. |

Motion: Write-ons: chart axes/curve/title f4–23, typed labels f402–421, COPPER f622–627; stroke draw-on + top-down paint fill of the statue f525–539; six linear 6-f cross-fades (sky, statue/copper, reaction, footnote, closing text lines). No camera moves.
Continuity: figure stays lower right through sky states; sun and question text fixed; statue drawing duplicated and recoloured (copper vs green); closing text builds line by line.
QA: (1) use A frame compare per state at native res; (2) every onset within ±1 frame of the ledger; (3) pops change on exactly 1 frame, multi-frame events match the measured curve (activity_curves.csv); (4) holds still (<0.1% changed px excluding grain); (5) all text exactly as transcribed in CLOSURE.md and legible at 320 px width; (6) use B originality check.
Not done: per-video render test (not required by contract v1).
