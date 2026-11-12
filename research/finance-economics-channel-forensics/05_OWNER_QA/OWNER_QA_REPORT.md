# Owner Q&A Report — Finance/Economics 69-Channel Study

Owner ke sawal aur unke jawab, ek jagah, tareekh ke saath. Har naya sawal neeche naye number ke saath add hota hai. Sources: `04_FINAL_SYNTHESIS/`, `01_CHANNEL_REPORTS/*/CHANNEL_REPORT.md`, `01_CHANNEL_REPORTS/*/VIDEO_INVENTORY.csv`, DB `data/catalog/finance_economics_complete.db` (read-only).

Labels: **VERIFIED** (DB/public source), **INFERRED** (analyst reading/rule), **HYPOTHESIS**, **UNKNOWN**. Data mein CTR, retention, traffic sources nahi hain.

## Index
| Q | Date | Topic |
|---|---|---|
| Q1 | 2026-11-12 | Overall tiers, top 10, weak 10, common model, repeatable pattern, ek asal baat |
| Q2 | 2026-11-12 | Thumbnails ka analysis hua? Packaging se click ka andaza (+ update: 35 baaki channels ka visual score test) |
| Q3 | 2026-11-12 | Research kahan rakhi hai + dusre agent ke liye handoff prompt |
| Q4 | 2026-11-12 | Wahi 6 sawal dobara (tiers, top 10, weak 10, model, pattern, ek baat) — Q1 ka compact dohrao + thumbnail update |
| Q5 | 2026-11-12 | "Sirf 35 channels ka thumbnail analysis hua, baaki 33 ka nahi?" — coverage ka sahi breakdown |
| Q6 | 2026-11-12 | 69 channels se practical WINNING CHANNEL MODEL (10 components, examples, reusable formula) |
| Q7 | 2026-11-12 | Channel 032 aur 033 ke blind montage dobara bana ke re-score |
| Q8 | 2026-11-12 | Channel 060 (Sarah Rickshaw) ka blind montage dobara bana ke re-score |

---

## Q1 — Overall success picture (2026-11-12)

**Sawal (owner ke alfaz, khulasa):** FINAL_RESEARCH_CONCLUSIONS.md aur 69 reports se simple language mein: (1) kitne channels successful / average / underperform; (2) top 10 successful, naam + reason; (3) weakest 10, naam + reason; (4) koi common business/content model?; (5) repeatable pattern ya topic-specific?; (6) ek baat — Finance/Economics mein channel kyun chalta hai? Har conclusion ke saath channel names, video examples, numbers; evidence na ho to clearly batao.

### Method (INFERRED — naya paimana, 2026-11-12)
Reports ka PI har channel ko **uske apne** baseline se compare karta hai, is liye channels ko aapas mein rank nahi karta. Cross-channel ranking ke liye: **ek normal long-form video ke median views** (Shorts-only channel par saare videos). Tiers: Successful ≥ 20,000 · Average 5,000–20,000 · Underperforming < 5,000. Poori table: `CHANNEL_TIER_RANKING.csv` (is folder mein).

### 1. Kitne successful / average / weak
| Tier | Channels |
|---|---|
| Successful (≥20k typical) | **20** |
| Average (5k–20k) | **21** |
| Underperforming (<5k) | **27** |
| Removed by YouTube | **1** (Wealth Logic — VERIFIED, DB `availability_note`) |

Caveats:
- 20 successful mein 7 purane established brands (Patrick Boyle, How Money Works, Economics Explained, Money & Macro, Modern MBA, Casual Finance, PensionCraft) — naye creator ke liye seedha comparison nahi; inke 6 undated hain (age-adjusted PI nahi).
- Chhota sample: Chronofold 2, David Explains Money 4, Millionaire Problems 9, Built On You 10 videos — "promising", proven nahi.
- Kai "weak" channels ke 1–2 bade hits hain lekin typical video nahi chalta — wahan success lottery jaisi hai.

