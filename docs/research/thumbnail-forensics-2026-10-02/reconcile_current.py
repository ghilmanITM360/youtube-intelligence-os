"""Read-only source reconciliation; generated artifacts never imply visual inspection."""
import csv, hashlib, io, json, re, sqlite3, zipfile
from pathlib import Path
from collections import Counter, defaultdict
from PIL import Image
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
SKIP={'.git','.venv','node_modules','__pycache__','.pytest_cache','.ruff_cache','.codex'}
IMAGE_EXT={'.jpg','.jpeg','.png','.webp','.avif','.gif','.bmp','.tif','.tiff'}
URL=re.compile(r'https?://(?:i\d?\.ytimg\.com|img\.youtube\.com)/(?:vi|vi_webp)/([A-Za-z0-9_-]{11})/[^\s"\'<>\\)\]]+')
assets=[]; refs=[]; documents=[]; errors=[]
def save(name,rows):
 (OUT/(name+'.json')).write_text(json.dumps(rows,indent=2,ensure_ascii=False))
 if rows:
  keys=list(dict.fromkeys(k for r in rows for k in r))
  with (OUT/(name+'.csv')).open('w') as f:
   w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in rows)
def visit(data,location,depth=0):
 ext=Path(location).suffix.lower(); sha=hashlib.sha256(data).hexdigest()
 ds=re.search(r'DS-\d{6}',location)
 r=dict(Asset_ID='AS-'+sha,sha256=sha,relative_path=location,bytes=len(data),extension=ext,source_dataset=ds.group() if ds else '',source_type='CONTAINER_MEMBER' if '!/' in location else 'FILE',classification='NOT_IMAGE',inspection_status='NOT_INSPECTED',width='',height='')
 if ext in IMAGE_EXT:
  r['classification']='UNKNOWN_IMAGE'
  try:
   im=Image.open(io.BytesIO(data));im.load();r.update(width=im.width,height=im.height,decode_status='ACCESSIBLE')
  except Exception as e:r['decode_status']=str(e)
 assets.append(r)
 if ext in {'.json','.jsonl','.csv','.tsv','.md','.txt','.xml','.rels','.html'}:
  text=data.decode('utf-8',errors='replace').replace('\\/','/')
  for m in URL.finditer(text):refs.append(dict(youtube_video_id=m.group(1),thumbnail_url=m.group().replace('&amp;','&'),source_path=location,source_sha256=sha))
 if ext in {'.zip','.xlsx','.docx','.pptx'}:
  try:
   with zipfile.ZipFile(io.BytesIO(data)) as z:
    for info in z.infolist():
     if info.is_dir():continue
     if depth>=12 or info.file_size>200_000_000: errors.append(dict(path=location+'!/'+info.filename,error='RESOURCE_LIMIT'));continue
     visit(z.read(info),location+'!/'+info.filename,depth+1)
  except Exception as e:errors.append(dict(path=location,error=str(e)))
 if ext=='.pdf':
  try:
   pdf=PdfReader(io.BytesIO(data))
   for pi,page in enumerate(pdf.pages):
    images=list(page.images)
    documents.append(dict(source_path=location,source_sha256=sha,page=pi+1,embedded_raster_images=len(images),vector_review_status='PENDING',text_characters=len(page.extract_text() or '')))
    for ii,img in enumerate(images):
     target=OUT/'document-images'/sha/(f'p{pi+1:03d}-{ii:03d}-'+img.name)
     target.parent.mkdir(parents=True,exist_ok=True)
     if not target.exists():target.write_bytes(img.data)
     visit(img.data,location+f'!/page-{pi+1}/'+img.name,depth+1)
     assets[-1]['classification']='DOCUMENT_EMBEDDED_IMAGE';assets[-1]['derived_local_path']=str(target.relative_to(ROOT))
  except Exception as e:errors.append(dict(path=location,error=str(e)))
for p in sorted(ROOT.rglob('*')):
 if not p.is_file() or OUT in p.parents or any(x in SKIP for x in p.relative_to(ROOT).parts):continue
 try:visit(p.read_bytes(),str(p.relative_to(ROOT)))
 except Exception as e:errors.append(dict(path=str(p.relative_to(ROOT)),error=str(e)))
# Source-location occurrences are distinct; identical references are not independent evidence.
refs=list({(r['youtube_video_id'],r['thumbnail_url'],r['source_path']):r for r in refs}.values())
inv=sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_inventory.db?mode=ro',uri=True);inv.row_factory=sqlite3.Row
reg=sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_channel_registry.db?mode=ro',uri=True);reg.row_factory=sqlite3.Row
videos={}
for rr in reg.execute('select v.*, c.channel_name from videos v join channels c using(canonical_channel_id)'):
 r=dict(rr);r.pop('description',None);r.pop('raw_json',None)
 r.update(video_id='',channel_id='',metric_source='data/catalog/youtube_channel_registry.db:videos',metrics_observed_at='',format='UNKNOWN' if not r['video_type'] else ('SHORTS' if 'short' in r['video_type'].lower() else 'LONG_FORM'))
 videos[r['youtube_video_id']]=r
