# HIIT: V1 → V2 correction log

**Files.**
- V1 files are unchanged: `animation/HIIT_After_60_V1_REVIEW*.mp4`, `project.py`, `tools/anim.py`.
- V2 lives in `animation/v2/`: editable `../project_v2.py`, engine `tools/anim_v2.py`.
- Frame evidence: `CORRECTED_FRAMES_V1_V2.png`.

## Audio: opening pace (owner-authorised)
**Measured rate.** Syllables per second (ASR words, vowel-group estimate):
- Opening "…or high-intensity interval training": **9.3**
- "good for cardiovascular conditioning": **8.5**
- Whole clip: 7.2 (Running speaker 5.7, Swimming speaker 4.8)
- "I'll give that 7 out of 10": 5.8, natural, so it was left unchanged.

**Edit plan.** All splice points sit in measured silences: 1.30 s at −56 dB, 2.96 s at −72 dB, 7.37 s at −74 dB.
- 0.00–1.30 s: `atempo` 0.90 (pitch-preserving WSOLA)
- 1.30 s: 0.12 s pause inserted, inside an existing pause
- 1.30–2.96 s: unchanged
- 2.96–7.37 s: `atempo` 0.93. There is no internal pause, so one uniform rate is used.
- 7.37 s to end: unchanged
- 6 ms micro-fades at every splice; 8 ms fade-in at the start.

**Result.** Duration went from 30.557 s to 31.127 s (+0.57 s). The voice is now ~8.4 syl/s at the opening and ~7.8 at "conditioning".

**Checks (machine only).**
- small.en re-transcribes the identical words, with mean word probability 0.923 → 0.926.
- Median F0 is 141.6 → 142.9 Hz, so pitch is preserved (<1%).

**Not verified.** Absence of metallic or phasey artefacts needs human listening. If artefacts are heard, revert: set `voice=None` in `project_v2.py`. Captions and keyframes re-time automatically.

**Provenance.** `VOICE_PACING.json` holds the plan, time map and hashes:
- source `original_audio.m4a` sha256 `c24c8990…6cc5` (unchanged, re-verified)
- derived `source_audio/voice_v2_paced.wav` sha256 `e8f9784e…60c9` (git-ignored like all audio, and reproducible from the plan)

Every word, cue, scene and keyframe time is mapped through the time map.

## Captions
- **Cue length.** 34 cues of 2–3 words (median 0.8 s, shortest 0.42 s) became 20 phrase cues (median 1.64 s, minimum 0.86 s).
- **Layout.** Two balanced lines, 66 px, placed at 1330–1492 px, above the Shorts title/UI band.
- **Wording.** "avoided/awarded" became "avoided in", "high intensity" became "high-intensity", plus the other rows in `CAPTION_VERIFICATION.md`.
- **Removed.** The amber underline and slash display.

## Removed from frames
- The "REVIEW PREVIEW" strip.
- The claim IDs and time ranges (H4/H5/H6) shown in V1 at 13.4–24.3 s.
- The amber QA styling.

These are now in the QA files only. The video remains publication-blocked.

## Hook (0–3 s)
- **Frame 0:** headline "HIIT after 60?", a tall WORK bar, and Sam already in a run cycle on a path. In V1 he was a floating static pose with a bob.
- **Bars:** EASY, WORK, EASY, WORK grow from the baseline in step with "intensity", "interval" and "training".
- **Label:** "example: hard + easy intervals", readable size. It replaces V1's 14 px "illustrative pattern" note and keeps the "not a prescription" boundary.
- **Rating:** the badge pops on "7" with "speaker's rating". V1's attribution text overflowed the badge outline.
- **Exit:** all hook graphics fade before the headline changes.

## Motion and continuity
- **Engine:** layers sit on one global timeline. V1 rebuilt every scene, so the heart jumped from (640,470,0.95) to (680,800,0.75) at 7.72 s.
- **Shots:** three stages, park/outdoor → clinic → park, with only two hard cuts. V1 had 7 scene rebuilds.
- **Run cycle:** arms swing about the shoulder anchors in opposite phase, the body hops twice per stride, and the legs rock about the hips. Sam slows before stopping on "However".
- **Heart:** it grows out of Sam's chest on "heart" and pulses on "cardiovascular" and "conditioning". The concern marker is parented to the heart.
- **Clinic:**
  - Plant removed (V1: it overlapped Sam's leg).
  - Window moved between the people, so Nora's pointing hand no longer touches it.
  - Nora enters from her own side.
  - Pose changes are staggered: Nora on "Or", Sam on "higher".
- **Camera:** eased push-ins (1.06 and 1.08) between ideas, then held. The camera stays still while captions change, and it widens before the callback.
- **Callback:** the hook's hard/easy bars return and dim on "avoided", tying the advice to the opening visual.
- **Endurance:** Sam runs into the frame (actual travel). The stopwatch appears on "endurance", then Sam stops and the rating returns.
- **Headlines:**
  - V1 "Risk needs context" became "Why the caution?".
  - V1 "Not one rule for everyone" softened the speaker's message, which is to avoid HIIT with CVD. It became "Heart disease? Avoid it", attributed as "the speaker's view".

## Sound
- **Reused:** the music synthesis and SFX palette. Music is now −24 dB and SFX −19 dB relative to speech (V1: −22 and −16).
- **SFX:** 9 events instead of 11; ticks only on two bars; a soft whoosh on the 2 cuts.
- **Edges:** 30 ms end fade. Peak −0.9 dBFS, no clipping.
- **Rights:** this does not settle any rights question.
