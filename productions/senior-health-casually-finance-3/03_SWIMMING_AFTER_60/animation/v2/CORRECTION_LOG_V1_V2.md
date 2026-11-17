# Swimming: V1 → V2 correction log

**Files.**
- V1 unchanged: `animation/Swimming_After_60_V1_REVIEW*.mp4`, `project.py`.
- V2 project: `../project_v2.py`.
- Frame evidence: `CORRECTED_FRAMES_V1_V2.png`.

## Audio
- **Narration:** original, unchanged, with an 8 ms fade-in and 30 ms fade-out.
- **Music:** −24 dB relative to speech.
- **SFX:** 5 events, the same count as V1.
- **Peak:** −1.0 dBFS.

## Captions
- **Cue length:** 14 V1 cues (lower-case, unpunctuated) became 9 phrase cues (minimum 0.94 s, median 1.82 s) with sentence case and punctuation.
- **Removed:** amber on the S5 sentence, the S5 claim ID and the review strip.

## Hook (0–3 s)
June is already swimming freestyle across the pool at frame 0, with a small beating heart above her ("and your heart?"). The rating lands on "9.5".

## Swimming animation
**One stage.** One pool and no cuts. V1 cut five times between the pool and a standing June, and back.

**Body as one rig.** An invisible root carries the travel (right → left, head-first, 250 → 90 px over the clip) and a gentle bob. Every part is parented to it:
- Front arm: a 15° pull about the shoulder, biased downward (+12°) so it reads as a stroke rather than a wave.
- Rear arm: an 18° recovery in opposite phase.
- Legs: a 7° flutter about the hips at 0.45 s.

**Checked across 12 consecutive frames at 10 fps (5.0–6.1 s):**
- shoulders and hips stay attached
- body orientation is constant
- the waterline crosses the torso, with the submerged limbs behind a 55% water layer
- no floating segments
- feet stay clear of the ladder

V1 had 4–6° limb swings on a stationary swimmer.

## Storytelling
Built with minimal new elements: text labels only, no new artwork.
- **Heart:** grows out of its place above the swimmer on "heart". Label: "the speaker's view".
- **Endurance:** the stopwatch joins on "best exercise for endurance".
- **Whole body:** the camera moves closer, and "arms", "legs" and "core" labels pop on the moving swimmer word by word.
- **Joints:** headline "What about the joints?" with a neutral healthy-joint close-up that pulses on each spoken "joints". This replaces V1's "Joints still move", which asserted an interpretation.
- **Rating:** the badge returns.

No ranking graphic is shown, and the "best exercise" claim is never presented as fact.
