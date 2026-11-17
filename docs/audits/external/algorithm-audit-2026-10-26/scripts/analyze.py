"""Hypothesis tests, replication, prediction and descriptive stats for the YIOS algorithm audit.

Usage: python3 -I analyze.py <repo_root> <out_dir>
Stdlib only (no numpy installed; no new deps). Read-only on the repository. Seeded RNG -> reproducible.
Outcome = log(lifetime views/day / median of same-channel, same-format, same-snapshot nearest-age peers),
the project's own METHODS.md benchmark, re-implemented here so replication sets use the identical rule.
"""
import csv, io, json, math, os, random, re, sqlite3, statistics as S, subprocess, sys, collections as C
from datetime import datetime, timezone

REPO, OUT = sys.argv[1], sys.argv[2]
FIN = f'{REPO}/research/finance-economics-intelligence'
CF_REF = 'origin/research/casually-finance-success-playbook'
CF_PATH = 'research/casually-finance-success-playbook/VIDEO_PERFORMANCE.csv'
RNG = random.Random(20261026)
B_PERM, B_BOOT = 4000, 1500
csv.field_size_limit(10**9)


def git_show(ref, path):
    return subprocess.run(['git', '-C', REPO, 'show', f'{ref}:{path}'], capture_output=True, text=True, check=True).stdout


def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def parse_ts(s):
    try:
        return datetime.fromisoformat(s.replace('Z', '+00:00')).astimezone(timezone.utc)
    except Exception:
        return None


# ---------------- peer benchmark (same rule as build_baseline.compare) ----------------
def peer_ratios(vids):
    """vids: dicts with id, ch, fmt, snap, age, views. Adds 'ratio','peers'."""
    groups = C.defaultdict(list)
    for v in vids:
        if v['age'] and v['age'] >= 7 and v['views'] is not None and v['fmt'] in ('LONG_FORM', 'SHORTS'):
            groups[(v['ch'], v['fmt'], v['snap'])].append(v)
    for v in vids:
        v.setdefault('ratio', None)
        g = groups.get((v['ch'], v['fmt'], v['snap']))
        if not g or v not in g:
            continue
        peers = sorted((p for p in g if p is not v and 0.5 <= p['age'] / v['age'] <= 2),
                       key=lambda p: (abs(p['age'] - v['age']), p['id']))[:10]
        if len(peers) < 5:
            continue
        base = S.median(p['views'] / p['age'] for p in peers)
        if base > 0 and v['views'] > 0:
            v['ratio'] = v['views'] / v['age'] / base
            v['peers'] = len(peers)


# ---------------- data loading ----------------
def load_originals():
    rows = list(csv.DictReader(open(f'{FIN}/VIDEO_AUDIT_966.csv', newline='')))
    led = {}
    for l in open(f'{FIN}/VIDEO_AUDIT_966.jsonl'):
        r = json.loads(l)
        led[r['Video_ID']] = r
    db = sqlite3.connect(f'file:{REPO}/data/catalog/youtube_channel_registry.db?mode=ro', uri=True)
    tx = {}
    for vid, t in db.execute('select youtube_video_id, transcript_text from transcripts where is_placeholder=0 and length(transcript_text)>=200'):
        tx[vid] = t
    out = []
    for r in rows:
        L = led[r['Video_ID']]
        out.append({
            'id': r['Video_ID'], 'ch': r['Channel'], 'title': r['Title'], 'set': 'ORIGINAL_966',
            'fmt': r['Format'], 'snap': r['Metric_snapshot_date'], 'age': fnum(r['Age_days']),
            'views': fnum(r['Views']), 'dur': fnum(r['Duration_seconds']), 'pub': parse_ts(r['Published_at_raw']),
            'likes': fnum(r['likes']), 'comments': fnum(r['comments']),
            'project_ratio': fnum(r['Lifetime_rate_ratio']), 'project_tier': r['Performance_tier'],
            'deep': all(v == 'COMPLETE_LIMITED_EVIDENCE' for v in L['statuses'].values()),
            'opening': ' '.join((tx.get(r['Video_ID']) or '').split()[:60]) or None,
            'thumb_text': (L.get('thumbnail') or {}).get('analysis') or '',
        })
    peer_ratios(out)
    return out


