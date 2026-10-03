import csv,json,sqlite3,hashlib
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
c=sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_inventory.db?mode=ro',uri=True);c.row_factory=sqlite3.Row
rows=[]
for p in sorted((ROOT/'data/manifests').glob('*thumbnail-snapshot*.json')):
 d=json.loads(p.read_text())
 for s in d.get('snapshots',[]):
  v=c.execute('select v.*,c.display_name from videos v join channels c using(channel_id) where video_id=?',(s['video_id'],)).fetchone()
  snapshots=[dict(x) for x in c.execute('select * from video_snapshots where video_id=? order by observed_at,video_snapshot_id',(s['video_id'],))]
  same=[x for x in snapshots if x['dataset_id']==s['dataset_id']];m=(same or snapshots)[-1] if snapshots else {}
  local=Path(s['local_path']);sha=hashlib.sha256(local.read_bytes()).hexdigest() if local.exists() else ''
  r={'Thumbnail_ID':'THB-'+s['sha256'],'channel_id':d['channel_id'],'channel':v['display_name'] if v else '', 'niche':'Science explanations' if d['channel_id']=='CH-000004' else 'Senior health','niche_label':'INFERENCE_channel_scope','video_id':s['video_id'],'youtube_video_id':v['youtube_video_id'] if v else '', 'title':s['title'],'format':s['format'],'published_at':m.get('published_at'),'views':m.get('views'),'metrics_observed_at':m.get('observed_at'),'metric_snapshot_id':m.get('video_snapshot_id'),'image_observed_at':s.get('retrieval_timestamp',d.get('retrieval_timestamp')),'local_path':str(local),'manifest':str(p.relative_to(ROOT)),'mapping_status':'HASH_VERIFIED' if sha==s['sha256'] else 'MISSING_OR_HASH_MISMATCH','temporal_alignment':'UNKNOWN','impressions':'','CTR':'','watch_time':'','retention':'','AVD':'','traffic_sources':'','experiment_result':'','inspection_status':'PENDING','score_100':''}
  try:r['video_age_days_at_metrics']=(datetime.fromisoformat(m['observed_at'].replace('Z','+00:00')).replace(tzinfo=None)-datetime.fromisoformat(m['published_at'].replace('Z','+00:00')).replace(tzinfo=None)).total_seconds()/86400
  except:r['video_age_days_at_metrics']=''
  rows.append(r)
with (OUT/'thumbnail-ledger.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
(OUT/'thumbnail-ledger.json').write_text(json.dumps(rows,indent=2))
selected=[]
for ch in sorted({r['channel_id'] for r in rows}):
 group=[r for r in rows if r['channel_id']==ch and r['format']=='LONG_FORM' and r['views'] is not None]
 group.sort(key=lambda r:r['views'])
 for label,r in [('LOWEST_CUMULATIVE_VIEWS',group[0]),('HIGHEST_CUMULATIVE_VIEWS',group[-1])]:
  selected.append({**r,'selection':label,'cohort_n':len(group)})
(OUT/'batch-001-selection.json').write_text(json.dumps(selected,indent=2))
print(json.dumps([{k:r[k] for k in ['channel','title','views','format','metrics_observed_at','video_age_days_at_metrics','selection','local_path']} for r in selected],indent=2))
assert len(rows)==144 and all(r['mapping_status']=='HASH_VERIFIED' for r in rows)
