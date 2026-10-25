#!/usr/bin/env python3
"""Strict integrity validator for production_intelligence_brain.

Every number this script prints is computed directly from the on-disk CSVs
and files at run time -- nothing here is a cached or remembered result.
Run from anywhere:

    python3 validator/validate_brain.py

Exit code 0 = PASS (all gates below report zero failures / all required
files present). Exit code 1 = FAIL. See validator/README.md.
"""
import csv
import hashlib
import json
import os
import re
import sys

VALIDATOR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, VALIDATOR_DIR)
from _canonical_files import list_canonical_files, dir_listing_matches_patterns  # noqa: E402

BRAIN = os.path.dirname(VALIDATOR_DIR)
MD = os.path.join(BRAIN, '01_master_data')

failures = []


def fail(msg):
    failures.append(msg)
    print(f'FAIL: {msg}')


def load(name):
    path = os.path.join(MD, name)
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def toks(s):
    return [t.strip() for t in re.split(r'[;|]', s) if t.strip()]


print('=' * 70)
print('PRODUCTION INTELLIGENCE BRAIN — STRICT VALIDATOR')
print('=' * 70)

sentences = load('MASTER_SENTENCES.csv')
words = load('MASTER_WORDS.csv')
motions = load('MASTER_MOTIONS.csv')
states = load('MASTER_STATES.csv')
shots = load('MASTER_SHOTS.csv')
assets = load('MASTER_ASSETS.csv')
audio_events = load('MASTER_AUDIO_EVENTS.csv')
sync = load('MASTER_AUDIO_VISUAL_SYNC.csv')

word_by_id = {(w['VIDEO_SLUG'], w['WORD_ID']): w for w in words}
words_by_sentence = {}
for w in words:
    words_by_sentence.setdefault((w['VIDEO_SLUG'], w['SENTENCE_ID']), []).append(w)
motion_by_id = {(m['VIDEO_SLUG'], m['MOTION_ID']): m for m in motions}
state_by_id = {(s['VIDEO_SLUG'], s['STATE_ID']): s for s in states}
shot_by_id = {(s['VIDEO_SLUG'], s['SHOT_ID']): s for s in shots}
asset_by_id = {(a['VIDEO_SLUG'], a['ASSET_ID']): a for a in assets}
audio_event_by_id = {(a['VIDEO_SLUG'], a['AUDIO_EVENT_ID']): a for a in audio_events}

# ---------- 26. SENTENCES ----------
print('\n--- 26. SENTENCE VALIDATION ---')
empty_meaningful = 0
missing_first = missing_last = invalid_first = invalid_last = 0
word_count_mismatch = 0
negative_duration = 0
for s in sentences:
    slug = s['VIDEO_SLUG']
    text = (s['TEXT'] or '').strip()
    if not text:
        empty_meaningful += 1
    fw, lw = s['FIRST_WORD_ID'].strip(), s['LAST_WORD_ID'].strip()
    if not fw:
        missing_first += 1
    elif (slug, fw) not in word_by_id:
        invalid_first += 1
    if not lw:
        missing_last += 1
    elif (slug, lw) not in word_by_id:
        invalid_last += 1
    linked = words_by_sentence.get((slug, s['SENTENCE_ID']), [])
    declared = s['WORD_COUNT'].strip()
    if declared.isdigit() and int(declared) != len(linked):
        word_count_mismatch += 1
    try:
        if float(s['END_SEC']) - float(s['START_SEC']) < 0:
            negative_duration += 1
    except ValueError:
        pass

print(f'TOTAL_SENTENCE_ROWS = {len(sentences)}')
print(f'EMPTY_MEANINGFUL_SENTENCES = {empty_meaningful}')
print(f'MISSING_FIRST_WORD_ID = {missing_first}')
print(f'MISSING_LAST_WORD_ID = {missing_last}')
print(f'INVALID_FIRST_WORD_ID = {invalid_first}')
print(f'INVALID_LAST_WORD_ID = {invalid_last}')
print(f'WORD_COUNT_MISMATCHES = {word_count_mismatch}')
print(f'NEGATIVE_DURATION_ROWS = {negative_duration}')
for label, val in [('EMPTY_MEANINGFUL_SENTENCES', empty_meaningful), ('MISSING_FIRST_WORD_ID', missing_first),
                    ('MISSING_LAST_WORD_ID', missing_last), ('INVALID_FIRST_WORD_ID', invalid_first),
                    ('INVALID_LAST_WORD_ID', invalid_last), ('WORD_COUNT_MISMATCHES', word_count_mismatch),
                    ('NEGATIVE_DURATION_ROWS', negative_duration)]:
    if val:
        fail(f'{label} = {val} (expected 0)')

# duplicate WORD_ID
seen = set()
dup_words = 0
for w in words:
    key = (w['VIDEO_SLUG'], w['WORD_ID'])
    if key in seen:
        dup_words += 1
    seen.add(key)
