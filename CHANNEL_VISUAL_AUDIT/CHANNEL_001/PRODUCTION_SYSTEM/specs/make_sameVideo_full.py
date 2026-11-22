"""Full 22-shot spec for reference 10nEByVLya0 (SH001-SH022, f0-1659). Timings = blueprint state frames (EXACT/MEAS per blueprint); positions = measured bboxes /
thumbnail reads (blueprints + FRAME_REFERENCES). Asset policy: approved registry ids only; third-party media = labelled stand-in panels (tag 'STAND-IN');
shots whose required art is not approved = labelled 'BLOCKED' slates. Output is a progress render, NOT an approved reconstruction.
Element tags in id: 'si_' stand-in, 'bl_' blocked slate, 'est_' estimated position/time."""
import json, os
H = os.path.dirname(os.path.abspath(__file__)); fps = 30
ocr = json.load(open(os.path.join(H, '..', '..', 'RECONSTRUCTION_TESTS', 'same_video', 'caption_ocr_10nE.json')))
cap = [dict(t=e['f'] / fps, text=' '.join(e['lines'])) for e in ocr if not (780 <= e['f'] <= 824)]   # SH014 has no caption in the source; OCR read noise there
cap.append(dict(t=1048 / fps, text='then')); cap.sort(key=lambda c: c['t'])   # OCR stride gap f1046-1061: caption switches to 'then' at f1048 (read from source frames)
cid, prev = [], ''
for c in cap:
    if not c['text'].startswith(prev) or not cid: cid.append([])
    cid[-1].append(c); prev = c['text']
for ch in cid:
    full = max((c['text'] for c in ch), key=len)
    for c in ch: c['full'] = full
SPAN = {1: (0, 98), 2: (99, 153), 3: (154, 253), 4: (254, 365), 5: (366, 439), 6: (440, 476), 7: (477, 510), 8: (511, 540), 9: (541, 630), 10: (631, 663), 11: (664, 706),
        12: (707, 729), 13: (730, 779), 14: (780, 824), 15: (825, 849), 16: (850, 1046), 17: (1047, 1104), 18: (1105, 1159), 19: (1160, 1191), 20: (1192, 1288),
        21: (1289, 1460), 22: (1461, 1659)}
def T(n, f): return (f - SPAN[n][0]) / fps
def panel(id, x, y, w, h, label, n, f=None, fill=(205, 208, 214), **k):
    return dict(id=id, type='panel', x=x, y=y, w=w, h=h, fill=fill, label=label, layer=k.pop('layer', 1), enter=dict(preset='cut', t=T(n, f) if f else 0), **k)
def slate(id, x, y, w, h, label, n):   # blocked art: loud, never mistaken for a final frame
    return panel('bl_' + id, x, y, w, h, 'BLOCKED\n' + label, n, fill=(255, 225, 225), outline=(200, 40, 45), outline_w=6, label_color=(160, 20, 25))
def yr(id, x, txt, n, f=None, **k): return dict(id=id, type='text', text=txt, font='hand', size=80, x=x, y=968, layer=2, enter=dict(preset='cut', t=T(n, f) if f else 0), **k)
def tl(n, xs, f0=None):
    e = [yr('y%d' % i, x, t, n, f0) for i, (x, t) in enumerate(xs)]
    return e
shots = {}
SPM = json.load(open(os.path.join(H, '..', 'shot_sprites', 'sprites_meta.json'))) if os.path.exists(os.path.join(H, '..', 'shot_sprites', 'sprites_meta.json')) else json.load(open(os.path.join(H, '..', 'shot_sprites', 'sprites_meta.json')))
def spr(name, id=None, **k):
    """whole-figure/shot sprite placed at its measured playback-scale position (sprite centre); extra keys pass through"""
    m = SPM[name]; return dict(id=id or name, asset='shot_sprites/%s.png' % name, x=m['x0'] + m['w'] / 2, y=m['y0'] + m['h'] / 2, **k)
shots[1] = [dict(id='q%d' % k, asset='asset:prop_qcircle', x=63 + 270 * k, y=954, scale=1.03, layer=1, enter=dict(preset='cut', t=.15 * k),
                 keys=[dict(t=0, x=63 + 270 * k), dict(t=99 / fps, x=63 + 270 * k - 72 * 99 / fps, ease='linear')]) for k in range(5)] + [
    dict(id='chart', asset='asset:prop_chart_screen', x=510, y=960, layer=2, enter=dict(preset='pop', t=2.95, dur=.2))]
