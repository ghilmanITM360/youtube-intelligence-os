# Finance Short 02 — animation: resume here

Status: **V3_RENDERED_OWNER_REVIEW_REQUIRED**.
- V3 is rendered and technically validated. It still needs the owner's human viewing and listening, and artistic sign-off.
- Branch `production/finance-short-02-assets`, draft PR https://github.com/ghilmanITM360/youtube-intelligence-os/pull/30. Do not merge.

V3 (2026-10-14) is a targeted polish of V2:
- comprehension-first retiming of the confirmed fast builds;
- one lettering morph;
- three registered face overlays;
- a 1.3 s end hold;
- an original, ducked music bed and 10 original effects.

The artwork, layouts and narration are unchanged. **V2 is kept** (`Finance_Short_02_FINAL.mp4`, `Finance_Short_02_PREVIEW.mp4`, `FINAL_VIDEO_QA.md`). V2's timeline and tools are at commit `9d0a93a`.

## Files (this folder)

| File | What |
|---|---|
| `Finance_Short_02_FINAL_v3.mp4` | **V3 deliverable.** 1080×1920, 30 fps, H.264 High BT.709, AAC 48 kHz mono (V3 mix). 51.00 s / 1530 frames |
| `Finance_Short_02_PREVIEW_v3.mp4` | 540×960 downscale of the V3 final (same audio) |
| `Finance_Short_02_FINAL_v3_NARRATION_ONLY.mp4` | V3 picture with the untouched narration only (safety and comparison) |
| `V3_EDIT_DECISIONS.csv` | What was wrong in V2 (confirmed on the encoded file), the fix, and the measured result |
| `V3_VISUAL_QA.md`, `V3_VIDEO_QA.json`, `V3_STATE_IDENTITY_QA.json`, `V3_CONTACT_SHEET.png` | V3 visual QA |
| `V3_AUDIO_MIX_QA.md`, `V3_AUDIO_MIX.json`, `V3_AUDIO_LICENSES.md` | Mix settings, measurements, effect cue list, rights |
| `audio/v3/FS02_V3_MUSIC_BED.wav`, `FS02_V3_SFX_STEM.wav`, `FS02_V3_MIX.wav` | Original bed (before ducking), effects stem, final mix. All 48 kHz mono 16-bit |
| `audio/…Skylar…wav` | Owner narration, immutable (SHA256 `3eff2e57…0328`) |
| `KEYFRAME_TIMELINE.json` | Editable V3 timeline: 36 states, 120 tracks, 634 keys, 28 camera keys, `audio_mix`, `end_hold` |
| `player.html` | Keyframe player. Scrubs and plays with the V3 mix |
| `tools/build_timeline.py` | Storyboard + layer map + alignment → timeline + SRT. **Retime here** (`CUES`, `WRITE`, `MORPH`, `FACES`, `END_HOLD`) |
| `tools/sound.py` | Timeline + narration → music bed, effects and mix. **Tune the mix here** (`BED_REL`, `DUCK`, `CUE_SFX`). `--music <file>` swaps in a licensed bed |
| `tools/render.cjs` | Headless Chrome over CDP → PNG → ffmpeg. Uses `audio_mix` when built; `--audio` overrides |
| `tools/qa.py` | `states`, `video [--narration]` and `sheet` checks |
| `AUDIO_ALIGNMENT.json`, `tools/align_audio.py`, `AUDIO_PROVENANCE.md` | Word timing behind every cue; narration provenance |
| V2 files | `Finance_Short_02_FINAL.mp4`, `Finance_Short_02_PREVIEW.mp4`, `FINAL_CONTACT_SHEET.png`, `FINAL_VIDEO_QA.md/json`, `STATE_IDENTITY_QA.json` |

## Rebuild V3 (from `finance-short-02-visual-calibration/`)

Requirements:
- Python 3.9+ with numpy; Pillow too for QA.
- Node 22+, Google Chrome and ffmpeg.

```sh
python3 animation/tools/build_timeline.py          # timeline + SRT
python3 animation/tools/sound.py                   # bed, effects, mix (deterministic, seed 20261014)
node animation/tools/render.cjs --out /tmp/clip.mp4 --from 14 --to 22 --scale 0.5   # check one window
node animation/tools/render.cjs --out animation/Finance_Short_02_FINAL_v3.mp4      # about 2.2 min
ffmpeg -i animation/Finance_Short_02_FINAL_v3.mp4 -vf "scale=540:960:flags=lanczos,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv" \
  -c:v libx264 -preset slow -crf 20 -tune animation -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -c:a copy -movflags +faststart animation/Finance_Short_02_PREVIEW_v3.mp4
python3 animation/tools/qa.py video animation/Finance_Short_02_FINAL_v3.mp4
python3 animation/tools/qa.py sheet animation/Finance_Short_02_FINAL_v3.mp4 animation/V3_CONTACT_SHEET.png
```

**Important:** re-run `sound.py` after any retime, because effect times are read from the timeline.

**Determinism:**
- The renderer runs Chrome with `--num-raster-threads=1`, so repeated or reordered renders of a frame are byte-identical.
- Cross-machine pixel identity is only expected with the same Chrome and ffmpeg versions: Chrome 155.0.8059.40, ffmpeg 9.0.1.

## Open items for the owner

1. **Watch and listen** to `Finance_Short_02_FINAL_v3.mp4` on a phone, on the speaker and on headphones. Nothing here certifies human listening or artistic approval. Check:
   - the bed level;
   - the 10 effects;
   - the three face reactions;
   - whether any hold still feels fast. The short ones are listed in `V3_VISUAL_QA.md`.
2. **Music.** The bed is original, with no third-party licence involved. A YouTube Audio Library track would need the owner's Studio download; see `V3_AUDIO_LICENSES.md` for the swap steps.
3. **Captions** are unchanged: lettering appears on the spoken words, plus `Finance_Short_02.en.srt` for CC.
4. **Fine attribution text** is small on a phone (inherited artwork).
5. **Re-check H.4.1** before publishing (−233,587, dated 7 Oct 2026 on screen).
