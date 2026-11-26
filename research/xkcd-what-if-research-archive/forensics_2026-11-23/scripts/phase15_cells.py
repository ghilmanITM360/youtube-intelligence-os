"""Phase 15 (literal Phase 6.4 per owner decision 2026-11-23): build per-shot cells and numbered sheets for scene coding.
Cell = label bar + 3 stills [start+0.2 s | middle | end-0.2 s] (clamped inside the shot). Sheets: 6 cells each, in shot order per video.
usage: uv run --no-project --with pillow python scripts/phase15_cells.py <tranche_name> <video_id> [<video_id> ...]
writes phase15_scene_coding/<tranche>_context.csv (one row per shot, prefilled narration) and sheets/<tranche>_<video>_<n>.jpg"""
import csv, os, subprocess, sys
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(__file__))
from ledger_lib import media
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P = A + '/phase15_scene_coding'
tr, vids = sys.argv[1], sys.argv[2:]
import json
CAMP = '/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/videos/'
shots = [r for r in csv.DictReader(open(A + '/ledgers_measured/ALL_SHOT_LEDGER.csv'))]
audit_ids = {r['video_id'] for r in shots}
def full_asr(v, st, en, fallback):
    for d in ('phase7b_asr', 'phase7c_asr'):
        f = f'{A}/{d}/{v}.json'
        if os.path.exists(f):
            t = json.load(open(f))['transcription']
            x = ' '.join(g['text'].strip() for g in t if g['offsets']['to'] / 1000 > st and g['offsets']['from'] / 1000 < en)
            return x
    return fallback
def campaign_rows(v):
    asr = json.load(open(CAMP + v + '/asr/asr_small_en.json'))['segments']; out = []
    for r in csv.DictReader(open(CAMP + v + '/shot_ledger.csv')):
        st, en = float(r['start_pts_seconds']), float(r['end_pts_seconds'])
        out.append(dict(video_id=v, shot_id=r['shot_id'], start_pts_seconds=st, end_pts_seconds=en, events_in_shot='', boundary_strength='',
                        asr_text=' '.join(g['text'].strip() for g in asr if g['end'] > st and g['start'] < en)))
    return out
inv = {r['video_id']: r for r in csv.DictReader(open(A + '/03_CHANNEL_MASTER_INVENTORY.csv'))}
def grab(v, t, jp):
    if os.path.exists(jp): return
    tmp = jp + '.png'
    for tt in (t, t - 0.3, t - 0.6, t - 1.0):
        r = subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{max(tt, 0):.3f}', '-i', media(v), '-frames:v', '1', tmp])
        if r.returncode == 0 and os.path.exists(tmp): break
    Image.open(tmp).convert('RGB').save(jp, quality=82); os.remove(tmp)
rows = []
for v in vids:
    S = [r for r in shots if r['video_id'] == v] if v in audit_ids else campaign_rows(v); S.sort(key=lambda r: float(r['start_pts_seconds'])); islong = inv[v]['format'].upper().startswith('LONG')
    W = 400 if islong else 170; cells = []
    for i, r in enumerate(S):
        st, en = float(r['start_pts_seconds']), float(r['end_pts_seconds']); d = en - st
        ts = [st + min(0.2, d / 3), st + d / 2, en - min(0.2, d / 3) - 0.04]
        ims = []
        for k, t in enumerate(ts):
            jp = f'{P}/cells/{v}_{r["shot_id"]}_{k}.jpg'; grab(v, t, jp); im = Image.open(jp); ims.append(im.resize((W, int(W * im.height / im.width))))
        h = ims[0].height; cell = Image.new('RGB', (W * 3 + 4, h + 18), 'white'); dr = ImageDraw.Draw(cell)
        dr.text((3, 3), f'{v} {r["shot_id"]}  {st:.2f}-{en:.2f}s ({d:.1f}s)  #{i+1}/{len(S)}', fill='black')
        for k, im in enumerate(ims): cell.paste(im, (k * (W + 2), 18))
        cells.append(cell)
        rows.append(dict(video_id=v, shot_id=r['shot_id'], n_in_video=i + 1, of=len(S), start_s=f'{st:.3f}', end_s=f'{en:.3f}', dur_s=f'{d:.2f}', fmt='LONG' if islong else 'SHORT', events_in_shot=r['events_in_shot'], layer=('AUDIT' if v in audit_ids else 'CAMPAIGN'), boundary_strength=r['boundary_strength'], asr_text=(full_asr(v, st, en, r['asr_text']) if v in audit_ids else r['asr_text']), sheet=f'sheets/{tr}_{v}_{i // 6 + 1}.jpg', pos_in_sheet=i % 6 + 1))
    for j in range(0, len(cells), 6):
        g = cells[j:j + 6]; sh = Image.new('RGB', (g[0].width, sum(c.height for c in g)), 'white'); y = 0
        for c in g: sh.paste(c, (0, y)); y += c.height
        sh.save(f'{P}/sheets/{tr}_{v}_{j // 6 + 1}.jpg', quality=80)
w = csv.DictWriter(open(f'{P}/{tr}_context.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows); print(len(rows), 'shots', len(vids), 'videos')
