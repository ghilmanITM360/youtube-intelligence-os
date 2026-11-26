#!/bin/zsh
# Full V15 rebuild, run from v15/:  zsh tools/build_v15.sh [--from-voice]
# --from-voice also re-edits the narration and re-transcribes it (needs whisper-cli); otherwise starts from the
# committed transcription in qa/asr/clean_words.json.
set -euo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
D=110.0417
if [[ "${1:-}" == "--from-voice" ]]; then
  $PY tools/prepare_voice.py
  ffmpeg -v error -y -i HAMZA_VOICEOVER_CLEAN.wav -ar 16000 -ac 1 qa/asr/clean16k.wav
  whisper-cli -m tools/whisper_models/ggml-small.en.bin -f qa/asr/clean16k.wav -ml 1 -sow -ojf -of qa/asr/clean_words --dtw small.en -l en -np
fi
$PY tools/align_v14.py                       # words, captions, SRT, picture time map
$PY tools/model.py > qa/model_check.txt       # physics checks
$PY tools/cloth_warp.py                      # rig deformation checks
$PY tools/v15.py --check                     # picture self-check (physics, continuity, warp)
$PY tools/v15.py --render --out SKYDIVER_SLOWDOWN_V15_picture.mp4 > qa/render_picture.log 2>&1
$PY tools/v15.py --render --out qa/caption_overlay.mov > qa/render_captions.log 2>&1
$PY tools/mix_v15.py                         # stems, publication mix, library review mix, cue sheet
ffmpeg -v error -y -i SKYDIVER_SLOWDOWN_V15_picture.mp4 -i audio/V15_mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -t $D -movflags +faststart SKYDIVER_SLOWDOWN_FINAL_V15.mp4
ffmpeg -v error -y -i SKYDIVER_SLOWDOWN_FINAL_V15.mp4 -i qa/caption_overlay.mov -filter_complex "[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -crf 17 -c:a copy -movflags +faststart SKYDIVER_SLOWDOWN_FINAL_V15_CAPTIONS.mp4
ffmpeg -v error -y -i SKYDIVER_SLOWDOWN_FINAL_V15_CAPTIONS.mp4 -i audio/V15_mix_library_review.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -t $D -movflags +faststart qa/review/review_library_mix.mp4
$PY tools/sync_map_v15.py > qa/sync_map.log
$PY tools/timeline_v15.py
rm -rf qa/_chunks_mp4 qa/_chunks_mov
echo "V15 build done"
