# Reviewer brief — xkcd What If? visual state review — FYoHYq8VRt0 (rvH3_FYoHYq8VRt0)

You are a bounded, fresh-context visual reviewer. Work ONLY inside `/Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/videos/FYoHYq8VRt0`. Write ONLY to `/Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/videos/FYoHYq8VRt0/review/rvH3_FYoHYq8VRt0/`. Do not edit any other file. Do not browse the web. Do not run analysis scripts.

## Inputs (read these)
1. `/Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/videos/FYoHYq8VRt0/tables/segments_v1.csv` — every frame of the video is in exactly one segment. `HOLD` = measured-static interval; `ACTIVITY` = interval where pixels changed (candidate event; may be a cut, a pop-on, a write-on, a dissolve, a camera move, a pose/state swap, or a false positive).
2. `/Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/videos/FYoHYq8VRt0/tables/sheet_index.csv` — maps each tile on each review sheet to segment, frame index and PTS.
3. Review sheets `/Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/videos/FYoHYq8VRt0/frames/sheets/SHEET_01.jpg … SHEET_NN.jpg` (NN = 14). Tiles are labelled `<seg> <H|A> f<frame> <pts>s`. Green border = HOLD (its settled last frame). Red border = ACTIVITY sample frame(s). **You must open every sheet with the Read tool, in order, one sheet per Read call.** Do not claim to have seen a sheet you did not open.
4. `/Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/videos/FYoHYq8VRt0/asr/asr_small_en_segments.csv` — provisional machine ASR (not listening; may contain errors).

## Output 1 — `review/rvH3_FYoHYq8VRt0/annotations.csv` (required, exact header)
`seg,event_class,subtype,description,confidence`
- One row for **every** segment in segments_v1.csv (same seg IDs, same order). No missing or extra rows.
- `event_class` for HOLD rows: `STATIC_HOLD`. For ACTIVITY rows one of: `SHOT_CUT` (whole composition replaced), `GRAPHIC/TEXT` (element/label/annotation appears, disappears or updates), `CAMERA` (whole canvas or anchor group translates/scales), `CHARACTER` (a drawn figure or object is redrawn in a new pose/state), `LIGHT/COLOR/EFFECT` (fade, dissolve, flash), `FALSE_POSITIVE` (no visible change), or a `+` combination such as `SHOT_CUT+CAMERA`.
- `subtype` — short UPPER_SNAKE label, e.g. `SCENE_SWAP, POP_ON_OBJECT, POP_ON_LABEL, WRITE_ON_TYPE, WRITE_ON_STRIKE, WRITE_ON_LINE, ANNOTATION_CIRCLE, CROSS_DISSOLVE, FADE_IN, PAN_LEFT, SCROLL_UP, ZOOM_IN, ZOOM_OUT, POSE_SWAP, STATE_SWAP_DAMAGE, POP_OFF_TEXT, HOLD, OPENING_STATE, ENDING_STATE`.
- `description` — literal, visible facts only: what is on the canvas (HOLD) or what changed (ACTIVITY), positions (upper/lower/left/right), exact readable text in quotes, colours (black ink, grey fill, red mark). If text is unreadable at tile scale say `unreadable at tile scale`. If you cannot tell what changed, say so and set confidence LOW. Include the word `UNRESOLVED` when an onset or identity cannot be determined from the tiles.
- `confidence` — HIGH / MEDIUM / LOW.
- Quote any field containing commas with double quotes (CSV).

Examples (from a different video, for format only):
```
G0001,STATIC_HOLD,OPENING_STATE,"White canvas; all-caps hand-lettered title RICHTER SCALE upper-middle; detailed seismograph line drawing lower-middle. No character.",HIGH
G0002,GRAPHIC/TEXT,WRITE_ON_STRIKE,"Red zigzag strike-through drawn left-to-right across RICHTER SCALE over the activity frames; seismograph static.",HIGH
G0008,SHOT_CUT,SCENE_SWAP,"Hard cut to newspaper 'The Daily News' with headline ... (top), phone (lower-left), TV with two stick figures (lower-right).",HIGH
G0026,CAMERA,PAN_LEFT_WITH_FADE,"Ruler slides to far-left edge with ghosting; red hatching fades out; small arrow marker appears at 9.",MEDIUM
```

## Output 2 — `review/rvH3_FYoHYq8VRt0/observations.md` (required, ≤ 900 words)
Answer from what you saw, citing seg IDs and PTS for every claim. Mark interpretations as INFERRED.
1. How is the question/premise introduced and bounded (first ~10 s)?
2. How do reasoning steps, estimates and escalation become visual steps? Name persistent anchors (axes, rulers, maps, characters) and how they change.
3. When do diagrams, labels, scale comparisons, graphs, numbers appear relative to the object they label?
4. Reveal types used (pop-on, write-on, dissolve, camera move) and which content uses which.
5. Visual jokes, deadpan figures, cutaways, callbacks — list each with seg/PTS and the ASR words nearby.
6. Camera motion vs drawing animation vs true cuts — counts and examples.
7. Characters/objects: stick figure construction, object detail level, any colour use (red, grey, other).
8. Anything unusual or contradicting these typical patterns: single persistent diagram; red only for marks; stick figures only in jokes.
9. List every segment you could not resolve.

## Rules
- Facts from tiles are OBSERVED; reasons/intent are INFERRED. ASR text is not listening; never claim to hear audio.
- Do not invent fonts, software, easing curves or sound effects.
- Finish by writing both files. Your final message: number of sheets opened, number of annotation rows, list of UNRESOLVED segs.
