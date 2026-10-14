#!/usr/bin/env python3
"""Compile FULL_STORYBOARD + SCENE_ASSET_MAP + AUDIO_ALIGNMENT into animation/KEYFRAME_TIMELINE.json.

Every visible state is the authored SCENE_ASSET_MAP layout (same assets, z order, placement, scale).
This script only decides WHEN each layer enters/exits/switches and HOW (simple keyframes).
Edit CUES to retime; re-run; render with tools/render.cjs. Stdlib only.
"""
import csv, json, math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FPS = 30
F = 1 / FPS
OPS = Counter()  # operation tally written into the timeline
LEAD = 0.07  # visuals land ~2 frames before the word onset

AL = json.loads((ROOT / 'animation/AUDIO_ALIGNMENT.json').read_text())
WORDS = AL['words']
NARRATION = AL['source']['duration_sec']
END_HOLD = 1.3  # V3: the payoff holds after the last word; the narration itself is untouched
DURATION = round(NARRATION + END_HOLD, 3)


def w(ref):
    """'idx:text' -> word onset minus LEAD; asserts the text so a retimed alignment cannot silently drift."""
    i, txt = ref.split(':', 1)
    word = WORDS[int(i)]
    assert word['text'] == txt, (ref, word['text'])
    return round(word['start_refined'] - LEAD, 3)


def at(v):
    return w(v) if isinstance(v, str) else v


