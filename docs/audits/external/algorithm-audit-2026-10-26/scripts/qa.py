"""Independent QA: numbers quoted in the reports must equal receipts. Usage: python3 -I qa.py <audit_root> <repo>"""
import hashlib, json, math, os, re, subprocess, sys

ROOT, REPO = sys.argv[1], sys.argv[2]
R = json.load(open(f'{ROOT}/derived/analysis_results.json'))
C = json.load(open(f'{ROOT}/receipts/census.json'))
T = {t['feature']: t for t in R['primary_tests']}
D = R['descriptive']
fails = []


def check(name, got, want, tol=0.005):
    ok = abs(got - want) <= tol if isinstance(want, float) else got == want
    print(('PASS' if ok else 'FAIL'), name, got, want)
    if not ok:
        fails.append(name)


check('deep complete 449', C['population']['live_ledger_all_six_complete'], 449)
check('universe 1612', C['population']['finance_universe_ids'], 1612)
check('universe stale 430', C['population']['universe_audit_status_frozen_2026_10_21']['DEEP_AUDIT_COMPLETE'], 430)
check('registry videos', C['population']['registry_db_videos'], 2303)
check('rated originals 723', R['populations']['original_966_with_ratio'], 723)
check('replication rated 418', sum(R['populations']['replication_with_ratio'].values()), 418)
check('benchmark reproduces stored', R['benchmark_reimplementation']['max_abs_rel_diff'] < 1e-4, True)
for f, m, q in (('H02_curiosity_gap', 1.349, .042), ('H03a_threat_fear', .751, .042), ('H03b_opportunity', 1.276, .089), ('H11a_open_question', .735, .042), ('H01_money_amount', 1.069, .742)):
    check(f + ' mult', round(T[f]['ratio_multiplier'], 3), m, .0011)
    check(f + ' q', round(T[f]['q_bh'], 3), q, .0011)
check('H02 replication', round(T['H02_curiosity_gap']['replication']['ratio_multiplier'], 2), .96, .006)
check('H05 replication', round(T['H05_explicit_audience']['replication']['ratio_multiplier'], 2), .50, .006)
check('no SURVIVED verdicts', sum(t['verdict'] == 'SURVIVED_ASSOCIATION' for t in R['primary_tests']), 0)
check('variance share fin', D['variance_share_originals']['between_channel_share_of_variance_log_vpd'], .378, .0005)
check('variance share all', D['variance_share_registry']['between_channel_share_of_variance_log_vpd'], .575, .0005)
conc = sorted(x['top10pct_share_of_views'] for x in D['concentration_registry_all_niches'].values())
check('concentration median', conc[len(conc) // 2], .669, .0005)
sl = sorted(x['slope'] for x in D['age_slope_originals'].values())
check('age slope fin median', sl[len(sl) // 2], .343, .0005)
sl = sorted(x['slope'] for x in D['age_slope_registry_all_niches'].values())
check('age slope all median', sl[len(sl) // 2], .574, .0005)
p = R['prediction']['splits']
check('temporal model not better', p[0]['mae_model'] >= p[0]['mae_baseline_peer_median'], True)
check('unseen model not better', p[1]['mae_model'] >= p[1]['mae_baseline_peer_median'], True)
check('gain CI spans 0', p[0]['mae_gain_vs_baseline_ci95'][0] < 0 < p[0]['mae_gain_vs_baseline_ci95'][1], True)
lr = R['continuous']['like_rate_vs_ratio']
check('like-rate negative 9/9', sum(v['spearman_likerate_vs_ratio'] < 0 for v in lr.values()), 9)

# repository untouched: DB hashes equal census-time hashes, worktree clean, HEAD unchanged
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
for d in C['sqlite']:
    check('unchanged ' + d['path'], sha(f"{REPO}/{d['path']}"), d['sha256'])
check('HEAD unchanged', subprocess.run(['git', '-C', REPO, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip(), C['repo_head'])
check('worktree clean', subprocess.run(['git', '-C', REPO, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip(), '')

# every video ID cited in reports exists in some source table
ids = set()
for line in open(f'{ROOT}/derived/per_video_features.csv'):
    ids.add(line.split(',')[1])
cited = set()
for f in os.listdir(ROOT):
    if f.endswith(('.md', '.csv')):
        cited |= set(re.findall(r'`([A-Za-z0-9_-]{11})`', open(f'{ROOT}/{f}').read()))
        if f.endswith('.csv'):
            cited |= {x for x in re.findall(r'(?<![A-Za-z0-9_-])([A-Za-z0-9_-]{11})(?![A-Za-z0-9_-])', open(f'{ROOT}/{f}').read()) if re.search(r'[A-Z]', x) and re.search(r'[a-z]', x) and re.search(r'\d', x)}
whatif = {'8fADp43wJwU', 'UXA-Af-JeCE', 'e3uk7jU3RHo', 'UmKdQCMCc98', 'UfqNzF7sQzo'}
missing = sorted(c for c in cited - ids - whatif if not re.fullmatch(r'[A-Za-z_]+', c))  # skip plain words like `Demand_type`
check('cited IDs resolvable', missing, [])
print('FAILURES:', fails)
sys.exit(1 if fails else 0)
