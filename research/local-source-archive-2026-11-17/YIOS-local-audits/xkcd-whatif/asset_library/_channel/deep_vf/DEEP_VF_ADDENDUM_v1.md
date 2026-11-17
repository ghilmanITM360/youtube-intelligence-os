# xkcd's What If? deep visual forensics: addendum v1 (2026-11-08, LOCAL ONLY, visual-only; audio BLOCKED)

This file adds to `../CLONE_READINESS_HANDOFF.md` (P1–P6), `campaign/CHANNEL_PRODUCTION_MANUAL_v0.7.md` and held-out v1–v6. It does not edit any of them. Labels used throughout: MEASURED / OBSERVED / ESTIMATED / INFERRED / UNAVAILABLE. Casual Finance supplied only the method (strata map, viewed sheets, motion windows, frozen held-out). None of its targets, rules or validator are applied here.

## 1. Denominators (kept separate)
| Set | Long | Short | Source |
|---|---|---|---|
| Channel census | 45 | 46 | census/census.csv |
| Local source present | 44 (alkJ7xScBiw missing) | 44 (NxVdO7M2YdM, XwJAbyn5uGY missing) | census local_paths |
| Reviewed-ledger library (dev + held-out 1–5) | 24 | 20 | asset_library/ |
| Independent within the library | ≈24 | ≈11 (9 of the 20 are narration excerpts of library longs) | P1 audit |
| Pop-6, quant-only, never visually reviewed before this session | 20 | 0 | selection_v6_pop6.json |
| Fully verified (all gates incl. listening) | **0** | **0** | campaign_matrix: listening BLOCKED 91/91 |
| Strictly fresh (never used anywhere) | **0** | 24 before this session, **22** now | strata_map.csv `prior_use` |
| Used as held-out in this session (v7) | 4 (Pop-6) | 2 | heldout_v7_selection.json |

Excerpt and independence links (MEASURED, text level):
- 38/46 Shorts are TEXT_EXCERPT_CANDIDATEs of a long video. All 22 remaining fresh Shorts with captions are excerpts of already-used longs; X97DDWvxaqQ and alBQCm0QpJg have no caption text.
- Alternate encodes exist for some IDs (census lists two paths). Every measurement here used the encode whose SHA matches `source_hashes_all_2026-11-06.json` or the ingest SHA.
- The 10 videos shared with the repo's forensic index use different encodes (checkpoint R finding). They are not double-counted.

## 2. Strata map and selection reasons
`strata_map.csv` gives one row per census video with:
- format and period (half-year);
- a uniform rhythm measure (automated ACTIVITY segments/min) and its tertile;
- non-canvas share;
- title-only explanation type (INFERRED; too coarse, since 35/45 longs fall in CONSEQUENCE);
- opening layout and question card at frame 3;
- Short→parent relation;
- prior use.

Development coverage already exceeds the starting plan of 12 long + 6 Shorts: there are 24 reviewed longs across 2023H2–2026H2 and every rhythm tertile, plus 20 Shorts (≈11 independent). This session added targeted dev batches B1–B3 on existing media and one frozen validation (v7).

v7 selection (seeded 20261109, written before viewing):
- Short A: U4cONnQxgvo, the excerpt with a library parent, which allows a parent-density test.
- Short B: X97DDWvxaqQ, no caption text, so it is the most independent.
- Longs: one per period from Pop-6.
  - e3uk7jU3RHo 2023-12
  - UXA-Af-JeCE 2024-09
  - X7sbn9LMZOg 2025-04
  - U8F7UNK9jco 2025-10

**Missing stratum:** 2026 long. Every 2026 long is already in dev or held-out.

## 3. Batch log and stopping rule
| Batch | Media | New production-relevant finding? |
|---|---|---|
| B1 opening reuse | frame n=3 of 44 longs, SHA 44/44 OK | **Yes.** Reuse is layer-level, not whole-frame (F1) |
| B2 motion windows | 15 new bounded windows (13 classes incl. 5 Shorts), SHA + PTS OK | **Yes.** Annotation circles pop, they do not draw on; Shorts slide 4 f (F4, F5) |
| B3 script vs visual | ASR segments × reviewed ledger, 24 long + 20 Short; 3 viewed beat sheets | **Yes.** Busy/calm comes from period and device mix, not script cue density; Shorts inherit parent density (F6–F8) |
| v7 frozen validation | 6 held-outs | **Yes.** Colour mode, glow gradients, slow process animation, red edit-marks (heldout_v7/RESULTS.md) |

