import json,subprocess,os,collections
from pathlib import Path
O=Path(__file__).parent;R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1')
hashes=json.loads((O/'hashes.json').read_text());wanted=collections.defaultdict(list)
for p,x in hashes.items():wanted[x['git_blob_sha1']].append(p)
results={};pub=collections.defaultdict(list)
for line in (O/'live_refs.txt').read_text().splitlines():
 sha,ref=line.split('\t');p=subprocess.run(['git','ls-tree','-r',sha],cwd=R,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 results[ref]={'sha':sha,'returncode':p.returncode,'stderr':p.stderr.decode(),'blob_count':0}
 if p.returncode:continue
 for ln in p.stdout.decode().splitlines():
  meta,path=ln.split('\t',1);mode,typ,blob=meta.split()
  if typ!='blob':continue
  results[ref]['blob_count']+=1
  if blob in wanted:
   for local in wanted[blob]:pub[local].append({'ref':ref,'sha':sha,'path':path,'git_blob_sha1':blob})
(O/'branch-tree-coverage.json').write_text(json.dumps(results,indent=2))
(O/'all-live-branch-matches.json').write_text(json.dumps(pub,indent=2))
print('refs',len(results),'unreadable',[(k,v['stderr'][:80]) for k,v in results.items() if v['returncode']])
for name in ['video data of what if','yios-recovery-status','yio-cf-editing-forensics-local-evidence','yios-visual-forensics-install-candidate-2026-10-24','YIOS-local-audits','yios-git-recovery']:
 a=[p for p in hashes if '/'+name+'/' in p];b=[p for p in a if p in pub];print(name,'hashed',len(a),'published_match',len(b),sum(hashes[p]['bytes'] for p in b))
