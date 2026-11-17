# 8 s silent proof — attempt 3 (owner-requested revision, LOCAL ONLY)

Attempt 2 is preserved unchanged in `../proof_v1/`.

## What changed from attempt 2
- **Editable source:** `timeline_a3.json`. It is a copy of attempt 2's timeline; the changes are recorded in `_revision`.
- **9:16 opening:**
  - a short question, "Moon made of ice?", pops at f6 (0.25 s), inside the board;
  - in attempt 2, nothing appeared before the moon pop at f60 (2.5 s).
- **Label states (both layouts):**
  - `MELTING` pops on the same frame as meltwater drips hanging from the night moon (`state: MELT_DRIPS`, f150);
  - `STEAM` pops on the same frame as three steam wisps rising from the moon (`state: STEAM_WISPS`, f160).
  - Before this, each label popped over an unchanged moon.
- **Tools:**
  - `render_proof_a3.py` and `verify_proof_a3.py` are new copies;
  - the attempt-2 tools are not edited.

## Per-criterion verdict (attempt 3)
| Criterion | 16:9 | 9:16 |
|---|---|---|
| P1 every pop changes on exactly 1 frame (pre-encode, exact) | PASS | PASS (includes the short-question pop at f6) |
| P2 dissolve linear over 6 frames | PASS: steps 0.161–0.173 | PASS: 0.160–0.176 |
| P3 no overshoot | PASS | PASS |
| P4 canvas / stroke | PASS: #F8F8F8, 8 px | PASS: #F6F6F6, 8 px |
| P5 red only on the emphasis layer | PASS | PASS |
| Red circle, native colour (ROI red px f106–f110) | PASS: 0, 0, 3576, 3576, 3576; grey diff 0.237 | PASS: 0, 0, 4601, 4600, 4600; grey diff 0.304 |
| P6 holds still | PASS: pre-encode 0 px on 140 frames; post MAD ≤ 0.0015 | PASS: 178 frames; ≤ 0.0045 |
| P7 24 fps CFR, 192 f, 8.000 s, 0 decode errors | PASS | PASS |
| Clipping / overlap (16 px margin, label against element) | PASS: 0 defects | PASS: 0 defects (`short_q` included) |
| A3 opening inside first second (>2000 px change vs f0 before f24) | PASS: from f2 (card) | PASS: from f6 (short question) |
| A3 label backed by a state change (changed px outside the label box ≥ 1500 on the pop frame) | PASS: MELTING 3561, STEAM 2240 | PASS: MELTING 4306, STEAM 2966 |
| P8 human keyframe and playback review | **PENDING_HUMAN** | **PENDING_HUMAN** |
| P9 HumanCraft scorecard | **PENDING_HUMAN** | **PENDING_HUMAN** |
| Audio sync / final AV | BLOCKED/PENDING | BLOCKED/PENDING |

## How the state-change check was revised
- **First run:** the A3 state check also required **0** changed pixels on the frame after the pop, measured post-encode. It failed on x264 residue of 10–57 px (16:9: 16 and 10; 9:16: 0 and 57).
- **Revision:** that clause was dropped, and the change is recorded in the tool.
- **Why this is still covered:** the one-frame property is still enforced exactly by P1 on the pre-encode frames (0 px on the next frame), and by P6 after encoding.

## Review status
- **What the model reviewed:** the keyframe sheets `keyframes_16x9.png` and `keyframes_9x16.png`. No defect was seen.
- **Still small:** the drips and wisps are small next to the moon. A human playback review should judge whether they read as "clear" at real size.
- **Playback:** no real-time playback capability was available, so P8/P9 stay pending until a human watches both MP4s.

## Files
- `proof_16x9.mp4`: sha256 92c85f73d8397e383d8e3dd74944c6fa0886a9d94dc17a7cc023ec89769f539f
- `proof_9x16.mp4`: sha256 aab0b65d536366eac1d3980f67520b93559f0abb51aa795c3c35a24c8e628e7e
- `VERIFY.json`, `preencode_*.json`, `keyframes_*.png`

**Verdict:** both exports pass every machine-checkable criterion. They are **not accepted** until P8, P9 and AV are done. This is not a final or AV sign-off.
