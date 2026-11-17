set -e
for id in mNLNb-Z4T0M GNaBxt_zIRA; do
 W=/Users/ghilmankhan/YIOS-local-audits/barely-evolved/2026-11-03-$id-deep-ct-scan; cd $W; F=$(ls "/Users/ghilmankhan/Downloads/videos in mp3/BarelyEvolved-MP4"/*$id*.mp4)
 cp /Users/ghilmankhan/YIOS-local-audits/barely-evolved/2026-11-02-uPQcyookL0Y-deep-ct-scan/v1_scripts/measure_all.py /Users/ghilmankhan/YIOS-local-audits/barely-evolved/2026-11-02-uPQcyookL0Y-deep-ct-scan/v1_scripts/scenedetect_run.py /Users/ghilmankhan/YIOS-local-audits/barely-evolved/2026-11-02-uPQcyookL0Y-deep-ct-scan/v1_scripts/be_asr_run.py scripts/
 shasum -a 256 "$F" > evidence/source_sha256.txt
 ffprobe -v error -show_format -show_streams -of json "$F" > evidence/ffprobe_full.json
 ffprobe -v error -select_streams v:0 -show_entries frame=pts_time,pkt_dts_time,pict_type -of csv=p=0 "$F" > evidence/video_frames_pts.csv
 nice /Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3 scripts/measure_all.py "$F" FULL_FRAME_MEASUREMENTS.csv > logs_measure.txt 2>&1
 nice /Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3 scripts/scenedetect_run.py "$F" > logs_scenedetect.txt 2>&1
 ffmpeg -v error -y -i "$F" -ac 1 -ar 16000 -c:a pcm_s16le asr/audio_16k_mono.wav
 nice /Users/ghilmankhan/YIOS-local-audits/barely-evolved/asr-venv/bin/python3 scripts/be_asr_run.py asr/audio_16k_mono.wav asr/asr_small_en small.en > asr/asr_run.log 2>&1
 echo "$(date -u +%FT%TZ) $id ingest done" >> /Users/ghilmankhan/YIOS-local-audits/barely-evolved/ingest_progress.txt
done
