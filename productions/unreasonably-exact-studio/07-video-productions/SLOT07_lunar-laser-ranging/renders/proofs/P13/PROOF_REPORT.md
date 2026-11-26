# P13 Narration-aligned sample, B17-B21 (code part)

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: narration_t 37.00-48.90 (B16 tail, B17-B21). yes 37.90, left 39.58, trick. 43.96, redirect 44.91, tiny fraction 45.59-46.2, light 46.92, back 46.98, from. 48.31

## Expected behaviour

Ghost mirror + dot-built question mark (B16 end state) -> on 'yes' the ghost dissolves and the real reflector array (10 x 10 dark-glass faces, aluminium frame, bright base; placeholder geometry) pops into the SAME place with a thin ring. Camera (Camera2D, log zoom) pulls back with 4-layer parallax (stars .08, ridge .30, ground .75, array 1.0); on 'left' the array settles with a damped tilt and ballistic dust arcs (low-g look, no billowing). A push-in glides one cube face onto the screen centre and dissolves, centred on 'trick.', into the neutral cutaway whose aperture circle it matches. Rays enter staggered from 'redirect', the key ray exits on 'light'; on 'tiny fraction' a magnified inset shows the wide beam footprint with the array as a tiny marker (no numbers; main-frame rays keep returning in full); on 'back' the third-face inset gives way to a small flat-mirror A/B inset (ray sent away); on 'from.' guide ticks land and all three exit rays line up with their entry rays together.

## Files

- `P13_B17-B21_narration_aligned.mp4` (540x960, 30 fps, 389 frames, h264 yuv420p)
- `P13_B17-B21_narration_aligned_audio_preview.mp4` (same video + slice of the master voice, preview only; master untouched)
- `P13_B17-B21_narration_aligned_start.png`, `P13_B17-B21_narration_aligned_middle.png`, `P13_B17-B21_narration_aligned_end.png`, `P13_B17-B21_narration_aligned_frame_stats.json`
- `cue_P13_B17-B21_narration_aligned_yes_real_array.png` (cue "yes_real_array", narration_t 39.14 s, frame 33)
- `cue_P13_B17-B21_narration_aligned_left_settle_dust.png` (cue "left_settle_dust", narration_t 41.23 s, frame 96)
- `cue_P13_B17-B21_narration_aligned_push_mid.png` (cue "push_mid", narration_t 44.74 s, frame 201)
- `cue_P13_B17-B21_narration_aligned_trick_cutaway.png` (cue "trick_cutaway", narration_t 45.91 s, frame 236)
- `cue_P13_B17-B21_narration_aligned_redirect_ray1.png` (cue "redirect_ray1", narration_t 46.57 s, frame 256)
- `cue_P13_B17-B21_narration_aligned_tiny_fraction_inset.png` (cue "tiny_fraction_inset", narration_t 47.61 s, frame 287)
- `cue_P13_B17-B21_narration_aligned_light_key_ray_exits.png` (cue "light_key_ray_exits", narration_t 48.70 s, frame 320)
- `cue_P13_B17-B21_narration_aligned_back_mirror_inset.png` (cue "back_mirror_inset", narration_t 49.27 s, frame 337)
- `cue_P13_B17-B21_narration_aligned_from_aligned.png` (cue "from_aligned", narration_t 50.78 s, frame 382)
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p13.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P13
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P13_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P13_B17-B21_narration_aligned: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 389 of 389 expected |
| P13_B17-B21_narration_aligned: frame-to-frame change | info | mean abs diff 2.942, max 27.744, min 0.000 (0-255 luma, 1/4 res); frames with ~no change: 40 of 389; max pixel luma 240; max step of mean luma 9.79 |
| event times are the beat-map anchor / word times | PASS | yes 39.14; left 41.23; trick. 45.91; light 48.70; from. 50.53 |
| ASSERT exit rays antiparallel to entry rays for the three rays shown | PASS | dots [-1.0, -1.0, -1.0] |
| key ray reaches its exit end exactly on "light" (48.70 s) | PASS | enters 47.47, exits 48.70; first ray enters 46.92 (word "redirect" 46.57) |
| match dissolve registration: cube face centre -> cutaway aperture centre (px error) | PASS | face centre (540.00, 932.55) vs aperture (540, 932.5); face radius 452.5 vs aperture half-width 452.5 design units |
| parallax: apparent shift / camera shift equals each layer factor (stars .08, ridge .30, ground .75, array 1.0) | PASS | {'stars': 0.08, 'ridge': 0.3, 'ground': 0.75, 'array': 1.0} |
| overscan: every layer covers the camera path (assert, B16-B19 push) | PASS | min margin per layer {'stars': 636, 'ridge': 1390, 'ground': 806} |
| dust follows parabolic arcs (a_x = 0, apex = v^2/2g), no billowing | PASS | apex 1245.314 vs 1245.314 ; max a_x 1.14e-13 ; g = 175 units/s^2 |
| before "yes": ghost mirror visible, no array faces; after: array faces present, ghost gone | PASS | ghost px 1076 -> 130 ; face px 1689 -> 8935 |