def load_replication():
    out = []
    for sub, label in (('expansion-12-channel-2026-10-20', 'EXPANSION_197'), ('expansion-monkey-explains-1999-2026-10-21', 'EXPANSION_MONKEY_63')):
        for r in csv.DictReader(open(f'{FIN}/{sub}/FINANCE_EXPANSION_MASTER.csv', newline='')):
            fmt = {'REGULAR': 'LONG_FORM', 'SHORT': 'SHORTS'}.get(r['video_type'], 'UNKNOWN')
            out.append({'id': r['video_id'], 'ch': r['channel_name'], 'title': r['title'], 'set': label, 'fmt': fmt,
                        'snap': (r.get('metadata_retrieval_timestamp_utc') or '')[:10], 'age': fnum(r['video_age_days_at_retrieval']),
                        'views': fnum(r['view_count']), 'dur': fnum(r['duration_seconds']), 'pub': parse_ts(r['publication_timestamp_utc']),
                        'likes': fnum(r['like_count']), 'comments': fnum(r['comment_count']), 'opening': None})
    for r in csv.DictReader(io.StringIO(git_show(CF_REF, CF_PATH))):
        fmt = {'LONG': 'LONG_FORM', 'LONG_FORM': 'LONG_FORM', 'SHORT': 'SHORTS', 'SHORTS': 'SHORTS'}.get(r['Format'].upper(), 'UNKNOWN')
        out.append({'id': r['Video_ID'], 'ch': 'Casually Finance', 'title': r['Title'], 'set': 'CASUALLY_FINANCE_206', 'fmt': fmt,
                    'snap': r['Snapshot_Date'][:10], 'age': fnum(r['Age_Days']), 'views': fnum(r['Public_Views']),
                    'dur': fnum(r['Duration_Sec']), 'pub': parse_ts(r['Publish_Date']), 'likes': None, 'comments': None, 'opening': None})
    peer_ratios(out)
    return out


# ---------------- pre-registered features (fixed before any outcome was inspected in this audit) ----------------
TITLE_FEATURES = {
    'H01_money_amount': r'\$\s?\d|\b\d[\d,.]*\s?(k|m|b|thousand|million|billion|trillion)\b|\b\d{1,3}(,\d{3})+\b',
    'H02_curiosity_gap': r"\b(why|secret|secrets|truth|nobody|no one|hidden|actually|real reason|what happens|not what you think|they don't|won't tell|don't know|the problem with|surprising|shocking)\b",
    'H03a_threat_fear': r'\b(crash|crashing|collapse|collapsing|broke|poor|poverty|lose|losing|lost|mistake|mistakes|warning|trap|scam|danger|dangerous|crisis|destroy|destroying|ruin|ruined|dying|dead|death|fail|failing|bankrupt|recession|bubble|worst|never|stop|disaster|panic)\b',
    'H03b_opportunity': r'\b(rich|richer|wealth|wealthy|millionaire|millionaires|passive income|retire early|financial freedom|make money|earn|earning|profit|build wealth|get ahead|win|winning)\b',
    'H04_first_person': r"\b(i|i'm|i've|my|me)\b",
    'H05_explicit_audience': r"\b(if you|for beginners|beginner|beginners|in your \d0s|\d0s|over \d+|under \d+|retirees|millennials|gen z|parents|middle class|average american|young people|students|age \d+)\b",
    'H06_question_mark': r'\?',
    'H07_list_count': r'^\s*\d+\s|\b\d+\s(ways|things|reasons|habits|signs|rules|steps|mistakes|lessons|money|stocks|investments|jobs)\b',
    'H10_timely_marker': r"\b(20(1\d|2\d)|now|today|this week|this year|just|breaking|new law|election|trump|tariff|tariffs|fed|rate cut|is coming|has landed)\b",
}
OPENING_FEATURES = {
    'H11a_open_question': r'\?',
    'H11b_open_personal_story': r"\b(i was|when i|i remember|my (wife|dad|mom|father|mother|friend|first)|i grew up|i used to)\b",
    'H11c_open_imagine': r'\b(imagine|picture this|what if)\b',
    'H11d_open_number': r'\$\s?\d|\b\d+\s?(%|percent)|\b\d{2,}\b',
    'H11e_open_contrarian': r"\b(most people|everyone thinks|you've been told|wrong|myth|lie|nobody tells|they don't want)\b",
}
TOPICS = [  # verbatim from build_baseline.TOPICS (project heuristic, keyword not semantic)
    ('retirement', r'retir|pension|social security|401k|401\(k\)'),
    ('housing_mortgages', r'hous|mortgage|rent\b|real estate|homeowner|home buy'),
    ('debt_credit_banking', r'debt|credit|bank|loan|borrow'),
    ('investing', r'invest|stock|portfolio|dividend|index fund|etf|s&p|compound'),
    ('macro_policy', r'inflat|econom|recession|interest rate|central|federal reserve|tariff|gdp'),
    ('business_models', r'business|company|companies|tesla|byd|costco|profit'),
    ('personal_finance', r'money|wealth|rich|poor|paycheck|salary|saving|budget|spend|financial'),
    ('economic_history', r'crash|depression|history|1973|2008|1929'),
    ('geopolitics', r'china|japan|america|europe|war|country|countries')]
