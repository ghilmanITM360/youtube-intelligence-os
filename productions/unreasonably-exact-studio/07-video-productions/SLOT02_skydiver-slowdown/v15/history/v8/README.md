# Skydiver slowdown — V8 source

Start with START_HERE.md. Final video: SKYDIVER_SLOWDOWN_V8.mp4.

## Reproduction

Python 3.14, Cairo (/opt/homebrew/lib/libcairo.2.dylib on this Mac), FFmpeg and the packages in requirements.txt are needed. From this directory:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/produce.py --check --boards
.venv/bin/python tools/produce.py --render
.venv/bin/python tools/review_export.py
```

Edit SPEC/SHOTS in tools/produce.py for shot timing, framing, text, forces, palette and camera/world travel. Edit motion_clips/compositions/M01–M12.json for articulated channels and rigs/*/rig.json for pivots, hierarchy and limits. Assets are separate SVG drawings. The native pipeline evaluates the rig each frame; fixed-posture diagrams deliberately sample a held pose.

The portable data timeline is timeline.json; SHOT_MANIFEST.csv is its readable view. The HyperFrames project in editorial/ exposes 22 baked-picture trims plus a narration lane. It does not expose native Cairo vector parts as DOM objects. After rerendering, copy the master to editorial/assets/picture_master.mp4. In editorial/, use the pinned HyperFrames 0.9.93 CLI to preview/check.

The original production is preserved at /Users/ghilmanislam360/GhilmanProjects/skydiver-slowdown/. V8 copied suitable assets instead of rewriting previous versions. prepare.py audits those original files and has that original path recorded; it is an audit helper, not required for rendering this self-contained V8 package.

Audio is copied from the existing V6 AAC narration stream. The original WAV is unavailable. Complete narration is retained; SFX were inventoried but not mixed without audition. Caption and phrase times remain approximate.
