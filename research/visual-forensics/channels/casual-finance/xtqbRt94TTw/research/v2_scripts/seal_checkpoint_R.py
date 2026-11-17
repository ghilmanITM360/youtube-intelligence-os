"""Publish the validated selection correction while chart review is separate/unintegrated."""
from pathlib import Path
import csv
import hashlib
import json
import shutil

R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');S=R/'session_20261104'
assert not (R/'EVIDENCE_SHA256SUMS_checkpoint_R').exists()
for line in (R/'EVIDENCE_SHA256SUMS_checkpoint_Q').read_text().splitlines():
    h,n=line.split(maxsplit=1);assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h,n
proof=json.loads((S/'selection_macro_independent_audit_v1.json').read_text());assert proof['bytehash_multiplicity']=='PASS' and proof['actual_new_native_ROI']==31
with (R/'integrated_v4/frame_partition_v4.csv').open() as f:parts=list(csv.DictReader(f))
counts=[0]*19862
for row in parts:
    for n in range(int(row['start']),int(row['end'])+1):counts[n]+=1
assert set(counts)=={1}
with (R/'integrated_v4/selection_graphic_variants_v1.csv').open() as f:variants=list(csv.DictReader(f))
assert len(variants)==7 and sum(int(x['n_frames']) for x in variants)==50
known=(S/'KNOWN_ISSUES_LEDGER_v6.md').read_text().replace('# V006 known issues v6 — checkpoint Q','# V006 known issues v7 — checkpoint R')
known+='''
## R native selection correction
- KI-9 RESOLVED_IN_CURATED_LAYER: raw EP0234 claimed second/later lines unchanged.31newnativeROIs show second-line selection8017–8025, followedby contractiontoone line8026 andendpointrefinement8027–28. Originalshard5JSON unchanged. Firstblueappearance8002confirmedagainst8001empty. A first-line-width jump is range-wrap logic,not measured cursorvelocity or camera motion.
- Selectionparentgesture is linked across EP0233/SUB101/EP0234/SUB103 in eventledgerv6. Seven bounded animation-phase intervals cover7996–8045 exactlyonce on a separate selection track within existingownerS0167/compositionS0165. These are not7newshots or a globalstate-count increase. New31nativeROI+1scaledcontext actualreturns byte/multiplicity audited,19priornativeROI receiptsreusedwithoutredisplay; all50firstline and31newsecondlinemaskpoints independentlyreproduced.
- The complete highlight-removal time beyond8045, physicalbutton timing andsourceeasing remainunknown. Chartmacroreview is a separate unintegratedoperation; inspect live reviewer and chart_macro_review_v1/OUT_chart_macro_review_v1.json before resuming. Do not duplicate active/finishedwork or infer everypreparedimagewasviewed.
'''
(S/'KNOWN_ISSUES_LEDGER_v7.md').write_text(known)
coverage=json.loads((S/'coverage_checkpoint_Q.json').read_text());coverage.update(event_ledger_version='v6;dominantpartitionv4unchanged',
    selection_macro_new_native_ROI_returns=31,selection_macro_new_scaled_context_returns=1,selection_macro_prior_native_ROI_reuses=19,
    selection_bounded_variant_phase_rows=7,selection_bounded_phase_window=[7996,8045],selection_first_blue_native_onset=8002,
    selection_two_line_interval=[8017,8025],selection_contract_to_one_line=8026,selection_removal_time='UNKNOWN_BEYOND8045',
    chart_macro='SEPARATE_UNINTEGRATED_OPERATION;readactualreviewer/outputstatus',actual_listening_seconds=0)
