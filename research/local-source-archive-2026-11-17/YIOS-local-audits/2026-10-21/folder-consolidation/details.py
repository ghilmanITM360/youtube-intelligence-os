import pathlib,json,hashlib,collections,csv,subprocess,os
out=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21/folder-consolidation');audit=out.parent;base=pathlib.Path('/Users/ghilmankhan/workprojects');rows=json.loads((out/'inventory.json').read_text());byhash=collections.defaultdict(list)
for r in rows:
 if 'sha256'in r:byhash[r['sha256']].append(r)
external=[]
for manifest in ['external-YIOS-Production-Library.json','external-CasuallyFinance-Forensic-Research.json']:
 for x in json.loads((audit/manifest).read_text()):
  size=x.get('bytes');candidates=[r for r in rows if r['size']==size and r['folder']!='yio-cf-editing-forensics']
  if not candidates:continue
  p=pathlib.Path(x['path'])
  if p.is_file()and not p.is_symlink():
   h=hashlib.sha256(p.read_bytes()).hexdigest()
   for r in candidates:
    if r.get('sha256')==h:external.append({'folder':r['folder'],'path':r['path'],'backup':str(p),'sha256':h})
(out/'external-duplicates.json').write_text(json.dumps(external,indent=2));print('verified external duplicates',collections.Counter(r['folder']for r in external))
f=base/'yio-cf-editing-forensics'; area=f/'research/casually-finance-editing-forensics';s=json.loads((area/'STATUS.json').read_text());qas=[]
for v in s['videos_complete']:
 q=json.loads((area/v['qa']).read_text());qas.append({'id':v['video_id'],'qa':q})
(out/'forensic-qa.json').write_text(json.dumps(qas,indent=2))
print('complete',len(qas),'qa first',str(qas[0])[:1100]);print('forensic ignored',len(subprocess.check_output(['git','-C',str(f),'ls-files','--others','--ignored','--exclude-standard','-z']).split(b'\0'))-1)
print('forensic tracked',len(subprocess.check_output(['git','-C',str(f),'ls-files','-z']).split(b'\0'))-1)
for n in ['bond100_review.json','debt_review.json','finalization-validation.json','preservation.json']:
 p=base/'yios-recovery-status/finance-final-qa'/n;x=json.loads(p.read_text());print(n,str(x)[:650])
print('recovery scripts', [r['path']for r in rows if r['folder']=='yios-recovery-status'and r['path'].endswith('.py')])
# Verify owner-listening receipts against actual clip bytes, no listening claim.
clips=json.loads((base/'yios-recovery-status/finance-owner-listening-2026-10-12/manifest.json').read_text())
for clip in clips:assert hashlib.sha256(pathlib.Path(clip['clip']).read_bytes()).hexdigest()==clip['clip_sha256']
print('listening clip hashes verified',len(clips))
