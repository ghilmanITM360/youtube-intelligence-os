"""Seal bounded native-cut milestone U; exclude active batch02 output."""
from pathlib import Path
import csv
import hashlib
import json
import shutil

R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
S=R/'session_20261105'
assert not (R/'EVIDENCE_SHA256SUMS_checkpoint_U').exists()
for line in (R/'EVIDENCE_SHA256SUMS_checkpoint_T').read_text().splitlines():
    h,n=line.split(maxsplit=1)
    assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h,n
proof=json.loads((S/'native_cut_batch01_resume_independent_return_audit_v1.json').read_text())
assert proof['actual_native_fullframe_returns']==12 and not proof['pending_case_ids']
stats=json.loads((S/'native_cut_batch01_integration_v11_stats.json').read_text())
assert stats['global_candidate_only_timing_rows_remaining']==729
parts=list(csv.DictReader((R/'integrated_v4/frame_partition_v5.csv').open()))
counts=[0]*19862
for row in parts:
    for n in range(int(row['start']),int(row['end'])+1):counts[n]+=1
assert set(counts)=={1}
events=list(csv.DictReader((R/'integrated_v4/visual_event_ledger_v11.csv').open()))
assert len(events)==len({x['event_id'] for x in events})==948
assert sum(x['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET' for x in events)==729
coverage=json.loads((R/'session_20261104/coverage_checkpoint_T.json').read_text())
coverage.update(event_ledger_version='v11',partial_verified_cut_onsets=37,global_candidate_only_timing_rows_remaining=729,
                checkpoint_U_new_native_cut_source_returns=12,checkpoint_U_independent_root_native_repeat_displays=2,
                checkpoint_U_new_unique_native_source_frames=12,pending_new_batch_native_reads='ACTIVE_BATCH02_UNINTEGRATED_READ_ACTUAL_OUTPUT_BEFORE_COUNTING',
                pending_new_batch_paths='native_cut_batch02_v1/items.json;24prepared paths are not proof of viewing',
                checkpoint_U_review_scope='6nativeadjacentpaircutonsets;37partialinventory;no_whole_shot_duration_or_global_semantic_pass',
                actual_listening_seconds=0,CT_SCAN_COMPLETE=False)
(S/'coverage_checkpoint_U.json').write_text(json.dumps(coverage,indent=2)+'\n')
quality=json.loads((R/'session_20261104/QUALITY_GATE_checkpoint_T.json').read_text())
quality.update(status='VISUAL_ANALYSIS_PARTIAL_PARTITION_V5_EVENTS_V11_CHECKPOINT_U',event_ledger='research/integrated_v4/visual_event_ledger_v11.csv',
               coverage_ref='research/session_20261105/coverage_checkpoint_U.json',known_issues='research/session_20261105/KNOWN_ISSUES_LEDGER_v10.md',
               active_task='One bounded batch02 reviewer; inspect actual status/saved outputs before resuming',
               next_task='Validate batch02 saved output and actual successful native returns, integrate only supported rulings; then unresolved compound cuts/global729candidate-only rows and other motion/object/facial/production/reconstruction/hearing gates',
               checkpoint_U=stats,resource_policy='Fivehour95% ceiling includes validation/publication/release reserve; stop new expensive work near weekly95%; no paid usage or reset credits')
quality['gates']['full_semantic_event_timing']='PARTIAL;6NEW_NATIVE_CUT_ONSETS;37PARTIAL_VERIFIED_INVENTORY;729CANDIDATE_ONLY_ROWS_PLUS_OTHER_PARTIAL_GATES'
assert quality['CT_SCAN_COMPLETE'] is False
(S/'QUALITY_GATE_checkpoint_U.json').write_text(json.dumps(quality,indent=2)+'\n')
known='''# Current issues — checkpoint U

T history remains immutable in session_20261104/KNOWN_ISSUES_LEDGER_v9.md.

- RESOLVED_BOUNDED: six native adjacent cut onsets EP0005/EP0010/EP0028/EP0033/EP0034/EP0040 at103/186/721/1065/1087/1171. Twelve actual1920x1080 returned images independently audited for bytes/order/multiplicity; root independently repeated720/721 as one semantic spot, not a second complete six-case semantic pass. Before720 has two release-page images, superseding coarse singular-page wording; I-frame claims are not inferred from pixels. Raw first-pass and sealed zero-read OUTv1 preserved.
- Eventledgerv11 retains948uniqueIDs. Partial cut-onset inventory37 is not a shotcount;729candidate-only timing rows remain plus exact-onset-only/sampled motion and interior gates. Partitionv5 remains19862frames once/626intervals/329compositiongroups; numerical continuity alone is not semantic validation.
- Batch02 twelve cases/twenty-four native paths were prepared and initially usage-interrupted with0actual returns. A later bounded resume may be active or saved: inspect actual reviewer/output and audit returned images before counting or resuming; no duplicated reviewer. Compound EP0032/EP0046/EP0050/EP0054 may begin with movement before a later cut; do not mechanically assign candidate start as cut.
- Retained open gates: global native/100ms/semantic/object/facial floor; SUB032 microfeature; selection removal after8045; chart cursor precursor/final offset; biography slide offset. Prior opening/chart/table/ambiguous-cut/narration/prototype reviews must not be repeated.
- Narration199sampledASRrows/21UNDETERMINED/7potentialflags remains; ASR156 already done. Qualified actual source hearing0seconds; fresh capability discovery found no enabled qualified source-audio perception tool. ASR never counts as listening. No AV or CT completion.
- Production447-state DRAFTv4,27missing integrated specs,152extended spans remain. A27row receipt-retrieval packet is preparation only, not original-production review or gap closure. Prior75/37frame original tests remain bounded; full production/static-anchor/cold-start/reconstruction QA incomplete.
- Exact35roster remains35distinct IDs filtered solely to Casual Finance. Local file existence/queue metadata are selection evidence. Revalidate each source hash/current status before its analysis; other34platform identities remain unverified here. Media/HTML/PNGs remain LOCAL_ONLY, not remotely available because a hash was published.

0/35 certified;CT_SCAN_COMPLETE=false.
'''
(S/'KNOWN_ISSUES_LEDGER_v10.md').write_text(known)
handoff='''# Video006 checkpoint U — six native cut boundaries integrated

Source xtqbRt94TTw: /Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4. Fresh49993573bytes/SHA256030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66 match. Workspace /Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan; media remains LOCAL_ONLY. Existing exact35roster at /Users/ghilmankhan/YIOS-local-audits/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104/target_roster_v1.json live-revalidated:35distinct IDs and queue-channel set only Casual Finance, no Casual Economics. Source hashes/current completion must be revalidated per next video.

ParentT4d625184deb606b9c0585e63cafb9b80b62e9974 freshly authenticated remote/readback42PASS/T39sealsPASS. U is SEALED_ONLY until session_20261103/publication_receipt_U.json establishes actual normal push/readback. Full U SHA/readback and final lock state belong in session_20261105/POST_PUBLICATION_HANDOFF_U.md. CanonicalHEADf4dc5d14d6ad03c1edd92e48fac779e7a8555fc5/localresearchref2b10f104c1edf0562e2628d1dab1afba2546bd8e preserved. Authenticated open-PR API returned[]; no PR created/merged/closed. Established isolated private-index/commit-tree publication only; recheck live remote parent and scoped diff, never force push.

All10first-pass shards reused,new0/pending0;123gapreviews/3116frames and146merge-split rulings retained. Partitionv5 still19862once/626intervals/329compositiongroups, not shotcount. NEW eventledgerv11:6native-adjacent-cut onsets103/186/721/1065/1087/1171,37partialcutinventory,729candidate-onlytimings,948uniqueIDs. Twelve native actual returns independently byte/order/multiplicity/dimension audited; root2repeat displays720/721 certify one independent semantic spot, not a full second six-case pass. Before720two pages correct coarse singular-page wording; old raw/drafts/zero-readv1 immutable. Newv2rawOUTsha cf447363c3a391b53185117e63e5478314637911f71156c69163b1c052b9e3d0.

199sampledASRrows/21UNDETERMINED/7potentialflags retained; ASR156 already integrated, never repeat it. Actual source LISTENING0seconds, current tools expose no qualified hearing capability. Production447-stateDRAFTv4/27missing integrated specs/152extended spans remain open;27row receipt retrieval is preparation only. Prior original75/37frame tests, full narration/nativeQA/chart/opening/selection reviews preserved. No global semantic/motion/facial/production/cold-start/AV pass and no CT_SCAN_COMPLETE.0/35fullycertified.

EXACT NEXT: inspect /root/gap_review_03 and native_cut_batch02_v1/OUT_native_cut_batch02_v1.json. Batch02 is a distinct12case/24nativepath packet with initial interruption0actual returns independently audited; a bounded resume was dispatched after fresh27%primary/69%weekly. Count only saved output plus actual image-return audit; do not duplicate an active/finished reviewer. IDs EP0032/EP0046/EP0050/EP0054/EP0058/EP0059/EP0063/EP0069/EP0077/EP0082/EP0097/EP0101; read BRIEF/items. Compound windows may start with scroll/entry; leave cut onset unresolved unless actual native adjacency supports it. Then remaining729candidate-only timings plus globalsemantic/nativefloor, SUB032, removalafter8045, chartcursorprecursor/finaloffset, biographyoffset, original per-state/static-anchor/reconstruction/qualifiedhearing gates.

At U seal own v3token HELD: labelcodex-v006-native-resume-20261105, run01a1a2b1-c283-75f3-b64f-f45a440501b1, actualexecutableCodexPID1455/startTueNov3 21:28:19. Private receipt session_20261105/native_resume_owner_receipt_private.txt. Same start/run verified and heartbeat renewed after usage interruption; never recover from heartbeat alone. Release only this token at safe stop; record actual final lock status. Preserve Finance/Barely work, processes, locks, schedulers, checkout/index/stashes/untracked/ignored evidence. No new worktrees/clones/reset/clean/force/Graphify/raw-media Git transport.

Latest root fresh primary3% after natural reset,weekly79%,credits0,resetcredit1untouched; shared other work is increasing weekly usage.78GiBfree,memory49%free,swap8636.75/10240MiB; context UI percentage unavailable. Owner95%fivehour ceiling includes publication/release reserve; stop new expensive work nearweekly95%, no paid/resetcredits. Same existing follow-up corrected to2hour interval and near95%weeklypolicy; retain until35qualitycontracts pass or ownercancels. Continue autonomously without asking continue; fresh resources/ownership/status govern each resume.
'''
(S/'CONTINUATION_HANDOFF_checkpoint_U.md').write_text(handoff)
(R/'CONTINUATION_HANDOFF.md').write_text(handoff)
(R/'visual_ct_scan_report_v8.md').write_text('# Video006 checkpoint U report\n\n'+handoff.split('\n',1)[1])
files=['native_cut_batch01_v1/OUT_native_cut_batch01_resume_v2.json','native_cut_batch01_v1/items.json','native_cut_batch02_v1/items.json','native_cut_batch02_v1/BRIEF.md',
       'integrated_v4/visual_event_ledger_v11.csv','production_v1/shot_ledger_PARTIAL_v4.csv','production_v1/motion_camera_facial_index_PARTIAL_v6.csv',
       'session_20261104/POST_PUBLICATION_HANDOFF_T.md','visual_ct_scan_report_v8.md']
files+=['session_20261105/'+x for x in ['live_resume_discovery_v1.json','live_existing_integrated_structure_audit_v1.json','qualified_listening_capability_recheck_v1.json',
       'missing_production_spec_retrieval_packet_v1.json','native_cut_batch01_resume_independent_return_audit_v1.json','native_cut_batch01_root_semantic_spot_audit_v1.json',
       'native_cut_batch01_integration_v11_stats.json','native_cut_batch02_interruption_zero_return_audit_v1.json','global_native_remaining_queue_v4.json',
       'coverage_checkpoint_U.json','QUALITY_GATE_checkpoint_U.json','KNOWN_ISSUES_LEDGER_v10.md','CONTINUATION_HANDOFF_checkpoint_U.md']]
files+=['v2_scripts/'+x for x in ['prepare_native_cut_batch02_v1.py','audit_native_pair_returns_v1.py','integrate_native_cut_batch01_v11.py','seal_checkpoint_U.py']]
assert len(files)==len(set(files)) and all('private' not in x.lower() for x in files)
seal=''.join(hashlib.sha256((R/x).read_bytes()).hexdigest()+'  '+x+'\n' for x in sorted(files))
(R/'EVIDENCE_SHA256SUMS_checkpoint_U').write_text(seal)
for line in seal.splitlines():
    h,n=line.split(maxsplit=1);assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h
mapping={x:'research/'+x for x in files}
mapping['EVIDENCE_SHA256SUMS_checkpoint_U']='research/EVIDENCE_SHA256SUMS_checkpoint_U'
mapping['CONTINUATION_HANDOFF.md']='research/CONTINUATION_HANDOFF.md'
shutil.copyfile(S/'QUALITY_GATE_checkpoint_U.json',S/'QUALITY_GATE_checkpoint_U_mirror.json')
mapping['session_20261105/QUALITY_GATE_checkpoint_U_mirror.json']='QUALITY_GATE.json'
(R/'publication_U.json').write_text(json.dumps(dict(message='research(visual-forensics): V006 checkpoint U six native cut onsets and independent return audit; partial CT\n',files=mapping),indent=2)+'\n')
print('SEALED_U',len(files),'immutable entries',len(mapping),'text artifacts; NOT_CT_COMPLETE')
