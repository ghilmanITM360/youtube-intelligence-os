"""Validated local milestone; union U artifacts because GitHub rejected U pushes."""
from pathlib import Path
import csv,json,hashlib,datetime,shutil
R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');S=R/'session_20261105'
assert not (R/'EVIDENCE_SHA256SUMS_checkpoint_V').exists()
for label in ['T','U']:
    for line in (R/f'EVIDENCE_SHA256SUMS_checkpoint_{label}').read_text().splitlines():
        h,n=line.split(maxsplit=1);assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h,n
early_ref='pdf_early_traversal_native_v1/OUT_pdf_early_traversal_native_v1.json'
early=json.loads((R/early_ref).read_text());ep=json.loads((S/'pdf_early_traversal_native_independent_return_audit_v1.json').read_text())
assert hashlib.sha256((R/early_ref).read_bytes()).hexdigest()==ep['saved_output_sha256']
assert not early['status'].startswith('IN_PROGRESS')
stats=json.loads((S/'native_reuse_focus_zoom_integration_v14_stats.json').read_text())
if (S/'pdf_complete_compound_integration_v15_stats.json').exists():stats.update(json.loads((S/'pdf_complete_compound_integration_v15_stats.json').read_text()))
event_version=stats['event_ledger_version'];event_ref=f'integrated_v4/visual_event_ledger_{event_version}.csv'
events=list(csv.DictReader((R/event_ref).open()));assert len(events)==len({x['event_id'] for x in events})==948
candidate=sum(x['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET' for x in events)
parts=list(csv.DictReader((R/'integrated_v4/frame_partition_v6.csv').open()));counts=[0]*19862
for x in parts:
    for n in range(int(x['start']),int(x['end'])+1):counts[n]+=1
assert set(counts)=={1} and len(parts)==627
proof_refs=['native_cut_batch01_resume','native_cut_batch02','compound_cut_followup','selection_focus_boundary','root_pdf_midpoint01','root_pdf_midpoint02','pdf_late_zoom_native','pdf_early_traversal_native']
proofs={n:json.loads((S/(n+'_independent_return_audit_v1.json')).read_text()) for n in proof_refs}
current_returns=sum(x['actual_native_fullframe_returns'] for x in proofs.values())
reuse=json.loads((S/'native_fullframe_prior_receipt_reuse_audit_v1.json').read_text())
facts=dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),checkpoint='V',publication='LOCAL_SEALED_PENDING_NORMAL_PUSH;U_SERVER_PUSH_FAILURE_RECORDED',
 remote_checkpoint='T',remote_sha='4d625184deb606b9c0585e63cafb9b80b62e9974',previous_local_U_commit='df22c7e07748f0701816e95f5e0e7acf723d68ae',
 source_sha256='030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66',source_path='/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4',
 first_pass_shards_reused=10,new_first_pass_shards=0,pending_first_pass_shards=0,gap_reviews=123,gap_frames=3116,merge_split_rulings=146,
 event_ledger=event_ref,event_rows=948,partition='integrated_v4/frame_partition_v6.csv',numeric_frames_once=19862,partition_intervals=627,distinct_states=475,composition_groups_not_shots=329,
 partial_verified_native_cut_onsets=50,candidate_only_timing_rows=candidate,narration_sampled_ASR_rows=199,narration_undetermined=21,potential_ASR_flags=7,
 current_successful_native_derivative_request_returns=current_returns,independent_root_repeat_displays=6,new_scaled_returns=0,
 prior_native_repeated_source_frame_instances_in_initial39requests=10,unique_source_frame_coverage='NOT_IMPLIED_BY_DERIVATIVE_PATHS;see priorreceipt reuse audit;8057alsohadoldercursorROI',
 source_actual_listening_seconds=0,fully_certified_videos=0,target_distinct_videos=35,exact_roster_channel='Casual Finance',
 production_original_draft_states=447,missing_integrated_production_specs=28,extended_prompt_intervals=152,
 early_PDF_review_status=early['status'],early_PDF_native_returns=ep['actual_native_fullframe_returns'],early_PDF_pending_paths=early['pending_paths'],
 source_media='DURABLE_LOCAL_ONLY;NO_RAW_MEDIA_OR_FRAMES_IN_GIT',CT_SCAN_COMPLETE=False)
