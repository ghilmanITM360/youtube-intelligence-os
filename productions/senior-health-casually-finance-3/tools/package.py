from pathlib import Path
import json,zipfile,hashlib
R=Path(__file__).resolve().parents[1];D=R/'delivery';D.mkdir(exist_ok=True);rows=[]
for P in sorted(R.glob('0*')):
 target=D/(P.name+'.zip')
 files=sorted(p for p in P.rglob('*') if p.is_file())
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in files:z.write(p,str(p.relative_to(R)))
 with zipfile.ZipFile(target) as z:
  assert z.testzip() is None
  assert len(z.infolist())==len(files)
  for p in files:assert hashlib.sha256(z.read(str(p.relative_to(R)))).hexdigest()==hashlib.sha256(p.read_bytes()).hexdigest()
 rows.append({'package':P.name,'file':str(target.relative_to(R)),'absolute_local_path':str(target.resolve()),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'member_count':len(files),'audio_included':True,'reference_screenshots_included':False,'status':'QA_BLOCKED'})
(D/'DELIVERY_MANIFEST.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
