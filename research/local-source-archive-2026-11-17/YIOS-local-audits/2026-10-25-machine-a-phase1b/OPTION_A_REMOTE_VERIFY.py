import pathlib,subprocess as s,json,hashlib,base64,concurrent.futures,datetime
D=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-25-machine-a-phase1b');P=D/'OPTION_A_EXECUTION_RECEIPT.json';x=json.loads(P.read_text());head=x['documentation_repair_commit'];repo='repos/ghilmanITM360/youtube-intelligence-os/'
def api(path):return json.loads(s.check_output(['gh','api',repo+path]))
def g(*a):return s.check_output(['git',*a]).decode().strip()
ref=api('git/ref/heads/codex/what-if-archive-main-integration');assert ref['object']['sha']==head
commits=[];expected=head
while expected!='08e719264e31ecd82de24f8eeb8f065c08359fe5':
 c=api('git/commits/'+expected);assert len(c['parents'])==1;parent=c['parents'][0]['sha'];assert parent==g('rev-parse',expected+'^');commits.append({'sha':expected,'parent':parent,'tree':c['tree']['sha']});expected=parent
assert len(commits)==6
tr=api('git/trees/'+commits[0]['tree']+'?recursive=1');assert not tr['truncated'];tree={r['path']:r for r in tr['tree']}
paths=[z.split('\t')[-1] for z in x['local_validation']['paths']];expected_files={p:pathlib.Path(p).read_bytes() for p in paths};checks=[]
def retrieve(p):
 row=tree[p];assert row['type']=='blob';v=api('git/blobs/'+row['sha']);assert v['encoding']=='base64';b=base64.b64decode(v['content']);assert b==expected_files[p],p
 assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['sha']
 return {'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':row['sha'],'status':'REMOTE_RETRIEVED','endpoint':'git/blobs/'+row['sha'],'commit':head}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 for row in pool.map(retrieve,paths):
  checks.append(row)
  if len(checks)%50==0:print('Retrieved and verified',len(checks),'/',len(paths),flush=True)
  if len(checks)%25==0:(D/'OPTION_A_REMOTE_PARTIAL.json').write_text(json.dumps({'commit':head,'files':checks},indent=2))
research=[v for v in checks if v['path'].startswith('research/')];assert len(research)==397 and sum(v['bytes'] for v in research)==8221384
ref2=api('git/ref/heads/codex/what-if-archive-main-integration');assert ref2['object']['sha']==head
x['remote_verification']={'commit':head,'ref_before':ref['object']['sha'],'ref_after':ref2['object']['sha'],'commits':commits,'tree_complete':True,'files':checks,'retrieved_count':len(checks),'research_count':397,'research_bytes':8221384,'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
x['publication_status']=['VERIFIED','COMMITTED','PUSHED','REMOTE_RETRIEVED'];P.write_text(json.dumps(x,indent=2));print('REMOTE PASS all400 paths,397 research files8221384bytes,six exact remote parents; ref unchanged',head,flush=True)