Every batch produced a material new finding, so **no candidate stopping point has been reached yet**. The rule (two consecutive dev batches with no material finding) has not triggered.

## 4. Findings (video, SHA prefix, frame/PTS, result, counterexample, production use)
**F1. The opening is a reused layer set, not a reused frame.**
- MEASURED on 44 longs at frame 3, as 120-px cells versus the modal opening jgafb8G7i4o (320cdf05).
  - No other video matches the whole frame.
  - The question card size and text, board contents and narrator modifiers differ.
  - The narrator + paper + whiteboard + ledge layers sit at exactly the same pixel offsets in 30/44 videos (head x0=241, board x0=612; "L1", 2024-02 → 2026-03).
  - A second offset set, L2 (259, 637), appears in 6 videos from 2026-05 onward (BnGq, FYoH, TFhr, BO8r, 4ZVt, 9VG0), which is a re-saved template.
  - 8 videos are OTHER: early 2023–24 variants, the EFRUL7vKdU8 disclaimer card, the Z_xJ40QXu7Q zoomed-out narrator, and the s3oLIDaElaE larger board.
- The question card is on screen at frame 3 in every L1/L2 video from 2024-04-16 (p2M8) onward, except IdlQsjq5vKo and 9VG0yqq_PHM. Before 2024-04 it is absent at frame 3.
- The variance map (`opening/variance_map.jpg`) shows the card text, board interior and narrator offset as the only varying regions.
- **Production use:** build one lecture-frame rig as separate layers (narrator, paper, board, ledge, card). Swap the card text and board content per episode. Never bake a full opening frame.
- The earlier P3 "18/24 pixel-identical openings" statement is **corrected** by F1. What matched was the narrator figure layer (617 px tall, head 231 px), not the frame.

**F2. Canvas is not always #F9F9F9.**
- MEASURED: frame 3 is #F9F9F9 in 42/44 longs. It is pure #FFFFFF in U8F7UNK9jco (38b212f4) and FYoHYq8VRt0 (d84737cd).
- Modal bright pixel on scaled held-out frames: #F7F7F7 in 5/6 and #FDFDFD in U8F7. The difference from #F9 is within decode/scale tolerance.
- **Use:** master canvas #F8F8F8 ±2; do not ship pure white.

**F3. Every long has a 12.0 s red title card; Shorts never do.**
- MEASURED from FULL_FRAME_MEASUREMENTS (mean R>150, G,B<110).
  - Longs: 44/44 have it, 280–288 frames (288 = 12.000 s in 40/44). It first appears at 6.1–30.4 s (median about 11.8 s).
  - Shorts: 0/20 dev and 0/2 fresh have one.
- **Use:** the original channel needs its own ident (BRD-001). Hold it 12 s on long-form, insert it after the question beat, and omit it on Shorts.

**F4. Red annotation circles pop; they are not drawn on.**
- MEASURED from reviewed ledgers: ANNOTATION_CIRCLE is 1 frame in 17/17 long and 15/16 Short events.
- The window ANNOT_CIRCLE_UQgw50GQu1A_G0020 (5049f27c, f657) shows two red circles appearing in one frame.
- Counterexample: one Short event lasting 5 frames.
- **Correction to P5 and the PROMPT_PACK:** "red circle write-on" becomes a red circle POP (1 f).
- Related: WRITE_ON_STRIKE is 1 frame in 13/22 long events; WRITE_ON_LINE is 1 frame in 34/66.
- Limit: this red-on-off-white event has diff 0.08 at 480-px greyscale, below the 0.3 threshold. Greyscale motion metrics miss red marks, and so do low-contrast pop-on labels (POP_LABEL_FYoHYq8VRt0_G0028: 0.30 and 0.28 in two steps 6 frames apart). The automated tags undercount these. The reviewed ledger caught them.