shots[2] = [dict(id='chart', asset='asset:prop_chart_screen', x=225, y=966, scale=.55, layer=2, keys=[dict(t=0, x=510, y=960, scale=1), dict(t=.3, x=225, y=966, scale=.55, ease='out')]),
            dict(id='bag', asset='asset:prop_moneybag_pair', x=925, y=1120, scale=.9, layer=1, enter=dict(preset='pop', t=.15, dur=.2)),
            dict(id='qs1', asset='asset:prop_qcircle', x=123, y=771, scale=.5, layer=1, enter=dict(preset='pop', t=.2, dur=.15)),
            dict(id='qs2', asset='asset:prop_qcircle', x=336, y=1140, scale=.5, layer=1, enter=dict(preset='pop', t=.7, dur=.15)),
            dict(id='qb', asset='asset:prop_qcircle', x=561, y=954, scale=1.03, layer=1, enter=dict(preset='pop', t=.85, dur=.2)),
            dict(id='qs3', asset='asset:prop_qcircle', x=885, y=861, scale=.5, layer=1, enter=dict(preset='pop', t=1.2, dur=.15))]
# SH003 (measured): bubble grows linearly d=60@f159 -> 493@f229 (stepped 24fps), alpha .62 over the approved dollar; f230-242 burst particles (static), f243+ dollar alone
shots[3] = [spr('dollar_bare', layer=2, enter=dict(preset='cut', t=0)),   # approved prop_dollar_sign is the in-bubble composite (not the bare $ the source shows at f154-158 / f243+)
            spr('bubble_disc', layer=3, enter=dict(preset='cut', t=T(3, 159)), exit=dict(t=T(3, 230)), keys=[dict(t=T(3, 159), scale=60 / 493.), dict(t=T(3, 229), scale=1.0, ease='linear')]),
            spr('burst_particles', layer=1, enter=dict(preset='cut', t=T(3, 230)), exit=dict(t=T(3, 243)))]
# SH004 (measured): man alone at +285px until f302, slides left linearly f302-319, Earth (googly eyes) cuts in at f319, lidded eyes + sweat drop from f339
shots[4] = [spr('man_brown', layer=2, keys=[dict(t=0, x=SPM['man_brown']['x0'] + SPM['man_brown']['w'] / 2 + 285), dict(t=T(4, 302), x=SPM['man_brown']['x0'] + SPM['man_brown']['w'] / 2 + 285), dict(t=T(4, 319), x=SPM['man_brown']['x0'] + SPM['man_brown']['w'] / 2, ease='linear')]),
            spr('earth_sh004_A', layer=1, enter=dict(preset='cut', t=T(4, 319)), exit=dict(t=T(4, 339))),
            spr('earth_sh004_B', layer=1, enter=dict(preset='cut', t=T(4, 339)))]
# SH005 / SH017 (measured by strip cross-correlation, rig_measurements/strip_offsets_raw.json): one timeline strip (2007..2012 + arrows, pitch 540) scrolls RIGHT 2080px f366-399 then stops;
# calendar+June cut in at f405; SH017 scrolls the same strip LEFT 432px f1063-1086. Per-frame x keys, linear, 24fps motion quantisation by the renderer.
OFF = json.load(open(os.path.join(H, '..', 'rig_measurements', 'strip_offsets_raw.json')))
def strip(n, f0, offs_for, cal_t):
    """offs_for(f) -> strip offset (px) at source frame f; returns years, arrows, calendar, June label"""
    fr = [f for f in range(f0, SPAN[n][1] + 1)]; prev = {}
    def ks(base):
        return [dict(t=T(n, f), x=base + offs_for(f), ease='linear') for f in fr]   # dense: one key per source frame (a sparse key set would interpolate across holds)
    el = []
    for Y in range(2007, 2013): el.append(dict(id='y%d' % Y, type='text', text=str(Y), font='hand_light', size=88, x=444 + 540 * (Y - 2007), y=965, layer=2, keys=ks(444 + 540 * (Y - 2007)), enter=dict(preset='cut', t=0)))
    am = SPM['arrow_left']; ax = am['x0'] + am['w'] / 2   # measured arrow centre (sprite), one per year gap
    for k in range(2007, 2012):
        el.append(dict(spr('arrow_left', id='ar%d' % k, layer=2, enter=dict(preset='cut', t=0)), x=ax + 540 * (k - 2007), keys=ks(ax + 540 * (k - 2007))))
    cm = SPM['calendar']; cx, cy = cm['x0'] + cm['w'] / 2, cm['y0'] + cm['h'] / 2
    el.append(dict(spr('calendar', layer=2, enter=dict(preset='cut', t=cal_t)), keys=ks(cx)))
    el.append(dict(id='june', type='text', text='June', font='hand_light', size=40, x=200, y=862, layer=2, enter=dict(preset='cut', t=cal_t), keys=ks(200)))
    return el
o5 = OFF['5']; o17 = OFF['17']
shots[5] = strip(5, 366, lambda f: (o5[min(f - 366, len(o5) - 1)] - 2080), T(5, 405))
shots[17] = strip(17, 1047, lambda f: o17[min(f - 1047, len(o17) - 1)], 0)
shots[6] = [panel('si_wallst', 515, 960, 1030, 607, 'STAND-IN third-party\nWall St sign + 2 clips', 6)]
shots[7] = [dict(id='t', type='text', text='The market:', font='hand', size=48, x=540, y=775, layer=2), panel('si_fire', 540, 1004, 496, 336, 'STAND-IN third-party\nfire meme clip', 7)]
# SH008/010/012/015: whole-figure pose sprites (shot_sprites/, measured, validated vs every source frame); static holds, hard cuts, same screen position in all four shots
for n, spr in ((8, 'hips_B_happy'), (10, 'hips_A_happy'), (12, 'hips_A_neutral'), (15, 'hips_A_neutral')):
    shots[n] = [dict(id='hips_man', asset='shot_sprites/%s.png' % spr, x=540, y=975, layer=1, enter=dict(preset='cut', t=0))]
