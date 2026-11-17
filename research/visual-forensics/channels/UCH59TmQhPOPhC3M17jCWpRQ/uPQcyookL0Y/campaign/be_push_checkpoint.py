# Push a prepared checkpoint (evidence/<X>_PREPARED.json) by commit-tree + normal push; verify remote and read back every published blob.
import json,sys,subprocess,hashlib,datetime
from pathlib import Path
X,msg=sys.argv[1],sys.argv[2];p=Path.cwd();repo='/Users/ghilmankhan/workprojects/youtube-intelligence-os';ref='refs/heads/research/barely-evolved-visual-forensics'
run=lambda *a,**k:subprocess.check_output(a,cwd=repo,text=True,**k).strip()
d=json.loads((p/f'evidence/{X}_PREPARED.json').read_text())
assert run('git','ls-remote','origin',ref).split()[0]==d['base'],'remote parent moved: reconcile, do not force'
commit=run('git','commit-tree',d['tree'],'-p',d['base'],input=msg+'\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n')
run('git','push','origin',commit+':'+ref)
remote=run('gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/ref/heads/research/barely-evolved-visual-forensics','--jq','.object.sha');assert remote==commit,remote
run('git','fetch','origin','research/barely-evolved-visual-forensics')
bad=[]
for path in d['paths']:
    blob=subprocess.check_output(['git','show',f'{commit}:{path}'],cwd=repo)
    rel=path.split('/uPQcyookL0Y/',1)[-1] if '/uPQcyookL0Y/' in path else path.split('/',5)[-1]
    if rel.startswith('campaign/'):local=p.parent/rel.split('/',1)[1]
    else:local=p/rel
    if not local.exists():local=Path(d.get('local_map',{}).get(path,''))
    if hashlib.sha256(blob).hexdigest()!=hashlib.sha256(local.read_bytes()).hexdigest():bad.append(path)
rec={'checkpoint':X,'parent_sha':d['base'],'published_sha':commit,'authenticated_remote_sha':remote,'tree':d['tree'],'published_paths':len(d['paths']),'readback_sha256_mismatches':bad,'seal_entries':d['seal_entries'],'canonical_checkout_head':run('git','rev-parse','HEAD'),'canonical_branch':run('git','branch','--show-current'),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'media_published':False,'pr':'none'}
(p/f'evidence/{X}_PUBLICATION_RECEIPT.json').write_text(json.dumps(rec,indent=1));print(json.dumps(rec,indent=1))
open('/Users/ghilmankhan/YIOS-local-audits/barely-evolved/BE_OPS_LOG.txt','a').write(f"{rec['utc']} {p.name} checkpoint {X} published {commit}; remote verified; readback mismatches {len(bad)}; lock held by {[l for l in open('/Users/ghilmankhan/YIOS-local-audits/barely-evolved/.be_writer_lock/owner') if l.startswith('session')][-1].split()[1]}\n")
