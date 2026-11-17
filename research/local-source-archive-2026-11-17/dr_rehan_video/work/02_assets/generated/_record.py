import sys,json,hashlib,shutil,struct
from pathlib import Path

root=Path(__file__).parent
rows=json.loads((root/'_manifest.json').read_text())
event=json.loads(sys.argv[1])
row=next(r for r in rows if r['id']==event['id'])
if event.get('source'):
    source=Path(event['source']); dest=root/row['file']
    if dest.exists():
        raise RuntimeError('Refusing to overwrite '+str(dest))
    shutil.copy2(source,dest)
    digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    assert digest(source)==digest(dest)
    data=dest.read_bytes()
    width,height,depth,color=struct.unpack('>IIBB',data[16:26])
    row.update(status='generated',source=str(source),sha256=digest(dest),actual_size=[width,height],png_color_type=color)
else:
    row.update(status='failed',error=event['error'])
    with (root/'_failed.txt').open('a') as f:f.write(row['id']+' '+row['file']+': '+event['error']+'\n')
(root/'_manifest.json').write_text(json.dumps(rows,indent=2))
lines=['# Dr. Rehan image assets','','Generated using the built-in image tool. Original outputs preserved; copies verified with SHA-256. Requested and actual dimensions are listed separately. Generated does not imply visual QA passed.','','| Prompt ID | File | Status | Requested | Actual |','|---|---|---|---|---|']
for r in rows:
    size=lambda s:'×'.join(map(str,s))
    lines.append('| '+r['id']+' | '+r['file']+' | '+r['status']+' | '+size(r['size'])+' | '+size(r.get('actual_size',[]))+' |')
(root/'_index.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({k:row[k] for k in ['id','status','actual_size','png_color_type'] if k in row}))
