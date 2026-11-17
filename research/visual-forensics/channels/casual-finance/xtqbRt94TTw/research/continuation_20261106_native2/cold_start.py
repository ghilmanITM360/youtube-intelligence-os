from pathlib import Path
import json,shutil,subprocess,hashlib
P=Path(__file__).parent;C=P/'cold_start_package';C.mkdir(exist_ok=False)
for n in ['render_g004.py','render_token_attempt02.py','G004_ORIGINAL_SPEC.json','TOKEN_VOUCHER_ORIGINAL_SPEC.json']:shutil.copyfile(P/n,C/n)
runner='''import sys,os,json,runpy
from pathlib import Path
root=Path(__file__).parent.resolve();reads=[]
def audit(event,args):
 if event!='open' or not isinstance(args[0],(str,bytes)):return
 p=Path(os.fsdecode(args[0])).resolve();mode=args[1]
 if isinstance(mode,str)and any(c in mode for c in 'wax+'):return
 q=str(p);reads.append(q)
 if '/Downloads/'in q or ('/YIOS-local-audits/'in q and not str(p).startswith(str(root)+'/')and '/YIOS-local-audits/tooling/'not in q):raise PermissionError('Source/evidence outside package denied')
sys.addaudithook(audit)
for renderer,spec,out in [('render_g004.py','G004_ORIGINAL_SPEC.json','g004_output'),('render_token_attempt02.py','TOKEN_VOUCHER_ORIGINAL_SPEC.json','token_output')]:
 sys.argv=[str(root/renderer),str(root/spec),str(root/out)];runpy.run_path(str(root/renderer),run_name='__main__')
(root/'read_audit.json').write_text(json.dumps({'reads':sorted(set(reads)),'scope':'Python open audit hook, not OS-level sandbox/trace'},indent=2)+'\\n')
''';(C/'run.py').write_text(runner)
r=subprocess.run(['/Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3','-I',str(C/'run.py')],cwd=C,capture_output=True,text=True,timeout=90);checks=[]
for original,new in [('g004_attempt01','g004_output'),('token_attempt02','token_output')]:
 for f in sorted((P/original).glob('f*.png')):checks.append({'frame':f.name,'system':original,'match':hashlib.sha256(f.read_bytes()).hexdigest()==hashlib.sha256((C/new/f.name).read_bytes()).hexdigest()})
out={'channel':'Casual Finance','video_id':'xtqbRt94TTw','exit_code':r.returncode,'stderr':r.stderr,'status':'PASS'if r.returncode==0 and all(x['match']for x in checks)and len(checks)==128 else'FAIL','frame_checks':checks,'package':str(C),'source_access':'Python open hook denies Downloads/source and external YIOS evidence; system libraries/fonts allowed. Not OS-level trace.','scope':'86+42 bounded original frames; not fullvideo','dependencies':{'python':'visual-ct-scan-venv','Pillow':'installed','font':'/System/Library/Fonts/Supplemental/Arial.ttf'}};(P/'COLD_START_EXECUTION.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],r.returncode,len(checks),r.stderr)
