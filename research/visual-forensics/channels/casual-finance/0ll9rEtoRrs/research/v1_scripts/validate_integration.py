#!/usr/bin/env python3
"""Validate tables/integrated against first pass + master tables. python3 -I; includes in-memory negative tests (--negative)."""
import csv, json, os, sys, copy
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def C(p): return list(csv.DictReader(open(os.path.join(ROOT, p))))
def load():
    d = {'cand': C('tables/integrated/candidates_final.csv'), 'states': C('tables/integrated/states_final.csv'),
         'disp': C('tables/integrated/disputes_final.csv'), 'un': C('tables/integrated/unowned_intervals_final.csv')}
    d['fp_c'] = [c['id'] for n in range(1, 9) for c in json.load(open(os.path.join(ROOT, f'tables/first_pass/FIRST_PASS_shard_{n}.json')))['candidates']]
    d['fp_s'] = [s['id'] for n in range(1, 9) for s in json.load(open(os.path.join(ROOT, f'tables/first_pass/FIRST_PASS_shard_{n}.json')))['states']]
    d['fp_d'] = [x['id'] for n in range(1, 9) for x in json.load(open(os.path.join(ROOT, f'tables/first_pass/FIRST_PASS_shard_{n}.json')))['disputes']]
    return d
def check(d, n=22583):
    errs = []
    if sorted(r['id'] for r in d['cand']) != sorted(d['fp_c']): errs.append('candidate id set != first pass (695)')
    if len(d['cand']) != 695: errs.append('candidate count != 695')
    if sorted(r['state_id'] for r in d['states']) != sorted(d['fp_s']) and len(d['states']) != 409: errs.append('state set/count mismatch')
    if len(d['states']) != 409: errs.append('state count != 409')
    if sorted(r['id'] for r in d['disp']) != sorted(d['fp_d']): errs.append('dispute id set != first pass (280)')
    for r in d['cand']:
        if r['final_decision'] not in ('ACCEPT_FIRST', 'USE_SECOND', 'UNVERIFIED'): errs.append('bad final_decision ' + r['id'])
        if r['agreement'] not in ('AGREE', 'CORRECTED', 'UNVERIFIED'): errs.append('bad agreement ' + r['id'])
    owner = [0] * n
    prev_end = -1
    for r in sorted(d['states'], key=lambda r: int(r['measured_start'])):
        s, e = int(r['measured_start']), int(r['draft_end'])
        if s > e: errs.append('state start>end ' + r['state_id'])
        for f in range(s, e + 1): owner[f] += 1
    for u in d['un']:
        for f in range(int(u['start']), int(u['end']) + 1):
            if owner[f] == 0: owner[f] = 1
    if any(o == 0 for o in owner): errs.append('uncovered frames: %d' % sum(1 for o in owner if o == 0))
    if any(o > 1 for o in owner): errs.append('overlapped frames: %d' % sum(1 for o in owner if o > 1))
    return errs
if __name__ == '__main__':
    d = load(); e = check(d)
    print('POSITIVE:', 'PASS' if not e else 'FAIL', e)
    if '--negative' in sys.argv:
        t = copy.deepcopy(d); t['cand'].pop(); r1 = check(t)
        t = copy.deepcopy(d); t['states'][5]['draft_end'] = str(int(t['states'][5]['draft_end']) + 2); r2 = check(t)
        t = copy.deepcopy(d); t['states'][7]['draft_end'] = str(int(t['states'][7]['measured_start']) + 0); t['un'] = [u for u in t['un'] if int(u['start']) > 1000 or True][:0]; r3 = check(t)
        t = copy.deepcopy(d); t['cand'][0]['final_decision'] = 'MAYBE'; r4 = check(t)
        t = copy.deepcopy(d); t['disp'].pop(); r5 = check(t)
        res = [bool(x) for x in (r1, r2, r3, r4, r5)]
        print('NEGATIVE (each must be detected):', res, 'PASS' if all(res) else 'FAIL')
        sys.exit(0 if (not e and all(res)) else 1)
    sys.exit(0 if not e else 1)
