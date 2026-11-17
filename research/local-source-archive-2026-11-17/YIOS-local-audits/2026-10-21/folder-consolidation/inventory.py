import os, pathlib, hashlib, json, subprocess, collections
base=pathlib.Path('/Users/ghilmankhan/workprojects'); out=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21/folder-consolidation')
names=['yio-cf-editing-forensics-local-evidence','yio-cf-editing-forensics','calf-pain-pad-explainer','yios-recovery-status']
allrows=[]; summary={}
for name in names:
 root=base/name; rows=[]
 for d,dirs,files in os.walk(root,followlinks=False):
  for f in files:
   p=pathlib.Path(d)/f; s=p.lstat(); r={'folder':name,'path':str(p.relative_to(root)),'size':s.st_size,'mtime_ns':s.st_mtime_ns,'mode':s.st_mode}
   if p.is_symlink():r['symlink']=os.readlink(p)
   else:
    h=hashlib.sha256()
    with p.open('rb') as stream:
     for block in iter(lambda:stream.read(4*1024*1024),b''):h.update(block)
    r['sha256']=h.hexdigest()
    if p.stat().st_mtime_ns!=s.st_mtime_ns: raise RuntimeError('Changed '+str(p))
   rows.append(r)
 summary[name]={'files':len(rows),'bytes':sum(r['size'] for r in rows),'du_k':subprocess.check_output(['du','-sk',str(root)],text=True).split()[0],'top':dict(collections.Counter({k:sum(r['size'] for r in rows if r['path'].split('/')[0]==k) for k in set(r['path'].split('/')[0] for r in rows)}).most_common(15))}
 allrows+=rows
(out/'inventory.json').write_text(json.dumps(allrows,indent=2));(out/'summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
