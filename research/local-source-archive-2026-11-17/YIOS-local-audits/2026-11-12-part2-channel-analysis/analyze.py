# usage: python3 -I analyze.py   (stdlib only; DB opened read-only; writes only into this folder)
import sqlite3, os, re, math, json, csv, statistics as st, collections, datetime as dt
B = os.path.dirname(os.path.abspath(__file__))
DB = 'file:/Users/ghilmankhan/workprojects/yios-audit-fixes/data/catalog/finance_economics_complete.db?mode=ro'
AS_OF = dt.date(2026, 11, 11)   # dataset snapshot date (merge date); video age = AS_OF - publish date
TOPICS = [('Crypto/Bitcoin', r'bitcoin|crypto|ethereum|blockchain|\bbtc\b|stablecoin'),
 ('Stocks/Investing', r'stock|invest|etf|portfolio|dividend|nasdaq|s&p|market|bull|bear|shares|buffett|index fund'),
 ('Inflation/Recession/Macro', r'inflation|recession|gdp|fed\b|federal reserve|interest rate|economy|economic|depression|crash|crisis|tariff|deflation'),
 ('Debt/Banking', r'debt|bank|loan|mortgage|credit|bond|default|bailout'),
 ('Real Estate/Housing', r'real estate|housing|house|rent|property|landlord'),
 ('Money/Personal Finance', r'save|saving|budget|retire|401k|income|salary|wealth|rich|poor|millionaire|billionaire|money|tax|passive'),
 ('Geopolitics/Trade', r'china|russia|ukraine|war|trade|sanction|dollar|currency|oil|gold|brics|india|japan|europe|usa|america|nation|country|countries'),
 ('Business/Companies', r'company|business|apple|tesla|amazon|google|microsoft|nvidia|startup|ceo|brand|empire|\bai\b'),
 ('History/Explainers', r'history|rothschild|explained|why|how|truth|story|collapse|rise|fall')]
def topic(t):
    t = (t or '').lower()
    for n, rx in TOPICS:
        if re.search(rx, t): return n
    return 'Other/Unclassified'
def pdate(s):
    m = re.match(r'(20\d\d)-(\d\d)-(\d\d)(?:[T ](\d\d):(\d\d))?', s or '')
    if not m: return None, None
    d = dt.date(int(m[1]), int(m[2]), int(m[3])); h = int(m[4]) if (m[4] and len(s) >= 19) else None
    return d, h
def fmt(v, vt, dur):
    if vt in ('SHORT', 'Short'): return 'SHORT', 'label'
    if vt in (None, '') and dur is not None and dur <= 60: return 'SHORT', 'inferred_duration<=60s'
    return 'LONG', 'label' if vt else 'inferred_default'
def q(xs, p):
    xs = sorted(xs); 
    if not xs: return None
    k = (len(xs) - 1) * p; f = math.floor(k); c = min(f + 1, len(xs) - 1); return xs[f] + (xs[c] - xs[f]) * (k - f)
def ols(x, y):
    n = len(x); mx = sum(x) / n; my = sum(y) / n; sxx = sum((a - mx) ** 2 for a in x)
    if sxx < 1e-9: return None
    b = sum((a - mx) * (c - my) for a, c in zip(x, y)) / sxx; return my - b * mx, b
con = sqlite3.connect(DB, uri=True); con.row_factory = sqlite3.Row
chs = {r['channel_id']: dict(r) for r in con.execute('select * from channels')}
vids = collections.defaultdict(list)
for r in con.execute('select video_id,channel_id,title,published,duration_seconds,video_type,views,likes,comments,has_transcript,metadata_level from videos'):
    v = dict(r); d, h = pdate(v['published']); v['date'] = d; v['hour'] = h
    v['fmt'], v['fmt_basis'] = fmt(v['video_type'], v['video_type'], v['duration_seconds'])
    v['age'] = (AS_OF - d).days if d else None; v['topic'] = topic(v['title']); vids[v['channel_id']].append(v)
