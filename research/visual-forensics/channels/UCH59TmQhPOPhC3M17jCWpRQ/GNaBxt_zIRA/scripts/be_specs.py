# Draft production spec from consolidated reviewer evidence. cwd = video workspace. Args: video_id
import csv,json,re,sys,collections
vid=sys.argv[1]
man=json.load(open('source_manifest.json'))
ev=list(csv.DictReader(open('tables/consolidated_motion_events.csv')))
pcs=list(csv.DictReader(open('tables/primary_corrections.csv'))) if __import__('os').path.exists('tables/primary_corrections.csv') else []
MOD={'M_ELEMENT_ENTER_EXIT':['ELEMENT_ENTER','ELEMENT_EXIT'],'M_CAMERA_SCALE_PAN':['CAMERA_SCALE','CAMERA_PAN'],'M_FADES':['FADE'],
     'M_CHARACTER_MOTION_POSE':['CHARACTER_MOTION'],'M_TEXT_REVEAL_SWAP':['TEXT_REVEAL','CUT_WITHIN_STRIP'],'M_HOLDS':['NO_VISIBLE_CHANGE'],'M_OTHER':['OTHER']}
KW={'overshoot_or_bounce':r'overshoot|bounce|settle|springs?','drop_from_top':r'from the top|drops? in|falls? in','slide_from_side':r'slides? (in|off|left|right)|from (the )?(left|right)','typing':r'typ(e|ing)|letter by letter|partial','word_swap':r'replaced|swap'}
def dur(e):
    try:return int(e['last_frame'])-int(e['first_frame'])+1
    except:return None
mods=[]
for mid,types in MOD.items():
    xs=[e for e in ev if e['event_type'] in types]
    if not xs:continue
    ds=sorted(d for d in map(dur,xs) if d)
    kw={k:sum(1 for e in xs if re.search(p,e['description'],re.I)) for k,p in KW.items()}
    exs=sorted(xs,key=lambda e:-(bool(re.search('|'.join(KW.values()),e['description'],re.I))))[:6]
    mods.append({'id':mid,'label':'OBSERVED by bounded sonnet reviewers (sampled 8-frame strips at 480x270); not primary-verified unless listed in primary_corrections',
      'event_types':types,'n_events':len(xs),'n_states':len({e['state'] for e in xs}),
      'observed_span_frames':{'min':ds[0] if ds else None,'median':ds[len(ds)//2] if ds else None,'max':ds[-1] if ds else None,'note':'spans are bounded by 8-frame strip windows; longer moves are truncated'},
      'description_keyword_counts':kw,
      'evidence':[f"{e['state']} f{e['first_frame']}-{e['last_frame']} [{e['batch']}]: {e['description'][:160]}" for e in exs],
      'original_production_choice':'PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.'})
spec={'version':'v1','source_video':vid,'source_sha256':man.get('sha256'),
 'status':'DRAFT_SPEC from validated reviewer batches; no reconstruction test run for this video',
 'audio':'ASR_UNCERTIFIED (faster-whisper small.en); listening BLOCKED_CAPABILITY; no SFX/music/sync rules specified',
 'implementation_limit':'Compressed output reveals output geometry and frame timing only; source software, fonts, layer stack, easing curves and asset origin are UNAVAILABLE. Frame numbers at 30000/1001 fps, +-1 frame.',
 'canvas':{'label':'MEASURED','resolution':f"{man.get('width','1920')}x{man.get('height','1080')}",'fps':'30000/1001 CFR'},
 'modules':mods,
 'primary_corrections':[{k:p[k] for k in ('id','state','status')} for p in pcs],
 'per_state_prompts':'tables/consolidated_state_prompts.csv',
 'motion_type_totals':dict(collections.Counter(e['event_type'] for e in ev))}
import os;os.makedirs('production_specs',exist_ok=True)
json.dump(spec,open('production_specs/specifications_v1.json','w'),indent=1)
print(json.dumps({m['id']:(m['n_events'],m['observed_span_frames']['median'],m['description_keyword_counts']) for m in mods}))
