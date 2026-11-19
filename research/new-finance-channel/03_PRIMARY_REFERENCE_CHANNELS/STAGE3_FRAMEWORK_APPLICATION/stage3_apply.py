"""Stage 3: apply framework rules (DS-000011, DS-000018, Playbook, framework DB) to actual six-channel videos.
Read-only on DB. Writes features CSV + results JSON for the report. Run: uv run --with scipy python stage3_apply.py"""
import sys, re, json, csv, math, statistics as st, itertools, collections, sqlite3
sys.path.insert(0,'../STAGE2_SIX_REPORTS')
import build_data as B
try:
    from scipy.stats import mannwhitneyu
except Exception:
    mannwhitneyu=None
SUBS={'Crayon Capital':319000,'MonkeyExplains':261000,'Capital Case':12000,'Casual Finance':440000,'Monkey Economics':224000,'Paper Billions':23600}
STOP=set('the a an and or of to in on for with is are was were be been it its this that these those why how what when who from by at as into than then just your you we our their they he she his her has have had not can could will would about over under more most very so but if'.split())
def words(t): return re.findall(r"[A-Za-z0-9$%'’.-]+",t)
def content(t): return {w.lower().strip(".'’-") for w in re.findall(r"[A-Za-z]{4,}",t) if w.lower() not in STOP}
MONTH=r'january|february|march|april|may|june|july|august|september|october|november|december'
FEAT={}
FAM={'curiosity/threat':r'worse than|nobody|no one|secret|hidden|truth|worst|terrifying|disturbing|brace|warning|trap|scam|lie',
 'explainer':r'explained|how |why |what ','warning/crisis':r'crash|crisis|collapse|bubble|recession|depression|bust|doom|breaking|imploding',
 'story/person':r'story of|rise of|how .* (built|became|got)|actually (built|happened|became)|man who',
 'contrarian':r"\bnot\b|never|isn't|wrong|myth|but |actually|(?<!\w)un\w+",'urgency/time':r'\bnow\b|today|2026|just |already|finally|again|keeps getting|yet\b',
 'question':r'\?','list/number':r'\d','superlative':r'biggest|worst|first|most|largest|greatest|best'}
def feats(r):
    t=r['title']; w=words(r['tx']); n=len(w); o60=' '.join(w[:60]); o75=' '.join(w[:75]); o120=' '.join(w[:120]); cl=' '.join(w[-150:])
    tc=content(t)
    f={}
    f['title_le55']=len(t)<=55
    f['title_digit']=bool(re.search(r'\d',t)); f['title_caps']=any(len(x)>2 and x.isupper() and x.isalpha() for x in t.split())
    f['title_dq']=t.count('?')>=2
    for k,p in FAM.items(): f['fam_'+k]=bool(re.search(p,t.lower()))
    f['dur_ge8']=r['dur']>=480
    f['open_digits']=len(re.findall(r'\d',o60))>=2 or bool(re.search(r'\b(million|billion|trillion|percent)\b|%|\$',o60.lower()))
    f['open_dated']=bool(re.search(r'\b(20[12]\d|'+MONTH+r')\b|last (week|month|year)|yesterday|days ago|this week|today|just (a )?(few|last)|weeks ago',o75.lower()))
    f['open_contrarian']=bool(re.search(r"\bbut\b|however|except|actually|so you'd think|the problem|wasn't|isn't|turns out|here's the|the real|never|nobody|no one|\byet\b|wait\b",o120.lower()))
    f['open_you']=bool(re.search(r"\b(you|your|you've|you're)\b",o75.lower()))
    caps=[x for i,x in enumerate(w[:60]) if x[:1].isupper() and i>0 and not re.match(r'(The|This|But|And|So|In|It|He|She|They|We|I|A|On|At|If|That|Now)$',x)]
    f['open_entity']=len(caps)>=3
    f['kw_in_open']=(len(tc & content(o75))/len(tc)>=0.5) if tc else False
    f['echo']=(len(tc & content(cl))>=1) if tc else False
    m=re.search(r'subscribe|like (the|this) video|hit the|comment below|patreon|sponsor|link in the description|check out',' '.join(w).lower())
    pos=None
    if m: pos=len(' '.join(w).lower()[:m.start()].split())/max(n,1)
    f['cta_any']=pos is not None; f['cta_early']=pos is not None and pos<0.15
    low=' '.join(w).lower()
    f['but_rate']=1000*len(re.findall(r'\b(but|however|yet|although)\b',low))/max(n,1)
    f['therefore_rate']=1000*len(re.findall(r'\b(therefore|because|so that|which means|that\'s why|as a result|which is why)\b',low))/max(n,1)
    f['andthen_rate']=1000*len(re.findall(r'\band then\b',low))/max(n,1)
    f['words']=n
    return f
def mwu(a,b):
    if len(a)<3 or len(b)<3: return None
    if mannwhitneyu: return float(mannwhitneyu(a,b,alternative='two-sided').pvalue)
    return None
