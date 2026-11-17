import subprocess,os,json,hashlib,time
from pathlib import Path
O=Path(__file__).parent;P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1')
def run(n,c,t=50):
 try:
  x=subprocess.run(c,cwd=P,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=t);(O/'evidence'/(n+'.txt')).write_bytes(x.stdout);(O/'evidence'/(n+'.meta.json')).write_text(json.dumps({'cmd':c,'exit':x.returncode,'stderr':x.stderr.decode(errors='replace')}));print(n,x.returncode,len(x.stdout),flush=True);return x.stdout
 except Exception as e:(O/'evidence'/(n+'.meta.json')).write_text(json.dumps({'cmd':c,'error':str(e)}));return b''
run('GIT_TRACKED_INDEX',['git','ls-files','--stage','-z'])
run('GIT_IGNORED',['git','ls-files','--others','--ignored','--exclude-standard','-z'])
run('GIT_UNTRACKED',['git','ls-files','--others','--exclude-standard','-z'])
run('LFS_HEAD',['git','lfs','ls-files','--long','--size'])
run('LFS_ALL',['git','lfs','ls-files','--all','--long','--size'],100)
run('LOCAL_UNPUBLISHED_COMMITS',['git','log','--branches','--not','--remotes','--format=%H %ad %s','--date=iso-strict'])
run('STASH_CONTENT',['git','stash','show','--name-status','--include-untracked','stash@{0}'])
run('PR36',['gh','pr','view','36','--repo','ghilmanITM360/youtube-intelligence-os','--json','number,title,state,isDraft,headRefName,headRefOid,baseRefName,baseRefOid,url,updatedAt'])
run('PR44',['gh','pr','view','44','--repo','ghilmanITM360/youtube-intelligence-os','--json','number,title,state,isDraft,headRefName,headRefOid,baseRefName,baseRefOid,url,updatedAt'])
refs=[]
for line in (O/'evidence/LIVE_REMOTE_REFS.txt').read_text().splitlines():
 sha,ref=line.split('\t');refs.append((sha,ref))
# Authenticated GitHub recursive API trees; no Git fetch and no writes to object database.
for label,ref in [('MAIN','refs/heads/main'),('FINANCE','refs/heads/research/finance-economics-intelligence'),('WHATIF','refs/heads/codex/what-if-archive-main-integration'),('WHATIF_ORIGINAL','refs/heads/research/what-if-brain-preservation-batch1'),('VISUAL','refs/heads/research/casually-finance-editing-forensics')]:
 sha=dict((r,s) for s,r in refs)[ref]
 run('REMOTE_TREE_'+label,['gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/trees/'+sha+'?recursive=1'],100)
 run('REMOTE_COMMIT_'+label,['gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/commits/'+sha])
# Local trees at every live advertised SHA already present; no lazy fetch.
for sha,ref in refs:
 p=subprocess.run(['git','cat-file','-e',sha+'^{tree}'],cwd=P,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if p.returncode==0:
  run('LOCAL_TREE_'+sha,['git','ls-tree','-r','--long',sha])
