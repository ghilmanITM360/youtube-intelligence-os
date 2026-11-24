"""CT_SCAN pilot, stage 2: merge my viewing of every event window into the ledgers, compare with the campaign ledger, write coverage and gates.
usage: python3 scripts/ct_pilot_code.py (video fixed below)"""
import csv, json, os, statistics as st, collections, sys
sys.path.insert(0, os.path.dirname(__file__))
V = '9VG0yqq_PHM'
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); O = f'{R}/ct_scan_pilot_{V}'
H, M, Lo = 'HIGH', 'MED', 'LOW'
# id: (class, what changed, confidence). Viewed on 200x112 native-frame windows (up to 8 native frames per event; sheet_NN.jpg).
C = {
'F001': ('FAINT_NOT_VISIBLE', 'frames 1-6, no visible change at 200 px', M), 'E001': ('LABEL_POP_ON', 'card tag "Q." appears', H),
'E002': ('TYPE_WRITE_ON', 'attribution line typed in the question card, about one character per frame', H), 'E003': ('TYPE_WRITE_ON', 'question text typed in the card over 6 frames', H),
'E004': ('SCENE_POP_ON', 'kitchen drawing appears inside the board in one frame', H), 'F002': ('FAINT_STABLE', 'window shows no visible change', M),
'F003': ('FAINT_NOT_VISIBLE', '7 frames of low-level full-frame change, not visible at 200 px', Lo), 'E005': ('OBJECT_POP_ON', 'toaster appears on the shelf', H),
'E006': ('OBJECT_POP_ON', 'small shelf item appears', M), 'E007': ('OBJECT_POP_ON', 'small shelf item appears', M),
'F004': ('TRANSITION_START', 'first ghosted frame of the zoom dissolve', M), 'E008': ('SCENE_DISSOLVE_ZOOM', '8-frame zoom and cross-dissolve to the close-up kitchen view (not a hard cut)', H),
'F005': ('FAINT_STABLE', 'no visible change', Lo), 'F006': ('FAINT_STABLE', 'no visible change', Lo), 'E009': ('POSE_SWAP', 'figure turns away from the pane in one frame', H),
'F007': ('LINE_WRITE_ON', 'red heat marks grow above the toaster over 6 frames', M), 'F008': ('PARTICLE_DRIFT', 'dots drift in around the scene and the toast darkens, 6 frames', M),
'E010': ('OBJECT_POP_ON', 'burnt toast appears', H), 'F009': ('FAINT_STABLE', 'no visible change', Lo), 'E011': ('STATE_SWAP', 'appliance state replaced and the figure now holds a plug', M),
'F010': ('FAINT_STABLE', 'no visible change', Lo), 'E012': ('OBJECT_POP_ON', 'small mark on the unit', Lo), 'E013': ('OBJECT_POP_ON', 'sparks at the plug', M),
'E014': ('HARD_CUT', 'white scene to grey scene with sparks', H), 'E015': ('LABEL_POP_ON', 'caption line appears at the top', H),
'E016': ('CUT_TO_TITLE_CARD', 'cut to the red series title card, 8-frame event', H), 'F011': ('TITLE_ANIMATION', 'title-card logo animation, 21 frames', M),
'E017': ('TITLE_ANIMATION', 'title-card logo animation', M), 'E018': ('TITLE_ANIMATION', 'title-card logo animation, 14 frames', M),
'F012': ('TITLE_CARD_OUT', 'last 7 frames of the title card, full-frame change before the cut', M), 'E019': ('HARD_CUT', 'red title card to white fridge scene', H),
'E020': ('OBJECT_POP_ON', 'toaster appears on the counter', H), 'F013': ('FAINT_STABLE', 'no visible change', Lo), 'E021': ('LABEL_POP_ON', '"FOR COOLING" label and dots', H),
'F014': ('FAINT_STABLE', 'no visible change', Lo), 'E022': ('LABEL_POP_ON', '"FOR HEATING" label with red heat marks', H), 'E023': ('OBJECT_POP_ON', 'steam lines over the toaster', M),
'E024': ('OBJECT_POP_ON', 'heating element drawn inside the toaster', H), 'E025': ('STATE_SWAP', 'toaster fills red', H), 'F015': ('FAINT_STABLE', 'no visible change', Lo),
'E026': ('TYPE_WRITE_ON', '"600 C" label typed over 3 frames', H), 'E027': ('HARD_CUT', 'toaster scene to temperature axis', H), 'F016': ('FAINT_STABLE', 'no visible change', Lo),
'E028': ('LABEL_POP_ON', '"ROOM TEMPERATURE" label and arrow', H), 'E029': ('LABEL_POP_ON', '"FRIDGE" label', H), 'E030': ('LABEL_POP_ON', '"FREEZER" label', H),
'E031': ('TYPE_WRITE_ON', 'bracket and "COLD (FOR TOASTER)" text drawn over 5 frames', H), 'F017': ('FAINT_STABLE', 'no visible change', Lo),
'E032': ('HARD_CUT', 'axis to a figure holding a smoking toaster', H), 'E033': ('LABEL_POP_ON', 'speech bubble', H), 'E034': ('HARD_CUT', 'to three figures at a fridge', H),
'F018': ('FAINT_STABLE', 'no visible change', Lo), 'E035': ('OBJECT_POP_ON', 'plug appears', M), 'E036': ('OBJECT_POP_ON', 'outlet appears', M), 'E037': ('STATE_SWAP', 'fridge door closes', H),
'F019': ('FADE_GLOW', 'red glow and frost drips grow over 6 frames', H), 'F020': ('FAINT_STABLE', 'no visible change', Lo), 'E038': ('TYPE_WRITE_ON', '"~1000W" typed over 3 frames', H),
'E039': ('HARD_CUT', 'to the appliance cutaway', H), 'F021': ('FAINT_STABLE', 'no visible change', Lo), 'E040': ('LINE_WRITE_ON', 'red arrow and "E_OUT" label drawn over 6 frames', H),
'F022': ('FAINT_STABLE', 'no visible change', Lo), 'E041': ('LABEL_POP_ON', '"COP = 3 (E_out/E_in)" label', H), 'E042': ('OBJECT_POP_ON', '"E_IN" arrow at the plug', H),
'E043': ('OBJECT_POP_ON', 'red radiating arrows', H), 'F023': ('FAINT_STABLE', 'no visible change', Lo), 'E044': ('OBJECT_POP_ON', 'toaster in the lower unit and a cable', H),
'F024': ('OBJECT_POP_ON', 'second plug and cable appear', M), 'E045': ('OBJECT_POP_ON', 'red arrow above the toaster', H), 'E046': ('OBJECT_POP_ON', 'arrow at the left plug', H),
'E047': ('LABEL_POP_ON', '"COP = 1" label on the toaster', H), 'F025': ('FAINT_NOT_VISIBLE', 'low-level full-frame change', Lo), 'E048': ('LINE_WRITE_ON', 'red upward arrows and black input arrows multiply over 9 frames', H),
'F026': ('LINE_WRITE_ON', 'arrow growth continues, 4 frames', M), 'F027': ('FAINT_STABLE', 'no visible change', Lo), 'E049': ('TYPE_WRITE_ON', '"~100W" typed over 4 frames', H),
'F028': ('FAINT_STABLE', 'no visible change', Lo), 'F029': ('FAINT_NOT_VISIBLE', 'tiny mark at the left edge', Lo), 'E050': ('TYPE_WRITE_ON', '"~1000W" typed on the left over 6 frames', H),
'F030': ('FADE_GLOW', 'toaster red fill fades in over 13 frames', H), 'E051': ('HARD_CUT', 'to the ice-cream-factory scene', H), 'F031': ('FAINT_STABLE', 'no visible change', Lo),
'F032': ('FADE_GLOW', 'toaster fades to red with a "600 C" label, 12 frames', H), 'F033': ('FADE_GLOW', 'red halo grows over 6 frames', H), 'F034': ('FAINT_STABLE', 'no visible change', Lo),
'E052': ('LABEL_POP_ON', '"-18 C" label', H), 'E053': ('HARD_CUT', 'to the Winnipeg scene', H), 'F035': ('FAINT_STABLE', 'no visible change', Lo),
'E054': ('FADE_DIM', 'scene dims to grey over 6 frames and a "(-20 C)" label appears; machine flagged a cut, it is a fade', H), 'F036': ('FAINT_STABLE', 'no visible change', Lo),
'E055': ('OBJECT_POP_ON', 'box (toaster) appears', H), 'E056': ('STATE_SWAP', 'toaster turns red and the figure changes pose', H), 'E057': ('POSE_SWAP', 'figure pose change', M),
'E058': ('POSE_SWAP', 'figure pose change', M), 'E059': ('POSE_SWAP', 'figure pose change', M), 'F037': ('FADE_POSE_DISSOLVE', 'pose cross-dissolve with ghosting and "AWOO" text appearing over 8 frames', H),
'E060': ('POSE_SWAP', 'figure sits, one-frame pose change', M), 'F038': ('FAINT_STABLE', 'no visible change', Lo), 'E061': ('HARD_CUT', 'to the podcast-table scene', H),
'F039': ('FAINT_STABLE', 'no visible change', Lo), 'E062': ('LABEL_POP_ON', 'speech bubble', H), 'E063': ('LABEL_POP_ON', 'second speech bubble', H),
'E064': ('HARD_CUT', 'to the closing red end card (10 s)', H), 'F040': ('TITLE_ANIMATION', 'one-frame change on the end card', Lo),
}
ev = list(csv.DictReader(open(O + '/events_machine.csv')))
assert {e['event_id'] for e in ev} == set(C), set(C) ^ {e['event_id'] for e in ev}
rows = []
for e in ev:
    c = C[e['event_id']]
    rows.append(dict(video_id=V, **e, event_class=c[0], what_changed=c[1], confidence=c[2], evidence_label='OBSERVED (viewed native-frame window, one coder)' if c[2] != Lo else 'OBSERVED_LOW (window too small or no visible change)'))
