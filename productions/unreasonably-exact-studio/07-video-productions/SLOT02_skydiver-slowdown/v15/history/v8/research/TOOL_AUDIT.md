# Candidate library audit

Inspected actual upstream README files and available package manifests on 2026-11-25. Snapshots are in library_docs/. Documentation inspection does not prove runtime compatibility. No candidate code executed merely because it was listed.

| Candidate | Availability, capability, dependency and selection |
|---|---|
| [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts) | README fetched. Remotion + three.js illustrated story shorts; Node/Python/FFmpeg and large media bundle. Not adopted: new 3D pipeline would replace the working V7 rigs. |
| [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | README fetched. Canvas/WebGL film authoring with optional audio engines; Node 20+, FFmpeg 7+, Python 3.11+. Not adopted: optional full production ecosystem unnecessary for a continuation. |
| [alexgreensh/anidoodle](https://github.com/alexgreensh/anidoodle) | README fetched. Code-drawn illustration and animation, optional sound pack. Not installed or smoke-tested; existing SVG FK renderer already covers this job. |
| [openai/whisper](https://github.com/openai/whisper) | README fetched. Speech recognition models; Python package normally uses PyTorch and FFmpeg. Used the existing whisper.cpp executable with medium.en weights instead of installing the Python package. |
| [kurbaitaev/ghost-editor](https://github.com/kurbaitaev/ghost-editor) | README fetched. AI editing orchestration with FFmpeg, Node, Python, Whisper/OpenCV; optional Gemini sends frames externally. Not installed or used. |
| [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | README fetched. Local FFmpeg editing/measurement toolkit. Documentation inspected; existing FFmpeg binary used directly, toolkit not installed. |
| [iart-ai/motion-skills](https://github.com/iart-ai/motion-skills) | README fetched. Catalog of specialized motion skill packs and optional remote service. Documentation inspected; no remote service or package adopted. |
| [agricidaniel/claude-shorts](https://github.com/agricidaniel/claude-shorts) | README fetched. Longform extraction/reframing with Remotion captions; Python 3.10+, Node18+, FFmpeg. Not an original character-animation renderer; not adopted. |
| [blixvip/MotionClone](https://github.com/blixvip/MotionClone) | HTTP Error 404: Not Found. GitHub repository returned HTTP 404 in this audit. Availability and capabilities unverified; not installed. |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | README fetched. Deterministic HTML/GSAP/media compositions; Node22+, FFmpeg. CLI and updated skills available. Native V7 animation retained; HyperFrames used for editorial timeline/preview validation if generated below, not for drawing the character. |
| [cloudai-x/threejs-skills](https://github.com/cloudai-x/threejs-skills) | README fetched. three.js reference skill files. No true 3D geometry required by these shots; not installed. |
| [zhuyansen/awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills) | README fetched. Repository catalog, not a production renderer. Inspected discovery table; did not treat marketing comparisons as evidence. |
| [storytold/effectcraft](https://github.com/storytold/effectcraft) | README fetched. Native Rust motion design/compositing app with web build; installers or cargo toolchain required. No native app project created. Website link is a distribution destination, not evidence of installation. |
| [hi-nikola/hand-drawn-explainer-video-nikola](https://github.com/hi-nikola/hand-drawn-explainer-video-nikola) | README fetched. HTML/SVG/GSAP/HyperFrames explanatory visuals, plus bitmap stroke extraction; Python3.10+, Node/browser/FFmpeg for procedural video. Not installed; canonical assets already drawn. |
| [zenstory-ai/video-recap-skills](https://github.com/zenstory-ai/video-recap-skills) | README fetched. Python3.10+ and FFmpeg recap/edit tools with optional cloud services and Remotion packaging. Recut workflow unnecessary; not adopted. |

## Tools actually used

Python 3.14 virtual environment; Cairo through cairocffi; CairoSVG; Pillow; installed FFmpeg/FFprobe; installed whisper.cpp medium.en; Browser for source review and playback observation. HyperFrames usage and skill-update commands executed; updated CLI reports general-video retired and consolidated into hyperframes. Native V7 renderer remains the animation authority. See editorial/ for the actual HyperFrames integration status.

## HumanCraft decisions applied

- V4 MD is the authoritative text; V4 PDF mirror located and extracted. Read its character, classical principles, camera, story, typography, timing, editorial and QA sections, plus 110-technique tables. V2 PDF relevant production sections read from extracted text. No claim of a visual page-by-page PDF review.
- Separate world/character/graphic layers; use time-varying FK channels; eyes lead brows/head; preserve intentionally held posture for the model.
- Stage one explanation at a time; common scale for forces, distinct dashed blue velocity, unlabeled curved airflow, sparse/dense schematic marks.
- Match cuts to the preserved narration; static diagrams are deliberate teaching holds, not claimed physical views. Keep opening wide, then show the closed pack and reaction.
- Review real renders and correct specific defects. Do not award artistic approval based on decode checks.

The standalone earlier Codex assignment was not located. The continuation brief, V1–V7 handoffs, manifests and actual files define the audited scope; this limitation is explicit in CONTINUATION_LEDGER.csv.