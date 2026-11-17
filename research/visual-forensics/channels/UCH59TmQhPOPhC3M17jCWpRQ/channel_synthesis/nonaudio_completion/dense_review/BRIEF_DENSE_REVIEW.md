# Dense interval visual review — reviewer brief (NAC, one video per reviewer)

You are a fresh, bounded visual reviewer. Inputs ONLY:
- `packs_local_only/<VID>/<VID>_P###.jpg` — each row = one previously-uninspected interval. Left label: interval_id, state, frames start-end, n frames, automated class (CAM/LOC/BOTH/STATIC = measured pixel/affine classification, NOT a visual name). Tiles: `pre` = frame before, then start, 1/3, 2/3, end, `post` = frame after. Tile frame numbers in blue. Tiles are 220x124 downscales.
- `PACK_INDEX_<VID>.csv` (which tiles were sampled).

For EVERY row on EVERY sheet, append one CSV line to `DENSE_REVIEW_<VID>_v1.csv` (create with header if absent):
`interval_id,sheet,event_name,event_class,what_changes,evidence_label,confidence,needs_native_crop,note`
- event_class: one of SHOT_CUT, INTRA_SHOT_STATE, CAMERA, DIGITAL_ZOOM, GRAPHIC_TEXT, CHARACTER, LIGHT_COLOR, STATIC_HOLD, MIXED (use MIXED with `+`-joined classes in what_changes, e.g. CAMERA+GRAPHIC_TEXT).
- event_name: short concrete name (e.g. "whip-slide to next panel", "text scales in", "fade to black", "eyes swap to bloodshot", "hold, no visible change").
- evidence_label: OBSERVED (seen in tiles) or INFERRED (between tiles, not seen). Anything happening between sampled tiles is unseen: say so.
- confidence: HIGH / MED / LOW. needs_native_crop: YES when tiles are too small/too sparse to name the change (tiny text, subtle motion, long interval with only 4 interior tiles).
- If the automated class disagrees with what you see (e.g. STATIC but something visibly changed), say `CLASS_DISAGREE` in note.

Rules: describe only what is visible; do not invent audio or intent. Write after EACH sheet (append, do not hold rows in memory). Process sheets in order P001.. If you must stop, the CSV shows where. Do not open any other files. Final reply: ≤120 words — rows written, sheets done, count of needs_native_crop=YES, count CLASS_DISAGREE, any systematic issue.
