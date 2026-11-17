# Source Manifest — what_if_the_moon_were_made_of_protons

## Reference file
- Path: `/Users/ghilmanislam360/Downloads/YTDown.com_Shorts_What-if-the-Moon-were-made-of-Protons_Media_mEUqVgGf4e0_002_720p.mp4`
- Size: 4,265,306 bytes
- SHA-256: `23090b2969f34a5f0fd6903addab54267ae82884252835810576fe7c7a0c71cb`
- VIDEO_SLUG: `what_if_the_moon_were_made_of_protons`

## Technical properties (ffprobe)
- Container: MP4 (`mov,mp4,m4a,3gp,3g2,mj2`)
- Resolution: 720x1280 (9:16 portrait)
- Video codec: H.264, profile Main, pix_fmt yuv420p
- Frame rate: 24 fps constant (r_frame_rate = avg_frame_rate = 24/1)
- Video stream duration: 88.083333s
- Total frame count: 2114 (confirmed via `-count_frames`; 88.083333 × 24 = 2114.0 exactly)
- Container/format duration: 88.142948s
- Audio codec: AAC-LC, 44.1kHz, stereo, present and decodable
- Audio stream duration: 88.142948s (audio runs marginally longer than video — trailing fade, consistent with the measured silence gap below)

## Audio transcription status
No working local speech-to-text tool is available in this environment (same broken system pip / `truststore` macOS-version-parsing issue documented for the other videos in this project: `whisper` and `mlx-whisper` are not importable/installed, and no working install path was found). `SCRIPT_OR_AUDIO_CUE` values in `TIMELINE.csv` are therefore UNKNOWN as exact spoken wording; on-screen caption/label text (fully readable in the source) is used as the best available proxy throughout.

Audio structure was instead derived directly from the waveform via `ffmpeg silencedetect=noise=-35dB:d=0.1` on a mono 16kHz PCM extraction. See `05_audio/AUDIO_MAP.md` for the measured gaps.

## Inspection methodology
- Extracted 88 source-resolution frames at 1fps (`01_evidence/frames/f0001.png`–`f0088.png`) covering the full runtime.
- Built two overview contact sheets (2s-interval and 1s-interval) plus 8 targeted native-resolution zoom grids over the video's more content-dense or ambiguous regions (`01_evidence/zoom_*.jpg`) to pin shot/state boundaries and read on-screen text.
- Confirmed shot-cut candidates via `ffmpeg` scene-detection at two thresholds (`scene>0.25` and `scene>0.10`); all 8 shot boundaries used in `TIMELINE.csv` were flagged by the detector at one of these thresholds and are therefore OBSERVED at the exact frame. All internal visual-STATE boundaries within a shot (new graphics/text/motion appearing without a hard cut) were determined by 1-second-interval visual sampling only, not exhaustive frame-by-frame confirmation, and are labeled LIKELY for their exact IN/OUT frame in `TIMELINE.csv` (the content and ordering itself is directly observed).

## Raw evidence preservation
- Original reference video: untouched.
- `00_source/audio/audio_original.aac` — lossless stream-copy of the source audio track.
- `00_source/audio/audio.wav` — mono 16kHz PCM extraction, used only for silence-detection analysis.
