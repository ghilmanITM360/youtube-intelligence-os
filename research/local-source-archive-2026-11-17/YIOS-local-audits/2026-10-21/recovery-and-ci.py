import pathlib,subprocess,json,concurrent.futures
A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21')
# Preserve dangling objects, without changing repository refs or garbage collection.
ids=[l.split()[2]for l in (A/'fsck.txt').read_text().splitlines()if l.startswith('dangling ')]
p=subprocess.run(['git','pack-objects','--revs',str(A/'unreachable-recovery')],input='\n'.join(ids)+'\n',text=True,capture_output=True,check=True)
(A/'recovery-pack.txt').write_text(p.stdout)
for idx in A.glob('unreachable-recovery-*.idx'):
 v=subprocess.run(['git','verify-pack',str(idx)],capture_output=True,text=True);assert v.returncode==0;print('recovery pack verified',idx.name)
p=subprocess.run(['git','bundle','create',str(A/'local-only-commits.bundle'),'--all','--not','--remotes'],capture_output=True,text=True);(A/'bundle-create.txt').write_text(p.stdout+p.stderr);assert p.returncode==0
p=subprocess.run(['git','bundle','verify',str(A/'local-only-commits.bundle')],capture_output=True,text=True);(A/'bundle-verify.txt').write_text(p.stdout+p.stderr);assert p.returncode==0
checks=[]
for pr in json.loads((A/'prs.json').read_text()):
 d=json.loads((A/f'pr-{pr["number"]}-checks.json').read_text())
 for c in d['checks'].get('check_runs',[]):
  if c.get('conclusion')=='failure':checks.append((pr['number'],c['id']))
def one(pair):
 n,i=pair;p=subprocess.run(['gh','api',f'repos/ghilmanITM360/youtube-intelligence-os/check-runs/{i}/annotations'],capture_output=True,text=True);return dict(pr=n,annotations=json.loads(p.stdout)if p.returncode==0 else p.stderr)
with concurrent.futures.ThreadPoolExecutor(max_workers=4)as ex:out=list(ex.map(one,checks))
(A/'ci-failure-annotations.json').write_text(json.dumps(out,indent=2))
for x in out:print(x['pr'],[a['message']for a in x['annotations']])
