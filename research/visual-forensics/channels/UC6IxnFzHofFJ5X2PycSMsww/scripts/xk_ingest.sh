#!/bin/bash
# Per-video ingest (no visual claims): sha256, ffprobe, frame PTS, full-frame measurements, scenedetect candidates, provisional ASR.
# Usage: xk_ingest.sh <video_id> [...]
set -u
WS=$HOME/YIOS-local-audits/xkcd-whatif; VPY=$HOME/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3
APY=$HOME/YIOS-local-audits/barely-evolved/asr-venv/bin/python3
SRCDIR="/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel"
for id in "$@"; do
  W=$WS/videos/$id; [ -f "$W/INGEST_DONE" ] && { echo "skip $id"; continue; }
  mkdir -p "$W"/{evidence,tables,asr,frames} && cd "$W" || exit 1
  F=$(ls "$SRCDIR"/*"[$id].mp4" 2>/dev/null | head -1); [ -z "$F" ] && { echo "NO SOURCE $id"; continue; }
  echo "$F" > evidence/source_path.txt
  shasum -a 256 "$F" > evidence/source_sha256.txt; stat -f %z "$F" > evidence/source_bytes.txt
  ffprobe -v error -show_format -show_streams -of json "$F" > evidence/ffprobe_full.json
  ffprobe -v error -select_streams v:0 -show_entries frame=best_effort_timestamp_time,pkt_duration_time,pict_type,key_frame -of csv=p=0 "$F" > evidence/video_frames_pts.csv
  nice "$VPY" -I "$WS/scripts/xk_measure.py" "$F" tables/FULL_FRAME_MEASUREMENTS.csv > evidence/log_measure.txt 2>&1
  nice "$VPY" -I "$WS/scripts/xk_scenedetect.py" "$F" tables/scenedetect_candidates.csv > evidence/log_scenedetect.txt 2>&1
  ffmpeg -v error -y -i "$F" -ac 1 -ar 16000 -c:a pcm_s16le asr/audio_16k_mono.wav
  ffmpeg -v error -i "$F" -af ebur128=peak=true -f null - 2> evidence/ebur128.txt
  nice "$APY" -I "$HOME/YIOS-local-audits/barely-evolved/2026-11-02-uPQcyookL0Y-deep-ct-scan/v1_scripts/be_asr_run.py" asr/audio_16k_mono.wav asr/asr_small_en small.en > asr/asr_run.log 2>&1
  rm -f asr/audio_16k_mono.wav
  date -u +%FT%TZ > INGEST_DONE; echo "$(date -u +%FT%TZ) $id ingest done" >> $WS/ingest_progress.txt
done