THUMB_FEATURES = {  # coded from analyst prose; analysts saw outcomes -> exploratory only
    'T01_thumb_arrow': r'arrow', 'T02_thumb_red': r'\bred\b', 'T03_thumb_face_expression': r'\bface\b|expression',
    'T04_thumb_number_or_dollar': r'\$\d|\$|\bnumbers? (shown|visible)|\d+[kKmM%]', 'T05_thumb_no_text': r'no (visible )?(text|words)',
}


def flag(pat, s):
    return bool(s) and bool(re.search(pat, s, re.I))


def add_features(v):
    t = v['title'] or ''
    for k, p in TITLE_FEATURES.items():
        v[k] = flag(p, t)
    v['H12_title_chars_long'] = None  # set per-channel later (above channel median)
    for k, p in OPENING_FEATURES.items():
        v[k] = flag(p, v['opening']) if v.get('opening') else None
    for k, p in THUMB_FEATURES.items():
        v[k] = flag(p, v.get('thumb_text')) if v.get('deep') else None
    v['topics'] = [n for n, p in TOPICS if re.search(p, t, re.I)]


# ---------------- statistics ----------------
def y(v):
    return math.log(v['ratio']) if v.get('ratio') else None


def strata(rows, feat):
    by = C.defaultdict(lambda: ([], []))
    for v in rows:
        if y(v) is None or v.get(feat) is None:
            continue
        by[(v['ch'], v['fmt'])][1 if v[feat] else 0].append(y(v))
    return {k: g for k, g in by.items() if len(g[0]) >= 2 and len(g[1]) >= 2}


def weighted_diff(st):
    num = den = 0.0
    for a0, a1 in st.values():
        w = len(a0) * len(a1) / (len(a0) + len(a1))
        num += w * (S.mean(a1) - S.mean(a0))
        den += w
    return num / den if den else None


def perm_p(st, obs):
    if obs is None:
        return None
    cells = [(a0 + a1, len(a1)) for a0, a1 in st.values()]
    hits = 0
    for _ in range(B_PERM):
        fake = {}
        for i, (pool, n1) in enumerate(cells):
            sh = pool[:]
            RNG.shuffle(sh)
            fake[i] = (sh[n1:], sh[:n1])
        if abs(weighted_diff(fake)) >= abs(obs) - 1e-12:
            hits += 1
    return (hits + 1) / (B_PERM + 1)


def boot_ci(st):
    vals = []
    for _ in range(B_BOOT):
        fake = {k: ([RNG.choice(a0) for _ in a0], [RNG.choice(a1) for _ in a1]) for k, (a0, a1) in st.items()}
        vals.append(weighted_diff(fake))
    vals.sort()
    return vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals)) - 1]


def bh(ps):
    idx = sorted(range(len(ps)), key=lambda i: ps[i])
    q, prev = [None] * len(ps), 1.0
    for rank, i in reversed(list(enumerate(idx, 1))):
        prev = min(prev, ps[i] * len(ps) / rank)
        q[i] = prev
    return q


