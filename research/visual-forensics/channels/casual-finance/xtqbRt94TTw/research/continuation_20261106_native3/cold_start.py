from pathlib import Path
import subprocess,sys,shutil,json,hashlib
P=Path(__file__).parent;D=P/'cold_package';D.mkdir(exist_ok=False)
for name in ['ORIGINAL_SPAN_SPEC.json','render_original_attempt02.py']:shutil.copy2(P/name,D/name)
runner='''from pathlib import Path
import sys,runpy,os
import PIL.Image,PIL.ImageDraw,PIL.ImageFont
root=Path(__file__).parent.resolve()
allowed=[root,Path(sys.base_prefix).resolve(),Path(sys.prefix).resolve(),Path('/System/Library/Fonts'),Path('/Library/Fonts'),Path(PIL.__file__).resolve().parent]
def audit(event,args):
 if event!='open':return
 p=args[0]
 if not isinstance(p,(str,bytes,os.PathLike)):return
 path=Path(p).resolve()
 if not any(path==a or a in path.parents for a in allowed):raise PermissionError('Cold package forbidden path: '+str(path))
sys.addaudithook(audit)
sys.argv=[str(root/'render_original_attempt02.py'),str(root/'ORIGINAL_SPAN_SPEC.json'),str(root/'output')]
runpy.run_path(str(root/'render_original_attempt02.py'),run_name='__main__')
'''
(D/'cold_runner.py').write_text(runner);r=subprocess.run([sys.executable,str(D/'cold_runner.py')],cwd=D,capture_output=True,text=True);record={'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'isolation':'Python audit open-hook after PIL import, allowed package+Python runtime+Pillow+systemfonts; not OS sandbox or full systemcall trace','dependency':'Pillow and system Arial font','scope':'48frames only, whole-video NOT_RUN'}
if r.returncode==0:
 a=json.loads((P/'original_attempt02/render_manifest.json').read_text());b=json.loads((D/'output/render_manifest.json').read_text());assert a==b;record.update(status='PASS',matching_PNGs=len(a),package_inputs={n:hashlib.sha256((D/n).read_bytes()).hexdigest()for n in ['ORIGINAL_SPAN_SPEC.json','render_original_attempt02.py','cold_runner.py']})
(P/'COLD_START_EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record));assert r.returncode==0
