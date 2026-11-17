import sys,runpy,json
from pathlib import Path
root=Path(__file__).parent;reads=[]
def audit(event,args):
 if event=='open' and isinstance(args[0],(str,bytes)):
  name=str(args[0]);reads.append(name)
  if ('YIOS-local-audits' in name and not name.startswith(str(root))) or 'Downloads/videos' in name:raise RuntimeError('Unpackaged source/evidence access: '+name)
sys.addaudithook(audit)
sys.argv=[str(root/'render_original.py'),str(root/'ORIGINAL_PRODUCTION_SPEC.json'),str(root/'output')]
runpy.run_path(str(root/'render_original.py'),run_name='__main__')
(root/'read_audit.json').write_text(json.dumps({'status':'PASS_NO_SOURCE_READS','opened_paths':sorted(set(reads))},indent=2)+'\n')
