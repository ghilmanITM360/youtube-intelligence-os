# Dr Rehan: Winning Models (Titles, Scripts, Thumbnails) aur Google Fact Recheck

- **Date:** 2026-11-16
- **Labels:** OBSERVED · INFERRED · HYPOTHESIS · NOT VERIFIED
- **Kis kaam ke liye:** [06-DR-REHAN-TALKING-CARDS.md](06-DR-REHAN-TALKING-CARDS.md) ke titles, talking points aur thumbnail prompts isi file par mabni hain.
- **Codex ka agla kaam:** [07-CODEX-BRIEF-2-SCRIPT-RESEARCH.md](07-CODEX-BRIEF-2-SCRIPT-RESEARCH.md).
- **Statin video:** online hai, is liye yahan uski long-form shamil nahi. Uske Shorts ki baat 06 ke Part C mein hai.
- **Update (Codex brief 2):** F1–F20 ke final verdicts aur primary-source wording [08-CODEX-SCRIPT-RESEARCH-RESULTS.md](08-CODEX-SCRIPT-RESEARCH-RESULTS.md) §B mein hain. Neeche ki table ke "SECONDARY-OK" status us se superseded hain. Teen numbers correct hue:
  - F2: DiPietro ka faida 3-hour post-dinner glucose par tha, 24 ghante par nahi.
  - F12: 90 din mein "up to 17.8%" hai, "1 in 5" nahi.
  - F17: US estimate ~21% silent hai.
- [06 cards](06-DR-REHAN-TALKING-CARDS.md) v2 mein yeh corrections shamil hain.

## 0. Sources
| Source | Kahan | Kya liya |
|---|---|---|
| 44-channel synthesis | `origin/research/senior-health-apify-2026-11-11` → `research/senior-health-forensics/SYNTHESIS_44_channels.md` | Strong patterns, failure patterns, clinician contrast |
| Thumbnail matrix summary | same branch → `research/senior-health-forensics/DR_REHAN_THUMBNAIL_PROMPTS.md` | 149 hand-coded thumbnails ke features |
| Report 2 (E, F, K.4) | `origin/research/senior-health-reports-2026-11-11` → `docs/research/senior-health-2026-11-11/REPORT-2-COMPETITOR-INTELLIGENCE.md` | 642 titles, 662 transcripts, 60 transcripts ki manual reading |
| Playbook extract §7–9 | same branch → `02a-playbook-framework-extract.md` | Script architecture aur hook rules (course guidance, platform fact nahi) |
| Transcript DBs | apify branch → `data/catalog/senior_health/senior_health_transcripts_{1,2,3}.db` | Final topics ke winners ke openings aur structure (is session mein parhe) |
| Codex pass 1 | [04-CODEX-VALIDATION-RESULTS.md](04-CODEX-VALIDATION-RESULTS.md), [03 CSV](03-topics-for-validation.csv) | Autocomplete, dominant channels, verified STREAM/FDA facts |
| Web search | Section 2 | 13 searches, 2026-11-16 |

---

## 1. Research 1: Senior-health niche ke winning models

### 1.1 Titles (OBSERVED, Report 2 §E: 642 mature long-form titles)
| Feature | Kitne titles mein | Median ratio (within-channel) |
|---|---|---|
| Explainer colon ("X: Y") | n=43 | **2.49**, lekin zyada tar BHWA ke search-style titles se aaya (confounded) |
| Sawal (question) | 18% | 1.19 |
| "Not what you think / real reason" | 8% | 1.09 |
| Warning / negative | 36% | 1.06 |
| Age marker ("after 60/65/70") | 42% | 1.05 |
| ALL-CAPS lafz | 34% | 0.95 |
| Length 50–70 characters | — | **1.21** (90+ chars: 0.85) |

**Kya follow karenge (INFERRED):**
1. Age marker har title mein ho ("After 60", "60+", "After 65"). Niche ki zabaan yahi hai.
2. Shakal: `Specific sawal ya situation + age : payoff`. Colon/question dono.
3. 50–70 characters.
4. Viewer ki search wali zabaan istemal karein. Codex autocomplete ke examples: "mini stroke symptoms", "ideal blood pressure after 65", "walking after eating blood sugar", "poor leg circulation", "silent heart attack symptoms".
5. Payoff sach ho, aur woh video ke andar poora ho.

