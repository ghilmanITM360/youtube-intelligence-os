#!/usr/bin/env python3
"""Channel-level AI-slop risk scan (proxy). Measures the channel/network signals the S-CTS paper names
(Ψ_A: cadence, templates, cross-channel reuse) on registry data. Outputs measured FACTS plus proxy flags;
a flag is not a detection verdict and a clean scan does not mean a channel "won't be detected".

  uv run python scripts/check_channel_slop_risk.py UC6IxnFzHofFJ5X2PycSMsww [--out DIR]
"""
import argparse, csv, json, re, sqlite3, statistics
from collections import Counter
from datetime import datetime, timedelta
from itertools import combinations
from pathlib import Path

from check_slop_risk import BOILERPLATE, COPY_FAIL, HASH_FAIL, PERSONA, REGISTRY, ROOT, TITLE_WARN, norm, shingles

LEDGER = ROOT / 'docs/research/thumbnail-forensics-2026-10-02/thumbnail-ledger.csv'


def thash(path):
    """dHash of the picture area only: Shorts thumbnails are pillarboxed, and the bars alone make unrelated images match."""
    from PIL import Image, ImageChops
    with Image.open(path) as im:
        g = im.convert('L')
        box = ImageChops.difference(g, Image.new('L', g.size, g.getpixel((0, 0)))).point(lambda v: 255 if v > 12 else 0).getbbox()
        px = (g.crop(box) if box else g).resize((9, 8)).tobytes()
    return sum(1 << i for i, (a, b) in enumerate((px[r * 9 + c], px[r * 9 + c + 1]) for r in range(8) for c in range(8)) if a > b)


def jac(a, b):
    a, b = set(norm(a).split()), set(norm(b).split())
    return len(a & b) / len(a | b) if a | b else 0.0


def load(channel):
    con = sqlite3.connect(f'file:{REGISTRY}?mode=ro', uri=True)
    rows = con.execute('select v.youtube_video_id, v.canonical_channel_id, v.title, v.published_at, v.video_type, v.duration_seconds, '
                       't.transcript_text from videos v left join transcripts t on t.youtube_video_id=v.youtube_video_id '
                       'and t.is_placeholder=0').fetchall()
    vids = [dict(id=r[0], ch=r[1], title=r[2] or '', date=r[3], type=r[4], dur=r[5], text=r[6] or '') for r in rows]
    own = [v for v in vids if v['ch'] == channel]
    if not own: raise SystemExit(f'{channel}: not in {REGISTRY.relative_to(ROOT)}')
    thumbs = {}
    if LEDGER.exists():
        for r in csv.DictReader(open(LEDGER)):
            p = Path(r['local_path'])
            if r['mapping_status'] == 'HASH_VERIFIED' and p.exists(): thumbs[r['youtube_video_id']] = p
    return own, [v for v in vids if v['ch'] != channel], thumbs


