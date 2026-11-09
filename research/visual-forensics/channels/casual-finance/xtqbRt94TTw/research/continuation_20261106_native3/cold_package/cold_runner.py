from pathlib import Path
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
