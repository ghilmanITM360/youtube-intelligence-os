import csv,json
from pathlib import Path
P=Path(__file__).parent;N5=P.parent/'Casual-Finance-Video006-native5-20261115'
rows=list(csv.DictReader(open(N5/'visual_event_ledger_v45.csv')));hdr=list(rows[0]);n=0
for r in rows:
    if r['event_id']=='EP0078':
        n+=1
        r.update(verdict='CONFIRMED_NATIVE_SINGLE_REVIEW',
         description="Native: static through 2436 (adjacent diffs max channel delta<=9, 0 px>60); motion onset EXACT at 2437. Article scrolls up 2437-2445 (banner headline 'Sept FOMC Preview...' rises into view); small-change lull 2446-2447; presenter pointer/arm swing at 2448 (changed bbox x137-926, left character region) with pointer then held raised through 2469 (2450 vs 2445 pose differs; swing sub-frames not decomposed); lull 2449-2450; article banner tag 'ECONOMIC DATA & ANALYSIS' appears by 2455 (scroll/reveal 2451-2455); small-change 2456-2457; Author card (Yelena Shulyatyeva, CFA) slides in from right edge 2458-2469 (2458 first pixels x1889+, 2459 partial, full card by ~2465, settles leftward through 2469); last changed frame 2469, static again from 2470 (<=4 px>60). Motion is multi-phase, not one continuous gesture.",
         observed_change_first_frame='2437',observed_change_last_frame='2469',motion_object='article scroll; presenter pointer; Author card',
         review_scope='BOUNDED_NATIVE_SINGLE_REVIEWER_NO_INDEPENDENT_QA;NO_GLOBAL_APPROVAL',
         timing_precision='NATIVE_EXACT_ONSET_2437_LAST_CHANGE_2469_SUBPHASES_MEASURED_NOT_SEMANTICALLY_SPLIT',
         bounds_role='NATIVE_VERIFIED_WINDOW_EQUALS_CANDIDATE_WINDOW',
         macro_review_ref=str(P/'EP0078_RULING.json'))
assert n==1
w=csv.DictWriter(open(P/'visual_event_ledger_v46.csv','w',newline=''),fieldnames=hdr);w.writeheader();w.writerows(rows)
q=json.load(open(N5/'CURRENT_NATIVE_QUEUE_v21.json'));k=len(q['items'])
q['items']=[i for i in q['items'] if i['event_id']!='EP0078'];assert len(q['items'])==k-1
q.update(queue_version=22,count=len(q['items']),baseline=str(P/'visual_event_ledger_v46.csv'))
nxt=q['items'][[i['event_id'] for i in json.load(open(N5/'CURRENT_NATIVE_QUEUE_v21.json'))['items']].index('EP0078')]
q['next_atomic_operation']=f"Verify next queue item {nxt['event_id']} ({nxt['source_start_frame']}-{nxt['source_end_frame']}) with adjacent native context; optionally apply S0015 [1141,1155] in a production-draft revision."
json.dump(q,open(P/'CURRENT_NATIVE_QUEUE_v22.json','w'),indent=1);print(q['count'],q['next_atomic_operation'])
