from pathlib import Path
import json,hashlib,subprocess
import numpy as np
from PIL import Image,ImageColor,ImageDraw
P=Path(__file__).parent;S=json.loads((P/'TOKEN_VOUCHER_ORIGINAL_SPEC.json').read_text());D=P/'token_attempt01';xs={n:np.array(Image.open(D/f'f{n:05}.png'))for n in range(1119,1161)};ink=np.array(ImageColor.getrgb(S['token']['color']));accent=np.array(ImageColor.getrgb(S['token']['visor']));checks={};observed=[]
for n,x in xs.items():
 m=(x[:815,:700]==ink).all(2);yy,xx=np.where(m);bb=None if not len(xx)else[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())];observed.append({'frame':n,'token_bbox':bb})
checks['42native1080frames']=len(xs)==42 and all(x.shape==(1080,1920,3)for x in xs.values());checks['token_absent1119_present1120']=observed[0]['token_bbox']is None and observed[1]['token_bbox']is not None
ys=dict(S['token']['y_centers']);checks['constant_size_declared_track']=all(r['token_bbox']==[255,ys.get(r['frame'],456)-126,545,ys.get(r['frame'],456)+126]for r in observed[1:])
checks['eyes_first1141']=not(xs[1140][:700,:700]==accent).all(2).any()and(xs[1141][:700,:700]==accent).all(2).any();checks['background_held']=all(np.array_equal(xs[1119][200:700,1000:1650],x[200:700,1000:1650])for x in xs.values())
counts={}
for n,x in xs.items():
 count=sum(bool((x[box[1]+15,box[0]+15]==accent).all())for box in S['vouchers']['boxes']);counts[n]=count
checks['voucher_sequential_counts']=all(c==sum(n>=a for a in [1151,1156,1159])for n,c in counts.items())
info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json',str(D/'token_silent.mp4')]))['streams'];checks['silent24fps42frames']=len(info)==1 and info[0]['r_frame_rate']=='24/1'and int(info[0]['nb_frames'])==42
r={'channel':'Casual Finance','video_id':'xtqbRt94TTw','status':'PASS'if all(checks.values())else'FAIL','frozen_criteria_sha256':hashlib.sha256((P/'TOKEN_VOUCHER_ACCEPTANCE_FROZEN.json').read_bytes()).hexdigest(),'checks':{k:bool(v)for k,v in checks.items()},'measurements':observed,'voucher_counts':counts,'scope':'G007.01 and G008.01 plus contextual eyes/third-ticket. Original behavior not source art.'};(P/'TOKEN_VALIDATION_attempt01.json').write_text(json.dumps(r,indent=2)+'\n');print(r['status'],r['checks'])
fs=[1119,1120,1125,1130,1140,1141,1150,1151,1155,1156,1158,1159];out=Image.new('RGB',(960,6*294),'#ddd');d=ImageDraw.Draw(out)
for i,n in enumerate(fs):
 im=Image.fromarray(xs[n]);im.thumbnail((480,270));x=i%2*480;y=i//2*294;out.paste(im,(x,y+24));d.text((x+5,y+5),f'Original{n}',fill='black')
out.save(P/'token_attempt01_overview.jpg',quality=96)
