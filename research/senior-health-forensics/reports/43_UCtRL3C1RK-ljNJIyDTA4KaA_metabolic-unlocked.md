# 43 — Metabolic Unlocked (UCtRL3C1RK-ljNJIyDTA4KaA, @MetabolicUnlockedTV) — STATUS: PARTIAL
Checked 2026-11-14. Sources: senior_health_complete.db (tier 2: Apify 2026-11-11; 12/12 transcripts), curl of 11 watch pages (status, views, likes; 11/11 HTTP 200, no Google block), 6 hqdefault thumbnails, `script_reuse.py`, `title_families.csv`. Chrome channel page opened (title "Metabolic Unlocked - YouTube") but header text came back empty — subs/video count live = UNKNOWN.

## A. Seedha jawab (Roman Urdu)
1. **Kis ke liye / promise:** 60+ seniors: qabz, baal safed hona, sarcopenia, visceral fat, creatinine/kidney, magnesium, peanut butter/chia, nahane ki frequency. Promise: "doctor-style" 12–21 min explainer jo "jo aap ko kabhi nahi bataya gaya" frame karta hai. Naya channel: 12 videos 2026-10-24 → 11-10 (4.9/hafta). Titles/transcripts mein **"Dr. Jason Fung"** naam (12 mein se 7 titles mein "| Dr. Jason Fung"); transcript: "I am Dr. Jason Fung". Yeh ek **asli, mashhoor doctor ka naam** hai; is channel ka unse taalluq maine verify nahi kiya — UNVERIFIED (neeche B).
2. **Kya repeat hota hai:** (a) Title: "… After 60", "SENIORS!", "THIS 1 Vitamin…", "| Dr. Jason Fung" suffix. (b) Thumbnail (6/6 dekhe): ek hi **chashma lagaya Asian mard presenter** (neeli shirt/scrubs), ungli se ishara, peela/laal bold claim-text ("POOP IN SECONDS!", "30X BETTER!", "10X MORE COLLAGEN … EVEN AT 90!", "ZERO PERCENT VISCERAL FAT INSTANTLY"), ek tile par "DR. JASON FUNG" caption. (c) Opening: "Stop right there / Stop believing / Stop dyeing…" 8/11 padhe hue openings "Stop" se shuru. (d) Ending: "Let me know in the comments… I read every comment… see you in the next video." **Concentration (DB):** total 41,428; top-1 86% (`xCh_vhbyf-w`), top-3 98%, median 88; baaki 9 videos 36–260 views.
3. **Winner vs weaker (matched):** `xCh_vhbyf-w` (2026-11-02, 18:04, **38,052 live**, 480 likes) "Constipation Relief: Stool Stuck in the Rectum? A Surgeon Explains What Helps" vs `3PcWX193d7o` (2026-11-01, 13:57, **263 live**, 4 likes) "How Often Should Seniors Take a Bath After 70? 7 Shocking Facts…" — 1 din ka farq, wahi presenter-face thumbnail style, **~145x**. Fark jo dikhta hai: winner = ek takleef-wala, sharmindagi wala, sawal-jaisa search topic ("stool stuck") + "A Surgeon Explains" (title mein Fung naam nahi); weaker = low-intent "bath after 70" topic. **Sab se plausible wajah (low confidence):** topic ki pehle se maujood demand; Trends nahi chalaya, traffic source UNKNOWN. Counterexample: `68FQ1zWFp7M` (hair dye + vitamin, "| Dr. Jason Fung" title) 4,075 — doosra, 9x kam; Fung naam akela traffic nahi laata (winner mein title mein naam hi nahi).
4. **Topic source / demand / competitor:** Winner ka topic (qabz) dusre channels par bhi top performer: ch 44 `Y6ntdtEI2aM` (qabz, 2,886 live) aur report 41 mein bhi stool/qabz titles hain — **qabz is batch mein 2 channels par upar dikha** (DB, low; sirf 2 data points). Title families: 3 titles dusre channels se milte (nahi-copy-direction known): bath (n=7: ch04 2026-08-22 506,628 → … → ch43 2026-11-01 260 → ch36 11-07 641), peanut butter (n=14: ch32 2026-10-17 1,130,985 → … → ch43 10-29 60), castor oil (n=96→2 members: ch10 2026-09-25 4,903 → ch43 11-07 49). **Teeno copies sab se kam views waale hain** is channel ke; winner (qabz) ka family nahi mila. Copy direction/ownership: Not known (DB `published` order only).
5. **Playbook rule:** Outlier concept (Playbook p.6–8, Module 2.1): ek outlier 86% share, 405x median — baaki 11 flat; ek hi data point, 17 din ka channel → confidence low. Title Formats (p.52–53): "… After 60" suffix 10+ titles mein hai magar sirf 1 outlier; format akela nahi chalta. Against the rule: "THIS 1 Vitamin" jaisa curiosity-gap title 4,075 par tha, constipation "Surgeon Explains" 38K par.
6. **Kya banayein (original):** "Qabz (constipation) after 60: 5 cheezein jo sach mein madad karti hain aur kab doctor se milna hai" — apni script, apne naam wala asli clinician. Thumbnail: clinician + ek simple "kab doctor?" label, bina "POOP IN SECONDS" ya doosre ke naam ke. First 30s: roz ka sawal ("kitne din se pet saaf nahi?") apne alfaaz mein; payoff = fiber/psyllium/hydration/footstool + red-flag (khoon, wazan girna). Clinical source jo verify karna hai (fetch NAHI kiya): ACG/AGA chronic constipation guideline aur NIDDK constipation page — video se pehle verify.

