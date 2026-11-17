#!/bin/sh
# Usage: prep_full.sh <video_id>   (features must already exist). Segments, renders lean event sheets, prints ASR and SMALL>=0.8% events.
V=$1; EV=/Users/ghilmankhan/workprojects/yio-cf-editing-forensics-local-evidence
cd /Users/ghilmankhan/workprojects/yio-cf-editing-forensics/research/casually-finance-editing-forensics
python3 -E scripts/segment_full.py $V $EV
python3 -E scripts/event_sheets.py $V $EV --classes CUT,BIG,ANI --per-sheet 77 --cols 11 --cell-w 128 --max-long 7 --lean --prefix ev | sed 's#.*/sheets/#sheet: #'
python3 -E - <<PY
import csv
v="$V"
r=list(csv.DictReader(open("videos/%s/auto/STAGE_EVENTS_AUTO.csv"%v)))
print("EVENTS:", " ".join("%s:%s+%s%s%s"%(x["event_id"][2:],x["start_frame"],x["n_active_span"],x["auto_hint"][0],x["auto_hint"][1] if x["auto_hint"][0]=="B" else "") for x in r if x["auto_hint"]!="SMALL" or float(x["peak_changed_frac_of_stage"])>=0.008))
w=list(csv.DictReader(open("videos/%s/auto/asr_words.csv"%v)))
seg={}
for q in w: seg.setdefault(q["segment"],[]).append(q)
for s,ws in seg.items(): print("[%s-%s] %s"%(ws[0]["start_sec"],ws[-1]["end_sec"]," ".join(x["word"] for x in ws)))
PY
