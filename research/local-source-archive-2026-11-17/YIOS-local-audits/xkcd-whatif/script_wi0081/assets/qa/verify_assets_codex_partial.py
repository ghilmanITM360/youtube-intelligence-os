"""WI-0081 partial pack verifier. Unimplemented visual checks are explicitly reported."""
from pathlib import Path
import csv,hashlib,json,re,sys
from PIL import Image
import numpy as np
R=Path(__file__).resolve().parents[2]; Q=R/'assets/qa'; sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def longest(a):
 z=np.pad(a.astype('int8'),(1,1)); d=np.diff(z); starts=np.flatnonzero(d==1); ends=np.flatnonzero(d==-1); return int((ends-starts).max()) if len(starts) else 0
rows=list(csv.DictReader((R/'assets/MANIFEST.csv').open())); specs=json.loads((Q/'spec_inventory.json').read_text()); results=[]; raw=list((R/'assets/raw').glob('*.png')); raw_hash={sha(p):p for p in raw}; (Q/'cutouts').mkdir(exist_ok=True)
for r in rows:
 p=R/r['filename']; aid=r['asset_id']; c={'exists':p.is_file()}
 if p.is_file():
  im=Image.open(p); c['sha256']=sha(p)==r['sha256'];c['manifest_size_mode']=im.size==(int(r['width']),int(r['height'])) and im.mode==r['mode']
  s=specs.get(aid,{}).get('spec',''); z=re.search(r'\*\*Output:\*\*\s*(\d+)x(\d+)',s);c['output_size']=im.size==tuple(map(int,z.groups())) if z else 'UNVERIFIED'
  if r.get('native_sha256'):
   n=raw_hash.get(r['native_sha256']);c['native_hash_exists']=bool(n);c['native_size']=bool(n) and Image.open(n).size==(int(r['native_w']),int(r['native_h']))
  if aid=='PIPE-01':c['master_identity']=sha(p)=='12b1f42ea48d0eb88c1b0fd63237904fd547d478fc7bf8a03bfdd67e3833ad9c'
  if im.mode=='RGBA':
   arr=np.asarray(im); a=arr[:,:,3]; strip=Image.new('RGB',(im.width*3,im.height))
   for i,bg in enumerate(('#f8f8f8','#0c0c0c','#ff00ff')):
    b=Image.new('RGBA',im.size,bg);b.alpha_composite(im);strip.paste(b.convert('RGB'),(im.width*i,0))
   strip.save(Q/'cutouts'/f"{aid}-attempt{r['attempt']}-{p.stem}.png")
   if aid.startswith(('CHR-V','CHR-X','CHR-P')):
    m=(arr[:,:,0]>190)&(arr[:,:,1]>220)&(arr[:,:,2]>190)&(a>10);ratio=float((a[m]==255).mean()) if m.any() else 0.; c['mint_alpha255_fraction']=round(ratio,6);c['head_opacity_heuristic_pass']=ratio>=.995
    if aid.startswith('CHR-V'):
     ys,xs=np.where(a>200)
     if len(ys):
      height=int(ys.max()-ys.min()+1); head=np.where(m);head_height=int(head[0].max()-head[0].min()+1) if m.any() else 0;c['figure_bounds_y']=[int(ys.min()),int(ys.max())];c['head_figure_ratio']=round(head_height/height,4)
    c['D0_no_floor_line']=all(longest(a[y]>40)<=150 for y in range(min(1000,a.shape[0]),a.shape[0]))
 results.append({'id':aid,'attempt':r['attempt'],'file':r['filename'],'status':r['status'],'checks':c})
gen=[i for i,s in specs.items() if '/ GEN /' in s['spec']]; done={r['asset_id'] for r in rows if r['generated_or_code']=='generated'}; accepted={r['asset_id'] for r in rows if r['generated_or_code']=='generated' and r['status']=='PASS'}
report={'master_ok':sha(R/'inputs/ALIEN_MASTER_001.png')=='12b1f42ea48d0eb88c1b0fd63237904fd547d478fc7bf8a03bfdd67e3833ad9c','gen_required':len(gen),'gen_attempted':len(done),'gen_approved':len(accepted),'gen_unattempted':[i for i in gen if i not in done], 'model_sheet':'FAILED: three builds, view figure proportions and foot baselines differ', 'not_run':['Full A verification of all required assets','B full visual review and all 14 poses','C eye, mouth, neck and spill checks','D pose alignment','E through J: missing downstream assets','Human review S16-S25, voice approval and wording decisions C1-C5'], 'results':results}
(Q/'verify_assets_output.json').write_text(json.dumps(report,indent=2)); print(json.dumps({k:v for k,v in report.items() if k!='results'},indent=2));print('Checks per manifest row:')
for x in results:print(x['id'],x['attempt'],x['status'],json.dumps(x['checks']))
sys.exit(1)
