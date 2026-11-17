from pathlib import Path
import json,hashlib,subprocess,re
r=Path(__file__).parent;repo=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');report=r.parent/'MACHINE_A_NICK_165_RETIREMENT_WITHDRAWAL_REVIEW.md'
pre=json.loads((r/'preflight-hashes.json').read_text());now={p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in pre};assert pre==now
trans=(r/'registered-transcript.txt').read_text();assert len(trans)==18252;assert hashlib.sha256(trans.encode()).hexdigest()=='697d0545e42e6b2a060a1dda252f3c0a75c7d4aefb3d933f3c324b085c8f1bdd'
claims=json.loads((r/'transcript-claim-inventory.json').read_text())
for c in claims:assert trans[c['start_char_inclusive']:c['end_char_exclusive']]==c['wording']
calc=json.loads((r/'calculations.json').read_text());assert abs(calc['monthly1076_3y7']-1076*sum((1+.07/12)**i for i in range(36)))<1e-7
assert calc['withdraw5000004']==500000*.04;assert abs(calc['monthly_equivalent']-500000*.04/12)<1e-9
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip();remote=subprocess.check_output(['git','ls-remote','origin','refs/heads/research/finance-economics-intelligence'],cwd=repo,text=True).split()[0]
pr=json.loads(subprocess.check_output(['gh','api','repos/ghilmanITM360/youtube-intelligence-os/pulls/36'],cwd=repo,text=True));assert head==remote==pr['head']['sha']=='7e70f061aae849e9929b531c4bc855b23edda179'
status=subprocess.check_output(['git','status','--porcelain'],cwd=repo,text=True);assert all(x.startswith('?? ') for x in status.splitlines())
body=report.read_text();assert all(f'## {i}.' in body for i in range(1,16));assert all(c['id'] in body for c in claims)
# Byte hashes of downloads establish local preservation, not authenticity of access-error pages.
p=r/'additional-source-downloads.json';d=json.loads(p.read_text())
for v in d:
 if v['file']=='dol2024-primary.html':v['content_status']='REQUEST_ACCESS_PAGE_NOT_SOURCE_CONTENT; ORIGINAL_TEXT_READ_VIA_WEB_TOOL';v['verified_source_download']=False
p.write_text(json.dumps(d,indent=2))
extra={'scf-nominal-historical.xlsx':'https://www.federalreserve.gov/econres/files/scf2025_tables_internal_nominal_historical.xlsx','scf2022-extract.zip':'https://www.federalreserve.gov/econres/files/scfp2022excel.zip','scf-chart-data.zip':'https://www.federalreserve.gov/econres/scf/dataviz/download/zips/scf.zip','trinity1998.pdf':'https://athenaconsulenza.it/wp-content/uploads/2025/05/Retirement-Savings-Choosing-a-withdrawal-rate-that-is-sustainable.pdf','nm2025-release.html':'https://news.northwesternmutual.com/2025-04-14-Americans-Believe-They-Will-Need-1-26-Million-to-Retire-Comfortably-According-to-Northwestern-Mutual-2025-Planning-Progress-Study'}
(r/'supplemental-source-urls.json').write_text(json.dumps(extra,indent=2))
result={'review_date':'2026-10-23 Asia/Karachi','head':head,'remote_finance_head':remote,'pr36_head':pr['head']['sha'],'pr36_base':pr['base']['sha'],'pr36_state':pr['state'],'tracked_clean':True,'status':status,'protected_hashes_before':pre,'protected_hashes_after':now,'transcript_slice_checks':len(claims),'arithmetic_cross_check':'36-deposit direct summation matches annuity formula; 4% year-one annual/monthly matched','report_sections':15,'final_live_usage':{'five_hour_used_percent':24,'weekly_used_percent':4,'paid_balance':0,'reset_credits_used':0},'canonical_edits':False}
(r/'final-checks.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