def test(rows, feat, full=True):
    st = strata(rows, feat)
    obs = weighted_diff(st)
    res = {'feature': feat, 'n_with': sum(len(g[1]) for g in st.values()), 'n_without': sum(len(g[0]) for g in st.values()),
           'strata': len(st), 'effect_log': obs, 'ratio_multiplier': math.exp(obs) if obs is not None else None}
    if obs is None or not full:
        return res
    res['p_perm'] = perm_p(st, obs)
    lo, hi = boot_ci(st)
    res['ci95_multiplier'] = [math.exp(lo), math.exp(hi)]
    loco = []
    for ch in {k[0] for k in st}:
        e = weighted_diff({k: g for k, g in st.items() if k[0] != ch})
        if e is not None:
            loco.append((ch, math.exp(e)))
    res['loco_min'] = min((x[1] for x in loco), default=None)
    res['loco_max'] = max((x[1] for x in loco), default=None)
    res['loco_sign_flips'] = [c for c, m in loco if (m > 1) != (math.exp(obs) > 1)]
    per = {f'{k[0]}|{k[1]}': (len(g[1]), len(g[0]), math.exp(S.mean(g[1]) - S.mean(g[0]))) for k, g in st.items()}
    res['per_stratum'] = per
    res['strata_same_sign'] = sum(1 for _, _, m in per.values() if (m > 1) == (math.exp(obs) > 1))
    return res


def examples(rows, feat, k=3):
    w = sorted((v for v in rows if v.get(feat) and v.get('ratio')), key=lambda v: v['ratio'])
    f = lambda v: {'id': v['id'], 'ch': v['ch'], 'title': v['title'], 'ratio': round(v['ratio'], 3)}
    return {'strongest': [f(v) for v in w[-k:][::-1]], 'weakest': [f(v) for v in w[:k]]}


def ols(X, Y, lam=0.0):
    """Ridge via normal equations + Gauss-Jordan; X rows include intercept as col 0 (unpenalized)."""
    p = len(X[0])
    A = [[sum(r[i] * r[j] for r in X) + (lam if i == j and i else 0) for j in range(p)] for i in range(p)]
    b = [sum(r[i] * yy for r, yy in zip(X, Y)) for i in range(p)]
    M = [A[i] + [b[i]] for i in range(p)]
    for c in range(p):
        piv = max(range(c, p), key=lambda r: abs(M[r][c]))
        M[c], M[piv] = M[piv], M[c]
        if abs(M[c][c]) < 1e-12:
            continue
        for r in range(p):
            if r != c:
                f = M[r][c] / M[c][c]
                M[r] = [a - f * bb for a, bb in zip(M[r], M[c])]
    return [M[i][p] / M[i][i] if abs(M[i][i]) > 1e-12 else 0.0 for i in range(p)]


def spearman(a, b):
    def rank(x):
        o = sorted(range(len(x)), key=lambda i: x[i])
        r = [0.0] * len(x)
        i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and x[o[j + 1]] == x[o[i]]:
                j += 1
            for k in range(i, j + 1):
                r[o[k]] = (i + j) / 2
            i = j + 1
        return r
    ra, rb = rank(a), rank(b)
    ma, mb = S.mean(ra), S.mean(rb)
    num = sum((x - ma) * (y_ - mb) for x, y_ in zip(ra, rb))
    den = math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y_ - mb) ** 2 for y_ in rb))
    return num / den if den else None


PRED_FEATS = list(TITLE_FEATURES) + ['title_len_z', 'dur_log_z']


def design(v, ch_stats):
    m = ch_stats.get(v['ch'], {})
    tl = (len(v['title']) - m.get('tl_mu', 0)) / (m.get('tl_sd') or 1)
    dl = ((math.log(v['dur']) if v['dur'] else m.get('dl_mu', 0)) - m.get('dl_mu', 0)) / (m.get('dl_sd') or 1)
    return [1.0] + [1.0 if v[f] else 0.0 for f in TITLE_FEATURES] + [tl, dl]


def chan_stats(rows):
    out = {}
    for ch in {v['ch'] for v in rows}:
        r = [v for v in rows if v['ch'] == ch]
        tl = [len(v['title']) for v in r]
        dl = [math.log(v['dur']) for v in r if v['dur']]
        out[ch] = {'tl_mu': S.mean(tl), 'tl_sd': S.pstdev(tl) or 1, 'dl_mu': S.mean(dl) if dl else 0, 'dl_sd': (S.pstdev(dl) if len(dl) > 1 else 1) or 1}
    return out


