import pathlib,json,collections,hashlib,time
O=pathlib.Path(__file__).parent;R=pathlib.Path('/Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21');p=R/'ALL_RESEARCH_FINDINGS.jsonl'
assert not p.stat().st_flags&0x40000000
stats=collections.Counter();schemas=collections.Counter();sources={};samples={};h=hashlib.sha256();errors=[];video=set();channel=set()
with p.open('rb') as f:
 for i,line in enumerate(f,1):
  h.update(line)
  try:x=json.loads(line)
  except Exception as e:errors.append({'line':i,'error':str(e)});continue
  kind=x.get('record_kind','');stats[kind]+=1;v=x.get('value');schema=','.join(sorted(v)) if isinstance(v,dict) else type(v).__name__;schemas[(kind,schema)]+=1
  sid=x.get('source_id','');s=sources.setdefault(sid,{k:x.get(k) for k in ['source_id','source_path','source_sha256','source_refs','source_snapshot_date','publication_status']});s['records']=s.get('records',0)+1;s.setdefault('kinds',{})[kind]=s.setdefault('kinds',{}).get(kind,0)+1
  if kind not in samples:samples[kind]={'line':i,'source_path':x.get('source_path'),'source_object':x.get('source_object'),'value_preview':str(v)[:5000]}
  if isinstance(v,dict):
   for k,z in v.items():
    if k in ('youtube_video_id','video_id','external_video_id') and isinstance(z,str):video.add(z)
    if k in ('channel_id','youtube_channel_id') and isinstance(z,str):channel.add(z)
(O/'evidence/findings_census.json').write_text(json.dumps(dict(records=sum(stats.values()),record_kinds=dict(stats),schemas=[dict(kind=k,schema=s,count=n) for (k,s),n in schemas.items()],sources=len(sources),errors=errors,sha256=h.hexdigest(),video_identity_values=len(video),channel_identity_values=len(channel),semantic_reading='Full JSON syntax/schema census; only first record per kind semantically sampled'),indent=2))
(O/'evidence/embedded_source_index.json').write_text(json.dumps(list(sources.values()),indent=2));(O/'evidence/semantic_samples.json').write_text(json.dumps(samples,indent=2));(O/'evidence/export_identity_values.json').write_text(json.dumps(dict(video=sorted(video),channel=sorted(channel))))
print('DONE',sum(stats.values()),len(sources),dict(stats),len(errors),h.hexdigest())
