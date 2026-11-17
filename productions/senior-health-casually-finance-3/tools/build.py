from pathlib import Path
import json,csv,math,hashlib,xml.etree.ElementTree as ET
from art import *
from story import SPECS
R=Path(__file__).resolve().parents[1]
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False))
def asset(id):
 if id.startswith('score'):
  val='9.5' if id=='score95' else '7'
  return 330,350,{'circle':path('M48 64 Q164 7 281 64 Q326 166 267 251 Q151 301 45 237 Q7 143 48 64 Z','#FAE7BC'),'value':text(val,164,161,96)+text('/ 10',166,215,39),'attribution':text('SPEAKER’S',165,294,36,font='Arial')+text('OPINION',165,333,36,font='Arial')},{'pivot':[165,155]}
 if id=='june-swim-warm':return swimmer()
 if id.split('-')[0] in ('sam','nora','june'):return person(*id.split('-'))
 return prop(id)
for folder,scenes in SPECS.items():
 P=R/folder;defs={};register=[]
 for id in sorted({l[0] for s in scenes for l in s[4]}):
  w,h,parts,anchors=asset(id);defs[id]=(w,h,parts,anchors)
  body=''.join(group(id+'--'+k,v) for k,v in parts.items());(P/'assets/svg'/f'{id}.svg').write_text(svg(w,h,body))
  layers=[]
  for k,v in parts.items():
   rel=f'assets/svg/parts/{id}--{k}.svg';p=P/rel;p.parent.mkdir(exist_ok=True);p.write_text(svg(w,h,group(id+'--'+k,v)))
   layers.append({'id':id+'--'+k,'svg':rel,'png':rel.replace('/svg/','/png/').replace('.svg','.png'),'z':len(layers),'registration':[0,0],'pivot':([143,244] if k=='rear-arm' else [258,244] if k=='front-arm' else [200,380] if k=='legs' else anchors['pivot'])})
  register.append({'asset_id':id,'design_id':id.split('-')[0] if '-' in id else 'rating' if id.startswith('score') else id,'category':'character' if id.split('-')[0] in ('sam','nora','june') else 'illustration','svg':f'assets/svg/{id}.svg','png':f'assets/png/{id}.png','width':w,'height':h,'anchors':anchors,'layers':layers,'provenance':'Original authored SVG paths; no copied/reference pixels','constraints':'Pose swap preferred; parts are not certified anatomical rigs.'})
 # Register is persisted after scene labels are added.
 asr_path=P/'script/ASR_SMALL_EN.json'
 if not asr_path.exists():asr_path=P/'script/ASR.json'
 asr=json.loads(asr_path.read_text());words=[w for seg in asr['segments'] for w in seg['words']]
 rows=[]; plans=[]
 for i,(start,end,title,sub,layers,note,claim) in enumerate(scenes):
  sid=f'S{i+1:02d}';f0=round(start*30);f1=math.ceil(end*30) if i==len(scenes)-1 else round(end*30)
  selected=[w for w in words if start<=w['start']<end];spoken=''.join(w['word'] for w in selected).strip()
  objects=[]
  for z,(id,x,y,scale,delay) in enumerate(layers):
   w,h,parts,anchors=defs[id];enter=min(f1-1,f0+round(delay*30));settle=min(f1-1,enter+(8 if delay else 0))
   frames=[]
   if enter>f0:frames.append({'frame':f0,'x':x,'y':y+24,'scale':scale,'rotation':0,'opacity':0,'easing':'hold'})
   frames.append({'frame':enter,'x':x,'y':y+(24 if delay else 0),'scale':scale,'rotation':0,'opacity':0 if delay else 1,'easing':'easeOutCubic' if delay else 'hold'})
   if settle>enter:frames.append({'frame':settle,'x':x,'y':y,'scale':scale,'rotation':0,'opacity':1,'easing':'hold'})
   frames.append({'frame':f1-1,'x':x,'y':y,'scale':scale,'rotation':0,'opacity':1,'easing':'hold'})
   objects.append({'instance_id':sid+'--'+id,'asset_id':id,'z':z,'pivot':anchors['pivot'],'entry':'visible_on_cut' if not delay else 'rise_24px_8frames','exit':'cut_at_scene_end','pose':id,'keyframes':frames,'hold_frames':max(0,f1-1-settle),'word_cue':next((w['word'].strip() for w in selected if w['start']>=enter/30),'scene boundary')})
  plan={'scene_id':sid,'start_seconds':start,'end_seconds':end,'in_frame':f0,'out_frame_exclusive':f1,'narration_verbatim_asr':spoken,'transcript_source':str(asr_path.relative_to(P)),'narration_status':'MACHINE_ASR_NOT_HUMAN_VERIFIED','title_proposed':title,'subtitle_proposed':sub,'claim_id':claim,'clinical_gate':'REVIEW_REQUIRED','source_technique':'CASUALLY_FINANCE_VISUAL_SPEC.md: additive reveal / retained character / staged comparison','transition':'hard cut; no added audio','continuity':note,'expected_result':note,'objects':objects}
  for obj in objects:
   if obj['asset_id']=='intervals':
    obj['component_visibility']=[{'target_id':obj['instance_id']+'--'+part,'asset_layer_id':'intervals--'+part,'visible_from_frame':min(f1-1,f0+round(delay*30)),'out_frame_exclusive':f1} for part,delay in [('baseline',.35),('work-1',.35),('rest-1',.7),('work-2',1.0),('rest-2',1.3),('work-3',1.6),('caption',.35)]]
  plans.append(plan)
  rows.append({'scene_id':sid,'start':start,'end':end,'spoken_words_ASR':spoken,'viewer_takeaway':title,'narrative_beat':'hook' if i==0 else 'payoff' if i==len(scenes)-1 else 'explanation_or_qualification','composition':'; '.join(f'{id}@({x},{y}) scale {sc}' for id,x,y,sc,de in layers),'character_pose_expression':'; '.join(l[0] for l in layers if l[0].split('-')[0] in ('sam','june','nora')),'environment':'; '.join(l[0] for l in layers if l[0] in ('park','clinic','pool')),'asset_ids':';'.join(l[0] for l in layers),'medical_diagram':';'.join(l[0] for l in layers if l[0] in ('heart','joint','lungs')),'layer_ids':';'.join(o['instance_id'] for o in objects),'entry_exit':'see KEYFRAME_PLAN.json; sequential 8-frame reveals then cut','keyframe_plan':f'animation_plan/KEYFRAME_PLAN.json#{sid}','hold':f'{end-start:.3f}s scene; per-object holds in plan','transition':'hard cut','CF_technique':'retained composition + progressive object reveal','clinical_qa':claim+': REVIEW_REQUIRED','continuity':note})
  for kind,copy in [('title',title),('subtitle',sub)]:
   if not copy:continue
   aid=sid+'-'+kind; size=62 if kind=='title' else 36
   fragment=group(aid,text(copy,540,76,size))
   (P/'assets/svg'/f'{aid}.svg').write_text(svg(1080,110,fragment))
   register.append({'asset_id':aid,'design_id':'text-label','category':'label','svg':f'assets/svg/{aid}.svg','png':f'assets/png/{aid}.png','width':1080,'height':110,'anchors':{'pivot':[540,55]},'layers':[],'provenance':'Proposed editorial overlay; not verbatim audio'})
   plan.setdefault('fixed_text_layers',[]).append({'asset_id':aid,'instance_id':aid,'x':0,'y':214 if kind=='title' else 294,'z':100,'opacity':1,'in_frame':f0,'out_frame_exclusive':f1})
  for label,frame in [('start',f0),('mid',(f0+f1-1)//2),('end',f1-1)]:
   b='<rect width="1080" height="1920" fill="white"/>'+text('AFTER 60  /  '+folder.split('_')[1],540,180,29,TEAL,font='Arial')
   b+=text(title,540,290,62)+ (text(sub,540,370,36) if sub else '')
   for obj in objects:
    kfs=obj['keyframes'];current=kfs[0]
    for k in kfs:
     if k['frame']<=frame:current=k
    if not current['opacity']:continue
    w,h,parts,_=defs[obj['asset_id']]
    b+=f'<g id="{obj["instance_id"]}" transform="translate({current["x"]} {current["y"]}) scale({current["scale"]})">'+''.join(group(obj['instance_id']+'--'+k,v) for k,v in parts.items() if not obj.get('component_visibility') or frame>=next(t['visible_from_frame'] for t in obj['component_visibility'] if t['asset_layer_id']==obj['asset_id']+'--'+k))+'</g>'
   b+=path('M100 1510 Q540 1504 980 1510','none','#D6DED8',3)+text('ILLUSTRATED REVIEW • ORIGINAL AUDIO UNCHANGED',540,1585,25,font='Arial')+text('Clinical wording and ASR need final review',540,1640,29,font='Arial')
   (P/'scene_states'/f'{sid}_{label}.svg').write_text(svg(1080,1920,b))
 dump(P/'assets/ASSET_REGISTER.json',register)
 dump(P/'animation_plan/KEYFRAME_PLAN.json',{'schema_version':'1.0','fps':30,'width':1080,'height':1920,'time_origin':'source container zero','duration_seconds':scenes[-1][1],'duration_frames':math.ceil(scenes[-1][1]*30),'interpolation':'linear values through easeOutCubic; step for hold; frames absolute; out exclusive','layer_transform':'translate(x,y) then rotate about asset pivot then uniform scale; rotation zero in supplied tracks','source_audio':'source_audio/narration_mix.wav','audio_processing':'none; no music/SFX added; mixed-source status unverified','scenes':plans})
 with (P/'storyboard/STORYBOARD.csv').open('w') as f:
  cw=csv.DictWriter(f,fieldnames=rows[0],lineterminator="\n");cw.writeheader();cw.writerows(rows)
 dump(P/'storyboard/STORYBOARD.json',rows)
 print(folder,len(register),'assets',len(scenes),'scenes')
