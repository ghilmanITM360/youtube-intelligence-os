# Focused Codex handoff — reference-critical corrections only (2026-11-21)
Do NOT regenerate the batch. Everything approved stays untouched (7 reference-critical + heads/legs/master). Corrected art goes to a new staging dir; Claude validates, reviews (fresh independent reviewer, SHA-256 bound) and registers with `--supersede`.
Matrix: `../SCENE_ASSET_MATRIX.md`. Frames: `../FRAME_REFERENCES/10nEByVLya0/`.

## 1. Hips set — needed by SH008, SH010, SH012, SH015 (blocks 4 shots)
Files: char_body_hips, rig_arm_left_hips, rig_arm_right_hips, rig_torso. Design the **whole silhouette first** from landmarks (px at 1080×1920, SH010 f647), then split into layers:
neck (535,950) · shoulders (533,1004)/(538,1003) · elbows (490,1018)/(585,1026) outward · hand tips (528,1046)/(565,1046): forearm angles down-inward, **ending short of the spine** (gap, no contact, no triangle loop) · hip fork (532,1125) · feet (480,1172)/(594,1180) · stroke ≈5 px, round caps, flat black #080808.
Note: this corrects my earlier spec (shoulders 15 % / hands at pelvis) — measured values above supersede it. The v2 anchor contract (shoulder 16 %) does not fit this pose; keep the arm pivot at the measured shoulder and declare it in staging_meta (`contract` override) so the validator can check it. A polyline prototype of this pose is in scratchpad `mx/hips_landmark_proto.png`.
Torso defects to remove (review FAIL): flanges, wide collar block y≈450-500 (2048 canvas), hard cut at the leg fork. Arm defects: curl hooks, centre meeting.
Accept when: composite over rig_legs + approved head (neutral and happy) matches SH010 within ~10 px at every landmark and shows no artifact at 300 % zoom.

## 2. Earth — needed by SH004 and SH018
First deliver ONE coherent master illustration (flat, outlined navy/mid-blue ocean patches + green land + white clouds, SH018 f1132), have it approved, then extract layers. Needed layers: body; **spiral-eye face (missing; two white ellipse eyes with black spirals, wavy mouth)**; two-eye neutral face with a real neutral mouth (SH004 f303-338); sweat face (larger, thicker spirals + blue drop; SH004 f339+); flames.
Flames (currently PARTIAL, reviewer-4): keep the 3-tone structure; remove ~5 k edge-fringe pixels per flame (alpha trim / decontaminate), match orange to ≈(216,120,26) and a single shared yellow, blunter rounded drooping tips with S-curl (reference flames have no black outline). Flames should overlap/clip the globe rim as in SH018 (≈ one third over the rim).
Motion note: SH018 alternates two drawings of the whole Earth every 10 frames; supply a second ±3 px jittered variant only if cheap (otherwise Claude jitters in the renderer).

## 3. Not requested now
Arms up/down/shrug/point, heads, brown-hair man, calendar icon, bubble layer: lower priority; ask only after 1 and 2 land. (Calendar icon and brown-hair man are reference-required but absent from the library — separate small requests.)
