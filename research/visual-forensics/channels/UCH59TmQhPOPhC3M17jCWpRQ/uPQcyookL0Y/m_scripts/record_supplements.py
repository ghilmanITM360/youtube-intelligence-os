from pathlib import Path
import csv,json
p=Path('.')
def write(name,rows):
 with (p/'tables'/name).open('w') as h:
  w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
rows=[]
def add(id,state,f,obs,limit):rows.append(dict(correction_id=id,state=state,frames=f,observation=obs,scope_limit=limit,author='primary Codex session 01a19dcb; not independent review',status='OBSERVED unless explicitly INFERRED'))
add('M01','W001','698-727 consecutive 640x360 sheet tiles; native 704,705,719','Label remains no shoes through f704; bold no idea replaces it at f705 (23.523500 s). Same smiling bone-haired character persists; frame content moves/scales. Right panel black divider first visible at f719 (23.990633 s); panel grows leftward through f727 while ancestor shrinks and caption is occluded/disappears. Refines J bracket f701-705 / f720-726.','No source project/layer/easing claim; native full frames 704,705,719 only; panel settling after f727 not newly reviewed.')
add('M02','W010','1531:30:2071 (19 unique samples); native 1621,2041','Timeline moves across generations; f1621 faces read YOU PAUSED? NERD.; old caveman upright f1651 and horizontal/fallen f1681; RIP stone at f1711 onward; ancestor fades at f1891; face-text returns at f1921/f1951; modern figures return; Daddy? appears at f2041 (68.101367 s); f2071 empty timeline endpoint.','Approximately 1.001 s sampling across entire 18.051 s state, not continuous motion review; action onsets/intermediate poses uninspected. Gag presence does not prove one-frame duration.')
add('M03','W001-W006 / ASR4','native batch01 f845,f887,f949; previous reviewer evidence retained','Segment 4 overarching label changed to MIXED_PARTIAL. CONTRADICTORY_JOKE restricted to exaggerated bloodshot-eye coffee face witnessed at f845 (28.194833 s), referring provisionally to mild caffeine dependency. f887 is return to calm split-panel comparison; f949 literal transition caption but here is the thing. Timeline portion retains prior literal assessment, not newly re-viewed.','No exact word timing or full-segment joke assertion. Raw reviewer_12 row unchanged; segment4 subintervals not speech-aligned.')
add('M04','W010 / ASR8','native checkpoint_M/W010_interval/f2041.png','Daddy? is visibly written at f2041 within ASR8 [64.48,72.24]. Supersedes claim no visual counterpart in viewed frames after expanded sampling.','ASR8 overall remains partial/low-confidence: W011 UNRELATED_HOLD retained separately; visual text does not certify audible word.')
write('m_supplement_corrections.csv',rows)
shared=['CHAR_TEACHER','SET_CLASSROOM_BG','PROP_CHALKBOARD','PROP_EVOLUTION_POSTER','PROP_SIGN_BARELY_EVOLVED_SHOOL','PROP_STONE_LECTERN','PROP_DESKS_STOOLS','PROP_POINTER_STICK']
cr=[]
for asset in shared:
 for rev in ['reviewer_13','reviewer_14']:
  cr.append(dict(reviewer=rev,original_id=asset,qualified_id=rev+':'+asset,resolved_identity='reviewer_13:'+asset,decision='SAME_VISIBLE_ASSET_FAMILY',evidence='native_rep/batch02/W011_f2114.png; native_rep/batch02/W017_f3015.png',limit='Observed matching design; source asset file identity unknown; cropped set pieces only partially visible in W017.'))
for rev,ids in [('reviewer_13',['TEXT_KINETIC_CAPTION','CHART_SURVIVAL_BAR','TEXT_TITLE_CARD']),('reviewer_14',['ASSET_GLOBE','ASSET_ICE_SHEET','ASSET_SCALE_BAR','ASSET_THERMOMETER','SCENE_ICE_LANDSCAPE','CHAR_CAVE_ICE','SCENE_SNOW_FLAT','CHAR_CAVE_FROZEN'])]:
 for asset in ids:cr.append(dict(reviewer=rev,original_id=asset,qualified_id=rev+':'+asset,resolved_identity=rev+':'+asset,decision='PRESERVE_ORIGINAL_NO_MERGE',evidence='agents/'+rev+'/art_audit_batch02'+('a' if rev.endswith('13') else 'b')+'.csv',limit='Original provenance preserved; no new identity invented; distinct identities not re-certified by this naming pass.'))
cr.append(dict(reviewer='reviewer_14',original_id='TEXT_KINETIC_CAPTION-style',qualified_id='reviewer_14:TEXT_KINETIC_CAPTION-style',resolved_identity='',decision='STYLE_REFERENCE_ONLY_NOT_IDENTITY_ALIAS',evidence='agents/reviewer_14/art_audit_batch02b.csv W016; reviewer_13 W012',limit='Generic style reference to text treatment does not merge different strings or graphics.'))
write('m_asset_alias_crosswalk.csv',cr)
print('corrections',len(rows),'crosswalk',len(cr))
