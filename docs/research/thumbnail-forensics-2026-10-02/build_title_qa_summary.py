"""Summarise manual title QA (150-title stratified sample + 40-title v2 re-check) into title-qa-summary.json."""
import csv, glob, json, math, subprocess
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
M = dict(clarity='clarity_score', specificity='specificity_score', curiosity='curiosity_score', promise_strength='promise_strength_score', credibility='credibility_score', audience_fit='audience_fit_score', concision='concision_score')
mean = lambda v: sum(v) / len(v)


def pearson(a, b):
    ma, mb = mean(a), mean(b); num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    return num / math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))


base = {}
for f in sorted(glob.glob(str(HERE / 'title-analyst-audit-T-*.json'))):
    rel = Path(f).relative_to(HERE.parents[2])
    for r in json.loads(subprocess.run(['git', 'show', f'8711eed:{rel}'], cwd=HERE.parents[2], capture_output=True, text=True, check=True).stdout): base[r['Video_ID']] = r
rev = [x for k in range(1, 7) for x in json.load((HERE / f'title-qa-review-{k}.json').open())]
sel = json.load((HERE / 'title-qa-selection.json').open())
tf = {r['Video_ID']: r for r in csv.DictReader((HERE / 'title-forensics.csv').open())}
mp = {r['Video_ID']: r for r in csv.DictReader((HERE / 'master-packages.csv').open())}
log = list(csv.DictReader((HERE / 'title-qa-corrections-log.csv').open()))
sample_log = [l for l in log if l['Source'].startswith('SAMPLE')]
iss = [(x['Video_ID'], i) for x in rev for i in x['issues']]
cls = Counter(i['class'] for _, i in iss)
by_layer = {L: Counter(i['class'] for _, i in iss if i['layer'] == L) for L in ('PROGRAMMATIC', 'ANALYST')}
rows_with = lambda f: len({v for v, i in iss if f(i)})
A = [base[x['Video_ID']]['score_100'] for x in rev]; B = [x['blind']['total'] for x in rev]; dif = [a - b for a, b in zip(A, B)]
comp = {c: round(mean([base[x['Video_ID']][m] - x['blind']['scores'][c] for x in rev]), 2) for c, m in M.items()}
cover = dict(channels=len({tf[v]['Channel_ID'] for v in sel['video_ids']}), channels_with_videos=len({t['Channel_ID'] for t in tf.values()}), formats=dict(Counter(tf[v]['Format'] for v in sel['video_ids'])),
             perf=dict(Counter(mp[v]['Relative_Performance_Class'] for v in sel['video_ids'])), archetype_v1_basis=dict(Counter(r['Title_Archetype'] for r in map(lambda v: tf[v], sel['video_ids']))),
             health_flag=dict(Counter(base[v]['medical_title_flag'] for v in sel['video_ids'])), number_titles=sum(tf[v]['Number_Present'] == '1' for v in sel['video_ids']),
             unmet_quota=sel['unmet_quota'])
re7 = None
p7 = HERE / 'title-qa-review-7.json'
if p7.exists():
    r7 = json.load(p7.open()); i7 = [i for x in r7 for i in x['issues']]
    re7 = dict(sample=len(r7), rows_with_any_issue=sum(1 for x in r7 if x['issues']), issues_by_class=dict(Counter(i['class'] for i in i7)), issues_by_field=dict(Counter(i['field'] for i in i7)),
               rows_clean_or_subjective_only=sum(1 for x in r7 if all(i['class'] in ('SUBJECTIVE', 'STYLE_ONLY') for i in x['issues'])))
