import json,csv,collections,statistics,datetime,hashlib
from pathlib import Path
O=Path('/private/tmp/yios-nick-channel-20261023');R=Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os');P=R/'research/finance-economics-intelligence';n=json.loads((O/'data.json').read_text());s=json.loads((O/'summary.json').read_text());ss=list(csv.DictReader(open(O/'package/PEER_COHORT_SENSITIVITY.csv')));sens={r['video_id']:r for r in ss};a=[json.loads(l) for l in open(P/'VIDEO_AUDIT_966.jsonl')]
def stats(rows):
 vs=[float(r['identity']['Views']) for r in rows if r['identity']['Views']];rs=[float(r['identity']['Lifetime_rate_ratio']) for r in rows if r['identity']['Lifetime_rate_ratio']];tiers=collections.Counter(r['identity']['Performance_tier'] for r in rows)
 return {'n':len(rows),'median_views':statistics.median(vs) if vs else None,'median_ratio':statistics.median(rs) if rs else None,'eligible':len(rs),'strong':tiers['STRONG'],'weak':tiers['WEAK']}
strata=[]
for group in s['patterns']:
 for period,lo,hi in [('7-29',7,30),('30-89',30,90),('90-179',90,180),('180+',180,99999)]:
  rows=[r for r in n if group in r['_patterns'] and r['identity']['Age_days'] and lo<=float(r['identity']['Age_days'])<hi];strata.append(dict(group=group,age_band=period,**stats(rows),ids='|'.join(r['Video_ID'] for r in rows)))
with open(O/'package/TITLE_PATTERN_AGE_STRATA.csv','w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(strata[0]));w.writeheader();w.writerows(strata)
for group,d in s['patterns'].items():
 ids=d['all_ids'];d['five_peer_median_ratio']=statistics.median(float(sens[v]['five_peers_ratio']) for v in ids if sens[v]['five_peers_ratio']);d['five_peer_strong']=sum(sens[v]['five_peers_tier']=='STRONG' for v in ids)
# Age/format/duration compatible cross-channel descriptive comparison, no pooling of peer denominators.
s['matched_competitors']={}
for name in ['Nick Invests','Lucas Grant','Carl Invests']:
 rows=[r for r in a if r['identity']['Channel']==name and r['identity']['Views'] and r['identity']['Format']=='LONG_FORM' and r['identity']['Metric_snapshot_date']=='2026-09-11' and r['identity']['Age_days'] and 30<=float(r['identity']['Age_days'])<180 and 1200<=float(r['identity']['Duration_seconds'])<1500];s['matched_competitors'][name]=dict(**stats(rows),ids=[r['Video_ID'] for r in rows])
vs=sorted(float(r['identity']['Views']) for r in n);s['quantiles']={str(q):vs[round((len(vs)-1)*q)] for q in [.25,.5,.75,.9,.95,.99]};s['malformed_date_ids']=[r['Video_ID'] for r in n if not r['identity']['Age_days']];s['sample_audit_statuses']={r['Video_ID']:r['statuses'] for r in n if r['Video_ID'] in json.loads((O/'sample.json').read_text())};s['sample_image_tiers']=dict(collections.Counter(next(r for r in n if r['Video_ID']==v)['identity']['Performance_tier'] for v in json.loads((O/'image_sample.json').read_text())))
# Existing audit completeness is structural, not a new entailment certification.
s['complete_script_tiers']=dict(collections.Counter(r['identity']['Performance_tier'] for r in n if r['statuses']['SCRIPT_REVIEW']=='COMPLETE_LIMITED_EVIDENCE'))
s['incomplete_deep_but_script_complete']=[r['Video_ID'] for r in n if r['statuses']['SCRIPT_REVIEW']=='COMPLETE_LIMITED_EVIDENCE' and not all(v=='COMPLETE_LIMITED_EVIDENCE' for v in r['statuses'].values())]
(O/'summary.json').write_text(json.dumps(s,indent=2));print(json.dumps({k:s[k] for k in ['matched_competitors','quantiles','sample_image_tiers','complete_script_tiers','incomplete_deep_but_script_complete']},indent=2))
# Verify all original frozen baseline source fingerprints without running repository validators.
m=json.loads((P/'audit-baseline/MANIFEST.json').read_text());checks=[]
for rel,expected in m['source_hashes'].items():
 p=R/rel;actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None;checks.append({'path':str(p),'expected':expected,'sha256':actual,'matches':expected==actual})
(O/'baseline_source_validation.json').write_text(json.dumps(checks,indent=2));print('baseline hashes',len(checks),'match',sum(r['matches'] for r in checks))
