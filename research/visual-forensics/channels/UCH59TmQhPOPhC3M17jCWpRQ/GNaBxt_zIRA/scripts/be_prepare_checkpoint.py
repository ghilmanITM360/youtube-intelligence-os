# Prepare a checkpoint tree via external GIT_INDEX_FILE (no checkout). Args: X base prefix_video prev_seal|- json_patterns json_seal_globs
import json,sys,hashlib,subprocess,os
from pathlib import Path
X,base,vid,prev,pats,sealg=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],json.loads(sys.argv[5]),json.loads(sys.argv[6])
p=Path.cwd();repo='/Users/ghilmankhan/workprojects/youtube-intelligence-os';prefix=f'research/visual-forensics/channels/UCH59TmQhPOPhC3M17jCWpRQ/{vid}/'
run=lambda *a,**k:subprocess.check_output(a,cwd=repo,text=True,**k).strip()
sel=sorted({x for pt in pats for x in p.glob(pt) if x.is_file() and not x.suffix in('.png','.jpg','.mp4','.wav','.index')})
files=set(sel);changed=[]
if prev!='-':
    for line in (p/prev).read_text().splitlines():
        h,f=line.split(None,1);q=Path(f);files.add(q)
        if hashlib.sha256(q.read_bytes()).hexdigest()!=h:changed.append(str(q.relative_to(p)))
    files.add(p/prev)
for g in sealg:files.update(x for x in p.glob(g) if x.is_file())
seal=p/f'EVIDENCE_SHA256SUMS_checkpoint_{X}';seal.write_text(''.join(hashlib.sha256(x.read_bytes()).hexdigest()+'  '+str(x)+'\n' for x in sorted(files)));sel.append(seal)
assert run('git','ls-remote','origin','refs/heads/research/barely-evolved-visual-forensics').split()[0]==base,'remote moved'
idx=p/f'evidence/{X}_publication.index';p.joinpath('evidence').mkdir(exist_ok=True);assert not idx.exists();env=dict(os.environ,GIT_INDEX_FILE=str(idx));run('git','read-tree',base,env=env)
for f in sel:run('git','update-index','--add','--cacheinfo','100644',run('git','hash-object','-w',str(f)),prefix+str(f.relative_to(p)),env=env)
tree=run('git','write-tree',env=env);paths=run('git','diff','--name-only',base,tree).splitlines()
assert all(x.startswith(prefix) for x in paths) and not any(x.endswith(('.png','.jpg','.mp4','.wav')) for x in paths)
(p/f'evidence/{X}_INTENDED_DIFF.txt').write_text(run('git','diff','--stat',base,tree)+'\n')
(p/f'evidence/{X}_PREPARED.json').write_text(json.dumps({'base':base,'tree':tree,'seal_entries':len(files),'paths':paths,'checkout_head':run('git','rev-parse','HEAD'),'changed_since_prev_seal':changed},indent=1))
print('changed_since_prev',changed);print('seal',len(files),'paths',len(paths),'tree',tree)