print(f'DUPLICATE_WORD_IDS = {dup_words}')
if dup_words:
    fail(f'DUPLICATE_WORD_IDS = {dup_words} (expected 0)')

# ---------- 27. MASTER FOREIGN KEYS ----------
print('\n--- 27. MASTER FOREIGN KEY VALIDATION ---')


def is_empty(v):
    return not v.strip() or v.strip().upper() in ('NONE', 'N/A')


orphan_shot_in_states = orphan_asset_in_states = orphan_motion_in_states = 0
for s in states:
    if not is_empty(s['SHOT_ID']) and (s['VIDEO_SLUG'], s['SHOT_ID']) not in shot_by_id:
        orphan_shot_in_states += 1
    for aid in toks(s['ASSET_IDS']):
        if (s['VIDEO_SLUG'], aid) not in asset_by_id:
            orphan_asset_in_states += 1
    for mid in toks(s['MOTION_IDS']):
        if (s['VIDEO_SLUG'], mid) not in motion_by_id:
            orphan_motion_in_states += 1
print(f'MASTER_STATES orphan SHOT_ID refs = {orphan_shot_in_states}')
print(f'MASTER_STATES orphan ASSET_IDS refs = {orphan_asset_in_states}')
print(f'MASTER_STATES orphan MOTION_IDS refs = {orphan_motion_in_states}')
for label, val in [('MASTER_STATES orphan SHOT_ID', orphan_shot_in_states),
                    ('MASTER_STATES orphan ASSET_IDS', orphan_asset_in_states),
                    ('MASTER_STATES orphan MOTION_IDS', orphan_motion_in_states)]:
    if val:
        fail(f'{label} = {val} (expected 0)')

orphan_asset_in_shots = 0
for sh in shots:
    for aid in toks(sh['ASSET_IDS']):
        if (sh['VIDEO_SLUG'], aid) not in asset_by_id:
            orphan_asset_in_shots += 1
print(f'MASTER_SHOTS orphan ASSET_IDS refs = {orphan_asset_in_shots}')
if orphan_asset_in_shots:
    fail(f'MASTER_SHOTS orphan ASSET_IDS = {orphan_asset_in_shots} (expected 0)')

# ---------- 28. A/V EVENTS ----------
print('\n--- 28. A/V SYNC EVENT VALIDATION ---')
ALLOWED_EVENT_TYPES = {'STATE_CHANGE', 'MOTION_START', 'MOTION_END', 'SHOT_CUT', 'TEXT_REVEAL', 'TEXT_CHANGE',
                        'GRAPHIC_REVEAL', 'OBJECT_ENTRY', 'OBJECT_EXIT', 'OBJECT_REPLACEMENT',
                        'TRANSITION_START', 'TRANSITION_END', 'CAMERA_MOVE_START', 'CAMERA_MOVE_END',
                        'ZOOM_START', 'ZOOM_END', 'PAYOFF_REVEAL'}
ALLOWED_RELATIONS = {'BEFORE_WORD', 'ON_WORD_START', 'DURING_WORD', 'ON_WORD_END', 'AFTER_WORD',
                      'BETWEEN_WORDS', 'DURING_PAUSE', 'DURING_SILENCE', 'NO_SPEECH', 'UNKNOWN'}

bad_event_type = 0
orphan_motion_sync = 0
orphan_sentence_sync = 0
orphan_word_sync = 0
orphan_audio_event_sync = 0
bad_relation = 0
seen_sync_ids = set()
dup_sync_ids = 0
av_orphan_shot = av_orphan_target_shot = av_orphan_source_state = av_orphan_target_state = 0

sentence_keys = {(s['VIDEO_SLUG'], s['SENTENCE_ID']) for s in sentences}

