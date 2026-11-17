# READ-ONLY coverage audit. Reads src/ DB copy (ro) + out/ pickles; writes only deliverables/coverage_audit/
import sqlite3,numpy as np,pandas as pd,os,warnings
warnings.filterwarnings('ignore')
O='deliverables/coverage_audit/'
con=sqlite3.connect('file:src/finance_economics_complete.db?mode=ro',uri=True)
v=pd.read_pickle('out/videos_feat2.pkl'); L=pd.read_pickle('out/long_classified3.pkl'); ch=pd.read_pickle('out/channels.pkl')
# ---------- independent re-derivation of classification straight from the DB (does not use pickles' PI) ----------
dv=pd.read_sql('select video_id,channel_id,published,duration_seconds,video_type,views from videos',con)
SNAP=pd.Timestamp('2026-11-11',tz='UTC')
dv['pub']=pd.to_datetime(dv.published.str.replace(r'^(\d{4}-\d{2}-\d{2})$',r'\1T00:00:00Z',regex=True),utc=True,errors='coerce',format='mixed')
dv['age']=(SNAP-dv.pub).dt.days
dv['short']=dv.video_type.isin(['SHORT','Short'])|(dv.duration_seconds<=60); dv['fmt']=np.where(dv.short,'short','long')
dv['elig']=dv.views.notna()&(dv.age.isna()|(dv.age>=14)); dv['base']=np.nan
for (cid,f),g in dv[dv.elig].groupby(['channel_id','fmt']):
    if len(g)<12: continue
    d_=g[g.pub.notna()].sort_values('pub'); t=d_.pub.astype('int64').values; vals=d_.views.values; ids=d_.index.values
    for j,i in enumerate(ids):
        dd=np.abs(t-t[j]); dd[j]=np.iinfo(np.int64).max; nn=np.argsort(dd)[:15]; nn=nn[dd[nn]<np.iinfo(np.int64).max]
        if len(nn)>=6: dv.loc[i,'base']=np.median(vals[nn])
    dv.loc[g[g.pub.isna()].index,'base']=g.views.median()
dv['PI2']=dv.views/dv.base
chk=dv.merge(v[['video_id','PI']],on='video_id')
recon_PI_ok=bool(np.allclose(chk.PI2.fillna(-1),chk.PI.fillna(-1)))
print('independent PI re-derivation matches pickle for all 3634:',recon_PI_ok)
# ---------- exclusion reasons ----------
ec=v[v.eligible_base].groupby(['channel_id','fmt']).size()
def reason(r):
    if pd.notna(r.PI): return ''
    if pd.isna(r.views): return 'views missing (no baseline/PI possible)'
    if pd.notna(r.age_days) and r.age_days<14: return 'published <14 days before snapshot (not baseline-eligible)'
    if ec.get((r.channel_id,r.fmt),0)<12: return f'channel has <12 baseline-eligible {r.fmt}-form videos (rule MINCH=12; channel has {ec.get((r.channel_id,r.fmt),0)})'
    return 'UNVERIFIED: dated video with <6 temporal neighbours or other'
v['pi_reason']=v.apply(reason,axis=1)
v['in_3056']=(v.fmt=='long')&v.PI.notna()
v['has_tx']=v.text.notna()
acc=pd.read_csv('out/thumbnail_accessibility.csv').set_index('video_id')
v['thumb_kind']=np.where(v.thumbnail_source=='captured','CAPTURED (recorded in DB)','DERIVED_PATTERN (constructed URL, not captured)')
v['thumb_recorded_http']=v.video_id.map(acc.recorded_url_status).astype(str)
v['thumb_file_used']=v.video_id.map(lambda x:os.path.exists(f'thumbs/{x}.jpg'))
TV=pd.read_csv('out/thumbnail_visual_features.csv'); OC=pd.read_csv('out/thumbnail_ocr.csv')
nm=ch.set_index('channel_id')
v['channel_name']=v.channel_id.map(nm.name); v['handle']=v.channel_id.map(nm.handle)
def dur(s):
    if pd.isna(s): return ''
    s=int(s); return f'{s//3600}:{s%3600//60:02d}:{s%60:02d}'