**F5. Motion timing additions (MEASURED windows, `motion_windows/`).**
- CUT is 1 frame: BnGq G0090 f2553, -1-ld G0170 f5463, Short kNry0bf7eC0 G0008 f216.
- STATE_SWAP_DAMAGE is 1 frame: s3oL G0104 f2641, JcXp G0152 f4858.
- WRITE_ON_STRIKE is 1 frame: JcXp G0154 f4897.
- POP_ON is 1 frame in a Short: 35KZm1yiyIE G0056 f1360.
- WRITE_ON_TYPE is 1 frame in a Short (SLd4hnmeW_g G0060 f1100). This is a whole word appearing at once. The ledger median is 6 frames in both formats.
- FADE_IN: qu8nx1qUwEU G0002 f53–58 is linear over 6 frames (progress 0.17/0.32/0.49/0.65/0.81/0.98).
  - Reviewed ledger: FADE_IN median 6 (n=8 long + 1 Short); CROSS_DISSOLVE median 6 (12 long + 8 Short).
- SCROLL_UP: r7B0MzvwDcA G0122 f3726–3735 is eased in-out over about 9–10 frames, with a vertical move of about 6 px at 480 px width.
- **Shorts slide:** 35KZm1yiyIE G0072 f1704–1707 is a 4-frame constant-speed horizontal slide to the next notebook page, with no visible blur. The ledger PAN_LEFT median in Shorts is 4 f (n=4), against 14 f in long (n=1).
- **Map-move Short:** U4cONnQxgvo G0016 f452–459 is an 8-frame blurred push-in and pan with overlay fades riding the move, followed by a hard landing.
- **Slow process animation (new class, held-out):** U8F7 G0104/G0106 run 216–220 frames.

**F6. Busy versus calm follows publication period, not script cue density.**
- MEASURED across 44 longs (uniform automated rate):
  - correlation with date r=+0.45;
  - medians per year: 2024 20.0, 2025 22.1, 2026 26.0 events/min;
  - non-canvas share r=−0.07.
- MEASURED on 24 library longs (ASR_UNCERTIFIED):
  - share of numeric/scale-cue sentences vs rate: r=−0.05;
  - ASR sentences/min vs rate: r=+0.25;
  - words/s is flat at 3.7–3.9 in BUSY, MID and CALM.
- So busy/calm is **not** driven by how many numbers the script says, nor by talking speed.

**F7. Busy and calm use different device mixes (MEASURED, reviewed ledgers).**
| Format, tertile | Label-pop share | Cut share | Mean activity length |
|---|---|---|---|
| Long BUSY | 18.9% | 15.5% | 5.7 f |
| Long CALM | 11.8% | 28.4% | 8.15 f |

- BUSY means accumulation: a persistent scene gets one label per noun phrase.
  - OBSERVED in BO8rOs05v48 (dc2a7b1b) 21.6–32.1 s: SECONDARY BOW, ALEXANDER'S DARK BAND, PRIMARY BOW, then droplets 1→2→3→4, each a 1-frame pop on its word.
- CALM means a new scene per idea, plus longer devices.
  - OBSERVED in WH4g1ptJ-70 (8ae3bc7c): 10 f strike write-on (26.8 s), 10–16 f globe rotations (28–30 s), 10 f blurred pan across a wide landscape (47.9 s), 11–12 f arrow write-ons on "hot air rises… flows poleward" (56.6–58.2 s).

**F8. Within a video, question and setup sentences get the most visual change.**
- MEASURED (ASR_UNCERTIFIED; cue tags are INFERRED text rules):
  - long: SETUP 30.3/min, QUESTION 28.6/min, NUMBER 22.0, SCALE 20.7, PLAIN 22.8;
  - Shorts: QUESTION 35.1/min.
- NUMBER sentences are led by POP_ON_LABEL (93/399 events in long).
- REVERSAL sentences ("but", "actually"…) are led by SCENE_SWAP in mid and calm videos.
- OBSERVED jokes:
  - WH4g puts the "1990s cinema" joke as a small vignette inside the board (9.9 s).
  - BO8r and UXA use small reaction figures with speech text ("PLEASE DON'T", "PHEW").
- Jokes cannot be detected from ASR text rules: UNAVAILABLE as a measured class.

