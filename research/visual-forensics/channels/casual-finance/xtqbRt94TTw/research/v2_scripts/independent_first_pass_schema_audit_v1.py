import pathlib,json,csv,collections,copy
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');out=[]
SF='objects background illustration typography readable_text unreadable_text hierarchy camera_motion entry_exit story_function evidence confidence continuity recon prompt family'.split()
CV={'CONFIRMED','RECLASSIFIED','CODEC_ARTIFACT','UNVERIFIED','NOT_A_CHANGE'};DV={'REAL_STATE_CHANGE','REAL_MOTION','WITHIN_STATE_CHANGE','NO_VISIBLE_CHANGE','UNVERIFIED'}
def audit(o,i):
 for key,file in [('states','states.csv'),('candidates','candidates.csv'),('disputes','disputes.csv')]:
  rows=list(csv.DictReader((R/f'agents/shard_{i}/{file}').open()));ids=[next(iter(r.values())) for r in rows];assert [x['id'] for x in o[key]]==ids,(i,key,'IDs/order');assert len(ids)==len(set(ids))
 for s in o['states']:
  assert all(isinstance(s.get(k),str) for k in SF),(i,s['id'],'missing/type')
  assert all(s[k].strip() for k in SF if k not in ('readable_text','unreadable_text')),(i,s['id'],'empty')
 for c in o['candidates']:
  assert c['verdict'] in CV and c['state_boundary'] in ('YES','NO') and c['shot_boundary'] in ('YES','NO','AMBIGUOUS'),(i,c['id'],'enum')
  assert isinstance(c['desc'],str) and len(c['desc'].split())>=4,(i,c['id'],'desc')
 for d in o['disputes']:assert d['verdict'] in DV,(i,d['id'],'enum')
 return True
for i in range(1,11):
 o=json.loads((R/f'agents/shard_{i}/OUT_shard_{i}.json').read_text());audit(o,i);out.append(dict(shard=i,counts={k:len(o[k]) for k in ('candidates','states','disputes')},status='PASS'))
o=json.loads((R/'agents/shard_1/OUT_shard_1.json').read_text());bad=copy.deepcopy(o);bad['candidates'][0]['verdict']='FORGED';rejected=False
try:audit(bad,1)
except AssertionError:rejected=True
assert rejected
(R/'session_20261103/independent_first_pass_schema_audit_v1.json').write_text(json.dumps({'shards':out,'tampered_verdict_rejected':rejected,'raw_outputs_unchanged':True,'scope':'independent IDs/order/required fields/types/enum coverage; not semantic approval'},indent=2));print('all10independent schema PASS; tampered verdict rejected')
