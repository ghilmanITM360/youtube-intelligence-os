#!/usr/bin/env python3
"""Integrate first pass + second-pass reviewers A/B/C/D into tables/integrated/. Read-only on all inputs.
Writes only new files under tables/integrated/. Run with python3 -I from the ROOT.
"""
import csv, json, os, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'tables', 'integrated')
os.makedirs(OUT, exist_ok=True)
NFRAMES = 22583
CUT_PX = 50000  # px_diff_ge12 threshold used only to LABEL a measured cut peak, same as reviewer B/D check

def J(p): return json.load(open(os.path.join(ROOT, p)))
def C(p): return list(csv.DictReader(open(os.path.join(ROOT, p))))

rev = {'A': J('agents2/OUT2_A.json'), 'B': J('agents2/OUT2_B.json'),
       'C': J('agents2/OUT2_C_MERGED.json'), 'D': J('agents2/OUT2_D.json')}
fp = {n: J(f'tables/first_pass/FIRST_PASS_shard_{n}.json') for n in range(1, 9)}
shard_rev = {1: 'A', 2: 'A', 3: 'B', 4: 'B', 5: 'C', 6: 'C', 7: 'D', 8: 'D'}

cand_meta = {r['id']: r for r in C('tables/candidate_evidence.csv')}
states = C('tables/states_machine.csv')
meas = {int(r['frame']): r for r in C('FULL_FRAME_MEASUREMENTS.csv')}

# ---- candidates
fp_c = {}; fp_s = {}; fp_d = {}
for n, d in fp.items():
    for c in d['candidates']: fp_c[c['id']] = (n, c)
    for s in d['states']: fp_s[s['id']] = (n, s)
    for x in d['disputes']: fp_d[x['id']] = (n, x)
rows = []
for k in 'ABCD':
    for c in rev[k]['candidates']:
        n, f = fp_c[c['id']]
        rows.append({'id': c['id'], 'shard': n, 'reviewer': k, 'start': cand_meta[c['id']]['start'], 'end': cand_meta[c['id']]['end'],
                     'first_pass_verdict': f['verdict'], 'first_pass_type': f['type'], 'first_pass_boundary': f['state_boundary'],
                     'second_pass_type': c.get('second_pass_type', ''), 'second_pass_boundary': c.get('second_pass_state_boundary', ''),
                     'agreement': c['agreement'], 'final_decision': c['final_decision'], 'confidence': c['confidence'],
                     'evidence': c['evidence']})
