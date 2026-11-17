# Animation QA — provisional muted preview

Status: ANIMATED_PREVIEW_READY_FOR_REVIEW · SCRIPT_OR_AUDIO_APPROVAL_REQUIRED · clinical review pending.

- Output: `Dr_Rehan_Heart_Warning_PREVIEW_MUTED.mp4` — 1080×1920, 30 fps, 1365 frames, 45.5 s, H.264, no audio track, "PROVISIONAL PREVIEW · MUTED · NOT FOR PUBLICATION" band.
- Timing: cues placed on word times from the owner MP3 (`AUDIO_ALIGNMENT.json`). Audio intentionally not muxed (approvals pending).
- States: 17 narrative states animated in handoff order. `S08-HOLD` excluded from every render.
- Assets: only existing `exports/assets/*.png` layers per KEYFRAME_HANDOFF.json positions; no new artwork, no originals modified.
- Operations: CUT, POSE_SWITCH (S02-B doctor, S06-B adult), POP_IN (9 f, pivot on anchor), SLIDE_IN (12 f, S05 man/woman), TRANSLATE (S06-B cuff, 18 f), DIAGRAM_BUILD (coronary overlay down, plaque up, flow right; 18 f each, staggered 0.6 s), TEXT_REVEAL (title then body band, 12 f wipe), CAMERA_PUSH per state (world layers only; text cards fixed, diagrams ≤1.05), WIPE_8F at location changes.
- Cadence: new visual event every ~0.5–2.5 s; longest no-change hold is S07-D end card (~5.5 s, slow push) carrying the emergency instruction.

## Checks done (sampled stills + contact sheet)
- Pops/pose switches pivot on feet/prop anchors → no foot slide or drift; glucose kit stays in hand; faces not detached (composites used, no separate pupil/nose motion).
- Diagram builds reveal stated layers only; no beat, ECG, test result or growth animation.
- Text never overlaps faces; one new label at a time; cards readable at 360×640 contact-sheet scale.
- Emergency instruction (S03-C, S01-B, S07-D) present; no booking/appointment treatment of acute symptoms.

## Known issues / not verified
- Not reviewed by a clinician or the owner; no claim of medical sign-off.
- Full motion watched only via sampled frames, not end-to-end playback by a human.
- S04-B/S05/S06 states are 1.3–1.8 s each (fast speech) — label read time is tight; S05/S06 body text carries across A→B to compensate.
- Cream text cards on cream stage have low card contrast (existing asset design).
- No music/SFX (only after approved audio; none licensed).
