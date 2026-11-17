# 28 — DR HENRY JASON (UC-a-yheeRqTvbKMt7UDivfA, @drhenryjason) — STATUS: PARTIAL
Checked 2026-11-14. Sources: senior_health_complete.db (tier 2: Apify complete catalog; 6 videos; 6/6 transcripts, likes/comments present), live channel page in built-in Chrome (header only; grid did not render), curl of all 6 watch pages (status, views, likes, publish date, description) and of the channel page, 6 hqdefault thumbnails viewed, `script_reuse.py`, `title_families.csv`, cross-DB title query + 5-gram similarity over 8 copies of the top title.

## A. Seedha jawab (Roman Urdu)
1. **Kis ke liye / promise:** 60–75+ seniors; hygiene ("old person smell"), aankhein/dhundhli nazar, stroke, anday, tez budhapa. Promise: "ek **retired doctor** (channel bio: "DR Henry Jason, 65", descriptions: "nearly 40 years in medicine", "retired doctor") jo chhupi hui baat batata hai". Naya channel: DB row joined 2025-07-05, 6 videos 2026-09-30 → 10-23 (1.8/hafta); header **"7 videos", 14.5k subs**.
2. **Kya repeat hota hai:** (a) Thumbnail: kaala background, **cartoon/illustrated bujurg** (nani-jaisa chehra), bold peela/safed text + laal highlight: "YOU CAN'T SMELL IT BUT OTHERS SMELL IT!", "YOU CAN'T FEEL IT BUT IT'S STEALING YOUR SIGHT!". (b) Title: "N … After 65/60 …", "Doctor Explains:", "(The Last One Is Silent!)". (c) Opening: **kirdar/manzar** ("You're sitting in a restaurant… menu looks smudged", "9:02 a.m. A woman named Margaret…") ya seedha claim ("There are nine hygiene mistakes that people over 65 make every day"). (d) Ending: "Thank you for spending this time with me. This is Dr. Henry Jason… the video on your screen now is the next one to watch." (e) Description: "WHAT YOU'LL LEARN" bullets + disclaimer jaisa text. **Concentration (live, 6 videos, ~1.78M views):** top-1 99% (`iJhmxqrgTa4` 1,767,636); baaki 5 ka median ~2.3K.
3. **Winner vs weaker (matched):** `iJhmxqrgTa4` (2026-10-18, 16:45, **1,767,636 views**, 27,044 likes) "9 Hygiene Mistakes After 65 That Make You Smell Worse Without Knowing It!" vs `NQwr6G-2Yh8` (2026-10-23, 20:13, **8,006 views**, 462 likes) "Doctor Explains: What Happens When You Eat 4 Eggs Every Day" — same channel, 5 din ka farq, same cartoon-grandma style, **221x**. Thumbnail: winner "YOU CAN'T SMELL IT BUT OTHERS SMELL IT!" (do kirdar, ek naak dabata hua — samajik sharmindagi); weak "4 EGGS EVERY DAY SHOCKING EFFECTS" (anday ki photo + chehra). Opening winner: *"There are nine hygiene mistakes that people over 65 make every single day and they are the same ones doctors notice almost immediately… what quietly gets called old person smell"*; weak: *"I want you to stop and think… a carton of eggs sitting in your refrigerator right now"*. Jo farq dikhta hai: **sharmindagi/doosre log notice karte hain** (social stigma) vs ek khane ka asar. Plausible (interpretation, low): topic ka emotional (sharam) trigger; **testable nahi** (traffic/CTR UNKNOWN). Counterexample (cross-channel): **wahi title family doosre channels par alag nateeje** — `590Y-uQiC9A` (UCK5aB2d…, 2026-08-31) 1,538,466; `QFOXCYTqV2Q` (2026-10-30) 7,131; `o1g_3An1kuk` (2026-10-26) 3,826; `c4gTI1JQ1Jg` 1,333; `-685iKw4NYU` (channel 09, 2026-11-03) 1,236; `EfcuDxKoc38` 784; `suRpmOpMrGg` 113; `wLSJWbjSF2I` 13 — yaani topic/title ne **sirf 2 jagah** 1.5M+ diye, baaki 6 jagah ≤7K. Confidence: low.
4. **Topic source / demand:** Hygiene/"smell" topic: DB mein 8 videos (upar), views 1.54M, 1.74M (do bade) aur 6 chhote — **do independent-ish bade results**, par scripts **alag** hain (5-gram: `iJhmxqrgTa4` vs `590Y-uQiC9A` 0.00, vs `o1g_3An1kuk` 0.00, `QFOXCYTqV2Q` 0.00), sirf channel 09 ka `-685iKw4NYU` **iski verbatim copy** (Jaccard 1.00 over first 200 words; channel 09 ki copy 2026-11-03, yani is channel ke 16 din baad). Demand check: do bade results isi niche mein ek topic ki mazboot demand dikhate hain (medium) par copies ka size sirf 784–7K → format chalna fix nahi. Google Trends nahi chalaya (UNKNOWN). Competitor example: `590Y-uQiC9A` (UCK5aB2dkLd7Nijh9cTdGNEw, 1,538,466).
5. **Playbook rule:** Outlier concept (Playbook p.6–8, Module 2.1): top-1 545x median; 6-video channel mein ek outlier — cross-validation sirf cross-channel title family se (1.54M aur 1.74M, 6 chhote) → topic hypothesis medium-low; **independence ka masla (AGENTS rule 9):** same title ke copies independent evidence nahi. Title Formats (Playbook p.52–53): "N Mistakes After 65" list-format. Against: same list-format ke andar `Dz_gjG-f-7w` "5 Reasons Your Vision Is Blurry" 2,332.
6. **Kya banayein (original idea, evidence-gated):** Emotional/social angle lekin sach aur bina sharam-shaming ke: "Body Odor Changes After 65: What's Normal, What Needs a Doctor (Diabetes, Kidney, Medications)". Thumbnail: asli clinician + ek chhota 3-point list, koi "others smell it". First 30s: "Kya aap ya aap ke walid ke kapdon mein ya saans mein naya, ajeeb smell aaya hai?", payoff = 3 medical wajah (zyada pasina, dawai, peshab/jigar-gurde) + kab doctor. Clinical source jo verify karna hai (yahan fetch NAHI kiya): age-related skin/sweat changes par dermatology review aur "new body odor and diabetic ketoacidosis/kidney disease" ke clinical references; video se pehle verify karein.

