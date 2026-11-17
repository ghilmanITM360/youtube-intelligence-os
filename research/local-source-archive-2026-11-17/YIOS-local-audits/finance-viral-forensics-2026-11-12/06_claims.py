import numpy as np,pandas as pd,re,warnings
warnings.filterwarnings('ignore')
from scipy import stats
import statsmodels.formula.api as smf
v=pd.read_pickle('out/videos_feat.pkl'); L=pd.read_pickle('out/long_classified.pkl')
def words(s): return re.findall(r"[a-z0-9$%']+",s.lower())
T=v.title.fillna('')
# ---- extra features
first=v.text.fillna('').map(lambda s:' '.join(words(re.sub(r'\[[^\]]*\]','',s))[:75]))
v['h_named_entity_30s']=first.str.contains(r"\b(trump|elon|musk|buffett|warren|fed|federal reserve|apple|tesla|amazon|nvidia|bitcoin|social security|medicare|irs|china|jpmorgan|dimon|vanguard|bezos|gates|walmart|google|taylor swift)\b")
v['h_snapback3']=(v.h_you_in_30s==True)&(v.h_but_30s.fillna(0)>=1)&(v.h_contrarian_30s==True)   # DS11 Hook guide 3-step proxy
v['h_but_any']=v.h_but_30s.fillna(0)>=1
v['t_len_le60']=v.t_len<=60; v['t_len_le40']=v.t_len<=40
v['t_ends_question']=T.str.strip().str.endswith('?')
v['t_turning_x_into_y']=T.str.contains(r'\bturn(ed|ing)? .* (in)?to\b',case=False)
v['t_enhancer']=T.str.contains(r'\b(secret|money|mistake|mistakes|rich|wealth|millionaire|broke|truth|shocking|hidden)\b',case=False)
v['pub_hour_utc']=np.where(v.published.str.len()>10,v.pub.dt.hour,np.nan); v['pub_dow']=v.pub.dt.dayofweek
# ---- Viral Checklist proxy score (11 items; proxies are coarse, documented in report)
chk=pd.DataFrame({
 '1_pain_point':v.t_fear_risk|(v.h_stakes_30s==True),
 '2_promise_transformation':v.t_howto_explained|(v.h_promise_30s==True),
 '3_emotion':v.t_fear_risk|v.t_secret_truth|v.t_caps_word,
 '4_contrarian':v.t_secret_truth|(v.h_contrarian_30s==True),
 '5_specificity_numbers':v.t_number|v.t_dollar|(v.h_number_30s==True),
 '6_urgency':v.t_urgency|v.t_year,
 '7_experience_familiarity':v.t_first_person|(v.h_first_person_30s==True)|v.t_pov,
 '9_concise':v.t_len<=60,
 '10_enhancer_words':v.t_enhancer,
 '11_credibility_hack':v.t_named_entity|(v.h_named_entity_30s==True)}) # item 8 (Motivate) not proxied
v['checklist_score']=chk.sum(axis=1)
chk.assign(video_id=v.video_id).to_csv('out/viral_checklist_proxy_items.csv',index=False)
L=L.drop(columns=[c for c in L.columns if c in v.columns and c not in('video_id',)]+[]) if False else L
for c in ['h_named_entity_30s','h_snapback3','h_but_any','t_len_le60','t_len_le40','t_ends_question','t_turning_x_into_y','t_enhancer','pub_hour_utc','pub_dow','checklist_score']: L[c]=L.video_id.map(v.set_index('video_id')[c])
out=[]
def bintest(col,label,src,claim):
    d=L.dropna(subset=[col]).copy(); d['f']=d[col].astype(float)
    n1=int(d.f.sum()); n0=len(d)-n1
    if min(n1,n0)<30: return
    m=smf.ols('logPI~f',d).fit(cov_type='cluster',cov_kwds={'groups':d.channel_id.astype('category').cat.codes})
    pos=tot=0
    for cid,g in d.groupby('channel_id'):
        a=g[g.f==1].logPI;b=g[g.f==0].logPI
        if len(a)>=4 and len(b)>=4: tot+=1; pos+=a.mean()>b.mean()
    out.append(dict(source=src,claim=claim,proxy=col,n_with=n1,n_without=n0,ratio=np.exp(m.params['f']),ci_lo=np.exp(m.conf_int().loc['f',0]),ci_hi=np.exp(m.conf_int().loc['f',1]),p=m.pvalues['f'],ch_pos=pos,ch_tot=tot))
