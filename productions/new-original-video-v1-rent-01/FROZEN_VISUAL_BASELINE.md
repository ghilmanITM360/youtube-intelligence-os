# Frozen temporary visual baseline (2026-11-21)
Status: FROZEN on independent QA PASS (no P1/P2): `out_r5/INDEPENDENT_QA_R4v4_R5v2.md`. Temporary because the host is placeholder art; final Codex rig will re-render the same beats, not redesign them.

| Segment | File | sha256 |
|---|---|---|
| 0-75 s | `out_r4/V1_RENT_R4_0-75s_v4.mp4` | 8501627ac0fbf32ce3c628e064664699011d8e732d88df04c6912c76d7f3a37b |
| 75.0-122.3 s | `out_r5/V1_RENT_R5_75-122s_v2.mp4` | a288a4388aeaf096ad86aa1573e5322807f9d5af89362570eca7179bd1a5d548 |

Preserved, untouched: R3 `out/V1_RENT_segment_0-75s_take2.mp4` (a40bbccc147368b49c7af10060c537225f4f6c1c1d25fb8e83ec8ba74577516c); R4 v1-v3 in `out_r4/`; R5 v1 in `out_r5/`; all review reports.
Unchanged builders: `tools/v1r4_render.py`, `tools/v1r5_seg2.py`. Segment 122.72-255.14 s remains unused (unsupported narration).
Accepted P3s (no further iteration): source tags unreadable at 360 px width; stepper shows Jan, Feb only; small red index "6"; some arrow tails touch labels; placeholder host scales/torso; room beat 4.6 s; Helvetica source face.

## Codex integration requirements (3 poses, 5 heads)
Renderer reads `v1r4_assets/rig/` first (else `v1r4_assets/provisional/`). Required files: `rig_body_{down,shrug,point}.png`, `rig_head_{neutral,smile,worried,surprised,smirk}.png`, `rig_anchors.json`.
- RGBA PNG, transparent, flat fills. Body canvases 1300x1300 (point 1500x1300); heads 700x700.
- Figure height 1800 px: head 0.31-0.38 of it (target 0.34), limb line 2-3% (about 45 px), outline 1.2-2.2%, torso olive #5B6B3A, ink #1F2430.
- Anchors: the renderer expects a flat JSON keyed by file name: `{"rig_body_down.png":{"neck":[x,y],"size":[w,h]}, "rig_head_smile.png":{"chin":[x,y],"size":[w,h]}, ...}`. Placeholder values: body neck (650,70), head chin (350,650).
- The renderer places the feet at `neck_y + 1165*scale`, so body sole must sit about 1165 px below the neck anchor (placeholder: neck y=70, soles about 1235). If Codex bodies differ, give the neck-to-sole distance and I change that one constant.
- Any head on any body within 6 px; identical chin across the 5 heads; same neck across bodies (point body may offset x, but state it in the anchor).
- Current Codex `provisional_family/rig_anchors.json` is nested (`heads{}`/`bodies{}`), the point neck is (750,70), the head chin is (350,651). It is valid content but needs either a flat file or a 5-line adapter in `host_img`. Not integrated: Codex master is PARTIAL (geometric outlines), pending the owner's separate coordination.
- Acceptance after drop-in: re-render both segments, rerun the stills check at 1080p and 640 px, confirm alignment, no halo on #FDFDFD, five heads distinguishable at 200 px.
