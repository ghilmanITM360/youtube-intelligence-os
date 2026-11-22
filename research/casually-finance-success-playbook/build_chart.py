from pathlib import Path
import csv,math
from reportlab.graphics.shapes import Drawing, String, Line, Circle, Rect
from reportlab.graphics import renderSVG
from reportlab.lib.colors import HexColor
root=Path('research/casually-finance-success-playbook')
rows=list(csv.DictReader((root/'VIDEO_PERFORMANCE.csv').open()))
d=Drawing(980,440);d.add(Rect(0,0,980,440,fillColor=HexColor('#FFF9EC'),strokeColor=None));d.add(String(30,409,'Public views/day versus publication age',fontSize=20,fillColor=HexColor('#243247')))
d.add(String(30,389,'October 11, 2026 snapshot · logarithmic axes · lifetime averages, not current daily traffic',fontSize=11))
colors={'BREAKOUT':'#157A78','TOP_PERFORMER':'#7358A6','ABOVE_BASELINE':'#3E76A0','TYPICAL':'#697681','BELOW_BASELINE':'#B38A53','UNDERPERFORMER':'#D55B47','INSUFFICIENT_DATA':'#C1C5C8'}
for panel,f in enumerate(['LONG_FORM','SHORT']):
 ox=65+panel*480;oy=70;w=375;h=260
 d.add(String(ox,350,f.replace('_',' ').title(),fontSize=16));d.add(Line(ox,oy,ox+w,oy));d.add(Line(ox,oy,ox,oy+h))
 for age in [1,7,30,100,450]:
  x=ox+math.log10(age)/math.log10(500)*w;d.add(Line(x,oy-4,x,oy));d.add(String(x-10,oy-20,str(age),fontSize=9))
 for v in [10,100,1000,10000,100000,1000000]:
  y=oy+(math.log10(v)-1)/5*h;d.add(Line(ox-4,y,ox,y));d.add(String(ox-53,y-3,str(v),fontSize=8))
 d.add(String(ox+100,oy-40,'Days since publication',fontSize=10))
 for r in rows:
  if r['Format']!=f:continue
  x=ox+math.log10(float(r['Age_Days']))/math.log10(500)*w;y=oy+(math.log10(max(10,float(r['Views_Per_Day'])))-1)/5*h
  d.add(Circle(x,y,3.3,fillColor=HexColor(colors[r['Tier']]),strokeColor=None))
for i,(k,v) in enumerate(colors.items()):
 x=30+(i%4)*240;y=17 if i<4 else 3;d.add(Circle(x,y,3,fillColor=HexColor(v),strokeColor=None));d.add(String(x+8,y-3,k,fontSize=8))
renderSVG.drawToFile(d,str(root/'PERFORMANCE_BY_AGE.svg'))
print('Saved two-format publication-age chart')
