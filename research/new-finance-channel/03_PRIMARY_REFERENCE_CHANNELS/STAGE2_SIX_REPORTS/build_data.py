"""Stage 2 data builder. Read-only on DB. Writes classified CSV + quant markdown per channel."""
import sqlite3, csv, json, re, statistics as st, datetime as dt, collections, os, sys
ROOT='/Users/ghilmankhan/workprojects/youtube-intelligence-os'
W=ROOT+'/research/new-finance-channel'
OUT=W+'/03_PRIMARY_REFERENCE_CHANNELS/STAGE2_SIX_REPORTS'
TODAY=dt.date(2026,11,19)
db=sqlite3.connect('file:'+ROOT+'/data/catalog/finance_economics_complete.db?mode=ro',uri=True)
CH={'casual-finance':'Casual Finance','monkey-economics':'Monkey Economics','monkeyexplains':'MonkeyExplains','crayon-capital':'Crayon Capital','paper-billions':'Paper Billions','capital-case':'Capital Case'}
# (subniche, regex, economics/finance/non). first match wins.
RULES=[
('Non-finance (gaming/social/tech culture)',r'roblox|discord|tiktok ban|social media ban|minecraft|youtube|game\b|gamer|instagram|snapchat|meta ai|streamer','Non-finance'),
('AI & tech bubble',r'\bai\b|nvidia|openai|bubble|chip|data ?cent|anthropic|semiconductor|tech|robot|chatgpt|software|palantir|tesla|microsoft|google|apple|meta\b|oracle|intel\b|amd\b|spacex|elon|musk','Finance'),
('Crashes, recessions & crises',r'crash|crisis|recession|collapse|depression|bust|2008|panic|meltdown|bank run|bankrupt|default|doom|brace|impact|over\.\.\.|no way out|should.?ve crashed|svb|lehman|evergrande','Finance'),
('Housing & real estate',r'hous|rent\b|rental|mortgage|home\b|homes|real estate|landlord|zillow|apartment|property','Economics'),
('Jobs, wages & labour',r'\bjobs?\b|layoff|unemploy|wage|salary|worker|labor|labour|employ|career|work from|gig|retire|pension|\bwork\b','Economics'),
('Trade, tariffs & geopolitics',r'tariff|trade war|china|chinese|russia|venezuela|oil\b|opec|sanction|war\b|gulf|saudi|iran|ukraine|taiwan|india|japan|europe|eu\b|brics|cuba|missile|military|empire|invasion|attack','Economics'),
('Debt, Fed & inflation',r'debt|deficit|treasury|\bfed\b|federal reserve|interest rate|inflation|dollar|currency|gold|tax|budget|stimulus|money printing|stagflation|yield|bond|gdp|cpi\b|economy|economic|economics','Economics'),
('Investing, stocks & crypto',r'invest|stock|bitcoin|crypto|etf|index fund|s&p|401k|wall street|hedge|trader|trading|market|dividend|portfolio|shares|ipo|fund\b|robinhood|gamestop|short sell|ponzi|scam|fraud|laundering|bank\b','Finance'),
('Companies, billionaires & business history',r'amazon|walmart|rockefeller|ford|disney|nike|starbucks|mcdonald|coca|costco|company|corporation|billionaire|richest|empire|brand|business|monopoly|how .* (makes|make) money|startup|founder|ceo|boeing|airline|airfare|flight','Finance'),
('Personal finance & consumer',r'credit|loan|saving|save|budget|rich|poor|cost of living|afford|price|prices|expensive|cheap|buy|insurance|college|student|paycheck|money|broke|wealth|income|inheritance|billion|million','Finance'),
]

GOV='Government, politics & policy'; EN='Energy, oil & commodities'; JOB='Jobs, wages & labour'
CO='Companies, billionaires & business history'; INV='Investing, stocks & crypto'; DEBT='Debt, Fed & inflation'
TRD='Trade, tariffs & geopolitics'; CR='Crashes, recessions & crises'; AI='AI & tech bubble'; NF='Non-finance (gaming/social/tech culture)'; PF='Personal finance & consumer'
E_,F_,N_='Economics','Finance','Non-finance'
OVR={}
def o(ids,cat,k):
    for i in ids.split(): OVR[i]=(cat,k)
