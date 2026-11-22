"""Asset pipeline: staging -> technical validation -> independent review -> approved registry -> renderer.
  python3 pipeline.py validate DIR... [--meta FILE]        dry run, never touches the registry
  python3 pipeline.py review ID SHA256 PASS|PARTIAL|FAIL --reviewer NAME --evidence TEXT
  python3 pipeline.py approve ID... --from DIR... [--dry-run] [--supersede]
  python3 pipeline.py rollback [--to BACKUP.json] | verify | status
Technical PASS is not artistic approval. Only assets with a matching independent review reach the registry."""
import argparse, glob, hashlib, json, math, os, shutil, sys, time
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PNG_SIG = b'\x89PNG\r\n\x1a\n'
ALPHA_T = 8  # alpha above this counts as content


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def write_json_atomic(path, obj):
    tmp = path + '.tmp%d' % os.getpid()
    try:
        with open(tmp, 'w') as f:
            json.dump(obj, f, indent=1); f.flush(); os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp): os.remove(tmp)
        raise


def load_schema(root=HERE):
    return json.load(open(os.path.join(root, 'asset_schema.json')))


def _cv(c): return int(str(c).lstrip('v'))


def expand_ids(schema, contract='v1'):
    out = []
    for fam, d in schema['families'].items():
        if _cv(d.get('min_contract', 'v1')) > _cv(contract): continue
        out += [fam + '_' + v for v in d['variants']] if d.get('variants') else [fam]
    return out


def parse_id(fname, schema):
    """filename -> (id, family, variant, error). Strips ext and a trailing _draft; applies aliases."""
    i = os.path.splitext(os.path.basename(fname))[0]
    if i.endswith('_draft'): i = i[:-6]
    i = schema.get('aliases', {}).get(i, i)
    fams = schema['families']
    if i in fams: return i, i, None, None if not fams[i].get('variants') else 'variant required for ' + i
    for fam in sorted(fams, key=len, reverse=True):
        if i.startswith(fam + '_'):
            v = i[len(fam) + 1:]
            if fams[fam].get('variants') and v in fams[fam]['variants']: return i, fam, v, None
            return i, fam, v, 'incorrect variant "%s" for %s (allowed: %s)' % (v, fam, fams[fam].get('variants') or 'none')
    return i, None, None, 'unknown asset id "%s" (not in asset_schema.json)' % i


def _near(mask, pt):
    ys, xs = np.nonzero(mask)
    return float(np.hypot(xs - pt[0], ys - pt[1]).min()) if len(xs) else math.inf


def _flame_side(bb, b, side, loose=False):
    """Side flame must overlap the globe bbox b and extend beyond its own side edge."""
    e = []
    ov = bb[0] < b[2] and bb[2] > b[0] and bb[1] < b[3] and bb[3] > b[1]
    if not ov: e.append('%s flame bbox %s does not overlap globe %s' % (side, bb, b))
    gcx = (b[0] + b[2]) / 2; fcx = (bb[0] + bb[2]) / 2
    if (side == 'left') != (fcx < gcx): e.append('%s flame centre x=%.0f on wrong side of globe centre x=%.0f' % (side, fcx, gcx))
    if not loose and not (bb[0] < b[0] if side == 'left' else bb[2] > b[2]): e.append('%s flame does not extend beyond the globe\'s %s edge' % (side, side))
    return e


