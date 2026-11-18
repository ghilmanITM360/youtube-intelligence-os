#!/usr/bin/env python3
"""Phase C: keyword-classify long-form videos into sub-niches (INFERRED, title+keywords only) and compute
per-sub-niche metrics from finance_economics_complete.db (read-only). Run from repo root: python3 -I <file>."""
import sqlite3,re,csv,statistics as st,random,collections
from datetime import date
T=date(2026,11,18); OUT='research/new-finance-channel/10_SUB_NICHE_RESEARCH/'
db=sqlite3.connect('file:data/catalog/finance_economics_complete.db?mode=ro',uri=True)
# first match wins; order = specific before general
RULES=[
('Wealth POV / fiction stories',r'(^\s*"?\s*pov\b|\bpov:|\bstepdad\b|\bex-wife\b|\bgrandpa\'?s will\b)'),
('Retirement, pensions & senior money',r'\b(retire\w*|pension\w*|social security|medicare|medicaid|roth|rmds?|annuit\w+|401\(?k\)?|ira|seniors?|boomers?|hmrc|winter fuel|state pension|over 50|at 55|at 60|at 62|age 6\d)\b'),
('Business economics (Economics of owning X / how X makes money)',r'(economics of owning|economics behind|how .{1,40} makes? money|inside the .{1,30} business|business of|rise and fall of|history of .{1,30} in \d+|why every .{1,30} needs|dominates)'),
('AI & big-tech economics',r'\b(ai|a\.i\.|nvidia|openai|chatgpt|anthropic|semiconductor|chips?|tsmc|tesla|apple|google|microsoft|amazon|meta|palantir|spacex|musk|data ?cent|datacenter|tech giants?)\b'),
('Industry, logistics & infrastructure economics',r'\b(ships?|shipping|shipbuilding|ports?|tankers?|freight|logistics|supply chains?|data cent\w+|nuclear|electricity|power grid|railways?|railroads?|airlines?|aviation|airports?|container\w*|warehouses?|trucking|factory|factories|manufactur\w+|energy)\b'),
('Housing & real estate',r'\b(hous(e|es|ing)|mortgages?|rent(s|ing|ers?)?|real estate|landlords?|homeowners?|home ?prices?|homes?|property|apartments?|airbnb)\b'),
('Crypto, gold & commodities',r'\b(bitcoin|btc|crypto\w*|ethereum|gold|silver|copper|commodit\w+|stablecoin\w*|blockchain)\b'),
('Crashes, crises & bubbles',r'\b(crash(es|ed)?|crisis|crises|recession|collapse[sd]?|depression|bubbles?|bankrupt\w*|default\w*|2008|meltdown|panic|doom|burst)\b'),
('Geopolitics, trade & energy',r'\b(tariffs?|trade war|trade|china|chinese|russia\w*|ukraine|oil|opec|sanctions?|iran|india|japan|europe\w*|saudi|taiwan|hormuz|brics|war|wars|sovereign|countr(y|ies)|nations?|eu|uk|germany|argentina|venezuela)\b'),
('Central banks, rates, inflation & debt',r'\b(fed|federal reserve|central banks?|interest rates?|rates?|inflation|deflation|money print\w*|printing money|dollar|debt|deficit|treasur(y|ies)|bonds?|yield\w*|qe|stagflation|monetary|currency|currencies|national debt|banks?|banking|money supply)\b'),
('Jobs, wages & cost of living',r'\b(jobs?|wages?|salar(y|ies)|minimum wage|unemployment|layoffs?|workers?|labou?r|cost of living|prices?|groceries|grocery|expensive|afford\w*|poverty|poor|middle class|gen ?z|boomers?|millennials?|paycheck|work)\b'),
('Personal finance & wealth',r'\b(save|saving[s]?|budget\w*|credit cards?|credit scores?|retire\w*|401\(?k\)?|ira|tax(es)?|invest(ing|ors?|ment[s]?)?|index funds?|etfs?|dividends?|millionaires?|billionaires?|rich|wealth\w*|money|loans?|student loans?|insurance|financial freedom|passive income|side hustle|net worth|schd|voo|vti|portfolio|invested|ahead|first \$?\d+|compound\w*|income|earners?|broke|rich|richer)\b'),
('Stock market & companies',r'\b(stocks?|stock market|s&p|nasdaq|dow|ipo|shares?|earnings|valuation|market caps?|wall street|hedge funds?|private equity|buffett|warren|company|companies|corporations?|brands?|startups?|profit\w*|revenue|business|billion\w*|trillion\w*|empire|rise and fall|founders?|ceo)\b'),
('Economic history & systems',r'\b(history|histories|historical|ancient|rome|roman|empires?|medieval|centur(y|ies)|gold standard|bretton|great depression|industrial revolution|colonial\w*|capitalism|communism|socialism|feudal\w*|\d{4}s?)\b'),
('Economics concepts (ELI5)',r'\b(econom(y|ics|ic|ist|ists)|gdp|supply and demand|supply|demand|opportunity cost|market|markets|explained|explain\w*|how it works|monopol\w+|competition|incentives?|game theory|scarcity|trade-?offs?|productivity|growth|capital)\b'),
]
comp=[(n,re.compile(p,re.I)) for n,p in RULES]
def d(p):
    m=re.match(r'(\d{4}-\d\d-\d\d)',p or ''); return date.fromisoformat(m.group(1)) if m else None