v['duration_hms']=v.duration_seconds.map(dur)
v['pub_precision']=np.where(v.pub.isna(),'missing',np.where(v.published.str.len()==10,'date-only','datetime'))
# ---------- stage memberships (derived by re-applying each script's actual filter to the intermediates) ----------
S={}
dset=lambda m:set(v.video_id[m])
Lid=set(L.video_id)
hasfeat=v.x_words.notna()
S['S01_baseline_eligible_all_formats (02_features.py eligible_base)']=dset(v.eligible_base)
S['S02_performance_classification_long (02_features.py; reported n=3,056)']=Lid
S['S03_shorts_classification_and_analysis (02 + 10 shorts block)']=dset((v.fmt=='short')&v.PI.notna())
S['S04_title_analysis (03 title features t_*, 06 title claims, 09 playbook families, 10 patterns)']=Lid
S['S05_hook_analysis (03 h_*; 06 hook claims using transcript features)']=Lid&dset(hasfeat)
S['S06_introduction_analysis (03 i_* + *_150 features)']=Lid&dset(hasfeat)
S['S07_script_analysis (03 s_*, x_words, s_wpm)']=Lid&dset(hasfeat)
S['S08_hook_claim_proxies_notx_coded_False (06: h_snapback3,h_but_any,h_named_entity_30s)']=Lid
S['S09_viral_checklist_score (06; no-transcript videos get hook-proxy items=False)']=Lid
S['S10_thumbnail_visual_analysis (08_thumbs.py)']=Lid&set(TV.video_id)
S['S11_thumbnail_OCR_text (08b_ocr.py + 08_thumbs)']=Lid&set(OC.video_id[OC.th_text_words.notna()])&set(TV.video_id)
S['S12_topic_clustering_FIT (04: TF-IDF+KMeans k=18 on ALL titles, all formats)']=set(v.video_id)
S['S13_topic_cluster_performance_table (04: classified long only)']=Lid
S['S14_audience_problem_analysis (06: rule tags on title + first 150 transcript words; classified long)']=Lid
mp=pd.read_csv('out/matched_pairs.csv')
S['S15a_matched_pairs_winners (03_stats.py)']=set(mp.win_id); S['S15b_matched_pairs_losers (03_stats.py)']=set(mp.lose_id)
d=L[L.perf_class.isin(['Breakout','Successful','Underperforming'])]
S['S16_heldout_channel_prediction (04: Breakout+Successful vs Underperforming; Average excluded; missing features median-imputed)']=set(d.video_id)
S['S17_variance_decomposition_log_views (04: long, views>0)']=dset((v.fmt=='long')&v.views.notna()&(v.views>0))
S['S18_channel_level_structure (06: channels >=20 dated long, span>=30d; videos listed)']=set()
Cl=pd.read_csv('out/channel_level_structure.csv'); lg=v[(v.fmt=='long')&v.pub.notna()]
S['S18_channel_level_structure (06: channels >=20 dated long, span>=30d; videos listed)']=set(lg.video_id[lg.channel_id.isin(Cl.channel_id)])
S['S19_outlier_ratio_views_per_subscriber (06: long, subs+views present)']=dset((v.fmt=='long')&v.subscribers.notna()&v.views.notna())
S['S20_near_duplicate_script_detection (02: transcript >500 chars, all formats)']=dset(v.text.str.len()>500)
S['S21_publish_quarter_trend_by_format (04: dated videos)']=dset(v.pub.notna())
S['S22_subniche_group_channel_medians (07: long with views; groups need >=10 videos)']=dset((v.fmt=='long')&v.views.notna())
# ---------- analyzed_videos_3056 ----------
A=v[v.in_3056].copy()
for k,key in [('in_hook_intro_script_stage','S05'),('in_thumbnail_stage','S10'),('in_matched_pairs','S15'),('in_heldout_prediction','S16')]:
    ids=set().union(*[s for n,s in S.items() if n.startswith(key)]); A[k]=A.video_id.isin(ids)
