#!/usr/bin/env python3
"""Casual Finance milestone counter (visual-only CT_SCAN contract, no audio sign-off).
A video counts only if, at run time: source SHA-256 == baseline, gate file says COMPLETE_WITH_EVIDENCE,
and the video's validator is clean (re-run command exit 0, or recorded failed==0).
Add an entry to visual_complete_ledger.json ONLY after the owner-accepted gate passes. Read-only otherwise."""
import hashlib, json, subprocess, sys, os
D = os.path.dirname(os.path.abspath(__file__))
base = {r['video_id']: r for r in json.load(open(f'{D}/source_identity_baseline_v1.json'))['rows']}
ledger = json.load(open(f'{D}/visual_complete_ledger.json'))
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
ok = 0
for e in ledger['videos']:
    v, w = e['video_id'], e['workspace']
    c = {'sha': sha(base[v]['source_path']) == base[v]['sha256'],
         'gate': 'COMPLETE_WITH_EVIDENCE' in json.dumps(json.load(open(f"{w}/{e['gate_file']}")))}
    if e.get('validator_cmd'):
        c['validator'] = subprocess.run(e['validator_cmd'], shell=True, cwd=w, capture_output=True).returncode == 0
    else:
        r = json.load(open(f"{w}/{e['validation_json']}")); c['validator'] = r['failed'] == 0 and r['passed'] == r['total']
    good = all(c.values()); ok += good
    print(('COUNTS  ' if good else 'REJECT  ') + v, c)
print(f"VERIFIED_COMPLETE {ok} / target {ledger['next_milestone']}  (roster 35)")
sys.exit(0 if ok else 1)
