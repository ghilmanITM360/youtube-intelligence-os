"""Curate the opening body/eyes/cards independently of shot and partition counts."""
from pathlib import Path
import csv
import json
import hashlib

R = Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
S = R / 'session_20261104'
ref = 'opening_macro_native_v1/OUT_opening_macro_native_v1.json'
review = json.loads((R / ref).read_text())
assert hashlib.sha256((R / ref).read_bytes()).hexdigest() == 'aee1d6b137238711c4df60f193758705ab4801ceef27b2c4218a8bccb2316add'
assert len(review['new_evidence_reads']) == 34 and not review['pending_new_image_paths']
assert json.loads((S / 'opening_macro_independent_return_audit_v1.json').read_text())['status'].startswith('PASS34')
assert json.loads((S / 'opening_independent_root_semantic_spot_QA_v1.json').read_text())['status'].startswith('PASS_BOUNDED')
geometry = json.loads((S / 'opening_source_geometry_measurements_v1.json').read_text())
objects = {x['id']: x for x in review['objects']}
assert [objects[k]['first_visible_frame_or_bracket']['frame'] for k in ['OPEN_BUILDING', 'OPEN_BUILDING_EYES', 'OPEN_CARD_NYT', 'OPEN_CARD_CONDUIT']] == [1, 12, 6, 32]

def read_csv(path):
    with path.open() as f:
        return list(csv.DictReader(f))

def write_csv(path, rows):
    assert not path.exists(), path
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

def write_json(path, value):
    assert not path.exists(), path
    path.write_text(json.dumps(value, indent=2) + '\n')

track = dict(source_review=ref, objects=review['objects'],
             global_camera=review['global_camera'],
             source_geometry='session_20261104/opening_source_geometry_measurements_v1.json',
             native_agent_views=34, independent_root_repeat_views=5,
             reused_prior_native_frames=[0, 1, 2],
             source_frame_scope=[0, 36],
             conflict='Original both-cards-drop claim is contradicted: Conduit card absent31/full32; no descending path observed. Building center also differs from old x.75 estimate.',
             source_layers='Unknown. Eyes are visibly absent11/present12; an independent source-project layer is not established.',
             lower_building_fully_visible=False, source_easing_preset='UNKNOWN',
             actual_listening_seconds=0, CT_SCAN_COMPLETE=False)
write_json(R / 'integrated_v4/opening_object_lifecycles_v1.json', track)
phases = [('BLANK', 0, 0), ('BODY_ENTRY', 1, 5), ('BODY_AND_PARTIAL_LEFT_CARD', 6, 11),
          ('BODY_HELD_EYES_VISIBLE_LEFT_CARD_PARTIAL', 12, 22),
          ('FULL_LEFT_CARD_STILL_MOVING', 23, 31), ('SECOND_CARD_POP_ALL_HELD', 32, 36)]
rows = [dict(phase_id=f'OPEN_PHASE{i:02}', track='BOUNDED_GRAPHIC_PHASE_NOT_SHOT',
             start_frame=a, end_frame=b, n_frames=b-a+1, start_pts=(a+1)/24,
             end_exclusive_pts=(b+2)/24, phase=name,
             underlying_composition='S0000' if a == 0 else 'S0001', source_review=ref,
             limit='Only source0–36; not global state/shot certification or a permanent hold after36')
        for i, (name, a, b) in enumerate(phases, 1)]
assert sum(x['n_frames'] for x in rows) == 37
write_csv(R / 'integrated_v4/opening_graphic_phases_v1.csv', rows)

events = read_csv(R / 'integrated_v4/visual_event_ledger_v8.csv')
for row in events:
    row['opening_lifecycle_ref'] = ''
    if row['event_id'] == 'EP0001':
        row.update(opening_lifecycle_ref='integrated_v4/opening_object_lifecycles_v1.json',
                   description='Building first visible1, last substantive upward movement12; base remains cropped. Eyes first12, absent11, then held. NYT card first sliver6, full23, last visible diagonal down/right movement32, held33–36. Conduit card absent31 and appears fully32, held through36; no descent observed for second card.',
                   visual_onset_verified_frame=1, observed_change_first_frame=1,
                   observed_change_last_frame=32, review_scope='CONSECUTIVE_NATIVE3_36_PLUS_REUSED_NATIVE0_1_2_AND_ROOT5_SPOTS',
                   timing_precision='BOUNDED_PER_OBJECT_NATIVE_ONSETS_AND_VISIBLE_HOLDS;NO_SOURCE_PRESET',
                   motion_object=json.dumps(review['objects']),
                   macro_review_ref=ref, bounds_role='ORIGINAL_CANDIDATE2_32_RETAINED;OBJECT_LIFECYCLES_SEPARATE',
                   native_vs_firstpass_conflict='Coarse two-card-drop claim contradicted by Conduit pop32; source building is centered and cropped, not oldx.75 estimate.')
