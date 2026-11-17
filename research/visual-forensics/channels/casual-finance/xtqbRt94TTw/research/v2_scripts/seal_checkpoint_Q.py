"""Seal native followups with explicit motion-bound, color and audio limitations."""
from pathlib import Path
import csv
import hashlib
import json
import shutil

R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');S=R/'session_20261104'
assert not (R/'EVIDENCE_SHA256SUMS_checkpoint_Q').exists()
for label in ['O','P']:
    for line in (R/f'EVIDENCE_SHA256SUMS_checkpoint_{label}').read_text().splitlines():
        expected,name=line.split(maxsplit=1);assert hashlib.sha256((R/name).read_bytes()).hexdigest()==expected,(label,name)
stats=json.loads((R/'production_v1/narration_visual_alignment_stats_v4.json').read_text())
motion=json.loads((S/'motion_integration_v5_stats.json').read_text())
assert stats['sampled_relation_rows_reviewed']==199 and stats['pending_unreviewed']==stats['current_used_sample_locations_outside_ASR_interval']==0
assert len(stats['undetermined_ids'])==21 and len(stats['potential_mismatch_ids'])==7 and motion['normalized_motion_objects_missing']==0
partition=list(csv.DictReader((R/'integrated_v4/frame_partition_v4.csv').open()));counts=[0]*19862
for row in partition:
    for n in range(int(row['start']),int(row['end'])+1):counts[n]+=1
assert set(counts)=={1}
proof={'O_and_P_immutable_seals':'PASS','partition_frames':19862,'missing':0,'overlap':0,'event_rows':motion['event_rows'],
       'current_crosswalk_sampled_rows':199,'source_aligned_native_followups':16,'outside_interval_used_samples':0,
       'semantic_undetermined':21,'potential_source_ASR_flags':7,'normalized_motion_objects_missing':0,'raw_firstpass_nulls_preserved':4,
       'native_ROI_actual_returns':40,'native_fullframe_actual_returns':48,'scaled_motion_context_returns':8,
       'native_derivative_seek_integrity':'88/88pixelidentical to full nonseeking same-pipeline decode','actual_listening_seconds':0,'CT_SCAN_COMPLETE':False}
(S/'checkpoint_Q_validation_v1.json').write_text(json.dumps(proof,indent=2)+'\n')
known=(S/'KNOWN_ISSUES_LEDGER_v5.md').read_text().replace('# V006 known issues v5 — checkpoint P','# V006 known issues v6 — checkpoint Q')
known+='''
## Q superseding rulings (earlier entries retain their checkpoint-P history)
- Eleven outside-provisional-ASR sample-location cases now have three actual native fullframes each strictly inside their intervals. All199current crosswalk rows have used source samples inside provisional intervals. This certifies sample geometry only, not word/audio timing.
- Native16case QA leaves21UNDETERMINED and7POTENTIAL_MISMATCH across199rows. New flags152(DEBT/dead) and171(0.15/1500s) are source-vs-unheard-machine-ASR issues, not proved creator or financial errors.55 may be rounding;125/126wording,178monthly/annual constant-dollar basis and185cash-flow/sales denominator need qualified source hearing/context.136/162fragments remain unresolved despite corrected sample locations.
- Four missing motion objects have curated supplements in motion_camera_facial_index_PARTIAL_v2.csv; raw first-pass nulls remain immutable.40native1:1ROI and8scaledcontext actual image-return hashes/multiplicity and36adjacent local change measurements were independently checked.
- SUB103 substantive cursor/selection-edge event8034–8038 andSUB104 cursor path8049–8057 extend beyond old candidate ends8037/8055. Eventledgerv5 records these changes, retaining original candidate bounds separately. SUB101 selection growth already active before8003 andcontinues8008; SUB151 cursor moves17780–17783 but pure appearance and full offsets remain unknown. EasingUNKNOWN for allfour. Do not convert these into shots.
- Four OpenCV random-seek warnings triggered independent checks. All88new native derivatives exactly match a full nonseeking same-decoder source scan(18674frames). A separate systemFFmpeg RGB conversion differs; precise color-conversion cause remains unestablished, not proof of frame corruption. Do not mix RGBthreshold/hex values across pipelines.
- Remaining executable source work: macro selection lifecycle EP0233/SUB101/EP0234 andchart-tooltip lifecycle SUB151/EP0540, remainingglobal native/cut/onset floor, SUB032semantic uncertainty, original per-state production/static-anchor/reconstruction QA. Actual full-source hearing remains0seconds andBLOCKED without a qualified listener/tool. NoCT/fullAVaward.
'''
(S/'KNOWN_ISSUES_LEDGER_v6.md').write_text(known)
coverage=json.loads((S/'coverage_checkpoint_P.json').read_text())
coverage.update(narration_reviewed=199,narration_pending=0,narration_new_image_returns=404,narration_scaled_return_instances=356,narration_native_fullframe_return_instances=48,
                motion_review_native_ROI_return_instances=40,motion_review_scaled_context_return_instances=8,
                narration_visual_semantic_review='199SAMPLED_ROWS;16NATIVE_SOURCE_ALIGNED_FOLLOWUPS;21UNDETERMINED;7POTENTIAL_MISMATCH;NOHEARING',
                narration_outside_interval_followup_ids=[],current_used_samples_outside_provisional_ASR_interval=0,
                missing_confirmed_motion_objects=[],raw_firstpass_motion_nulls_preserved=['SUB101','SUB103','SUB104','SUB151'],
                event_ledger_version='v5; composition/frame partition remainsv4',semantic_certification=False,
                macro_bounds_still_unknown=['SUB101','SUB151'],actual_listening_seconds=0,
                decoder_warning_disposition='88/88same-pipeline sequential pixel identity; cross-pipeline RGBconversion ambiguity recorded')
