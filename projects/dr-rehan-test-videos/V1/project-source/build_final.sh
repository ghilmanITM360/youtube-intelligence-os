#!/bin/sh
# Render -> broadcast-range yuv420p -> remux the ORIGINAL narration (sample-exact sync).
# Remotion's own AAC adds 2048 samples (42.7 ms) of priming delay, so its audio is discarded.
set -e
cd "$(dirname "$0")"
SRC_MP3="${1:-public/narration.mp3}"
npx remotion render CalfPain out/render_raw.mp4 --codec=h264 --crf=18 --concurrency=4 --log=error
ffmpeg -v error -y -i out/render_raw.mp4 -an -vf "scale=in_range=full:out_range=tv,format=yuv420p" \
  -c:v libx264 -preset slow -crf 18 -profile:v high -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  out/video_yuv420p.mp4
ffmpeg -v error -y -i out/video_yuv420p.mp4 -i "$SRC_MP3" -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -ar 48000 \
  -movflags +faststart ../Calf_Pain_PAD_FINAL.mp4
echo "built ../Calf_Pain_PAD_FINAL.mp4"
