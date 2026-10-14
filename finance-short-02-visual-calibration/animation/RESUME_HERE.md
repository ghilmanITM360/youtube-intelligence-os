# Finance Short 02 — animation: resume here

Status: **VIDEO_RENDERED_REVIEW_REQUIRED**. The final MP4 is rendered and technically validated. It still needs the owner's human viewing and listening, plus artistic sign-off. Branch `production/finance-short-02-assets`, draft PR https://github.com/ghilmanITM360/youtube-intelligence-os/pull/30. Do not merge.

## Files (this folder)

| File | What |
|---|---|
| `Finance_Short_02_FINAL.mp4` | 1080×1920, 30 fps, H.264 High yuv420p BT.709, AAC 48 kHz mono. 49.70 s / 1491 frames |
| `Finance_Short_02_PREVIEW.mp4` | 540×960 downscale of the final (same picture and audio) |
| `Finance_Short_02.en.srt` | Closed-caption sidecar for upload (approved wording, phrase timing). Nothing is burned into the picture |
| `FINAL_CONTACT_SHEET.png` | One tile per storyboard state (36), taken from the encoded final at each state's last frame |
| `FINAL_VIDEO_QA.md` / `FINAL_VIDEO_QA.json` / `STATE_IDENTITY_QA.json` | QA report and machine results |
| `AUDIO_PROVENANCE.md` / `AUDIO_ALIGNMENT.json` | WAV hash and QA; ASR word timing and the 18 phrase onsets every visual cue references |
| `KEYFRAME_TIMELINE.json` | The editable timeline: 36 states, 117 layer tracks, 621 keys, 28 camera keys |
| `player.html` | Keyframe player. Serve the project folder and open it to scrub and play with audio |
| `audio/…Skylar…wav` | Owner WAV, immutable copy (SHA256 `3eff2e57…0328`) |
| `tools/align_audio.py` | WAV → `AUDIO_ALIGNMENT.json` (whisper base + silencedetect) |
| `tools/build_timeline.py` | Storyboard + layer map + alignment → `KEYFRAME_TIMELINE.json` + SRT. **Retime here (`CUES`)** |
| `tools/render.cjs` | Headless Chrome over CDP → PNG frames → ffmpeg. No npm dependencies |
| `tools/qa.py` | `states`, `video` and `sheet` checks |

No artwork was copied or redrawn. Every layer is loaded from `../assets/**.svg` at its `SCENE_ASSET_MAP.csv` placement.

## Rebuild (from `finance-short-02-visual-calibration/`)

Requirements: Python 3.9+ with Pillow and numpy (QA only); Node 22+; Google Chrome; ffmpeg. openai-whisper is needed only to re-run the alignment.

```sh
python3 animation/tools/build_timeline.py                     # after editing CUES
node animation/tools/render.cjs --out /tmp/clip.mp4 --from 20 --to 26 --scale 0.5   # local check of one window
node animation/tools/render.cjs --out animation/Finance_Short_02_FINAL.mp4
python3 animation/tools/qa.py video animation/Finance_Short_02_FINAL.mp4
python3 animation/tools/qa.py sheet animation/Finance_Short_02_FINAL.mp4 animation/FINAL_CONTACT_SHEET.png
```

To scrub interactively, run `python3 -m http.server 8765` in this project folder and open `http://127.0.0.1:8765/animation/player.html`.

The renderer runs Chrome with `--num-raster-threads=1`. With that flag, repeated renders of the same frame are byte-identical. A full 1080×1920 render takes about 2 minutes on Laptop B.

## Open items for the owner

1. Watch and listen to the final on a phone. Nothing here certifies human listening or artistic approval.
2. Captions: lettering is revealed on the spoken words in place of a separate subtitle band. An `.srt` file is provided for YouTube CC. If burned-in captions are wanted, choose a zone, because the art already reaches y≈1590.
3. Fine attribution text inherited from the artwork (e.g. the full FOMC sentence, H.4.1 row label) is small on a phone, as already recorded in `ASSET_QA.md`.
4. Re-check H.4.1 before publishing. The −233,587 (7 Oct 2026) figure is dated on screen.