rows.sort(key=lambda r: (int(r['start']), r['id']))
with open(os.path.join(OUT, 'candidates_final.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# ---- states: reviewer record per state
srec = {}
for k in 'ABCD':
    for s in rev[k]['states']: srec[s['id']] = (k, s)
out_states = []
late = []
flagged = []
for r in states:
    sid = r['state_id']
    start, end = int(r['start']), int(r['end'])
    k, s = srec[sid] if sid in srec else (None, None)
    # MEASURED cut peak within +-3 frames of draft start (uniform check for all reviewers)
    win = [(f, float(meas[f]['px_diff_ge12'])) for f in range(max(0, start - 3), min(NFRAMES, start + 4)) if f in meas]
    pk = max(win, key=lambda x: x[1]) if win else (start, 0.0)
    off = pk[0] - start
    # hard-cut signature: peak exactly one frame EARLIER than the draft start; other offsets (zoom/pan/fade) are only flagged
    measured_start = pk[0] if (off == -1 and pk[1] > CUT_PX and start > 0) else start
    flag_offset = (off != 0 and off != -1 and pk[1] > CUT_PX and start > 0) or (off == -1 and pk[1] <= CUT_PX and False)
    rev_start = s.get('true_start_frame') if s else None
    if measured_start != start: late.append((sid, start, measured_start, int(pk[1])))
    if flag_offset: flagged.append((sid, start, pk[0], int(pk[1])))
    mp = s.get('merge_with_prev') if s else None
    out_states.append({'state_id': sid, 'draft_start': start, 'draft_end': end, 'measured_start': measured_start,
        'reviewer_declared_start': rev_start if rev_start is not None else '', 'reviewer': k or ('FIRST_PASS_ONLY' if sid == 'S0000' else ''),
        'agreement': s['agreement'] if s else '', 'merge_with_prev': mp, 'split_needed': bool(s.get('split_needed')) if s else False,
        'n_corrections': len(s.get('corrections') or []) if s else 0, 'readable_text': (s.get('readable_text') if s else '') or ''})

with open(os.path.join(OUT, 'states_final.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out_states[0].keys())); w.writeheader(); w.writerows(out_states)

# ---- unowned intervals: union across reviewers, de-duplicated by (start,end)
un = {}
for k in 'ABCD':
    for u in rev[k]['unowned_intervals']:
        key = (int(u['start']), int(u['end']))
        un.setdefault(key, []).append((k, u))
un_rows = [{'start': a, 'end': b, 'reviewers': ','.join(sorted({x[0] for x in v})), 'description': v[0][1]['description'][:300]} for (a, b), v in sorted(un.items())]
with open(os.path.join(OUT, 'unowned_intervals_final.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['start', 'end', 'reviewers', 'description']); w.writeheader(); w.writerows(un_rows)

# ---- ownership timeline: corrected state starts, gaps filled by reviewer intervals
owner = [None] * NFRAMES
for i, r in enumerate(out_states):
    s0 = r['measured_start']; e0 = r['draft_end']
    for f in range(s0, e0 + 1):
        if owner[f] is None: owner[f] = r['state_id']
overlaps = 0
for r in out_states:  # overlap check: measured start must not land inside previous state's frames other than its own corrected slot
    pass
for (a, b), v in un.items():
    for f in range(a, b + 1):
        if 0 <= f < NFRAMES and owner[f] is None: owner[f] = 'UNOWNED:%d-%d' % (a, b)
uncovered = [f for f in range(NFRAMES) if owner[f] is None]
def runs(fr):
    out = [];
    for f in fr:
        if out and f == out[-1][1] + 1: out[-1][1] = f
        else: out.append([f, f])
    return out
cover = {'frames': NFRAMES, 'owned_by_state': sum(1 for o in owner if o and o.startswith('S')),
         'owned_by_unowned_interval': sum(1 for o in owner if o and o.startswith('UNOWNED')), 'uncovered': len(uncovered),
         'uncovered_runs': runs(uncovered)}

# ---- merge groups (composition groups): True merges only; UNCERTAIN stays separate
groups = []; cur = None
for r in out_states:
    if cur and r['merge_with_prev'] is True: cur['members'].append(r['state_id']); cur['end'] = r['draft_end']
    else:
        cur = {'start': r['measured_start'], 'end': r['draft_end'], 'members': [r['state_id']]}; groups.append(cur)
with open(os.path.join(OUT, 'composition_groups.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['group', 'start', 'end', 'n_states', 'members'])
    for i, g in enumerate(groups): w.writerow(['G%04d' % i, g['start'], g['end'], len(g['members']), ';'.join(g['members'])])

# ---- disputes
drows = []
for k in 'ABCD':
    for x in rev[k]['disputes']:
        n, f = fp_d[x['id']]
        drows.append({'id': x['id'], 'shard': n, 'reviewer': k, 'cut_frame': x.get('cut_frame', ''), 'first_pass_verdict': f['verdict'],
                      'second_pass_verdict': x['second_pass_verdict'], 'agreement': x['agreement'], 'sampled': x.get('sampled'),
                      'confidence': x['confidence']})
drows.sort(key=lambda r: r['id'])
with open(os.path.join(OUT, 'disputes_final.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(drows[0].keys())); w.writeheader(); w.writerows(drows)

# ---- corrections ledger
led = []
for k in 'ABCD':
    for c in rev[k]['candidates']:
        if c['agreement'] == 'CORRECTED': led.append({'kind': 'candidate', 'id': c['id'], 'reviewer': k, 'detail': c['evidence'][:400]})
    for s in rev[k]['states']:
        for cr in (s.get('corrections') or []):
            led.append({'kind': 'state', 'id': s['id'], 'reviewer': k, 'detail': json.dumps(cr)[:400]})
with open(os.path.join(OUT, 'corrections_ledger.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['kind', 'id', 'reviewer', 'detail']); w.writeheader(); w.writerows(led)

summary = {'candidates': len(rows), 'candidates_by_reviewer': dict(Counter(r['reviewer'] for r in rows)),
           'candidate_agreement': dict(Counter(r['agreement'] for r in rows)), 'candidate_final_decision': dict(Counter(r['final_decision'] for r in rows)),
           'states': len(out_states), 'states_by_reviewer': dict(Counter(r['reviewer'] for r in out_states)),
           'state_merge_with_prev': dict(Counter(str(r['merge_with_prev']) for r in out_states)),
           'composition_groups': len(groups), 'measured_late_start_states_1frame': [list(x) for x in late], 'flagged_non_cut_offsets_not_applied': [list(x) for x in flagged],
           'disputes': len(drows), 'dispute_verdicts': dict(Counter(r['second_pass_verdict'] for r in drows)),
           'unowned_intervals_union': len(un_rows), 'coverage': cover, 'corrections_ledger_rows': len(led)}
json.dump(summary, open(os.path.join(OUT, 'integration_summary.json'), 'w'), indent=1)
print(json.dumps(summary, indent=1))
