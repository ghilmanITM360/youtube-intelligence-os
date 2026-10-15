# Swimming After 60 — V1 review preview QA

**Status: owner-review preview. NOT publication-ready.** Clinical and listening approvals are pending. The original audio is unchanged apart from one whole-mix gain.

## Outputs
- **Full preview:** `Swimming_After_60_V1_REVIEW.mp4`: 17.867 s, 1080×1920, 30 fps, H.264 yuv420p plus AAC 192k, 536 frames.
- **Mobile preview:** `Swimming_After_60_V1_REVIEW_MOBILE_540x960.mp4`.
- **Editable project:** `project.py`, using the shared engine `../../tools/anim.py`.
- **Supporting files:**
  - `raster/`: 3× PNGs
  - `KEYFRAME_TIMELINE.json`: 59 layer tracks
  - `CAPTIONS_REVIEW.srt`: 14 chunks
  - `AUDIO_PROVENANCE.json`
  - `CONTACT_SHEET.png`
  - `qa/RENDER_QA.json`

## Artwork gate
The assets were kept as delivered: June standing, June swimming, the pool, heart, stopwatch, joint and the 9.5 score.

**Confirmed defect: the swimmer floated on top of the water** in the static states, with the whole body above the pool line. This was fixed in the compositor without redrawing anything:
- The waterline now runs through June's torso, and the pool's water part is drawn again in front at 55% opacity, so the submerged arm and legs read as under water.
- The swimmer is 1.1× and moved left so the forward hand stays inside the pool wall and the feet are clear of the ladder.
- S05 also shows the pool, so the swimmer is never in mid-air.

The same headline, caption and review-strip fixes as in the other two videos also apply here.

## Motion
There are 6 scenes and 5 hard cuts.
- **Hook:** frame 0 shows "Swimming after 60?" with June swimming. The 9.5/10 score pops on the spoken "9".
- **Swim stroke:** the straight forward arm swings ±6° about the shoulder and the recovery arm ±5°. The legs flutter ±4° about the hip in opposite phase. There is no rotation at the elbow and no whole-body bob, so the limbs stay attached. The ripples drift.
- **Heart:** it pops on "heart" and moves into S03 from its S02 position.
- **Stopwatch:** it appears on "endurance" and its hands rotate.
- **Joint (S05):** the joint and its ring pop on "joints", and the ring pulses on the second "joints".

## Audio
- **Voice:** `original_audio.m4a` (sha256 `bebc1a4d…20cf0`, verified) is unchanged. The whole mix is scaled ×0.855 and the encoded max is −1.1 dB.
- **Source check:** the source has no music bed; the noise floor is about −69 dB.
- **Music:** a calm bed synthesised here (F–C–Dm–B♭) sits 22 dB under the speech.
- **SFX:** 5 soft synthesised effects.

## Technical QA
- **Decoding:** the full file decodes with no errors.
- **Blank frames:** none. The lowest frame std is 28.9.
- **Scene cuts:** no unplanned jumps.
- **Sync:** video and audio are both 17.867 s.

## Medical / listening items (still blocking)
- **S5, 11.9–14.8 s:** "without using the joints you are using the joints". Both ASR runs contradict each other here. The caption is amber and verbatim. The headline "Joints still move" is the claims register's editorial clarification, not speech.
- **S2/S3:** the "best exercise" ranking is spoken but has no supporting evidence. No podium or ranking visual is used; the headlines say "Heart fitness" and "Fitness + endurance".
- **S1/S6:** the 9.5/10 rating is labelled "speaker's opinion".
- No human listening or clinical approval has been given.