### 2. Top 10 successful
| # | Channel | Typical | Best video | Main reason |
|---|---|---|---|---|
| 1 | Patrick Boyle | 1.4M | Scott Bessent vs Prices (2.5M) | Personality brand; creator ki pehchaan views tay karti hai (29/30 videos ek hi band) |
| 2 | How Money Works | 775k | National Debt Default… (3.0M) | Aam aadmi ke paise ko chhoone wala systemic risk, sawal ki shakal mein |
| 3 | Economics Explained | 546k | Australia May Have Solved the Housing Crisis (1.5M) | Ghar ki economy + surprising answer; war/geopolitics kam chala |
| 4 | Casual Finance | 485k | The New American Housing Crisis Has Landed (2.35M) | Data + history ka milta-julta waqia + aaj ki fikr |
| 5 | Primate Economics | 449k | Inflation Short (15.7M) | "Explained with Bananas" format ka originator; core concepts |
| 6 | MonkeyExplains | 348k | US National Debt Explained with Bananas (1.92M) | Satire format + timely scandals/bubbles |
| 7 | Modern MBA | 282k | Why Crumbl Cookies Can't Survive (2.2M) | "Mashhoor consumer business kyun fail ho raha hai" |
| 8 | Crayon Capital | 250k | Wolf of Wall Street Scam Explained Like You're 5 (4.2M) | Mashhoor scams/crises ELI5, ~2 uploads/month |
| 9 | Money & Macro | 229k | What happens when you stop taxing billionaires? (510k) | Policy sawal jo sab ki jeb ko lagta hai |
| 10 | Capital Case | 54k (13 videos) | Rockefeller Explained in 10 Minutes (380k) | Canonical financial-history; BlackRock conspiracy/FTX ~5k par flop |

Bilkul bahar: **Neu** (46k; Ship Graveyard 1.12M — slow upload aur ~9-min videos ke bawajood), **Kevin Explains** (28k; Born Before 1967? 696k).

### 3. Weakest 10
| # | Channel | Typical | Best video | Main reason |
|---|---|---|---|---|
| 1 | Max Invests | 178 | 34.8k | "<Name> Invests" template ka failing clone; 98% descriptions mein CFD affiliate link |
| 2 | Ronnie Finance | 405 | Stepdad Kicked You Out… (282k) | Revenge-POV lottery: same genre 671 views; explainers 28–319 |
| 3 | Finance Simplified | 536 | Dividend vs Growth Stocks (205k) | Sirf ek vein chali; consumer comparisons ~400–560 |
| 4 | Nostalgic Wheels | 653 | Economics of Owning a Cafe (187k) | Naam/handle/description teeno alag — identity unclear |
| 5 | Madeline | 661 | IRS $600 Threshold (243k) | Hit galat claim par (IRS IR-2025-107: threshold $20,000 — VERIFIED); Kevin ka presenter reuse |
| 6 | Housing | 669 | Never Keep More Than This in the Bank (185k) | 24 mein 13 near-duplicate scripts; Nia ka hook copy → 43 views |
| 7 | Mark Invests | 1,430 | Renting vs Buying (495k) | Sirf A-vs-B decisions chalte hain; psychology/"levels" ~600 |
| 8 | Uncle Frank Retirement | 1,593 | $500k in Retirement (37k) | Matty concept ki late copy 148 views; narrow topics (RMD, spouse tax) |
| 9 | Finance ANALYST | 1,696 | 10-Year Reunion as Secret Multimillionaire (368k) | Generic titles; wahi kahani generic title ke saath 367 views |
| 10 | Carl Invests | 1,697 | 9 Signs Someone is Secretly Wealthy (126k) | Library weak; "$100/$500/$1,000 a month" series se turnaround (PI 25–71) |

Alag se: Wealth Logic removed; The Wealth Engine sirf 6 videos (insufficient); Tom Talks Money 67.7k subs magar typical 1.8k — subscribers views ki guarantee nahi.

