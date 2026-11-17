# Claude animation handoff: Finance Short 01, "The interest that waits"

**Package status: `AUDIO_CORRECTION_REQUIRED`.** The illustrated asset library is complete and QA'd. All timings below are **provisional**: the supplied MP3 says "introductory **April**" instead of "A-P-R" at 38.63–39.03 s (see `audio_analysis/AUDIO_QA_REPORT.md`).

**Do not start animating until both of these are true:**
1. The owner supplies a corrected MP3.
2. The owner explicitly authorizes the animation phase.

## 0. Gate procedure once the corrected MP3 arrives

```
cd finance-short-experiment-01/PHASE_2_ASSETS
python3 build/align_audio.py <corrected.mp3> ../FINAL_SCRIPT.md AUDIO_ALIGNMENT.json <scratch_dir> audio_analysis/pronunciation_gate.json
python3 build/build_assets.py   # regenerates SCENE_ASSET_MAP.csv, typography/CAPTIONS.json and the storyboard sheet from the new timings
```

Then check the following:
- `AUDIO_ALIGNMENT.json → script_comparison.differences` must be empty.
- `phrase_assignment_method` must still read `PUNCTUATION_CHUNKS_MATCH_MEASURED_PAUSES_1_TO_1` (21 phrases = 21 shots). If it reads `FALLBACK_…`, the TTS paused differently; fix the shot ↔ phrase mapping in `build/shots.py` by hand.
- Re-verify the pronunciation by listening, update `pronunciation_gate.json` → `result`, and only then freeze keyframes.
- Never edit the MP3. Place a copy beside the original in `audio_analysis/source_audio/`.

## 1. Output spec

| Item | Value |
|---|---|
| Canvas | 1080×1920, 30 fps, frame = round(seconds × 30) |
| Duration | audio frames + 8-frame end hold. Current file: 1582 + 8 = **1590 frames** |
| Audio | `audio_analysis/source_audio/TTSOL-…-154730.mp3`, SHA256 `f4a9e22d…7b33`, 52.728 s, −20.6 LUFS (raise toward about −14 LUFS in the mix only) |
| Safe zones | Essential text/diagrams within x 60–960 and y 180–1520. Shorts UI covers the bottom ~320 px and the right ~110 px column |
| Font | `Avenir Next` 700/800 (installed on this Mac). Every label is live `<text>`. If rendering elsewhere, load an equivalent and re-check widths |
| Palette | `build/style.py` tokens (see `STYLE_GUIDE.md`) |

## 2. Package map

| Path | Contents |
|---|---|
| `custom_scenes/SCN_*.svg/.png` | 17 hero frames (start/hero state of each composition) |
| `custom_scenes/SCN_*.layout.json` | Exact rebuild data: z-ordered world instances (asset_id + SVG transform + pose/expression/feet/scale/flip for characters), camera transform, screen-fixed UI |
| `SCENE_ASSET_MAP.csv` | 21 shots × 25 columns: frames, narration, understanding, composition, poses, layers, methods, asset IDs, facts, qualifiers |
| `characters/main/remy_rig.json` | Joints, parts, hierarchy, transform rule, slots, angle limits, hands, expressions, **19 poses with resolved joint degrees** |
| `characters/main/parts|hands|faces|expressions|poses/` | Rig parts in one rest frame, 10 hand drawings, 22 face components, 15 expression heads, 19 pose renders |
| `characters/supporting/` | Store associate (assoc-1): head, torso, 3 expressions, 3 poses, `associate_rig.json` |
| `props/`, `props/sofa_layers/` | 40 prop files (26 base designs + states), sofa split into 7 occlusion layers |
| `environments/`, `environments/layers/` | Store, checkout, living room, navy stage, paper macro; every kit also split into layers |
| `diagrams/`, `diagrams/layers/` | 6 diagram compositions; each layer is a separate full-frame transparent SVG in reveal order |
| `typography/` | Caption plate, qualifier strip, headline, 8 label pills, `CAPTIONS.json` (39 chunks, provisional) |
| `contact_sheets/` | Pose, expression, gaze/tilt, hands, rig-pivot, associate, props, environments, diagrams, storyboard, phone-scale sheets |
| `manifests/asset_manifest.json`, `ASSET_REGISTER.csv` | 244 records: anchor/pivot, layers, occlusion, compatibility, usage, provenance, SHA256, QA |
| `build/` | Generators, so any asset can be regenerated deterministically (`python3 build/build_assets.py`) |

## 3. Rebuilding a scene in Remotion

1. Load `SCN_<id>.layout.json`. Render `world[]` in ascending `z` inside a `camera` group. Apply `camera` if it isn't `none`. Render `ui[]` outside the camera (screen-fixed).
2. Each instance is `<g transform={instance.transform}>{asset SVG inner}</g>`. Prop and diagram SVGs are drawn around their documented anchor, so the transform positions that anchor. Environment and diagram layers are full-frame (transform `none`).
3. **Characters:** don't animate the flattened pose SVGs. Rebuild with the rig (section 4) from `pose`, `expr`, `feet`, `scale` and `flip`. The pose SVG is the visual target for that state.
4. Captions are procedural. Use `typography/CAPTIONS.json` with the `TYP_CAPTION_PLATE` style.