def scan(own, others, thumbs):
    f = {}
    # 1 cadence
    ds = sorted(datetime.fromisoformat(v['date'][:19]) for v in own if v['date'])
    gaps = [(b - a).total_seconds() / 86400 for a, b in zip(ds, ds[1:])]
    max7 = max(sum(1 for d in ds if s <= d < s + timedelta(days=7)) for s in ds) if ds else 0
    same_day = sum(c - 1 for c in Counter(d.date() for d in ds).values() if c > 1)
    f['cadence'] = dict(videos=len(own), first=str(ds[0].date()) if ds else None, last=str(ds[-1].date()) if ds else None,
                        by_type=dict(Counter(v['type'] for v in own)), median_gap_days=round(statistics.median(gaps), 1) if gaps else None,
                        max_uploads_in_7_days=max7, extra_same_day_uploads=same_day)
    # 2 title template (within channel)
    pre = Counter(' '.join(norm(v['title']).split()[:2]) for v in own)
    pairs = [(a['id'], b['id'], round(jac(a['title'], b['title']), 2)) for a, b in combinations(own, 2)]
    f['titles'] = dict(top_2word_prefixes=pre.most_common(5), mean_pair_jaccard=round(statistics.mean(p[2] for p in pairs), 3) if pairs else 0,
                       near_duplicate_pairs=[p for p in pairs if p[2] >= TITLE_WARN])
    # 3 script reuse within channel / 4 across channels
    sh = {v['id']: shingles(v['text']) for v in own}
    osh = [(f"{v['ch']}/{v['id']}", shingles(v['text'])) for v in others if v['text']]
    typ = {v['id']: v['type'] for v in own}
    intra, cross = [], []
    for v in own:
        A = sh[v['id']]
        if len(A) < 20: continue
        best = max(((len(A & sh[w]) / len(A), w) for w in sh if w != v['id']), default=(0, None))
        if best[0] >= COPY_FAIL: intra.append(dict(video=v['id'], type=v['type'], overlaps=best[1], other_type=typ[best[1]], share=round(best[0], 3)))
        xb = max(((len(A & B) / len(A), k) for k, B in osh), default=(0, None))
        cross.append((round(xb[0], 3), v['id'], xb[1]))
    cross.sort(reverse=True)
    f['script_reuse_within'] = dict(threshold=COPY_FAIL, videos_with_transcript=sum(len(s) >= 20 for s in sh.values()),
                                    hits=sorted(intra, key=lambda h: -h['share']),
                                    hit_types=dict(Counter(f"{h['type']}->{h['other_type']}" for h in intra)))
    f['script_reuse_cross_channel'] = dict(compared_against=len(osh), max_share=cross[0] if cross else None,
                                           over_threshold=[c for c in cross if c[0] >= COPY_FAIL], top5=cross[:5])
    # cross-channel title near-duplicates
    xt = [(v['id'], f"{w['ch']}/{w['id']}", round(jac(v['title'], w['title']), 2)) for v in own for w in others]
    f['titles_cross_channel'] = [t for t in xt if t[2] >= TITLE_WARN][:20]
    # 5 thumbnails
    oh = {v['id']: thash(thumbs[v['id']]) for v in own if v['id'] in thumbs}
    xh = {k: thash(p) for k, p in thumbs.items() if k not in oh}
    ham = lambda a, b: bin(a ^ b).count('1')
    f['thumbnails'] = dict(own_hashed=len(oh), others_hashed=len(xh), hash_fail=HASH_FAIL,
                           within=[(a, b, ham(oh[a], oh[b])) for a, b in combinations(oh, 2) if ham(oh[a], oh[b]) <= HASH_FAIL],
                           cross=[(a, b, ham(h, g)) for a, h in oh.items() for b, g in xh.items() if ham(h, g) <= HASH_FAIL])
    # 6 persona / boilerplate
    bp = Counter(p for v in own for p in BOILERPLATE if p in v['text'].lower())
    f['persona_boilerplate'] = dict(persona_videos=[v['id'] for v in own if PERSONA.search(v['text'])],
                                    boilerplate_phrase_hits=bp.most_common(10),
                                    videos_with_any_boilerplate=sum(any(p in v['text'].lower() for p in BOILERPLATE) for v in own))
    return f


def flags(f, n):
    c, out = f['cadence'], []
    if c['max_uploads_in_7_days'] >= 7 or c['extra_same_day_uploads'] >= 3: out.append('CADENCE: burst uploads')
    if f['titles']['mean_pair_jaccard'] >= 0.3 or len(f['titles']['near_duplicate_pairs']) >= 3: out.append('TITLES: templated within channel')
    if f['script_reuse_within']['hits']: out.append(f"SCRIPT: {len(f['script_reuse_within']['hits'])} videos reuse ≥{COPY_FAIL:.0%} of another own video {f['script_reuse_within']['hit_types']}")
    if f['script_reuse_cross_channel']['over_threshold'] or f['titles_cross_channel']: out.append('NETWORK: script/title overlap with other channels')
    if f['thumbnails']['within'] or f['thumbnails']['cross']: out.append('THUMBNAILS: near-identical hashes')
    if f['persona_boilerplate']['persona_videos']: out.append('PERSONA: expert self-claims')
    if f['persona_boilerplate']['videos_with_any_boilerplate'] >= n / 2: out.append('BOILERPLATE: generic phrases in ≥half of videos')
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('channel', help='YouTube channel id as stored in the registry (UC...)')
    ap.add_argument('--out', default='docs/research/channel-slop-risk')
    a = ap.parse_args()
    own, others, thumbs = load(a.channel)
    f = scan(own, others, thumbs)
    rep = dict(channel=a.channel, title=f"{own[0]['ch']}", generated=datetime.now().isoformat(timespec='seconds'),
               source=str(REGISTRY.relative_to(ROOT)), note='Proxy signals only; not a platform detection verdict.',
               proxy_flags=flags(f, len(own)), findings=f)
    out = ROOT / a.out; out.mkdir(parents=True, exist_ok=True)
    p = out / f"{a.channel}-{datetime.now():%Y-%m-%d}.json"
    p.write_text(json.dumps(rep, indent=1, ensure_ascii=False, default=str))
    print(json.dumps(rep, indent=1, ensure_ascii=False, default=str)[:6000]); print('\nwrote', p.relative_to(ROOT))


if __name__ == '__main__':
    main()