### 4. Common model?
Haan — 5 models baar-baar:
1. Rozmarra business economics — Mr. Finance (Gym 266k), Millionaire Problems (Casino 700k), Business Decoded (Buffets 1.46M), Neu (1.12M).
2. Retirement adequacy "kya mere paas kaafi hai?" — Matty (1.08M), Uncle John (632k), Tom Lazy (282k).
3. Decision duels — Logical Money Renting vs Buying (1.73M), Mark Invests (495k).
4. Second-person POV / secret wealth — POV Wealth (682k), Lucas Grant (705k), This make cents (611k), Dark Ledger (1.11M).
5. Senior benefits/protection — Nia (1.13M), Mark Calloway (724k), Kevin (696k); breakout share sabse zyada (24%), policy risk bhi sabse zyada.

Bade brands ka model "expert personality" hai — naye creator ke liye copy karna mushkil.

### 5. Repeatable pattern ya topic-specific?
Dono: pattern repeatable hai, asal lever **topic choice** hai.
- Mr. Finance: ek template, 65 videos, 401 → 266k sirf business badalne se.
- Matty Invests: wahi scripts, audience retirees ki taraf → ~200 se 1M.
- Finance ANALYST: same kahani, behtar title → 367 se 368k.
- Hamesha search hone wale topics par copy chalti hai (rent vs buy, 10 channels); browse-topic ki late copy fail (Uncle Frank 148).
- Apna hit kuch hafton mein dobara banana fail (6 channels CONTRADICTED); parameter series kaam karti hai (Carl, Robin Costco → Aldi).
- Support nahi hua: upload frequency (correlation ≈ 0), "8+ min = zyada views", micro-cliffhangers.

### 6. Ek asal baat
Finance channel tab chalta hai jab viewer title padh kar **khud ko usmein dekh le** — apni umar, balance, dukaan ya faisla — saath mein ek concrete number ya scene ho, aur framing faida/ijazat/hifazat ki ho, dar ya gussa ki nahi.

### Evidence gaps
CTR/retention/traffic nahi; zyada tar channels ke sirf latest ≤100 videos; 6 bade brands undated; Google Trends, comments, VidIQ, timed transcripts use nahi hue; external fact-check sirf 3 claims; network/ownership rishte INFERRED.

---

## Q2 — Thumbnails aur packaging (2026-11-12)

**Sawal (khulasa):** Kya 68 channels ke thumbnails analyze nahi kiye? Thumbnail performance par asar dalta hai; exact CTR nahi, lekin andaza to lag sakta hai ke packaging kaisi thi aur user click karega ya nahi.

### Kya hua aur kya nahi (VERIFIED — files se)
| Kaam | Coverage |
|---|---|
| Thumbnails download | 3,577 images (`~/YIOS-local-audits/.../thumbs/`, commit nahi) |
| Automatic features (brightness, contrast, colour, face, text words via OCR) | sab images; 3,001 long-form videos par statistical test (`deliverables/08_thumbnail_feature_tests.csv`) |
| Winners vs losers montage (6 best + 6 weakest) | 60 channels ke bane (001–060); 061–068 ke nahi bane |
| **Aankh se visual review** | sirf **32 channels** (001–031 + 037 Casual Finance). Baaki **36 channels sirf OCR/automatic** — yeh asal gap hai |

### Automatic test ka nateeja (VERIFIED numbers, INFERRED reading)
Apne hi channel ke andar style features ka asar **taqreeban zero**:
- Face/character: 1.12x (q=0.13, sirf 21/37 channels mein positive) — kamzor, cartoon faces detector miss karta hai.
- ≤4 words text: 0.97x (no effect); >8 words: 1.11x (no effect).
- Brightness, contrast, saturation, red colour: ρ ≈ 0.
- Sirf edge density (detail) ρ=0.054 (q=0.048) — statistically chhota sa, amali taur par bekar.

Matlab: **thumbnail ka style channel ki pehchaan hai, views ka faisla karne wala lever nahi.** Lana Maynes: winners aur losers ek jaise dikhte hain. Mr. Finance: same layout 65 videos, views 401 → 266k sirf topic se.