## 4. Rig: Remy (remy-2)

- One rest frame: `viewBox 0 0 640 1060`, ground y = 1030, ground point (314, 1030). Every part file in `characters/main/parts/` is drawn already in place.
- Transform rule: `world = parent · translate(pivot) · rotate(angle) · translate(−pivot)`. Hierarchy: `root → translate(0, body_dy) → legs (hip→knee→ankle)` and `upper_body = rotate(lean @ hip_c) → neck, torso, head (rotate neck @ neck), arms (shoulder→elbow→wrist→hand)`.
- Hand: `forearm · rotate(wrist @ wri) · translate(wri) · rotate(90) [· scale(1,−1) if flip]`. Hand files are authored with the wrist at the origin, fingers pointing +x and thumb toward −y.
- Angles are SVG degrees: positive = clockwise; `lean +` = forward (toward screen-right). Values in `poses.*` are normalized to ±180° for shortest-path tweening. Suggested limits are in the JSON.
- **Layer slots, back to front:** `legF, legN, armF, neck, torso, head, mid, armN, prop, top`. Poses can override slots: sitting puts the legs in `mid`.
- **Held props:** sandwich them. `hand_*` (`grip_back`/`pen_back`) → prop (`prop` slot) → `hand_*_front` (`grip_front`/`pen_front`, `top` slot). Offer sheet, statement and card attach to the upper body; pen and marker attach to the hand (offsets in the pose JSON).
- **Face:** `CHR_REMY_PART_HEAD_FACE`, then features (eyes, brows, nose, mouth), then `CHR_REMY_PART_HAIR` on top. Gaze adds (dx, dy) ≤ 6 px to both eye centres. Expressions and hand shapes are **step switches** at the extreme frame of a move. Never morph between different-topology paths.
- **No lip-sync.** Remy is an on-screen shopper; the narrator is off-screen.
- **Tweening:** interpolate angles, `lean`, `neck` and `body_dy` over 6–12 frames with ease-in-out. Add a 2–3-frame settle on big moves. Hold readable poses at least 12 frames.
- **Walk:** alternate `walk_a` / `walk_b` (plus mirrored legs) every 6 frames, with a 6 px body bob.
- **Mirror** a character with `scale(−1, 1)` on its root (the `flip: true` instances).
- **Store associate:** same skeleton and API, different design (`build/rig_associate.py`). Always mirrored to face Remy.

## 5. Shot keyframe intent (provisional frames; anchors are DTW word estimates)

