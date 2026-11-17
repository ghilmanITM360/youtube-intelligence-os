import pathlib,json,os,hashlib,collections,subprocess
A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21'); roots=[pathlib.Path('/Users/ghilmankhan')/s for s in ['Downloads/all training data of youtube','Downloads/dr rehan old videos','Downloads/CasuallyFinance','Downloads/casual_economics','Downloads/CasuallyFinance-Forensic-Research','workprojects/yios-recovery-status','workprojects/yio-cf-editing-forensics-local-evidence','Documents/YIOS-Production-Library','Documents/YIOS-Research-Export-2026-10-21','Documents/yios-private-backups']]
summary=[]
for root in roots:
 rows=[]
 for dp,ds,fs in os.walk(root,followlinks=False):
  for name in fs:
   p=pathlib.Path(dp)/name
   try:
    st=p.lstat();rows.append(dict(path=str(p),bytes=st.st_size,mtime_ns=st.st_mtime_ns,symlink=p.is_symlink()))
   except OSError as e:rows.append(dict(path=str(p),error=str(e)))
 (A/('external-'+root.name.replace(' ','_')+'.json')).write_text(json.dumps(rows,indent=2))
 rec=dict(path=str(root),exists=root.exists(),files=len(rows),bytes=sum(r.get('bytes',0)for r in rows),git_marker=(root/'.git').exists(),extensions=dict(collections.Counter(pathlib.Path(r['path']).suffix for r in rows)),preservation='RETAINED_IN_PLACE; no writes/moves')
 summary.append(rec);print({k:v for k,v in rec.items()if k!='extensions'})
(A/'external-summary.json').write_text(json.dumps(summary,indent=2))
# Fresh independent count from exact Finance head; universe's static labels need overlay.
ref='d41a5774f1381a21022b70f02d206303195be3a7';base='research/finance-economics-intelligence/'
b=subprocess.check_output(['git','show',ref+':'+base+'VIDEO_AUDIT_966.jsonl']);rows=[json.loads(l)for l in b.splitlines()];complete=lambda r:all(s in {'COMPLETE_LIMITED_EVIDENCE','COMPLETE_EVIDENCE_BACKED'}for s in r['statuses'].values())
count=sum(complete(r)for r in rows);full=sum(all(s=='COMPLETE_EVIDENCE_BACKED'for s in r['statuses'].values())for r in rows);nextid=next(r['Video_ID']for r in rows if any(s in {'NOT_STARTED','IN_PROGRESS'}for s in r['statuses'].values()))
result=dict(deep_audited_limited_evidence=count-full,full_evidence=full,remaining_original=len(rows)-count,remaining_combined=1612-count,next_id=nextid,latest_audit=next(r['batch_id']for r in rows if r['Video_ID']=='SU-3ZcgmCJ4'))
assert count==437 and full==0 and nextid=='S_8SLGjLrBM';(A/'finance-current-counts.json').write_text(json.dumps(result,indent=2));print('CURRENT_FINANCE',result)
# Preserve a list of independent repository markers; no reads of their content or modifications.
markers=[]
for p in pathlib.Path('/Users/ghilmankhan/workprojects').glob('*/.git'):
 if p.parent.name not in ['youtube-intelligence-os','yio-cf-editing-forensics']:markers.append(str(p))
(A/'independent-repository-markers.json').write_text(json.dumps(markers,indent=2))
