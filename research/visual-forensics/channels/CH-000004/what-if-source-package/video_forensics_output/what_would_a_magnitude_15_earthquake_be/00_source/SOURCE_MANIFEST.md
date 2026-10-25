# SOURCE MANIFEST

FILE: YTDown.com_YouTube_What-would-a-magnitude-15-earthquake-be-_Media_e3uk7jU3RHo_002_720p.mp4
VIDEO_SLUG: what_would_a_magnitude_15_earthquake_be
LOCATION: ~/Downloads/ (user-supplied, third-party downloader export of a YouTube video, id e3uk7jU3RHo)
SHA-256: b7b66d11af29d37aea735e94e5df5c97a589e060d44c009abc38661ac45aa1e7 — OBSERVED

## OBSERVED TECHNICAL SPECS (ffprobe)
- DURATION: 185.29s (video stream, 4447 frames / 24fps) / 185.34s (container) — OBSERVED
- RESOLUTION: 1280x720 — OBSERVED
- ASPECT RATIO: 16:9 (landscape) — OBSERVED
- FPS: 24 (constant) — OBSERVED
- FRAME COUNT: 4447 (ffprobe -count_frames) — OBSERVED
- VIDEO CODEC: H.264, yuv420p, bt709 — OBSERVED
- AUDIO: AAC-LC, stereo, 44.1kHz — OBSERVED
- CONTAINER: MP4 (isom), `handler_name: ISO Media file produced by Google Inc.` (consistent with a YouTube-sourced re-mux) — OBSERVED

## PRODUCTION IDENTIFICATION
Same "xkcd's what if?" video-series production as the other videos already reconstructed in this project (hand-drawn black-ink stick-figure style, red "xkcd's what if? THE VIDEO SERIES" bumper, identical end-credits card format: Randall Munroe / Henry Reich / Lizah van der Aart / Ever Salazar / Know Art Studios, "GET THE BOOKS: xkcd.com/books"). Subject: comparing real-world earthquake (Richter/moment-magnitude) scale values against a hypothetical magnitude-15 quake, ranging the scale from Magnitude 25 (Earth-destroying) down to Magnitude -15 (a mouse's footstep). — OBSERVED (visual style match), LIKELY (same creative team as prior project videos, based on identical credits block)

## SHOT-CUT DETECTION
`ffmpeg scdet` (score-based) found 16 hard-cut boundaries corroborated at score ≥5 (score range 5.4–50.5), consistent with genuine full-composition swaps confirmed visually against extracted frames — OBSERVED. A much larger set of lower-score spikes (2.0–4.9) was also measured; these correspond to in-shot content swaps (e.g. each successive magnitude value's illustration) rather than camera/shot cuts, and are recorded as visual-state transitions / motion events within their parent shot, not as separate shots — OBSERVED (scores measured), LIKELY (interpretation as intra-shot swap vs. shot cut, based on visual confirmation against extracted frames at 1fps and native-resolution spot checks).

## EVIDENCE CAPTURED
- `01_evidence/frames/f_001.jpg`…`f_093.jpg` — overview frames, 1 per 2s (0.5fps), 480px wide
- `01_evidence/dense/d_001.jpg`…`d_185.jpg` — dense native-content frames, 1 per 1s (1fps), 480px wide, used to pin exact per-second transitions
- `01_evidence/CONTACT_SHEET_1.jpg`–`CONTACT_SHEET_3.jpg` — tiled overview of the 0.5fps frames
- `01_evidence/DENSE_A_19-48.jpg` … `DENSE_H_0-18.jpg` — tiled 1fps inspection sheets covering the full runtime in overlapping windows
- `01_evidence/cuts/` — targeted native-resolution (1280x720) single-frame grabs used to read exact on-screen text (newspaper headline, ending vignette, sample magnitude cards)

## AUDIO — LIMITATION
No speech-to-text / audio-listening capability is available in this environment (broken local `whisper`/`mlx-whisper` install, the same standing issue as every other video in this project). Audio structure was mapped using `ffmpeg silencedetect`; narration content itself is UNKNOWN except where readable on-screen text substitutes. See `05_audio/AUDIO_MAP.md`.