for r in sync:
    if r['VISUAL_EVENT_TYPE'] not in ALLOWED_EVENT_TYPES:
        bad_event_type += 1
    if r['SYNC_RELATION'] not in ALLOWED_RELATIONS:
        bad_relation += 1
    # MOTION_ID is the singular FK; MOTION_IDS (added to resolve 15 originally
    # compound STATE_CHANGE rows, e.g. "A27;A28") is the general field -- for
    # a single-motion row it mirrors MOTION_ID, for a genuinely-simultaneous
    # row MOTION_ID is left blank and MOTION_IDS holds the semicolon list.
    for t in toks(r.get('MOTION_IDS', '') or r['MOTION_ID']):
        if (r['VIDEO_SLUG'], t) not in motion_by_id:
            orphan_motion_sync += 1
    if r['SHOT_ID'].strip() and (r['VIDEO_SLUG'], r['SHOT_ID'].strip()) not in shot_by_id:
        av_orphan_shot += 1
    tshot = r.get('TARGET_SHOT_ID', '').strip()
    if tshot and (r['VIDEO_SLUG'], tshot) not in shot_by_id:
        av_orphan_target_shot += 1
    src_state = r['SOURCE_STATE'].strip()
    if src_state and (r['VIDEO_SLUG'], src_state) not in state_by_id:
        av_orphan_source_state += 1
    tgt_state = r['TARGET_STATE'].strip()
    if tgt_state and (r['VIDEO_SLUG'], tgt_state) not in state_by_id:
        av_orphan_target_state += 1
    sid = r['SENTENCE_ID'].strip()
    if sid and (r['VIDEO_SLUG'], sid) not in sentence_keys:
        orphan_sentence_sync += 1
    wid = r['WORD_ID'].strip()
    if wid and (r['VIDEO_SLUG'], wid) not in word_by_id:
        orphan_word_sync += 1
    aeid = r['AUDIO_EVENT_ID'].strip()
    if aeid and (r['VIDEO_SLUG'], aeid) not in audio_event_by_id:
        orphan_audio_event_sync += 1
    key = (r['VIDEO_SLUG'], r['SYNC_ID'])
    if key in seen_sync_ids:
        dup_sync_ids += 1
    seen_sync_ids.add(key)

print(f'TOTAL_SYNC_ROWS = {len(sync)}')
print(f'INVALID_VISUAL_EVENT_TYPE = {bad_event_type}')
print(f'INVALID_SYNC_RELATION = {bad_relation}')
print(f'REQUIRED_ORPHAN_MOTION_REFS = {orphan_motion_sync}')
print(f'AV_ORPHAN_SHOT_REFS = {av_orphan_shot}')
print(f'AV_ORPHAN_TARGET_SHOT_REFS = {av_orphan_target_shot}')
print(f'AV_ORPHAN_SOURCE_STATE_REFS = {av_orphan_source_state}')
print(f'AV_ORPHAN_TARGET_STATE_REFS = {av_orphan_target_state}')
print(f'ORPHAN_SENTENCE_REFS = {orphan_sentence_sync}')
print(f'ORPHAN_WORD_REFS = {orphan_word_sync}')
print(f'ORPHAN_AUDIO_EVENT_REFS = {orphan_audio_event_sync}')
print(f'DUPLICATE_COMPOSITE_SYNC_IDS = {dup_sync_ids}')
for label, val in [('INVALID_VISUAL_EVENT_TYPE', bad_event_type), ('INVALID_SYNC_RELATION', bad_relation),
                    ('REQUIRED_ORPHAN_MOTION_REFS', orphan_motion_sync),
                    ('AV_ORPHAN_SHOT_REFS', av_orphan_shot), ('AV_ORPHAN_TARGET_SHOT_REFS', av_orphan_target_shot),
                    ('AV_ORPHAN_SOURCE_STATE_REFS', av_orphan_source_state),
                    ('AV_ORPHAN_TARGET_STATE_REFS', av_orphan_target_state),
                    ('ORPHAN_SENTENCE_REFS', orphan_sentence_sync),
                    ('ORPHAN_WORD_REFS', orphan_word_sync), ('ORPHAN_AUDIO_EVENT_REFS', orphan_audio_event_sync),
                    ('DUPLICATE_COMPOSITE_SYNC_IDS', dup_sync_ids)]:
    if val:
        fail(f'{label} = {val} (expected 0)')

# ---------- 29. CROSS-TABLE COMPLETENESS ----------
print('\n--- 29. MOTION START/END LINKAGE ---')
motions_with_start = {(r['VIDEO_SLUG'], r['MOTION_ID']) for r in sync
                       if r['VISUAL_EVENT_TYPE'] == 'MOTION_START' and r['MOTION_ID'].strip()}
motions_with_end = {(r['VIDEO_SLUG'], r['MOTION_ID']) for r in sync
                     if r['VISUAL_EVENT_TYPE'] == 'MOTION_END' and r['MOTION_ID'].strip()}
total_motions = len(motions)
start_linked = sum(1 for m in motions if (m['VIDEO_SLUG'], m['MOTION_ID']) in motions_with_start)
start_unresolved = total_motions - start_linked
instant = sum(1 for m in motions if float(m['END_SEC']) <= float(m['START_SEC']))
end_linked = sum(1 for m in motions if (m['VIDEO_SLUG'], m['MOTION_ID']) in motions_with_end)
# a motion has a "documented evidence-based reason" for no MOTION_END exactly when it is instantaneous
end_unresolved_undocumented = sum(
    1 for m in motions
    if (m['VIDEO_SLUG'], m['MOTION_ID']) not in motions_with_end and float(m['END_SEC']) > float(m['START_SEC'])
)
print(f'TOTAL_MOTIONS = {total_motions}')
print(f'MOTION_START_LINKED = {start_linked}')
print(f'MOTION_START_UNRESOLVED = {start_unresolved}')
print(f'MOTION_END_LINKED = {end_linked}')
print(f'MOTION_END_UNRESOLVED_UNDOCUMENTED = {end_unresolved_undocumented} (instant transitions with no separate end, which ARE documented, are not counted here)')
if start_unresolved:
    fail(f'MOTION_START_UNRESOLVED = {start_unresolved} (expected 0)')
