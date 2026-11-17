import re,numpy as np,pandas as pd
from collections import defaultdict
v=pd.read_pickle('out/videos.pkl')
# ---------- classification (long-form only; short analysed separately) ----------
MINAGE=14; K=15; MINCOMP=6; MINCH=12
v['eligible_base']=v.views.notna()&(v.age_days.isna()|(v.age_days>=MINAGE))
v['baseline']=np.nan; v['baseline_method']=''
for (cid,fmt),g in v[v.eligible_base].groupby(['channel_id','fmt']):
    if len(g)<MINCH: continue
    med=g.views.median()
    dated=g[g.pub.notna()].sort_values('pub'); t=dated.pub.astype('int64').values; vals=dated.views.values; ids=dated.index.values
    for j,i in enumerate(ids):
        d=np.abs(t-t[j]); d[j]=np.iinfo(np.int64).max
        nn=np.argsort(d)[:K]; nn=nn[d[nn]<np.iinfo(np.int64).max]
        if len(nn)>=MINCOMP: v.loc[i,'baseline']=np.median(vals[nn]); v.loc[i,'baseline_method']=f'temporal_neighbors_k{K}'
    und=g[g.pub.isna()].index
    v.loc[und,'baseline']=med; v.loc[und,'baseline_method']='channel_median_undated'
v['PI']=v.views/v.baseline
def cls(x):
    if pd.isna(x): return 'NOT_CLASSIFIED'
    return 'Breakout' if x>=5 else 'Successful' if x>=2 else 'Average' if x>=.5 else 'Underperforming'
