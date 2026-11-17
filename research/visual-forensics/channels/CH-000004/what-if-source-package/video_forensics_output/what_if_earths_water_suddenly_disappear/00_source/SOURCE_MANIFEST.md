# Source Manifest — what_if_earths_water_suddenly_disappear

## Source file
- Path: `/Users/ghilmanislam360/Downloads/YTDown.com_YouTube_What-if-Earth-s-Water-Suddenly-Disappear_Media_4ZVtHknKuvg_001_1080p.mp4`
- Size: 6,088,562 bytes
- SHA-256: `cd785cf411d81ee611e9b4e757dbc5db2437104117b2c44a5d9d7bb4a2190123`
- VIDEO_SLUG: `what_if_earths_water_suddenly_disappear`

## Technical properties (OBSERVED via ffprobe)
- Resolution: 1920x1080 (16:9, landscape) — first video in this project's set to use landscape framing rather than 9:16 Shorts
- Video codec: H.264, yuv420p
- Frame rate: 24/1 constant
- Total frames (video stream, `-count_frames`): 4411
- Video stream duration: 183.791667s
- Container duration: 183.855601s
- Audio codec: AAC, 44100 Hz, stereo

## Audio
- Audio stream present: YES, decodes successfully
- Lossless extraction: `00_source/audio/audio_original.aac`
- Analysis extraction: `00_source/audio/audio.wav` (mono 16kHz PCM)
- Transcript: UNAVAILABLE — local `whisper`/`mlx-whisper` install fails in this environment (broken system `pip` / `truststore` macOS-version-parsing bug), the same known issue documented for every other video in this project. Not re-attempted; see `05_audio/AUDIO_MAP.md` for the `silencedetect`-based structural analysis used instead.
- On-screen text (Q-cards, diagram labels, captions, chemical formulas) is extensive throughout and used as a partial content proxy, though — unlike `weird_and_worrying_questions` — it does NOT cover full narration verbatim (this video has continuous explanatory narration describing diagrams whose content is only partially mirrored in on-screen labels).

## Structural finding: multi-shot production, XKCD "What If?" video-series style
Unlike `weird_and_worrying_questions` (a single locked shot), this video is a genuinely edited, multi-scene explainer in the recognizable "xkcd's what if?" video-series house style (hand-drawn black-ink stick-figure illustrations, the same illustration family used elsewhere in this project). Shot/scene boundaries were determined using `ffmpeg scdet` (threshold sweep 5–8), which found 17 strong composition-change candidates across the full runtime, corroborated by direct visual review of 2-second-interval overview frames and 4 targeted native-resolution zoom grids at ambiguous windows. This yields **18 shots (S01–S18)** covering the full 183.792s / 4411 frames.

OBSERVED scene-cut timestamps (ffmpeg scdet, threshold 5–8, used as shot boundaries S01/S02 through S17/S18):
8.291667, 10.291667, 17.375, 26.791667, 39.625, 58.75, 64.375, 69.208333, 78.333333, 107.458333, 114.333333, 136.791667, 143.583333, 155.208333, 166.75, 170.791667, 173.791667

One shot boundary (S18 start = video end) is trivial (natural end of file, not a detected cut).

Within-shot state boundaries were determined by 2-second-interval visual sampling (92 overview frames) and are labeled LIKELY unless independently corroborated by a scdet score or a `silencedetect` gap coinciding with the same timestamp (labeled OBSERVED in those cases — see `02_analysis/TIMELINE.csv` CONFIDENCE column).

## Evidence assets
- `01_evidence/CONTACT_SHEET_1.jpg` – `CONTACT_SHEET_4.jpg`: 92 overview frames (1 per 2s), 6x4 grids
- `01_evidence/frames/overview_001.jpg`–`overview_092.jpg`: source frames used for the contact sheets
- `01_evidence/cuts/`: 34 native-resolution before/after frame pairs at each scdet candidate timestamp
- `01_evidence/zoom_60_70s.jpg`, `zoom_78_96s.jpg`, `zoom_108_132s.jpg`, `zoom_134_156s.jpg`, `zoom_156_184s.jpg`: 5 targeted native-resolution grids used to resolve ambiguous transitions (dual-panel sink-time comparison, seaplane/jar-diagram fade, rain-drought-fire sequence, CO2/volcano chemistry sequence, billion-years epilogue+credits)
