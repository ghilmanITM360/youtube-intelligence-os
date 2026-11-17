#!/bin/sh
# Usage: prep_banded.sh <video_id>  (features exist). Writes bands.json (banded defaults), segments, renders lean sheets, prints events + ASR.
V=$1; EV=/Users/ghilmankhan/workprojects/yio-cf-editing-forensics-local-evidence
cd /Users/ghilmankhan/workprojects/yio-cf-editing-forensics/research/casually-finance-editing-forensics
echo '{"header":[0.20,0.30],"stage":[0.30,0.665],"caption":[0.665,0.80],"stage_thr":8,"gap":4,"auto_cuts":true,"caption_last_frame":99999,"auto_fill":true}' > videos/$V/auto/bands.json
python3 -E scripts/segment_events.py $V $EV
python3 -E scripts/event_sheets.py $V $EV --per-sheet 99 --cols 11 --cell-w 120 --max-long 6 --lean --classes HARD,ANIM --prefix ev | sed 's#.*/sheets/#sheet: #'
python3 -E - <<PY
import csv, json
v="$V"
print(json.load(open("videos/%s/auto/AUTO_SUMMARY.json"%v))["frames_decoded"], json.load(open("videos/%s/auto/AUTO_SUMMARY.json"%v))["fps"])
r=list(csv.DictReader(open("videos/%s/auto/STAGE_EVENTS_AUTO.csv"%v)))
print("EVENTS:", " ".join("%s:%s+%s%s"%(x["event_id"][2:],x["start_frame"],x["n_active_span"],x["auto_hint"][0]) for x in r if x["auto_hint"][0]!="S" or float(x["peak_changed_frac_of_stage"])>=0.008))
w=list(csv.DictReader(open("videos/%s/auto/asr_words.csv"%v)))
seg={}
for q in w: seg.setdefault(q["segment"],[]).append(q)
for s,ws in seg.items(): print("[%s-%s] %s"%(ws[0]["start_sec"],ws[-1]["end_sec"]," ".join(x["word"] for x in ws)))
PY
