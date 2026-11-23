# CF reference 10nEByVLya0 — 22-shot asset requirements matrix (2026-11-21)
Evidence: FRAME_REFERENCES (22 proof frames viewed), SCENE_BLUEPRINTS state tables, per-frame diff of the source MP4 (`motion` column), registry + hash-bound reviews.
Legend: ✔ approved (registry) · ◐ PARTIAL · ✖ FAIL · ∅ no asset exists · 3P third-party media (provenance = owner decision; stand-in panel only).

| Shot | f | Visible assets | Poses/expr | Earth | Motion observed | Today |
|---|---|---|---|---|---|---|
| SH001 | 0-98 | qcircle ✔ ×5 scrolling, chart ✔ | – | – | linear scroll 72 px/s, pop-in chart; 78% frames change, runs ≤4 (24 fps phase) | **RENDERS, matches** |
| SH002 | 99-153 | chart ✔, moneybag ✔, qcircle ✔ ×4 | – | – | cut + staggered pops | **RENDERS, matches** |
| SH003 | 154-253 | dollar ✔; teal bubble (procedural); burst particles ∅ | – | – | bubble grows f155-229, burst f230 (1 frame), cut | partial (bubble approx, no particles) |
| SH004 | 254-365 | brown-hair man ∅; Earth body ◐ + 2-eye face ◐ + sweat face ◐ | man, Earth slides in f303-319, sweat f339 | yes | hard cut, slide-in, pose swap | **blocked** (man ∅, Earth ◐) |
| SH005 | 366-439 | text "2007/2008", red arrow (procedural), calendar ∅ | – | – | pop-in calendar f405 | partial (calendar ∅) |
| SH006 | 440-476 | 3P Wall St sign + 2 clips | – | – | – | stand-in only |
| SH007 | 477-510 | 3P fire meme + text | – | – | – | stand-in only |
| SH008 | 511-540 | black-hair man, **hips pose** (head: black-hair happy — NOT the approved brown heads) | hips **variant B** (right arm swung out); static for all 30 frames | – | static hold (only ≤3 noise px change; the earlier 'micro swaps' were compression noise) | **blocked** (hips ✖) |
| SH009 | 541-630 | 3P Blackstone logo, 2 portraits | – | – | pops f566, f596 | stand-in only |
| SH010 | 631-663 | man **hips** (happy) | hips | – | near static, 6 change frames | **blocked** (hips ✖) |
| SH011 | 664-706 | 3P yacht clip; moneybags (pair ✔ approximates 2+1) | – | – | clip plays (86% frames change, run 14) | stand-in + bags |
| SH012 | 707-729 | man **hips** (neutral) | hips | – | near static | **blocked** (hips ✖) |
| SH013 | 730-779 | 3P cartoon baby + speech bubble | – | – | pop bubble f747 | stand-in only |
| SH014 | 780-824 | 3P cartoon newborn close-up; no caption | – | – | 2 change frames | stand-in only |
| SH015 | 825-849 | man **hips** (neutral) | hips | – | near static | **blocked** (hips ✖) |
| SH016 | 850-1046 | 3P article page, logo, 2 portraits, banknotes drawing | – | – | pops, drifting notes | stand-in only |
| SH017 | 1047-1104 | text timeline + arrows, calendar ∅ | – | – | scroll left f1065-1086 | partial (calendar ∅) |
| SH018 | 1105-1159 | Earth body ◐, **spiral-eye face ∅**, flames ◐ | – | yes | **whole-Earth 2-state boil, switch every 10 frames (1115/1125/1135/1145/1155), no fade, no continuous flicker** | **blocked** |
| SH019 | 1160-1191 | 3P red meme tiles ×6 | – | – | pops | stand-in only |
| SH020 | 1192-1288 | 3P chart screenshot, red arrow, "90%", face (head_shocked ✔ approximates) | open-mouth face | – | arrow draw-on, pops | stand-in + approx |
| SH021 | 1289-1460 | 3P search card, logo, red ellipse | – | – | draw-on ellipse, logo slide-out | stand-in only |
| SH022 | 1461-1659 | 3P table page, check, skyscrapers, crowd clip; smiling man leans in (pointing arm) | peek+point | – | slide-in, sweep, 12-frame bursts | stand-in; man ◐ |