if end_unresolved_undocumented:
    fail(f'MOTION_END_UNRESOLVED_UNDOCUMENTED = {end_unresolved_undocumented} (expected 0)')

# ---------- 31. MASTER_MOTIONS DIRECT VALIDATION ----------
print('\n--- 31. MASTER_MOTIONS DIRECT VALIDATION ---')
TOL = 0.06  # ~1.5 frames at 24fps; covers rounding, not a license to be sloppy

motion_orphan_shot = motion_orphan_target_shot = motion_orphan_source_state = motion_orphan_target_state = 0
motion_duration_mismatch = 0
seen_motion_ids = set()
motion_dup = 0
for m in motions:
    if m['SHOT_ID'] and (m['VIDEO_SLUG'], m['SHOT_ID']) not in shot_by_id:
        motion_orphan_shot += 1
    tshot = m.get('TARGET_SHOT_ID', '').strip()
    if tshot and (m['VIDEO_SLUG'], tshot) not in shot_by_id:
        motion_orphan_target_shot += 1
    if m['SOURCE_STATE'] and (m['VIDEO_SLUG'], m['SOURCE_STATE']) not in state_by_id:
        motion_orphan_source_state += 1
    if m['TARGET_STATE'] and (m['VIDEO_SLUG'], m['TARGET_STATE']) not in state_by_id:
        motion_orphan_target_state += 1
    try:
        if abs((float(m['END_SEC']) - float(m['START_SEC'])) - float(m['DURATION_SEC'])) > TOL:
            motion_duration_mismatch += 1
    except ValueError:
        motion_duration_mismatch += 1
    key = (m['VIDEO_SLUG'], m['MOTION_ID'])
    if key in seen_motion_ids:
        motion_dup += 1
    seen_motion_ids.add(key)

print(f'MOTION_ORPHAN_SHOT_REFS = {motion_orphan_shot}')
print(f'MOTION_ORPHAN_TARGET_SHOT_REFS = {motion_orphan_target_shot}')
print(f'MOTION_ORPHAN_SOURCE_STATE_REFS = {motion_orphan_source_state}')
print(f'MOTION_ORPHAN_TARGET_STATE_REFS = {motion_orphan_target_state}')
print(f'MOTION_DURATION_MISMATCHES = {motion_duration_mismatch}')
print(f'MOTION_DUPLICATE_IDS = {motion_dup}')
for label, val in [('MOTION_ORPHAN_SHOT_REFS', motion_orphan_shot),
                    ('MOTION_ORPHAN_TARGET_SHOT_REFS', motion_orphan_target_shot),
                    ('MOTION_ORPHAN_SOURCE_STATE_REFS', motion_orphan_source_state),
                    ('MOTION_ORPHAN_TARGET_STATE_REFS', motion_orphan_target_state),
                    ('MOTION_DURATION_MISMATCHES', motion_duration_mismatch),
                    ('MOTION_DUPLICATE_IDS', motion_dup)]:
    if val:
        fail(f'{label} = {val} (expected 0)')

# ---------- 32. MASTER_SHOTS / MASTER_STATES DIRECT VALIDATION ----------
print('\n--- 32. MASTER_SHOTS / MASTER_STATES DIRECT VALIDATION ---')

state_duration_mismatch = 0
state_orphan_shot = 0
for s in states:
    try:
        if abs((float(s['END_SEC']) - float(s['START_SEC'])) - float(s['DURATION_SEC'])) > TOL:
            state_duration_mismatch += 1
    except ValueError:
        state_duration_mismatch += 1
    if s['SHOT_ID'] and (s['VIDEO_SLUG'], s['SHOT_ID']) not in shot_by_id:
        state_orphan_shot += 1

states_by_shot = {}
for s in states:
    states_by_shot.setdefault((s['VIDEO_SLUG'], s['SHOT_ID']), []).append(s)

state_non_monotonic = 0
for key, rows in states_by_shot.items():
    rows_sorted = sorted(rows, key=lambda r: float(r['START_SEC']))
    prev_end = None
    for r in rows_sorted:
        if prev_end is not None and float(r['START_SEC']) < prev_end - TOL:
            state_non_monotonic += 1
        prev_end = max(prev_end or 0.0, float(r['END_SEC']))

motions_by_shot = {}
for m in motions:
    motions_by_shot.setdefault((m['VIDEO_SLUG'], m['SHOT_ID']), []).append(m)

