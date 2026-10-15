# HIIT After 60 — V1 review preview QA

**Status: owner-review preview. NOT publication-ready.** Clinical and listening approvals are pending. The original audio is unchanged apart from one whole-mix gain.

## Outputs
- **Full preview:** `HIIT_After_60_V1_REVIEW.mp4`: 30.567 s, 1080×1920, 30 fps, H.264 yuv420p plus AAC 192k, 917 frames.
- **Mobile preview:** `HIIT_After_60_V1_REVIEW_MOBILE_540x960.mp4`.
- **Editable project:** `project.py` holds the scene, layer and keyframe data; the engine is `../../tools/anim.py`.
  - `raster/` contains 3× PNGs of the package's own SVGs. They are committed so a clone can render with Python, Pillow and ffmpeg alone.
- **Supporting files:**
  - `KEYFRAME_TIMELINE.json`: 37 layer tracks.
  - `CAPTIONS_REVIEW.srt`: 34 chunks.
  - `AUDIO_PROVENANCE.json`
  - `CONTACT_SHEET.png`, made from the encoded MP4.
  - `qa/RENDER_QA.json`

## Artwork gate (against `CASUALLY_FINANCE_VISUAL_SPEC.md` and `reference_local/reference_sheet.jpg`)
The assets were kept as delivered. The characters, heart, intervals, clinic, park, stopwatch and score are consistent, original, white-canvas and outlined, and their parts register correctly.

The confirmed defects were at composition level. They were fixed in the compositor, not by redrawing assets:
1. **Small headlines.** They were about 36–50 px, which is not readable on a phone. They are now 100+ px Chalkboard Bold with one coral keyword.
2. **Internal review copy in the viewer area.** Lines such as "No risk percentage supplied", "Clinical review required" and the review footer have moved to a single top review strip. That strip names the claim ID and timestamp during disputed windows.
3. **No captions.** Word-timed captions have been added from the small.en ASR, and the current word is highlighted.
4. **Hook.** Frame 0 now shows "HIIT after 60?" with Sam running, and the interval bars build on "high / interval / training".

## Motion
There are 8 scenes and 7 hard cuts at the storyboard times. The motion is restrained:
- **Staged builds:** the work and recovery bars build one by one. Entrances are 8-frame rises or pops on the spoken cue word.
- **Pose changes:** Sam keeps one stage position across S01–S03 and S05 and swaps between run, stand and concern poses. He stops running on "good for the heart".
- **Small movements:** a light bob while running and a heart pulse on "cardiovascular". In S03 the heart moves from its S02 position.
- **Line and background reveals:** the arrow is revealed with a stroke wipe. In S07 the tree moves for parallax while the runner stays in place, so the feet do not slide.
- **Other motion:** the stopwatch hand rotates around the dial centre, and the camera pushes in slowly by 2–6% per scene.
- **Nothing added:** no bounce, whooshes or random entrances.

## Audio
- **Voice:** `original_audio.m4a` (sha256 `c24c8990…6cc5`, verified) is decoded unchanged from t=0. Its peaks reach about 0 dBFS, so the whole mix is scaled ×0.871. The encoded max is −1.0 dB.
- **Source check:** pauses measure about −56 dB and the noise floor about −69 dB, so the source has no music bed. This was measured, not listened to.
- **Music:** a bed synthesised here (C–F–G–Am) sits 22 dB under the speech RMS. No samples or library tracks are used.
- **SFX:** 11 soft synthesised ticks, pops and chimes at visual events.

## Technical QA
- **Decoding:** the full file decodes with no errors.
- **Blank frames:** none. The lowest frame std at 10 fps is 32.6.
- **Scene cuts:** large frame jumps occur only at the planned cuts.
- **Sync:** audio and video durations are equal. Cues come from the ASR word times and have not been checked by listening.

## Medical / listening items (still blocking)
- **H4, 13.4–16.2 s:** "must be supervised by an expert cardiologist". The absolute wording needs clinical review.
- **H5, 16.2–21.3 s:** "mortality or mobility" may be "morbidity". The caption is amber and the strip is flagged.
- **H6, 21.3–24.3 s:** one ASR model heard "avoided" and the other "awarded". The caption shows `avoided/awarded` in amber. The headline "Not one rule for everyone" is an editorial proposal from the claims register, not speech.
- **H1 and H8:** the ratings are labelled "speaker's opinion".
- No human has listened to the full preview or approved it clinically.
