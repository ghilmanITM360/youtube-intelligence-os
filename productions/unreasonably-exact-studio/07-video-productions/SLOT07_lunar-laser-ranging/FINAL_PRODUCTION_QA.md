> **Superseded (2026-11-26).** This file describes V2. The final version is V3: see `renders/roughcut_v3/FINAL_PRODUCTION_QA.md` and `OWNER_ACCEPTANCE_RECORD.md`.

# Final production QA: ROUGH_CUT_V2 (2026-11-26)

**Status:** V2 editorial revision complete. It is **not** owner-accepted and **not** human-reviewed.

## Deliverables

All video files are in `renders/roughcut_v2/`.

| File | Check |
|---|---|
| `ROUGH_CUT_V2_PREMIUM.mp4` | 1080×1920, H.264 + AAC 256k, 96.000 s, 2880 frames; clean, no captions; global grade |
| `ROUGH_CUT_V2_PREMIUM_CAPTIONS.mp4` | the same picture with caption style A burned in |
| `ROUGH_CUT_V2.srt` | 49 cues; all 245 narration words in order; no overlaps |
| `CAPTION_STYLE_COMPARISON.png` + `CAPTION_STYLE_NOTES.md` | 3 treatments × 3 scenes; decision record |
| `SFX_LICENCE_MANIFEST.csv` | 23 original files, 3 OFL fonts, the local library (EXCLUDED), 3 researched sources (nothing downloaded) |
| `SOUND_DESIGN_CUE_SHEET.csv` | 115 cues, each with time, file, gain, kind (literal vs illustrative), stem and purpose |
| `ON_SCREEN_TEXT_AUDIT.csv` | 21 text elements classified, with action and result |
| `AI_GENERATED_APPEARANCE_AUDIT.md` | per defect: timestamp, cause, correction, verification |
| `SCIENTIFIC_COMPREHENSION_QA.md` | object → happens → why → result, per concept; muted-viewer protocol |
| `V1_V2_IMPROVEMENT_REPORT.md` | before/after table |
| `qa/V2_TIMESTAMPED_CORRECTION_LIST.csv` | written from the V1 review before changes; status for each item |
| `FINAL_REPORT_ROMAN_URDU.md` | owner report |

### Editable sources

- **Assembler:** `animation/roughcut.py`, with a `--range` patch mode.
- **Scenes:** `animation/proofs/*.py`.
- **Captions:** `tools/captions_v2.py`.
- **Sound:** `tools/sound_design_v2.py`.
- **Finishing (grade, mux, burn):** `tools/finish_v2.sh`.
- **Stems:** `renders/roughcut_v2/stems/`, covering narration, music bed, ambience and mechanical, illustrative FX, and the bed total.
- **Pre-master mix:** `final_mix_v2_premaster.wav`.
- **Art provenance:** unchanged (`qa/asset_tracker.csv`, `MASTER_ASSET_MANIFEST.csv`). No artwork was replaced.

### How the clean picture was assembled

`ROUGH_CUT_V2_clean.mp4` is the full render (`*_prepatch.mp4`) with frames 2022–2141 (67.40–71.40 s) replaced by `patches/PATCH_067.40_071.40.mp4`. That patch carries the G29 label-size fix and the trail clamp. The frame-difference values at both splice edges are 0.16–0.28, the same as neighbouring frames.

## Review passes

### 1. Scientific correctness

- **Code checks.** All checks that can run without a render pass:

  | Scene | Checks passed |
  |---|---|
  | OPEN | 19/19 |
  | P03 | 9/9 |
  | P04 | 6/6 |
  | P06 | 6/6 |
  | P08 | 6/6 |
  | P09 | 6/6 |
  | P10 | 10/10 |
  | P12 | 8/8 |
  | P13 | 8/8 |
  | Gap scenes (including the new G29) | 6/6 |

  P11's checks need its own render output and were not re-run; P11's code was not changed. Results are in `qa/V2_check_results.json`.
