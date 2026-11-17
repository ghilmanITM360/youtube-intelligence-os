# Keyframe recipe library (PRELIMINARY; derived from 38 validated Shorts of 48 local videos of 210 public; snapshot 2026-10-20 night; original-production guidance)

Conventions: timeline 24 fps; **1 frame = 41.7 ms**; "word onset W" = the ASR start of the keyword; `W-2f` = two frames before. Easing default is **linear** because linear is the most common single measured curve (13 of 21 supported camera-scale fits with a real zoom, 18 of 31 supported pans, 8 of 11 pointer x-fits; the other supported scale fits are 8 ease-out; the earlier ease-in and ease-in-out scale tallies were withdrawn, see `OBSERVATIONS_VS_HYPOTHESES.md`); use other curves only where noted. Reference IDs/times are Casually Finance sources for **private timing comparison only**; never reuse their pixels. Layers are listed bottom → top. Mobile rule: nothing meant to be read may be smaller than 0.028 of frame height.

---
## R01 First-three-second visual hook
- **Situation**: the first sentence states a claim or a paradox. **Assets/layers**: white canvas; one large character or object; caption (word-append).
- **Initial composition**: complete at frame 0 (no fade-in): `Qof71Ef-3EU` f0 Earth character already full-size.
- **States**: 0-2 s object enters by motion that matches the claim (barrels fall in, f1-48 `HvnVO1_YrMQ`; receipt unrolls f1-81 `RB5zVghPor8`; falling price line drawn f0-29 `7bm7XYssqlU`); first hard cut at 1.8-3.0 s.
- **Keyframes**: stroke draw = linear, 0.027 frame-widths/frame; falls = linear or hand-set per frame. **Text**: first word on frame 5 (`Qof71Ef-3EU`), words append at onset +1f. **Duration**: 1.8-3.0 s. **Sound**: voice from frame 0; no intro sting observed (unlistened).
- **Mistakes**: fading in from white; a title card first; more than one new idea in 3 s. **Mobile**: hook object >= 0.25 of frame height.
- **Reference**: `Qof71Ef-3EU` 0-2.9 s; `7bm7XYssqlU` 0-2.7 s; `HvnVO1_YrMQ` 0-2.0 s; `RB5zVghPor8` 0-3.2 s. More hook states: a building scales up over f1-48 while the caption types (`bF9WVzzS4ds`, ink area linear; `gGNVpOo7BK8` f531-575, ease-out cubic); a Japan Times article and two yen notes slide in over f3-40 (`Kq5VMugQMHw`); a portrait slides in over f1-33 (`H3PRCteue9Y`).

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
- **Keyframes**: visibility pops, no motion between them. **Text**: tiny labels on the diagram are decoration. **Duration**: 4.5-6 s. More beats: five bond papers at f882, 888, 893, 899, 905 (5-6 frame intervals, `Kq5VMugQMHw`); three calendar icons on 'about three weeks' at f460, 475, 486; three bond papers at f1284, 1291, 1297 (`ODMyV3F_G2g`). **Sound**: optional tick per pop (design choice, unobserved). **Mistakes**: building before the keyword; removing earlier units.
- **Reference**: `DEgQTSsSX9U` 8.1-12.2 s; `Qof71Ef-3EU` S25 (f1816-1884).

## R05 Number reveal
- **Situation**: a headline figure. **Assets**: large hand-lettered number (3-6x caption size) in red/green/black.
- **Initial**: caption under the position. **States**: figure pops in one frame on the word (`Es5c2MKzbDg` f49 '58%', f573 '$429,000'; `HvnVO1_YrMQ` f347 '3%'); optional highlight on the source.
- **Keyframes**: visibility only. **Text**: number >= 0.06 of frame height; units in the caption. **Duration**: hold 1.5-3 s. **Timing (measured)**: pop on the word onset or up to 80 ms before it (`$74B` -20 ms, `3.5` bubble -10 ms, `6%` -60 ms, `3.8` -80 ms, `$6.3` -70 ms, `1998` -50 ms, `50` 0 ms); a figure may also lead by 0.3-0.5 s when it is the topic of the sentence (`$60B`, `$101`). Later Shorts add a wider spread (25 marks, -540 to +390 ms, median -90 ms, 11 within ±100 ms): pop on the word or up to 0.35 s before it; do not place a mark after the word. **Mistakes**: counting animations; more than one number at a time.

## R06 Visual comparison
- **Situation**: A versus B. **Assets**: two charts/props, divider or labels, per-side icon sets.
- **Initial**: both sides in one frame (`mT2hOLrCYSk` S19 f2481-2620: Amazon | Meta with red divider). **States**: left pops, right pops, icon rows pop; or an X and a check on two items (`Qof71Ef-3EU` f1089 both bonds, X f1108, check f1182).
- **Keyframes**: pops. **Text**: labels in hand lettering. **Duration**: 2-6 s. **Mistakes**: asymmetric icon sets; colour as the only cue.

