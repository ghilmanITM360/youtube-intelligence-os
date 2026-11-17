import json,sys,hashlib,shutil,struct
from pathlib import Path
root=Path(__file__).parent
rows=json.loads((root/'_manifest.json').read_text());ev=json.loads(sys.argv[1]);r=next(r for r in rows if r['id']==ev['id'])
if ev.get('source'):
 src=Path(ev['source']);dst=root/r['file']
 if dst.exists() and ev.get('revision'):
  archive=root/'_revisions';archive.mkdir(exist_ok=True)
  old=archive/(dst.stem+'_initial.png');assert not old.exists();dst.rename(old)
  r.setdefault('history',[]).append(dict(file=str(old),source=r['source'],sha256=r['sha256']))
 assert not dst.exists(),dst
 shutil.copy2(src,dst);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(src)==sha(dst)
 w,h,depth,color=struct.unpack('>IIBB',dst.read_bytes()[16:26]);r.update(status='generated — awaiting approval',source=str(src),sha256=sha(dst),actual_size=[w,h],png_color_type=color)
else:
 r.update(status='failed',error=ev['error'])
 with (root/'_failed.txt').open('a') as f:f.write(r['id']+': '+ev['error']+'\n')
(root/'_manifest.json').write_text(json.dumps(rows,indent=2))
lines=['# Two Mornings — v3 cast and location review','','Story shots and FX await owner approval of these masters. Default master: a. Originals preserved; copies verified with SHA-256. Built-in image generation. Prompts and provenance: `_manifest.json`; full brief: `_source_prompts.txt`.','','| ID | File | References attached | Actual pixels | Status |','|---|---|---|---|---|']
for x in rows:
 refs=', '.join(next(y['file'] for y in rows if y['id']==ref) for ref in x['refs']) or 'None'
 lines.append('| '+x['id']+' | ['+x['file']+']('+x['file']+') | '+refs+' | '+' × '.join(map(str,x.get('actual_size',[])))+' | '+x['status']+' |')
(root/'_index.md').write_text('\n'.join(lines)+'\n');print(r['id'],r['status'],r.get('actual_size'))
