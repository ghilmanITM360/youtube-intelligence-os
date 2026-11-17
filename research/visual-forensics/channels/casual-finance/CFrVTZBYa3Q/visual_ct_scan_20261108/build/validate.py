import csv, json, hashlib, os, sys, copy
checks = []; 
def chk(name, ok, detail=''): checks.append(dict(check=name, passed=bool(ok), detail=str(detail)))
rd = lambda p: list(csv.DictReader(open(p)))
def core(st, ev, sh, fm, eps, N):
    out = []
    t = lambda n, c, d='': out.append((n, bool(c), d))
    t('states start at 0', st[0]['start_frame'] == 0); t('states end at last frame', st[-1]['end_frame'] == N - 1)
    t('states contiguous, no gap/overlap', all(st[k]['end_frame'] + 1 == st[k+1]['start_frame'] for k in range(len(st) - 1)))
    t('state pts == frame/24', all(abs(s['start_pts_seconds'] - s['start_frame'] / 24) < 1e-3 for s in st))
    ids = {s['visual_state_id'] for s in st}; t('event states resolve', all(e['after_state'] in ids for e in ev)); t('shot ids resolve', {s['shot_id'] for s in st} <= {s['shot_id'] for s in sh})
    t('events ordered', all(ev[k]['start_frame'] < ev[k+1]['start_frame'] for k in range(len(ev) - 1))); t('events within range', all(0 <= e['start_frame'] <= e['end_frame'] <= N - 1 for e in ev))
    def inside(e):
        x = next((s for s in st if s['visual_state_id'] == e['after_state']), None); return x is not None and x['start_frame'] <= e['start_frame'] and e['end_frame'] <= x['end_frame']
    t('event inside its state', all(inside(e) for e in ev))
    starts = {s['start_frame'] for s in st}; motion = {'PAN', 'PAN+DRAWON', 'CUT+PAN', 'SLIDE_IN', 'RISE_IN', 'HOP_IN', 'SCROLL+SLIDE', 'FADE+RISE', 'CUT+ENTRY', 'TEXT_TYPE'}
    miss = []
    for e in eps:
        a, b = int(e['start_frame']), int(e['end_frame'])
        if any(abs(a - x) <= 1 for x in starts): continue
        cov = [s for s in st if s['start_frame'] <= a <= s['end_frame']]
        if not (cov and cov[0]['entering_class'] in motion): miss.append(e['ep'])
    t('every measured episode explained by a state boundary or a motion state', not miss, miss)
    cuts = [s for s in st if s['entering_class'] == 'CUT' and s['start_frame'] > 0]
    t('every hard-cut start has a large measured entry change (frac>=0.05 or >=100k px)', all(float(s['entry_changed_frac']) >= 0.05 or int(s['entry_fullres_px']) >= 100000 for s in cuts), [s['start_frame'] for s in cuts if not (float(s['entry_changed_frac']) >= 0.05 or int(s['entry_fullres_px']) >= 100000)])
    return out
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
man = json.load(open('source_manifest.json')); N = man['decoded_frames_pts_listed']
def load():
    st = rd('visual_states.csv'); ev = rd('visual_event_ledger.csv'); sh = rd('shot_ledger.csv')
    for s in st:
        for k in ('start_frame', 'end_frame', 'frames', 'rep_frame'): s[k] = int(s[k])
        s['start_pts_seconds'] = float(s['start_pts_seconds'])
    for e in ev: e['start_frame'] = int(e['start_frame']); e['end_frame'] = int(e['end_frame'])
    return st, ev, sh