### Visual review se jo pattern mila (32 channels, INFERRED)
Pixels nahi, **idea** farq dalta hai — thumbnail ek baat kahe aur title ki baat ko aage badhaye:
- **Binary choice + numbers:** Mark Invests BUY −$88k / RENT +$70k (Renting vs Buying 495k); Finance Simplified GROWTH vs DIVIDENDS $54K vs $7K (205k). Losers: 3–5 options, crowded infographic.
- **Ek goal + ek amount:** Carl $100/$500/$1,000 jar; Mark Retired at 55 freedom metaphor + amount. Losers: trap, gauge, shocked face.
- **Calm hero vs show-off (bina text):** Lucas Grant, POV Wealth, Finance POV. Losers: text overlay ya akela scene.
- **Physical risk metaphor:** Tom Talks Money umbrella in rain of zeros; losers abstract numbers ("Rule of 173").
- **Senior channels:** Nia ke winners mein date ya "$0 bill"; losers "YOUR MONEY IS AT RISK" jaisi dhamki.
- **Exception:** Kevin Explains 8–10 words wale thumbnails bhi winners — few-words rule universal nahi.
- **Packaging ka sabse saaf saboot:** Finance ANALYST — same kahani, title+packaging badla, 367 → 368k.

### Click ka andaza lag sakta hai?
Sirf aadha. Views = impressions × CTR; humare paas impressions nahi, is liye kam views ka matlab "bura thumbnail" bhi ho sakta hai aur "YouTube ne dikhaya hi nahi" bhi (UNKNOWN). Behtareen proxy: **same channel, same topic, alag packaging** ke pairs (Finance ANALYST jaise). Asal CTR sirf channel owner ke YouTube Studio mein hai.

### Pending (agla kaam) — ab POORA hua, neeche "Q2 update" dekhein

### Q2 update — baaki channels ka visual review + score test (2026-11-12)

**Kya kiya (VERIFIED):** Channels 032–036 aur 038–068 (36 mein se **35**) ke thumbnails aankh se dekhe. Har channel se 4 sabse bade (PI) + 4 sabse chhote videos (kam videos wale channel mein kam), **262 thumbnails**. Sheets **blind** thi: tiles shuffle, sirf title dikha, PI/views chhupe; answer key alag file mein. **Channel 057 (Shaami Finance) UNKNOWN:** uske 13 thumbnail files local folder mein hain hi nahi (download nahi hue the; purana montage khali).

**Score (har thumbnail par 0/1, INFERRED — meri subjective padhai):** I = ek hi idea? · N = number/amount dikhta hai? · C = title ko complement karta hai (nayi baat/angle, sirf title ki copy nahi)? · E = saaf emotion/stakes? Total 0–4.

**Test:** har channel ke andar winners ka average minus losers ka average, phir 35 channels par Wilcoxon (BH-corrected).
| Score | Winners avg | Losers avg | Winners ahead / Losers ahead / tie (channels) | p | q (corrected) |
|---|---|---|---|---|---|
| One idea | 0.94 | 0.92 | 7 / 3 / 25 | 0.37 | 0.52 |
| Number | 0.34 | 0.38 | 9 / 14 / 12 | 0.42 | 0.52 |
| Complements title | 0.32 | 0.44 | 6 / 16 / 13 | 0.048 | 0.24 |
| Emotion | 0.24 | 0.27 | 9 / 12 / 14 | 0.63 | 0.63 |
| **Total (0–4)** | **1.85** | **2.01** | 9 / 18 / 8 | 0.13 | 0.33 |
Channel ke andar total score vs views ka average Spearman = **−0.11** (31 channels, p=0.17).

**Nateeja (INFERRED):** Rubric score **PI ko predict nahi karta** — koi bhi test correction ke baad significant nahi, aur disha thodi ulti hai (winners ka score kam). Pehle ka automatic-feature nateeja (style ≈ zero asar) yahan visual rubric se bhi confirm hua. "One idea" lagbhag sab thumbnails mein hai (93%), isliye ceiling effect hai — yeh farq nahi kar sakta.
Misaalein (VERIFIED numbers):
- **Marcus Retires:** winners 74k–245k views, losers 93–242 views; thumbnail style almost same (text banner + senior-benefit prop). Farq topic/hook ka hai, packaging ka nahi.
- **Uncle Frank Retirement:** sabse zyada score wale thumbnails (3–4: "$6,000 Tax Surprise", "Before You Withdraw $50,000") losers the (148–408 views); winners 7k–27k.
- **The Expensive Part:** winners (Tavern 88k, Blacksmith 37k) ke thumbnails busy infographic-style (score 0); losers (Brothel 713) saaf scene — fir bhi hare.
- **PensionCraft:** winners ka score zyada (2–3 vs 0–2) — 35 mein se sirf 9 channels aise.

