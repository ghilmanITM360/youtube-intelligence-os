#!/usr/bin/env python3
"""Video 004 second-pass integration -> integrated_v2/ (originals in integrated/ untouched). Run with python3 -I from workspace root."""
import csv, json, os, sys, copy, collections
def R(p): return list(csv.DictReader(open(p)))
def W(p, rows, cols=None):
    cols = cols or list(rows[0].keys())
    with open(p, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
N = 24298
SPLITS = {  # parent -> [(child_suffix, start, end)] ; evidence: second_pass/A/A_split_decisions.csv
 'S0089': [('.1', 2962, 3003), ('.2', 3004, 3021)],
 'S0097': [('.1', 3223, 3226), ('.2', 3227, 3348)],
 'S0116': [('.1', 4097, 4111), ('.2', 4112, 4208)],
 'S0475': [('.1', 22094, 22116), ('.2', 22117, 22157), ('.3', 22158, 22227)]}
def build():
    cand = R('integrated/reviewed_candidates.csv'); states = R('integrated/reviewed_states.csv')
    disp = R('integrated/reviewed_disputes.csv'); un = R('repair/unowned_intervals.csv')
    A = {r['id']: r for r in R('second_pass/A/A_decisions.csv')}
    B = {r['id']: r for k in range(1, 6) for r in R(f'second_pass/B/B{k}_decisions.csv')}
    C = {r['id']: r for k in range(1, 4) for r in R(f'second_pass/C/C{k}_decisions.csv')}
    D = {r['gap_id']: r for k in range(1, 4) for r in R(f'second_pass/D/D{k}_decisions.csv')}
    for c in cand:
        s = A.get(c['id']) or B.get(c['id'])
        if s:
            c['sp_decision'] = s['decision']; c['sp_reason'] = s['reason']; c['sp_viewed'] = s['viewed']
            c['sp_corrected_type'] = s.get('corrected_type', '') if s['decision'] == 'CORRECTED' else ''
            c['final_type'] = c['sp_corrected_type'] or c['type']; c['pass'] = 'SECOND_PASS_REVIEWED'
        else:
            c.update(sp_decision='NOT_SECOND_PASSED', sp_reason='', sp_viewed='', sp_corrected_type='', final_type=c['type'])
    for d in disp:
        s = C[d['id']]
        d.update(sp_decision=s['decision'], sp_corrected_verdict=s['corrected_verdict'], sp_confidence=s['confidence'],
                 sp_strip_viewed=s['strip_viewed'], sp_repaired_viewed=s['repaired_viewed'], pass_='SECOND_PASS_REVIEWED')
    out = []
    for s in states:
        if s['id'] in SPLITS:
            for suf, a, b in SPLITS[s['id']]:
                t = copy.deepcopy(s); t.update(id=s['id'] + suf, parent_id=s['id'], start=str(a), end=str(b), n_frames=str(b - a + 1),
                    pass_='SECOND_PASS_SPLIT_DESCRIPTIVE_FIELDS_INHERITED_FROM_PARENT'); out.append(t)
        elif s['id'] == 'S0466':
            t = copy.deepcopy(s); t.update(parent_id='', pass_='SECOND_PASS_START_EXTENDED_21639_TO_21628_INFERRED_MEDIUM', start='21628', n_frames=str(int(s['end']) - 21628 + 1))
            p = {k: '' for k in s}; p.update(id='S0466P', parent_id='', start='21569', end='21627', n_frames='59',
                story_function='Pension chart (Defined Contribution vs Defined Benefit) with red arrow, brown-haired figure',
                evidence='second_pass/A/split/S0466.jpg; second_pass/D/evidence/U129.jpg (OBSERVED f21569-21627)', confidence='MEDIUM', pass_='SECOND_PASS_NEW_STATE_DESCRIPTIVE_FIELDS_PENDING')
            out += [p, t]
        else:
            t = dict(s); t['parent_id'] = ''; t['pass_'] = s.get('pass', ''); out.append(t)
    un2 = []
    for u in un:
        if u['gap_id'] == 'U129': continue  # fully consumed: 21569-21627 -> S0466P, 21628-21638 -> S0466
        d = D[u['gap_id']]
        u = dict(u); u.update(sp_class=d['classification'], sp_relation_proposed=d['relation'], sp_confidence=d['confidence'],
            sp_desc=d['description'], sp_sparse_sampling=d['sampled_frames_limit'], desc_mentions_cut='YES' if 'cut' in d['description'].lower() else 'NO',
            status='UNOWNED_CLASSIFIED_NOT_ABSORBED'); un2.append(u)
    return cand, out, disp, un2
def check(cand, states, disp, un2):
    e = []
    if len(cand) != 1032 or len({c['id'] for c in cand}) != 1032: e.append('candidate count/uniqueness')
    if len(disp) != 148 or len({d['id'] for d in disp}) != 148: e.append('dispute count/uniqueness')
    ids = [s['id'] for s in states]
    if len(ids) != len(set(ids)): e.append('duplicate state ids')
    own = [0] * N
    for s in states:
        a, b = int(s['start']), int(s['end'])
        if a > b: e.append('start>end ' + s['id'])
        for f in range(a, b + 1): own[f] += 1
    for u in un2:
        for f in range(int(u['start']), int(u['end']) + 1): own[f] += 1
    z = sum(1 for o in own if o == 0); m = sum(1 for o in own if o > 1)
    if z: e.append('uncovered frames %d' % z)
    if m: e.append('overlapped frames %d' % m)
    if sum(1 for c in cand if c['sp_decision'] == 'CORRECTED') != 13: e.append('B corrections != 13')
    return e
if __name__ == '__main__':
    cand, states, disp, un2 = build(); e = check(cand, states, disp, un2)
    print('POSITIVE:', 'PASS' if not e else 'FAIL', e)
    def neg(f):
        t = copy.deepcopy((cand, states, disp, un2)); f(*t); return check(*t)
    tests = {'drop candidate': lambda c, s, d, u: c.pop(), 'overlap state': lambda c, s, d, u: s[3].update(end=str(int(s[3]['end']) + 2)),
             'drop gap': lambda c, s, d, u: u.pop(), 'duplicate state id': lambda c, s, d, u: s[1].update(id=s[0]['id']),
             'drop dispute': lambda c, s, d, u: d.pop()}
    neg_ok = True
    for k, f in tests.items():
        r = neg(f); print('NEGATIVE', k, 'DETECTED' if r else 'MISSED', r); neg_ok &= bool(r)
    if e or not neg_ok: sys.exit(1)
    os.makedirs('integrated_v2', exist_ok=True)
    W('integrated_v2/reviewed_candidates_v2.csv', cand); W('integrated_v2/reviewed_states_v2.csv', states)
    W('integrated_v2/reviewed_disputes_v2.csv', disp); W('integrated_v2/unowned_intervals_v2.csv', un2)
    import shutil; shutil.copy('integrated/cross_shard_references.csv', 'integrated_v2/cross_shard_references.csv')
    an = R('integrated/anomaly_ledger.csv'); keys = list(an[0].keys())
    first = keys[0]
    new = ['S0033 first-pass SPLIT_NEEDED claim corrected: stickman through f1294, infographic from f1295 lies in unowned U011 (not in S0033/S0034)',
           'U129 (21569-21638) consumed: S0466P 21569-21627 new state, S0466 start extended to 21628 (21628-21638 INFERRED from f21628/f21639 same composition)',
           '45 disputes second-passed on dispute strips only (14 CONFIRMED candidates have no repaired image); strips may lag a few frames',
           '13 unowned intervals mention a hard cut at the last sampled frame; candidate boundaries, not applied',
           'EMBEDDED_VIDEO label for PDF/browser scrolls in D3 is INFERRED']
    for i, t in enumerate(new): an.append({k: (f'SP{i+1}' if k == first else (t if k == keys[1] else '')) for k in keys})
    W('integrated_v2/anomaly_ledger_v2.csv', an, keys)
    owned = sum(int(s['end']) - int(s['start']) + 1 for s in states); gap = sum(int(u['n_frames']) for u in un2)
    json.dump({'candidates': len(cand), 'candidate_second_pass': collections.Counter(c['sp_decision'] for c in cand),
        'states': len(states), 'state_frames': owned, 'disputes': len(disp), 'disputes_sp': collections.Counter(d['sp_decision'] for d in disp),
        'unowned_intervals': len(un2), 'unowned_frames': gap, 'total_frames': owned + gap,
        'unowned_class': collections.Counter(u['sp_class'] for u in un2),
        'status': 'SECOND_PASS_INTEGRATED_STRUCTURE_ONLY_NOT_SEMANTICALLY_CERTIFIED', 'audio': 'AUDIO_NOT_VERIFIED'},
        open('integrated_v2/integration_summary_v2.json', 'w'), indent=1, default=dict)
    print(json.dumps(json.load(open('integrated_v2/integration_summary_v2.json'))))
