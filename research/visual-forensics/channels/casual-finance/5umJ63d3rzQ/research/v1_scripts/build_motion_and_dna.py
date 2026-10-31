#!/usr/bin/env python3
"""Checkpoint 10: motion ledger, timing resolution, DNA statistics, per-group reconstruction specs. Read-only on inputs; run python3 -I from ROOT."""
import csv, json, os, bisect, statistics as st
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(ROOT, 'tables', 'integrated'); os.makedirs(os.path.join(ROOT, 'tables', 'dna'), exist_ok=True); D = os.path.join(ROOT, 'tables', 'dna')
R = lambda p: list(csv.DictReader(open(os.path.join(ROOT, p))))
FPS = 30
cands = R('tables/integrated/candidates_final.csv'); ev = {r['id']: r for r in R('tables/candidate_evidence.csv')}
states = R('tables/integrated/states_final.csv'); groups = R('tables/integrated/composition_groups.csv'); disp = R('tables/integrated/disputes_final.csv')
unowned = R('tables/integrated/unowned_intervals_final.csv'); align = R('tables/integrated/script_visual_alignment.csv')
sums = json.load(open(os.path.join(T, 'integration_summary.json')))
sbound = sorted((int(s['measured_start']), int(s.get('measured_end', s['draft_end'])), s['state_id']) for s in states)
starts = [b[0] for b in sbound]; sgroup = {}
for g in groups:
    for m in g['members'].split(';'): sgroup[m] = g['group']
def owner(f):
    i = bisect.bisect_right(starts, f) - 1
    if i >= 0 and sbound[i][0] <= f <= sbound[i][1]: return sbound[i][2], sgroup[sbound[i][2]]
    return 'UNOWNED', 'UNOWNED'
EMB = {'THIRD_PARTY_PLAYBACK', 'FOOTAGE_MOTION', 'SCREEN_RECORDING_TYPING', 'SCREEN_RECORDING_TEXT_STREAM'}
def cls(t):
    t = t.upper()
    if t in ('FULL_REPLACE', 'HARD_REPLACE', 'LARGE_PARTIAL_REPLACE'): return 'REPLACE_CUT'
    if t in ('ADDITIVE_ENTRY', 'ADDITIVE_OVERLAY', 'SEQUENTIAL_POP_IN', 'HIGHLIGHT_ADD'): return 'ENTRY_POP_IN'
    if 'POSE' in t or 'EXPRESSION' in t or t == 'ELEMENT_SWAP': return 'POSE_OR_ELEMENT_SWAP'
    if 'DRAW' in t: return 'DRAW_ON_REVEAL'
    if 'TEXT' in t or 'NUMBER' in t or 'SUBTITLE' in t: return 'TEXT_CHANGE'
    if 'POINTER' in t or 'PROGRESS' in t: return 'POINTER_OR_PROGRESS'
    if t in EMB: return 'EMBEDDED_PLAYBACK'
    if t == 'NOT_A_CHANGE': return 'NOT_A_CHANGE'
    return 'OTHER'
led = []
for c in cands:
    t = c['second_pass_type'] or c['first_pass_type']; s, e = int(c['start']), int(c['end']); sid, gid = owner(s); e0 = ev.get(c['id'], {})
    led.append({'ledger_id': 'M-' + c['id'], 'source_id': c['id'], 'source_kind': 'CANDIDATE', 'start_frame': s, 'end_frame': e, 'start_sec': round((s + 1) / FPS, 3), 'duration_frames': e - s + 1,
        'state_id': sid, 'composition_group': gid, 'motion_type_raw': t, 'motion_class': cls(t), 'origin': 'EMBEDDED_THIRD_PARTY_OR_CAPTURE' if t.upper() in EMB or cls(t) == 'EMBEDDED_PLAYBACK' else 'AUTHORED_EDIT',
        'object_layer_and_direction': 'REVIEWER_TEXT_ONLY (see observation); no per-object vector measured', 'diff_bbox_raw': e0.get('diff_bbox', ''), 'net_changed_frac': e0.get('net_changed_frac', ''),
        'observation': c['evidence'], 'evidence_ref': 'evidence/%s.jpg' % c['id'], 'confidence': c['confidence'], 'verification': 'REVIEWER_%s' % c['agreement'], 'reviewer': c['reviewer']})
