# Chair stand safety Short — Stage A production pack

Status: design ready; timing and aspect ratio provisional. No Dr. Rehan source clip found in workspace. Do not edit CapCut until source and generated assets are present. Preserve original narration and project.

## Evidence used

Inspected `production_intelligence_brain/01_master_data` through `05_blueprints`, indexed all 56 forensic rebuild/prompt files across 14 videos, and examined representative per-video prompt content plus coffee/heart revision, audit, character master, and production pack. Canonical CSVs govern counts; prose documents supply implementation examples. The 56 files span 9,240 lines; this pass searched them for cut, camera, transparency, text, mask, opacity, keyframe, and I2V guidance. It did not manually verify every individual frame or instruction in every file.

- 200 shots: median 7.77 s overall. Portrait subset 72 shots: median 6.45 s; median 3 states and 2 motions per shot. Avoid forcing a cut for each sentence.
- 581 states: 522 labelled locked/static (89.8%). 146/200 shot entrances use cut-family wording. All 186 measured internal shot boundaries have 0 s gap. Default locked frame and hard cut.
- 438 motions: 230 state replacements; 144 last under 0.5 s. Motion starts usually during or between spoken words. `MASTER_AUDIO_VISUAL_SYNC.csv`: state changes median offset 37 ms from associated word start; motion starts median 33 ms. This does not prove all events occur exactly on word onset. Anchor this edit to meaningful spoken words, then refine by ear/frame.
- Corpus has no measured palette, typography, or line width. Thin black line art, off-white field, single muted-red warning mark, text in CapCut come from concrete forensic prompts and coffee/heart production pack, not aggregate measurement. Coffee test used 5 visuals, 20 states, 15 animations, zero I2V.
- No corpus medical chair-test precedent; chair/person design, speaker visibility, warning meaning and CTA are **NEW CREATIVE DECISIONS**. No clinical score thresholds appear.

## Semantic beat map

| Beat | Script anchor | Viewer must grasp |
|---|---|---|
| Safety hook | “Before… one safety rule” | Familiar test has safety condition. |
| Setup/timer | “start the counter…30 seconds” | Timer measures test window. |
| Repetition/count | “count…stand up…sit down” | One cycle means rise then return to seat. |
| Unassisted | “unassisted” | Person completes movement alone; no helper shown. |
| Unsafe/dizziness/ataxia | “unsafe…dizziness or ataxia” | Any named warning means stop, shown as generic unsteadiness only. |
| Stop | “don't do this test” | Test ends, no extra rep. |
| Result | “Once you have your number” | Personal count belongs to one person. |
| Universal comparison | “don't compare…universal number” | One person's score is not one shared cutoff for everyone. |
| Low concern | “score looks low” | Viewer may worry about result. |
| Non-diagnosis | “number alone doesn't diagnose you” | Score cannot directly become diagnosis. |
| Expert/CTA | “Dr. Rehan…full video on the channel” | Return to speaker, point to full explanation. |

## Consistency bible

Assume 9:16, 2160×3840; **VERIFY AGAINST SOURCE** before generation. Flat warm off-white `#F7F5F0`; black `#202020` fine-marker line, nominal 5 px at 2160 width; muted red `#B64D48` used only for stop/invalid link. No gradients, textures, shadows, perspective, photorealism, stock art, labels baked into generated images, or camera motion. CapCut makes all words, numerals, arrows, score glyphs, X/strike, captions. Keep center 80% width readable on phone; reserve lower 20% for captions. Locked orthographic side view for test action. One chair, one person, reused across scenes.

**Character master C01:** generic adult, neutral gender, average proportions; head oval, one short dark hair contour, no eyes/nose/mouth; plain light-blue short-sleeve shirt, dark charcoal trousers, simple dark shoes; thin black outline, flat fill; side profile facing right. Seated and standing PNGs must share identical head, clothing, limb thickness, body scale and foot baseline. Derive standing from approved seated master using same reference image/character sheet. Use hard pose replacement; no generated halfway pose. No likeness to Dr. Rehan. Chair C02: simple stable four-legged dining chair, side view facing left (seat/back fixed), dark outline, no wheels/arms/medical device. The person's sit/stand poses align to same chair footprint. Never imply testing while dizzy; warning replaces test action.

