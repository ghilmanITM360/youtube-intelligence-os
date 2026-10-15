from pathlib import Path
import json,hashlib,zipfile,subprocess,csv
R=Path(__file__).resolve().parents[1]; C=R/'reference_local'; C.mkdir(exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,indent=2))
paths=['/Users/ghilmankhan/Desktop/causal finace example .zip']+[str(Path('/Users/ghilmankhan/Downloads')/n) for n in ['HIIT After 60 Good for Your Heart or Too Intense.mp4','Running After 60 Good for Your Heart, Bad for You.mp4','Swimming After 60 Why This Heart Exercise Gets 9..mp4']]
manifest=[]
for i,s in enumerate(paths):
 p=Path(s); row={'path':s,'bytes':p.stat().st_size,'sha256':sha(p),'disposition':'REFERENCE_ONLY' if i==0 else 'SUPPORTING_EVIDENCE','rights':'User-supplied; ownership and publication rights unverified'}
 if i:
  folder=R/['','01_HIIT_AFTER_60','02_RUNNING_AFTER_60','03_SWIMMING_AFTER_60'][i]
  for d in ['source_audio','script','storyboard','assets/svg','assets/png','scene_states','animation_plan','qa']: (folder/d).mkdir(parents=True,exist_ok=True)
  probe=json.loads(subprocess.check_output(['ffprobe','-v','quiet','-show_format','-show_streams','-of','json',s])); write(folder/'source_audio/FFPROBE.json',probe)
  for codec,out in [('copy','original_audio.m4a'),('pcm_s24le','narration_mix.wav')]:
   target=folder/'source_audio'/out
   if not target.exists(): subprocess.run(['ffmpeg','-v','error','-i',s,'-map','0:a:0','-vn','-c:a',codec,str(target)],check=True)
  row['package']=folder.name
  row['audio']=[{'file':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in (folder/'source_audio').glob('*')]
  subprocess.run(['ffmpeg','-v','error','-i',s,'-vf','fps=1/3,scale=240:-1,tile=4x3','-frames:v','1','-y',str(C/f'video_{i}_sheet.png')],check=True)
 manifest.append(row)
write(R/'INPUT_MANIFEST.json',manifest)
with zipfile.ZipFile(paths[0]) as z:
 entries=[]
 for n,info in enumerate(z.infolist()):
  b=z.read(info); safe=not info.filename.startswith('/') and '..' not in Path(info.filename).parts
  row={'member':info.filename,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'disposition':'NOISE' if info.filename.startswith('__MACOSX/') else 'REFERENCE_ONLY' if safe else 'UNSAFE'}
  if row['disposition']=='REFERENCE_ONLY':
   target=C/f'ref_{n:02d}.png'; target.write_bytes(b); row['local']=str(target.relative_to(R))
  entries.append(row)
 write(R/'ZIP_MANIFEST.json',entries)
from PIL import Image,ImageOps,ImageDraw
files=sorted(C.glob('ref_*.png')); sheet=Image.new('RGB',(1200, len(files)//3*270),'#dddddd'); draw=ImageDraw.Draw(sheet)
for i,p in enumerate(files):
 im=Image.open(p).convert('RGB'); im.thumbnail((390,240)); x=(i%3)*400;y=(i//3)*270;sheet.paste(im,(x,y));draw.text((x,y+242),p.name,fill='black')
sheet.save(C/'reference_sheet.jpg')
print('Prepared',len(manifest),'inputs;',len(entries),'ZIP dispositions')
