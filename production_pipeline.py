"""Voiceover to editable CapCut production package. Standard library plus ffprobe/Whisper."""
from __future__ import annotations
import argparse, csv, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path
from PIL import Image
from production_pipeline_providers import PromptOnlyImageGenerator

VERSION = '0.1.0'
BRAIN = Path(os.environ.get('PRODUCTION_BRAIN', Path(__file__).resolve().parent.parent / 'video data of what if' / 'production_intelligence_brain'))

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def stamp(seconds):
    ms = round(seconds * 1000)
    return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'

def media_info(path):
    return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(path)]))

def classify(text, index, count):
    s=text.lower()
    if index==0: return 'HOOK'
    if 'unsafe' in s or 'dizz' in s or 'ataxia' in s: return 'WARNING'
    if 'compare' in s or 'universal' in s: return 'REFRAME'
    if 'diagnos' in s: return 'CLAIM'
    if 'full video' in s or 'channel' in s: return 'CTA'
    if 'number' in s: return 'EXPLANATION'
    return 'SETUP' if index < count-1 else 'CONCLUSION'

def visual(kind):
    return {'HOOK':'TEXT_CARD','WARNING':'SEQUENTIAL_REVEAL','REFRAME':'COMPARISON','CLAIM':'TEXT_CARD','CTA':'TEXT_CARD','EXPLANATION':'NUMBER_CARD','SETUP':'DIAGRAM','CONCLUSION':'TEXT_CARD'}.get(kind,'NONE')

def asset_specs(kind):
    if kind=='WARNING': return [('chair','simple sturdy chair, seen in three-quarter view'),('caution','amber warning triangle with exclamation symbol')]
    if kind=='SETUP': return [('chair','simple sturdy chair, seen in three-quarter view'),('person','neutral adult standing beside chair, full body, anatomically plausible')]
    if kind=='EXPLANATION': return [('counter','simple circular counter ring with empty center')]
    if kind=='REFRAME': return [('scores','two distinct score tally cards without digits')]
    return []

