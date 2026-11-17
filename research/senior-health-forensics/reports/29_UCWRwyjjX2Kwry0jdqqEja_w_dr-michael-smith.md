# 29 — DR.MICHAEL SMITH (UCWRwyjjX2Kwry0jdqqEja_w, @dr_michael_smith-e5x) — STATUS: PARTIAL
Checked 2026-11-14. Sources: senior_health_complete.db (tier 2: Apify complete catalog; 8 videos; 8/8 transcripts), live channel page in built-in Chrome (header only; grid did not render), curl of all 8 watch pages (status, views, likes, publish date, description) and of the channel page, 6 hqdefault thumbnails viewed, `script_reuse.py`, `title_families.csv`, cross-DB title query.

## A. Seedha jawab (Roman Urdu)
1. **Kis ke liye / promise:** 50–70+ seniors jo dil/BP/cholesterol aur rozmarra ki dawaiyon se pareshan hain: BP ki dawaiyon ka chhupa side effect, chakkar, taango ki soojan, qabz, restless legs. Promise: "ek doctor jo aap ki dawai/symptom ka chhupa sabab batata hai". Channel bio: "Senior heart health, blood pressure, and cholesterol after 50." Bilkul naya: joined 2026-10-11, 8 videos 2026-10-17 → 11-11 (2.2/hafta); **header "8 videos", 134 subs**.
2. **Kya repeat hota hai:** (a) Title: "<symptom> After 60: 5 Hidden Causes/Warning Signs", "(Medications Are #1)", "Doctor Explains!". (b) Thumbnail: kaala background, bold peela/safed text + laal label, **cartoon/illustrated bujurg** (ek hi style) — "AMLODIPINE? LISINOPRIL? METOPROLOL?", "DIZZY SPELLS? CAUSE #1 YOUR PILLS". (c) Opening: **manzar jo darshak ke jism mein ho raha hai** ("You get up from the couch… the room tilts", "You take off your shoes and the sock leaves a deep groove"), ya dawai ke naam ("one of these three names is printed on a bottle in your home"). (d) Ending: "tell me in the comments which cause surprised you most" + **"This video is for education and doesn't replace advice from your own healthcare professional."** (e) Description: guideline ka naam ("Based on the 2019 ACR/Arthritis Foundation osteoarthritis guideline"). **Concentration (live, 8 videos, ~26.2K views):** top-1 96% (`k60S_3aPZN0` 25,104); baaki 7 ka median ~162.
3. **Winner vs weaker (matched):** `k60S_3aPZN0` (2026-10-28, 16:04, **25,104 views**, 257 likes) "Amlodipine, Lisinopril, Metoprolol After 60: The Side Effect Everyone Misses" vs `Mrni_nGORjM` (2026-10-20, 14:05, **314 views**, 7 likes) "Dizzy When You Stand Up? 5 Hidden Causes After 60 (Medications Are #1)" — same channel, 8 din ka farq, same thumbnail template, **80x**. Thumbnails: winner sirf **3 dawai ke naam** + chinta karta hua bujurg; weak "DIZZY SPELLS? CAUSE #1 YOUR PILLS" (symptom-first). Opening: winner = dawai ka naam jo ghar mein hai (specific); weak = symptom ka manzar. Jo farq dikhta hai: **dawai ke naam (searchable brand/drug query) vs generic symptom**; plausible (interpretation, low): "amlodipine/lisinopril/metoprolol" jaise naam search/suggested mein alag audience se match karte hain — **testable nahi** (traffic source UNKNOWN; channel sirf 134 subs par 25K views — audience subs se nahi). Counterexample: isi channel ke "Medications Are #1" wale weak video (314) mein bhi "pills" hai, aur DB mein **"Amlodipine" title ka cluster doosre channels par ek jaisa nahi chala:** `6jLS5B7_9FU` (UCPjG4ZR…, 2026-06-01) 179,476, `744OX9u30y4` (2026-06-05) 94,069, `_dt5OX_1fx8` (UCXZi5JV…, 2026-06-12) 47,032, `F3phhk_savo` 1,748, `RDirpuzBNZk` 5,181 aur 5+ aur ~160–190 par — yaani naam akela nahi, channel/timing zaroori. Confidence: low.
4. **Topic source / demand:** **BP medicines (amlodipine/losartan/lisinopril/metoprolol) ka side effect/"doctors won't tell you"** cluster DB mein kai channels par: 179K, 94K, 47K (teen bade) aur ek darjan ≤5K — demand real, par har copy nahi chalti (is channel ka 25K, medium). Baaki is channel ke topics (chakkar, soojan, qabz, restless legs, sleeping posture) 13–314 views — koi cross-validation nahi. Google Trends nahi chalaya (UNKNOWN). Competitor example: `6jLS5B7_9FU` (179,476, 2026-06-01).
5. **Playbook rule:** Outlier concept (Playbook p.6–8, Module 2.1): top-1 131x median par 8-video channel — rule nahi, sirf hypothesis; cross-validation sirf cross-channel dawai-cluster se (3 bade + bohat chhote) → medium-low. Script Audit (Playbook p.353): har video mein **named guideline/data** (ACR guideline, "33 out of 100 adults…") aur har video ke end mein disclaimer — yeh evidence-discipline ka acha example hai. Against: wahi evidence-discipline wale 7 videos ≤314 views par.
6. **Kya banayein (original idea, evidence-gated):** BP dawaiyon par apna angle jo dawai band karne ko na kahe: "Blood Pressure Pills After 60: 3 Side Effects to Report to Your Doctor (Never Stop Them on Your Own)". Thumbnail: asli pharmacist/cardiologist + 3 icons, koi "doctors won't tell you". First 30s: "Aap ki goliyon ke dabbe par ye naam hain? Ye 3 symptoms note karein aur doctor ko batayein", payoff = symptom checklist + "kab turant call karein". Clinical source jo verify karna hai (yahan fetch NAHI kiya): ACC/AHA hypertension guideline aur har dawai-class ke prescribing information (FDA label) ke side-effect sections; video se pehle verify karein.

