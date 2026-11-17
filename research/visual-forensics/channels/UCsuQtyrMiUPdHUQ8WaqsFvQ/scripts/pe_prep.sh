#!/bin/bash
# segment + sheets + strips + palette + brief. Usage: pe_prep.sh <id>...
WS=$HOME/YIOS-local-audits/primitive-education; VPY=$HOME/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3
for id in "$@"; do
  V=$WS/videos/$id; [ -f "$V/INGEST_DONE" ] || { echo "not ingested $id"; continue; }
  [ -f "$V/tables/segments_v1.csv" ] || $VPY -I $WS/scripts/pe_segment.py "$V" > "$V/evidence/log_segment.txt" 2>&1 || { echo "segment FAIL $id"; continue; }
  [ -f "$V/tables/sheet_index.csv" ] || $VPY -I $WS/scripts/pe_sheets.py "$V" > "$V/evidence/log_sheets.txt" 2>&1
  [ -f "$V/tables/strip_frames.csv" ] || $VPY -I $WS/scripts/pe_strip.py "$V" > "$V/evidence/log_strips.txt" 2>&1
  [ -f "$V/tables/palette_measured.json" ] || $VPY -I $WS/scripts/pe_palette.py "$V" > /dev/null 2>&1
  n=$(ls "$V/frames/sheets" | wc -l | tr -d ' '); ns=$(ls "$V/frames/strips" 2>/dev/null | wc -l | tr -d ' '); R=rv1_$id
  sed -e "s#VIDEO_DIR#$V#g" -e "s#VIDEO_ID#$id#g" -e "s#REVIEWER_ID#$R#g" -e "s#SHEET_COUNT#$n#g" -e "s#STRIP_COUNT#$ns#g" $WS/scripts/reviewer_brief_template.md > "$V/review_brief_$R.md"
  mkdir -p "$V/review/$R"; echo "$id sheets=$n strips=$ns $(cat $V/evidence/log_sheets.txt)"
done