## R07 Source / article highlight
- **Situation**: a document supports the claim. **Assets**: raster page, marker highlight, optional red box.
- **Initial**: page appears by hard cut (small), or slides in (`Es5c2MKzbDg` f5-13). **States**: push-in or scroll 0.9-3.7 s (linear for fast reads), highlight sweep 10-30 frames left to right (`Qof71Ef-3EU` f1467-1517; `RB5zVghPor8` f858-888), presenter pops in to point.
- **Keyframes**: scale 1.00→1.3-2.0 with a drift over 16-63 frames (linear in 13 of 21 supported zoom fits: 1.72x over 63 frames, 1.60x over 31, 1.85x over 43, 1.55x over 30; 1.38x over 23 frames on a chart); a second stage may pan 165-205 px (analysis size) over 15-57 frames with ease-in-out; highlight area grows linearly over 0.5-7.7 s and starts on the first word of the quoted clause, ending near its end. **Text**: crop to the supporting fragment; keep date/source visible. **Duration**: 3-10 s. **Mistakes**: full unreadable page; highlight before the clause is spoken.
- **Reference**: `Qof71Ef-3EU` 49-55.7 s; `RB5zVghPor8` 28-37 s; `ffIiiPLDFdM` 42-46 s.

## R08 Context transition (hard cut)
- **Situation**: every scene change. **Layers**: whole stage replaced.
- **States**: composition A on frame n, composition B on frame n+1, new objects all present on n+1 (stagger by 1 frame only if the layers are separate clips). **Timing**: cut at W-2f to W-4f (sample median -80 ms; p10 -207; p90 +73; n = 696 cuts); optionally clear the caption block one frame before the cut (seen at 11 of 46 cuts in three Shorts); at a pause end if present. **Keyframes**: none. **Sound**: unknown. **Mistakes**: dissolve; cutting before the previous caption chunk ends.

## R09 Narrative escalation
- **Situation**: stakes rise or a theme is repeated. **Patterns**: rapid source montage (`Qof71Ef-3EU` f1936-2048: 8 pages in 3.7 s, holds 0.35-0.7 s, captions dropped); a branded overlay repeated at each 'billions' beat (`mT2hOLrCYSk` rain at 29.5, 46.6, 79.6 s); callback of the opening image (`Qof71Ef-3EU` 26.1 s).
- **Keyframes**: cuts only; overlay clip loop. **Mistakes**: montage held long enough to be read (it should read as texture); overlay on every beat.

## R10 Character reaction
- **Situation**: an irony or admission. **Assets**: face variants (neutral/frown/smile/worried) as separate head layers; eyes layer for map/planet characters.
- **States**: expression swap in one frame (`Qof71Ef-3EU` f163 US-map eyes wide → half-lid); pose swap in one frame (`Es5c2MKzbDg` f1125); surprised host rises (`7bm7XYssqlU` f262-265). Keep bodies still.
- **Keyframes**: visibility swap. **Mistakes**: continuous face morphing.

## R11 Camera moves
- **Situation**: guide the eye over a still. **Assets**: raster page, a single parent group.
- **States/keyframes** (measured): push-in scale 1.00→1.52 over 0.87 s **linear** with drift (-39 px x, -25 px y at 180x320 analysis size); alternative 1.00→1.43 over 1.7 s that **decelerates** (`Qof71Ef-3EU`); 1.96x over 27 frames then a 170 px pan over 57 frames (ease-in-out) and a 165 px pan back over 15 frames (`bF9WVzzS4ds`); 1.67x over 16 frames ease-out quad (`-WJDfT-MwmY`); a chart image panned 205 px over ~31 frames ease-out quad (`bF9WVzzS4ds`). Pointer/arrow translation **linear** 0.151 frame-widths/s, or 0.62 frame-widths over 87 frames for a red arrow along a yield curve (`06pN9dDvVVU`).
- **Mistakes**: ease-in-out on every move; zooming characters instead of the page.

## R12 Payoff scene
- **Situation**: the last sentence resolves the thesis. **Patterns**: thesis object acted out (`DEgQTSsSX9U` black '?' circle fades to white over f1881-1902, **linear** ~10.7 gray levels/frame at 30 fps; `RB5zVghPor8` tiny crystal-ball figure; `7bm7XYssqlU` tiny builder with larger 'builder' caption).
- **Keyframes**: opacity linear 0.7 s; scale hold. Other measured payoffs: a black box that grows linearly over 145 frames and then fades into the key photo at ~2.4 gray levels per frame over 25 frames (`ODMyV3F_G2g`); a red circle that draws in 12 frames and blinks off and on (`JztI-l-0-x4`, `zkeA5cH9nyM`); a 146-frame hold with only a slow downward drift of ~0.05 of the frame height (`Kq5VMugQMHw`). **Mistakes**: summary text card; music swell (unobserved).

## R13 Ending hold
- **Situation**: last 0.3-1.0 s. **States**: final composition held, captions may already be gone (`Qof71Ef-3EU`: no captions from 62.8 s, last page held 0.35 s; `7bm7XYssqlU` final hold 0.83 s). **Mistakes**: end card, fade to white; no loop point is observed.

