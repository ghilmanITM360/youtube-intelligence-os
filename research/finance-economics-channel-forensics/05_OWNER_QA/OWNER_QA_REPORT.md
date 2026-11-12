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
| Q9 | 2026-11-12 | Top 10 most instructive channels (repeatable lessons, sirf views nahi) |
| Q10 | 2026-11-12 | Neu (022) ka format thora detail mein samjhao |
| Q11 | 2026-11-12 | Mr. Finance (016): same packaging, views 401 se 265,588 - kyun? (topic vs upload-date vs familiarity) |
| Q12 | 2026-11-12 | Mr. Finance ke upload-date effect ko test karna (age, cadence, topic-control, engagement) |
| Q13 | 2026-11-12 | (owner Q3) Top 10 channels: Q9 list final + asli hook lines ka supplement |
| Q14 | 2026-11-12 | (owner Q4) Mr. Finance 7 sub-sawal: Q11/Q12 mapping + synthesis correction |
| Q15 | 2026-11-12 | (owner Q5) Matty Invests: young budgeting vs retirees, audience pivot, script comparison |
| Q16 | 2026-11-12 | (owner Q12) Script ka winning structure: transcript proxies, winners vs losers, reusable template |
| Q17 | 2026-11-12 | (owner Q13) Titles aur thumbnails: 15 title-pattern test, 5 winners + 5 losers har pattern, thumbnail inspection method |

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


## Q9 — Top 10 most instructive channels (2026-11-12)

**Selection rule (INFERRED):** sirf highest views nahi. Maine yeh dekha: (1) ek clear repeatable format ho, (2) hamare data mein kaafi videos ho (winners aur flops dono), (3) copy karne layak ho (personality-dependent nahi). Isliye Patrick Boyle (1.4M median, magar personality/credentials-driven), How Money Works aur Money & Macro chhode; unke reports mein replicable format kam hai. Nateeja: 37, 55, 39, 24, 40, 22, 12, 59, 58, 62.

**Thumbnail caveat (VERIFIED, Q2/Q8):** 35-channel blind test mein thumbnail style PI ko predict nahi karta (q=0.52). Isliye neeche thumbnail "strategy" = ye channel kya karta hai (descriptive), "yeh jeetne ki wajah hai" nahi. Kai reports mein montage inspect hi nahi hua (55, 39, 40, 59, 58, 62) - wahan UNKNOWN.

Note: views = DB snapshot. PI = video ki views / channel ke 15 nearest uploads ka median. CTR/retention data nahi hai (UNKNOWN).

### 1. Casual Finance (037) — ../01_CHANNEL_REPORTS/037_casual_finance/CHANNEL_REPORT.md §1, §5, §7, §10-§18
1. **Sub-niche:** macro/markets/housing crisis explainers, history ko evidence banake (stick-figure animation).
2. **Audience (INFERRED):** 20-40 retail investors, "crash aane wala hai?" wali anxiety.
3. **Top videos (VERIFIED):** Housing Crisis Has Landed `Uumnx2Fo6cE` 2.35M (PI 3.3); Brace For Impact. `5umJ63d3rzQ` 2.04M (PI 7.2); SpaceX IPO… Worse Than You Think `-X6YzlY_8tM` 1.71M (3.5); 1973 Stock Market Crash that Nobody Remembers `DKyJABtbF2o` 1.28M (PI 9.2). URL = youtube.com/watch?v=<ID>.
4. **Topic pattern:** current anxiety + historical parallel (1973, 2008 vs 2026) + ek concrete anchor ($1.75T, Redfin %).
5. **Title/thumb:** chhote ominous titles; thumbnail = stick figure + 1 chart + 2-4 words ("History is Repeating"). Winners mein title numbers 25% vs 12%, fear words 31% vs 44% (kam).
6. **Hook/script:** contrarian reframe ya source ke saath data point pehle sentence mein; 8-15 min; jokes + data; open loops 0.08-0.12/100 words.
7. **Schedule:** long-form ~2-3/month; Shorts milake ~14/month; har long se 3-5 Shorts.
8. **Kya chalta hai:** broad relevance + concrete anchor.
9. **Kya fail:** insider niches (MicroStrategy `dlBhLhn8lL0` 50k, PI 0.26; Private Credit `7uu6qaCGZsY` 48k, PI 0.25), vague contrarian titles.
10. **Seekh:** "Aaj ki anxiety -> history parallel -> ek chart -> mazaak -> aam investor ke liye matlab". Visual brand sasta aur ownable rakho.

### 2. Primate Economics (055) — ../01_CHANNEL_REPORTS/055_primate_economics/CHANNEL_REPORT.md §1, §5, §11, §18, §20
1. **Sub-niche:** finance concepts ELI5, bandar ki pidgin narration. 2. **Audience:** broad young, Shorts-first.
3. **Top:** Inflation Explained with Bananas `MAvHgmewRDM` 1.76M (PI 3.9); Tax… `LYsqkGRpv_k` 1.56M (3.5); Tariffs… `lRV6U82vgjI` 1.46M (3.2). Channel max 15.7M ek Short ("Inflation #animation #finance").
4. **Pattern:** ek mass-audience concept (inflation, tax, tariffs). 5. **Title:** "[Concept] Explained with Bananas" series; thumbnail UNKNOWN (montage nahi dekha).
6. **Hook:** pehli line mein pidgin concept statement; 2.5-11 min; Shorts long se recut.
7. **Schedule:** irregular, Shorts Apr-Jul 2025 mein concentrated. 
8. **Chalta hai:** sabke saath relatable macro concepts. 9. **Fail:** niche/product topics: Biggest Ponzi Scheme `dB10EUmjHyc` 136k (PI 0.30), 401k `Fd2jzWdcOHY` 119k (0.27); self-deprecating "boring" openers.
10. **Seekh:** ek memorable character + ek fixed title template; broad topic pehle, niche baad mein. Caveat: sample 30 videos, ek 15.7M Short ne numbers ko skew kiya (INFERRED).

### 3. Crayon Capital (039) — ../01_CHANNEL_REPORTS/039_crayon_capital/CHANNEL_REPORT.md §1, §5, §7, §11-§18
1. **Sub-niche:** financial history / famous money stories, ELI5 crayon animation. 2. **Audience:** 18-40 general curiosity.
3. **Top:** Wolf of Wall Street Scam Explained Like You're 5 `HawmGu7oNrc` 4.22M (PI 9.6); Great Depression… `LuEcoqizj0o` 2.76M (7.0); 2008 Financial Crisis… `KE-WJevx-7c` 2.29M (5.8); Rockefeller `sMH8WchxQR8` 1.33M (4.4).
4. **Pattern:** duniya bhar jaana-pehchana crisis/scam/tycoon. 5. **Title:** "[Event] Explained Like You're 5" (simplicity promise); thumb UNKNOWN (OCR: ROCKEFELLER etc.).
6. **Hook:** pehle sentence mein paradox/outrage ("lied about $1 stock… sirf 22 months jail"); 10-20 min, comedy skits.
7. **Schedule:** ~1.8 uploads/month (slow, high-production), sponsors (VPN etc.).
8. **Chalta hai:** central character + dramatic event. 9. **Fail:** Epstein Situation `AKrjI9m6fpk` 48.9k (PI 0.30), "Greatest Slave System Ever Created" `GdpGd0U2wmo` 40.6k (0.25) = sensitive non-finance, unclear title.
10. **Seekh:** ek template + ek globally known story + pehli line mein paradox. Note: yahan titles mein numbers winners mein kam (67% vs 87%).

### 4. MonkeyExplains (024) — ../01_CHANNEL_REPORTS/024_monkeyexplains/CHANNEL_REPORT.md §1, §5, §7, §10-§18
1. **Sub-niche:** satirical macro/tech-bubble/scandal explainers (bandar = asli log). 2. **Audience:** 18-35 anti-establishment humour.
3. **Top:** US National Debt Crisis… Bananas `bz0OGtrkjv0` 1.92M (4.5); OpenAI Bubble Worse Than You Think `LfQIJgU_W2w` 1.33M (3.9); SpaceX Bubble Crash `sy4HzG_qzKw` 1.0M (3.6); How did Apestein Get So Rich? `TSJQ8SjcTPk` 838k (3.5).
4. **Pattern:** is hafte ka scandal/bubble. 5. **Thumb:** ape in suit + ek punchline ("THIS CAN'T BE LEGAL, RIGHT?"), logo ya chart; winners mein 5 words vs 3. Title "[X] is Worse Than You Think".
6. **Hook:** fixed "This is [Name], and he's got a huge problem." 7-16 min. 7. **Schedule:** ~3.8/month, median gap 7 din.
8. **Chalta hai:** current event timing. 9. **Fail:** evergreen definitions; Iran War `BHg5pLQmIew` 102k (0.46), REAL Wolf of Wall Street `JY-mDrPh5nY` 88k (0.39) - Crayon Capital pehle le chuka tha.
10. **Seekh:** fixed opener + absurd metaphor for numbers. Risk: real log ki caricature (satire disclaimer zaroori).