## B. Persona / claims / monetization
- **Fact:** transcript + titles mein "Dr. Jason Fung" / "Dr Jason Fung". Thumbnails mein ek presenter ka chehra (sab ek jaisa); koi licence/clinic detail nahi. **Maine verify nahi kiya** ki yeh channel ya presenter asli Dr. Jason Fung se judaa hai; asli Fung ka kaam/naam is channel ke saath link hona UNVERIFIED. **Interpretation (low):** ek asli doctor ka naam bina evidence ke use ho raha ho sakta hai (impersonation risk) — ghalat ya sahi dono mumkin; copy NAHI karna, kisi asli doctor ka naam use nahi karna.
- **Fact (thumbnails vs transcript):** "30X BETTER", "10X MORE COLLAGEN… EVEN AT 90", "ZERO PERCENT VISCERAL FAT INSTANTLY", "1,000,000X Better" (title) — numeric/instant claims; transcripts ka tone zyada hedged (maine sirf open/end padha). **Interpretation:** thumbnail/title claim-inflation; health-misinformation risk.
- Fact: `c1QNaM9xi_U` ka opening ek "real case report" (chia seed blockage) cite karta hai — source maine verify nahi kiya.
- Description links / Gumroad / AI-disclosure: curl se parse nahi kiye — UNKNOWN. Monetization UNKNOWN.

## C. Script reuse — `script_reuse.py 43`
0/12 scripts ≥0.85 (max 0.02; best matches ch 08, 09, 13, 21 etc., sab ≤0.02). Scripts original; titles ka overlap alag (family check upar).

## D. Live vs snapshot
- Header live: UNKNOWN (page text empty). DB: 12 videos, 447 subs, "Sep 9, 2026" joined.
- Views (11 curl, 2026-11-14): `xCh_vhbyf-w` 35,469 → 38,052; `68FQ1zWFp7M` 4,049 → 4,075; `C1sGRvZDDaY` 1,031 → 1,036; baaki ±3–15. Sab OK.

## E. Coverage
| Layer | Status |
|---|---|
| DB titles/views/dates/durations | 12/12 |
| Transcripts | 12/12 (open/end 11 read) |
| Live channel header | NO (empty text) |
| Live watch metadata (curl) | 11 of 12 |
| Thumbnails | 6 of 12 |
| Playback / comments / vidIQ / Trends | NOT done |
| Credentials / Fung identity | NOT verified |
Pending IDs: `qTx4gFmgGpI` watch page; 6 thumbnails; playback + comments.

## F. Evidence ledger
| Claim | Evidence | Conf |
|---|---|---|
| xCh_vhbyf-w 38,052 live views | curl 2026-11-14 | high |
| 3PcWX193d7o 263 views | curl + DB | high |
| top-1 86%, top-3 98%, 41,428 total | DB snapshot | medium |
| 3 titles in families (bath, peanut butter, castor oil) | title_families.csv | high |
| 0/12 scripts ≥0.85 | script_reuse.py | high |
| "Dr. Jason Fung" in titles/transcript | DB titles + transcript text | high |
| Link to real Dr. Fung | not checked | UNKNOWN |
| Why constipation video won | interpretation | low |
