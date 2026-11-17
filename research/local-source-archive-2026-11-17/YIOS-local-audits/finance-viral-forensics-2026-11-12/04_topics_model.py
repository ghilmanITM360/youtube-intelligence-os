import numpy as np,pandas as pd,warnings,re
warnings.filterwarnings('ignore')
import statsmodels.formula.api as smf, statsmodels.api as sm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import silhouette_score, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import GroupKFold
v=pd.read_pickle('out/videos_feat.pkl'); L=pd.read_pickle('out/long_classified.pkl')
# --- variance decomposition of log views (long, views>0)
D=v[(v.fmt=='long')&v.views.notna()&(v.views>0)].copy(); D['lv']=np.log(D.views)
m0=smf.ols('lv~C(channel_id)',D).fit(); print('R2 channel only (log views):',round(m0.rsquared,3),'n',len(D))
D2=D[D.pub.notna()].copy(); D2['la']=np.log(D2.age_days.clip(lower=1))
m1=smf.ols('lv~C(channel_id)+la+I(la**2)',D2).fit(); print('R2 channel+age:',round(m1.rsquared,3))
# --- topics from titles (derived from data)
txt=(v.title.fillna('')).str.lower().str.replace(r'[^a-z\s]',' ',regex=True)
tv=TfidfVectorizer(stop_words='english',min_df=8,max_df=.25,ngram_range=(1,2),sublinear_tf=True)
X=tv.fit_transform(txt); Z=TruncatedSVD(60,random_state=0).fit_transform(X); Z/=np.linalg.norm(Z,axis=1,keepdims=True)+1e-9
best=None
for k in [10,14,18,22]:
    km=KMeans(k,n_init=10,random_state=0).fit(Z); s=silhouette_score(Z,km.labels_,sample_size=2000,random_state=0); print(k,round(s,3))
    if k==18: best=km
km=best; v['topic_id']=km.labels_
terms=np.array(tv.get_feature_names_out()); cent=np.asarray(X.T.dot(np.eye(len(v))[:,:0]) if False else 0)
tops={}
for t in range(km.n_clusters):
    idx=np.where(km.labels_==t)[0]; score=np.asarray(X[idx].mean(axis=0)).ravel(); tops[t]=', '.join(terms[np.argsort(-score)[:9]])
v['topic_terms']=v.topic_id.map(tops)
L=L.merge(v[['video_id','topic_id']],on='video_id',how='left') if 'topic_id' not in L else L
L['topic_id']=L.video_id.map(v.set_index('video_id').topic_id)
rows=[]
rng=np.random.default_rng(0)
for t,g in L.groupby('topic_id'):
    br=g.perf_class.isin(['Breakout','Successful']); bo=g.perf_class=='Breakout'; un=g.perf_class=='Underperforming'
    # cluster bootstrap CI for median logPI by channel resampling
    chs=g.channel_id.unique(); meds=[]
    for _ in range(300):
        s=rng.choice(chs,len(chs)); meds.append(np.median(np.concatenate([g[g.channel_id==c].logPI.values for c in s])))
    rows.append(dict(topic_id=t,top_terms=tops[t],n_videos=len(g),n_channels=g.channel_id.nunique(),median_views=g.views.median(),median_PI=g.PI.median(),
      PI_ci95_lo=np.exp(np.percentile(meds,2.5)),PI_ci95_hi=np.exp(np.percentile(meds,97.5)),success_rate=br.mean()*100,breakout_rate=bo.mean()*100,underperf_rate=un.mean()*100,
      top_channel_share=g.channel_id.value_counts(normalize=True).iloc[0]*100))
TP=pd.DataFrame(rows).sort_values('median_PI',ascending=False); TP.to_csv('out/topic_cluster_database.csv',index=False); print(TP.round(2).to_string())
# omnibus: topic within-channel effect
mt=smf.ols('logPI~C(topic_id)',L).fit(cov_type='cluster',cov_kwds={'groups':L.channel_id.astype('category').cat.codes})
print('topic joint Wald p (cluster robust):',mt.wald_test(' , '.join([f'C(topic_id)[T.{t}] = 0' for t in sorted(L.topic_id.unique())[1:]]),scalar=True).pvalue,'R2',round(mt.rsquared,3))
# trend by pub quarter (descriptive; age-confounded)
Q=v[(v.fmt=='long')&v.pub.notna()].copy(); Q['q']=Q.pub.dt.to_period('Q').astype(str)
Q.groupby('q').agg(n=('video_id','size'),channels=('channel_id','nunique'),median_views=('views','median'),median_PI=('PI','median')).to_csv('out/pub_quarter_trend.csv')
F=v[v.pub.notna()].copy(); F['q']=F.pub.dt.to_period('Q').astype(str)
F.groupby(['q','fmt']).agg(n=('video_id','size'),median_views=('views','median'),median_PI=('PI','median')).to_csv('out/pub_quarter_by_format.csv')
# --- predictive: unseen-channel generalisation (GroupKFold by channel)
d=L[L.perf_class.isin(['Breakout','Successful','Underperforming'])].copy(); d['y']=d.perf_class.isin(['Breakout','Successful']).astype(int)
featsets={'title_surface':[c for c in d.columns if c.startswith('t_') and d[c].dtype!=object],
 'hook_intro':[c for c in d.columns if c.startswith(('h_','i_'))],'script':[c for c in d.columns if c.startswith('s_') or c in('x_words','duration_seconds')]}
featsets['all_text']=sum(featsets.values(),[])
res=[]
topic_dm=pd.get_dummies(d.topic_id,prefix='tp').astype(float)
for name,cols in list(featsets.items())+[('topic_only',[]),('all_text+topic',featsets['all_text'])]:
    M=d[cols].astype(float).fillna(d[cols].astype(float).median()) if cols else pd.DataFrame(index=d.index)
    if 'topic' in name: M=pd.concat([M,topic_dm],axis=1)
    M=M.values; y=d.y.values; g=d.channel_id.values; aucs=[]; 
    for tr,te in GroupKFold(5).split(M,y,g):
        mod=HistGradientBoostingClassifier(max_depth=3,learning_rate=.05,max_iter=150,random_state=0).fit(M[tr],y[tr])
        if len(set(y[te]))>1: aucs.append(roc_auc_score(y[te],mod.predict_proba(M[te])[:,1]))
    # permutation baseline
    yp=np.random.default_rng(1).permutation(y); pa=[]
    for tr,te in GroupKFold(5).split(M,yp,g):
        mod=HistGradientBoostingClassifier(max_depth=3,learning_rate=.05,max_iter=150,random_state=0).fit(M[tr],yp[tr])
        if len(set(yp[te]))>1: pa.append(roc_auc_score(yp[te],mod.predict_proba(M[te])[:,1]))
    res.append(dict(feature_set=name,n=len(d),n_pos=int(y.sum()),AUC_unseen_channels=np.mean(aucs),AUC_sd=np.std(aucs),AUC_shuffled_label=np.mean(pa)))
R=pd.DataFrame(res); R.to_csv('out/predictive_unseen_channel.csv',index=False); print(R.round(3).to_string())
v.to_pickle('out/videos_feat.pkl'); L.to_pickle('out/long_classified.pkl')
