import csv,statistics as st,pathlib,markdown,datetime as dt
D=pathlib.Path(__file__).parent
CH=[('01','monkeyexplains','MonkeyExplains'),('02','casual-finance','Casual Finance'),('03','monkey-economics','Monkey Economics'),('04','crayon-capital','Crayon Capital'),('05','paper-billions','Paper Billions'),('06','capital-case','Capital Case')]
T=dt.date(2026,11,19)
rows=['| Channel | Held | Long (public) | Shorts | Long median views | Shorts median | Long/wk (all history) | Long, last 90 d | Shorts, last 90 d | Report |','|---|---:|---:|---:|---:|---:|---:|---:|---:|---|']
for n,s,t in CH:
    R=list(csv.DictReader(open(D/f'data/{s}_classified.csv')))
    for r in R: r['d']=dt.date.fromisoformat(r['date'])
    L=[r for r in R if r['type']=='L']; S=[r for r in R if r['type']=='S']; M=[r for r in R if r['type']=='M']
    lv=[int(r['views']) for r in L if r['views'] not in('','None')]; sv=[int(r['views']) for r in S if r['views'] not in('','None')]
    span=max((max(r['d'] for r in R)-min(r['d'] for r in R)).days,1)
    l90=sum(1 for r in L+M if (T-r['d']).days<=90); s90=sum(1 for r in S if (T-r['d']).days<=90)
    rows.append(f"| {t} | {len(R)} | {len(L)}{' (+'+str(len(M))+' Members)' if M else ''} | {len(S)} | {int(st.median(lv)):,} | {int(st.median(sv)):,} | {(len(L)+len(M))/(span/7):.2f} | {l90} | {s90} | [{n}](REPORT_{n}_{s}.html) |" if sv else f"| {t} | {len(R)} | {len(L)}{' (+'+str(len(M))+' Members)' if M else ''} | 0 | {int(st.median(lv)):,} | n/a | {(len(L)+len(M))/(span/7):.2f} | {l90} | 0 | [{n}](REPORT_{n}_{s}.html) |")
md=f"""# Stage 2: six individual forensic reports (2026-11-19)

Each channel has its own report (inventory, top videos, recent uploads, 30/60/90-day patterns, Finance vs Economics categories, sub-niches, winners and failures, title structures, thumbnail patterns, script and hook structure, visual storytelling status, Shorts vs long, upload frequency). This index only links them and shows one quick comparison table; it is NOT a substitute for the six reports.

{chr(10).join(rows)}

Notes: 'Held' for MonkeyExplains is 136 of 149 reported (13 probable Member Edition items not recovered). Long counts for MonkeyExplains include 35 Member Edition items with no public views, so its median uses the 64 public long videos only. The Paper Billions history is 11 days, so its per-week figure is a launch burst.

## What the six reports say together (INFERRED; every item is traceable to a report)

1. **Both Finance and Economics are covered by the set, but unevenly.** Finance sub-niches (AI/tech bubble, companies, crashes, investing) dominate. Economics (housing, Fed/debt, trade, jobs, energy) is strongest at Casual Finance (housing median 1.58M) and MonkeyExplains (National Debt 1.92M). Crayon, Capital Case and Paper Billions cover Economics mostly as history or not at all.
2. **Biggest long-form winners are one macro question or one famous subject**: National Debt, "Why Hasn't The AI Bubble Popped (Yet)?", Housing Crisis, Wolf of Wall Street, Great Depression, Nvidia spy story. Single obscure companies and money theory fail (Crayon BYD/TSMC/PayPal ~100K, Capital Case debt/currency ~6K).
3. **Shorts are not a long-form engine in this set.** Monkey Economics reached 57.2M Shorts views but only 10K long median; Casual Finance cut Shorts from about 30 a month (Mar to Aug 2026) to 12 in October while long rose from 1 to 5 a month; MonkeyExplains' Shorts median is 15.5K against 275K long.
4. **Cadence evidence** (feeds Stage 7): long-form per week over each channel's own history is 0.2 to 1.3. Highest sustained: MonkeyExplains about 2 a week from 2026-03 including Member Edition re-edits (1.29 over its whole history); Casual Finance 0.56 (peaking at 5 in 2026-10); Crayon 0.43; Capital Case 0.36; Monkey Economics 0.22. Paper Billions 3.8 a week is an 11-day launch burst. The set contains no channel that sustained more than 2 long videos a week.
5. **Hook structures repeat inside channels**: MonkeyExplains and Paper Billions "This is X, and he has a huge problem"; Crayon/Capital Case dated-scene openers; Casual Finance fact then contradiction.
6. **Visual storytelling and editing: NOT AVAILABLE** for all six in this stage (no video media analysed); thumbnails are covered by the earlier six-channel thumbnail model.
7. **Classification caveat**: sub-niche labels are title-keyword rules plus manual overrides listed in `build_data.py`; the full title list per channel is in each report's section 10 for audit.

## Evidence and method
- Source: `data/catalog/finance_economics_complete.db` (read-only), MonkeyExplains merged inventory (DB + Apify R4/R5). Builder `build_data.py`, report builder `build_reports.py`, classified lists `data/*_classified.csv`.
- No new paid run and no DB modification in Stage 2. Nothing committed.
- Not done in Stage 2: frame-level visual analysis, new thumbnail review, CTR/retention (no data exists), Google Trends (Stage 5).
"""
(D/'INDEX.md').write_text(md)
css=open(D/'build_reports.py').read().split('css="')[1].split('"\n')[0]
(D/'INDEX.html').write_text(f"<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><title>Stage 2 index</title><style>{css}</style><p><a href='../../START_HERE.html'>&larr; START HERE</a></p>"+markdown.markdown(md,extensions=['tables']))
print(md[:1800])
