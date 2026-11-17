#!/bin/bash
# Per-video ingest, no visual claims: sha256 check, ffprobe, frame PTS, measurements, scenedetect candidates, provisional ASR. Usage: pe_ingest.sh <video_id>
set -u
WS=$HOME/YIOS-local-audits/primitive-education; VPY=$HOME/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3
APY=$HOME/YIOS-local-audits/barely-evolved/asr-venv/bin/python3
SRCDIR="/Users/ghilmankhan/Downloads/videos in mp3/PrimitiveEducation-MP4"
id=$1; W=$WS/videos/$id; [ -f "$W/INGEST_DONE" ] && { echo "skip $id"; exit 0; }
mkdir -p "$W"/{evidence,tables,asr,frames} && cd "$W" || exit 1
F=$(ls "$SRCDIR"/*"[$id].mp4" 2>/dev/null | head -1); [ -z "$F" ] && { echo "NO SOURCE $id"; exit 1; }
echo "$F" > evidence/source_path.txt
shasum -a 256 "$F" > evidence/source_sha256.txt; stat -f %z "$F" > evidence/source_bytes.txt
ffprobe -v error -show_format -show_streams -of json "$F" > evidence/ffprobe_full.json
ffprobe -v error -select_streams v:0 -show_entries frame=best_effort_timestamp_time,pkt_duration_time,pict_type,key_frame -of csv=p=0 "$F" > evidence/video_frames_pts.csv
nice "$VPY" -I "$WS/scripts/pe_measure.py" "$F" tables/FULL_FRAME_MEASUREMENTS.csv > evidence/log_measure.txt 2>&1
nice "$VPY" -I "$WS/scripts/pe_scenedetect.py" "$F" tables/scenedetect_candidates.csv > evidence/log_scenedetect.txt 2>&1
ffmpeg -nostdin -v error -y -i "$F" -ac 1 -ar 16000 -c:a pcm_s16le asr/audio_16k_mono.wav
ffmpeg -nostdin -i "$F" -af ebur128=peak=true -f null - > evidence/ebur128.txt 2>&1
nice "$APY" -I "$WS/scripts/pe_asr_run.py" asr/audio_16k_mono.wav asr/asr_small_en small.en > asr/asr_run.log 2>&1
rm -f asr/audio_16k_mono.wav
date -u +%FT%TZ > INGEST_DONE; echo "$(date -u +%FT%TZ) $id ingest done" >> $WS/ingest_progress.txt
