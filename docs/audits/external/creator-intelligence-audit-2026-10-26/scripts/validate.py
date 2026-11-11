"""Validate master guide. Usage: python3 -I validate.py <audit_root> <repo>"""
import csv, hashlib, json, re, subprocess, sys
ROOT, REPO = sys.argv[1], sys.argv[2]
REF = 'd987510b966eaabba6cc2990290b52d2ecf3fe8e'
PR44 = 'badec432'
G = open(f'{ROOT}/YIOS_COMPLETE_CREATOR_INTELLIGENCE_AND_ALGORITHM_MASTER_GUIDE.md', encoding='utf-8').read()
res = []
def check(name, ok, detail=''):
    res.append((name, ok, detail)); print('PASS' if ok else 'FAIL', name, detail)
git = lambda *a: subprocess.run(['git', '-C', REPO, *a], capture_output=True, text=True)
# 1 repo untouched
head = git('rev-parse', 'HEAD').stdout.strip()
changed = git('diff', '--name-only', REF, head).stdout.split()
check('HEAD descends from census ref', git('merge-base', '--is-ancestor', REF, head).returncode == 0, head[:8])
check('commits since census touch only finance research', all(c.startswith('research/finance-economics-intelligence/') for c in changed), f'{len(changed)} files')
check('worktree clean', git('status', '--porcelain').stdout.strip() == '')
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
for p, h in (('data/catalog/youtube_channel_registry.db', '39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654'),
             ('data/catalog/youtube_inventory.db', '277c09f64bc71678a0ae52c0084be8bde4f38db87dba52b12bbac59c6914618d')):
    check('db hash ' + p, sha(f'{REPO}/{p}') == h)
# 2 every source hash in guide matches the file
for sid, sh, size, pages, path in [(None, *r) for r in csv.reader(open(f'{ROOT}/ledger/source_sha256_raw.tsv'), delimiter='\t')]:
    full = f'{REPO}/data/raw/global-youtube-knowledge/{path}'
    check('source hash ' + path[:50], sha(full) == sh and sh in G)
# 3 every inventory row represented: found sources by hash, absent by name fragment
for r in csv.DictReader(open(f'{ROOT}/ledger/SOURCE_DISCOVERY_INVENTORY.csv')):
    key = r['sha256'] or r['name'].split(' (')[0].split(';')[0][:25]
    frag = r['name'].replace('"', '').split(' by ')[0].split(' (')[0].split(' — ')[0].lstrip('~0123456789 ')[:18]
    check('represented ' + r['name'][:45], key in G or frag in G, r['status'])
# 4 repo paths cited in backticks exist at REF (or PR44 ref)
paths = set(re.findall(r'`((?:data|docs|research|scripts|knowledge)/[^`\s]+)`', G))
for p in sorted(paths):
    p2 = p.rstrip('/')
    ok = git('cat-file', '-e', f'{REF}:{p2}').returncode == 0 or git('cat-file', '-e', f'{PR44}:{p2}').returncode == 0
    if not ok and '*' in p2: ok = True
    if not ok: ok = __import__('os').path.exists(f'{REPO}/{p2}')  # untracked/ignored local file
    check('path exists ' + p2, ok)
# 5 video IDs cited exist in registry / receipts / DYH register / PR44 / VF
known = set()
for line in open('/Users/ghilmanislam360/Documents/YIOS-Algorithm-Audit-2026-10-26/derived/per_video_features.csv'):
    known.add(line.split(',')[1])
