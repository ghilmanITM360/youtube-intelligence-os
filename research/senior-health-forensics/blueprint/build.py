# builds NEW_CHANNEL_BLUEPRINT.html (Chrome prints it to PDF)
import html
V=[
("Constipated After 60? Check These 5 Medicines Before Blaming Age",
 "Constipation / opioids, anticholinergics, verapamil-type CCBs, iron-calcium, some antidepressants",
 "A: ch43 38,052 live (86% of channel); ch44 2,886",
 "Left half: presenter holding an open pill drawer, worried look. Right: big 'AGE?' crossed, 'PILLS?' circled. Text: 'AGE or PILLS?'",
 "If you are over sixty and constipated for weeks, people tell you it is just age. Before you accept that, open your pill drawer. Some very common medicines are a known cause, and the fix is a conversation, not a guess. Today: five kinds of medicine to check, and three signs that mean call your doctor this week.",
 "1) Opioid pain medicines. 2) Anticholinergics: some bladder pills, older allergy and sleep pills. 3) Some calcium-channel blockers for blood pressure (verapamil is the usual example). 4) Iron and calcium supplements or antacids. 5) Some antidepressants. For each: where to find it on the label, and the question to ask: 'Is there another option, or a timing change?' Red flags: blood in stool, unexplained weight loss, severe pain, a sudden change that lasts weeks.",
 "Do not stop any pill on your own. Write the medicine name and the date constipation began. The one-page Ask-Your-Pharmacist card is in the description.",
 "ACG/AGA constipation guidance; NIDDK constipation page; drug labels (VERIFY)"),
("Waking Up to Pee at Night? Your Pill TIMING May Be the Reason",
 "Nocturia / water pills (diuretics) and evening dosing",
 "B: ch04 night-urination/mucus 160,522; ch40 sibling 11,851 (cluster, not independent)",
 "Clock showing 2:47 AM, presenter yawning, a pill bottle with a small clock icon. Text: 'IS IT YOUR PILL?'",
 "Two forty-seven in the morning. Third trip to the bathroom. You blame your bladder, your age, your tea. Here is a question almost nobody asks: what time did you take your water pill? Timing can change your nights. Let me show you what to check, and what to ask your prescriber.",
 "What a diuretic does and why timing matters (general principle; prescriber decides). Other contributors to check: evening fluids, caffeine, alcohol, swollen legs lying down, sleep apnea, prostate in men. A 3-day 'night log' the viewer can fill: time of pills, drinks, trips. Red flags: burning, blood in urine, sudden new urgency, fever.",
 "Never move a dose on your own: bring the night log to your pharmacist or doctor and ask 'Can this be taken earlier in the day?'",
 "Drug label for the specific diuretic; AUA/NIDDK nocturia information (VERIFY)"),
("Dizzy When You Stand Up? 4 Medicine Types Behind Many Falls After 65",
 "Orthostatic hypotension / BP pills, alpha-blockers, some antidepressants, diuretics",
 "A-: ch44 BP-pill video 48,366; ch29 BP-pill 25,104 (same frame, 2 channels)",
 "Presenter gripping a chair, motion lines, four small pill-class icons. Text: 'DIZZY? CHECK THESE 4'",
 "You stand up and the room tilts for a second. You tell yourself it is nothing. For many people over sixty-five, that second is the start of a fall. And one of the most common causes is sitting in the medicine cabinet. Four kinds of medicine, and the three-step standing test you can do tonight.",
 "Explain blood-pressure drop on standing in plain words. Four classes to check: blood-pressure medicines (including combinations), alpha-blockers used for prostate or BP, some antidepressants and sedatives, water pills. Safe habit: sit on the bed edge for a minute before standing. Show how to take lying-sitting-standing BP readings and write them down for the clinician. Red flags: fainting, chest pain, new confusion.",
 "Falls are about the whole picture. Ask: 'Which of my medicines can lower BP on standing, and should any be reviewed?' Do not skip BP pills on your own.",
 "AGS Beers Criteria; CDC STEADI falls guidance; drug labels (VERIFY)"),
("Memory Fog After 65? Check These Pills Before You Blame Aging",
 "Cognition / anticholinergics, benzodiazepines, some sleep aids",
 "A: ch27 memory-and-medication 3.59M (named clinician); ch07 dementia-medication 724K",
 "Presenter with a thought-bubble full of fog, one pill bottle clear in the foreground. Text: 'FOG: AGE OR PILL?'",
 "Forgetting words. Losing your train of thought. Many families hear 'it's just aging' and move on. But some common medicines are known to cloud thinking in older adults, and sometimes the fog lifts when the plan is reviewed. This is not about scaring you. It is about asking the right question first.",
 "Medicine groups linked with confusion or memory complaints in older adults: strongly anticholinergic drugs (some bladder, allergy, sleep products), benzodiazepines and similar sleep drugs, some pain medicines. How to read an OTC label for 'PM' or 'diphenhydramine'. A one-line symptom diary. Red flags: sudden confusion, getting lost, personality change: urgent medical review, not a video.",
 "Bring your list to the pharmacist and ask: 'Is anything here on the Beers list for my age?' Never stop a sleep or anxiety pill suddenly: stopping can be harmful.",
 "AGS Beers Criteria; anticholinergic-burden research; FDA benzodiazepine labeling (VERIFY)"),
("The 'PM' Pill Many Seniors Take Nightly: What Pharmacists Want You to Ask",
 "Diphenhydramine-containing 'PM' sleep/pain products",
 "C: ch44 sleep-pill video only 140 views; ch27 safety theme. TEST VIDEO (weak direct evidence)",
 "Closeup of an OTC 'PM' box, presenter pointing at the small print. Text: 'READ THIS WORD'",
 "Look at the box you take at night. Find the small word in the ingredient list. That one word is why pharmacists get nervous when a person over sixty-five takes this every night. Let me show you where to find it and what to ask instead of guessing.",
 "Why one ingredient appears in many products (sleep, cold, 'PM' pain relief). Why older adults are more sensitive (dry mouth, urine retention, next-day drowsiness, confusion, falls). Non-drug sleep basics in 3 lines. How to ask: 'What are my safer options for sleep, for me?'",
 "Not 'stop tonight' but 'ask this week'. Pharmacist card in description.",
 "AGS Beers Criteria; FDA OTC labeling (VERIFY)"),
("Swollen Ankles After 60? Medicines That Cause Fluid Retention",
 "Edema / amlodipine-type CCBs, NSAIDs, some diabetes pills",
 "C+: no direct DB winner; adjacent BP-medicine frame (ch44, ch29). TEST VIDEO",
 "Presenter pressing a sock-mark in a swollen ankle, sock-line visible. Text: 'SOCK MARKS? PILLS?'",
 "Pull off your socks at night. Do you see deep lines around your ankles? Swelling is not always the heart, and it is not always age. Sometimes it is a medicine effect your clinician can adjust. Here are the medicine groups to check, and the swelling signs that need a same-day call.",
 "Medicine groups linked with ankle swelling: some blood-pressure drugs (for example amlodipine-type), NSAID pain relievers, some diabetes medicines. Other causes to rule out (heart, kidney, veins): why a clinician must check. Red flags: swelling on one leg only, breathlessness, chest pain: emergency.",
 "Ask: 'Could any of my medicines cause this, and is there another option?' Do not stop heart or BP medicines on your own.",
 "Drug labels; AHA/ACC edema guidance (VERIFY)"),
("Always Tired After 60? 3 Medicine Types That Quietly Drain Your Energy",
 "Fatigue / beta-blockers, sedating antihistamines, sleep and anxiety drugs",
 "C+: tiredness is a high-volume search symptom (Trends NOT run). TEST VIDEO",
 "Presenter slumped at a table with an untouched coffee, three pill-type icons above. Text: 'TIRED? THREE PILLS'",
 "You sleep eight hours and still wake up flat. You tell your family, I'm just old. But there are three medicine types that can quietly pull your energy down, and a short checklist that tells your doctor exactly what to look at.",
 "Three groups: beta-blockers (may cause tiredness in some people), sedating antihistamines and sleep aids, benzodiazepine-type drugs. Also not-pill causes to ask about: low thyroid, low B12, anaemia, poor sleep, low mood. A 7-day energy score and pill-time sheet.",
 "Ask the clinician to review the list and consider blood tests; never stop a beta-blocker abruptly.",
 "Drug labels; AGS Beers Criteria; clinical guidance on fatigue (VERIFY)"),
("Tylenol, Advil or Aleve? Which One Fits Which Senior",
 "OTC pain relievers by condition (kidney, stomach, BP, liver)",
 "A: ch27 Tylenol/Advil 825K",
 "Three pain-reliever boxes as podium, presenter holding 'WHICH ONE FOR ME?' card. Text: 'ONE DRAWER, 3 RISKS'",
 "Three boxes in your drawer. Everyone reaches for the nearest one. But if you are over sixty with blood pressure, stomach, or kidney concerns, the right choice may be different from your neighbour's. Let me give you the one-minute chart pharmacists use.",
 "Acetaminophen: liver limits and hidden duplicates in cold products. Ibuprofen and naproxen (NSAIDs): stomach, kidney and BP effects; special caution with blood thinners. A simple grid by condition. Duplicate-ingredient trap with combination products.",
 "Ask the pharmacist: 'Given my conditions and medicines, which is safest for me and what is my daily limit?'",
 "FDA/NIDDK OTC analgesic labeling; AGS pain guidance (VERIFY)"),
("Brown Bag Review: The 10-Minute Pill Check You Can Do Tonight (Free Card)",
 "Evergreen flagship: whole medicine-cabinet review",
 "B: dawai-safety theme across ch27, ch29, ch44, ch07",
 "Presenter at a kitchen table, all pill bottles laid out in a row, a paper bag. Text: 'EMPTY THE DRAWER'",
 "Empty your pill drawer onto the table, include vitamins and creams. Ten minutes, one pen. By the end you will know which questions to take to your pharmacist, and you will have a one-page list your whole family can use in an emergency.",
 "Step 1 list everything with dose and time. Step 2 for each: what is it for? Step 3 still needed? Step 4 duplicates and interactions. Step 5 timing and food. Step 6 questions card. Show the printable card. Explain 'brown bag' visits at pharmacies.",
 "This is a preparation tool, not a prescription. Review is done with a pharmacist or doctor.",
 "Pharmacy brown-bag medication-review guidance; WHO/NHS medication-review resources (VERIFY)"),
("Mom Takes 12 Pills: The 5-Step Review for Caregivers Before the Next Appointment",
 "Caregiver / polypharmacy / adult children as the buyer-viewer",
 "B-: ch27's caregiver audience; direct competitor video not measured",
 "Adult daughter beside older mother, a long pill list in her hand. Text: 'MOM'S 12 PILLS'",
 "If you manage a parent's medicines, you know the fear: is something wrong in this list? You are not a pharmacist, and you do not need to be. Here is a five-step review you can finish before the next appointment, and the exact questions to ask.",
 "Steps: one master list; ask what each is for; flag recent changes (new symptom after new pill?); check for duplicates; bring everything to one pharmacy. Scripts for the conversation with a doctor. When it is urgent.",
 "Say the last line: 'Questions are not rude. Good clinicians welcome them.'",
 "Medication-review guidance for caregivers (NIA, AARP-type resources) (VERIFY)"),
]
plan=[
 ("1","Decide pharmacist/clinician partner (real, named, licence checkable). No partner = no launch.","Signed partner, licence noted"),
 ("2","Lock name, handle check, logo, 3 thumbnail templates, caption style.","Brand kit"),
 ("3","Write Ask-Your-Pharmacist card (1 page, printable).","PDF card v1"),
 ("4","Pharmacist reviews scripts V1, V3, V8 facts line by line against labels/Beers.","Fact sheet"),
 ("5","Record V1 and V3 (batch day). Test mic, large-font captions.","2 raw videos"),
 ("6","Edit V1; thumbnail A/B (2 versions).","V1 ready"),
 ("7","Edit V3; write channel description with disclaimer + sources habit.","V3 ready"),
 ("8","PUBLISH V1 (Constipated After 60). Pin card in comment.","Live"),
 ("9","Reply to every comment; note which questions viewers ask (next topics).","Comment log"),
 ("10","Record V2 and V4.","2 raw videos"),
 ("11","PUBLISH V3 (Dizzy When You Stand Up).","Live"),
 ("12","Shorts 1-2: original single-question cuts, NOT a re-upload of the long video.","2 Shorts"),
 ("13","Edit V2 and V4.","Ready"),
 ("14","Read Studio data for V1 (first-party). Record numbers; no decision yet.","Data sheet"),
 ("15","PUBLISH V2 (Night Pee / pill timing).","Live"),
 ("16","Record V8 (Tylenol/Advil/Aleve) and V9 (Brown Bag flagship).","2 raw"),
 ("17","Shorts 3-4.","2 Shorts"),
 ("18","PUBLISH V4 (Memory Fog).","Live"),
 ("19","DECISION POINT 1: rank V1-V4 by views, average view duration, comments. Kill/keep angles.","Decision note"),
 ("20","Edit V8 and V9.","Ready"),
 ("21","Record V5 (PM pill) and V10 (caregiver).","2 raw"),
 ("22","PUBLISH V8 (Painkiller drawer).","Live"),
 ("23","Shorts 5-6 from comment questions.","2 Shorts"),
 ("24","Edit V5, V10; pharmacist fact check.","Ready"),
 ("25","PUBLISH V9 (Brown Bag flagship).","Live"),
 ("26","Record V6, V7 (only if decision point says symptom angle works).","2 raw"),
 ("27","PUBLISH V5 (PM pill).","Live"),
 ("28","Shorts 7-8; playlist 'Aging or Pills?' set up.","Playlist"),
 ("29","PUBLISH V10 (Caregiver 12 pills).","Live"),
 ("30","DECISION POINT 2: double down on the winning symptom family or change; plan next 30 days. V6, V7 go out in week 5.","30-day review"),
]
def esc(s): return html.escape(s)
h=[]
h.append("""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Pill or Aging - New Senior Health Channel Blueprint</title>
<style>
@page{size:A4;margin:16mm 14mm}
body{font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:10.5pt;line-height:1.45;color:#1d2330}
h1{font-size:25pt;margin:0 0 4px;color:#0f4c5c}h2{font-size:15pt;color:#0f4c5c;border-bottom:2px solid #0f4c5c;padding-bottom:3px;margin-top:22px;page-break-after:avoid}
h3{font-size:11.5pt;margin:0 0 4px;color:#9a3412}
.sub{color:#555;margin-bottom:10px}.box{background:#f3f7f8;border-left:4px solid #0f4c5c;padding:8px 11px;margin:8px 0}
.warn{background:#fff6ed;border-left:4px solid #c2410c;padding:8px 11px;margin:8px 0}
table{border-collapse:collapse;width:100%;margin:6px 0;font-size:9.5pt}th,td{border:1px solid #cfd8dc;padding:4px 6px;vertical-align:top;text-align:left}th{background:#e6eef0}
.v{border:1px solid #cfd8dc;border-radius:6px;padding:9px 11px;margin:10px 0;page-break-inside:avoid}
.k{font-weight:700;color:#0f4c5c}.tag{display:inline-block;background:#0f4c5c;color:#fff;border-radius:3px;padding:0 6px;font-size:9pt;margin-right:6px}
.small{font-size:9pt;color:#555}p{margin:4px 0}
</style></head><body>
<h1>Pill or Aging?</h1><div class="sub">Naya Senior Health channel: niche, naam, top 10 videos, titles, scripts, thumbnails, 30-day plan. Banane ki tareekh 2026-11-14. Zaban: Roman Urdu (titles/scripts audience ke liye English).</div>

<div class="warn"><b>Seedhi baat pehle.</b> Koi bhi blueprint views ki <b>guarantee nahi</b> de sakta. Hamare 44 channels mein naye channels ki median video 88 (ch43) aur 732 (ch44) views par thi; ek video 80-86% views le gaya. Ye niche "ek outlier + baaki flat" wala hai. Is liye plan 10 videos ko 10 tickets ki tarah rakhta hai aur din 19 aur 30 par decision points deta hai. "Kisi ne nahi dekha" ka matlab yahan: <b>44 channels mein ye format nahi mila (fact)</b>; poore YouTube par nahi hai (<b>Not known</b>, check nahi hua). Demand par yaqeen sirf symptom-topics ka hai jo hamare data mein jeete; naya angle <b>hypothesis</b> hai jise pehle 3-4 videos test karengi.</div>

<h2>1. Niche: kyun aur kya</h2>
<p><span class="k">Niche:</span> <b>Symptom-first medicine-cabinet safety for 60+ aur unke caregivers</b>: "Ye meri umr ki wajah se hai ya meri goli ki?" Har video ek aam symptom se shuru hota hai (qabz, raat ko peshab, chakkar, yaadasht ka dhundhlapan, thakan, sujan), phir un dawai-groups ko dekhta hai jinke baare mein maloom hai ke woh yeh asar kar sakti hain, aur akhir mein viewer ko doctor/pharmacist ke liye ek sawal-card deta hai.</p>
<table><tr><th>Hamari research se (fact)</th><th>Naya kya hai (interpretation)</th></tr>
<tr><td>Dawai-safety mein sab se bade jeetne wale: ch27 memory-aur-dawai 3.59M, Tylenol/Advil 825K; ch44 BP-dawai 48,366; ch29 25,104; ch07 724K.</td><td>Ye sab <b>dawai-pehle</b> hain ("is goli ka sach"). Hum <b>symptom-pehle</b> hain, jo search karne wala viewer asal mein type karta hai.</td></tr>
<tr><td>Sharminda sawal-topics jeete: qabz ch43 38,052 (86%), ch44 2,886; raat ko peshab ch04/40.</td><td>Hum in dono winners ko jodte hain: "qabz/raat ka peshab" + "dawai-wajah".</td></tr>
<tr><td>Clone factories (04/06/09/31/32/33) wellness-food par; tail patla; copies ke views purani copy ke ~3.3% (median).</td><td>Kisi cluster ka topic/script nahi uthaya. Sirf yeh dekha ke kahan demand sabit hui.</td></tr>
<tr><td>Ch27 (asli named clinician) jeeta, ch30 (clinician, naya, Shorts-heavy) ~10K total.</td><td>Credential akela kaafi nahi; topic + asli chehra + caregiver audience + lamba tail milkar kaam karte hain (n=2, low).</td></tr></table>
<h3>Platform context (2026-11-14)</h3>
<ul>
<li><b>DS-000018 se validated (primary evidence se):</b> ranking har viewer aur surface ke liye alag hai, kisi ek metric par nahi (CLM-001, 004); subscribe karne se video dikhna zaroori nahi (CLM-008); <b>templated, mutashabeh episodes</b> par monetization risk hai, lekin <b>jo episodes maani khez tor par badalte hain woh inauthentic nahi</b> (CLM-009, monetization rule, ranking rule nahi). Shorts aur long ek channel par rakhna <b>audience overlap</b> par munhasir hai (CLM-005/018). DS-000018 ke 33 claims mein sirf kuch validate hue; baqi unverified hain, unhein rule nahi banaya.</li>
<li><b>Jul 2026 policy (secondary sources, official page check nahi hua):</b> YouTube ne inauthentic content ki wazahat ki; reports ke mutabiq "AI personas on sensitive topics" (health/finance) monetize nahi. Is liye <b>asli insaan presenter zaroori</b>, AI-awaz/AI-chehra nahi. Sources: <a href="https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/">Tubefilter</a>, <a href="https://outlierkit.com/blog/youtube-updates-july-2026">OutlierKit</a>, <a href="https://thedesk.net/2026/07/youtube-clamps-down-low-quality-ai-slop/">TheDesk</a>.</li>
<li><b>Oct 2026:</b> Shorts recommendations original content ko tarjeeh dete hain; bina izafe ke re-uploads kam reach (secondary report). Hum long video ki clip dobara upload nahi karenge; Shorts alag sawal par.</li>
<li><b>Nahi chala:</b> Google Trends, vidIQ, Studio data, playback. Demand ke numbers sirf hamare DB/live curl se.</li></ul>

<h2>2. Channel ka naam</h2>
<table><tr><th>#</th><th>Naam</th><th>Kyun</th></tr>
<tr><td>1 (pick)</td><td><b>Pill or Aging?</b>  (handle idea: @PillOrAging)</td><td>Pehle 3 lafz mein promise; har title ka sawal-frame; thumbnail ka "AGING | PILL" split; senior ke liye saaf.</td></tr>
<tr><td>2</td><td>The Brown Bag Review</td><td>Pharmacy ka asli term; evergreen, lekin symptom-hook nahi.</td></tr>
<tr><td>3</td><td>Symptom or Side Effect?</td><td>Seedha, par lamba aur kam yaad rehne wala.</td></tr></table>
<p class="small">Naam ki availability, trademark aur handle check <b>nahi hua</b>; launch se pehle YouTube search + trademark search karein.</p>
<p><b>Presenter:</b> ek asli licensed pharmacist ya doctor jo apne naam se aaye, licence verify ho. Maine koi naam ya credential <b>nahi gadha</b>. Kisi aur ke naam (jaise ch43 ka "Dr. Jason Fung") ya ch27/30 ke clinician ka istemal nahi.</p>

<h2>3. Format (jo har episode mein fix hai, content badalta hai)</h2>
<ol><li><b>Symptom-hook (0-30s):</b> ek roz ka manzar, phir "kya ye umr hai ya goli?"</li><li><b>Suspect list:</b> 3-5 dawai-groups, har ek ke saath label ka naam screen par.</li><li><b>Case file:</b> ek <i>composite</i> (disclosed: "ye misaal hai, asli mareez nahi") jiska list se mukabla dikhaya jaye.</li><li><b>Red flags:</b> kab fauran doctor/emergency.</li><li><b>Card:</b> Ask-Your-Pharmacist card (free PDF), sources description mein.</li></ol>
<div class="box">Variation rule (CLM-009 ke liye): har episode mein alag symptom, alag dawai-groups, alag misaal, alag kis cheez ka jawab. Sirf title mein naam badalna <b>nahi</b>. Har script se pehle <code>script_reuse.py</code> se hamare 44 channels ke scripts ke saath jaccard check karein (&lt;0.85, behtar &lt;0.2).</div>
<div class="warn"><b>Hamesha:</b> "apni goli khud band na karein"; har clinical line ke saath source (label / AGS Beers / guideline); pharmacist ya doctor har script review kare; disclaimer description mein. Neeche ki clinical lines meri taraf se <b>VERIFY nahi hui</b>; recording se pehle clinician check zaroori hai.</div>

<h2>4. Thumbnail system (sab videos)</h2>
<ul><li>Asli presenter ka chehra (cartoon/AI nahi, ch41/44 ki kaali background wali look nahi) + <b>2-4 lafz</b>, bohat bara font (senior ki nazar ke liye).</li>
<li>Rang: cream background, gehra teal (#0f4c5c), ek laal accent. Har thumbnail mein <b>split "AGING | PILL"</b> motif ek jaisa (brand), lekin har ek mein symptom ka alag manzar.</li>
<li>"SHOCKING / EXPOSED / DEATH" nahi, aur title se zyada claim nahi.</li>
<li>Har video ke 2 thumbnail variant (A/B).</li></ul>

<h2>5. Top 10 videos</h2>
<p class="small">Evidence grade: A = hamare data mein seedha winner; B = adjacent theme; C = test video (kamzor direct evidence). Views live curl/DB 2026-11-14.</p>
""")
for i,(t,topic,ev,th,hook,body,close,src) in enumerate(V,1):
    h.append(f'<div class="v"><h3><span class="tag">V{i}</span>{esc(t)}</h3>'
      f'<p><span class="k">Topic:</span> {esc(topic)}</p><p><span class="k">Evidence:</span> {esc(ev)}</p>'
      f'<p><span class="k">Thumbnail:</span> {esc(th)}</p>'
      f'<p><span class="k">Script, hook (0-30s):</span> &ldquo;{esc(hook)}&rdquo;</p>'
      f'<p><span class="k">Script, beech:</span> {esc(body)}</p>'
      f'<p><span class="k">Script, akhir:</span> {esc(close)}</p>'
      f'<p class="small"><b>Sources (VERIFY, fetch nahi):</b> {esc(src)}</p></div>')
