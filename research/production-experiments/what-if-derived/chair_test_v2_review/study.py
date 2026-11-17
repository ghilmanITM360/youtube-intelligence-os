from pathlib import Path
import subprocess,json,re,csv
from PIL import Image,ImageDraw,ImageFont
ROOT=Path.cwd(); OUT=ROOT/'chair_test_v2_review/evidence'; OUT.mkdir(exist_ok=True)
font=ImageFont.truetype('/System/Library/Fonts/Monaco.ttf',16)
def probe(p):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]))
def grab(p,t,d):
 subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',str(p),'-frames:v','1','-vf','scale=640:-1','-y',str(d)],check=True)
def sheet(items,d,cols=4,w=256,h=480):
 im=Image.new('RGB',(cols*w,((len(items)+cols-1)//cols)*h),'#dddddd');dr=ImageDraw.Draw(im)
 for i,(p,label) in enumerate(items):
  a=Image.open(p).convert('RGB');a.thumbnail((w-8,h-36));x=(i%cols)*w;y=(i//cols)*h
  im.paste(a,(x+(w-a.width)//2,y+26));dr.text((x+4,y+3),label,fill='black',font=font)
 im.save(d)
if __name__=='__main__':
 refs=[]
 for i,folder in enumerate(sorted((ROOT/'video_forensics_output').iterdir())):
  if not folder.is_dir():continue
  m=(folder/'00_source/SOURCE_MANIFEST.md').read_text(); candidates=[p for p in (ROOT/'videos').glob('*.mp4') if p.name in m]
  if not candidates and folder.name.startswith('Could you power'):candidates=list((ROOT/'videos').glob('*X97*'))
  p=candidates[0];meta=probe(p);s=next(s for s in meta['streams'] if s['codec_type']=='video');dur=float(s.get('duration',meta['format']['duration']));rid=f'R{i+1:02}'
  dest=OUT/rid;dest.mkdir(exist_ok=True);times=[round(dur*q,3) for q in [.02,.14,.28,.42,.56,.70,.84,.96]];items=[]
  for k,t in enumerate(times):
   f=dest/f'overview_{k+1:02}_{t:.3f}.jpg';grab(p,t,f);items.append((f,f'{rid} {t:.3f}s'))
  sheet(items,OUT/f'{rid}_overview.jpg',4,300,560 if s['height']>s['width'] else 205)
  refs.append(dict(id=rid,slug=folder.name,source=str(p),duration=dur,width=s['width'],height=s['height'],audio=any(s['codec_type']=='audio' for s in meta['streams']),times=times))
 (OUT/'sources.json').write_text(json.dumps(refs,indent=2))
 p=Path('/Users/ghilmankhan/Downloads/0921.mp4');(OUT/'failed_probe.json').write_text(json.dumps(probe(p),indent=2)); dest=OUT/'failed';dest.mkdir(exist_ok=True)
 subprocess.run(['ffmpeg','-v','error','-i',str(p),'-vf','fps=4,scale=270:-1','-y',str(dest/'f%04d.jpg')],check=True)
 fs=sorted(dest.glob('f*.jpg'))
 for start in range(0,len(fs),24):sheet([(f,f'{(j+start)/4:.2f}s') for j,f in enumerate(fs[start:start+24])],OUT/f'failed_{start//24+1:02}.jpg',6,200,385)
 print(json.dumps(refs,indent=2))