# ---- age-adjusted expectation per (channel, format): ln(views+1) = a + b ln(age+7)
for cid, vs in vids.items():
    for f in ('SHORT', 'LONG'):
        g = [v for v in vs if v['fmt'] == f and v['views'] is not None and v['age'] is not None]
        fit = None
        if len(g) >= 15:
            fit = ols([math.log(v['age'] + 7) for v in g], [math.log(v['views'] + 1) for v in g])
            if fit and fit[1] < 0: fit = None   # negative age slope is not credible -> fall back
        med = st.median([v['views'] for v in vs if v['fmt'] == f and v['views'] is not None] or [0])
        for v in vs:
            if v['fmt'] != f or v['views'] is None: continue
            if fit and v['age'] is not None:
                exp = math.exp(fit[0] + fit[1] * math.log(v['age'] + 7)) - 1; v['basis'] = 'age_adjusted_fit'
            else:
                exp = med; v['basis'] = 'format_median_only (n<15, no age/slope, or no date)'
            v['ratio'] = (v['views'] + 1) / (exp + 1)
ratios = [v['ratio'] for vs in vids.values() for v in vs if v.get('ratio') is not None]
T = {'under': q(ratios, .25), 'avg_hi': q(ratios, .65), 'breakout': q(ratios, .90)}   # pooled quantiles of dimensionless ratio
def cls(r): return 'Breakout' if r >= T['breakout'] else 'Successful' if r >= T['avg_hi'] else 'Average' if r >= T['under'] else 'Underperforming'
for vs in vids.values():
    for v in vs: v['class'] = cls(v['ratio']) if v.get('ratio') is not None else 'Unclassified (no views)'
def stats(xs):
    if not xs: return {'n': 0}
    return {'n': len(xs), 'total': sum(xs), 'mean': round(st.mean(xs), 1), 'median': st.median(xs), 'max': max(xs), 'min': min(xs),
            'p10': round(q(xs, .1)), 'p25': round(q(xs, .25)), 'p75': round(q(xs, .75)), 'p90': round(q(xs, .9)), 'p99': round(q(xs, .99)),
            'cv': round(st.pstdev(xs) / st.mean(xs), 2) if st.mean(xs) else None}
