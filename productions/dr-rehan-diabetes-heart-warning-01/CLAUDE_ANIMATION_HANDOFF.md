# Claude Code: Phase 2 assembly handoff

This is a static illustration review package, not a final video or an audio-verified edit. Do not animate/publish until the owner supplies MP3 and approves script/labels/identity. Do not infer approval from this handoff. Keep PR draft.

## Recover

Fetch and check out `production/dr-rehan-diabetes-heart-warning-assets`; all essential sources, PNGs, manifests and scene states are tracked in Git, no LFS or external media download is needed. Open README.md and SOURCE_MANIFEST.json, then run `python3 tools/validate.py` from this package (Pillow required). Do not rebuild unless an actual correction is required. Reference research lives at pinned SHA in RESEARCH_REFERENCES.json, accessible through safe Git refs; it is not a package dependency.

## Assemble exactly

1. Use a 1080×1920 composition; suggested 30 fps. Final duration follows the approved MP3, never a mandatory 60 s.
2. Read KEYFRAME_HANDOFF.json `states` in order. Each layer points to `assets/<asset_id>.svg` or `exports/assets/<asset_id>.png`. The SVG scene is the authoritative composed final state. Flat scene PNG is a visual reference, not the sole animation source.
3. Coordinate contract: x/y are top-left placement of the untrimmed source canvas; scale is uniform. Local point `(u,v)` maps to `(x+s*u,y+s*v)`. For anchor-based editors, set anchor to `anchor_local`, position to `(x+s*anchor_x,y+s*anchor_y)`. Increasing z renders later/above. Opacity is 0–1, rotation degrees. All character parts use the full 600×900 canvas. Avoid auto-trimming PNGs.
4. Import source groups for fine changes, or independent part SVG/PNG files from PART_REGISTER.csv. Never use both a full character composite and its full set of parts at once (double rendering). Within the part rig use the recorded order; preserve attached hand/sleeve paths. Do not separately pivot detached pupils or noses.
5. Use suggested recipes only as starting points. They are inferred production choices, not measured competitor keyframes. Static backgrounds stay at opacity 1; only incoming concept layers reveal. Within one scene preserve shared layers and swap changes. At scene change use a cut, with optional 8-frame wipe. No simulated physics, camera rig, walk cycle or continuous lip sync.
6. Align scene changes to verified phrases after listening. `script_span` provides text locations only, not time. Repeated spans in adjacent states are ONE narration span, not instructions to repeat the spoken words. Educational labels are not quotations or extra recorded speech. `suggested_entry_frame` is relative to a state's beginning; multiply frames by final fps/30 if changing fps. Hold after the last reveal for reading; respect minimum_hold_seconds, and extend when spoken words need longer.
7. S01-A→B: preserve patient/home; emergency-help text changes and phone appears. S02-A→B: swap whole doctor pose at a hold frame. S03: text-led exertion context → seated symptom concept → urgency. S04: charcoal reset → diabetes context; attach kit to patient. S05: add older woman beside man. S06: change pose and introduce second example without implying a diagnosis.
8. S07-A: heart base visible, coronary overlay reveals after 18 frames; no artificial beat or ECG. S07-B: wall visible, plaque reveals at 18 frames, flow-direction overlay at 36; do not imply real-time plaque growth or measured flow speed. S07-C: clinician/patient and assessment symbol, followed by mandatory S07-D emergency instruction. No booking-calendar icon or “wait for appointment” treatment of acute symptoms.
9. S08-HOLD is editorial only. Exclude from every public render. Wait for complete sentence and approve an appropriate ending; reuse home set if relevant, but do not imply recovery because the neutral pose exists.
10. Keep safety language readable and separate from captions. Source labels are short references; full URLs belong in description/research notes. Owner must approve locale/emergency number; country-neutral “local emergency services” is current draft. Do not invent endorsements, credentials or Dr. Rehan's portrait.

## Inputs still required

Original MP3; exact correction/confirmation of “acute chronic syndrome”, “not particularly significantly angina” and symptom referent; complete ending; display name/consultant credit approval; generic-presenter approval or owner-approved likeness brief; doctor/clinical review of labels and simplified anatomy; audience/locale; final YouTube health-policy review. No silent corrections. Record changes beside original transcript.

## Final QA after owner approval

Listen end-to-end; verify exact captions/voice and claims, correct timing and medical context, local emergency wording, character identity and object contact. Review 1080×1920 and 360×640 with actual platform chrome. Current native QA is sampled; current mobile QA covers all 18 static states. The final motion/audio/platform cut has not been tested. Optional music/SFX require separately documented rights; none supplied or claimed necessary.
