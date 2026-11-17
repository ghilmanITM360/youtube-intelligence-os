#!/bin/bash
# segment + sheets + palette + asr check + brief for ingested videos. Usage: xk_prep.sh <reviewer_prefix> <id>...
WS=$HOME/YIOS-local-audits/xkcd-whatif; VPY=$HOME/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3
P=$1; shift
for id in "$@"; do
  V=$WS/videos/$id; [ -f "$V/INGEST_DONE" ] || { echo "not ingested $id"; continue; }
  [ -f "$V/tables/segments_v1.csv" ] || $VPY -I $WS/scripts/xk_segment.py "$V" > "$V/evidence/log_segment.txt" 2>&1 || { echo "segment FAIL $id"; continue; }
  [ -f "$V/tables/sheet_index.csv" ] || $VPY -I $WS/scripts/xk_sheets.py "$V" > "$V/evidence/log_sheets.txt" 2>&1
  [ -f "$V/tables/palette_measured.json" ] || $VPY -I $WS/scripts/xk_palette.py "$V" > /dev/null 2>&1
  python3 -I $WS/scripts/xk_asr_check.py "$V" > /dev/null
  n=$(ls "$V/frames/sheets" | wc -l | tr -d ' '); R=${P}_$id
  sed -e "s#VIDEO_DIR#$V#g" -e "s#VIDEO_ID#$id#g" -e "s#REVIEWER_ID#$R#g" -e "s#SHEET_COUNT#$n#g" $WS/scripts/reviewer_brief_template.md > "$V/review_brief_$R.md"
  mkdir -p "$V/review/$R"; echo "$id sheets=$n $(cat $V/evidence/log_sheets.txt)"
done