assert len(events) == len({x['event_id'] for x in events}) == 948
write_csv(R / 'integrated_v4/visual_event_ledger_v9.csv', events)

motion = read_csv(R / 'production_v1/motion_camera_facial_index_PARTIAL_v4.csv')
for row in motion:
    row['opening_lifecycle_ref'] = ''
    if row['id'] == 'EP0001':
        row.update(opening_lifecycle_ref='integrated_v4/opening_object_lifecycles_v1.json',
                   motion_status='BOUNDED_CONSECUTIVE_NATIVE_PER_OBJECT_REVIEWED',
                   path='Body upward1–12; NYT diagonal down/right6–32; eyes appear12; Conduit appears fully32 without observed travel.',
                   easing='UNKNOWN_SOURCE_PRESET;BODY_VISIBLY_SLOWS;NYT_BROADLY_REGULAR_STEPPING',
                   duration_note='Distinct object windows, not one31frame motion: body1–12, leftcard6–32, secondcardappearance32; boundedhold through36.',
                   curated_motion_review=ref, curated_motion_object=json.dumps(review['objects']),
                   curated_observed_change='Native per-object timing supersedes coarse first-pass shared entrance.')
write_csv(R / 'production_v1/motion_camera_facial_index_PARTIAL_v5.csv', motion)

production = read_csv(R / 'production_v1/per_state_production_spec_DRAFT_v3.csv')
for row in production:
    row['native_geometry_review_ref'] = ''
    if row['state_id'] == 'S0001':
        row.update(source_objects='Centered Federal Reserve building, lower body cropped; two complete open oval eyes. Left tilted NYT card; upper-center/right tilted Conduit Street Blog card. Native36 threshold bboxes: building530,615,902,465; NYT75,236,674,219; Conduit632,63,684,178. Visible building bbox centerx~.511; oldx.75 estimate superseded.',
                   source_entry_exit='Body entry1–12; eye appearance12; first card enters6, full23, last change32; second card appears fully32. All observed objects held33–36; subsequent coin/card events outside this native scope.',
                   source_camera_motion='No common camera transform observed; building holds while left card continues moving. Bounded native0–36 only.',
                   source_evidence='34 consecutive new native frames3–36, reused actual native0/1/2, five independent root spot views; source color/layers/preset and hidden building base remain unknown.',
                   native_geometry_review_ref='session_20261104/opening_source_geometry_measurements_v1.json;'+ref,
                   curated_interval_note='Stable draft interval33–36 has bounded native geometry/anchor support; source transition phases belong separate opening track. Full production remains pending.')
write_csv(R / 'production_v1/per_state_production_spec_DRAFT_v4.csv', production)
write_json(S / 'opening_macro_integration_v9_stats.json',
           dict(event_rows=948, unique_event_ids=948, motion_rows=766,
                frame_partition='v5 unchanged', composition_groups=329,
                consecutive_new_native_source_frames=34, reused_source_frames=[0, 1, 2],
                independent_root_spot_repeat_returns=5, unique_source_frames_added_by_root_spots=0,
                source_window=[0, 36], object_lifecycles=4, graphic_phase_rows=6,
                source_building_bbox=geometry['components']['BUILDING_OUTLINE'],
                native_conflicts_curated=['Second card pop32 instead of shared drop path', 'Building bbox center~.511 instead of oldx.75'],
                firstpass_immutable=True, global_semantic_pass=False,
                actual_listening_seconds=0, CT_SCAN_COMPLETE=False))
print('Openingv9:4native object lifecycles/6phases;34agent+5rootrepeatviews;948uniqueevents;partitionv5 unchanged')
