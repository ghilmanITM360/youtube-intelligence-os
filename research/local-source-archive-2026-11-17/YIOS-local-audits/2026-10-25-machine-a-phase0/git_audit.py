import subprocess,os,json
from pathlib import Path
out=Path(__file__).parent
repo=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1')
cmds={
'status':['git','status','--porcelain=v2','--branch'],
'refs':['git','show-ref'],
'worktrees':['git','worktree','list','--porcelain'],
'remotes':['git','remote','-v'],
'live_refs':['git','ls-remote','--heads','--tags','origin'],
'live_pr_ref':['git','ls-remote','origin','refs/pull/36/head','refs/pull/36/merge'],
'stashes':['git','stash','list','--format=%H %gd %s'],
'git_config_storage':['git','config','--get-regexp','remote\..*\.(promisor|partialclonefilter)|extensions\..*|core\.repositoryformatversion'],
'pr36':['gh','pr','view','36','--repo','ghilmanITM360/youtube-intelligence-os','--json','number,title,state,isDraft,headRefName,headRefOid,baseRefName,baseRefOid,url,updatedAt,body'],
'process_names':['ps','-axo','pid,ppid,comm'],
'disk':['df','-k',str(repo)],
'head_tree':['git','ls-tree','-r','--long','HEAD'],
'live_head_tree':['gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/trees/1adb8129f689207552f0838414e5823e4255bde1?recursive=1'],
'live_main_tree':['gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/trees/08e719264e31ecd82de24f8eeb8f065c08359fe5?recursive=1'],
'lfs':['git','lfs','ls-files','--long','--size'],
}
for name,cmd in cmds.items():
 try:
  p=subprocess.run(cmd,cwd=repo,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=40)
  # Avoid retaining unrelated process names; preserve only YIOS-relevant agent process names.
  stdout=p.stdout.decode(errors='replace')
  if name=='process_names':stdout='\n'.join(x for x in stdout.splitlines() if any(s in x.lower() for s in ['claude','codex','python','ffmpeg','git','node']))
  (out/(name+'.txt')).write_text(stdout)
  (out/(name+'.meta.json')).write_text(json.dumps({'command':cmd,'returncode':p.returncode,'stderr':p.stderr.decode(errors='replace')}))
  print(name,p.returncode,len(stdout))
 except Exception as ex:print(name,str(ex))