st, ev, sh = load(); fm = rd('tables/frame_metrics.csv'); eps = rd('tables/episodes.csv')
for n, c, d in core(st, ev, sh, fm, eps, N): chk(n, c, d)
h = hashlib.sha256(open(man['source_path'], 'rb').read()).hexdigest(); chk('source sha256 recomputed == manifest', h == man['source_sha256'])
base = {r['video_id']: r for r in json.load(open('/Users/ghilmankhan/YIOS-local-audits/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104/source_identity_baseline_v1.json'))['rows']}
chk('source sha256 == campaign baseline', h == base['CFrVTZBYa3Q']['sha256'])
chk('CFR proven (single frame delta)', man['cfr_assessment'] == 'CFR' and len(man['frame_delta_distinct']) == 1); chk('all frames measured', len(fm) == N == 1189)
chk('37/37 episodes present', len(eps) == 37); spec = json.load(open('PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json')); chk('one spec per state', len(spec) == len(st))
chk('every spec has image+animation prompts and QA', all(s['image_prompt'] and s['animation_prompt'] and s['qa_acceptance'] for s in spec)); chk('no spec asks to copy third-party assets', all('Replace every third-party item' in s['image_prompt'] for s in spec))
for f in ['source_manifest.json', 'coverage.json', 'shot_ledger.csv', 'visual_event_ledger.csv', 'visual_states.csv', 'audio_visual_alignment.csv', 'audio_visual_alignment_phrase.csv', 'visual_ct_scan_report.md', 'reconstruction_blueprint.md', 'quality_gate.json', 'continuation_handoff.md']: chk('exists non-empty ' + f, os.path.exists(f) and os.path.getsize(f) > 0)
q = json.load(open('quality_gate.json')); chk('AV sign-off not claimed', q['gates']['final_av_signoff'] == 'BLOCKED' and q['full_av_signoff'] == 'NO' and q['gates']['audio_human_listening'] == 'NOT_COMPLETED')
chk('audio rows all labelled ASR_UNCERTIFIED', all('ASR_UNCERTIFIED' in r['audio_listening_status'] for r in rd('audio_visual_alignment.csv') + rd('audio_visual_alignment_phrase.csv')))
chk('native windows named in coverage exist as sheets', all(os.path.exists(f'frames/{n}') for n in ['nat_01.jpg', 'nat_02.jpg', 'onset_01.jpg', 'onset_02.jpg', 'cut1007_01.jpg', 'ptr_01.jpg', 'anim_a.jpg', 'anim_b.jpg', 'pans_a.jpg', 'state_rep_01.jpg', 'state_rep_04.jpg', 'episodes_10.jpg', 'overview_03.jpg']))
fs = [l.split('  ', 1) for l in open('EVIDENCE_SHA256SUMS').read().splitlines()]; bad = [f for h_, f in fs if hashlib.sha256(open(f, 'rb').read()).hexdigest() != h_]
chk('checksum seal verifies (all listed files)', not bad, bad[:3])
# negative tests: the core checks must DETECT injected defects
neg = []
def neg_test(name, mut):
    s2, e2, h2 = copy.deepcopy(st), copy.deepcopy(ev), copy.deepcopy(sh); mut(s2, e2, h2); res = core(s2, e2, h2, fm, eps, N); neg.append(dict(test=name, detected=any(not c for _, c, _ in res)))
neg_test('gap between states', lambda s, e, h: s[10].__setitem__('end_frame', s[10]['end_frame'] - 3))
neg_test('overlap between states', lambda s, e, h: s[20].__setitem__('end_frame', s[20]['end_frame'] + 2))
neg_test('wrong end of video', lambda s, e, h: s[-1].__setitem__('end_frame', 1100))
neg_test('event outside state', lambda s, e, h: e[30].__setitem__('end_frame', e[30]['end_frame'] + 5000))
neg_test('hard cut with no measured change', lambda s, e, h: [x.__setitem__('entry_changed_frac', 0.0) or x.__setitem__('entry_fullres_px', 0) for x in s if x['entering_class'] == 'CUT' and x['start_frame'] == 644])
def drop_state(s, e, h):
    i = next(k for k, x in enumerate(s) if x['start_frame'] == 644); s[i-1]['end_frame'] = s[i]['end_frame']; s.pop(i)
neg_test('missing state for a measured episode (state at f644 deleted)', drop_state)
for n in neg: chk('negative test detected: ' + n['test'], n['detected'])
p = sum(c['passed'] for c in checks); res = dict(video_id='CFrVTZBYa3Q', total=len(checks), passed=p, failed=len(checks) - p, checks=checks, negative_tests=neg)
json.dump(res, open('VALIDATION_RESULTS.json', 'w'), indent=1)
for c in checks:
    if not c['passed']: print('FAIL', c['check'], c['detail'])
print(f"{p}/{len(checks)} passed"); sys.exit(0 if p == len(checks) else 1)