## Asset classification (library of 33 + missing art)
**A — required for the reference** (16 library assets): approved 7 = prop_qcircle (new, this pass), prop_chart_screen, prop_moneybag_pair, prop_dollar_sign, rig_legs, char_head_happy, char_head_neutral. Not approved 9 = char_body_hips ✖, rig_arm_left_hips ✖, rig_arm_right_hips ✖, rig_torso ✖ (hips set; 4 shots), prop_earth_body ◐, prop_earth_face_neutral ◐, prop_earth_face_sweat ◐, prop_earth_flame_left ◐, prop_earth_flame_right ◐ (SH004/SH018). **Also required but not in the library at all:** Earth spiral-eye face (SH018), brown-hair man (SH004; the ledger's "CH_STICKMAN_BROWN" label for SH008+ is wrong — those are black-hair/peach), calendar icon (SH005/017), bubble layer + burst particles (SH003).
**B — original-video production**: char_head_worried ✔, char_head_shocked ✔, char_head_sweat ◐, char_body_down ✔ (earlier approval kept; candidate differs, PARTIAL), char_body_up/shrug/point ◐, arms up/shrug/point ◐, rig_arm_*_down ✖.
**C — optional extended library**: char_master_sheet ✔ (design sheet, not rendered), alternate poses beyond the reference set.
**D — duplicate / superseded**: prop_earth_flames (composite of left+right), legacy char_stick_* ×9, legacy prop_dollar/prop_earth.
Hips is **not optional**: four reference shots use it. Down/up/shrug/point arms are NOT needed for the reference except a pointing arm in SH022.

## Scoreboard
- Reference-critical assets approved vs required: **7 / 16** library assets (+4 art items absent from library).
- Full 33-asset library approved: **11 / 33 IDs registered**; 10 of them match the current candidate file (qcircle, chart, moneybag, dollar, legs, master sheet, 4 heads); char_body_down is registered from an earlier approved file while its current candidate is PARTIAL. 22 IDs are not approved. Unique approved registry IDs = 11 (reviewer-count vs ID reconciliation: 33 reviews exist, one per ID; 4 were re-reviewed this pass because their hash changed).
- Shots reconstructed & visually verified against the reference: **2 / 22** (SH001-002). Partial 3 (SH003, 005, 017). Stand-in-only (3P media) 11. Blocked by art 6 (SH004, 008, 010, 012, 015, 018) + SH022 man.

## Motion verification (source MP4 per-frame diff, 108×192 gray, threshold 0.02)
- Motion is **stepped**: longest consecutive-change run ≤4 frames in 15/22 shots; the 24 fps phase rule is already in the renderer. No easing evidence in character shots: SH008/010/012/015 change on 3-6 isolated frames (stepped micro pose swaps), SH014 2 frames.
- SH018: the **whole Earth alternates between two drawings every 10 frames (3 fps boil)**; 20-frame lag diff (13-62) ≪ 10-frame lag diff (96-134). No fades, no continuous flicker → the earlier "flames fade in / flicker" idea is NOT supported; implement a 2-state alternation (±few px jitter) once the Earth is approved.
- SH004: Earth slide-in f303-319 (constant per-frame change), cut at f254, sweat pop f339.
- Implemented now: stepped motion quantisation, pops, cuts, linear scroll. Not yet implemented: SH018 boil, SH003 burst, SH016 banknote drift.

## Hips landmark measurements (SH010 f647, 1080×1920 px; also SH008/012/015)
neck (535,950) · shoulders (533,1004) L / (538,1003) R = **31 % down the 175-px torso** · elbows (490,1018) L / (585,1026) R · hand tips (528,1046) / (565,1046) = **55 % down**, ≈7 px–35 px **short of the spine** (no contact) · hip fork (532,1125) · feet (480,1172) / (594,1180) · stroke ≈5 px.
**Contract flag:** rig contract v2 puts the shoulder anchor at 16 % of the torso ((454-320)/(1146-320)); SH010 measures 31 %. A diagnostic polyline drawn from the landmarks above reproduces the pose coherently (scratchpad `mx/hips_landmark_proto.png`, not an asset). The contract should be re-examined against ≥2 more poses before more hips art is made.


## Geometry correction (2026-11-21, supersedes the scoreboard above where they differ)
Measured on 12+ frames (`PRODUCTION_SYSTEM/rig_measurements/hips_landmarks.json`; source MP4 frames SH004 f300, SH008 f511-535/520, SH010 f631-660/647, SH012 f707-725/715, SH015 f825-845/835):
- Torso is **identical in every hips frame**: head-bottom y=953, shoulder y=1003 (**50 px = 29 %** of the 173-px torso), hip fork y=1126. SH004 (shrug) shoulder is 46-50 px below its head bottom at the *same* head height (184 px) → the v2 value (16 %) is a shared error, not a pose quirk. SH004's torso is cropped (≥211 px, no legs), so its torso *fraction* is unknown; the neck→shoulder *offset* is what is shared.
- Hips are **static inside each shot** (frame diff ≤3 px). SH008 = variant B (right forearm out to (607,1054)); SH010/012/015 = variant A.
- **Approved `rig_legs` does not match the reference**: v2 legs are 601 canvas px tall (≈126 src px), straight, narrow; the reference legs are ≈54 src px tall (≈258 canvas), splayed and curved, ≈114 src px wide.
- **Approved `char_head_*` are the brown-haired tan character**; SH008/010/012/015/020/022 use a **black-haired peach** man. The approved heads are not reference-matching for those shots (SH004's brown-hair head not yet verified against them).
- Corrected reference-critical scoreboard: approved *and* reference-matching = **4** (qcircle, chart_screen, moneybag_pair, dollar_sign). Approved but not matching the reference character/geometry = 3 (rig_legs, char_head_happy, char_head_neutral). Earlier "7/16" overstated.
- Contract **v3** added (schema `rig_versions.v3`; v1/v2 untouched; same neck/hip as v2): shoulder (1024,559), hips hand-band 47-62 %, legs 200-340 px. Hips prototype (`rig_measurements/hips_proto.py`, `prototype/`): body ink within 3 px of the source for 99.8 % of prototype pixels and 96.7 % of source pixels (SH010) / 96.8 % (SH008 variant B). Prototype layers PASS the v3 validator; the current Codex hips arms FAIL v3 (roots ~120 px too high). Prototype is geometry spec art, not a registered asset.
- SH018 boil implemented as stepped poses (cuts at f1105/1115/1125/1135/1145/1155 verified in the rendered MP4); the content is still a BLOCKED slate (no approved Earth).
