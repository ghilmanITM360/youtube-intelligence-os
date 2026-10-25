# Audio Map — weird_and_worrying_questions

## Audio access check
- Audio stream present: YES
- Audio decodes successfully: YES
- Lossless extraction (`00_source/audio/audio_original.aac`): SUCCESSFUL
- Analysis extraction (`00_source/audio/audio.wav`, mono 16kHz PCM): SUCCESSFUL
- Transcript: UNAVAILABLE (local `whisper`/`mlx-whisper` install fails in this environment — broken system `pip` / `truststore` macOS-version-parsing bug, the same known issue as the other videos in this project)

## Method
Audio structure was mapped using `ffmpeg silencedetect` (`-35dB:d=0.1`) against `audio.wav`, since no transcription tool is available. Because every question and reaction line in this video is also displayed verbatim on-screen (Q-cards and captions, see `../02_analysis/TIMELINE.csv`), the on-screen text serves as a near-complete proxy for spoken narration content — unlike the other videos in this project, very little is actually UNKNOWN here.

## Measured near-silence gaps (4 total)
| TIMESTAMP | AUDIO TYPE | DESCRIPTION | VISUAL EVENT IT SYNCS WITH | CONFIDENCE |
|---|---|---|---|---|
| 34.480–34.582s (0.102s) | SILENCE | Brief near-silence gap | Falls just before the reactor meltdown burst (F01.20, ~34.0s) | LIKELY |
| 34.584–34.703s (0.119s) | SILENCE | Second brief gap immediately after the first | Falls within/just after F01.20, close to the plaque's appearance (F01.21, ~34.7s) | LIKELY |
| 45.468–45.978s (0.510s) | SILENCE | Longer pause, the most prominent gap in the video | Falls within the closing crying/puddle-growth state (F01.24) and its clear to blank (F01.25, ~45.0s) | LIKELY |
| 46.916–47.308s (0.391s) | SILENCE | Second longer pause near the very end | Falls within the closing "...KARL, IS EVERYTHING OK?" caption (F01.26, ~46–47s) | LIKELY |

## Narration / music / SFX / ambience / silence
| TYPE | DESCRIPTION | CONFIDENCE |
|---|---|---|
| NARRATION | Continuous spoken narration reading each Q-card's question text aloud, plus the aside/caption lines ("HOW MANY MIRRORS...", "...MAYBE", "FOR GOD'S SAKE...", "...KARL"); exact words UNKNOWN without transcript, but on-screen text is a reliable proxy for content. | LIKELY |
| MUSIC | Cannot be isolated from narration in the undifferentiated mix; presence/absence and specific track UNKNOWN. | UNKNOWN |
| SFX | Cannot be confirmed as a distinct layer at this analysis depth (e.g. a possible "whoosh" under the mug-throw A06, or an "explosion" sound under A15/A19, would be consistent with the visuals but are not verified). | POSSIBLE |
| AMBIENCE | None distinctly identified; the mix reads as narration-forward with minimal or no ambient bed. | UNKNOWN |
| SILENCE | 4 measured near-silence gaps totaling ~1.12s, concentrated in the video's final third (see table above); none exceed 0.51s, consistent with fast pacing throughout rather than deliberate dramatic pauses. | OBSERVED (gap timestamps); LIKELY (interpretation) |

## Limitations
No transcript exists; every `SCRIPT_OR_AUDIO_CUE` value in `TIMELINE.csv` is recorded as UNKNOWN for exact wording, though on-screen Q-card and caption text is fully transcribed and used as the primary content proxy throughout this project's analysis. Music/SFX/ambience presence and identity are not verifiable from silence-detection alone.
