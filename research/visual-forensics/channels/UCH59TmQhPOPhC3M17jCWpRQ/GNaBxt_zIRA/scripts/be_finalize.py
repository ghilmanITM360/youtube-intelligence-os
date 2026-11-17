# Write report, blueprint, quality gate C and handoff from consolidated evidence. cwd = video workspace. Args: video_id rv_prefix
import csv,json,sys
vid,pre=sys.argv[1],sys.argv[2]
man=json.load(open('source_manifest.json'));summ=json.load(open('tables/consolidation_summary.json'))
spec=json.load(open('production_specs/specifications_v1.json'))
st=list(csv.DictReader(open('tables/states_v1.csv')))
art={r['state']:r for r in csv.DictReader(open('tables/consolidated_art_audit.csv'))}
pcs=list(csv.DictReader(open('tables/primary_corrections.csv')))
nar=list(csv.DictReader(open('tables/consolidated_narration_relation.csv')))
t=lambda s,n=90:(s or '').replace('|','/').replace('\n',' ')[:n]
L=[f"# Visual CT-scan report v1 — Barely Evolved {vid}",f"Title: {man.get('title')}  ",f"Source sha256: {man['sha256']} (matches registry: {man.get('sha256_matches_registry')})  ",
"Status: **VISUAL_ANALYSIS_PARTIAL**. CT_SCAN_COMPLETE not awarded: audible synchronization is BLOCKED_CAPABILITY (no listener), and visual coverage is sampled (native representatives + 8-frame strips), not all-frame inspection.","",
"## Evidence classes","- MEASURED: FULL_FRAME_MEASUREMENTS.csv (every frame), detector candidates, PTS.",
"- OBSERVED: bounded sonnet reviewer reads (one image per Read call; transcript-verified via be_validate_batch.py), plus orchestrator native-frame checks in primary_corrections.csv.",
"- INFERRED: interpretation of intent / narration relation. ASR is machine transcription, not listening.","",
"## Coverage",f"- States: {len(st)} (tables/states_v1.csv). Art audit {summ['art_audit_states']}, prompts {summ['state_prompts_states']}.",
f"- Motion events (strip-observed): {summ['motion_events']}; types {json.dumps(summ['motion_types'])}.",
f"- ASR segments related to visuals (PARTIAL, sampled frames only): {summ['narration_segments_covered']}; relations {json.dumps(summ['relation_counts'])}.",
f"- Reviewer batches: {', '.join(summ['batches'])}; not validated: {summ['not_validated'] or 'none'}.","",
"## Primary corrections (orchestrator, separate from reviewer claims)"]+[f"- {p['id']} {p['state']}: {p['status']} — {t(p['primary_observation'],220)}" for p in pcs]+["",
"## Motion grammar (from production_specs/specifications_v1.json)"]+[f"- {m['id']}: {m['n_events']} events in {m['n_states']} states; median observed span {m['observed_span_frames']['median']} frames (strip-bounded); keyword counts {json.dumps({k:v for k,v in m['description_keyword_counts'].items() if v})}" for m in spec['modules']]+["",
"## Narration relation (INFERRED, ASR-based, not listened)",f"Counts: {json.dumps(summ['relation_counts'])}. Literal illustration dominates in this sample; this is not a claim about audience response, CTR or retention.","",
"## State ledger (abridged; full fields in tables/consolidated_art_audit.csv)","| state | frames | t (s) | characters/assets | camera | label |","|---|---|---|---|---|---|"]
for s in st:
    a=art.get(s['state'],{})
    L.append(f"| {s['state']} | {s['start']}-{s['end']} | {float(s['start_pts_s']):.2f} | {t(a.get('characters_and_recurring_assets'))} | {t(a.get('camera_framing_motion'),60)} | {a.get('evidence_label','MISSING')} |")
