#!/bin/bash
# V2 finishing: one global grade on the clean render + the V2 mix -> PREMIUM; then the caption pass -> PREMIUM_CAPTIONS.
set -e
cd "$(dirname "$0")/.."
D=renders/roughcut_v2
GRADE="eq=contrast=1.05:saturation=0.94:gamma=0.98,colorbalance=bs=0.03:bm=0.01:rh=0.02:gh=0.01,vignette=angle=PI/5.5,noise=alls=3:allf=t"
ffmpeg -v error -y -i $D/ROUGH_CUT_V2_clean.mp4 -i $D/final_mix_v2.wav -vf "$GRADE" -map 0:v -map 1:a \
  -c:v libx264 -crf 17 -preset medium -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 256k -ar 48000 -t 96.000 $D/ROUGH_CUT_V2_PREMIUM.mp4
~/.venvs/uepipe/bin/python tools/captions_v2.py burn $D/ROUGH_CUT_V2_PREMIUM.mp4 $D/ROUGH_CUT_V2_PREMIUM_CAPTIONS.mp4 A
for f in $D/ROUGH_CUT_V2_PREMIUM.mp4 $D/ROUGH_CUT_V2_PREMIUM_CAPTIONS.mp4; do ffprobe -v error -show_entries format=duration:stream=codec_name,width,height -of compact $f; done
