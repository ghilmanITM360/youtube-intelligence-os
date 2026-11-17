# xkcd's What If? — motion windows (P4, 2026-11-08, LOCAL ONLY)

13 bounded windows (10–21 frames each, 211 frames total, 26 MB JPEG q2) extracted one at a time from SHA-256-verified source MP4s (all 13 `pts_check` OK, 24 fps). Tool: `~/YIOS-local-audits/tooling/asset_library/xkcd/motion_window.py`. Per window: `window.csv` (per-frame metrics), `window.json` (summary + source SHA), `strip.jpg` (all frames).
Metrics (MEASURED on 480-px greyscale): `progress` = projection of each frame onto (last − first); exact for a cross-dissolve, a proxy for strokes and type; unreliable for blurred camera moves. `diff_prev` = mean absolute frame difference (motion/blur energy). `ecc_*` = affine alignment to the first frame (valid only for camera-like moves until blur breaks it).
Strips opened by me: ZOOM_TFhrRrRdUbA_G0130, PAN_SLIDE_WH4g1ptJ-70_G0156. Others were read from the numbers plus the ledger description (labelled accordingly).

| Class | Window | Frames | Curve (progress per frame) | Overshoot / settle | Verdict |
|---|---|---|---|---|---|
| DISSOLVE | 9VG0yqq_PHM G0112 (white → grey night) | 6 | 0.17, 0.34, 0.50, 0.67, 0.83, 1.00 | none; hard stop | MEASURED: exact linear cross-dissolve, 6 frames (0.25 s) |
| DISSOLVE | TFhrRrRdUbA G0152 (fire out, "NOT" in) | 6 | 0.17, 0.33, 0.50, 0.67, 0.83, 1.00 | none | MEASURED: identical linear 6-frame dissolve |
| POSE_SWAP (dissolved) | 2LSyizrk8-0 G0092 (operator leans over keyboard) | 6 | 0.16, 0.33, 0.50, 0.66, 0.83, 1.00 | none | MEASURED: the "ghosted intermediate pose" is the same linear 6-frame dissolve between two drawings, not an in-between |
| POSE_SWAP | UQgw50GQu1A G0024 | 1 | 0 → 1 | frames after are identical (no settle) | MEASURED: 1-frame drawing swap |
| POP_ON | qu8nx1qUwEU G0092 (moon + red halo) | 1 | 0 → 1 | no scale-up, no overshoot, no fade | MEASURED |
| POP_ON | s3oLIDaElaE G0066 (red scribble + scattered letters) | 1 | 0 → 1 | none | MEASURED |
| DRAW_ON_STROKE | r7B0MzvwDcA G0104 (red line L→R + pink fill) | 6 | 0.01, 0.21, 0.41, 0.57, 0.76, 0.96, 1.00 | none | MEASURED proxy: constant-speed write-on (~0.2 of the stroke per frame) |
| DRAW_ON_STROKE | 2LSyizrk8-0 G0018 (red zigzag scribble) | 10 | 0.01, 0.04, 0.12, 0.24, 0.34, 0.45, 0.61, 0.75, 0.94, 1.00 | none | MEASURED proxy: slow first 2-3 frames then steady (ease-in start) |
| DRAW_ON_TYPE | WH4g1ptJ-70 G0178 ("MAN" → "MANILA" + magenta dot) | 7 + late dot | stepwise: 0.18, 0.32, 0.53, 0.58, 0.65, 0.79, hold 4 f, 0.87, 1.00 | none | MEASURED proxy + ledger: letters appear about one per frame, then a hold, then the city dot pops |
| DRAW_ON_TYPE | lLlwvmu1ZeA G0092 ("≈ 1") | 8 + late step | 0.13, 0.21, 0.32, 0.43, 0.58, 0.68, 0.77, 0.81, hold 5 f, 0.91, 1.00 | none | MEASURED proxy: hand-written strokes on at near-constant speed, a short pause, a final element |
| PAN_SLIDE (whip pan) | WH4g1ptJ-70 G0156 (map, Asia → Africa) | 12 | blur energy diff_prev 27, 32, 33, 34, 34, 36, 36, 33, 29, 26, 24, 20 | crisp landing, no overshoot | OBSERVED (strip) + MEASURED energy: horizontal motion blur, speed ramps up fast, peaks mid, decelerates; ease-in-out |
| PAN_SLIDE (scroll) | EsUBRd1O2dU G0016 (panel scrolls up) | 10 | 0.07, 0.17, 0.32, 0.46, 0.50, 0.63, 0.79, 0.94, 1.00 | none | MEASURED proxy: near-linear with soft start; vertical motion blur (ledger) |
| ZOOM (out) | TFhrRrRdUbA G0130 (museum shrinks, giant shape enters) | 10 | 0.02, 0.06, 0.13, 0.21, 0.34, 0.54, 0.80, 0.92, 0.98, 1.00; ECC scale 0.98 → 0.63 by f3029 | none, hard settle | OBSERVED (strip) + MEASURED: S-curve ease-in-out, directional blur in the middle frames, scale anchored near lower-left |
| ZOOM (in) | 2LSyizrk8-0 G0132 (into speech bubble) | 9 | 0.58, 0.71, 0.74, 0.80, 0.91, 0.97, 1.00 | none | MEASURED proxy (ECC fails on blur): big first-frame jump then deceleration = ease-out |

## What this tells the clone (INFERRED from the 13 windows)
- No overshoot and no bounce anywhere (0/13). Settles are hard stops. A "pop with overshoot" preset would be OFF-style.
- Most changes have no motion at all: pop-on and pose swap are 1-frame cuts of a drawing.
- Dissolves are exactly linear and 6 frames; the channel also uses that same dissolve between two poses.
- Write-ons run at roughly constant speed (≈0.2 of a stroke per frame for short strokes; 1 letter per frame for typing), sometimes with a slow first 2 frames.
- Camera moves (whip pan, scroll, zoom) last 9–12 frames, use directional motion blur, and ease in-out or ease-out. They are the only eased motion.
- Limits: 13 windows, 1–2 per class; easing labels describe output shape, not the creator's software curves. Blur makes ECC fail mid-move, so camera curves are energy/proxy based (ESTIMATED).