(S/'coverage_checkpoint_Q.json').write_text(json.dumps(coverage,indent=2)+'\n')
quality=json.loads((S/'QUALITY_GATE_checkpoint_P.json').read_text())
quality.update(status='VISUAL_ANALYSIS_PARTIAL_INTEGRATED_V4_EVENTS_V5_CHECKPOINT_Q',CT_SCAN_COMPLETE=False,
               coverage_ref='research/session_20261104/coverage_checkpoint_Q.json',known_issues='research/session_20261104/KNOWN_ISSUES_LEDGER_v6.md',
               event_ledger='research/integrated_v4/visual_event_ledger_v5.csv',narration_review=stats,
               active_task='NONE_REVIEWERS_FINISHED;root sealing/publication',
               next_task='Native macro lifecycles EP0233/SUB101/EP0234 andSUB151/EP0540;remainingsemantic/nativecut/onset andoriginalproductionQA; qualifiedfullsourcehearing required')
quality['gates'].update(narration_visual_semantics='199SAMPLED_ROWS_REVIEWED;0OUTSIDE_INTERVAL_SAMPLES;PARTIAL21UNDETERMINED_7POTENTIAL_MISMATCH_ASR_ONLY',
                        full_required_motion_field_schema='FOUR_CURATED_SUPPLEMENTS_PRESENT;RAW_FIRSTPASS4NULLS_PRESERVED;NOT_GLOBAL_NATIVE_MOTION_PASS',
                        full_semantic_event_timing='PARTIAL;4NATIVE_ROI_SUPPLEMENTS_WITH2REFINEDBOUNDS;MACRO_BOUNDS_SUB101_SUB151_AND_GLOBAL_ONSET_FLOOR_OPEN')
quality['motion_supplements']=motion
(S/'QUALITY_GATE_checkpoint_Q.json').write_text(json.dumps(quality,indent=2)+'\n')
handoff='''# Video006 checkpoint Q — native followups integrated, CT still partial
Source xtqbRt94TTw, SHA256030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66. Original unchanged at /Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4. Workspace /Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan; all media LOCAL_ONLY.
Parent P578913ca5d1cceb92aadddd8f7a946a2daaa9ce0; localHEADf4dc5d14d6ad03c1edd92e48fac779e7a8555fc5/localresearchref2b10f104c1edf0562e2628d1dab1afba2546bd8e unchanged. Private-index/commit-tree normal publication only. Authenticated PRlist empty atP; no PR created/merged/closed. QfullSHA/readback in session_20261103/publication_receipt_Q.json and postpublicationQhandoff afterpush; a seal alone is not publication.
Firstpass10/10 reused,new0,pending0. Frame/composition partitionv4 still19862frames exactlyonce;0numeric gaps/overlaps/unresolvedowners,123gap and146merge/split reviews preserved;329compositionintervals are not a shotcount. Eventledgerv5 has948rows, separates originalcandidatebounds from newnativeobservations.
Narrationvisual crosswalkv4:199/199sampled ASR-qualified rows reviewed,0unreviewed,21UNDETERMINED/7POTENTIAL_MISMATCH.16targeted cases used48actual nativefullframes; all11previous outside-interval sample cases corrected, andall199currentusedsamples lie inside their provisionalASRintervals. This is sample-location proof, not audio/wordtiming or financialtruth. Root2+part0356scaledreturnaudit preserved. ActualLISTENING0seconds; no qualifiedhearingtool discovered. ASR820.52s union/final6.91suntranscribed do not mean verifiedspeech/silence.
Motion:4/4curatedobjects integrated,40actual native1:1ROI+8scaledcontext imagebytes/multiplicity audited; adjacentpixelmetrics independently reproduced. SUB103change8034–8038 andSUB104change8049–8057 extend beyond oldcandidateends. SUB101alreadyactivebefore8003/stillgrowing8008;SUB151rightwardmotion17780–17783confirmed butpureappearance/fullmotionboundsunknown. All easingUNKNOWN; raw4nullmotionobjects andoriginaldescriptions preserved. Productiondraftv2S0000referencefixedf36→f0,all447locatorsinrange; originality/static-anchor/perstatemotion/wholevideoreconstruction QA stillopen. Boundedoriginal75frame test is notwholevideopass.
Decodewarning audit:88/88preparednative derivatives pixel-identical to full nonseeking sameOpenCVsource decode18674frames. No derivative/source replacement. Separate systemFFmpeg RGBconversion differs; exactconversioncauseunestablished. Native means declared spatialresolution within the named decodepipeline; neverclaim codedYUV identity ormixRGB/hex thresholds acrosspipelines.
EXACT NEXT afterfreshresource/ownershipchecks: inspectallfinishedoutputs and do notrerun33narration/16QA/4motion tasks. Native macro-lifecycle followup forEP0233(f8002selectionstart)/SUB101/EP0234(f8009–8026selectiongrowth), andSUB151/EP0540(f17784–17882chartcursor/tooltips/highlight). Useboundednativeframes aroundactual first/lastchanges; preserve unknowns andrawcandidate windows. Then remainingglobal semantic/nativecut/onsetfloor,SUB032microfeature andoriginal per-state production/static-anchor/reconstruction requirements; actualqualifiedsourcehearing required beforeCT/fullAV. Continueotherexecutablegates;35selectedvideos remaingoal,nonecertifiedfullCTbythiscampaign.
35roster/sourcebaseline recoveredunder campaign_35_v1; hashes proveidentity/readiness,notfullanalysisorremote mediaavailability. Current35targetLATEST_PROGRESS pointer is local, checknewerhandoffs/remote beforeuse. Source/output/noGraphify andnoFinance/Barelywork/index/stash/untracked/process/lock/scheduler mutation policies unchanged.
Resources atlatestreviewer46%five-hour/23%weekly,credits0,one resetcredit observed; no reset/paidtool invoked here. Refreshbeforework. Allreviewersfinished. Ownv3lockHELDatseal(actualCodexPID1455); releaseONLYsession_20261104/owner_receipt_private.txt token atstop andrecordactualstatusafterpublication.2hourheartbeat retainedforresumption,notclaimofunattendedcompletion.
'''
(S/'CONTINUATION_HANDOFF_checkpoint_Q.md').write_text(handoff)
(R/'CONTINUATION_HANDOFF.md').write_text(handoff)
(R/'visual_ct_scan_report_v4.md').write_text('# Video006 checkpoint Q visual-forensics report\n\n'+handoff.split('\n',1)[1])
files=[]
for name in ['motion_missing_fields_review_v1','narration_source_aligned_QA_v1']:
    files += [str(p.relative_to(R)) for p in (R/name).iterdir() if p.is_file() and (p.suffix in {'.json','.md','.txt'} or p.name.startswith('SHA256SUMS'))]