out = dict(
    sample_size=len(rev), sampling='deterministic hash-seeded greedy stratified cover (title_qa_select.py); six independent blind-first reviewers x 25 titles', coverage=cover,
    issues_total=len(iss), issues_by_class=dict(cls), issues_by_layer={k: dict(v) for k, v in by_layer.items()},
    rows=dict(with_any_issue=len({v for v, _ in iss}), with_non_subjective_issue=rows_with(lambda i: i['class'] in ('MATERIAL_ERROR', 'MINOR_FACTUAL', 'CLASSIFICATION')),
              with_analyst_non_subjective_issue=rows_with(lambda i: i['layer'] == 'ANALYST' and i['class'] in ('MATERIAL_ERROR', 'MINOR_FACTUAL', 'CLASSIFICATION')),
              with_programmatic_issue=rows_with(lambda i: i['layer'] == 'PROGRAMMATIC'), clean=sum(1 for x in rev if x['verdict'] == 'CLEAN')),
    material_errors=[dict(Video_ID=v, layer=i['layer'], field=i['field'], current=i['current'], proposed=i['proposed']) for v, i in iss if i['class'] == 'MATERIAL_ERROR'],
    analyst_score_vs_blind_reviewer=dict(n=len(rev), mean_diff=round(mean(dif), 2), mean_abs_diff=round(mean([abs(d) for d in dif]), 2), within_12=sum(abs(d) <= 12 for d in dif), gap_ge_20=sum(abs(d) >= 20 for d in dif),
                                         pearson=round(pearson(A, B), 3), sd_analyst=round(math.sqrt(mean([(a - mean(A)) ** 2 for a in A])), 1), sd_reviewer=round(math.sqrt(mean([(b - mean(B)) ** 2 for b in B])), 1), mean_component_diff_analyst_minus_reviewer=comp),
    corrections_log=dict(total_rows=len(log), by_status=dict(Counter(l['Status'] for l in log)), sample_rows=len(sample_log), systematic_mechanical=sum(l['Source'] == 'SYSTEMATIC_MECHANICAL_ALL_ROWS' for l in log)),
    programmatic_rule_fixes=['curly apostrophes/quotes normalised before regex matching (117 titles had defeated n\'t/’ patterns)', 'Question_Form = literal ? or interrogative opener (How to / Why X / Do this no longer questions)',
                             'genuine ?-questions keep archetype QUESTION; Why-led titles do not fire WARNING/MISTAKE/STOP_DOING/AVOID/DO_THIS or Warning/Mistake/Urgency frames', 'DOCTOR_WARNS needs a warning verb; any *ologist/surgeon counts as a doctor',
                             'HEALTH vocabulary extended (nails, feet, stool, covid, vaccines, clove, ...); Health_Topic=1 for every SENIOR_HEALTH-channel title', 'claim types: bare "health" no longer matches REVERSAL; "Instant Oatmeal" no longer INSTANT_CURE; EXAGGERATED_BENEFIT added',
                             'Urgency_Frame no longer fires on bare "before" or calendar years; Fear_Frame adds irreversible/poison/strain/harm/damage', 'List_Form counts "These 4 Habits"/"All 32 States"; units (kg, lbs, cups) no longer make a list', 'overpromise proxy fires on by-morning/flush/melt/N kg/Nx/in N hours'],
    analyst_mechanical_fix='unnecessary_words: negation words (never/not/no/stop/...) and items absent from the title removed project-wide; each removal logged',
    analyst_not_rewritten=True, post_fix_recheck=re7,
    known_limitations=['Title_Archetype primary is first-match in a fixed priority list; Title_Archetypes_All is the authoritative multi-label field and should be used for pattern mining', 'Hope/Positive/Secret/Transformation/Authority_Frame regexes are coarse keyword frames (reviewers disagreed on ~3-7 of 150 rows each)',
                       'Age_Number_Present means senior-age (55+) markers only', 'named-person authority (e.g. "Warren Buffett") is not detected as Authority_Cue'],
    status='PASS_WITH_CORRECTIONS')
(HERE / 'title-qa-summary.json').write_text(json.dumps(out, indent=1))
print(json.dumps({k: out[k] for k in ('sample_size', 'issues_by_class', 'rows', 'analyst_score_vs_blind_reviewer', 'corrections_log', 'post_fix_recheck')}, indent=1))
