# Sound design spec (PRELIMINARY, n = 32 Shorts for audio statistics; snapshot 2026-10-20 evening) — **MEASURED SIGNAL ONLY; NOTHING HERE WAS LISTENED TO**

The agent that produced this research has no auditory capability. Everything below comes from signal measurement (50 ms RMS windows, band energies, spectral flux, spectrograms) and Whisper small.en ASR. Statements about music, sound effects, tone, accent, originality, licensing or software are `NOT_VERIFIED`. A human must listen before any audio decision is copied. Absence of a detected transient is `NOT_DETECTED`, not `ABSENT`.

## Measured facts (32 videos, 37.7 min; `scripts/aggregate_audio.py` -> `evidence/audio_aggregate.json`)
| Measure | Value (median; range across videos) |
|---|---|
| Voiced fraction (windows within 14 dB of the 90th-percentile level) | 76 % (72-81 %) |
| Speaking rate over whole video | 190 words/min (163-214) |
| Phrase rate (phrases of >=4 words) | 3.5 words/s (p10 2.8, p90 4.4; 581 phrases) |
| Pauses >= 0.25 s | 13.5 per minute (10.3-19.8); median length 0.30 s, longest 0.60 s (524 pauses) |
| Speech level (median RMS of voiced windows) | about -20.4 dBFS (-20.9 to -15.3) |
| Pause noise floor (median RMS inside pauses) | about -53.2 dBFS (-66.6 to -44.4), i.e. ~33 dB below speech; the n = 10 snapshot quoted -39.6 dBFS from an aggregation that was not recorded, so that figure is superseded and not comparable |
| Cut-to-word alignment | 54 % of hard cuts within 100 ms of an ASR word onset, 76 % lead the onset (median -73 ms, p10 -207, p90 +76, n = 606); in `Qof71Ef-3EU` 10 of 33 cuts coincide with the end of a pause, in `7bm7XYssqlU` 13 of 18 pauses end within 120 ms of a visual event |

## What the measurements do and do not show
- **Narration-driven pacing**: the picture is cut to the speech, not the speech to the picture. Cut-to-word offsets (median -73 ms) and caption-to-word offsets (+13 to +53 ms by video, 14 videos with a caption band) show visuals lead or meet the voice.
- **Dense, short pauses**: ~13.5 pauses/minute of ~0.3 s suggest an edited, tightened voice track (`PLAUSIBLE_HYPOTHESIS`; could also be a fast reader).
- **Music/SFX**: no sustained tonal bed appears in the spectrograms of the two videos inspected (`Qof71Ef-3EU`; the signal floor in pauses is low, now measured at about -53 dBFS across 32 videos); a music bed below the noise floor of the measurement cannot be excluded. Spectral flux at cut times (maximum within ±100 ms, median 3.28) is higher than at random times (1.89), but 54 % of cuts sit within 100 ms of a word onset, so the rise cannot be separated from speech onsets. No distinct SFX category could be identified, so **no SFX cue recipe is given here**.
- The sponsor/brand sound identity, audio mastering and loudness targets are `UNKNOWN`.

## Instructions for an original production (design suggestions, not observations)
1. Record narration first; target ~3.5 words/s with deliberate 0.25-0.35 s pauses at sentence ends; trim breaths.
2. Place each hard cut within -150..+50 ms of the keyword onset, on the frame before if undecided (the sampled channel leads by ~73 ms).
3. Decide music and SFX by ear: keep the bed >=20 dB below speech, add short transients only on emphasis pops, never under a caption word. Validate with a phone speaker.
4. Run `scripts/forensic_features.py --asr` on your own export to check cut-to-word offsets before publishing.

## Gap
`GAP-006` (direct listening) remains `BLOCKED`. Owner action: listen to at least one banded-era and one full-bleed Short and record music presence, SFX types and loudness feel in `audio_listening_notes.md`.