# state -> (start, cut?, {layer: enter/switch time}). Unlisted entering layers stagger 4 frames after start.
CUES = {
    'S01_01': (0.0, True, {'FED': 0.0, 'HOST': 0.0, 'RATES': 0.0, 'RATE': w('3:raised')}),
    'S01_02': (w('4:interest'), False, {}),
    'S01_03': (w('6:and'), False, {'BILL_UP': w('8:own'), 'BILL': w('10:bill'), 'EMPHASIS': w('11:went')}),
    'S01_04': (w('11:went') + 0.1, False, {}),  # V3: label lands with 'went up' so it reads before the cut
    'S02_01': (w('13:In'), True, {'POLICY_DATE': w('14:September,'), 'POLICY': w('14:September,') + 0.3, 'POLICY_ATTR': w('14:September,') + 0.55,
                                  'POLICY_FOCUS': w('17:raised'), 'QUARTER_POINT': w('18:rates'), 'POLICY_HL': w('21:quarter')}),
    'S02_02': (w('21:quarter') + 0.11, False, {}),
    'S02_03': (w('24:the'), True, {'HOST': w('25:problem.') + 0.1, 'BANKER': w('26:Banks')}),  # V3: cut on 'the problem' gives TARGET ~1 s
    'S02_04': (w('29:$3'), False, {'BALANCE_LINK': w('30:trillion') + 0.1, 'BALANCE_LABEL': w('30:trillion') + 0.35}),
    'S02_05': (w('31:in'), False, {'RESERVE_UNITS': w('31:in') + 0.25, 'RESERVE_HL': w('32:reserves')}),
    'S02_06': (w('36:and'), False, {'PAY_FLOW': w('36:and') + 0.12, 'PAY_NOTE': w('36:and') + 0.3, 'FED_EXPENSE': w('39:pays')}),
    'S02_07': (w('40:them'), False, {}),
    'S03_01': (w('44:quarter'), True, {'DELTA': w('44:quarter') + 2 * F, 'HOST': w('44:quarter') + 0.3, 'CASH': w('51:billion')}),
    'S03_02': (w('46:increase'), False, {}),  # V3: 0.25% morphs into 0.25% = 0.0025 (MORPH)
    'S03_03': (w('47:would'), False, {'MATH': w('48:add'), 'CALC_UNDERLINE': w('49:about') + 0.1}),
    'S03_04': (w('50:$7.5'), False, {'PER_YEAR': w('53:year'), 'INTEREST_COSTS': w('55:interest')}),
    'S03_05': (w('57:if'), False, {'ILLUSTRATION': w('57:if') + 0.2}),
    'S04_01': (w('62:But'), True, {'BOND': w('63:much') + 0.1, 'COUPON': w("66:Fed's") + 0.1, 'BOND_INCOME': w('68:income'), 'CLOCK': w("69:doesn't")}),  # V3: bond fills the frame on 'much of'
    'S04_02': (w('70:rise'), False, {'SLOW_LABEL': w('70:rise') + 0.2, 'AS_QUICKLY': w('72:quickly.')}),
    'S04_03': (24.45, False, {'HOST': 24.45, 'EXPENSE_LABEL': w('73:When'), 'BILL': w('74:expenses') + 0.1, 'EXPENSE_UP': w('75:outweigh')}),
    'S04_04': (w('75:outweigh') + 0.2, False, {}),
    'S05_01': (26.42, True, {'HOST': 26.42 + 3 * F, 'MISMATCH': 26.42 + 6 * F}),  # V3: cut inside the 0.6 s pause so the recap header registers before 'losses'
    'S05_02': (w('77:losses'), False, {'DOWN': w('77:losses'), 'LEDGER': w('79:into')}),
    'S05_03': (w('80:what\'s'), False, {'DEFERRED': w('83:deferred')}),
    'S05_04': (w('84:asset.') - 0.25, False, {'NOT_THIS_HIKE': w('84:asset.') + 0.1}),
    'S05_05': (30.6, False, {'OCT_DATE': 30.75, 'H41_ATTR': w('88:that'), 'SOURCE_LABEL': w('88:that') + 0.1, 'SOURCE_TOTAL': w('89:balance') + 0.2,
                             'MILLIONS': w('91:roughly'), 'SOURCE_HL': w('91:roughly') + 0.2, '234B': w('92:$234')}),
    'S05_06': (w('92:$234') + 0.55, False, {}),
    'S06_01': (w('94:Until'), True, {'EARNINGS_BAG': w('95:future'), 'LEDGER': w('96:earnings'), 'COVER': w('97:cover'), 'COVER_FIRST': w('97:cover') + 0.12}),
    'S06_02': (w('98:it,') - 0.05, False, {'STEPS': w('98:it,') - 0.05, 'BEFORE': w('98:it,') + 0.07}),
    # V3: cut on 'payments' so 'the Fed's normal...' is heard over BEFORE NORMAL PAYMENTS RESUME
    'S06_03': (w('102:payments'), True, {'FED': w('102:payments') + 0.13, 'TREASURY': w('105:Treasury'), 'NORMAL_ROUTE': w('105:Treasury') + 0.12,
                                        'PAUSE': w('106:stay'), 'PAUSE_LABEL': w('107:paused.'), 'WHILE_BALANCE': w('107:paused.') + 0.15}),
    'S06_04': (38.8, False, {}),
    'S06_05': (40.25, True, {'ROUTE': w('110:those'), 'NOTE': w('110:those') + 0.15, 'HIST_AMOUNT': w('115:$107'), 'HIST_REMITTED': w('115:$107') + 0.35,
                              'HIST_SOURCE': 42.3, 'HIST_HL': 42.55}),
    'S06_06': (42.9, False, {}),
    'S07_01': (w('117:Higher'), True, {'HOST': w('119:can'), 'SHIELD': w('119:can'), 'SHIELD_GRIP': w('119:can'), 'FIGHT': w('120:fight'), 'PRICE': w('121:inflation.')}),
    'S07_02': (w('121:inflation.') + 0.3, False, {}),
    'S07_03': (w('122:But'), True, {'WRENCH': w('122:But'), 'TOOL_GRIP': w('122:But'),  # held tool lands with the hand,
                                     'REPAIR_HEADER': w('126:make'),
                                     'LEDGER': w("128:Fed's"), 'FED_RECOVERY': w('129:own'), 'STEPS': w('130:finances')}),
    'S07_04': (w('131:harder'), False, {'SHIELD': w('131:harder') + 0.13, 'BOTH': 48.6}),
}
# Attached parts animate about one shared world pivot (host feet) so hands never separate from held props.
GROUPS = {('SCENE_07', 'S07_01'): ['HOST', 'SHIELD', 'SHIELD_GRIP'], ('SCENE_07', 'S07_03'): ['HOST', 'WRENCH', 'TOOL_GRIP']}
# Trace-reveal direction follows the drawn flow so money arrows never play backwards.
WIPE = {'DGM_INTEREST_FLOW': ('rl', 14), 'DGM_REMIT_FLOW': ('lr', 14), 'DGM_RESERVE_LINK': ('lr', 14), 'DGM_SLOW_CHANGE': ('lr', 36),
        'ANN_EXPENSE_UP': ('bt', 7), 'ANN_RATE_UP': ('bt', 10), 'ANN_ARROW_RED': ('lr', 8), 'ANN_ARROW_GREEN': ('lr', 10), 'ANN_UNDERLINE': ('lr', 10),
        'DGM_CONDITION_DOWN': ('tb', 10), 'ENV_RECOVERY_STEPS': ('lr', 14), 'ANN_SOURCE_BOX': ('lr', 8), 'ANN_SOURCE_WIDE': ('lr', 8)}
