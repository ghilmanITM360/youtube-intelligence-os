# REPORT 4 — Dr Rehan Channel Recovery Plan (30/60/90 din)

- **Date:** 2026-11-11
- **Input:** Report 3 Issue Register (R-01…R-15) aur Report 2 v2.
- **Frameworks:**
  - DS-000031: CS-012 (70–80% proven / 20–30% experiments), CS-023 (No traffic / No click / No watch), CS-024 (ek waqt mein ek change), CS-015 (next viewer question).
  - Playbook topic validation; Packaging SOP (DS-000011).
  - Yeh sab creator heuristics hain, platform facts nahi.
- **Rules:**
  - Koi mass deletion ya mass editing nahi; koi purani video unlist/delete nahi.
  - Publish ya title ki har change Dr Rehan ki manzoori se hogi.
  - Views/subs ka koi wada nahi.

## 0. Priority logic
Score = usefulness × evidence strength ÷ (effort × risk).

| Rank | Action | Issues | Evidence | Effort | Risk |
|---|---|---|---|---|---|
| 1 | Studio export lena | R-05 | — (prerequisite) | Low | None |
| 2 | Pillar focus: "Decode your heart & metabolic numbers" | R-01, R-03 | Medium | Low | Low |
| 3 | 8–12 min structured explainer format | R-02, R-06 | High (gap), effect SUSPECTED | Medium | Low |
| 4 | Medical QA checklist + disclaimer | R-08, R-10 | Medium | Low | Reduces risk |
| 5 | Specific end-loops + end screens + playlists | R-07 | Low-Med | Low | Low |
| 6 | Shorts → long-form bridge | R-04, R-12 | Medium | Low | Low |
| 7 | Name/brand consistency | R-09, R-14 | High (observed) | Low | Low (naam change par alag faisla) |

---

## Days 1–30: Diagnose + fix the foundation
1. **Studio export** (Dr Rehan ya channel manager kare; Claude login nahi karega). Kya export karna hai:
   - Last 365 days ka Content tab, per video: Impressions, Impressions CTR, Views, Average view duration, Average percentage viewed.
   - Traffic source; Audience: age, geography, new vs returning; Shorts vs Videos split.
   - Isse YIOS ka file-based first-party ingestion (`READY_FOR_REAL_DATA`) chalaya ja sakta hai.
2. **CS-023 diagnosis** har LF video par:
   - Impressions bahut kam → **discovery/topic** ka masla.
   - Impressions theek magar CTR kam → **packaging** ka masla.
   - CTR theek magar APV kam → **script/promise** ka masla.
   - Iske baad hi R-02/R-11 ki wajoohat confirm hongi.
3. **Medical QA checklist** (har nayi video, publish se pehle):
   - (a) Har claim ka source (guideline/society/peer-reviewed) notes mein ho.
   - (b) Koi absolute claim na ho ("never stop", "cure", "reverse").
   - (c) Dawai band ya shuru karne ki baat sirf "apne doctor se baat karein" ke saath ho.
   - (d) Emergency symptoms par "call emergency services" ho.
   - (e) Verbal + description disclaimer ho.
   - (f) Title ka promise video mein poora ho.
4. **Purani videos (optimize, delete nahi):**
   - Report 3 ke 4 flagged statements (`sUL6SU8LnEg`, `tf7f4RhQwtc`, `RD7ugxaBHSQ`, `8JdBlF-ragM`) par Dr Rehan khud review karein.
   - Fix ke options: pinned comment ya description mein correction/qualification. Re-edit sirf zaroorat par.
5. **Packaging cleanup (low-risk):**
   - Shorts titles se hashtags description mein le jayein.
   - Naam ki ek spelling (Omer/Omar) har jagah use karein.
   - Top 5 videos par end screens aur playlists lagayein: "Heart tests explained", "Heart warning signs after 60".
6. **Pehli 4 nayi long-form videos (proven pillar, 8–12 min):**
   - Lp(a) ki success par follow-ups:
     - "Coronary calcium score: 0, 1–99, 100+ ka matlab"
     - "HbA1c vs fasting sugar: kaunsa number zyada batata hai"
     - "Kidney report: eGFR aur urine albumin (UACR) kaise parhein"
     - "ECG report ki 5 lines jo mareez poochte hain"
   - Script spine:
     - question hook (number/test ke saath)
     - yeh test kya naapta hai
     - ranges
     - 3 common misreadings
     - kab doctor ko dikhayein
     - doctor se poochhne ke 3 sawal
     - specific next video

## Days 31–60: Test packaging + format, one variable at a time
1. **Titles:** Studio ke CTR ke mutabiq. Sirf woh videos jinke impressions theek hain magar CTR kam hai, unke titles ek-ek karke badlein. YouTube "Test & compare" (agar channel par available ho — NOT VERIFIED) thumbnails ke liye.
   - Title pattern options (HYPOTHESIS):
     - "[Test] Explained: What Your Number Really Means After 50"
     - "Your [Test] Is Normal — So Why Did Your Doctor Order Another?"
     - "[Number] on Your Report? A Cardiologist Explains"
2. **Thumbnails:** pehle audit (images dekhna — ijazat chahiye). Phir ek variable test karein: report-paper close-up + number vs face + text.
3. **Length experiment:** 8–12 min vs 4–6 min (2–3 videos each, same pillar). Metric: AVD, APV, aur subs per 1k views.
4. **Shorts bridge:** har LF se 2 Shorts banayein (ek number/myth), jo related video se linked hon. Naye standalone Shorts topics band karein.
5. **Experiments budget (CS-012):**
   - 70–80% "numbers/tests" pillar.
   - 20–30% experiments: heart symptoms after 60 (swollen ankles 171, cold feet 148 — moderate signal), medication-safety (aspirin 97, competitor demand: BHWA 665k).

## Days 61–90: Double down or pivot (data-led)
1. Agar numbers-series ka LF median 2 cycles mein baseline (73) se wazeh oopar ho → series ko barhayein: BNP, troponin, echo EF, Holter, ABPM, ankle-brachial index.
2. Agar impressions hi kam rahein → topic demand dekhein. Search-type titles try karein (`explainer_colon` style, Report 2 E) aur playlists/search ke liye description optimize karein.
3. Channel name: "Decode Your Heart" numbers-pillar ke saath fit hai. **Naam change ki recommendation nahi**, sirf "— Dr. Rehan Omer, Cardiologist" consistency.
4. Monthly review: Studio export ko YIOS ingestion mein dalein; Issue Register update karein.

## KPI tracking (official YouTube Analytics metrics; Help Center 9717005, fetched 2026-11-11)
| Layer | KPI | Source | Baseline |
|---|---|---|---|
| Discovery | Impressions per video (first 28 days), traffic source mix | Studio Reach | NOT VERIFIED (export pending) |
| Packaging | Impressions CTR | Studio Reach | NOT VERIFIED |
| Watch | Average view duration, Average percentage viewed, retention at 30 s | Studio Engagement / retention report | NOT VERIFIED |
| Loyalty | Returning viewers, subs per 1k views | Studio Audience | 55 subs total (OBSERVED) |
| Output | LF/week, pillar share, QA checklist pass % | Internal | LF ~3/month (OBSERVED) |
| Public proxy | LF median views per 4 videos | Public metadata | **73.5** (OBSERVED) |

## Kya nahi karna
- Purani videos ko mass-delete ya unlist nahi karna.
- Network-style sensational titles nahi lagane: koi evidence nahi ke Rehan ke liye chalein, aur policy risk hai.
- AI-generated persona ya voice nahi use karna. Asli doctor hi channel ki USP hai.