**Speaker:** source Dr. Rehan footage stays full frame for SH01 and SH07; SH02–SH06 are illustrated cutaways with original voice continuous. This balance is a **NEW CREATIVE DECISION**, pending actual source framing. If his face would be cropped by a 9:16 conversion, recrop manually without altering audio.

## Shot plan

Durations below are **ESTIMATED — REPLACE AFTER SOURCE VIDEO ANALYSIS**. Approximate 3.9 words/s, no exact timecodes. Word onset triggers are editorial targets; verify against audio waveform.

| Shot | Script words | Purpose | Visual concept | Base image | Separate assets | Type | Est. duration | Cut/reveal trigger |
|---|---|---|---|---|---|---|---|---|
| SH01 | “Before you try…shouldn't ignore” | Safety hook | Speaker with small chair/timer visual, then red caution interrupt | source video | C02, G01 | B+D | ~3.6 s | timer on “30-second”; warning on “safety rule” |
| SH02 | “So, start…sit down” | Procedure | Seated/standing/seated pose replacements; count increments | BG01 | C01A/B, C02, G02 | C+D | ~5.7 s | “counter”, “stand”, “sit” |
| SH03 | “However, if you feel unsafe, if you got dizziness or ataxia” | Warning signs | Person holds still beside chair; two small wobble arcs and caution icon | BG01 | C01A, C02, G01, G03 | B+D | ~3.4 s | cut “However”; arcs “unsafe”; warning “dizziness/ataxia” |
| SH04 | “then don't do this test” | Stop | Existing test diagram removed; large red stop mark over empty timer | BG01 | G01, G02 | C+D | ~1.6 s | “don't” |
| SH05 | “Once you have your number, don't compare that to universal number” | Personal score | One score card near character; duplicate blank score cards under 3 distinct people; shared equals link crossed out | BG01 | C01B, G04 | B+D | ~3.3 s | “your number”, “universal” |
| SH06 | “And even if your score looks low, that number alone doesn't diagnose you” | Non-diagnosis | score card, proposed diagnosis card, red slash through connecting arrow | BG01 | G04, G05 | B+D | ~3.7 s | “low”, “doesn't diagnose” |
| SH07 | “Dr. Rehan explains…full video on the channel” | Expert + CTA | Speaker returns; small score card retires; native full-video CTA | source video | G04 | B+D | ~3.5 s | “Dr. Rehan”; CTA on “full video” |

Total ~24.8 s **ESTIMATED**, excludes source pauses. No I2V: all meaning is pose/state/diagram change; continuous physical motion adds little and threatens consistency.

## Asset manifest

Generated PNGs only. All exports at 2160×3840 canvas so coordinates align; transparent items retain full-size canvas. Save with these names. Text stays in CapCut.

| ID / filename | Purpose | Alpha | Reuse / derivation | Text | Shots |
|---|---|---|---|---|---|
| BG01 `BG_01_offwhite.png` | Uniform full-frame field | opaque | all illustrated shots | none | 02–06 |
| C02 `CHAIR_01.png` | Fixed chair | transparent | same original all shots | none | 01–03 |
| C01A `PERSON_SEATED_01.png` | seated pose | transparent | character master | none | 02–03 |
| C01B `PERSON_STANDING_01.png` | standing pose | transparent | derive from C01A; same person | none | 02,05 |
| G01 `WARNING_TRIANGLE_01.png` | caution icon outline | transparent | repeat exactly | none | 01,03,04 |
| G02 `STOPWATCH_OUTLINE_01.png` | empty timer | transparent | repeat exactly | none | 01,02,04 |
| G03 `UNSTEADY_ARCS_01.png` | restrained wobble marks | transparent | one group | none | 03 |
| G04 `SCORE_CARD_EMPTY_01.png` | blank result plate | transparent | duplicate in editor | none | 05–07 |
| G05 `DIAGNOSIS_CARD_EMPTY_01.png` | blank second plate | transparent | separate from G04 | none | 06 |

No extra image needed for people in universal comparison: duplicate C01B as identical schematic figures; CapCut native text differentiates personal cards. No generated warning X, arrow, counter, CTA or number.

## Copy-paste image prompts and motion notes

Each prompt independent. Feed approved previous asset as reference where named. Generate PNG transparency, no matte, unless `BG01`.

### SH01 — speaker hook

