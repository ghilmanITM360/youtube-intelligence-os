# Independent visual QA: Codex provisional rig in V1 Rent (R6)

Reviewer: independent QA agent, read-only except this file. Frames extracted with ffmpeg into a scratch folder (not in the project). Baselines: `out_r4/V1_RENT_R4_0-75s_v4.mp4`, `out_r5/V1_RENT_R5_75-122s_v2.mp4` (frozen, not touched).

## Verdicts

| File | Verdict |
|---|---|
| `out_r6/INTEGRATION_TEST_codexrig_19s.mp4` | PASS WITH FIXES (test clip; frames sampled, shares the same assets) |
| `out_r6/V1_RENT_R6_0-75s_codexrig_v1.mp4` | PASS WITH FIXES (no P1; 3 P2) |
| `out_r6/V1_RENT_R6_75-122s_codexrig_v1.mp4` | PASS WITH FIXES (no P1; same P2 items) |

Basis: no blocking defect found. Graphics, text, figures, source tags and audio are unchanged versus the frozen baselines. The provisional host is acceptable for production testing, but the expression set and the torso colour need a Codex pass before the host can replace the baseline permanently.

## Verified clean (evidence-based)

- Content invariance: for 19 matched timestamps in the 0-75 file and 10 in the 75-122 file (29 pairs), a pixel diff (luma threshold 40) of R6 against the baseline shows differences only inside the host box. No differing pixels at x >= 800 on any white-canvas frame. The one exception is a single 2 px speck at (1506,166) on the 19 s room frame, which is codec noise on the plate. Figures (2.8%, 2.7%, about 3%), source tags ("Source: BLS, CPI release Oct 14, 2026, Table 1", Zillow tag, BLS factsheet tag), labels and the RENT bill are identical.
- Audio: decoded PCM MD5 of R6 equals baseline for both segments (0-75: 9920006e9318376d664d441cc89deba7; 75-122: efbcec5acbd6e4ddc25dfe8215a81511). Durations 75.000 s / 47.300 s for audio and video in both, same frame counts (2250 / 1419; test clip 576 frames, 19.200 s). Full decode `-f null` returned no errors for all three files.
- Neck join (head chin (350,651) to body neck (650,70) / point (750,70)): no gap, seam or offset visible at 3x zoom on down, shrug and point bodies. A small skin-tone neck sliver shows under the chin on all three. Head bbox identical on all five heads (13,82,687,667), so no head-to-head jitter.
- Proportion: head about 585 px over about 1750 px figure height = 0.33 (target 0.31-0.38). Passes.
- Point arm (R side, 0.34 scale, x up to about 515): never reaches the bars (starts x about 855), calendar, house or text. No collision.
- Fringe/halo: none seen on #FDFDFD (colour histogram around the figure shows only bg, ink, skin, olive, hair) or on the cream room plate at 19 and 21 s. No clipping at frame edges or by other layers. The room feet at y about 980 are fully on the floor.
- Identity: same face shape, hair, ear and skin tone on all five heads and three bodies; consistent from 0.5 s to the end of the second segment.
- Grammar: host changes happen only on hard cuts or as stepped swaps (12.0 to 13.7 s neutral to smirk, 30.4 to 31.5 s smirk to worried); no bobbing, no lip sync, no tween.
- Join at 75.0 s: last frame of the 0-75 file (down/smile, 0.46) and first frame of the 75-122 file (down/smile, 0.46) are the same host state, same position; the missing title text in the first frame of segment 2 is identical in the baseline (title pops at 75.3 s).

## Defects

