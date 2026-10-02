"""Read-only source inventory; hashes identify bytes, never visual equivalence."""
import csv, hashlib, io, json, re, zipfile
from pathlib import Path
from collections import Counter
from PIL import Image
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
IMAGES={'.jpg','.jpeg','.png','.webp','.avif','.gif','.bmp','.tif','.tiff'}
rows=[]; errors=[]
def visit(data, location, depth=0):
    ext=Path(location).suffix.lower(); digest=hashlib.sha256(data).hexdigest()
    row={'location':location,'extension':ext,'bytes':len(data),'sha256':digest,'asset_id':'AS-'+digest,'width':'','height':'','decode_status':'NOT_IMAGE','inspection_status':'NOT_INSPECTED','role':'SUPPORTING_FILE'}
    if ext in IMAGES:
        row['role']='IMAGE_UNCLASSIFIED'
        if '/forensic-analysis/' in location: row['role']='FORENSIC_SUPPORT_IMAGE_PENDING_REVIEW'
        if 'thumbnail-snapshots/' in location: row['role']='REGISTERED_THUMBNAIL'
        if 'Screenshot' in location: row['role']='SCREENSHOT_PENDING_THUMBNAIL_EXTRACTION'
        if '/preflight/' in location: row['role']='ACQUISITION_SCREENSHOT_PENDING_REVIEW'
        try:
            im=Image.open(io.BytesIO(data)); im.load()
            row.update(width=im.width,height=im.height,decode_status='ACCESSIBLE')
        except Exception as e: row['decode_status']='ERROR: '+str(e)
    rows.append(row)
    if ext in {'.zip','.xlsx','.docx','.pptx'}:
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                for member in z.infolist():
                    if member.is_dir(): continue
                    if depth>=12 or member.file_size>200_000_000:
                        errors.append({'location':location+'!/'+member.filename,'error':'RESOURCE_LIMIT_PENDING'});continue
                    try: visit(z.read(member),location+'!/'+member.filename,depth+1)
                    except Exception as e: errors.append({'location':location+'!/'+member.filename,'error':str(e)})
        except Exception as e: errors.append({'location':location,'error':str(e)})
for base in ['data','docs/research','channels']:
    for p in sorted((ROOT/base).rglob('*')):
        if p.is_file() and OUT not in p.parents and '__pycache__' not in p.parts:
            try: visit(p.read_bytes(),str(p.relative_to(ROOT)))
            except Exception as e: errors.append({'location':str(p.relative_to(ROOT)),'error':str(e)})
with (OUT/'asset-inventory.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
imgs=[r for r in rows if r['extension'] in IMAGES]
summary={'scope':['data','docs/research (excluding this output directory)','channels'],'file_and_member_occurrences':len(rows),'image_occurrences':len(imgs),'unique_image_byte_hashes':len({r['sha256'] for r in imgs}),'accessible_image_occurrences':sum(r['decode_status']=='ACCESSIBLE' for r in imgs),'visually_inspected_images':0,'excluded_images':0,'archive_occurrences':sum(r['extension']=='.zip' for r in rows),'nested_zip_occurrences':sum(r['extension']=='.zip' and '!/' in r['location'] for r in rows),'image_roles':dict(Counter(r['role'] for r in imgs)),'errors':errors}
(OUT/'inventory-summary.json').write_text(json.dumps(summary,indent=2))
assert len({r['location'] for r in rows})==len(rows), 'Duplicate member paths require disambiguation'
assert all(r['sha256'] and r['inspection_status']=='NOT_INSPECTED' for r in imgs)
print(json.dumps(summary,indent=2))