**Limits:** score maine diya (ek rater, human-coded second opinion nahi); title dikhne se topic ka asar poori tarah hat nahi sakta; PI-top/bottom compare hota hai, poora spectrum nahi; 064 aur 067 mein sirf 1 pair; Shorts-style/AI-faces ka alag test nahi. CTR/impressions UNKNOWN — "bura thumbnail" aur "YouTube ne dikhaya nahi" alag nahi kiye ja sakte.

**Files:** local (commit nahi) `~/YIOS-local-audits/finance-viral-forensics-2026-11-12/out/thumb_review_{scores.txt,key.csv,scored.csv,results.csv}`, sheets `montage_blind/`; scripts `_scripts/15_thumb_review_sheets.py`, `16_thumb_review_stats.py` (repo).

**Baaki UNKNOWN:** 057 ke thumbnails (fetch karne ki ijazat chahiye); human second rater.

---

## Q3 — Research kahan hai + handoff prompt (2026-11-12)

### Jagah (VERIFIED)
| Kya | Kahan | GitHub par? |
|---|---|---|
| Saari reports (69 channel reports, cross-channel, final synthesis, owner Q&A) | `/Users/ghilmankhan/workprojects/yios-audit-fixes/research/finance-economics-channel-forensics/` | Haan, branch `data/finance-economics-complete-2026-11-11` (pushed tak `93657440`; Q&A commits `979f82ea`, `d96dff9e` + yeh Q3 sirf local) |
| Database | `/Users/ghilmankhan/workprojects/yios-audit-fixes/data/catalog/finance_economics_complete.db` | Haan (same branch) |
| Thumbnails (3,577), montages, feature CSVs, scripts, venv, HANDOFF.md | `~/YIOS-local-audits/finance-viral-forensics-2026-11-12/` | Nahi — sirf is Mac par |

### Handoff prompt
```
You are taking over the Finance/Economics 69-channel forensic study (YouTube Intelligence OS).
Work only in /Users/ghilmankhan/workprojects/yios-audit-fixes on branch data/finance-economics-complete-2026-11-11 (do not create worktrees/clones or switch branches).
Read first: research/finance-economics-channel-forensics/00_PROJECT_OVERVIEW/README.md, 04_FINAL_SYNTHESIS/FINAL_RESEARCH_CONCLUSIONS.md, 05_OWNER_QA/OWNER_QA_REPORT.md.
Local evidence (not in git): ~/YIOS-local-audits/finance-viral-forensics-2026-11-12/ (thumbs/, montage_forensics/, deliverables/, HANDOFF.md, .venv). Open the DB read-only.
Rules: use VERIFIED/INFERRED/HYPOTHESIS/UNKNOWN labels; no CTR/retention claims (not in data); never modify raw evidence; answer owner questions in simple Hinglish and append each one to OWNER_QA_REPORT.md as the next Q number with the index updated; commit locally, push only when the owner says so; stop expensive work near 90% 5-hour usage.
Next task: visual thumbnail review for the 36 channels not yet inspected (032-036, 038-068): build missing montages for 061-068, score each thumbnail (one idea? number? complements title? emotion), test score vs PI, add results to Q2.
```

---

## Q4 — Q1 wale 6 sawal dobara (2026-11-12)

**Sawal:** Q1 jaisa hi paste: tiers, top 10, weak 10, common model, repeatable pattern, ek asal baat; names, video examples, numbers, evidence gap. Poora jawab **Q1** mein hai (data badla nahi); neeche compact dohrao + Q2 ka thumbnail nateeja jo Q1 ke baad aaya.