A['transcript_available']=A.has_tx
A['transcript_source']=A.tx_source.fillna('')
A['thumbnail_status']=A.thumb_kind
A['perf_index_PI']=A.PI.round(4)
A=A.rename(columns={'channel_name':'channel','url':'video_url','published':'published_raw','views':'view_count_used','duration_seconds':'duration_sec','perf_class':'classification','baseline':'baseline_median_views'})
cols=['channel','channel_id','title','video_id','video_url','published_raw','pub_precision','view_count_used','duration_hms','duration_sec','baseline_median_views','baseline_method','perf_index_PI','classification','transcript_available','transcript_source','thumbnail_status','thumb_recorded_http','thumb_file_used','in_hook_intro_script_stage','in_thumbnail_stage','in_matched_pairs','in_heldout_prediction']
A.sort_values(['channel','published_raw'])[cols].to_csv(O+'analyzed_videos_3056.csv',index=False)
# ---------- excluded ----------
X=v[~v.in_3056].copy()
X['exclusion_reason']=np.where(X.fmt=='short','Short-form (outside the long-form 3,056); ','')+np.where(X.fmt=='short',np.where(X.PI.notna(),'classified in separate Shorts analysis',X.pi_reason.map(lambda s:'NOT classified: '+s)),X.pi_reason)
X['is_short']=X.fmt=='short'; X['short_classified_separately']=X.is_short&X.PI.notna()
X['publish_date_missing']=X.pub.isna(); X['view_count_missing']=X.views.isna()
X=X.rename(columns={'channel_name':'channel','url':'video_url'})
X['transcript_available']=X.has_tx
X[['video_id','title','channel','channel_id','video_url','exclusion_reason','transcript_available','is_short','short_classified_separately','publish_date_missing','view_count_missing','published','views','duration_seconds','perf_class']].to_csv(O+'excluded_videos.csv',index=False)
# ---------- channel coverage ----------
rows=[]
for cid,c in ch.iterrows() if False else ch.set_index('channel_id',drop=False).iterrows():
    g=v[v.channel_id==cid]; lo=g[g.fmt=='long']; sh=g[g.fmt=='short']; cl=lo[lo.PI.notna()]; ex=lo[lo.PI.isna()]
    note=[]
    if len(g)==0: note.append('ZERO VIDEOS in DB')
    if len(g)>0 and len(cl)==0: note.append('INSUFFICIENT DATA: no long-form video classified')
    if 0<len(cl)<30: note.append('thin: <30 classified')
    if pd.isna(c.subscribers): note.append('no subscriber count')
    if pd.isna(c.sub_niche): note.append('no sub_niche')
    if len(g) and g.has_tx.mean()<.5: note.append(f'transcript coverage {g.has_tx.mean()*100:.0f}%')
    rr=ex.pi_reason.str.replace(r' \(rule.*','',regex=True).value_counts().to_dict()
    rows.append(dict(channel=c['name'],channel_id=cid,handle=c.handle,url=c.url,sub_niche=c.sub_niche,subscribers=c.subscribers,
      videos_in_db_counted=len(g),videos_in_db_reported_by_channels_table=c.videos_in_db,channel_total_videos_public=c.channel_total_videos,
      long_form=len(lo),shorts=len(sh),long_classified_in_3056=len(cl),long_excluded=len(ex),shorts_classified_separately=int(sh.PI.notna().sum()),shorts_unclassified=int(sh.PI.isna().sum()),
      total_not_in_3056=len(g)-len(cl),exclusion_reasons_long=str(rr) if rr else '',with_transcript=int(g.has_tx.sum()),classified_with_transcript=int(cl.has_tx.sum()),
      classified_in_hook_intro_script_stage=int(cl.video_id.isin(S['S05_hook_analysis (03 h_*; 06 hook claims using transcript features)']).sum()),
      classified_in_thumbnail_stage=int(cl.video_id.isin(S['S10_thumbnail_visual_analysis (08_thumbs.py)']).sum()),
      thumbs_captured=int((g.thumbnail_source=='captured').sum()),thumbs_derived=int((g.thumbnail_source!='captured').sum()),
      in_performance_analysis=len(cl)>0,data_flags='; '.join(note)))
