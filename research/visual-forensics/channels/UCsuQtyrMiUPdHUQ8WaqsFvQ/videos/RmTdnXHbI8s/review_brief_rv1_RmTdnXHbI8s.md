# Reviewer brief — Primitive Education visual state review — RmTdnXHbI8s (rv1_RmTdnXHbI8s)

Bounded fresh-context visual reviewer. Work ONLY inside `/Users/ghilmankhan/YIOS-local-audits/primitive-education/videos/RmTdnXHbI8s`. Write ONLY to `/Users/ghilmankhan/YIOS-local-audits/primitive-education/videos/RmTdnXHbI8s/review/rv1_RmTdnXHbI8s/`. No web. No scripts. No other files.

## Inputs
1. `tables/segments_v1.csv` — every frame is in exactly one segment. `HOLD` = measured static; `ACTIVITY` = pixels changed (candidate; may be cut, pose swap, zoom, pop-on, false positive).
2. `tables/sheet_index.csv` — tile → seg, frame, PTS.
3. `frames/sheets/SHEET_01.jpg … ` (17 sheets). Tiles labelled `<seg> <H|A> f<frame> <pts>s`. Green border = HOLD settled last frame; red = ACTIVITY sample.
4. `frames/strips/<seg>.jpg` (2 strips; may be 0) — dense frames of long ACTIVITY segments, labelled frame + changed-fraction.
5. `asr/asr_small_en_segments.csv` — provisional machine ASR (not listening; may contain errors).

**Open every sheet and every strip with the Read tool, one per call, sheets in order. Never claim a view you did not make.** **Read budget: open each image exactly once (no navigation pass, no re-reads unless a specific tile is ambiguous; name that tile in notes). Draft the rows for a sheet immediately after viewing it. Write the output files with the Write tool (not scripts), each once at the end or in at most 3 appends; do not make per-row Edits.**

## Critical classification rule (known failure of automatic detectors on this channel)
Shot cut ≠ pose change ≠ camera move ≠ text event. A stepped or smooth **zoom of the same drawing is CAMERA, not SHOT_CUT**. The same character redrawn in a new pose/expression with same framing is CHARACTER (POSE_SWAP). SHOT_CUT = whole composition replaced by a different subject/setting. If a zoom proceeds in steps, each step is CAMERA (ZOOM_STEP).

Holds with detector `D4` or `D4C` changed gradually (slow move or colour drift); they show first/mid/last tiles: describe the change and keep `STATIC_HOLD` class with subtype `DRIFT_COLOUR` or `DRIFT_MOTION`. Column `enc_artifact_frames` lists compression refreshes, not visible motion; do not treat it as drift.

Tiles sit at different places on a sheet: never infer framing or position change by comparing tiles across rows or columns unless you compare position inside each tile. A hold shows only its last frame; do not report drift from that comparison.

## Output 1 — `annotations.csv`, exact header `seg,event_class,subtype,description,confidence`
One row per segment, same IDs, same order. HOLD rows: `STATIC_HOLD`. ACTIVITY rows: `SHOT_CUT`, `GRAPHIC/TEXT`, `CAMERA`, `CHARACTER`, `LIGHT/COLOR/EFFECT`, `FALSE_POSITIVE`, or `+` combos using these exact strings (the class is literally `GRAPHIC/TEXT`). `subtype` UPPER_SNAKE (e.g. SCENE_SWAP, POSE_SWAP, EXPRESSION_SWAP, ZOOM_STEP, ZOOM_IN, ZOOM_OUT, PAN, POP_ON_OBJECT, POP_ON_TEXT, POP_OFF, SLIDE_ON, SLIDE_OFF, BOUNCE, SCALE_POP, SHAKE, CROSS_DISSOLVE, FADE, OPENING_STATE, ENDING_STATE, HOLD). `description` = literal visible facts: subjects, pose, expression, position (left/right/upper/lower), relative size, readable text in quotes, colours. Unreadable text → `unreadable at tile scale`. Undeterminable → say so, confidence LOW and word `UNRESOLVED`. `confidence` HIGH/MEDIUM/LOW. Quote fields with commas.

## Output 2 — `asset_inventory.csv`, exact header `alias,kind,description,segs,confidence`
One row per recurring or notable visual asset. `alias` = your own short neutral id (e.g. CAVEMAN_A_POSE_THINK). `kind` = CHARACTER_POSE / PROP / BACKGROUND / TEXT_STYLE / DIAGRAM / EFFECT. `segs` = `;`-separated seg IDs where seen. Note when a drawing appears re-used identically vs redrawn.

## Output 3 — `narration_visual.csv`, exact header `asr_start,asr_end,asr_text,segs,relation,note`
One row per row of asr_small_en_segments.csv, same order; copy `start`,`end`,`text` verbatim into first three columns. `segs` = `;`-separated seg IDs overlapping that time span (use PTS). `relation` from LITERAL, METAPHOR, DEMONSTRATIVE, DATA, CONTRAST, HUMOR, EMOTIONAL, DECORATIVE, POTENTIALLY_MISLEADING, UNDETERMINED (`+` allowed). `note` ≤ 15 words: what visual does relative to words, and whether visual leads or lags words where visible.

## Output 4 — `observations.md` (≤ 900 words), cite seg + PTS for each claim, mark interpretations INFERRED
1. Hook: first 5 s, how premise/title promise appears. 2. Explanation chain: how concept is built step by step (setup → but → therefore), visual metaphors. 3. Jokes: visual gags with seg, PTS, ASR words. 4. Payoff and ending/CTA. 5. Characters: design, poses, expression range, reuse vs redraw. 6. Props, backgrounds, palette, line treatment. 7. Typography/text: amount, placement, size, mobile readability. 8. Motion vocabulary: counts of cuts, pose swaps, zoom steps, smooth moves, pops; whether in-betweens exist; easing appearance only as shape. 9. Camera behaviour. 10. Pacing: where holds are long/short relative to narration. 11. Anything contradicting the rest of this video. 12. Every unresolved segment.

## Rules
OBSERVED from tiles vs INFERRED intent. ASR is not listening; never claim hearing. No invented fonts, software, easing curves, SFX, retention, CTR. Finish by writing all four files. Final message: sheets opened, strips opened, annotation rows, unresolved segs. Keep it under 80 words.
