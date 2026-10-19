# Keyframe recipe library (PRELIMINARY; derived from 12 validated Shorts; original-production guidance)

Conventions: timeline 24 fps; **1 frame = 41.7 ms**; "word onset W" = the ASR start of the keyword; `W-2f` = two frames before. Easing default is **linear** because 5 of 6 clean measurements were linear (see `OBSERVATIONS_VS_HYPOTHESES.md`); use ease-out only where noted. Reference IDs/times are Casually Finance sources for **private timing comparison only**; never reuse their pixels. Layers are listed bottom → top. Mobile rule: nothing meant to be read may be smaller than 0.028 of frame height.

---
## R01 First-three-second visual hook
- **Situation**: the first sentence states a claim or a paradox. **Assets/layers**: white canvas; one large character or object; caption (word-append).
- **Initial composition**: complete at frame 0 (no fade-in): `Qof71Ef-3EU` f0 Earth character already full-size.
- **States**: 0-2 s object enters by motion that matches the claim (barrels fall in, f1-48 `HvnVO1_YrMQ`; receipt unrolls f1-81 `RB5zVghPor8`; falling price line drawn f0-29 `7bm7XYssqlU`); first hard cut at 1.8-3.0 s.
- **Keyframes**: stroke draw = linear, 0.027 frame-widths/frame; falls = linear or hand-set per frame. **Text**: first word on frame 5 (`Qof71Ef-3EU`), words append at onset +1f. **Duration**: 1.8-3.0 s. **Sound**: voice from frame 0; no intro sting observed (unlistened).
- **Mistakes**: fading in from white; a title card first; more than one new idea in 3 s. **Mobile**: hook object >= 0.25 of frame height.
- **Reference**: `Qof71Ef-3EU` 0-2.9 s; `7bm7XYssqlU` 0-2.7 s; `HvnVO1_YrMQ` 0-2.0 s; `RB5zVghPor8` 0-3.2 s.

## R02 Character introduction
- **Situation**: a presenter reacts to or points at evidence. **Assets**: character with pointer-arm and neutral/surprised face variants.
- **Initial**: evidence already on screen. **States**: character **pops** in one frame at W-2f (`7bm7XYssqlU` f103-104), or **rises** from the bottom edge over ~14 frames (`Es5c2MKzbDg` f292-304; `7IMFHclDn8k` f1535-1548), or **slides** from the left edge over 18-21 frames (`RB5zVghPor8` f1483-1502).
- **Keyframes**: position only, linear; hold the final pose >= 1 s. **Text**: caption continues unbroken. **Duration**: 0.1-0.9 s entrance. **Mistakes**: mid-sentence entrances without a keyword; scaling during entrance. **Reference** as above.

## R03 Concept object entrance
- **Situation**: a noun is introduced. **Assets**: single flat prop, optional label.
- **Initial**: empty or previous composition. **States**: prop appears fully formed in 1 frame at W-2f (`PR_BOND` etc.); pairs may pop together (`HvnVO1_YrMQ` f142, f152 gas cylinders).
- **Keyframes**: visibility only; no scale overshoot observed at 30 fps sampling. **Text**: label hand-lettered, same frame. **Duration**: hold until the sentence ends (1-3 s). **Mistakes**: bounce/overshoot; two unrelated props at once.

## R04 Progressive diagram building
- **Situation**: a process or schedule explained step by step. **Assets**: timeline line, N unit props, end prop, curved arrow + label.
- **Initial**: line + first prop in one frame (`DEgQTSsSX9U` f245-259). **States**: one unit per narration beat (bills at file frames 259, 284, 307, 331 of a 30 fps file = intervals 25, 23, 24 frames ≈ 0.8 s per unit), end prop (f347), label+arrow together (f361).
- **Keyframes**: visibility pops, no motion between them. **Text**: tiny labels on the diagram are decoration. **Duration**: 4.5-6 s. **Sound**: optional tick per pop (design choice, unobserved). **Mistakes**: building before the keyword; removing earlier units.
- **Reference**: `DEgQTSsSX9U` 8.1-12.2 s; `Qof71Ef-3EU` S25 (f1816-1884).

## R05 Number reveal
- **Situation**: a headline figure. **Assets**: large hand-lettered number (3-6x caption size) in red/green/black.
- **Initial**: caption under the position. **States**: figure pops in one frame on the word (`Es5c2MKzbDg` f49 '58%', f573 '$429,000'; `HvnVO1_YrMQ` f347 '3%'); optional highlight on the source.
- **Keyframes**: visibility only. **Text**: number >= 0.06 of frame height; units in the caption. **Duration**: hold 1.5-3 s. **Mistakes**: counting animations; more than one number at a time.

