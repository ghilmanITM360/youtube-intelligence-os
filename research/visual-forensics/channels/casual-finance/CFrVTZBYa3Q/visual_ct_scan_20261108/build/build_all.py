# usage: build_all.py  (cwd = workspace)  -> ledgers, specs, coverage; deterministic from states_data.py + tables/*
import csv, json, sys, bisect, statistics as S, os
sys.path.insert(0, 'build'); from states_data import D, LAST
VID = 'CFrVTZBYa3Q'; FPS = 24
man = json.load(open('source_manifest.json')); fm = list(csv.DictReader(open('tables/frame_metrics.csv'))); eps = list(csv.DictReader(open('tables/episodes.csv')))
N = len(fm); assert N == 1189 and LAST == N - 1
pts = lambda f: round(f / FPS, 4)
iframes = set(man['iframe_indices'])
# ---- states
st = []
for i, d in enumerate(D):
    a = d[0]; b = (D[i+1][0] - 1) if i + 1 < len(D) else LAST
    seg = fm[a:b+1]; fr = [float(x['changed_frac_thr10']) for x in seg]; px = [int(x['fullres_changed_px_thr25']) for x in seg]
    st.append(dict(video_id=VID, visual_state_id=f'S{i+1:03d}', shot_id=d[1], start_pts_seconds=pts(a), end_pts_seconds=pts(b + 1), start_frame=a, end_frame=b, frames=b-a+1, duration_s=round((b-a+1)/FPS, 3),
        rep_frame=(a+b)//2, entering_class=d[2], label=d[3], visible_text=d[4] or '-', asset_ids=d[5] or '-', literal_description=d[6], onset_precision=d[7],
        entry_changed_frac=float(fm[a]['changed_frac_thr10']) if a else 0.0, entry_fullres_px=int(fm[a]['fullres_changed_px_thr25']) if a else 0,
        max_changed_frac=round(max(fr), 4), active_frames=sum(1 for x, p in zip(fr, px) if x >= 0.0006 or p >= 300), iframes_inside=sum(1 for f in range(a, b+1) if f in iframes)))
assert st[0]['start_frame'] == 0 and st[-1]['end_frame'] == LAST and all(st[k]['end_frame'] + 1 == st[k+1]['start_frame'] for k in range(len(st)-1))
def w(name, rows):
    with open(name, 'w', newline='') as f:
        q = csv.DictWriter(f, fieldnames=list(rows[0])); q.writeheader(); q.writerows(rows)
w('visual_states.csv', st)
# ---- shots
shots = {}
for s in st: shots.setdefault(s['shot_id'], []).append(s)
sh = []
for k, ss in shots.items():
    a, b = ss[0]['start_frame'], ss[-1]['end_frame']; hard = ss[0]['entering_class'].startswith(('CUT', 'START'))
    sh.append(dict(video_id=VID, shot_id=k, start_pts_seconds=pts(a), end_pts_seconds=pts(b+1), start_frame=a, end_frame=b,
        shot_boundary_evidence=('start of file' if a == 0 else f'hard cut: {ss[0]["entry_changed_frac"]:.3f} of pixels changed (thr10, 320px) / {ss[0]["entry_fullres_px"]} full-res px at f{a}; adjacent decoded frames f{a-1},f{a} viewed' if hard else 'n/a'),
        shot_verified='YES (OBSERVED + MEASURED)' if hard else 'n/a', subject='; '.join(sorted({x['label'] for x in ss}))[:160], setting='white canvas' if k not in ('SH018',) else 'black',
        framing='vertical 1080x1920, full-bleed screenshot or centred character', camera_motion='; '.join(sorted({x['entering_class'] for x in ss if 'PAN' in x['entering_class'] or 'SCROLL' in x['entering_class']})) or 'none',
        subject_motion='; '.join(sorted({x['entering_class'] for x in ss if x['entering_class'] not in ('HOLD', 'START', 'CUT')}))[:120] or 'none',
        graphics_text=' | '.join(x['visible_text'] for x in ss if x['visible_text'] != '-')[:200], entrance=ss[0]['entering_class'], exit=('hard cut' if k != 'SH018' else 'end of file'), narrative_function='see report', source_frame_refs=f'frames/episodes_*.jpg; frames/nat_*.jpg', uncertainty='shot grouping is INFERRED where a cut keeps the same page (none here)'))
