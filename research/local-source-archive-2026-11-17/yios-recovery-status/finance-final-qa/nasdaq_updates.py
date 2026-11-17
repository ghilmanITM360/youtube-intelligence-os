from pathlib import Path
import csv,json
r=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/extracted/forensic-analysis/casually-finance/2026-10-12');u='https://indexes.nasdaqomx.com/docs/2026_NDX_Changes_FAQ.pdf';n='https://www.nasdaq.com/newsroom/nasdaq100-index-methodology-update-why-now'
a={
'C21':('PARTIALLY_VERIFIED_PRIMARY_RULE_DATE','May 8 official explanation corroborates May 1 implementation after consultation; February announcement and June company IPO target remain unverified. '+n),
'C26':('VERIFIED_PRIMARY_RULE_PROVISIONS_AUDIO_UNVERIFIED','FAQ pages 3-5 verifies ordinary three-month seasoning and eligible top-40 fast entry after 15 trading days, subject to eligibility/scheduling. No spoken wording or actual admission certification.'),
'C27':('PARTIALLY_VERIFIED_PRIMARY_FLOAT_RULE','FAQ pages 6-8 verifies removal of prior 10% minimum and final 3x weighting cap. SpaceX actual float and qualification unverified.'),
'C28':('CONTRADICTED_THRESHOLD_PARTIAL_WEIGHT_ARITHMETIC','FAQ pages 5-6 threshold is 33 1/3%, not 20%; 4x3=12 and 5x3=15 are weighting arithmetic, not purchases. Eligible listed capitalization and float are distinct.'),
'C29':('CONTRADICTED_PURCHASE_MECHANISM_ACTUAL_ADMISSION_UNVERIFIED','FAQ page 7 hypothetical $1T/6% float/$600B tracking assets yields $6B purchases, 10% of float, not 300%. Conditional inclusion is not compulsory triple-share buying or actual named-company admission.')}
for v in ['-X6YzlY_8tM','JsK53moCyZA','MASTER']:
 p=r/('03_MASTER_DATA/MASTER_FINANCE_CLAIMS.csv' if v=='MASTER' else f'02_VIDEO_FORENSICS/{v}/FINANCE_CLAIMS.csv');rows=list(csv.DictReader(p.open()))
 for x in rows:
  vid=x.get('video_id',v)
  if vid=='-X6YzlY_8tM' and x['claim_id'] in a:
   st,note=a[x['claim_id']];x['verification_status']=st;x['notes']+=' FINALIZATION_PRIMARY_QA_2026-10-12: '+note+' '+u+' July FAQ includes July31 additions, not a silently assumed pre-upload vintage. Audio unlistened.'
  if vid=='JsK53moCyZA' and x['claim_id']=='C04':
   x['verification_status']='PARTIALLY_VERIFIED_RULE_EXISTENCE_BUYER_RANKING_UNVERIFIED';x['notes']+=' FINALIZATION_PRIMARY_QA_2026-10-12: Official rule verifies fast-entry pathway, not retirement-account buyer ranking or causal certainty. '+n
 with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(r/'07_VALIDATION/NASDAQ_RULE_VERIFICATION.md').write_text('''# Nasdaq rule-family verification

Scope: -X6YzlY_8tM C21/C26–C29 and JsK53moCyZA C04. Source observations, interpretations and external verification remain distinct; narration remains unlistened.

[Official May 8 explanation](https://www.nasdaq.com/newsroom/nasdaq100-index-methodology-update-why-now) corroborates May 1 implementation following public consultation, and separates full-capitalization eligibility ranking from listed-share weighting. Actual named-company admission, February announcement and June IPO completion are not established.

[July technical FAQ](https://indexes.nasdaqomx.com/docs/2026_NDX_Changes_FAQ.pdf), pages 3–8, verifies conditional top-40 fast entry after 15 trading days, removal of the 10% minimum float, and a final 3x weighting cap with a 33⅓% threshold. Weighting arithmetic is not purchases of shares. Its hypothetical example implies 10% of available float purchased, not 300%; actual flows depend on index weight and tracking assets. July31 additions are identified as a later vintage. Ordinary eligibility requirements remain.

[Current methodology](https://indexes.nasdaq.com/docs/Methodology_NDX.pdf) corroborates eligibility versus weighting. Current retrieval is not a complete historical version archive. Its archived bytes/checksum are in NASDAQ_PRIMARY_SOURCE_QA.json. FAQ was independently read through the web PDF reader, but direct archival retrieval failed DNS resolution; no nonexistent archive is claimed.

C26 rule provisions verified; C21/C27 partly verified; C28 threshold contradicted, arithmetic valid; C29 purchase mechanism contradicted. C04 rule exists, buyer ranking remains unverified. No exact spoken wording or actual financial flows are certified.
''')
print('six claim rows updated and reconciled')