o('uJ_vkUHLJNs jjRo2QSMybU Fv3STb4g23Q',CO,F_); o('0k5C-MrLjAI',EN,E_)
o('YUyoWFlaOKg JZDpLZG2r6Y 6nge7gASsmA hRkfDFM1-ag Oqo7oIWv5aQ s6L9MLjEm4A tf79W1_Dr4 tf79W1j_Dr4 TlwjaaiXLxA EZklJvuoteE dKIS9hkumi8 fA3_jXbGliI 4IZIyIQDrLY SEvbCWZjWXU QLsDb613nMA QLsDb613nvA 6joc36V3KQw BqE-JSB4W80',INV,F_)
o('DgbHW0IqHrI Q3Nb4ymp81w PxgCsLSf-w4 ud1ESmogrFY 6jhJfw2TZsY YTRlgYeRXm4 77km5ikcqA8 FttHpJYd3-o',DEBT,E_)
o('Im-N3K9Pnf0 Zc_XHh_hEKY zHekycA0R3E',CR,F_); o('gG239LrksH4',TRD,E_); o('4zUVBW2z7dc uzPl-GZRrRA',PF,F_); o('kWrm36EKD3c',AI,F_)
o('tsZIyy18qIo aDCKVS8aA8E ybP8g6xzCIs p9x9s_-IOOM EedHneVKmpo',CO,F_); o('AKrjI9m6fpk GdpGd0U2wmo',NF,N_); o('adpt6KW4Jb4',INV,F_); o('RB-DTXw1Yzw y51JjcymEAY',TRD,E_)
o('UNzjgBbmt3o',TRD,E_); o('awOgsY9IMbk bi_T23spSmc',GOV,E_)
o('5x5IaKO6R5I',EN,E_); o('9vpo6p-7J1I',TRD,E_); o('ktOignjy2TE 84YaEDQMY1c 6sz9FpHgAWU ZyHwdD26BtY C2K-FryxkW8',GOV,E_)
o('OQgRqLUmvPk l3yWpDmRXk8 mVRXhCkrtf8 zLDMOAlWLfc v-2hJnwK5yw',NF,N_); o('PejedlEOsh0',TRD,E_); o('rgm0ZDdNLOA',JOB,E_); o('cvKe_WYeITU',AI,F_)
o('bz0OGtrkjv0',DEBT,E_); o('TSJQ8SjcTPk',CO,F_)

TOV=[(r'housing (crisis|bubble)|real estate crisis','Housing & real estate','Economics'),(r'dot-com','Crashes, recessions & crises','Finance'),(r'steve jobs|elon musk actually|\bbyd\b|spacex','Companies, billionaires & business history','Finance'),(r'100 trillion','Debt, Fed & inflation','Economics')]
def classify(t):
    tl=t.lower()
    for r,c,k in TOV:
        if re.search(r,tl): return c,k
    for n,r,k in RULES:
        if re.search(r,tl): return n,k
    return 'Other / unclassified','Unclassified'
def srt_text(s):
    out=[]
    for ln in s.split('\n'):
        ln=ln.strip()
        if not ln or re.fullmatch(r'\d+',ln) or '-->' in ln: continue
        if out and out[-1]==ln: continue
        out.append(ln)
    return re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',' '.join(out))).strip()