**IMG001 / `CHAIR_01.png`** — transparent asset; used SH01–03. Prompt: “Create one simple side-view dining chair on a transparent 2160×3840 9:16 canvas. Place chair at x38–62%, y46–72%; seat horizontal; straight back on image right; four simple legs visibly stable. Thin 5 px slightly imperfect black fine-marker outlines, flat 2D orthographic view, no perspective, no fill except off-white seat. Preserve generous transparent space. No human, timer, captions, words, digits, symbols, medical equipment, wheels, arms, texture, gradient or shadow.” Consistency: C02 geometry remains pixel-identical in every shot. CapCut: overlay small near speaker only if no face overlap; otherwise reserve for SH02. Animation: **CAPCUT**, one-frame appearance on “chair stand test”; static thereafter.

**IMG002 / `STOPWATCH_OUTLINE_01.png`** — transparent asset; used SH01,02,04. Prompt: “Single clean outline of a simple analog stopwatch, centered x35–65%, y28–53% on transparent 2160×3840 vertical canvas; round face, small top button, no hands, tick marks, markings, numerals, letters, or display. Thin 5 px naturally uneven black marker line, flat frontal 2D; open center for editable CapCut text. No person, chair, colored fill, depth, shadow, glow, border, texture or extra icons.” Consistency: all uses duplicate same PNG. CapCut: add editable `30 s` centered; one-frame appear on “30-second”/“counter”, freeze at warning. Animation: **CAPCUT**, opacity 0→100 in one frame, no ticking hand.

**IMG003 / `WARNING_TRIANGLE_01.png`** — transparent asset; used SH01,03,04. Prompt: “One empty triangular caution-outline icon with rounded corners and a small vertical exclamation mark inside, centered on transparent 2160×3840 9:16 canvas at x39–61%, y34–50%. Uniform muted red #B64D48 line, roughly 8 px at full width, flat 2D, no fill or other color. No words, extra symbols, glow, drop shadow, perspective, paper texture, circles or decorative marks.” Consistency: exact same asset at all uses; red means safety interruption only. CapCut: scale 90→100 over 4 frames at “safety rule”; hold. Animation: **CAPCUT**.

### SH02 — procedure and count

**IMG004 / `BG_01_offwhite.png`** — background, used SH02–06. Prompt: “Uniform flat warm off-white #F7F5F0 filling exact 2160×3840 vertical 9:16 canvas. One color everywhere. No vignette, paper texture, gradient, border, objects, labels, shadows or pattern.” CapCut: locked full frame; reuse unchanged. Animation: **STATIC**.

**IMG005 / `PERSON_SEATED_01.png`** — character state, used SH02–03. Prompt: “One gender-neutral adult in a simple seated pose on a transparent 2160×3840 9:16 canvas, positioned x36–62%, y35–71%, side profile facing right. Average adult proportions; oval head, one short dark hair contour, no facial features; plain light-blue short-sleeve shirt, charcoal trousers, dark plain shoes. Thin 5 px slightly imperfect black fine-marker outline, flat solid fills, orthographic 2D; knees bent about 90 degrees, feet flat, arms relaxed near body. Seat contact point must align with `CHAIR_01.png` seat at y~58%; do not draw the chair. Large transparent margins. No helper, support rail, cane, diagnosis marks, words, numbers, texture, perspective, shadow, extra limbs or hands on a chair.” Consistency: C01 character master; use this image as reference for IMG006. CapCut: position on CHAIR_01; hold seated on “start”; hard replace at “stand”. Animation: **CAPCUT state replacement**.

**IMG006 / `PERSON_STANDING_01.png`** — character state, used SH02,05. Prompt: “Using `PERSON_SEATED_01.png` as exact identity and style reference, draw that same gender-neutral adult fully standing, transparent 2160×3840 vertical canvas, side profile facing right. Same oval head, short dark hair contour, featureless face, light-blue shirt, charcoal trousers, shoes, 5 px imperfect black outline, flat fills and overall body size. Feet baseline y71%; body centered x49%; arms relaxed; no chair in image. Keep head/body proportions and clothing shape visibly identical to seated reference. No second person, helper, motion blur, text, numbers, medical prop, perspective, shadow or extra limbs.” CapCut: replace seated pose on “stand”; replace back on “sit”; one complete cycle counts one. Duplicate replacement once only if clip timing allows; counter natively `1`, `2` as illustrative repetition, then clear. Animation: **CAPCUT discrete swaps**, no tweened rising anatomy.