(S/'checkpoint_V_verified_stats.json').write_text(json.dumps(facts,indent=2)+'\n')
q=json.loads((R/'session_20261105/QUALITY_GATE_checkpoint_U.json').read_text());q.update(status=f'VISUAL_ANALYSIS_PARTIAL_PARTITION_V6_EVENTS_{event_version.upper()}_CHECKPOINT_V_LOCAL_SEALED',
 coverage_ref='research/session_20261105/coverage_checkpoint_V.json',known_issues='research/session_20261105/KNOWN_ISSUES_LEDGER_v11.md',event_ledger='research/'+event_ref,
 active_task='ALL_REVIEWERS_STOPPED;resource/publication reserve',next_task='Inspect LOCAL_SEALED_HANDOFF_V.md and live remote parent. Publish V superset by normal push once GitHub ref-rule failure permits; then only exact pending early-PDF paths if any, otherwise global candidate timing/native floor and remaining motion/production/hearing gates.',checkpoint_V=facts,
 resource_policy=dict(five_hour_used_ceiling=95,publication_validation_release_reserve=True,weekly_preservation_near_used_percent=95,paid_usage=False,reset_credits_redeemed=False))
q['gates']['all_frame_numeric_timeline']='PASS19862ONCE_PARTITION_V6;NOT_SEMANTIC_COMPLETION'
q['integration']=dict(partition='research/integrated_v4/frame_partition_v6.csv',interval_rows=627,distinct_states=475,composition_groups_not_shot_count=329,frames_once=19862,numeric_gaps=0,numeric_overlaps=0,gap_reviews=123,gap_frames=3116,merge_split_rulings=146,semantic_status='Native refinements plus prior independent firstpass/gap rulings; global semantic/native floor remains partial')
q['gates']['full_semantic_event_timing']=f'PARTIAL;{candidate}CANDIDATE_ONLY_ROWS_PLUS_OTHER_PARTIAL_GATES;50PARTIAL_CUT_ONSETS;NOT_SHOTCOUNT'
q['gates']['production_state_prompts']='DRAFT447;28MISSING_INTEGRATED_SPECS;152EXTENDED_SPANS;WHOLE_VIDEO_STATIC_ANCHOR_COLD_START_RECONSTRUCTION_PENDING'
q['production_current']=dict(draft='production_v1/per_state_production_spec_DRAFT_v4.csv',retrieval_index='production_integrated_v1/integrated_production_interval_index_v4.json',original_prompt_states=447,missing_integrated_states=28,extended_prompt_spans=152,global_production_pass=False)
assert q['CT_SCAN_COMPLETE'] is False
(S/'QUALITY_GATE_checkpoint_V.json').write_text(json.dumps(q,indent=2)+'\n')
coverage=dict(facts,temporal_semantic_scope='Native pairs/selected object windows and prior qualified evidence only; numeric19862once does not certify all-frame semantic/100ms floor.',
 selection_visible_native_samples=[8057,8086],selection_removal='UNKNOWN_AFTER8086;NO_FOCUS_OR_GRAY_BOUNDARY_CERTIFIED',
 staged_document_replacement='Foreground2769,backdropclear2770;nativeone-frameintermediatestatewithinexistingcompositiongroup,notnewshot',
 native_document_zoom_component_exits=dict(thumbnail_fragments=1633,outer_dark_sidebar=1636,final_dark_gutter=1639),
 remaining=['Global native/100ms/semantic/object/facial/cut/onset floor','SUB032 microfeature','Selection eventual removal after8086','Chart cursor precursor/final motion offset','Biography slide offset','28original integrated production specs/152extended spans/447state global QA','Full original reconstruction/cold-start/AV requirements','Qualified actual source hearing0;ASRneverlistening'])
