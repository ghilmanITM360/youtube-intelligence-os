#!/bin/zsh
# Bounded, read-only visual evidence extraction for ONE source video (ffmpeg/ffprobe only).
# Usage: pilot_extract.sh <source.mp4> <video_id> <out_dir>
# Outputs (all small, regenerable from the source):
#   source.sha256, ffprobe.json, frame_count.txt
#   scene_scores.txt   per-frame ffmpeg scene score for EVERY decoded frame (full temporal pass)
#   cuts_0.30.tsv      frames with scene score >= 0.30 (hard-cut candidates), pts seconds
#   sheet_1fps_NN.jpg  uniform coverage: 1 frame per second (t = k + 0.0 s), 6x5 tiles = 30 s per sheet
#   cuts_sheet_NN.jpg  first frame after each cut candidate, 6x5 tiles
#   audio_ebur128.txt, silence.txt   measured signal only (no listening)
# ponytail: 1 fps sheets can miss sub-second overlays; dense windows are extracted separately (dense_window.sh).
set -euo pipefail
src="$1"; vid="$2"; out="$3"
mkdir -p "$out"
shasum -a 256 "$src" | cut -d' ' -f1 > "$out/source.sha256"
ffprobe -v error -print_format json -show_format -show_streams "$src" > "$out/ffprobe.json"
ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of csv=p=0 "$src" > "$out/frame_count.txt"

# full pass: scene score for every frame (passthrough keeps native frame timing)
ffmpeg -hide_banner -nostats -i "$src" -an -fps_mode passthrough \
  -vf "select='gte(scene,0)',metadata=print:file=$out/scene_scores.txt" -f null - 2>/dev/null
awk '/pts_time/{split($3,a,":"); t=a[2]} /scene_score/{split($1,b,"="); if (b[2]+0>=0.30) printf "%s\t%s\n", t, b[2]}' \
  "$out/scene_scores.txt" > "$out/cuts_0.30.tsv"

# uniform 1 fps coverage sheets (tile k covers t = k s from sheet start)
ffmpeg -hide_banner -loglevel error -i "$src" -an \
  -vf "fps=1:round=down,scale=320:-2,tile=6x5:padding=4:color=white" -fps_mode vfr "$out/sheet_1fps_%02d.jpg"

# frames right after each cut candidate
sel=$(awk '{printf "%sgte(t,%s)*lt(t,%s+0.001)", (NR>1?"+":""), $1, $1}' "$out/cuts_0.30.tsv")
if [[ -n "$sel" ]]; then
  ffmpeg -hide_banner -loglevel error -i "$src" -an -vf "select='$sel',scale=320:-2,tile=6x5:padding=4:color=white" \
    -fps_mode vfr "$out/cuts_sheet_%02d.jpg"
fi

# audio: measured signal only
ffmpeg -hide_banner -nostats -i "$src" -vn -af ebur128 -f null - 2> "$out/audio_ebur128.txt" || true
ffmpeg -hide_banner -nostats -i "$src" -vn -af silencedetect=noise=-35dB:d=0.4 -f null - 2>&1 | grep silence_ > "$out/silence.txt" || true
echo "$vid done: $(wc -l < "$out/cuts_0.30.tsv") cut candidates, $(cat "$out/frame_count.txt") frames"
