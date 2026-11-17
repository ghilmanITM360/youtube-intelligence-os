from pathlib import Path
import csv,json,hashlib,subprocess
from PIL import Image,ImageDraw
r=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/extracted/forensic-analysis/casually-finance/2026-10-12')
v='rSa2aziEsAI';s=json.loads((r/'02_VIDEO_FORENSICS'/v/'SOURCE.json').read_text());files=list(Path('/Users/ghilmankhan/Downloads/CasuallyFinance').glob('*.mp4'));source=next(p for p in files if p.name==Path(s['local_file']).name)
assert hashlib.sha256(source.read_bytes()).hexdigest()==s['sha256']
rows=[x for x in csv.DictReader((r/'02_VIDEO_FORENSICS'/v/'MOTIONS.csv').open()) if x['label_vs_measure_check'].startswith('LABEL_IMPLIES_')]
out=Path('/Users/ghilmankhan/workprojects/yios-recovery-status/finance-final-qa/JsK53moCyZA-motion');out.mkdir(exist_ok=True)
canvas=Image.new('RGB',(9*180,len(rows)*350),'white');draw=ImageDraw.Draw(canvas);meta=[]
for i,m in enumerate(rows):
 a=float(m['start_sec']);b=float(m['end_sec']);times=[max(0,a-2/30),a,a+1/30,a+2/30,a+(b-a)*.25,a+(b-a)*.5,a+(b-a)*.75,b,b+2/30]
 for j,t in enumerate(times):
  p=out/f"{m['motion_id']}-{j}.png"
  subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss',str(t),'-i',str(source),'-frames:v','1','-vf','scale=180:320','-y',str(p)],check=True)
  with Image.open(p) as im:canvas.paste(im,(j*180,i*350+30))
  draw.text((j*180,i*350+15),f'{t:.4f}s',fill='black')
 draw.text((0,i*350),f"{m['motion_id']} {m['action_label']} {a}-{b}",fill='black')
 meta.append({'motion_id':m['motion_id'],'times':times})
canvas.save(out/'review.png');
for first in range(0,len(rows),5): canvas.crop((0,first*350,1620,min(len(rows),first+5)*350)).save(out/f'review-{first//5+1}.png')
(out/'metadata.json').write_text(json.dumps({'video_id':v,'source_sha256':s['sha256'],'sequences':meta},indent=2));print(out/'review.png')
