# Video forensic rebuild report

## Source summary

`YTDown.com_YouTube_What-if-Earth-grew-1cm-every-second_Media_-1-ldW4kpLM_001_1080p.mp4` is a 315.675-second, 1920×1080, 24-fps landscape H.264 video with stereo AAC audio. Source checksum and codec data: `00_source/SOURCE_MANIFEST.md`.

## Observed production DNA

Sparse black/gray hand-drawn explanatory animation, red emphasis, locked framing, hard cuts, and local graphic reveals. Details: `02_analysis/VISUAL_DNA.md`.

## Counts

- Shots: 39
- Stable visual states explicitly catalogued: 41
- Reusable/recreation assets: 66 IDs (C 5, E 10, O 16, G 23, T 11, AU 1; shared IDs are counted once)
- Meaningful motion/transition events: 41

## Way 1 — CapCut

Complete rebuild instructions: `03_capcut/CAPCUT_REBUILD.md`. The approach uses fixed image/vector layers, editor text, keyframes only for observed movement, masks for local deformation, and source audio as timing authority.

## Way 2 — Image-to-video

Complete rebuild instructions: `04_image_to_video/IMAGE_PROMPTS.md`, `ANIMATION_PROMPTS.md`, and `I2V_REBUILD.md`. It maximizes clean-plate reuse and deliberately holds static shots; text/diagrams are final overlays.

## Important fidelity limitations

- Audio is present but no verified transcript or isolated music/SFX classification was produced. Preserve source mix or transcribe/listen before replacing it.
- Tiny opening/end-card copy and some formula annotations are not transcribed; inspect corresponding `01_evidence/frames/critical_*` source frames before typing exact wording.
- Contact-sheet and scene-detection timing supports cut timing; internal graphic-build start times marked APPROXIMATE in CapCut are not claimed as frame-exact.
- Original fonts, editor, models, stock assets, and music source remain UNKNOWN.

## File index

- Source and evidence: `00_source/`, `01_evidence/`
- Canonical shot/state timeline, asset map, motion map, visual rules: `02_analysis/`
- Manual rebuild: `03_capcut/`
- Generated-image/I2V rebuild: `04_image_to_video/`
- Audio timing limits/map: `05_audio/`
