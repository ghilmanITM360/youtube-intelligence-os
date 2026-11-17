"""Build the measured chair-test edit as native CapCut timeline materials.

Uses a CapCut-created image/audio/text sample from Timeline 02 as schema source.
Writes a replacement draft JSON to the workspace for review before installation.
"""

from __future__ import annotations

import copy
import json
import math
import uuid
from pathlib import Path

ROOT = Path('/Users/ghilmankhan/Movies/CapCut/User Data/Projects/com.lveditor.draft/0921')
TIMELINE = Path(__file__).with_name('timeline_02_before_edit.json')
OUT = Path(__file__).with_name('chair_test_completed_draft.json')
DOWNLOADS = Path('/Users/ghilmankhan/Downloads')
FPS = 30
END = 34.4
INK = '#252321'
RED = '#B94E4A'

def uid(): return str(uuid.uuid4()).upper()
def frame(t): return round(t * FPS)
def micro(t): return round(frame(t) * 1_000_000 / FPS)

draft = json.loads(TIMELINE.read_text())
video_sample = next(t for t in draft['tracks'] if t['type'] == 'video')
text_sample = next(t for t in draft['tracks'] if t['type'] == 'text')
audio_track = next(t for t in draft['tracks'] if t['type'] == 'audio')
video_segment = video_sample['segments'][0]
text_segment = text_sample['segments'][0]
video_material = draft['materials']['videos'][0]
text_material = draft['materials']['texts'][0]

draft['tracks'] = []
draft['materials']['videos'] = []
draft['materials']['texts'] = []
draft['canvas_config'] = {'ratio': '9:16', 'width': 1080, 'height': 1920, 'background': None}
draft['fps'] = {'num': 30, 'den': 1}
draft['duration'] = micro(END)

asset_ids = {}
def asset(filename):
    if filename not in asset_ids:
        mat = copy.deepcopy(video_material)
        mat['id'] = uid()
        mat['path'] = str(DOWNLOADS / filename)
        mat['material_name'] = filename
        mat['width'] = 941
        mat['height'] = 1672
        mat['local_material_id'] = uid()
        asset_ids[filename] = mat['id']
        draft['materials']['videos'].append(mat)
    return asset_ids[filename]

def track(kind):
    sample = video_sample if kind == 'video' else text_sample
    t = {k:copy.deepcopy(v) for k,v in sample.items() if k != 'segments'}
    t['id'] = uid()
    t['segments'] = []
    t['type'] = kind
    draft['tracks'].append(t)
    return t

background = track('video')
visual_tracks = []
label_tracks = []
caption_track = track('text')

def available(tracks, kind, a, b):
    for t in tracks:
        if all(s['target_timerange']['start'] + s['target_timerange']['duration'] <= micro(a)
               or s['target_timerange']['start'] >= micro(b) for s in t['segments']):
            return t
    t = track(kind)
    tracks.append(t)
    return t

def add_image(filename, a, b, scale=1, x=0, y=0, base=False):
    s = copy.deepcopy(video_segment)
    s['id'] = uid()
    s['material_id'] = asset(filename)
    s['target_timerange'] = {'start':micro(a), 'duration':micro(b)-micro(a)}
    s['source_timerange'] = {'start':0, 'duration':micro(b)-micro(a)}
    s['clip']['scale'] = {'x':scale, 'y':scale}
    s['uniform_scale'] = {'on':True, 'value':scale}
    s['clip']['transform'] = {'x':x, 'y':y}
    s['render_index'] = 0
    t = background if base else available(visual_tracks, 'video', a, b)
    t['segments'].append(s)
    return s

