from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1]
sources={
 'CDC_ACTIVITY':('Older Adult Activity: An Overview','https://www.cdc.gov/physical-activity-basics/guidelines/older-adults.html','Adults 65+: activity amount is individualized to ability; weekly aerobic, strength and balance guidance. Does not establish a universal three-run limit for everyone over 60.'),
 'AHA_REHAB':('AHA: exercise after heart attack','https://www.heart.org/en/news/2019/04/18/scared-to-exercise-after-a-heart-attack-its-probably-scarier-if-you-dont','Selected heart-disease patients may undertake HIIT in cardiac rehabilitation; not universal clearance or universal prohibition.'),
 'AHA_PLAN':('Develop a Physical Activity Plan for You','https://www.heart.org/en/health-topics/cardiac-rehab/getting-physically-active/develop-a-physical-activity-plan-for-you','Work with healthcare team to choose intensity after cardiac events.'),
 'CDC_SWIM':('Swimming and Your Health','https://www.cdc.gov/healthy-swimming/about/index.html','Water exercise can benefit health and allow exercise with less joint pain. This does not mean joints are unused.'),
 'YOUTUBE':('Medical misinformation policy','https://support.google.com/youtube/answer/13813322?hl=en','Policy concerns harmful medical misinformation contradicting local health-authority guidance. This is not a YouTube clearance decision.')}
