import csv,json
from pathlib import Path
P=Path(__file__).parent;N6=P.parent/'Casual-Finance-Video006-native6-20261115'
rows=list(csv.DictReader(open(N6/'visual_event_ledger_v46.csv')));hdr=list(rows[0]);n=0
for r in rows:
    if r['event_id']=='EP0079':
        n+=1
        r.update(verdict='CONFIRMED_NATIVE_SINGLE_REVIEW',
         description="Native: before 2519 only the thin red stroke changes (<=195 px>60, y240-247). Author card (portrait, Yelena Shulyatyeva CFA, 'Senior US Economist', 'Read Bio') exit onset EXACT 2519; card slides off right edge 2519-2533 (bbox reaches x1919 from 2525); last card change 2533; from 2534 only stroke pixels change again. The red stroke above the headline is a SEPARATE track already drawing right-to-left before 2510 and continuing past 2545 (reaches x914 at 2541, turns downward by 2543); its own bounds are not measured here and no ledger event owns it in 2470-2586.",
         observed_change_first_frame='2519',observed_change_last_frame='2533',motion_object='Author card (exit right); red stroke separate track',
         review_scope='BOUNDED_NATIVE_SINGLE_REVIEWER_NO_INDEPENDENT_QA;NO_GLOBAL_APPROVAL',
         timing_precision='NATIVE_EXACT_ONSET_2519_LAST_CHANGE_2533_CARD_ONLY',
         bounds_role='NATIVE_VERIFIED_WINDOW_EQUALS_CANDIDATE_WINDOW',
         macro_review_ref=str(P/'EP0079_RULING.json'))
assert n==1
w=csv.DictWriter(open(P/'visual_event_ledger_v47.csv','w',newline=''),fieldnames=hdr);w.writeheader();w.writerows(rows)
q0=json.load(open(N6/'CURRENT_NATIVE_QUEUE_v22.json'));ids=[i['event_id'] for i in q0['items']];k=ids.index('EP0079')
q=dict(q0);q['items']=[i for i in q0['items'] if i['event_id']!='EP0079'];assert len(q['items'])==len(ids)-1
nxt=q['items'][k]
q.update(queue_version=23,count=len(q['items']),baseline=str(P/'visual_event_ledger_v47.csv'),
 next_atomic_operation=f"Verify next queue item {nxt['event_id']} ({nxt['source_start_frame']}-{nxt['source_end_frame']}) with adjacent native context; open: red-stroke draw track (<2510..>2545, pre-SUB051) has no owning event; optionally apply S0015 [1141,1155] in a production-draft revision.")
json.dump(q,open(P/'CURRENT_NATIVE_QUEUE_v23.json','w'),indent=1);print(q['count'],q['next_atomic_operation'])