| Shot (frames) | Keyframes and states |
|---|---|
| **S01A** 0–41, C01A | f0–14: sign swings in from above (rotate about string tops, −8°→0°, ≤3° overshoot). f2–16: Remy rises from below the frame. f10–20: arms ease into `shrug`, expression `confused`. Hold through "interest?" f13–34. |
| **S01B** 41–100, C01B | Cut on the pause. f44–60: statement slides up into the grip; arms switch to `hold_bill` at f58, expression `concerned`. f80–91 ("bill?"): interest row pulse (scale 1→1.04→1). |
| **S02A** 100–175, C02 | Cut to the store. f100–150: Remy walks in from x≈−150 to x=250, then settles in `stand_neutral`/`curious`. f133 ("sofa"): associate switches to `assoc_present`. Qualifier strip visible from f105. |
| **S02B** 175–268, C03 | Cut. Sheet already in hand. Reveal groups in order: `offer_headline` f182, **`offer_if` f200 ("if")**, `offer_condition` f208–242. f182–250: slow camera push toward the sheet (≤1.2). |
| **S03** 268–332, C04 | Match cut from the sheet's IF to the switch lever. f272–290: arm slides in from the left. Fingertip contact f289 ("“if”" f289–296). Lever press of 4 px at f292–296, then hold. |
| **S04A** 332–378, C05 | Cut to the stage. Title pop f341 ("deferred" f345). Balance card slides in f345–360. Remy in `think_chin`. |
| **S04B** 378–441 | Month strip staggers in (2 f/month) f383–412. `ledger_receipt_rows_01` f383 → `_03` f400 → `_06` f421 (mask down). `ledger_purchase_day` + link f412 ("purchase"). |
| **S04C** 441–507 | Remy → `point_across` at the clip f448. `ledger_not_charged` pops f476 ("charged"). |
| **S05A** 507–617, C06A | Four coins drop from the `release` hand to the card (10-frame arcs) at f520/545/570/595. `balance_fill` width steps 0.75→0.5→0.25→0 and reaches 0 by f600, before "deadline," f596. Flag pops f596. |
| **S05B** 617–672, C06B | WAIVED stamp hits f650 ("waived."): scale 1.6→1 in 5 f plus a 2-frame settle. Remy → `relieved` f652. Receipt fades f660–672. |
| **S06A** 672–719, C07A | Coral rewind wipe f672–680 marks an *alternative* path. Title pops f681. Calendar page flip f690–700. Remainder pulse f694–714 ("unpaid,"). |
| **S06B** 719–805, C07B | Receipt (rows 12) drops onto the statement, ease-in, f731–750 ("accumulated"). Statement swaps `empty`→`charged` at f750. Remy → `shocked` f752. CHARGED stamp f787 ("bill."). No explosion. |
| **S07A** 805–869, C08 | Magnifier slides over the remainder f814–835. Label pops f851 ("left:"). |
| **S07B** 869–988, C09 | Bars build left→right f876–919 (3 f stagger), chips follow. Bracket draws f919–940 ("balances" f919), then arrow + receipt. Gold arrow draws right→left f950–975. Sofa icon pops f970 ("sofa."). Remy walks right→left at the bottom. |
| **S08** 988–1097, C10 | Twelve ticks pop (3 f stagger) f997–1032 ("minimum" f1024). Remainder + flag highlight f1069–1088 ("time."). Expression `focused`→`concerned` f1076. |
| **S09A** 1097–1197, C11 | Left panel builds f1105–1130, right panel f1136–1170. **"APR" ≈ f1156: re-time after the corrected MP3.** Remy in `open_hands`. |
| **S09B** 1197–1314 | Right-column highlight f1204–1230. X over the rewind arrow f1239–1267. "Interest may start after the promo period" stays visible until the cut. |
| **S10A** 1314–1376, C12 | Cut home. Marker circle stroke draws f1351–1371 ("deadline,"). Remy in `circle_marker`. |
| **S10B** 1376–1437 | PAYMENT DUE card pop f1381. EVERY MONTH label f1400 ("monthly"). ONE DEADLINE label f1417 ("date."). |
| **S11** 1437–1508, C13 | Sofa settle (scaleY 0.98→1) f1445–1455. Remy seated (`sit_relaxed`). DAY 1 tag pops f1485 ("day"). |
| **S12** 1508–1590, C14 | Camera refit to the C14 camera, f1508–1540. Receipt + clock reveal f1541 ("waiting"). Clock minute hand ticks backward once f1551–1560. Remy → `sit_notice` f1545. Qualifier fades in f1560. Hold to f1590. |

Transitions are hard cuts at phrase-pause midpoints unless noted: the match cut S02B→S03, the rewind wipe at S06A, and the camera refits.

## 6. Object handoffs and occlusion

- **S01B statement → hands:** the statement enters as a free prop. At the grip frame, switch to the pose prop (`held_statement`, upper-body attached) inside the hand sandwich.
- **S05A coins:** each coin starts at the `release` hand fingertip (`scenes.char_point`). It ends occluded *behind* the balance card's top edge (draw coin under the card for the last 3 frames).
- **S06B receipt → statement:** the receipt is drawn above the statement while falling, then stays partly over the statement header.
- **Sofa scenes:** `PRP_SOFA_L_shadow, legs, back, seat` → Remy → `arm_left, arm_right, pillow` (→ receipt/clock in C14).
- **Checkout:** the associate is drawn *before* `ENV_CHECKOUT_L_CHECKOUT_COUNTER`, which hides them below the waist.

## 7. Captions, qualifiers, facts

- `typography/CAPTIONS.json`: 39 chunks of ≤4 words or ≤20 characters, no orphan single words. Plate centred at x=540, y≈1430, Avenir Next 800 at 56 px.
- On-screen qualifiers per shot are in `SCENE_ASSET_MAP.csv` (`onscreen_qualifier`). Keep these visible:
  - F2 "Illustrative offer • U.S. store card" in S02A/B.
  - F8 "Interest may start after the promo period" in S09B.
  - F10 "Deferred interest • waived only if paid in full on time" in S12.
- **Never** label the deferred offer "0%", add dollar amounts, rates or dates, or claim that every minimum schedule fails.

## 8. What Claude may and may not create

**May create procedurally:** captions, masks/clip paths, stroke-dash draws, the rewind wipe, simple motion trails, soft shadows, transition geometry.

**May not:** replace the illustrated scenes with generic cards, draw a different Remy, add competitor-style characters, or invent new financial claims.

**Must reuse:** Remy, the associate and all props come from this library. If a needed state is missing, extend the generators in `build/` and re-run the build so provenance and hashes stay complete.

## 9. QA limitations to respect

See `ASSET_QA.md`. In short:
- No human art-director or listening review yet.
- Word anchors are ASR-DTW estimates; phrase edges are measured.
- remy-2 hair is a refined rendering of the Phase 1 curls and needs owner sign-off.
- Hands are stylised mittens with simple anatomy. They're good at video scale but not close-up portrait quality.
- Remy sits in 3/4 view on a front-facing sofa, which is cartoon licence.
- Some diagram labels are 20–24 px. Check them on a phone before publishing.
