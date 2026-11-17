# Source Manifest

**File:** `YTDown.com_Shorts_What-would-the-world-s-largest-cities-be_Media_GgEGcxJRDik_001_1080p.mp4`
**Slug:** `worlds-largest-cities-what-if`
**Size:** 12,351,567 bytes (~11.8 MB)

## Container / Streams (OBSERVED, ffprobe)
| Property | Value |
|---|---|
| Format | MP4 (isom, Lavf62.3.100 muxer — re-encoded/re-muxed, not a raw platform export) |
| Duration | 83.333 s (video), 83.406 s (audio) |
| Resolution | 1080x1920 (9:16 vertical) |
| SAR/DAR | 1:1 / 9:16 |
| Video codec | H.264 High Profile, yuv420p, level 4.0 |
| Frame rate | 24 fps (constant), 2000 frames total |
| Video bitrate | ~1.05 Mbps |
| Audio codec | AAC-LC, 44.1 kHz, stereo |
| Audio bitrate | ~128 kbps |
| Color | bt709, tv range |

## Evidence extracted
- `01_evidence/CONTACT_SHEET.jpg` — 7x12 tile, 1 fps overview.
- `01_evidence/frames/` — 23 full-resolution frames at forensically chosen timestamps (shot boundaries + holds).
- `05_audio/audio_extract.mp3` — isolated audio track.
- `05_audio/silence_raw.log` — silencedetect output (noise=-30dB, d=0.3s).

## Known limitations (declared up front, see also MASTER_REPORT)
- No local speech-to-text engine is available in this environment (checked: `whisper`, `whisper-cli`, `whisper.cpp`, `openai-whisper` — none installed). Narration/voiceover **wording is UNKNOWN** — only silence/volume envelope evidence was used. Do not treat any spoken line in this package as verified; none is transcribed.
- Original authoring tool (e.g. the specific "rotated-earth" map generator, whiteboard-doodle template, sticker pack) is UNKNOWN. Only the observable output is reconstructed.
