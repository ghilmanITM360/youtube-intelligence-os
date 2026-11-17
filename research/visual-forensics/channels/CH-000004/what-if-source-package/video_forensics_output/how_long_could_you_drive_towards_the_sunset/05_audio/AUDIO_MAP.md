# Audio Map — how_long_could_you_drive_towards_the_sunset

## Audio access check
- VIDEO STREAM PRESENT: YES
- AUDIO STREAM PRESENT: YES
- AUDIO DECODE SUCCESSFUL: YES
- Audio duration: 129.980544s, stereo, 44100 Hz, AAC-LC.
- Extracted derived copies (originals untouched): `00_source/audio/audio_original.aac`, `00_source/audio/audio.wav`.
- TRANSCRIPT: UNAVAILABLE — no local speech-to-text tool could be installed in this environment (`pip`/`ensurepip` fail on a vendored `truststore` macOS-version-parsing bug; see `00_source/SOURCE_MANIFEST.md` for the exact error). This is a tooling limitation, not an audio-quality or access problem.

## Method
Structural audio analysis was performed directly on the decoded waveform via `ffmpeg -af silencedetect=noise=-35dB:d=0.1`, since no transcript could be produced. This identifies near-silence gaps only; it cannot separate narration from music/SFX/ambience by itself. On-screen caption text (fully legible in the source frames) is used as the best available proxy for narration content and is transcribed verbatim per state in `02_analysis/TIMELINE.csv`.

## Measured silence gaps
| Timestamp | Duration | Nearest shot/state | Visual event it syncs with | Confidence |
|---|---|---|---|---|
| 25.062s-25.172s | 0.110s | S04 / F04.5→F04.6 boundary (~frame 602) | Falls right at the transition from the second "cracking" gag into the mountain-rolling-ball sequence. | LIKELY (a brief pause/breath plausibly punctuates this beat change; exact narration content unknown) |
| 128.228s-129.981s | 1.753s | S14 / F14.5 (final state, holds to end) | Audio fades out under the final held caption ("HERE WITH YOU.") as the video ends. | OBSERVED (measured fade-to-silence coincides with the last video frame and the container's tail) |

No other gaps ≥0.1s at -35dB were found; the track is otherwise continuous for the full 130s runtime.

## Narration / Music / SFX / Ambience / Silence assessment
| Type | Assessment | Confidence |
|---|---|---|
| NARRATION | LIKELY present continuously, closely paraphrased by the on-screen captions (location names, data callouts, closing dialogue) — cannot be isolated from music without a transcript or stem separation. | LIKELY |
| MUSIC | LIKELY present as an underlying bed for most/all of the runtime, given the "full-mix" waveform shape (no isolated music-only stretch was identified). | LIKELY |
| SFX | POSSIBLE — a comedic "BRWWAAK" sound effect is strongly implied by the on-screen lettering/sound-effect callout at approximately t=20-24s (S04, states F04.4-F04.5), but cannot be confirmed audible without a transcript. | POSSIBLE |
| AMBIENCE | UNKNOWN — no distinguishing evidence either way from waveform structure alone. | UNKNOWN |
| SILENCE | OBSERVED at the two measured gaps above; no other silence detected. | OBSERVED |

## Limitations
- Exact spoken words are UNKNOWN throughout; every `SCRIPT_OR_AUDIO_CUE` value in `TIMELINE.csv` is marked UNKNOWN, with on-screen caption text (where present) noted as the best available proxy.
- Narration/music/SFX cannot be separated from the single mixed stream without a transcript or audio source-separation tool, neither of which was available.
- If a working speech-to-text tool becomes available later, re-run it against `00_source/audio/audio.wav` and patch `SCRIPT_OR_AUDIO_CUE` in `TIMELINE.csv` plus the AUDIO SYNC lines in `03_capcut/CAPCUT_REBUILD.md` / `04_image_to_video/I2V_REBUILD.md`.
