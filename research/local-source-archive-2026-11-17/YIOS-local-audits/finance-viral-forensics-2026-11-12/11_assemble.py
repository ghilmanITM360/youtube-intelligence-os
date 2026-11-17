import pandas as pd,numpy as np,re,hashlib,json,os
pd.set_option('display.width',250,'display.max_colwidth',100)
v=pd.read_pickle('out/videos_feat2.pkl'); L=pd.read_pickle('out/long_classified3.pkl')
D='deliverables/'
L['topic_terms']=L.video_id.map(v.set_index('video_id').topic_terms)
if 'group' not in L: L['group']=L.video_id.map(v.set_index('video_id').group)
# ---- 3/4 unique video DB + classification
cols=['video_id','channel_id','name','group','url','title','published','fmt','duration_seconds','views','likes','comments','age_days','baseline','baseline_method','PI','perf_class','topic_id','topic_terms','tx_source','tx_status','tx_words','dup_script_flag','thumbnail_url','thumbnail_source']
v[cols].to_csv(D+'03_unique_video_performance_database.csv',index=False)
v[['video_id','channel_id','fmt','views','baseline','baseline_method','PI','perf_class']].to_csv(D+'04_video_success_classification.csv',index=False)
# classification summary
cs=v.groupby(['fmt','perf_class']).size().unstack(fill_value=0); cs.to_csv(D+'04_classification_counts.csv'); print(cs)
# ---- 12/13 forensics
first=lambda s,n=60:' '.join(str(s).split()[:n]) if isinstance(s,str) else ''
b=L[L.perf_class=='Breakout'].sort_values('PI',ascending=False)
f=b.head(60)[['video_id','name','group','title','views','baseline','PI','duration_seconds','topic_terms','checklist_score','h_you_in_30s','h_number_30s','h_but_30s','audience_target_age','gap_most_miss','th_has_face','th_text_words','text']].copy()
f['opening_60_words']=f.text.map(first); f.drop(columns='text').assign(opening_60_words=f.opening_60_words).to_csv(D+'12_successful_video_forensics_top60.csv',index=False)
u=L[L.perf_class=='Underperforming'].copy(); u['baseline_rank']=u.baseline
uu=u.sort_values('baseline',ascending=False).groupby('channel_id').head(3).sort_values('baseline',ascending=False).head(60)
uu=uu[['video_id','name','group','title','views','baseline','PI','duration_seconds','topic_terms','checklist_score','h_you_in_30s','h_number_30s','h_but_30s','audience_target_age','gap_most_miss','th_has_face','th_text_words','text']].copy(); uu['opening_60_words']=uu.text.map(first); uu.drop(columns='text').to_csv(D+'13_underperforming_video_forensics_60.csv',index=False)
# ---- 14 matched pairs
P=pd.read_csv('out/matched_pairs.csv'); P[['channel_id','channel','win_id','win_title','win_views','win_PI','lose_id','lose_title','lose_views','lose_PI','days_apart','dur_ratio']].to_csv(D+'14_matched_pairs.csv',index=False)
pd.read_csv('out/matched_pair_tests.csv').to_csv(D+'14_matched_pair_feature_tests.csv',index=False)
# template counterexamples: same title template, wildly different outcomes
tpl=L[L.title.str.contains(r"^If You(?:'re| Are) Over (60|65), .* (Will Give You|Owes You|Gives You)",case=False,regex=True)][['video_id','name','title','views','baseline','PI']].sort_values('PI',ascending=False); tpl.to_csv(D+'14_counterexample_same_title_template.csv',index=False)
print('template cases',len(tpl),tpl.PI.describe()[['min','50%','max']].to_dict())
# ---- 15 cross-channel: consistency table merged
B=pd.read_csv('out/binary_feature_tests.csv'); B['cross_channel_share_positive']=B.ch_pos/B.ch_tot
B.to_csv(D+'15_cross_channel_feature_replication.csv',index=False)
# per-channel breakout concentration
cc=L.groupby(['channel_id','name','group']).agg(n_classified=('PI','size'),breakouts=('perf_class',lambda s:(s=='Breakout').sum()),successful=('perf_class',lambda s:(s=='Successful').sum()),under=('perf_class',lambda s:(s=='Underperforming').sum()),median_PI=('PI','median')).reset_index(); cc.to_csv(D+'15_channel_class_counts.csv',index=False)
# ---- 11 transcript coverage
cov=v.groupby(['channel_id','name']).agg(videos=('video_id','size'),with_tx=('text',lambda s:s.notna().sum()),with_date=('pub',lambda s:s.notna().sum()),with_views=('views',lambda s:s.notna().sum())).reset_index(); cov['tx_coverage_pct']=cov.with_tx/cov.videos*100; cov.to_csv(D+'01_channel_coverage.csv',index=False)
print('channels w/ <50% tx coverage:',(cov.tx_coverage_pct<50).sum(), cov[cov.tx_coverage_pct<50][['name','videos','with_tx']].to_string())
# ---- opportunity inputs
L['senior_formula']=L.audience_target_age&L.gap_most_miss
for nm,m in [('senior_formula (audience age + gap framing)',L.senior_formula),('free_perks_money_owed',L.free_perks_money_owed),('audience_target_age',L.audience_target_age),('deadline_date',L.deadline_date)]:
    g=L[m]; print(nm,len(g),g.channel_id.nunique(),'PI q25/50/75',g.PI.quantile([.25,.5,.75]).round(2).tolist(),'breakout',round((g.perf_class=='Breakout').mean()*100,1),'under',round((g.perf_class=='Underperforming').mean()*100,1))
base=L; print('baseline all PI q25/50/75',base.PI.quantile([.25,.5,.75]).round(2).tolist())
L.to_pickle('out/long_classified3.pkl')
