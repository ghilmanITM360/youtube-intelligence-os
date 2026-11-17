# Audio Map — what_if_earths_water_suddenly_disappear

## Audio access check
- Audio stream present: YES
- Audio decodes successfully: YES
- Lossless extraction (`00_source/audio/audio_original.aac`): SUCCESSFUL
- Analysis extraction (`00_source/audio/audio.wav`, mono 16kHz PCM): SUCCESSFUL
- Transcript: UNAVAILABLE (local `whisper`/`mlx-whisper` install fails in this environment — broken system `pip` / `truststore` macOS-version-parsing bug, the same known issue as every other video in this project)

## Method
Audio structure was mapped using `ffmpeg silencedetect` (`-35dB:d=0.15`) against `audio.wav`, since no transcription tool is available. Unlike `weird_and_worrying_questions`, on-screen text here covers only diagram labels, captions, and chemical formulas — it does NOT mirror the full narration (the narrator explains each diagram verbally at greater length than the on-screen text shows), so significant narration content remains genuinely UNKNOWN in `TIMELINE.csv`.

## Measured near-silence gaps (selected; full list in generation log)
| TIMESTAMP | AUDIO TYPE | DESCRIPTION | VISUAL EVENT IT SYNCS WITH | CONFIDENCE |
|---|---|---|---|---|
| 9.480–10.351s (0.871s) | SILENCE | Gap right after the intro Q&A shot | Falls at the S01→S02 cut into the title card | LIKELY |
| 32.392–32.612s (0.220s) | SILENCE | Brief gap | Falls within F05.1/F05.2 (debris accumulating on the beach) | LIKELY |
| 58.745–58.921s (0.177s) | SILENCE | Brief gap | Coincides almost exactly with the S06→S07 gray-fade transition | OBSERVED (timing match) |
| 140.995–141.228s (0.234s) | SILENCE | Brief gap | Falls within S13 (host + tombstone), near the "WORSE? FOR WHO?" caption reveal | LIKELY |
| 154.859–155.125s (0.265s) | SILENCE | Brief gap | Falls almost exactly at the S14→S15 shot boundary (155.208s) | OBSERVED (timing match) |
| 172.273–184.0s (multiple gaps, ~9s of near-silence across 15+ short intervals) | SILENCE | Extensive fragmented silence through the remainder of the runtime | Falls within S17 (Hi! gag) and all of S18 (credits) | LIKELY |

Full gap list (22 intervals) is reproducible via `ffmpeg -i 00_source/audio/audio.wav -af silencedetect=noise=-35dB:d=0.15 -f null -`.

## Narration / music / SFX / ambience / silence
| TYPE | DESCRIPTION | CONFIDENCE |
|---|---|---|
| NARRATION | Continuous spoken explanation for nearly the entire runtime through S17, describing each diagram in more detail than the on-screen labels show; exact words UNKNOWN without a transcript. | LIKELY |
| MUSIC | Cannot be isolated from narration in the undifferentiated mix; presence/absence and specific track UNKNOWN. The dense, fragmented silence pattern from ~172–184s (S18 credits) is consistent with a low-level music bed continuing after narration ends, but this cannot be confirmed without source separation. | UNKNOWN |
| SFX | Not confirmed as a distinct layer at this analysis depth; no obvious isolated SFX hits detected via silence-gap analysis. | UNKNOWN |
| AMBIENCE | None distinctly identified. | UNKNOWN |
| SILENCE | 22 measured near-silence gaps; the two most evidentially useful (58.7s and 154.9s) coincide almost exactly with independently-detected `scdet` shot boundaries, corroborating those cuts. The credits card (S18) and the tail of S17 show markedly more/longer silence than the rest of the video, consistent with narration ending before the visual content does. | OBSERVED (gap timestamps); LIKELY (interpretation) |

## Limitations
No transcript exists; every `SCRIPT_OR_AUDIO_CUE` value in `TIMELINE.csv` is recorded as UNKNOWN for exact wording. Unlike `weird_and_worrying_questions`, on-screen text in this video covers only diagram labels and short captions, not full narration content, so the narration's actual explanatory detail (e.g., exactly what is said about each depth-scale panel or chemistry step) is not recoverable from the visual evidence alone. Music/SFX/ambience presence and identity are not verifiable from silence-detection alone.
