import sqlite3,re,numpy as np,pandas as pd
c=sqlite3.connect('src/finance_economics_complete.db')
v=pd.read_sql('select * from videos',c); ch=pd.read_sql('select * from channels',c)
tx=pd.read_sql('select video_id,source,caption_type,status,text,word_count from transcripts',c)
SNAP=pd.Timestamp('2026-11-11',tz='UTC')
v['pub']=pd.to_datetime(v.published.str.replace(r'^(\d{4}-\d{2}-\d{2})$',r'\1T00:00:00Z',regex=True),utc=True,errors='coerce',format='mixed')
v['age_days']=(SNAP-v.pub).dt.days
v['is_short']=v.video_type.isin(['SHORT','Short'])|(v.duration_seconds<=60)
v['fmt']=np.where(v.is_short,'short','long')
# one transcript per video: prefer creator > youtube auto > registry auto > whisper
pri={'youtube_creator_caption':0,'youtube_auto_caption':1}
tx['p']=tx.source.map(pri).fillna(tx.source.str.startswith('registry').map({True:2,False:3}))
tx=tx.sort_values(['video_id','p','word_count'],ascending=[True,True,False])
t1=tx.drop_duplicates('video_id')[['video_id','source','caption_type','status','text','word_count']].rename(columns={'source':'tx_source','status':'tx_status','word_count':'tx_words'})
v=v.merge(t1,on='video_id',how='left')
v=v.merge(ch[['channel_id','name','sub_niche','subscribers']],on='channel_id',how='left')
# inventory
inv={'channels_table':len(ch),'video_rows':len(v),'unique_video_ids':v.video_id.nunique(),'unique_urls':v.url.nunique(),
'distinct_titles':v.title.str.lower().str.strip().nunique(),'transcript_rows':len(tx),'videos_with_transcript':tx.video_id.nunique(),
'videos_with_2plus_transcript_rows':int((tx.groupby('video_id').size()>1).sum()),'thumb_urls_distinct':v.thumbnail_url.nunique(),
'thumb_captured':int((v.thumbnail_source=='captured').sum()),'thumb_derived_pattern':int((v.thumbnail_source!='captured').sum()),
'missing_published':int(v.pub.isna().sum()),'missing_views':int(v.views.isna().sum()),'channels_without_videos':int((ch.videos_in_db.fillna(0)==0).sum()),
'channels_with_null_subs':int(ch.subscribers.isna().sum()),'shorts':int(v.is_short.sum()),'long':int((~v.is_short).sum()),
'partial_transcripts':int((v.tx_status=='PARTIAL').sum()),'asr_uncertified_tx':int((v.tx_status=='ASR_UNCERTIFIED').sum()),
'pub_date_only(len10)':int((v.published.str.len()==10).sum())}
print(inv)
# duplicate title groups within channel
d=v.assign(t=v.title.str.lower().str.strip()).groupby(['channel_id','t']).video_id.apply(list); d=d[d.map(len)>1]
d.reset_index().to_csv('out/dup_title_groups.csv',index=False)
pd.Series(inv).to_csv('out/inventory_verified.csv',header=['value'])
v.to_pickle('out/videos.pkl'); ch.to_pickle('out/channels.pkl')
