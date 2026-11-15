import html
src=open('build.py').read().split('def esc')[0]
exec(src)  # gives V (old list) and plan
OLD=V
def esc(s): return html.escape(s)
# (old index, new title, tested evidence, status)
R=[
(6,"Tired on a Beta-Blocker? What Metoprolol Fatigue Looks Like and 3 Questions to Ask",
 "YT test 2026-11-14: JJ Medicine metoprolol 1,013,965; Medicine with Dr. Moran 204,590; small channels 196-849. Demand proven, giants exist, no 'after 60' needed.","LAUNCH"),
(4,"Benadryl or 'PM' Pills Every Night? What the Dementia Studies Actually Say",
 "YT test: Leonid Kim MD 'This Pill is linked to DEMENTIA' 6,598,380; Doctor Mike 781,788; new small channels 127-301. Biggest demand, biggest competition.","LAUNCH (test)"),
(0,"Medicines That Cause Constipation: Check Your List Before Buying Another Laxative",
 "YT test: KenDBerryMD 72K (5 yr); Dr Nimra 815 (1 mo, exact angle exists); ~6 of 7 recent 'after 60' clones <1K. Modest, angle NOT new.","LAUNCH"),
(2,"Dizzy When You Stand Up? Your Pills Could Be the Reason (3-Step Check)",
 "YT test: Fauquier ENT 1,140,511; motivationaldoc Short 531,525; 7 recent 'after 60' clones 10-900. Trends 'dizziness' last 52w +42% vs prior.","LAUNCH"),
(1,"Waking to Pee at Night? Check WHEN You Take Your Water Pill",
 "YT test: Rena Malik 1,324,269 (5 yr); TopHealthTips 94,765 ('Do THIS before bed'); 6 recent clones 38-420. Pill-timing angle: none seen in top 9.","LAUNCH (test)"),
(3,"Medicines Linked to Memory Fog: 3 Shorts First, Long Video Later",
 "YT test: Shorts 26K-65K (Dr. Ethan Melillo PharmD 64,636); long videos 15-1,278. Shorts carry demand, long form unproven.","MONTH 2 (Shorts now)"),
(7,"Tylenol, Advil or Aleve? Which Fits Which Senior",
 "YT test: Better Health While Aging 826,303; Talking With Docs 682,056; 5+ others 300K-1.7M. Saturated by giants.","LOW PRIORITY"),
(5,"Swollen Ankles? Medicines That Cause Fluid Retention",
 "YT test: KenDBerryMD '11 Common Medications That Cause Edema' 1,752,304. Trends 'swollen ankles' Nov-Feb 25.2 vs 43.0 other months (-41%).","SPRING (Apr-Jun), not next 3 months"),
(8,"Brown Bag Review: The 10-Minute Pill Check (Free Card)",
 "YT test: top 9 results all <=1,177 views. Low demand.","LEAD MAGNET only"),
(9,"Mom Takes 12 Pills: The 5-Step Review for Caregivers",
 "YT test: top 9 results 16-2,176 views. Low demand.","LEAD MAGNET only"),
]
plan2=[
("1-2","Real named pharmacist/doctor partner (licence checkable). No partner = no launch.","Signed partner"),
("3","Re-run YouTube search + Trends for R1-R5 (last 7 days). Drop any title where the exact angle now has a fresh competitor.","Check sheet"),
("4","Brand kit, 3 thumbnail templates, Ask-Your-Pharmacist card.","Kit + card"),
("5","Pharmacist fact-checks scripts R1, R3, R4 against labels / Beers / guidelines.","Fact sheet"),
("6-7","Record + edit R1 and R3.","2 videos"),
("8","PUBLISH R1 (beta-blocker fatigue). Pin card.","Live"),
("9-10","Record R2 and R4; 2 Shorts (original single questions).","2 videos, 2 Shorts"),
("11","PUBLISH R2 (Benadryl/PM).","Live"),
("12-14","Edit; reply to every comment; log viewer questions.","Comment log"),
("15","PUBLISH R3 (constipation medicines).","Live"),
("16-17","Record R5; 2 Shorts (memory-fog meds).","1 video, 2 Shorts"),
("18","PUBLISH R4 (dizzy on standing).","Live"),
("19-20","Studio data for R1-R2 (first-party). Notes only.","Data sheet"),
("21","DECISION 1: compare R1-R4 (views, avg view duration, comments). Keep the winning drug/symptom family; kill angles that match clone-level results.","Decision note"),
("22","PUBLISH R5 (night-pee, pill timing).","Live"),
("23-25","Record next video from the winning family; 2 Shorts.","1 video, 2 Shorts"),
("26","PUBLISH it.","Live"),
("27-29","Shorts + playlist 'Pill or Aging?'; publish lead-magnet Short for the card.","Playlist"),
("30","DECISION 2: next 30 days. Spring video (ankles) scheduled for Apr.","30-day review"),
]
h=[]
h.append("""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Pill or Aging - Blueprint v2 (tested)</title>
<style>
@page{size:A4;margin:16mm 14mm}
body{font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:10.5pt;line-height:1.45;color:#1d2330}
h1{font-size:24pt;margin:0 0 4px;color:#0f4c5c}h2{font-size:15pt;color:#0f4c5c;border-bottom:2px solid #0f4c5c;padding-bottom:3px;margin-top:22px;page-break-after:avoid}
h3{font-size:11.5pt;margin:0 0 4px;color:#9a3412}
.sub{color:#555;margin-bottom:10px}.box{background:#f3f7f8;border-left:4px solid #0f4c5c;padding:8px 11px;margin:8px 0}
.warn{background:#fff6ed;border-left:4px solid #c2410c;padding:8px 11px;margin:8px 0}
table{border-collapse:collapse;width:100%;margin:6px 0;font-size:9.3pt}th,td{border:1px solid #cfd8dc;padding:4px 6px;vertical-align:top;text-align:left}th{background:#e6eef0}
.v{border:1px solid #cfd8dc;border-radius:6px;padding:9px 11px;margin:10px 0;page-break-inside:avoid}
.k{font-weight:700;color:#0f4c5c}.tag{display:inline-block;background:#0f4c5c;color:#fff;border-radius:3px;padding:0 6px;font-size:9pt;margin-right:6px}
.small{font-size:9pt;color:#555}p{margin:4px 0}
</style></head><body>
<h1>Pill or Aging? &mdash; v2 (YouTube + Trends se tested)</h1>
<div class="sub">Test ki tareekh 2026-11-14. Pehli PDF ko YouTube search aur Google Trends par dobara parkha; jo ghalat nikla woh neeche saaf likha hai. Roman Urdu; titles/scripts English.</div>

<div class="warn"><b>Seedha nateeja.</b> (1) Angle "meri dawai is symptom ki wajah?" <b>naya nahi</b> hai; pehle se maujood hai, aur bohat bade views bhi le chuka hai (KenDBerryMD edema 1.75M, Leonid Kim dementia-pill 6.6M). (2) Jo naye channels "After 60 / After 65" suffix par bane hain unki recent videos lagbhag sab <b>1,000 se kam</b> par hain. (3) Isliye plan badla: suffix hata kar <b>ek naam wali dawai/class</b>, aur 5 topics launch par, baqi baad mein. (4) Agle 3 mahine mein <b>views ki guarantee nahi</b>; mausam (winter) ki wajah se demand nahi girti (sirf swollen-ankles girti hai), lekin asli rukawat muqabla aur naye channel ki shuruaat hai.</div>

<h2>1. Kya test hua</h2>
<ul><li><b>YouTube search</b> (page ka apna ytInitialData, login/cookie nahi): 9 topics, har ek ke top 9-10 results ke views/age/channel. Taareekh 2026-11-14, US-style English queries. Order personalised ho sakta hai.</li>
<li><b>Google Trends</b> (web search, US, past 5 years, data 8 Nov 2026 tak): constipation, dizziness, frequent urination, memory loss, benadryl, swollen ankles, nocturia. Seasonality: Nov&ndash;Feb ka average baqi mahinon ke muqabil.</li>
<li><b>Limit:</b> Trends sab umar ka US data hai (60+ alag nahi); lambay phrases ("constipation after 60", "medications that cause constipation") YouTube-Trends par ~0 aaye, yaani measure karne layak data nahi. Ye "demand nahi" ka saboot nahi, sirf "number nahi mila". Studio/vidIQ data nahi.</li></ul>

<h2>2. YouTube search ke nateeje (fact)</h2>
<table><tr><th>Topic</th><th>Bade/purane winners</th><th>Naye "after 60"/clone channels</th><th>Is angle ki maujoodgi</th></tr>
<tr><td>Constipation + dawai</td><td>Better Health While Aging 319,380; Doctor Sethi 563,475 (Short); KenDBerryMD "Medicines that Cause CONSTIPATION" 72K (5 yr)</td><td>628, 815, 16, 9, 279, 236, Dr. Dani Fisher 4,603</td><td><b>Maujood:</b> "10 Common Medications That Can Secretly Cause Constipation" 815 views</td></tr>
<tr><td>Raat ko peshab</td><td>Rena Malik 1,324,269; TopHealthTips 94,765</td><td>265, 313, 164, 65, 38, 420</td><td>Pill-timing angle top 9 mein nahi dikha</td></tr>
<tr><td>Khade hote chakkar</td><td>Fauquier ENT 1,140,511; motivationaldoc Short 531,525</td><td>10, 100, 163, 125, 319, 23, 900</td><td>"Medications Are #1" title maujood (319 views)</td></tr>
<tr><td>Memory aur dawai</td><td>Shorts 25,997 / 29,769 / 64,636; News4JAX 31,972</td><td>long videos 15, 267, 1,278</td><td>Maujood; Shorts jeet rahe, long kamzor</td></tr>
<tr><td>Benadryl / PM pill</td><td>Leonid Kim MD 6,598,380; Doctor Mike 781,788; KenDBerryMD 359,329</td><td>127, 301</td><td>Bohat bheed</td></tr>
<tr><td>Sujan + dawai</td><td>KenDBerryMD 1,752,304; Michigan Foot Doctors 3,366,382</td><td>(seniors-clones kam)</td><td>Maujood, bohat bada</td></tr>
<tr><td>Beta-blocker thakan</td><td>JJ Medicine 1,013,965; Dr. Moran 204,590</td><td>196, 664, 849</td><td>Maujood</td></tr>
<tr><td>Tylenol/Advil/Aleve</td><td>Better Health While Aging 826,303; Talking With Docs 682,056; Bob &amp; Brad 1,751,414</td><td>78</td><td>Bohat bheed</td></tr>
<tr><td>Brown bag review</td><td>sab 1,177 se kam</td><td>6-490</td><td>Demand kam</td></tr>
<tr><td>Caregiver polypharmacy</td><td>sab 2,176 se kam</td><td>16-91</td><td>Demand kam</td></tr></table>
<div class="box"><b>Kya seekha (interpretation, medium):</b> (a) "Medicines that cause X" ek <b>purana, sabit</b> frame hai, lekin jeetne wale bade/established doctors ya pharmacists hain. (b) "After 60/65" + "Dr. X Senior" wale naye channels ek jaisi clone-shakal mein hain (naam ya sheer-title farq, views 9&ndash;900); is suffix ka koi faida nahi dikha. (c) Jeetne wale titles saade hain: ek dawai/ek sawal, 5&ndash;12 minute ya Short, asli chehra. (d) Ye search sample hai, pura YouTube nahi, aur views ka matlab "us wakt tak" hai, naye videos ko time lagta hai.</div>

<h2>3. Google Trends (fact, US web search, 5 saal, data 8 Nov 2026 tak)</h2>
<table><tr><th>Term</th><th>Nov&ndash;Feb avg</th><th>Baqi mahine avg</th><th>Pichle 52 hafte vs us se pehle</th><th>Matlab</th></tr>
<tr><td>constipation</td><td>63.8</td><td>65.8</td><td>74.7 vs 66.5 (+12%)</td><td>Winter mein flat, barh raha hai</td></tr>
<tr><td>dizziness</td><td>22.0</td><td>24.4</td><td>31.3 vs 22.1 (+42%)</td><td>Flat winter, tez barhat</td></tr>
<tr><td>benadryl</td><td>39.8</td><td>46.9</td><td>42.2 vs 44.1</td><td>Halka winter dip (~15%)</td></tr>
<tr><td>memory loss</td><td>7.3</td><td>7.5</td><td>9.8 vs 7.3 (+34%)</td><td>Chhota par barh raha hai</td></tr>
<tr><td>frequent urination</td><td>4.5</td><td>4.9</td><td>5.1 vs 4.7</td><td>Chhota, flat</td></tr>
<tr><td>nocturia</td><td>10.8</td><td>12.1</td><td>16.0 vs 11.0</td><td>Halka dip, barhat</td></tr>
<tr><td>swollen ankles</td><td>25.2</td><td>43.0</td><td>35.9 vs 35.5</td><td><b>Winter mein -41%</b>; peak Apr&ndash;Jul</td></tr></table>
<p class="small">Numbers ek hi cluster ke andar relative hain (do alag comparison runs ke beech scale mila kar mat parhein). Sab umar ka US data hai, 60+ alag nahi.</p>

<h2>4. Agle 3 mahine (14 Nov 2026 &ndash; 14 Feb 2027): videos chalengi?</h2>
<table><tr><th>Sawal</th><th>Jawab</th><th>Confidence</th></tr>
<tr><td>Kya winter mein demand gir jati hai?</td><td>Nahi: constipation, dizziness, memory loss, nocturia flat ya upar. Benadryl halka kam. <b>Swollen ankles gir jati hai</b> (is liye spring).</td><td>Medium (Trends, US, sab umar)</td></tr>
<tr><td>Kya naye channel ki videos 3 mahine mein chalengi?</td><td>Sample mein constipation, chakkar, raat-peshab aur Benadryl ke recent naye-channel videos 22 dekhe: 21 ek hazaar se kam, ek 4,603. Isliye <b>zyada tar videos 50&ndash;1,000 views</b> par rahengi; "chalna" (10K+) ek lottery hai, guarantee nahi. 100K+ ka koi sample nahi mila.</td><td>Medium (sample chhota, view-lag)</td></tr>
<tr><td>Kya koi cheez asaani se jeet degi?</td><td>Sab se mazboot candidate: ek <b>naam wali dawai</b> + asli chehra (R1 beta-blocker, R2 Benadryl), lekin bade channels ke saath muqabla hai. Pill-timing (R5) mein angle khali dikha, demand ka size anjana.</td><td>Low</td></tr>
<tr><td>Kya Q4/holidays ka asar hai?</td><td>Is test ne measure nahi kiya. UNKNOWN.</td><td>&mdash;</td></tr></table>
<div class="warn"><b>Aap ki baat ka jawab:</b> "kisi ne nahi dekha lekin views aayen" dono saath mushkil hai. Demand wahin hai jahan pehle se videos hain. Hamari <b>asli jeet</b> topic mein nahi, execution mein ho sakti hai: asli named clinician, naam wali dawai, saaf script, source-cited, aur ek jaisi series. Ye hypothesis hai; pehle 4 videos (din 21 ka decision) isay test karengi.</div>

<h2>5. Naya top 10 (test ke baad dobara tarteeb)</h2>
<p class="small">Format: <b>Symptom/dawai &rarr; sawal &rarr; "pharmacist se kya poochhein"</b> card. "After 60" suffix nahi. Presenter asli, named pharmacist/doctor. Har clinical line source se VERIFY.</p>
<table><tr><th>#</th><th>Title</th><th>Status</th></tr>""")
for i,(oi,t,ev,st) in enumerate(R,1):
    h.append(f"<tr><td>R{i}</td><td>{esc(t)}</td><td>{esc(st)}</td></tr>")