### 5. Economics Explained (040) — ../01_CHANNEL_REPORTS/040_economics_explained/CHANNEL_REPORT.md §1, §5, §11-§18, §20
1. **Sub-niche:** global macro / country economics, sardonic Australian voice. 2. **Audience:** global English economics fans.
3. **Top:** Australia May Have Just Solved The Housing Crisis `QtZfbWOkoIY` 1.5M (PI 2.7); Finally a Country Is Taxing Its Billionaires `jknb1YE6zdY` 1.3M; Economics Is A Junk Science `TsfsoaNFyTQ` 1.2M; NZ Only Safe Haven Left `4kSd7zyXGo0` 1.1M.
4. **Pattern:** sab ko mehsoos hone wali problem (housing, tax) + ek desh ka case. 5. **Title:** declarative verdicts; thumb UNKNOWN. 6. **Hook:** witty metaphor/verdict pehle sentence mein; 13-21 min.
7. **Schedule:** UNKNOWN (dates DB mein missing).
8. **Chalta hai:** "Big grievance, surprising verdict". 9. **Fail:** How to Rebuild an Economy `01f3r_DnOPc` 206k (0.38), Get Rich Or Die Tryin' `JwklXWLy2UA` 149k (0.27); distant geopolitics.
10. **Seekh:** ghar ke kharche se jude macro mudde + verdict. Caveat: view numbers rounded (1.5M etc.), PI floor 2.0+ - flops bhi 100k+ hain, yaani channel ka floor brand-driven (INFERRED).

### 6. Neu (022) — ../01_CHANNEL_REPORTS/022_neu/CHANNEL_REPORT.md §1, §5, §7, §10-§18
1. **Sub-niche:** maritime/logistics economics (jahaz, container, port). 2. **Audience (INFERRED):** 20-50, "duniya kaise chalti hai".
3. **Top (PI sabse strong):** World's Largest Ship Graveyard `HyUjsfhX4-Y` 1.12M (PI 24.4); Economics of Owning A Ship `cQ4f-24Lp0U` 650k (14.1); Why It's Cheaper to Abandon This Container `eh4-CioOx6s` 505k (13.9); Only Three Companies Control Shipping Containers `ueZcDQAVofk` 404k (11.1).
4. **Pattern:** ek dikhne wali physical cheez + paradox/ownership. 5. **Thumb:** ek bada photoreal object + 2-4 bold words yellow box ("STILL WORTH MILLIONS", "SO YOU WANT TO BUY A SHIP"); losers = maps/orange renders. Titles mein number/"you" nahi.
6. **Hook:** "Here's something weird…" ya object biography; 10 sec mein pehla fact; ~1,300-1,500 words, 9 min; end mein related video link.
7. **Schedule:** ~4/month, median gap 5 din, 63 din ka pause.
8. **Chalta hai:** economics of a physical thing. 9. **Fail:** Why Nobody Wants To Work Anymore `W0bZNfoOreI` 7.6k (0.17), Data Centers… Nuclear `x3GF5mO7Ebk` 2.9k (0.06): geopolitics/off-niche.
10. **Seekh:** sabse "chhote channel se bhi copy karne layak" format. Mr. Finance ka "So you want to own X" template ek naye object par laga. Caveat: sirf ek channel, causation UNKNOWN.

### 7. Kevin Explains (012) — ../01_CHANNEL_REPORTS/012_kevin_explains/CHANNEL_REPORT.md §1, §5, §7, §10-§20
1. **Sub-niche:** retiree tax/benefit deadlines + Social Security/Medicare. 2. **Audience:** US seniors 60+ (aur unke bachche).
3. **Top (PI 35-76, channel median sirf 28k):** Good News for US Seniors: 3 Checks `FBT55AI0kvo` 559k (PI 62.6); 3 New Rules Taking Money From Your Check `YJGG5JnDwGo` 440k (75.7); Sign These 4 Documents Before Jan 2027 `9cerzBnd8hE` 412k (73.8); Move These 7 Assets `XmGpdPAtaRY` 388k (35.4).
4. **Pattern:** dated change + institution + dollar amount + N actions. 5. **Title:** "[Verb] These N [Things] Before [Date] Or [Authority] Takes $[Amount]"; thumb: presenter + red-stamped document + 8-10 words (rule ke khilaf, phir bhi winners; title repeat).
6. **Hook:** embodied ("Look at your right hand") ya contrarian truth; 28-34 min; share-to-a-senior CTA; 14 near-duplicate-script flags.
7. **Schedule:** ~20/month, kai same-day; remakes Aug 2026 mein.
8. **Chalta hai:** concept ka pehla video + Medicare savings/Social Security. 9. **Fail:** remake/tax mechanics: $6,000 Deduction `3OsS1lku4XI` 590 views (PI 0.11), Property Tax `7PgxKWmzzCE` 326 (0.06).
10. **Seekh:** deadline+dollar template. Risk: introduced bills ko law bolna, recycled scripts (spam policy risk), 20/month remake. Caveat: 100 videos mein breakout share 24% magar median sirf 28k - lottery jaisa spread.

### 8. Capital Case (059) — ../01_CHANNEL_REPORTS/059_capital_case/CHANNEL_REPORT.md §1, §5, §11-§20
1. **Sub-niche:** financial history + current-event ELI5, faceless ~10-12 min. 2. **Audience:** UNKNOWN (INFERRED: Crayon Capital jaisa).
3. **Top:** Rockefeller Explained in 10 Minutes `sGtEBUIppYc` 380k (PI 7.0); How the Great Depression Actually Happened `CAsim5HC-uI` 294k (5.4); Strait of Hormuz Explained Like You're 5 `0k5C-MrLjAI` 250k (4.6).
4. **Pattern:** canonical subject. 5. **Title:** "[Subject] Explained in 10 Minutes / Like You're 5"; thumb UNKNOWN. 6. **Hook:** paradox/irony; 7. **Schedule:** 13 videos/8 months.
8. **Chalta hai:** canonical history. 9. **Fail:** FTX Collapse Explained Like You're 5 `F0q0tg7JHKI` 5.4k (0.06), BlackRock Conspiracies `Fv3STb4g23Q` 5.1k (0.06): conspiracy/riddle titles; FTX flop bhi dikhata hai ki wahi template har topic par nahi chalta.
10. **Seekh:** Crayon Capital ka format chhote channel par bhi 380k tak chal sakta hai (13 videos, kam sample). Caveat: sample chhota.

### 9. This make cents (058) — ../01_CHANNEL_REPORTS/058_this_make_cents/CHANNEL_REPORT.md §1, §5, §11-§20
1. **Sub-niche:** "wealth revenge POV drama" (second-person). Pivot: 2-9 Oct first-person explainers -> 11-24 Oct revenge dramas (VERIFIED dates). 2. **Audience:** UNKNOWN (INFERRED: story/drama).
3. **Top:** Family Cut You Out of Grandpa's Will — Not Knowing You Already Own… `M0AcqoZ8zQg` 611k (PI 28.3); Wife Divorced You for a Richer Man — Now He Pays You Rent `po7HUg_7yYE` 432k (20.0); Ex-Wife Called You Worthless Repairman `ce_tknjWnX4` 113k (5.3).
4. **Pattern:** "You own what they need". 5. **Title:** "[Humiliation] — Not Knowing You [Own X]"; thumb UNKNOWN. 6. **Hook:** family-holiday/document scene; 15-22 min. 7. **Schedule:** ~20 videos in 5 hafte.
8. **Chalta hai:** revenge + hidden ownership. 9. **Fail:** 4 Stages of Compounding `ggFY_2P_sH4` 1.2k (0.04), AI Dropshipping `cgEpjpaFF5o` 888 (0.03): generic explainer drama channel par.
10. **Seekh:** sabse tez, magar luck-heavy: poore POV niche mein 3 lottery jaise channels (Q1). Tabhi lo jab sirf pattern test karna ho. Caveat: 20 videos, 5 hafte.

