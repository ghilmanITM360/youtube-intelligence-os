# R13 blind interval review — reviewer brief (frozen 2026-11-05, before the review)

You are an independent reviewer. You have not seen and must not open any earlier review, ledger or report for these videos.

## Sources (identity frozen; you do not need to open the MP4s)

| video | sha256 | frames (CFR 30000/1001) |
|---|---|---|
| uPQcyookL0Y | 1416669f10d7231f8110eb27044986912984dcdbacbd7d9f6440726349a0c69d | 14647 |
| mNLNb-Z4T0M | e6799e8f16ad31772020d98404f2c9cf90536a255c6169d29e838c55bd1dd061 | 16689 |
| GNaBxt_zIRA | cbe7a3afac6c6b7b13db10b7ce2493715f5299208d6f3ebffb7fd74e2bf5c0f7 | 16319 |

## Inputs ONLY

- `BLIND_SHEET_INDEX_FOR_REVIEWER.csv`: one row per interval (video, sheet, interval_id, frames shown, crop box).
- `sheets_local_only/<VID>_B###.jpg`: each block is one interval, up to 8 native-resolution frames of it (all frames for short intervals, else 8 evenly spaced, including one frame before and after). Frame numbers are in blue. A crop of `0-1919x0-1079` is the full frame.

Open no other file.

## Frozen criteria

For EVERY interval, append one line to `BLIND_REVIEW_B2.csv` (create it with this header if absent):
`video,interval_id,sheet,event_class,event_name,what_changes,camera_move,frames_seen,evidence_label,confidence,note`

- `event_class`: exactly one of SHOT_CUT (different shot/artwork replaces the frame), INTRA_SHOT_STATE (same shot, a discrete state change such as a scene element swap), CAMERA (the whole framing moves/scales together), DIGITAL_ZOOM (discontinuous one-frame reframe of the same artwork), GRAPHIC_TEXT, CHARACTER, LIGHT_COLOR, STATIC_HOLD (nothing visible changes), MIXED (two or more of these).
- `camera_move`: one of NONE, PAN, ZOOM_IN, ZOOM_OUT, PUNCH_IN, SHAKE, UNSURE. Judge it by whether background and foreground elements shift/scale together across the shown frames. Compare first vs last tile edges and fixed background objects. If the change is too small to judge, write UNSURE, not a guess.
- `evidence_label`: OBSERVED for changes visible in the shown frames; INFERRED_BETWEEN_SAMPLES for anything assumed to happen between sampled frames.
- `confidence`: HIGH, MED or LOW.
- Name concretely with frame numbers, e.g. "red label pops in at f4654, holds, pops out by f4681".
- Describe only what is visible. Do not guess intent or audio.

Append after EACH sheet. Final reply (≤80 words): rows written, and counts per event_class and per camera_move.
