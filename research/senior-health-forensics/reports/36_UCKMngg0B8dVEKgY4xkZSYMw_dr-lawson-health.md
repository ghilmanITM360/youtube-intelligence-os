# 36 — Dr. Lawson Health (UCKMngg0B8dVEKgY4xkZSYMw, @Dr.LawsonHealth-Tv) — STATUS: PARTIAL
Checked 2026-11-14. Sources: senior_health_complete.db (tier 2: Apify 2026-11-11; 27/27 transcripts), curl of 12 watch pages (status, views, likes, description), built-in Chrome channel header, 6 hqdefault thumbnails (current versions), `script_reuse.py`, `title_families.csv`.

## A. Seedha jawab (Roman Urdu)
1. **Kis ke liye / promise:** 60–70+ seniors jo dawai (BP), neuropathy, sugar, qabz, thyroid, jhurriyan/pet, aankh jaisi mukhtalif masail dhoondte hain. Promise: "ye ek cheez/exercise/dawai ki baat jo doctor nahi batate" — 15–25 min explainer. **Koi ek niche nahi** (27 videos, ~15 topic clusters). Naya channel: joined Oct 8 2026, 27 videos 2026-10-11 → 11-11 (6.1/hafta), live 792 subs. Presenter ka naam transcripts/descriptions mein dekha nahi (channel naam "Dr. Lawson Health").
2. **Kya repeat hota hai:** (a) Do title styles: ALL-CAPS dash style ("YELLOW TOENAIL ISN'T ALWAYS FUNGUS — …") aur shared-family titles ("Cardiologist Warns…", "NEVER REHEAT…", "How Often Should Seniors Take a Shower…"). (b) Thumbnail: kaala background, peela/safed/laal text, cartoon bujurg (6/6 dekhe). (c) Opening: "Imagine finding out that…" / "Most blood pressure pills come with one sentence…". (d) Descriptions: **0/12 mein koi link (source ya product)**. **Concentration (DB, 27 videos, 109,837 views):** top-1 76% (`CvXavlG9eQI`), top-3 86%, median 422.
3. **Winner vs weaker (matched, same channel, same topic cluster):** `CvXavlG9eQI` (2026-10-31, 23:32, **84,715 live views**, 7,220 likes) "Taking Amlodipine, Losartan, or Lisinopril for Blood Pressure? Here's What Most Seniors Don't Know!" vs `qgAluc5jPps` (2026-10-14, 21:32, **1,414 DB views**) "5 Important Things to Avoid If You Are Taking Amlodipine Now!" — dono amlodipine/BP-dawai topic, 17 din ka farq, ~60x. Farq jo dikhta hai: winner 3 dawaiyon (Amlodipine, Losartan, Lisinopril) ke naam + "Most Seniors Don't Know"; thumbnail "MUST READ! CRITICAL FINDINGS… SIDE EFFECTS & INTERACTIONS INSIDE!" dawai ki bottles ke saath (cartoon bujurg nahi — is channel ke baaki template se alag); opening "one sentence of explanation… leaves out almost everything that matters" (calm, medication-specific). Weaker ki opening/thumbnail maine nahi dekhi. **Script winner ki dusre channel (33) ki `wjqxdytTdtY` se verbatim match (Jaccard 1.00)** — neeche C. Sab se plausible wajah: teen mashhoor dawaiyon ke naam par search-style demand; **traffic source UNKNOWN**. Counterexample: isi script ka doosra copy (ch 33 `wjqxdytTdtY`) 10,039 par — yaani same script 8x kam; aur `_ydSrr3g35Y` ("6 Golden Habits", 2,327) jaisa generic title bhi 2K+ par. Confidence: low.
4. **Topic source / demand:** BP-medication topic: sirf 2 channels (36 aur 33) ka data, dono ek hi script — independent validation NAHI. Baaki top clusters: eggs 6,673; neuropathy 4,400 aur 455 (same topic, 9x farq); reheat/pancreatic cancer 3,138. Neuropathy dono channels ke liye mashhoor-sa lagta hai (title `soUSW0wQOGM` ka family ch UC6VFF… 2026-03-10 se purana) par yahan sirf ek bada. Google Trends nahi chalaya (UNKNOWN). Competitor example: ch 33 `wjqxdytTdtY` (10,039 live).
5. **Playbook rule:** Outlier concept (Playbook p.6–8, Module 2.1): 76% ek outlier = 198x median — rule banane ke liye cross-validation nahi (copy, independent nahi, AGENTS rule 9). Title Formats (Playbook p.52–53): "specific object (3 dawaiyon ke naam) + curiosity gap" format yahan outlier hai; against: usi channel ka `qgAluc5jPps` "Amlodipine" naam wala title sirf 1,414.
6. **Kya banayein (original idea, evidence-gated):** "Amlodipine, Lisinopril or Losartan: What Each Actually Does and the Questions to Ask Your Doctor" — apni script, bina "poison/dangerous" ke. Thumbnail: asli clinician/pharmacist + 3 dawai ke naam + "3 sawal". First 30s: "Aap ka BP dawai kaise kaam karta hai — teen raaste, teen alag side effects", payoff = har dawai ka ek-line farq + doctor se poochne ke 3 sawal ("kabhi dawai khud band na karein"). Clinical source jo verify karna hai (yahan fetch NAHI kiya): hypertension guideline (ACC/AHA ya ESC) aur ACE-inhibitor/ARB/CCB ke common adverse effects ka drug-label/review.