(S/'coverage_checkpoint_V.json').write_text(json.dumps(coverage,indent=2)+'\n')
known='''# Current issues — checkpoint V, local only until remote receipt

- Prior raw/draft/reviewer/sealed layers are immutable.10firstpass/123gap/146merge-split/199sampledASR retained. Actual source listening0; ASR is not hearing.0/35certified.
- Two normal U pushes failed GitHub fatal error in commit_refs_rules. RemoteT is still the latest remotely verified checkpoint42textbyte readbacks/39seals. U localcommit/rawobject and diagnosis preserved; no force/alternate-ref/config/payment bypass. V superset includes unpublished U artifacts. V is not remotely available until an actual remote SHA/readback receipt says so.
- New native01/02 pair review18cases:16single cut onsets; compound0054/0082 separately investigated. EP0082 is a two-stage foreground/backdrop substitution2769/2770, with one-frame intermediate state now explicit in partitionv6. Twelve old native receipts reused for4more parent rulings/3newinventoryentries3810/4270/5448; cut6830 already in inventory. Candidate start4245 is fragmentation;6771 is rain overlay, distinct from later cuts4270/6830.
- First native-receipt census found10of39early-current derivative returns alreadyhadpriornativefullframe receipts. Root6repeat semantic spots are separate repeat displays. New PNG paths/display counts are not new global source-frame coverage. Later requests excluded prior fullframe receipts;8057addsfullcontext around an older cursorROI. All actual byte/order/native-dimension audits are saved.
- Selection remains blue at8057/8086. Fixed-coordinate mask loses correspondence under page zoom; declining mask count is not deselection. Gray/focus/removal boundary unproven; eventual offset remains unknown beyond8086.
- LatePDF1631–1640 is progressive same-page enlarge/translate/crop, not whole-scene cut. Native component exits1633/1636/1639; motion continues1640, no settle. Entire early-window status and exact pending paths are in checkpoint_V_verified_stats.json and raw/audit output; never treat prepared or missing paths as viewed.
-627intervals/475states/329dominantcompositiongroups cover19862frames once. These are not a certified shotcount.50partialcut-onset inventory, candidate-only count in latest stats; exact/selected native onsets do not certify every compound motion or global100msfloor.
-447state original-productionDRAFT still requires global originality/static-anchor/animation/cold-start/reconstruction QA.28inserted specs missing,152extended spans. Prior75/37frame original tests are bounded. SUB032, selection final removal, chart cursor precursor/final offset, biography offset and other global semantic/native/motion/facial gates remain open.
- Exact35roster independently rechecked for distinct IDs and exact Casual Finance queue channel only. Queue/file presence is selection evidence. Revalidate each source hash/current status/platform identity before its analysis; other34platformIDs not freshly confirmed here. Media/PNG/HTML remain local even if their hashes are published.
'''
(S/'KNOWN_ISSUES_LEDGER_v11.md').write_text(known)
handoff='''# Video006 checkpoint V — recoverable local milestone

This is LOCAL_SEALED until actual remote publication/readback. Latest verified remote T4d625184deb606b9c0585e63cafb9b80b62e9974 (42textreadbacksPASS/39sealsPASS). Local unpublished U df22c7e07748f0701816e95f5e0e7acf723d68ae was rejected twice by GitHub commit_refs_rules. V includes U's text evidence. Do not claim U/V remote availability from hashes. See PUBLICATION_BLOCKER_U_v1.json, exact raw Ucommit backup, prepared_U.json. No configuration/visibility/payment/bypass changes. After V prepare, exact localVcommit/tree/parent and remote readback state belong in LOCAL_SEALED_HANDOFF_V.md. Recheck live remote parent/scoped diff; normal push only, reconcile newer work, never force. If V supersedes U, publish the V superset directly when remoteT is still its parent; do not publish U first and create a sibling-parent conflict.

Source xtqbRt94TTw hash030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66 at /Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4; workspace /Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan. Original media unchanged/durableLOCAL_ONLY. Exact35roster at /Users/ghilmankhan/YIOS-local-audits/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104/target_roster_v1.json,35distinct exactCasualFinance, noCasualEconomics; source/status/platform checks remain per-video,0/35certified. ContinueVideo006first.

Live saved-output counts and final PDFstatus: checkpoint_V_verified_stats.json. Event ledger/partition are versioned, originals immutable.10firstpass reused,0new/0pending;123gaps/3116frames and146rulings preserved.199sampledASRrows/21UNDETERMINED/7potentialflags;actualqualifiedhearing0. ASR156, completed narration33/nativeQA16/motion4/selection/chart/table/ambiguous/bio/opening/prototypes must not be repeated. Newnativecut/followup/focus/late/earlyPDF requests and proof audits are explicit; prior-native lookup prevents avoidable redisplays. Rawfinal and recoverable partial snapshots preserved. Display counts are not global uniqueness or quality certification.

Native staged replacement2769/2770 adds one-frame intermediate state;627partitionintervals/475distinctstates/329dominantcompositiongroups cover19862once, not shotcount.50partialcutonsets; globalcandidate-only and otherpartialtiming gates remain. Blue selection visible8057/8086; removal/gray/focus boundary unknownafter8086. Native latePDF1631–1640 progressive same-page zoom/crop, chrome components exit1633/1636/1639; no source-preset/settle claim. Full earlyPDF decision/pending details are in actual raw/audit/stats, not inferred from extraction.28missing original integrated production specs/152extended spans/447draftstate QA plus global semantic/native/object/facial/100ms/shot/motion/production/reconstruction andactualhearing gates remain. CT_SCAN_COMPLETE=false.

NEXT: after fresh resource/ownership gates inspect current earlyPDF final/partial output and pending_paths; resume only actual pending images if any. Otherwise continue global candidate-only timings and other remaining gates, first reuse prior_native_fullframe_receipt_index_v1.json and qualified saved reviews before requesting images. One video/one bounded reviewer at a time. No new reviewer near resource limits; owner95%fivehour ceiling includes validation/publication/release reserve, weekly preservation near95%, no paid/resetcredits. Current resource evidence saved separately; samechat2hour follow-up retained until35fullqualitycontracts pass or ownercancels, no busy-wait/duplicate automations.

Own v3session labelcodex-v006-native-resume-20261105,run01a1a2b1-c283-75f3-b64f-f45a440501b1,actualCodexPID1455/startTueNov3 21:28:19;private acquisition receipt session_20261105/native_resume_owner_receipt_private.txt. Verify actualPID/start/token/live sessions, never recoverfromheartbeat/quietremotealone. Lock HELD atseal; release only this token at safe stop and record actualFREE in LOCAL_SEALED_HANDOFF_V.md. Preserve Finance/Barely work/processes/locks/schedulers and unrelated checkout/index/stashes/untracked/ignored. CanonicalHEADf4dc5d14d6ad03c1edd92e48fac779e7a8555fc5/localresearchref2b10f104c1edf0562e2628d1dab1afba2546bd8e unchanged; authenticatedopenPRsnapshot[];noPRcreated/merged/closed. No newworktrees/clones/reset/clean/Graphify/rawmediaGittransport.
'''
(S/'CONTINUATION_HANDOFF_checkpoint_V.md').write_text(handoff)
(R/'CONTINUATION_HANDOFF.md').write_text(handoff)
(R/'visual_ct_scan_report_v9.md').write_text('# Video006 checkpoint V partial report\n\n'+handoff.split('\n',1)[1])
files=[]
for folder in ['native_cut_batch02_v1','compound_cut_followup_v1','selection_focus_boundary_v1','pdf_transition_midpoint_v1','pdf_transition_midpoint02_v1','pdf_late_zoom_native_v1','pdf_early_traversal_native_v1']:
    files.extend(str(p.relative_to(R)) for p in (R/folder).iterdir() if p.is_file() and p.suffix in {'.json','.md','.txt'})