shot_duration_mismatch = shot_state_count_mismatch = shot_motion_count_mismatch = 0
shot_first_state_errors = shot_last_state_errors = 0
for sh in shots:
    key = (sh['VIDEO_SLUG'], sh['SHOT_ID'])
    real_states = states_by_shot.get(key, [])
    real_motions = motions_by_shot.get(key, [])
    try:
        if abs((float(sh['END_SEC']) - float(sh['START_SEC'])) - float(sh['DURATION_SEC'])) > TOL:
            shot_duration_mismatch += 1
    except ValueError:
        shot_duration_mismatch += 1
    if int(sh['STATE_COUNT']) != len(real_states):
        shot_state_count_mismatch += 1
    if int(sh['MOTION_COUNT']) != len(real_motions):
        shot_motion_count_mismatch += 1
    if real_states:
        real_first = min(real_states, key=lambda r: float(r['START_SEC']))
        real_last = max(real_states, key=lambda r: float(r['END_SEC']))
        if sh['FIRST_STATE_ID'] != real_first['STATE_ID']:
            shot_first_state_errors += 1
        if sh['LAST_STATE_ID'] != real_last['STATE_ID']:
            shot_last_state_errors += 1

print(f'STATE_DURATION_MISMATCHES = {state_duration_mismatch}')
print(f'STATE_NON_MONOTONIC_ERRORS = {state_non_monotonic}')
print(f'STATE_ORPHAN_SHOT_REFS = {state_orphan_shot}')
print(f'SHOT_DURATION_MISMATCHES = {shot_duration_mismatch}')
print(f'SHOT_STATE_COUNT_MISMATCHES = {shot_state_count_mismatch}')
print(f'SHOT_MOTION_COUNT_MISMATCHES = {shot_motion_count_mismatch}')
print(f'SHOT_FIRST_STATE_ERRORS = {shot_first_state_errors}')
print(f'SHOT_LAST_STATE_ERRORS = {shot_last_state_errors}')
for label, val in [('STATE_DURATION_MISMATCHES', state_duration_mismatch),
                    ('STATE_NON_MONOTONIC_ERRORS', state_non_monotonic),
                    ('STATE_ORPHAN_SHOT_REFS', state_orphan_shot),
                    ('SHOT_DURATION_MISMATCHES', shot_duration_mismatch),
                    ('SHOT_STATE_COUNT_MISMATCHES', shot_state_count_mismatch),
                    ('SHOT_MOTION_COUNT_MISMATCHES', shot_motion_count_mismatch),
                    ('SHOT_FIRST_STATE_ERRORS', shot_first_state_errors),
                    ('SHOT_LAST_STATE_ERRORS', shot_last_state_errors)]:
    if val:
        fail(f'{label} = {val} (expected 0)')

# ---------- 33. RAW CSV WIDTH VALIDATION ----------
print('\n--- 33. RAW CSV WIDTH VALIDATION ---')
CSV_FILES = ['MASTER_SENTENCES.csv', 'MASTER_WORDS.csv', 'MASTER_MOTIONS.csv', 'MASTER_STATES.csv',
             'MASTER_SHOTS.csv', 'MASTER_ASSETS.csv', 'MASTER_AUDIO_EVENTS.csv', 'MASTER_AUDIO_VISUAL_SYNC.csv']
malformed_csv_rows = 0
for fname in CSV_FILES:
    path = os.path.join(MD, fname)
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        width = len(header)
        for i, row in enumerate(reader, start=2):
            if len(row) != width:
                malformed_csv_rows += 1
                print(f'  malformed row: {fname}:{i} has {len(row)} fields, header has {width}')
print(f'MALFORMED_CSV_ROWS = {malformed_csv_rows}')
if malformed_csv_rows:
    fail(f'MALFORMED_CSV_ROWS = {malformed_csv_rows} (expected 0)')

# ---------- HARD TIMESTAMP ERRORS (rollup) ----------
print('\n--- HARD TIMESTAMP ERRORS (rollup across motions/states/shots) ---')
hard_timestamp_errors = 0
for label, rows in [('MASTER_MOTIONS', motions), ('MASTER_STATES', states), ('MASTER_SHOTS', shots)]:
    for r in rows:
        try:
            s, e = float(r['START_SEC']), float(r['END_SEC'])
        except ValueError:
            hard_timestamp_errors += 1
            continue
        if e < s:
            hard_timestamp_errors += 1
print(f'HARD_TIMESTAMP_ERRORS = {hard_timestamp_errors}')
if hard_timestamp_errors:
    fail(f'HARD_TIMESTAMP_ERRORS = {hard_timestamp_errors} (expected 0)')

