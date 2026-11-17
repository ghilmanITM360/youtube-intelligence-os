from pathlib import Path
import csv,json,collections
r=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/extracted/forensic-analysis/casually-finance/2026-10-12');q=r/'07_VALIDATION';a=json.loads((q/'JAPAN_2024_MARKET_WINDOW_QA.json').read_text());url='https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500&cosd=2024-07-31&coed=2024-08-06';boj='https://www.boj.or.jp/en/mopo/mpmdeci/state_2024/k240731a.htm';march='https://www.boj.or.jp/en/mopo/mpmdeci/state_2024/k240319a.htm';nik='https://indexes.nikkei.co.jp/atoz/2024/09/202408.html'
updates={('5umJ63d3rzQ','C07'):('PARTIALLY_VERIFIED_POLICY_AND_MARKET_WINDOWS_AUDIO_UNVERIFIED',f'BoJ March19 ended YCC/negative-rate framework and set overnight call target0–0.1%; July31 target0.25%, effectiveAug1. Nikkei original August report gives Aug5 daily decline12.39%, largest point loss and second-largest percentage loss. S&P daily closes show Aug2→Aug5 {a["Aug2_to_Aug5_percent"]:.4f}%, while July31→Aug5 is {a["Jul31_to_Aug5_percent"]:.4f}% across threeUSsessions. Thus6% fits multiday window, not Aug5 daily decline. Exact narration, causal attribution and17-year superlative not independently certified. '+march+'; '+boj+'; '+nik+'; '+url),('rSa2aziEsAI','C04'):('PARTIALLY_VERIFIED_RESERVE_INTEREST_TERMS_COST_UNVERIFIED','BoJ July31 statement applies0.25% to financial-institution current-account balances excluding required reserves, effectiveAug1,2024. This verifies reserve-remuneration mechanism/exception, not current2026 policy rate, trillions-loss magnitude, bond-portfolio yield or causal inevitability. '+boj)}
for v in ['5umJ63d3rzQ','rSa2aziEsAI','MASTER']:
 p=r/('03_MASTER_DATA/MASTER_FINANCE_CLAIMS.csv' if v=='MASTER' else f'02_VIDEO_FORENSICS/{v}/FINANCE_CLAIMS.csv');rows=list(csv.DictReader(p.open()))
 for x in rows:
  key=(x.get('video_id',v),x['claim_id'])
  if key in updates:x['verification_status']=updates[key][0];x['notes']+=' JAPAN_PRIMARY_QA_2026-10-12: '+updates[key][1]
 with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
p=q/'FINANCE_CLAIM_VERIFICATION.csv';rows=list(csv.DictReader(p.open()))
for x in rows:
 key=(x['video_id'],x['claim_id'])
 if key in updates:x.update(external_verification_result='PARTIALLY_VERIFIED',existing_evidence_status=updates[key][0],verification_scope='Policy/event components only; audio, causal attribution and remaining measurements not certified',primary_source_url=boj+'; '+url if key[0]=='5umJ63d3rzQ' else boj,evidence_notes=x['evidence_notes']+' JAPAN_PRIMARY_QA_2026-10-12: '+updates[key][1])
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
p=q/'FINALIZATION_CLAIM_CENSUS.json';o=json.loads(p.read_text());o['result_counts']=dict(collections.Counter(x['external_verification_result'] for x in rows));p.write_text(json.dumps(o,indent=2)+'\n')
(q/'JAPAN_PRIMARY_SOURCE_QA.md').write_text(f'''# Japan policy and market-window verification

5umJ63d3rzQ C07 (204.4–231.16s) and rSa2aziEsAI C04 retain exact-audio uncertainty. Existing ASR is a wording basis, not direct listening.

[BoJ March19 decision]({march}) verifies termination of the YCC/negative-rate framework and overnight call target0–0.1%. [July31 decision]({boj}) sets0.25%, effectiveAugust1. Its current-account interest terms explicitly exclude required reserves. This qualifies the reserve mechanism, not the Short’s trillions-loss magnitude or2026 rate.

[Original Nikkei August report]({nik}) supports August5 decline12.39%, largest point loss and second-largest percentage decline. Point and percentage records differ. This is a primary Japanese-language index-publisher report; paraphrase does not certify narrator wording.

[S&P daily closes via FRED]({url}) give5346.56 onAugust2 and5186.33 onAugust5: {a['Aug2_to_Aug5_percent']:.4f}%. July31 close5522.30 toAugust5 gives {a['Jul31_to_Aug5_percent']:.4f}% across threeUSsessions. Approximately6% can fit the multi-session window, while the Nikkei figure is one day. Do not force the entire ASR sentence into a shared one-day window or infer rate-hike causality from chronology. The17-year superlative still needs a comparable historical policy series/primary attribution.

Results: two composite claim groups PARTIALLY_VERIFIED. Source CSV and lossless gzip wrappers of original official/publication bytes, checksums and arithmetic are inJAPAN_2024_MARKET_WINDOW_QA.json. No original video/recovered files changed; no direct listening occurred.
''');print(o['result_counts'])