(S/'coverage_checkpoint_R.json').write_text(json.dumps(coverage,indent=2)+'\n')
quality=json.loads((S/'QUALITY_GATE_checkpoint_Q.json').read_text());quality.update(status='VISUAL_ANALYSIS_PARTIAL_PARTITION_V4_EVENTS_V6_CHECKPOINT_R',
    coverage_ref='research/session_20261104/coverage_checkpoint_R.json',known_issues='research/session_20261104/KNOWN_ISSUES_LEDGER_v7.md',
    event_ledger='research/integrated_v4/visual_event_ledger_v6.csv',active_task='Chartmacroreview separate;inspectactual live task/output before resuming',
    next_task='Validate actual chartmacro finished/partial output andpendingpaths; thennative exactboundaryframes,remainingsemantic/productionQA andqualifiedsourcehearing')
quality['gates']['full_semantic_event_timing']='PARTIAL;NATIVE_SELECTION_APPEARANCE_WRAP_CONTRACTION_VERIFIED;CHART_MACRO_UNINTEGRATED_GLOBAL_ONSET_FLOOR_OPEN'
quality['selection_macro']=json.loads((S/'selection_macro_integration_v6_stats.json').read_text());assert quality['CT_SCAN_COMPLETE'] is False
(S/'QUALITY_GATE_checkpoint_R.json').write_text(json.dumps(quality,indent=2)+'\n')
handoff='''# Video006 checkpoint R — native selection wrap corrected
Source xtqbRt94TTw SHA256030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66 unchanged at /Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4. Evidence workspace /Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan; mediaLOCAL_ONLY,notGit.
ParentQ8b30857c11f359d66dfe7d6cf6ae36b131a916b9. LocalHEADf4dc5d14d6ad03c1edd92e48fac779e7a8555fc5/localresearchref2b10f104c1edf0562e2628d1dab1afba2546bd8e preserved. PrivateGitindex/commit-tree normalpush only; recheck liveparent/scopeddiff. Rfullcommit/readbacks in session_20261103/publication_receipt_R.json andpostpublicationhandoff afterpush; sealalone isnotpublication. NoPRcreated/merged/closed; latestPRsnapshotQempty.
All10firstpass shards reused,new0/pending0;123gapreviews/3116frames/146merge-split rulings preserved. Dominantpartitionv4all19862framesonce,no numericgaps/overlaps/unresolvedowners;329compositiongroups arenotshots. Eventledgerv6 has948rows withparentgesture links andEP0234correction. Sevenboundedselectionphaseintervals7996–8045withinownerS0167/compositionS0165 are a separategraphictrack,not7newshots/dominantcompositions.
NEW:Natively verifiedfirstblueappearance8002(before8001empty),two-linewrap8017–8025,contractiontoone line8026,refinement8027–28,heldrange8029–36,endpointretraction8037withcursorchangeuntil8038. Nativeproof contradictsrawEP0234second/laterlinesunchanged;rawshard5preserved.31newnative1425x115ROI+1scaled960context actualreturns independentlybyte/multiplicityaudited;19previousnativeROIreceiptsreusedwithoutredisplay. All50firstline and31newsecondlinemaskpointsreproduced. Range widthjump isnotcursorpositionjump. Selectionremovalbeyond8045,sourcecurve,physicalbuttonandtruecolorunknown.
Narrationcrosswalkv4still199sampledASRrows reviewed,0unreviewed/usedsamplesoutsideprovisionalintervals,21UNDETERMINED/7potentialsource-ASRflags.16nativeQAcases/48nativefullframes and4motionobjects/40nativeROI+8scaledcontextfromQpreserved. ActualLISTENING0seconds;ASRneverhearing;noqualifiedsoundtool. Production447stateDRAFTv2andbounded75frameoriginaltestremainpartial;nofullproduction/coldstart/AVpass. NOT_CT_COMPLETE;35-video goalACTIVE/UNCOMPLETED.
EXACTNEXT: Inspectactual /root/gap_review_03 status and chart_macro_review_v1/OUT_chart_macro_review_v1.json. Thisnewcharttask has64requestednewimages(51nativefullframes,13nativecursorROIs),5priorSUB151nativeROIsreused; do notclaim64readunlessactualoutputs/returnsproveit. Lastreported41/64displayed at78%primary/28%weekly; reviewerstopnewreads83%,saveexactpendingpaths. Do notduplicateactive/finishedreviewer. Fullframes17784–17882every2frames83.333ms are bounded4.125sstrategy,notglobal100ms/one-frameprecision. ReuseG116up57first17875proof. Afteroutputaudit, supplyonlylistedadditionalexactboundaryframesandpendingrequests. Thenremainingglobalnative/cut/onsetfloor,SUB032microfeature,originalproduction/staticanchor/reconstruction andqualifiedhearinggates.
Writerlock atseal isthisroot's v3token,actualCodexPID1455; privateacquisitionreceipt session_20261104/macro_selection_owner_receipt_private.txt. ReleaseONLYthistokenatsafestop andrecordactualstatus. NoFinance/Barelyprocess/lock/scheduler/index/stash/untrackedevidence edits;read-onlyscopechecksfoundotherliveWhatIf/XKCDsessions,nocompetingCFwriter. NoGraphify/worktrees/clones/forcepush/sourceedits/paid/resettoolcalls. Freshresourcechecksrequired;primary95%ownerceilingincludesvalidation/publication/releasereserve,near95%weeklypolicy;noexpensiverunnearlimits. Samechat2hourlyfollowupreadsnewesthandoff/pointer;donotaskcontinuebetweenmilestones.
'''
(S/'CONTINUATION_HANDOFF_checkpoint_R.md').write_text(handoff);(R/'CONTINUATION_HANDOFF.md').write_text(handoff)
(R/'visual_ct_scan_report_v5.md').write_text('# Video006 checkpoint R report\n\n'+handoff.split('\n',1)[1])
files=[str(p.relative_to(R)) for p in (R/'selection_macro_review_v1').iterdir() if p.is_file() and p.suffix in {'.json','.md','.txt'}]
files+=['integrated_v4/visual_event_ledger_v6.csv','integrated_v4/selection_graphic_variants_v1.csv','production_v1/motion_camera_facial_index_PARTIAL_v3.csv']
files+=['session_20261104/'+x for x in ['selection_macro_independent_audit_v1.json','selection_macro_integration_v6_stats.json','macro_resume_live_evidence_v1.json','KNOWN_ISSUES_LEDGER_v7.md','coverage_checkpoint_R.json','QUALITY_GATE_checkpoint_R.json','CONTINUATION_HANDOFF_checkpoint_R.md','POST_PUBLICATION_HANDOFF_Q.md']]
files+=['v2_scripts/'+x for x in ['prepare_selection_macro_v1.py','prepare_chart_macro_v1.py','integrate_selection_macro_v6.py','seal_checkpoint_R.py']]+['visual_ct_scan_report_v5.md']
assert len(files)==len(set(files)) and all('private' not in x.lower() for x in files)
seal=''.join(hashlib.sha256((R/x).read_bytes()).hexdigest()+'  '+x+'\n' for x in sorted(files));(R/'EVIDENCE_SHA256SUMS_checkpoint_R').write_text(seal)
for line in seal.splitlines():
    h,n=line.split(maxsplit=1);assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h
mapping={x:'research/'+x for x in files};mapping['EVIDENCE_SHA256SUMS_checkpoint_R']='research/EVIDENCE_SHA256SUMS_checkpoint_R';mapping['CONTINUATION_HANDOFF.md']='research/CONTINUATION_HANDOFF.md'
shutil.copyfile(S/'QUALITY_GATE_checkpoint_R.json',S/'QUALITY_GATE_checkpoint_R_mirror.json');mapping['session_20261104/QUALITY_GATE_checkpoint_R_mirror.json']='QUALITY_GATE.json'
(R/'publication_R.json').write_text(json.dumps(dict(message='research(visual-forensics): V006 checkpoint R native selection wrap correction and7phase overlay; partial CT\n',files=mapping),indent=2)+'\n')
print('SealedR',len(files),'immutabletextentries;',len(mapping),'publicationartifacts;chartseparate/unintegrated;NOT_CT_COMPLETE')