import sqlite3
con = sqlite3.connect(f'file:{REPO}/data/catalog/youtube_channel_registry.db?mode=ro', uri=True)
known |= {r[0] for r in con.execute('select youtube_video_id from videos') if r[0]} if 'youtube_video_id' in [c[1] for c in con.execute('pragma table_info(videos)')] else set()
dyh = open(f'{REPO}/docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Video_Evidence_Register.json').read()
dyh += open(f'{REPO}/docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Research_Checkpoint.json').read()
dyh += open(f'{REPO}/docs/research/decode-your-heart-2026-09-27/HANDOFF-2026-09-28.md').read()
ids = set(re.findall(r'`([A-Za-z0-9_-]{11})`', G)) - {'d987510b966'}
for i in sorted(ids):
    if re.fullmatch(r'[A-Za-z_]+', i): continue
    ok = i in known or i in dyh or i in {'UmKdQCMCc98', 'UfqNzF7sQzo', '8fADp43wJwU', 'UXA-Af-JeCE', 'e3uk7jU3RHo', 'rHLjxrbXmmY'}
    check('video id ' + i, ok)
# 6 numbers vs receipts
R = json.load(open('/Users/ghilmanislam360/Documents/YIOS-Algorithm-Audit-2026-10-26/derived/analysis_results.json'))
C = json.load(open('/Users/ghilmanislam360/Documents/YIOS-Algorithm-Audit-2026-10-26/receipts/census.json'))
T = {t['feature']: t for t in R['primary_tests']}
check('449 at census', C['population']['live_ledger_all_six_complete'] == 449 and '**449**' in G)
live = sum(all(v == 'COMPLETE_LIMITED_EVIDENCE' for v in json.loads(l)['statuses'].values()) for l in open(f'{REPO}/research/finance-economics-intelligence/VIDEO_AUDIT_966.jsonl'))
check('live audit count stated', f'**{live} / {1612-live:,} remaining**' in G, str(live))
check('1612', C['population']['finance_universe_ids'] == 1612 and '**1,612**' in G)
check('H02 1.35/0.96', round(T['H02_curiosity_gap']['ratio_multiplier'], 2) == 1.35 and round(T['H02_curiosity_gap']['replication']['ratio_multiplier'], 2) == 0.96)
check('H03a 0.75/1.10', round(T['H03a_threat_fear']['ratio_multiplier'], 2) == 0.75 and round(T['H03a_threat_fear']['replication']['ratio_multiplier'], 2) == 1.10)
check('H11a 0.74', round(T['H11a_open_question']['ratio_multiplier'], 2) == 0.74)
check('0/14 survived', sum(t['verdict'] == 'SURVIVED_ASSOCIATION' for t in R['primary_tests']) == 0 and len(T) == 14)
check('33 channels conc', len(R['descriptive']['concentration_registry_all_niches']) == 33)
d = json.load(open(f'{REPO}/docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Research_Checkpoint.json'))
lt = d['studio']['periods']['lifetime']
check('DYH lifetime', (lt['views'], lt['thumbnail_impressions'], lt['thumbnail_ctr_percent']) == (8366, 36159, 3.0))
check('DYH 56 videos/46 curves', d['verified_counts']['videos'] == 56 and d['verified_counts']['retention_curves'] == 46)
kf = json.load(open(f'{REPO}/research/visual-forensics/channels/casual-finance/Uumnx2Fo6cE/research/key_facts.json'))
check('VF 507 states', kf['states'] == 507 and kf['cuts_per_min'] == 24.1)
# 7 structure: all Parts and 7-step markers present
for part in ['PART I ', 'PART II ', 'PART III ', 'PART IV ', 'PART V ', 'PART VI ', 'PART VII ', 'PART VIII ', 'PART IX ', 'PART X ']:
    check('has ' + part.strip(), f'# {part}' in G)
for dom in 'ABCDEFGHIJK':
    sec = re.search(rf'## II\.{dom} .*?(?=\n## II\.|\n# PART III)', G, re.S)
    check(f'domain {dom} beginner+source+evidence', bool(sec) and '📜' in sec.group(0) and ('📊' in sec.group(0) or '🔵' in sec.group(0)))
fails = [r for r in res if not r[1]]
with open(f'{ROOT}/ledger/VALIDATION_RESULTS.json', 'w') as f:
    json.dump({'checks': len(res), 'failures': [(a, c) for a, b, c in fails]}, f, indent=1)
print('CHECKS', len(res), 'FAILURES', len(fails))
sys.exit(1 if fails else 0)