**Kya nahi karenge:**
- "Cardiologist Warns", "SHOCKING", "INSTANTLY", "52%", "K*LLS" aur "300x". Clone network ke saturated templates hain, aur Rehan ka "Cardiologist Warns" title sirf 37 views laya.
- Title–promise mismatch. Report 2 K.4 ke examples: "sleeping position stroke" title par content asal mein sleep apnea ka tha.
- Report 2 ke mutabiq title features ka asar **low confidence** hai. Topic title se zyada aham hai (synthesis §3.4).

### 1.2 Scripts (OBSERVED + INFERRED)

**Winners kya karte hain** (Report 2 §F aur K.4, plus is session mein final topics ke winners ki transcript sampling):
| Pattern | Evidence |
|---|---|
| Lambi videos | Median ~3,100–3,300 words (15–25 min). Real-clinician BHWA 4,700–6,000 words |
| Listicle spine | ~5 list markers per video ("number two", "next") |
| 6 opening types | Scene ("You turned your head on the pillow this morning…", Waterling dizzy 458K) · Patient story ("Her children gave her a gift for her 67th birthday…", Ares checkups) · Stat ("Every 40 seconds…", Waterling stroke 2.19M) · "What if I told you" (Doctor Thomas) · Credential-first (BHWA) · Fear/insider (Hub) |
| Patient case beech mein | Waterling dizzy (25% par ek patient ki kahani). BHWA Tylenol/Advil: real patient story, phir "American Geriatrics Society recommends…" |
| Recap aur action aakhir mein | BHWA: "So to recap…". Waterling: "Bring that description to your next appointment…" |
| Re-hooks bohat kam | 0.25 per 1,000 words. Report 2 isse ek opportunity kehti hai (HYPOTHESIS) |
| Specific next video | Ending mein ek specific video ka naam, generic subscribe nahi |

**Sab se aham model, BHWA (Better Health While Aging):** asli named geriatrician jo **script nahi parhti**.
- Transcript mein "um", "I forget what it is" jaisi baatein hain. Yaani notes se baat karti hain.
- Phir bhi 665K (Tylenol/Advil) aur 3.58M (memory drugs) views hain.
- Spine: apna taaruf, topic, har dawa par "kya hai, kitni kaam karti hai, risk", ek asli patient ki kahani, guideline ka naam, aur recap.
- **INFERRED:** jo doctor script follow nahi karta, uske liye yeh saboot hai ke **talking points + apni kahani** wala format kaam kar sakta hai.

**Dr Rehan abhi kya karte hain (OBSERVED, apne transcripts):**
- Openings lecture style mein hain:
  - "Cardiovascular diseases are the number one causes of mortality in the world…" (`jLEp6jDsN3Q`)
  - "Hi, today I'm going to discuss a very very important topic…" (`3dRcNqiLHgY`)
  - "…so one should always be critically appraisal…" (`iltS1TPt4jo`)
- Jargon jaise "diaphoresis" aur "acute coronary syndrome" bina tarjume ke.
- Koi patient story nahi, koi recap nahi, aur ~150–535 words.

**Imandari wali baat:** Report 2 K.4 ke mutabiq ek channel apne hits aur flops dono mein **same opening** istemal karta hai. Opening type akela hit nahi banata. Topic aur packaging bara farq dalte hain. Isliye neeche ka structure **clarity aur trust** ke liye hai. Is se views barhenge, yeh HYPOTHESIS hai. Studio ka retention data aane par test hoga.

**Dr Rehan ka model, "Clinic Story"** (yeh 06 mein Dr ko samjhaya gaya hai):
1. Scene
2. Main kaun aur aap ko kya milega
3. Ek asli patient ki kahani, jiska anjaam abhi nahi batana
4. Ek seedhi misaal (analogy)
5. 3 points
6. Kab emergency hai
7. Kahani ka anjaam
8. Doctor se poochhne ke 3 sawal, aur agli specific video

Ab tak niche mein "composite patients" (Dorothy, 74) jaise **nakli** kirdaar hain. Dr Rehan ke **asli, gumnaam (anonymized)** patient isi format ko sacha bana dete hain. Yahi unka farq hai (HYPOTHESIS).

