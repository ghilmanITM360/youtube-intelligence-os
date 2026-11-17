# For every remote branch tip: find LFS-tracked paths, read pointers, ask GitHub's LFS batch API whether payloads are downloadable.
import subprocess,json,fnmatch,base64,re,urllib.request,sys
from pathlib import Path
repo=str(Path.home()/'workprojects/youtube-intelligence-os');S=Path(sys.argv[0]).parent
run=lambda *a:subprocess.run(a,cwd=repo,capture_output=True,text=True)
heads=[l.split('\t') for l in (S/'ls_remote_heads.txt').read_text().splitlines()]
obj={};perbranch={}
for sha,ref in heads:
    b=ref.replace('refs/heads/','')
    ga=run('git','show',f'{sha}:.gitattributes')
    pats=[l.split()[0] for l in ga.stdout.splitlines() if 'filter=lfs' in l and not l.startswith('#')] if ga.returncode==0 else []
    if not pats: perbranch[b]={'patterns':[], 'paths':[]};continue
    files=run('git','ls-tree','-r','--name-only',sha).stdout.splitlines()
    hit=[f for f in files if any(fnmatch.fnmatch(f,p) or fnmatch.fnmatch(f.split('/')[-1],p) for p in pats)]
    rows=[]
    for f in hit:
        c=subprocess.run(['git','cat-file','-p',f'{sha}:{f}'],cwd=repo,capture_output=True).stdout[:400].decode('latin1')
        m=re.search(r'oid sha256:([0-9a-f]{64})\s+size (\d+)',c)
        if m: obj[m[1]]=int(m[2]);rows.append((f,m[1],int(m[2])))
        else: rows.append((f,None,len(c)))
    perbranch[b]={'patterns':pats,'paths':rows}
tok=subprocess.check_output(['gh','auth','token'],text=True).strip()
res={}
o=list(obj.items())
for i in range(0,len(o),50):
    body=json.dumps({'operation':'download','transfers':['basic'],'objects':[{'oid':k,'size':v} for k,v in o[i:i+50]]}).encode()
    rq=urllib.request.Request('https://github.com/ghilmanITM360/youtube-intelligence-os.git/info/lfs/objects/batch',data=body,headers={'Accept':'application/vnd.git-lfs+json','Content-Type':'application/vnd.git-lfs+json','Authorization':'Basic '+base64.b64encode(f'x-access-token:{tok}'.encode()).decode()})
    r=json.load(urllib.request.urlopen(rq))
    for x in r['objects']: res[x['oid']]={'download':'download' in x.get('actions',{}),'error':x.get('error')}
for b,d in sorted(perbranch.items()):
    if not d['paths'] and not d['patterns']: continue
    bad=[p for p in d['paths'] if not p[1] or not res.get(p[1],{}).get('download')]
    print(b,'lfs_paths',len(d['paths']),'not_downloadable',[(p[0],p[1] and p[1][:10],p[1] and res.get(p[1])) for p in bad])
print('no LFS patterns on',sum(1 for d in perbranch.values() if not d['patterns']),'branches of',len(perbranch))
print('unique objects',len(o),'downloadable',sum(1 for v in res.values() if v['download']),{k[:12]:v for k,v in obj.items()})
json.dump({'per_branch':perbranch,'objects':res},open(S/'lfs_audit.json','w'),indent=1)
