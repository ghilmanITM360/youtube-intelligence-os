"""Run existing validators, redirecting only their generated reports externally."""
import sys, runpy
from pathlib import Path
from unittest.mock import patch
base=Path(sys.argv[1]).resolve();out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(base))
original=Path.write_text
def redirected(p,data,*args,**kwargs):
 if p.parent==base and p.name in ['VALIDATION_966.json','VALIDATION.json']:
  return original(out/p.name,data,*args,**kwargs)
 raise RuntimeError('Unexpected validator write blocked: '+str(p))
with patch.object(Path,'write_text',redirected):
 runpy.run_path(str(base/sys.argv[3]),run_name='__main__')