def evaluate(train, test_, label):
    cs = chan_stats(train + test_)
    X, Y = [design(v, cs) for v in train], [y(v) for v in train]
    beta = ols(X, Y, lam=5.0)
    pred = [sum(a * b for a, b in zip(design(v, cs), beta)) for v in test_]
    obs = [y(v) for v in test_]
    tier = lambda z: 'STRONG' if z >= math.log(2) else 'WEAK' if z < math.log(0.5) else 'TYPICAL'
    obs_t = [tier(z) for z in obs]
    res = {'split': label, 'n_train': len(train), 'n_test': len(test_),
           'mae_baseline_peer_median': S.mean(abs(o) for o in obs),
           'mae_baseline_train_mean': S.mean(abs(o - S.mean(Y)) for o in obs),
           'mae_model': S.mean(abs(o - p) for o, p in zip(obs, pred)),
           'spearman_model': spearman(pred, obs),
           'tier_acc_always_typical': sum(t == 'TYPICAL' for t in obs_t) / len(obs_t),
           'tier_acc_model': sum(tier(p) == t for p, t in zip(pred, obs_t)) / len(obs_t),
           'strong_recall_model': (sum(1 for p, t in zip(pred, obs_t) if t == 'STRONG' and tier(p) == 'STRONG') / max(1, obs_t.count('STRONG'))),
           'coef': dict(zip(['intercept'] + PRED_FEATS, [round(b, 4) for b in beta]))}
    # bootstrap CI on MAE improvement over peer-median baseline
    d = [abs(o) - abs(o - p) for o, p in zip(obs, pred)]
    bs = sorted(S.mean(RNG.choice(d) for _ in d) for _ in range(B_BOOT))
    res['mae_gain_vs_baseline_ci95'] = [bs[int(.025 * len(bs))], bs[int(.975 * len(bs)) - 1]]
    return res


# ---------------- descriptive ----------------
def log_vpd_slope(rows):
    """Within-channel OLS slope of log(views) on log(age): 1 => constant lifetime rate; <1 => views/day falls with age."""
    out = {}
    for ch in sorted({v['ch'] for v in rows}):
        r = [v for v in rows if v['ch'] == ch and v['fmt'] == 'LONG_FORM' and v['age'] and v['age'] >= 7 and v['views']]
        if len(r) < 15:
            continue
        b = ols([[1.0, math.log(v['age'])] for v in r], [math.log(v['views']) for v in r])
        out[ch] = {'n': len(r), 'slope': round(b[1], 3)}
    return out


def concentration(rows):
    out = {}
    for ch in sorted({v['ch'] for v in rows}):
        vs = sorted((v['views'] for v in rows if v['ch'] == ch and v['views'] is not None), reverse=True)
        if len(vs) < 10 or not sum(vs):
            continue
        k = max(1, round(len(vs) * 0.1))
        out[ch] = {'n': len(vs), 'top10pct_share_of_views': round(sum(vs[:k]) / sum(vs), 3),
                   'max_over_median': round(vs[0] / max(1, S.median(vs)), 1)}
    return out


def variance_share(rows):
    vals = [(v['ch'], math.log(v['views'] / v['age'])) for v in rows if v['age'] and v['age'] >= 7 and v['views'] and v['fmt'] == 'LONG_FORM']
    allv = [x for _, x in vals]
    by = C.defaultdict(list)
    for c, x in vals:
        by[c].append(x)
    within = sum(sum((x - S.mean(xs)) ** 2 for x in xs) for xs in by.values())
    total = sum((x - S.mean(allv)) ** 2 for x in allv)
    return {'n': len(vals), 'channels': len(by), 'between_channel_share_of_variance_log_vpd': round(1 - within / total, 3)}


def registry_niches():
    """Multi-niche descriptive from registry DB with dataset collection dates (manifests)."""
    snap = {'DS-000020': '2026-09-12', 'DS-000021': '2026-09-12', 'DS-000023': '2026-09-13', 'DS-000024': '2026-09-13',
            'DS-000025': '2026-09-13', 'DS-000027': '2026-09-20', 'DS-000028': '2026-09-22', 'DS-000029': '2026-09-23',
            'DS-000030': '2026-09-24', 'DS-000032': '2026-09-25', 'DS-000033': '2026-09-25', 'DS-000022': '2026-09-11', 'DS-000017': '2026-08-31'}
    db = sqlite3.connect(f'file:{REPO}/data/catalog/youtube_channel_registry.db?mode=ro', uri=True)
    rows = []
    for vid, ch, title, pub, dur, vt, views, likes, ds in db.execute(
            'select v.youtube_video_id,c.channel_name,v.title,v.published_at,v.duration_seconds,v.video_type,v.views,v.likes,dv.dataset_id '
            'from videos v join channels c using(canonical_channel_id) join dataset_videos dv using(youtube_video_id)'):
        p = parse_ts(pub) if pub and 'T' in pub else None
        if ds not in snap or not p:
            continue
        s = datetime.fromisoformat(snap[ds] + 'T23:59:59+00:00')
        fmt = 'SHORTS' if (vt or '').lower() in ('short', 'shorts') else 'LONG_FORM' if vt else 'UNKNOWN'
        rows.append({'id': vid, 'ch': ch, 'title': title, 'fmt': fmt, 'snap': snap[ds], 'age': (s - p).total_seconds() / 86400,
                     'views': views, 'dur': dur, 'likes': likes, 'ds': ds})
    return rows