## R14 Aside bubble
- **Situation**: an irony or joke the script does not say. **Assets**: speech bubble with hand-lettered text, one character or prop as speaker.
- **States**: the bubble pops in one frame at W±2f; its text may swap in one frame ('Pls don't leave me!' f369 to 'I'll stay for them dollars' f402, `gGNVpOo7BK8`; 'More money pls!' f1887, 'That's kinda sus...' f1951, 'But OK I guess?' f1990, `bF9WVzzS4ds`); tiny captions beside props do the same job ('his glasses were thick AF'). Bubble pops land at 0.0-0.3 s from the matching word ('Stability!' 40 ms before 'stability').
- **Keyframes**: visibility only. **Duration**: 1-3 s. **Mistakes**: bubble text that repeats the narration; more than one aside per scene. **Rights**: write original jokes.

## R15 Time card
- **Situation**: a time jump or a pun ('two weeks later', 'the next day'). **Assets**: full-width card with bold text on a flat pattern.
- **States**: card replaces the stage in one frame, holds 1.5-1.8 s, is replaced in one frame; the card appears 0.15-1.1 s before the pun word and goes after it (`gGNVpOo7BK8` f702-747, f1480-1511; `bF9WVzzS4ds` f175-219).
- **Keyframes**: none (hard cuts). **Mistakes**: a dissolve; leaving the card until the next sentence.

## R16 Clip insert (third-party footage or meme)
- **Situation**: a reaction or analogy shown by short borrowed footage. **Assets**: a short clip in a bounded rectangle plus a caption.
- **States**: the rectangle appears in one frame; the clip updates about every third frame (10 updates per second on a 30 fps timeline, alternating 2/3-frame gaps on 24 fps; 15 per second in `rSa2aziEsAI`) for 1.5-4 s, then holds on its last frame until the cut (`bF9WVzzS4ds` f289-346, `gGNVpOo7BK8` f816-867, `JztI-l-0-x4` f1755-1804, `m8NC4L8hmeE` f1042-1086).
- **Mistakes**: using footage you do not have rights to; a full-rate clip beside a 10-fps look. **Rights**: use original or licensed clips only; the sources here are `UNKNOWN`.

## R18 Read-along page pan
- **Situation**: a quoted passage must be read at the narrator's pace. **Assets**: raster text page wider than the frame, yellow marker layer, optional desk figure.
- **States**: page cut in (small) at the start of the sentence; the highlighter grows across the line over the spoken duration (0.4-8.7 s; start 0.12-0.38 s before the first word, end at the last word); the page pans left at a constant step (-2.0 to -4.7 px per frame at the 180-px analysis size, 15-69 frames) and returns to the line start at a faster constant step in 5-11 frames before the next line (`2EZzwupIa80` f957-993, f1035-1080, f1321-1397, f1680-1790).
- **Keyframes**: linear translate only; no scale. **Text**: the page carries the words; the caption may be dropped. **Mistakes**: ease-in-out on the pan; a highlighter that is ahead of the voice. **Reference**: `2EZzwupIa80` 35.8-47.1 s and 64.5-75.3 s.

## R19 Metronomic wobble
- **Situation**: a character must stay alive through a long hold. **States**: two poses swapped exactly every 10 frames (3 per second at 30 fps) for 200+ frames (`JsK53moCyZA` f139-349, 22 swaps); a small figure at the corner may blink-swap at irregular 11-34-frame gaps.
- **Keyframes**: visibility swap, no tween. **Mistakes**: continuous morphing.

## R20 Chart draw-on
- **Situation**: a rate or yield line is introduced. **States**: the line is drawn left to right over 34-41 frames (`rSa2aziEsAI` f228-261 ease-in-out, f558-598 linear-ambiguous, the second followed by a tooltip at the line end); in a source recording the chart scrolls left ~215 px (analysis size) over 92 frames with tooltips every 22-24 frames (`6S3PzAUFnXQ` f360-451).
- **Keyframes**: reveal mask progress, smoothstep or linear. **Mistakes**: drawing faster than the caption can be read.

## R17 Turning ring (feedback loop)
- **Situation**: a self-reinforcing process. **Assets**: ring of three arrows, one typed phrase inside.
- **States**: ring pops in one frame (two in `Kq5VMugQMHw`), changes continuously for 36-115 frames (~550-570 changed px per frame), is removed in one frame; a glowing card ('THE DOOM LOOP') may follow and fade over 20 frames (`-WJDfT-MwmY` f921-1018 and f1047-1082; `Kq5VMugQMHw` f1548-1688).
- **Keyframes**: rotation; rate not measured; start with a constant angular speed. **Mistakes**: a static ring with no motion.

---
**Open items**: easing of pops is unobservable below one frame; sound cues are unknown; long-form recipes are not covered; verify every recipe against your own render with `scripts/forensic_features.py` and `build_video_tables.py`.
