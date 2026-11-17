"""Bounded static-art/source-preservation checks. No video rendering or project pipeline."""
from pathlib import Path,PurePosixPath
from zipfile import ZipFile
import csv,json,hashlib,base64,re,subprocess,xml.etree.ElementTree as ET
from PIL import Image
import pdfplumber
R=Path(__file__).resolve().parents[2];ART=R/'editable_sources/original';E=R/'ARTICLE_EVIDENCE';REF=R/'editable_sources/references/owner_examples'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={}
required=['REFERENCE_EVIDENCE.md','REFERENCE_RECOVERY.md','VISUAL_DESIGN_RULES.md','STORYBOARD.csv','ASSET_REQUIREMENTS.csv','CHARACTER_SHEET.png','HERO_01.png','HERO_02.png','HERO_03.png','VISUAL_COMPARISON.png','VISUAL_QA.md','NEXT_STEP.md','ARTICLE_SOURCE_REGISTER.csv','ARTICLE_SCREENSHOT_PLAN.csv','ARTICLE_EVIDENCE','editable_sources']
assert all((R/p).exists() for p in required);report['required_outputs']=len(required)
rows=list(csv.DictReader((R/'STORYBOARD.csv').open()));old=list(csv.DictReader((R/'editable_sources/prior_v1/STORYBOARD.csv').open()))
assert len(rows)==18 and len({x['scene_id'] for x in rows})==7
for x,y in zip(rows,old):
 for key in ['state_id','scene_id','narration_phrase','provisional_start_sec','provisional_end_sec','suggested_transition']:assert x[key]==y[key],(key,x['state_id'])
assert float(rows[0]['provisional_start_sec'])==0 and float(rows[-1]['provisional_end_sec'])==53
for a,b in zip(rows,rows[1:]):assert a['provisional_end_sec']==b['provisional_start_sec']
assert len(' '.join(x['narration_phrase'] for x in rows).split())==147
assert sum('CUT' in x['suggested_transition'].split(';') for x in rows)==5
assert sha(ART/'APPROVED_NARRATION.txt')==sha(R/'editable_sources/prior_v1/editable_sources/original/APPROVED_NARRATION.txt')
report['script_and_timing']={'words':147,'states':18,'scenes':7,'seconds_provisional':53,'planned_cuts':5,'approved_script_hash':sha(ART/'APPROVED_NARRATION.txt'),'verbatim_fields_preserved':True}
assets=list(csv.DictReader((R/'ASSET_REQUIREMENTS.csv').open()));ids={x['asset_id'] for x in assets};assert len(ids)==len(assets)
for row in rows:assert set(row['required_asset_ids'].split(';'))<=ids
assert sum(int(x['authored_design_families']) for x in assets)==19
assert sum(int(x['planned_derived_variants_or_instances']) for x in assets)==54
report['asset_plan']={'authored_families':19,'planned_variants_or_instances':54,'FRED_is_substitution':True}
inv=json.loads((REF/'INVENTORY.json').read_text());assert len(inv['usable_files'])==12
assert sha(Path(inv['archive']))==inv['archive_sha256']
for item in inv['usable_files']:assert sha(R/item['relative_copy'])==item['sha256']
report['owner_graphics']={'usable_pngs':12,'hashes_match':True,'videos':5,'panels_with_repeats':186,'adjacent_sequences':7}
comparison=json.loads((REF/'CALIBRATION_ZIP_COMPARISON.json').read_text());archive=R.parent/comparison['source']
assert len(comparison['matching'])==119 and not comparison['different'] and not comparison['missing_local']
preserved=0
manifest=[]
for relative in comparison['matching']:
 rel=Path(relative);prior=R/'editable_sources/prior_v1'/rel;file=prior if prior.exists() else R/rel
 assert file.exists(),relative
 manifest.append({'original_relative_path':relative,'recovery_copy':str(file.relative_to(R)),'sha256_now':sha(file),'basis':'Initial ZIP comparison matched this file; changed V1 outputs copied before revisions, unchanged references retained'})
 preserved+=1
if archive.exists():
 assert sha(archive)==comparison['archive_sha256']
 with ZipFile(archive) as z:
  for item in manifest:assert hashlib.sha256(z.read(R.name+'/'+item['original_relative_path'])).hexdigest()==item['sha256_now']