1. **Tiers (VERIFIED count, INFERRED paimana: typical long-form median views):** 20 successful (≥20k) · 21 average (5k–20k) · 27 underperforming (<5k) · 1 removed (Wealth Logic).
2. **Top 10:** Patrick Boyle 1.4M (personality brand) · How Money Works 775k (National Debt Default 3.0M) · Economics Explained 546k (Australia Housing 1.5M) · Casual Finance 485k · Primate Economics 449k (Inflation Short 15.7M) · MonkeyExplains 348k · Modern MBA 282k (Crumbl 2.2M) · Crayon Capital 250k (Wolf of Wall Street 4.2M) · Money & Macro 229k · Capital Case 54k.
3. **Weakest 10:** Max Invests 178 (failing clone, CFD affiliate) · Ronnie Finance 405 (revenge-POV lottery, hit 282k) · Finance Simplified 536 · Nostalgic Wheels 653 · Madeline 661 (hit galat claim par) · Housing 669 (13/24 near-duplicate scripts) · Mark Invests 1,430 · Uncle Frank Retirement 1,593 · Finance ANALYST 1,696 · Carl Invests 1,697.
4. **Common models (5):** rozmarra business economics; retirement adequacy; decision duels (rent vs buy); second-person POV/secret wealth; senior benefits (breakout share 24%, policy risk bhi sabse zyada).
5. **Repeatable?** Pattern repeatable, asal lever topic: Mr. Finance 401 → 266k (sirf business badla); Matty ~200 → 1M (audience badli); Finance ANALYST 367 → 368k (title/packaging). Support nahi: upload frequency, 8+ min, micro-cliffhangers.
6. **Ek baat:** viewer title mein khud ko dekhe (apni umar/balance/dukaan/faisla) + ek concrete number ya scene + faida/hifazat framing, dar/gussa nahi.

**Q2 se naya (INFERRED):** 68-channel thumbnail review (35 channels blind-scored) ne dikhaya ke thumbnail ka style/rubric score views ko predict nahi karta (score vs PI Spearman −0.11, correction ke baad kuch significant nahi). Isliye "ek baat" mein thumbnail lever nahi; topic + title ka angle hi lever hai. Misaal: Marcus Retires — winners 74k–245k aur losers 93–242 views, thumbnail style lagbhag same.

**Evidence gaps:** CTR/retention/impressions UNKNOWN; zyada tar channels ke latest ≤100 videos; 6 bade brands undated; channel 057 thumbnails UNKNOWN; network/ownership rishte INFERRED.

---

---

## Q5 — "Sirf 35 channels ka thumbnail analysis hua, baaki 33 ka nahi?" (2026-11-12)

**Jawab: nahi, 33 bache nahi hain.** 35 sirf *blind scoring test* ka number hai.
| Hissa | Channels | Kaise dekhe | Label |
|---|---|---|---|
| Pehle wale | 001-031 (lagbhag 32) | Aankh se review + winners/losers montages, blind score nahi | VERIFIED (montages 001-060 maujood), count ~ INFERRED |
| Blind rubric test | 032-036, 038-068 (35) | titles shuffle, PI hidden, alag answer key; Wilcoxon + BH; Spearman -0.11 | VERIFIED |
| Channel 057 | 1 | thumbnails local folder mein hain hi nahi | UNKNOWN |
| Automatic OCR/feature metrics | jin ke thumbnails local mein hain | edge density etc. | VERIFIED |

**Kamzori:** channel 032, 033 (aur 060) ke montage image viewer mein decode nahi hue, phir bhi 032/033 ke scores likhe gaye -> un 2 scores ko VERIFIED nahi kaha ja sakta (UNKNOWN, dobara check chahiye). Next step (owner ki ijazat par): 032/033/060 ke montage dobara bana ke re-score, 057 ke thumbnails fetch.

---

## Q6 — 69 channels se practical WINNING CHANNEL MODEL (2026-11-12)

Source: `04_FINAL_SYNTHESIS/FINANCE_ECONOMICS_WINNING_MODELS.md`, `03_CROSS_CHANNEL_FINDINGS/REPEATED_WINNING_PATTERNS.md`, channel reports. **Koi CTR/retention data nahi** -> "audience ko rokna" wala hissa transcript-based INFERRED hai, measured nahi. Sab patterns correlational hain.

