#!/bin/zsh
# Dense window: every Nth native frame between start and end seconds, tiled 6x5.
# Usage: dense_window.sh <source.mp4> <start_s> <dur_s> <fps> <out.jpg>
set -euo pipefail
ffmpeg -hide_banner -loglevel error -ss "$2" -t "$3" -i "$1" -an \
  -vf "fps=$4,scale=320:-2,tile=6x5:padding=4:color=white" -frames:v 1 -update 1 "$5"
