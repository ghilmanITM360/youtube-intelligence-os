# Writes EVIDENCE_DOSSIER.md (computed evidence) per channel + a thumbnail montage (local, not committed).
import os, re, numpy as np, pandas as pd
from PIL import Image, ImageDraw
AUD = os.path.expanduser('~/YIOS-local-audits/finance-viral-forensics-2026-11-12')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = pd.read_pickle(f'{AUD}/out/forensics_dossier.pkl')
V = pd.read_pickle(f'{AUD}/out/forensics_videos.pkl')
os.makedirs(f'{AUD}/montage_forensics', exist_ok=True)
shape_owner = V.groupby('title_shape').channel_id.nunique()

def pct(x): return f"{100*x:.0f}%" if pd.notna(x) else 'n/a'
def fnum(x): return 'n/a' if pd.isna(x) else (f"{x:,.0f}" if abs(x) >= 100 else f"{x:.2f}")
def short(s, n): s = str(s or '').replace('\n', ' ').replace('|', '/'); return s if len(s) <= n else s[:n] + '…'

TF = ['t_number', 't_dollar', 't_question', 't_you', 't_fear_risk', 't_urgency', 't_secret_truth', 't_named_entity', 't_caps_word', 't_year']
HF = ['h_first_sentence_q', 'h_you_in_30s', 'h_number_30s', 'h_dollar_30s', 'h_stakes_30s', 'h_contrarian_30s', 'h_open_loop_30s', 'h_promise_30s', 'h_story_open', 'h_greeting_open', 'h_first_person_30s', 's_cta_end']
SF = ['tx_words', 's_num_density', 's_q_density', 's_but_density', 's_example_density', 's_data_density', 's_loop_density', 's_you_density', 's_wpm', 'h_title_overlap_150', 'i_promise_pos']

def montage(folder, W, U):
    tiles = [(r.video_id, 'W') for r in W.head(6).itertuples()] + [(r.video_id, 'U') for r in U.head(6).itertuples()]
    if not tiles: return None
    tw, th = 240, 135; im = Image.new('RGB', (tw * 6, th * 2 + 4), 'white')
    for i, (vid, k) in enumerate(tiles):
        p = f'{AUD}/thumbs/{vid}.jpg'
        row = 0 if k == 'W' else 1; col = i if k == 'W' else i - len([t for t in tiles if t[1] == 'W'])
        if os.path.exists(p):
            try: im.paste(Image.open(p).convert('RGB').resize((tw, th)), (col * tw, row * (th + 4)))
            except Exception: pass
        ImageDraw.Draw(im).text((col * tw + 3, row * (th + 4) + 2), f"{k}{col+1}", fill='yellow')
    out = f'{AUD}/montage_forensics/{folder}.png'; im.save(out); return out

