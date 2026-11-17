# Casual Finance — visual asset library (LOCAL ONLY, never on GitHub)

**Open the images yourself. Do not rely only on the text prompts/ledgers.** Use your image-view tool on the files below.

## Layout
- `<video_id>/states/*.jpg` — one full-resolution frame (native source resolution, JPEG q2 re-encode of the decoded frame) for every verified visual state of that video. Name: `<state_id>_f<frame_index>_t<pts_seconds>.jpg`.
- `<video_id>/states_index.csv` — file, state_id, shot_id, source frame index, measured source PTS, pts_check, how the state entered (CUT / POP_IN / POSE / ...), what changed, visible text, asset ids, MP4 SHA-256, image SHA-256.
- `_channel/unique_frames/` + `unique_frames_index.csv` + `cluster_members.csv` — near-duplicate clustering across all videos (64x36 thumbnail RMS <= 3.0; highest-resolution frame kept as representative). `n_videos > 1` marks recurring visuals.
- `library_manifest.csv` — per-video counts and source MP4 SHA-256.

## Rules and limits
- One representative frame per state (the ledger's `rep_frame`; legacy Uumnx2Fo6cE uses start+3 clipped to state end). It is NOT every frame; motion between frames is described in each workspace's `visual_event_ledger.csv` and report, not here.
- Source MP4s are untouched; each frame's source SHA-256 and PTS were verified at extraction (pts_check OK for all). Image hashes re-verified after copy.
- Labels (`what_changed`, `visible_text`) come from the per-video ledgers and keep their own MEASURED/OBSERVED/INFERRED status. Nothing here is audio-verified (audio = ASR only, AV sign-off BLOCKED).
- Dedup merges near-identical pixels only. It does not group by meaning (same character in a different layout stays separate). Category folders (characters / environments / props / graphics_ui / typography / transitions) need a viewing pass and are built in the model-sheet step.
- Originality: use this to learn the visual SYSTEM (style, rhythm, layout rules). Generated assets should be original characters, logo and branding, not a 1:1 copy of the source channel's own assets.
- Library covers only the videos in `library_manifest.csv` (19 verified when built; gG239LrksH4 was still pending). 20-35 videos is a sample.

## Added 2026-11-08 (night): category audit, model sheets, HumanCraft alignment
- `_channel/CATEGORY_AUDIT.md` + `_channel/category_index.csv` (rule tags; only 168/3,945 clusters viewed) + `_channel/review_sheets/` (7 contact sheets with `.members.csv`).
- `_channel/model_sheets/MODEL_SHEETS_CASUAL_FINANCE.md` (v0.1 character/environment/graphics/rhythm/palette sheets, MEASURED/OBSERVED/ESTIMATED/INFERRED labels) + exemplar images + CSVs (asset_roster, rhythm_by_video, entering_class_counts, palettes, head_ratio_samples, resolution_by_video).
- `_channel/HUMANCRAFT_ALIGNMENT.md`: how the owner's HumanCraft PDF (layered, keyframed, no image-to-video) changes the build plan and what is still missing.
- Open the images yourself; tags are for finding candidates, not ground truth.