WRITE = {'TX_DECIMAL': 10, 'TX_MATH': 10, 'TX_TARGET_RANGE': 10, 'TX_COVER_FIRST': 10, 'TX_BEFORE': 10}  # V3: faster write-on, longer read
# V3: TX_DELTA draws the same '0.25%' glyphs as the start of TX_DECIMAL, so it glides onto them and only '= 0.0025' writes on.
MORPH = {('S03_02', 'DECIMAL'): ('DELTA', 8)}
# V3: expression overlays (CHARACTER_BIBLE: FACE_* top-left at host-local 100,65, original eyes/brows/mouth hidden).
FACES = {('S03_04', 'HOST'): ('FACE_WOW', w('51:billion') + 0.2), ('S03_05', 'HOST'): ('FACE_THINK', w('59:stayed')),
         ('S07_04', 'HOST'): ('FACE_RESOLVE', 49.45)}
BIG_NUMBERS = {'TX_ANNUAL_COST', 'TX_234B', 'TX_HIST_AMOUNT', 'TX_DELTA', 'TX_THREE_TRILLION'}
FOCUS_CROPS = {'EVD_FOMC_QUARTER', 'EVD_DEFERRED', 'EVD_2021', 'EVD_IORB', 'EVD_RESERVES'}
TRAVEL = {'PAY_NOTE': (170, 0, 18), 'NOTE': (-230, 0, 20)}  # start offset (dx,dy) and frames; follows flow direction
# Gentle per-scene push plus attention pushes on documentary evidence (cx, cy, k).
CAMERA_FOCUS = {'S02_05': (540, 1080, 1.06), 'S05_05': (540, 1000, 1.06), 'S06_05': (540, 1000, 1.05)}