v['perf_class']=v.PI.map(cls)
v['logPI']=np.log(v.PI)
v['rel_perf_pct']=v.PI*100
# ---------- title features ----------
T=v.title.fillna('')
w=lambda p:T.str.contains(p,case=False,regex=True)
v['t_len']=T.str.len(); v['t_words']=T.str.split().str.len()
v['t_number']=w(r'\d'); v['t_dollar']=w(r'[$€£]\s?\d|\b\d[\d,\.]*\s?(k|m|million|billion|trillion|dollars)\b')
v['t_question']=w(r'\?'); v['t_colon_dash']=w(r'[:\|–—-]\s')
v['t_paren']=w(r'[\(\[]'); v['t_year']=w(r'\b20(2\d)\b')
v['t_you']=w(r'\b(you|your|you\'re)\b'); v['t_first_person']=w(r'\b(i|my|me|we|our)\b')
v['t_caps_word']=T.map(lambda s:any(x.isupper() and len(x)>=3 and x.isalpha() for x in s.split()))
v['t_pov']=w(r'\bpov\b')
v['t_fear_risk']=w(r'\b(crash|collapse|broke|bankrupt|scam|trap|danger|warning|risk|mistake|mistakes|stop|never|dead|ruin|lose|losing|worst|fail|crisis|recession|debt|panic|fall|falling|disaster)\b')
v['t_secret_truth']=w(r'\b(secret|truth|hidden|nobody|no one|they don\'t|really|actually|real reason|exposed|why)\b')
v['t_urgency']=w(r'\b(now|today|before|urgent|immediately|soon|this year|2026|2027|breaking|just)\b')
v['t_howto_explained']=w(r'\b(how to|how|explained|explains|guide|why|what is|works)\b')
v['t_named_entity']=w(r'\b(trump|elon|musk|buffett|fed|federal reserve|apple|tesla|amazon|nvidia|bitcoin|social security|medicare|irs|china|jpmorgan|dimon|vanguard|bezos|gates|walmart|google)\b')
v['t_ranking_list']=w(r'\b(top|best|biggest|\d+ (ways|things|reasons|mistakes|tips|stocks|etfs|rules))\b')
v['t_story_fmt']=w(r'\b(pov|story|rise and fall|how .* (built|became|made)|what happened)\b')
# ---------- transcript features ----------
STOP=set('the a an and or of to in on for with is are was were be it this that how why what you your i my we our at as by from about do does'.split())
def words(s): return re.findall(r"[a-z0-9$%']+",s.lower())
def feats(r):
    s=r.text
    if not isinstance(s,str) or len(s)<200: return pd.Series(dtype=float)
    s=re.sub(r'\[[^\]]*\]|>>','',s); s=re.sub(r'\s+',' ',s)
    W=words(s); n=len(W); f={}
    f['x_words']=n
    W75=W[:75]; first=' '.join(W75); first150=' '.join(W[:150]); f10=' '.join(W[:25]); f5=' '.join(W[:12])
    sents=re.split(r'(?<=[.?!])\s+',s); s1=sents[0] if sents else ''
    tw=[x for x in words(r.title) if x not in STOP and len(x)>2]
    f['h_first_sentence_q']=s1.strip().endswith('?')
    f['h_q_in_30s']='?' in ' '.join(re.split(r'\s+',s)[:85])
    f['h_you_in_30s']=bool(re.search(r"\b(you|your|you're)\b",first))
    f['h_you_open']=bool(re.match(r"\W*(have you|do you|did you|what if you|if you|you |imagine|picture)",s.lower()))
    f['h_number_30s']=bool(re.search(r'\d',first))
    f['h_dollar_30s']=bool(re.search(r'\$|\bpercent\b|%|\bmillion\b|\bbillion\b|\btrillion\b|\bthousand\b',first))
    f['h_but_30s']=len(re.findall(r"\bbut\b|\bhowever\b|\byet\b|\bexcept\b",first))
    f['h_contrarian_30s']=bool(re.search(r"(most people|everyone|nobody|no one|you've been told|myth|wrong|actually|the truth|the real|doesn't work|isn't what)",first))
    f['h_stakes_30s']=bool(re.search(r"\b(lose|losing|broke|crash|collapse|risk|danger|trap|cost you|bankrupt|wipe|destroy|panic|disaster|ruin|afford|mistake)\b",first))
    f['h_open_loop_30s']=bool(re.search(r"(by the end|stay|until the end|i'll show|i will show|you'll see|here's why|here is why|let me explain|let's break|in this video|today we|but first|wait|that's what we|find out|the answer)",first150))
    f['h_promise_30s']=bool(re.search(r"(in this video|today (i|we)|i'll show|i will show|here's how|here is how|you'll learn|we're going to|let's (look|break|talk|dive))",first150))
    f['h_story_open']=bool(re.match(r"\W*(in \d{4}|it was|it's \d|picture|imagine|\d{4},|back in|when i|on [a-z]+ \d)",s.lower()))
    f['h_first_person_30s']=bool(re.search(r"\b(i|i'm|i've|my)\b",first))
    f['h_greeting_open']=bool(re.match(r"\W*(hey|hi|hello|welcome|what's up|good (morning|evening)|before we|today's video)",s.lower()))
    f['h_credibility_150']=bool(re.search(r"(years of experience|i've been|i have been|i worked|as a (cpa|financial|advisor)|i'm a|certified|my (career|clients|portfolio))",first150))
    f['h_why_matters_150']=bool(re.search(r"(why this matters|this matters|affects (you|every)|if you're (over|retir|close)|before you)",first150))
    f['h_title_overlap_30s']=np.mean([t in W75 for t in tw]) if tw else np.nan
    f['h_title_overlap_150']=np.mean([t in W[:150] for t in tw]) if tw else np.nan
    f['h_sent_len_first5']=np.mean([len(words(x)) for x in sents[:5]]) if sents else np.nan
    # position of first promise/core claim (words)
    m=re.search(r"(in this video|today (i|we)|i'll show|here's how|you'll learn|let's (look|break|talk|dive))",' '.join(W))
    f['i_promise_pos']=len(' '.join(W)[:m.start()].split()) if m else np.nan
    f['i_sponsor_or_plug_300']=bool(re.search(r"(sponsor|subscribe|like and|hit the bell|link in the description|patreon|newsletter)",' '.join(W[:300])))
    f['i_bg_markers_150']=len(re.findall(r"\b(history|originally|founded|born in|back in \d{4}|in \d{4})\b",first150))
    # script
    f['s_num_density']=len(re.findall(r'\b\d[\d,\.]*\b',s))/max(n,1)*100
    f['s_q_density']=s.count('?')/max(n,1)*100
    f['s_but_density']=len(re.findall(r"\bbut\b",s.lower()))/max(n,1)*100
    f['s_therefore_density']=len(re.findall(r"\b(therefore|so that's why|which means|that's why|as a result|because of this|this is why)\b",s.lower()))/max(n,1)*100
    f['s_example_density']=len(re.findall(r"(for example|for instance|imagine|let's say|say you|picture this|think of it|like a |as if)",s.lower()))/max(n,1)*100
    f['s_data_density']=len(re.findall(r"(percent|%|according to|study|data|report|research|survey|\$\d)",s.lower()))/max(n,1)*100
    f['s_loop_density']=len(re.findall(r"(but here's|here's the (thing|catch|problem)|we'll get to|more on that|hold that thought|stick around|which brings us|the real question|so what happened|what happened next|here's where)",s.lower()))/max(n,1)*100
    f['s_you_density']=len(re.findall(r"\b(you|your)\b",s.lower()))/max(n,1)*100
    f['s_ttr']=len(set(W[:1500]))/max(len(W[:1500]),1)
    f['s_sent_len']=n/max(len(sents),1)
    tail=' '.join(W[-int(n*.1):]) if n>200 else ''
    f['s_cta_end']=bool(re.search(r"(subscribe|like|comment|next video|watch (this|next)|check out|link below|description)",tail))
    f['s_cta_any_density']=len(re.findall(r"(subscribe|hit the like|leave a comment|smash)",s.lower()))/max(n,1)*1000
    f['s_wpm']=n/(r.duration_seconds/60) if r.duration_seconds else np.nan
    return pd.Series(f)
