"""Merge reviewer C partial (OUT2_C) with reruns C2a/C2b into OUT2_C_MERGED.json; originals untouched, each row tagged with source_file."""
import json, collections, sys
R = sys.argv[1]
c = json.load(open(f'{R}/agents2/OUT2_C.json'))
a = json.load(open(f'{R}/agents2/OUT2_C2a.json'))
b = json.load(open(f'{R}/agents2/OUT2_C2b.json'))
fp = {n: json.load(open(f'{R}/tables/first_pass/FIRST_PASS_shard_{n}.json')) for n in (5, 6)}

def merge(base, new, key, src_new):
    nm = {x[key]: x for x in new}
    out = []
    for x in base:
        if x[key] in nm:
            y = dict(nm[x[key]]); y['source_file'] = src_new; y['superseded_row_in_OUT2_C'] = True
        else:
            y = dict(x); y['source_file'] = 'OUT2_C.json'
        out.append(y)
    assert len(out) == len(base) and set(nm) <= {x[key] for x in base}
    return out

m = {'name': 'C_MERGED', 'shards': c['shards']}
m['candidates'] = merge(c['candidates'], a['candidates'], 'id', 'OUT2_C2a.json')
m['states'] = merge(c['states'], b['states'], 'id', 'OUT2_C2b.json')
m['disputes'] = merge(c['disputes'], b['disputes'], 'id', 'OUT2_C2b.json')
m['unowned_intervals'] = merge(c['unowned_intervals'], b['unowned_intervals'], 'start', 'OUT2_C2b.json')
m['extra'] = [dict(x, source_file='OUT2_C.json') for x in c['extra']] + [dict(x, source_file='OUT2_C2a.json') for x in a['extra']] + [dict(x, source_file='OUT2_C2b.json') for x in b['extra']]
json.dump(m, open(f'{R}/agents2/OUT2_C_MERGED.json', 'w'), indent=1)

# validation
for sec in ('candidates', 'states', 'disputes'):
    ids = [x['id'] for n in (5, 6) for x in fp[n][sec]]
    got = [x['id'] for x in m[sec]]
    print(sec, len(got), 'ids_match_first_pass', got == ids, collections.Counter(x['agreement'] for x in m[sec]), collections.Counter(x['source_file'] for x in m[sec]))
print('unowned', len(m['unowned_intervals']), collections.Counter(x['confidence'] for x in m['unowned_intervals']))
print('extra', len(m['extra']))
bad = [x['id'] for x in m['candidates'] + m['states'] + m['disputes'] if x['agreement'] == 'UNVERIFIED']
print('remaining UNVERIFIED:', bad)