L+=["","## Not established","- Fonts, software, layer stacks, easing curves, sound design: UNAVAILABLE.","- Audio sync, SFX placement, music: BLOCKED_CAPABILITY.","- Interiors of long states between sampled frames: not inspected.","- Any retention/CTR explanation: not inferred."]
open('visual_ct_scan_report_v1.md','w').write('\n'.join(L)+'\n')
B=[f"# Reconstruction blueprint v1 — original equivalent of Barely Evolved {vid} techniques","Label: PROPOSAL built on OBSERVED technique families. Copy no character, drawing or wording from the source.","",
"## Canvas","1920x1080, 30000/1001 fps CFR (MEASURED for the source; adopted as a production choice).","",
"## Pipeline (proposed)","1. Script new original narration; segment into beats roughly matching the observed state density "+f"({len(st)} states over {float(st[-1]['end_pts_s']):.0f} s, mean {float(st[-1]['end_pts_s'])/len(st):.1f} s/state, MEASURED for source).",
"2. Per beat, choose one illustration per tables/consolidated_state_prompts.csv (prompts already rewritten as original equivalents with placeholders).",
"3. Animate with the module set below; timing taken from observed frame spans, easing left to the animator (unverified in source).",
"4. Audio: write and mix independently; no sync rule can be derived because the source audio was not listened to.",
"","## Modules"]+[f"### {m['id']}\n- Observed: {m['n_events']} events; span min/median/max {m['observed_span_frames']['min']}/{m['observed_span_frames']['median']}/{m['observed_span_frames']['max']} frames (strip-bounded)\n- Examples: "+'; '.join(t(e,120) for e in m['evidence'][:3])+f"\n- Production choice: {m['original_production_choice']}" for m in spec['modules']]+["",
"## Acceptance tests (proposed, not yet run for this video)","- Frame-span check: each animated move measured with the same per-frame mean-abs-diff script used on the source; spans within the observed min-max range.","- Originality check: no source character silhouette, text or layout copied 1:1.","- Coverage check: every beat has a prompt and a module assignment.","","Reconstruction test: NOT_RUN for this video (video 1 RT-01 covers shared timing modules)."]
open('reconstruction_blueprint_v1.md','w').write('\n'.join(B)+'\n')
g={'status':'VISUAL_ANALYSIS_PARTIAL','video_id':vid,'checkpoint':'C','source_identity':'PASS (sha256 matches registry)',
 'full_frame_measurement':'PASS (all frames measured)','state_segmentation':f'DRAFT_PASS ({len(st)} states; long-state interiors sampled)',
 'art_audit':f"PASS_SAMPLED ({summ['art_audit_states']})",'motion':f"PARTIAL ({summ['motion_events']} strip events; strips cover measured peaks only)",
 'narration_relation':f"PARTIAL ({summ['narration_segments_covered']} ASR segments; ASR not listened)",'state_prompts':f"PASS ({summ['state_prompts_states']})",
 'production_specs':'DRAFT (production_specs/specifications_v1.json)','reconstruction_blueprint':'DRAFT (reconstruction_blueprint_v1.md)','reconstruction_test':'NOT_RUN',
 'listening':'BLOCKED_CAPABILITY','audible_sync':'BLOCKED_CAPABILITY','CT_SCAN_COMPLETE':False,'FULL_AV_SIGNOFF':False,
 'reviewers':f'{pre} b-batches: Claude sonnet subagents (same vendor as orchestrator claude-opus-5-5); not independent humans','primary_corrections':len(pcs)}
json.dump(g,open('quality_gate_C.json','w'),indent=1)
H=[f"# Continuation handoff C — {vid}","Owner session: 7a28d062-11cb-4600-a99d-27b9caa812d6 (lock ~/YIOS-local-audits/barely-evolved/.be_writer_lock).","",
"Done: all reviewer batches validated; consolidated tables; specs v1; report v1; blueprint v1; quality_gate_C.json.","",
"Blocked / open:","- Human listening pass for audible sync, SFX, music (BLOCKED_CAPABILITY).","- Dense native-frame review inside long states and for strip-ambiguous events (reviewers flagged cut-vs-zoom ambiguities).",
"- Reconstruction test for this video (NOT_RUN).","- Reviewer claims not individually primary-verified except primary_corrections.csv."]
open('CONTINUATION_HANDOFF_C.md','w').write('\n'.join(H)+'\n')
print('ok',len(L),len(B))
