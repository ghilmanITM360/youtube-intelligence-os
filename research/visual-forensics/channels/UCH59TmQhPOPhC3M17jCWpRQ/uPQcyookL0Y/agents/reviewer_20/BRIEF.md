# Bounded reviewer brief — Barely Evolved uPQcyookL0Y, batch08 (states W071-W080)
Workspace (cwd for all relative paths): /Users/ghilmankhan/YIOS-local-audits/barely-evolved/2026-11-02-uPQcyookL0Y-deep-ct-scan
You are one bounded visual reviewer. Source: 1920x1080 cartoon explainer, 29.97fps (30000/1001), frame f -> pts f*1001/30000 s.
Evidence rules (YIOS Visual Forensics kit v1.0 refs 01/03/04/05/07/13):
- Label claims OBSERVED (seen in an image you opened), MEASURED (numbers supplied below), INFERRED (interpretation), UNAVAILABLE.
- Do NOT claim fonts, software, layers, easing curves, sound assets or anything between/outside frames you actually viewed. Sparse samples are not full temporal inspection.
- ASR text is provisional machine transcription, NOT listened audio. Nobody has heard the audio. Never claim audio sync.
- Use your own asset IDs prefixed `reviewer_20:`; do not rename earlier reviewers' IDs.
## Inputs
1. States: `tables/states_v6_draft.csv` rows W071..W080 (start/end frames inclusive).
2. Native representative PNGs: listed in `tables/k_rep_frames_batch08.csv` (palette column = kmeans clusters, MEASURED, not design swatches).
3. Motion strips: `tables/o_motion_peaks_batch08.csv` — each strip PNG tiles ~8 consecutive frames (downscaled 480x270, labelled fNNNN) around a measured pixel-difference peak. Peaks are detector candidates; you decide what actually changes.
4. ASR excerpt: `tables/o_asr_excerpt_batch08.csv` (seg_index, start/end s). Segments may extend outside this batch; judge only the in-batch portion and say so.
## Task
Open EVERY native PNG and EVERY strip PNG with the Read tool (one image per Read call). Then write, in `agents/reviewer_20/`:
- `evidence_reads.csv`: state,frame_or_strip,path,sha256,witness (one short sentence of what that image shows). Compute sha256 with `shasum -a 256`.
- `art_audit_batch08.csv` with columns exactly: state,frames_viewed,characters_and_recurring_assets,pose_expression_action,foreground_background_layers_occlusion,layout_spatial_relationships,palette_observed,typography,illustration_texture_outline_shading,camera_framing_motion,text_graphic_subevents,in_state_changes_between_viewed_frames,uncertainty_unavailable,evidence_label,confidence  (one row per state; frames_viewed = full relative PNG paths separated by ';').
- `motion_events_batch08.csv`: state,strip_path,first_frame,last_frame,event_type(TEXT_REVEAL|CHARACTER_MOTION|CAMERA_SCALE|CAMERA_PAN|ELEMENT_ENTER|ELEMENT_EXIT|FADE|CUT_WITHIN_STRIP|NO_VISIBLE_CHANGE|OTHER),description,evidence_label. Use frame numbers printed on the tiles.
- `narration_relation_batch08.csv`: seg_index,asr_start_s,asr_end_s,visual_states_overlapping,visual_frames_judged,relation(LITERAL_*/ILLUSTRATIVE_*/CONTRADICTORY_JOKE_*/MIXED_PARTIAL/UNRELATED_HOLD/UNCERTAIN; suffix _PARTIAL when only sampled),rationale,timing_confidence,suspicious_asr_words. visual_frames_judged must be paths of native PNGs or strips whose frame time lies inside that segment's [start,end); if none fall inside, write NONE and relation UNCERTAIN.
- `state_prompts_batch08.csv`: state,observed_basis_paths,image_prompt_original,image_to_video_prompt_original,static_anchors,do_not_change,unverifiable_left_open. Prompts must describe a NEW ORIGINAL equivalent (kit ref 09): reuse the observed abstract technique (layout, shape grammar, palette family, framing, motion type and timing from your strip frames) but never copy the source's specific characters, drawings or exact wording; write any on-screen text as a placeholder like <ORIGINAL_HEADLINE>. Motion timing only from frame numbers you saw; otherwise say "timing unverified".
Valid CSV (quote fields containing commas). Final message: counts of images opened, rows per file, and any image you could not open.