shots[9] = [panel('si_logo', 540, 774, 336, 132, 'Blackstone', 9, fill=(10, 10, 10), label_color=(250, 250, 250), label_size=44),
            panel('si_p1', 384, 1038, 248, 324, 'STAND-IN\nportrait 1', 9, 566), panel('est_si_p2', 640, 1038, 248, 324, 'STAND-IN\nportrait 2', 9, 596)]
shots[11] = [panel('si_yacht', 540, 960, 600, 296, 'STAND-IN third-party\nyacht clip', 11), dict(id='bags', asset='asset:prop_moneybag_pair', x=216, y=1050, scale=.45, layer=2)]
shots[13] = [panel('si_baby', 540, 960, 1080, 643, 'STAND-IN cartoon\nbaby in bed', 13), panel('si_bubble', 790, 900, 300, 200, 'And my baby\nwill be called...', 13, 747, fill=(255, 255, 255), outline=(14, 14, 14), outline_w=5, shape='ellipse')]
shots[14] = [panel('si_newborn', 540, 960, 1080, 607, 'STAND-IN cartoon\nnewborn close-up\n"Peterson!"', 14)]
shots[16] = [panel('si_article', 560, 1000, 760, 560, 'STAND-IN third-party\nnews article page', 16), panel('si_logo', 900, 770, 220, 90, 'Blackstone', 16, 859, fill=(10, 10, 10), label_color=(250, 250, 250), label_size=30),
             panel('si_pp', 640, 1180, 330, 200, 'portraits', 16, 892)]
def boil(n, f0, f1, step=10):
    """SH018 source motion (measured): the whole Earth alternates between two drawings every 10 frames, no fades/flicker. State S0 first (f1105-1114), S1 f1115-1124 ..."""
    return [dict(t=(f - f0) / fps, asset='shot_sprites/earth_%s.png' % ('A' if i % 2 == 0 else 'B')) for i, f in enumerate(range(f0, f1, step))]
shots[18] = [dict(id='earth', asset='shot_sprites/earth_A.png', x=520, y=962, layer=1, enter=dict(preset='cut', t=0), poses=boil(18, 1105, 1160))]
shots[19] = [panel('si_tiles', 555, 960, 920, 500, 'STAND-IN third-party\nred meme tiles x6', 19, fill=(190, 40, 50), label_color=(255, 255, 255))]
shots[20] = [panel('si_chart', 540, 960, 607, 507, 'STAND-IN chart screenshot', 20),
             dict(id='arrow', type='arrow', len=100, x=420, y=1000, rot=30, color=(200, 40, 45), layer=3, enter=dict(preset='cut', t=T(20, 1226)), t0=T(20, 1226), dur=.8),
             dict(id='pct', type='text', text='90%', font='hand', size=60, color=(200, 40, 45), x=300, y=860, layer=3, enter=dict(preset='cut', t=T(20, 1251))),
             dict(id='face', asset='asset:char_head_shocked', x=760, y=1020, scale=.18, layer=3, enter=dict(preset='pop', t=T(20, 1264), dur=.15))]
shots[21] = [panel('si_card', 600, 1030, 760, 540, 'STAND-IN dark search card', 21, fill=(30, 30, 34), label_color=(240, 240, 240)),
             panel('est_ellipse', 560, 1010, 520, 90, '', 21, 1321, fill=None, outline=(200, 40, 45), outline_w=7, shape='ellipse'),
             panel('si_logo', 840, 1180, 220, 90, 'Blackstone', 21, fill=(10, 10, 10), label_color=(250, 250, 250), label_size=30)]
shots[22] = [panel('si_table', 283, 963, 364, 498, 'STAND-IN\ndata table', 22), panel('est_si_yellow', 130, 963, 60, 400, '', 22, 1534, fill=(250, 235, 90)),
             slate('man_peek', 80, 960, 160, 300, 'man_peek: hips/leaning\npose not approved', 22)]
out = []
for n in range(1, 23):
    a, b = SPAN[n]; out.append(dict(id='SH%03d' % n, start=a / fps, dur=(b - a + 1) / fps, elements=shots.get(n, [])))
json.dump(dict(id='same_video_full_progress', w=1080, h=1920, fps=fps, motion_fps=24, bg=[255, 255, 255],
               caption=dict(font='comic', size=57, y=1353, wrap=800, stroke=1, events=cap), shots=out), open(os.path.join(H, 'same_video_full_progress.json'), 'w'), indent=1)
print('shots', len(out), 'events', len(cap))
