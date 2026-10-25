# Source Manifest — weird_and_worrying_questions

VIDEO_SLUG: `weird_and_worrying_questions`
SOURCE PATH: `/Users/ghilmanislam360/Downloads/YTDown.com_Shorts_Weird-and-worrying-questions_Media_SLd4hnmeW_g_001_1080p.mp4`
SIZE: 13,478,240 bytes
SHA-256: `4ec6072844c4028960d1d4b505608a7126e95ff1fca21acdff80b8f514a2fdd1`

## Technical specification (OBSERVED via ffprobe)
- Container: MOV/MP4 (`mov,mp4,m4a,3gp,3g2,mj2`)
- Resolution: 1080x1920 (9:16 portrait)
- Video codec: H.264, `yuv420p`
- Frame rate: 24/1 constant (confirmed via `-count_frames`: exactly 1139 frames)
- Video stream duration: 47.458333s (1139 frames ÷ 24fps)
- Container duration: 47.508027s (audio runs ~0.05s longer than video — trailing tail)
- Audio codec: AAC-LC, 44.1kHz, stereo
- Audio: present, decoded successfully

## Inspection methodology
- Frame count cross-checked via `ffprobe -count_frames`: 1139 read frames, consistent with 24fps × 47.4583s.
- Scene-cut candidates detected via `ffmpeg` `scene` filter at thresholds 0.25 and 0.10 (see `01_evidence/`). Unlike the other videos in this project, visual inspection (contact sheet + 5 targeted zoom grids) confirmed this video uses a **single fixed camera composition for its entire runtime** — a stick-figure narrator at a desk — with all detected "scene" deltas corresponding to large *content* swaps (thought-bubble graphics appearing/clearing, a second character entering/exiting) rather than camera cuts. Per spec, this is modeled as **one shot (S01)** with 27 internal visual states; the 7 largest content-swap deltas (frames 213, 292, 507, 675, 833, 977, ~1134) are OBSERVED (scene-detector-confirmed at the exact frame); all other internal state boundaries are LIKELY (derived from 1-second-interval visual sampling only).
- No speech transcript could be produced: the local `whisper`/`mlx-whisper` install fails in this environment (broken system `pip` / `truststore` macOS-version-parsing bug), the same known issue as the other videos in this project. `ffmpeg silencedetect` (`-35dB:d=0.1`) was used instead to map audio structure (see `05_audio/AUDIO_MAP.md`). Unusually for this project, the on-screen Q-card and caption text gives a near-complete proxy for spoken narration content, since every question is displayed verbatim on-screen.

## Extracted evidence
- `00_source/audio/audio_original.aac` — lossless stream-copy of the original audio track.
- `00_source/audio/audio.wav` — mono 16kHz PCM, for waveform/silence analysis only.
- `01_evidence/CONTACT_SHEET_1.jpg` — 1s-interval overview (47 frames + 1 pad duplicate, 8 cols).
- `01_evidence/frames/f0001.png`–`f0047.png` — 1fps source-resolution PNG extractions.
- `01_evidence/zoom_00_07s.jpg`, `zoom_08_16s.jpg`, `zoom_16_25s.jpg`, `zoom_23_40s.jpg`, `zoom_39_47s.jpg` — targeted native-resolution grids used to pin exact state boundaries and read all on-screen text; not required for downstream reconstruction stages.
