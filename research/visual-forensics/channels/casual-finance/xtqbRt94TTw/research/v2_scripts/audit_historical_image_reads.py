import pathlib,json,csv,hashlib,collections
from PIL import Image
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan'); L=pathlib.Path('/Users/ghilmankhan/.claude/projects/-Users-ghilmankhan-workprojects-youtube-intelligence-os');O=R/'session_20261103';reads=[]
# Only source-matching tool invocations. Tool-result image blocks, not assistant summaries, establish success.
for f in L.glob('*/subagents/*.jsonl'):
 if not ('ceaf5788' in str(f) or '92f2cdab' in str(f) or '6e5ed00f' in str(f) or 'c1b75aa6' in str(f) or 'fa028ab4' in str(f)):continue
 calls={}
 with f.open() as stream:
  for line in stream:
   try:d=json.loads(line)
   except Exception:continue
   content=d.get('message',{}).get('content',[])
   if not isinstance(content,list):continue
   for b in content:
    if b.get('type')=='tool_use' and b.get('name')=='Read':
     path=b.get('input',{}).get('file_path','')
     if path.startswith(str(R)+'/') and pathlib.Path(path).suffix.lower() in ('.jpg','.png','.jpeg'):calls[b['id']]=path
    if b.get('type')=='tool_result' and b.get('tool_use_id') in calls:
     path=calls[b['tool_use_id']];blocks=b.get('content',[]);success=not b.get('is_error') and isinstance(blocks,list) and any(x.get('type')=='image' for x in blocks);q=pathlib.Path(path)
     dims='';sha=''
     if q.exists():
      with Image.open(q) as im:dims=f'{im.width}x{im.height}'
      sha=hashlib.sha256(q.read_bytes()).hexdigest()
     relative=str(q.relative_to(R));kind='MIXED_SCALED_FULLFRAMES_AND_NATIVE_BBOX_CROPS' if relative.startswith('evidence/') else 'SCALED_960x540' if relative.startswith('frames/') else 'SCALED_480x270_TILES' if relative.startswith('disputes/') else 'CROP_DIMENSIONS_DO_NOT_PROVE_NATIVE_SEEK_ACCURACY'
     reads.append(dict(log=str(f),tool_use_id=b['tool_use_id'],path=relative,successful_image_result=success,dimensions=dims,sha256_current=sha,evidence_kind=kind))
# Find early logs not captured by known sessions by searching tool invocation lines (do not emit image contents).
seen={x['path'] for x in reads if x['successful_image_result']}
summary=[]
for i in range(1,11):
 out=json.loads((R/f'agents/shard_{i}/OUT_shard_{i}.json').read_text());d=R/f'agents/shard_{i}';s={}
 for kind in ('candidates','states','disputes'):
  rows=list(csv.DictReader((d/f'{kind}.csv').open()));key='evidence' if kind=='candidates' else 'rep_image' if kind=='states' else None
  expected=[r[key] if key else f'disputes/{r["id"]}.jpg' for r in rows]
  missing=[x for x in expected if x not in seen];s[kind]={'expected_rows':len(rows),'successful_exact_path_rows':len(rows)-len(missing),'missing_exact_paths':missing}
 s['shard']=i;summary.append(s)
with (O/'historical_image_read_receipts.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(reads[0]) if reads else ['path']);w.writeheader();w.writerows(reads)
(O/'historical_image_read_audit.json').write_text(json.dumps({'method':'Actual logged Read tool_use paired with tool_result image block; current artifact SHA/dimensions. Exact-path success does not prove model attention, native source viewing, or delivery without client scaling. Early session logs not found remain UNKNOWN.','successful_reads':sum(x['successful_image_result'] for x in reads),'all_result_rows':len(reads),'shards':summary,'raw_logs_local_only':True},indent=2))
print('results',len(reads),'successful',sum(x['successful_image_result'] for x in reads));
for s in summary:print(s['shard'],{k:(s[k]['successful_exact_path_rows'],s[k]['expected_rows']) for k in ('candidates','states','disputes')})
