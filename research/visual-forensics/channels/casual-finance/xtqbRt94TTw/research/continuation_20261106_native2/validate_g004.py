from pathlib import Path
import json,hashlib,subprocess,sys
import numpy as np
from PIL import Image,ImageColor,ImageDraw
P=Path(__file__).parent;S=json.loads((P/'G004_ORIGINAL_SPEC.json').read_text());D=P/'g004_attempt01';ims={n:np.array(Image.open(D/f'f{n:05}.png'))for n in range(565,651)}
color=lambda c:np.array(ImageColor.getrgb(c));accent=color(S['palette']['accent']);ink=color(S['palette']['ink']);skin=color(S['palette']['skin']);checks={}
checks['86_native1080frames']=all(x.shape==(1080,1920,3)for x in ims.values())and len(ims)==86
checks['robot565_not566']=int((ims[565][485:795,1355:1665]==skin).all(2).sum())>50000 and int((ims[566][485:795,1355:1665]==skin).all(2).sum())==0
checks['layout_begins567']=not np.array_equal(ims[566][:250],ims[567][:250]);checks['layout_last584']=not np.array_equal(ims[583][:250],ims[584][:250]);checks['headers_hold584_650']=all(np.array_equal(ims[584][90:235],ims[n][90:235])for n in range(585,651))
checks['firstvisible_newaccent575']=not (ims[574][600:620,:88]==accent).all(2).any()and(ims[575][600:620,:88]==accent).all(2).all()
def band(n,i):
 x0,y0,x1,y1=S['original_system']['highlight_local_bands'][i];x=ims[n][90+y0:90+y1+1,1002+x0:1002+x1+1];m=(x==accent).all(2);yy,xx=np.where(m);return {'pixels':int(m.sum()),'rightedge':int(xx.max())if len(xx)else None}
checks['parallel_lines_grow584_606']=all(band(584,i)['pixels']<band(606,i)['pixels']for i in [0,1])
checks['third_first607']=band(606,2)['pixels']==0 and band(607,2)['pixels']>0
checks['third_complete622_holds']=band(621,2)['pixels']<band(622,2)['pixels']and all(band(n,2)==band(622,2)for n in range(623,651))
orange=color('#eda645');checks['left_yellow608_orange609']=bool((ims[608][605,125]==accent).all()and(ims[609][605,125]==orange).all())
checks['cursor_changes_through648']=not np.array_equal(ims[647],ims[648]);checks['static649_650']=np.array_equal(ims[648],ims[649])and np.array_equal(ims[649],ims[650])
info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json',str(D/'g004_silent.mp4')]))['streams'];checks['silent24fps86frames']=len(info)==1and info[0]['codec_type']=='video'and info[0]['r_frame_rate']=='24/1'and int(info[0]['nb_frames'])==86
res={'channel':'Casual Finance','video_id':'xtqbRt94TTw','status':'PASS'if all(checks.values())else'FAIL','frozen_criteria_sha256':hashlib.sha256((P/'G004_ACCEPTANCE_FROZEN.json').read_bytes()).hexdigest(),'checks':{k:bool(v)for k,v in checks.items()},'scope':'86frame original bounded system; G004.01 span566–584. Not source fidelity or wholevideo.','cold_start':'SEPARATE_RECEIPT_REQUIRED'};(P/'G004_VALIDATION_attempt01.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
fs=[565,566,567,575,583,584,606,607,608,609,621,622,648,649];o=Image.new('RGB',(960,((len(fs)+1)//2)*294),'#ddd');dr=ImageDraw.Draw(o)
for i,n in enumerate(fs):
 im=Image.fromarray(ims[n]);im.thumbnail((480,270));x=i%2*480;y=i//2*294;o.paste(im,(x,y+24));dr.text((x+5,y+5),f'Original{n}',fill='black')
o.save(P/'g004_attempt01_overview.jpg',quality=96)