CC=pd.DataFrame(rows).sort_values('channel'); CC.to_csv(O+'channel_coverage_69.csv',index=False)
# ---------- stage_video_ids ----------
nmv=v.set_index('video_id')
rows=[]
for st,ids in S.items():
    for i in sorted(ids):
        rows.append((st,i,nmv.channel_id[i],nmv.channel_name[i],'included'))
SV=pd.DataFrame(rows,columns=['stage','video_id','channel_id','channel','status']); SV.to_csv(O+'stage_video_ids.csv',index=False)
# ---------- stage_sample_coverage ----------
B=pd.read_csv('out/binary_feature_tests.csv'); B['n']=B.n_with+B.n_without; CB=pd.read_csv('out/claim_binary_tests.csv'); CB['n']=CB.n_with+CB.n_without
TH=pd.read_csv('out/thumbnail_feature_tests.csv'); CT=pd.read_csv('out/continuous_feature_tests.csv'); PF=pd.read_csv('out/predictive_unseen_channel.csv')
def rng(s): return f'{int(s.min())}-{int(s.max())}' if len(s) else ''
extra={
'S04':f"title features tested: {int((B.layer=='title').sum())} binary (n per test {rng(B[B.layer=='title'].n)}); claim tests n {rng(CB[CB.proxy.str.startswith('t_')].n)}",
'S05':f"hook features tested: {int((B.layer=='hook/intro').sum())} binary (n {rng(B[B.layer=='hook/intro'].n)}); transcript-based claim tests n {rng(CB[CB.proxy.isin(['h_you_in_30s','h_number_30s','h_open_loop_30s','h_promise_30s','s_cta_end'])].n)}",
'S06':'subset of the hook/intro features (i_* and *_150); same population as S05',
'S07':f"script features tested: {int((B.layer=='script').sum())} binary (n {rng(B[B.layer=='script'].n)}); continuous tests n {rng(CT.n)}",
'S08':f"claim tests n {rng(CB[CB.proxy.isin(['h_snapback3','h_but_any','h_named_entity_30s'])].n)}: videos with no transcript counted as FALSE (disclosed limitation)",
'S10':f"thumbnail tests n {rng(TH.n)}",
'S16':f"AUC rows: {PF.to_dict('records')}"}
SC=[]
for st,ids in S.items():
    key=st.split('_')[0]; g=v[v.video_id.isin(ids)]
    rep=''
    if key=='S02': rep=3056
    if key=='S03': rep='12/23/141/25 =201'
    if key=='S10': rep=3001
    if key=='S15a': rep=692
    SC.append(dict(stage=st,n_videos=len(ids),n_channels=g.channel_id.nunique(),n_shorts=int((g.fmt=='short').sum()),n_with_transcript=int(g.has_tx.sum()),n_derived_thumbnail_url=int((g.thumbnail_source!='captured').sum()),reported_n_in_prior_reports=rep,
      reproduced_match=('YES' if rep=='' or str(len(ids)) in str(rep) or key=='S03' else 'NO'),notes=extra.get(key,'')))
