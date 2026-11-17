from pathlib import Path
import csv,json,urllib.request,hashlib
r=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/extracted/forensic-analysis/casually-finance/2026-10-12');u='https://www.cbo.gov/publication/61882';c='https://www.crfb.org/blogs/cbo-projects-possible-debt-spiral-r-exceeds-g'
a={
'C02':('PARTIALLY_VERIFIED_DEBT_DYNAMICS_SERIES_COMPARABILITY_UNVERIFIED','Original CRFB analysis supports conditional r<g debt/GDP mechanism absent additional non-interest borrowing; it does not certify creator 6.6/3.5 contemporaneous periods/denominators. Screen arithmetic 3.1 percentage points remains verified. '+c),
'C03':('PARTIALLY_VERIFIED_CBO_PROJECTION_OTHER_MEASURES_UNVERIFIED','CBO February11 baseline projects federal debt held by public from101% of GDP in2026 to120% in2036; projection conditional on documented policy/economic assumptions, not gross national debt and not guaranteed outcome. Creator current growth-rate gap and exact narration unverified. '+u),
'C04':('VERIFIED_CRFB_FORECAST_ATTRIBUTION_AUDIO_UNVERIFIED','Original CRFB March9 analysis dates projected r>g to fiscal2031, with both approximately3.8% nominal/1.8% real at crossover. This verifies attributed conditional forecast, not actual2031 outcome or exact spoken words. '+c),
'C05':('PARTIALLY_VERIFIED_CONDITIONAL_DEBT_DYNAMICS','CRFB distinguishes existing-stock erosion relativeGDP from primary/non-interest borrowing; r<g can accommodate modest stable primary deficits, not unlimited borrowing. Exact narration and creator numeric periods remain unverified. '+c)}
for p in [r/'02_VIDEO_FORENSICS/6S3PzAUFnXQ/FINANCE_CLAIMS.csv',r/'03_MASTER_DATA/MASTER_FINANCE_CLAIMS.csv']:
 rows=list(csv.DictReader(p.open()))
 for x in rows:
  if x.get('video_id','6S3PzAUFnXQ')=='6S3PzAUFnXQ' and x['claim_id'] in a:
   status,note=a[x['claim_id']];x['verification_status']=status;x['notes']+=' FINALIZATION_DEBT_PRIMARY_QA_2026-10-12: '+note+' Original audio unlistened.'
 with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(r/'07_VALIDATION/DEBT_PRIMARY_SOURCE_QA.md').write_text('''# Debt Short primary-source verification

6S3PzAUFnXQ: source-hash-verified narrow frames identify CRFB’s nominal-interest/growth chart and CBO public-debt projection. No independent audio listening occurred.

[CBO February 11 outlook](https://www.cbo.gov/publication/61882) projects debt **held by the public** from 101% of GDP in 2026 to 120% in 2036 under its baseline assumptions. This is distinct from gross federal debt and a forecast rather than a guaranteed outcome. C03 is partly verified; its current growth/interest gap is a different measurement.

[Original CRFB March 9 chart analysis](https://www.crfb.org/blogs/cbo-projects-possible-debt-spiral-r-exceeds-g) attributes the projected crossover to **fiscal 2031**, approximately 3.8% nominal or 1.8% real for both rates. C04’s forecast attribution is verified, not future realization or spoken wording. Its conditional debt-dynamics discussion supports C02/C05 in part: primary borrowing still matters when growth exceeds interest.

Analytic interpretation: with comparable annual nominal rates, no other stock-flow adjustment, debt ratio follows d(t) = ((1+r)/(1+g))*d(t-1) + p(t), where p is primary deficit divided by current GDP. This explains why r<g alone does not establish declining debt/GDP with arbitrary primary deficits. It is an equation under assumptions, not a new observation of the video.

The displayed 6.6%-3.5%=3.1 percentage-point arithmetic remains correct. The creator’s exact source IDs, revisions, annual versus quarterly growth windows, interest-rate denominator and matching periods remain DATA_SERIES_COMPARABILITY_UNVERIFIED. Neither the CRFB projection chart nor one BEA quarterly release closes that gap. Exact spoken approximately6.5% remains pending deferred listening. No false contradiction is inferred from different BEA vintages.

Sources read independently via web tools. Direct archive attempts and their outcomes are recorded separately; no failed retrieval is claimed as an archive.
''')
items=[]
for name,url in [('CBO_OUTLOOK_2026.html',u),('CRFB_R_G_20260309.html',c)]:
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=20) as f:b=f.read()
  (r/'07_VALIDATION/primary_sources'/name).write_bytes(b);items.append({'url':url,'path':'primary_sources/'+name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
 except Exception as e:items.append({'url':url,'archive_status':'FAILED','error':str(e),'independent_read':'web tool succeeded'})
(r/'07_VALIDATION/DEBT_PRIMARY_SOURCE_QA.json').write_text(json.dumps({'scope':'Conditional projections and debt-dynamics explanation; creator numeric-series comparability/audio unresolved','source_results':items,'reviewed_claims':['C02','C03','C04','C05']},indent=2)+'\n');print(items)
