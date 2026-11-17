"""Plain-SVG charts from derived/analysis_results.json and receipts/census.json (stdlib only).
Usage: python3 -I charts.py <audit_root>"""
import json, math, sys

ROOT = sys.argv[1]
R = json.load(open(f'{ROOT}/derived/analysis_results.json'))
CS = json.load(open(f'{ROOT}/receipts/census.json'))
INK, MUTED, GRID, A, B = '#1f2937', '#6b7280', '#e5e7eb', '#2563eb', '#d97706'
FONT = 'font-family="system-ui,-apple-system,Segoe UI,sans-serif"'


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" {FONT}>'
            f'<title>{title}</title><rect width="{w}" height="{h}" fill="#ffffff"/>{body}</svg>')


def forest():
    tests = R['primary_tests']
    lo, hi = math.log(0.4), math.log(2.5)
    W, L, top, rh = 860, 250, 50, 30
    H = top + rh * len(tests) + 50
    x = lambda m: L + (math.log(m) - lo) / (hi - lo) * (W - L - 30)
    b = [f'<text x="{L}" y="22" font-size="14" fill="{INK}" font-weight="600">Within-channel peer-ratio multiplier (95% bootstrap CI)</text>',
         f'<text x="{L}" y="40" font-size="11" fill="{MUTED}">blue = original 966 (n with ratio 723) · amber = unseen-channel replication (418) · 1.0 = no difference</text>']
    for m in (0.5, 1, 2):
        b.append(f'<line x1="{x(m):.1f}" x2="{x(m):.1f}" y1="{top - 5}" y2="{H - 40}" stroke="{GRID if m != 1 else MUTED}" stroke-dasharray="{"" if m == 1 else "3,3"}"/>'
                 f'<text x="{x(m):.1f}" y="{H - 24}" font-size="11" fill="{MUTED}" text-anchor="middle">{m}×</text>')
    for i, t in enumerate(tests):
        yy = top + rh * i + 12
        b.append(f'<text x="{L - 10}" y="{yy + 4}" font-size="12" fill="{INK}" text-anchor="end">{t["feature"]} (q={t["q_bh"]:.2f})</text>')
        c = t.get('ci95_multiplier')
        if c:
            b.append(f'<line x1="{x(max(c[0], .41)):.1f}" x2="{x(min(c[1], 2.45)):.1f}" y1="{yy}" y2="{yy}" stroke="{A}" stroke-width="2"/>')
        b.append(f'<circle cx="{x(t["ratio_multiplier"]):.1f}" cy="{yy}" r="5" fill="{A}"/>')
        r = t.get('replication') or {}
        if r.get('ratio_multiplier'):
            rc = r.get('ci95_multiplier')
            if rc:
                b.append(f'<line x1="{x(max(rc[0], .41)):.1f}" x2="{x(min(rc[1], 2.45)):.1f}" y1="{yy + 8}" y2="{yy + 8}" stroke="{B}" stroke-width="2"/>')
            b.append(f'<rect x="{x(r["ratio_multiplier"]) - 4:.1f}" y="{yy + 4}" width="8" height="8" fill="{B}"/>')
    return svg(W, H, ''.join(b), 'Hypothesis forest plot')


def concentration():
    c = sorted(R['descriptive']['concentration_registry_all_niches'].items(), key=lambda kv: -kv[1]['top10pct_share_of_views'])
    W, L, top, rh = 760, 230, 50, 18
    H = top + rh * len(c) + 30
    b = [f'<text x="{L}" y="22" font-size="14" fill="{INK}" font-weight="600">Share of channel lifetime views from its top 10% of videos</text>',
         f'<text x="{L}" y="40" font-size="11" fill="{MUTED}">Registry DB, {len(c)} channels with ≥10 videos (public frozen snapshot views)</text>']
    for i, (ch, d) in enumerate(c):
        yy = top + rh * i
        w = d['top10pct_share_of_views'] * (W - L - 70)
        b.append(f'<text x="{L - 8}" y="{yy + 12}" font-size="11" fill="{INK}" text-anchor="end">{ch[:30].replace("&", "&amp;")} (n={d["n"]})</text>'
                 f'<rect x="{L}" y="{yy + 2}" width="{w:.1f}" height="13" rx="2" fill="{A}"/>'
                 f'<text x="{L + w + 6:.1f}" y="{yy + 12}" font-size="11" fill="{MUTED}">{d["top10pct_share_of_views"] * 100:.0f}%</text>')
    return svg(W, H, ''.join(b), 'View concentration')


def coverage():
    p = CS['population']
    rows = [('Finance registered identities', 1612), ('Metadata available (universe)', 1612),
            ('Transcript text available (universe)', 955), ('Peer ratio computable (originals)', 723),
            ('Peer ratio computable (replication sets)', sum(R['populations']['replication_with_ratio'].values())),
            ('Deep audit: all six reviews complete', p['live_ledger_all_six_complete']),
            ('Visual Forensics accepted videos (this checkout)', 2), ('First-party Studio analytics', 0)]
    W, L, top, rh = 760, 300, 40, 26
    H = top + rh * len(rows) + 20
    mx = 1612
    b = [f'<text x="{L}" y="22" font-size="14" fill="{INK}" font-weight="600">Different units — never add these together</text>']
    for i, (k, n) in enumerate(rows):
        yy = top + rh * i
        w = max(1.5, n / mx * (W - L - 70))
        b.append(f'<text x="{L - 8}" y="{yy + 14}" font-size="12" fill="{INK}" text-anchor="end">{k}</text>'
                 f'<rect x="{L}" y="{yy + 3}" width="{w:.1f}" height="16" rx="2" fill="{A if n else "#dc2626"}"/>'
                 f'<text x="{L + w + 6:.1f}" y="{yy + 15}" font-size="12" fill="{MUTED}">{n:,}</text>')
    return svg(W, H, ''.join(b), 'Evidence coverage')


for name, fn in (('hypothesis_forest', forest), ('view_concentration', concentration), ('evidence_coverage', coverage)):
    open(f'{ROOT}/charts/{name}.svg', 'w').write(fn())
print('ok')
