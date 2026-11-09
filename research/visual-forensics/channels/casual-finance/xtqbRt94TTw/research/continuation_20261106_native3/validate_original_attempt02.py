from pathlib import Path
import json,hashlib,subprocess,shutil,sys
import numpy as np
from PIL import Image
P=Path(__file__).parent;O=P/'original_attempt02';s=json.loads((P/'ORIGINAL_SPAN_SPEC.json').read_text());freeze=json.loads((P/'FREEZE_RECEIPT.json').read_text());assert freeze['criteria_sha256']==hashlib.sha256((P/'ACCEPTANCE_FROZEN.json').read_bytes()).hexdigest();assert freeze['spec_sha256']==hashlib.sha256((P/'ORIGINAL_SPAN_SPEC.json').read_bytes()).hexdigest();checks={}
def a(g,n):return np.array(Image.open(O/g/f'f{n:05}.png'))
def same(g,ns,roi):
 l,t,r,b=roi;x=a(g,ns[0])[t:b,l:r];return all(np.array_equal(x,a(g,n)[t:b,l:r])for n in ns[1:])
def bbox(mask):
 y,x=np.where(mask);return None if not len(x)else list(map(int,[x.min(),y.min(),x.max(),y.max()]))
bg=np.array([248,250,248]);checks['48_native_canvas_frames']=len(list(O.rglob('f*.png')))==48 and all(Image.open(x).size==(1920,1080)for x in O.rglob('f*.png'))
checks['G005_absent749_present750']=np.all(a('G005',749)[:,:][0:1080,800:]==bg)and np.any(a('G005',750)[:,1800:]!=bg)
checks['G005_robot_pointer_static']=same('G005',list(range(749,770)),[0,0,800,1080])
checks['G005_final766_hold']=same('G005',[766,767,768,769],[0,0,1920,1080])
# Mask original badge top edge; copy is below/away. Pin expected positions, constant-size once unclipped.
lefts=[]
for n in range(750,767):
 x=a('G005',n);mask=np.all(x[112:120,:, :]==np.array([32,60,74]),axis=2);bb=bbox(mask);assert bb;lefts.append(bb[0])
checks['G005_observed_left_track_bound']=lefts==[v for n,v in s['systems']['G005.01']['card_left_track']if n<=766]
from PIL import ImageFont
F=ImageFont.truetype(s['font'],35);checks['G005_final_copy_fits']=all(884+F.getlength(t)<1784 for t in s['systems']['G005.01']['copy'][3:])
checks['G006_cut837']=not np.array_equal(a('G006',836),a('G006',837))
checks['G006_static_text_and_robot']=same('G006',list(range(837,863)),[0,0,1920,450])and same('G006',list(range(837,863)),[1000,450,1920,1080])
color=np.array([44,129,127]);bbars={n:bbox(np.all(a('G006',n)==color,axis=2))for n in range(837,863)}
checks['G006_firstvisible839']=bbars[837]is None and bbars[838]is None and bbars[839]is not None
checks['G006_group_right_track']=all(bbars[n][2]==v for n,v in s['systems']['G006.01']['arrow_right_track']if n<=857)
checks['G006_fixed_final_geometry_and_five_bars']=bbars[857]==[325,605,663,935]and all(np.all(a('G006',857)[700:931,x:x+19]==color)for x in[325,485])
checks['G006_final_hold']=same('G006',list(range(857,863)),[0,0,1920,1080])
font42=ImageFont.truetype(s['font'],42);checks['G006_copy_fits']=all(175+font42.getlength(t)<1850 for t in s['systems']['G006.01']['copy'][:2])
checks={k:bool(v)for k,v in checks.items()}
mask=np.all(a('G006',857)==color,axis=2);runs=[];active=False
for x in range(1920):
 on=bool(mask[:,x].any())
 if on and not active:runs.append(x)
 active=on
checks['G006_exactly_five_bar_components']=runs==[325,405,485,565,645]
result={'channel':'Casual Finance','video_id':'xtqbRt94TTw','checks':checks,'status':'PASS'if all(checks.values())else'FAIL','scope':'48original frames; source timing/anchor behavior transfer, not source-art fidelity or whole-video approval','frozen_criteria_sha256':freeze['criteria_sha256'],'render_manifest_sha256':hashlib.sha256((O/'render_manifest.json').read_bytes()).hexdigest()};(P/'ORIGINAL_VALIDATION_attempt02.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));assert all(checks.values())
