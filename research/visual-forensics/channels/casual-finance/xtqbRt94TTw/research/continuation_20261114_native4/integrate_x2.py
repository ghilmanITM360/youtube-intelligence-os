import csv,json,hashlib
from pathlib import Path
P=Path(__file__).parent;N3=P.parent/'Casual-Finance-Video006-native3-20261106'
rows=list(csv.DictReader(open(N3/'visual_event_ledger_v43.csv')));hdr=list(rows[0])
rul=json.load(open(P/'SUB050_RULING.json'))
for r in rows:
    if r['event_id']=='SUB050':
        r.update(verdict='CORRECTED_NATIVE_SINGLE_REVIEW',
         description='Cursor moves continuously DOWNWARD over held article/presenter, visible 2420-2427 (accelerating; rest by 2427/2428 near lower article text). Candidate 2421-2427 is a sub-interval; motion starts no later than 2420 (2419 is a hard scene change, earlier not examined). No scroll, no presenter pose change.',
         observed_change_first_frame='2420',observed_change_last_frame='2427',motion_object='mouse cursor',
         review_scope='BOUNDED_NATIVE_SINGLE_REVIEWER_NO_INDEPENDENT_QA;NO_GLOBAL_APPROVAL',
         timing_precision='NATIVE_BOUNDED_MOTION_START_NOT_EXACT_END_2427_VISUAL_ESTIMATE',
         bounds_role='DECLARED_CURSOR_MOTION_WINDOW;CURSOR_POSITIONS_APPROXIMATE',
         native_vs_firstpass_conflict='First pass window 2421-2427 starts one frame late; motion visible from 2420.',
         macro_review_ref=str(P/'SUB050_RULING.json'),
         evidence=str(P/'sub050_2417_2431'))
w=csv.DictWriter(open(P/'visual_event_ledger_v44.csv','w',newline=''),fieldnames=hdr);w.writeheader();w.writerows(rows)
q=json.load(open(N3/'CURRENT_NATIVE_QUEUE_v19.json'))
q['items']=[i for i in q['items'] if i['event_id']!='SUB050'];q['count']=len(q['items']);q['queue_version']=20
q['baseline']=str(P/'visual_event_ledger_v44.csv')
q['next_atomic_operation']='Verify next source-contiguous queue item (first of items) with adjacent native context; production G007.02 frame 1141 explicit-interval classification remains open.'
json.dump(q,open(P/'CURRENT_NATIVE_QUEUE_v20.json','w'),indent=1)