### 1.3 Thumbnails (OBSERVED, 149 hand-coded thumbnails, 2026-09-25 matrix)
| Feature | With | Without | Faisla |
|---|---|---|---|
| Bara number | 2.13 | 0.80 | Use karein |
| Jawab chhupa ho | 1.90 | 0.63 | Use karein |
| Jawab thumbnail par dikha ho | 0.47 | 1.76 | Kabhi nahi |
| Medical render / 3D | 1.76 | 1.00 | Use karein |
| Warning icon | 0.55 | 1.24 | Nahi |
| Dawai dikhayi ho | 0.87 | 1.27 | Nahi (goli/dibba thumbnail par nahi) |
| Bhara hua background | 0.91 | 1.16 | Nahi |
| Sketch/cartoon insaan | 0.38 | 1.10 | Nahi, asli photo |
| Asli chehra | ~1.1 | ~0.9–1.1 | Neutral. Trust ke liye rakhein |

**Caveat:** features channel templates ke saath confounded hain. Yeh direction hai, saboot nahi.

**Winning layout:** text left (peela/safaid), doctor right (camera ki taraf, halka muskurata), ek medical render, ek bara number ya 2–4 lafz ka sawal.

---

## 2. Research 2: Google par deep recheck (web search, 2026-11-16)

**Status ka matlab:**
- **SECONDARY-OK:** search mein bharosemand secondary sources ne baat confirm ki. Primary paper maine poora nahi parha, Codex primary kholega.
- **PRIMARY-OK:** Codex pass 1 ne primary source (NEJM/FDA) se verify kiya.
- **PARTLY:** baat sahi hai magar number ya wording mein farq hai.
- **NOT VERIFIED.**