**F9. Shorts inherit the parent's density; they do not re-animate faster.**
- MEASURED on matched ASR sentences:
  - Ny9m2l6h478 (3f2dc68b) runs 26.7/min against parent p2M8Y0z9Rl0 (c949504f) at 27.0/min on the same sentences (reviewed ledgers). The parent's whole-video rate is 22.8.
  - Fresh held-out U4cONnQxgvo runs 20.4 against WH4g at 18.4 (automated, +11%).
- The Short is busier than its parent overall only because it keeps the denser sentences and drops "This question comes from…".
- 9:16 layout (OBSERVED in Ny9m):
  - board in the top half, narrator below;
  - no card, no title card;
  - wide strips cropped to centre;
  - list sentences become stacked vignettes.
- **Use:** cut Shorts from the long-form edit and re-lay them out. Do not re-time them.

**F10. Colour and red usage needs a wider rule (held-out failure).**
- See `heldout_v7/RESULTS.md`. What was observed:
  - painted colour plates and gradients (U8F7);
  - glow vignettes (UXA, X97D);
  - pink region highlights on maps (U4cO);
  - red-drawn props (X97D).
- Colour share is a continuum across the channel (`colour_mode_share.csv`).

## 5. Busy/calm decision rules for an original production (INFERRED from F6–F9; not yet validated)
1. Choose one house density per series era and hold it. Target 24–27 events/min for a "current" look; 18–21 is the 2024-style calm baseline. Do not vary density with how numeric the script is.
2. Beat-level modulation:
   - question/setup sentences get about 1.3× base density (board fills, card, first objects);
   - number sentences get a label pop on the number word;
   - a reversal gets a cut to a new scene;
   - a joke gets a small vignette or reaction figure with text, held long enough to read.
3. For a BUSY episode, keep a scene and accumulate up to about 4 labels or objects on it before cutting. For a CALM episode, cut to a new scene per idea and use one longer device (a 10–16 f rotation or write-on, or a 9–12 f blurred pan).
4. Scale-ladder/journey episodes may exceed 6% camera moves through a persistent ruler or anchor scroll. Budget up to about 12% for that format only (e3uk, oTzW).
5. Shorts are excerpts. Keep the parent's per-sentence density and re-lay out to 9:16.

## 6. Motion timing table v2 (supersedes the P4/P5 table where they differ)
| Class | Frames @24 | Curve | Evidence |
|---|---|---|---|
| Pop-on object/label/inset | 1 | step | ledger: POP_ON_LABEL 1 f in 263/271 long and 81/81 Short |
| Red circle / mark | 1 | step | F4 |
| Strike-through | 1 (59%) or write-on ≤10 | step or linear | ledger |
| Hard cut / scene swap | 1 | step | 393/401 long |
| State swap (damage, object) | 1 | step | 33/34 |
| Pose swap | 1 (or 6 f dissolve, once) | step | 52/55 |
| Type-on text | median 6, up to 26; whole-word pops occur | linear, about 1 letter/f | ledger + SLd4 |
| Line write-on | 1 (52%) or 4–14 | about constant speed | ledger |
| Cross-dissolve / fade-in | 6 | linear | 3/3 + qu8n window |
| Pan / scroll (long) | 9–14 | ease in-out, directional blur, hard landing | r7B0, WH4g, EsUB |
| Slide (Short) | 4 | constant, no blur | 35KZm |
| Zoom | 9–10 | S-curve out, ease-out in | P4 |
| Map move with overlay fade (Short) | 8–9 | eased + blur, fades ride the move | U4cO |
| Object path / slow process | 21–220 | about constant | U8F7 (n=1 video) |
| Title card (long only) | 288 hold | cut in/out | F3 |
| Rejected | overshoot, squash, idle loops, shake | — | 0/15 windows |

## 7. Style-bible corrections (to apply when PROMPT_PACK v2 is written; the existing pack is not edited)
- "Red circle write-on" → red circle **pop** (GFX-002).
- "No gradients" → gradients are allowed for light and glow (sun surface, screen glow, sky/dusk plates); never on line-art objects (ENV-003 widened; NEG lock revised).
- Red is the **emphasis layer**: marks, circles, strikes, arrows, labels, highlighted region tints and occasional emphasis props. Never a full background, except in the painted colour mode.
- Add a **painted colour mode** plate set (sunset, night sky, map biome colours) as an optional ENV family. A series should use it sparingly: in 5/44 longs, more than 20% of frames are colourful.
- Lecture-frame rig: layered, with fixed offsets (F1). Card on top from frame 0. Template revisions are allowed (L1 → L2 shifted about 20 px).
- Optional anchors: scale-ladder ruler (left edge, persistent, blurred scroll) and timeline strip.

