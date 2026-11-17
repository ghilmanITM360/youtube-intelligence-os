"""Draft stills assembled from delivered assets. Not an acceptance compositor.

The source drawings have unresolved geometry and this script does not animate
state changes or prove text clearance. Do not treat its results as approved shots.
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import csv

root=Path(__file__).resolve().parents[2];qa=root/'assets/qa';shots=qa/'shots';shots.mkdir(exist_ok=True)
selected={r['asset_id']:r['filename'] for r in csv.DictReader((qa/'review_selection.csv').open())}
def img(id):return Image.open(root/selected[id]).convert('RGBA')
def put(c,id,xy,scale=.5):
    a=img(id);a=a.resize((round(a.width*scale),round(a.height*scale)),Image.Resampling.LANCZOS);c.alpha_composite(a,(round(xy[0]),round(xy[1])))
def centered(c,id,center,scale=.5):
    a=img(id);a=a.resize((round(a.width*scale),round(a.height*scale)),Image.Resampling.LANCZOS);c.alpha_composite(a,(round(center[0]-a.width/2),round(center[1]-a.height/2)))
def character(c,id):put(c,id,(440-768*.78,1700-1102*.78),.78)
def text(c,id,xy,size=44,color='#0C0C0C'):
    p=root/'assets/text'/f'{id}.txt';string=p.read_text().splitlines()[0].removeprefix('String: ')
    try:f=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',size)
    except OSError:f=ImageFont.load_default()
    ImageDraw.Draw(c).text(xy,string,fill=color,font=f,stroke_width=0)
def stage(c,water='WTR-01',spoon='SPN-05',pose='CHR-P01'):
    put(c,'TBL-01',(0,0));centered(c,'THM-01',(950,1260));centered(c,'THM-02',(950,1230));centered(c,'MUG-01',(660,1240));centered(c,'THM-03',(800,1200));centered(c,water,(660,1240));centered(c,spoon,(660,1170));centered(c,'MUG-02',(660,1240));character(c,pose)
def ruler(c):put(c,'RUL-01',(0,140));text(c,'TXT-03',(90,110),40)
def labels(c,*ids):
    for i,id in enumerate(ids):text(c,id,(190,185+i*60),36,'#D7263D' if id in ('TXT-06','TXT-15') else '#0C0C0C')
for n in range(1,30):
 c=Image.new('RGBA',(1080,1920),'white')
 if n<=6:
  poses={1:'CHR-P01',2:'CHR-P03',3:'CHR-P06',4:'CHR-P07',5:'CHR-P10',6:'CHR-P11'}
  stage(c,'WTR-02' if n in (3,4) else 'WTR-01','SPN-01' if n in (3,4) else ('SPN-06' if n>=5 else 'SPN-05'),poses[n]);labels(c,'TXT-01')
  if n==2:centered(c,'STR-01',(335,210),1)
  if n==4:centered(c,'HEAT-01',(620,1180),1)
  if n>=6:ruler(c)
 elif n<=13:
  ruler(c);character(c,'CHR-P02')
  if n<=10:
   centered(c,'JUG-01',(370,510));centered(c,'THR-01',(660,500));centered(c,'BRK-01',(760,530),1);labels(c,'TXT-17')
  if n>=8 and n<=10:labels(c,'TXT-04')
  if n==9:centered(c,'CLK-01',(850,500));labels(c,'TXT-05')
  if n==10:centered(c,'RDC-01',(110,480),1);labels(c,'TXT-06')
  if n==11:
   for i in range(7):centered(c,'BLB-01',(250+i*115,475))
   labels(c,'TXT-07')
  if n==12:centered(c,'MWV-01',(540,480));labels(c,'TXT-20')
  if n==13:centered(c,'HRS-01',(540,480));labels(c,'TXT-19')
 elif n in (14,15):
  put(c,'NIA-01' if n==14 else 'NIA-03',(0,100));centered(c,'NIA-02' if n==14 else 'NIA-04',(540,480));character(c,'CHR-P14')
  if n==14:centered(c,'NIA-05',(170,510),1);text(c,'TXT-16',(210,430),36)
  else:centered(c,'NIA-06',(880,510));labels(c,'TXT-08','TXT-14')
 elif n<=20:
  stage(c,'WTR-02' if n==19 else 'WTR-03','SPN-04','CHR-P03' if n==19 else 'CHR-P09');ruler(c)
  if n>=17:centered(c,'DOT-01',(70,1250),1);labels(c,'TXT-09')
  if n==18:centered(c,'RDC-01',(100,1240),1);centered(c,'BLB-01',(275,1230))
  if n==19:centered(c,'HLS-01',(660,1020),1);centered(c,'HLS-03',(570,1170),1);labels(c,'TXT-18')
  if n==20:labels(c,'TXT-10')
 elif n in (21,22):
  ruler(c);centered(c,'CAV-01',(600,510));centered(c,'CAV-02',(600,510));labels(c,'TXT-11')
  if n==22:centered(c,'CAV-03',(300,740));centered(c,'FLM-01',(300,860));centered(c,'XOUT-01',(300,860),1);labels(c,'TXT-12')
 elif n==23:
  stage(c,'WTR-03','SPN-04','CHR-P09');ruler(c);centered(c,'WTR-04',(660,1110));centered(c,'HLS-02',(660,1020),1)
 elif n in (24,25):
  ruler(c);put(c,'EXP-01',(0,100),1)
  for x in (180,540,900):centered(c,'MUG-01',(x,525));centered(c,'WTR-01',(x,525));centered(c,'MUG-02',(x,525));centered(c,'THM-01',(x,680));centered(c,'THM-02',(x,650))
  centered(c,'SPN-01',(180,480));centered(c,'EXP-02',(540,300),1);labels(c,'TXT-13')
  if n==25:put(c,'CHT-01',(0,940),1);labels(c,'TXT-14')
 else:
  stage(c,'WTR-02' if n>=27 else 'WTR-01','SPN-01' if n>=27 else 'SPN-05','CHR-P12' if n>=28 else ('CHR-P13' if n==27 else 'CHR-P11'));ruler(c)
  if n>=27:centered(c,'SUG-01',(680,1110),1)
  if n>=28:labels(c,'TXT-15')
 c.convert('RGB').save(shots/f'S{n:02}.png')
print('29 DRAFT stills written; visual, geometry, text, animation and full shot QA remain incomplete')