for d in disp:
    if d['second_pass_verdict'] != 'REAL_MOTION' or not d['cut_frame']: continue
    f = int(d['cut_frame']); sid, gid = owner(f)
    led.append({'ledger_id': 'M-' + d['id'], 'source_id': d['id'], 'source_kind': 'SCENEDETECT_DISPUTE', 'start_frame': f, 'end_frame': f, 'start_sec': round((f + 1) / FPS, 3), 'duration_frames': 1,
        'state_id': sid, 'composition_group': gid, 'motion_type_raw': 'REAL_MOTION', 'motion_class': 'WITHIN_STATE_MOTION', 'origin': 'UNCLASSIFIED', 'object_layer_and_direction': 'UNAVAILABLE',
        'diff_bbox_raw': '', 'net_changed_frac': '', 'observation': 'scenedetect cut judged motion, not a state change', 'evidence_ref': 'first_pass/second_pass shard %s' % d['shard'], 'confidence': d['confidence'], 'verification': 'REVIEWER_' + d['agreement'], 'reviewer': d['reviewer']})
led.sort(key=lambda r: (r['start_frame'], r['ledger_id']))
with open(os.path.join(D, 'motion_ledger.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(led[0].keys())); w.writeheader(); w.writerows(led)
# timing resolution
meas = {int(r['frame']): float(r['px_diff_ge12']) for r in R('FULL_FRAME_MEASUREMENTS.csv')}
CLASS = {'S0248': ('APPLIED_HARD_CUT', 'single-frame spike f13439, reviewer C declared same'), 'S0079': ('APPLIED_HARD_CUT', 'single-frame spike f3283, reviewer A declared same'),
 'S0260': ('APPLIED_FRAME_VIEWED', 'checkpoint 11: hard cut f14312 (199,621 px; frames f14311 vs f14312 viewed: slide -> donut screen); f14314-16 is a scroll-in inside the state; earlier +-3 window around draft start missed f14312; reviewer C declared 14312; previous state ends f14311'),
 'S0037': ('RESOLVED_IN_STATE_EVENT', 'checkpoint 11 frames f1697-1702 viewed: f1699 character brow/pose swap, f1700 bubble pops into particles (95,077 px); no scene cut; draft f1699 kept'),
 'S0263': ('APPLIED_FRAME_VIEWED', 'checkpoint 11: f14364 still shows the slide, cartoon first appears f14365 (667,283 px); reviewers declared 14364 (off by one); S0262 end extended to f14364'),
 'S0156': ('NOT_APPLIED_TRANSITION_ENDS_AT_START', 'sustained peaks f6920-6923 (~150k) end right before draft start: zoom/pan/fade settling'),
 'S0259': ('NOT_APPLIED_TRANSITION_ENDS_AT_START', 'sustained peaks f14293-14296 end before draft start'),
 'S0327': ('NOT_APPLIED_TRANSITION_ENDS_AT_START', 'sustained peaks f18113-18116 end before draft start'),
 'S0379': ('NOT_APPLIED_TRANSITION_ENDS_AT_START', 'sustained peaks f21205-21208 end before draft start'),
 'S0252': ('NOT_APPLIED_WITHIN_STATE_EVENT', 'peak f13944 is after draft start f13941; in-state event'),
 'S0253': ('NOT_APPLIED_WITHIN_STATE_EVENT', 'peak f13986 is after draft start f13983; in-state event')}
sm = {s['state_id']: s for s in states}
with open(os.path.join(D, 'timing_resolution.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['state_id', 'draft_start', 'measured_start_final', 'reviewer_declared_start', 'classification', 'evidence', 'px_diff_ge12_window'])
    for sid, (c, note) in CLASS.items():
        s = sm[sid]; d0 = int(s['draft_start']); w.writerow([sid, d0, s['measured_start'], s['reviewer_declared_start'], c, note, ' '.join('%d:%d' % (x, meas.get(x, 0)) for x in range(d0 - 3, d0 + 4))])
# stats
dur = lambda g: int(g['end']) - int(g['start']) + 1
gd = [dur(g) / FPS for g in groups]
cc = Counter(r['motion_class'] for r in led if r['source_kind'] == 'CANDIDATE'); org = Counter(r['origin'] for r in led if r['source_kind'] == 'CANDIDATE')
per_min = Counter(int(g['start']) // (FPS * 60) for g in groups)
stats = {'groups': len(groups), 'group_dur_s': {'median': st.median(gd), 'mean': round(st.mean(gd), 2), 'min': min(gd), 'max': max(gd), 'p90': sorted(gd)[int(.9 * len(gd))]},
    'motion_class_candidates': dict(cc), 'origin_candidates': dict(org), 'groups_per_minute': dict(sorted(per_min.items())), 'ledger_rows': len(led),
    'sentence_visual_rate': {'median_groups_per_sentence': st.median(int(a['n_groups']) for a in align), 'sentences': len(align)},
    'raw_type_top': Counter(r['motion_type_raw'] for r in led if r['source_kind'] == 'CANDIDATE').most_common(12)}
json.dump(stats, open(os.path.join(D, 'dna_stats.json'), 'w'), indent=1)
# per-group reconstruction spec (structural, data-derived; art content is a slot, not copied)
AO = {'REPLACE_CUT': 'new full composition on cut', 'ENTRY_POP_IN': 'element pops/slides in on top of base', 'POSE_OR_ELEMENT_SWAP': 'character pose/element swap in place', 'DRAW_ON_REVEAL': 'draw-on or reveal',
      'TEXT_CHANGE': 'text/number change or typing', 'POINTER_OR_PROGRESS': 'pointer move or progress tick', 'EMBEDDED_PLAYBACK': 'embedded footage/screen capture (use own licensed capture)', 'NOT_A_CHANGE': '', 'OTHER': 'other', 'WITHIN_STATE_MOTION': 'continuous motion'}
al_by_g = {}
for a in align:
    if a['first_group']:
        for gi in range(int(a['first_group'][1:]), int(a['last_group'][1:]) + 1): al_by_g.setdefault('G%04d' % gi, []).append(a['sentence_id'])
bygrp = {}
for r in led: bygrp.setdefault(r['composition_group'], []).append(r)
with open(os.path.join(D, 'reconstruction_specs_per_group.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['group', 'start_frame', 'end_frame', 'approx_duration_s', 'timing_basis', 'source_sentences_provisional', 'entry_transition_inferred', 'editable_layers_inferred', 'animation_order_from_ledger', 'beats_ms_offsets_MEASURED_frames', 'embedded_playback_present', 'illustration_prompt_slot', 'originality_note'])
    prev = None
    for g in groups:
        rows = [r for r in bygrp.get(g['group'], []) if r['motion_class'] != 'NOT_A_CHANGE']
        a, b = int(g['start']), int(g['end']); classes = [r['motion_class'] for r in rows]
        layers = ['background'] + (['character'] if 'POSE_OR_ELEMENT_SWAP' in classes else []) + (['overlay_elements'] if 'ENTRY_POP_IN' in classes else []) + (['text'] if 'TEXT_CHANGE' in classes else []) + (['drawn_strokes'] if 'DRAW_ON_REVEAL' in classes else []) + (['pointer/progress'] if 'POINTER_OR_PROGRESS' in classes else [])
        order = ' > '.join(AO.get(c, c) for c in dict.fromkeys(classes)) or 'static hold'
        w.writerow([g['group'], a, b, round((b - a + 1) / FPS, 2), 'MEASURED frames; seconds = frame/30', ';'.join(al_by_g.get(g['group'], [])), 'hard cut at group start (all state boundaries are cuts unless transition flagged)', '|'.join(layers), order,
            ';'.join(str(r['start_frame'] - a) for r in rows[:12]), any(r['origin'].startswith('EMBEDDED') for r in rows),
            'ORIGINAL art for new-script beat {BEAT}: express concept {CONCEPT} in the channel-style-agnostic form; do not copy source characters/captures', 'Structure only; no source artwork, narration or sequence reuse'])
print(json.dumps(stats, indent=1))