| # | Sev | Asset | Where (time in file) | Finding | Codex fix |
|---|---|---|---|---|---|
| 1 | P2 | `rig_head_worried.png` | 0-75: 19-22.5 s (room, 0.5), 31.5-32.9 s (shrug, 0.34) | Reads as "puzzled/unsure", not worried: brows only slightly tilted, tiny wavy mouth. At 640x360 (checked at 31.8 s) it is almost indistinguishable from neutral. The frozen baseline worried face read clearly. The room beat's emotional line ("why does rent feel bigger?") loses punch. | Stronger inner-brow raise and brow tilt, larger downturned or wobbly mouth; keep chin anchor and bbox. |
| 2 | P2 | `rig_head_smirk.png` vs `rig_head_smile.png` | 12.0 s (13.7 swap), 14.3, 22.5, 70.3 s; 75-122 file 104.5 s (29.5 in file) | Smirk is a small one-sided curve; smile is a small symmetric curve. At 200 px head height (heads_200 test) they can be told apart only on close inspection; at 640x360 they merge. Neutral vs smirk also close (flat line vs short curve). | Make the smirk clearly asymmetric (one corner up, one brow raised) and enlarge both mouth strokes about 1.5x. |
| 3 | P2 | `rig_body_down/shrug/point.png` | all appearances | Torso reads almost entirely as black ink with only a narrow olive stripe (olive #5B6B3A fills a thin band about one third of torso width); arms and legs are heavy ink columns. Baseline had a broad olive shirt. Identity colour of the character is weakened and the body looks thinner than the baseline. Accepted by the "provisional/geometric" rating in principle, but the olive shirt is a palette identity item. | Widen the olive fill so the shirt reads olive, keep outline 1.2-2.2%. Not blocking. |
| 4 | P2 (minor) | `rig_head_worried.png` with room caption box | 17.9-22.5 s (room) | Hair and right ear touch the left edge of the caption box ("Why does rent feel bigger?") at x about 760-770, y about 120-200. The baseline touched less. No text is covered. | Either move host x by about 30 px or tolerate; not a Codex asset issue (layout). |
| 5 | P3 | scale | 3.1-12 s, 14.3-17.2 s, 22.5-39.9 s, 70.3-72.4 s vs 0.46 beats | Host switches between 0.46 (down/shrug at hook, 12 s, 16.5 s, 39.9 s, 63.7 s, 72.4 s, 75 s, 103.6 s) and 0.34 (point, mid beats) and 0.5 (room). Still visibly different sizes; the character remains thin. Known accepted P3. | None. |
| 6 | P3 | `rig_body_point.png` | 3.1-5.4, 14.3, 22.5-27.5, 32.9, 70.3 s; 84.7 s | Pointing arm is a single straight line, hand a tiny wedge; body leans slightly (torso offset by the 750 neck). Reads as pointing, less expressive than the baseline round hand. Geometric contours as rated PARTIAL. | None for now. |
| 7 | P3 | all bodies | all | Contours geometric, neck very short, hands tiny in shrug (small curled shapes). Accepted provisional. | None. |
| 8 | P3 | `rig_head_surprised.png` | 63.7-66.5 s | Small "o" mouth and raised brows; readable at full size, weaker at 640x360. Acceptable. | None. |

No P1 (blocking) defect found.

## Expression test results (5 heads)

- Full size: neutral (flat mouth), smile (clear U), surprised (o-mouth) are distinct. Worried and smirk are the weak pair (see 1, 2).
- 200 px head width composite: surprised and smile clear; neutral/smirk/worried separable only by the mouth shape and need attention. At 640x360 whole frame (31.8 s sample) the worried head looks neutral.

## Frames inspected

0-75 file (R6 vs R4 side by side, pixel-diffed): 0.5, 4, 12.5, 13.9, 14.8, 17.2, 19, 21, 23, 26, 28, 31, 31.8, 33.5, 40.5, 64.5, 71, 73.5, 74.9, last frame (74.96). Visually read on screen: 0.5, 4, 12.5, 13.9, 14.8, 17.2, 19 (R6 only), 21, 23 (R6 only), 26, 28, 31, 31.8, 33.5, 40.5, 64.5, 71, 73.5. Pixel-diff only: 74.9.
75-122 file (R6 vs R5): 0.0, 0.3, 4, 10.5, 14, 20, 29.5, 35, 44.5, 46, first frame. Visually read: 4, 10.5, 29.5, 44.5; pixel-diff only: 0.0, 0.3, 14, 20, 35, 46 (14, 20, 35 have no host; zero difference from baseline). Join: last frame 0-75 vs first frame 75-122.
Integration test clip: frames extracted at 0.5, 5, 8, 10, 12, 14, 17, 18.5 s but not viewed individually; the clip uses the same assets and frame ranges that were viewed in the two full files, so its verdict is inferred, not independently read frame by frame. Rig assets inspected: 5 heads (full size composite and 200 px composite), 3 bodies (bbox and anchors from `v1r4_assets/rig/rig_anchors.json`), 3x crops of down/shrug/point necks and the room head.

## Could not check

- Motion/timing between sampled frames (only still frames sampled; stepped swaps confirmed from the renderer source and from before/after samples at 12.5/13.9 and 31/31.8).
- Frames between 33.5-63.7 s have no host and were not part of the check beyond the pixel diff of the sampled stills.
- Pixel-level anti-aliasing at 4K or on non-sRGB players; judged on 1080p decoded stills only.
- Exact intensity of fringe on the cream plate beyond visual zoom.
