"""Deterministic stratified QA sample over package audits (5 per PK batch, greedy cover of primary relationship, channel and score tercile)
and reviewer packets (12 packages per reviewer, sourced from the same inputs the auditors saw plus the audit rows). Usage: package_qa_select.py [per_batch=5]"""
import hashlib, json, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCR = Path('/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/e9d5fa3f-9fa3-4acc-b7cf-207755ab01a1/scratchpad')
per = int(sys.argv[1]) if len(sys.argv) > 1 else 5
plan = json.load((HERE / 'package-batch-plan.json').open())['batches']
sel, packets = {}, []
rows_all = {}
for pk in plan:
    p = HERE / f'package-audit-{pk}.json'
    if not p.exists(): continue
    rows = json.load(p.open()); inp = {i['Package_ID']: i for i in json.load((SCR / 'packages' / f'{pk}.json').open())}
    s = sorted(r['score_100'] for r in rows); lo, hi = s[len(s) // 3], s[2 * len(s) // 3]
    tier = lambda v: 'L' if v <= lo else 'H' if v >= hi else 'M'
    order = sorted(rows, key=lambda r: hashlib.sha256(('pqa' + r['Package_ID']).encode()).hexdigest())
    chosen, seen_rel, seen_ch = [], set(), set()
    for r in order:
        i = inp[r['Package_ID']]
        if r['primary_relationship'] not in seen_rel or i['Channel_Name'] not in seen_ch or tier(r['score_100']) not in {tier(c['score_100']) for c in chosen}:
            chosen.append(r); seen_rel.add(r['primary_relationship']); seen_ch.add(i['Channel_Name'])
        if len(chosen) == per: break
    for r in order:
        if len(chosen) == per: break
        if r not in chosen: chosen.append(r)
    sel[pk] = [r['Package_ID'] for r in chosen]
    for r in sorted(chosen, key=lambda r: r['seq']):
        i = inp[r['Package_ID']]
        packets.append(dict(pk=pk, seq=r['seq'], Package_ID=r['Package_ID'], Title=i['Title'], Channel_Name=i['Channel_Name'], Niche=i['Niche'], Format=i['Format'], Image_Path=i['Image_Path'], thumbnail_audit=i['thumbnail_audit'], title_audit=i['title_audit'], audit_row=r))
(HERE / 'package-qa-selection.json').write_text(json.dumps(sel, indent=1))
(SCR / 'packages').mkdir(exist_ok=True)
n = 0
for k in range(0, len(packets), 12):
    n += 1; (SCR / 'packages' / f'qa_packet_{n}.json').write_text(json.dumps(packets[k:k + 12], indent=1))
print(len(packets), 'sampled packages;', n, 'reviewer packets;', dict(Counter(p['audit_row']['primary_relationship'] for p in packets)))
