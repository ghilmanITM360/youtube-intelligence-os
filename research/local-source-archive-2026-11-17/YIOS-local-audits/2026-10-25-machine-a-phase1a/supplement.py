from pathlib import Path
import json,hashlib,subprocess,os,base64,sqlite3,importlib.metadata,collections,csv
O=Path(__file__).parent;R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');W=R.parent/'video data of what if';env={**os.environ,'GIT_OPTIONAL_LOCKS':'0','GIT_NO_LAZY_FETCH':'1','GIT_TERMINAL_PROMPT':'0'}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(n,x):(O/n).write_text(json.dumps(x,indent=2))
# Independent GitHub retrieval on current advertised refs.
head=json.loads((O/'live-snapshot.json').read_text())['receipts']['head']['stdout'].strip();protected='090f84b3292a3b6c6e94653a6ef1867726e4ebdd';checks=[]
for tip,path in [(head,'research/finance-economics-intelligence/FINANCE_WRITER_OWNERSHIP.md'),(head,'data/manifests/what-if-forensic-source-v1.json'),(head,'data/intelligence/channels/CH-000004/forensic-observation-index-v1.json'),(protected,'research/casually-finance-editing-forensics/scripts/forensic_features.py'),(protected,'research/casually-finance-editing-forensics/SOURCE_MEDIA_INVENTORY.csv')]:
 blob=subprocess.check_output(['git','rev-parse',tip+':'+path],cwd=R,env=env,text=True).strip();local=subprocess.check_output(['git','show',tip+':'+path],cwd=R,env=env)
 p=subprocess.run(['gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/blobs/'+blob],env=env,capture_output=True,text=True);rec={'tip':tip,'path':path,'blob':blob,'code':p.returncode}
 if p.returncode==0:
  d=json.loads(p.stdout);remote=base64.b64decode(d['content']);rec.update(bytes=len(remote),retrieved_sha256=hashlib.sha256(remote).hexdigest(),local_blob_sha256=hashlib.sha256(local).hexdigest(),status='PASS' if remote==local else 'FAIL')
 else:rec.update(status='REMOTE_UNVERIFIED',error=p.stderr)
 checks.append(rec)
dump('fresh-github-retrievals.json',checks)
# Explicitly readonly immutable catalog identity checks.
p=R/'data/catalog/youtube_inventory.db';c=sqlite3.connect(p.as_uri()+'?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
cat={'channel':dict(c.execute("select * from channels where channel_id='CH-000004'").fetchone()),'video_count':c.execute("select count(*) from videos where channel_id='CH-000004'").fetchone()[0],'held_ids_present':{i:c.execute('select count(*) from videos where youtube_video_id=?',(i,)).fetchone()[0] for i in ['X97DDWvxaqQ','9VG0yqq_PHM']},'access':'mode=ro&immutable=1'};c.close();dump('catalog-identity-receipt.json',cat)
releases=[]
for root in [W/'production_intelligence_brain',W/'releases/production_intelligence_brain-v1.0.0']:
 d=json.loads((root/'RELEASE_MANIFEST.json').read_text())
 for r in d['files']:
  p=root/r['relative_path'];actual=sha(p);releases.append({'manifest':str(root/'RELEASE_MANIFEST.json'),'path':str(p),'expected':r['sha256'],'actual':actual,'status':'PASS' if actual==r['sha256'] and p.stat().st_size==r['size_bytes'] else 'FAIL'})
dump('what-if-release-manifest-verification.json',releases)
# Source media for accepted 001/002 and partial003 by old explicit verification rows.
old=list(csv.DictReader(open(O.parent/'2026-10-25-machine-a-phase0/manifest-checks.csv')));v=[]
for r in old:
 if r['file'].endswith('.mp4') and any(t in r['file'] for t in ['Why The Dumbest Investors','Housing Crisis','Brace For Impact']):
  p=Path(r['file']);actual=sha(p) if p.is_file() else None;v.append({**r,'current_sha256':actual,'current_status':'PASS' if actual==r['expected'] else 'FAIL'})
dump('video-source-rechecks.json',v)
# Current package metadata, NOT attribution to original execution.
versions={}
for n in ['numpy','Pillow','openai-whisper','torch']:
 try:versions[n]=importlib.metadata.version(n)
 except importlib.metadata.PackageNotFoundError:versions[n]='NOT_AVAILABLE_TO_THIS_PYTHON'
dump('current-package-metadata.json',{'python':__import__('sys').version,'packages':versions,'historical_execution_version_proven':False})
# Recheck installed skill against Phase0, no installation invocation.
prior=json.loads((O.parent/'2026-10-25-machine-a-phase0/skill-comparison.json').read_text());skill=[]
for root,files in prior.items():
 if not isinstance(files,dict):continue
 for rel,r in files.items():
  if not isinstance(r,dict) or 'sha256' not in r:continue
  p=Path(root)/rel
  if p.is_file():skill.append({'path':str(p),'expected':r['sha256'],'actual':sha(p),'status':'PASS' if sha(p)==r['sha256'] else 'CHANGED'})
dump('skill-current-verification.json',skill)
print('retrieved',collections.Counter(r['status'] for r in checks),'release',collections.Counter(r['status'] for r in releases),'sources',len(v),'skills',collections.Counter(r['status'] for r in skill),'catalog',cat['video_count'])
