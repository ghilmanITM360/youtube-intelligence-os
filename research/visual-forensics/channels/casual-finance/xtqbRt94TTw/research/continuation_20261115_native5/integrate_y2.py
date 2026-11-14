import csv,json
from pathlib import Path
P=Path(__file__).parent;N4=P.parent/'Casual-Finance-Video006-native4-20261114'
rows=list(csv.DictReader(open(N4/'visual_event_ledger_v44.csv')));hdr=list(rows[0])
before={r['event_id']:dict(r) for r in rows}
n=0
for r in rows:
    if r['event_id']=='G007.02':
        n+=1
        r.update(verdict='NATIVE_ONSET_OF_S0015_SINGLE_REVIEW',
         description='Downturned (worried) eyes appear on orange percentage disc at 1141 (absent 1140); only the disc changes vs 1140. This is the exact onset of draft production state S0015, not a separate state; disc at 1141 equals disc at 1155 (mid-span 1142-1154 inferred static, not measured).',
         observed_change_first_frame='1141',observed_change_last_frame='1141',motion_object='percentage disc eyes',
         review_scope='BOUNDED_NATIVE_SINGLE_REVIEWER_NO_INDEPENDENT_QA;NO_GLOBAL_APPROVAL',
         bounds_role='ONSET_EVENT_OF_S0015;PROPOSED_S0015_BINDING_1141_1155_END_BOUNDED',
         native_vs_firstpass_conflict='Draft production S0015 [1142,1155] starts one frame late; observed onset 1141.',
         macro_review_ref=str(P/'G007_02_RULING.json'))
assert n==1
w=csv.DictWriter(open(P/'visual_event_ledger_v45.csv','w',newline=''),fieldnames=hdr);w.writeheader();w.writerows(rows)
q=json.load(open(N4/'CURRENT_NATIVE_QUEUE_v20.json'))
assert all(i['event_id']!='G007.02' for i in q['items'])
q['queue_version']=21;q['baseline']=str(P/'visual_event_ledger_v45.csv')
q['next_atomic_operation']='Verify next source-contiguous queue item EP0078 (2437-2469) with adjacent native context. G007.02 integrated in ledger v45; production spec S0015 interval [1141,1155] still to be applied in a production-draft revision.'
json.dump(q,open(P/'CURRENT_NATIVE_QUEUE_v21.json','w'),indent=1)