def check_png(path, schema, fam, meta_entry, sibling_body=None, contract='v1'):
    """Technical validation of one file. Returns dict(status, errors, warnings, metrics)."""
    errs, warns, m = [], [], {}
    try:
        with open(path, 'rb') as f:
            if f.read(8) != PNG_SIG: return dict(status='FAIL', errors=['not a PNG (bad signature)'], warnings=[], metrics={})
        im = Image.open(path); im.verify(); im = Image.open(path); im.load()
    except Exception as e:
        return dict(status='FAIL', errors=['corrupt/truncated PNG: %s' % e], warnings=[], metrics={})
    if im.mode != 'RGBA': return dict(status='FAIL', errors=['mode %s, RGBA required' % im.mode], warnings=[], metrics={})
    w, h = im.size; m['size'] = [w, h]
    a = np.asarray(im.getchannel('A')); mask = a > ALPHA_T
    fd = schema['families'][fam]
    if contract not in schema['rig_versions']: return dict(status='FAIL', errors=['unknown contract "%s"' % contract], warnings=[], metrics={})
    if _cv(fd.get('min_contract', 'v1')) > _cv(contract): return dict(status='FAIL', errors=['%s requires contract >= %s (got %s)' % (fam, fd['min_contract'], contract)], warnings=[], metrics={})
    RV = schema['rig_versions'][contract]; m['contract'] = contract
    kind = fd.get('kind_' + contract, fd.get('kind_v2', fd['kind']) if _cv(contract) >= 2 else fd['kind']); kd = schema['kinds'][kind]
    if not (64 <= w <= 8192 and 64 <= h <= 8192): errs.append('dimensions %dx%d out of range' % (w, h))
    want = fd.get('canvas') or (RV['canvas'] if kind.startswith('rig_') else None)
    if want and [w, h] != list(want): errs.append('canvas %dx%d, expected %s' % (w, h, 'x'.join(map(str, want))))
    n = int(mask.sum()); m['opaque_px'] = n
    if n == 0: errs.append('empty: no alpha content'); return dict(status='FAIL', errors=errs, warnings=warns, metrics=m)
    if n < kd['min_opaque_px']: errs.append('only %d content pixels (min %d)' % (n, kd['min_opaque_px']))
    if int(a.min()) == 255: errs.append('no transparency (alpha fully opaque)')
    if any(a[y, x] > ALPHA_T for y, x in ((0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1))): errs.append('opaque canvas corner')
    ys, xs = np.nonzero(mask); bb = [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]; m['bbox'] = bb
    frac = (bb[2] - bb[0]) * (bb[3] - bb[1]) / (w * h); m['bbox_frac'] = round(frac, 3)
    if 'min_height_frac' in kd and (bb[3] - bb[1]) / h < kd['min_height_frac']: errs.append('subject height %.0f%% of canvas < %.0f%% (%s)' % ((bb[3] - bb[1]) / h * 100, kd['min_height_frac'] * 100, kind))
    if 'min_bbox_frac' in kd and frac < kd['min_bbox_frac']: errs.append('subject bbox %.0f%% of canvas < %.0f%% (%s)' % (frac * 100, kd['min_bbox_frac'] * 100, kind))
    if 0.0 < (np.count_nonzero((a > ALPHA_T) & (a < 255)) / n) < 0.002: warns.append('almost no partial alpha: hard/aliased edges')
    # clipping: content touching the canvas border (neck join on the top edge is allowed for torso/body)
    band = fd.get('neck_band')
    for side, sl in (('top', mask[0]), ('bottom', mask[-1]), ('left', mask[:, 0]), ('right', mask[:, -1])):
        idx = np.nonzero(sl)[0]
        if not len(idx): continue
        if side == 'top' and band and all(abs(i - w // 2) <= band for i in idx): continue
        errs.append('content touches %s canvas edge at %d..%d: likely clipped' % (side, idx.min(), idx.max()))
    A = RV['anchors']; tol = RV.get('anchor_tol', schema['anchor_tol'])
    if kind == 'rig_arm':
        d = _near(mask, A['shoulder']); m['dist_shoulder'] = round(d, 1)
        if d > tol: errs.append('arm does not reach shoulder anchor %s (nearest content %.0fpx > %d)' % (A['shoulder'], d, tol))
        cx = float(xs.mean()); m['cx'] = round(cx, 1)
        if (fd['side'] == 'left') != (cx < A['shoulder'][0]): errs.append('%s arm centroid x=%.0f on wrong side of shoulder x=%d' % (fd['side'], cx, A['shoulder'][0]))
    elif kind == 'rig_body':
        for nm in ('neck', 'shoulder', 'hip'):
            d = _near(mask, A[nm]); m['dist_' + nm] = round(d, 1)
            if d > tol: errs.append('body has no content within %dpx of %s anchor %s (nearest %.0fpx)' % (tol, nm, A[nm], d))
    elif kind == 'rig_torso':
        d = _near(mask, A['neck']); m['dist_neck'] = round(d, 1)
        if d > tol: errs.append('torso top %.0fpx from neck anchor (> %d)' % (d, tol))
        if bb[3] < A['hip'][1] - tol: errs.append('torso ends y=%d above hip anchor y=%d' % (bb[3], A['hip'][1]))
        if abs(float(xs.mean()) - A['neck'][0]) > 40: errs.append('torso off-centre from spine x=%d' % A['neck'][0])
    elif kind == 'rig_legs':
        d = _near(mask, A['hip']); m['dist_hip'] = round(d, 1)
        if d > tol: errs.append('legs %.0fpx from hip anchor (> %d)' % (d, tol))
        lmin, lmax = RV.get('legs_min_h', 300), RV.get('legs_max_h')
        if bb[3] - bb[1] < lmin: errs.append('legs shorter than %dpx' % lmin)
        if lmax and bb[3] - bb[1] > lmax: errs.append('legs taller than %dpx (contract %s)' % (lmax, contract))
        if abs(float(xs.mean()) - A['hip'][0]) > 40: errs.append('legs off-centre from hip x=%d' % A['hip'][0])
    elif kind == 'head':
        nk = fd['neck']; m['neck_in_bbox_x'] = bb[0] <= nk[0] <= bb[2]
        if not m['neck_in_bbox_x']: errs.append('neck anchor x=%d outside head bbox' % nk[0])
        if abs(bb[3] - nk[1]) > 60: errs.append('head bottom y=%d is %dpx from neck anchor y=%d' % (bb[3], abs(bb[3] - nk[1]), nk[1]))
    elif kind == 'earth_body':
        ar = (bb[2] - bb[0]) / (bb[3] - bb[1])
        if not .8 <= ar <= 1.2: errs.append('globe aspect %.2f not round' % ar)
    elif kind == 'earth_flame_side' and sibling_body: errs += _flame_side(bb, sibling_body, fd['side'])
    elif kind == 'earth_flames' and contract != 'v1' and sibling_body:
        errs += _flame_side([bb[0], bb[1], (bb[0] + bb[2]) // 2, bb[3]], sibling_body, 'left', loose=True) + _flame_side([(bb[0] + bb[2]) // 2, bb[1], bb[2], bb[3]], sibling_body, 'right', loose=True)
    elif kind in ('earth_face', 'earth_flames') and sibling_body:
        b = sibling_body
        if kind == 'earth_face' and not (b[0] <= bb[0] and bb[2] <= b[2] and b[1] <= bb[1] and bb[3] <= b[3]): errs.append('face bbox %s not inside globe bbox %s' % (bb, b))
        if kind == 'earth_flames' and not (bb[0] >= b[0] - 60 and bb[2] <= b[2] + 60 and bb[1] < b[3] and bb[3] > b[3]): errs.append('flames bbox %s do not overlap globe lower edge %s' % (bb, b))
    for k in ('provenance', 'generator', 'author', 'source'):
        if not (meta_entry or {}).get(k): errs.append('missing metadata field "%s"' % k)
    return dict(status='FAIL' if errs else 'PASS', errors=errs, warnings=warns, metrics=m)


def _pose_pairs(res, schema, ctr):
    """Anatomical relationships between the left/right arm of one pose (contract-aware anchors)."""
    by = {}
    for r in res:
        if r.get('family') in ('rig_arm_left', 'rig_arm_right') and r.get('metrics', {}).get('bbox'): by.setdefault(r['variant'], []).append(r)
    for pose, rs in by.items():
        A = schema['rig_versions'][ctr(rs[0]['id'])]['anchors'] if ctr(rs[0]['id']) in schema['rig_versions'] else None
        if not A: continue
        sh, hp = A['shoulder'], A['hip']; mid = sh[1] + (hp[1] - sh[1]) // 2
        msgs = []
        if pose == 'up' and not any(r['metrics']['bbox'][1] < sh[1] - 100 for r in rs): msgs.append('pose "up": no arm rises >=100px above the shoulder anchor y=%d' % sh[1])
        if pose == 'point' and not any(max(abs(r['metrics']['bbox'][0] - sh[0]), abs(r['metrics']['bbox'][2] - sh[0])) >= 250 for r in rs): msgs.append('pose "point": no arm extends >=250px horizontally from the shoulder')
        PR = schema['rig_versions'][ctr(rs[0]['id'])].get('pose_rules', {}).get(pose)
        if pose == 'hips' and PR:
            lo, hi = (A['neck'][1] + f * (hp[1] - A['neck'][1]) for f in PR['hand_y_frac'])
            for r in rs:
                if not lo <= r['metrics']['bbox'][3] <= hi: msgs.append('pose "hips" (measured): hand bottom y=%d outside source-measured band %d..%d' % (r['metrics']['bbox'][3], lo, hi))
        elif pose == 'hips' and not all(r['metrics']['bbox'][3] >= mid for r in rs): msgs.append('pose "hips": hands end above waist y=%d' % mid)
        if pose == 'down' and not all(r['metrics']['bbox'][3] >= mid for r in rs): msgs.append('pose "down": arm ends above waist y=%d' % mid)
        for m_ in msgs:
            for r in rs: r['errors'].append(m_); r['status'] = 'FAIL'


def validate(dirs, meta=None, root=HERE, contract=None):
    schema = load_schema(root); files = []; contract = contract or schema.get('default_contract', 'v1')
    ctr = lambda i: ((meta or {}).get(i) or {}).get('contract') or contract
    for d in dirs: files += [f for f in ([d] if os.path.isfile(d) else sorted(glob.glob(os.path.join(d, '*.png')))) if not os.path.basename(f).startswith(tuple(schema.get('ignore_prefixes', [])))]
    seen, res = {}, []
    for f in files:
        i, fam, var, err = parse_id(f, schema); seen.setdefault(i, []).append(f)
        res.append(dict(id=i, family=fam, variant=var, file=f, _err=err))
    bodies = {r['id']: r for r in res}
    body_bb = None
    if 'prop_earth_body' in seen and len(seen['prop_earth_body']) == 1:
        r0 = check_png(seen['prop_earth_body'][0], schema, 'prop_earth_body', (meta or {}).get('prop_earth_body'), contract=ctr('prop_earth_body')); body_bb = r0['metrics'].get('bbox')
    for r in res:
        if r['_err']:
            r.update(status='FAIL', errors=[r['_err']], warnings=[], metrics={})
        else:
            r.update(check_png(r['file'], schema, r['family'], (meta or {}).get(r['id']), body_bb, ctr(r['id'])))
            if len(seen[r['id']]) > 1: r['status'] = 'FAIL'; r['errors'].append('duplicate id: %s' % ', '.join(os.path.basename(x) for x in seen[r['id']]))
        if os.path.exists(r['file']): r['sha256'] = sha256(r['file'])
        r.pop('_err')
    _pose_pairs(res, schema, ctr)
    present = {r['id'] for r in res if r['family']}
    missing = sorted(set(expand_ids(schema, contract)) - present)
    dups = sorted(i for i, v in seen.items() if len(v) > 1)
    p = sum(r['status'] == 'PASS' for r in res)
    summary = dict(files=len(res), pass_=p, fail=len(res) - p, missing=missing, duplicates=dups,
                   batch='COMPLETE' if not missing and p == len(res) else 'INCOMPLETE')
    return dict(summary=summary, files=res)


# ---------- registry workflow ----------
def _paths(root):
    return dict(reg=os.path.join(root, 'asset_registry.json'), bak=os.path.join(root, 'registry_backups'),
                rev=os.path.join(root, 'reviews'), app=os.path.join(root, 'approved'))


def load_registry(root=HERE):
    p = _paths(root)['reg']
    return json.load(open(p)) if os.path.exists(p) else []


def backup_registry(root=HERE):
    P = _paths(root); os.makedirs(P['bak'], exist_ok=True)
    dst = os.path.join(P['bak'], 'asset_registry.%d.json' % time.time_ns())
    if os.path.exists(P['reg']): shutil.copy2(P['reg'], dst)
    else: write_json_atomic(dst, [])
    return dst


def record_review(aid, sha, verdict, reviewer, evidence, root=HERE):
    meta = load_meta(root); author = (meta.get(aid) or {}).get('author', '')
    if verdict not in ('PASS', 'PARTIAL', 'FAIL'): raise ValueError('verdict must be PASS|PARTIAL|FAIL')
    if not reviewer or not evidence: raise ValueError('reviewer and evidence are required')
    if reviewer.strip().lower() == author.strip().lower() or 'same-agent' in reviewer.lower(): raise ValueError('reviewer must be independent of author "%s"' % author)
    P = _paths(root); os.makedirs(P['rev'], exist_ok=True)
    cur = os.path.join(P['rev'], aid + '.json')
    if os.path.exists(cur):  # keep every earlier review as history
        old = json.load(open(cur)); hd = os.path.join(P['rev'], 'history'); os.makedirs(hd, exist_ok=True)
        write_json_atomic(os.path.join(hd, '%s@%s.json' % (aid, old.get('sha256', 'unknown')[:8])), old)
    write_json_atomic(cur, dict(asset_id=aid, sha256=sha, verdict=verdict, reviewer=reviewer, evidence=evidence, independent=True, reviewed_at=time.strftime('%Y-%m-%dT%H:%M:%S')))


def load_meta(root=HERE):
    p = os.path.join(root, 'staging_meta.json')
    return json.load(open(p)) if os.path.exists(p) else {}


def approve(ids, dirs, supersede=False, dry_run=False, root=HERE):
    """All-or-nothing. Returns (ok, messages, new_entries)."""
    P = _paths(root); meta = load_meta(root); rep = validate(dirs, meta, root); by = {r['id']: r for r in rep['files']}
    reg = load_registry(root); live = {r['id']: r for r in reg if r.get('status') in ('approved',)}; msgs, new = [], []
    for i in ids:
        r = by.get(i)
        if not r: msgs.append('%s: not found in staging' % i); continue
        if r['status'] != 'PASS': msgs.append('%s: technical validation FAIL: %s' % (i, '; '.join(r['errors']))); continue
        rp = os.path.join(P['rev'], i + '.json')
        if not os.path.exists(rp): msgs.append('%s: no independent review on record' % i); continue
        rv = json.load(open(rp))
        if rv.get('sha256') != r['sha256']: msgs.append('%s: review is for a different file version (sha mismatch)' % i); continue
        if rv.get('verdict') != 'PASS' or not rv.get('independent'): msgs.append('%s: review verdict %s, PASS required' % (i, rv.get('verdict'))); continue
        if i in live and not supersede: msgs.append('%s: already approved; use --supersede to replace' % i); continue
        if i in live and live[i].get('sha256') == r['sha256']: msgs.append('%s: identical file already approved' % i); continue
        im = Image.open(r['file']); fd = load_schema(root)['families'][r['family']]; ctr_ = r['metrics'].get('contract', 'v1')
        new.append(dict(id=i, file='approved/%s@%s.png' % (i, r['sha256'][:8]), family=r['family'], variant=r['variant'], type=fd.get('kind_' + ctr_, fd['kind']), contract=ctr_, size=list(im.size), transparent=True,
                        provenance=meta[i]['provenance'], generator=meta[i]['generator'], level=4, validation='APPROVED_INDEPENDENT', status='approved', sha256=r['sha256'],
                        review=dict(reviewer=rv['reviewer'], verdict=rv['verdict'], at=rv['reviewed_at']), approved_at=time.strftime('%Y-%m-%dT%H:%M:%S'), render_scale=float(meta[i].get('render_scale', 1.0)),
                        supersedes=live[i]['sha256'] if i in live else None, _src=r['file']))
    if msgs or dry_run: return (not msgs), msgs or ['dry-run OK: would register %s' % [n['id'] for n in new]], new
    os.makedirs(P['app'], exist_ok=True); backup_registry(root); added = []
    try:
        for n in new:  # copy + verify first: orphan files are harmless if the swap below fails
            dst = os.path.join(root, n['file']); tmp = dst + '.tmp%d' % os.getpid(); shutil.copyfile(n.pop('_src'), tmp)
            if sha256(tmp) != n['sha256']: os.remove(tmp); raise IOError('copy checksum mismatch for ' + n['id'])
            os.replace(tmp, dst); added.append(n)
        keep = [r for r in reg if r['id'] not in {n['id'] for n in new}]
        for r in reg:  # superseded entries stay in the file as history, but are not resolved
            if r['id'] in {n['id'] for n in new}: keep.append(dict(r, status='superseded'))
        write_json_atomic(P['reg'], keep + added)
    except Exception as e:
        return False, ['registration aborted, registry unchanged: %s' % e], []
    return True, ['registered %s' % [n['id'] for n in added]], added


def rollback(to=None, root=HERE):
    P = _paths(root); baks = sorted(glob.glob(os.path.join(P['bak'], 'asset_registry.*.json')))
    tgt = to or (baks[-1] if baks else None)
    if not tgt or not os.path.exists(tgt): raise FileNotFoundError('no backup to roll back to')
    json.load(open(tgt)); cur = backup_registry(root); write_json_atomic(P['reg'], json.load(open(tgt))); return tgt, cur


def verify(root=HERE):
    P = _paths(root); bad = []
    for r in load_registry(root):
        if r.get('status') != 'approved': continue
        f = os.path.join(root, r['file'])
        if not os.path.exists(f): bad.append('%s: approved file missing' % r['id'])
        elif sha256(f) != r['sha256']: bad.append('%s: approved file checksum changed' % r['id'])
        if not os.path.exists(os.path.join(P['rev'], r['id'] + '.json')): bad.append('%s: review record missing' % r['id'])
    return bad


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); sp = ap.add_subparsers(dest='cmd', required=True)
    v = sp.add_parser('validate'); v.add_argument('dirs', nargs='+', help='staging dirs or single PNG files'); v.add_argument('--out'); v.add_argument('--contract', help='default rig contract for files without a meta contract (v1 legacy, v2 corrected)')
    r = sp.add_parser('review'); r.add_argument('id'); r.add_argument('sha'); r.add_argument('verdict'); r.add_argument('--reviewer', required=True); r.add_argument('--evidence', required=True)
    a = sp.add_parser('approve'); a.add_argument('ids', nargs='+'); a.add_argument('--from', dest='dirs', nargs='+', required=True); a.add_argument('--dry-run', action='store_true'); a.add_argument('--supersede', action='store_true')
    b = sp.add_parser('rollback'); b.add_argument('--to')
    sp.add_parser('verify'); sp.add_parser('status')
    x = ap.parse_args(argv)
    if x.cmd == 'validate':
        rep = validate(x.dirs, load_meta(), contract=x.contract)
        for f in rep['files']: print('%-4s %-28s %s' % (f['status'], f['id'], '; '.join(f['errors']) or ''))
        print(json.dumps(rep['summary'], indent=1))
        if x.out: write_json_atomic(x.out, rep)
        return 0 if rep['summary']['fail'] == 0 else 1
    if x.cmd == 'review': record_review(x.id, x.sha, x.verdict, x.reviewer, x.evidence); print('review recorded'); return 0
    if x.cmd == 'approve':
        ok, msgs, _ = approve(x.ids, x.dirs, x.supersede, x.dry_run); print(*msgs, sep='\n'); return 0 if ok else 1
    if x.cmd == 'rollback': t, c = rollback(x.to); print('restored', t, '(previous state saved as %s)' % c); return 0
    if x.cmd == 'verify': bad = verify(); print(*(bad or ['registry verified']), sep='\n'); return 1 if bad else 0
    if x.cmd == 'status':
        from collections import Counter
        print(dict(Counter(r.get('status', 'legacy') for r in load_registry()))); return 0


def cli():
    try: return main()
    except (ValueError, FileNotFoundError) as e: print('ERROR:', e); return 2


if __name__ == '__main__': sys.exit(cli())