files.extend(str(p.relative_to(R)) for p in S.iterdir() if p.is_file() and p.suffix in {'.json','.md','.txt'} and 'private' not in p.name.lower() and 'publication_' not in p.name)
files.extend(['integrated_v4/visual_event_ledger_v12.csv','integrated_v4/visual_event_ledger_v13.csv','integrated_v4/visual_event_ledger_v14.csv','integrated_v4/frame_partition_v6.csv','integrated_v4/composition_intervals_v6.csv','integrated_v4/reused_compound_cut_tracks_v2.json','integrated_v4/document_zoom_track_v1.json','production_v1/shot_ledger_PARTIAL_v5.csv','production_v1/shot_ledger_PARTIAL_v6.csv','production_v1/motion_camera_facial_index_PARTIAL_v7.csv','production_v1/motion_camera_facial_index_PARTIAL_v8.csv','production_v1/motion_camera_facial_index_PARTIAL_v9.csv','production_integrated_v1/integrated_production_interval_index_v4.json','v2_scripts/curate_final_motion_index_v9.py','visual_ct_scan_report_v9.md'])
if event_version=='v15':files.extend(['integrated_v4/visual_event_ledger_v15.csv','integrated_v4/document_zoom_track_v2.json'])
files.extend(str(p.relative_to(R)) for p in (R/'v2_scripts').glob('*.py') if any(x in p.name for x in ['native_pair_returns','bounded_native_returns','native_cut_batch02','compound_followup','compound_cut_followup','selection_focus','native_reuse_and_focus','additional_native_reuse','pdf_complete_compound','seal_checkpoint_V']))
files=sorted(set(files));assert all('private' not in x.lower() for x in files)
seal=''.join(hashlib.sha256((R/x).read_bytes()).hexdigest()+'  '+x+'\n' for x in files)
(R/'EVIDENCE_SHA256SUMS_checkpoint_V').write_text(seal)
for line in seal.splitlines():h,n=line.split(maxsplit=1);assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h
mapping={src:rel for src,rel in json.loads((R/'publication_U.json').read_text())['files'].items() if rel!='QUALITY_GATE.json'}
mapping.update({x:'research/'+x for x in files});mapping['EVIDENCE_SHA256SUMS_checkpoint_V']='research/EVIDENCE_SHA256SUMS_checkpoint_V';mapping['CONTINUATION_HANDOFF.md']='research/CONTINUATION_HANDOFF.md'
shutil.copyfile(S/'QUALITY_GATE_checkpoint_V.json',S/'QUALITY_GATE_checkpoint_V_mirror.json');mapping['session_20261105/QUALITY_GATE_checkpoint_V_mirror.json']='QUALITY_GATE.json'
(R/'publication_V.json').write_text(json.dumps(dict(message='research(visual-forensics): V006 checkpoint V native compound corrections and provenance reuse audit; partial CT\n',files=mapping),indent=2)+'\n')
print('SEALED_LOCAL_V',len(files),'immutableVentries;',len(mapping),'text source mappings;includes unpublishedU;CTfalse;no remote publication claimed')