## B. Persona / claims / engagement anomaly (facts vs interpretation)
- **Fact:** 0/12 sampled descriptions mein koi source ya product link; AI-disclosure nahi. Presenter ka naam/credentials UNVERIFIED (transcripts mein name nahi dekha).
- **Fact:** thumbnails/titles mein "EGG TURNS INTO POISON", "DOES IT CAUSE PANCREATIC CANCER?", "TINNITUS DISAPPEARS… FOREVER", "ONE SIMPLE MOVE… DROP BLOOD SUGAR BY 52%" — transcript hedged ("Some of the concern is solid food safety science"; "Never change or stop a medication without professional guidance") — **interpretation:** thumbnail/title text script se zyada extreme.
- **Fact (anomaly):** chhote videos par likes views ke muqabil bahut zyada: `ar67enMl0g0` 446 views / 120 likes, `ypa8YkYs0JM` **16 views / 96 likes**, `QD5oHH1Gzgo` 426 / 130, `soUSW0wQOGM` 455 / 125; winner par 8.5% (7,220/84,715). **Wajah Not known** (organic ho sakta hai, view-count lag ho sakta hai, ya aur) — kisi source se saabit nahi; sirf observation. 0-view video `yve-TxAoOgg` ka live 21.

## C. Script reuse (fact) — `script_reuse.py 36`
1/27 ≥0.85: `CvXavlG9eQI` ≡ ch 33 `wjqxdytTdtY` (Jaccard 1.00). **Order (DB `published`):** ch 36 2026-10-31 → ch 33 2026-11-04 (ch 36 pehle). Copy direction/ownership Not known. Baaki 26 scripts mein koi ≥0.85 match nahi (max 0.08) — scripts mostly original ya alag-alag source (kai ch UCrz5nlYL41… se halka overlap).

## D. Live vs snapshot
- Live 2026-11-14: header **29 videos, 792 subs** (/videos grid render nahi hua); DB: 27 videos, 781 subs. 11/12 curl IDs playable (sab 12 OK). 2 extra videos ke ID UNKNOWN.
- Views: `CvXavlG9eQI` 83,515 → 84,715; `QHb7PZdRcT4` 4,124 → 4,400; `soUSW0wQOGM` 413 → 455; `nWoHmn-fft0` 19 → 21.

## E. Coverage
| Layer | Status |
|---|---|
| Catalog titles/views/dates/durations (DB) | 27/27 |
| Transcripts | 27/27 (open/end of 11 read; script reuse over all 27) |
| Live channel header | yes (grid not rendered) |
| Live watch metadata (curl) | 12 of 27 |
| Thumbnails | 6 of 20 |
| Chrome playback / comments | NOT done / NOT read |
| vidIQ / Trends | not run |
| Credentials | NOT verified |
Pending IDs: 2 unseen header videos; remaining 15 watch pages; 14 thumbnails; playback + comments.

## F. Evidence ledger
| Claim | Evidence | Conf |
|---|---|---|
| CvXavlG9eQI 84,715 views, 7,220 likes | curl 2026-11-14 | high |
| Script ≡ ch 33 `wjqxdytTdtY` (1.00); ch 36 earlier by DB date | script_reuse.py + DB published | high (data); direction unknown |
| Top-1 76%, top-3 86%, 109,837 total | DB | high |
| Header 29 vs DB 27 | Chrome header | high (cause UNKNOWN) |
| Small videos' likes ≫ views ratio | curl | high (observation); cause UNKNOWN |
| 0/12 descriptions with links | curl | high |
| Why BP video won | interpretation | low |