# ---------- 30. CANONICAL ARTIFACTS ----------
print('\n--- 30. CANONICAL ARTIFACT PRESENCE ---')
required = {
    '01_master_data': ['MASTER_SENTENCES.csv', 'MASTER_WORDS.csv', 'MASTER_MOTIONS.csv', 'MASTER_STATES.csv',
                        'MASTER_SHOTS.csv', 'MASTER_ASSETS.csv', 'MASTER_AUDIO_EVENTS.csv', 'MASTER_AUDIO_VISUAL_SYNC.csv'],
    '02_production_dna': ['ASSET_DNA.md', 'AUDIO_DNA.md', 'AUDIO_VISUAL_SYNC_DNA.md', 'EDITING_DNA.md',
                           'MOTION_DNA.md', 'PACING_DNA.md', 'VISUAL_DNA.md'],
    '03_reconstruction_system': ['CAPCUT_PRODUCTION_SYSTEM.md', 'IMAGE_TO_VIDEO_SYSTEM.md',
                                  'ASSET_CREATION_SYSTEM.md', 'DECISION_RULES.md'],
    '04_patterns': ['AUDIO_TRIGGER_PATTERNS.csv', 'MOTION_PATTERNS.csv', 'SHOT_PATTERNS.csv',
                     'STATE_PATTERNS.csv', 'TRANSITION_PATTERNS.csv', 'VISUAL_CHANGE_PATTERNS.csv'],
    '05_blueprints': ['NEW_VIDEO_BLUEPRINT.md', 'SHOT_DESIGN_BLUEPRINT.md',
                       'NARRATION_TO_VISUAL_BLUEPRINT.md', 'RECONSTRUCTION_CHECKLIST.md'],
}
missing_files = []
trivial_files = []
for folder, files in required.items():
    for fname in files:
        path = os.path.join(BRAIN, folder, fname)
        if not os.path.exists(path):
            missing_files.append(f'{folder}/{fname}')
        elif os.path.getsize(path) < 50:
            trivial_files.append(f'{folder}/{fname}')

for extra_name in ['validator/validate_brain.py', 'validator/README.md', 'validator/_canonical_files.py',
                    'validator/build_release_manifest.py',
                    'validator/schemas/brain_manifest.schema.json', 'validator/schemas/release_manifest.schema.json',
                    'SOURCE_VIDEO_INDEX.csv', 'SOURCE_TO_FORENSIC_MAP.csv',
                    'BRAIN_SUMMARY.md', 'BRAIN_MANIFEST.json', 'VALIDATION_REPORT.md',
                    'CONTINUATION_HANDOFF.md', 'CANONICAL_PATHS.md', 'RELEASE_NOTES.md', 'PACKAGE_AUDIT.md',
                    'testing/GENERALIZATION_TEST_PROTOCOL.md', 'testing/UNSEEN_SCRIPT_INPUT_TEMPLATE.md',
                    'testing/UNSEEN_VIDEO_INPUT_TEMPLATE.md', 'testing/TEST_RESULT_SCHEMA.json']:
    path = os.path.join(BRAIN, extra_name)
    if not os.path.exists(path):
        missing_files.append(extra_name)
    elif os.path.getsize(path) < 50:
        trivial_files.append(extra_name)

print(f'MISSING_CANONICAL_FILES = {len(missing_files)}')
for m in missing_files:
    print('  missing:', m)
print(f'TRIVIAL_(NON_SUBSTANTIVE)_FILES = {len(trivial_files)}')
for t in trivial_files:
    print('  trivial:', t)
if missing_files:
    fail(f'MISSING_CANONICAL_FILES = {len(missing_files)}')
if trivial_files:
    fail(f'TRIVIAL_CANONICAL_FILES = {len(trivial_files)}')


def load_json(rel_path):
    path = os.path.join(BRAIN, rel_path)
    if not os.path.exists(path):
        return None
    with open(path, encoding='utf-8') as f:
        return json.load(f)


# ---------- INDEX / MANIFEST CONSISTENCY ----------
print('\n--- INDEX / MANIFEST CONSISTENCY (DNA_INDEX / RECONSTRUCTION_INDEX / BRAIN_MANIFEST vs. canonical data) ---')

with open(os.path.join(BRAIN, 'SOURCE_VIDEO_INDEX.csv'), newline='', encoding='utf-8') as f:
    source_video_count = sum(1 for _ in csv.DictReader(f))

computed = {
    'source_video_count': source_video_count,
    'word_count': len(words),
    'meaningful_sentence_count': len(sentences),
    'shot_count': len(shots),
    'state_count': len(states),
    'motion_count': len(motions),
    'asset_count': len(assets),
    'audio_event_count': len(audio_events),
    'av_sync_total': len(sync),
    'state_change_count': sum(1 for r in sync if r['VISUAL_EVENT_TYPE'] == 'STATE_CHANGE'),
    'motion_start_count': sum(1 for r in sync if r['VISUAL_EVENT_TYPE'] == 'MOTION_START'),
    'motion_end_count': sum(1 for r in sync if r['VISUAL_EVENT_TYPE'] == 'MOTION_END'),
}

dna_index = load_json('02_production_dna/DNA_INDEX.json')
if dna_index is None:
    fail('02_production_dna/DNA_INDEX.json missing')
