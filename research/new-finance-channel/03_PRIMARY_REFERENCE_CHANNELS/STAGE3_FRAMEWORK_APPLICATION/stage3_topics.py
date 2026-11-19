"""Cross-channel topic clusters (Playbook P01 cross-validated outliers, P06 competitor topic overlap, DS-000018 REC-004/009 differentiation)."""
import sys,re,json,statistics as st,collections
sys.path.insert(0,'../STAGE2_SIX_REPORTS'); import build_data as B
CL=[('Crisis history (Depression / 2008 / 1973 / dot-com / WW2 era)',r'great depression|2008|financial crisis|dot-com|1973|oversimplified|world war|housing bubble|100 trillion|every financial crisis'),
('AI bubble / OpenAI / Nvidia / Anthropic / big tech',r'\bai\b|openai|nvidia|anthropic|palantir|data center|big tech|microsoft|meta\b|bubble|tsmc|chip'),
('SpaceX / IPO',r'spacex|\bipo\b'),('Epstein / Apestein',r'epstein|apestein'),
('Billionaire and company origin stories',r'rockefeller|bezos|jobs actually|musk actually|billionaire|rothschild|j\.p\. morgan|amazon|paypal|enron|theranos|blackrock|ozempic|voc\b'),
('Scams / Wolf of Wall Street / fraud / crypto',r'wolf of wall street|scam|fraud|ponzi|laundering|ftx|bitcoin|crypto|margin call'),
('Tariffs / trade war',r'tariff|trade war'),('National debt / US debt / bonds',r'national debt|debt crisis|\bdebt\b|treasury|bond'),
('Fed / interest rates / inflation',r'\bfed\b|interest rate|rate cut|inflation|rates are going up'),
('Housing / real estate / mortgage',r'hous|real estate|mortgage|homes|rent\b'),
('Iran / Hormuz / war / oil / Venezuela',r'iran|hormuz|middle east|\boil\b|\bwar\b|venezuela|missile'),
('China / Xi / Singapore / other countries',r'china|chinese|xi jinping|byd|singapore|korea|indonesia|japan|france|europe|\beu\b'),
('Stock market structure and current crashes',r'stock market|crash|market is|safest market|dumping|exit|liquidity|private credit'),
('Jobs / careers / wages',r'\bjobs?\b|career|wage|job market|layoff'),('Gold / money system / dollar',r'gold|petrodollar|dollar|currency'),
('Government shutdown / US politics',r'shutdown|doj|congress|lobbying|big beautiful bill|government')]
out=[]
allv=[]
for slug in B.CH:
    nm,cid,R=B.load(slug)
    cm=st.median([r['views'] for r in R if not r['short'] and r['views'] and not r['member']] or [1])
    for r in R:
        r['channel']=nm; r['pi']=(r['views']/cm) if r['views'] and not r['short'] else None; allv.append(r)
assigned=set()
for name,pat in CL:
    M=[r for r in allv if r['id'] not in assigned and re.search(pat,r['title'].lower()) and not r['member']]
    assigned|={r['id'] for r in M}
    L=[r for r in M if not r['short'] and r['views']]; S=[r for r in M if r['short']]
    if not L and not S: continue
    ch=collections.Counter(r['channel'] for r in L)
    best=max(L,key=lambda r:r['views']) if L else None
    first=min((r for r in M if r['d']),key=lambda r:r['d'])
    pis=[r['pi'] for r in L]
    out.append(dict(topic=name,channels=len(ch),by_channel=dict(ch),long=len(L),shorts=len(S),views=sum(r['views'] for r in L),med_pi=round(st.median(pis),2) if pis else None,winners=sum(1 for r in L if r['pi']>=2),best=(best['channel'],best['title'],best['views'],best['url']) if best else None,first=(first['channel'],first['date'],first['title'])))
json.dump(out,open('stage3_topics.json','w'),indent=1)
for o in out: print(o['topic'],'|',o['channels'],'ch',o['long'],'L',o['shorts'],'S',o['views'],'med PI',o['med_pi'],'win',o['winners'],'|first',o['first'][:2])