## Start / middle / end frames

P13_B17-B21_narration_aligned

![P13_B17-B21_narration_aligned start](P13_B17-B21_narration_aligned_start.png)
![P13_B17-B21_narration_aligned middle](P13_B17-B21_narration_aligned_middle.png)
![P13_B17-B21_narration_aligned end](P13_B17-B21_narration_aligned_end.png)

## Defects I found by viewing frames

- v1: the three ray origins at y=1520 sat under the caption scrim and were hidden.
- v1: the thin ring ping on 'yes' crossed the array's own faces and looked like a glossy circle over the object.
- v1: at the fastest part of the push-in (43.3-43.4 s) the cube grid strobed: frame-to-frame luma difference 63.6 (all other proofs <6) and the screen flashed to light grey metal.
- v1: the A/B mirror inset was too small to read and the final hold showed three equally bright ray pairs crossing.
- v1: ridge/ground layer extents failed the overscan assertion (the first overscan test I ran) because their extents were band-shaped.
- Open: ALL lunar art is procedural placeholder (array looks like a waffle iron, ground is flat, no astronaut); B18's astronaut sequence is not in this clip; the cube-to-cutaway change is a dissolve, not a true shape morph; the cutaway rays still cross in the middle during B20; the dissolve drops mean luma 62 -> 20 within 0.35 s (a single dip of 8.9/255 per frame, no flashing, but abrupt); only stills and decoded MP4 frames viewed.

## Corrections made

- Cutaway lifted (apex 480, ray origins at y=1370, above the caption band) via p07.build(); ring ping starts outside the array (r 262-440); 7-sample temporal motion blur (0.9 frame shutter) added to the renderer and used on this clip, macro metal darkened: max frame diff 63.6 -> 39.5; mirror inset radius 120 with larger strokes; at 'from.' only the key pair stays lit (others 30%); layer extents may be open on a side (sky above ridge) and the overscan assertion now passes with real margins.

## Re-test result

- Re-rendered; decoded MP4 frames at 5.5-7.3 s (push + dissolve) and stills at 8.5-11.7 s viewed: blur reads as a camera push, registration of face circle and aperture is within 0.05 px (check), key ray exits on 'light' (check). All checks PASS. Max frame diff still 39.5 because the push is a near-full-frame change; judged acceptable only as a candidate.

## Scientific verification

Optics as in P07 (exact two-reflection geometry, antiparallel asserted; exit offset, not collinear). C06 picture rule is implemented: footprint inset on 'tiny fraction', no numbers, array a tiny marker, and the main frame's ray returns in full with no absorption; the inset fades before the A/B mirror inset so reflect-to-source and tiny-fraction never share visual weight (rule 7). Array: 10 x 10 faces per C05 (Apollo 11/14: 100 cubes, 46 cm panel); film shows one array (Apollo 11). No astronaut is drawn or named (C05 naming still open). Dust gravity is a stylised low-g value, not a physical simulation. ALL ART IN THE LUNAR SCENE IS PLACEHOLDER GEOMETRY, not Codex's final reflector/astronaut art.

## Known defects still open

- B18 astronaut kneel-and-set sequence is NOT in this clip (needs rigged art). The 'left' event is represented by array settle + dust only.
- Lunar scene art is procedural placeholder; final art comes from Codex assets.

---
Status words used: `candidate`. Nothing here is `approved`.
