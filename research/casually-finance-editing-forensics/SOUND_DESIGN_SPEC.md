# Sound design spec (PRELIMINARY, n = 10 Shorts for audio statistics; snapshot 2026-10-20) — **MEASURED SIGNAL ONLY; NOTHING HERE WAS LISTENED TO**

The agent that produced this research has no auditory capability. Everything below comes from signal measurement (50 ms RMS windows, band energies, spectral flux, spectrograms) and Whisper small.en ASR. Statements about music, sound effects, tone, accent, originality, licensing or software are `NOT_VERIFIED`. A human must listen before any audio decision is copied. Absence of a detected transient is `NOT_DETECTED`, not `ABSENT`.

## Measured facts (10 videos, 11.8 min)
| Measure | Value (median; range across videos) |
|---|---|
| Voiced fraction (windows within 14 dB of the 90th-percentile level) | 76 % (72-79 %) |
| Speaking rate over whole video | 195 words/min (163-214) |
| Phrase rate (phrases of >=4 words) | 3.6 words/s (p10 2.7, p90 4.5) |
| Pauses >= 0.25 s | 15.8 per minute (10.6-19.8); median length 0.30 s, longest 0.60 s (184 pauses) |
| Speech level (RMS) | about -20.6 dBFS (one video -15.8) |
| Pause noise floor | about -39.6 dBFS, i.e. ~20 dB below speech; `mT2hOLrCYSk` floor -34.7 dBFS |
| Pause-to-visual alignment | 55 % of cuts within 100 ms of an ASR word onset; in `Qof71Ef-3EU` 10 of 33 cuts coincide with the end of a pause, in `7bm7XYssqlU` 13 of 18 pauses end within 120 ms of a visual event |

## What the measurements do and do not show
- **Narration-driven pacing**: the picture is cut to the speech, not the speech to the picture. Cut-to-word offsets (median -80 ms) and caption-to-word offsets (+33 ms) show visuals lead or meet the voice.
- **Dense, short pauses**: ~16 pauses/minute of ~0.3 s suggest an edited, tightened voice track (`PLAUSIBLE_HYPOTHESIS`; could also be a fast reader).
- **Music/SFX**: no sustained tonal bed appears in the spectrograms of the two videos inspected (`Qof71Ef-3EU`; the signal floor in pauses is low); a music bed below the noise floor of the measurement cannot be excluded. Spectral flux at cut times (median 2.96) is not separable from speech onsets (random-time median 1.87 is inflated by speech). No distinct SFX category could be identified, so **no SFX cue recipe is given here**.
- The sponsor/brand sound identity, audio mastering and loudness targets are `UNKNOWN`.

## Instructions for an original production (design suggestions, not observations)
1. Record narration first; target ~3.5 words/s with deliberate 0.25-0.35 s pauses at sentence ends; trim breaths.
2. Place each hard cut within -150..+50 ms of the keyword onset, on the frame before if undecided (the sampled channel leads by ~80 ms).
3. Decide music and SFX by ear: keep the bed >=20 dB below speech, add short transients only on emphasis pops, never under a caption word. Validate with a phone speaker.
4. Run `scripts/forensic_features.py --asr` on your own export to check cut-to-word offsets before publishing.

## Gap
`GAP-006` (direct listening) remains `BLOCKED`. Owner action: listen to at least one banded-era and one full-bleed Short and record music presence, SFX types and loudness feel in `audio_listening_notes.md`.
