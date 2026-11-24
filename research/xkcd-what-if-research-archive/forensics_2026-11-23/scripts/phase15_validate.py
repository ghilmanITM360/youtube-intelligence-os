"""Validate phase15 scene-coding outputs against the context CSV and merge into one CSV. usage: python3 -I scripts/phase15_validate.py <tranche>"""
import csv, json, os, sys, collections, glob
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P = A + '/phase15_scene_coding'; tr = sys.argv[1]
KEYS = 'video_id shot_id boundary_check q2_seen q3_concept q4_why_visual q5_moves q6_fixed q7_simplified q8_quantity q9_causality q10_next_change q11_effect q12_muted q13_accuracy q14_technique text_on_screen narration_check confidence'.split()
ctx = list(csv.DictReader(open(f'{P}/{tr}_context.csv'))); by = collections.defaultdict(list)
for r in ctx: by[r['video_id']].append(r)
rows = []; report = {}
for v, cs in by.items():
    f = f'{P}/out/{tr}_{v}.json'
    if not os.path.exists(f): report[v] = 'MISSING'; continue
    try: d = json.load(open(f))
    except Exception as e: report[v] = f'BAD_JSON {e}'; continue
    ok = len(d) == len(cs) and [x.get('shot_id') for x in d] == [c['shot_id'] for c in cs] and all(set(KEYS) <= set(x) for x in d)
    empty = sum(1 for x in d for k in KEYS if not str(x.get(k, '')).strip())
    report[v] = dict(ok=ok, n=len(d), expected=len(cs), empty_fields=empty, low=sum(x.get('confidence') == 'LOW' for x in d), q5_not_assessable=sum('NOT_ASSESSABLE' in str(x.get('q5_moves')) for x in d), false_prog=sum(x.get('boundary_check') == 'FALSE_PROGRESSIVE' for x in d))
    if ok:
        for x, c in zip(d, cs): rows.append({**{k: x.get(k, '') for k in KEYS}, 'narration_asr': c['asr_text'], 'start_s': c['start_s'], 'end_s': c['end_s'], 'layer': c.get('layer', ''), 'review': 'SAME_MODEL_SUBAGENT_SELF_REVIEW'})
if rows:
    w = csv.DictWriter(open(f'{P}/{tr}_SCENE_CODING.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(json.dumps(report, indent=1)); print(len(rows), 'rows merged of', len(ctx))
