# Audio Map — what_if_the_moon_were_made_of_protons

## Access check
- Audio stream present: YES
- Audio decodable: YES (AAC-LC, 44.1kHz stereo)
- Transcript: UNAVAILABLE (no working local speech-to-text tool in this environment; see `00_source/SOURCE_MANIFEST.md`)

## Method
Full audio structure derived from `ffmpeg silencedetect=noise=-35dB:d=0.1` run against a mono 16kHz PCM extraction (`00_source/audio/audio.wav`). No transcription or narration/music/SFX separation was possible without a working STT/source-separation tool; the split below reflects only what is directly measurable (silence vs. non-silence) plus what is visually inferable from on-screen captions.

## Measured near-silence gaps
| Timestamp range | Duration | Likely significance (visual correlation) |
|---|---|---|
| 19.152s–19.264s | 0.112s | Falls within S03 (orbit/force comparison sequence, ~F03.1–F03.2) |
| 26.083s–26.193s | 0.110s | Falls almost exactly at the S03→S04 shot cut (measured cut at 26.208s) |
| 63.414s–63.603s | 0.189s | Falls almost exactly at the S06→S07 shot cut (measured cut at 63.5s) |
| 67.003s–67.253s | 0.250s | Falls within S08 (F08.1, the brief plain-black beat before 'DARK ENERGY' appears) |
| 74.250s–74.351s | 0.102s | Falls within S09 (F09.0, near the 'WHAT A BEAUTIFUL DAY' caption) |
| 80.622s–80.779s | 0.157s | Falls within S09 (F09.3, near the 'HO HUM' caption change) |
| 86.736s–88.143s | 1.407s | Trailing fade under the final growing-circle frames (F09.5–F09.6) through the end of the audio stream |

## Narration / music / SFX / ambience / silence
| Type | Coverage | Confidence |
|---|---|---|
| NARRATION | LIKELY present continuously except during the measured gaps above; exact words UNKNOWN (no transcript) — on-screen captions/labels are the best proxy for content and timing. | LIKELY |
| MUSIC | POSSIBLE — cannot be isolated from narration in a single undifferentiated mixed track without source separation. | POSSIBLE |
| SFX | UNKNOWN — no discrete SFX hits could be confirmed from waveform/silence analysis alone. | UNKNOWN |
| AMBIENCE | UNKNOWN | UNKNOWN |
| SILENCE | 7 measured gaps totaling ~2.23s, listed above; the final 1.407s gap is a trailing fade to the end of the clip. | OBSERVED |

## Limitations
- No narration/music/SFX separation is possible from this single mixed-down audio asset (`AU01`).
- Silence-gap timestamps are measured to millisecond precision by `silencedetect`, but their causal link to specific visual events (column above) is an inference (LIKELY), not a confirmed sync point.
