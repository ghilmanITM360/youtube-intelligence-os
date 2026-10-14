"""Generic scratch prep: verify source, 4s point frames, contact sheets, captions, metadata, thumbnail, audio stats.
Usage: prep_video.py VIDEO_ID PREFIX   (re-runnable; skips existing frames)"""
import hashlib, json, re, subprocess, sys, urllib.request, datetime
from pathlib import Path
from PIL import Image, ImageDraw
V, PFX = sys.argv[1], sys.argv[2]
R = Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os'); D = R/'research/casual-economics-deep-dive-2026-10'
W = Path(__file__).parent/V; (W/'frames').mkdir(parents=True, exist_ok=True); (W/'temporal').mkdir(exist_ok=True)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
s = json.loads((D/'01_SOURCE_INVENTORY'/f'{V}.json').read_text()); src = s['actual_path']; dur = s['actual_duration_sec']
if not (W/'SOURCE_OK').exists():
    assert sha(src) == s['actual_sha256'], 'SOURCE MISMATCH'; (W/'SOURCE_OK').write_text(s['actual_sha256'])
def grab(t, out):
    if not out.exists():
        subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.3f}', '-i', src, '-frames:v', '1', '-q:v', '3', str(out)], check=True)
times = [float(t) for t in range(0, int(dur), 4)]
if dur - times[-1] >= .25: times.append(round(dur - .1, 3))
frames = []
for i, t in enumerate(times):
    out = W/'frames'/f'{i:03d}_{t:.3f}.jpg'; grab(t, out)
    frames.append(dict(observation_id=f'{PFX}{i:03d}', source_seek_sec=int(t) if t == int(t) else t, local_frame=str(out), frame_sha256=sha(out)))
(W/'FRAME_MANIFEST.json').write_text(json.dumps(dict(video_id=V, source_sha256=s['actual_sha256'], sampling='POINT_SAMPLES_NOT_SHOT_SEGMENTATION', frames=frames), indent=1))
def sheet(paths, labels, out, cols=5, w=320):
    ims = [Image.open(p) for p in paths]; h = int(w*ims[0].height/ims[0].width); rows = -(-len(ims)//cols)
    S = Image.new('RGB', (cols*w, rows*(h+16)), 'white'); d = ImageDraw.Draw(S)
    for k, (im, lb) in enumerate(zip(ims, labels)):
        x, y = k % cols*w, k//cols*(h+16); S.paste(im.resize((w, h)), (x, y+16)); d.text((x+3, y+2), lb, fill='black')
    S.save(out, quality=80)
for k in range(0, len(frames), 20):
    out = W/f'sheet_{k//20:02d}.jpg'
    if not out.exists(): sheet([f['local_frame'] for f in frames[k:k+20]], [f"{f['observation_id']} {f['source_seek_sec']}s" for f in frames[k:k+20]], out)
recs = json.loads((W.parent/'normalized-records.json').read_text()); recs = recs.get('records', recs) if isinstance(recs, dict) else recs
recs = recs if isinstance(recs, list) else list(recs.values())
meta = next((r for r in recs if isinstance(r, dict) and r.get('youtube_video_id') == V), None)
if meta: (W/'METADATA.json').write_text(json.dumps({k: v for k, v in meta.items() if k != 'transcript'}, indent=2))
srt = json.loads((R/'data/extracted/channel-data/DS-000036/caption-tracks.json').read_text())['tracks'][V]['srt']
(W/'captions-readable.txt').write_text('\n'.join(' '.join(b.splitlines()) for b in re.split(r'\n\s*\n', srt.strip()) if len(b.splitlines()) >= 3 and ' '.join(b.splitlines()[2:]).strip()))
if not (W/'thumbnail.jpg').exists():
    url = f'https://i.ytimg.com/vi/{V}/maxresdefault.jpg'; b = urllib.request.urlopen(url, timeout=30).read(); (W/'thumbnail.jpg').write_bytes(b)
    (W/'THUMBNAIL_PROVENANCE.json').write_text(json.dumps(dict(video_id=V, url=url, retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat(), sha256=hashlib.sha256(b).hexdigest(), bytes=len(b), historical_thumbnail_bytes='NOT_AVAILABLE_FOR_COMPARISON', note='Current public CDN image; not certified upload-time thumbnail.'), indent=2)+'\n')
if not (W/'audio_exit.txt').exists():
    p = subprocess.run(['ffmpeg', '-hide_banner', '-i', src, '-vn', '-af', 'astats=measure_perchannel=none', '-f', 'null', '-'], capture_output=True, text=True)
    (W/'audio_signal.log').write_text(p.stderr); (W/'audio_exit.txt').write_text(str(p.returncode))
print(V, len(frames), 'frames', -(-len(frames)//20), 'sheets; meta', bool(meta), 'dur', dur)
