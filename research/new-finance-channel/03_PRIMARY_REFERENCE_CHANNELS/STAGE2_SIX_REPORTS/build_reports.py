"""Combine <slug>_qual.md + <slug>_quant.md into REPORT_*.md and HTML. Run: uv run --with markdown python build_reports.py"""
import pathlib, markdown, re
D=pathlib.Path(__file__).parent
CH=[('01','monkeyexplains','MonkeyExplains'),('02','casual-finance','Casual Finance'),('03','monkey-economics','Monkey Economics'),('04','crayon-capital','Crayon Capital'),('05','paper-billions','Paper Billions'),('06','capital-case','Capital Case')]
css="body{font-family:system-ui,sans-serif;max-width:1000px;margin:24px auto;padding:0 16px;line-height:1.55;color:#1a1a1a}table{border-collapse:collapse;width:100%;font-size:13.5px;margin:12px 0}th,td{border:1px solid #ccc;padding:5px 8px;vertical-align:top;text-align:left}th{background:#f1f1f1}code{background:#f4f4f4;padding:1px 4px}h1,h2{border-bottom:1px solid #ddd;padding-bottom:4px}a{color:#0b5cd5}.box{background:#f6f8fa;border-left:4px solid #0b5cd5;padding:8px 14px;margin:12px 0}@media(prefers-color-scheme:dark){body{background:#15171a;color:#e6e6e6}th{background:#23262b}td,th{border-color:#444}code,.box{background:#23262b}a{color:#7ab4ff}}"
LEG="**Evidence labels:** VERIFIED = read from the DB or raw Apify file. INFERRED = our reading of a pattern. HYPOTHESIS = untested idea. NOT AVAILABLE = no data or media in this workspace. Views are public counts as of the pull dates (2026-11-17 to 2026-11-19). Shorts = duration <= 180 s. No view count proves a cause; there is no CTR or retention data."
nav=lambda cur:' | '.join(f'<a href="REPORT_{n}_{s}.html">{t}</a>' if s!=cur else f'<b>{t}</b>' for n,s,t in CH)
for n,s,t in CH:
    q=(D/f'data/{s}_qual.md').read_text(); d=(D/f'data/{s}_quant.md').read_text()
    md=f"# Forensic report {n}: {t}\n\nStage 2, 2026-11-19. Scope: this channel only, from `finance_economics_complete.db` (read-only){' plus Apify R4/R5 merge' if s=='monkeyexplains' else ''}. Data builder: `build_data.py`. Classified video list: `data/{s}_classified.csv`.\n\n{LEG}\n\n# Part 1. Reading\n\n{q}\n\n# Part 2. Data tables\n\n{d}\n"
    (D/f'REPORT_{n}_{s}.md').write_text(md)
    html=markdown.markdown(md,extensions=['tables'])
    (D/f'REPORT_{n}_{s}.html').write_text(f"<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><title>Forensic report: {t}</title><style>{css}</style><p><a href='../../START_HERE.html'>&larr; START HERE</a> | <a href='INDEX.html'>Stage 2 index</a></p><p>{nav(s)}</p>{html}")
print('ok')
