# Running After 60 — V3 motion QA (review version)

Output: `Running_After_60_V3_REVIEW.mp4` (+ `_MOBILE_540x960.mp4`), built by `../project_v3.py` with `tools/anim_v3.py` and `tools/rig.py`.
V2 is unchanged. The rig method, colours and references are the same as HIIT; see `01_HIIT_AFTER_60/animation/v3/MOTION_QA_V3.md`.

## Defect (V2) and root cause
- One leg appeared raised while the other stayed down. `sam-run-warm` has one rigid `legs` SVG part (a fixed running pose) that only rocked ±3.5°.
- Neither leg ever completed a stride, and the arms were rigid.

## V3 gait (`rig.RunRig()` defaults, cycle 0.68 s ≈ 176 steps/min easy run; Hamner et al. 2010 report a 0.683 s cycle)
The eight requested checkpoints, by leg phase. The left leg (image-left hip) is phase p and the right leg is p+0.5.

| # | Event | Phase |
|---|---|---|
| 1 | Right-foot stance, left-leg swing | p 0.50–0.90 |
| 2 | Right-foot push-off: heel rises, toes plantarflex to 28° | p ≈ 0.80–0.90 |
| 3 | Flight: no foot on the ground | p 0.90–1.00 |
| 4 | Left-foot heel-first landing, then stance | p 0.00–0.40 |
| 5 | Right-leg heel recovery and swing-through | p 0.00–0.50 |
| 6 | Left-foot push-off | p ≈ 0.30–0.40 |
| 7 | Flight | p 0.40–0.50 |
| 8 | Back to checkpoint 1 | p = 1.00 equals p = 0.00 exactly (loop closure 0 px) |

- **Arms:** contralateral, elbow bent 76–104°, swing biased forward (−16°…+32°).
- **Body:** vertical oscillation 6 asset px (≈6.6 screen px), lowest at mid-stance.
- **Ground:** marks move at the stance-foot speed, so the planted foot does not slide against the visible ground. The S01 tree parallax is kept from V2.
- The S01 cadence still eases to 0.55× before Sam stops on "However" (V2 timing).

## Checks run
**Rig self-check** (`qa/RIG_CHECK_V3.json`):

| Check | Result |
|---|---|
| Stance ground-contact error | 0 px |
| Stance slip | 0 px |
| Thigh/shin length error | 0 px |
| Loop closure | 0 px |
| Knee flexion | 40–108° (both legs) |
| Max joint step per 1/240 cycle | 1.84 px |

The self-check also asserts that a foot never goes below the ground.

**Encoded-video temporal review** (`tools/motion_qa_v3.py` on the MP4):
- `GAIT_PHASES_V3.png` / `qa/run_S1_PHASES.png`: 8 even phases of one cycle (t=0.68–1.275 s), plus the −1/0/+1 frames at both contacts, both toe-offs and the loop boundary.
- `qa/run_S1_SEQUENCE.png`: every frame of two cycles (41 frames).
- `qa/run_S8_PHASES.png` / `_SEQUENCE.png`: the run-on in S08, where the root travels.
- **Observed:**
  - No stationary leg.
  - No permanently airborne foot.
  - The knee never bends backwards.
  - No detached limbs.
  - No pop at contacts or at the loop boundary.
  - The heart on Sam's chest (hook) stays attached through the bounce.
- The S08 "contact 0.00 −1f" cell shows the planned cut from the standing pose to the runner.

**Before/after:** `MOTION_V2_V3.png`.

**Render QA** (`RENDER_QA_V3.json`):

| Check | Result |
|---|---|
| Duration | 31.933 s, 1080×1920, 30 fps |
| Decode errors | none |
| A/V delta | 0.000 s |
| Peak | −1.0 dBFS |
| Blank frames | 0 |
| `CAPTIONS_V3.srt` | byte-identical to V2 |
| Narration | original, unedited |

The only large-frame-change flags are 0.1 s and 2.5 s, the bar entrance and exit.

## Red opening headline bar
- **Text:** "RUNNING AFTER 60" / "GOOD OR BAD?" on two lines. The em dash became the line break.
- **Look:** same component as HIIT: red (206,32,41), Arial Black in white, x 60–1020, top y 160.
- **Timing:** 0–2.66 s (frames 0–79), ending with the opening sentence "Running, I'll give you 7 out of 10". It enters with a 6-frame fade and settle, and exits with an 8-frame fade and lift.
- It matches the spoken topic: the speaker rates running 7/10, calls it very good, then raises knee/ankle caution.

## Still open
- Frame-by-frame inspection only; no human has viewed it at playback speed.
- The park path wave versus the straight contact line is the same as V2.
- Human listening for "of the blood", clinical review R3/R5/R7 and owner approval remain open.
