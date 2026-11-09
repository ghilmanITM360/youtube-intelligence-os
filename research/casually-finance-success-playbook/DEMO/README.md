# Original asset and keyframe demonstration

An eight-second silent proof at 1920×1080, 30fps, 240 frames. It shows one original Mira rig (three poses, three expressions, nine derived combinations), one reusable study and one schematic diagram revealed step by step. This is not competitor artwork, a complete financial explanation, narration/sound QA, sophisticated character acting or a throughput benchmark.

## Files

- `build_assets.py`: shared editable SVG geometry and original design tokens.
- `assets/mira_*.svg`: nine derived states from one rig; not nine unique illustrations.
- `assets/environment.svg`: reusable original environment.
- `character-grid.svg`: pose/expression matrix using the nine assets.
- `index.html` and `compositions/scene.html`: editable scene, parent-child composition and one paused scene timeline.
- `shot-plan.json`: integer-frame event map; `BRIEF.md`: owner scope and inferred design decisions.
- `assets/gsap.min.js`: frozen GSAP 3.14.2 runtime with original attribution header and notice.
- `CHECK_RESULTS.json`: zero lint/runtime/layout/contrast errors or warnings; 39/39 contrast checks, motion automated sampling disabled (not falsely claimed passed).
- `proof/contact-sheet.jpg`: visually inspected frames at 0, 1.8, 3.5, 5.9 and 7.9 seconds.
- `renders/original-keyframe-demo.mp4`: rendered proof, 8s, no audio track.
- `RENDER_VALIDATION.json`: media properties, asset hashes and repeated backward-seek image equality.

## Reproduce

From this DEMO directory, Python 3.12+ and Node/FFmpeg:

```sh
python3 build_assets.py
npx --yes hyperframes@0.8.150 check .
npx --yes hyperframes@0.8.150 snapshot . --at 0,1.8,3.5,5.9,7.9 --no-end --output proof
npx --yes hyperframes@0.8.150 preview . --background --port 3014
npx --yes hyperframes@0.8.150 render . -q standard -o renders/original-keyframe-demo.mp4
```

The version pin was deliberately upgraded 0.8.141 to 0.8.150, then rechecked. Render used screenshot capture with hardware GPU and took 12.3s on this Mac; this is one measured execution, not a production-speed guarantee. Fonts use generic sans-serif, so raster output across OS/font environments is not guaranteed identical. Timing and geometry are deterministic; repeated 5.9s after seeking to 0s was byte-identical on this environment. Fresh installs can require downloading the pinned free CLI/browser dependencies; this run used the installed/cached renderer. No paid generation service was invoked.

The registry was searched and its measured SVG-path stroke-reveal pattern adapted. The unused full primitive and scaffold instructions are omitted from the deliverable. No medical art/code or identifiable Casually Finance character was copied. The Dr Rehan project was inspected read-only as a technical reference.

Studio preview: http://localhost:3014/#project/DEMO while this local server runs. Editable source is retained even after the preview stops. The HyperFrames desktop app adds editing through Framey chat: https://hyperframes.dev/studio/download . No upload/publish command was used.