### 10 components (har ek: model + examples)
1. **Audience** - viewer apne aap ko number/age/jagah mein place kar sake. Examples: Matty Invests (retirees, pivot ke baad PI 0.03-0.10 -> 20-498), Ivan "Ready at 45?", Lana "Born Before 1966?". (VERIFIED data, reading INFERRED)
2. **Problem/desire/curiosity** - "Kya main aage hoon? kya ruk sakta hoon? mera paisa safe hai?" (adequacy/permission/protection). Examples: Tom Lazy "Secretly Ahead at 55" (282k), Uncle John (440k, 399k), Nia Prescott (1.13M).
3. **Topic type** - perennial decision, rozmarra ki jagah/cheez, thresholds (age/amount), benefits calendar. Examples: Business Decoded buffets (1.46M), Neu ship graveyard (1.12M), Mr. Finance gym 266k vs ski resort 401 views (same template - sirf subject ka farq).
4. **Angle** - gain/permission/protection > loss/outrage; chhupa hua number > general salah. Examples: Nia/Lana (keep/claim jeetta, scam-fear haarta), Uncle John "earned the right to stop", Alicia (aspiration > warning).
5. **Title structure** - specific subject + situation + stake (number). Examples: Matty "$500,000... $1,667 per month", Mark Calloway "$117 more every month", Finance ANALYST wahi story 367 -> 368k sirf specific title se (VERIFIED pair).
6. **Thumbnail** - ek idea: binary choice, ya ek amount, ya calm-vs-showy contrast; <=4 words; consistent character. Examples: BUY vs RENT / ROTH vs 401k, "WALK-AWAY MONEY", "$0 BILL". Dhyan: blind test mein style PI ko predict nahi karta (Spearman -0.11, kuch significant nahi) -> thumbnail *enabler* hai, driver nahi.
7. **Opening hook (0-5s)** - matched pair / exact-time story + object + price / number-first with named source. Examples: Mark Invests & Logical Money "two guys same age same $X", Tom Lazy "$364,000... Survey of Consumer Finances", Finance POV "6:52... ticket $84 million". Hook sab mein common hai -> differentiator nahi.
8. **Content sequence** - intro mein title ka promise confirm (self-intro nahi) -> escalation/ladder ya 20-year race ya list of mini-scenes -> real numbers + named dataset -> verdict. Examples: Dark Ledger ladder (1.11M), Mark Invests/Logical Money duel, Robin MBA/Business Decoded dream->numbers->verdict.
9. **End tak rokna** - INFERRED (retention UNKNOWN): built-in curiosity gap (kaun jeetega, hidden number kab khulega), escalation, har item mein mini-scene + stat + ek action. Examples: Logical Money race, Dark Ledger levels, Nia's "ek action" endings.
10. **Next-video interest** - parameter series (naya amount/store/age) + explicit next-video tease. Examples: Carl $100->$500->$1,000 (PI 71, 25, 55), Robin Costco->Aldi (446, 159), Uncle John "next video: widow's tax" tease, Alicia next-video links.

### Reusable formula
**WINNING VIDEO = [Self-placement audience] x [Perennial/everyday subject] x [Gain/permission/protection angle] x [Title: subject+situation+number] x [Thumbnail: 1 idea/1 number/1 contrast] x [Hook: matched pair ya number+source] x [Promise confirm by 30s] x [Escalation + real data] x [Verdict + 1 action] x [Next parameter video]**

**Channel level:** (1) ek sentence: "yeh un logon ke liye hai jo ___". (2) 15+ channels ka outlier list; sirf wahi concept jo >=2 channels par >=5x ho aur perennial ho. (3) Pehle 10 videos: 5 cross-validated subjects + 3 parameter variants of best + 2 doosre format ke tests. (4) Flop par abandon nahi, specific scene/stake ke saath retitle. (5) Original scripts, sources description mein, synthetic presenter disclose.

