"""Curate one now-contiguous native compound; not a global temporal pass."""
from pathlib import Path
import csv,json,hashlib,datetime
R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');S=R/'session_20261105'
ref='pdf_early_traversal_native_v1/OUT_pdf_early_traversal_native_v1.json';o=json.loads((R/ref).read_text());p=json.loads((S/'pdf_early_traversal_native_independent_return_audit_v1.json').read_text());a=json.loads((S/'pdf_compound_47frame_independent_coverage_audit_v1.json').read_text())
assert p['actual_native_fullframe_returns']==31 and hashlib.sha256((R/ref).read_bytes()).hexdigest()==p['saved_output_sha256']
assert a['accounted_distinct_native_frames']==47 and not a['missing_frames'];assert o['shot_cut_verdict']['coarse_full_replace_claim']=='REJECTED'
events=list(csv.DictReader((R/'integrated_v4/visual_event_ledger_v14.csv').open()));e=next(x for x in events if x['event_id']=='EP0054')
assert e['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET'
e.update(event_class='RETAINED_DOCUMENT_TRAVERSAL_THEN_GROUP_ENLARGEMENT_CROP_AND_ADDITIVE_HOST',verdict='RECLASSIFIED',shot_boundary_claim='NO',
 description='Contiguous native1596–1642 observes retained-viewer rapid uneven page-position updates, main-pane Table1 partial entry1622/all11rows1623, viewer/table enlargement1625, successive chrome crop exits1633/1636/1639, and retained-table host entry1642. No observable full-scene replacement within compound. Exact input/edit/crop mechanism, hidden content-preserving edits, zoom settle and wider motion onset unknown.',
 timing_precision='CONSECUTIVE_NATIVE_COMPOUND1596_1642_WITH_QUALIFIED_REUSES;NO_OBSERVED_WHOLE_SCENE_CUT',
 macro_review_ref='integrated_v4/document_zoom_track_v2.json',cut_adjudication_ref=ref+'#shot_cut_verdict',cut_adjudication_precision='47DISTINCT_NATIVE_FRAME_OBSERVATIONS;COARSE_SHOT_CLAIM_REJECTED',
 native_vs_firstpass_conflict='Original full-replacement/shotYES claim rejected in curated layer after native whole bounded construction; source raw remains immutable. Table comes into main pane1622, enlargement1625, host1642;these are not one hard cut.',review_scope='BOUNDED_CONTIGUOUS_NATIVE_COMPOUND;31NEW_TASK_READS_AND16QUALIFIED_REUSES')
dest=R/'integrated_v4/visual_event_ledger_v15.csv';assert not dest.exists()
with dest.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(events[0]));w.writeheader();w.writerows(events)
doc=json.loads((R/'integrated_v4/document_zoom_track_v1.json').read_text());doc.update(aggregate_native_window=[1596,1642],aggregate_native_accounting_ref='session_20261105/pdf_compound_47frame_independent_coverage_audit_v1.json',source_early_review=ref,phase_segments=o['phase_segments'],component_onsets_and_offsets=o['component_onsets_and_offsets_known_vs_unknown'],aggregate_shot_verdict=o['shot_cut_verdict'],entire_compound_native_certification='PASS_BOUNDED_VISIBLE_CONSTRUCTION_ONLY;NOT_SOURCE_EDITOR_MECHANISM_OR_GLOBAL_PASS',actual_listening_seconds=0,CT_SCAN_COMPLETE=False)
(R/'integrated_v4/document_zoom_track_v2.json').write_text(json.dumps(doc,indent=2)+'\n')
q=json.loads((S/'global_native_remaining_queue_v7.json').read_text());q.update(baseline_event_ledger='integrated_v4/visual_event_ledger_v15.csv',current_candidate_only_rows=712,ambiguous_shot_claims_remaining=0,new_compound_cut_uncertainties=[],candidate_only_items=[x for x in q['candidate_only_items'] if x['event_id']!='EP0054'],next_pending_native_batch='NONE_PREPARED_ACTIVE;resource-safe-stop then fresh ownership/resources;global712candidate timing rows/otherqualitygates;reusepriornativeindexfirst')
assert len(q['candidate_only_items'])==sum(x['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET' for x in events)==712
(S/'global_native_remaining_queue_v8.json').write_text(json.dumps(q,indent=2)+'\n')
stats=dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),event_ledger_version='v15',event_rows=948,candidate_only_timing_rows_remaining=712,partial_cut_onset_inventory=50,
           PDF_contiguous_native_compound=[1596,1642],PDF_native_distinct_observations=47,PDF_early_new_actual_native_returns=31,PDF_early_qualified_native_reuses=16,PDF_pending_paths=0,PDF_whole_scene_cut_claim='REJECTED_BOUNDED_CONSTRUCTION',
           PDF_main_table_partial_entry=1622,PDF_main_table_full11rows=1623,PDF_group_enlargement_first_visible_change=1625,PDF_chrome_crop_exits=[1633,1636,1639],PDF_host_entry=1642,PDF_settle='UNKNOWN',
           actual_listening_seconds=0,CT_SCAN_COMPLETE=False)
(S/'pdf_complete_compound_integration_v15_stats.json').write_text(json.dumps(stats,indent=2)+'\n')
print('V15:PDF47nativecompoundcuratedNOwhole-scenecut;712candidate-only/50partialcutonsets;948uniqueevents;CTfalse')
