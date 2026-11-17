import sys,os,json,runpy
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
(root/'read_audit.json').write_text(json.dumps({'reads':sorted(set(reads)),'scope':'Python open audit hook, not OS-level sandbox/trace'},indent=2)+'\n')
