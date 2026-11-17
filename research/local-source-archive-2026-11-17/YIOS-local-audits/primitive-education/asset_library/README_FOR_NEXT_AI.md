# primitive-education — visual asset library (LOCAL ONLY, never on GitHub)

**Open the images yourself. Do not rely only on the text prompts/ledgers.** Use your image-view tool on the files below.

## Layout
- `<video_id>/states/*.jpg` — one full-resolution frame (native source resolution, JPEG q2 re-encode of the decoded frame) per ledger state. Name: `<state_id>_f<frame_index>_t<pts_seconds>.jpg`.
- `<video_id>/states_index.csv` — file, state_id, frame index, measured source PTS, pts_check, event/entry class, what changed, ledger status, MP4 SHA-256, image SHA-256.
- `_channel/unique_frames/` + `unique_frames_index.csv` + `cluster_members.csv` — near-duplicate clustering across all videos (64x36 thumbnail RMS <= 3.0; highest-resolution member kept). `n_videos > 1` marks recurring visuals.
- `library_manifest.csv` — per-video counts, ledger status, source MP4 SHA-256.

## Source of states
Built from: tables/state_ledger.csv segments (one representative frame per segment row; status VISUAL_ANALYSIS_PARTIAL, audio not signed off). 15 videos at build time.

## Rules and limits
- One representative frame per state/segment (start + min(3, frames-1)). NOT every frame: motion and timing are in each workspace's ledgers and report.
- Source MP4s untouched; SHA-256 verified before extraction; PTS cross-checked per frame (pts_check). Image hashes re-verified after copy.
- Labels keep their ledgers' own status; ledgers are VISUAL_ANALYSIS_PARTIAL / audio unverified. Nothing here is audio-verified.
- Dedup merges near-identical pixels only, not meaning. Category folders (characters / environments / props / graphics_ui / typography / transitions) need a viewing pass and are built in the model-sheet step.
- Originality: learn the visual SYSTEM (style, rhythm, layout rules); generated assets should be original characters, logo and branding, not a 1:1 copy of the source channel's own assets. Source videos are third-party material; keep frames local.
