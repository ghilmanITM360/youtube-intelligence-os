# Video forensic reconstruction report

## Source summary

1920x1080 H.264, 24 fps, 162.261043 s, AAC stereo. Full-duration overview plus 4 fps dense samples cover every shot; source checksum and metadata are in `00_source/SOURCE_MANIFEST.md`.

## Observed production DNA

White hand-drawn line-art scenes, locked compositions, black outlines, sparse red heat/diagram accents, state replacements and hard cuts. Full evidence-backed rules: `02_analysis/VISUAL_DNA.md`.

## Counts

- Shots: 12
- Visual states: 51
- Unique production assets: 26
- Motion events: 38

## Way 1 — CapCut

Complete. Setup and per-shot build blocks: `03_capcut/CAPCUT_REBUILD.md`.

## Way 2 — Image-to-video

Complete with controlled limitations. Unique image prompts: `04_image_to_video/IMAGE_PROMPTS.md`; motion prompts: `04_image_to_video/ANIMATION_PROMPTS.md`; per-shot assembly: `04_image_to_video/I2V_REBUILD.md`.

## Important fidelity limitations

- Timings are sampled to 0.25 s; refine against AU01/frame matching for frame-exact edit points.
- No local ASR was available: narration words, music identity, and SFX names are intentionally not guessed. `05_audio/AUDIO_MAP.md` records supported audio evidence.
- Exact font, original assets, software, editor, effects, and source artwork are UNKNOWN. Use authored clean plates and editor text/vector overlays where generated text or diagram geometry could drift.

## File index

- Canonical temporal record: `02_analysis/TIMELINE.csv`
- Required recreation assets: `02_analysis/ASSET_MANIFEST.csv`
- Motion/state changes: `02_analysis/MOTION_EVENTS.csv`
- Evidence: `01_evidence/CONTACT_SHEET.jpg`, `01_evidence/frames/`