def load(slug):
    name=CH[slug]
    cid=db.execute('select channel_id from channels where name=?',(name,)).fetchone()[0]
    rows=[]
    if slug=='monkeyexplains':
        tx={r[0]:r[1] for r in db.execute('select video_id,text from transcripts where video_id in (select video_id from videos where channel_id=?)',(cid,))}
        raw={}
        for f in ['R4_monkeyexplains_full_iOq4GnI0JmGbegdSv.json','R5_monkeyexplains_7ids_F5CfAyeghGyPt4WsM.json']:
            for it in json.load(open(W+'/05_FRESH_COMPETITOR_DATA/raw/'+f)):
                sub=it.get('subtitles')
                if sub and isinstance(sub,list) and sub[0].get('srt'): raw[it['id']]=srt_text(sub[0]['srt'])
                if it.get('isMembersOnly') in (True,'True'): raw.setdefault('MEM_'+it['id'],'')
        mem={k[4:] for k in raw if k.startswith('MEM_')}
        for r in csv.DictReader(open(W+'/05_FRESH_COMPETITOR_DATA/MONKEYEXPLAINS_MERGED_INVENTORY_2026-11-19.csv')):
            vid=r['id']; v=r['views']
            rows.append(dict(id=vid,title=r['title'],date=r['date'],dur=int(float(r['duration_s'] or 0)),views=int(float(v)) if v not in ('','None') else None,likes=int(float(r['likes'])) if r['likes'] not in('','None') else None,comments=int(float(r['comments'])) if r['comments'] not in('','None') else None,url=r['url'],tx=tx.get(vid) or raw.get(vid) or '',member=vid in mem or r['title'].startswith('(Member Edition)')))
    else:
        tx={r[0]:r[1] for r in db.execute('select video_id,text from transcripts where video_id in (select video_id from videos where channel_id=?)',(cid,))}
        for r in db.execute('select video_id,title,published,duration_seconds,views,likes,comments,url from videos where channel_id=?',(cid,)):
            rows.append(dict(id=r[0],title=r[1],date=(r[2] or '')[:10],dur=r[3] or 0,views=r[4],likes=r[5],comments=r[6],url=r[7],tx=tx.get(r[0]) or '',member=False))
    for r in rows:
        r['short']=r['dur']<=180
        r['cat'],r['kind']=classify(r['title'])
        if r['id'] in OVR and OVR[r['id']][0]: r['cat'],r['kind']=OVR[r['id']]
        try: r['d']=dt.date.fromisoformat(r['date'])
        except: r['d']=None
        r['age']=(TODAY-r['d']).days if r['d'] else None
    return name,cid,rows
def med(x): x=[a for a in x if a is not None]; return int(st.median(x)) if x else 0
def fm(n): return '—' if n is None else f'{int(n):,}'
def tfeat(t):
    w=t.split()
    return dict(q='?' in t,num=bool(re.search(r'\d',t)),colon=':' in t,ell='...' in t or '…' in t,caps=any(len(x)>2 and x.isupper() for x in w),year=bool(re.search(r'20[12]\d',t)),howwhy=bool(re.match(r'(how|why|what|when|who|is|are|can|will|should|does|do)\b',t.lower())),you=bool(re.search(r'\b(you|your|we|us|our)\b',t.lower())),neg=bool(re.search(r"\b(worse|worst|crash|collapse|end|over|dead|doom|broke|fail|lost|never|no one|nobody|can't|won't|wrong|lie|secret|hidden|truth|trap)\b",t.lower())),words=len(w))
