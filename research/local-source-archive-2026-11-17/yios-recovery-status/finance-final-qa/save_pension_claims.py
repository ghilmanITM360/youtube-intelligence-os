from pathlib import Path
import csv,json,collections,urllib.request,gzip,hashlib
r=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/extracted/forensic-analysis/casually-finance/2026-10-12');q=r/'07_VALIDATION';fed='https://www.federalreserve.gov/monetarypolicy/fomcminutes20260617.htm';abp='https://www.abp.nl/over-abp/het-vernieuwde-pensioenstelsel/veelgestelde-vragen/ik-bouw-pensioen-op';updates={
'C11':('VERIFIED_FED_ATTRIBUTION_CAUSAL_SCOPE_UNVERIFIED','June16–17,2026 FOMC minutes record manager describing Treasury ownership shift from relatively price-insensitive official holders to more price-sensitive private investors, with possible implications for term premiums. Attribution verified, not universal elasticity, pension-specific cause or magnitude. Exact video narration unlistened. '+fed),
'C18':('PARTIALLY_VERIFIED_ABP_PLAN_AGGREGATE_UNVERIFIED','ABP official participant FAQ states planned January1,2027 transition. Planned future date verified as institutional attribution, not realized conversion, guaranteed outcome or nearly€1T aggregate2027 conversion value. Current page retrievedOctober12,2026; historical video-date version not assumed. '+abp)}
for p in [r/'02_VIDEO_FORENSICS/0ll9rEtoRrs/FINANCE_CLAIMS.csv',r/'03_MASTER_DATA/MASTER_FINANCE_CLAIMS.csv']:
 rows=list(csv.DictReader(p.open()))
 for x in rows:
  if x.get('video_id','0ll9rEtoRrs')=='0ll9rEtoRrs' and x['claim_id'] in updates:
   st,note=updates[x['claim_id']];x['verification_status']=st;x['notes']+=' PENSION_PRIMARY_QA_2026-10-12: '+note
 with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
p=q/'FINANCE_CLAIM_VERIFICATION.csv';rows=list(csv.DictReader(p.open()))
for x in rows:
 if x['video_id']=='0ll9rEtoRrs' and x['claim_id'] in updates:
  st,note=updates[x['claim_id']];x.update(external_verification_result='VERIFIED' if x['claim_id']=='C11' else 'PARTIALLY_VERIFIED',existing_evidence_status=st,verification_scope='Institutional statement/plan attribution only; audio and broader causal/value claims unresolved',primary_source_url=fed if x['claim_id']=='C11' else abp,evidence_notes=x['evidence_notes']+' PENSION_PRIMARY_QA_2026-10-12: '+note)
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
p=q/'FINALIZATION_CLAIM_CENSUS.json';o=json.loads(p.read_text());o['result_counts']=dict(collections.Counter(x['external_verification_result'] for x in rows));p.write_text(json.dumps(o,indent=2)+'\n');archives=[]
for name,url in [('FED_FOMC_20260617.html.gz',fed),('ABP_TRANSITION_FAQ_20261012.html.gz',abp)]:
 try:
  raw=urllib.request.urlopen(url,timeout=20).read();b=gzip.compress(raw,mtime=0);(q/'primary_sources'/name).write_bytes(b);assert gzip.decompress(b)==raw;archives.append({'url':url,'path':'primary_sources/'+name,'source_sha256':hashlib.sha256(raw).hexdigest(),'archive_sha256':hashlib.sha256(b).hexdigest(),'source_bytes':len(raw),'archive_bytes':len(b),'encoding':'gzip; exact original source bytes preserved'})
 except Exception as e:archives.append({'url':url,'archive_status':'FAILED','error':str(e),'web_read':'Succeeded'})
(q/'PENSION_PRIMARY_SOURCE_QA.json').write_text(json.dumps({'video_id':'0ll9rEtoRrs','claims':['C11','C18'],'retrieval_date':'2026-10-12','audio_listened':False,'sources':archives},indent=2)+'\n');(q/'PENSION_PRIMARY_SOURCE_QA.md').write_text(f'''# Pension and Treasury-owner source verification

0ll9rEtoRrs C11: [June2026 FOMC minutes]({fed}) verify the manager’s attribution of a shift toward more price-sensitive private Treasury owners and possible term-premium implications. This does not independently quantify elasticity, prove pensions caused yield changes or establish inevitable higher rates. Exact soundtrack wording remains unlistened.

C18: [ABP official FAQ]({abp}) corroborates the planned January1,2027 transition. Future implementation and the nearly€1T aggregate claim remain unverified. The current page is a dated retrieval, not silently a historical video-date snapshot.

Result: C11 institutional attribution VERIFIED; C18 composite PARTIALLY_VERIFIED. Documentary sources, lossless archive outcomes and checksums are inPENSION_PRIMARY_SOURCE_QA.json. No original media or other channel changed.
''');print(o['result_counts']);print([(x['url'],x.get('archive_status','ARCHIVED')) for x in archives])
