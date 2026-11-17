"""Prepare individual multiscale panels. Rendering is not inspection."""
import json,sys
from pathlib import Path
from PIL import Image,ImageDraw
OUT=Path(__file__).resolve().parent
batch=sys.argv[1] if len(sys.argv)>1 else 'B002-01'
u=json.loads((OUT/'thumbnail-ledger.json').read_text()); done={r['Thumbnail_ID'] for p in OUT.glob('individual-audit-batch-*.json') for r in json.loads(p.read_text())}
rows=[r for r in u if r['Thumbnail_ID'] not in done][:24]
dest=OUT/'inspection-panels'/batch;dest.mkdir(parents=True,exist_ok=True)
for i,r in enumerate(rows,1):
 im=Image.open(r['local_path']).convert('RGB')
 canvas=Image.new('RGB',(max(im.width,520),im.height+220),'#888888');canvas.paste(im,(0,20));d=ImageDraw.Draw(canvas)
 d.text((5,3),f"{batch}-{i:02d} | {r['video_id']} | native {im.width} x {im.height}",fill='white')
 for size,x in [((320,180),0),((160,90),340)]:
  small=im.copy();small.thumbnail(size,Image.Resampling.LANCZOS);canvas.paste(small,(x,im.height+40));d.text((x,im.height+24),str(size),fill='white')
 r['panel_path']=str(dest/f'{i:02d}.png');r['audit_id']=f'{batch}-{i:02d}';canvas.save(r['panel_path'])
(OUT/(batch.lower().replace('b','batch-',1)+'-selection.json')).write_text(json.dumps(rows,indent=2))
print([(r['audit_id'],r['video_id'],r['title']) for r in rows])
