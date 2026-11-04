# Native-crop verification — reviewer brief (NAC, one video per reviewer)

Inputs ONLY:
- `crops_local_only/<VID>/<VID>_C###.jpg`. Each block is one interval that the dense reviewer flagged `needs_native_crop=YES`. It holds up to 8 frames, either every frame of a short interval or 8 evenly spaced ones, cropped at native resolution to the measured change region. Frame numbers are in blue.
- `DENSE_REVIEW_<VID>_v1.csv`, the dense reviewer's rows. Read only the rows for the interval IDs on your sheets.

For EVERY interval block, append one line to `DENSE_REVIEW_<VID>_v2_crop_corrections.csv` (create it with a header if it is absent):
`interval_id,sheet,v1_event_name,verdict,event_name_v2,event_class_v2,what_changes_v2,frames_seen,evidence_label,confidence,note`
- `verdict` is one of CONFIRMED, CORRECTED or STILL_UNRESOLVED. Use CORRECTED when v1 named the wrong thing or the wrong class.
- `evidence_label`:
  - OBSERVED only for changes visible in the shown frames;
  - INFERRED_BETWEEN_SAMPLES for anything happening between sampled frames of a long interval.
- `event_class_v2` uses the same classes as v1: SHOT_CUT, INTRA_SHOT_STATE, CAMERA, DIGITAL_ZOOM, GRAPHIC_TEXT, CHARACTER, LIGHT_COLOR, STATIC_HOLD or MIXED.
- Name concretely, for example: "medkit prop pops in at f4654, holds, pops out by f4681"; "arrow pointer appears and wiggles 1-frame steps".

Rules:
- Describe only what is visible. Append after EACH sheet.
- Open no other files.

Final reply (≤100 words): rows written, and counts of CONFIRMED, CORRECTED and STILL_UNRESOLVED.
