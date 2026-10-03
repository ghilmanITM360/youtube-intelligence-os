import csv,json
from pathlib import Path
P=Path(__file__).resolve().parent
selected=json.loads((P/'batch-001-selection.json').read_text())
notes=[
 dict(text="99% DOCTORS WON’T TELL! / SENIORS! / YOU MUST KNOW THIS ABOUT / AMLODIPINE / LOWERS BLOOD PRESSURE / REDUCES RISK OF STROKE / IMPROVES BLOOD CIRCULATION / SAFE & EFFECTIVE FOR SENIORS; badge: DR.TAVINGHI / PHARMACIST",
 scene="Dark-haired woman in green scrubs on right, slight smile and direct gaze, index finger pointing left; glowing anatomical heart; ECG line; four bottom benefit icons. Black, navy and gold background.",mechanism="Hidden information / authority",
 composition="Asymmetric text-left, person-right layout; large AMLODIPINE lower-left block competes with SENIORS and top headline. Pointing finger routes toward text; no separate arrow. Bust/waist crop, little negative space; icon row adds a third horizontal layer. Approximate thirds, not a strict grid.",
 typography="Large condensed uppercase yellow/white text with shadows; at 160x90 the drug name and SENIORS survive, bottom captions and badge do not. Dense multi-tier hierarchy.",
 colors="Yellow urgency, white supporting copy, blue medicine panel, green scrubs, red heart; strong text/background separation but competing bright regions.",
 psychology="Calm smiling portrait and pointing pose offer reassurance beside secrecy rhetoric. Professional identity and authenticity cannot be established from the image.",
 partnership="Title identifies amlodipine/blood pressure and withheld knowledge; image mostly repeats that promise and adds four benefit claims. Exact hidden fact remains unanswered. Content fulfillment not checked.",
 scan="INFERENCE visual heuristic: SENIORS or AMLODIPINE -> portrait/heart -> upper secrecy line; bottom icons last. Not eye-tracking.",
 art="Crisp portrait-plus-graphics composite; no definite anatomy defect visible. Very smooth lighting is not proof of AI generation. Badge names a different identity from the channel label; this warrants verification, not an impersonation conclusion.",
 strength="Drug name is large and concrete.",weakness="Multiple competing promises and unreadable bottom detail.",bottleneck="Viewer must decode drug, age target, secrecy and four benefits at once.",action="Remove four-icon footer and 99% claim; retain drug name plus one content-supported question. Verify presenter badge against documented identity.",scores=[9,10,8,5,5,6,5,3,2]),
 dict(text="UNSTABLE WALK / IF YOU ARE 70, 80 OR 90 / YEARS OLD / DO THIS SIMPLE MOVEMENT!; badge: Dr. Olivia Hart / PharmD; lower-right: SUSCRÍBETE",
 scene="Dark-haired woman in green scrubs on right, slight smile, direct gaze, points left; gold halo/gradient, no walking demonstration or hero object.",mechanism="Recognition / hidden solution",
 composition="Large text fills left two-thirds; cropped standing torso on right. Pointing finger leads toward age text. Four horizontal type tiers, no separate arrow; little empty space and no literal movement.",
 typography="White condition line, yellow ages, white YEARS OLD, yellow bottom instruction on navy. Main headline survives 160x90; badge and subscription mark do not. Large age line consumes space that could show the action.",
 colors="Gold background with dark edges; white/yellow outlined type and green scrubs. Strong silhouette separation, consistent warm background.",
 psychology="Relaxed reassuring face contrasts with instability topic; direct gaze and pointing instruct viewer where to look. Authenticity unverified.",
 partnership="Title offers a life-saving walking change after 70; thumbnail specifies unstable walking and ages 70/80/90, repeats a simple movement but withholds which. Content fulfillment not checked.",
 scan="INFERENCE visual heuristic: UNSTABLE WALK -> portrait or age line -> bottom movement instruction. Not measured.",
 art="Clean cutout and coherent pointing hand at this resolution; no definitive AI artifact. Badge identity differs from channel label and from the amlodipine portrait badge; provenance unresolved.",
 strength="Recognizable audience problem is named immediately.",weakness="The promised movement is not pictured.",bottleneck="Text supplies all semantic work while portrait adds little action information.",action="Test a verified demonstrator showing the actual first step, replacing the long age block; retain one accurate age qualifier and a short condition line.",scores=[11,12,11,7,7,7,6,4,2]),
 dict(text="what if? (brand badge)",scene="Black line-art sailboat and stick figure falling through white space, falling fish and larger marine animal below; red circular lower-left logo with black suspended animal silhouette.",mechanism="Contradiction / consequence",
 composition="Central tilted boat, diagonals in mast/sail, vertical falling marks; scattered animals create downward sequence. Broad negative space; objects uncropped apart from lower-left brand badge. No arrows; motion marks communicate gravity.",
 typography="Only brand text; no explanatory headline. At 160x90 the boat remains visible but small fish and gesture details weaken.",
 colors="Mostly black on white; red badge is the only saturated region and can compete with the narrative.",
 psychology="Stick figure limbs suggest loss of control; facial emotion not legible. No photographic identity or authenticity claim.",
 partnership="Title supplies disappearing water, image supplies the immediate absurd consequence: boat and sea life falling. Unknown is the larger planetary outcome. Content fulfillment not checked.",
 scan="INFERENCE visual heuristic: boat -> falling figure/animals -> red brand badge, with badge-first also plausible. Not eye-tracking.",
 art="Intentional schematic illustration; physical realism is not its visual contract. Clean separation, no obvious compositing defect; AI origin cannot be inferred.",
 strength="Visual consequence adds information beyond the question.",weakness="The absent water is hard to infer without the title.",bottleneck="Small supporting animals require closer looking.",action="Test larger falling marine subject and slightly heavier boat line weight while keeping the same title and brand footprint.",scores=[13,13,14,8,7,8,7,9,4]),
 dict(text="what if?; RIP",scene="Dark island scene: engine/generator left, glowing hut doorway and window/bulb centrally, palm tree right, gravestone, water and sparse stars; no live person.",mechanism="Contradiction / consequence / persistence",
 composition="Bright doorway is center focal point; generator left and grave right encode cause and mortality. Palm leans diagonally toward hut. Wide dark sky provides negative space. Lower-left badge competes; no arrows.",
 typography="Brand badge dominates text; small RIP label is vulnerable at mobile size. Story primarily pictorial.",
 colors="Charcoal and black with white glow; local luminance contrast supplies narrative isolation. Red brand circle is secondary competing accent.",
 psychology="Empty dwelling and grave imply absence; no face or gaze. Loneliness is an interpretation, not an observed viewer response.",
 partnership="Title supplies all-human death and asks duration; image shows a light persisting beside a grave and a possible power source. It illustrates persistence without answering when. Content fulfillment not checked.",
 scan="INFERENCE visual heuristic: luminous doorway -> generator -> grave/palm; red badge may interrupt. Not measured.",
 art="Coherent deliberately simplified night illustration. Dark generator and gravestone lose detail at 160x90; no definitive AI-like defect.",
 strength="One luminous object embodies the title’s unanswered question.",weakness="Small dark explanatory details disappear on mobile.",bottleneck="The grave and power source may be missed.",action="Test restrained rim lighting on the generator and a larger grave silhouette; preserve the doorway as brightest region.",scores=[14,14,15,8,6,9,8,9,4]),
 dict(text="HOW A / STROKE / ACTUALLY / STARTS!",scene="Illustrated gray-haired older person on right, furrowed brow and downturned mouth, hand across chest, radiating lines; red curved arrow points toward face; black background.",mechanism="Consequence / recognition",
 composition="Text left, chest-up person right, red arrow connects text to face. Torso and hair approach edges; chest gesture is a secondary focal region. Little negative space, strong two-column balance.",
 typography="Yellow HOW A/STROKE, white ACTUALLY, white STARTS on red block. Readable main copy at 160x90; fine facial lines less clear.",
 colors="Black field, yellow headline, red warning accents, white/blue/red portrait strokes. Good separation, several warning focal points.",
 psychology="Visible furrowed brow, downturned mouth and chest-clutch pose communicate distress. Specific condition cannot be diagnosed from an illustration.",
 partnership="Title specifies day-before warnings; image says how a stroke starts, losing the anticipatory time frame. Chest gesture is nonspecific to the promised condition; no clinical claim is established. Content fulfillment not checked.",
 scan="INFERENCE visual heuristic: STROKE -> face via arrow -> STARTS -> chest gesture. Not measured.",
 art="Hatched illustration is internally stylized; hand visible without an obvious extra digit. Arrow highlights face while radiating lines highlight chest, splitting explanatory focus.",
 strength="Condition label and distress are immediately visible.",weakness="Time-frame distinction is absent and depicted symptom is ambiguous.",bottleneck="A generic distress image does not explain which early warning matters.",action="Use one medically reviewed sign actually addressed by the video, paired with accurate timing; remove arrow if it does not locate that sign. Do not invent a diagnostic sign.",scores=[10,10,7,8,8,7,5,4,2]),
 dict(text="THE FRUIT / REPAIRS EYES / OVERNIGHT / CATARACTS",scene="Large illustrated gray-haired older woman right, looking left/up, faint smile, visibly pale/cloudy-looking pupils/irises; dark top and black background. No fruit shown.",mechanism="Hidden information / transformation",
 composition="Large face fills right half, dense four-line copy left; gaze points toward words. Hair and torso cropped, clean silhouette, no arrow and minimal negative space.",
 typography="Yellow top two lines, white OVERNIGHT, white CATARACTS on red panel. All main words survive 160x90; strong but competing emphasis across four blocks.",
 colors="Yellow/white/red on black; warm peach skin and silver hair separate face. Red isolates condition name.",
 psychology="Mild hopeful expression and leftward gaze complement a transformation promise. Illustrated cloudy eyes are a visual cue, not evidence of a diagnosis or cure.",
 partnership="Title promises best fruit for healthy eyesight; thumbnail escalates to repair overnight and cataracts, while concealing fruit identity. Stronger time-specific treatment promise is not established by the title. Content fulfillment not checked.",
 scan="INFERENCE visual heuristic: THE FRUIT -> face/eyes -> OVERNIGHT -> CATARACTS. Not measured.",
 art="Polished illustrative face, consistent crop, no definite generation artifact. Smooth rendering does not establish AI use. Eye detail is lost at mobile size.",
 strength="One hidden item linked to an immediately named audience concern.",weakness="Unsupported escalation from healthy eyesight to overnight repair.",bottleneck="The compelling promise carries an unverified credibility burden.",action="Remove OVERNIGHT and REPAIRS unless independently substantiated; align with the actual nutrition discussion and show the real fruit when that better represents the content.",scores=[11,14,5,8,8,8,7,1,3])]