def build(input_path, script_path, out, brain_path=BRAIN):
    out=Path(out); input_path=Path(input_path); script_path=Path(script_path)
    for d in ['source','transcript','planning','prompts','assets/overlays','assets/illustrations','captions','timeline','capcut','qc']:(out/d).mkdir(parents=True,exist_ok=True)
    source=out/'source'/('source'+input_path.suffix.lower()); shutil.copy2(input_path,source)
    written=script_path.read_text(); (out/'source'/'script.txt').write_text(written)
    info=media_info(source); duration=float(info['format']['duration']); has_video=any(s['codec_type']=='video' for s in info['streams'])
    raw_path=out/'transcript'/'whisper.json'
    if not raw_path.exists():
        subprocess.run([sys.executable,'-m','whisper',str(source),'--model','base','--language','English','--word_timestamps','True','--output_format','json','--output_dir',str(raw_path.parent),'--fp16','False'],check=True)
        produced=raw_path.parent/(source.stem+'.json'); produced.rename(raw_path)
    raw=json.loads(raw_path.read_text()); words=[]; repairs=[]
    for seg in raw['segments']:
        for item in seg.get('words',[]):
            word=item['word'].strip(); start=max(0,float(item['start'])); end=min(duration,float(item['end']))
            if word.lower()=='mh.' and start>duration-2: continue
            if word.lower()=='taxia,' and words and words[-1]['word'].lower()=='a':
                words[-1]['word']='ataxia,'; words[-1]['end_sec']=end; continue
            if words and start<words[-1]['end_sec']:
                repairs.append({'word':word,'old_start':start,'new_start':words[-1]['end_sec']}); start=words[-1]['end_sec']
            if not word or end<=start: continue
            words.append({'word_id':f'W{len(words)+1:04}','start_sec':round(start,3),'end_sec':round(end,3),'word':word,'confidence':item.get('probability')})
    if not words: raise ValueError('Whisper returned no word timestamps')
    with (out/'transcript'/'words.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(words[0]));writer.writeheader();writer.writerows(words)
    spoken=' '.join(w['word'] for w in words).replace('30 -second','30-second'); (out/'transcript'/'transcript.txt').write_text(spoken+'\n')
    # Boundaries follow punctuation or audible pauses. Word timestamps remain Whisper estimates.
    groups=[]; current=[]
    for w in words:
        if current and w['start_sec']-current[-1]['end_sec']>=0.55: groups.append(current);current=[]
        current.append(w)
        if re.search(r'[.!?]$',w['word']) and len(current)>=4: groups.append(current);current=[]
    if current:groups.append(current)
    sentences=[]
    for i,g in enumerate(groups,1):
        sentences.append({'sentence_id':f'S{i:03}','start_sec':g[0]['start_sec'],'end_sec':g[-1]['end_sec'],'text':' '.join(x['word'] for x in g),'first_word_id':g[0]['word_id'],'last_word_id':g[-1]['word_id'],'word_count':len(g)})
    with (out/'transcript'/'sentences.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(sentences[0]));wr.writeheader();wr.writerows(sentences)
    # Produce explicit silence coverage, so each shot spans start to next sentence start.
    beats=[]; scenes=[]; shots=[]; assets=[]; motions=[]; image_prompts=[]; actions=[]; captions=[]; sync=[]
    image_generator=PromptOnlyImageGenerator()
    background=out/'assets'/'illustrations'/'BACKGROUND.png'
    if not background.exists(): Image.new('RGB',(1080,1920),'#F6F3EA').save(background)
    assets.append({'asset_id':'A_BACKGROUND','path':'assets/illustrations/BACKGROUND.png','role':'background','asset_type':'PNG','transparent_background':False,'dimensions':[1080,1920],'safe_region':[0,0,1,1],'z_order':0,'initial_position':[0.5,0.5],'generation_strategy':'PROCEDURAL','reuse_key':'background','status':'READY','subject':'warm off-white canvas'})
    priors=[{'rule':'HARD_CUT','source':str(brain_path/'03_reconstruction_system/CAPCUT_PRODUCTION_SYSTEM.md'),'basis':'CORPUS_DERIVED'}, {'rule':'LOCKED_CAMERA','source':str(brain_path/'03_reconstruction_system/CAPCUT_PRODUCTION_SYSTEM.md'),'basis':'CORPUS_DERIVED'}]
    for i,s in enumerate(sentences):
        kind=classify(s['text'],i,len(sentences)); start=0.0 if i==0 else s['start_sec']; end=duration if i==len(sentences)-1 else sentences[i+1]['start_sec']; sid=f'SH{i+1:03}'; bid=f'B{i+1:03}'; scene=f'SC{i+1:03}'
        beat={'beat_id':bid,'start_sec':s['start_sec'],'end_sec':s['end_sec'],'text':s['text'],'primary_function':kind,'secondary_functions':[],'entities':[],'numbers':re.findall(r'\d+',s['text']),'concepts':[],'visual_importance':'HIGH' if kind in ('HOOK','WARNING','REFRAME') else 'MEDIUM','confidence':0.65,'reasoning_summary':'Deterministic lexical classification; review recommended.','provenance':'PROJECT_INFERENCE'};beats.append(beat)
        vf=visual(kind); specs=asset_specs(kind); shot_assets=[]
        for role,subject in specs:
            aid=f'A_{role.upper()}'
            if aid not in [a['asset_id'] for a in assets]:
                path=f'assets/overlays/{aid}.png'
                assets.append({'asset_id':aid,'path':path,'role':role,'asset_type':'TRANSPARENT_PNG','transparent_background':True,'dimensions':[1080,1920],'safe_region':[0.08,0.12,0.92,0.86],'z_order':3,'initial_position':[0.5,0.48],'generation_strategy':'PROMPT_ONLY','reuse_key':role,'status':'PENDING_GENERATION','subject':subject})
                prompt=f'Create one isolated {subject}. Original flat editorial vector illustration. Thick rounded navy outline, restrained coral and teal fills, minimal interior detail. Center object with generous clear margin. Orthographic three-quarter perspective where applicable. Transparent background, 9:16 canvas, 1080x1920. No text, letters, numbers, watermark, logo, brand, shadows, gradient, photo texture, or background scene. Keep scale and line weight consistent with all project objects.'
                image_generator.generate(prompt,out/path)
                image_prompts.append({'asset_id':aid,'expected_output':path,'narrative_purpose':kind,'subject':subject,'composition':'single isolated object','framing':'centered, generous margin','background':'transparent','visual_hierarchy':'one clear focal object','placement':'center','perspective':'orthographic three-quarter when applicable','illustration_treatment':'original flat editorial vector','palette':['#17263C','#16A6A0','#F27863','#F3C85A'],'line_treatment':'thick rounded navy outline','aspect_ratio':'9:16','transparent_background':True,'consistency_rules':'Same contour thickness, flat color, no branded motifs.','negative_constraints':'No text, numbers, watermark, logos, gradients, or photo texture.','prompt':prompt})
            shot_assets.append(aid)
        strategy='CAPCUT_NATIVE' if shot_assets else 'STATIC'
        shot={'shot_id':sid,'scene_id':scene,'beat_id':bid,'start_sec':round(start,3),'end_sec':round(end,3),'duration_sec':round(end-start,3),'narration':s['text'],'visual_purpose':kind,'visual_function':vf,'speaker_visible':has_video and not shot_assets,'composition':{'aspect_ratio':'9:16','background':'warm off-white','foreground':shot_assets,'layout':'central object with captions in lower safe area'},'assets':shot_assets,'transition_in':'HARD_CUT' if i else 'NONE','transition_out':'HARD_CUT' if i<len(sentences)-1 else 'NONE','camera':{'mode':'LOCKED'},'motion_strategy':strategy,'confidence':0.65,'provenance':{'semantic':'PROJECT_INFERENCE','production_grammar':priors}};shots.append(shot)
        scenes.append({'scene_id':scene,'shot_ids':[sid],'start_sec':round(start,3),'end_sec':round(end,3),'purpose':kind})
        if i:actions.append({'time':round(start,3),'operation':'HARD_CUT','shot_id':sid,'track':1})
        for j,aid in enumerate(shot_assets):
            a=next(a for a in assets if a['asset_id']==aid); reveal=min(end-0.05,start+0.15+j*0.35); reveal=max(start,reveal)
            m={'motion_id':f'M{len(motions)+1:03}','shot_id':sid,'asset_id':aid,'track':3+j,'z_order':3+j,'start_sec':round(start,3),'end_sec':round(end,3),'reveal_sec':round(reveal,3),'position_start':[0.5,0.46],'position_end':[0.5,0.46],'scale_start':1.0,'scale_end':1.06,'opacity_start':0.0,'opacity_end':1.0,'rotation_start_deg':0,'rotation_end_deg':0,'mask':None,'keyframes':[{'time':round(reveal,3),'opacity':0,'scale':1.0},{'time':round(min(end,reveal+0.4),3),'opacity':1,'scale':1.06}],'easing':'EASE_OUT'}; motions.append(m)
            actions += [{'time':round(start,3),'operation':'ADD_MEDIA','asset':a['path'],'track':3+j,'duration_sec':round(end-start,3),'shot_id':sid}, {'time':round(reveal,3),'operation':'POSITION','asset':a['path'],'track':3+j,'value':[0.5,0.46]}, {'time':round(reveal,3),'operation':'SET_OPACITY','asset':a['path'],'track':3+j,'value':0}, {'time':round(reveal,3),'operation':'ADD_KEYFRAME','asset':a['path'],'track':3+j,'value':m['keyframes'][0]}, {'time':round(min(end,reveal+0.4),3),'operation':'ADD_KEYFRAME','asset':a['path'],'track':3+j,'value':m['keyframes'][1]}, {'time':round(end,3),'operation':'HIDE','asset':a['path'],'track':3+j}]
        if kind in ('HOOK','WARNING','REFRAME','CLAIM','CTA'):
            label={'HOOK':'30-second chair stand','WARNING':'Stop if unsafe or dizzy','REFRAME':'No universal score','CLAIM':'Score alone is not a diagnosis','CTA':'Full video on channel'}[kind]
            actions.append({'time':round(start,3),'operation':'ADD_TEXT','track':6,'text':label,'duration_sec':round(end-start,3),'shot_id':sid})
        captions.append({'caption_id':f'C{i+1:03}','start_sec':s['start_sec'],'end_sec':s['end_sec'],'text':s['text'],'emphasis_words':re.findall(r'unsafe|dizziness|ataxia|diagnose|30-second',s['text'],re.I),'priority':kind})
        sync.append({'word_id':s['first_word_id'],'shot_id':sid,'event':'SHOT_START','time_sec':s['start_sec']})
    # Caption groups follow actual word boundaries, capped for mobile readability.
    captions=[]; chunk=[]
    def flush_caption():
        if not chunk:return
        text=' '.join(w['word'] for w in chunk).replace('30 -second','30-second')
        captions.append({'caption_id':f'C{len(captions)+1:03}','start_sec':chunk[0]['start_sec'],'end_sec':chunk[-1]['end_sec'],'text':text,'emphasis_words':re.findall(r'unsafe|dizziness|ataxia|diagnose|30-second',text,re.I),'priority':'NORMAL'})
    for w in words:
        proposal=' '.join(x['word'] for x in chunk+[w])
        if chunk and (len(chunk)>=9 or len(proposal)>50 or w['start_sec']-chunk[-1]['end_sec']>0.55):
            flush_caption();chunk=[]
        chunk.append(w)
        if re.search(r'[.!?]$',w['word']) and len(chunk)>=3:flush_caption();chunk=[]
    flush_caption()
    write_json(out/'transcript'/'semantic_beats.json',beats);write_json(out/'planning'/'scenes.json',scenes);write_json(out/'planning'/'shots.json',shots);write_json(out/'planning'/'asset_plan.json',assets);write_json(out/'planning'/'motion_plan.json',motions)
    write_json(out/'prompts'/'IMAGE_PROMPTS.json',image_prompts)
    (out/'prompts'/'IMAGE_PROMPTS.md').write_text('# Image prompts\n\n'+'\n\n'.join(f"## {p['asset_id']} — {p['expected_output']}\n\n{p['prompt']}" for p in image_prompts)+'\n')
    write_json(out/'prompts'/'ANIMATION_PROMPTS.json',[]);(out/'prompts'/'ANIMATION_PROMPTS.md').write_text('# Animation prompts\n\nNo image-to-video shots justified. All planned motion uses CapCut keyframes.\n')
    style={'corpus_priors':priors,'project_decisions':{'illustration':'original flat editorial vector','background':'#F6F3EA','outline':'#17263C','accent':'#16A6A0','warning':'#F27863','camera':'locked','transition':'hard cut'},'provenance_note':'Color and illustration style are original project choices, not corpus measurements.'};write_json(out/'STYLE_BIBLE.json',style);(out/'STYLE_BIBLE.md').write_text('# Style bible\n\nLocked camera and hard cuts derive from referenced corpus. Original vector identity, palette, and layouts are project decisions.\n')
    write_json(out/'COLOR_RULES.json',style['project_decisions']);write_json(out/'LAYOUT_RULES.json',{'canvas':[1080,1920],'caption_safe_bottom':0.18,'object_safe_region':[0.08,0.12,0.92,0.76],'coordinates':'normalized from upper left'});write_json(out/'ASSET_REGISTRY.json',assets)
    (out/'captions'/'captions.srt').write_text('\n\n'.join(f"{i+1}\n{stamp(c['start_sec'])} --> {stamp(c['end_sec'])}\n{c['text']}" for i,c in enumerate(captions))+'\n',encoding='utf-8');write_json(out/'captions'/'caption_plan.json',captions)
    timeline={'schema_version':'1.0','project':{'name':out.name,'duration_sec':duration,'canvas':[1080,1920]},'source_media':[{'path':str(source.resolve()),'type':'video' if has_video else 'audio','duration_sec':duration}],'scenes':scenes,'shots':shots,'tracks':[{'id':1,'role':'source_video' if has_video else 'voiceover'},{'id':3,'role':'illustrations'},{'id':6,'role':'editable_text'}],'assets':assets,'audio':[{'path':str(source.resolve()),'master':True,'start_sec':0,'end_sec':duration}],'captions':captions,'motions':motions,'keyframes':[{'motion_id':m['motion_id'],**k} for m in motions for k in m['keyframes']],'transitions':[{'type':'HARD_CUT','time_sec':s['start_sec']} for s in shots[1:]],'sync_events':sync};write_json(out/'timeline'/'timeline.json',timeline)
    actions=[{'time':0,'operation':'IMPORT_MEDIA','asset':str(source.resolve())},{'time':0,'operation':'ADD_MEDIA','asset':str(source.resolve()),'track':1,'duration_sec':duration},{'time':0,'operation':'SET_VOLUME','track':1,'value':1.0},{'time':0,'operation':'ADD_MEDIA','asset':'assets/illustrations/BACKGROUND.png','track':2,'duration_sec':duration}]+[{'time':0,'operation':'IMPORT_MEDIA','asset':a['path']} for a in assets]+actions+[{'time':0,'operation':'IMPORT_SRT','asset':'captions/captions.srt','track':7}]
    actions.sort(key=lambda a:(a['time'],0 if a['operation']=='IMPORT_MEDIA' else 1));write_json(out/'capcut'/'CAPCUT_ACTIONS.json',{'schema_version':'1.0','actions':actions})
    missing=[a['asset_id'] for a in assets if not (out/a['path']).exists()];manifest={'source_video':str(source.resolve()) if has_video else None,'voiceover':str(source.resolve()),'images':[a['path'] for a in assets if a['asset_id'] not in missing],'captions':'captions/captions.srt','expected_missing_assets':missing,'ready_for_capcut':not missing};write_json(out/'capcut'/'MEDIA_IMPORT_MANIFEST.json',manifest)
    build_lines=['# CapCut build','Use original voiceover as timing master. Canvas: 1080 × 1920. Track 1: source media. Track 7: imported SRT.','']
    for s in shots:
        build_lines += [f"## {s['shot_id']} {stamp(s['start_sec'])} to {stamp(s['end_sec'])}",f"Narration: {s['narration']}",f"Visual: {s['visual_function']}. Camera: locked. Transition: {s['transition_in']}.",f"Assets: {', '.join(s['assets']) or 'none; editable CapCut text only'}.", '']
    build_lines += ['Follow CAPCUT_ACTIONS.json for exact tracks, keyframes, normalized positions, opacity, and times.'];(out/'capcut'/'CAPCUT_BUILD.md').write_text('\n'.join(build_lines)+'\n')
    (out/'capcut'/'CHATGPT_WORK_CAPCUT_PROMPT.md').write_text(f'''# ChatGPT Work CapCut task\n\nOpen CapCut Desktop and create/open project `{out.name}`. Read package at `{out.resolve()}`. Read `capcut/MEDIA_IMPORT_MANIFEST.json` first. Stop and report missing assets if `ready_for_capcut` is false; their exact paths and prompts are in `ASSET_REGISTRY.json` and `prompts/IMAGE_PROMPTS.md`.\n\nImport source media and all ready images. Place original source video on primary track if supplied; this package contains voiceover only, so place original MP3 on Track 1. Keep original audio unchanged. Read `capcut/CAPCUT_ACTIONS.json`; execute operations in timestamp order, using specified asset, track, duration, normalized position, scale, rotation, opacity, mask, keyframes, and easing. Use hard cuts where specified. Add editable text layers. Import `captions/captions.srt`. Avoid random templates and generic effects. Preview full edit, fix GUI placement issues without changing timing or visual intent, then present final review before export. Do not manipulate undocumented CapCut project files.\n''')
    script_words=re.findall(r"[\w'-]+",written.lower());spoken_words=re.findall(r"[\w'-]+",spoken.lower());difference={'written_word_count':len(script_words),'spoken_word_count':len(spoken_words),'written_only_terms':sorted(set(script_words)-set(spoken_words)),'spoken_only_terms':sorted(set(spoken_words)-set(script_words)),'timing_authority':'MP3 / Whisper word alignment'};write_json(out/'transcript'/'script_difference.json',difference);write_json(out/'transcript'/'timing_repairs.json',repairs)
    write_json(out/'PROJECT_MANIFEST.json',{'pipeline_version':VERSION,'timeline_schema':'1.0','input_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),'duration_sec':duration,'brain_path':str(brain_path),'brain_available':brain_path.exists(),'source':'USER_PROVIDED','asset_count':len(assets)})
    validate(out)
    return out

def validate(out):
    out=Path(out); t=json.loads((out/'timeline'/'timeline.json').read_text());actions=json.loads((out/'capcut'/'CAPCUT_ACTIONS.json').read_text())['actions'];duration=t['project']['duration_sec'];assets=t['assets']; missing=[a['asset_id'] for a in assets if not (out/a['path']).exists()]
    timeline_schema=json.loads((Path(__file__).resolve().parent/'timeline/schema/v1.json').read_text())
    action_schema=json.loads((Path(__file__).resolve().parent/'timeline/schema/capcut_actions_v1.json').read_text())
    checks={'schema_version':t['schema_version']=='1.0' and all(k in t for k in timeline_schema['required']),'transcript_words':bool((out/'transcript'/'words.csv').stat().st_size),'shot_coverage':bool(t['shots']) and t['shots'][0]['start_sec']==0 and abs(t['shots'][-1]['end_sec']-duration)<0.01 and all(abs(a['end_sec']-b['start_sec'])<0.01 for a,b in zip(t['shots'],t['shots'][1:])),'beat_linkage':all(s['beat_id'] in {b['beat_id'] for b in json.loads((out/'transcript'/'semantic_beats.json').read_text())} for s in t['shots']),'prompt_coverage':all(a['generation_strategy']=='PROCEDURAL' or a['asset_id'] in {p['asset_id'] for p in json.loads((out/'prompts'/'IMAGE_PROMPTS.json').read_text())} for a in assets),'motion_validity':all(0<=m['start_sec']<=m['reveal_sec']<=m['end_sec']<=duration and all(m['start_sec']<=k['time']<=m['end_sec'] for k in m['keyframes']) for m in t['motions']),'capcut_action_times':all(0<=a['time']<=duration for a in actions), 'capcut_action_schema':all(a['operation'] in action_schema['properties']['actions']['items']['properties']['operation']['enum'] for a in actions),'srt_valid':(out/'captions'/'captions.srt').read_text().count(' --> ')==len(t['captions']),'asset_status_explicit':all((out/a['path']).exists() or a['status']=='PENDING_GENERATION' for a in assets)}
    editorial_warnings=[]
    transcript=(out/'transcript'/'transcript.txt').read_text().lower()
    if 'stand up on the chair' in transcript: editorial_warnings.append('Voiceover says stand up on the chair; confirm intended wording before publication. Visuals must not depict standing on the chair.')
    sys.path.insert(0,str(Path(__file__).resolve().parent/'scripts'));from check_slop_risk import run as slop_gate  # AGENTS.md pre-delivery gate
    slop=slop_gate(out/'source'/'script.txt',project=out.name,images=[out/'assets']);checks['slop_risk_gate']=slop['verdict']!='FAIL'
    editorial_warnings+=[f"AI-slop gate {slop['verdict']} {f['rule']}: {f['detail']}" for f in slop['findings']]
    ready=all(checks.values()) and not missing;report={'editorial_warnings':editorial_warnings,'checks':checks,'missing_assets':missing,'ready_for_capcut':ready,'counts':{'words':sum(1 for _ in csv.DictReader((out/'transcript'/'words.csv').open())),'beats':len(json.loads((out/'transcript'/'semantic_beats.json').read_text())),'shots':len(t['shots']),'assets':len(assets),'actions':len(actions)}};write_json(out/'qc'/'validation.json',report)
    (out/'qc'/'QC_REPORT.md').write_text('# QC report\n\n'+''.join(f"- {'PASS' if v else 'FAIL'} {k}\n" for k,v in checks.items())+f"\nWARNING: {len(missing)} image assets pending generation.\n"+''.join(f'WARNING: {w}\n' for w in editorial_warnings)+f"\nREADY_FOR_CAPCUT: {str(ready).lower()}\n")
    manifest=json.loads((out/'capcut'/'MEDIA_IMPORT_MANIFEST.json').read_text());manifest['expected_missing_assets']=missing;manifest['images']=[a['path'] for a in assets if a['asset_id'] not in missing];manifest['ready_for_capcut']=ready;write_json(out/'capcut'/'MEDIA_IMPORT_MANIFEST.json',manifest)
    for a in assets:
        a['status']='READY' if a['asset_id'] not in missing else 'PENDING_GENERATION'
        if (out/a['path']).exists():
            with Image.open(out/a['path']) as im: a['actual_dimensions']=list(im.size)
    t['assets']=assets; write_json(out/'timeline'/'timeline.json',t)
    write_json(out/'ASSET_REGISTRY.json',assets);write_json(out/'planning'/'asset_plan.json',assets)
    print(json.dumps(report,indent=2));return ready

def main():
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest='command',required=True);prep=sub.add_parser('prepare');prep.add_argument('input');prep.add_argument('--script',required=True);prep.add_argument('--output',required=True);prep.add_argument('--brain',default=str(BRAIN));v=sub.add_parser('validate');v.add_argument('output');s=sub.add_parser('status');s.add_argument('output');args=p.parse_args()
    if args.command=='prepare':build(args.input,args.script,args.output,Path(args.brain))
    elif args.command=='validate':validate(args.output)
    else:print((Path(args.output)/'qc'/'validation.json').read_text())
if __name__=='__main__':main()
