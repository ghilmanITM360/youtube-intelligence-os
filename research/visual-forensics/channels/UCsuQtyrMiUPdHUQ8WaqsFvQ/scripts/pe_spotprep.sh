#!/bin/bash
# Deterministic evidence for primary spot-check. Usage: pe_spotprep.sh <id> <sheet_no 2-digit>
WS=$HOME/YIOS-local-audits/primitive-education; VP=$HOME/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3; id=$1; V=$WS/videos/$id; cd $WS
$VP -I scripts/pe_native.py $V 3 | python3 -c "import sys,ast;[print(r['seg'],r['file'],r['crop_w'],r['crop_h']) for r in ast.literal_eval(sys.stdin.read())]"
$VP -I scripts/pe_stroke.py $V > /dev/null; python3 -I scripts/pe_enc_audit.py $V
segs=$(grep "SHEET_$2" $V/tables/sheet_index.csv | cut -d, -f3 | sort -u | tr '\n' '|' | sed 's/|$//')
grep -E "^($segs)," $V/review/rv1_$id/annotations.csv | cut -c1-200
python3 -I -c "
import csv;A=list(csv.DictReader(open('$V/review/rv1_$id/annotations.csv')))
print('FLAG',[a['seg'] for a in A if a['confidence']=='LOW' or 'UNRESOLVED' in a['description']]); print('D4',[s['seg'] for s in csv.DictReader(open('$V/tables/segments_v1.csv')) if 'D4' in s['detectors']])"
