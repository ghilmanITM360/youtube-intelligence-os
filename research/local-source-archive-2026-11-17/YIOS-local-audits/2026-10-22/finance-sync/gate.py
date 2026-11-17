import subprocess,json,os
from pathlib import Path
out=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-22/finance-sync')
def g(*a):return subprocess.check_output(['git',*a]).decode().strip()
a=json.loads((out/'before.json').read_text())
assert g('rev-parse','HEAD')==a['head']=='d41a5774f1381a21022b70f02d206303195be3a7'
assert g('branch','--show-current')=='research/finance-economics-intelligence'
assert not g('status','--porcelain','--untracked-files=no')
assert g('rev-list','--left-right','--count','HEAD...@{upstream}').split()==['0','5']
subprocess.run(['git','merge-base','--is-ancestor','HEAD','@{upstream}'],check=True)
remote=g('rev-parse','@{upstream}')
pr=json.loads(subprocess.check_output(['gh','pr','view','36','--json','state,headRefOid']))
assert remote==pr['headRefOid'] and pr['state']=='OPEN'
changed=g('diff','--name-only','HEAD','@{upstream}').splitlines()
local=list(a['untracked'])+list(a['ignored'])
collisions=[(p,q) for p in changed for q in local if p==q or p.startswith(q+'/') or q.startswith(p+'/')]
assert not collisions,collisions
for p in changed:
 f=Path(p)
 for parent in f.parents:
  assert not parent.is_symlink(),str(parent)
assert not list(Path('.git').glob('*.lock'))
record={'start':a['head'],'target':remote,'pr':pr,'changed_paths':changed,'collisions':collisions,'commits':g('log','--reverse','--format=%H %s','HEAD..@{upstream}')}
(out/'gates.json').write_text(json.dumps(record,indent=2))
print('PASS: ancestry, clean index/tree, 0 local Finance commits, 27 paths no collisions, PR alignment, no locks/symlink parents'); print(record['target'])