(R/'MEDICAL_SOURCES.json').write_text(json.dumps([{'id':k,'title':v[0],'url':v[1],'checked':'2026-10-15','limited_summary':v[2]} for k,v in sources.items()],indent=2))
claims={
'01_HIIT_AFTER_60':[
 ('H1',0,3.24,'Seven out of ten rating','OPINION_NOT_EVIDENCE','No validated scoring rubric supplied.','', 'Show speaker opinion; no efficacy scale.'),
 ('H2',3.24,7.72,'Good for heart and cardiovascular conditioning','BROADLY_SUPPORTED_CONDITIONAL','Suitability and intensity depend on individual health.','AHA_PLAN','Symbolic heart, not guaranteed improvement.'),
 ('H3',7.72,13.36,'Concern with underlying cardiovascular disease','CONTEXT_REQUIRED','Risk differs by diagnosis, fitness and supervision.','AHA_PLAN','Concerned character, no catastrophe.'),
 ('H4',13.36,16.20,'Must be supervised by expert cardiologist','CLINICIAN_REVIEW','Appropriate medically supervised programmes may involve a clinical team; absolute wording is too broad.','AHA_REHAB','Proposed clarification: assessment and supervised plan.'),
 ('H5',16.20,21.26,'Higher mortality or mobility [ASR]','ASR_AND_CLINICIAN_REVIEW','Could be morbidity; no comparative risk estimate or population supplied.','AHA_REHAB','No quantitative risk chart.'),
 ('H6',21.26,24.34,'Avoided in patients with cardiovascular diseases [base]; awarded [small.en]','ASR_AND_CLINICIAN_REVIEW','Medically consequential model disagreement. Selected cardiac rehab patients may undertake HIIT. Blanket avoidance cannot be certified.','AHA_REHAB','Proposed overlay: Not one rule for everyone. Keep audio; do not publish before review.'),
 ('H7',24.34,28.90,'Improves endurance/stamina in normal patients','CONTEXT_REQUIRED','Normal patients is undefined; no exercise prescription supplied.','AHA_PLAN','Conceptual endurance only.')],
'02_RUNNING_AFTER_60':[
 ('R1',0,2.70,'Seven out of ten rating','OPINION_NOT_EVIDENCE','Not a validated medical score.','','Attribute speaker.'),
 ('R2',2.70,4.64,'Running is good exercise','BROADLY_SUPPORTED_CONDITIONAL','CDC lists running as vigorous aerobic activity; suitability varies.','CDC_ACTIVITY','No guaranteed benefit.'),
 ('R3',4.64,11.36,'Problems for knees, ankles, musculoskeletal system','CLINICIAN_REVIEW','Audio implies a broad consequence; no population, injury history or risk estimate supplied. Do not infer inevitable damage.','CDC_ACTIVITY','An intact joint illustration, no cracking cartilage.'),
 ('R4',11.36,14.42,'Exercise in moderation','CONTEXT_REQUIRED','Moderation is undefined; not individualized dosing.','CDC_ACTIVITY','Stopwatch is symbolic; no target time.'),
 ('R5',14.42,19.66,'No more than three times per week; moderate distance','CLINICIAN_REVIEW','No evidence supplied for a universal frequency limit. General older-adult guidance does not impose this cap.','CDC_ACTIVITY','Calendar is explicitly speaker advice, not universal prescription.'),
 ('R6',19.66,24.04,'Normal heart: improves cardiac function','CONTEXT_REQUIRED','Normal heart not defined; broad exercise benefit is not a guarantee.','AHA_PLAN','Symbolic heart, no before/after scan.'),
 ('R7',24.04,28.44,'VO2 / maximum oxygen extraction of blood [ASR]','ASR_AND_CLINICIAN_REVIEW','Terminology may conflate oxygen uptake with extraction; no correction silently added to speech.','','Proposed visual label VO₂; no values or fabricated physiology.'),
 ('R8',28.44,31.927438,'Endurance and stamina benefit','BROADLY_SUPPORTED_CONDITIONAL','Individual response varies.','CDC_ACTIVITY','Runner continuity; no numerical improvement.')],
'03_SWIMMING_AFTER_60':[
 ('S1',0,2.88,'9.5 out of ten rating','OPINION_NOT_EVIDENCE','No comparison method or clinical scoring system supplied.','','Attribute speaker opinion.'),
 ('S2',2.88,5.92,'One of best exercises for heart','CONTEXT_REQUIRED','Benefits supported; best ranking not established.','CDC_SWIM','No winning podium or disease protection shield.'),
 ('S3',5.92,10.16,'Best for cardiovascular fitness and endurance','CONTEXT_REQUIRED','Benefit plausible; universal superiority not verified.','CDC_SWIM','Sequential heart and stopwatch, no rankings.'),
 ('S4',10.16,11.88,'Uses whole body','ILLUSTRATIVE_GENERALIZATION','Different strokes recruit different muscles; no quantified full-body activation claim.','','Show arms and legs moving in a conceptual pose.'),
 ('S5',11.88,14.82,'Without using joints you are using joints [both ASRs]','ASR_AND_CLINICIAN_REVIEW','Contradictory wording persists across models. Lower-impact does not mean joints unused.','CDC_SWIM','Proposed clarification: joints still move. This overlay is editorial, not spoken.')]
}
for folder,rows in claims.items():
 p=R/folder/'qa/MEDICAL_CLAIMS.csv'
 with p.open('w') as f:
  w=csv.writer(f,lineterminator="\n");w.writerow(['claim_id','start_seconds','end_seconds','source_claim_ASR_or_paraphrase','status','reason','source_id','visual_handling'])
  w.writerows(rows)
 (p.parent/'PUBLICATION_GATE.md').write_text('''# Publication gate: QA_BLOCKED

All artwork is review material. The unchanged source audio contains claims/wording that require human listening and clinician review; see MEDICAL_CLAIMS.csv. Never infer that completed files mean clinical approval. Do not silently dub, rewrite, cut or time-stretch the source.

Optional editorial overlays are visibly marked in storyboard/title_proposed and fixed_text_layers. They are not transcript quotes, unless explicitly quoted and attributed. A clinician-approved correction may require a new narration version; preserve the original and its hash if that happens. Human editor must reconcile DRAFT_ASR.srt before using captions. No fake voice clone is authorized.

YouTube policy was checked on 2026-10-15 (MEDICAL_SOURCES.json). Content review here does not certify platform compliance, credentials, ownership, or medical safety. The actual claims, audience and local health guidance need review. Source audio rights are user-supplied/unverified.
''')
print('Saved',sum(map(len,claims.values())),'claim records')
