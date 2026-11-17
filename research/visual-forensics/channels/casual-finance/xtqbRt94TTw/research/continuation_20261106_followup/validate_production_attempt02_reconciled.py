from pathlib import Path
import json,hashlib,subprocess
from PIL import Image,ImageColor
import numpy as np
P=Path(__file__).parent;A=P/'production_attempt02';C=P/'cold_start_package_attempt02'
o=lambda n:np.array(Image.open(A/f'opening/f{n:05d}.png'))
bg=np.array(ImageColor.getrgb('#f8faf8'));checks={}
checks['frame0_blank']=np.all(o(0)==bg);yy,xx=np.where(np.any(o(1)!=bg,axis=2));checks['frame1_roof_only_bottom']=len(xx)>0 and yy.min()>=1072
checks['eyes_absent11_present12']=not np.any(np.all(o(11)[700:835,815:1100]==[255,255,255],axis=2)) and np.any(np.all(o(12)[700:835,815:1100]==[255,255,255],axis=2))
checks['stable33_36']=all(np.array_equal(o(33),o(n))for n in [34,35,36])
checks['card1_absent5_present6']=np.all(o(5)[0:10,100:800]==bg) and np.any(o(6)[0:10,100:800]!=bg)
checks['card2_absent31_present32']=np.all(o(31)[90:200,800:1460]==bg) and np.any(o(32)[90:200,800:1460]!=bg)
checks['bulletin_stable301_303']=all((A/'bulletin/f00301.png').read_bytes()==(A/f'bulletin/f{n:05d}.png').read_bytes()for n in [302,303])
checks['dimensions']=all(Image.open(f).size==(1920,1080)for f in A.glob('*/*.png'))
checks['40_cold_start_hashes_match']=len(list(A.glob('*/*.png')))==40 and all(hashlib.sha256(f.read_bytes()).hexdigest()==hashlib.sha256((C/'output'/f.relative_to(A)).read_bytes()).hexdigest()for f in A.glob('*/*.png'))
checks['no_source_reads']=json.loads((C/'read_audit.json').read_text())['status']=='PASS_NO_SOURCE_READS'
for group,n in [('opening',37),('bulletin',3)]:
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json',str(A/(group+'.mp4'))]));checks[group+'_silent_24fps_framecount']=len(probe['streams'])==1 and probe['streams'][0]['r_frame_rate']=='24/1'and int(probe['streams'][0]['nb_frames'])==n
# First-card dark-fill bboxheight inx100..740 excludessecondcardx750+. Fullbox is181inclusive rows.
cardrgb=np.array(ImageColor.getrgb('#203c4a'));heights={}
for n in range(6,33):
 a=o(n);yy,xx=np.where(np.all(a[:570,100:740]==cardrgb,axis=2));heights[n]=int(yy.max()-yy.min()+1)if len(yy)else 0
checks['card1_first_fully_visible23']=min(n for n,h in heights.items()if h>=181)==23
checks['card1_clipped13_14_22']=all(heights[n]<181 for n in [13,14,22])
checks['card1_full23_final32']=heights[23]==181 and heights[32]==181 and np.any(np.all(o(32)[210:390,110:740]==cardrgb,axis=2))
checks={k:bool(v)for k,v in checks.items()}
result={'status':'PASS'if all(checks.values())else'FAIL','checks':checks,'root_visual_review':'Opening0/1/6/12/23/31/32/36 contact and native bulletin301 viewed; readable original labels, two open eyes, smiling robot, page not a source screenshot.','scope':'opening0-36 plus bulletin301-303 only','whole_video_visual_cold_start':'PENDING; remaining spans/source semantics incomplete','audio':'BLOCKED'}
(P/'PRODUCTION_VALIDATION_attempt02_reconciled.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));assert all(checks.values())
(P/'ROOT_QA_REPAIR_READY.json').write_text(json.dumps({'new_native_scope_ready':True,'production_scope_ready':True,'coldstart_validation':'PRODUCTION_VALIDATION_attempt02_reconciled.json','attempt':'production_attempt02','preflight_regression':'preflight_GREEN_final.txt','independent_approval_pending':True},indent=2)+'\n')
