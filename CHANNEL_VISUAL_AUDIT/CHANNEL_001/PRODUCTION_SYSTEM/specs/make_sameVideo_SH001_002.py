"""Spec for reference 10nEByVLya0 f0-153 (SH001-SH002). Geometry measured from ref frames f10/30/60/90/110/140 (JPEG strip viewed);
circle drift 72 px/s left, pitch 270. SH002 element entry times are ESTIMATED (not frame-measured). Captions = OCR events (caption_ocr_10nE.json)."""
import json, os
H = os.path.dirname(os.path.abspath(__file__)); fps = 30
ocr = [e for e in json.load(open(os.path.join(H, '..', '..', 'RECONSTRUCTION_TESTS', 'same_video', 'caption_ocr_10nE.json'))) if e['f'] < 154]
cap = [dict(t=e['f'] / fps, text=' '.join(e['lines'])) for e in ocr]
cid, prev = [], ''
for c in cap:                       # chunk = run of events where text extends the previous; layout uses the longest text of the chunk
    if not c['text'].startswith(prev): cid.append([])
    if not cid: cid.append([])
    cid[-1].append(c); prev = c['text']
for ch in cid:
    full = max((c['text'] for c in ch), key=len)
    for c in ch: c['full'] = full
s1 = dict(id='SH001', start=0, dur=99 / fps, elements=[
    dict(id='q%d' % k, asset='assets/prop_qcircle.png', x=63 + 270 * k, y=954, scale=1.03, layer=1, enter=dict(preset='cut', t=.15 * k),
         keys=[dict(t=0, x=63 + 270 * k), dict(t=99 / fps, x=63 + 270 * k - 72 * 99 / fps, ease='linear')]) for k in range(5)] + [
    dict(id='chart', asset='assets/prop_chart_screen.png', x=510, y=960, layer=2, enter=dict(preset='pop', t=3.0 - .05, dur=.2))])
s2 = dict(id='SH002', start=99 / fps, dur=55 / fps, elements=[
    dict(id='chart', asset='assets/prop_chart_screen.png', x=225, y=966, scale=.55, layer=2, enter=dict(preset='cut', t=0),
         keys=[dict(t=0, x=510, y=960, scale=1), dict(t=.3, x=225, y=966, scale=.55, ease='out')]),
    dict(id='bag', asset='assets/prop_moneybag_pair.png', x=925, y=1120, scale=.9, layer=1, enter=dict(preset='pop', t=.15, dur=.2)),
    dict(id='qs1', asset='assets/prop_qcircle.png', x=123, y=771, scale=.5, layer=1, enter=dict(preset='pop', t=.2, dur=.15)),
    dict(id='qs2', asset='assets/prop_qcircle.png', x=336, y=1140, scale=.5, layer=1, enter=dict(preset='pop', t=.7, dur=.15)),
    dict(id='qb', asset='assets/prop_qcircle.png', x=561, y=954, scale=1.03, layer=1, enter=dict(preset='pop', t=.85, dur=.2)),
    dict(id='qs3', asset='assets/prop_qcircle.png', x=885, y=861, scale=.5, layer=1, enter=dict(preset='pop', t=1.2, dur=.15))])
json.dump(dict(id='same_video_SH001_002', w=1080, h=1920, fps=fps, motion_fps=24, bg=[253, 253, 253],
               caption=dict(font='comic', size=57, y=1353, wrap=800, stroke=1, events=cap), shots=[s1, s2]), open(os.path.join(H, 'same_video_SH001_002.json'), 'w'), indent=1)
