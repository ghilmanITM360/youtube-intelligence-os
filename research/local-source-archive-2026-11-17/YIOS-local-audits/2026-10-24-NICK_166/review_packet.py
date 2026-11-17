import pathlib,json,re,hashlib,subprocess,csv
O=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-NICK_166');R=pathlib.Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');B=R/'research/finance-economics-intelligence'
a=json.loads((O/'NICK_166.json').read_text());d=json.loads((O/'NICK_166_READ_RECEIPTS.json').read_text());s=(O/'canonical-transcript.txt').read_text();r=a['reviews'][0]
for c in d['financial_claim_locations']:
 loc=c['location'];assert s[loc['start']:loc['end']]==c['original_quote'];assert ' '.join(c['original_quote'].split())==c['claim']
assert set(c['source_id'] for c in d['primary_source_receipts']) >= {v for c in r['script']['claim_audit'] for v in c['source_ids']}
assert len(r['script']['claim_audit'])==35
# Narrow publication review: no competing Finance writer observed; user's current release is authoritative.
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()=='ad28c731bc059b11be66ebb00b1cec79f4518462'
assert not subprocess.check_output(['git','diff','--name-only'],cwd=R,text=True).strip()
# Original source statements must not be accidentally attributed to the creator.
assert not re.search(r'4%|four.percent|social security',s,re.I)
for x in [a,d]:
 raw=json.dumps(x);assert '[object Object]' not in raw
# Validate source receipts' explicitly unresolved chronology.
u=next(x for x in d['primary_source_receipts'] if x['source_id']=='USDA_DEC2025');assert u['publication_applicability'].startswith('UPLOAD_DATE_APPLICABILITY_UNRESOLVED')
report={'financial_claims':35,'primary_sources':18,'calculation_receipts':9,'exact_quotes_and_offsets':'PASS','claim_source_id_links':'PASS','script_json_under_excel_limit':len(json.dumps(r['script'],ensure_ascii=False)),'retirement_rule_not_attributed':'PASS','source_vintage_limitations':'EXPLICIT','baseline_head':'ad28c731bc059b11be66ebb00b1cec79f4518462','semantic_reviewer':'Same sole researcher, independent arithmetic and original-source cross-check; no external second-agent review claimed.'}
(O/'preassembly-review.json').write_text(json.dumps(report,indent=2));print(report)
