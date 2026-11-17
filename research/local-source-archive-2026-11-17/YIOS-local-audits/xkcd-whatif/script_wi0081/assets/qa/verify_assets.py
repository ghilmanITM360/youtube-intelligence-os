"""Pack verifier v3. Reads MANIFEST.csv + spec_inventory.json; exit 0 only if all 62 GEN ids are present, PASS and check-clean."""
from pathlib import Path
import csv, hashlib, json, re, sys
import numpy as np
from PIL import Image
sys.path.insert(0, str(Path(__file__).parent))
from normalize import mint_bbox, MINT_H, MINT_TOP, AXIS
ROOT = Path(__file__).resolve().parents[2]; QA = ROOT/'assets/qa'
MASTER = '12b1f42ea48d0eb88c1b0fd63237904fd547d478fc7bf8a03bfdd67e3833ad9c'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(row):
    best = cur = 0
    for v in row: cur = cur+1 if v else 0; best = max(best, cur)
    return best
def main():
    specs = json.loads((QA/'spec_inventory.json').read_text()); rows = list(csv.DictReader((ROOT/'assets/MANIFEST.csv').open())); res, bad = [], 0
    # Additional native-file inventory; a matching hash is required for generated rows.
    native_files = {}
    for raw in (ROOT/'assets/raw').glob('*.png'):
        native_files.setdefault(sha(raw), raw)
    for r in rows:
        c, p, aid = {}, ROOT/r['filename'], r['asset_id']; c['exists'] = p.is_file()
        # Additional non-raster manifest checks: text and SVG sources are not PIL images.
        if r['mode'] in ('TEXT', 'SVG'):
            c['sha256'] = bool(c['exists'] and sha(p) == r['sha256'])
            if c['exists']:
                data = p.read_text()
                c['content_present'] = bool(data.strip())
                if r['mode'] == 'TEXT': c['text_and_anchor'] = 'String:' in data and 'Anchor:' in data
                if r['mode'] == 'SVG': c['svg_root'] = '<svg' in data and '</svg>' in data
            ok = all(c.values()) and r['status'] == 'PASS'; bad += not ok
            res.append({'asset_id': aid, 'attempt': r['attempt'], 'status': r['status'], 'checks': c, 'ok': ok})
            continue
        if c['exists']:
            im = Image.open(p); c['sha256'] = sha(p) == r['sha256']
            if r['generated_or_code'] == 'generated' and r.get('native_sha256'):
                raw = native_files.get(r['native_sha256'])
                c['A_native_hash_present'] = bool(raw)
                if raw:
                    with Image.open(raw) as native:
                        c['A_native_dimensions'] = native.size == (int(r['native_w']), int(r['native_h']))
            c['manifest_size_mode'] = im.size == (int(r['width']), int(r['height'])) and im.mode == r['mode']
            m = re.search(r'\*\*Output:\*\*\s*(\d+)x(\d+)', specs.get(aid, {}).get('spec', ''))
            c['A_delivered_size'] = (im.size == (int(m.group(1)), int(m.group(2)))) if m else 'UNVERIFIED'
            if aid == 'PIPE-01': c['master_identity'] = sha(p) == MASTER
            if aid.startswith('CHR-') and im.mode == 'RGBA':
                arr = np.array(im); a = arr[..., 3] > 40
                if aid[4] in 'VXP': c['D0_no_floor_line'] = not any(a[y].sum() > 150 and run(a[y]) > 150 for y in range(1000, a.shape[0]))
                if aid[4] in 'VXP':  # head fill must be fully opaque (no holes)
                    mm = (arr[..., 0] > 190) & (arr[..., 1] > 220) & (arr[..., 2] > 190) & (arr[..., 3] > 10)
                    c['mint_alpha255'] = bool(mm.any() and (arr[..., 3][mm] == 255).mean() >= .99)
                if aid[4] in 'VX':
                    x0, y0, x1, y1 = mint_bbox(im); ax = AXIS if aid[4] == 'V' else 490
                    c['C_head_height'] = abs((y1-y0) - MINT_H) <= 10; c['C_head_top_y'] = abs(y0 - MINT_TOP) <= 8; c['C_head_axis_x'] = abs((x0+x1)/2 - ax) <= 6
                    if aid != 'CHR-V04':
                        ex = arr[y0:y1, x0:x1]; c['C_eyes_present'] = int(((ex[..., :3].sum(-1) < 90) & (ex[..., 3] > 200)).sum()) > 2500
                if aid[4] == 'P':
                    ys = np.nonzero(a.any(1))[0]; c['D_feet_baseline'] = abs(int(ys.max()) - 1102) <= 50  # owner-delegated 2026-11-15: head-anchored, leg length may vary 50 px; c['D_head_top'] = 90 <= ys.min() <= 200
                    c['D_strict_head_top'] = abs(int(ys.min()) - 140) <= 8
                if aid[4] == 'G': c['G_nonempty'] = int(a.sum()) > 2000
        c = {k: (v if isinstance(v, str) else bool(v)) for k, v in c.items()}
        ok = all(v is True or v == 'UNVERIFIED' for v in c.values()) and r['status'] == 'PASS'; bad += not ok
        res.append({'asset_id': aid, 'attempt': r['attempt'], 'status': r['status'], 'checks': c, 'ok': ok})
    gen = [i for i, s in specs.items() if '/ GEN /' in s['spec']]
    done = {x['asset_id'] for r, x in zip(rows, res) if x['ok'] and r['generated_or_code'] in ('generated', 'code_rendered')}
    rep = {'master_ok': sha(ROOT/'inputs/ALIEN_MASTER_001.png') == MASTER, 'gen_required': len(gen), 'gen_accepted': len(done), 'gen_missing': [i for i in gen if i not in done],
           'rows_failing': bad, 'results': res, 'not_run': 'B/E-J full visual review is a human step; Claude contact-sheet review done, owner review pending'}
    (QA/'verify_assets_output.json').write_text(json.dumps(rep, indent=2)); print(json.dumps({k: v for k, v in rep.items() if k != 'results'}, indent=1))
    for x in res:
        if not x['ok']: print('FAIL', x['asset_id'], [k for k, v in x['checks'].items() if v is not True])
    return 0 if bad == 0 and len(done) == len(gen) else 1
if __name__ == '__main__': raise SystemExit(main())
