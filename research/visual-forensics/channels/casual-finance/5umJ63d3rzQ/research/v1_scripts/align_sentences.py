#!/usr/bin/env python3
"""PROVISIONAL sentence-level alignment of ASR sentences (SENTENCES.csv, not human-verified) to composition groups. python3 -I."""
import csv, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = list(csv.DictReader(open(os.path.expanduser('~/Downloads/CasuallyFinance-Forensic-Research/02_VIDEO_FORENSICS/5umJ63d3rzQ/SENTENCES.csv'))))
G = list(csv.DictReader(open(os.path.join(ROOT, 'tables/integrated/composition_groups.csv'))))
for g in G: g['t0'] = (int(g['start']) + 1) / 30.0; g['t1'] = (int(g['end']) + 1) / 30.0
out = []
for s in S:
    a, b = float(s['start_sec']), float(s['end_sec'])
    hit = [g for g in G if g['t0'] < b and g['t1'] > a]
    out.append({'sentence_id': s['sentence_id'], 'start_sec': a, 'end_sec': b, 'text': s['text'], 'n_groups': len(hit),
                'first_group': hit[0]['group'] if hit else '', 'last_group': hit[-1]['group'] if hit else '',
                'visual_changes_per_sec': round(len(hit) / max(b - a, 0.01), 2), 'status': 'PROVISIONAL_ASR_ALIGNMENT'})
with open(os.path.join(ROOT, 'tables/integrated/script_visual_alignment.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
import statistics as st
print(len(out), 'sentences; no-group:', sum(1 for o in out if o['n_groups'] == 0), '; median groups/sentence', st.median(o['n_groups'] for o in out), '; median changes/sec', st.median(o['visual_changes_per_sec'] for o in out))
print('groups per minute overall:', round(len(G) / (752.847 / 60), 1))