rows=[]
for slug,name in B.CH.items():
    nm,cid,R=B.load(slug)
    L=[r for r in R if not r['short'] and r['views'] is not None and r['tx'] and not r['member']]
    cm=st.median([r['views'] for r in L])
    for r in L:
        f=feats(r); f.update(channel=nm,id=r['id'],title=r['title'],views=r['views'],pi=r['views']/cm,age=r['age'],dur=r['dur'],cat=r['cat'],url=r['url'],date=r['date'],ratio_subs=r['views']/SUBS[nm],tx=r['tx'])
        rows.append(f)
print(len(rows),'videos with transcripts, public views, long-form')
BIN=[k for k in rows[0] if k in ('title_le55','title_digit','title_caps','title_dq','dur_ge8','open_digits','open_dated','open_contrarian','open_you','open_entity','kw_in_open','echo','cta_any','cta_early') or k.startswith('fam_')]
res=[]
def test(sub,label):
    out=[]
    for k in BIN:
        a=[r['pi'] for r in sub if r[k]]; b=[r['pi'] for r in sub if not r[k]]
        if len(a)<4 or len(b)<4: out.append(dict(feat=k,n_with=len(a),n_without=len(b),note='too few')); continue
        chans=collections.defaultdict(lambda:([],[]))
        for r in sub: chans[r['channel']][0 if r[k] else 1].append(r['pi'])
        agree=0;tot=0
        for c,(x,y) in chans.items():
            if len(x)>=2 and len(y)>=2: tot+=1; agree+= st.median(x)>st.median(y)
        out.append(dict(feat=k,n_with=len(a),n_without=len(b),share=len(a)/len(sub),med_with=st.median(a),med_without=st.median(b),p=mwu(a,b),chan_agree=agree,chan_tot=tot))
    return out
excl_pb=[r for r in rows if r['channel']!='Paper Billions']
older=[r for r in excl_pb if r['age'] and r['age']>=60]
res={'all':test(rows,'all'),'excl_pb':test(excl_pb,'excl_pb'),'older60':test(older,'older60')}
# continuous
def spear(x,y):
    from scipy.stats import spearmanr
    c,p=spearmanr(x,y); return float(c),float(p)
cont={}
for k in ('but_rate','therefore_rate','andthen_rate','words','dur'):
    try: cont[k]=spear([r[k] for r in excl_pb],[r['pi'] for r in excl_pb])
    except Exception as e: cont[k]=None
# repetition (P04 / CLM-009): 8-gram jaccard on first 400 words
def grams(t,n=8):
    w=[x.lower() for x in words(t)[:400]]; return {tuple(w[i:i+n]) for i in range(len(w)-n+1)}
rep={}
for ch in SUBS:
    V=[r for r in rows if r['channel']==ch]; G=[grams(r['tx']) for r in V]; js=[]
    for i,j in itertools.combinations(range(len(V)),2):
        u=len(G[i]|G[j]); js.append(len(G[i]&G[j])/u if u else 0)
    first8=collections.Counter(' '.join(w.lower() for w in words(r['tx'])[:4]) for r in V)
    rep[ch]=dict(n=len(V),pairs=len(js),mean=(st.mean(js) if js else None),max=(max(js) if js else None),ge25=sum(x>=.25 for x in js),top_open=first8.most_common(2))
# outlier ratio (Playbook 2.1): views / subs
orr={}
for ch in SUBS:
    V=[r['ratio_subs'] for r in rows if r['channel']==ch]
    orr[ch]=dict(n=len(V),ge1=sum(x>=1 for x in V),ge2=sum(x>=2 for x in V),ge5=sum(x>=5 for x in V),mx=max(V),med=st.median(V))
# age/evergreen (CLM-003)
ev={}
for ch in SUBS:
    V=[r for r in rows if r['channel']==ch and r['age']]
    if len(V)>=8:
        try: ev[ch]=spear([r['age'] for r in V],[r['views'] for r in V])
        except: ev[ch]=None
# 8+ min per channel
dur8={}
for ch in SUBS:
    V=[r for r in rows if r['channel']==ch]; a=[r['views'] for r in V if r['dur']>=480]; b=[r['views'] for r in V if r['dur']<480]
    dur8[ch]=dict(n8=len(a),med8=(st.median(a) if a else None),nlt=len(b),medlt=(st.median(b) if b else None))
json.dump(dict(res=res,cont=cont,rep=rep,orr=orr,ev=ev,dur8=dur8,n=len(rows)),open('stage3_results.json','w'),default=str,indent=1)
with open('stage3_features.csv','w',newline='') as f:
    w=csv.writer(f); cols=['channel','id','date','views','pi','age','dur','cat']+BIN+['but_rate','therefore_rate','andthen_rate','title','url']
    w.writerow(cols)
    for r in rows: w.writerow([r.get(c) if not isinstance(r.get(c),float) else round(r[c],3) for c in cols])
print('done')