F=v.apply(feats,axis=1)
for c in F.columns: v[c]=F[c]
# ---------- duplicate script detection (rule 9) ----------
def sh(s,k=8):
    W=words(re.sub(r'\[[^\]]*\]','',s))[:400]; return {hash(' '.join(W[i:i+k])) for i in range(max(len(W)-k,0))}
S={i:sh(t) for i,t in v.text.items() if isinstance(t,str) and len(t)>500}
inv=defaultdict(list)
for i,hs in S.items():
    for h in hs: inv[h].append(i)
cnt=defaultdict(int)
for h,ids in inv.items():
    if 1<len(ids)<40:
        for a in ids:
            for b in ids:
                if a<b: cnt[(a,b)]+=1
dups=[]
for (a,b),c in cnt.items():
    jac=c/len(S[a]|S[b]) if (S[a]|S[b]) else 0
    if jac>=.25: dups.append((v.video_id[a],v.video_id[b],v.channel_id[a],v.channel_id[b],round(jac,3)))
dd=pd.DataFrame(dups,columns=['video_a','video_b','channel_a','channel_b','jaccard_first400w'])
dd.to_csv('out/near_duplicate_scripts.csv',index=False)
v['dup_script_flag']=v.video_id.isin(set(dd.video_a)|set(dd.video_b))
print('near-dup pairs',len(dd),'videos flagged',v.dup_script_flag.sum(),'cross-channel pairs',(dd.channel_a!=dd.channel_b).sum())
print(v.perf_class.value_counts()); print(v.groupby('fmt').PI.describe())
v.to_pickle('out/videos_feat.pkl')
v.drop(columns=['text']).to_csv('out/unique_video_performance_database.csv',index=False)