## B. Persona / claims / monetization (facts vs interpretation)
- **Fact:** channel bio "I'm DR Henry Jason, 65"; descriptions: "After nearly 40 years in medicine, Dr. Henry Jason looked at what the research actually says", "retired doctor Henry Jason"; transcripts end "This is Dr. Henry Jason". **Koi licence/institution/specialty nahi; credentials UNVERIFIED** (maine registry nahi dekhi). Thumbnails par sirf cartoon/illustrated kirdar (ek `cVQrd2mHrDI` par saccha-sa dikhne wala bujurg — **interpretation (low):** AI/stock chehra); presenter ki awaaz/video maine nahi dekhi/suni (playback nahi).
- **Fact:** channel page par link `fatimakhania.gumroad.com/l/ovjdzh` — Gumroad ka naam "fatimakhania" presenter ke naam se alag; relation/ownership **Not known** (interpretation karna unsupported hai). Gumroad product/sales UNKNOWN. AI-disclosure descriptions mein nahi dekha.
- **Fact (claims):** "She's 103 and eats red potatoes, whole eggs, ground beef…", "the real science behind why aging after 75 feels different", "one effect shows up within weeks that almost nobody expects" — koi cited study/link maine verify nahi kiya (UNVERIFIED); `Dz_gjG-f-7w` ending mein "please see an eye care professional" (responsible caveat — fact).
- **Fact:** script reuse: 1/6 videos ka script doosre channel ke transcript se ≥0.85 (`iJhmxqrgTa4` → channel 09 `-685iKw4NYU`, dates ke hisaab se 09 ki copy **baad** ki hai); `NQwr6G-2Yh8` vs channel 31 `tDh1EtV3Ol8` 0.09 (alag).

## C. Live vs snapshot
- Live 2026-11-14: header **"7 videos", 14.5k subs**; DB 6 videos, 14.4K subs. 6/6 saved IDs playable (curl OK); publish dates 2026-09-30 → 2026-10-23. **1 header video DB mein nahi** (grid render nahi hua) — Not known.
- Views DB → live: `iJhmxqrgTa4` 1,744,751 → 1,767,636 (+1.3%); `NQwr6G-2Yh8` 7,948 → 8,006; `zhfv9m4ystc` 4,090 → 4,106. Aakhri upload 2026-10-23 (~3 hafte pehle).

## D. Coverage
| Layer | Status |
|---|---|
| Catalog titles/views/dates/durations (DB) | 6/6 (of header 7) |
| Playability / publish date / views / likes (curl 6) | 6/6 |
| Transcripts | 6/6; open/end read for 5 |
| Live channel header (Chrome) | yes (grid not rendered) |
| Thumbnails | 6 of 6 |
| Chrome playback / comments | NOT done / NOT read (DB comment counts present) |
| vidIQ / Trends | not run |
| Credentials / claims | NOT verified |
Pending IDs: 1 header video not in DB; playback + comments for all 6.

## E. Evidence ledger
| Claim | Evidence | Conf |
|---|---|---|
| iJhmxqrgTa4 1,767,636 vs NQwr6G-2Yh8 8,006 | curl watch pages 2026-11-14 | high |
| Hygiene title family: 1.54M, 1.74M, then 7.1K…13 across 8 channels | DB title query | high (DB views stale) |
| iJhmxqrgTa4 ≡ -685iKw4NYU (ch 09, later date) | 5-gram Jaccard 1.00 | high |
| Scripts of the other 6 hygiene copies differ (0.00–0.01) | 5-gram Jaccard | high |
| "Retired doctor / 40 years in medicine" claims | descriptions only | UNVERIFIED |
| Gumroad link name differs from presenter name | channel page text | high (text); relation unknown |
| Why hygiene beat eggs | interpretation | low |