weights=[15,15,15,10,10,10,10,10,5]
score_names=['story','psychological_hook','title_partnership','hierarchy','mobile_readability','composition','emotion_subject_alignment','credibility','distinctiveness']
audit=[]
for r,n in zip(selected,notes):
 scores=n.pop('scores');assert all(0<=x<=w for x,w in zip(scores,weights))
 audit.append({**r,**n,**{k+'_score':v for k,v in zip(score_names,scores)},'score_100':sum(scores),'inspection_status':'INSPECTED_NATIVE_AND_160x90','evidence_labels':'text,scene=DATA; diagnostic fields and scores=INFERENCE; proposed changes=HYPOTHESIS','confidence':'High for visible major elements; moderate for small badge text; low for performance attribution','content_promise_verified':'NOT_CHECKED','batch_id':'B001'})
(P/'individual-audit-batch-001.json').write_text(json.dumps(audit,indent=2))
with (P/'individual-audit-batch-001.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=audit[0]);w.writeheader();w.writerows(audit)
ledger=json.loads((P/'thumbnail-ledger.json').read_text());byid={r['Thumbnail_ID']:r for r in audit}
for r in ledger:
 if r['Thumbnail_ID'] in byid:r.update(inspection_status=byid[r['Thumbnail_ID']]['inspection_status'],score_100=byid[r['Thumbnail_ID']]['score_100'])
(P/'thumbnail-ledger.json').write_text(json.dumps(ledger,indent=2))
with (P/'thumbnail-ledger.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=ledger[0]);w.writeheader();w.writerows(ledger)
assets=list(csv.DictReader((P/'asset-inventory.csv').open()))
for r in assets:
 if 'THB-'+r['sha256'] in byid:r['inspection_status']='INSPECTED_NATIVE_AND_160x90'
with (P/'asset-inventory.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=assets[0]);w.writeheader();w.writerows(assets)
summary=json.loads((P/'inventory-summary.json').read_text());summary['visually_inspected_images']=6
(P/'inventory-summary.json').write_text(json.dumps(summary,indent=2))
print([(r['video_id'],r['score_100']) for r in audit])
