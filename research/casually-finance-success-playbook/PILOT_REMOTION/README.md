# Nori: rendered original finance-quality pilot

**Status: PILOT_RENDERED_QUALITY_GAPS.** A 42-second, 1920×1080, 30-fps original explanation of why a policy rate cut does not automatically reset a standard U.S. fixed-rate mortgage. The final H.264/AAC MP4 is real animation; SVG limbs, charts, props and camera transforms remain editable. It contains original artwork/script, local synthetic narration, an original synthesized music bed and SFX. No competitor artwork enters the pilot.

## Open these first

- Final pilot MP4 (retained target `render/fixed-mortgage-pilot.mp4`)
- Actual moving comparison, internal review only (retained target `evidence/motion-comparison.mp4`)
- [Honest ten-dimension comparison and next fixes](QUALITY_REVIEW.md)
- [Timing, asset counts and 5–8-minute scaling estimate](PRODUCTION_REPORT.md)
- [Primary factual sources, attribution correction and rights](SOURCE_REFERENCES.md)
- Final contact sheet (retained target `evidence/pilot-contact-sheet.jpg`), paired comparison (retained target `evidence/quality-comparison.jpg`), temporal samples (retained target `evidence/temporal-motion-strip.jpg`), 320px/160px previews (retained target `evidence/mobile-preview.png`)
- Character pose/expression board (retained target `evidence/CharacterBoard.png`), asset board (retained target `evidence/AssetBoard.png`), editable SVG assets (retained target `assets`)
- [Measured QA](evidence/render-qa.json), [seek determinism](evidence/seek-determinism.json), [asset/motion inventory](evidence/asset-and-motion-inventory.json), [hash manifest](evidence/FILE_HASHES.json)

The root 206-upload research, 29-page Word report and ten-sheet Excel workbook were reused; they were not audited again. This pilot extends PR #28 in a new directory and does not modify PR #21, PR #25 or Dr Rehan deliverables. The earlier eight-second HyperFrames demonstration remains a separate artifact. This pilot is **Remotion**, as explicitly requested.

## Rebuild and edit

From this directory, with Node 20+ and npm:

```sh
npm ci
npm run check
npm run studio
```

`src/art.tsx` owns the original character/environment/props; `src/motion.ts` owns pose interpolation, two-bone legs and motion functions; `src/camera-presets.ts` provides push/pull/pan; `src/Pilot.tsx` owns eight scenes and caption staging; `src/story.ts` records the original narrative. `src/timeline.json` freezes measured clip timings. `assets/` contains 21 derived editable SVG exports, not 21 unique character drawings.

Render uses retained audio stems and does not call a paid service or regenerate narration:

```sh
npm run render
node tools/determinism.mjs
```

The default browser is macOS Google Chrome at `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`; set `PILOT_BROWSER` to your Chrome executable if needed. The standard macOS Arial font was used. A different browser/font/platform can change rasterization or layout, so check output again rather than assuming pixel-identical results. This machine's seek sequence 556 → 0 → 556 produced identical PNG hashes.

QA/contact sheets and optional audio rebuilding require Python with NumPy/Pillow and system FFmpeg/FFprobe. Set `PILOT_FONT` for a different licensed Arial-compatible font if needed. The creator's bundled Python is `/Users/ghilmanislam360/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`.

```sh
python3 -m pip install -r tools/requirements.txt
python3 tools/qa.py
node_modules/.bin/tsx tools/export-assets.tsx
python3 tools/inventory.py
python3 tools/hash_outputs.py
```

Optional **local** voice regeneration (not needed to rerender): `node tools/voice.mjs`, then `python3 tools/mix_audio.py`. The pinned open-source Kokoro model may download about 96MB of local cache on first use. `af_heart` is a bundled synthetic voice, not a clone. Regenerated TTS output may vary across library/platform changes; validate clip durations and regenerate timing before rendering. Frozen WAV stems are the final render's source of truth.

Internal reference reconstruction: `python3 tools/references.py` then `python3 tools/compare.py`. This needs the three existing local source files at the paths recorded in `evidence/reference-sequences.json`; it performs three bounded extracts after hash validation. Do not publish reference footage/contact sheets as original assets.

Local review player:

```sh
python3 -m http.server 3033 --bind 127.0.0.1
```

Open `http://127.0.0.1:3033/preview.html`. Exact narration is supplied in SRT/VTT; burned captions summarize each sentence. Full-text cue subdivision is proportional timing, not certified word alignment.

## Validation and limits

Final video: 1,260 frames, full decode clean; no detected black or byte-identical consecutive decoded frames; zero clipped SVG text in every rendered frame; no browser runtime errors; eight scheduled voice clips fit; no clipped narration by duration; measured mix about −16.7 LUFS with headroom. Fixed bone lengths and reachable feet were checked for every frame. These are technical proxies, not a human quality certificate. Slow camera motion can make frames differ during intentional information holds.

Native samples and temporal excerpts retain identity and coherent anatomy at inspected states. Detailed hand acting, mirrored grips, torso turns, word-level synchronization and long-form variety need further work. Full human listening and independent art-direction passes are pending. The output has not been published, and overall Casually Finance-level quality is not claimed.


Publication note. Retained targets named here are outside this scoped export. See the [folder and file map](../../../CHANNEL_VISUAL_AUDIT/CHANNEL_001/COMPLETE_FOLDER_AND_FILE_MAP.md) for disposition.