def add_text(value, a, b, x=0, y=0, size=28, color=INK, caption=False, scale=1):
    # CapCut's native font-size unit renders much larger than a canvas pixel.
    size = max(8, round(size * .36))
    m = copy.deepcopy(text_material)
    m['id'] = uid()
    m['type'] = 'text'
    m['name'] = value
    m['text_color'] = color
    m['font_size'] = float(size)
    m['text_size'] = size
    m['has_shadow'] = False
    m['shadow_alpha'] = 0.0
    m['use_effect_default_color'] = False
    m['alignment'] = 1
    m['font_path'] = '/Applications/CapCut.app/Contents/Resources/Font/SystemFont/en.ttf'
    m['font_name'] = 'System'
    m['fonts'] = []
    m['content'] = json.dumps({'styles':[{'fill':{'alpha':1.0,'content':{'render_type':'solid','solid':{'alpha':1.0,'color':[int(color[i:i+2],16)/255 for i in (1,3,5)]}}},'font':{'id':'','path':m['font_path']},'range':[0,len(value)],'size':float(size)}], 'text':value},separators=(',',':'))
    m['base_content'] = m['content']
    draft['materials']['texts'].append(m)
    s = copy.deepcopy(text_segment)
    s['id'] = uid()
    s['material_id'] = m['id']
    s['target_timerange'] = {'start':micro(a), 'duration':micro(b)-micro(a)}
    s['clip']['transform'] = {'x':x, 'y':y}
    s['clip']['scale'] = {'x':scale, 'y':scale}
    s['uniform_scale'] = {'on':True,'value':scale}
    s['caption_info'] = None
    (caption_track if caption else available(label_tracks,'text',a,b))['segments'].append(s)
    return s

# Background resets at semantic boundaries. No transitions or source-video layer.
cuts = [0,6.13,14.87,19.06,20.76,24.46,29.12,END]
for a,b in zip(cuts,cuts[1:]): add_image('BG_01_offwhite.png',a,b,base=True)

# SH01: simple test; safety condition interrupts.
add_image('CHAIR_01.png',1.52,6.13,.72,-.24,-.10)
add_image('STOPWATCH_OUTLINE_01.png',.88,6.13,.48,.30,.29)
add_text('30 s',.88,6.13,.34,.29,34)
hook_warning = add_image('WARNING_TRIANGLE_01.png',3.70,6.13,.38,.55,0)
hook_warning['common_keyframes'].append({
    'id':uid(), 'material_id':'', 'property_type':'KFTypeScaleX',
    'keyframe_list':[
        {'id':uid(),'curveType':'Line','time_offset':0,
         'left_control':{'x':0.0,'y':0.0},'right_control':{'x':0.0,'y':0.0},
         'values':[.342],'string_value':'','graphID':''},
        {'id':uid(),'curveType':'Line','time_offset':micro(4/FPS),
         'left_control':{'x':0.0,'y':0.0},'right_control':{'x':0.0,'y':0.0},
         'values':[.38],'string_value':'','graphID':''}]
})

# SH02: chair never moves. Hard anatomy replacements.
add_image('CHAIR_01.png',6.13,14.87)
add_image('PERSON_SEATED_01.png',6.13,11.36)
add_image('PERSON_STANDING_01.png',11.36,13.58)
add_image('PERSON_SEATED_01.png',13.58,14.87)
add_image('STOPWATCH_OUTLINE_01.png',7.30,14.87,.38,.37,.39)
add_text('30 s',8.30,14.87,.40,.39,30)
add_text('1',11.64,13.58,-.41,.30,33)
add_text('2',13.80,14.87,-.41,.30,33)

# SH03: steady, static person. Warning state arrives on spoken cues.
add_image('CHAIR_01.png',14.87,19.06)
add_image('PERSON_SEATED_01.png',14.87,19.06)
add_image('UNSTEADY_ARCS_01.png',16.20,19.06,1,-.34,0)
add_image('WARNING_TRIANGLE_01.png',17.36,19.06,.30,.55,.45)

