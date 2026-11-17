# Write a receipt for a checkpoint whose push landed but whose verification step failed (e.g. fetch exit 128). Args: X commit
import json,sys,subprocess,hashlib,datetime
from pathlib import Path
X,commit=sys.argv[1],sys.argv[2];p=Path.cwd();repo='/Users/ghilmankhan/workprojects/youtube-intelligence-os'
run=lambda *a:subprocess.check_output(a,cwd=repo,text=True).strip()
d=json.loads((p/f'evidence/{X}_PREPARED.json').read_text())
c=run('git','cat-file','-p',commit).splitlines();assert c[0]=='tree '+d['tree'] and c[1]=='parent '+d['base'],c[:2]
remote=run('gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/ref/heads/research/barely-evolved-visual-forensics','--jq','.object.sha')
bad=[]
for path in d['paths']:
    blob=subprocess.check_output(['git','show',f'{commit}:{path}'],cwd=repo)
    rel=path.split('/uPQcyookL0Y/',1)[-1] if '/uPQcyookL0Y/' in path else path.split('/',5)[-1]
    if hashlib.sha256(blob).hexdigest()!=hashlib.sha256((p/rel).read_bytes()).hexdigest():bad.append(path)
rec={'checkpoint':X,'parent_sha':d['base'],'published_sha':commit,'authenticated_remote_sha_at_receipt':remote,'tree':d['tree'],'published_paths':len(d['paths']),'readback_sha256_mismatches':bad,'seal_entries':d['seal_entries'],'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'media_published':False,'pr':'none','note':'push succeeded; be_push_checkpoint verification fetch failed (exit 128, network); receipt written afterwards by be_receipt_existing.py after fetch + tree/parent check + blob readback'}
(p/f'evidence/{X}_PUBLICATION_RECEIPT.json').write_text(json.dumps(rec,indent=1));print(json.dumps(rec,indent=1))
open('/Users/ghilmankhan/YIOS-local-audits/barely-evolved/BE_OPS_LOG.txt','a').write(f"{rec['utc']} {p.name} checkpoint {X} published {commit} (receipt post-hoc after fetch failure); readback mismatches {len(bad)}\n")
