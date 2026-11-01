import csv,glob,collections,json
rd=lambda p:list(csv.DictReader(open(p)))
C=rd('integrated_v3/reviewed_candidates_v3.csv')
R={}
for f in sorted(glob.glob('phaseA/cand_review_[0-9].csv')):
    for r in rd(f):R[r['id']]=dict(r,wave='SAMPLE_STRATIFIED')
for f in sorted(glob.glob('phaseA/cand_expand_review_*.csv')):
    for r in rd(f):R[r['id']]=dict(r,wave='EXPANSION_ERROR_PRONE_TYPES')
for f in sorted(glob.glob('phaseA/cand_rest_review_*.csv')):
    for r in rd(f):R[r['id']]=dict(r,wave='REMAINDER_FIRST_PASS_ONLY_ROWS')
ctl={k for k in R if k.startswith('CTL')}
for k in ctl:R.pop(k)
for c in C:
    r=R.get(c['id']);c['smp_status']='REVIEWED_'+r['decision'] if r else ('SECOND_PASSED' if c['sp_decision']!='NOT_SECOND_PASSED' else 'FIRST_PASS_ONLY')
    c['smp_wave']=r['wave'] if r else '';c['smp_suggested_type']=r['suggested_type'] if r else '';c['smp_reason']=r['reason'] if r else '';c['smp_confidence']=r['confidence'] if r else ''
    t=c['final_type']
    if r and r['decision']=='CONFIRMED_TYPE_WRONG' and r['suggested_type'] and r['confidence'] in('HIGH','MEDIUM'):t=r['suggested_type']
    c['final_type_v3']=t
w=csv.DictWriter(open('integrated_v3/reviewed_candidates_v3.csv','w',newline=''),fieldnames=C[0].keys());w.writeheader();w.writerows(C)
cnt=collections.Counter(c['smp_status'] for c in C);print(cnt)
print(sum(1 for c in C if c['final_type_v3']!=c['final_type']),'types updated')
json.dump(dict(cnt),open('integrated_v3/candidate_verification_counts_v3.json','w'),indent=1)