bintest('h_snapback3','','DS-000011 Hook guide','3-step formula: Context Lean -> Scroll Stop Interjection (but/however) -> Contrarian Snapback')
bintest('h_but_any','','DS-000011 Hook guide','Scroll-stop interjection (contrastive but/however/yet in opening)')
bintest('h_named_entity_30s','','DS-000011 Hook guide','Cult Hopping: familiar brand/celebrity reference in hook')
bintest('h_you_in_30s','','DS-000011 Hook guide','Benefit/pain framing: address viewer ("you") in hook')
bintest('h_number_30s','','DS-000011 Viral Checklist #5','Specificity & numbers in hook')
bintest('t_number','','DS-000011 Viral Checklist #5','Specificity & numbers in title')
bintest('t_len_le60','','DS-000011 SEO checklist / Packaging SOP','Title under 60 characters / fewer characters')
bintest('t_len_le40','','DS-000011 Packaging SOP','Fewer characters (stricter 40)')
bintest('t_enhancer','','DS-000011 Viral Checklist #10','Enhancer words (secret, money, mistake)')
bintest('t_named_entity','','DS-000011 Viral Checklist #11','Credibility hack: famous names/brands in title')
bintest('t_fear_risk','','DS-000011 Viral Checklist #1/#3','Pain point / emotion (fear-risk words)')
bintest('t_urgency','','DS-000011 Viral Checklist #6','Urgency / timeliness')
bintest('t_first_person','','DS-000011 Viral Checklist #7','Experience & familiarity (first person)')
bintest('t_ends_question','','DS-000018 tab 35 (creator claim, 4M-title study)','Titles ending in a question have ~0.82x lift')
bintest('t_turning_x_into_y','','DS-000018 tab 35 (creator claim)','"Turning X into Y" transformation frame ~3.22x lift')
bintest('s_cta_end','','DS-000011 Script Analyzer','CTA placement near end')
bintest('h_open_loop_30s','','DS-000011 Script/Intro Analyzer','Open loop / curiosity gap in first 30s')
bintest('h_promise_30s','','DS-000011 Hook guide (Compress Speed to Value / Intro Analyzer narrative promise)','Core promise stated in opening')
R=pd.DataFrame(out); R.to_csv('out/claim_binary_tests.csv',index=False); print(R.drop(columns=['source']).round(3).to_string())
# checklist
d=L.dropna(subset=['checklist_score']); rho,p=stats.spearmanr(d.checklist_score,d.logPI)
cl=d.groupby(d.checklist_score.clip(upper=7)).agg(n=('logPI','size'),median_PI=('PI','median'),success_rate=('perf_class',lambda s:s.isin(['Breakout','Successful']).mean()*100),under_rate=('perf_class',lambda s:(s=='Underperforming').mean()*100))
cl.to_csv('out/viral_checklist_score_vs_perf.csv'); print('checklist rho',round(rho,3),'p',round(p,4),'n',len(d)); print(cl.round(2))
mm=smf.ols('logPI~checklist_score',d).fit(cov_type='cluster',cov_kwds={'groups':d.channel_id.astype('category').cat.codes}); print('per-point ratio',np.exp(mm.params['checklist_score']),np.exp(mm.conf_int().loc['checklist_score'].values),mm.pvalues['checklist_score'])
# publish time (UTC) & dow
dt=L.dropna(subset=['pub_dow']); 
print('DOW kruskal p',stats.kruskal(*[g.logPI.values for _,g in dt.groupby('pub_dow')]).pvalue, dt.groupby('pub_dow').PI.agg(['size','median']).round(2).to_dict())
dh=L.dropna(subset=['pub_hour_utc']); print('HOUR kruskal p',stats.kruskal(*[g.logPI.values for _,g in dh.groupby(pd.cut(dh.pub_hour_utc,[-1,5,11,17,23]))]).pvalue)
# ---- format
sh=v[(v.fmt=='short')&v.PI.notna()]; print('shorts classified',len(sh),'median PI',sh.PI.median())
fm=v[v.views.notna()].groupby(['channel_id','fmt']).views.median().unstack().dropna(); print('channels with both formats',len(fm),'short/long median views ratio (median across channels)',(fm.short/fm.long).median())
# ---- channel level: cadence, topic concentration, subs
cs=[]
for cid,g in v[(v.fmt=='long')&v.pub.notna()].groupby('channel_id'):
    if len(g)<20: continue
    span=(g.pub.max()-g.pub.min()).days
    if span<30: continue
    shares=g.topic_id.value_counts(normalize=True); ent=-(shares*np.log(shares)).sum()
    cs.append(dict(channel_id=cid,name=g['name'].iloc[0],n=len(g),uploads_per_30d=len(g)/span*30,topic_entropy=ent,median_views=g.views.median(),median_dur=g.duration_seconds.median(),subs=g.subscribers.iloc[0],n_dated=len(g)))
C=pd.DataFrame(cs); C['lmv']=np.log(C.median_views)
for col in ['uploads_per_30d','topic_entropy','median_dur']:
    r,p=stats.spearmanr(C[col],C.lmv); print('channel-level',col,'rho',round(r,3),'p',round(p,3),'n',len(C))
