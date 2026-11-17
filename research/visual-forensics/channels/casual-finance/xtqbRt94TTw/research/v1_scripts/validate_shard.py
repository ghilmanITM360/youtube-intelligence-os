import json,sys,pandas as pd,os
R=os.path.expanduser('~/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
CV={'CONFIRMED','RECLASSIFIED','CODEC_ARTIFACT','UNVERIFIED','NOT_A_CHANGE'};DV={'REAL_STATE_CHANGE','REAL_MOTION','WITHIN_STATE_CHANGE','NO_VISIBLE_CHANGE','UNVERIFIED'}
SF='objects background illustration typography readable_text unreadable_text hierarchy camera_motion entry_exit story_function evidence confidence continuity recon prompt family'.split()
for n in sys.argv[1:]:
    d=f'{R}/agents/shard_{n}';o=json.load(open(f'{d}/OUT_shard_{n}.json'));err=[]
    for k,f,vf in(('candidates','candidates.csv',None),('states','states.csv',None),('disputes','disputes.csv',None)):
        ids=pd.read_csv(f'{d}/{f}').iloc[:,0].tolist();got=[x.get('id') for x in o[k]]
        if ids!=got:err.append(f'{k} id/order mismatch {len(ids)} vs {len(got)}')
    for c in o['candidates']:
        if c.get('verdict') not in CV or len(str(c.get('desc','')).split())<4:err.append('cand '+c.get('id','?'))
    for c in o['disputes']:
        if c.get('verdict') not in DV:err.append('disp '+c.get('id','?'))
    for s in o['states']:
        if any(not isinstance(s.get(f),str) or not s.get(f).strip() and f not in('readable_text','unreadable_text') for f in SF):err.append('state fields '+s.get('id','?'))
    pr=[s['prompt'] for s in o['states'] if isinstance(s.get('prompt'),str)];dup=len(pr)-len(set(pr))
    print(n,'ERRORS' if err else 'PASS',err[:8],'dup_prompts',dup,'verdicts',pd.Series([c['verdict'] for c in o['candidates']]).value_counts().to_dict())
