import csv,json,pathlib,cv2,numpy as np,hashlib
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');D=R/'agents/merge_split_review';D.mkdir(exist_ok=True);E=D/'sheets';E.mkdir(exist_ok=True)
def read(n):return list(csv.DictReader((R/n).open()))
S=read('tables/states_machine.csv');by={s['state_id']:s for s in S};prev={b['state_id']:a for a,b in zip(S,S[1:])};first={s['id']:s for i in range(1,11) for s in json.loads((R/f'agents/shard_{i}/OUT_shard_{i}.json').read_text())['states']};requests=[]
for x in read('integrated_v1/merge_split_prompt_audit.csv'):
 sid=x['state_id'];s=by[sid];a=prev[sid];image=np.vstack([cv2.imread(str(R/a['rep_image'])),cv2.imread(str(R/s['rep_image']))]);path=E/(sid+'.jpg');assert not path.exists();cv2.imwrite(str(path),image)
 related=[]
 for c in read('tables/candidates_classified.csv'):
  if int(a['end'])-2<=int(c['start'])<=int(s['end']):related.append({k:c[k] for k in ('id','start','end','evidence','kind')})
 requests.append(dict(state_id=sid,previous=a['state_id'],start=int(s['start']),end=int(s['end']),sheet=str(path),layout='TOP previous scaled960x540, BOTTOM current scaled960x540; representative images not boundary/motion proof',merge_requested=x['merge_requested']=='True',split_requested=x['split_requested']=='True',duplicate_of=x['duplicate_of'],claim=x['evidence'],previous_objects=first[a['state_id']]['objects'],current_objects=first[sid]['objects'],related_candidates=related))
(D/'items.json').write_text(json.dumps(requests,indent=2));print('adjudication items',len(requests))