else:
    for key, expected in computed.items():
        actual = dna_index.get(key)
        if actual != expected:
            fail(f'DNA_INDEX.json[{key}] = {actual!r} (expected {expected})')

brain_manifest = load_json('BRAIN_MANIFEST.json')
MANIFEST_FIELD_MAP = {
    'source_video_count': 'source_video_count', 'word_count': 'total_words',
    'meaningful_sentence_count': 'total_meaningful_sentences', 'shot_count': 'total_shots',
    'state_count': 'total_states', 'motion_count': 'total_motions', 'asset_count': 'total_assets',
    'audio_event_count': 'total_audio_events', 'av_sync_total': 'total_av_sync_events',
    'motion_start_count': 'motion_start_events', 'motion_end_count': 'motion_end_events',
}
if brain_manifest is None:
    fail('BRAIN_MANIFEST.json missing')
else:
    for computed_key, manifest_key in MANIFEST_FIELD_MAP.items():
        actual = brain_manifest.get(manifest_key)
        if actual != computed[computed_key]:
            fail(f'BRAIN_MANIFEST.json[{manifest_key}] = {actual!r} (expected {computed[computed_key]})')
    if brain_manifest.get('release_status') not in ('PREPARING', 'FROZEN'):
        fail(f"BRAIN_MANIFEST.json[release_status] = {brain_manifest.get('release_status')!r} (expected PREPARING or FROZEN)")

CANONICAL_RECONSTRUCTION_DOCS = ['CAPCUT_PRODUCTION_SYSTEM.md', 'IMAGE_TO_VIDEO_SYSTEM.md',
                                  'ASSET_CREATION_SYSTEM.md', 'DECISION_RULES.md']
LEGACY_RECONSTRUCTION_GUIDES = ['CAPCUT_RECONSTRUCTION_GUIDE.md', 'IMAGE_TO_VIDEO_RECONSTRUCTION_GUIDE.md']
reconstruction_index = load_json('03_reconstruction_system/RECONSTRUCTION_INDEX.json')
if reconstruction_index is None:
    fail('03_reconstruction_system/RECONSTRUCTION_INDEX.json missing')
else:
    docs = reconstruction_index.get('documents')
    if docs != CANONICAL_RECONSTRUCTION_DOCS:
        fail(f'RECONSTRUCTION_INDEX.json[documents] = {docs!r} (expected exactly {CANONICAL_RECONSTRUCTION_DOCS})')
    serialized = json.dumps(reconstruction_index)
    for legacy_name in LEGACY_RECONSTRUCTION_GUIDES:
        if legacy_name in serialized:
            fail(f'RECONSTRUCTION_INDEX.json references legacy guide {legacy_name} as if canonical')
    dna_ref = reconstruction_index.get('dna_reference', {})
    sp = dna_ref.get('sentence_pacing', {})
    if sp.get('total_sentences') != len(sentences):
        fail(f"RECONSTRUCTION_INDEX.json[dna_reference.sentence_pacing.total_sentences] = {sp.get('total_sentences')!r} (expected {len(sentences)})")
    sr = dna_ref.get('sync_relationships', {})
    if sr.get('total_syncs') != len(sync):
        fail(f"RECONSTRUCTION_INDEX.json[dna_reference.sync_relationships.total_syncs] = {sr.get('total_syncs')!r} (expected {len(sync)})")

print('DNA_INDEX / BRAIN_MANIFEST / RECONSTRUCTION_INDEX checked against canonical master-data counts.')

# ---------- LEGACY ISOLATION ----------
print('\n--- LEGACY ISOLATION (no canonical index/blueprint may cite legacy/ as authority) ---')
legacy_scan_targets = ['02_production_dna/DNA_INDEX.json', '03_reconstruction_system/RECONSTRUCTION_INDEX.json',
                        'BRAIN_MANIFEST.json']
blueprint_dir = os.path.join(BRAIN, '05_blueprints')
if os.path.isdir(blueprint_dir):
    legacy_scan_targets += [f'05_blueprints/{n}' for n in sorted(os.listdir(blueprint_dir)) if n.endswith('.md')]

legacy_refs_found = 0
for rel_path in legacy_scan_targets:
    path = os.path.join(BRAIN, rel_path)
    if not os.path.exists(path):
        continue
    with open(path, encoding='utf-8') as f:
        content = f.read()
    if 'legacy/' in content:
        legacy_refs_found += 1
        fail(f'{rel_path} references legacy/ as if it were current authority')
print(f'CANONICAL_INDEX_OR_BLUEPRINT_LEGACY_REFERENCES = {legacy_refs_found}')

