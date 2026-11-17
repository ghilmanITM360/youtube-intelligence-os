import numpy as np,pandas as pd,re,warnings
warnings.filterwarnings('ignore')
import statsmodels.formula.api as smf
from statsmodels.stats.multitest import multipletests
L=pd.read_pickle('out/long_classified2.pkl'); v=pd.read_pickle('out/videos_feat2.pkl'); T=L.title.fillna('')
ch=pd.read_pickle('out/channels.pkl')
L['group']=L.video_id.map(v.set_index('video_id').group)
P={'audience_target_age':r"(senior|seniors|over 6\d|over 5\d|after 6\d|at 6\d|age 6\d|retiree|retirees|retired|boomer|over 70|over 65|over 60|if you're (over|retiring)|60\+|65\+)",
'gap_most_miss':r"(most (people|seniors|retirees|never|miss|don't|do not|still)|nobody tells|never told|no one tells|don't know|doesn't tell|not required to tell|owes you|they can't)",
'numbered_list_lead':r"^\s*\d+\s",
'deadline_date':r"(before (october|november|december|january|march|april|june|july|aug|sept|\w+ \d+)|by (october|november|december|january)|in 2026|in 2027|starting|new rule|changes?\b|\bnew\b)",
'authority_agency':r"(irs|ssa|social security|medicare|medicaid|hmrc|dwp|cra|va\b|treasury|fdic|fed)",
'dash_split':r"\s[—–]\s",
'free_perks_money_owed':r"(free|owes you|will give you|refund|rebate|unclaimed|discount|can't take|cannot touch|can't touch)"}
rows=[]
for k,p in P.items():
    L[k]=T.str.contains(p,case=False,regex=True)
for k in P:
  for scope,d in [('all',L)]+[(g,x) for g,x in L.groupby('group') if len(x)>200]:
    d=d.copy(); d['f']=d[k].astype(float); n1=int(d.f.sum())
    if n1<30 or len(d)-n1<30: continue
    m=smf.ols('logPI~f',d).fit(cov_type='cluster',cov_kwds={'groups':d.channel_id.astype('category').cat.codes}); pos=tot=0
    for cid,g in d.groupby('channel_id'):
        a=g[g.f==1].logPI;b=g[g.f==0].logPI
        if len(a)>=4 and len(b)>=4: tot+=1;pos+=a.mean()>b.mean()
    rows.append(dict(pattern=k,scope=scope,n_with=n1,n_without=len(d)-n1,median_PI_with=d[d.f==1].PI.median(),median_PI_without=d[d.f==0].PI.median(),
      breakout_rate_with=(d[d.f==1].perf_class=='Breakout').mean()*100,breakout_rate_without=(d[d.f==0].perf_class=='Breakout').mean()*100,
      ratio=np.exp(m.params['f']),ci_lo=np.exp(m.conf_int().loc['f',0]),ci_hi=np.exp(m.conf_int().loc['f',1]),p=m.pvalues['f'],ch_pos=pos,ch_tot=tot,n_channels=d.channel_id.nunique()))
R=pd.DataFrame(rows); R['q_BH']=multipletests(R.p,method='fdr_bh')[1]; R.to_csv('out/discovered_pattern_tests.csv',index=False)
print(R.round(3).to_string())
# conjunction: age target + gap + number
L['senior_formula']=L.audience_target_age&L.gap_most_miss
for scope,d in [('all',L)]+[(g,x) for g,x in L.groupby('group')]:
    a=d[d.senior_formula]; b=d[~d.senior_formula]
    if len(a)>=20: print(scope,'formula n',len(a),'median PI',round(a.PI.median(),2),'vs',round(b.PI.median(),2),'breakout',round((a.perf_class=='Breakout').mean()*100,1),'vs',round((b.perf_class=='Breakout').mean()*100,1))
L.to_pickle('out/long_classified2.pkl')