| # | Claim jo cards mein hai | Status | Kaise bolna hai | Source |
|---|---|---|---|---|
| F1 | Meal ke baad walk: type 2 diabetes ke 41 adults (avg age 60). Itni hi total walking ke muqable mein meal ke baad walk se post-meal glucose ~12% kam | SECONDARY-OK | "In one trial, the same walking done after meals lowered after-meal sugar more than one walk a day." Number bolna ho to "about 12% in that study" | [PubMed 27747394](https://pubmed.ncbi.nlm.nih.gov/27747394/) · [Healthline](https://www.healthline.com/health-news/how-a-2-minute-walk-after-meals-can-help-lower-type-2-diabetes-risk) |
| F2 | Older adults (glucose intolerance ke risk wale, diabetes nahi): meal ke baad 3×15 min walk, subah ki ek 45 min walk se behtar 24h glucose | SECONDARY-OK (DiPietro 2013) | Population wazeh batayein | [News-Medical](https://www.news-medical.net/health/Walking-After-Meals-Small-Habit-Big-Metabolic-Gains.aspx) |
| F3 | Chhoti light walks bhi baithne se behtar (2022 meta-analyses, chhote trials, zyada tar healthy adults) | SECONDARY-OK, evidence kamzor | "Small studies suggest even a few minutes helps" | [PubMed 36715875](https://pubmed.ncbi.nlm.nih.gov/36715875/) |
| F4 | Decongestants (pseudoephedrine, phenylephrine) aur NSAIDs BP barha sakte hain. AHA dono ko list karti hai | SECONDARY-OK | "Can raise blood pressure, especially if it's not controlled" | [AHA Eastern States](https://easternstates.heart.org/?p=7802) · [MedShadow](https://medshadow.org/cold-medicines-can-impact-those-with-high-blood-pressure-heart-issues) |
| F5 | Pseudoephedrine ka average asar chhota hai: ~1 mmHg systolic (2005, 24 trials ka review) | PARTLY, secondary mein mila | "On average small, but bigger in some people." "Dangerous pill" na kahein | Same as F4 |
| F6 | FDA ne Nov 2024 mein oral phenylephrine hatane ki **proposal** di thi, kyunke woh decongestant ke taur par kaam nahi karta. Wajah effectiveness thi, safety nahi. 2026 ke latest reports mein final order nahi mila | SECONDARY-OK (status check zaroori) | Recording se pehle status dobara check karein | [FDA Law Blog](https://www.thefdalawblog.com/2024/11/fdas-proposal-to-remove-oral-phenylephrine-from-the-otc-monograph-isnt-a-surprise-but-what-is-left-over-the-counter/) · [Becker's](https://www.beckershospitalreview.com/pharmacy/fda-proposes-pulling-common-decongestant-from-shelves.html) · [Medfinder 2026](https://www.medfinder.com/blog/phenylephrine-shortage-update-2026) |
| F7 | 2026 ACC/AHA lipid guideline: CAC un logon ke liye jinka risk borderline/intermediate hai aur jahan statin ka faisla clear nahi. 75+ mein bhi ho sakta hai agar faisla uncertain ho. CAC 0 (ya 1–10) wale lower risk mein reclassify ho sakte hain | SECONDARY-OK | "Can help when the statin decision is unclear." "Zero means stop" na kahein | [ACC 2026 press release](https://www.acc.org/About-ACC/Press-Releases/2026/03/13/18/01/ACCAHA-Issue-Updated-Guideline-for-Managing-Lipids-Cholesterol) · [EBSCO summary](https://about.ebsco.com/blogs/health-notes/ebm-focus-top-takeaways-updated-accaha-guideline-management-dyslipidemia) |
| F8 | Orthostatic hypotension: khare hone ke 3 min ke andar systolic ≥20 ya diastolic ≥10 mmHg ki girawat. 60+ ke ~1 in 5 logon mein. Falls ka risk | SECONDARY-OK | Number ke saath | [Merck Manual](https://www.merckmanuals.com/en-ca/professional/cardiovascular-disorders/symptoms-of-cardiovascular-disorders/orthostatic-hypotension) · [PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC8033893) |
| F9 | 2025 AHA/ACC BP guideline: zyada tar adults ke liye goal <130/80, individualized. Guideline ab orthostatic hypotension ko address karti hai. BP control behtar hone se OH ka risk kam ho sakta hai | SECONDARY-OK | "Your target should be set for you." Koi universal "65+ ka ideal number" nahi | [ACC 2025 press release](https://www.acc.org/About-ACC/Press-Releases/2025/08/13/20/03/New-high-blood-pressure-guideline-emphasizes-prevention-early-treatment-to-reduce-cvd-risk) · [AAFP 2026](https://www.aafp.org/afp/2026/1000/practice-guidelines-hypertension-aha-acc) |
| F10 | Heart attack subah 6 baje se dopahar 12 tak zyada hote hain (Muller 1985 NEJM, 2,999 patients). CK-MB subset mein ~3x zyada 9am par vs 11pm. Beta-blocker lene walon mein yeh rhythm nahi dikha | SECONDARY-OK | "More heart attacks start in the morning hours." Isse beta-blocker ki salah na banayein | [RTI publication record](https://rti.org/publication/circadian-variation-frequency-onset-acute-myocardial-infarction) · [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC484040) |
| F11 | Subah blood zyada "chipchipa" hota hai aur clot todne wala system kamzor (PAI-1 ~6:30am peak, chhoti study) | SECONDARY-OK, chhoti study | "One reason scientists think…" | [HealthDay](https://www.healthday.com/health-news/cardiovascular-diseases/morning-heart-attacks-cause-more-damage-study-finds-652317.html) |
| F12 | TIA ke baad: kuch dinon mein ~10% tak stroke. Post-TIA strokes mein se ~aadhe pehle 48 ghante mein. 90 din mein 10–18%, kuch sources "1 in 5" | SECONDARY-OK, numbers mein range | "As many as 1 in 5 within 3 months, and many in the first 2 days" | [Harvard Health](https://www.health.harvard.edu/heart-health/reducing-your-stroke-risk-after-a-transient-ischemic-attack-tia) · [AAFP 2004](https://www.aafp.org/pubs/afp/issues/2004/0401/p1665.html) · [Allina](https://www.allinahealth.org/healthysetgo/care/transient-ischemic-attack-vs-stroke) |
| F13 | BE-FAST: Balance, Eyes, Face, Arm, Speech, Time | SECONDARY-OK | — | Same as F12 |
| F14 | Gait speed (Studenski, JAMA 2011): 34,485 adults 65+, 9 cohorts. Har 0.1 m/s tez = HR 0.88. ~0.8 m/s average life expectancy ke qareeb, ≥1.0 m/s walon ne prediction se zyada umar payi. Association hai, wajah nahi | SECONDARY-OK | "Doctors use it like a vital sign." "Walking speed predicts death" na kahein | [core.ac.uk abstract](https://core.ac.uk/download/357380987.pdf) · [ACP](https://immattersacp.org/weekly/archives/2011/01/11/4.htm) |
| F15 | ABI ≤0.90 abnormal · 0.91–0.99 borderline · 1.00–1.40 normal · >1.40 stiff (noncompressible). Symptoms hon aur resting ABI normal ho to exercise ABI | SECONDARY-OK | — | [AHA "What is PAD"](https://international.heart.org/-/media/Files/Health-Topics/Answers-by-Heart/What-is-Peripheral-Artery-Disease.pdf) · [ACC 2024 key points](https://www.acc.org/latest-in-cardiology/ten-points-to-remember/2024/05/09/15/00/2024-guideline-for-lower-extremity-pad) |
| F16 | PAD guideline 2024: supervised exercise therapy Class 1 (~3x/hafta, ≥12 hafte). Cilostazol claudication ke liye Class 1 | SECONDARY-OK | — | [ACC 2024](https://www.acc.org/Latest-in-Cardiology/Articles/2024/05/14/13/40/New-ACC-AHA-Guideline-Focused-on-Management-of-LE-PAD-gl-pad) |
| F17 | Silent heart attacks: estimates ~20% se 45%+ tak. 2016 Circulation (ARIC) ~45%. Silent MI walon mein heart-related death ka risk zyada | SECONDARY-OK, range wide | "Studies estimate anywhere from 1 in 5 to nearly half" | [CBS News](https://www.cbsnews.com/news/almost-half-of-heart-attacks-are-silent) · [WCAX 2025](https://www.wcax.com/2025/10/21/women-face-higher-risk-silent-heart-attacks-with-no-symptoms/) |
| F18 | STREAM trial details | PRIMARY-OK (Codex) | 04 §3 dekhein | [NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa2606634) |
| F19 | FDA recalls: Macleods olmesartan/amlodipine/HCTZ, Advagen metoprolol 50 mg (lots ke saath) | PRIMARY-OK (Codex) | Publish wale din status phir dekhein | [FDA 100113](https://www.accessdata.fda.gov/scripts/ires/index.cfm?Event=100113) · [FDA 100234](https://www.accessdata.fda.gov/scripts/ires/index.cfm?Event=100234) |
| F20 | Heart attack ki nishaniyan: seene ka dabao, bazu/kamar/gardan/jaw/pet mein takleef, saans phoolna, thanda paseena, matli, chakkar | PRIMARY-OK (Codex 04 AHA link) | — | [AHA warning signs](https://www.heart.org/health-topics/heart-attack/warning-signs-of-a-heart-attack) |

**Abhi verify nahi hue (NOT VERIFIED, Codex check karega):**
- Older adults ki physical activity guidance (150 min/hafta + strength + balance)
- Decongestant nasal spray ka label par "3 din se zyada nahi" wala rule
- Kaun si BP aur prostate dawaiyan standing BP girati hain (alpha-blockers, diuretics wagaira)
- CAC dobara karwane ka waqfa (interval)
- Hypertensive crisis ka 180/120 threshold, AHA ki current wording
- Stroke mein ghar par aspirin na dene ki current guidance
- ABI test kitni der ka hota hai

Cards mein yeh baatein ehtiyat se likhi gayi hain, aur Codex brief mein yeh check ke liye shamil hain.

---

## 3. Nateeja (INFERRED)
1. **Titles:** search ki zabaan, age marker aur ek sacha sawal. Clone templates nahi.
2. **Script:** Dr Rehan ke liye likhi hui script nahi. **Talking-point card** jo BHWA model jaisa ho, magar scene opening aur asli patient story ke saath.
3. **Thumbnail:** ek asli chehra, ek render, ek bara number ya sawal, aur jawab chhupa hua.
4. **Medical claims:** sirf upar ki table wale. Jo NOT VERIFIED hain woh recording se pehle Codex confirm karega.
