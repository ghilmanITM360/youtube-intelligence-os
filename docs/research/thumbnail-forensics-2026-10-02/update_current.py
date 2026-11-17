"""Merge preserved acquisitions/audits and calculate reproducible visual features."""
import csv,hashlib,json,sqlite3
from collections import Counter
from pathlib import Path
import numpy as np
from PIL import Image
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
def save(name,rows):
 (OUT/(name+'.json')).write_text(json.dumps(rows,indent=2,ensure_ascii=False))
 if rows:
  keys=list(dict.fromkeys(k for r in rows for k in r))
  with (OUT/(name+'.csv')).open('w') as f:
   w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in rows)
u=json.loads((OUT/'thumbnail-universe.json').read_text())
retrieval={r['youtube_video_id']:r for r in map(json.loads,(OUT/'public-retrieval.jsonl').read_text().splitlines())}
audits=[]
for p in sorted(OUT.glob('individual-audit-batch-*.json')):audits.extend(json.loads(p.read_text()))
assert len({r['Thumbnail_ID'] for r in audits})==len(audits)
byid={r['Thumbnail_ID']:r for r in audits}
inv=sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_inventory.db?mode=ro',uri=True)
channelmap=dict(inv.execute('select channel_id,youtube_channel_id from channels'))
for r in u:
 if r['classification']=='URL_ONLY_THUMBNAIL' and r['youtube_video_id'] in retrieval:
  fetched=retrieval[r['youtube_video_id']];s=fetched['snapshot']
  r['retrieval_status']=s['result'];r['retrieval_attempts']=fetched['attempts']
  if fetched['success']:
   r.update(reference_Thumbnail_ID=r['Thumbnail_ID'],Thumbnail_ID='THB-'+s['sha256'],Asset_ID='AS-'+s['sha256'],sha256=s['sha256'],relative_path=str(Path(s['local_path']).relative_to(ROOT)),local_path=s['local_path'],width=s['width'],height=s['height'],classification='REGISTERED_LOCAL_THUMBNAIL',source_type='CURRENT_PUBLIC_URL_CAPTURE',capture_date=s['retrieval_timestamp'],temporal_alignment='UNKNOWN_CURRENT_PUBLIC_IMAGE_NOT_PROVEN_AT_METRIC_DATE',inspection_status='PENDING',mapping_confidence='EXACT_CATALOG_VIDEO_ID_AND_PUBLIC_THUMBNAIL_URL')
  else:r['inspection_status']='RETRIEVAL_FAILED_URL_ONLY'
 if not r.get('canonical_channel_id'):r['canonical_channel_id']=channelmap.get(r.get('channel_id'),'')
 a=byid.get(r['Thumbnail_ID'])
 if a:r.update(inspection_status=a['inspection_status'],audit_id=a.get('audit_id',a.get('Audit_ID','')),score_100=a.get('score_100'))
# Every original mapping is retained even if two files later share a creative.
save('thumbnail-universe',u)
save('individual-audits-current',audits)
features=[]
k=np.arange(8)[:,None];x=np.arange(32)[None,:];dct=np.cos(np.pi*(2*x+1)*k/64)
for r in u:
 if not r.get('sha256'):continue
 p=ROOT/r['relative_path'];digest=hashlib.sha256(p.read_bytes()).hexdigest();assert digest==r['sha256']
 im=Image.open(p).convert('RGB');a=np.asarray(im,dtype=float)/255
 # Encoded-sRGB luma proxy; not physical light or audience perception.
 lum=a@np.array([.2126,.7152,.0722])
 edge=(np.abs(np.diff(lum,axis=0)).mean()+np.abs(np.diff(lum,axis=1)).mean())/2
 gray=np.asarray(im.convert('L').resize((32,32),Image.Resampling.LANCZOS),dtype=float)
 coeff=(dct@gray@dct.T).flatten();bits=coeff[1:]>np.median(coeff[1:]);ph=sum(int(b)<<i for i,b in enumerate(bits))
 small=im.resize((128,128)).quantize(colors=5);pal=small.getpalette();colors=sorted(small.getcolors(),reverse=True)
 features.append(dict(Thumbnail_ID=r['Thumbnail_ID'],sha256=digest,width=im.width,height=im.height,aspect_ratio=im.width/im.height,mean_encoded_srgb_luma=float(lum.mean()),rms_luma_contrast=float(lum.std()),mean_adjacent_luma_difference=float(edge),dominant_palette=[dict(rgb=pal[3*c:3*c+3],proportion=n/(128*128)) for n,c in colors],phash63=f'{ph:016x}',phash_method='32px_gray_LANCZOS_8x8_unscaled_DCT_exclude_DC_median_63bits',text_area_proportion=None,largest_face_relative_area=None,hero_object_relative_area=None,unmeasured_reason='No reliable detector/segmentation; blank is not zero'))
save('objective-visual-features',features)
# ponytail: pairwise scan is sufficient for this 2,275-image snapshot; index only if it grows materially.
candidates=[]
for i,a in enumerate(features):
 for b in features[i+1:]:
  dist=(int(a['phash63'],16)^int(b['phash63'],16)).bit_count()
  if dist<=9:candidates.append(dict(Thumbnail_ID_A=a['Thumbnail_ID'],Thumbnail_ID_B=b['Thumbnail_ID'],hamming_distance=dist,Similarity_Type='PERCEPTUAL_CANDIDATE_NOT_CONFIRMED',Similarity_Confidence='UNREVIEWED',Visual_Family_ID='',Canonical_Thumbnail_ID='',review_status='PENDING_VISUAL_COMPARISON'))
save('visual-family-candidates',candidates)
summary=dict(canonical_video_mappings=len(u),classification_counts=dict(Counter(r['classification'] for r in u)),unique_local_hashes=len({r.get('sha256') for r in u if r.get('sha256')}),preserved_b001=6,new_multiscale_audits=len(audits)-6,all_audit_records=len(audits),pending_local=sum(bool(r.get('sha256')) and r['Thumbnail_ID'] not in byid for r in u),url_only=sum(r['classification']=='URL_ONLY_THUMBNAIL' for r in u),public_downloads=sum(r['success'] for r in retrieval.values()),public_failures=sum(not r['success'] for r in retrieval.values()),perceptual_candidates=len(candidates),channels_with_local_images=len({r['canonical_channel_id'] for r in u if r.get('sha256')}),Dr_Rehan_local=sum(r.get('channel_id')=='CH-000009' and bool(r.get('sha256')) for r in u),note='Source support/screenshot/document triage pending. No automatic near-duplicate merge. B001 lacks separate 320px supplemental validation.')
(OUT/'current-progress.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
