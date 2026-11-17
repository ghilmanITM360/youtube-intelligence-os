import os,json,subprocess,hashlib,csv
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).parent;E=O/'evidence';A=Path('/Users/ghilmankhan/YIOS-v8-readiness-20261026T235710Z');P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1')
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def dump(n,d):(E/n).write_text(json.dumps(d,indent=2)+'\n')
def load(p):return json.loads(p.read_text())
def refs(t):return {l.split()[1]:l.split()[0] for l in t.splitlines()}
def delta(a,b):return {'added':{k:v for k,v in b.items() if k not in a},'removed':{k:v for k,v in a.items() if k not in b},'changed':{k:{'before':v,'after':b[k]} for k,v in a.items() if k in b and v!=b[k]}}
a=load(A/'evidence/GIT_BEFORE.json');b=load(A/'evidence/GIT_AFTER.json');c=load(E/'GIT_CURRENT_BEFORE.json');obj=load(E/'EXACT_REF_INSPECTION.json');x,y,z=[refs(s['refs']['stdout']) for s in [a,b,c]]
remote=load(E/'REMOTE_PUBLICATION_CURRENT.json');oldremote=refs((A/'evidence/LIVE_REMOTE_REFS.txt').read_text());newremote=refs(remote['stdout'])
d={'historical_delta':delta(x,y),'since_previous_final_delta':delta(y,z),'actor':'ACTOR_UNKNOWN','exact_ref_current':obj['exact_ref'],'target_object_type':obj['object_type'],'target_object_bytes':obj['object_size'],'historical_before_existing_target_refs':[k for k,v in x.items() if v==obj['expected_oid']],'current_existing_target_refs':[k for k,v in z.items() if v==obj['expected_oid']],'historical_core_equal':{k:a[k]==b[k] for k in ['head','branch','status','stashes','worktrees']},'fresh_core_equal':{k:b[k]==c[k] for k in ['head','branch','status','stashes','worktrees']},'non_auxiliary_local_delta':delta({k:v for k,v in y.items() if not k.startswith('refs/codex/')},{k:v for k,v in z.items() if not k.startswith('refs/codex/')}),'live_remote_delta':delta(oldremote,newremote),'index_history_limit':'Prior readiness did not record raw index bytes; historical staged/unstaged state supported only by porcelain status. Current raw index baseline recorded for final comparison.','canonical_research_scope':'Tracked research git diff HEAD empty and six selected documents full-byte hash matched; no full ignored/untracked source census repeated.'}
# Compare immutable capture tree with HEAD tree; this reads tree metadata, not media payloads.
r=subprocess.run(['git','diff-tree','--no-commit-id','--name-status','-r','-z',obj['expected_oid'],'HEAD^{tree}'],cwd=P,env=env,capture_output=True,timeout=30);parts=r.stdout.decode().split('\0');entries=[{'reverse_status':parts[i],'path':parts[i+1]} for i in range(0,len(parts)-1,2)]
dump('CAPTURE_TREE_VS_HEAD_METADATA.json',{'exit':r.returncode,'direction':'capture tree -> HEAD; D here means extra entry exists in capture tree, not evidence of a source deletion','changes':entries,'count':len(entries),'all_capture_additions_only':all(q['reverse_status']=='D' for q in entries)})
gitdocs=[]
for q in load(E/'EIGHT_SOURCE_REFRESH.json'):
 if '/research/' not in q['path']:continue
 rel=str(Path(q['path']).relative_to(P));r=subprocess.run(['git','cat-file','blob',obj['expected_oid']+':'+rel],cwd=P,env=env,capture_output=True,timeout=20)
 gitdocs.append({'path':rel,'git_read_exit':r.returncode,'capture_blob_bytes':len(r.stdout),'capture_blob_sha256':hashlib.sha256(r.stdout).hexdigest(),'matches_current_and_prior':r.returncode==0 and hashlib.sha256(r.stdout).hexdigest()==q['sha256']==q['expected_sha256']})
dump('RESEARCH_CAPTURE_BLOB_HASHES.json',gitdocs)
d['research_capture_blob_matches']=gitdocs;d['capture_tree_all_extra_entries']=all(q['reverse_status']=='D' for q in entries);d['capture_tree_extra_entries_count']=len(entries)
(O/'GIT_REF_DELTA_EVIDENCE.json').write_text(json.dumps(d,indent=2)+'\n')
# Recheck only historical control receipts already explicitly enumerated; no new full inventory.
checks=[]
for q in load(A/'evidence/V7_HISTORICAL_RECEIPTS_UNCHANGED_FINAL.json')['checks']:
 p=Path(q['path']);h=sha(p);checks.append({'path':str(p),'expected_sha256':q.get('expected_sha256') or q['sha256'],'actual_sha256':h,'pass':h==(q.get('expected_sha256') or q['sha256'])})
dump('V7_RECEIPTS_CURRENT_CHECK.json',{'count':len(checks),'passed':sum(q['pass'] for q in checks),'checks':checks})
# Preserve 13 verified payload receipts without downloading or duplicating payloads.
lf=list(csv.DictReader((A/'LFS_REMOTE_PAYLOAD_VERIFICATION.csv').open()));verified=[q for q in lf if q['integrity']=='PASS'];dump('LFS_THIRTEEN_PRESERVED_RECEIPTS.json',{'source':str(A/'LFS_REMOTE_PAYLOAD_VERIFICATION.csv'),'source_sha256':sha(A/'LFS_REMOTE_PAYLOAD_VERIFICATION.csv'),'count':len(verified),'bytes':sum(int(q['expected_bytes']) for q in verified),'receipts':verified,'new_downloads':0,'scope':'Original full-byte observations retained; prior sealed scratch bytes also verified under 84-entry manifest. No new remote readback.'})
print(json.dumps({'historical_core':d['historical_core_equal'],'fresh_core':d['fresh_core_equal'],'nonaux_delta':d['non_auxiliary_local_delta'],'remote_delta':d['live_remote_delta'],'retaining_refs':len(d['current_existing_target_refs']),'capture_extra_entries':len(entries),'all_extra':d['capture_tree_all_extra_entries'],'research_blob_matches':sum(q['matches_current_and_prior'] for q in gitdocs),'v7_seals':[sum(q['pass'] for q in checks),len(checks)]},indent=2))
