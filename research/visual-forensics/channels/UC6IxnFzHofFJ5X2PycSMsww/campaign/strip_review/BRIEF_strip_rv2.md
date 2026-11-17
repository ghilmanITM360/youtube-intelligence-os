# Dense-strip re-review brief (strip_rv1)

You are a visual reviewer. Tasks: /Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/campaign/strip_review/strip_tasks_rv2.csv (30-31 rows). Each row is one long ACTIVITY segment of an xkcd "What If?" video that the first review saw only as ≤6 sampled tiles. Its strip image shows EVERY frame (or every `stride`-th frame) of the segment in order, left→right, top→bottom; label under each tile = `f<frame> <changed_frac>` (yellow label = changed_frac > 0.05, i.e. large change from previous frame).

For EACH row, in order:
1. Open the strip image with the Read tool (one Read call per strip; do not skip any).
2. Compare with `prior_class` / `prior_desc`.
3. Record the internal structure: list sub-events with frame ranges, e.g. `f307-f330 sky rotates (CAMERA continuous); f331 hard cut to map (SHOT_CUT); f332-f340 red path write-on`. Count hard cuts INSIDE the segment (a cut = complete canvas change between two adjacent tiles at stride 1; at stride >1 say "cut between fA and fB").
4. Verdict: CONFIRMS (prior description complete), REFINES (prior right but missed sub-events), or CONTRADICTS (prior wrong; explain).

Write ONLY this file: /Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/campaign/strip_review/strip_rv2/strip_annotations.csv with header exactly:
`video,seg,verdict,internal_cuts,sub_events,motion_devices,confidence`
- internal_cuts: integer
- sub_events: `;`-separated `fA-fB description` items
- motion_devices: `+`-joined from {POP_ON, WRITE_ON, DISSOLVE_FADE, SLIDE_PAN_BLUR, CONTINUOUS_CAMERA, SCROLL, ZOOM, STATE_SWAP, SHOT_CUT, MORPH, OTHER}
- confidence: HIGH/MEDIUM/LOW
Quote fields with commas. Describe only what is visible; no guessing about narration, software or fonts. Do not read any other images. Reply at the end with 3 lines: strips opened, verdict counts, total internal cuts.
