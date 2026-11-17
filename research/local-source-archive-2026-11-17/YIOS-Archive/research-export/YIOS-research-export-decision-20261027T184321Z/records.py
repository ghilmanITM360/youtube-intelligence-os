import pathlib,json,collections,re,sqlite3,csv,hashlib
O=pathlib.Path(__file__).parent;E=O/'evidence';R=pathlib.Path('/Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21');repo=pathlib.Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
texts={};ids={};docs=[];dup=collections.Counter();refs=collections.Counter();table=collections.Counter();vkeys={'video_id','youtube_video_id','external_video_id','youtubeVideoId'};ckeys={'channel_id','youtube_channel_id','channelId'}
selected=['DEEP-KNOWLEDGE-AUDIT','FINANCE_ECONOMICS_MASTER_REPORT','casually-finance-script-intelligence/','casually-finance-editing-forensics/README','12-channel-metadata/RESUME_HERE','12-channel-metadata/SOURCE_RECONCILIATION_REPORT','WHAT_IF','SOURCE_CONTRACT','BRANCH_SOURCE_INDEX','REPOSITORY-SUPERSET-CONSOLIDATION-REPORT']
def observe(d,x,line):
 if not isinstance(d,dict):return
 for k,v in d.items():
  if not isinstance(v,str):continue
  typ='video' if (k in vkeys or k in ('id','actor_id') and re.fullmatch('[A-Za-z0-9_-]{11}',v)) else 'channel' if k in ckeys else None
  if typ and ((typ=='video' and re.fullmatch('[A-Za-z0-9_-]{11}',v)) or (typ=='channel' and re.fullmatch('UC[A-Za-z0-9_-]{22}',v))):
   z=ids.setdefault((typ,v),dict(type=typ,identity=v,first_line=line,source_path=x['source_path'],source_object=str(x.get('source_object','')),occurrences=0,example_title=str(d.get('video_title',d.get('title',d.get('channel_name',''))))[:200]));z['occurrences']+=1
with (R/'ALL_RESEARCH_FINDINGS.jsonl').open() as f:
 for line,l in enumerate(f,1):
  x=json.loads(l);v=x.get('value');kind=x.get('record_kind');p=x['source_path'];table[str(x.get('source_object','')).split(':')[0]]+=1
  observe(v,x,line)
  if isinstance(v,list):
   for d in v:observe(d,x,line)
  if kind in ('text_document','recovered_github_text','pdf_text') and isinstance(v,dict) and 'text' in v:
   text=v['text'];docs.append(dict(source_id=x['source_id'],path=p,line=line,characters=len(text),sha256_text=hashlib.sha256(text.encode()).hexdigest()))
   if any(s in p for s in selected) and len(texts)<65:texts[p+'#'+x['source_id']]={'line':line,'text':text[:60000],'truncated':len(text)>60000,'source_sha256':x['source_sha256']}
  if kind in ('table_row','sqlite_row','recovered_github_lfs_row','recovered_table_row','archive_row'):
   digest=hashlib.sha256((kind+'\0'+json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False)).encode()).hexdigest();dup[digest]+=1
c=sqlite3.connect('file:'+str(repo/'data/catalog/youtube_channel_registry.db')+'?mode=ro&immutable=1',uri=True)
print('video schema',c.execute('pragma table_info(videos)').fetchall()[:6]);print('channel schema',c.execute('pragma table_info(channels)').fetchall()[:5])
cv={r[0] for r in c.execute('select youtube_video_id from videos')};cc={r[0] for r in c.execute('select canonical_channel_id from channels')};c.close()
for (typ,key),z in ids.items():z['in_current_registry']='YES' if key in (cv if typ=='video' else cc) else 'NO';z['meaning']='Identity observed in export; absence from registry is not absence from repository or a completed audit'
rows=list(ids.values())
with (O/'EXPORT_IDENTITY_REGISTRY_COMPARISON.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(E/'selected_embedded_document_excerpts.json').write_text(json.dumps(texts,indent=2));(E/'embedded_document_index.json').write_text(json.dumps(docs));(E/'record_value_duplicates.json').write_text(json.dumps(dict(compared_records=sum(dup.values()),unique_values=len(dup),repeated_value_occurrences=sum(n-1 for n in dup.values()),method='Exact kind plus canonical JSON value; ignores provenance intentionally; duplicates must retain source lineage',identity_counts={t:dict(collections.Counter(z['in_current_registry'] for z in rows if z['type']==t)) for t in ['video','channel']},selected_documents=len(texts)),indent=2));print((E/'record_value_duplicates.json').read_text())
