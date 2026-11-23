"""Recompute the numbers behind the 23 knowledge-base rules from the files they cite, plus a colour-share measurement of the 160 frames viewed in the ten-episode pass (counterexample search for K10).
Output: prints a JSON dict and writes 11_RULE_RECOMPUTE.json. usage: uv run --no-project --with numpy --with pillow python scripts/phase11_rule_recompute.py"""
import csv, json, os, statistics as st, collections
import numpy as np
from PIL import Image
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = '/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/videos/'
rd = lambda f: list(csv.DictReader(open(A + '/' + f)))
o = {}
m = rd('05_SCRIPT_METRICS.csv'); L = [r for r in m if r['format'] == 'long']; S = [r for r in m if r['format'] != 'long']
o['K01_long_attributed_flag'] = f"{sum(r['opens_attributed']=='1' for r in L)}/{len(L)} long, {sum(r['opens_attributed']=='1' for r in S)}/{len(S)} short (metrics flag; R01 adds V015 by hand)"
o['K03_words'] = [r for r in rd('05_HOLDOUT_TEMPORAL_SPLIT.csv') if r['metric'] == 'words'][0]
o['K03_tests'] = len(rd('05_HOLDOUT_TEMPORAL_SPLIT.csv')) - 2  # numeric metrics tested with a permutation p
o['K04_wps_median_long'] = st.median(float(r['wps']) for r in L)
fam = rd('05_FAMILY_AND_REUSE_TABLE.csv'); sh = [r for r in fam if r['format'] != 'long']; der = [r for r in sh if r['role'] == 'DERIVED_SHORT']
o['K05'] = f"{len(der)}/{len(sh)} shorts derived; median containment {st.median(float(r['containment_8gram']) for r in der):.3f}; parents {len({r['best_parent'] for r in der})}"
b = rd('ct_scan_batch/BATCH_SUMMARY.csv')
for fmt in ('LONG', 'SHORT'):
    h = [float(r['hold_pct']) for r in b if r['fmt'] == fmt]; o[f'K09_{fmt}'] = f'n={len(h)} median {st.median(h):.1f} min {min(h):.1f} max {max(h):.1f}'
o['K09_low'] = [(r['video_id'], r['hold_pct']) for r in b if float(r['hold_pct']) < 80]
s = rd('06_STYLE_MEASUREMENTS_125.csv'); rs_ = lambda r: float(r['red_share']) > 0.001
o['K10_red_frames'] = f"{sum(rs_(r) for r in s)}/{len(s)}"; o['K10_other_accent_gt1pct'] = f"{sum(float(r['other_accent_share'])>0.01 for r in s)}/{len(s)}"
for fmt in ('LONG_FORM', 'SHORT'):
    ss = [r for r in s if r['fmt'] == fmt]; sw = [float(r['stroke_px']) for r in ss if r['stroke_px'] not in ('nan', '')]
    o[f'K11_{fmt}'] = f'n={len(ss)} stroke median {st.median(sw):.2f}'; o[f'K12_{fmt}'] = f"negative space median {st.median(float(r['negative_space']) for r in ss):.3f}"
