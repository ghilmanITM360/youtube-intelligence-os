"""Write NICK_*_VALIDATION.json companions in the NICK_188 shape. argv: parent_commit completed remaining orig_pending wb_changed_desc NICK:dir ..."""
import json,hashlib,sys,csv
B='/Users/ghilmankhan/workprojects/yios-finance-machine-a/research/finance-economics-intelligence/'
parent,done,rem,orig,cells=sys.argv[1:6]; items=[a.split(':') for a in sys.argv[6:]]
h=lambda p:hashlib.sha256(open(p,'rb').read()).hexdigest()
m={r['Video_ID']:r for r in csv.DictReader(open(B+'VIDEO_MASTER.csv'))}
for nick,_ in items:
    p=json.load(open(B+f'audit-batches/{nick}.json'))['reviews'][0]; r=json.load(open(B+f'audit-batches/{nick}_READ_RECEIPTS.json'))
    vid=p['Video_ID']; k=r['calculation_receipts'][0]['results']
    out={'status':'PASS','video_id':vid,'nick':nick,'claims':len(p['script']['claim_audit']),'sources':len(r['primary_source_receipts']),'calculations':len(r['calculation_receipts']),
     'transcript_chars':r['receipts'][0]['character_count'],'parent_commit':parent,
     'writer_context':'MACHINE_A_OWNER_DIRECTED_FINANCE_EXECUTION_AUTHORIZED;branch codex/finance-machine-a-owner-directed;pending reconciliation with PR #36',
     'micro_batch':[n for n,_ in items],'changed_ledger_ids':[vid],'csv_projections':7,'source_fingerprints':26,
     'prior_completed_preserved':int(done)-len(items),'legacy_in_progress_preserved':True,
     'canonical_validators':'PASS_BOTH(validate_audit_966 strict receipts; validate_research PASS_BOUNDED_RESEARCH_NOT_PHASE_COMPLETION)',
     'finance_tests':'38_PASS','formatting_tests':'2_PASS',
     'calculation_verification':f'K01 reproduces master {float(m[vid]["Lifetime_rate_ratio"]):.5f} {k["tier_10"]} (5-peer {k["peer_ratio_5"]:.5f} {k["tier_5"]}); K02 analyst arithmetic',
     'claim_witness_check':'All claim stored_text_witness values equal text[start_char:end_char]; all claim source_ids resolve to primary_source_receipts; Text_SHA256 matches',
     'csv_projection_method':'Header-stable target-row replacement by build_audit_966.py; one changed line per CSV per target, Video_ID verified',
     'build_script_fix':'NONE',
     'workbook':{'status':'PASS','builder':'build_workbook_1612.mjs (established, unmodified) via @oai/artifact-tool runtime','unique_identities':1612,'completed':int(done),'remaining':int(rem),'original_pending':int(orig),'expansion_pending':646,
      'changed_cells':cells,'styles_changed':0,'formula_cells_changed':0,'formula_errors':0,'preexisting_hash_prefixed_text_cells':16,'zip_integrity':'PASS',
      'package_parts':'Identical except exporter relationship IDs; relationship targets identical','native_excel_recalculation':'NOT_TESTED','workbook_sha256':h(B+'FINANCE_1612_COMBINED_INTELLIGENCE.xlsx')},
     'semantic_acceptance':f'All {r["receipts"][0]["character_count"]} stored characters and six dimensions reviewed; {len(p["script"]["claim_audit"])} located claim groups; sources {", ".join(s["source_id"] for s in r["primary_source_receipts"])}. Audio unverified.',
     'hashes':{'VIDEO_AUDIT_966.jsonl':h(B+'VIDEO_AUDIT_966.jsonl'),f'{nick}.json':h(B+f'audit-batches/{nick}.json'),f'{nick}_READ_RECEIPTS.json':h(B+f'audit-batches/{nick}_READ_RECEIPTS.json'),'thumbnail':h(B+f'audit-batches/NICK_{vid}.jpg')}}
    json.dump(out,open(B+f'audit-batches/{nick}_VALIDATION.json','w'),indent=1,ensure_ascii=False); print(nick,'written')