**Sabse bada rule:** subject > packaging (46 channels follow, 3 contradict). **Risk:** senior-benefits mein accuracy/policy risk sabse zyada (ek channel terminated); late copies of browse concepts flop.

---

## Q7 — 032 aur 033 ke montage dobara bana ke re-score (2026-11-12)

**Kya kiya (VERIFIED, local files):** dono channels ke 8-8 thumbnails naye random shuffle (seed 1000+n) aur naye labels ke saath **JPEG** montage mein banaye (`montage_blind_v2/032.jpg, 033.jpg`; purane PNG decode nahi ho rahe the). Dono naye montage image viewer mein decode hue. Scoring blind thi: titles dikhe, PI/views nahi; naya answer key alag file `out/thumb_review_key_v2_032_033.csv` mein, scoring ke baad hi kholi. Rubric wahi (I, N, C, E). Purani files `*_v1` naam se backup hain (`thumb_review_scores_v1.txt`, `..._results_v1.csv`, `..._scored_v1.csv`).

**Nateeja:**
| | Purana (v1) | Re-score (v2) |
|---|---|---|
| 032 mean total/tile | 2.625 | 2.875 |
| 033 mean total/tile | 2.250 | 2.625 |
| 35-channel Wilcoxon, total: W vs L | 1.85 vs 2.01, p=0.131, q=0.33 | 1.87 vs 2.02, p=0.183, q=0.46 |
| W-higher / L-higher / tie channels | 9 / 18 / 8 | 11 / 17 / 7 |
| Criterion C (title ko complement) | p=0.048, q=0.24 | p=0.063, q=0.31 |
| Mean within-channel Spearman | -0.11 | -0.088 (n=31, t-test p=0.26) |

**Matlab:** purane scores 032/033 ke bhi zyada door nahi the (zyadatar tiles ke scores same ya 1 point ka farq). Kuch bhi BH-correction ke baad significant nahi, **thumbnail style PI ko predict nahi karta** wala nateeja badla nahi. 032/033 ab VERIFIED-rescored hain; ek hi scorer (Claude) ne dono baar score kiya, isliye inter-rater reliability UNKNOWN. **Baaki khula:** channel 060 ka montage bhi decode nahi hua tha (dobara check baaki), aur 057 ke thumbnails local mein nahi hain (UNKNOWN).

---

## Q8 — Channel 060 ka re-score (2026-11-12)

Q7 wala tareeqa: 060 ke 8 thumbnails naye shuffle (seed 1060) + naye labels, JPEG montage (`montage_blind_v2/060.jpg`, decode hua), titles only, PI hidden, key alag (`out/thumb_review_key_v2_060.csv`), scoring ke baad kholi. Backup: `thumb_review_scores_v2.txt` (Q7 ke baad ki state).

**060 ka asar (VERIFIED):** winners vs losers total 3.0 vs 2.5 (v2 mein). Purane aur naye scores mein 4 tiles same rahe, baaki mein 1-2 point ka farq; naye mein crowded/multi-element tiles (B, D, F) ko "one idea = 0" mila.

**Final 35-channel test (032, 033, 060 re-scored):**
| Metric | Original | Q7 ke baad | Q8 ke baad |
|---|---|---|---|
| total W vs L | 1.85 vs 2.01 | 1.87 vs 2.02 | 1.92 vs 2.06 |
| Wilcoxon p / q | 0.131 / 0.33 | 0.183 / 0.46 | 0.271 / 0.52 |
| W-higher / L-higher / tie | 9/18/8 | 11/17/7 | 12/16/7 |
| Criterion C p / q | 0.048 / 0.24 | 0.063 / 0.31 | 0.133 / 0.52 |
| Mean Spearman | -0.11 | -0.088 | -0.071 (n=31, p=0.37) |

**Nateeja:** koi bhi criterion BH ke baad significant nahi; "thumbnail style PI ko predict nahi karta" badla nahi. Original C p=0.048 sirf uncorrected tha, ab 0.13 hai. Bache hue: 057 ke thumbnails local mein nahi (UNKNOWN); scorer ek hi (Claude) hai isliye inter-rater reliability UNKNOWN.