Cs=C.dropna(subset=['subs']); r,p=stats.spearmanr(np.log(Cs.subs),Cs.lmv); print('subs vs median views rho',round(r,3),'p',round(p,4),'n',len(Cs))
C.to_csv('out/channel_level_structure.csv',index=False)
# outlier ratio views/subs (Playbook Module 2.1)
o=v[(v.fmt=='long')&v.subscribers.notna()&v.views.notna()].copy(); o['outlier_ratio']=o.views/o.subscribers
bins=pd.cut(o.outlier_ratio,[0,1,3,5,10,50,100,1e9],labels=['<1x','1-3x','3-5x','5-10x','10-50x','50-100x','100x+']); print(bins.value_counts(sort=False).to_dict(),'n',len(o),'channels',o.channel_id.nunique())
o['PIbreak']=o.perf_class.isin(['Breakout'])
print('Playbook outlier>=10x videos that are NOT breakout vs own baseline:', ((o.outlier_ratio>=10)&(o.perf_class!='Breakout')&o.PI.notna()).sum(),'of',((o.outlier_ratio>=10)&o.PI.notna()).sum())
print('agreement spearman(outlier_ratio, PI):',stats.spearmanr(o.dropna(subset=['PI']).outlier_ratio,o.dropna(subset=['PI']).PI)[0])
# breakout rate by sub tier
o2=L[L.subscribers.notna()].copy(); o2['tier']=pd.cut(o2.subscribers,[0,5e3,2e4,1e5,1e9],labels=['<5k','5-20k','20-100k','100k+'])
tr=o2.groupby('tier').agg(n=('PI','size'),channels=('channel_id','nunique'),breakout_rate=('perf_class',lambda s:(s=='Breakout').mean()*100),success_rate=('perf_class',lambda s:s.isin(['Breakout','Successful']).mean()*100),median_views=('views','median')); print(tr.round(1)); tr.to_csv('out/subscriber_tier_outcomes.csv')
# ---- audience problems (rule-based taxonomy; multi-label on title + first 150 transcript words)
ap={'retirement_money_runs_out':r"(retire|retirement|retiree|401k|ira\b|rmd|pension|nest egg|run out of money|outlive)",
'social_security_benefits_changes':r"(social security|medicare|medicaid|ssi\b|ssa\b|cola|benefit|survivor|disability|va benefit|cpp|oas)",
'taxes_irs':r"(\birs\b|tax|taxes|roth|hmrc|deduction|audit)",
'banking_accounts_scams':r"(bank account|freeze|scam|fraud|joint account|seniors? miss|bank)",
'inflation_cost_of_living':r"(inflation|cost of living|prices|grocery|afford|expensive|housing|rent|mortgage)",
'investing_returns_dividends':r"(dividend|etf|index fund|stock|stocks|portfolio|invest|s&p|schd|vanguard|compound)",
'wealth_status_pov_class':r"(\bpov\b|net worth|millionaire|rich people|wealthy|wealth|poor|salary|income level|lottery|old money)",
'frugality_habits_psychology':r"(frugal|habit|mindset|stealth wealth|spend|save|saving|budget|psychology|lifestyle)",
'macro_crisis_collapse':r"(crash|collapse|recession|crisis|depression|bubble|debt|default|fed\b|rates?\b|dollar|tariff|trade war|economy)",
'business_company_history':r"(company|empire|brand|history|rise and fall|founder|how .* (built|made)|business model|ceo|economics of|monopoly|supply chain|industry)",
'explainer_eli5_concepts':r"(explained|eli5|like you're 5|like you're five|simply|what is|how .* works|bananas|for beginners)"}
txt=(T+' '+first.where(v.text.notna(),'')).str.lower()
tag=pd.DataFrame({k:txt.str.contains(p,regex=True) for k,p in ap.items()}); 
Lt=L[['video_id','PI','perf_class','channel_id','views']].join(tag.set_index(v.video_id).loc[L.video_id].reset_index(drop=True).set_index(L.index))
rows=[]
allc=v[v.fmt=='long']
for k in ap:
    g=Lt[Lt[k]]; n_all=int(tag.loc[allc.index,k].sum())
    if len(g)<30: continue
    rows.append(dict(audience_problem=k,videos_classified=len(g),videos_total_long=n_all,supply_share_pct=n_all/len(allc)*100,channels=g.channel_id.nunique(),median_PI=g.PI.median(),median_views=g.views.median(),
      success_rate=g.perf_class.isin(['Breakout','Successful']).mean()*100,breakout_rate=(g.perf_class=='Breakout').mean()*100,under_rate=(g.perf_class=='Underperforming').mean()*100,top_channel_share=g.channel_id.value_counts(normalize=True).iloc[0]*100))
AP=pd.DataFrame(rows).sort_values('median_PI',ascending=False); AP.to_csv('out/audience_problem_database.csv',index=False); print(AP.round(2).to_string())
tag.assign(video_id=v.video_id).to_csv('out/audience_problem_tags.csv',index=False)
v.to_pickle('out/videos_feat2.pkl'); L.to_pickle('out/long_classified2.pkl')
