# Running After 60 — V1 review preview QA

**Status: owner-review preview. NOT publication-ready.** Clinical and listening approvals are pending. The original audio is unchanged apart from one whole-mix gain.

## Outputs
- **Full preview:** `Running_After_60_V1_REVIEW.mp4`: 31.933 s, 1080×1920, 30 fps, H.264 yuv420p plus AAC 192k, 958 frames.
- **Mobile preview:** `Running_After_60_V1_REVIEW_MOBILE_540x960.mp4`.
- **Editable project:** `project.py`, using the shared engine `../../tools/anim.py`. The committed `raster/` holds 3× PNGs of this package's own SVGs.
- **Supporting files:**
  - `KEYFRAME_TIMELINE.json`: 45 layer tracks.
  - `CAPTIONS_REVIEW.srt`: 30 chunks.
  - `AUDIO_PROVENANCE.json`
  - `CONTACT_SHEET.png`, made from the encoded MP4.
  - `qa/RENDER_QA.json`

## Artwork gate
The assets were kept as delivered: Sam, Nora, the park, heart, joint, shoe, stopwatch, calendar, lungs, arrow and score.

The same composition defects as in HIIT were fixed in the compositor:
- tiny headlines
- internal copy in the viewer area
- no captions

The calendar was enlarged to 1.25× so its "SPEAKER'S LIMIT" label can be read on a phone.

## Motion
There are 8 scenes and 7 hard cuts at the storyboard times.
- **Hook:** frame 0 shows "Running after 60?" with the runner. The 7/10 score pops on the spoken "7".
- **Runner:** stays in place with a bob while the park tree drifts at 28 px/s for parallax, so the feet do not slide. The park runs continuously across S01 and S02, and the closing scene repeats it as a callback.
- **Joint (S03):** the bones appear on "problems" and the ring highlight on "knees". The joint stays intact, with no damage drawn. The shoe appears on "ankles".
- **Calendar (S05):** the frame appears on "not", the days wipe in on "3" and the "speaker's limit" note on "week".
- **Lungs and heart (S07):** the lungs are on screen at the cut. The O₂ mark appears on "oxygen", the heart on "maximum", and the arrow wipes in on "extraction".
- **Stopwatch:** the hands rotate. Each scene has a gentle camera push of 3–6%.

## Audio
- **Voice:** `original_audio.m4a` (sha256 `a00c28af…7277`, verified) is unchanged. The whole mix is scaled ×0.831 because the source peaks reach about 0 dBFS. The encoded max is −0.9 dB.
- **Source check:** the source has no music bed. The noise floor measures about −71 dB.
- **Music:** a bed synthesised here (G–D–Em–C) sits 22 dB under the speech.
- **SFX:** 13 soft synthesised effects.

## Technical QA
- **Decoding:** the full file decodes with no errors.
- **Blank frames:** none. The lowest frame std is 27.5.
- **Scene cuts:** no unplanned large frame jumps.
- **Sync:** video 31.933 s, audio 31.933 s.

## Medical / listening items (still blocking)
- **R3, 4.6–11.4 s:** a broad joint-problem claim. The ASR "muscular scuttle system" is shown amber and is probably "musculoskeletal", but this has not been verified.
- **R5, 14.4–19.7 s:** "not more than 3 times per week". This is a universal frequency limit with no supporting evidence. It is shown only as "Speaker's limit".
- **R7, 24.0–28.4 s:** the VO₂ / "maximum oxygen extraction" terminology. "of the other blood" is shown amber. No numbers or physiology diagram were added.
- **R1:** the 7/10 rating is labelled "speaker's opinion".
- No human listening or clinical approval has been given.
