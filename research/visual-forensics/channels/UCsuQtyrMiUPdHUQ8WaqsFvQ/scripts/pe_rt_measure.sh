#!/bin/bash
# Measure a reconstruction render with the SAME source pipeline. Usage: pe_rt_measure.sh <rt_attempt_dir> (contains render.mp4)
WS=$HOME/YIOS-local-audits/primitive-education; VPY=$HOME/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3
R=$(cd "$1" && pwd); F=$R/render.mp4; mkdir -p $R/evidence $R/tables
echo "$F" > $R/evidence/source_path.txt; shasum -a 256 "$F" > $R/evidence/render_sha256.txt
ffprobe -v error -show_format -show_streams -of json "$F" > $R/evidence/ffprobe_full.json
$VPY -I $WS/scripts/pe_measure.py "$F" $R/tables/FULL_FRAME_MEASUREMENTS.csv > $R/evidence/log_measure.txt 2>&1
$VPY -I $WS/scripts/pe_scenedetect.py "$F" $R/tables/scenedetect_candidates.csv > $R/evidence/log_scenedetect.txt 2>&1
$VPY -I $WS/scripts/pe_segment.py $R > $R/evidence/log_segment.txt 2>&1
$VPY -I $WS/scripts/pe_palette.py $R > /dev/null 2>&1
$VPY -I $WS/scripts/pe_sheets.py $R > $R/evidence/log_sheets.txt 2>&1
$VPY -I $WS/scripts/pe_native.py $R 1 > /dev/null 2>&1; $VPY -I $WS/scripts/pe_stroke.py $R > /dev/null 2>&1
$VPY -I $WS/scripts/pe_rt_eval.py $R