fg = [float(r['height_over_head']) for r in rd('06_FIGURE_CANDIDATES.csv')]; q = np.percentile(fg, [25, 50, 75]); o['K13'] = f'n={len(fg)} quartiles {q.round(2).tolist()}'
cod = sum((rd(f) for f in ('07_SCIENCE_VISUAL_CODING_SAMPLE.csv', '07_SCIENCE_VISUAL_CODING_HOLDOUT.csv', '07b_SCIENCE_VISUAL_CODING_20LONG.csv', '07c_SCIENCE_VISUAL_CODING_SHORTS.csv')), [])
c = collections.Counter(r['spoken_qty_restated'] for r in cod); o['K14'] = f"{dict(c)}; YES share of non-NA = {c['YES']/(len(cod)-c['NA']):.3f}"
o['K15_devices'] = collections.Counter(r['device'] for r in cod).most_common(6)
av = rd('09_AV_ALIGNMENT_ALL88.csv'); segs = sum(int(r['segments']) for r in av); o['K17'] = f"{len(av)} videos, segments {segs}, pooled within 0.5 s = {sum(int(r['segments'])*float(r['share_within_0p5s']) for r in av)/segs:.3f}"
lu = [float(r['integrated_lufs']) for r in rd('09_AUDIO_LEVELS_88.csv')]; o['K18'] = f"{len(lu)} files, median {st.median(lu):.1f}, within -17.5..-15.5: {sum(-17.5<=x<=-15.5 for x in lu)}"
rv = rd('review_sample/REVIEWED_SAMPLE.csv'); o['K22'] = dict(collections.Counter(r['boundary_check'] for r in rv)); o['K22_camera'] = dict(collections.Counter(r['camera_motion'] for r in rv))
o['K02_endcard_rows'] = {f: len(rd('review_sample/' + f)) for f in ('endcards_order.csv', 'endcards_other24_order.csv', 'endcard_lengths_20long.csv')}
# K06: first ASR segment start per video
first = []
for v in os.listdir(V):
    p = f'{V}{v}/asr/asr_small_en.json'
    if os.path.exists(p): d = json.load(open(p)); first.append((v, d['segments'][0]['start']))
for dd in ('phase7b_asr', 'phase7c_asr'):
    for f in os.listdir(A + '/' + dd):
        if f.endswith('.json'): d = json.load(open(f'{A}/{dd}/{f}')); first.append((f[:-5], d['transcription'][0]['offsets']['from'] / 1000))
fd = {}
for v, t in first: fd.setdefault(v, t)
o['K06_first_asr'] = f"{len(fd)} videos; <=0.5 s: {sum(t<=0.5 for t in fd.values())}; max {max(fd.values()):.2f} s"
# colour share of the 160 ten-episode frames (960-px scaled JPEGs; shares are scale-invariant)
rows = rd('07e_EPISODE_SHEET_FRAMES.csv'); res = []
for r in rows:
    im = np.asarray(Image.open(A + '/' + r['frame']).convert('RGB')).astype(np.int16); mx = im.max(2); mn = im.min(2); sat = (mx - mn) / np.maximum(mx, 1)
    q = (im // 16).reshape(-1, 3); key = q[:, 0] * 256 + q[:, 1] * 16 + q[:, 2]; vals, cnt = np.unique(key, return_counts=True); bgk = vals[cnt.argmax()]
    bg = np.array([(bgk // 256) * 16 + 8, ((bgk // 16) % 16) * 16 + 8, (bgk % 16) * 16 + 8]); nonbg = np.abs(im - bg).sum(2) > 60
    red = nonbg & (im[..., 0] > 140) & (im[..., 1] < 110) & (im[..., 2] < 110) & (sat > 0.45); oth = nonbg & (sat > 0.45) & (mx > 90) & ~red
    col = nonbg & (sat > 0.15)  # any chroma
    res.append(dict(video_id=r['video_id'], t_s=r['t_s'], red=float(red.mean()), other=float(oth.mean()), chroma=float(col.mean())))
o['E160_frames'] = len(res); o['E160_red_gt0.1pct'] = sum(x['red'] > 0.001 for x in res); o['E160_other_accent_gt1pct'] = sum(x['other'] > 0.01 for x in res); o['E160_chroma_gt5pct'] = sum(x['chroma'] > 0.05 for x in res)
per = collections.defaultdict(list)
for x in res: per[x['video_id']].append(x['chroma'] > 0.05)
o['E160_chroma_frames_by_video'] = {k: sum(v) for k, v in per.items()}
o['E160_examples'] = [(x['video_id'], x['t_s'], round(x['other'], 3), round(x['chroma'], 3)) for x in sorted(res, key=lambda x: -x['chroma'])[:8]]
w = csv.DictWriter(open(A + '/11_RULE_COLOUR_160_FRAMES.csv', 'w', newline=''), fieldnames=list(res[0])); w.writeheader(); w.writerows(res)
json.dump(o, open(A + '/11_RULE_RECOMPUTE.json', 'w'), indent=1, default=str); print(json.dumps(o, indent=1, default=str))