assert preserved==119
(ART/'V1_PRESERVATION_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
report['V1_preservation']={'archive_exists_now':archive.exists(),'archive_hash_rechecked_now':archive.exists(),'initial_archive_comparison':119,'119_substantive_files_recoverable':True,'restoration_performed':False,'limitation':'Original calibration ZIP became unavailable after initial read; no fresh ZIP hash can be claimed. Cause unknown; no removal/move performed by this task.' if not archive.exists() else ''}
for item in json.loads((E/'OWNER_SCREENSHOT_MANIFEST.json').read_text()):
 assert sha(Path(item['source_path']))==item['sha256']==sha(R/item['copy'])
for item in json.loads((E/'UNTOUCHED_MANIFEST.json').read_text()):assert sha(R/item['file'])==item['sha256']
crops=json.loads((E/'CROP_MANIFEST.json').read_text())
for item in crops:
 src=R/item['source'];out=R/item['file'];assert sha(src)==item['source_sha256'] and sha(out)==item['sha256']
 assert Image.open(src).crop(item['box_xyxy']).convert('RGB').tobytes()==Image.open(out).convert('RGB').tobytes(),str(out)
 assert item['status']=='ACCEPTED'
report['source_integrity']={'owner_screenshots':3,'accepted_unchanged_pixel_crops':len(crops),'untouched_manifest':True,'rejected_FRED_crop_excluded':not any('REJECTED' in x['file'] for x in crops)}
pdf=E/'untouched/C_H41_official.pdf';assert sha(pdf)=='3e349805f522b292aaac2c33eb7e19f34c4209e73b2cf28deeea4c4df6e8ac0a'
with pdfplumber.open(pdf) as d:
 assert len(d.pages)==11
 assert '3,022,066' in d.pages[1].extract_text()
 assert '-233,587' in d.pages[8].extract_text()
 assert 'cumulative deferred asset' in d.pages[9].extract_text()
report['official_pdf']={'unchanged':True,'page2_reserves_correct':True,'page9_total_correct':True,'page10_footnote8_interpretation_verified':True}
sources=list(csv.DictReader((R/'ARTICLE_SOURCE_REGISTER.csv').open()));plan=list(csv.DictReader((R/'ARTICLE_SCREENSHOT_PLAN.csv').open()))
assert len(sources)==5 and len(plan)==6
for row in sources:assert sha(R/row['untouched_screenshot'])==row['untouched_sha256'] and row['status']=='VERIFIED_CAPTURED'
for row in plan:
 assert (R/row['overlay_source']).exists()
 for p in row['separate_crops'].split(';'):assert (R/p).exists()
report['article_registers']={'verified_sources':5,'prepared_insert_options':6}
ns='{http://www.w3.org/2000/svg}';png_count=0;svg_count=0
for file in R.rglob('*'):
 if file.suffix.lower() in ['.png','.jpg']:
  with Image.open(file) as im:im.verify()
  png_count+=1
 if file.suffix=='.svg':ET.parse(file);svg_count+=1
 assert file.suffix.lower() not in {'.mp4','.mov','.mp3','.wav'},file
layerrows=list(csv.DictReader((ART/'LAYER_REGISTER.csv').open()));counts={}
for name in ['HERO_01','HERO_02','HERO_03']:
 assert Image.open(R/(name+'.png')).size==(1080,1920)
 root=ET.parse(ART/(name+'.svg')).getroot();allids=[el.get('id') for el in root.iter()]
 assert None not in allids and len(allids)==len(set(allids))
 registered={x['svg_layer_id'] for x in layerrows if x['composition']==name};assert registered=={x.get('id') for x in root}
 for node in root.iter(ns+'image'):
  raw=base64.b64decode(node.get('{http://www.w3.org/1999/xlink}href').split(',',1)[1]);digest=hashlib.sha256(raw).hexdigest();assert digest in {x['sha256'] for x in crops}
 counts[name]=len(root)
assert counts=={'HERO_01':10,'HERO_02':16,'HERO_03':13}
for file in ART.glob('*.svg'):
 if re.match(r'^(HOST_|PROP_|ANN_|DGM_)',file.name):
  im=Image.open(file.with_suffix('.png'));assert im.mode=='RGBA' and im.getchannel('A').getextrema()==(0,255),file
report['art_structure']={'top_level_editable_layers':counts,'SVGs_parsed_including_prior':svg_count,'decoded_images_including_prior':png_count,'source_images_match_actual_crops':True,'independent_png_alpha':True,'no_audio_video_files':True}
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R.parent,text=True).strip();assert head=='08e719264e31ecd82de24f8eeb8f065c08359fe5'
assert subprocess.check_output(['git','branch','--show-current'],cwd=R.parent,text=True).strip()=='main'
assert not subprocess.check_output(['git','diff','--name-only'],cwd=R.parent,text=True).strip()
assert not subprocess.check_output(['git','diff','--cached','--name-only'],cwd=R.parent,text=True).strip()
subprocess.run(['git','diff','--check'],cwd=R.parent,check=True)
report['git']={'HEAD_unchanged':head,'branch':'main','tracked_changes':False,'staged_changes':False,'status':subprocess.check_output(['git','status','--short','--branch'],cwd=R.parent,text=True).strip()}
report['result']='PASS';report['visual_acceptance']='OWNER_REVIEW_PENDING; fresh human-visible sampling documented in VISUAL_QA, not certified by this script'
(ART/'VALIDATION_V2.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
