"""Apply package-QA findings (package-qa-review-K.json) to package-audit-PK-NN.json and log every event in package-qa-corrections-log.csv.
Starts from the committed pre-QA state (BASE) so reruns are idempotent. MATERIAL/MINOR_FACTUAL/CLASSIFICATION findings with a valid concrete corrected_value are applied; SUBJECTIVE and STYLE_ONLY are logged only.
score_100 is recomputed. Sampled rows get qa_status QA_SAMPLED."""
import csv, glob, json, subprocess
from collections import Counter
from pathlib import Path
import validate_package_audit as V

HERE = Path(__file__).resolve().parent
BASE = '2c6c197ff1a7b6759a861f87ce67a2059c99c4f9'
APPLY = {'MATERIAL_ERROR', 'MINOR_FACTUAL_ERROR', 'CLASSIFICATION_ERROR'}
YN, YPN = set(V.YN), set(V.YPN)


MANUAL = {  # reviewer corrections whose proposed text exceeded the word limit or needed a companion edit; coordinator shortened them, meaning unchanged
    ('PKG-ciWCTKap5ZM', 'thumbnail_says'): "'START HERE' with a black arrow from the headline down to a green piggy bank; a man holds a coin, cash stacks right.",
    ('PKG-AhW5FoY9oOQ', 'thumbnail_says'): 'NEVER TAKE BP PILLS AT THIS TIME, then STOP NOW, beside a pill bottle and a large red clock showing about 5:10.',
    ('PKG-BfBpog8OgSY', 'thumbnail_says'): 'A snowy park scene: a SPY-labelled soldier in a greatcoat walks toward the camera, away from two seated officers, one tagged HITLER.',
    ('PKG-suBe29FPt4Q', 'thumbnail_says'): 'THE BILLIONAIRE TRAP, 95% END UP BROKE: a podium winner holds MY SECRETS books under a COPY ME! banner, beside broke people.',
    ('PKG-mhb_Nd-0VjQ', 'thumbnail_says'): "'BUY THIS ETF NOW!' with a grinning cartoon man pointing at the headline above ETF 1, 2, 3 bars, rising arrow, money sack.",
    ('PKG-bsJ25LPIMDI', 'title_only_information'): 'NONE',
    ('PKG-0aiVrlKNMeM', 'primary_relationship'): 'REDUNDANT',  # also appends REDUNDANT to relationships
    ('PKG-rA9Osr-7fQo', 'thumbnail_only_information'): 'A blue couch, an open laptop angled away, a mug and a man seated upright, fists on knees, in diagonal window light; no numbers.',
}


def load(pk):
    rel = (HERE / f'package-audit-{pk}.json').relative_to(HERE.parents[2])
    return json.loads(subprocess.run(['git', 'show', f'{BASE}:{rel}'], cwd=HERE.parents[2], capture_output=True, text=True, check=True).stdout)


def set_value(r, f, v):
    if f in V.MAX: ok = isinstance(v, int) or str(v).strip().isdigit(); v = int(v) if ok else v; ok = ok and 0 <= v <= V.MAX[f]
    elif f in YN: ok = v in ('Y', 'N')
    elif f in YPN: ok = v in ('YES', 'PARTIAL', 'NO')
    elif f in V.ENUM: ok = v in V.ENUM[f]
    elif f == 'relationships':
        v = [x.strip() for x in v.replace(',', ';').split(';')] if isinstance(v, str) else v; ok = bool(v) and set(v) <= V.REL
    elif f == 'primary_relationship': ok = v in V.REL and v in r['relationships']
    elif f in V.WORDS: ok = isinstance(v, str) and 2 <= len(v.split()) <= V.WORDS[f] + 4
    else: ok = False
    if ok: r[f] = v
    return ok


def main():
    batches = {}
    for pk in sorted(json.load((HERE / 'package-batch-plan.json').open())['batches']): batches[pk] = load(pk)
    idx = {r['Package_ID']: r for rows in batches.values() for r in rows}
    sel = {p for v in json.load((HERE / 'package-qa-selection.json').open()).values() for p in v}
    log = []
    for f in sorted(glob.glob(str(HERE / 'package-qa-review-*.json'))):
        d = json.load(open(f))
        for rv in d['rows']:
            r = idx[rv['Package_ID']]
            for n, e in enumerate(rv['errors']):
                st, applied = 'LOGGED_NOT_APPLIED', ''
                if e['error_class'] in APPLY:
                    if e['field'] == 'primary_relationship' or e['field'] == 'relationships': pass
                    key = (rv['Package_ID'], e['field'])
                    if key in MANUAL:
                        if e['field'] == 'primary_relationship' and MANUAL[key] not in r['relationships']: r['relationships'].append(MANUAL[key])
                        if e['field'] == 'primary_relationship': r[e['field']] = MANUAL[key]; ok = True
                        else: r[e['field']] = MANUAL[key]; ok = True
                        st = 'APPLIED_MANUAL_SHORTENED'
                    else: st = 'APPLIED' if set_value(r, e['field'], e['corrected_value']) else 'MANUAL_REVIEW_NEEDED'
                    applied = r.get(e['field'], '') if st.startswith('APPLIED') else ''
                else: st = 'NOT_APPLIED_' + e['error_class'].split('_')[0]
                log.append(dict(Package_ID=rv['Package_ID'], Reviewer=d['reviewer'], Field=e['field'], Error_Class=e['error_class'], Original_Value=e['original_value'], Proposed_Value=e['corrected_value'], Status=st, Applied_Value=applied, Reason=e['reason'], Evidence=e.get('evidence', '')))
    for r in idx.values():
        r['score_100'] = sum(r[k] for k in V.MAX); r['qa_status'] = 'QA_SAMPLED' if r['Package_ID'] in sel else 'NOT_SAMPLED'
    for pk, rows in batches.items(): json.dump(rows, open(HERE / f'package-audit-{pk}.json', 'w'), indent=1, ensure_ascii=False)
    with (HERE / 'package-qa-corrections-log.csv').open('w', newline='') as fh:
        w = csv.DictWriter(fh, list(log[0])); w.writeheader(); w.writerows(log)
    print(len(log), dict(Counter(l['Status'] for l in log)))
    return log


if __name__ == '__main__': main()
