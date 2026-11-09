"""Curate bounded chart observations without replacing raw reviews or partition."""
from pathlib import Path
import csv
import collections
import hashlib
import json

R = Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
S = R / 'session_20261104'
base_ref = 'chart_macro_review_v1/OUT_chart_macro_review_v1.json'
sup_ref = 'chart_boundary_supplement_v1/OUT_chart_boundary_supplement_v1.json'
base = json.loads((R / base_ref).read_text())
sup = json.loads((R / sup_ref).read_text())
assert hashlib.sha256((R / base_ref).read_bytes()).hexdigest() == '080fe01a3442213fb1a03b7753f0ebcbc1adb273272f8b31c779f3f7b3e4f3f4'
assert hashlib.sha256((R / sup_ref).read_bytes()).hexdigest() == '62b3e783dc9850231584f9e16e088d7ab5a6816bfbbd22f391e7b3fa8fae11ed'
assert json.loads((S / 'chart_macro_independent_audit_v1.json').read_text())['actual_new_native_fullframes'] == 51
assert json.loads((S / 'chart_boundary_independent_return_audit_v1.json').read_text())['status'].startswith('PASS_9_')
assert json.loads((S / 'chart_boundary_source_decode_reproduction_v1.json').read_text())['reproduced_mask_points'] == 126
assert not base['pending_new_image_paths'] and not sup['pending_new_image_paths']
assert base['actual_listening_seconds'] == sup['actual_listening_seconds'] == 0
rulings = {x['id']: x for x in sup['rulings']}
exact = {k: v['exact_onset_or_change_frame_or_bracket'].get('frame') for k, v in rulings.items()}
assert [exact[f'CBS{i:02}'] for i in range(1, 8)] == [17766, 17784, 17784, 17791, 17823, 17853, 17879]

def write_json(path, value):
    text = json.dumps(value, indent=2) + '\n'
    if path.exists():
        assert path.read_text() == text, ('Existing artifact differs; preserve and investigate', path)
        return
    path.write_text(text)

def read_csv(path):
    with path.open() as f:
        return list(csv.DictReader(f))

def write_csv(path, rows):
    assert not path.exists(), path
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

track = dict(status='BOUNDED_NATIVE_CHART_EVENT_TRACK_NOT_SHOTS',
             base_review=base_ref, supplement=sup_ref,
             events=base['events'], superseding_native_rulings=sup['rulings'],
             distinct_visual_states_observed=base['distinct_visual_states'],
             motion_objects=base['motion_object'], static_anchors=base['static_anchors'],
             source_text_panel=base['source_text_panel'],
             measured_title_trajectory='session_20261104/chart_title_mask_trajectory_v1.json',
             motion_offset_status=sup['motion_offset_status'],
             limitations=['Base brackets are retained as historical observations; CBS exact rulings supersede corresponding onset/completion brackets.',
                          'Content hold is not motion hold. Cursor appearance and exact final cursor/card motion offset remain unverified.',
                          '51 original fullframes every2frames in17784–17882 and9 targeted native fullframes are bounded coverage, not a global100ms or every-frame pass.',
                          'Six meaningful observed graphic states are not six new shots or dominant compositions.'],
             actual_new_native_fullframes=60, actual_new_native_ROIs=13,
             prior_native_ROI_reuses=5, actual_listening_seconds=0, CT_SCAN_COMPLETE=False)
write_json(R / 'integrated_v4/chart_macro_event_track_v1.json', track)

