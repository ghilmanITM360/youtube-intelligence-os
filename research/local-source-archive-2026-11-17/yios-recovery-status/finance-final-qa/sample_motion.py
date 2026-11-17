from pathlib import Path
import csv,json,hashlib,subprocess,sys
from PIL import Image,ImageDraw
r=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/extracted/forensic-analysis/casually-finance/2026-10-12');v=sys.argv[1];s=json.loads((r/'02_VIDEO_FORENSICS'/v/'SOURCE.json').read_text());fps=float(s['probe']['fps']);w,h=(240,135) if int(s['probe']['width'])>int(s['probe']['height']) else (180,320);source=next((p for p in Path('/Users/ghilmankhan/Downloads/CasuallyFinance').glob('*.mp4') if p.name==Path(s['local_file']).name),None);source=source or Path(next(x['path'] for x in json.loads((r/'00_MANIFEST/NEW_MAC_RECOVERY_2026-10-12.json').read_text())['source_files'] if x['video_id']==v));assert hashlib.sha256(source.read_bytes()).hexdigest()==s['sha256'];rows=[x for x in csv.DictReader((r/'02_VIDEO_FORENSICS'/v/'MOTIONS.csv').open()) if x['label_vs_measure_check'].startswith('LABEL_IMPLIES_')];rows=sorted(rows,key=lambda x:float(x['duration_sec']),reverse=True)[:int(sys.argv[2])] if len(sys.argv)>2 else rows;o=Path('/Users/ghilmankhan/workprojects/yios-recovery-status/finance-final-qa')/(v+'-motion');o.mkdir(exist_ok=True);meta=[]
for first in range(0,len(rows),5):
 batch=rows[first:first+5];can=Image.new('RGB',(9*w,len(batch)*(h+30)),'white');dr=ImageDraw.Draw(can)
 for i,m in enumerate(batch):
  a=float(m['start_sec']);b=float(m['end_sec']);times=[max(0,a-2/fps),a,a+1/fps,a+2/fps,a+(b-a)*.25,a+(b-a)*.5,a+(b-a)*.75,b,b+2/fps]
  for j,t in enumerate(times):
   p=o/f"{m['motion_id']}-{j}.png";result=subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss',str(t),'-i',str(source),'-frames:v','1','-vf',f'scale={w}:{h}','-y',str(p)],capture_output=True,check=True)
   with Image.open(p) as im:can.paste(im,(j*w,i*(h+30)+30))
   dr.text((j*w,i*(h+30)+15),f'{t:.4f}s',fill='black')
  dr.text((0,i*(h+30)),f"{m['motion_id']} {m['action_label']} {a}-{b}",fill='black');meta.append({'motion_id':m['motion_id'],'times':times})
 can.save(o/f'review-{first//5+1}.png')
(o/'metadata.json').write_text(json.dumps({'video_id':v,'source_sha256':s['sha256'],'fps':fps,'sequences':meta},indent=2));print(v,len(rows),'sequences',o)
