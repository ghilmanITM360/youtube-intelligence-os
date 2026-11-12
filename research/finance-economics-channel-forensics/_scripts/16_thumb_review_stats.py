"""Join blind scores to hidden key; within-channel winners (top PI/views) vs losers (bottom)."""
import pandas as pd, numpy as np, os, re
from scipy import stats
L=os.path.expanduser('~/YIOS-local-audits/finance-viral-forensics-2026-11-12/out')
k=pd.read_csv(L+'/thumb_review_key.csv'); rows=[]
for ln in open(L+'/thumb_review_scores.txt'):
    if ln.startswith('#') or not ln.strip(): continue
    c,*t=ln.split(); 
    for x in t: rows.append((int(c),x[0],*map(int,x[1:])))
s=pd.DataFrame(rows,columns=['channel_number','tile','I','N','C','E']); s['total']=s[['I','N','C','E']].sum(axis=1)
d=k.merge(s,on=['channel_number','tile'],validate='1:1'); assert len(d)==len(s)
d.to_csv(L+'/thumb_review_scored.csv',index=False)
print('tiles',len(d),'channels',d.channel_number.nunique())
out=[]; crit=['I','N','C','E','total']
g=d.groupby(['channel_number','grp'])[crit].mean().unstack()
for c in crit:
    diff=(g[(c,'W')]-g[(c,'L')]).dropna()
    nz=diff[diff!=0]
    p=stats.wilcoxon(nz).pvalue if len(nz)>=6 else np.nan
    out.append(dict(criterion=c,n_channels=len(diff),mean_W=g[(c,'W')].mean(),mean_L=g[(c,'L')].mean(),mean_diff=diff.mean(),ch_W_higher=(diff>0).sum(),ch_L_higher=(diff<0).sum(),ch_tie=(diff==0).sum(),wilcoxon_p=p))
r=pd.DataFrame(out)
ok=r.wilcoxon_p.notna(); m=ok.sum(); o=r.wilcoxon_p[ok].sort_values(); q=(o*m/np.arange(1,m+1))[::-1].cummin()[::-1].clip(upper=1); r.loc[q.index,'q_BH']=q
# within-channel Spearman of total vs rank metric, averaged
sp=[]
for n,x in d.groupby('channel_number'):
    v=x.PI.where(x.rank_col=='PI',x.views)
    if x.total.nunique()>1 and len(x)>=4: sp.append(stats.spearmanr(x.total,v)[0])
r.to_csv(L+'/thumb_review_results.csv',index=False)
print(r.round(3).to_string()); print('mean within-channel spearman total~perf',np.mean(sp).round(3),'n',len(sp),'ttest p',stats.ttest_1samp(sp,0).pvalue.round(3))
# pooled score distribution by grp
print(d.groupby('grp')[crit].mean().round(2))
# channel-type strata: high vs low variance of scores
print('per-channel diff total:');print((g[('total','W')]-g[('total','L')]).round(2).to_string())