- **Numbers on screen.** Every number comes from the claims ledger (C01, C03, C04, C10). G29 shows no number, as the C09 rule requires, and carries the badge "SLOWDOWN HUGELY EXAGGERATED".
- **Sound in vacuum.** No sound implies sound travels through space. The pulse flight, the Moon set-down and the reflector have only illustrative musical accents, and the cue sheet labels each one.

### 2. Narration synchronisation

- **Unchanged anchors.** All proof anchors are as before: the pulse arrives on "reflector", the stopwatch on "seconds", the fold on "two", the reticle on "where".
- **New or moved in V2:**
  - "A few photons" now shows three dots.
  - G29's correction lands 0.15–0.75 s after "atmosphere".
  - The P13 dissolve still completes on "trick".
- **Caption timing.** Cues follow the word timestamps, which are estimates good to about ±0.12 s.

### 3. Animation craft

- **Frame differences, V1 → V2.**
  - Maximum: 30.1 → 25.8.
  - Frames above 3× median + 2: 277 → 188.
  - The remaining peaks are at the P13 push (44.6–45.1 s). That is a deliberate fast push, softened by motion blur and rack focus.
- **Continuity.** The astronaut now completes the release before the dissolve.
- **Stills.** The 1080 stills show smooth cube rims through the push.

### 4. Composition

- **Fixed:** badges are inside the safe area, and captions are clear of the Earth-limb station.
- **Still weak (V3):**
  - the imagined-mirror box at 38–39 s;
  - the empty data-plot fields at 60–67 s;
  - the small final orbit at 88–96 s.

### 5. Sound

| Measure | Value |
|---|---|
| Final loudness | −17.4 LUFS integrated |
| True peak | −1.9 dBTP |
| Voice above bed | 19.9 LU overall; 26 dB during speech |
| Limiter | touches 0.38 % of samples |

- **Ducking.** The bed is ducked 8 dB under speech, with an extra 1–4 kHz cut.
- **Intentional silence.** The bed drops for "But hold on" (31.0–31.7 s) and before the answer at 15.2–15.9 s.
- **Not listened to by anyone.**

### 6. Typography

- **Font:** Comic Neue Bold (OFL), phrase-level captions, no card.
- **Reading rate:** at most 23 characters per second.

### 7. Mobile readability

- **Checked:** labelled contact sheets at 270×480 per frame, roughly a phone thumbnail. These show:
  - captions readable;
  - G29 labels readable after the second patch;
  - badges small but legible.
- **Not checked:** the film has not been watched on a real phone.

### 8. Artistic consistency

- **Global grade:** contrast, saturation, split tone, vignette and grain.
- **Not done:** the painterly-versus-photoreal question (D10) still needs the owner's decision.

## V2 full-film review: method and limits

### What Claude did

- Read 4 labelled contact sheets (46 frames across the 96 s), plus close strips of P13 (44.9–45.5 s) and G29 (67.6–71.2 s, three times while fixing it).
- Measured frame differences on every frame of V1 and V2.
- Measured loudness with ebur128.
- Ran the code checks.

Defects found during the review and fixed before delivery:

- G29 labels too small.
- "no air" label invisible on white ice.
- Pulse trail running past the finish line.
- A splice jump at 71.0 s.

### What Claude did NOT do

- **Continuous real-time viewing.** Claude cannot play video in real time; it can only read sampled frames.
- **Listening.** Claude cannot hear audio.
- **Muted-viewer test with real people.**
- **Owner acceptance.**

### Review package for the owner

1. Watch `ROUGH_CUT_V2_PREMIUM_CAPTIONS.mp4` on a phone, once with sound and once muted.
2. Listen to the first 16 s on headphones. Check that the curiosity bed is audible but never competes with the voice, and that the "not this" and "question" cues feel playful rather than cartoonish.
3. Run the muted-viewer protocol in `SCIENTIFIC_COMPREHENSION_QA.md`.
4. Decide D10 (keep the near-photoreal style with the grade, or commission a painterly pass).
