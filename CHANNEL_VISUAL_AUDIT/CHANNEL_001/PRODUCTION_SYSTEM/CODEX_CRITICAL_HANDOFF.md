# Codex critical handoff v2 — measured geometry (2026-11-21)
Supersedes `CODEX_CRITICAL_HANDOFF_v1_superseded.md`. Every number below was measured on the source MP4 `10nEByVLya0` (1080×1920) — **do not invent proportions or poses; reproduce these**. Machine-readable data: `rig_measurements/hips_landmarks.json`. Geometry reference art (NOT final art, do not ship): `rig_measurements/prototype/*.png` (layers on the 2048 canvas) and `prototype/sheet.png` (source | prototype | diff).
Do NOT resubmit anything outside this list. Staging folder for the answer: a new `assets_codex/qa/correction_staging/final_pass/geometry_v3/` (do not touch `method_change/`).

## What was wrong (corrected facts)
1. The rig contract put the shoulder at 16 % of the torso. Measured: **29 %** (50 of 173 source px below the head bottom) on 12 frames of SH008/010/012/015, and the same 46–50 px below the head bottom in SH004 at identical head height (184 px). New contract **v3** = v2 neck/hip, shoulder (1024, 559). Your v2 hips arms started at y≈436 — ~120 canvas px too high.
2. Hands in the hips pose stop at **54–55 % of the torso** (canvas y≈764–774), they do **not** reach the pelvis. Hand-bottom band in the contract: 47–62 %.
3. The approved `rig_legs` (narrow straight inverted-V, 601 canvas px tall) does **not** match the reference. The reference legs are short and splayed: fork→feet ≈ 54 source px = **≈258 canvas px tall × ≈544 wide**.
4. The approved heads (`char_head_*`) are a brown-haired tan character. The reference man in SH008/010/012/015/020/022 is a **different, black-haired, peach character**. Only SH004 shows the brown-haired man.
5. Within each hips shot the man is perfectly static (hard cut in, no arm or face change; only SH008 differs from the other three: right arm swung out, "variant B"). No arm swaps exist.

## Scale (use exactly)
Rig canvas 2048². 1 source px = **4.775 canvas px**. Spine x = 1024 (source 535.5). Neck (head-bottom) (1024, 320). Hip fork (1024, 1146) (source y 1126). Stroke ≈ 4.5 source px = **≈21 canvas px**, uniform, round caps, black ≈(14,14,14), hand-drawn marker wobble ±2 px allowed, no fills in the body.
Tolerance for every landmark: **±10 canvas px**.

