import csv,collections,json
rd=lambda p:list(csv.DictReader(open(p)))
P='integrated_v4/reviewed_candidates_v4.csv'
C=rd(P);R={}
for i in(1,2):
    for r in rd(f'phaseA/native58_review_{i}.csv'):R[r['id']]=r
assert len(R)==58
for c in C:
    if 'nat_decision' in c:break
    r=R.get(c['id']);c['nat_decision']=r['decision'] if r else '';c['nat_type']=r['type'] if r else '';c['nat_what']=r['what_changed'] if r else '';c['nat_confidence']=r['confidence'] if r else ''
    c['final_type_prev']=c['final_type_v3']
    if r and r['decision']=='TYPE_CHANGED' and r['confidence'] in('HIGH','MEDIUM') and r['type'] and r['type']!=c['final_type_v3']:c['final_type_v3']=r['type']
w=csv.DictWriter(open(P,'w',newline=''),fieldnames=C[0].keys());w.writeheader();w.writerows(C)
print(collections.Counter(r['decision'] for r in R.values()),collections.Counter((r['decision'],r['confidence']) for r in R.values()))
print(sum(1 for c in C if c['final_type_v3']!=c['final_type_prev']),'types updated at native check')
print([c['id'] for c in C if c['nat_decision']=='NO_REAL_CHANGE'])
