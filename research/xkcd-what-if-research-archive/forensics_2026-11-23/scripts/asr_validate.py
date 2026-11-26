"""Validate every local whisper ASR file against its media (duration) and, where a catalog transcript exists, against that transcript (3-gram containment both ways).
For videos with no catalog transcript, report best 8-gram containment against all 83 catalog transcripts (reuse/parent check) and the ASR text head for title check.
Read-only on repo and media. Output: 03_ASR_VALIDATION.csv   Run: python3 -I scripts/asr_validate.py"""
import csv, json, re, os
from pathlib import Path
A = Path(__file__).resolve().parent.parent
RP = Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os')
RS = RP / 'research/what-if-scripts'
V = RP / 'research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/videos'
inv = {i['id']: i for i in json.load(open(RS / 'analysis/inventory.json'))}
probe = {r['video_id']: r for r in csv.DictReader(open(A / 'media_probe_88.csv'))}
inv_rows = {r['video_id']: r for r in csv.DictReader(open(A / '03_CHANNEL_MASTER_INVENTORY.csv'))}
tok = lambda t: re.findall(r"[a-z0-9']+", t.lower())
gr = lambda w, n: {tuple(w[i:i+n]) for i in range(len(w) - n + 1)}

def cat_text(vid):
    r = inv[vid]; return (RS / r['script']).read_text().split('## Script\n', 1)[1]

cat = {v: tok(cat_text(v)) for v in inv}
src = {}  # vid -> list of (source, path)
for v in os.listdir(V):
    p = V / v / 'asr/asr_small_en.json'
    if p.exists(): src.setdefault(v, []).append(('campaign', p))
for d, s in (('phase7b_asr', 'audit_7b'), ('phase7c_asr', 'audit_7c')):
    for f in (A / d).glob('*.json'): src.setdefault(f.stem, []).append((s, f))

def asr_text(p):
    j = json.load(open(p))
    if 'transcription' in j:
        segs = j['transcription']; return ' '.join(s['text'].strip() for s in segs), segs[-1]['offsets']['to'] / 1000
    segs = j.get('segments') or j.get('result', {}).get('segments') or []
    if segs: return ' '.join(s['text'].strip() for s in segs), segs[-1].get('end', 0)
    return j.get('text', ''), 0

rows = []
for v, lst in sorted(src.items()):
    for s, p in lst:
        try: t, end = asr_text(p)
        except Exception as e: t, end = '', 0
        w = tok(t); dur = float(probe[v]['duration']) if v in probe else None
        row = dict(video_id=v, asr_source=s, asr_path=str(p), asr_words=len(w), asr_end_s=round(end, 2), media_dur_s=round(dur, 2) if dur else '',
                   end_over_dur=round(end / dur, 3) if dur and end else '', title=inv_rows.get(v, {}).get('title', ''), catalog_words=len(cat[v]) if v in cat else '')
        if v in cat and w:
            a3, c3 = gr(w, 3), gr(cat[v], 3)
            row['cont_asr_in_catalog_3g'] = round(len(a3 & c3) / max(1, len(a3)), 3); row['cont_catalog_in_asr_3g'] = round(len(a3 & c3) / max(1, len(c3)), 3)
        else: row['cont_asr_in_catalog_3g'] = row['cont_catalog_in_asr_3g'] = ''
        if v not in cat and w:
            g8 = gr(w, 8); best = (0, '')
            for o, ow in cat.items():
                c = len(g8 & gr(ow, 8)) / max(1, len(g8))
                if c > best[0]: best = (c, o)
            row['best_8g_containment_in_catalog'] = round(best[0], 3); row['best_8g_video'] = best[1]
        else: row['best_8g_containment_in_catalog'] = row['best_8g_video'] = ''
        row['asr_head'] = ' '.join(w[:14])
        ok_dur = bool(dur and end and 0.9 <= end / dur <= 1.02)
        ok_txt = (row['cont_asr_in_catalog_3g'] != '' and row['cont_asr_in_catalog_3g'] >= 0.5)
        row['check'] = ('IDENTITY_CONFIRMED_VS_CATALOG' if (ok_dur and ok_txt) else
                        'DURATION_OK_NO_CATALOG_TEXT' if (ok_dur and v not in cat) else 'REVIEW')
        rows.append(row)
cols = list(rows[0]); w = csv.DictWriter(open(A / '03_ASR_VALIDATION.csv', 'w', newline=''), fieldnames=cols); w.writeheader(); w.writerows(rows)
import collections
print(len(rows), 'files', len({r['video_id'] for r in rows}), 'videos', collections.Counter(r['check'] for r in rows), collections.Counter(r['asr_source'] for r in rows))
for r in rows:
    if r['check'] != 'IDENTITY_CONFIRMED_VS_CATALOG': print(r['video_id'], r['asr_source'], r['check'], r['asr_end_s'], r['media_dur_s'], r['cont_asr_in_catalog_3g'], r['best_8g_containment_in_catalog'], r['best_8g_video'])