## R06 Visual comparison
- **Situation**: A versus B. **Assets**: two charts/props, divider or labels, per-side icon sets.
- **Initial**: both sides in one frame (`mT2hOLrCYSk` S19 f2481-2620: Amazon | Meta with red divider). **States**: left pops, right pops, icon rows pop; or an X and a check on two items (`Qof71Ef-3EU` f1089 both bonds, X f1108, check f1182).
- **Keyframes**: pops. **Text**: labels in hand lettering. **Duration**: 2-6 s. **Mistakes**: asymmetric icon sets; colour as the only cue.

## R07 Source / article highlight
- **Situation**: a document supports the claim. **Assets**: raster page, marker highlight, optional red box.
- **Initial**: page appears by hard cut (small), or slides in (`Es5c2MKzbDg` f5-13). **States**: push-in or scroll 0.9-3.7 s (linear for fast reads), highlight sweep 10-30 frames left to right (`Qof71Ef-3EU` f1467-1517; `RB5zVghPor8` f858-888), presenter pops in to point.
- **Keyframes**: scale 1.00→1.4-1.5 with a leftward drift; highlight width linear. **Text**: crop to the supporting fragment; keep date/source visible. **Duration**: 3-10 s. **Mistakes**: full unreadable page; highlight before the clause is spoken.
- **Reference**: `Qof71Ef-3EU` 49-55.7 s; `RB5zVghPor8` 28-37 s; `ffIiiPLDFdM` 42-46 s.

## R08 Context transition (hard cut)
- **Situation**: every scene change. **Layers**: whole stage replaced.
- **States**: composition A on frame n, composition B on frame n+1, new objects all present on n+1 (stagger by 1 frame only if the layers are separate clips). **Timing**: cut at W-2f to W-4f (sample median -76 ms; p10 -204); at a pause end if present. **Keyframes**: none. **Sound**: unknown. **Mistakes**: dissolve; cutting before the previous caption chunk ends.

## R09 Narrative escalation
- **Situation**: stakes rise or a theme is repeated. **Patterns**: rapid source montage (`Qof71Ef-3EU` f1936-2048: 8 pages in 3.7 s, holds 0.35-0.7 s, captions dropped); a branded overlay repeated at each 'billions' beat (`mT2hOLrCYSk` rain at 29.5, 46.6, 79.6 s); callback of the opening image (`Qof71Ef-3EU` 26.1 s).
- **Keyframes**: cuts only; overlay clip loop. **Mistakes**: montage held long enough to be read (it should read as texture); overlay on every beat.

## R10 Character reaction
- **Situation**: an irony or admission. **Assets**: face variants (neutral/frown/smile/worried) as separate head layers; eyes layer for map/planet characters.
- **States**: expression swap in one frame (`Qof71Ef-3EU` f163 US-map eyes wide → half-lid); pose swap in one frame (`Es5c2MKzbDg` f1125); surprised host rises (`7bm7XYssqlU` f262-265). Keep bodies still.
- **Keyframes**: visibility swap. **Mistakes**: continuous face morphing.

## R11 Camera moves
- **Situation**: guide the eye over a still. **Assets**: raster page, a single parent group.
- **States/keyframes** (measured): push-in scale 1.00→1.52 over 0.87 s **linear** with drift (-39 px x, -25 px y at 180x320 analysis size); alternative 1.00→1.43 over 1.7 s that **decelerates** (`Qof71Ef-3EU`). Pointer/arrow translation **linear** 0.151 frame-widths/s.
- **Mistakes**: ease-in-out on every move; zooming characters instead of the page.

## R12 Payoff scene
- **Situation**: the last sentence resolves the thesis. **Patterns**: thesis object acted out (`DEgQTSsSX9U` black '?' circle fades to white over f1881-1902, **linear** ~10.7 gray levels/frame at 30 fps; `RB5zVghPor8` tiny crystal-ball figure; `7bm7XYssqlU` tiny builder with larger 'builder' caption).
- **Keyframes**: opacity linear 0.7 s; scale hold. **Mistakes**: summary text card; music swell (unobserved).

## R13 Ending hold
- **Situation**: last 0.3-1.0 s. **States**: final composition held, captions may already be gone (`Qof71Ef-3EU`: no captions from 62.8 s, last page held 0.35 s; `7bm7XYssqlU` final hold 0.83 s). **Mistakes**: end card, fade to white; no loop point is observed.

---
**Open items**: easing of pops is unobservable below one frame; sound cues are unknown; long-form recipes are not covered; verify every recipe against your own render with `scripts/forensic_features.py` and `build_video_tables.py`.