def main():
    os.makedirs(OUT, exist_ok=True)
    orig, rep = load_originals(), load_replication()
    for v in orig + rep:
        add_features(v)
    R = {'generated_utc': datetime.now(timezone.utc).isoformat(), 'seed': 20261026, 'B_perm': B_PERM, 'B_boot': B_BOOT}

    # benchmark fidelity: our re-implementation vs stored project ratio
    pairs = [(v['ratio'], v['project_ratio']) for v in orig if v['ratio'] and v['project_ratio']]
    R['benchmark_reimplementation'] = {'n_both': len(pairs), 'max_abs_rel_diff': max(abs(a - b) / b for a, b in pairs),
                                       'stored_only': sum(1 for v in orig if v['project_ratio'] and not v['ratio']),
                                       'ours_only': sum(1 for v in orig if v['ratio'] and not v['project_ratio'])}
    R['populations'] = {
        'original_966_with_ratio': sum(1 for v in orig if v['ratio']),
        'original_by_channel_with_ratio': dict(C.Counter(v['ch'] for v in orig if v['ratio'])),
        'original_with_opening_text': sum(1 for v in orig if v['opening']),
        'deep_complete': sum(1 for v in orig if v['deep']), 'deep_complete_with_ratio': sum(1 for v in orig if v['deep'] and v['ratio']),
        'replication_rows': dict(C.Counter(v['set'] for v in rep)),
        'replication_with_ratio': dict(C.Counter(v['set'] for v in rep if v['ratio'])),
        'replication_by_channel_with_ratio': dict(C.Counter(f"{v['ch']}|{v['fmt']}" for v in rep if v['ratio'])),
    }

    # ---- primary family: title hypotheses on originals, with replication, holdout, nick-excluded ----
    primary = list(TITLE_FEATURES) + list(OPENING_FEATURES)
    tests = []
    pub_sorted = sorted(v['pub'] for v in orig if v['ratio'] and v['pub'])
    cut = pub_sorted[len(pub_sorted) // 2]
    for f in primary:
        t = test(orig, f)
        t['family'] = 'PRIMARY_PREREGISTERED'
        t['examples'] = examples(orig, f)
        t['replication'] = test(rep, f) if f in TITLE_FEATURES else {'note': 'NO_TRANSCRIPT_OPENINGS_IN_REPLICATION_SETS'}
        t['early_half'] = test([v for v in orig if v['pub'] and v['pub'] < cut], f, full=False)
        t['late_half'] = test([v for v in orig if v['pub'] and v['pub'] >= cut], f, full=False)
        t['excluding_nick'] = test([v for v in orig if v['ch'] != 'Nick Invests'], f, full=False)
        tests.append(t)
    q = bh([t['p_perm'] for t in tests])
    for t, qq in zip(tests, q):
        t['q_bh'] = qq
        rep_m = t['replication'].get('ratio_multiplier') if isinstance(t['replication'], dict) else None
        same = lambda m: m is not None and (m > 1) == (t['ratio_multiplier'] > 1)
        t['verdict'] = ('SURVIVED_ASSOCIATION' if qq < 0.10 and same(rep_m) and not t['loco_sign_flips'] and same(t['late_half'].get('ratio_multiplier'))
                        else 'SUGGESTIVE_NOT_ROBUST' if t['p_perm'] < 0.05 else 'NOT_SUPPORTED_NULL_OR_INCONSISTENT')
    R['primary_tests'] = tests

    # ---- secondary/exploratory: thumbnails (analyst prose; outcome-aware), topics ----
    expl = []
    deep = [v for v in orig if v['deep']]
    for f in THUMB_FEATURES:
        t = test(deep, f)
        t['family'] = 'EXPLORATORY_ANALYST_PROSE_OUTCOME_AWARE'
        t['examples'] = examples(deep, f)
        expl.append(t)
    for name, _ in TOPICS:
        for v in orig + rep:
            v['topic_' + name] = name in v['topics']
        t = test(orig, 'topic_' + name)
        t['family'] = 'EXPLORATORY_TOPIC_KEYWORD_HEURISTIC'
        t['replication'] = test(rep, 'topic_' + name, full=False)
        expl.append(t)
    for t, qq in zip(expl, bh([t.get('p_perm') or 1 for t in expl])):
        t['q_bh'] = qq
    R['exploratory_tests'] = expl

    # ---- continuous: duration, title length; publication weekday ----
    cont = {}
    for key, fn in (('duration_log', lambda v: math.log(v['dur']) if v['dur'] else None), ('title_chars', lambda v: len(v['title']))):
        per = {}
        for ch in sorted({v['ch'] for v in orig}):
            r = [(fn(v), y(v)) for v in orig if v['ch'] == ch and v['fmt'] == 'LONG_FORM' and y(v) is not None and fn(v) is not None]
            if len(r) >= 15:
                per[ch] = {'n': len(r), 'spearman': round(spearman([a for a, _ in r], [b for _, b in r]), 3)}
        rr = {}
        for ch in sorted({v['ch'] for v in rep}):
            r = [(fn(v), y(v)) for v in rep if v['ch'] == ch and v['fmt'] == 'LONG_FORM' and y(v) is not None and fn(v) is not None]
            if len(r) >= 15:
                rr[ch] = {'n': len(r), 'spearman': round(spearman([a for a, _ in r], [b for _, b in r]), 3)}
        cont[key] = {'original_per_channel': per, 'replication_per_channel': rr,
                     'original_median_rho': S.median(x['spearman'] for x in per.values()) if per else None,
                     'original_positive_channels': sum(x['spearman'] > 0 for x in per.values()), 'original_channels': len(per)}
    wk = C.defaultdict(list)
    for v in orig:
        if y(v) is not None and v['pub']:
            wk['weekend' if v['pub'].weekday() >= 5 else 'weekday'].append(y(v))
    cont['publication_weekend_vs_weekday_utc'] = {k: {'n': len(x), 'median_ratio': round(math.exp(S.median(x)), 3)} for k, x in wk.items()}
    hr = C.defaultdict(list)
    for v in orig:
        if y(v) is not None and v['pub']:
            hr[f'{v["pub"].hour // 6 * 6:02d}-{v["pub"].hour // 6 * 6 + 5:02d}UTC'].append(y(v))
    cont['publication_hour_block_utc'] = {k: {'n': len(x), 'median_ratio': round(math.exp(S.median(x)), 3)} for k, x in sorted(hr.items())}
    # engagement rate association (likes/views) — both use views; association only
    eng = {}
    for ch in sorted({v['ch'] for v in orig}):
        r = [(v['likes'] / v['views'], y(v)) for v in orig if v['ch'] == ch and y(v) is not None and v['likes'] is not None and v['views']]
        if len(r) >= 15:
            eng[ch] = {'n': len(r), 'spearman_likerate_vs_ratio': round(spearman([a for a, _ in r], [b for _, b in r]), 3)}
    cont['like_rate_vs_ratio'] = eng
    R['continuous'] = cont

    # ---- template repetition: same title skeleton with both strong and weak outcomes ----
    def skel(t):
        t = re.sub(r'\$?\d[\d,.]*\s?(k|m|b|%)?', '#', t.lower())
        return ' '.join(t.split()[:3])
    tg = C.defaultdict(list)
    for v in orig:
        if v['ratio']:
            tg[(v['ch'], skel(v['title']))].append(v)
    tmpl = []
    for (ch, s), vs in tg.items():
        if len(vs) >= 4:
            rs = sorted(vs, key=lambda v: v['ratio'])
            tmpl.append({'channel': ch, 'skeleton': s, 'n': len(vs), 'strong': sum(v['ratio'] >= 2 for v in vs), 'weak': sum(v['ratio'] < 0.5 for v in vs),
                         'min': {'id': rs[0]['id'], 'title': rs[0]['title'], 'ratio': round(rs[0]['ratio'], 3)},
                         'max': {'id': rs[-1]['id'], 'title': rs[-1]['title'], 'ratio': round(rs[-1]['ratio'], 3)}})
    R['title_templates'] = sorted(tmpl, key=lambda d: -d['n'])

    # ---- prediction ----
    lab = [v for v in orig if y(v) is not None and v['fmt'] == 'LONG_FORM']
    lab.sort(key=lambda v: v['pub'])
    k = int(len(lab) * 0.75)
    pred = [evaluate(lab[:k], lab[k:], 'TEMPORAL_75_25_ORIGINALS')]
    reps = [v for v in rep if y(v) is not None and v['fmt'] == 'LONG_FORM']
    pred.append(evaluate(lab, reps, 'TRAIN_ORIGINALS_TEST_UNSEEN_CHANNELS_REPLICATION'))
    loco = []
    for ch in sorted({v['ch'] for v in lab}):
        te = [v for v in lab if v['ch'] == ch]
        if len(te) >= 20:
            e = evaluate([v for v in lab if v['ch'] != ch], te, f'LOCO:{ch}')
            loco.append({x: e[x] for x in ('split', 'n_test', 'mae_baseline_peer_median', 'mae_model', 'spearman_model')})
    R['prediction'] = {'splits': pred, 'leave_one_channel_out': loco}

    # ---- descriptive structure ----
    reg = registry_niches()
    R['descriptive'] = {
        'age_slope_originals': log_vpd_slope(orig), 'age_slope_replication': log_vpd_slope(rep), 'age_slope_registry_all_niches': log_vpd_slope(reg),
        'concentration_registry_all_niches': concentration(reg),
        'variance_share_originals': variance_share(orig), 'variance_share_registry': variance_share(reg),
        'registry_rows_with_dated_snapshot': len(reg), 'registry_channels': len({v['ch'] for v in reg}),
        'tier_distribution_ours_originals': dict(C.Counter(('STRONG' if v['ratio'] >= 2 else 'WEAK' if v['ratio'] < .5 else 'TYPICAL') for v in orig if v['ratio'])),
        'tier_distribution_replication': dict(C.Counter(('STRONG' if v['ratio'] >= 2 else 'WEAK' if v['ratio'] < .5 else 'TYPICAL') for v in rep if v['ratio'])),
    }
    # shorts vs long-form in channels with both (lifetime vpd, not comparable reach units)
    peer_ratios(reg)
    both = {}
    for ch in sorted({v['ch'] for v in reg + rep}):
        allv = [v for v in reg + rep if v['ch'] == ch and v['age'] and v['age'] >= 7 and v['views']]
        s = [v['views'] / v['age'] for v in allv if v['fmt'] == 'SHORTS']
        l = [v['views'] / v['age'] for v in allv if v['fmt'] == 'LONG_FORM']
        if len(s) >= 5 and len(l) >= 5:
            both[ch] = {'shorts_n': len(s), 'long_n': len(l), 'shorts_median_vpd': round(S.median(s), 1), 'long_median_vpd': round(S.median(l), 1)}
    R['descriptive']['shorts_vs_long_lifetime_vpd'] = both

    # export per-video derived table (no private data; public metadata only)
    cols = ['set', 'id', 'ch', 'fmt', 'snap', 'age', 'views', 'dur', 'ratio', 'project_ratio', 'deep'] + primary + list(THUMB_FEATURES)
    with open(f'{OUT}/per_video_features.csv', 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for v in orig + rep:
            w.writerow([v.get(c) if not isinstance(v.get(c), float) else round(v[c], 6) for c in cols])
    json.dump(R, open(f'{OUT}/analysis_results.json', 'w'), indent=1, default=str)
    for t in tests:
        print(f"{t['feature']:28s} n={t['n_with']:4d}/{t['n_without']:4d} x{t['ratio_multiplier']:.3f} CI[{t['ci95_multiplier'][0]:.2f},{t['ci95_multiplier'][1]:.2f}] p={t['p_perm']:.4f} q={t['q_bh']:.3f} rep=x{(t['replication'].get('ratio_multiplier') or float('nan')):.3f} late=x{(t['late_half'].get('ratio_multiplier') or float('nan')):.3f} noNick=x{(t['excluding_nick'].get('ratio_multiplier') or float('nan')):.3f} flips={len(t['loco_sign_flips'])} {t['verdict']}")


if __name__ == '__main__':
    main()
