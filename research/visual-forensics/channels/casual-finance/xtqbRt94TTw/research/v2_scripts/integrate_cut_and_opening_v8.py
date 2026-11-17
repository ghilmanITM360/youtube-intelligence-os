"""Versioned cut taxonomy and the independently witnessed first-frame correction."""
from pathlib import Path
import csv
import itertools
import json
import hashlib

R = Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
S = R / 'session_20261104'
ref = 'ambiguous_cut_review_v1/OUT_ambiguous_cut_review_v1.json'
review = json.loads((R / ref).read_text())
assert hashlib.sha256((R / ref).read_bytes()).hexdigest() == '8dd00e1b4416be179ccc14ca256f840d258a086786b105163ce2b33a143e23f6'
assert len(review['items']) == 14 and len(review['new_evidence_reads']) == 18
assert json.loads((S / 'ambiguous_cut_independent_return_audit_v1.json').read_text())['status'].startswith('PASS18')
opening = json.loads((S / 'opening_frame0_1_reused_native_audit_v1.json').read_text())
assert opening['status'] == 'PASS_PRIOR_ACTUAL_NATIVE_RETURN_REUSE'
bio_ref = 'biography_entry_boundary_v1/OUT_biography_entry_boundary_v1.json'
bio = json.loads((R / bio_ref).read_text())
assert json.loads((S / 'biography_entry_independent_return_audit_v1.json').read_text())['status'].startswith('PASS3')
assert bio['exact_onset_or_bracket']['frame'] == 750

def read_csv(path):
    with path.open() as f:
        return list(csv.DictReader(f))

def write_csv(path, rows):
    assert not path.exists(), path
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

def write_json(path, data):
    assert not path.exists(), path
    path.write_text(json.dumps(data, indent=2) + '\n')

parts = read_csv(R / 'integrated_v4/frame_partition_v4.csv')
assert parts[0]['state_id'] == 'S0000' and parts[0]['start'] == '0' and parts[0]['end'] == '1'
first = parts[0]
first.update(end=0, n_frames=1, end_exclusive_pts=2 / 24,
             semantic_status='REUSED_NATIVE0_BLANK_ONLY;OLD0_1_BLANK_CLAIM_SUPERSEDED',
             boundary_precision='EXACT_NATIVE_ENDPOINT_AND_NATIVE1_ROOF_WITNESS',
             source_ref='session_20261104/opening_frame0_1_reused_native_audit_v1.json',
             description='Only sourceframe0 is blank. Roof tip already visible at1; original draft and prior partitions preserved.')
entry = dict(first)
entry.update(interval_id='OPENING_F00001', state_id='S0001', start=1, end=1,
             origin='REUSED_NATIVE_OBSERVATION_CORRECTION', semantic_status='OBSERVED_NATIVE_ROOF_ENTRY',
             description='Tiny black roof tip already visible at bottom edge at1; farther risen at2. First element enters before original candidate2.',
             n_frames=1, start_pts=2 / 24, end_exclusive_pts=3 / 24, composition_group='S0001')
parts.insert(1, entry)
counts = [0] * 19862
for row in parts:
    for n in range(int(row['start']), int(row['end']) + 1):
        counts[n] += 1
assert len(parts) == 626 and set(counts) == {1}
write_csv(R / 'integrated_v4/frame_partition_v5.csv', parts)
compositions = []
for group, segment in itertools.groupby(parts, key=lambda x: x['composition_group']):
    segment = list(segment)
    a, b = int(segment[0]['start']), int(segment[-1]['end'])
    compositions.append(dict(composition_group=group, start=a, end=b,
                             state_ids=';'.join(x['state_id'] for x in segment),
                             interval_ids=';'.join(x['interval_id'] for x in segment),
                             n_frames=b - a + 1, start_pts=(a + 1) / 24, end_exclusive_pts=(b + 2) / 24))
assert len(compositions) == 329 and sum(x['n_frames'] for x in compositions) == 19862
write_csv(R / 'integrated_v4/composition_intervals_v5.csv', compositions)

