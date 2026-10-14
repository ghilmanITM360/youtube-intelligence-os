"""Generic temporal sampling: reads <V>/temporal_spec.txt lines 'sid|name|start|end|step'; reuses point frames at matching times."""
import hashlib, json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw
V = sys.argv[1]; W = Path(__file__).parent/V
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
s = json.loads((Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/casual-economics-deep-dive-2026-10/01_SOURCE_INVENTORY')/f'{V}.json').read_text())
pts = {float(f['source_seek_sec']): f for f in json.loads((W/'FRAME_MANIFEST.json').read_text())['frames']}
seqs = []
for k, line in enumerate(x for x in (W/'temporal_spec.txt').read_text().splitlines() if x):
    sid, name, a, b, step = line.split('|'); a, b, step = float(a), float(b), float(step)
    n = round((b-a)/step); frames = []
    for i in range(n+1):
        t = round(a+i*step, 3)
        if t in pts: p = pts[t]['local_frame']
        else:
            p = W/'temporal'/f'{sid}_{t:.3f}.jpg'
            if not p.exists(): subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.3f}', '-i', s['actual_path'], '-frames:v', '1', '-q:v', '3', str(p)], check=True)
        frames.append(dict(time_sec=t, local_frame=str(p), sha256=sha(p)))
    seqs.append(dict(sequence_id=sid, name=name, start_sec=frames[0]['time_sec'], end_sec=frames[-1]['time_sec'], frames=frames))
(W/'TEMPORAL_MANIFEST.json').write_text(json.dumps(seqs, indent=1))
w = 256; h = 144
for g in range(0, len(seqs), 4):
    grp = seqs[g:g+4]; cols = max(len(z['frames']) for z in grp)
    S = Image.new('RGB', (cols*w, len(grp)*(h+14)), 'white'); d = ImageDraw.Draw(S)
    for r, z in enumerate(grp):
        for c, f in enumerate(z['frames']):
            S.paste(Image.open(f['local_frame']).resize((w, h)), (c*w, r*(h+14)+14)); d.text((c*w+2, r*(h+14)+1), f"{z['sequence_id']} {f['time_sec']}", fill='black')
    S.save(W/f'temporal_{g//4:02d}.jpg', quality=80)
print(len(seqs), 'sequences', sum(len(z['frames']) for z in seqs), 'frame entries')
