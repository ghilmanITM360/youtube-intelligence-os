"""Framework-version delta tasks: reassessed videos whose record predates the current rule set.
A video is due a targeted delta review for every rule in the current index that its record never compared (reusing its existing observations).
Usage: python delta_tasks.py   -> writes FRAMEWORK_DELTA_TASKS.csv (empty rule list means no delta)."""
import csv, json, pathlib
H = pathlib.Path(__file__).resolve().parent
rules = {r['Rule_ID'] for r in csv.DictReader(open(H.parent / 'reference-framework/REFERENCE_RULE_INDEX_v1.csv')) if r['Rule_Kind'] != 'NOT_APPLICABLE'}
rows = []
for p in sorted((H / 'videos').glob('*.json')):
    d = json.load(open(p)); seen = {c['rule_id'] for c in d['comparisons']}
    rows.append({'video_id': d['video_id'], 'record_framework_version': d['framework_version'], 'rules_in_current_index': len(rules), 'rules_compared': len(seen & rules),
                 'not_yet_compared': '|'.join(sorted(rules - seen))})
w = csv.DictWriter(open(H / 'FRAMEWORK_DELTA_TASKS.csv', 'w', newline=''), list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), 'records;', sum(1 for r in rows if r['not_yet_compared']), 'with uncompared rules')
