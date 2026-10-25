# Source Manifest — how_long_could_you_drive_towards_the_sunset

## Reference file
- Path: `/Users/ghilmanislam360/Downloads/How long could you drive towards the sunset_.mp4`
- Size: 3,676,085 bytes
- SHA-256: `8af6a88e81339db037d0cd93bb6ea0f399cc6d6f2c77eb7ab228ff730e45052d`
- VIDEO_SLUG: `how_long_could_you_drive_towards_the_sunset`
- PREVIOUS MUTED ANALYSIS DETECTED: NO (first forensic pass for this slug).

## Technical properties (OBSERVED via ffprobe)
- Container: MOV/MP4 (isom), encoder tag `Lavf59.27.100`.
- Video stream: H.264 Main profile, yuv420p, 480x1280... actually 480x854, SAR 1:1, DAR 240:427 (≈9:16 vertical).
- Frame rate: 24/1 constant (r_frame_rate = avg_frame_rate = 24/1).
- Video duration: 129.875000s exactly (duration_ts 1595904 / timebase 1/12288).
- Total frames: 3117 (confirmed via `ffprobe -count_frames`; 129.875 × 24 = 3117.0 exactly — clean CFR, no drift).
- Container/format duration: 129.980544s (audio stream runs fractionally longer than video, consistent with an audio fade tail after the last video frame).
- Color: bt709 (range tv), progressive.
- Audio stream: AAC-LC, stereo, 44100 Hz, `mp4a.40.2`, language tag `eng`, duration 129.980544s.

## Audio access check (v8.0-COMPACT §11/§12 — audio present and used)
- VIDEO STREAM PRESENT: YES
- AUDIO STREAM PRESENT: YES
- AUDIO DECODE SUCCESSFUL: YES (ffmpeg decoded and extracted without error)
- Extracted derived audio (originals untouched):
  - `00_source/audio/audio_original.aac` — lossless stream copy of the original AAC track.
  - `00_source/audio/audio.wav` — mono 16kHz PCM, decode/analysis convenience copy.
- AUDIO STATUS: AVAILABLE (no limitation to declare for stream access).

## Speech transcription attempt
No local speech-to-text tool is available in this environment (same broken system-pip/`truststore` macOS-version-parsing issue documented for the prior slug in this project persists — `pip install --break-system-packages openai-whisper`/`mlx-whisper` fail with `ValueError: invalid literal for int() with base 10: ''` inside vendored `truststore`, and `python3 -m venv` + `ensurepip` also fail for the same reason, blocking a venv-based workaround). Per spec, semantic transcription is not a hard dependency; audio structure was instead analyzed directly via `ffmpeg -af silencedetect` against the real decoded waveform (see `05_audio/AUDIO_MAP.md`). All `SPOKEN_WORDS_OR_AUDIO_CUE` values in the timeline are therefore UNKNOWN as exact wording, though on-screen caption text (which likely mirrors spoken narration closely, given the format) is fully transcribed OBSERVED from frames.

## Inspection methodology
- Full-video overview: two tiled contact sheets (`01_evidence/CONTACT_SHEET_1.jpg` at 4s intervals, `CONTACT_SHEET_2.jpg` at 2s intervals).
- 130 source-resolution PNG frames extracted at 1fps (`01_evidence/frames/f0001.png`..`f0130.png`) — the primary evidence base for shot/state timing.
- `ffmpeg` `scene` filter at thresholds 0.25 and 0.10 for hard-cut candidate detection.
- `ffmpeg silencedetect` (noise=-35dB, d=0.1s) for audio structural analysis.
- Native-fps zoom grids (`01_evidence/zoom_*.jpg`) built around every 1-second interval to resolve caption text and confirm shot boundaries; not required for downstream stages.
- Shot/state boundaries are pinned to the nearest whole second from 1fps sampling; a few shot cuts were confirmed only by visual content comparison rather than the automated scene-cut filter (noted per-shot as LIKELY in `02_analysis/TIMELINE.csv`), since this video's fast-paced whiteboard-style redraws mostly occur on a static white/plain canvas that does not always trigger a high scene-change score even at a genuine hard cut.
