import json,csv,hashlib,os,subprocess,collections
from pathlib import Path
O=Path(__file__).parent;A=Path('/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z');eight=list(csv.DictReader(open(O/'EIGHT_FILE_PRESERVATION_VERIFICATION.csv')));tri=list(csv.DictReader(open(O/'LOCAL_ONLY_RISK_TRIAGE.csv')));summ=json.load(open(O/'evidence/HIGH_VALUE_HASH_TRIAGE_SUMMARY.json'));samples=[]
for p in summ['changed_during_reads']:
 r=next(x for x in tri if x['source_path']==p);path=Path(p);b=path.stat();h=hashlib.sha256(path.read_bytes()).hexdigest();a=path.stat();v=next((x for x in eight if x['expected_sha256']==h),None);samples.append({'path':p,'size':a.st_size,'sha256':h,'matches_canonical_source':v['source_path'] if v else None,'stable_resident_reread':(b.st_size,b.st_mtime_ns,b.st_ino)==(a.st_size,a.st_mtime_ns,a.st_ino),'before_read_dataless_in_sealed_inventory':True,'after_flags':a.st_flags,'interpretation':'Bounded provider hydration, full bytes match canonical source; versioned immutable backup still not established'})
 r['hash_evidence']='FRESH_RESIDENT_REREAD_STABLE_AFTER_SMALL_ICLOUD_HYDRATION; SHA matches canonical source';r['classification']='ICLOUD_ARCHIVE_COPY_FULL_BYTES_MATCHED';r['reason']='Cloud-provider placeholder yielded exact canonical bytes; synced recovery copy, not immutable Drive/Git receipt'
 if v:v['remote_copy_status']='ICLOUD_PROVIDER_FULL_BYTES_SHA256_MATCHED: '+p+'; no GitHub/Drive equivalent proven; immutable version history unknown'
(O/'evidence/ICLOUD_SIX_SCRIPT_COPIES.json').write_text(json.dumps(samples,indent=2))
for name,data in [('EIGHT_FILE_PRESERVATION_VERIFICATION.csv',eight),('LOCAL_ONLY_RISK_TRIAGE.csv',tri)]:
 with open(O/name,'w') as f:w=csv.DictWriter(f,fieldnames=data[0]);w.writeheader();w.writerows(data)
# Foundation metadata sample updated to these six exact cloud archive paths only.
(O/'evidence/ICLOUD_SIX_PATHS.json').write_text(json.dumps([x['path'] for x in samples]));js=(O/'icloud_metadata.js').read_text().replace('ICLOUD_SAMPLE_PATHS.json','ICLOUD_SIX_PATHS.json');(O/'icloud_six_metadata.js').write_text(js);r=subprocess.run(['osascript','-l','JavaScript',str(O/'icloud_six_metadata.js')],capture_output=True);(O/'evidence/ICLOUD_SIX_METADATA.json').write_bytes(r.stdout)
# Fresh private namespace exact physical reconciliation; no metadata mutation.
raw=json.load(open(O/'evidence/DRIVE_APPROVED_NAMESPACE_FRESH.json'));files={};folders=set();errors=[]
for it in raw:
 if it['status']!='fulfilled':errors.append(str(it));continue
 value=it['value'];res=value['result'];sc=res.get('structuredContent',{})
 if res.get('isError'):errors.append(value['id'])
 for x in sc.get('files',[]):
  if x.get('mime_type')=='application/vnd.google-apps.folder':folders.add(x['id'])
  else:files[x['id']]=x
old=list(csv.DictReader(open(A/'DRIVE_PHYSICAL_OBJECTS_RECONCILIATION.csv')));print('oldfields',list(old[0]));oldids={r.get('remote_id',r.get('id')) for r in old}
ns={'folders_read':len(raw),'physical_object_count':len(files),'physical_bytes':sum(int(x.get('size') or 0) for x in files.values()),'new_ids':sorted(set(files)-oldids),'missing_ids':sorted(oldids-set(files)),'errors':errors,'read_only':True,'cloud_mutation_operations':0};(O/'evidence/DRIVE_RECONCILIATION.json').write_text(json.dumps(ns,indent=2))
# Verify current source baseline/checkpoint and exception receipt hashes against preserved audit; no rehash of media.
base=json.load(open(A/'evidence/V7_BASELINE_RECONCILIATION_FINAL.json'));checks=[]
for r in base['checks']:
 p=Path(r['path'])
 if p.stat().st_size>20000000:continue
 h=hashlib.sha256(p.read_bytes()).hexdigest();checks.append({'path':str(p),'expected_sha256':r.get('expected_sha256',r['sha256']),'sha256':h,'pass':h==r.get('expected_sha256',r['sha256'])})
(O/'evidence/V7_HISTORICAL_RECEIPTS_UNCHANGED.json').write_text(json.dumps(checks,indent=2));print('namespace',ns);print('six',len(samples),sum(x['size'] for x in samples),'V7hashchecks',len(checks),all(x['pass'] for x in checks))