### SH03 — unsafe / dizziness / ataxia

**IMG007 / `UNSTEADY_ARCS_01.png`** — transparent diagram component. Prompt: “Two small, spare curved motion marks only, black thin 5 px hand-drawn fine-marker lines, each a short arc, placed near x58–70%, y28–42% on transparent 2160×3840 vertical canvas. They indicate generic unsteadiness without severe falling. No person, chair, spiral, star, medical symbol, label, words, color fill, blur, shadow, background, extra marks or dramatic action.” Consistency: same black stroke as chair/person; no red. CapCut: reveal arcs together on “unsafe”; place warning triangle on “dizziness or ataxia”; seated figure stays fixed. Animation: **CAPCUT one-frame grouped reveal**. No I2V sway, because warning should read as stop condition, not depict continued unsafe test.

### SH04 — stop

No new generated image. Reuse IMG002 and IMG003 over BG01. CapCut native `DO NOT TEST` text and one red slash/X may appear on “don't”; remove person and chair at cut, leave timer stopped. Warning remains static. Animation: **CAPCUT state replacement**, no camera change.

### SH05 — personal result versus universal cutoff

**IMG008 / `SCORE_CARD_EMPTY_01.png`** — transparent diagram component; used SH05–07. Prompt: “One simple blank rounded-rectangle score card outline, 5 px slightly uneven black fine-marker line, x31–69%, y30–49% on transparent 2160×3840 vertical 9:16 canvas. Flat orthographic 2D, empty center large enough for editable text. No digits, words, tick marks, scale, badge, person, color fill, drop shadow, perspective, texture or additional plates.” Consistency: reuse exact same file; duplicate in editor at smaller size for three people. CapCut: add `YOUR SCORE` then optionally `?` in native text. Three identical small figures may be duplicated from IMG006, each with a separate blank card. Use native equals sign plus red strike on “universal” to reject *shared cutoff*, not people or their scores. Animation: **CAPCUT layered reveals**. Never display illustrative `8` or numerical threshold.

### SH06 — score does not diagnose

**IMG009 / `DIAGNOSIS_CARD_EMPTY_01.png`** — transparent diagram component. Prompt: “One blank rectangular diagram plate with modest square corners, thin 5 px slightly imperfect black marker outline, x34–66%, y51–68% on transparent 2160×3840 vertical canvas. Flat orthographic 2D, empty interior for editor text. No letters, numbers, medical icon, disease imagery, checklist, color, arrows, shadow, texture, perspective or other objects.” CapCut: `DIAGNOSIS` native text in plate; score card above. Add native thin arrow only briefly on “number alone”, then red slash over arrow at “doesn't diagnose”; keep two plates visible but unconnected. If showing arrow risks misreading before negation, start with faint dotted connector and slash immediately on “doesn't”. Animation: **CAPCUT**, one-frame arrow/strike replacement; no I2V.

### SH07 — Dr. Rehan and CTA

No new generated image. Return to source video full frame at “Dr. Rehan”; small IMG008 score card may sit in free space for first clause, then disappear. Native text: `Full video on channel` only on “full video on the channel”. Animation: **CAPCUT one-frame text reveal**, static hold to audio end; no inferred channel URL, subscribe claim or logo.

## CapCut execution specification

Layer order in illustrated shots, bottom to top: BG01; chair; person state; score/diagram cards; timer/wobble; warning/strike; native labels/counter/captions. Speaker shots: original video bottom, optional small icon overlay above, captions top. Keep original audio continuous and unmodified. No generated sound effects. Hard cuts at shot boundaries, zero transition duration. Positions in prompts are asset layout references; verify visual safe areas against source crop before placement. Captions follow verbatim script. Use one-frame reveals except warning scale (4 frames); no idle float/zoom. Exact start/end, FPS, scale and frame numbers must be set after source inspection.

## QC before Stage B handoff

Confirm exported PNG transparency and consistent person/chair registration; same stroke weight/palette; no generated text; score has no numeric cutoff; dizziness/ataxia do not imply diagnosis; stop shown before further motion; speaker source framing and face visibility; source ratio/FPS and real word onsets measured. Then import assets, duplicate CapCut project, build, watch muted and with audio, revise any confusing state.
