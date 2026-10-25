# Audio Map — what_would_a_magnitude_15_earthquake_be

## Audio access check
- Audio stream present: YES
- Audio decodes successfully: YES
- Lossless extraction (`00_source/audio/audio_original.aac`): SUCCESSFUL
- Analysis extraction (`00_source/audio/audio.wav`, mono 16kHz PCM): SUCCESSFUL
- Transcript: UNAVAILABLE (local `whisper`/`mlx-whisper` install fails in this environment — broken system `pip` / `truststore` macOS-version-parsing bug, the same standing issue as every other video in this project)

## Method
Audio structure was mapped using `ffmpeg silencedetect` (`-35dB:d=0.15`) against `audio.wav`, since no transcription tool is available. On-screen text in this video (headlines, newspaper, LIVE-TV captions) covers only labels/captions and does not mirror the full narration, so the narrator's actual explanatory content for each magnitude value remains genuinely UNKNOWN in `TIMELINE.csv`.

## Measured near-silence gaps (26 intervals total; selected below for their correlation with visual cuts)
| TIMESTAMP | AUDIO TYPE | DESCRIPTION | VISUAL EVENT IT SYNCS WITH | CONFIDENCE |
|---|---|---|---|---|
| 0.000–0.383s | SILENCE | Video open, pre-narration | Start of S01 (caption fade-in) | OBSERVED |
| 18.727–18.967s (0.240s) | SILENCE | Brief gap | Falls almost exactly at the S02→S03 cut (18.917s, title card → seismograph) | OBSERVED (timing match) |
| 61.439–61.598s / 65.226–65.437s | SILENCE | Two brief gaps | Fall within S06 (46.25–66.667s), near the Magnitude 11→15 globe-cracking progression | LIKELY |
| 84.641–85.067s (0.426s) | SILENCE | Brief gap | Falls within S10 (Magnitude 24 sun sequence), close to the F10.0→F10.1 texture-morph boundary (~85s) | LIKELY |
| 106.888–107.234s / 108.608–108.862s / 111.051–111.287s | SILENCE | Three gaps in quick succession | Fall within S12 (97.083–125.958s), in the host-figure / thought-bubble region | LIKELY |
| 125.601–125.967s (0.366s) | SILENCE | Brief gap | Falls almost exactly at the S12→S13 cut (125.958s, thought-bubble demo → truck impact) | OBSERVED (timing match) |
| 144.518–148.125s (two gaps) | SILENCE | Two brief gaps | Fall within S14, near the Magnitude -4→-5 boundary (144.75s, dog → computer-click) | LIKELY |
| 158.184–158.401s (0.217s) | SILENCE | Brief gap | Falls almost exactly at the Magnitude -7→-8 state boundary (158.4s, feather → hourglass) | OBSERVED (timing match) |
| 173.789–185.342s (15+ short gaps, ~9s of near-silence total) | SILENCE | Extensive fragmented silence through the remainder of the runtime | Falls within S15 (black wipe + ending vignette) and all of S16 (credits) | LIKELY |

Full gap list (26 intervals) is reproducible via `ffmpeg -i 00_source/audio/audio.wav -af silencedetect=noise=-35dB:d=0.15 -f null -`.

## Narration / music / SFX / ambience / silence
| TYPE | DESCRIPTION | CONFIDENCE |
|---|---|---|
| NARRATION | Continuous spoken explanation runs through nearly the entire runtime (S01–S15), describing each magnitude value in more detail than the on-screen "MAGNITUDE ##" labels alone convey; exact words UNKNOWN without a transcript. | LIKELY |
| MUSIC | Cannot be isolated from narration in the undifferentiated mix; presence/absence and specific track UNKNOWN. | UNKNOWN |
| SFX | Onomatopoeia is rendered as on-screen TEXT (WHUMP, CRASH, PLINK, CLICK, KERTHUMP) rather than confirmed as a distinct audible sound layer; whether these are also voiced/sounded in the mix is UNKNOWN without a transcript or stem separation. | UNKNOWN |
| AMBIENCE | None distinctly identified. | UNKNOWN |
| SILENCE | 26 measured near-silence gaps; three (18.9s, 125.6–126.0s, 158.2s) coincide almost exactly with independently-detected shot/state boundaries, corroborating those cuts. The final ~11 seconds (173.8–185.3s, covering the ending vignette and credits) show markedly more/longer silence than the rest of the video, consistent with narration ending before the visual content does — the same pattern observed in other videos in this project. | OBSERVED (gap timestamps); LIKELY (interpretation) |

## Limitations
No transcript exists; every `SCRIPT_OR_AUDIO_CUE` value in `TIMELINE.csv` is recorded as UNKNOWN. On-screen text in this video covers only headlines, captions, and gag-specific props (newspaper, phone alert, LIVE-TV box) — it does not substitute for the narrator's actual explanation of each magnitude value, so that content is not recoverable from visual evidence alone. Music/SFX/ambience presence and identity are not verifiable from silence-detection alone.
