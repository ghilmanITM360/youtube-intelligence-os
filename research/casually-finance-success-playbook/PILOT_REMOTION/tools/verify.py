"""Final deliverable integrity gate, without rerunning the channel audit."""
import hashlib,json,re,subprocess
from pathlib import Path
root=Path.cwd();manifest=json.loads(Path('evidence/FILE_HASHES.json').read_text())
for item in manifest['files']:
 p=root/item['path'];assert p.is_file(),p;assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],p
repo=root.parents[2];source=json.loads(Path('evidence/attribution-and-sources.json').read_text())
for item in source['files']:
 if item['path'].startswith('research/') and item['path'].endswith('.md'):
  data=subprocess.check_output(['git','show',source['source_playbook_commit']+':'+item['path']],cwd=repo)
 else:data=(repo/item['path']).read_bytes()
 assert hashlib.sha256(data).hexdigest()==item['sha256'],item['path']
qa=json.loads(Path('evidence/render-qa.json').read_text());assert qa['text_bounds_frames_checked']==1260;assert not qa['clipped_text'];assert not qa['black_frame_indices'];assert not qa['browser_errors'];assert len(qa['narration_coverage'])==8
assert qa['video_sha256']==hashlib.sha256(Path('render/fixed-mortgage-pilot.mp4').read_bytes()).hexdigest()
assert len(list(Path('assets').rglob('*.svg')))==21
seek=json.loads(Path('evidence/seek-determinism.json').read_text());assert seek['png_hash_first']==seek['png_hash_repeated']
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-of','json','evidence/motion-comparison.mp4']));assert abs(float(probe['format']['duration'])-10.2)<.01
missing=[]
for p in root.glob('*.md'):
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if '://' in link:continue
  if not (p.parent/link.split('#')[0]).exists():missing.append((p.name,link))
assert not missing,missing
print(f'PASS {len(manifest["files"])} pilot file hashes, 8 reused input hashes, 21 SVGs, final render/QA/comparison links, seek determinism')