h.append("</table><h2>6. Har video: evidence, thumbnail, script</h2>")
for i,(oi,t,ev,st) in enumerate(R,1):
    _,topic,_,th,hook,body,close,srcs=OLD[oi]
    h.append(f'<div class="v"><h3><span class="tag">R{i}</span>{esc(t)}</h3>'
      f'<p><span class="k">Status:</span> {esc(st)}</p><p><span class="k">Test evidence:</span> {esc(ev)}</p>'
      f'<p><span class="k">Thumbnail:</span> {esc(th)} (asli presenter ka chehra, cartoon nahi)</p>'
      f'<p><span class="k">Script, hook (0-30s):</span> &ldquo;{esc(hook)}&rdquo;</p>'
      f'<p><span class="k">Script, beech:</span> {esc(body)}</p>'
      f'<p><span class="k">Script, akhir:</span> {esc(close)}</p>'
      f'<p class="small"><b>Sources (VERIFY, fetch nahi):</b> {esc(srcs)}</p></div>')
h.append("""<h2>7. Thumbnail system</h2>
<ul><li>Asli presenter ka chehra + 2&ndash;4 lafz, bara font; cream background, teal (#0f4c5c), ek laal accent; ek jaisa "AGING | PILL" split.</li>
<li>Clone-pattern se alag: search results mein AI-cartoon dadi/dada, "DANGEROUS / WARNING" laal-peele text bhare hain; hum ye nahi karte.</li>
<li>Har video ke 2 variants (A/B).</li></ul>
<h2>8. 30-day plan (sirf 5 long + Shorts)</h2>
<p>Pehle 4&ndash;5 videos launch group (R1&ndash;R5); baqi decision point 1 ke baad. Shorts hamesha alag original sawal, long video ka clip dobara upload nahi (Oct 2026 Shorts originality report, secondary source).</p>
<table><tr><th>Din</th><th>Kaam</th><th>Output</th></tr>""")
for d,t,o in plan2: h.append(f"<tr><td>{d}</td><td>{esc(t)}</td><td>{esc(o)}</td></tr>")
h.append("""</table>
<h2>9. Platform context aur UNKNOWN</h2>
<ul><li>DS-000018 se validated: ranking har viewer/surface ke liye alag; subscribe se dikhna zaroori nahi; templated episodes par monetization risk (varied format theek). Baqi claims unvalidated.</li>
<li>Jul 2026 policy aur Oct 2026 Shorts report secondary sources se hain (Tubefilter, OutlierKit, TheDesk); official YouTube page check nahi hua. Health topics par AI persona monetize nahi hone ka claim isi category mein hai: asli insaan presenter rakhein.</li>
<li><b>UNKNOWN:</b> CTR, retention, traffic source, monetization; 60+ ke liye alag Trends; Studio/vidIQ; kya dusre log yahi angle abhi bana rahe hain; presenter/partner; channel naam availability; saari clinical lines (pharmacist review lazmi).</li>
<li>Test ek din ka snapshot hai (14 Nov 2026). Launch se pehle dobara chalayein.</li></ul>
<p class="small">Basis: ghalat nikle v1 claims ki list: (a) "dawai-wajah angle naya" ghalat; (b) "After 60" suffix faida deta hai: ghalat/unproven; (c) swollen ankles ko Nov&ndash;Feb mein rakhna ghalat (seasonal).</p>
</body></html>""")
open("NEW_CHANNEL_BLUEPRINT_v2.html","w").write("".join(h))
