"""Deterministic adversarial-QA sample: >=6 rows from each audited batch, stratified over niche, format and score tercile.

Selection is hash-seeded (reproducible) and greedy: each pick must add a new (niche, format, tercile) stratum or
a new channel until the sample is full. Usage: qa_select.py B002-01 B002-02 B002-03
"""
import hashlib, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCR = Path('/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/e9d5fa3f-9fa3-4acc-b7cf-207755ab01a1/scratchpad/audit')


def pick(bid, k=6):
    rows = json.loads((HERE / f'audit-batch-{bid}.json').read_text())
    inp = {i['Thumbnail_ID']: i for i in json.loads((SCR / bid / 'input.json').read_text())}
    s = sorted(r['score_100'] for r in rows); lo, hi = s[len(s) // 3], s[2 * len(s) // 3]
    tier = lambda v: 'LOW' if v <= lo else 'HIGH' if v >= hi else 'MID'
    order = sorted(rows, key=lambda r: hashlib.sha256(('qa' + r['Thumbnail_ID']).encode()).hexdigest())
    chosen, seen, chans = [], set(), set()
    for r in order:
        i = inp[r['Thumbnail_ID']]; key = (i['Niche_Label'][:10], i['Format'][:5], tier(r['score_100']))
        if key not in seen or i['Channel_ID'] not in chans:
            chosen.append(r['Thumbnail_ID']); seen.add(key); chans.add(i['Channel_ID'])
        if len(chosen) == k: break
    for r in order:  # top up if strata were exhausted
        if len(chosen) == k: break
        if r['Thumbnail_ID'] not in chosen: chosen.append(r['Thumbnail_ID'])
    return chosen


if __name__ == '__main__':
    out = {b: pick(b) for b in sys.argv[1:]}
    (HERE / ('qa-selection-%s.json' % '+'.join(sys.argv[1:]))).write_text(json.dumps(out, indent=1))
    print({b: len(v) for b, v in out.items()})