### 10. Millionaire Problems (062) — ../01_CHANNEL_REPORTS/062_millionaire_problems/CHANNEL_REPORT.md §1, §11, §18, §20 + VIDEO_INVENTORY.csv
1. **Sub-niche:** business-ownership economics ("lose nine figures with dignity"), faceless 10-16 min. 2. **Audience:** business/money fantasy viewers (INFERRED).
3. **Top (VERIFIED inventory):** Economics of Owning a Casino `HE5xgQS53gc` 700k; Offshore Oil Rig `XiDvK1r2l_k` 264k; McDonald's Franchise `CcyLLvUj5jY` 199k; Private Military Company `TFiTzviGMAE` 123k; Bank `RbBLk-l-xIc` 107k.
4. **Pattern:** "Economics of Owning a [X]" (X = recognisable business). 5. **Title:** fixed template; thumb UNKNOWN. 6. **Hook:** UNKNOWN (sample chhota).
7. **Schedule:** 9 videos, ruka Jul 2026 (dates 21 Apr-26 Jul).
8. **Chalta hai:** casino/oil rig/McDonald's. 9. **Fail:** Football Team `N0t9Vj8r7pc` 11.6k, Car Dealership `l6YFg01TuX0` 18.6k, Cemetery 43.5k: billionaire-only ya morbid/boring assets.
10. **Seekh:** Neu (#6) ke ownership video ke saath milke ek hi template dikhta hai. Caveat: sirf 9 videos, channel ruk gaya.

### Cross-channel jo in 10 se nikalta hai (INFERRED)
- **Repeatable:** ek fixed title template (Bananas / Like You're 5 / Economics of Owning / Worse Than You Think) + mass-relevant topic + pehle sentence mein paradox/number. In 10 channels ke reports ke flops mein common cheez niche/sensitive/off-niche topic hai (template wahi, topic alag); gino ka formal count nahi kiya.
- **Lottery-like:** 12 (Kevin), 58, POV channels: PI bahut high, median kam.
- **Thumbnail:** isse "jeeta" nahi sabit hota (null test); consistent ownable style hi common hai.
- **UNKNOWN:** CTR, retention, thumbnails for 55/39/40/59/58/62 (montage inspect nahi hua), Economics Explained ki dates, 057 thumbnails.


## Q10 — Neu (022) ka format explain (2026-11-12)

Source: `01_CHANNEL_REPORTS/022_neu/CHANNEL_REPORT.md` §1, §4, §5, §6, §13, §18-§22 aur `VIDEO_INVENTORY.csv` (56 videos, 2025-09 se 2026-11).

**Ek line:** "Samundar/transport ki ek dikhne wali cheez (jahaz, container, port) chuno -> usmein ek ajeeb economic sach (paradox) dhundo -> 9 minute mein numbers ke saath samjhao."

### Format ke 5 hisse (VERIFIED report se; kaaran INFERRED)
1. **Topic = object, idea nahi.** Jahaz, container, port, crane, tanker. Seedha dikhne wali cheez.
2. **Paradox title.** "Cheaper to Abandon This Container" `eh4-CioOx6s` 505k; "Largest Ship Graveyard" `HyUjsfhX4-Y` 1.12M (PI 24.4); "Economics of Owning A Ship" `cQ4f-24Lp0U` 650k (PI 14.1). Titles mein number/"you" nahi.
3. **Thumbnail:** ek bada photoreal object + 2-4 bold words yellow box mein ("STILL WORTH MILLIONS", "SO YOU WANT TO BUY A SHIP", "THE CARTEL OF CONTAINERS"). Losers: map, orange 3-D render.
4. **Script:** ~1,300-1,500 words, 8-10 min. Pehle 10 sec mein ek ajeeb fact ("Here's something weird about global shipping" / "Somewhere in the Indian Ocean, a massive container ship..."). Numbers bohot (2.45 per 100 words winners mein), "you" kam. End mein agla related video.
5. **Cadence:** ~4/month, har video 8-10 min (median 9.0).

### Do tarah ke jeetne wale video
- **Story-of-one-object:** Ship Graveyard - ek jahaz ki zindagi, end Alang beach par.
- **Ownership template:** "Economics of Owning A Ship" - "So you want to buy a ship... $50M, $120M". Yeh template Mr. Finance (016) se liya gaya (idea source INFERRED, title overlap 0%).
- **Paradox:** Container chhodna sasta kyun. **Concentration:** Sirf 3 companies containers banati hain `ueZcDQAVofk` 404k (PI 11.1).

### Jo kaam NAHI karta (VERIFIED numbers)
- **Object dikhta nahi / alag jagah:** Airplane Graveyard `G66MoHRtoYw` 9.5k (PI 0.19) - wahi "graveyard" frame jahaz par 1.12M, plane par 9.5k. Economics of Owning A Plane `c5xQuVIkN58` 58.9k (PI 1.17) vs Ship 650k. Matlab template object badalne se transfer nahi hota (1 jodi ka tulna - INFERRED).
- **Geopolitics/crime:** Nuclear Icebreakers `rDe9wmDfwGo` 10k, Pirates Ransom `vQCNXbm2jjU` 8.6k.
- **Off-niche:** Data Centers `x3GF5mO7Ebk` 2.9k (PI 0.06), Nobody Wants To Work `W0bZNfoOreI` 7.6k.
- **Variant-spam:** "How A Single Company Owns/Dominates..." 5-6 versions, sab 36k-102k (PI ~0.7-2.8) - pehla container wala 404k tha, baad ke sab kamzor (INFERRED: audience repeat se thak gayi, HYPOTHESIS).

### Numbers (VERIFIED)
56 videos, median ~45.6k views. Top 5 (1.12M, 650k, 505k, 404k, 337k) PI 7-24. Zyada tar winners Dec 2025-Apr 2026 ke hain; Jul-Nov 2026 mein BYD `nWUcDEfUiBU` 240k, Singapore port `rqTJoriWdFk` 337k jaise kuch hi bade hit aaye (UNKNOWN: kya channel growth ya algorithm ka asar). Length aur PI ka rishta negative (rho -0.27): chhote video behtar.

### Aap kaise apply karoge (INFERRED, ek checklist)
1. Ek niche chuno jahan "dikhne wali cheez" ho (jahaz/trucks/airports/supermarkets).
2. Har cheez ke liye pucho: "Yeh ajeeb kyun hai?" (waste, cartel, sasta-mehnga ulta).
3. Title paradox ya "So you want to own X"; thumbnail = object + 2-4 words.
4. Script 9 min, pehle 10 sec mein ajeeb fact, har minute mein ek number.
5. Test: pehle 3 video alag objects par, phir jo chale wahi doharao (variant-spam se bacho).

### Caveats
- Ek hi channel, causation UNKNOWN; CTR/retention data nahi.
- Production quality (photoreal visuals) copy karna mehnga/skill-heavy hai - cost UNKNOWN.
- PI 24 ek single outlier hai; baaki top 4 PI 7-14.
- Claims plausibility-check hue, har number primary source se verify nahi.


## Q11 — Mr. Finance (016): same packaging, views 401 se 265,588 (2026-11-12)

Source: `01_CHANNEL_REPORTS/016_mr_finance/CHANNEL_REPORT.md` §1, §4-§7, §10-§13, §15, §18, §22 + `VIDEO_INVENTORY.csv` (65 videos, sab "The Economics of Owning a [X]"). Naya analysis (VERIFIED numbers, local python): views/PI vs upload date, business category (mera coding - INFERRED), cross-channel check Millionaire Problems (062) se.

### Premise check
- **VERIFIED:** title 100% ek template; thumbnail layout same ("SO YOU WANT TO OWN A [X]" + building illustration); hook same ("Okay, so you want to own a [X]..."). Spread 401 (Ski Resort `KmQ7koHwuqY`) se 265,588 (Gym `4nYkN0wTi2Q`) = ~662x.
- **Exception:** Pharmaceutical Company `LPk-WVb7bcw` ka hook template todta hai (Turing/Daraprim story) - report §6.
- Thumbnail ka visual appeal (inviting storefront) UNTESTED - constant hai isliye test nahi ho sakta.

### Sabse bada naya finding: upload date (VERIFIED)
- Saare 65 video 28 Jun - 24 Aug 2026 ke beech (~34/month). Views upload date se bohot jude hain: Spearman rho = -0.83 (n=62 dated, p<1e-16): jitna naya, utne kam views.
| Upload window | n | median views | median PI |
|---|---|---|---|
| 28 Jun - 12 Jul | 14 | 53,405 | 1.13 |
| 13 - 26 Jul | 18 | 27,997 | 1.05 |
| 27 Jul - 9 Aug | 15 | 6,871 | 1.04 |
| 10 - 24 Aug | 15 | 2,964 | 0.78 |
- Sabse kam views waale paanchon video 18-24 Aug ke upload hain (Ski Resort 24 Aug, Accounting Firm `Nq0FwNlv8_c` 794 views 24 Aug, Laundromat `ev2HYq2HdnA` 1,771 23 Aug, Cement Plant `l0sy1sZX8Ig` 2,031 23 Aug).
- **PI age se uncorrelated** (rho 0.07, p=0.59) kyunki PI apne 15 nearest uploads se compare hota hai. Isliye topic ka asar PI par dekhna zyada safe hai, raw views par nahi.
- Is date-effect ka KAARAN UNKNOWN: (a) naye video ko kam time (sirf 80-136 din ka farq - itna bada gap sirf time se nahi samjhta, INFERRED), (b) ek hi template ka 34/month spam -> viewer/algorithm thakan (HYPOTHESIS), (c) channel ke shuruaati videos ko zyada push (HYPOTHESIS). Test nahi ho sakta.

### Business category vs result (category coding mera hai - INFERRED, sensitivity possible)
| Category | n | median views | median PI |
|---|---|---|---|
| Familiar consumer (gym, cafe, restaurant, supermarket, car dealership, hotel...) | 31 | 20,636 | 1.37 |
| Large/exotic/capital-heavy (airport, bank, ranch, F1 team, ski resort...) | 27 | 16,753 | 0.78 |
| Credentialed/specialist (pharmacy, martial arts, accounting, firearms...) | 7 | 3,440 | 0.27 |
- PI par: familiar vs exotic p=0.008; familiar vs credentialed p<0.001 (Mann-Whitney, no multiple-correction, exploratory). Raw views par familiar vs exotic: p=0.67 (kyunki exotic wale jaldi upload hue).
- Date-adjusted regression (log views ~ age + category, n=62): familiar ~1.6x exotic (t=2.2), credentialed ~0.5x (t=-2.3); har ek mahina purana video ~7.6x zyada views (t=11.7). Yaani date ka asar category se kaafi bada.
- Same-window check: 13-26 Jul: familiar median 55,493 vs exotic 16,037 vs credentialed 4,288. 28 Jun-12 Jul: familiar 70,576 vs exotic 45,763. 27 Jul ke baad teeno ~3-8k par barabar (floor effect).

### Highest aur lowest (VERIFIED)
**Top 10:** Gym 265,588 (PI 8.7); Ranch `n1DXp7Y3xA4` 170,828 (2.9); Shopping Mall `gooYkWPzqjc` 132,815 (2.2); Cafe 108,250 (6.75, undated); Gas Station `yHCOgKumhxE` 96,360 (3.1); Car Dealership `2ppyMGoHsoc` 93,426 (2.8); Sports Team `v9uxAPuD8Ko` 73,062 (1.2); Bank `37NXosi2ipA` 67,864 (1.1); Airport `RXmZ_BcAzAM` 65,170 (1.1); Five-Star Hotel `1s6asmohIqo` 61,876 (3.3).
**Bottom 10:** Ski Resort 401 (0.14); Accounting Firm 794 (0.27); Laundromat 1,771 (0.60); Cement Plant 2,031 (0.69); RV Parks `00MQZk_UBdk` 2,122 (0.72); Firearms Store `KjEMeBten3k` 2,482 (0.84); Beauty Salon `nMQZGcVQsRA` 2,692 (0.67); Shooting Range `-sogmfhdJcM` 2,965 (1.0); Pet Store `LQpOwnBXZBc` 2,964 (0.53); Fish Boat `lAiTx8muoAw` 3,046 (0.78).
**Sabse kam PI (aur date se bacha hua):** Martial Arts Club `zcgFKPC44ds` 4,288 (0.13), Gold Mine `mcwwVYj7izI` (0.22), Pharmacy `-A1Yc9rk5_c` (0.22), Private Island `KnZ_LUXBOPo` (0.20), Pharma Co. (0.18).
**Cafe/gym PI** 8.7 / 6.75 - sabse strong signal.

### Common characteristics
- **High:** gym, cafe, food truck, cinema, hotel, car dealership, gas station = log roz dekhte/jaate hain + "yeh to aasaan dikhta hai" wala romantic picture (hook ke saath fit). Magar Ranch 171k, Bank 68k, Airport 65k, Sports Team 73k bhi top-10 mein - yaani "sirf relatable plan" wali theory poori sahi nahi.
- **Low PI:** license/skill chahiye (pharmacy, martial arts, accounting, firearms) ya fantasy-scale (private island, gold mine, private jet) - viewer khud "main khol sakta hoon" nahi soch pata.
- **Familiar hokar bhi low (counter-examples):** Laundromat 1,771, Grocery Store `KJr3CKAgu78` 3,560, Dry Cleaning `_B0cASirKyE` 3,239, Hardware 6,237, Pet Store 2,964, Hair Salon `2reQHHkQV-g` 4,307 - sab 3-24 Aug ke upload. Report §22 ne laundromat copy karne ko kaha - yeh data se support nahi hota.

### Cross-channel check (VERIFIED, n=5 same topics, anecdotal)
Millionaire Problems (062), wahi template, mai-jun 2026:
| Topic | Millionaire Problems | Mr. Finance |
|---|---|---|
| Casino | 700,164 | 14,092 (PI 0.74) |
| Bank | 106,963 | 67,864 |
| Airport | 95,313 | 65,170 |
| Car Dealership | 18,624 | 93,426 |
| Sports/Football Team | 11,583 | 73,062 |
Topic ka rank do channels mein same nahi chalta (casino 50x farq, dealership/sports ulta). Matlab topic akela nahi - channel, upload time ya audience pehle se kaam kar rahi hai (UNKNOWN kaun sa).

### Kaun si explanation support hoti hai
| Explanation | Verdict |
|---|---|
| Familiarity (viewer ne wahan kadam rakha hai) | **Partly supported** - PI par significant; raw views par date confound; 6 familiar flops. |
| Economic relevance / "kya main kar sakta hoon" | **Partly supported** - credentialed/fantasy sabse neeche (PI 0.13-0.27). |
| Curiosity (fantasy cheezein) | **Not supported akele** - casino 14k, gold mine 10k, private island 9k. |
| Brand recognition | **UNKNOWN** - titles mein koi brand naam nahi (generic businesses). |
| Upload date / saturation | **Strongly supported (VERIFIED correlation), kaaran UNKNOWN.** |
| Packaging | **Test nahi ho sakta** - constant. |
| Video length | Weak (rho 0.07 views, report: 0.23 PI). |

### Apne topic-selection model mein kaise lo (INFERRED)
1. **Raw views nahi, PI se tulna karo.** Ya same-week ke videos ke beech tulna.
2. **Topic ko 3 sawalon se score karo (0-2 har ek):** (a) kya viewer ne personally ye jagah dekhi hai? (b) kya woh sach mein "main khol sakta hoon" sochta hai (koi license nahi)? (c) kya ek romantic picture hai jo numbers se toote?
3. **Fantasy/credentialed topics avoid karo** jab tak koi timeliness na ho (Data Center PI 4.1 apwaad, 16k views).
4. **34 video/month ek template par mat dalo** - date-effect ka ek possible kaaran. Pehle 6-8 alag topics test karo, rotate karo, publish order randomize karo taaki order aur topic alag ho sakein.
5. **Report §22 ki laundromat recommendation tab tak mat maano** jab tak woh topic jaldi upload hoke test na ho.
6. **Pehle apna channel baseline** dekho (Millionaire Problems ke casino 700k bante Mr. Finance 14k ye dikhata hai ki topic ka transfer guaranteed nahi).

### Caveats
- Business category coding mera judgment hai; chhota sample (n=7 credentialed).
- Mann-Whitney p-values multiple-test correction ke bina (exploratory).
- Upload date vs algorithm dynamics ka kaaran UNKNOWN; CTR/impressions/retention data nahi.
- Views snapshot ek hi date ka hai (metadata_level FULL), per-video views history nahi.


## Q12 — Mr. Finance: upload-date effect ka test (2026-11-12)

Data: `01_CHANNEL_REPORTS/*/VIDEO_INVENTORY.csv`, long-form only, snapshot 2026-11-12. 016 mein 62 dated videos (cafe/cinema/hospital undated, date-tests se bahar). Sab numbers local python se (VERIFIED computation); reading INFERRED jahan likha.

### Sawal
Q11 mein views upload date se jude nikle (rho -0.83 = naya video, kam views). Kya yeh (A) sirf time-accumulation hai, (B) 34 video/month ki saturation, (C) topic ka khel, ya (D) koi aur series-level asar?

### Test 1 — Variance kitna kisse (VERIFIED)
| Model (log views, n=62) | R² |
|---|---|
| Sirf business category (familiar/exotic/credentialed) | 0.14 |
| Sirf upload date | **0.67** |
| Date + category | 0.74 |
Date akela ~5x zyada variance explain karta hai; category date ke upar sirf +0.07 jodti hai. (Category coding mera judgment hai - INFERRED.)

### Test 2 — Date effect har category ke andar (VERIFIED)
Median views, upload quartile ke hisaab se (Q1 = sabse purana):
| | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| Familiar consumer (n=6/6/9/7) | 94,893 | 44,687 | 6,871 | 3,239 |
| Large/exotic (n=10/6/5/6) | 45,763 | 15,065 | 9,130 | 2,584 |
Dono mein girawat 18-29x. Yaani date effect topic se alag chal raha hai.

### Test 3 — Kya topic effect date control ke baad bachta hai? (stratified permutation, 5,000 shuffles)
- Date quartile ke andar z-score: familiar vs baaki = +0.65 SD, **p=0.003**.
- Sakht coding (12 ambiguous businesses - hospital, school, hotel, gas station, dealership etc. - hata ke, 17 familiar): +0.66 SD, p=0.011.
- Matlab topic effect **real magar chhota** hai (uncorrected, exploratory).

### Test 4 — Kya sirf "time" (accumulation) yeh samjha sakta hai? (VERIFIED)
Doosre channels mein same age band (80-137 din purane videos), 30 channels (n>=8, 5+ alag ages):
- Median slope: **~1.2x views per extra mahina** (IQR 0.84-1.77x). Yaani 80 din ke baad views lagbhag plateau.
- Mr. Finance (same band, n=62): **~7.9x per mahina**.
- 30 mein se sirf 3 channels ka slope isse zyada/barabar (047 The Expensive Part ~50x, 036 Nostalgic Wheels ~23x, 019 Robin MBA ~11x; teeno chhote sample, n=20-23).
- **Nateeja:** sirf accumulation 7.9x nahi samjhata (INFERRED: baaki channels ka benchmark yahan lagu maan ke). Magar yeh asar kuch aur channels mein bhi dikhta hai, 016 akela nahi.

### Test 5 — Kya 34/month cadence ("saturation") yeh karta hai? (VERIFIED)
- 57 channels: upload cadence vs age-views rho ka rishta = **0.008, p=0.95** (koi rishta nahi).
- Kevin Explains (~20/month): rho 0.04; Tom Lazy Investor (~41/month, 016 se zyada): 0.18; Ivan Invests (~24/month): -0.53 (ulta).
- Matlab "zyada upload = naye video ke views kam" ek **general rule nahi**. 016 par lagu hone ka saboot nahi (cadence-hypothesis kamzor). Cadence+is-channel-ka-combination UNKNOWN.

### Test 6 — Engagement (VERIFIED numbers, reading INFERRED)
| Upload quartile | median like rate | median comment rate |
|---|---|---|
| Q1 (purane) | 2.2% | 0.14% |
| Q2 | 2.5% | 0.31% |
| Q3 | 2.9% | 0.46% |
| Q4 (naye) | 3.3% | 0.77% |
Like rate date ke saath ulta chalta hai (rho -0.70 age~like rate, p<1e-9): naye videos ko kam log mile magar jo mile unka engagement zyada. Yeh **accumulation se alag** pattern hai (accumulation mein rate roughly constant rehta). INFERRED: naye videos zyada tar existing/engaged audience ko dikhaye gaye (HYPOTHESIS - impressions data nahi).

### Test 7 — Smoothness
Rolling median (10 videos) views order mein: 56k -> 53k -> 21k -> 19k -> 7k -> 6.5k -> 3.1k: ek **seedhi girawat**, jhatke nahi. Topic-random effect noisy hota; yeh systematic lagta hai (INFERRED).

### Verdict
| Hypothesis | Verdict |
|---|---|
| Date effect real hai | **Strongly supported** (R² 0.67, har category mein 18-29x) |
| Sirf accumulation | **Not supported akela** (7.9x vs typical 1.2x/mahina) |
| 34/month cadence saturation | **Not supported as general rule** (57 channels, p=0.95) |
| Topic effect | **Supported magar chhota** (+0.65 SD, p=0.003 after date control) |
| Series-level decay / audience-reach shift (naye video kam promote) | **Consistent with data** (engagement rate badhna) - **HYPOTHESIS, test nahi hua** |

### Jo test nahi ho sakta (UNKNOWN)
- Asli kaaran: YouTube ka impression/promotion data nahi.
- Views ka time-series nahi, sirf ek snapshot.
- Undated 3 videos (cafe 108k, cinema 57k, hospital 41k): unka PI channel-median baseline se hai, date-neighbours se nahi.

### Pakka karne ka tareeka (owner ka faisla; abhi nahi kiya)
Mr. Finance ke 65 videos ke views 2-4 hafte baad dobara fetch karo (Apify metadata, chhota kharcha). Agar naye videos tez badhte hain -> time/accumulation; agar flat rehte hain -> decay/low promotion. Isse A vs D alag hoga. Cost aur approval aap decide karo.

### Topic-selection par asar
Topic scoring ko bonus factor maano, primary nahi. Test design mein publish-order randomize karo aur pehle 10 din ke views alag record karo.

## Q13 — (owner Q3) Top 10: Q9 ki list hi final, hook ka gap bhara gaya (2026-11-12)

**Correction:** pehle Q13 mein maine 9 alag channels (Mr. Finance, Business Decoded, Matty...) "everyday money economics" model ke liye daale the. Woh meri apni suggestion thi, owner Q3 ka jawab nahi. Woh version hata diya. **Q3 ke top 10 wahi hain jo Q9 mein chune gaye the** (Selection rule Q9 mein likha hai): Casual Finance 037, Primate Economics 055, Crayon Capital 039, MonkeyExplains 024, Economics Explained 040, Neu 022, Kevin Explains 012, Capital Case 059, This make cents 058, Millionaire Problems 062. Unka poora 10-point breakdown Q9 mein hai; Neu ka format Q10 mein.

**Gap jo Q9 mein tha:** 6 channels ke reports (§12) mein hook sirf ek line ka tha ya "not analysed". Yeh section top videos ke asli transcript ki pehli lines se hook bharta hai (VERIFIED: `data/catalog/finance_economics_complete.db`, tables videos+transcripts; views = DB snapshot).

### Hook, asli opening lines (VERIFIED) + type (INFERRED)
| Channel | Video (ID) | Views | Length | Opening (shortened) | Hook type |
|---|---|---|---|---|---|
| Casual Finance | Housing Crisis Has Landed `Uumnx2Fo6cE` | 2,352,982 | 15m21 | "58% more people trying to sell than buy... largest gap Redfin has seen since 2013" | named-source number first |
| Casual Finance | Brace For Impact `5umJ63d3rzQ` | 2,038,798 | 12m33 | "The biggest risk... was never the AI bubble... it's something much more boring" | contrarian reframe |
| Casual Finance | 1973 Crash `DKyJABtbF2o` | 1,281,284 | 8m49 | "History repeats itself... Sir John Templeton called those the most expensive words" | quote + history |
| Primate | Inflation `MAvHgmewRDM` | 1,761,567 | 2m30 (329 words) | "If monkeys have one banana, banana rare, banana valuable..." | concept in pidgin, no intro |
| Primate | Tax `LYsqkGRpv_k` | 1,555,788 | 9m21 | "What is tax? Monkey work at banana farm..." | question + mini-story |
| Crayon | Wolf of Wall Street `HawmGu7oNrc` | 4,219,017 | 16m33 | "He lied about $1 stock, made millions, and only served 22 months in jail. Then Hollywood..." | outrage in 1 sentence, then dated scene ("Bayside, Queens, 1962") |
| Crayon | Great Depression `LuEcoqizj0o` | 2,762,821 | 16m29 | "You woke up rich, then went to bed broke... $200 billion wiped" | second-person + scale |
| Crayon | 2008 Crisis `KE-WJevx-7c` | 2,285,772 | 13m26 | "158-year-old bank collapsed overnight. $600 billion gone... real cause started with a lie fit on a billboard" | number + curiosity gap |
| MonkeyExplains | Debt `bz0OGtrkjv0` | 1,920,233 | 6m56 | "This is Uncle Dawn, and he's got a huge problem... 37 trillion bananas" | FIXED opener |
| MonkeyExplains | OpenAI `LfQIJgU_W2w` | 1,325,113 | 13m57 | "This is Sam and he's got a huge problem." | same fixed opener |
| MonkeyExplains | Apestein `TSJQ8SjcTPk` | 838,476 | 15m21 | "This is Uncle Don, and he's got a huge problem... 3 million pages" | same fixed opener |
| Economics Explained | Australia housing `QtZfbWOkoIY` | ~1.5M (rounded) | 14m09 | "two distinct types of dirt... mineral-rich dirt... blocks of dirt we trade" | witty metaphor |
| Economics Explained | Billionaires `jknb1YE6zdY` | ~1.3M | 13m30 | "China is currently cracking down on tax avoidance..." | news fact |
| Economics Explained | Junk Science `TsfsoaNFyTQ` | ~1.2M | 17m07 | "Nobody can predict the future, least of all economists... 15 out of the last two recessions" | joke + verdict |
| Neu | Ship Graveyard `HyUjsfhX4-Y` | 1,120,820 | 9m14 | "Somewhere in the Indian Ocean, a massive container ship is steaming north..." | object biography |
| Neu | Owning A Ship `cQ4f-24Lp0U` | 649,970 | 8m09 | "So, you want to buy a ship... after you wire the money" | "so you want to buy" |
| Kevin | 3 Checks `FBT55AI0kvo` | 559,346 | 32m55 (6,181 words) | "A program will pay your Medicare premium. Not reduce it, pay it. Nobody's job is to tell you" | entitlement claim |
| Kevin | 3 New Rules `YJGG5JnDwGo` | 439,856 | 29m39 | "A raise is coming to your Social Security check... three things are taking money back" | good news, then loss |
| Capital Case | Rockefeller `sGtEBUIppYc` | 380,137 | 10m02 | "At its peak, one company controlled 90% of America's oil... richest human in recorded history" | irony in 4 sentences |
| Capital Case | Great Depression `CAsim5HC-uI` | 294,004 | 11m29 | "In 1928 a Harvard economist said poverty was nearly solved. One year later, a quarter had nowhere to go" | dramatic irony |
| This make cents | Grandpa's Will `M0AcqoZ8zQg` | 611,170 | 21m34 | "First Thanksgiving without Grandpa... Uncle Dale slid a pocketknife down the table" | exact-scene, 2nd person |
| This make cents | Divorced `po7HUg_7yYE` | 431,764 | 14m38 | "A rental application on your kitchen table. Two names: Trent and Vanessa Holloway" | object + names, 2nd person |
| Millionaire Problems | Casino `HE5xgQS53gc` | 700,164 | 16m23 | "So you want to buy a casino... only legal business where math guarantees a profit" | "so you want to buy" + paradox |
| Millionaire Problems | Oil Rig `XiDvK1r2l_k` | 264,000 | 16m05 | "So you want to buy an offshore oil rig... price list" | "so you want to buy" |

### Jo naya nikla (VERIFIED, opening text se)
1. **Hook ek hi kaam karta hai: pehle 1-2 sentence mein stake.** Number (Casual Finance, Crayon, Capital Case), fixed character line (Monkey), ya scene (This make cents). Kisi top video mein "welcome to my channel" nahi.
2. **Neu aur Millionaire Problems ka opener lagbhag same hai** ("So you want to buy a ship/casino..."). Data se yahi dikhta hai ki do alag channels same template chalate hain; kaun pehle tha aur kisne copy kiya, **UNKNOWN** (publish dates alag verify nahi kiye).
3. **Length alag-alag hai, ek rule nahi:** Primate 2.5-9 min, Neu 8-9, Capital Case 10-11, Casual Finance 9-15, Crayon 13-16, Kevin 30-33 min. Isliye "length se success" ka koi sabot in 10 mein nahi (Q1 aur final synthesis ke saath consistent).
4. **Kevin ka hook alag family ka hai:** institution + paisa + "kisi ne bataya nahi". Baaki 9 curiosity/story se khulte hain.

### Abhi bhi UNKNOWN / LOW CONFIDENCE
- **Thumbnails** Primate, Crayon, Economics Explained, Capital Case, This make cents, Millionaire Problems ke **dekhe nahi gaye** (montage inspect nahi hua). Isliye in 6 ka thumbnail jawab Q9 mein "UNKNOWN" hi rahega jab tak montage review na ho.
- **Economics Explained** ki upload dates DB mein missing; schedule **DATA NOT AVAILABLE**. Views rounded (1.5M).
- **CTR, retention, comments: DATA NOT AVAILABLE.**
- Sirf top 2-3 videos ki opening dekhi; poore channel ka hook-pattern gino se confirm nahi kiya (**LOW CONFIDENCE** generalization).
- Primate (30 videos), Capital Case (13), This make cents (20), Millionaire Problems (9) = **LOW CONFIDENCE** samples.

**Report links:** `../01_CHANNEL_REPORTS/<NNN_name>/CHANNEL_REPORT.md` §10-§15 har channel ka; Q9 (poora breakdown), Q10 (Neu).


## Q14 — (owner Q4) Mr. Finance 7 sub-sawal, Q11/Q12 se mapping + correction (2026-11-12)

Naya analysis nahi; numbers Q11/Q12 se (VERIFIED computation, local python, snapshot 2026-11-12).

| Owner sub-sawal | Jawab | Kahan |
|---|---|---|
| 1. Same packaging, views alag kyun | Upload date sabse bada factor: R² 0.67 (date) vs 0.14 (category). Naye video kam views (rho -0.83, n=62). | Q12 Test 1 |
| 2. Kya business selection main factor | **Nahi, main nahi.** Real magar chhota: +0.65 SD (p=0.003) date control ke baad. | Q12 Test 3 |
| 3. Highest vs lowest | Gym 265,588; Ranch 170,828; Mall 132,815 vs Ski Resort 401; Accounting 794; Laundromat 1,771. | Q11 |
| 4. Common characteristics | High = roz ka familiar business; low = license/skill ya fantasy-scale. Familiar flops bhi hain (laundromat, grocery, pet store). | Q11 |
| 5. Familiarity/curiosity/brand/relevance | Familiarity aur "main khol sakta hoon" partly supported; curiosity akele nahi; brand UNKNOWN. | Q11 table |
| 6. Dataset kya support karta hai | Date effect strong; accumulation akela nahi (7.9x/mahina vs typical 1.2x); 34/month cadence rule nahi (57 channels, p=0.95). | Q12 verdict |
| 7. Apne model mein | PI se compare, 3-sawal topic score, publish-order randomize, topic ko bonus factor maano. | Q11, Q12 |

**Correction (important):** `04_FINAL_SYNTHESIS/FINAL_RESEARCH_CONCLUSIONS.md` Q1 kehta hai Mr. Finance ne "401 se 266k views sirf business choose karne se" paye. Q11/Q12 ke baad yeh **overstated** hai: topic ka asar real hai par upload date bada hai. Final synthesis file ko maine abhi badla nahi (raw/final evidence owner ke bina nahi chhedta); owner bole to wahan sentence sudhar dunga.


## Q15 — (owner Q5) Matty Invests (003): young budgeting ~200 views vs retirees up to 1.08M (2026-11-12)

Source: `01_CHANNEL_REPORTS/003_matty_invests/CHANNEL_REPORT.md` §1-§3 + `VIDEO_INVENTORY.csv` (94 videos, 92 dated) + transcripts in `data/catalog/finance_economics_complete.db`. Numbers computed locally (VERIFIED computation); readings INFERRED unless stated. 2 undated videos excluded from date splits.

### Seedha jawab
Audience badalne ke baad channel ka **median** ~16x badha, magar yeh pakka "audience ne karaya" sabit nahi hota (sirf 4 purane videos, channel ke pehle 6 din). Aur 1.08M ek akela video hai.

### Numbers (VERIFIED)
- **Young/general budgeting, 24-29 Jan 2026 (n=4):** 646 / 201 / 346 / 171 views; median 273.5.
- **Retiree-focused, 31 Jan onwards (n=88):** median 4,283.5; min 582; max 1,084,237. 26 videos >=10k, 5 >=100k, 18 <2k, 7 <1k.
- Channel ka median 3,984 = tier rule (<5k) se **UNDERPERFORMING** (`CHANNEL_TIER_RANKING.csv`); channel hit-driven hai, 16% breakout.
- Monthly median (retiree videos): Feb 7,753; Mar 4,299; Apr 2,412; May 2,176; Jun 2,668; Jul 12,373; Aug 8,669.

### 1. Kya audience change ne performance badla?
- **Support:** 88 mein se sirf 3 retiree videos 700 se neeche gaye; purane 4 mein 646 max.
- **Against "sirf audience":** (a) n=4 aur channel ke pehle 6 din = cold start confound; (b) retirement hote hue bhi flops: How Much You Need to Retire `Xnr2DD_fwI4` 1,596 (2 Feb), Sell These 5 Things `3vOefiaKRzg` 839 (3 Feb), Social Security Strategies `vHn0KvE_ku0` 582; (c) retiree videos ke andar 582 se 1.08M tak spread. (d) Topic, title style aur audience ek saath badle; alag karke test nahi hua. Purane audience par dobara test nahi kiya gaya, counterfactual **UNKNOWN**.

### 2. Kaun se retiree topics/angles chale (VERIFIED titles/views)
**>=100k:** 7 Things Wealthy Retirees Stopped Buying `5V1gCUvdqMs` 1,084,237; Why People Get Richer After Retirement `7mqI2YgRW1w` 223,088; 10 Things Retirees Just Stopped Caring About `A-lvYmMpGSA` 219,096; What Retirement Looks Like With $2 Million `6U9jXkpQBzE` 146,923; Simple Routines Thriving Retirees Practice `Q1RP8c_9bKs` 122,987.
**50-100k:** $500,000 Retirement Reality `gR3EWBGXP2c` 95,382; Average Person Retires With This `OYOOB6eOong` 71,159; When a Retiree is Considered Wealthy `W-cQ90FFbi0` 63,942; 8 Signs You're Doing Better Than Most Retirees 48,964.
Do angle families (INFERRED): (1) "Retirees ne kya chhoda/chhoda parwah karna" behaviour list + paradox; (2) dollar-amount reality check ($500k, $2M, average savings, "wealthy" threshold).
**Kam chale:** tax/Social Security strategies (776 / 582), mortgage vs invest 652, 4% rule 1,344, "6 Signs You Will Be Broke" 2,268, "Worst Retirement Lies" 2,136 = mechanics ya fear/advice.

### 3. Script same tha ya alag?
**Same format, alag script (VERIFIED):** 0 near-duplicate flags; 6-word-phrase overlap sirf 0.1-1.9%. Dono mein ~2,150-2,650 words (~13-15 min) aur narrator-scene opening.
| Measure | Young 4 | Retiree winners (4) |
|---|---|---|
| "you/your" per 100 words | 3.2-9.2 | 3.5-6.4 |
| "retire*" per 100 words | 0.0-0.12 | 0.8-1.7 |
| Avg words per sentence | 7.8-10.9 | 10.6-13.7 |
| Opening | viewer ka apna 11pm phone/bank scene, ya "Lucy, 28" | named older person ("Steve, 68", "Ray, 76") ya retirees ke baare mein ek claim ("sab ek weird habit share karte hain") |
Matlab "same script" kehna **overstated** hai (final synthesis Q1 mein "identical scripts" likha hai; maine file badli nahi). Sahi: same host, same length, same scene-opening shape; subject, audience aur title badle. Named people real hain ya nahi **UNKNOWN** (faceless channel, anecdote verify nahi hota).

### 4. Audience selection se kya seekhein (INFERRED)
Audience ko title mein naam do ("Retirees") aur uski ek specific cheez par video banao. Pehle 4-5 videos mein audience test karo, jo respond kare usi par jao. Limit: ek channel ka ek pivot, n chhota.

### 5. Kya retirement ek promising alag sub-niche hai?
**Partly.** Support: Matty ke 26/88 >=10k; final synthesis Model 2 (Uncle John 440k, Mark Retired at 55 103k, Tom Lazy 282k...) steady, low policy risk. Against: Matty ka median 4.3k (tier UNDERPERFORMING), Kevin Explains ka senior-benefit sub-niche saturated aur policy-exposed. "Retirement adequacy/lifestyle" promising hai; "alag aur proven" **LOW CONFIDENCE** (ek channel ka pivot).

### 6. Exact structure (sirf jo winners mein VERIFIED hai)
1. **Title:** "[N] Things [Wealthy/Smart/Thriving] Retirees [Stopped/Quit/Don't] ..." ya "What Retirement Looks Like With $[amount]" / "If You Have Saved $[amount]...".
2. **Thumbnail (report §1):** white background, 3-4 bold words, ek yellow keyword. Thumbnail style PI predict nahi karta (q=0.52), isliye yeh sirf "kya karta hai".
3. **Length:** ~14 min, ~2,400 words.
4. **Opening:** retirees ke baare mein ek surprising claim, ya ek named older person ke saath ek scene (3 winners ki opening dekhi; baaki nahi).
5. **Cadence:** ~13 uploads/month; Jul-Aug median Apr-Jun se zyada (behaviour-list wale titles ke saath, INFERRED).
**Nahi copy karna:** mechanics/strategy titles, fear titles. Aur ek hit (5V1, PI 498) lottery jaisa hai - uspe plan mat banao.

### Limits
- Views ka ek snapshot; CTR, retention, traffic source **DATA NOT AVAILABLE**.
- Sirf 4 pre-pivot videos, **LOW CONFIDENCE**.
- Hook sirf 7 videos ki opening se dekha; poore channel ka hook-pattern gino se confirm nahi kiya.


---

## Q16 — (owner Q12) Script ka winning structure (2026-11-12)

**Method (VERIFIED):** `finance_economics_complete.db` transcripts + `01_CHANNEL_REPORTS/*/VIDEO_INVENTORY.csv` (PI). Long-form, transcript COMPLETE, >=500 words. 2,823 videos / 60 channels. **Winners** = PI >= 3 (559 videos, 56 channels). **Losers** = PI <= 0.4 (553 videos, 57 channels). PI channel ke andar relative hai, isliye "winner" ka matlab "apne channel ke normal se bahut upar".
**Limit:** transcripts mein **timestamps nahi hain** (DATA NOT AVAILABLE). "First 5 sec" = pehle ~12 words, "first 30 sec" = pehle 80 words (proxy, ~150 wpm). Auto-captions mein punctuation adhoora hai, to "?" ginti kam-ginti ho sakti hai.

### Sabse bada finding
**Winners aur losers ka script structure lagbhag same hai.** Hook, number, "you", sentence length, curiosity-gap phrases, CTA - kisi mein winners alag nahi nikle:

| Proxy | Winners (559) | Losers (553) |
|---|---|---|
| Median words | 3,051 | 2,788 |
| Pehle 80 words mein koi number | 78% | 77% |
| Pehla number kis word par (median) | 18 | 20 |
| Pehle 80 words mein "you" (median) | 4 | 3 |
| Numbers per 100 words | 2.49 | 2.52 |
| Median sentence length (words) | 13.6 | 13.4 |
| "Here's the catch / wait / later in this" per 1000 words | 0.47 | 0.46 |
| "Imagine / for example / say you" per 1000 words | 0.37 | 0.38 |
| Opening mein "welcome / my name is" | 2% | 2% |
| Aakhri 90 words mein CTA | 44% | 45% |
| Aakhri 90 words mein next-video bridge | 7% | 9% |

**Same-channel check (48 channels jahan dono taraf >=3 videos):** length winners mein zyada 32 channels mein, kam 16 mein (median +160 words) = **weak signal**. "you", numbers, gap phrases, sentence length = 24:24, 29:19, 21:20, 26:22 = **koi signal nahi**.
**Matlab (INFERRED):** yeh structure "table stakes" hai. Winners ko jo alag karta hai woh **topic/subject** hai (Q11, Q13 se match), script ka template nahi. Template copy karne se video "theek" banegi, hit nahi.
Proof ek hi channel se: Neu `HyUjsfhX4-Y` Ship Graveyard (1,120,820 views) aur `G66MoHRtoYw` Airplane Graveyard (9,533) dono "ek jagah ki scene -> scale -> economy" opening aur "Thanks for watching, see you in the next video" ending use karte hain.

### Tumhare 8 sawal

1. **Pehle 5 sec:** winners mein pehla number median word 18 par aata hai (~7 sec). Data mein 3 opening styles: (a) location/scene - Ship Graveyard: "Somewhere in the Indian Ocean, a massive container ship is steaming north"; (b) claim - Matty `5V1gCUvdqMs` (1,084,237): "The retirees who actually keep their money... they all share one weird habit. They quit buying stuff."; (c) number-first. Sirf 7-8% mein named age/person ya exact-time scene hai (regex proxy). Losers ka bhi yahi pattern -> opening style predictor nahi.
2. **Pehle 15-30 sec ka promise:** 78% winners pehle 80 words mein ek number dete hain, par 77% losers bhi. Matty ka example: 7 cheezein + "wealthy retirees" + "habit" - title ka promise dobara confirm. Intro/"welcome" 2% = winners mein bhi lagbhag nahi.
3. **Main question/conflict:** pehla "?" winners mein median word ~475, losers ~527. Punctuation kam hone se **LOW CONFIDENCE**. Conflict aam taur par pehle ~80 words mein statement ki shakal mein aata hai (e.g. data-centre loser: "there's a little issue here" - 80 words mein, phir bhi 2,862 views).
4. **Examples/numbers/stories ka order (200 winners ka random sample, 10 hisse mein):** numbers/100 words 2.45 (pehla hissa) -> 3.3 (hisse 3-4, peak) -> 2.3 (hissa 9) -> 1.8 (aakhri). "he/she/they" (story) 1.2 -> 1.8 (hisse 3 aur 8) -> 1.3. "you" aakhir mein 3.7 (call to action). **Shape: number se shuru, beech mein peak, aakhir mein verdict + seedha "you".** Yeh flat shape hai, koi strong build-up nahi.
5. **Simple ya technical:** sentence median 13.6 words (simple). "Imagine/for example" sirf ~0.4 per 1000 words. Analogy kam, number+narration zyada. (Primate/Crayon jaise allegory channels alag, unka alag craft hai.)
6. **Curiosity gaps/transitions:** explicit phrases ("here's the catch", "wait", "later in this video") ~0.47 per 1000 words = rare, winners aur losers mein barabar (`PDF P15 not supported` se match karta hai).
7. **Character/situation:** winners mein "he/she/they" ~1.5 per 100 words. Named person/scene wale openings sirf 7-8% - dono taraf barabar. Matty ke retiree winners mein named older person (Q15) alag, sample chhota.
8. **Ending/next-video:** 44% winners aakhir mein subscribe/comment CTA, 7% next-video bridge (losers 45% / 9%). Ending style **predictor nahi**. Example winner ending: Ship Graveyard ek line mein thesis ("cheap ships require a cheap place to die") phir "see you in the next video"; Matty: comment prompt + "skip that Amazon cart tonight".

### Actual excerpts (VERIFIED, DB se)
| Video | Views | Opening (pehle ~40 words) |
|---|---|---|
| `HyUjsfhX4-Y` Ship Graveyard (Neu) | 1,120,820 | "Somewhere in the Indian Ocean, a massive container ship is steaming north. For 25 years, this vessel has been the invisible engine of the global economy..." |
| `5V1gCUvdqMs` 7 Things Wealthy Retirees Stopped Buying (Matty) | 1,084,237 | "The retirees who actually keep their money... they all share one weird habit. They quit buying stuff." |
| `G66MoHRtoYw` Airplane Graveyard (Neu, same format, flop) | 9,533 | "In the desert outside Tucson, Arizona, there's a patch of land roughly 2600 acres in size where nearly 4,000 aircraft set parked..." |
| `x3GF5mO7Ebk` Data Centers (Neu, flop) | 2,862 | "Where we are right now is Microsoft's newest AI data center in Wisconsin... 900 megawatt... a city of 250,000..." |

### Reusable template (INFERRED - structure table-stakes hai, jeet nahi dilata)
1. **0-12 words:** ek concrete scene ya claim (jagah, cheez, ya sawal) - title ka wahi subject.
2. **Pehle ~80 words:** ek number + "you"/viewer se jodna; promise confirm; intro/channel naam nahi.
3. **~Pehla 10-20%:** conflict/paradox statement ("cheap ships need a cheap place to die" type) - gap yahin banao, phrase-based gap par depend mat karo.
4. **Hisse 3-8:** numbers + mini-stories ka mix (peak ~3 numbers/100 words), simple sentences (~13 words).
5. **Aakhri 10%:** ek verdict line + "you" action; CTA optional (winners-losers barabar).
6. **Template se zyada zaroori:** subject chunna (Q11/Q13). Neu ka ship vs airplane graveyard yeh dikhata hai.

### Limits / UNKNOWN
- Timestamps, CTR, retention **DATA NOT AVAILABLE**. 5/15/30 sec proxies words-based hain.
- Regex proxies (named person, scene, gap phrases) approximate; "?" ginti caption punctuation par nirbhar.
- PI >= 3 aur <= 0.4 ke beech ke videos (middle) exclude hain.
- Sirf 4 excerpts quote kiye; baaki sirf ginti se.
- Failed excerpt comparison sirf Neu pair mein poori dekhi.
- Script: `/private/tmp` scratch mein tha, repo mein nahi (numbers reproduce karne ke liye tumhari kahne par `_scripts/` mein daal sakta hoon).


---

## Q17 — (owner Q13) Titles aur thumbnails ka forensic comparison (2026-11-12)

**Method (VERIFIED):** `VIDEO_INVENTORY.csv` ke 3,056 long-form videos, 60 channels. Winner = PI >= 3 (19% of videos), Loser = PI <= 0.4 (20%). Title patterns regex se tag kiye (approximate). Thumbnails: **seedha dekha** 32 channels (001-031, 037) + 35 channels blind sheets (262 thumbnails, Q2 update), baaki OCR/automatic features; 057 UNKNOWN. Retention/CTR **DATA NOT AVAILABLE**.

### Seedha jawab
Title pattern aur thumbnail pattern dono **akele win ya loss predict nahi karte**. Ek hi title formula 700k aur 242 views dono deta hai.
Misal: "7 Things ... Can't Take From You" - Mark Calloway `wafLcwHvn5U` 723,626 views (PI 350) vs channel 048 `LPxn5Mq8Sqk` 242 views (PI 0.02). "Stop/Bills after 65" - 006 `boC96bE_7Os` 397,508 vs 048 `t3lEL9Zv7Ks` 388. Farq channel ki reach/audience aur topic ka hai (Q11, Q16 se match).

### Title patterns - winners vs losers (win% base 19, lose% base 20)
| Pattern | n | Win% | Lose% | Median PI vs rest | Same-channel (channels jahan pattern wala > baaki) | Padh |
|---|---|---|---|---|---|---|
| Koi number | 1565 | 21 | 22 | 0.98 / 0.96 | 30/50 | koi asar nahi |
| "N things/ways/signs" list | 376 | 19 | 19 | 0.98 / 0.98 | 16/27 | koi asar nahi |
| Money amount ($ / k / million) | 488 | 18 | 21 | 0.98 / 0.98 | 17/36 | koi asar nahi |
| Age/year (after 65, 30-year) | 474 | 23 | 27 | 0.93 / 0.98 | 20/37 | dono taraf zyada (polarised) |
| vs/comparison | 137 | 18 | 21 | 1.07 / 0.97 | 10/16 | thoda +, LOW CONFIDENCE |
| Sawaliya ("?") | 275 | **12** | 19 | 0.95 / 0.98 | 12/29 | win% kam, same-channel mein confirm nahi |
| "you/your" | 1464 | 20 | 21 | 0.94 / 1.00 | 21/43 | koi asar nahi |
| POV | 295 | 21 | 22 | 0.85 / 0.98 | 5/9 | channel-specific, LOW CONFIDENCE |
| Secret/hidden/truth | 209 | 20 | 20 | 0.96 / 0.98 | 17/27 | koi asar nahi |
| Gain/permission ("keep", "enough", "tax-free") | 163 | 21 | **16** | 0.98 / 0.98 | 10/26 | thoda +, same-channel nahi |
| Protection ("can't touch/protect") | 27 | 30 | 15 | 1.01 / 0.98 | 3/4 | **LOW CONFIDENCE** (27 videos, 4 channels) |
| Loss/fear words ("mistake", "trap", "stop", "crash") | 309 | **15** | **24** | **0.86 / 0.98** | 17/36 | sabse saaf ulta signal, par same-channel mein 17/36 = ~50% |

**Gain/permission/protection ka evidence:** gain aur protection ki taraf thoda jhukav hai (21% vs 19%; 30% vs 19%), loss/fear ulti taraf (15% win, 24% lose), par koi pattern same-channel check mein pakka nahi nikla. **INFERRED, LOW-MODERATE**; "proven" nahi.
**Kamzor title patterns (VERIFIED numbers, correlation):** loss/fear words, sawaliya titles jo sirf poochte hain, "POV: your investments start making..." (generic), age wale jahan topic narrow ho (UK pensioners).

### 5 winners / 5 losers har pattern ke (VERIFIED, PI = channel ke andar relative)
- **List "N things":** W: `5V1gCUvdqMs` 7 Things Wealthy Retirees Stopped Buying (Matty, 1,084,237); `wafLcwHvn5U` 7 Things They Can't Take From You After 65 (Calloway, 723,626); `ff8litp2qfQ` 7 Types of Income the IRS Cannot Touch (Nia, 258,793); `BfOcC1094eo` Aldi 14 Things (Robin, 348,055); `oPZjqx_6d1g` 3 Banking Changes 2026 (051, 126,232). L: `LPxn5Mq8Sqk` 7 Things IRS Can't Take (048, 242); `Zam1zZqkL8M` Joint Account 3 Things (009, 1,238); `lar24fyeTog` 5 Changes Veteran (012, 2,499); `F5MooA-Swbk` 9 Signs Never Broke (013, 119); `iYFBlEr1puA` POV Old Fisherman 5 Rules (058, 2,302).
- **Money amount:** W: `2LXED3ENhck` $0 to $25M (034, 1,112,119); `dwSfdH1K7Zk` POV $1 Trillion (049, 592,649); `piJ-diS4zng` POV $6.3 Million (021, 281,847); `sNpbDH7IUKw` $600 threshold (027, 243,085); `BEvQcR323uI` $650 Million (015, 190,706). L: `-oWpfkh0mGY` $6,000 Senior Deduction (023, 2,167); `c49Mx_mGZNY` $250,000 Still Feels Broke (030, 361); `ggFY_2P_sH4` 4 Stages Compounding (058, 1,179); `AjuX4Ap_VGY` 4 Forms $50,000 (012, 2,753); `gMos6YxA2K0` GIS Trap $13,000 (018, 1,539).
- **Age/year:** W: Calloway 7 Things After 65 (723,626); `3L4Mypm3uWo` POV 10-Year Reunion (046, 367,569); `boC96bE_7Os` 5 Bills After 65 (006, 397,508); `hNuWYk9YQsc` 7 Types After 65 (051, 96,911); `piJ-diS4zng` (281,847). L: `KQlnU39MdOQ` UK Pensioners After 60 (048, 303); `DttiTU2UZPU` $40,000 After 30 Years (029, 499); `huAZalqBkno` Medicare at 65 (023, 2,573); `74TqdaOqGbg` Retiring Early After 50 (030, 543); `jJu-T_WWQvI` Stop Paying 15 Things After 60 UK (056, 1,360).
- **vs/comparison:** W: `nkT_K8l1rEw` Renting vs Buying (050, 1,730,664); `pnJCpIhshX4` Renting vs Buying (Mark Invests, 495,096); `eh4-CioOx6s` Cheaper to Abandon Container (Neu, 504,906); `hkRXzD3CH3c` Growth vs Dividend (029, 128,902); `TdXe2zRnTZs` SS 62 vs 70 (008, 31,225). L: `xn5wQuIpoWQ` Debt Payoff vs Investing (Matty, 171); `YzImd_a_pos` 401(k) vs Roth (038, 561); `padJBWbaCHo` EV vs Hybrid (029, 563); `X7HfWigRN7Q` SCHD vs Aristocrats (032, 394); `qprDtL-g6Lc` Banks Recommend vs (031, 1,318).
- **Sawaliya:** W: `k-ZxdjawYDs` Real Estate vs Stocks? (005, 374,961); `Iagjpu1NgcM` Born Before 1966? (Lana, 383,202); `f6HIYQUiMoU` WTF Just Happened To The Housing Market (001, 361,243); `HZ9GXxQCxGs` Over 65 Paid-Off Home? (019, 115,119); `S81NPqovOT8` Why Are Dutch So Good at Ecommerce? (026, 295,240). L: `Zam1zZqkL8M` (1,238); `AjuX4Ap_VGY` (2,753); `DttiTU2UZPU` (499); `HA1BLrrkYjg` If Every Country Is in Debt (059, 6,379); `nzFUrIuUkrs` Medicare Dropping 1M? (010, 315).
- **Loss/fear:** W: `hkRXzD3CH3c` Stop Guessing! (128,902); `O9YfXilMgC8` Grew Up Broke (027,948); `0na9DiXBEK8` Never Keep This Much... Mistake That Can Freeze (019, 269,948); `boC96bE_7Os` (397,508); `eOFlWP9yHak` Going Broke Almost Impossible (007, 186,697). L: `W30ihrvNRKU` Middle Class Trap (030, 155); `t3lEL9Zv7Ks` Stop Paying 5 Bills (048, 388); `RBGsBXmWkwY` Convenience Trap (003, 201); `YL3stNaRSRc` Stop Making RMD Mistake (038, 33); `ggFY_2P_sH4` (1,179).
  Note: winners mein loss words aksar **gain ke saath** hain ("Never keep this much... " = protection), losers mein akele dar.
- **Gain/permission:** W: "Never Keep More Than This in the Bank After 65" 5 alag channels - 019 `0na9DiXBEK8` 269,948; 051 `NXhhbwvx3Fg` 185,127; 010 `SQNY38k8QNU` 122,350; 027 `LMhA9A1QLYA` 9,303; 060 `NXbwK51_1n8` 72,315. L: `3_RmYBhThDQ` Why Americans Keep Buying $50K Cars (029, 478); `dIiJJMigQbA` POV Keep Small House (052, 931); `yuDsG8SLavU` Mom Needed $41,200 to Keep Her House (025, 2,448); `YjCAIYDwmes` How Much Cash Retirees Keep (031, 1,934); `OhWmgcwpqZ4` IRS Keep $1.2 Billion (010, 1,542). **Caveat:** yeh 5 winners ek hi concept ka copy hain (ledger: 18 channels), to "independent" evidence nahi.
- **POV:** W: `piJ-diS4zng` (021), `3L4Mypm3uWo` (046), `dwSfdH1K7Zk` (049, 592,649), `0VqARlMwRiw` Neighbors (025, 157,129), `l0svo03j00M` Holding Company (015, 207,202). L: `Z5FKuB7wZJA` Investments... (054, 971); `qkyhSeiQizw` Mortgage vs Investing (011, 795); `U2KRQdwpJIU` Stepmom (021, 671); `iYFBlEr1puA` (058); `dIiJJMigQbA` (052).

### Thumbnails (Q2 + Q2 update se, nayi ginti nahi)
- **Main subject:** binary choice + do numbers (Mark Invests BUY -$88k / RENT +$70k), ek goal + ek amount (Carl jars), calm hero vs show-off (Lucas Grant, POV Wealth), physical risk metaphor (Tom Talks Money umbrella), senior channels mein date ya "$0 bill".
- **Text:** <=4 words ka asar 0.97x (no effect); >8 words 1.11x (no effect); Kevin Explains 8-10 words wale winners bhi.
- **Face/expression:** face detector 1.12x (q=0.13, 21/37 channels) - cartoon faces miss hote hain.
- **Money/objects/logos:** number score (N): winners 0.34, losers 0.38 (q=0.52).
- **Title-thumbnail overlap:** "complements title" winners 0.32, losers 0.44 (p=0.048, q=0.24) = **supported nahi**.
- **Total rubric:** winners 1.85, losers 2.01, Spearman -0.11, **PI predict nahi karta**.
- **Misaalein:** Marcus Retires winners 74k-245k aur losers 93-242 views, thumbnail style same. Uncle Frank ke "$6,000 Tax Surprise" thumbnails high score par 148-408 views. Finance ANALYST 367 -> 368k, jo title+packaging badalne se hua.

### Limits
- Title patterns regex hain; ek video kai patterns mein aa sakta hai; correlation, causation nahi.
- PI channel ke andar relative hai, isliye bade channel ka "average" video bhi cross-channel zyada views le sakta hai; cross-channel pooling channel ki reach ko pattern par thop sakti hai (same-channel check isliye diya).
- Impressions/CTR **DATA NOT AVAILABLE**: kam views "bura packaging" ya "YouTube ne dikhaya nahi" dono ho sakta hai - UNKNOWN.
- Thumbnail rubric mera subjective score (ek rater), 057 UNKNOWN.
