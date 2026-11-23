# Tool decision matrix (2026-11-20). Only "TESTED" rows were run here; others were NOT installed or run.
| Tool | License / activity (gh api) | Evidence | Decision |
|---|---|---|---|
| Pillow + render_scene.py (ours) | n/a | TESTED: 2 specs rendered, md5-reproducible | **Baseline backend**, keep |
| ffmpeg/ffprobe (installed) | LGPL/GPL | TESTED: encode, frame-count, md5 | **Keep** (encode, validate, frame extraction) |
| HyperFrames (heygen) | Apache-2.0, pushed today | TESTED: `init` + `render` in scratchpad, 1080p 30 fps 10 s clip in 8 s, Chrome + node 24 present | **Second backend** for GSAP easing, camera/parallax, SVG/HTML motion graphics; migrate nothing until a shot proves better than Pillow |
| whisper / whisper-cli (installed earlier) | MIT | previously used for ASR | keep as timing reference (OCR beat ASR for captions) |
| kajisho5/ffmpeg-skill | MIT | NOT inspected | defer; raw ffmpeg already covers needs |
| iart-ai/motion-skills (56 skills) | MIT | NOT inspected | candidate: easing/typography presets; read before borrowing |
| hi-nikola hand-drawn-explainer | Apache-2.0 | NOT inspected (Chinese docs) | candidate for hand-drawn stroke animation; read before any use |
| storytold/effectcraft | Apache-2.0 | NOT inspected | defer (compositing app, overlaps HyperFrames) |
| alexgreensh/anidoodle | Apache-2.0 | NOT inspected | defer |
| lemo-opuscar | NOASSERTION (no clear license) | NOT inspected | **avoid** until licence is clear |
| claude-shorts / ghost-editor / video-recap-skills | MIT | NOT inspected | **skip**: long-to-short, talking-head and recap tools, not our need |
| threejs-skills | MIT | NOT inspected | **skip**: no 3D in reference (camera grammar = none) |
| MotionClone (blixvip) | repo 404 via gh | not found | **skip** (diffusion, GPU, not our need) |
| Codex / image generation | external | Codex prompts written; no images generated | needed for category-A assets |
