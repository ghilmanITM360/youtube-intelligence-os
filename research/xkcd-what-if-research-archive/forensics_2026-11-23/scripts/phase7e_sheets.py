"""Contact sheets for the ten episode studies: 16 frames per episode = frames at the ASR time (+0.8 s) of each checked claim (up to 9) + evenly spaced fill across the video.
Frames are native-resolution grabs from the library MP4 at the stated time; the sheet shows them at 480x270 with the time. Writes phase7e_frames/ and 07e_EPISODE_SHEET_FRAMES.csv.
usage: uv run --no-project --with pillow python scripts/phase7e_sheets.py"""
import csv, os, subprocess, sys
from PIL import Image, ImageDraw
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = A + '/phase7e_frames'; os.makedirs(OUT, exist_ok=True)
inv = {r['video_id']: r for r in csv.DictReader(open(A + '/03_CHANNEL_MASTER_INVENTORY.csv'))}
cl = list(csv.DictReader(open(A + '/07e_EPISODE_CLAIM_CHECKS.csv')))
eps = []
for r in cl:
    if r['video_id'] not in [e for e, _ in eps]: eps.append((r['video_id'], r['episode']))
rows = []
for v, title in eps:
    dur = float(inv[v]['duration_s_ffprobe']); anchors = []
    for r in cl:
        if r['video_id'] == v and r['asr_time_s']:
            t = min(dur - 0.5, float(r['asr_time_s']) + 0.8)
            if all(abs(t - a[0]) > 2 for a in anchors) and len(anchors) < 9: anchors.append((t, r['claim_id']))
    n_fill = 16 - len(anchors); fill = [((i + 0.5) * dur / n_fill, 'fill') for i in range(n_fill)]
    fill = [f for f in fill if all(abs(f[0] - a[0]) > 3 for a in anchors)]
    pts = sorted(anchors + fill)[:16]
    while len(pts) < 16: pts.append((dur * len(pts) / 17, 'fill'))
    pts = sorted(pts)
    tiles = []
    for t, tag in pts:
        jp = f'{OUT}/{v}_{t:.1f}.jpg'
        if not os.path.exists(jp):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', inv[v]['local_media_path'], '-frames:v', '1', '-vf', 'scale=960:-2', jp], check=True)
        tiles.append((jp, t, tag)); rows.append(dict(video_id=v, episode=title, t_s=round(t, 2), tag=tag, frame=os.path.relpath(jp, A), media_sha256_prefix=inv[v]['sha256'][:12]))
    sheet = Image.new('RGB', (1920, 1080), 'white'); d = ImageDraw.Draw(sheet)
    for i, (jp, t, tag) in enumerate(tiles):
        im = Image.open(jp).convert('RGB'); im.thumbnail((480, 270)); x, y = (i % 4) * 480, (i // 4) * 270
        sheet.paste(im, (x, y)); d.rectangle([x, y, x + 150, y + 16], fill='black'); d.text((x + 3, y + 2), f'{t:.1f}s {tag}', fill='yellow')
    sheet.save(f'{OUT}/SHEET_{v}.jpg', quality=88); print(v, title, len(tiles), 'frames', 'dur', dur, file=sys.stderr)
w = csv.DictWriter(open(A + '/07e_EPISODE_SHEET_FRAMES.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), 'frames', len(eps), 'sheets')