w('shot_ledger.csv', sh)
# ---- events
CLS = {'CUT': 'SHOT_CUT', 'CUT+PAN': 'SHOT_CUT', 'CUT+ENTRY': 'SHOT_CUT', 'START': 'STATIC_HOLD', 'HOLD': 'STATIC_HOLD', 'PAN': 'CAMERA', 'PAN+DRAWON': 'CAMERA', 'SCROLL+SLIDE': 'CAMERA', 'POSE': 'CHARACTER', 'POP_IN': 'GRAPHIC/TEXT', 'TEXT_TYPE': 'GRAPHIC/TEXT', 'SLIDE_IN': 'GRAPHIC/TEXT', 'RISE_IN': 'CHARACTER', 'HOP_IN': 'CHARACTER', 'FADE+RISE': 'LIGHT/COLOR/EFFECT'}
epr = [(int(e['start_frame']), int(e['end_frame']), e['ep']) for e in eps]
def act_end(a, b):
    c = [e for e in epr if e[0] <= b and e[1] >= a]; return (min(b, max(e[1] for e in c)), ','.join(e[2] for e in c)) if c else (a, '-')
ev = []
for k, s in enumerate(st):
    a, b = s['start_frame'], s['end_frame']; cls = CLS[s['entering_class']]; before = st[k-1]['visual_state_id'] if k else '-'
    if cls == 'STATIC_HOLD': e1, ref = b, '-'
    else: e1, ref = act_end(a, b)
    prec = s['onset_precision']
    ev.append(dict(video_id=VID, shot_id=s['shot_id'], visual_state_id=s['visual_state_id'], event_id=f'E{k+1:03d}', start_pts_seconds=pts(a), end_pts_seconds=pts(e1 + 1), start_frame=a, end_frame=e1,
        event_class=cls, subject_object_id=s['asset_ids'].split(';')[-1] if s['asset_ids'] != '-' else '-', before_state=before, after_state=s['visual_state_id'], motion_vector_or_direction=('pan right (content moves left)' if 'PAN' in s['entering_class'] else 'enter from edge' if 'IN' in s['entering_class'] else 'none/measured only'),
        transition_type=s['entering_class'], source_frame_paths='frames/episodes_*.jpg;frames/nat_*.jpg;frames/onset_*.jpg;frames/anim_*.jpg;frames/cut1007_*.jpg', source_audio_reference='see audio_visual_alignment.csv', coverage_level='ADJACENT_DECODED_FRAMES' if prec == 'EXACT' else ('STEP_SAMPLED_BOUNDED' if prec.startswith('BOUND') else 'MEASURED_ACTIVITY_EDGE'),
        evidence_label='OBSERVED+MEASURED' if prec == 'EXACT' else ('ESTIMATED' if prec.startswith('BOUND') else 'MEASURED'), confidence='HIGH' if prec == 'EXACT' else 'MEDIUM',
        alternative_interpretation=('onset anywhere in ' + prec[5:-1] if prec.startswith('BOUND') else 'activity end taken at threshold; ease-out tail may be sub-threshold' if prec == 'MEAS' else 'none material'),
        creative_function_hypothesis='INFERRED: see report', editor_reconstruction_note=f'{s["label"]}: {s["frames"]} frames at 24 fps'))