w = csv.DictWriter(open(O + '/visual_event_ledger_ct.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
# shots = hard cuts
hc = [r for r in rows if r['event_class'] in ('HARD_CUT', 'CUT_TO_TITLE_CARD')]
fps = 24.0; n = 3893
starts = [0] + [int(r['start_frame']) for r in hc]; ends = [s - 1 for s in starts[1:]] + [n - 1]
with open(O + '/shot_ledger_ct.csv', 'w', newline='') as o:
    cw = csv.writer(o); cw.writerow(['video_id', 'shot_id', 'start_frame', 'end_frame', 'start_pts_s', 'end_pts_s', 'duration_s', 'boundary_event', 'boundary_kind', 'events_in_shot'])
    for i, (a, b) in enumerate(zip(starts, ends), 1):
        k = sum(a < int(r['start_frame']) <= b for r in rows if r['event_class'] not in ('FAINT_STABLE',))
        cw.writerow([V, f'S{i:02d}', a, b, round(a / fps, 3), round((b + 1) / fps, 3), round((b - a + 1) / fps, 2), hc[i - 2]['event_id'] if i > 1 else 'video start', hc[i - 2]['event_class'] if i > 1 else '', k])
# stats
pf = list(csv.DictReader(open(O + '/per_frame_table.csv')))
by = collections.Counter(r['state'] for r in pf)
cls = collections.Counter(r['event_class'] for r in rows)
iv = list(csv.DictReader(open(O + '/state_intervals.csv'))); holds = [int(i['frames']) for i in iv if i['state'] == 'HOLD']
print('frames by state', dict(by)); print('event classes', dict(cls.most_common()))
print('HOLD intervals', len(holds), 'median frames', st.median(holds), 'max', max(holds), 'sum', sum(holds))
vis = [r for r in rows if r['event_class'] not in ('FAINT_STABLE', 'FAINT_NOT_VISIBLE')]
print('visible changes', len(vis), 'hard cuts', len([r for r in rows if r['event_class'] == 'HARD_CUT']) + 1, '(+1 cut to title)')
sh = list(csv.DictReader(open(O + '/shot_ledger_ct.csv'))); d = [float(s['duration_s']) for s in sh]; print('shots', len(sh), 'median', st.median(d), 'min', min(d), 'max', max(d))
# campaign comparison
from ledger_tune import campaign, match
csh, cev = campaign(V)
mine_c = [int(r['start_frame']) for r in hc]; mine_e = sorted({int(r['start_frame']) for r in vis})
print('campaign shots(boundaries)', len(csh), 'mine', len(mine_c), 'hit', match(csh, mine_c, 2), '| mine hit', match(mine_c, csh, 2))
print('campaign events', len(cev), 'mine visible', len(mine_e), 'hit(c->m,tol3)', match(cev, mine_e, 3), 'hit(m->c)', match(mine_e, cev, 3))
json.dump(dict(frames=len(pf), by_state=dict(by), classes=dict(cls), hold_intervals=len(holds), shots=len(sh), campaign=dict(shots=len(csh), events=len(cev))), open(O + '/stats.json', 'w'), indent=1)