## 8. Layered keyframe blueprint (original assets; extends HUMANCRAFT_ALIGNMENT §3–4)
- Layers, bottom to top:
  1. canvas plate (#F8);
  2. optional colour/glow plate;
  3. scene line-art group;
  4. labels (text layers);
  5. red emphasis layer (vector paths and tints);
  6. anchors (ruler, timeline);
  7. lecture rig (narrator parts, board, ledge, card).
- Keys: every event is a step key at round(t_word × 24). Fades are 6 f linear. Moves are 9–12 f eased, with a blur equal to velocity and a hard final frame.
- Beat sheet input: sentence → cue tag → device (§5). The timing authority is the owner's narration file; until it exists, word times are placeholders.

## 9. 5–12 s moving proof: test brief and pass criteria (render NOT run: no render authorization is recorded for this pass)
- **Beat (original script, about 8 s, 192 frames, 1920x1080, silent):**
  1. f0: lecture rig on screen with an original question card (card text types on, about 1 letter/f).
  2. f60: board pops an object (1 f).
  3. f84: label pop.
  4. f108: red circle pop.
  5. f132: hard cut to a full-bleed scene.
  6. f150: second and third label pops (accumulation).
  7. f170: 6-frame linear dissolve to a glow plate.
- Then the same beat re-laid at 1080x1920 (board top, narrator below, no card).
- **Pass criteria (each measured on the render with the existing motion_window metrics):**
  - P1 every pop changes on exactly 1 frame (diff_prev >0.3 on one frame only);
  - P2 dissolve progress is linear over 6 frames (each step 0.17±0.04);
  - P3 no overshoot (progress_max ≤1.03);
  - P4 canvas #F8 ±2, stroke 7–9 px at 1080 h;
  - P5 red appears only on the emphasis layer;
  - P6 holds are dead still (diff 0 between keys);
  - P7 ffprobe shows 24 fps CFR, the frame count matches, and the file decodes;
  - P8 a human views every keyframe and the 9:16 layout has no clipped elements;
  - P9 the 10-dimension HumanCraft scorecard is ≥4 on all non-audio rows.
- Narration sync, listening and final AV acceptance stay **separate and BLOCKED** until owner narration exists and a human listens.
- Renderer: Python (PIL/OpenCV) frames + ffmpeg encode, which needs no install. ffmpeg here has no drawtext, so text is pre-rendered as layers.

## 10. How many videos are needed (provisional)
- **Development:** already sufficient in count. 24 reviewed longs and 20 Shorts (≈11 independent) exceed 12+6. They are not "fully verified": 0/88 are, because listening is blocked.
- **Validation:**
  - v7 tested 4 long + 2 Shorts and scored 82.6%, below the 90% bar.
  - The failures are confined to (a) colour/red usage and (b) camera share in the scale-ladder/journey format. Both are rule-wording issues, and existing dev already contains these formats (WH4g, BO8r, r7B0, qu8n for colour; oTzW, Z_xJ, IdlQ, e3uk for journey).
- **Provisional count:** **≈28 long + 24 Shorts** analysed in total.
  - Already eligible: 24 long + 20 Shorts.
  - Already used for v7: 4 long + 2 Shorts.
  - Still to analyse: re-view about 4 existing colour/journey dev videos for the rule revision (no new media), then **4 more long + 2 more Shorts** as a fresh v8 validation of the revised colour and journey rules only.
    - Longs: remaining visually-unseen Pop-6, which are quant-exposed and not strictly fresh.
    - Shorts: 22 fresh remain.
- **Stop:** if v8 reaches ≥90% and two consecutive dev batches add no material finding.
- **Hard limit:** no strictly fresh long-form video exists locally. A truly fresh long needs a new upload or acquisition (owner decision; alkJ7xScBiw has no local source).