# ---------- STRICT CANONICAL FILE ENUMERATION ----------
print('\n--- STRICT CANONICAL FILE ENUMERATION ---')
EXPECTED_TOP_LEVEL = {
    'SOURCE_VIDEO_INDEX.csv', 'SOURCE_TO_FORENSIC_MAP.csv',
    '01_master_data', '02_production_dna', '03_reconstruction_system', '04_patterns', '05_blueprints',
    'validator', 'testing', 'legacy',
    'BRAIN_MANIFEST.json', 'BRAIN_SUMMARY.md', 'VALIDATION_REPORT.md', 'CONTINUATION_HANDOFF.md',
    'CANONICAL_PATHS.md', 'RELEASE_NOTES.md', 'PACKAGE_AUDIT.md',
}
OPTIONAL_TOP_LEVEL = {'RELEASE_MANIFEST.json'}  # only exists once the release is built
actual_top_level = {n for n in os.listdir(BRAIN) if not n.startswith('.')}
unexpected_top_level = actual_top_level - EXPECTED_TOP_LEVEL - OPTIONAL_TOP_LEVEL
if unexpected_top_level:
    fail(f'Unexpected top-level entries in production_intelligence_brain/: {sorted(unexpected_top_level)}')
print(f'UNEXPECTED_TOP_LEVEL_ENTRIES = {sorted(unexpected_top_level)}')

stray_files_total = 0
for rel_dir in ['01_master_data', '02_production_dna', '03_reconstruction_system', '04_patterns',
                 '05_blueprints', 'validator', 'validator/schemas', 'testing']:
    stray = dir_listing_matches_patterns(BRAIN, rel_dir)
    # validator/ itself also legitimately holds README.md, not covered by a glob pattern above.
    stray = [s for s in stray if not (rel_dir == 'validator' and s == 'README.md')]
    if stray:
        stray_files_total += len(stray)
        fail(f'{rel_dir}/ has unlisted canonical-looking file(s): {stray}')
print(f'STRAY_FILES_IN_CANONICAL_DIRS = {stray_files_total}')

# ---------- RELEASE_MANIFEST VALIDATION ----------
print('\n--- RELEASE_MANIFEST VALIDATION ---')
release_manifest = load_json('RELEASE_MANIFEST.json')
if release_manifest is None:
    print('RELEASE_MANIFEST.json not present yet (pre-freeze) -- skipping hash verification.')
else:
    declared = {e['relative_path']: e for e in release_manifest['files']}
    if 'RELEASE_MANIFEST.json' in declared:
        fail('RELEASE_MANIFEST.json must not list itself (recursive hash dependency)')

    hash_mismatches = missing_on_disk = 0
    for rel_path, entry in declared.items():
        fpath = os.path.join(BRAIN, rel_path)
        if not os.path.exists(fpath):
            missing_on_disk += 1
            fail(f'RELEASE_MANIFEST entry missing on disk: {rel_path}')
            continue
        if os.path.getsize(fpath) != entry['size_bytes']:
            hash_mismatches += 1
            fail(f'RELEASE_MANIFEST size mismatch: {rel_path}')
            continue
        h = hashlib.sha256()
        with open(fpath, 'rb') as bf:
            h.update(bf.read())
        if h.hexdigest() != entry['sha256']:
            hash_mismatches += 1
            fail(f'RELEASE_MANIFEST sha256 mismatch: {rel_path}')

    current_canonical = {rel for rel, _cat, _sz, _sha in list_canonical_files(BRAIN)}
    undeclared = current_canonical - set(declared)
    stale_declared = set(declared) - current_canonical
    if undeclared:
        fail(f'Canonical files not listed in RELEASE_MANIFEST.json: {sorted(undeclared)}')
    if stale_declared:
        fail(f'RELEASE_MANIFEST.json lists files no longer canonical/present: {sorted(stale_declared)}')
    print(f'RELEASE_MANIFEST files declared = {len(declared)}, hash/size mismatches = {hash_mismatches}, '
          f'missing on disk = {missing_on_disk}, undeclared canonical = {len(undeclared)}, stale declared = {len(stale_declared)}')

# ---------- ROW COUNT SUMMARY ----------
print('\n--- ROW COUNT SUMMARY (actual, computed now) ---')
print(f'sentences (meaningful): {len(sentences)}')
print(f'words: {len(words)}')
print(f'motions: {len(motions)}')
print(f'states: {len(states)}')
print(f'shots: {len(shots)}')
print(f'assets: {len(assets)}')
print(f'audio_events: {len(audio_events)}')
print(f'av_sync total: {len(sync)}')
from collections import Counter
print(f'  by type: {dict(Counter(r["VISUAL_EVENT_TYPE"] for r in sync))}')

# ---------- VERDICT ----------
print('\n' + '=' * 70)
if failures:
    print(f'RESULT: FAIL ({len(failures)} failing checks)')
    print('=' * 70)
    sys.exit(1)
else:
    print('RESULT: PASS (all gates report zero failures)')
    print('=' * 70)
    sys.exit(0)
