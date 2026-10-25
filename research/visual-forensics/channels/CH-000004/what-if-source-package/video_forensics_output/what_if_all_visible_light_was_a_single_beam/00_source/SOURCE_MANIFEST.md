# Source Manifest

- SOURCE VIDEO: `/Users/ghilmanislam360/Downloads/What if all visible light was a single beam.mp4`
- VIDEO_SLUG: `what_if_all_visible_light_was_a_single_beam`
- SIZE: 71,131,247 bytes
- SHA-256: `9a80deaf298eccb128f87ddf42dfbdef01804a9f86d4e5aaf576ec8e37127038`
- DURATION: video stream 123.933333s (3718 frames @ 30fps CFR); container 123.994558s (audio tail slightly longer)
- RESOLUTION: 720x1280, ASPECT RATIO: 9:16
- FPS: 30 (constant, `r_frame_rate=avg_frame_rate=30/1`)
- VIDEO CODEC: H.264 High profile, yuv420p, BT.709, avc1
- AUDIO CODEC: AAC-LC, 44100 Hz, stereo, ~180 kbps, 5340 frames, duration 123.994558s
- AUDIO PRESENT: YES
- AUDIO DECODE STATUS: SUCCESSFUL (extracted losslessly to `00_source/audio/audio_original.aac` and as mono PCM WAV `00_source/audio/audio.wav` for analysis; original video untouched)
- AUDIO CHANNELS: 2 (stereo, downmixed to mono for analysis only)
- AUDIO SAMPLE RATE: 44100 Hz
- PREVIOUS MUTED ANALYSIS DETECTED: NO — this is the first forensic pass for this VIDEO_SLUG (no prior `video_forensics_output/what_if_all_visible_light_was_a_single_beam/` directory existed before this session)
- REANALYSIS WITH AUDIO REQUIRED: N/A (first pass already performed with audio enabled from the start)
- REANALYSIS STATUS: N/A

## Speech transcription attempt

A local speech-to-text pass was attempted (`openai-whisper`, then Apple-Silicon `mlx-whisper`) so that exact narration words could be recorded. Both installs failed in this environment: system `pip` is broken by a macOS-version-parsing bug in its vendored `truststore` module (`ValueError: invalid literal for int() with base 10: ''` in `pip._vendor.truststore._macos`), and creating an isolated venv fails for the same underlying `ensurepip`/pip reason on both Python 3.12 and 3.14. No working transcription tool was available.

Per the governing spec (§3), semantic transcription is not a hard dependency. Audio structure was instead analyzed directly from the decoded waveform:
- `ffmpeg -af silencedetect=noise=-30dB:d=0.15` was run against the full mono WAV to find silence/pause boundaries (see `05_audio/AUDIO_MAP.md`).
- Exact spoken words are therefore **UNKNOWN** throughout; audio type (narration/music/silence) and its synchronization with visual events are labeled **OBSERVED** (measured silence timing) or **LIKELY** (inferred narration/music presence from continuous non-silent audio and topical match to on-screen captions), never fabricated as verbatim transcript.

## Inspection methodology
- Full video decoded once via ffmpeg `select='gt(scene,0.10)'` scene-change scoring to generate shot-cut candidates.
- Two 6x6 tiled contact sheets (4s sampling) built for a full-video overview.
- One source-resolution PNG saved per second (124 frames, `01_evidence/frames/f####.png`) as primary evidence.
- Dense (±0.2-0.4s, native 30fps) frame windows extracted and tiled around every scene-cut candidate and around all major motion/reveal sequences to pin exact boundaries and read on-screen text.
- Provenance labeling: OBSERVED (directly seen/measured), LIKELY (strong inference), POSSIBLE (plausible, unverified), UNKNOWN (not determinable from source).
