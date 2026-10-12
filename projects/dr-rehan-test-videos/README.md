# Dr. Rehan Omar — Calf Pain / PAD Medical Explainer

Vertical YouTube Short explaining calf pain when walking (intermittent claudication) and peripheral arterial disease. It is a production test video and is separate from the YIOS research datasets.

## Versions
| | File | Notes |
|---|---|---|
| **V2 (preferred)** | `V2/Calf_Pain_PAD_FINAL_v2.mp4` | Premium finishing pass. It adds sans-serif keyword captions, a rebuilt hook, the Dr. Rehan Omar name in graphics, clearer artery and oxygen diagrams, and original music plus 10 SFX under the untouched narration. |
| V1 (original) | `V1/Calf_Pain_PAD_FINAL.mp4` | Kept for comparison. The V1 editable source snapshot is in `V1/project-source/`. |

**Specs (both versions):** 1080×1920, 30 fps, 1818 frames (60.6 s), H.264 High yuv420p BT.709 video with AAC 48 kHz stereo audio.

**Visuals:** all original SVG/React art in a Remotion timeline:
- one parametric patient/doctor rig with an IK walk;
- artery, plaque and oxygen-flow diagrams;
- a body risk map;
- word-timed captions.

## Layout
- `project/`: editable V2 Remotion project.
  - `src/rig.tsx`: character rigs.
  - `src/anatomy.tsx`: anatomy.
  - `src/env.tsx`: park and clinic environments.
  - `src/scenes.tsx`: scenes and transitions.
  - `src/ui.tsx`: captions.
  - `public/narration.mp3`: original voiceover, unmodified.
  - `audio/`: original synthesized music bed, SFX and cue list.
  - `tools/`: audio, SRT, contact-sheet and QA scripts.
- `captions/`: V2 SRT, with V1's SRT in `captions/V1/`.
- `documentation/`: QA, changes, style guide and audio licences, with V1 docs in `documentation/V1/`.
- `previews/`: contact sheets for V1 and V2.
- `SOURCE_MANIFEST.json`: path, size, SHA-256, version, storage and purpose for every file.

Binaries (mp4, wav, mp3, png) are stored with Git LFS through this folder's `.gitattributes`.

## Rebuild V2
Requires Node 18+ (tested on 24.14), ffmpeg, and python3 with NumPy.
```bash
git lfs pull --include="projects/dr-rehan-test-videos/**"
cd projects/dr-rehan-test-videos/project
npm ci
npm run final
```

`build_final.sh` runs these steps:
1. Remotion render.
2. Transcode to yuv420p BT.709.
3. `tools/make_audio.py public/narration.mp3`, which regenerates the seeded music and SFX and mixes them under the narration into `audio/mix.wav`.
4. Mux with AAC 192 kbps.

The build writes `../Calf_Pain_PAD_FINAL_v2.mp4` and `../Calf_Pain_PAD.srt` (project folder root). It never touches `V1/` or `V2/`. Use `npm run studio` to preview and `npm run draft` for a half-scale draft.

## Known limitations (not corrected)
1. The narration says **"Dr. Rahim"**, but the graphics say **Dr. Rehan Omar**. The caption is kept verbatim. A re-record by the original speaker is needed.
2. The phrase near **41.5 s** is uncertain. The caption reads "critical [limb] ischemia", where the bracketed word is inferred.
3. **Human full-audio listening QA is pending.** All audio checks are measured, not heard.
4. Minor issues:
   - lip-sync follows loudness rather than phonemes;
   - feet slip by a few pixels at walk stops;
   - the finale title is a few pixels from the hair.

No physician has clinically signed off this video. Details are in `documentation/FINAL_QA.md`.
