# SOURCE MANIFEST

FILE: YTDown.com_Shorts_How-high-could-the-magnitude-of-Earthqua_Media_wBLVmEZV2Oc_001_1080p.mp4
VIDEO_SLUG: earthquake-magnitude-shorts-wBLVmEZV2Oc
LOCATION: ~/Downloads/ (user-supplied, third-party downloader export of a YouTube Short, id wBLVmEZV2Oc)

## OBSERVED TECHNICAL SPECS (ffprobe)
- DURATION: 65.96s (video stream) / 66.01s (audio stream) — OBSERVED
- RESOLUTION: 1080x1920 — OBSERVED
- ASPECT RATIO: 9:16 (vertical/Shorts) — OBSERVED
- FPS: 24 (constant) — OBSERVED
- FRAME COUNT: 1583 — OBSERVED
- VIDEO CODEC: H.264 High Profile, yuv420p, bt709 — OBSERVED
- AUDIO: AAC-LC, stereo, 44.1kHz, ~128kbps — OBSERVED
- CONTAINER: MP4 (isom), encoder tag `Lavf62.12.100` (re-mux/re-encode signature, consistent with a downloader tool re-wrapping the original YouTube stream) — OBSERVED
- SCENE-CUT DETECTION: ffmpeg histogram scene filter found 0 cuts even at a very low threshold (0.08) — OBSERVED. Interpreted as: no traditional camera/hard-cut boundaries exist; the entire video is one continuous static-canvas composition with layered 2D elements being added/removed/replaced on top (see TIMELINE.csv). Treated as a single shot, S01.

## EVIDENCE CAPTURED
- `01_evidence/CONTACT_SHEET.jpg` — full-video overview, 2fps, 11x12 grid (132 frames)
- `01_evidence/SEG_A_0-19s.jpg`, `SEG_B_20-44s.jpg`, `SEG_C_45-65s.jpg` — 2fps zoomed segment sheets used to locate transition boundaries
- `01_evidence/GROUP1_intro.jpg`, `GROUP2_mid.jpg`, `GROUP3_finale.jpg` — full-resolution stills at key timestamps, used to read on-screen text exactly
- `01_evidence/frames/f_001.jpg`…`f_132.jpg` — individual 270x480 frames at 2fps across the full duration
- `01_evidence/hires/t_*.jpg` — full-resolution (1080x1920) single frames at 14 key timestamps

## AUDIO — LIMITATION
No speech-to-text / audio-listening capability was available in this environment (no local ASR tool, no way to play audio). The AAC track's presence and format are OBSERVED; its actual narration/music/SFX content is UNKNOWN except where it can be inferred from on-screen text. See `05_audio/AUDIO_MAP.md`.