def S(d): return ' | '.join(f'{k}={v}' for k, v in d.items())
slug = lambda n: re.sub(r'[^a-z0-9]+', '_', (n or 'x').lower()).strip('_')[:40]
rows = []
for cid, vs in sorted(vids.items(), key=lambda kv: -len(kv[1])):
    c = chs.get(cid, {}); name = c.get('name') or cid
    viewed = [v for v in vs if v['views'] is not None]; dated = [v for v in vs if v['date']]
    all_s = stats([v['views'] for v in viewed]); shorts = [v for v in viewed if v['fmt'] == 'SHORT']; longs = [v for v in viewed if v['fmt'] == 'LONG']
    s_s, l_s = stats([v['views'] for v in shorts]), stats([v['views'] for v in longs])
    ds = sorted({v['date'] for v in dated}); gaps = [(b - a).days for a, b in zip(ds, ds[1:])]
    span = (ds[-1] - ds[0]).days + 1 if ds else None
    pubfreq = round(len(dated) / (span / 7), 2) if span and span > 7 else None
    mon, qtr = collections.defaultdict(list), collections.defaultdict(list)
    for v in dated:
        mon[v['date'].strftime('%Y-%m')].append(v); qtr[f"{v['date'].year}-Q{(v['date'].month - 1) // 3 + 1}"].append(v)
    wd = collections.Counter(v['date'].strftime('%a') for v in dated); hr = collections.Counter(v['hour'] for v in dated if v['hour'] is not None)
    tp = collections.defaultdict(list)
    for v in viewed: tp[v['topic']].append(v['views'])
    cc = collections.Counter(v['class'] for v in vs); ccf = {f: collections.Counter(v['class'] for v in vs if v['fmt'] == f) for f in ('SHORT', 'LONG')}
    top = sorted(viewed, key=lambda v: -v['ratio'])[:5] if viewed else []
    durs = [v['duration_seconds'] for v in vs if v['duration_seconds']]
    bins = collections.Counter('<=60s' if d <= 60 else '1-3m' if d <= 180 else '3-8m' if d <= 480 else '8-15m' if d <= 900 else '15-30m' if d <= 1800 else '>30m' for d in durs)
    lim = []
    if len(vs) < 15: lim.append(f'only {len(vs)} videos: baselines low-confidence')
    if len(dated) < len(vs): lim.append(f'{len(vs)-len(dated)} videos lack publish date (excluded from time/age analysis)')
    if len(viewed) < len(vs): lim.append(f'{len(vs)-len(viewed)} videos lack view counts')
    if len(vs) < 100: lim.append('dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos')
    if c.get('channel_total_videos') and len(vs) < c['channel_total_videos']: lim.append(f"coverage {len(vs)}/{c['channel_total_videos']} of channel's reported videos")
    lim += ['single view-count snapshot; no historical snapshots, so no growth curves', 'topic = keyword heuristic on title (inference, not fact)', 'likes/comments/CTR/retention not used for classification']
    lines = [f'# {name}', f'Channel id `{cid}` · niche {c.get("niche")} · subs {c.get("subscribers")} · snapshot {AS_OF}', '',
     '## 1. Channel Performance Report', f'- Total videos in DB: {len(vs)} (Shorts {sum(v["fmt"]=="SHORT" for v in vs)}, Long-form {sum(v["fmt"]=="LONG" for v in vs)})', f'- Views (all): {S(all_s)}', '',
     '## 2. Performance Distribution', f'- All: p10={all_s.get("p10")} p25={all_s.get("p25")} median={all_s.get("median")} p75={all_s.get("p75")} p90={all_s.get("p90")} p99={all_s.get("p99")} CV={all_s.get("cv")}',
     f'- Mean/median ratio: {round(all_s["mean"]/all_s["median"],2) if all_s.get("median") else "n/a"} (>1 = right-skew, a few hits dominate)', '',
     '## 3. Shorts vs Long-form', f'- Shorts: {S(s_s)}', f'- Long-form: {S(l_s)}', '',
     '## 4. Topic Distribution (heuristic)'] + [f'- {t}: {len(x)} videos, median views {st.median(x):.0f}' for t, x in sorted(tp.items(), key=lambda kv: -len(kv[1]))] + [
     f'- Duration bins: {dict(bins)}', '', '## 5. Publishing Pattern',
     f'- Date range: {ds[0] if ds else "n/a"} → {ds[-1] if ds else "n/a"} ({span} days); uploads/week ≈ {pubfreq}',
     f'- Days between upload dates: median={st.median(gaps) if gaps else "n/a"}, mean={round(st.mean(gaps),1) if gaps else "n/a"}, max={max(gaps) if gaps else "n/a"}; consistency (CV of gaps)={round(st.pstdev(gaps)/st.mean(gaps),2) if gaps and st.mean(gaps) else "n/a"}',
     f'- Weekday counts: {dict(wd)}', f'- Upload hour (UTC, only where timestamp exists, n={sum(hr.values())}): {dict(sorted(hr.items()))}', '- Monthly (n, median views, age-adj median ratio):']
    lines += [f'  - {m}: {len(x)}, {st.median([v["views"] for v in x if v["views"] is not None] or [0]):.0f}, {st.median([v["ratio"] for v in x if v.get("ratio")] or [0]):.2f}' for m, x in sorted(mon.items())]
    lines += ['- Quarterly:'] + [f'  - {m}: {len(x)}, {st.median([v["views"] for v in x if v["views"] is not None] or [0]):.0f}, {st.median([v["ratio"] for v in x if v.get("ratio")] or [0]):.2f}' for m, x in sorted(qtr.items())]
    lines += ['', '## 6. Performance Classification', f'- All: {dict(cc)}', f'- Shorts: {dict(ccf["SHORT"])}  Long-form: {dict(ccf["LONG"])}', '- Top 5 by age-adjusted ratio:'] + [f'  - {v["video_id"]} "{(v["title"] or "")[:70]}" views={v["views"]} age={v["age"]}d ratio={v["ratio"]:.2f} [{v["fmt"]}]' for v in top]
    lines += ['', '## 7. Baseline Methodology', f'- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.',
     '- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).',
     f'- Thresholds from pooled ratio distribution of all {len(ratios)} classified videos: Underperforming < P25 ({T["under"]:.2f}); Average P25–P65 (<{T["avg_hi"]:.2f}); Successful P65–P90 (<{T["breakout"]:.2f}); Breakout ≥ P90 ({T["breakout"]:.2f}).', '- Percentile cut-offs are descriptive conventions, not performance claims.',
     '', '## 8. Data Limitations'] + [f'- {x}' for x in lim]
    fn = f'{slug(name)}_{cid[-6:]}.md'; open(os.path.join(B, 'channels', fn), 'w').write('\n'.join(lines))
    rows.append({'channel': name, 'channel_id': cid, 'niche': c.get('niche'), 'subs': c.get('subscribers'), 'videos': len(vs), 'shorts': sum(v['fmt'] == 'SHORT' for v in vs), 'long': sum(v['fmt'] == 'LONG' for v in vs),
      'total_views': all_s.get('total'), 'mean': all_s.get('mean'), 'median': all_s.get('median'), 'max': all_s.get('max'), 'min': all_s.get('min'), 'skew_mean_over_median': round(all_s['mean'] / all_s['median'], 2) if all_s.get('median') else None,
      'median_short': s_s.get('median'), 'median_long': l_s.get('median'), 'first': ds[0] if ds else None, 'last': ds[-1] if ds else None, 'uploads_per_week': pubfreq, 'median_gap_days': st.median(gaps) if gaps else None,
      'breakout': cc['Breakout'], 'successful': cc['Successful'], 'average': cc['Average'], 'under': cc['Underperforming'], 'report': fn})
