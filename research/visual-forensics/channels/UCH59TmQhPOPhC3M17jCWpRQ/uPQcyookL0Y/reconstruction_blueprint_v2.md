# Reconstruction blueprint v2 (ORIGINAL production guidance) — derived from uPQcyookL0Y evidence
v1 blueprint preserved. Observations cite visual_ct_scan_report_v2.md; everything here is a production PROPOSAL for new original work.

## Asset library (original)
1. One original narrator character kit: outlined head, textured hair mass, flat torso, stick arms; 2 mouth states, 2 eye states (swap-based, M5).
2. Teacher/classroom set: board, pointer, projector, desk — for "explainer" cutaways (observed 13–14 states use this family).
3. White-card template 1920x1080 #fcfcfc, ink #050505, upright rounded handwritten-class font (licensed/original).
4. Flat-fill scene backgrounds with dark outlines; globe/map assets for scale cuts.

## Motion modules (frame counts at 29.97 fps; spec: production_specs/specifications_v2_1.json)
M1 clip reveal 3–6 f · M2 trailing-end slide 6–7 f · M3 pop+overshoot peak at +2 f · M4 fades 4–5 f, collapse 3–4 f · M5 single-frame swaps · M6 edge entries 3–4 f · M7 digital push/pan.

## Edit structure (from v1 + v4 pacing, MEASURED)
Median state 4.2 s, ~10.9 states/min, narration ~140 wpm (ASR). Countdown list: title card per rank (white card + chapter number) → establishing scale shot (globe/map) → 3–5 consequence visuals → classroom/explainer beat → comic character beat.

## Per-state prompts
89/89 rows (see report §1); each lists static anchors and do-not-change rules; on-screen text uses placeholders.

## QA checklist
Frame-count tolerances ±1 f per module (evaluate_rt01.py pattern); text never morphs; character IDs persist; no source characters, drawings or wording; audio cues NOT specified (listening blocked).

## Reconstruction test status
RT-01 PASS (M1/M3/M5 timing, geometry, palette); style fidelity not specified in v2 → added in v2.1, untested. Full-scene tests (layout boxes, classroom set) PENDING.