h.append("<h2>6. 30-day content plan</h2><p>Cadence: <b>10 long videos + 8 original Shorts</b>. Hamare naye channels ne 3-6 videos/hafta se bhi baseline nahi banayi (fact, ch38-44); isliye quantity nahi, pharmacist-checked quality. Order: pehle A-grade topics, C-grade test videos baad mein.</p><table><tr><th>Din</th><th>Kaam</th><th>Output</th></tr>")
for d,t,o in plan: h.append(f"<tr><td>{d}</td><td>{esc(t)}</td><td>{esc(o)}</td></tr>")
h.append("""</table>
<h2>7. Test aur kill rules (hamare apne, platform ke nahi)</h2>
<p>YouTube koi universal CTR/retention threshold nahi deta (validation). Isliye ye hamare faislay ke nishan hain, Studio data aane ke baad apne channel ke andar mukabla:</p>
<ul><li><b>Din 19:</b> V1-V4 mein se jis symptom-family ki views, average view duration aur comments sab se zyada hain use agle mahine barhao. Agar 4 mein se koi bhi doosron se saaf aage nahi, to "symptom-pehle" angle ko dawai-pehle (ch44 jaisa frame) se badal kar dubara test karein.</li>
<li><b>Din 30:</b> 10 videos ke baad top-1 ka share dekhein. Agar ek video 80% se zyada hai (hamare niche ki aam shakal), usi video ke siblings banayein (alag symptom, wahi suspect-list frame).</li>
<li>Pehle 3 videos ke baad agar presenter ya script mein clinical ghalti mili to saari pipeline rok kar sab review.</li></ul>
<h2>8. Kya UNKNOWN hai</h2>
<ul><li>CTR, retention, traffic source, monetization: naye channel ka data nahi, hamare 44 mein bhi UNKNOWN.</li>
<li>"Symptom-first" angle ki demand: hypothesis. Symptoms (qabz, raat ka peshab, chakkar) ki demand hamare data mein dikhi; "wajah dawai?" wala angle kisi channel par measure nahi hua.</li>
<li>Google Trends, vidIQ: nahi chale. Launch se pehle 10 symptom-topics par Trends aur YouTube search-suggest check karein.</li>
<li>Presenter/partner: abhi nahi mila. Naam availability: check nahi.</li>
<li>Saari clinical lines: unverified; pharmacist review lazmi.</li></ul>
<p class="small">Basis: research/senior-health-forensics/SYNTHESIS_44_channels.md aur reports 01-44; title_families.csv; DS-000018 validation (data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md). Web trends: Tubefilter, OutlierKit, TheDesk, TechRepublic (secondary).</p>
</body></html>""")
open("/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/senior-health-forensics/blueprint/NEW_CHANNEL_BLUEPRINT.html","w").write("".join(h))
