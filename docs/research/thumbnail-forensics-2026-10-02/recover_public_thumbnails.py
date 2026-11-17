"""Zero-spend recovery of CURRENT public thumbnails for canonical videos with no local image.

Order per video: registered URL, then official i.ytimg.com variants (best first), stopping at the
first HTTP 200 that decodes as an image. Images are stored content-addressed; nothing is overwritten.
YouTube serves a 120x90 grey placeholder for some missing variants, so tiny images are rejected.
"""
import hashlib, io, json, sqlite3, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
DB = ROOT / 'data/catalog/youtube_channel_registry.db'
STORE = ROOT / 'data/raw/competitors/thumbnail-recovery-2026-10-04'
OUT = ROOT / 'data/manifests/thumbnail-recovery-2026-10-04.json'
VARIANTS = ['maxresdefault', 'sddefault', 'hq720', 'hqdefault', 'mqdefault', 'default']
UA = {'User-Agent': 'Mozilla/5.0 (research; public thumbnail fetch)'}
MIN_W = 300  # below this width the placeholder / default.jpg 120x90 is not a usable creative


def have_local():
    ids = set()
    for m in (ROOT / 'data/manifests').glob('DS-*-thumbnail-snapshot-*.json'):
        for s in json.loads(m.read_text())['snapshots']:
            ids.add(s['original_registered_url'].split('/vi/')[1].split('/')[0])
    return ids


def fetch(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b''
    except Exception as e:
        return 'ERR:' + type(e).__name__, b''


def recover(row):
    vid, reg = row
    urls = ([reg] if reg else []) + [f'https://i.ytimg.com/vi/{vid}/{v}.jpg' for v in VARIANTS]
    attempts, seen = [], set()
    for u in urls:
        if u in seen: continue
        seen.add(u)
        st, data = fetch(u)
        info = f'{u}|{st}|{len(data)}'
        if st == 200 and data:
            try:
                im = Image.open(io.BytesIO(data)); im.load()
                if im.width >= MIN_W:
                    attempts.append(info)
                    h = hashlib.sha256(data).hexdigest()
                    p = STORE / h[:2] / f'{h}.jpg'
                    p.parent.mkdir(parents=True, exist_ok=True)
                    if not p.exists(): p.write_bytes(data)
                    kind = 'RESOLVED_PRIMARY_URL' if u == reg else 'RESOLVED_ALT_VARIANT'
                    return dict(video_id=vid, status=kind, final_url=u, sha256=h, bytes=len(data), width=im.width,
                                height=im.height, path=str(p.relative_to(ROOT)), attempts=attempts,
                                captured_at=datetime.now(timezone.utc).isoformat())
                info += '|TOO_SMALL'
            except Exception:
                info += '|NOT_IMAGE'
        attempts.append(info)
    codes = {a.split('|')[1] for a in attempts}
    status = 'VIDEO_UNAVAILABLE' if codes <= {'404', '410'} else 'ACCESS_RESTRICTED' if codes & {'403', '401'} else 'UNKNOWN'
    return dict(video_id=vid, status=status, attempts=attempts, captured_at=datetime.now(timezone.utc).isoformat())


if __name__ == '__main__':
    local = have_local()
    rows = [r for r in sqlite3.connect(DB).execute("select youtube_video_id, coalesce(thumbnail_url,'') from videos order by 1") if r[0] not in local]
    print('to recover', len(rows), 'already local', len(local), flush=True)
    t = time.time()
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(recover, rows))
    OUT.write_text(json.dumps({'collected_at': datetime.now(timezone.utc).isoformat(), 'paid_apify': False,
                               'evidence_state': 'CURRENT_REMOTE_SNAPSHOT', 'results': res}, indent=1))
    from collections import Counter
    print(Counter(r['status'] for r in res), round(time.time() - t), 's')
