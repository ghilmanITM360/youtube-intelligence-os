"""Manifest only durable pilot files, excluding dependencies and inspection caches."""
import hashlib,json
from pathlib import Path
root=Path.cwd();excluded={'node_modules','.cache','.bundle','qa_frames','reference_clips','__pycache__'}
files=[]
for p in sorted(root.rglob('*')):
 rel=p.relative_to(root)
 if not p.is_file() or any(x in excluded for x in rel.parts) or rel.as_posix()=='evidence/FILE_HASHES.json' or p.suffix=='.log':continue
 files.append({'path':rel.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
Path('evidence/FILE_HASHES.json').write_text(json.dumps({'scope':'durable pilot inputs, source caches, source hashes and outputs; manifest excludes itself','files':files},indent=2))
print(f'Hashed {len(files)} durable files / {sum(x["bytes"]for x in files):,} bytes')