for rr in inv.execute('select v.*,c.display_name,c.youtube_channel_id from videos v join channels c using(channel_id)'):
 v=dict(rr);m=inv.execute('select * from video_snapshots where video_id=? order by observed_at desc,video_snapshot_id desc limit 1',(v['video_id'],)).fetchone();m=dict(m) if m else {}
 r=videos.setdefault(v['youtube_video_id'],{})
 r.update(youtube_video_id=v['youtube_video_id'],video_id=v['video_id'],channel_id=v['channel_id'],canonical_channel_id=v['youtube_channel_id'],channel_name=v['display_name'],title=m.get('title'),published_at=m.get('published_at'),views=m.get('views'),likes=m.get('likes'),comments=m.get('comments'),metrics_observed_at=m.get('observed_at'),metric_source='data/catalog/youtube_inventory.db:video_snapshots:'+str(m.get('video_snapshot_id')),dataset_id=m.get('dataset_id'),format='SHORTS' if 'short' in str(m.get('video_type')).lower() else ('LONG_FORM' if m.get('video_type') else r.get('format','UNKNOWN')))
for row in reg.execute("select youtube_video_id,thumbnail_url from videos where thumbnail_url is not null and thumbnail_url!=''"):
 refs.append(dict(row)|dict(source_path='data/catalog/youtube_channel_registry.db:videos',source_sha256=''))
for row in inv.execute('select v.youtube_video_id,t.thumbnail_url,t.thumbnail_evidence_id from thumbnail_evidence t join videos v using(video_id)'):
 d=dict(row);refs.append(dict(youtube_video_id=d['youtube_video_id'],thumbnail_url=d['thumbnail_url'],source_path='data/catalog/youtube_inventory.db:thumbnail_evidence:'+d['thumbnail_evidence_id'],source_sha256=''))
byvideo=defaultdict(list)
for r in refs:
 if URL.fullmatch(r['thumbnail_url']):byvideo[r['youtube_video_id']].append(r)
old=json.loads((OUT/'thumbnail-ledger.json').read_text());audit=json.loads((OUT/'individual-audit-batch-001.json').read_text());done={r['Thumbnail_ID']:r for r in audit}
universe=[];oldvideos=set()
for r in old:
 p=Path(r['local_path']);sha=hashlib.sha256(p.read_bytes()).hexdigest();assert r['Thumbnail_ID']=='THB-'+sha
 oldvideos.add(r['youtube_video_id']);im=Image.open(p)
 universe.append(dict(r,Asset_ID='AS-'+sha,sha256=sha,relative_path=str(p.relative_to(ROOT)),width=im.width,height=im.height,classification='REGISTERED_LOCAL_THUMBNAIL',source_type='MANIFEST_LOCAL_SNAPSHOT',source_dataset=re.search(r'DS-\d{6}',r['manifest']).group(),thumbnail_url=(byvideo[r['youtube_video_id']][0]['thumbnail_url'] if byvideo[r['youtube_video_id']] else ''),mapping_confidence='EXACT_MANIFEST_VIDEO_ID_HASH',inspection_status=done.get(r['Thumbnail_ID'],{}).get('inspection_status','PENDING'),capture_date=r['image_observed_at']))
for yid,v in videos.items():
 if yid in oldvideos:continue
 rr=byvideo[yid];urls=sorted({x['thumbnail_url'] for x in rr},key=lambda s:('maxresdefault' not in s,s))
 universe.append(dict(v,Thumbnail_ID='URL-'+yid if urls else 'NOIMAGE-'+yid,Asset_ID='',sha256='',relative_path='',width='',height='',classification='URL_ONLY_THUMBNAIL' if urls else 'NO_THUMBNAIL_REFERENCE',source_type='CANONICAL_VIDEO_METADATA',source_dataset=v.get('dataset_id',''),thumbnail_url=urls[0] if urls else '',all_thumbnail_urls=urls,mapping_confidence='EXACT_YOUTUBE_VIDEO_ID',inspection_status='PENDING_RETRIEVAL' if urls else 'NO_ACCESSIBLE_ASSET',capture_date='',temporal_alignment='UNKNOWN',url_sources=rr))
# References absent from both catalogs stay visible without fabricated canonical mapping.
for yid,rr in byvideo.items():
 if yid in videos or all(x['source_path'].startswith('tests/') for x in rr):continue
 universe.append(dict(Thumbnail_ID='URL-'+yid,youtube_video_id=yid,video_id='',channel_id='',classification='URL_ONLY_THUMBNAIL',thumbnail_url=rr[0]['thumbnail_url'],all_thumbnail_urls=sorted({x['thumbnail_url'] for x in rr}),url_sources=rr,mapping_confidence='AMBIGUOUS_MAPPING_NOT_IN_CATALOGS',inspection_status='PENDING_RETRIEVAL',sha256='',relative_path=''))
bysha={r['sha256']:r for r in universe if r.get('sha256')}
for r in assets:
 if r['sha256'] in bysha:
  t=bysha[r['sha256']];r.update(classification='REGISTERED_LOCAL_THUMBNAIL',Thumbnail_ID=t['Thumbnail_ID'],video_id=t.get('video_id',''),channel_id=t.get('channel_id',''),inspection_status=t['inspection_status'])
assert len(done)==6 and all(a['Thumbnail_ID'] == bysha[a['Thumbnail_ID'][4:]]['Thumbnail_ID'] for a in audit)
save('current-source-inventory',assets);save('thumbnail-url-provenance',refs);save('thumbnail-universe',universe);save('document-image-inventory',documents)
summary=dict(file_member_occurrences=len(assets),image_occurrences=sum(bool(r['width']) for r in assets),image_classifications=dict(Counter(r['classification'] for r in assets if r['width'])),universe_classifications=dict(Counter(r['classification'] for r in universe)),canonical_video_union=len(videos),url_reference_occurrences=len(refs),document_pages=len(documents),pdf_embedded_images=sum(r['embedded_raster_images'] for r in documents),errors=errors)
(OUT/'current-inventory-summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
