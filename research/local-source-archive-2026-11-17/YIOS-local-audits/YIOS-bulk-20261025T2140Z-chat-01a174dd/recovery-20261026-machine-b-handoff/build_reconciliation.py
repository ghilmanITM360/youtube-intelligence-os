import json,hashlib,datetime,collections,re,subprocess,os
from pathlib import Path
o=Path(__file__).parent;r=o.parent;pilot=r.parent/'YIOS-pilot-20261025T2120Z-chat-01a174dd'
def read(p):return json.loads(p.read_text())
def save(n,x):
 p=o/n
 with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False)
 p.chmod(0o600)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks=[]
for p in [pilot/'RECEIPT_SHA256SUMS']+[r/f'batch-{i:04d}/SHA256SUMS' for i in range(1,9)]:
 for line in p.read_text().splitlines():
  h,n=line.split(None,1);q=p.parent/n.strip();checks.append({'file':str(q),'expected':h,'actual':sha(q),'match':h==sha(q)})
assert all(a['match'] for a in checks)
save('FROZEN_CHECKPOINT_INTEGRITY.json',checks)
objects=[]
for x in read(pilot/'receipt.json')['files']:
 assert x['restore_status']=='VERIFIED' and x['restored_bytes']==x['bytes'] and x['restored_sha256']==x['refreshed_sha256']
 objects.append({'source':x['source'],'restore_relative':x['restore_relative'],'bytes':x['bytes'],'sha256':x['refreshed_sha256'],'remote_id':x['remote_id'],'remote_url':x['remote_url'],'batch':'pilot','status':'VERIFIED','independently_retrieved_bytes':x['restored_bytes'],'verification_receipt':str(pilot/'receipt.json'),'role':x.get('role')})
batch9=[]
for i in range(1,10):
 b=r/f'batch-{i:04d}';mf=read(b/'MANIFEST.json')['files']
 for x in mf:
  seq=x['sequence'];u=read(b/f'upload-{seq:05d}.json');attempts=sorted(o.glob(f'object-{seq:05d}-attempt-*.json')) if i==9 else []
  candidates=attempts+([b/f'verify-{seq:05d}.json'] if (b/f'verify-{seq:05d}.json').exists() else [])
  verified=[]
  for p in candidates:
   v=read(p)
   if v.get('retrieved_bytes')==x['bytes'] and v.get('retrieved_sha256')==x['fresh_sha256'] and v.get('remote_id')==u['remote_id']:verified.append((p,v))
  p,v=verified[0] if verified else (None,{})
  z={'source':x['source_absolute'],'restore_relative':x['restore_relative'],'bytes':x['bytes'],'sha256':x['fresh_sha256'],'remote_id':u['remote_id'],'remote_url':u.get('remote_url',f"https://drive.google.com/file/d/{u['remote_id']}/view"),'batch':f'batch-{i:04d}','sequence':seq,'status':'VERIFIED' if verified else 'UPLOADED_UNVERIFIED','independently_retrieved_bytes':v.get('retrieved_bytes',0) if verified else 0,'verification_receipt':str(p) if p else None,'priority':x.get('backup_priority'),'role':x.get('evidence_role','original media')}
  objects.append(z)
  if i==9:batch9.append(dict(z,attempt_receipts=[str(p) for p in attempts],old_failure_attribution='Grouped original log cannot assign mismatch/timeout to an exact failed object; prior partial reads do not prove remote corruption.'))
assert len({x['remote_id'] for x in objects})==len(objects),'DUPLICATE_REMOTE_ID'
media=read(o/'MACHINE_B_REQUIRED_MEDIA.json')['files'];known={x['sha256']:x['video_id'] for x in media if x['role']=='ORIGINAL_MP4'}
for x in objects:
 p=x['source'];x['video_id']=known.get(x['sha256'])
 if '/CasuallyFinance/' in p or '/yio-cf-editing-forensics-local-evidence/' in p or '5umJ63d3rzQ-deep-ct-scan' in p:x['channel']='Casual Finance'
 elif '/productions/senior-health-casually-finance-3/' in p:x['channel']='Owner production: senior health (folder provenance; public channel unconfirmed)'
 else:x['channel']='UNASSIGNED (no channel claim)'
 if p.endswith('/gray.npy'):x['video_id']=Path(p).parent.name
 x['type']=('original_video' if Path(p).suffix.lower() in ['.mp4','.mov'] else 'production_audio' if '/source_audio/' in p else 'forensic_array' if p.endswith('.npy') else 'editing_json' if '/CapCut/' in p else 'evidence_checksum_manifest')
groups=collections.defaultdict(lambda:{'files':0,'uploaded_bytes':0,'verified_files':0,'verified_bytes':0})
for x in objects:
 g=groups[x['channel']+' | '+x['type']];g['files']+=1;g['uploaded_bytes']+=x['bytes'];g['verified_files']+=x['status']=='VERIFIED';g['verified_bytes']+=x['independently_retrieved_bytes']
tot={'source_files_uploaded':len(objects),'source_bytes_uploaded':sum(x['bytes'] for x in objects),'source_files_verified':sum(x['status']=='VERIFIED' for x in objects),'source_bytes_independently_verified':sum(x['independently_retrieved_bytes'] for x in objects),'source_original_media_files_verified':sum(x['status']=='VERIFIED' and x['type'] in ['original_video','production_audio'] for x in objects),'remaining_payload_before_handoff_bytes':12000000000-sum(x['bytes'] for x in objects),'batch9_status':'VERIFIED' if all(x['status']=='VERIFIED' for x in batch9) else 'PARTIAL_UPLOADED_UNVERIFIED','no_duplicate_remote_ids_in_receipts':True,'duplicate_scope':'All184 recorded object IDs unique; no exhaustive remote namespace listing claim; no re-uploads performed.'}
save('BATCH9_RECONCILIATION.json',{'observed_utc':now,'status':tot['batch9_status'],'files':batch9,'uploaded_bytes':sum(x['bytes'] for x in batch9),'verified_bytes':sum(x['independently_retrieved_bytes'] for x in batch9)})
save('SOURCE_TO_DRIVE_INVENTORY.json',{'observed_utc':now,'totals':tot,'channel_type_totals':dict(groups),'files':objects})
save('VERIFIED_RECOVERY_MAPPING.json',{'files':[x for x in objects if x['status']=='VERIFIED']})
plan=read(r/'ORDERED_PLAN_V2.json')['files'];done={x['source'] for x in objects};remaining=[x for x in plan if x['source_absolute'] not in done]
save('REMAINING_SELECTED_SCOPE.json',{'basis':'Existing ordered plan only; no repeated inventory. Other unscheduled source roots remain outside this list.','files':remaining,'files_count':len(remaining),'bytes':sum(x['bytes'] for x in remaining)})
for m in media:m['cloud_objects']=[{'remote_id':x['remote_id'],'status':x['status']} for x in objects if x['source']==m['path'] and x['sha256']==m['sha256']]
save('MACHINE_B_MEDIA_CLOUD_COVERAGE.json',media)
save('SUMMARY.json',{'observed_utc':now,'totals':tot,'channel_type_totals':dict(groups),'remaining_selected_plan_files':len(remaining),'remaining_selected_plan_bytes':sum(x['bytes'] for x in remaining)})
print(json.dumps(read(o/'SUMMARY.json'),indent=2))