events = read_csv(R / 'integrated_v4/visual_event_ledger_v7.csv')
rulings = {x['id']: x for x in review['items']}
assert len(rulings) == 14
for row in events:
    row.update(cut_adjudication_ref='', pre_ambiguous_shot_claim='', cut_adjudication_precision='')
    ruling = rulings.get(row['event_id'])
    if ruling is None:
        continue
    assert row['shot_boundary_claim'] == 'AMBIGUOUS'
    row.update(pre_ambiguous_shot_claim='AMBIGUOUS', shot_boundary_claim=ruling['shot_boundary'],
               cut_adjudication_ref=ref + '#' + row['event_id'],
               cut_adjudication_precision=json.dumps(ruling['observed_onset_or_bracket']),
               event_class=ruling['event_type'])
    if len(ruling['evidence_paths']) == 2 and not ruling['reused_review_ref']:
        row.update(visual_onset_verified_frame=row['source_start_frame'],
                   review_scope='NATIVE_ADJACENT_CUT_VS_INTRASHOT_ADJUDICATION',
                   timing_precision='EXACT_NATIVE_VISIBLE_DISCONTINUITY;NOT_FULL_SUBSEQUENT_MOTION')
    if row['event_id'] == 'EP0001':
        row.update(visual_onset_verified_frame=1, observed_change_first_frame=1,
                   review_scope='REUSED_ACTUAL_NATIVE0_BLANK_AND_NATIVE1_ROOF_PLUS_G001',
                   timing_precision='EXACT_FIRST_ELEMENT1;OTHER_ELEMENT_TIMES_SAMPLED',
                   bounds_role='ORIGINAL_CANDIDATE2_32_RETAINED;FIRST_VISIBLE_ELEMENT1',
                   description=ruling['description'] + ' Root separately audited actual native0blank/native1roof returns; first entry resolved at1.')
    if row['event_id'] == 'EP0029':
        row.update(visual_onset_verified_frame=749,
                   macro_review_ref=bio_ref,
                   review_scope='REUSED_NATIVE_POSE749_PLUS3NEW_NATIVE_BIO_ENTRY750',
                   timing_precision='SELECTED_NATIVE_ONSETS749_AND750;FULL_SLIDE_OFFSET_UNKNOWN',
                   cut_adjudication_precision=json.dumps(dict(pose_laptop_substitution=749, biography_first_visible=750, slide_offset='UNKNOWN')),
                   description=bio['description'])
assert len(events) == len({x['event_id'] for x in events}) == 948
assert not any(x['shot_boundary_claim'] == 'AMBIGUOUS' for x in events)
write_csv(R / 'integrated_v4/visual_event_ledger_v8.csv', events)

shots = read_csv(R / 'production_v1/shot_ledger_PARTIAL_v2.csv')
lookup = {x['event_id']: x for x in events}
for key, ruling in rulings.items():
    if ruling['shot_boundary'] != 'YES':
        continue
    n = int(lookup[key]['source_start_frame'])
    assert not any(int(x['start_frame']) == n for x in shots)
    shots.append(dict(video_id='xtqbRt94TTw', shot_id=f'ONSET_{n}', start_frame=n,
                      start_pts_seconds=(n + 1) / 24, end_frame='UNVERIFIED', end_pts_seconds='UNVERIFIED',
                      transition='GRAPHICAL_COMPOSITION_CUT', verification='Independent native adjacent pair; taxonomy confidence=' + ruling['confidence'],
                      source_ref=ref + '#' + key, description=ruling['description'],
                      limitations='Onset only; global inventory, subsequent motion and whole-shot durations unverified.'))
shots.sort(key=lambda x: int(x['start_frame']))
assert len(shots) == 31
write_csv(R / 'production_v1/shot_ledger_PARTIAL_v3.csv', shots)

production = read_csv(R / 'production_v1/per_state_production_spec_DRAFT_v2.csv')
for row in production:
    row['curated_original_proposal'] = ''
    row['curated_interval_note'] = ''
    if row['state_id'] == 'S0000':
        assert row['start_frame'] == '0' and row['end_frame'] == '1'
        row.update(end_frame=0, end_exclusive_pts=2 / 24,
                   source_entry_exit='Only sourceframe0 is blank; first roof element enters at1.',
                   source_evidence='Reused actual native0blank and native1roof observations; old two-blank-frame draft claim superseded.',
                   curated_original_proposal='Original timing proposal: one empty lead-in frame at24fps before first asset entry, rather than inherited two-frame proposal.',
                   curated_interval_note='Version3 source interval0only; original first-pass proposal retained as history, superseded by curated one-frame proposal.')
write_csv(R / 'production_v1/per_state_production_spec_DRAFT_v3.csv', production)
write_json(S / 'cut_opening_integration_v8_stats.json',
           dict(event_rows=948, unique_event_ids=948, partition_rows=626, frames_once=19862,
                composition_intervals=329, composition_count_is_not_shotcount=True,
                ambiguous_claims_resolved=14, cut_yes=6, cut_no=8, new_native_fullframe_returns=18,
                prior_gap_cases_reused=5, partial_verified_cut_onsets=31,
                biography_entry_new_native_returns=3, biography_first_entry_frame=750,
                opening_first_element_frame=1, opening_blank_interval=[0, 0],
                opening_new_visual_reads=0, historical_partitions_and_drafts_immutable=True,
                global_native_semantic_pass=False, actual_listening_seconds=0, CT_SCAN_COMPLETE=False))
print('v5partition626/19862once;v8events948unique;14cutclaimsresolved;31partialcutonsets;blank0only/entry1;NOT_CT_COMPLETE')
