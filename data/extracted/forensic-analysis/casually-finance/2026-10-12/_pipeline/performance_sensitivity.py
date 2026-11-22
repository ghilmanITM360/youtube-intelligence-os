import csv,json,statistics as st
from pathlib import Path
rows=list(csv.DictReader(open('01_CHANNEL_METADATA/all-videos-metadata.csv')))
for r in rows:
 for k in ['views','views_per_day','age_days_at_collection','duration_sec']:r[k]=float(r[k] or 0)
out=['# Publication-age sensitivity — saved snapshot only','', 'MEASURED_ASSOCIATION: Lifetime views/day is views divided by age, not an observed daily trajectory. Bands are descriptive, chosen as7–30,30–90,90–365and365+days. No significance or causality claim. Source01_CHANNEL_METADATA/all-videos-metadata.csv; snapshot20261011T182811Z.','','| Format | Age band | n | Median views | Median lifetime views/day | Top velocity ID | Bottom velocity ID |','|---|---|---:|---:|---:|---|---|'];data=[]
for fmt in ['LONG_FORM','SHORT']:
 for lo,hi,label in [(7,30,'7–30d'),(30,90,'30–90d'),(90,365,'90–365d'),(365,1e9,'365+d')]:
  g=[r for r in rows if r['format_class']==fmt and lo<=r['age_days_at_collection']<hi]
  if not g:continue
  top=max(g,key=lambda r:r['views_per_day']);bot=min(g,key=lambda r:r['views_per_day']);v=st.median(r['views'] for r in g);vp=st.median(r['views_per_day'] for r in g);out.append(f'| {fmt} | {label} | {len(g)} | {v:,.0f} | {vp:,.0f} | {top["video_id"]} | {bot["video_id"]} |');data.append({'format':fmt,'age_band':label,'n':len(g),'median_views':v,'median_vpd':vp,'top':top['video_id'],'bottom':bot['video_id']})
out+=['','The smallest/youngest bands can be dominated by one topic or changing channel size. Within-band extrema still differ in age, exposure and production era. Cumulative snapshots cannot reveal launch curves or current recommendation momentum. Videos younger than7days appear in selected-video context but not the aged association tables.','','Counterexamples: MicroStrategy dlBhLhn8lL0 is a selected long-form with a readable Bitcoin Trojan-horse image yet low lifetime velocity. Two missing Shorts are among the strongest public performers; this prohibits an audiovisual explanation of their outlier status. SpaceX JsK53moCyZA short and -X6YzlY_8tM long-form share a hook/mechanism, so repeated observations are not independent script experiments.']
Path('06_REPORTS/PERFORMANCE_AGE_SENSITIVITY.md').write_text('\n'.join(out)+'\n');Path('03_MASTER_DATA/PERFORMANCE_AGE_SENSITIVITY.json').write_text(json.dumps(data,indent=1));print('\n'.join(out[4:]))
