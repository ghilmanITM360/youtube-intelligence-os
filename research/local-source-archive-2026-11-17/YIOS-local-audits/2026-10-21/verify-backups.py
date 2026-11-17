import pathlib,json,hashlib
A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21'); roots=[pathlib.Path.cwd(),pathlib.Path('/Users/ghilmankhan/workprojects/yio-cf-editing-forensics')];n=0
for i,r in enumerate(roots):
 d=json.loads((A/f'worktree-{i}-files.json').read_text())
 for cat in ['modified','untracked']:
  for x in d[cat]:
   q=A/'preserved-files'/f'worktree-{i}'/pathlib.Path(x['path']).relative_to(r)
   assert hashlib.sha256(q.read_bytes()).hexdigest()==x['sha256'],str(q)
   n+=1
(A/'backup-verification.txt').write_text(f'{n} preserved files verified SHA-256\n');print(n)