files+=['production_v1/'+x for x in ['motion_camera_facial_index_PARTIAL_v2.csv','narration_visual_alignment_v4.csv','narration_visual_alignment_stats_v4.json']]
files+=['integrated_v4/visual_event_ledger_v5.csv']
files+=['session_20261104/'+x for x in ['motion_missing_fields_independent_audit_v1.json','motion_integration_v5_stats.json','motion_index_column_provenance_check_v1.json',
        'sequential_decoder_pixel_identity_audit_v1.json','sequential_same_decoder_seek_integrity_audit_v1.json','decoder_seek_warning_disposition_v1.json','sequential_ffmpeg_pixel_audit_stderr_v1.txt',
        'source_aligned_QA_independent_validation_v1.json','checkpoint_Q_validation_v1.json','KNOWN_ISSUES_LEDGER_v6.md','coverage_checkpoint_Q.json','QUALITY_GATE_checkpoint_Q.json','CONTINUATION_HANDOFF_checkpoint_Q.md','POST_PUBLICATION_HANDOFF_P.md']]
files+=['v2_scripts/'+x for x in ['integrate_motion_missing_fields_v5.py','integrate_source_aligned_QA_v4.py','seal_checkpoint_Q.py']]
files+=['visual_ct_scan_report_v4.md']
assert len(files)==len(set(files)) and all('private' not in x.lower() for x in files)
seal=''.join(hashlib.sha256((R/x).read_bytes()).hexdigest()+'  '+x+'\n' for x in sorted(files))
(R/'EVIDENCE_SHA256SUMS_checkpoint_Q').write_text(seal)
for line in seal.splitlines():
    expected,name=line.split(maxsplit=1);assert hashlib.sha256((R/name).read_bytes()).hexdigest()==expected
mapping={x:'research/'+x for x in files};mapping['EVIDENCE_SHA256SUMS_checkpoint_Q']='research/EVIDENCE_SHA256SUMS_checkpoint_Q';mapping['CONTINUATION_HANDOFF.md']='research/CONTINUATION_HANDOFF.md'
shutil.copyfile(S/'QUALITY_GATE_checkpoint_Q.json',S/'QUALITY_GATE_checkpoint_Q_mirror.json');mapping['session_20261104/QUALITY_GATE_checkpoint_Q_mirror.json']='QUALITY_GATE.json'
(R/'publication_Q.json').write_text(json.dumps(dict(message='research(visual-forensics): V006 checkpoint Q native motion and16source-aligned QA; partial CT with honest audio/bounds limits\n',files=mapping),indent=2)+'\n')
print('Sealed Q:',len(files),'immutabletext entries;',len(mapping),'publication artifacts; CT_SCAN_COMPLETE false')
