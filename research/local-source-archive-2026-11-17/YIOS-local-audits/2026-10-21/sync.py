import subprocess,json,pathlib
A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21')
def g(*a):return subprocess.check_output(['git',*a],text=True).strip()
bs=json.loads((A/'branches-before.json').read_text()); live={l.split()[1]:l.split()[0] for l in (A/'github-before.txt').read_text().splitlines()}; results=[]
for b in bs:
 b=b.copy();u=b['upstream'];old=b['sha'];b['final']=old
 if not u: b.update(outcome='NO_UPSTREAM_PRESERVED',ahead=None,behind=None)
 elif 'refs/heads/'+u.removeprefix('origin/') not in live:b.update(outcome='MISSING_GITHUB_UPSTREAM',ahead=None,behind=None)
 else:
  remote=g('rev-parse',u);b['github_sha']=remote;a,z=map(int,g('rev-list','--left-right','--count',b['branch']+'...'+u).split()); b.update(ahead=a,behind=z)
  if not a and not z:b['outcome']='ALREADY_SYNCED'
  elif b['branch']=='research/finance-economics-intelligence':b['outcome']='BLOCKED_DIRTY_MACHINE_B_OWNED'
  elif b['branch']=='research/casually-finance-editing-forensics':b['outcome']='BLOCKED_ACTIVE_OWNER'
  elif a and z:b['outcome']='DIVERGED_PRESERVED'
  elif a:b['outcome']='LOCAL_AHEAD_PRESERVED'
  else:
   # Only unoccupied local replica refs; no checkout/production changes, expected-old CAS.
   wt=g('worktree','list','--porcelain');assert 'branch refs/heads/'+b['branch']+'\n' not in wt+'\n'
   assert g('rev-parse','refs/heads/'+b['branch'])==old
   subprocess.run(['git','merge-base','--is-ancestor',old,remote],check=True)
   assert not list(pathlib.Path('.git').rglob('*.lock'))
   subprocess.run(['git','update-ref','-m','Machine A audited fast-forward from origin','refs/heads/'+b['branch'],remote,old],check=True)
   assert g('rev-parse',b['branch'])==remote
   b.update(final=remote,outcome='FAST_FORWARDED',ahead=0,behind=0)
 results.append(b)
(A/'branches-after.json').write_text(json.dumps(results,indent=2))
for b in results: print(b['branch'],b['outcome'],b.get('ahead'),b.get('behind'))
