import pathlib,subprocess,json
A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21')
reachable={l.split()[0]for l in subprocess.check_output(['git','rev-list','--objects','--all','--missing=print'],text=True).splitlines()}
idx=next(A.glob('unreachable-recovery-*.idx'))
objects=[l.split()[0]for l in subprocess.check_output(['git','verify-pack','-v',str(idx)],text=True).splitlines()if len(l.split())>=5 and len(l.split()[0])==40]
unique=set(objects)-reachable
# Include reflog-only object graphs as well, retaining records independently of reflog expiration.
reflog={l.split()[0]for l in subprocess.check_output(['git','rev-list','--objects','--reflog','--missing=print'],text=True).splitlines()}
unique|=reflog-reachable
p=subprocess.run(['git','pack-objects',str(A/'recovery-unique-objects')],input='\n'.join(sorted(unique))+'\n',text=True,capture_output=True,check=True)
newidx=A/('recovery-unique-objects-'+p.stdout.strip()+'.idx');subprocess.run(['git','verify-pack',str(newidx)],check=True)
check={l.split()[0]for l in subprocess.check_output(['git','verify-pack','-v',str(newidx)],text=True).splitlines()if len(l.split())>=5 and len(l.split()[0])==40};assert unique==check
(A/'preserved-recovery-object-ids.txt').write_text('\n'.join(sorted(unique))+'\n')
# Remove only this audit's redundant initial archive after compact archive verification.
removed=[]
for f in A.glob('unreachable-recovery-*'):
 removed.append(dict(path=str(f),bytes=f.stat().st_size));f.unlink()
(A/'recovery-preservation.json').write_text(json.dumps(dict(unique_objects=len(unique),compact_index=str(newidx),redundant_audit_archives_replaced=removed,repository_objects_untouched=True),indent=2));print('preserved',len(unique),'unique/reflog objects')
