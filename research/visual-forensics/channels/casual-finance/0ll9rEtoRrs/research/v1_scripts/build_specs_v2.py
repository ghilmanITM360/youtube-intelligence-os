#!/usr/bin/env python3
"""Checkpoint 11: evidence-grounded per-group specs. Read-only on inputs; writes tables/dna/reconstruction_specs_v2.csv. Run python3 -I from ROOT.
Source descriptions are OBSERVED/INFERRED research notes. The original_prompt_template is built from story function + layout role only, never from the source's art description."""
import csv, json, os, re
from collections import defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda p: json.load(open(os.path.join(ROOT, p)))
C = lambda p: list(csv.DictReader(open(os.path.join(ROOT, p))))
fp = {}
for n in range(1, 9):
    for s in J(f'tables/first_pass/FIRST_PASS_shard_{n}.json')['states']: fp[s['id']] = (n, s)
sp = {}
for k, f in zip('ABCD', ['OUT2_A', 'OUT2_B', 'OUT2_C_MERGED', 'OUT2_D']):
    for s in J(f'agents2/{f}.json')['states']: sp[s['id']] = (k, s)
groups = C('tables/integrated/composition_groups.csv')
led = defaultdict(list)
for r in C('tables/dna/motion_ledger.csv'): led[r['composition_group']].append(r)
def clean(t): return re.sub(r'^(INFERRED|OBSERVED):\s*', '', (t or '').strip())
rows = []
for g in groups:
    mem = g['members'].split(';'); first = mem[0]
    n, s0 = fp.get(first, (None, {}))
    texts = []; descs = []; story = []; conf = []; revs = set()
    for m in mem:
        if m in sp:
            k, s = sp[m]; revs.add(k); conf.append(s.get('confidence', ''))
            if s.get('readable_text') and s['readable_text'] != 'no text present': texts.append(s['readable_text'])
            if s.get('final_state_description'): descs.append(s['final_state_description'])
        if m in fp and fp[m][1].get('story_function'): story.append(clean(fp[m][1]['story_function']))
    beats = sorted(led.get(g['group'], []), key=lambda r: int(r['start_frame']))
    cls = [b['motion_class'] for b in beats]
    emb = any(b['origin'] != 'AUTHORED_EDIT' for b in beats)
    pops = sum(c in ('ENTRY_POP_IN', 'DRAW_ON_REVEAL') for c in cls)
    layers = ['base_composition'] + ([f'{pops}_separate_reveal_elements'] if pops else []) + (['text_layer'] if texts else []) + (['pointer_or_progress_layer'] if 'POINTER_OR_PROGRESS' in cls else []) + (['licensed_capture_slot'] if emb else [])
    concept = '; '.join(dict.fromkeys(story))[:300] or 'UNAVAILABLE'
    dur = round((int(g['end']) - int(g['start']) + 1) / 30, 2)
    rows.append({'group': g['group'], 'start_frame': g['start'], 'end_frame': g['end'], 'duration_s': dur, 'member_states': g['members'],
        'evidence_files': f"tables/first_pass/FIRST_PASS_shard_{n}.json;agents2/OUT2_{'/'.join(sorted(revs)) or 'NA'}.json;" + ';'.join(dict.fromkeys(b['evidence_ref'] for b in beats if b['evidence_ref']))[:200],
        'reviewers': ','.join(sorted(revs)), 'reviewer_confidence': '|'.join(dict.fromkeys(conf)) or 'UNAVAILABLE',
        'story_function_INFERRED': concept,
        'readable_text_OBSERVED': ' || '.join(dict.fromkeys(texts))[:400],
        'source_observation_OBSERVED_do_not_use_as_art_prompt': ' || '.join(dict.fromkeys(descs))[:500],
        'layout_hierarchy_OBSERVED': clean(s0.get('hierarchy'))[:250], 'camera_motion_OBSERVED': clean(s0.get('camera_motion')),
        'beats_frame_class_MEASURED_start': ';'.join(f"{b['start_frame']}:{b['motion_class']}" for b in beats)[:300],
        'embedded_playback_present': emb, 'required_editable_layers': '|'.join(layers),
        'original_prompt_template': f"ORIGINAL artwork, house style of the new channel. Concept to express (new script beat {{BEAT}}): {concept}. Composition role: one clear focal subject, supporting elements revealed in reading order. Deliver as separate layers: {', '.join(layers)}. No source characters, captures, text or sequence.",
        'creative_instruction_label': 'CREATIVE_INSTRUCTION (not source observation)'})
with open(os.path.join(ROOT, 'tables/dna/reconstruction_specs_v2.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows), sum(r['story_function_INFERRED'] != 'UNAVAILABLE' for r in rows), sum(bool(r['readable_text_OBSERVED']) for r in rows), sum(bool(r['layout_hierarchy_OBSERVED']) for r in rows))
