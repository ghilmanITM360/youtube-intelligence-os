import numpy as np,pandas as pd,re
from scipy import stats
v=pd.read_pickle('out/videos_feat2.pkl'); ch=pd.read_pickle('out/channels.pkl')
def grp(s):
    s=s.lower() if isinstance(s,str) else ''
    if re.search(r'pov|wealth (revenge|fantasy|psychology)|salary|frugality|stealth|family drama|workplace|lifestyle|business-owner life|wealth/business',s): return 'wealth-POV / story-drama'
    if re.search(r'senior|social security|medicare|benefit|pension|irs|retire|rmd|cpp|hmrc|dwp|super',s): return 'retirement & senior-benefits'
    if re.search(r'macro|economic|explain|eli5|company|history|business|corporate|logistics|retail|medieval|shipping|tech-industry|finance concepts|economics',s): return 'business/economics explainers'
    if re.search(r'invest|dividend|etf|personal finance|saving|compound|consumer|money psych|investing|wealth',s): return 'investing & personal finance'
    return 'other/unclassified'
FB={'Economics Explained':'business/economics explainers','How Money Works':'business/economics explainers','Modern MBA':'business/economics explainers','Money & Macro':'business/economics explainers','Patrick Boyle':'business/economics explainers','PensionCraft':'investing & personal finance','Chronofold':'business/economics explainers','Primitive Education':'business/economics explainers'}
ch['group']=ch.sub_niche.map(grp)
m=ch.sub_niche.isna(); ch.loc[m,'group']=ch.loc[m,'name'].map(FB).fillna('other/unclassified')  # null sub_niche -> fallback by channel name (analyst judgement, flagged)
# unknown sub_niche channels: use video titles manually later
v['group']=v.channel_id.map(ch.set_index('channel_id').group)
L=v[(v.fmt=='long')&v.views.notna()]
cm=L.groupby(['channel_id','name','group']).agg(n=('video_id','size'),median_views=('views','median'),p90_views=('views',lambda s:s.quantile(.9)),median_dur=('duration_seconds','median'),subs=('subscribers','first'),
   breakout_rate=('perf_class',lambda s:(s=='Breakout').mean()*100),dup_script=('dup_script_flag','mean')).reset_index()
cm.to_csv('out/channel_performance_report_69.csv',index=False)
g=cm[cm.n>=10].groupby('group').agg(channels=('channel_id','size'),median_of_channel_median_views=('median_views','median'),min_cm=('median_views','min'),max_cm=('median_views','max'),videos=('n','sum'))
print(g.round(0).to_string()); g.to_csv('out/subniche_group_summary.csv')
print(stats.kruskal(*[x.median_views.values for _,x in cm[cm.n>=10].groupby('group')]))
print(cm.sort_values('median_views',ascending=False).head(12)[['name','group','n','median_views','subs']].to_string())
print(cm.sort_values('median_views').head(8)[['name','group','n','median_views','subs']].to_string())
v.to_pickle('out/videos_feat2.pkl')