events = read_csv(R / 'integrated_v4/visual_event_ledger_v6.csv')
assert len(events) == 948
duplicates = {k: n for k, n in collections.Counter(x['event_id'] for x in events).items() if n > 1}
assert duplicates == {'G121_TARGETED': 2}, duplicates
for row in events:
    row['legacy_event_id'] = row['event_id']
    if row['event_id'] == 'G121_TARGETED':
        row['event_id'] += '_' + row['source_start_frame'] + '_' + row['source_end_frame']
    row['chart_macro_track_ref'] = ''
    if row['event_id'] not in {'EP0539', 'SUB151', 'EP0540'}:
        continue
    row['chart_macro_track_ref'] = 'integrated_v4/chart_macro_event_track_v1.json'
    row['pre_macro_record_ref'] = row['source_ref']
    row['macro_review_ref'] = base_ref + ';' + sup_ref
    row['parent_gesture_id'] = 'CHART_CURSOR_TITLE_TOOLTIP_17766_17890'
    if row['event_id'] == 'EP0539':
        row.update(visual_onset_verified_frame=17766, review_scope='NATIVE_FULLFRAME_ADJACENT17765_17766',
                   timing_precision='EXACT_NATIVE_SHOT_ONSET;NOT_WHOLE_SHOT_DURATION')
    elif row['event_id'] == 'SUB151':
        row.update(description='Cursor precursor remains unidentifiable before the clear arrow17780; rightward motion17780–17783 is reused nativeROI evidence. Fullframe17783 confirms cursor precedes first tooltip17784. Pure cursor appearance and full motion offset unverified.',
                   review_scope='13NEW_NATIVE_ROI_AND5PRIOR_ROI_PLUS_FULLFRAME_MACRO',
                   bounds_role='CANDIDATE_FRAGMENT_OF_LONGER_CURSOR_TRAVERSAL;APPEARANCE_OFFSET_UNKNOWN')
    else:
        row.update(description='Fixed chart/page anchors. First yellow title stroke and first tooltip17784; tooltip changes to left side17791. Title reaches full extent17823. May2026/$3.99b content first17853 while card still moves; Jun2026/$4.36b first17879. Red up57% onset17875 reused. Late content holds through sampled17890; exact cursor/card motion offset unknown.',
                   event_class='TITLE_HIGHLIGHT_AND_CURSOR_TOOLTIP_MACRO',
                   visual_onset_verified_frame=17784,
                   review_scope='51BASE_NATIVE_FULLFRAMES_9TARGETED_NATIVE_FULLFRAMES_PLUS13EARLY_ROI',
                   timing_precision='EXACT_SELECTED_NATIVE_BOUNDARIES;OTHER_TOOLTIP_UPDATES_SAMPLED;FINAL_MOTION_OFFSET_UNKNOWN',
                   native_vs_firstpass_conflict='Original final-tooltip lock wording conflated content with physical card/cursor hold; curated track distinguishes them. Rawshard9 remains immutable.',
                   motion_object=json.dumps(base['motion_object']),
                   bounds_role='ORIGINAL17784_17882CANDIDATE_RETAINED;MACRO_OBSERVED_SAMPLES_THROUGH17890')
assert len({x['event_id'] for x in events}) == 948
write_csv(R / 'integrated_v4/visual_event_ledger_v7.csv', events)

motion = read_csv(R / 'production_v1/motion_camera_facial_index_PARTIAL_v3.csv')
for row in motion:
    row['chart_macro_track_ref'] = ''
    if row['id'] in {'EP0539', 'SUB151', 'EP0540'}:
        row['chart_macro_track_ref'] = 'integrated_v4/chart_macro_event_track_v1.json'
    if row['id'] == 'EP0540':
        row.update(motion_status='BOUNDED_NATIVE_MACRO_REVIEWED;FINAL_MOTION_OFFSET_UNKNOWN',
                   easing='UNKNOWN_SOURCE_PRESET;TITLE_MASK_APPROX_CONSTANT_RATE_IN_DECLARED_PIPELINE',
                   curated_motion_review=base_ref + ';' + sup_ref,
                   curated_motion_object=json.dumps(base['motion_object']),
                   curated_observed_change='Exact:stroke/tooltip17784,side17791,titlefull17823,May17853,June17879; red17875reused; contenthold not cursor/card motionhold.')
write_csv(R / 'production_v1/motion_camera_facial_index_PARTIAL_v4.csv', motion)

shots = read_csv(R / 'production_v1/shot_ledger_PARTIAL_v1.csv')
assert not any(x['start_frame'] == '17766' for x in shots)
shots.append(dict(video_id='xtqbRt94TTw', shot_id='ONSET_17766', start_frame=17766,
                  start_pts_seconds=17767 / 24, end_frame='UNVERIFIED', end_pts_seconds='UNVERIFIED',
                  transition='SHOT_CUT', verification='native adjacent17765new/17766previous independently audited byte returns; onset only',
                  source_ref=sup_ref + '#CBS01', description=rulings['CBS01']['description'],
                  limitations='Partial cut inventory; no whole-video count or duration certification.'))
shots.sort(key=lambda x: int(x['start_frame']))
write_csv(R / 'production_v1/shot_ledger_PARTIAL_v2.csv', shots)

counts = [0] * 19862
for row in read_csv(R / 'integrated_v4/frame_partition_v4.csv'):
    for frame in range(int(row['start']), int(row['end']) + 1):
        counts[frame] += 1
assert set(counts) == {1}
write_json(S / 'chart_macro_integration_v7_stats.json',
           dict(event_rows=len(events), motion_index_rows=len(motion), partial_cut_onset_rows=len(shots),
                new_native_fullframes=60, new_native_ROIs=13, prior_native_ROI_reuses=5,
                exact_boundary_rulings=7, unique_resolved_source_boundary_frames=6,
                legacy_duplicate_event_id='G121_TARGETED',
                unique_curated_event_ids=948, legacy_event_labels_preserved=True,
                frame_partition_unchanged=True, frames_once=19862,
                candidate_windows_preserved=True, global_semantic_pass=False,
                final_cursor_card_motion_offset='UNRESOLVED', source_easing_preset='UNKNOWN',
                actual_listening_seconds=0, CT_SCAN_COMPLETE=False))
print('Chartv7:948events/766motionrows/25partialcutonsets;73newnativeactualreturns;19862framesonce;NOT_CT_COMPLETE')
