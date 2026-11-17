"""Editorial scene specifications. All text here is proposed visual copy, never transcript."""
# layer tuple: asset id, x, y, scale, reveal delay seconds
SPECS={
'01_HIIT_AFTER_60':[
 (0,3.24,'HIIT','Work. Recover. Repeat.',[('sam-run-warm',125,650,1.35,0),('intervals',175,430,1.0,.35),('score7',630,920,1,.9)],'Hook: illustrate interval contrast, then attribute rating.','H1'),
 (3.24,7.72,'Heart conditioning','An exercise benefit',[('sam-stand-warm',115,600,1.45,0),('heart',610,670,.85,1.7),('arrow',520,1040,.65,2.3)],'Heart appears on the spoken heart cue; symbolic, not diagnostic.','H2'),
 (7.72,13.36,'The important caveat','Existing heart disease',[('sam-concern-concern',120,620,1.45,0),('heart',650,810,.65,2.4),('question',690,580,.54,.6)],'Retain patient identity; concern without catastrophe.','H3'),
 (13.36,16.20,'Supervised care','Individual assessment',[('clinic',65,950,1.02,0),('nora-point-explain',105,690,1.08,.05),('sam-stand-warm',535,720,1.02,.4)],'Explainer and patient; fictional host has no implied credentials.','H4'),
 (16.20,21.26,'Risk needs context','No risk percentage supplied',[('sam-concern-concern',115,660,1.4,0),('question',610,740,.8,.5)],'Hold concern; never invent a mortality statistic or damaged heart.','H5'),
 (21.26,24.34,'Not one rule for everyone','Clinical review required',[('nora-open-concern',120,630,1.4,0),('heart',650,770,.7,.5)],'Audio avoidance statement remains disputed; no universal prohibition icon.','H6'),
 (24.34,28.90,'Endurance + stamina','Suitability matters',[('park',70,1080,1,0),('sam-run-warm',155,660,1.3,.05),('stopwatch',640,740,.7,1.4)],'Return to same patient; conceptual stamina, not prescribed HIIT session.','H7'),
 (28.90,30.557460,'The speaker’s verdict','A rating, not a medical scale',[('nora-open-warm',140,660,1.25,0),('score7',610,870,1,0)],'Short closing callback; no extra CTA or rewritten speech.','H1')],
'02_RUNNING_AFTER_60':[
 (0,2.70,'RUNNING','The speaker’s rating',[('park',70,1080,1,0),('sam-run-warm',135,650,1.35,0),('score7',650,550,1,.9)],'Immediate run pose; rating appears on spoken seven.','R1'),
 (2.70,4.64,'A form of exercise','',[('sam-run-warm',180,650,1.35,0),('heart',640,750,.65,.45)],'Preserve runner, add symbolic heart.','R2'),
 (4.64,11.36,'Consider your joints','Knees • ankles',[('sam-concern-concern',100,650,1.4,0),('joint',640,720,.8,2.8),('shoe',640,1100,.65,3.8)],'Highlight joints without asserting running always causes injury.','R3'),
 (11.36,14.42,'In moderation','',[('nora-open-explain',140,630,1.4,0),('stopwatch',635,800,.75,1.3)],'Conceptual pacing; no automatic dose recommendation.','R4'),
 (14.42,19.66,'“Three times per week”','Speaker’s advice — verify',[('calendar',570,680,1.0,.5),('nora-point-concern',80,760,1.25,0),('shoe',620,1150,.55,2.6)],'Attribute frequency; do not promote it as an age-based universal limit.','R5'),
 (19.66,24.04,'Heart function','The speaker’s conditional claim',[('sam-stand-warm',120,620,1.4,0),('heart',620,730,.85,1.6)],'Retain the normal-heart condition without implying a visual diagnosis.','R6'),
 (24.04,28.44,'Oxygen + exercise','VO₂: terminology needs review',[('lungs',145,680,1.05,.6),('heart',650,790,.65,1.4),('arrow',490,1040,.65,2.0)],'Symbolic oxygen/heart relation; no physiological numbers or bogus ECG.','R7'),
 (28.44,31.927438,'Endurance + stamina','',[('park',65,1080,1,0),('sam-run-warm',150,650,1.35,0),('stopwatch',650,800,.7,.6)],'Close on movement; do not add score absent from ending speech.','R8')],
'03_SWIMMING_AFTER_60':[
 (0,2.88,'SWIMMING','The speaker’s rating',[('pool',70,880,1,0),('june-swim-warm',150,900,1.05,0),('score95',570,510,1.05,.9)],'Immediate swimmer silhouette and attributed rating.','S1'),
 (2.88,5.92,'Heart fitness','A benefit, not a guarantee',[('pool',70,1000,1,0),('june-swim-warm',150,1020,1.05,0),('heart',370,570,.8,1.5)],'Heart revealed to match the spoken claim.','S2'),
 (5.92,10.16,'Fitness + endurance','',[('june-stand-warm',125,660,1.4,0),('heart',650,620,.65,.5),('stopwatch',640,1030,.65,2.4)],'Two-stage benefit build; not a comparison proving best exercise.','S3'),
 (10.16,11.88,'Whole-body movement','',[('pool',70,880,1,0),('june-swim-warm',150,900,1.05,0)],'Hold clear swimming pose; brief phrase has no extra text burden.','S4'),
 (11.88,14.82,'Joints still move','Wording needs listening review',[('june-swim-warm',110,700,1.05,0),('joint',370,1050,.8,.45)],'Do not visualize unused joints. Lower-impact explanation is a proposed clarification.','S5'),
 (14.82,17.866667,'The speaker’s verdict','A rating, not a medical scale',[('june-stand-warm',135,650,1.35,0),('score95',600,880,1,0)],'Preserve ending speech and tail; no invented title completion.','S1')]
}
