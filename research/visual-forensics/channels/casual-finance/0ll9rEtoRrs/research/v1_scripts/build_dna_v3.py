#!/usr/bin/env python3
"""Video 004 DNA statistics from integrated_v2 (24 fps). python3 -I from workspace root. Statistics are MEASURED from ledgers; qualitative rules INFERRED."""
import csv, json, bisect, statistics as st
from collections import Counter, defaultdict
R = lambda p: list(csv.DictReader(open(p)))
FPS = 24
S = R('integrated_v3/reviewed_states_v3.csv'); C = R('integrated_v3/reviewed_candidates_v3.csv'); U = R('integrated_v3/unowned_intervals_v3.csv')
bounds = sorted((int(s['start']), int(s['end']), s['id'], (s['family'] or 'UNKNOWN').split(' ', 1)[0] + ' ' + (s['family'].split(' ', 1)[1] if ' ' in s['family'] else '')) for s in S)
starts = [b[0] for b in bounds]
def own(f):
    i = bisect.bisect_right(starts, f) - 1
    return bounds[i] if i >= 0 and bounds[i][0] <= f <= bounds[i][1] else None
def norm(fam): return fam.replace('full-bleed screenshot/document', 'full-bleed screenshot').replace('F4 full-bleed screenshot', 'F4 full-bleed screenshot/document') if fam.startswith('F4') else fam
fam_of = {b[2]: norm(b[3]).strip() for b in bounds}
fam = defaultdict(lambda: {'states': 0, 'frames': 0, 'dur': [], 'events': Counter(), 'ex': []})
for b in bounds:
    f = fam[fam_of[b[2]]]; f['states'] += 1; f['frames'] += b[1] - b[0] + 1; f['dur'].append(b[1] - b[0] + 1)
cls_all = Counter(); inside = outside = 0
for c in C:
    if c['final_type_v3'] in ('NOT_A_CHANGE', 'CODEC_ARTIFACT') or c['verdict'] in ('NOT_A_CHANGE', 'CODEC_ARTIFACT'): continue
    o = own(int(c['start'])); cls_all[c['final_type_v3']] += 1
    if o: fam[fam_of[o[2]]]['events'][c['final_type_v3']] += 1; inside += 1
    else: outside += 1
COMP=R('integrated_v3/compositions_v3.csv'); cs=[int(c['span_frames']) for c in COMP]
mins = 24298 / FPS / 60
durs = [b[1] - b[0] + 1 for b in bounds]
q = st.quantiles(durs, n=10)
stats = {'fps': FPS, 'total_frames': 24298, 'minutes': round(mins, 2), 'states': len(bounds),
  'states_per_min': round(len(bounds) / mins, 2), 'state_dur_s': {'median': round(st.median(durs) / FPS, 2), 'mean': round(st.mean(durs) / FPS, 2), 'p10': round(q[0] / FPS, 2), 'p90': round(q[-1] / FPS, 2), 'max': round(max(durs) / FPS, 2)},
  'edit_events_total': sum(cls_all.values()), 'edit_events_per_min': round(sum(cls_all.values()) / mins, 1), 'events_in_states': inside, 'events_in_unowned_gaps': outside,
  'event_types': dict(cls_all.most_common()), 'unowned_frames': sum(int(u['n_frames']) for u in U), 'unowned_share_pct': round(100 * sum(int(u['n_frames']) for u in U) / 24298, 1),
  'unowned_class_frames': dict(Counter({k: sum(int(u['n_frames']) for u in U if (u['rr_class'] or u['sp_class']) == k) for k in {(u['rr_class'] or u['sp_class']) for u in U}}).most_common()),
  'families': {k: {'states': v['states'], 'share_of_state_frames_pct': round(100 * v['frames'] / sum(x['frames'] for x in fam.values()), 1), 'median_dur_s': round(st.median(v['dur']) / FPS, 2), 'top_events': dict(v['events'].most_common(4))} for k, v in sorted(fam.items())},
  'compositions': len(COMP), 'composition_span_s': {'median': round(st.median(cs)/FPS,2), 'mean': round(st.mean(cs)/FPS,2), 'p90': round(sorted(cs)[int(.9*len(cs))]/FPS,2)}, 'compositions_per_min': round(len(COMP)/mins,2), 'candidate_verification': dict(Counter(c['smp_status'] for c in C)), 'label': 'MEASURED from v3 ledgers; all 807 first-pass CONFIRMED candidates now independently viewed; type corrections applied only with HIGH/MEDIUM reviewer confidence; unowned gaps not absorbed; 48 priority gaps re-reviewed; embedded-video label corrected only for those 48'}
json.dump(stats, open('production/dna_statistics_v3.json', 'w'), indent=1)
with open('production/composition_family_specs_v3.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['family', 'states', 'share_state_frames_pct', 'median_dur_s', 'top_events'])
    for k, v in stats['families'].items(): w.writerow([k, v['states'], v['share_of_state_frames_pct'], v['median_dur_s'], json.dumps(v['top_events'])])
print(json.dumps({k: v for k, v in stats.items() if k != 'families'}, indent=1)); 
for k, v in stats['families'].items(): print(k, v)
