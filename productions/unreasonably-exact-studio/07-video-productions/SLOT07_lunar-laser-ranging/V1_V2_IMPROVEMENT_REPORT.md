# V1 → V2 improvement report (slot 07, lunar laser ranging)

## Files

- **V1 (kept unchanged):** `renders/roughcut/ROUGH_CUT_V1_final.mp4`. Assembler frozen as `animation/roughcut_v1.py`.
- **V2:** `renders/roughcut_v2/`.
  - `ROUGH_CUT_V2_PREMIUM.mp4`: clean, no captions.
  - `ROUGH_CUT_V2_PREMIUM_CAPTIONS.mp4`: captions burned in.
  - `ROUGH_CUT_V2.srt`
  - stems in `stems/`
- **Narration:** unchanged. The V2 take is 95.39 s and 245 words; `narration/raw_v2/` was read only.

## At a glance

| | V1 | V2 |
|---|---|---|
| Resolution | 540×960 review render | 1080×1920 (supersampled 2×, 3-sample motion blur) |
| Opening 3.5–7 s sound | wind only (bed −49.9 dBFS RMS) | curiosity pad + "not this" + "question" cues (bed −37.7 dBFS RMS before master gain) |
| Sound library | 6 inline synth sounds | 23 original synthesised files in 8 categories (`audio/sfx/`), 115 cues, cue sheet |
| Mix | −21.8 LUFS, −1.0 dBFS sample peak | −17.4 LUFS integrated, −2.0 dBTP true peak; voice 19.9 LU above the bed (26 dB during speech); 1–4 kHz anti-masking cut |
| Captions | Helvetica-style bold on a dark card, gold box on each word | Comic Neue Bold (OFL), phrase level, no card, balanced lines, below the Earth-limb station; SRT delivered |
| B29 atmosphere | no picture | G29: air layer, slowed pulse vs no-air twin, delay, corrected |
| "A few photons" | histogram (mismatch) | three dots light one by one |
| Dome seam | visible while the shutter opens | removed (blend restricted to the slit) |
| P13 push | pixel stair-steps from 45.2 s, over-soft at 44.8 s | resolution follows the zoom; lighter rack focus; earlier dissolve |
| Astronaut → array cut | astronaut vanishes mid-action | P06 completes the release, then dissolves |
| Small dots | 4–6.5 units | 7–9.5 units, glow on the final points |
| Badges | 5 % from the top | 7.8 % (phone safe area); jargon badge simplified |
| Look | separate-looking photoreal and vector scenes | one global grade, vignette and grain |

## What did not change, and why

- **Codex artwork and rigs.** The brief says to preserve the reference-based realism.
- **Scene timing against the narration.** The proof checks still pass.
- **Remaining known weak spots** (`qa/V2_TIMESTAMPED_CORRECTION_LIST.csv`, C13–C15): the imagined-mirror box, the small final composition and the empty data-plot fields. All three are deferred to V3.

## What has not been verified

- Nobody has watched V2 continuously in real time.
- Nobody has listened to it.
- No muted-viewer test has been run.
- The owner has not accepted it.

Claude's own checks were frame stills, contact sheets, frame-difference statistics, loudness measurements and code checks. Those are not a substitute for watching and listening.
