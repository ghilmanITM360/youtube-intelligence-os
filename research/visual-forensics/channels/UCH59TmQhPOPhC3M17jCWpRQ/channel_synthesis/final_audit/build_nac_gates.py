# Per-video quality_gate_NAC.json from FINAL_AUDIT_MATRIX_v2.csv; R18/R19 evidence refreshed from FINAL_VALIDATION_v2.json. quality_gate_FINAL.json untouched.
import csv,json,glob
val=json.load(open('FINAL_VALIDATION_v2.json'));M=list(csv.DictReader(open('FINAL_AUDIT_MATRIX_v2.csv')))
for v in ['uPQcyookL0Y','mNLNb-Z4T0M','GNaBxt_zIRA']:
    r=val[v];g={}
    for m in M:
        ev=m['evidence_'+v]
        if m['req_id']=='R18':ev=f"{r['seal']['file']} {r['seal']['entries']} entries, {len(r['seal']['mismatches'])} mismatches (FINAL_VALIDATION_v2.json)"
        if m['req_id']=='R19':ev=f"{r['remote_readback']['remote_files']} remote files, {len(r['remote_readback']['sha_mismatch_vs_local'])} sha mismatches vs local, invalid json {len(r['remote_readback']['invalid_json'])} (FINAL_VALIDATION_v2.json; v1 1 file maps to campaign/)"
        g[m['req_id']+' '+m['requirement']]=dict(status=m[v],evidence=ev)
    out=dict(video_id=v,audit='BE non-audio completion close-out 2026-11-05 (session 1e8761b1)',status='VISUAL_ANALYSIS_PARTIAL',CT_SCAN_COMPLETE=False,FULL_AV_SIGNOFF=False,
        non_audio_verdict='NON_AUDIO_WORK_REMAINS',remaining_non_audio=['R20 STORAGE_DESTINATION_REQUIRED','R13 independent (non-Claude) review'],
        excluded_audio=['R08 PARTIAL (ASR only)','R09 BLOCKED','R21 BLOCKED'],gates=g,supersedes='quality_gate_FINAL.json kept unchanged')
    o=glob.glob(f'kit_outputs/{v}_*')[0]+'/quality_gate_NAC.json';json.dump(out,open(o,'w'),indent=1);print(o,sum(x['status'].startswith('PASS') for x in g.values()),'/',len(g))
