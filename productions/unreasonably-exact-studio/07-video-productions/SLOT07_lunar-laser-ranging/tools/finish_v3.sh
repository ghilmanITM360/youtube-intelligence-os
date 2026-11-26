#!/bin/bash
# V3 finishing: the V2 global grade on the V3 clean render + the V3 mixes -> PREMIUM (private review, contains Small_Variables.mp3),
# a rights-clear master (no supplied music), then the caption pass. V1/V2 files are never touched.
set -e
cd "$(dirname "$0")/.."
D=renders/roughcut_v3
GRADE="eq=contrast=1.05:saturation=0.94:gamma=0.98,colorbalance=bs=0.03:bm=0.01:rh=0.02:gh=0.01,vignette=angle=PI/5.5,noise=alls=3:allf=t"
ffmpeg -v error -y -i $D/SLOT07_V3_clean.mp4 -vf "$GRADE" -c:v libx264 -crf 17 -preset medium -pix_fmt yuv420p -an -t 96.000 $D/_graded_video.mp4
mux() { ffmpeg -v error -y -i "$1" -i "$2" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -ar 48000 -movflags +faststart -t 96.000 "$3"; }
mux $D/_graded_video.mp4 $D/final_mix_v3_review_music.wav $D/SLOT07_V3_PREMIUM.mp4
~/.venvs/uepipe/bin/python tools/captions_v2.py burn $D/SLOT07_V3_PREMIUM.mp4 $D/_captions_video.mp4 A
mux $D/_captions_video.mp4 $D/final_mix_v3_review_music.wav $D/SLOT07_V3_PREMIUM_CAPTIONS.mp4
mux $D/_graded_video.mp4 $D/final_mix_v3_rights_clear.wav $D/SLOT07_V3_RIGHTS_CLEAR_MASTER_NO_MUSIC.mp4
mux $D/_captions_video.mp4 $D/final_mix_v3_rights_clear.wav $D/SLOT07_V3_RIGHTS_CLEAR_MASTER_NO_MUSIC_CAPTIONS.mp4
~/.venvs/uepipe/bin/python tools/captions_v2.py srt $D/SLOT07_V3.srt
rm -f $D/_graded_video.mp4 $D/_captions_video.mp4
for f in $D/SLOT07_V3_*.mp4; do ffprobe -v error -show_entries format=duration:stream=codec_name,width,height -of compact "$f"; done