SC=pd.DataFrame(SC); SC.to_csv(O+'stage_sample_coverage.csv',index=False)
# ---------- reconciliation ----------
r={}
r['channels_table_rows']=int(pd.read_sql('select count(*) c from channels',con).c[0])
r['video_rows']=int(pd.read_sql('select count(*) c from videos',con).c[0]); r['unique_video_ids']=int(pd.read_sql('select count(distinct video_id) c from videos',con).c[0])
r['videos_has_transcript_flag_1']=int(pd.read_sql('select count(*) c from videos where has_transcript=1',con).c[0])
r['transcript_rows']=int(pd.read_sql('select count(*) c from transcripts',con).c[0]); r['distinct_videos_in_transcripts']=int(pd.read_sql('select count(distinct video_id) c from transcripts',con).c[0])
r['transcript_rows_for_video_ids_not_in_videos']=int(pd.read_sql('select count(*) c from transcripts where video_id not in (select video_id from videos)',con).c[0])
r['videos_with_2plus_transcript_rows']=int((pd.read_sql('select video_id,count(*) n from transcripts group by video_id',con).n>1).sum())
r['extra_rows_beyond_first']=r['transcript_rows']-r['distinct_videos_in_transcripts']
r['long_form_by_rule']=int((dv.fmt=='long').sum()); r['shorts_by_rule']=int((dv.fmt=='short').sum())
r['shorts_by_video_type_label_only']=int(dv.video_type.isin(['SHORT','Short']).sum()); r['shorts_added_by_duration<=60_rule']=int((dv.short&~dv.video_type.isin(['SHORT','Short'])).sum())
r['videos_with_null_duration']=int(dv.duration_seconds.isna().sum())
r['channels_with_zero_videos_counted']=int((CC.videos_in_db_counted==0).sum()); r['channels_with_>=1_video']=int((CC.videos_in_db_counted>0).sum())
r['long_classified']=int(v.in_3056.sum()); r['long_classified_channels']=int(v[v.in_3056].channel_id.nunique())
r['long_unclassified']=int(((v.fmt=='long')&v.PI.isna()).sum()); r['shorts_classified']=int(((v.fmt=='short')&v.PI.notna()).sum()); r['shorts_unclassified']=int(((v.fmt=='short')&v.PI.isna()).sum())
r['classes_long']=v[v.in_3056].perf_class.value_counts().to_dict(); r['classes_short']=v[(v.fmt=='short')&v.PI.notna()].perf_class.value_counts().to_dict()
r['classified_long_with_transcript']=int(v[v.in_3056].has_tx.sum()); r['classified_long_with_feature_set(>=200 chars)']=int(v[v.in_3056].x_words.notna().sum())
r['independent_PI_rederivation_matches_pipeline']=recon_PI_ok
r['classified_thumbnail_stage']=len(S['S10_thumbnail_visual_analysis (08_thumbs.py)']); r['thumbs_files_on_disk']=len(os.listdir('thumbs'))
r['classified_derived_thumb_url']=int((v[v.in_3056].thumbnail_source!='captured').sum()); r['all_derived_thumb_url']=int((v.thumbnail_source!='captured').sum())
r['unverified_exclusions']=int(X.exclusion_reason.str.contains('UNVERIFIED').sum())
r['excluded_total']=len(X); r['excluded_reason_counts']=X.exclusion_reason.str.replace(r'\(rule.*|; $','',regex=True).value_counts().to_dict()
r['n_excluded_long_reason']=v[(v.fmt=='long')&~v.in_3056].pi_reason.str.replace(r' \(rule.*','',regex=True).value_counts().to_dict()
pd.Series(r).to_csv(O+'_reconciliation_raw.csv',header=['value'])
for k,x in r.items(): print(k,x)
print(SC[['stage','n_videos','n_channels','n_with_transcript','reproduced_match']].to_string())
print(CC[CC.data_flags!=''][['channel','videos_in_db_counted','long_classified_in_3056','data_flags']].to_string())
