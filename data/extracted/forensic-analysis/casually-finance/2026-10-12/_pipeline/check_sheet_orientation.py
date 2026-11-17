import ast
from pathlib import Path
s=ast.parse(Path('_pipeline/build_video.py').read_text())
node=next(n.value for n in ast.walk(s) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='per_sheet' for t in n.targets))
expr=compile(ast.Expression(node),'build_video.py','eval')
assert eval(expr,{'meta':{'height':'1920','width':'1080'}})==16,'Portrait evidence sheets must contain16 frames'
assert eval(expr,{'meta':{'height':'720','width':'1280'}})==12,'Landscape evidence sheets must contain12 frames'
print('Sheet orientation regression PASS')