def report(slug):
    name,cid,rows=load(slug)
    L=[r for r in rows if not r['short']]; S=[r for r in rows if r['short']]
    pub=[r for r in rows if r['views'] is not None]
    Lp=[r for r in L if r['views'] is not None]; Sp=[r for r in S if r['views'] is not None]
    o=[]; a=o.append
    a(f'## 1. Full inventory (VERIFIED from DB' + (' + Apify R4/R5 merge' if slug=='monkeyexplains' else '') + ')\n')
    ds=[r['d'] for r in rows if r['d']]
    a(f'- Videos held: **{len(rows)}** (long-form {len(L)}, Shorts {len(S)} by duration <= 180 s). Date range {min(ds)} to {max(ds)}.')
    a(f'- With public view counts: {len(pub)}. Transcripts held: {sum(1 for r in rows if r["tx"])} of {len(rows)}.')
    if slug=='monkeyexplains':
        m=[r for r in rows if r['member']]
        a(f'- Member Edition items: **{len(m)}** (no public views or transcripts; excluded from every views statistic below). Coverage 136 of 149 reported; 13 items not recovered (Stage 1, INFERRED probable Member Edition).')
    a(f'- Views, long-form: total {fm(sum(r["views"] for r in Lp))}, median {fm(med([r["views"] for r in Lp]))}, mean {fm(st.mean([r["views"] for r in Lp]) if Lp else 0)}, max {fm(max([r["views"] for r in Lp],default=0))}.')
    if Sp: a(f'- Views, Shorts: total {fm(sum(r["views"] for r in Sp))}, median {fm(med([r["views"] for r in Sp]))}, max {fm(max(r["views"] for r in Sp))}.')
    a(f'- Median long-form duration: {med([r["dur"] for r in L])//60} min {med([r["dur"] for r in L])%60:02d} s.\n')
    # top
    def tbl(lst,n):
        a('| # | Views | Date | Dur | Category | Title |'); a('|---:|---:|---|---:|---|---|')
        for i,r in enumerate(sorted(lst,key=lambda r:-(r['views'] or 0))[:n],1):
            a(f'| {i} | {fm(r["views"])} | {r["date"]} | {r["dur"]//60}:{r["dur"]%60:02d} | {r["cat"]} | [{r["title"].replace("|","/")}]({r["url"]}) |')
        a('')
    a('## 2. Top videos\n'); a('### Top 15 long-form'); tbl(Lp,15)
    if len(Sp)>=3: a('### Top 8 Shorts'); tbl(Sp,8)
    # recent
    a('## 3. Recent uploads (newest 12, any type)\n'); a('| Date | Type | Views | Age (d) | Title |'); a('|---|---|---:|---:|---|')
    for r in sorted([r for r in rows if r['d']],key=lambda r:r['d'],reverse=True)[:12]:
        a(f'| {r["date"]} | {"Short" if r["short"] else ("Member" if r["member"] else "Long")} | {fm(r["views"])} | {r["age"]} | {r["title"].replace("|","/")} |')
    a('')
    # windows
    a('## 4. 30 / 60 / 90-day patterns (to 2026-11-19)\n'); a('| Window | Uploads | Long | Shorts | Long views median | Long views total | Per week |'); a('|---|---:|---:|---:|---:|---:|---:|')
    for w in (30,60,90,180,365):
        x=[r for r in rows if r['age'] is not None and r['age']<=w]; xl=[r for r in x if not r['short'] and r['views'] is not None]
        a(f'| last {w} d | {len(x)} | {len([r for r in x if not r["short"]])} | {len([r for r in x if r["short"]])} | {fm(med([r["views"] for r in xl]))} | {fm(sum(r["views"] for r in xl))} | {len(x)/(w/7):.1f} |')
    a('')
    mc=collections.Counter((r['d'].strftime('%Y-%m'),'S' if r['short'] else 'L') for r in rows if r['d'])
    months=sorted({k[0] for k in mc})[-14:]
    a('Monthly uploads (last 14 active months): '+'; '.join(f'{m}: {mc[(m,"L")]}L/{mc[(m,"S")]}S' for m in months)+'\n')
    wd=collections.Counter(r['d'].strftime('%a') for r in L if r['d'])
    a('Long-form upload weekday: '+', '.join(f'{k} {v}' for k,v in wd.most_common())+'\n')
    # categories
    a('## 5. Finance / Economics categories and sub-niche distribution\n')
    a('Classification: title-keyword rules (`build_data.py`), then **audited by reading the titles** (section 9). Labels are INFERRED, not channel-declared.\n')
    cm=med([r['views'] for r in Lp])
    a('| Sub-niche | F/E | Long n | Long median views | x channel median | Long total views | Shorts n |'); a('|---|---|---:|---:|---:|---:|---:|')
    cats=collections.defaultdict(list)
    for r in rows: cats[r['cat']].append(r)
    for c,lst in sorted(cats.items(),key=lambda kv:-sum(r['views'] or 0 for r in kv[1] if not r['short'])):
        ll=[r for r in lst if not r['short'] and r['views'] is not None]
        a(f'| {c} | {lst[0]["kind"]} | {len(ll)} | {fm(med([r["views"] for r in ll]))} | {(med([r["views"] for r in ll])/cm if cm else 0):.2f} | {fm(sum(r["views"] for r in ll))} | {len([r for r in lst if r["short"]])} |')
    kinds=collections.Counter(); kv=collections.Counter()
    for r in Lp: kinds[r['kind']]+=1; kv[r['kind']]+=r['views']
    a('\nFinance vs Economics (long-form, public views): '+'; '.join(f'{k}: {kinds[k]} videos / {fm(kv[k])} views' for k in kinds)+'\n')
    # winners / failures
    a('## 6. Winning and failing topics (long-form, relative to channel long median %s)\n'%fm(cm))
    win=[r for r in Lp if r['views']>=2*cm]; brk=[r for r in Lp if r['views']>=5*cm]
    old=[r for r in Lp if r['age'] and r['age']>=60]; fail=[r for r in old if r['views']<=0.5*cm]
    a(f'- Winners (>= 2x median): **{len(win)}** of {len(Lp)}; breakouts (>= 5x): **{len(brk)}**; failures (<= 0.5x, older than 60 d): **{len(fail)}** of {len(old)}.')
    wc=collections.Counter(r['cat'] for r in win); fc=collections.Counter(r['cat'] for r in fail)
    a('- Winners by sub-niche: '+('; '.join(f'{k} {v}' for k,v in wc.most_common()) or 'none')+'.')
    a('- Failures by sub-niche: '+('; '.join(f'{k} {v}' for k,v in fc.most_common()) or 'none')+'.\n')
    a('Breakouts:\n')
    for r in sorted(brk,key=lambda r:-r['views']): a(f'- {fm(r["views"])} ({r["views"]/cm:.1f}x) {r["date"]} [{r["title"]}]({r["url"]})')
    a('\nLowest long-form (older than 60 d):\n')
    for r in sorted(old,key=lambda r:r['views'])[:8]: a(f'- {fm(r["views"])} ({r["views"]/cm:.2f}x) {r["date"]} [{r["title"]}]({r["url"]})')
    a('')
    # titles
    a('## 7. Title structures (long-form)\n')
    F=[tfeat(r['title']) for r in Lp]
    if F:
        a('| Feature | Share of long titles | Median views with | Median views without |'); a('|---|---:|---:|---:|')
        for k,lab in [('q','Question mark'),('num','Contains a digit'),('colon','Colon'),('ell','Ellipsis'),('caps','ALL-CAPS word'),('year','Year'),('howwhy','Starts with how/why/what/is…'),('you','Addresses you/we'),('neg','Negative/threat word')]:
            w=[r['views'] for r,f in zip(Lp,F) if f[k]]; wo=[r['views'] for r,f in zip(Lp,F) if not f[k]]
            a(f'| {lab} | {100*len(w)/len(F):.0f}% | {fm(med(w))} | {fm(med(wo))} |')
        a(f'\nMedian title length {med([f["words"] for f in F])} words (top-10 median {med([tfeat(r["title"])["words"] for r in sorted(Lp,key=lambda r:-r["views"])[:10]])}). Feature medians are descriptive; they do not show causation.\n')
    # shorts vs long
    a('## 8. Shorts vs long-form and upload frequency\n')
    a(f'- Long-form: {len(L)} items, median views {fm(med([r["views"] for r in Lp]))}. Shorts: {len(S)} items, median views {fm(med([r["views"] for r in Sp]))}.')
    if rows:
        span=max((max(ds)-min(ds)).days,1)
        a(f'- Whole-history cadence: {len(rows)/(span/7):.2f} uploads/week ({len(L)/(span/7):.2f} long, {len(S)/(span/7):.2f} Shorts) over {span} days.')
    a('')
    # hooks
    a('## 9. Hook data (first ~60 words of transcript, top 8 long-form)\n')
    for r in sorted([r for r in Lp if r['tx']],key=lambda r:-r['views'])[:8]:
        a(f'- **{r["title"]}** ({fm(r["views"])}): "{" ".join(r["tx"].split()[:60])}"')
    a('')
    # all titles for audit
    a('## 10. Title audit list (all items with assigned sub-niche)\n'); a('<details><summary>Show all %d titles</summary>\n'%len(rows))
    a('| Date | T | Views | Sub-niche | Title |'); a('|---|---|---:|---|---|')
    for r in sorted(rows,key=lambda r:r['date'],reverse=True):
        a(f'| {r["date"]} | {"S" if r["short"] else ("M" if r["member"] else "L")} | {fm(r["views"])} | {r["cat"]} | {r["title"].replace("|","/")} |')
    a('\n</details>\n')
    open(f'{OUT}/data/{slug}_quant.md','w').write('\n'.join(o))
    with open(f'{OUT}/data/{slug}_classified.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['id','date','type','views','dur_s','cat','fe','title','url'])
        for r in sorted(rows,key=lambda r:r['date'],reverse=True): w.writerow([r['id'],r['date'],'S' if r['short'] else ('M' if r['member'] else 'L'),r['views'],r['dur'],r['cat'],r['kind'],r['title'],r['url']])
    return name,len(rows),len(L),len(S)
if __name__=='__main__':
    for s in CH: print(report(s))