for folder, x in D.items():
    C, d, L, W, U, T = x['C'], x['d'], x['L'], x['W'], x['U'], x['T']
    lines = [f"# Evidence dossier — {C['name']} ({folder})", '',
             'Computed, read-only evidence. Labels: topic/format = rule-based INFERRED tags; hook windows = word-position approximations (13/38/75 words ≈ 5/15/30 s at ~150 wpm; transcripts are untimed); PI = views ÷ median views of the 15 nearest-in-time uploads of the same channel & format (age-aware; not CTR/retention).', '']
    lines += [f"- Channel ID `{C.channel_id}` · handle {C.handle} · {C.url}", f"- Registered sub-niche: {C.sub_niche} · subscribers: {fnum(C.subscribers)} · availability: {C.availability} {short(C.availability_note,120)}",
              f"- Description: {short(C.description, 400)}"]
    if len(d) == 0:
        lines += ['', '**No videos in database.**']; open(f'{ROOT}/01_CHANNEL_REPORTS/{folder}/EVIDENCE_DOSSIER.md', 'w').write('\n'.join(lines)); continue
    nl, ns = (d.fmt == 'long').sum(), (d.fmt == 'short').sum()
    lines += [f"- Videos in DB {len(d)} (long {nl}, Shorts {ns}); views {d.views.notna().sum()}; transcripts {int(d.has_transcript.sum())} ({pct(d.has_transcript.mean())}); thumbnail images {int(d.thumb_file.sum())} ({pct(d.thumb_file.mean())}); FULL metadata {pct((d.metadata_level=='FULL').mean())}; PI-classified long {len(L)}",
              f"- Dates {d.pub_date.min()} → {d.pub_date.max()}; median views {fnum(d.views.median())}; p90 {fnum(d.views.quantile(.9))}; max {fnum(d.views.max())}"]
    ds = d[d.pub.notna()].sort_values('pub'); gaps = ds.pub.diff().dt.days.dropna()
    if len(ds) > 2:
        span_m = max((ds.pub.max() - ds.pub.min()).days / 30.4, 1)
        lines += [f"- Cadence: {len(ds)/span_m:.1f} uploads/month over {span_m:.1f} months; median gap {gaps.median():.1f} d; max gap {gaps.max():.0f} d; weekday mode {ds.pub.dt.day_name().mode().iat[0]}",
                  f"- Duration (min): median {d.duration_seconds.median()/60:.1f}; p10 {d.duration_seconds.quantile(.1)/60:.1f}; p90 {d.duration_seconds.quantile(.9)/60:.1f}; first-third median {ds.head(len(ds)//3).duration_seconds.median()/60:.1f} vs last-third {ds.tail(len(ds)//3).duration_seconds.median()/60:.1f}"]
        if len(L) >= 12:
            Lg = L.sort_values('pub').copy(); Lg['gap'] = Lg.pub.diff().dt.days
            r = Lg[['gap', 'PI']].corr(method='spearman').iloc[0, 1]
            Lg['dmin'] = Lg.duration_seconds / 60; rd = Lg[['dmin', 'PI']].corr(method='spearman').iloc[0, 1]
            third = len(Lg) // 3
            lines += [f"- Spearman(gap-before-upload, PI) = {r:.2f}; Spearman(duration, PI) = {rd:.2f}; median PI first third {Lg.head(third).PI.median():.2f} vs last third {Lg.tail(third).PI.median():.2f}"]
    if len(L): lines += [f"- PI classes (long): " + ', '.join(f"{k} {v}" for k, v in L.perf_class.value_counts().items()) + f"; near-duplicate-script flags {int(d.dup_script_flag.sum())}"]
    xs = d[d.title_shape.map(shape_owner) > 1]
    lines += [f"- Titles whose word-set also appears on another channel: {len(xs)} ({pct(len(xs)/len(d))})"]
    lines += ['', '## Topic map', '| topic | n | long | median views | median PI | succ/breakout | under | first | last |', '|---|---|---|---|---|---|---|---|---|']
    for r in T.sort_values('videos', ascending=False).head(12).itertuples():
        lines.append(f"| {r.topic} | {r.videos} | {r.long} | {fnum(r.median_views)} | {fnum(r.median_PI)} | {r.breakout_or_success} | {r.underperforming} | {r.first} | {r.last} |")
    fm = d.groupby('content_format').agg(n=('video_id', 'size'), mv=('views', 'median'), mpi=('PI', 'median')).sort_values('n', ascending=False)
    lines += ['', '## Title format mix', ' · '.join(f"{i}: n={r.n}, medPI={fnum(r.mpi)}" for i, r in fm.iterrows())]
    def block(name, X):
        out = ['', f'## {name}']
        for r in X.itertuples():
            out += [f"- **{short(r.title,110)}** — [{r.video_id}](https://www.youtube.com/watch?v={r.video_id}) · {r.pub_date} · {fnum(r.duration_seconds/60)} min · {fnum(r.views)} views · PI {r.PI:.2f} ({r.perf_class}) · {r.topic}/{r.content_format} · face={r.th_has_face} · thumb text: “{short(r.th_text,60)}”",
                    f"  - 0-30s: “{short(r.hook_30s, 430)}”",
                    f"  - end: “{short(r.ending_60w, 220)}”" + (f" · sources: {r.tx_sources}" if r.tx_sources else '') + (f" · desc links: {short(r.desc_urls,80)}" if r.desc_urls else '')]
        return out
    lines += block('Top PI long-form (winners)', W) + block('Bottom PI long-form (underperformers)', U)
    if ns:
        S = d[d.fmt == 'short'].sort_values('views', ascending=False)
        lines += ['', f'## Shorts ({ns}) — top / bottom by raw views (Shorts not PI-compared with long-form)']
        for r in pd.concat([S.head(4), S.tail(3)]).itertuples(): lines.append(f"- {short(r.title,90)} · {r.pub_date} · {fnum(r.views)} views · “{short(r.hook_15s,160)}”")
    if len(L) >= 8:
        top, bot = L.head(len(L) // 2), L.tail(len(L) // 2)
        lines += ['', '## Upper-half vs lower-half PI contrast (long-form; text proxies, correlation only)', '| feature | upper half | lower half |', '|---|---|---|']
        for f in TF + HF:
            if f in L: lines.append(f"| {f} | {pct(top[f].astype(float).mean())} | {pct(bot[f].astype(float).mean())} |")
        for f in SF + ['t_len', 'th_text_words', 'th_colorfulness']:
            if f in L: lines.append(f"| {f} (median) | {fnum(top[f].astype(float).median())} | {fnum(bot[f].astype(float).median())} |")
        lines.append(f"| thumbnail has face | {pct(top.th_has_face.astype(float).mean())} | {pct(bot.th_has_face.astype(float).mean())} |")
    src = d.tx_sources.str.split('; ').explode(); src = src[src.fillna('') != '']
    dom = d.desc_urls.str.split(' ').explode(); dom = dom[dom.fillna('') != '']
    lines += ['', '## Sources named (transcript/description) — counts of videos', ', '.join(f"{k} {v}" for k, v in src.value_counts().head(10).items()) or 'none detected',
              'Description link domains: ' + (', '.join(f"{k} {v}" for k, v in dom.value_counts().head(10).items()) or 'none')]
    m = montage(folder, W, U)
    lines += ['', f"Thumbnail montage (local, not committed): `{m}` (row 1 = winners W1-6, row 2 = underperformers U1-6)" if m else '']
    open(f'{ROOT}/01_CHANNEL_REPORTS/{folder}/EVIDENCE_DOSSIER.md', 'w').write('\n'.join(lines))
print('dossiers', len(D))
