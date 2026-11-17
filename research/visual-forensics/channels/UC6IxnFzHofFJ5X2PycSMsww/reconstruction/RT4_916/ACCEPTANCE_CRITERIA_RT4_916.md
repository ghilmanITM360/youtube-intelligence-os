# RT4_916 — portrait 9:16 Short reconstruction: ACCEPTANCE CRITERIA (frozen before any render)
Frozen 2026-11-05T19:30Z-ish (see sha256 file written immediately after; render attempts only after that). Source manual: v0.7 sha bb5e76f2da25…; sections 6, 8, 9.
Scope: ORIGINAL silent animatic, portrait only. A PASS here is a portrait-rhythm/format PASS; it does NOT carry over to landscape/long-form (RT3) nor to narration sync, audio, or story quality.
Attempts: max 3. Every attempt dir (attempt_N/) and its measured result is preserved, including failures; criteria are not edited after the first render.
Measured (same segmenter/eval pipeline as source videos):
- M1 format 1080x1920, r_frame_rate 24/1, exactly 1440 frames (60 s), CFR, libx264 yuv420p.
- M2 events/min 17.9–28.2 (manual Shorts n=9 measured range).
- M3 median HOLD 1.44–2.84 s.
- M4 intended events matched to measured ACTIVITY onsets within ±2 frames: ≥ 80 %, and 0 unexplained measured events beyond intended + 2.
- M5 no series/title card and no end card: first frame is subject drawing/board, last segment is not a full-frame card (visual check, sheet).
Visual (primary viewer: orchestrator reads ≥2 render sheets/frames, records what is seen):
- V1 vertical composition uses the 9:16 canvas: either ≥2 stacked panels or a landscape panel in the upper half; a persistent anchor (scale/timer/map band) stays on screen on ≥ 90 % of sampled frames.
- V2 no text/object clipped by frame edges; text within x 60..1020, y 120..1700 (my chosen safe zone; hypothesis, not a measured platform rule).
- V3 original identity (pebble narrator, teal #1F8A8A, no stick figure/red/dinosaur/'what if'); objects more detailed than narrator.
- V4 no overlapping text/object collisions.
Not testable: narration sync, audio, loudness (silent). Verdict labels: RT4_916_PASS_PORTRAIT (all M and V pass), PARTIAL (list failures), FAIL.
