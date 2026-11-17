# Audio Map — what_if_all_visible_light_was_a_single_beam

## Audio access check
- VIDEO STREAM PRESENT: YES
- AUDIO STREAM PRESENT: YES (AAC-LC, 44.1kHz, stereo, ~180kbps, 5340 frames, 123.994558s)
- AUDIO DECODE SUCCESSFUL: YES — extracted losslessly to `00_source/audio/audio_original.aac` (stream copy) and as mono PCM WAV `00_source/audio/audio.wav` (for analysis only); original source video was not modified.
- TRANSCRIPT: UNAVAILABLE. Local speech-to-text (`openai-whisper`, `mlx-whisper`) could not be installed in this environment — system `pip` fails with a macOS-version-parsing bug in its vendored `truststore` module, and this blocks both direct install and venv creation (`ensurepip` depends on the same broken pip). See `00_source/SOURCE_MANIFEST.md` for the exact error. Per governing spec §3/§16, this is not treated as a hard blocker; audio structure below is derived from direct waveform measurement instead of a transcript.

## Method
`ffmpeg -af silencedetect=noise=-30dB:d=0.15` was run against the full mono WAV to find every gap of near-silence ≥0.15s. Outside of the five gaps below, the track is continuously non-silent for its full 123.99s duration — consistent with continuous background music with narration on top (labeled MIXED), but the narration/music split and all spoken words are UNKNOWN without a transcript.

## Measured silence gaps (OBSERVED)

| # | RANGE | DURATION | SHOT_ID | STATE_ID | VISUAL EVENT AT THIS TIME | SYNC RELATIONSHIP | CONFIDENCE |
|---|---|---|---|---|---|---|---|
| 1 | 75.226s - 75.393s | 0.167s | S08 | F08.0 | Twilight ring is mid-wrap (roughly 3/4 closed) | brief pause occurs during a continuous visual motion, not at a cut | OBSERVED (timing); LIKELY (that this is a narration breath/beat rather than an edit artifact) |
| 2 | 95.778s - 96.079s | 0.301s | S11 | boundary of F11.0/F11.1 | Coincides closely with the simplified-diagram hold ending and the first starburst arrows beginning | pause occurs right at a visual motion's start | LIKELY |
| 3 | 109.181s - 109.345s | 0.164s | S13 | start of F13.0 | Moon has just begun deflecting away from the beam as a red comet | pause occurs right after a shot's opening beat | LIKELY |
| 4 | 114.036s - 114.285s | 0.248s | S13 | F13.1 | Comet is partway through its flight away from the beam | pause occurs mid-motion | LIKELY |
| 5 | 122.711s - 123.995s | 1.284s | S15 | F15.0 | Final outro tombstone card, held static | long fade/hold under the closing card to the end of the video | OBSERVED (this is the video's ending, audio and video both trail off together) |

## Narration / music / SFX / ambience (per governing spec categories)

| TYPE | ASSESSMENT |
|---|---|
| NARRATION | LIKELY present and continuous through most of the runtime (topical match between the near-constant audio and the near-constant stream of on-screen captions/labels strongly suggests a voiced narration track), but exact spoken words are UNKNOWN — no transcript could be produced. |
| MUSIC | LIKELY present under the narration for some or all of the runtime (audio is non-silent even during shots with no on-screen text, e.g. S08's ring wrap and S12/S13's chase), but cannot be isolated from narration without stem separation, which was not attempted. |
| SFX | UNKNOWN — no discrete SFX hits were reliably distinguishable from the mixed waveform without a spectrogram-level pass beyond this project's scope; do not fabricate specific sound-effect names. |
| AMBIENCE | UNKNOWN. |
| SILENCE | Five measured gaps, OBSERVED, see table above. |

## Limitations
- No isolated narration/music/SFX stems exist for this source; `AU01` in `ASSET_MANIFEST.csv` represents the undifferentiated full mix.
- Do not invent exact spoken words, a music track name, or a sound-effect library — none is verifiable from this source.
- The CapCut and I2V rebuilds (below) therefore sync visuals to the five measured silence points and to "continuous audio" elsewhere, not to specific words.