## B. Persona / claims (facts vs interpretation)
- **Fact:** channel naam "DR.MICHAEL SMITH"; titles mein "Doctor Explains!", "I'd NEVER Do" (pehla-shakhs); transcripts mein presenter ka koi naam/credential/specialty nahi — **kisi doctor ki identity/licence UNVERIFIED**; presenter ka chehra thumbnails par sirf illustrated cartoon; awaaz/video maine nahi dekhi/suni (playback nahi hua). Is naam ka ek aur "Dr. Michael Smith" channel (report 04 mein "Dr. Eric Smith", report 09 "Dr. Michael Carter") ki shakl mein persona-naam pattern dikhta hai — **interpretation (low)**, ownership/connection UNKNOWN.
- **Fact:** descriptions mein "Educational only", "doesn't replace advice from your own healthcare professional"; `tvxW7iqcAmE` ka description khali. AI-disclosure descriptions mein nahi dekha. **Monetization:** koi shop/affiliate link nahi dekha (8 descriptions manual scan) — UNKNOWN.
- **Fact (claims):** `EEeV7YguP44` title "The 60-Second Trick That Stops Joint Pain Instantly" par description ka jawab "Honestly, no" — **title/thumbnail ("FIX YOUR JOINT PAIN INSTANTLY IN 60 SECOND") aur description/content mein tanaza**; (clickbait-vs-content gap, fact). Cited guideline maine fetch nahi ki (UNVERIFIED).
- **Fact:** script reuse vs doosre channels max ≈0.02 (0/8 ≥0.85); `k60S_3aPZN0` aur `cfP4RVGtx3Q` (channel 44) ka best match 0.02 — alag script.

## C. Live vs snapshot
- Live 2026-11-14: header **"8 videos", 134 subs**; DB 8 videos, 123 subs. 8/8 saved IDs playable (curl OK); publish dates 2026-10-17 → 2026-11-10. IDs matched (8/8).
- Views DB → live: `k60S_3aPZN0` 22,457 → 25,104 (+12%, 2 hafte mein); `Mrni_nGORjM` 255 → 314; `EEeV7YguP44` 13 → 22.

## D. Coverage
| Layer | Status |
|---|---|
| Catalog titles/views/dates/durations (DB) | 8/8 |
| Playability / publish date / views / likes (curl 8) | 8/8 |
| Transcripts | 8/8; open/end read for 5 |
| Live channel header (Chrome) | yes (grid not rendered) |
| Thumbnails | 6 of 8 |
| Chrome playback / comments | NOT done / NOT read (DB comment counts: 20 on `k60S_3aPZN0`) |
| vidIQ / Trends | not run |
| Credentials / claims | NOT verified |
Pending IDs: playback + comments for all 8; 2 thumbnails.

## E. Evidence ledger
| Claim | Evidence | Conf |
|---|---|---|
| k60S_3aPZN0 25,104 vs Mrni_nGORjM 314 | curl watch pages 2026-11-14 | high |
| 134 subs, "8 videos" | Chrome header | high |
| BP-medicine title cluster: 179K / 94K / 47K + many ≤5K | DB title query | high (DB views) |
| Script reuse max 0.02 | script_reuse.py | high |
| "60-second trick" title vs "Honestly, no" description | curl description | high |
| Credentials of "Dr. Michael Smith" | none in any source | unknown |
| Why drug-names video beat symptom video | interpretation | low |
