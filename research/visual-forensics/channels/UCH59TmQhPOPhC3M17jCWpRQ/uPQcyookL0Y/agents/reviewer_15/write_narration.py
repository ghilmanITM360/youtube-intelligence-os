import csv,json
from pathlib import Path
p=Path('.');o=p/'agents/reviewer_15';a=json.loads((p/'asr/asr_small_en.json').read_text())['segments'];F=list(csv.DictReader((p/'tables/k_rep_frames_batch03.csv').open()));S=list(csv.DictReader((p/'tables/states_v5_draft.csv').open()))[20:30]
data={
16:('LITERAL_ILLUSTRATION_PARTIAL','Only overlap120.4203–123.16: human/mammoth comparison supports mammoth size idea; no school bus or hunting seen. Hypothermia/head before batch unassessed.','medium'),
17:('MIXED_PARTIAL','Mammoth hold then lion biting dangling man and label Panthera spelaea; illustrates predator danger but running away not witnessed.','medium'),
18:('LITERAL_ILLUSTRATION_PARTIAL','Lion hold, bone hut, then cave interior fit cat/housing concepts. Only one figure in viewed cave sample within this segment; forty not demonstrated.','medium'),
19:('MIXED_LITERAL_AND_JOKE','Five cave figures at f4070 fit relatives without proving forty. Wardrobe sequence suit removed by giant hand, stitched tunic placed; literal clothing plus inferred anachronistic joke. Needles visible as props, no sewing seen.','medium'),
20:('LITERAL_ILLUSTRATION_PARTIAL','Sharp stick appears in man hand; mammoth reveal f4454 is148.614s, outside this ASR segment, so not used as in-segment witness. Six tons not directly shown in its viewed frames.','medium'),
21:('MIXED_PARTIAL','Mammoth/man juxtaposition then wounded man in bed. No active attack, starvation or infection progression established; red cut visibly supports cut phrase.','medium'),
22:('UNCERTAIN','Bed at beginning; W028 three near-blank frames and cropped right-edge fragment, then herbal-bed frame late. No antibiotics/vaccine/emergency-room graphic readable. Cannot claim intentional blank hold or infer omitted symbols.','low'),
23:('LITERAL_ILLUSTRATION_PARTIAL','Green sprig held at mouth in bed supports plants/remedy concept; chewing cycle and efficacy unverified. Classroom at tail is context change.','medium'),
24:('LITERAL_ILLUSTRATION_PARTIAL','Board image shows fur-clad group around fire, then animal rock painting by f5118. Supports fire/early-art topic; tool invention not demonstrated.','medium'),
25:('LITERAL_ILLUSTRATION_PARTIAL','Only head172.06–173.9404 judged: f5209 displays second rock-art image. Lascaux identification not independently verified. Number four/agriculture/10000-years tail outside batch entirely unassessed.','low')}
fields=list(csv.DictReader((p/'agents/reviewer_14/narration_relation_batch02b.csv').open()).fieldnames);rows=[]
for i,(rel,why,conf) in data.items():
 s=a[i]; fs=[r for r in F if s['start']<=int(r['frame'])*1001/30000<=s['end']]
 states=[r['state_v4'] for r in S if int(r['end'])*1001/30000>=s['start'] and int(r['start'])*1001/30000<=s['end']]
 rows.append(dict(zip(fields,[i,s['start'],s['end'],';'.join(states),';'.join(r['native_png'] for r in fs),rel,why+' ASR_ONLY_NOT_AUDIO_VERIFIED; sparse frames, intermediate motion uninspected.',conf+'; segment timestamps provisional, not frame-accurate speech', 'seg17 ASR Panthera spalia versus visible Panthera spelaea; no silent transcript correction' if i==17 else 'Unheard ASR; wording not certified'])))
with (o/'narration_relation_batch03.csv').open('w',newline='') as h:
 w=csv.DictWriter(h,fieldnames=fields);w.writeheader();w.writerows(rows)
assert len(list(csv.DictReader((o/'art_audit_batch03.csv').open())))==10
assert len(list(csv.DictReader((o/'evidence_reads.csv').open())))==34
print('VALIDATED 10 art rows, 10 narration rows (16-25), 34 actual image witnesses')
