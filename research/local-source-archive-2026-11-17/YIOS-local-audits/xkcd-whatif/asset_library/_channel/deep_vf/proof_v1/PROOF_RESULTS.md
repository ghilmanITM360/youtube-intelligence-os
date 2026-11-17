# 8 s silent proof v1 — results (owner-authorized render, LOCAL ONLY)

## What was built
- **Brief:** DEEP_VF_ADDENDUM_v1 §9.
- **Editable source:** `timeline_v1.json`. It holds the events, geometry for both layouts, colours and text, and both exports render from this one file.
- **Renderer and verifier:** `~/YIOS-local-audits/tooling/asset_library/xkcd/render_proof.py` and `verify_proof.py`.
  - They use Python/PIL with ffmpeg libx264 (CRF 12, yuv420p).
  - Nothing was installed.
  - No paid service was used.
- **Original placeholders:**
  - our own question ("What if the Moon were a ball of ice?");
  - our own narrator design ("Pip": a rounded-square head with an antenna dot);
  - our own card style;
  - our own night scene and glow plate.
  - No source logo, card or character was used. The source's red title/end card style was deliberately left out.
- **Outputs:**
  - `proof_16x9.mp4`: 1920×1080, 192 f, 8.000 s.
  - `proof_9x16.mp4`: 1080×1920, 192 f, 8.000 s.
  - `keyframes_*.png`: keyframe sheets for human review.
  - `preencode_*.json`: per-frame changed pixels, red pixels and layout boxes.
  - `VERIFY.json`: all measured values.
  - `attempt1/`: the first render, kept as a record.

## Attempt history
1. **Attempt 1: FAIL on frame review.** Three defects were found by viewing the keyframes:
   - the 16:9 question text overflowed the card;
   - the 16:9 red circle was off the crack;
   - the 9:16 narrator was squashed under the board, with the lower 40% empty and "STEAM" overlapping the moon.

   After adding the automated layout check, I re-rendered attempt 1 into scratch. The check flagged the two measurable defects (card overflow, STEAM overlap); the composition defect needs human judgment.
2. **Attempt 2:** only the geometry was edited in the timeline, with the edit recorded in `_revision`. The keyframes were viewed again and no defect was seen. The automated layout check found 0 defects in both layouts.

## Per-criterion verdict (attempt 2)
| Criterion | 16:9 | 9:16 | How measured |
|---|---|---|---|
| P1 every pop changes on exactly 1 frame | PASS | PASS | Pre-encode: changed pixels >0 on the event frame and 0 on the next frame. Post-encode MAD at pops 0.13–1.3 (cut 213/199), next frame 0.000–0.002 |
| P2 dissolve linear over 6 f | PASS: steps 0.172/0.165/0.166/0.173/0.163/0.161 | PASS: 0.162–0.176 | Decoded progress against the frames before and after |
| P3 no overshoot | PASS (≤1.0) | PASS | Decoded progress |
| P4 canvas #F8 ±2, stroke 7–9 px | PASS #F8F8F8, 8 px | PASS #F6F6F6, 8 px | Modal colour of decoded frame 59; dark run across the board edge |
| P5 red only on the emphasis layer | PASS: 0 red px before f108 and after f132; 3600 px during | PASS (4628 px) | Pre-encode native RGB mask |
| Red-circle pop, native colour | PASS: ROI red px f106–f110 = 0, 0, 3576, 3576, 3576 | PASS: 0, 0, 4601, 4600, 4600 | Decoded HSV red in the circle ROI |
| (same frame, greyscale) | mean luma diff 0.237; 0.18% of pixels change ≥12 | 0.304; 0.23% | Shows why grey-only detectors miss this event |
| P6 holds dead still | PASS: pre-encode 0 changed px on 140 hold frames; post MAD max 0.0009 | PASS: 179 frames; 0.0019 | Pre-encode exact, post-encode tolerance <0.5 |
| P7 24 fps CFR, frame count, decode | PASS: h264 yuv420p 24/1, 192 frames, 8.000 s, 0 decode errors | PASS | ffprobe -count_frames plus a full ffmpeg decode |
| Clipping/overlap | PASS: 0 defects | PASS: 0 defects | Element bounding boxes against a 16 px safe margin, and text against other elements |
| P8 human keyframe and playback review | **PENDING_HUMAN** | **PENDING_HUMAN** | The model viewed the keyframe sheets. **No real-time playback capability was available in this session.** |
| P9 HumanCraft scorecard ≥4 | **PENDING_HUMAN** (not self-scored) | **PENDING_HUMAN** | — |
| Audio sync, listening, final AV | **BLOCKED/PENDING**: the proof is silent and no narration exists | same | — |

**Render verdict: both exports pass every machine-checkable criterion (P1–P7, the native-colour red pop, clipping). The proof is not accepted yet:**
- **P8 human playback review and P9 are pending;**
- **AV acceptance is pending.**

Nothing here is a final or AV sign-off.
