# Consolidate validated reviewer batches. Args: rv_prefix batch1,batch2,...  (cwd = video workspace)
import csv,json,sys
from pathlib import Path
pre,batches=sys.argv[1],sys.argv[2].split(',')
states=[r['state'] for r in csv.DictReader(open('tables/states_v1.csv'))]
out={};summary={'batches':batches,'not_validated':[]}
for kind in ('art_audit','motion_events','narration_relation','state_prompts'):
    rows=[]
    for b in batches:
        v=Path(f'tables/validation_{pre}_{b}_{b}.json')
        if not v.exists() or json.load(open(v))['errors']:
            summary['not_validated'].append(b);continue
        for r in csv.DictReader(open(f'agents/{pre}_{b}/{kind}_{b}.csv')):r['batch']=b;rows.append(r)
    if rows:
        cols=list(dict.fromkeys(k for r in rows for k in r))
        with open(f'tables/consolidated_{kind}.csv','w',newline='') as f:
            w=csv.DictWriter(f,cols);w.writeheader();w.writerows(rows)
    out[kind]=rows
summary['not_validated']=sorted(set(summary['not_validated']))
for k in ('art_audit','state_prompts'):
    have={r['state'] for r in out[k]};summary[k+'_states']=f'{len(have & set(states))}/{len(states)}';summary[k+'_missing']=[s for s in states if s not in have]
summary['motion_events']=len(out['motion_events'])
segs={}
for r in out['narration_relation']:
    if r['seg_index'].isdigit():segs.setdefault(int(r['seg_index']),[]).append(r['relation'])
nseg=sum(1 for _ in csv.DictReader(open('asr/asr_small_en_segments.csv')))
summary['narration_segments_covered']=f'{len(segs)}/{nseg}';summary['narration_missing']=[i for i in range(nseg) if i not in segs]
from collections import Counter
summary['relation_counts']=dict(Counter(x.split('_PARTIAL')[0] for v in segs.values() for x in v))
summary['motion_types']=dict(Counter(r['event_type'] for r in out['motion_events']))
json.dump(summary,open('tables/consolidation_summary.json','w'),indent=1);print(json.dumps({k:v for k,v in summary.items() if 'missing' not in k}))