with open(os.path.join(B, 'combined_channel_comparison.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, rows[0].keys()); w.writeheader(); w.writerows(rows)
json.dump({'as_of': str(AS_OF), 'thresholds': T, 'n_classified': len(ratios)}, open(os.path.join(B, 'thresholds.json'), 'w'), indent=1)
md = ['# Combined Channel Comparison (Part 2)', f'Snapshot {AS_OF}; {len(rows)} channels with videos. Raw views are NOT comparable across channels — use median, skew and age-adjusted class mix. See channels/*.md for method.', '',
 '| Channel | Vids | Shorts | Long | Median | Mean/Med | Med Short | Med Long | Up/wk | Gap d | Brk | Succ | Avg | Under |', '|' + '---|' * 14]
for r in sorted(rows, key=lambda r: -(r['median'] or 0)):
    md.append(f"| {r['channel']} | {r['videos']} | {r['shorts']} | {r['long']} | {r['median']} | {r['skew_mean_over_median']} | {r['median_short']} | {r['median_long']} | {r['uploads_per_week']} | {r['median_gap_days']} | {r['breakout']} | {r['successful']} | {r['average']} | {r['under']} |")
md += ['', f'Classification thresholds (pooled ratio quantiles): {T}', 'Because thresholds are pooled quantiles, ~10% of all videos are Breakout by construction; per-channel class mix shows where they concentrate, not absolute quality.']
open(os.path.join(B, 'COMBINED_CHANNEL_COMPARISON.md'), 'w').write('\n'.join(md))
print(len(rows), 'channels', len(ratios), 'classified', T)
