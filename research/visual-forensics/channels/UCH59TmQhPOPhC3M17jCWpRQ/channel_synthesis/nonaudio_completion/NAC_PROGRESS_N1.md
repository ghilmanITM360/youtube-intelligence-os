# Non-audio completion — progress checkpoint N1 (2026-11-04 ~17:20 UTC)

- **Session:** 1e8761b1.
- **Lock:** `.be_writer_lock`, held since 17:03:58Z.
- **Remote parent:** afadfbc402b89131210d03677fbdf6845d3520c2.
- **Why this checkpoint exists:** the five-hour meter reached 83% at 17:17 UTC, so model-heavy work is paused until the 20:00 UTC reset.
- **Scope:** this is a progress checkpoint, not a completion claim. Listening and AV sign-off stay BLOCKED and are excluded.

## Done (with evidence)

**Camera ease.** Evidence is in `camera_ease/` and `../../2026-11-03-mNLNb-Z4T0M-deep-ct-scan/reconstruction_test/RT-V2-02/`.
- **Diagnosis: COMBINATION.**
  - The reference spec was wrong. S080 is a horizontal pan: tx 0→137.8 px over 16 frames, f8178–8193, scale constant at about 1.001. It was mislabelled as a push.
  - The `mad>0.3` criterion was unsuitable because it depends on texture.
  - The flat test scene was also unsuitable.
- **RT-V2-01** keeps its original FAIL, and its EVALUATION.json is unchanged.
- **RT-V2-02.**
  - The criterion was pre-registered before the render (sha256 ef7b5533…).
  - A fresh worker rendered the test.
  - Deterministic evaluation: PASS on 7/7 criteria (progress RMS 0.0012, tx 137.34).
  - Negative control: the RT-V2-01 render FAILs 6/7 criteria under the same criterion.

**v1 closure** (`v1_closure/`).
- **W085b.** The text fades in over f13993–13999, a word swaps on a single frame at f14029, and the shot ends in a hard exit at f14059. There is no fade-out, so the states_v6 "fade to black" claim is NOT_SUPPORTED.
- **f2835 and f5429.** Both are recorded as CAMERA:DIGITAL_ZOOM_PUNCH_IN events, not splits. The partition stays at 89 states.

**Dense every-frame measurement** (`dense/`).
- Every decoded frame of all three videos (47,655 frames) was given a frame-to-previous similarity fit and a residual.
- Every frame of the 850 previously uninspected intervals (`UNINSPECTED_INTERVALS_v1.csv`) was classified as CAM, LOC, BOTH or STATIC.
- **Label: MEASURED.** This is not visual naming. No event in these intervals has been visually identified yet.

**Crosswalk prep.** The per-state thumbnail sheets are local-only, and `crosswalk/BRIEF_CROSSWALK.md` is written.

## Not done (next operations, in order)

1. **Name the dense intervals visually.**
   - Build contact sheets around LOC spikes, long LOC runs and stepped-camera flags taken from `dense/DENSE_INTERVAL_CLASSIFICATION_v1.csv`.
   - Run one bounded reviewer per video, one at a time.
   - Write any corrections to new ledger versions.
2. **Crosswalk reviewer** → `crosswalk/ASSET_CROSSWALK_v1.csv`, then spot-check it.
3. **Style and full-scene reconstruction tests.**
   - Scenes: v1 W021, v2 S067, v3 S057.
   - Build the specs, render with fresh workers, then evaluate with a deterministic pass plus a visual pass.
4. **Portability:** inventory the needed files and check for an approved storage destination.
5. **Close-out:** matrix v2, gates, synthesis v1.2, manual, handoff, validate, publish, release the lock.

R05, R07, R10, R11, R15, R16 and R20 remain PARTIAL until these are done.