# SH04: discrete stop punctuation.
add_image('STOPWATCH_OUTLINE_01.png',19.06,20.76,.55,0,.20)
add_image('WARNING_TRIANGLE_01.png',19.06,20.76,.25,.37,.34)
add_text('DO NOT TEST',19.20,20.76,0,-.25,40,RED)
add_text('×',19.20,20.76,0,.20,72,RED)

# SH05: one personal score and multiple people. Reject common cutoff logic.
add_image('SCORE_CARD_EMPTY_01.png',20.76,24.46,.65,0,.41)
add_text('YOUR SCORE',21.30,24.46,0,.49,25)
for x in [-.38,0,.38]:
    add_image('PERSON_STANDING_01.png',22.28,24.46,.27,x,-.12)
add_text('ONE NUMBER FOR EVERYONE',22.76,24.46,0,-.47,24)
add_text('≠',23.16,24.46,0,.12,48,RED)

# SH06: connection drawn, then rejected. No numerical threshold.
add_image('SCORE_CARD_EMPTY_01.png',24.46,29.12,.75,0,.36)
add_image('DIAGNOSIS_CARD_EMPTY_01.png',25.98,29.12,.85,0,-.15)
add_text('YOUR SCORE',24.46,29.12,0,.45,25)
add_text('DIAGNOSIS',25.98,29.12,0,-.23,20)
add_text('↓',26.74,27.56,0,.11,48)
add_text('≠',27.56,29.12,0,.11,56,RED)

# SH07: illustrated text conclusion. No invented portrait or branding.
add_image('SCORE_CARD_EMPTY_01.png',29.12,END,.55,0,.29)
add_text('YOUR SCORE',29.12,END,0,.35,28)
add_text('Interpret the score properly',30.76,END,0,-.02,28)
add_text('Full video on channel',31.96,END,0,-.29,32)

# Verbatim speech in readable thought groups. Caption-safe lower band.
captions = [
 (0,.88,'Before you try the'),(.88,2.56,'30-second chair stand test,'),
 (3.04,4.40,'there is one safety rule'),(4.40,5.38,"you shouldn't ignore."),
 (6.14,8.06,'So, start the counter,'),(8.06,9.10,'up to 30 seconds.'),
 (9.54,10.58,'Try to count the number'),
 (10.58,11.36,'of times that you can'),
 (11.36,12.40,'stand up on the chair'),
 (12.40,13.04,'unassisted'),
 (13.04,14.14,'and then sit down.'),
 (14.88,16.68,'However, if you feel unsafe,'),
 (16.68,17.36,'if you got'),
 (17.36,18.62,'dizziness or ataxia,'),(19.06,20.26,"then don't do this test."),
 (20.76,22.28,'Once you have your number,'),
 (22.28,23.16,"don't compare that to"),
 (23.16,24.02,'universal number.'),
 (24.46,26.28,'And even if your score looks low,'),
 (26.74,27.56,'that number alone'),
 (27.56,28.64,"doesn't diagnose you."),
 (29.12,30.76,'Dr. Rehan explains how to'),
 (30.76,31.68,'interpret it properly'),
 (31.68,33.04,'in the full video on the channel.')]
for a,b,value in captions:
    add_text(value,a,b,0,-.77,22,INK,caption=True)

for t in draft['tracks']:
    t['segments'].sort(key=lambda s:s['target_timerange']['start'])
draft['tracks'].append(audio_track)

ids = {m['id'] for group in draft['materials'].values() if isinstance(group,list) for m in group if isinstance(m,dict) and 'id' in m}
for t in draft['tracks']:
    for s in t['segments']:
        assert s['material_id'] in ids
        assert s['target_timerange']['duration'] > 0
assert len(background['segments']) == 7
OUT.write_text(json.dumps(draft,ensure_ascii=False,separators=(',',':')))
print(OUT)
print('tracks',[(t['type'],len(t['segments'])) for t in draft['tracks']])
print('materials',len(draft['materials']['videos']),len(draft['materials']['texts']),len(draft['materials']['audios']))
