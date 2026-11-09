import pathlib,json,csv,collections
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');O=R/'production_v1';rows=[]
S={x['state_id']:x for x in csv.DictReader((R/'tables/states_machine.csv').open())}
for i in range(1,11):
 d=json.loads((R/f'agents/shard_{i}/OUT_shard_{i}.json').read_text())
 for s in d['states']:
  b=S[s['id']];rows.append(dict(state_id=s['id'],start_frame=b['start'],end_frame=b['end'],start_pts=(int(b['start'])+1)/24,end_exclusive_pts=(int(b['end'])+2)/24,family=s['family'],source_objects=s['objects'],source_background=s['background'],source_illustration=s['illustration'],source_typography=s['typography'],readable_source_text=s['readable_text'],unreadable_source_text=s['unreadable_text'],source_hierarchy=s['hierarchy'],source_camera_motion=s['camera_motion'],source_entry_exit=s['entry_exit'],story_function_inference=s['story_function'],source_evidence=s['evidence'],source_confidence=s['confidence'],continuity=s['continuity'],first_pass_original_proposal=s['recon'],first_pass_image_prompt=s['prompt'],generation_prompt_status='UNAPPROVED_DRAFT: originality/text/native-visual checks required; may retain source-like identities',animation_spec_status='PARTIAL: source entry/exit and candidate intervals; exact curves/layers/kinematics unknown',static_anchors_status='PER_STATE_VALIDATION_PENDING',audio_status='ASR_ONLY_NOT_HEARD',review_ref=f'agents/shard_{i}/OUT_shard_{i}.json',rep_image=b['rep_image']))
rows.sort(key=lambda x:int(x['state_id'][1:]));assert len(rows)==447
with (O/'per_state_production_spec_DRAFT_v1.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
counts=collections.Counter(r['family'].split()[0] for r in rows)
(O/'production_draft_stats_v1.json').write_text(json.dumps({'draft_states':447,'families':dict(counts),'duplicate_prompt_count':len(rows)-len(set(x['first_pass_image_prompt'] for x in rows)),'rendered_reconstruction_tests':0,'full_production_approval':False,'scope':'Existing first-pass proposals indexed for retrieval; gaps/merges/splits not yet applied. Not a validated production package.'},indent=2))
(O/'RECONSTRUCTION_BLUEPRINT_DRAFT_v1.md').write_text('''# Video006 original-production blueprint: DRAFT
Source: xtqbRt94TTw / SHA256030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66. This is a within-video transfer proposal, not validated channel DNA or exact recreation of original layers/software.

## Source-to-production index
per_state_production_spec_DRAFT_v1.csv contains447 immutable first-pass state IDs with source objects, layout estimates, text, hierarchy, entry/exit, continuity, image proposals and provenance. State proposals may duplicate or retain source identity; they are explicitly unapproved. Gap-review insertions and142 merge/3split rulings must be applied before this can become a usable final timeline.

## Proposed original asset system
Use visibly different rounded geometric characters, a new navy/coral/cream palette, clean sans-serif typesetting, and generic diagrams/documents carrying independently verified claims. These are original proposals, not measured source tokens. Generate image layers without text or branded logos; typeset meaningful new script text separately. Lock character silhouette, proportions, palette, prop scale and screen positions across adjacent states. Preserve the useful abstract grammar: stable scene anchors, sequential evidence reveal, annotations, figurative comparison and occasional reset composition.

## Measured reconstruction unit: G003 timing
The newly verified missing scene is sourceframes226–300 inclusive:75frames /3.125seconds. Relativeframe0–35 table+fourfigures with no bubble;36–52 first bubble;53–74 replacement bubble. Exact source pairs225/226,261/262,278/279,300/301 were actually displayed natively. Source speech-bubble words are evidence only; an original production must use different original discussion text and distinct characters/layout.
Proposed editable stack: background, table, four independent original character layers, bubble shape, editable type; everything static except an explicit bubble state replacement at relative36 and53. This unit does not prove unseen limb curves or easing; do not invent them. The next-source Fed-page cut is at301. Audio synchronization unavailable until actual hearing. This timing unit is ready for a bounded render test, but no render is claimed here.

## Required per-state completion
For each final state: explicit source frame references, original scene graph with normalized positions, specific image/asset brief, motion path and measured onset/settle or uncertainty, static anchors, typography copy, transitions, continuity locks and editor QA. For charts/screenshots, independently verify numbers/units and legibility. For running/meme insertions, inspect actual native sequences; do not derive motion from a still.

## Reconstruction checks still open
1. Resolve semantic timeline and merge/split rulings, then test one ORIGINAL75frame G003 analogue without giving the renderer the competitor frames.
2. Render native1920x1080 at24fps; verify75frames, bubbles absent before36, first at36–52, replacement53–74, static-anchor geometry unchanged.
3. Independently view actual renderedframes0,35,36,52,53,74 and inspect frame-to-frame changes, not just filenames or schema presence. Record failures and iterate.
4. Native/mobile text readability, character continuity, original-identity differentiation and factual label accuracy.
5. Qualified source and output listening before sound/synchronization or AV sign-off. ASR is not listening.

Schema retrieval alone is not a cold-start reconstruction pass. No rendered test, visual parity, production readiness orCT_SCAN_COMPLETE is awarded by this draft.
''')
print('draft index447 states; pending original/native/reconstruction validation')