def label(t):
    for n,r in comp:
        if r.search(t): return n
    return 'Unclassified'
ch={r[0]:r[1:] for r in db.execute("select channel_id,name,subscribers,data_category from channels")}
vs=[]; bych=collections.defaultdict(list)
for vid,cid,t,pub,dur,vw,vt in db.execute("select video_id,channel_id,title,published,duration_seconds,views,video_type from videos"):
    dt=d(pub)
    if dt is None or vw is None or not t or ch.get(cid,('',))[0]=='Mr. Finance': continue  # anomaly: excluded until checked by hand
    if (vt or '').upper()=='SHORT' or (dur or 999)<=60: continue
    x=dict(id=vid,cid=cid,ch=ch.get(cid,('?',0,''))[0],subs=ch.get(cid,('?',0,''))[1] or 0,t=t,dt=dt,v=vw,age=max((T-dt).days,1),sn=label(t)); vs.append(x); bych[cid].append(x)
med={c:st.median([x['v'] for x in l]) for c,l in bych.items() if len(l)>=8}
for x in vs: x['ratio']=x['v']/med[x['cid']] if x['cid'] in med and med[x['cid']]>0 else None
rows=[]; groups=collections.defaultdict(list)
for x in vs: groups[x['sn']].append(x)
for sn,l in sorted(groups.items(),key=lambda kv:-len(kv[1])):
    rat=[x['ratio'] for x in l if x['ratio'] is not None and x['age']>=14]
    small=[x for x in l if x['subs'] and x['subs']<100000 and x['age']>=14]
    l90=[x for x in l if x['age']<=90]
    rows.append(dict(sub_niche=sn,videos=len(l),channels=len({x['cid'] for x in l}),share_of_long_pct=round(100*len(l)/len(vs),1),
      median_views=int(st.median([x['v'] for x in l])),median_views_per_day=int(st.median([x['v']/x['age'] for x in l if x['age']>=14] or [0])),
      median_ratio_to_own_channel=round(st.median(rat),2) if rat else '',pct_2x_own_median=round(100*sum(r>=2 for r in rat)/len(rat)) if rat else '',pct_below_half=round(100*sum(r<0.5 for r in rat)/len(rat)) if rat else '',
      small_ch_videos=len(small),small_ch_median_views=int(st.median([x['v'] for x in small])) if small else '',small_ch_channels=len({x['cid'] for x in small}),
      videos_last_90d=len(l90),channels_last_90d=len({x['cid'] for x in l90})))
w=csv.DictWriter(open(OUT+'SUBNICHE_METRICS_2026-11-18.csv','w',newline=''),fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
# per channel x sub-niche for the six primaries
P0=['Casual Finance','Monkey Economics','MonkeyExplains','Crayon Capital','Capital Case','Paper Billions']
mx=collections.defaultdict(lambda:collections.Counter())
for x in vs:
    if x['ch'] in P0: mx[x['ch']][x['sn']]+=1
with open(OUT+'PRIMARY_CHANNEL_BY_SUBNICHE_2026-11-18.csv','w',newline='') as f:
    cw=csv.writer(f); names=[r['sub_niche'] for r in rows]; cw.writerow(['channel']+names)
    for c in P0: cw.writerow([c]+[mx[c][n] for n in names])
# classification audit sample + top videos per sub-niche
random.seed(7)
with open(OUT+'CLASSIFICATION_AUDIT_SAMPLE_2026-11-18.csv','w',newline='') as f:
    cw=csv.writer(f); cw.writerow(['sub_niche','channel','title','views'])
    for sn,l in groups.items():
        for x in random.sample(l,min(12,len(l))): cw.writerow([sn,x['ch'],x['t'],x['v']])
with open(OUT+'TOP_VIDEOS_BY_SUBNICHE_2026-11-18.csv','w',newline='') as f:
    cw=csv.writer(f); cw.writerow(['sub_niche','channel','subs','title','published','views','ratio_to_channel_median'])
    for sn,l in groups.items():
        for x in sorted([y for y in l if y['ratio'] and y['age']>=14],key=lambda y:-y['ratio'])[:8]: cw.writerow([sn,x['ch'],x['subs'],x['t'],x['dt'],x['v'],round(x['ratio'],1)])
print('long dated videos',len(vs),'channels with median',len(med))
for r in rows: print(r['sub_niche'][:36].ljust(36),*[r[k] for k in list(r)[1:]])
print(); 
for c in P0: print(c.ljust(16),dict(mx[c]))
