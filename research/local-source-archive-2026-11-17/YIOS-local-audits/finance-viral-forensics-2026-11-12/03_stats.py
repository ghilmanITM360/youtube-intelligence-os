import numpy as np,pandas as pd,warnings,json
warnings.filterwarnings('ignore')
import statsmodels.formula.api as smf
from scipy import stats
from statsmodels.stats.multitest import multipletests
v=pd.read_pickle('out/videos_feat.pkl')
L=v[(v.fmt=='long')&v.PI.notna()].copy()
print('classified long',len(L),'channels',L.channel_id.nunique())
BINH=[c for c in v.columns if c.startswith(('h_','i_','s_')) and v[c].dropna().isin([0,1,True,False]).all() and v[c].notna().sum()>0 and not c.endswith('_density')]
for c in BINH: L[c]=L[c].astype(float).where(L[c].notna())
tf=[c for c in L.columns if c.startswith('t_') and c not in('t_len','t_words')]
hf=[c for c in BINH if c.startswith(('h_','i_'))]
sf=[c for c in BINH if c.startswith('s_')]
cont=['t_len','t_words','h_but_30s','h_title_overlap_30s','h_title_overlap_150','h_sent_len_first5','i_promise_pos','i_bg_markers_150',
 's_num_density','s_q_density','s_but_density','s_therefore_density','s_example_density','s_data_density','s_loop_density','s_you_density','s_ttr','s_sent_len','s_cta_any_density','s_wpm','x_words','duration_seconds']
rows=[]
def chan_consistency(d,col,binary=True):
    pos=tot=0
    for cid,g in d.groupby('channel_id'):
        if binary:
            a=g[g[col]==True].logPI; b=g[g[col]==False].logPI
            if len(a)>=4 and len(b)>=4: tot+=1; pos+= a.mean()>b.mean()
        else:
            g=g.dropna(subset=[col])
            if len(g)>=15 and g[col].nunique()>3:
                r=stats.spearmanr(g[col],g.logPI)[0]
                if not np.isnan(r): tot+=1; pos+= r>0
    return pos,tot
for col in tf+hf+sf:
    d=L.dropna(subset=[col]).copy(); d['f']=d[col].astype(float); n1=int(d.f.sum()); n0=len(d)-n1
    if n1<30 or n0<30: continue
    m=smf.ols('logPI~f',d).fit(cov_type='cluster',cov_kwds={'groups':d.channel_id.astype('category').cat.codes})
    pos,tot=chan_consistency(d,col)
    br=lambda x:(x.perf_class.isin(['Breakout','Successful'])).mean()*100
    un=lambda x:(x.perf_class=='Underperforming').mean()*100
    rows.append(dict(layer='title' if col in tf else 'hook/intro' if col in hf else 'script',feature=col,n_with=n1,n_without=n0,
      med_PI_with=d[d.f==1].PI.median(),med_PI_without=d[d.f==0].PI.median(),succ_rate_with=br(d[d.f==1]),succ_rate_without=br(d[d.f==0]),
      under_rate_with=un(d[d.f==1]),under_rate_without=un(d[d.f==0]),coef_logPI=m.params['f'],ratio_exp=np.exp(m.params['f']),
      ci_lo=np.exp(m.conf_int().loc['f',0]),ci_hi=np.exp(m.conf_int().loc['f',1]),p_cluster=m.pvalues['f'],ch_pos=pos,ch_tot=tot,
      n_channels=d.channel_id.nunique()))
B=pd.DataFrame(rows)
B['q_BH']=multipletests(B.p_cluster,method='fdr_bh')[1]
def verdict(r):
    cons=r.ch_pos/r.ch_tot if r.ch_tot else np.nan
    if r.q_BH<.05 and r.ci_lo>1 and cons>=.6: return 'SUPPORTED_POSITIVE(cross-channel)'
    if r.q_BH<.05 and r.ci_hi<1 and cons<=.4: return 'SUPPORTED_NEGATIVE(cross-channel)'
    if r.q_BH<.05: return 'POOLED_ONLY(weak channel replication)'
    return 'NO_RELIABLE_EFFECT'
B['verdict']=B.apply(verdict,axis=1)
B.sort_values('p_cluster').to_csv('out/binary_feature_tests.csv',index=False)
rows=[]
for col in cont:
    d=L.dropna(subset=[col]); 
    if len(d)<200: continue
    rho,p=stats.spearmanr(d[col],d.logPI); pos,tot=chan_consistency(d,col,False)
    # within-channel mean rho
    rows.append(dict(feature=col,n=len(d),spearman_rho=rho,p=p,ch_pos=pos,ch_tot=tot,n_channels=d.channel_id.nunique()))
C=pd.DataFrame(rows); C['q_BH']=multipletests(C.p,method='fdr_bh')[1]
C.sort_values('p').to_csv('out/continuous_feature_tests.csv',index=False)
print(B.sort_values('p_cluster')[['feature','n_with','med_PI_with','med_PI_without','ratio_exp','ci_lo','ci_hi','q_BH','ch_pos','ch_tot','verdict']].round(3).to_string())
print(C.sort_values('p').round(3).to_string())
# ---------- sensitivity: percentile-based classes ----------
L['pct']=L.groupby('channel_id').PI.rank(pct=True)
# ---------- matched pairs ----------
W=L[L.perf_class.isin(['Breakout','Successful'])]; U=L[L.perf_class=='Underperforming']
used=set(); pairs=[]
for i,r in W.sort_values('PI',ascending=False).iterrows():
    c=U[(U.channel_id==r.channel_id)&(~U.index.isin(used))]
    if r.pub is not pd.NaT and pd.notna(r.pub): c=c[c.pub.notna()&((c.pub-r.pub).abs().dt.days<=150)]
    else: continue
    c=c[(c.duration_seconds/r.duration_seconds).between(.6,1.67)]
    if len(c)==0: continue
    j=(c.pub-r.pub).abs().dt.days.idxmin(); used.add(j); u=L.loc[j]
    pairs.append(dict(channel_id=r.channel_id,channel=r['name'],win_id=r.video_id,win_title=r.title,win_views=r.views,win_PI=r.PI,lose_id=u.video_id,lose_title=u.title,lose_views=u.views,lose_PI=u.PI,days_apart=abs((u.pub-r.pub).days),dur_ratio=u.duration_seconds/r.duration_seconds,**{f'W_{c}':r[c] for c in tf+hf+sf},**{f'U_{c}':u[c] for c in tf+hf+sf}))
P=pd.DataFrame(pairs); P.to_csv('out/matched_pairs.csv',index=False); print('pairs',len(P),'channels',P.channel_id.nunique())
mp=[]
for col in tf+hf+sf:
    a=P[f'W_{col}'].astype(float); b=P[f'U_{col}'].astype(float); ok=a.notna()&b.notna()
    wo=int(((a==1)&(b==0)&ok).sum()); uo=int(((a==0)&(b==1)&ok).sum())
    if wo+uo>=15: mp.append(dict(feature=col,winner_only=wo,loser_only=uo,discordant=wo+uo,sign_p=stats.binomtest(wo,wo+uo,.5).pvalue))
MP=pd.DataFrame(mp); MP['q_BH']=multipletests(MP.sign_p,method='fdr_bh')[1]; MP.sort_values('sign_p').to_csv('out/matched_pair_tests.csv',index=False)
print(MP.sort_values('sign_p').round(3).head(15).to_string())
L.to_pickle('out/long_classified.pkl')
