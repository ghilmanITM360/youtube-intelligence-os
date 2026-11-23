"""ES1 original storyboard -> spec. Choices come from the documented grammar (05/06/12/14): one subject per beat, hard cuts, pop-in props,
slide-in character, pose switch for emotion, procedural chart/counter, one red accent, no camera, 24 fps motion, lowercase Comic 57 caption."""
import json, os
H = os.path.dirname(os.path.abspath(__file__)); fps = 30
def words(text, t0, per=.30):
    ws = text.split(); ev = []
    for i in range(len(ws)): ev.append(dict(t=round(t0 + i * per, 3), text=' '.join(ws[:i + 1]), full=text))
    return ev
RED = (200, 40, 45)
S = []
S.append(dict(id='S1', start=0, dur=3.0, elements=[
    dict(id='man', asset='assets/char_stick_worried_shrug.png', x=420, y=930, layer=1, enter=dict(preset='slide_left', t=0, dur=.35, dist=600),
         poses=[dict(t=2.0, asset='assets/char_stick_neutral_shrug.png')]),
    dict(id='q', asset='assets/prop_qcircle.png', x=760, y=780, scale=.8, layer=2, enter=dict(preset='pop', t=.9, dur=.2))]))
S.append(dict(id='S2', start=3.0, dur=3.0, elements=[
    dict(id='cost', type='counter', **{'from': 0, 'to': 1200}, prefix='$', size=170, font='comic_bold', color=RED, x=540, y=900, layer=1, t0=.2, dur=.9, enter=dict(preset='pop', t=.2, dur=.2)),
    dict(id='arr', type='arrow', len=220, x=540, y=1130, layer=1, t0=1.3, dur=.4, enter=dict(preset='cut', t=1.3)),
    dict(id='lbl', type='text', text='repair bill', font='hand', size=70, x=540, y=720, layer=1, enter=dict(preset='fade', t=.1, dur=.3))]))
S.append(dict(id='S3', start=6.0, dur=3.5, elements=[
    dict(id='ttl', type='text', text='saving grows', font='hand', size=72, x=540, y=700, layer=1, enter=dict(preset='cut', t=0)),
    dict(id='bars', type='bars', values=[1, 2, 3, 4, 5, 6], w=800, h=420, colors=[(235, 190, 50)] * 5 + [(80, 170, 90)], x=540, y=1000, t0=.3, dur=.6, stagger=.3, layer=1, enter=dict(preset='cut', t=0)),
    dict(id='m1', type='text', text='month 1', font='hand', size=40, x=210, y=1260, layer=1, enter=dict(preset='cut', t=.4)),
    dict(id='m6', type='text', text='month 6', font='hand', size=40, x=870, y=1260, layer=1, enter=dict(preset='cut', t=2.0))]))
S.append(dict(id='S4', start=9.5, dur=3.0, elements=[
    dict(id='man', asset='assets/char_stick_happy_down.png', x=380, y=930, layer=1, enter=dict(preset='cut', t=0), poses=[dict(t=1.2, asset='assets/char_stick_happy_up.png')]),
    dict(id='bag', asset='assets/prop_moneybag_pair.png', x=730, y=1060, scale=1.6, layer=2, enter=dict(preset='pop', t=.5, dur=.25),
         keys=[dict(t=.5, y=1060), dict(t=1.4, y=1030, ease='out')])]))
S.append(dict(id='S5', start=12.5, dur=2.0, elements=[
    dict(id='txt', type='text', text='start small', font='hand', size=120, x=540, y=800, layer=1, enter=dict(preset='cut', t=0)),
    dict(id='usd', asset='assets/prop_dollar.png', x=540, y=1050, scale=1.1, layer=1, enter=dict(preset='pop', t=.5, dur=.25))]))
cap = words('your car breaks down.', .3) + words('and the bill is due today.', 3.3) + words('so save a little every month.', 6.3) + words('three months of costs is a start.', 9.8) + words('start small. start today.', 12.7)
json.dump(dict(id='ES1_emergency_fund', w=1080, h=1920, fps=fps, motion_fps=24, bg=[253, 253, 253],
               caption=dict(font='comic', size=57, y=1353, wrap=800, stroke=1, events=cap), shots=S), open(os.path.join(H, 'original_ES1.json'), 'w'), indent=1)