def main():
    assets = {r['asset_id']: r for r in csv.DictReader(open(ROOT / 'ASSET_REGISTER.csv'))}
    board = list(csv.DictReader(open(ROOT / 'FULL_STORYBOARD.csv')))
    rows = [r for r in csv.DictReader(open(ROOT / 'SCENE_ASSET_MAP.csv')) if r['asset_id'] != 'BG_WHITE']
    order = [b['state_id'] for b in board]
    assert set(order) == set(CUES), set(order) ^ set(CUES)
    start = {s: round(CUES[s][0], 3) for s in order}
    assert all(start[a] < start[b] for a, b in zip(order, order[1:])), 'states must be in time order'
    end = {s: (start[order[i + 1]] if i + 1 < len(order) else DURATION) for i, s in enumerate(order)}
    scene_of = {b['state_id']: b['scene_id'] for b in board}

    lay = {}  # (state, layer) -> row
    for r in rows:
        lay[(r['state_id'], r['layer_id'].split('_', 2)[2])] = r
    tracks = {}

    def place(r):
        return dict(x=float(r['x']), y=float(r['y']), s=float(r['scale']), r=float(r['rotation_degrees']))

    def track(scene, layer, asset):
        key = f'{scene}:{layer}:{asset}'
        if key not in tracks:
            a = assets[asset]
            piv = json.loads(a['anchor_pivot_json'])
            lp = piv.get('feet') or piv.get('pivot') or [float(a['width']) / 2, float(a['height']) / 2]
            tracks[key] = dict(id=key, scene=scene, layer=layer, asset=asset, src='../' + a['filename'], w=float(a['width']), h=float(a['height']),
                               pivot=lp, wipe=WIPE.get(asset, ('lr', 0))[0] if asset in WIPE or asset.startswith('TX_') else None,
                               z=None, states=[], keys=[])
        return tracks[key]

    def key(t, tr, p, **v):
        k = dict(t=round(t, 4), x=p['x'], y=p['y'], s=p['s'], r=p['r'], k=1.0, o=1.0, wp=1.0, e='linear', px=None, py=None)
        k.update(v)
        tr['keys'].append(k)

    def enter(tr, t, p, op, group_pivot=None):
        a = tr['asset']
        gp = {}
        if group_pivot:  # express the shared world pivot in this layer's local units
            gp = dict(px=(group_pivot[0] - p['x']) / p['s'], py=(group_pivot[1] - p['y']) / p['s'])
        if a in TRAVEL_ASSETS.get(tr['layer'], ()):
            dx, dy, n = TRAVEL[tr['layer']]
            OPS['POSITION_XY travel along flow'] += 1
            key(t - F, tr, dict(p, x=p['x'] + dx, y=p['y'] + dy), o=0)
            key(t, tr, dict(p, x=p['x'] + dx, y=p['y'] + dy), o=0)
            key(t + 3 * F, tr, dict(p, x=p['x'] + dx * 0.9, y=p['y'] + dy * 0.9), o=1, e='linear')
            key(t + n * F, tr, p, e='inout')
            return t + n * F
        if a in WIPE or (a.startswith('TX_') and a not in BIG_NUMBERS):
            n = WIPE[a][1] if a in WIPE else WRITE.get(a) or max(8, min(16, round(tr['w'] * p['s'] / 60)))
            OPS['SOURCE_HIGHLIGHT wipe' if a.startswith('ANN_SOURCE') else 'TRACE_REVEAL wipe (arrow/diagram)' if a in WIPE else 'TRACE_REVEAL lettering write-on'] += 1
            key(t - F, tr, p, o=0, wp=0)
            key(t, tr, p, o=1, wp=0, e='step')
            key(t + n * F, tr, p, wp=1, e='out')
            return t + n * F
        if a.startswith('EVD_'):
            OPS['documentary evidence entrance'] += 1
            if a in FOCUS_CROPS:
                key(t - F, tr, p, o=0, k=0.85)
                key(t, tr, p, o=0, k=0.85)
                key(t + 8 * F, tr, p, e='out')
                return t + 8 * F
            key(t - F, tr, dict(p, y=p['y'] + 30), o=0)
            key(t, tr, dict(p, y=p['y'] + 30), o=0)
            key(t + 10 * F, tr, p, e='out')
            return t + 10 * F
        # pop: characters about their feet (or shared group pivot), props/numbers about their centre
        OPS['POP_IN (group pivot)' if group_pivot else 'POP_IN'] += 1
        k0 = 0.88 if a.startswith(('HOST_', 'SUPPORT_', 'HAND_')) or group_pivot else (0.6 if a in BIG_NUMBERS else 0.75)
        key(t - F, tr, p, o=0, k=k0, **gp)
        key(t, tr, p, o=0, k=k0, **gp)
        key(t + 3 * F, tr, p, o=1, k=k0 + (1 - k0) * 0.6, e='out', **gp)
        key(t + 9 * F, tr, p, k=1.0, e='back', **gp)
        return t + 9 * F

    def leave(tr, t, p, hard):
        OPS['exit (hard cut)' if hard else 'exit (5-frame fade)'] += 1
        if hard:
            key(t - 0.0005, tr, p)
            key(t, tr, p, o=0, e='step')
        else:
            key(t, tr, p)
            key(t + 5 * F, tr, p, o=0, k=0.97, e='inout')

    built = {}
    for i, s in enumerate(order):
        scene, T, cut, cues = scene_of[s], start[s], CUES[s][1], CUES[s][2]
        prev = order[i - 1] if i else None
        cur = {l: r for (st, l), r in lay.items() if st == s}
        old = {l: r for (st, l), r in lay.items() if st == prev} if prev else {}
        same = bool(prev) and scene_of[prev] == scene
        if prev and not same and cut:
            old_persist = {}  # a cut to a new scene: nothing carries over
        else:
            old_persist = old  # includes S04->S05, an authored non-cut scene change where the host continues
        group = GROUPS.get((scene, s), [])
        gpiv = None
        if group:
            hr = cur['HOST']; ha = json.loads(assets[hr['asset_id']]['anchor_pivot_json'])['feet']
            gpiv = (float(hr['x']) + float(hr['scale']) * ha[0], float(hr['y']) + float(hr['scale']) * ha[1])
        exits = [l for l in old if l not in cur or l not in old_persist]
        morph_src = {src for (st, _), (src, _) in MORPH.items() if st == s}
        for l in exits:
            if l in morph_src:
                continue  # leaves by gliding into its successor (below)
            r = old[l]
            leave(track(scene_of[prev], l, r['asset_id']), T, place(r), hard=cut)
        gap = 4 * F if (exits and not cut) else 0
        rank = 0
        finish = T
        for l, r in sorted(cur.items(), key=lambda kv: int(kv[1]['z_order'])):
            tr = track(scene, l, r['asset_id'])
            tr['states'].append(s)
            tr['z'] = tr['z'] if tr['z'] is not None else int(r['z_order'])
            p = place(r)
            if l in old_persist:
                o = old[l]; po = place(o)
                if o['asset_id'] == r['asset_id'] and po == p:
                    continue
                ts = cues.get(l, T)
                big = math.hypot(p['x'] - po['x'], p['y'] - po['y']) > 150
                person = r['asset_id'].startswith(('HOST_', 'SUPPORT_'))
                if same and o['asset_id'] == r['asset_id'] and not (big and person):
                    key(ts, tr, po); key(ts + 15 * F, tr, p, e='inout')  # prop glide / camera-like refit
                    OPS['POSITION_XY/SCALE glide (persistent prop)'] += 1
                    finish = max(finish, ts + 15 * F)
                    continue
                ot = track(scene_of[prev], l, o['asset_id'])
                if big or l in group or not same:  # relocate: old pose (and its held prop) fades, new pose pops in place
                    OPS['POSE_SWITCH with relocation'] += 1
                    leave(ot, ts, po, hard=cut)
                    finish = max(finish, enter(tr, ts + (0 if cut else RELOC), p, 'pop', gpiv if l in group else None))
                else:  # pose switch on the spot: step swap, then settle any small authored offset
                    OPS['POSE_SWITCH on the spot'] += 1
                    key(ts - 0.0005, ot, po); key(ts, ot, po, o=0, e='step')
                    key(ts - 0.0005, tr, po, o=0); key(ts, tr, po, e='step'); key(ts + 8 * F, tr, p, e='inout')
                    finish = max(finish, ts + 8 * F)
                continue
            if (s, l) in MORPH:  # glide the predecessor onto this layer's identical glyphs, then write on the rest
                src, n = MORPH[(s, l)]
                ot, po = track(scene_of[prev], src, old[src]['asset_id']), place(old[src])
                t0 = at(cues.get(l, T))
                key(t0, ot, po); key(t0 + n * F, ot, p, e='inout'); key(t0 + n * F + 0.0005, ot, p, o=0, e='step')
                frac = ot['w'] / tr['w']
                key(t0 + n * F, tr, p, o=0, wp=frac); key(t0 + n * F + 0.0005, tr, p, wp=frac, e='step')
                m = WRITE.get(r['asset_id'], 10)
                key(t0 + (n + m) * F, tr, p, e='out')
                OPS['MORPH glide into matching lettering'] += 1
                finish = max(finish, t0 + (n + m) * F)
                rank += 1
                continue
            if l in cues:
                t0 = at(cues[l])
            elif cut and rank == 0:
                t0 = T  # cut-then-push: the scene's first layer is on screen on the cut frame
            else:
                t0 = T + gap + 4 * F * rank
            rank += 1
            if cut and t0 == T and l not in group:  # visible on the cut frame, settles over 8 frames
                key(T - 0.0005, tr, p, o=0)
                key(T, tr, p, k=1.04, e='step')
                OPS['cut-then-push first layer'] += 1
                key(T + 8 * F, tr, p, e='out')
                finish = max(finish, T + 8 * F)
            else:
                finish = max(finish, enter(tr, t0, p, 'pop', gpiv if l in group else None))
        built[s] = round(finish, 3)
        if finish > end[s] + 1e-6:  # an entrance may finish inside the next state; fine unless that state moves the same layer
            print(f'note: {s} entrance finishes {finish - end[s]:.2f}s into the next state')

    # expression overlays: shown while the host pose holds still; the host's own eyes/brows/mouth are hidden meanwhile
    by_host = {}
    for (s, l), (face, tf) in sorted(FACES.items(), key=lambda kv: kv[1][1]):
        by_host.setdefault((scene_of[s], l, lay[(s, l)]['asset_id']), []).append((s, face, tf))
    for (scene, l, asset), faces in by_host.items():
        host = tracks[f'{scene}:{l}:{asset}']
        sub = json.loads(assets[asset]['editable_subparts_json'])
        parts = [i for k in ('eyes', 'brows', 'mouth') for i in (sub[k] if isinstance(sub[k], list) else [sub[k]])]
        for j, (s, face, tf) in enumerate(faces):
            gone = min([k['t'] for k in host['keys'] if k['t'] > tf and k['o'] < 0.5] + [DURATION])
            t1 = min(gone, faces[j + 1][2]) if j + 1 < len(faces) else gone
            assert all(k['t'] >= gone - 0.001 for k in host['keys'] if k['t'] > tf), f'{s}:{l} moves under its face overlay'
            hp = place(lay[(s, l)]); ax, ay = json.loads(assets[face]['anchor_pivot_json'])['host_attach']
            fp = dict(x=hp['x'] + hp['s'] * ax, y=hp['y'] + hp['s'] * ay, s=hp['s'], r=0.0)
            ft = track(scene, l + '_FACE', face)
            ft['states'].append(s); ft['z'] = host['z']
            key(tf - F, ft, fp, o=0); key(tf, ft, fp, e='step'); key(t1 - 0.0005, ft, fp); key(t1, ft, fp, o=0, e='step')
            host.setdefault('hide', []).append(dict(t0=round(tf, 4), t1=round(t1, 4), ids=parts))
            OPS['EXPRESSION_SWAP (FACE overlay)'] += 1
    for k, tr in tracks.items():
        tr['keys'].sort(key=lambda kk: kk['t'])

    cam = []
    segs = []
    for s in order:
        if CUES[s][1] or not segs:
            segs.append([])
        segs[-1].append(s)
    for sts in segs:
        t0, t1 = start[sts[0]], end[sts[-1]]
        cam.append(dict(t=t0, k=1.0, cx=540, cy=900, e='step'))
        k_end, c = 1.03, (540, 900)
        for s in sts:
            if s in CAMERA_FOCUS:
                cx, cy, kk = CAMERA_FOCUS[s]
                cam.append(dict(t=start[s], k=round(1 + 0.03 * (start[s] - t0) / (t1 - t0), 4), cx=540, cy=900, e='linear'))
                cam.append(dict(t=round(start[s] + 0.8, 3), k=kk, cx=cx, cy=cy, e='inout'))
                k_end, c = kk + 0.01, (cx, cy)
        cam.append(dict(t=round(t1 - 0.0005, 4), k=k_end, cx=c[0], cy=c[1], e='linear'))

    scene_rank = {sc: i for i, sc in enumerate(dict.fromkeys(scene_of[s] for s in order))}
    out = dict(
        fps=FPS, width=1080, height=1920, duration=DURATION, frames=math.ceil(round(DURATION * FPS, 6)), narration_duration=NARRATION, end_hold=END_HOLD,
        audio='audio/' + Path(AL['source']['project_copy']).name, audio_sha256=AL['source']['sha256'], audio_mix='audio/v3/FS02_V3_MIX.wav',
        note='Times in seconds. Keys interpolate x,y,s (authored placement), k (scale about pivot px/py or track pivot), r, o (opacity), wp (wipe 0..1). e = easing into that key: linear|out|inout|back|step.',
        states=[dict(id=s, scene=scene_of[s], start=start[s], end=round(end[s], 3), built=built[s], cut=CUES[s][1],
                     phrase=next(b['narration_phrase'] for b in board if b['state_id'] == s)) for s in order],
        operations=dict(sorted(OPS.items())), camera_keys=len(cam),
        camera=cam,
        tracks=sorted(tracks.values(), key=lambda tr: (scene_rank[tr['scene']], tr['z'] if tr['z'] is not None else 99, tr['id'])),
    )
    for tr in out['tracks']:
        for k in tr['keys']:
            for f in ('x', 'y', 's', 'k', 'r', 'o', 'wp'):
                k[f] = round(k[f], 4)
            if k['px'] is None:
                del k['px'], k['py']
    # closed-caption sidecar (approved wording, ASR phrase timing) for upload; nothing is burned into the picture
    def ts(x):
        return f"{int(x // 3600):02}:{int(x % 3600 // 60):02}:{int(x % 60):02},{round(x % 1 * 1000) % 1000:03}"
    srt = [f"{i}\n{ts(p['start'])} --> {ts(min(p['end'] + 0.25, NARRATION))}\n{p['text']}\n" for i, p in enumerate(AL['phrases'], 1)]
    (ROOT / 'animation/Finance_Short_02.en.srt').write_text('\n'.join(srt))
    (ROOT / 'animation/KEYFRAME_TIMELINE.json').write_text(json.dumps(out, separators=(',', ':')) + '\n')
    nkeys = sum(len(t['keys']) for t in out['tracks'])
    print(f"{len(out['tracks'])} tracks, {nkeys} keys, {len(cam)} camera keys, {out['frames']} frames")


RELOC = 6 * F  # relocation: old pose fully faded (5 frames) before the new one pops
TRAVEL_ASSETS = {'PAY_NOTE': ('PROP_NOTE',), 'NOTE': ('PROP_NOTE',)}

if __name__ == '__main__':
    main()