## P1 — Black-haired man hips set (needed by SH008, SH010, SH012, SH015)
Layers (all 2048² RGBA, transparent outside the stroke; torso/arms/legs separate files so the renderer can swap SH008's arm):
| file | landmarks (canvas px, from the spine origin (1024,320)) |
|---|---|
| `rig_torso` | straight line (1024,320) → (1010,1146); thin, no collar, no dome, no flanges, no hard cut; ends exactly at the leg fork |
| `rig_arm_left_hips` | shoulder (1022,559) → elbow (797,630) → hand tip (983,774). Hand tip stops **≈19 px (4 src px) short of the spine** |
| `rig_arm_right_hips` (variant A, SH010/012/015) | shoulder (1036,559) → elbow (1256,669) → hand tip (1170,764). Hand tip ≈ **138 px (29 src px) away from the spine** (asymmetric on purpose) |
| `rig_arm_right_hips_B` (SH008 only) | shoulder (1036,564) → elbow (1165,759) → hand tip (1365,802) |
| `rig_legs_hips` | fork (1010,1146); left leg curves out through (940,1210),(845,1290) to a small foot hook at ≈(759,1366); right leg through (1090,1200),(1230,1310) to ≈(1303,1404). Height 258, width ≈544 |
Pose reads: elbows pointing out, forearms returning toward the spine — "hands on hips" at chest-lower height, exactly like `prototype/sheet.png` (middle panel).

## P1 — Black-haired man heads (SH008 + SH010 happy; SH012 + SH015 neutral; SH020 open-mouth, SH022 smiling: later)
1024² head canvas, **neck anchor (521,887)**, head visible height **729 px**, width ≈710 (source 179×184). Peach fill ≈(250,212,180), black outline ≈20 px (5 src px), spiky black scribble hair over the upper-left of the head (src x 462–595, y 765–825), eye dots r≈20 px at source (508,836) and (568,826), happy mouth = long smile curve src (497,874)→(540,898)→(566,897), neutral mouth = flat line src (505,887)→(577,886). Head placement in the rig: scale **1.205** so head height = 879 canvas px (contract v3 `head_scale`).

## P2 — Earth for SH018 (and SH004)
Reference: `FRAME_REFERENCES` SH018 frames 1110/1120. The reference Earth is a detailed illustration (navy ocean ≈(20,40,90) with deep blue swirls, green land ≈(65,125,60), white ice caps, thick black outline), **not** a flat globe. Master illustration first (one full image, approval before layers), then layers: `prop_earth_body`, `prop_earth_face_spiral` (two white oval eyes with black spirals, a pale curved mouth/tongue stroke), `prop_earth_face_neutral`, `prop_earth_face_sweat` (blue drop), and flames.
SH018 state geometry: two states alternate every 10 frames. Earth+flames bbox is x 65–974 in state 1 and x 48–983 in state 2 (≈3 % larger) and the flame shapes differ → **deliver flames in two variants A/B** (left & right) plus the Earth body; do not add fades or flicker.
Flames: orange ≈(216,120,26) fill, shared yellow core ≈(240,200,60) with a pale highlight, blunt rounded tips, black-free, **no edge fringe/halo pixels**, bottom-left flame hugging the lower-left of the globe, top-right flame leaning right off the globe edge.
SH004 Earth: slides in from the right f303-319; sweat face from f339; bbox of the whole shot x 118–924.

## P3 — Brown-haired man for SH004 (shrug, waist-up crop)
Head 212×184 src px (brown swoop hair, tan skin ≈(205,170,130), dot eyes, small mouth), neck y=1049, shoulder y≈1095. Body is **cropped**: torso visible from the neck down to source y=1260 (≥211 px), no hips/legs. Arms (source px): left shoulder (527,1098) → elbow (484,1160) → hand (404,1128); right shoulder (536,1100) → elbow (598,1152) → hand (642,1068). Uncertainty ±4 px. Torso length beyond the crop is unknown — draw the torso to the crop line only.

## P4 — Calendar icon (SH005, SH017) ≈125×125 px: rounded square, red top band with two ring marks, white body with a 3×2 grid of red dots, thick black outline; a small hand-lettered "June" label sits above it (the label is text, not part of the icon). Source position SH005: x≈132–260, y≈905–1029.

## P5 — SH003 bubble layer + burst particles. Teal bubble grows f155→f229 (bbox 313×303 → 493×475, centre ≈(536,955)); burst at f230: radial particles within bbox x 290–814, y 748–1166. Deliver (a) a bubble disc, (b) one burst frame of ~10–14 particles. One frame is enough (the burst lasts 1 frame).

## Explicitly NOT requested
Everything else in the 33-asset batch (down/up/point arms, remaining heads, master sheet variants, extra faces). Do not regenerate approved assets: `prop_qcircle`, `prop_chart_screen`, `prop_moneybag_pair`, `prop_dollar_sign`, the brown-haired heads, `char_body_down`, `char_master_sheet`.

## Validation you can self-run
`python3 pipeline.py validate <dir> --contract v3` (v3 checks: arms reach the shoulder anchor (1024,559); hips hand-bottom within 47–62 % of the torso; legs 200–340 px tall). Put `"contract": "v3"` in each `staging_meta.json` entry (a per-entry contract overrides the CLI flag) plus author/provenance/generator/source. New names (`char_head_black_*`, `rig_arm_right_hips_B`, `rig_legs_hips`, `prop_earth_face_spiral`, `char_man_brown_*`, `prop_calendar`, `prop_burst`) are not in the schema yet — the schema entries are added when the files arrive; reuse existing IDs where one exists (`rig_torso`, `rig_arm_*_hips`).