w('visual_event_ledger.csv', ev)
# ---- ASR alignment
asr = json.load(open('audio/CFrV_small_en.json')); words = [(x['start'], x['end'], x['word'].strip()) for sg in asr['segments'] for x in sg['words']]; ws_ = [x[0] for x in words]
rows = []; offs = []
for e in ev:
    if e['event_class'] == 'STATIC_HOLD': continue
    t = float(e['start_pts_seconds']); i = bisect.bisect_left(ws_, t); c = [j for j in (i-1, i) if 0 <= j < len(words)]; j = min(c, key=lambda j: abs(words[j][0]-t)); off = round(t - words[j][0], 3); offs.append(off)
    ctx = ' '.join(x[2] for x in words[max(0, j-3):j+4])
    rows.append(dict(video_id=VID, event_id=e['event_id'], audio_source='local ASR openai-whisper small.en word timestamps (system python)', audio_listening_status='ASR_UNCERTIFIED - NO HUMAN LISTENING', phrase_or_sound=f'[{words[j][2]}] …{ctx}…',
        audio_start_pts=round(words[j][0], 3), audio_end_pts=round(words[j][1], 3), visual_start_pts=t, visual_end_pts=e['end_pts_seconds'], lead_lag_seconds=off, timestamp_method='visual PTS minus nearest ASR word start',
        confidence='MEDIUM (ASR word timing roughly +/-0.1-0.3 s; visual exact for EXACT rows)', limitations='ASR text unverified; no music/SFX claim; nearest word may be unrelated'))
w('audio_visual_alignment.csv', rows)
a_ = sorted(offs); n = len(a_)
json.dump(dict(events=n, median_lag=S.median(a_), p10=a_[n//10], p90=a_[9*n//10], within_0_3s=sum(abs(x) <= 0.3 for x in a_), text=asr['text']), open('tables/asr_alignment_summary.json', 'w'), indent=1)
# ---- per-state reconstruction specs
spec = []
for s in st:
    dur = s['frames']; anchors = [x for x in s['asset_ids'].split(';') if x and x != '-']
    third = [x for x in anchors if x.startswith('IMG_')]
    spec.append(dict(visual_state_id=s['visual_state_id'], frames=f"f{s['start_frame']}-f{s['end_frame']}", seconds=f"{s['start_pts_seconds']}-{s['end_pts_seconds']}", duration_frames=dur,
        image_prompt=f"ORIGINAL asset, 9:16 1080x1920, flat 2D hand-drawn explainer style on near-white (#FCFCFC) canvas, thick uneven black outlines, flat fills. Layout to rebuild: {s['literal_description']} Replace every third-party item ({', '.join(third) or 'none here'}) with your own licensed or self-made equivalent using your own data; no logos, no meme footage, no copied screenshots. Negative: gradients, glow, photoreal shading, 3D.",
        animation_prompt=f"Entry class {s['entering_class']} ({s['label']}), {dur} frames at 24 fps. Keep all unchanged anchors pixel-still; only the entering element(s) move. Onset precision {s['onset_precision']}. Camera: {'horizontal pan right across a screenshot wider than the frame' if 'PAN' in s['entering_class'] else 'locked'}. Sound: pending (no listening done).",
        anchors_static=anchors, qa_acceptance=f"Nearest-frame check: the first frame of this state must equal frame {s['start_frame']} +/-0 for EXACT onsets (+/-bound otherwise); the prior state's last frame must differ by the measured entry change ({s['entry_changed_frac']:.3f})."))
json.dump(spec, open('PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json', 'w'), indent=1)
# ---- headline numbers for the report
cuts = [s for s in st if s['entering_class'].startswith(('CUT',)) and s['start_frame'] > 0]
json.dump(dict(states=len(st), shots=len(sh), events=len(ev), hard_cuts=len(cuts), cut_frames=[s['start_frame'] for s in cuts], longest_hold=max((s['frames'], s['visual_state_id']) for s in st if s['entering_class'] in ('HOLD', 'START')),
  mean_state_s=round(sum(s['frames'] for s in st)/len(st)/FPS, 3), median_state_s=round(S.median(s['frames'] for s in st)/FPS, 3), episodes=len(eps), bound_onsets=sum(s['onset_precision'].startswith('BOUND') for s in st), exact_onsets=sum(s['onset_precision'] == 'EXACT' for s in st)), open('tables/key_facts.json', 'w'), indent=1)
print(open('tables/key_facts.json').read())
