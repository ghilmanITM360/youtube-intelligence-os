# Opening-line test: kya "claim/number-first" opening strong videos se juda hai? (2026-11-13)

Labels: VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN. Is file ka kaam: handoff item 2 (transcript openings ko ginti ke saath test karna).

## 1. Kya kiya (VERIFIED)
- Source: `data/catalog/finance_economics_complete.db` (read-only). 7 channels (Monkey, Casual Finance, Crayon, Economics Explained, Primate, Capital Case, Nutshell), sirf long videos (>=180 s) jinka transcript DB mein hai: **181 videos**. PENNY aur Paper Billions DB mein nahi, transcript nahi -> is test mein **shamil nahi** (UNKNOWN).
- Har video ke pehle 150 words (~60 s) nikaale. Har channel ke andar views se top-third = STRONG (S), bottom-third = WEAK (W), beech ka = MID (M).
- Maine S aur W ke ~120 hooks (pehle ~38 words) khud parhe; phir rule-based label sab 181 par lagaya (rule `_scripts/opening_test_2026-11-13.py` ke docstring mein). Label **automatic hain, human-blind nahi** (INFERRED).
  - STAKE = pehle 30 words mein digit/$/%/year/million-billion-trillion, aur persona-start nahi.
  - PERSONA = "This is <Naam>...", "Meet...", "<Naam> is <umar>", "Monkey ...", "What is/are...", "Close your eyes".
  - OTHER = baaqi (general bayan, sawal, mazaq).
- Files: `_analysis/openings_150w_2026-11-13.csv`, `openings_tiered_...csv`, `openings_labeled_...csv`, `opening_test_output_2026-11-13.txt` (SHA-256 neeche).

## 2. Table (VERIFIED counts, label rule INFERRED)

| channel | n | STAKE n (S/W) | PERSONA n (S/W) | OTHER n (S/W) | STAKE median views / channel-median | non-STAKE median |
|---|---|---|---|---|---|---|
| Casual Finance | 33 | 14 (8/1) | 3 (0/3) | 16 (3/7) | 1.54 | 0.76 / 0.19 |
| Crayon | 30 | 25 (9/6) | 4 (1/3) | 1 (0/1) | 1.21 | 0.40 |
| Capital Case | 13 | 11 (4/2) | 0 | 2 (0/2) | 1.59 | 0.10 |
| Nutshell | 14 | 12 (4/2) | 2 (0/2) | 0 | 3.04 | 0.14 |
| Economics Explained | 30 | 12 (4/4) | 1 (0/1) | 17 (6/5) | 1.00 | 1.01 |
| Primate | 16 | 1 (0/0) | 15 (5/5) | 0 | n/a | 0.99 |
| Monkey | 45 | 0 | 43 (15/15) | 2 (0/0) | n/a | 1.01 |
| **Pooled** | 181 | 75 (29/15) | 68 (21/29) | 38 (9/15) | 1.27 | 0.72-0.77 |

Permutation test (label channel ke andar 5,000 baar shuffle; statistic = mean log(views / channel-median) STAKE minus non-STAKE; one-sided):
- 7 channels pooled: +0.64, p < 0.001. Monkey ke bina: +0.77, p < 0.001.
- Alag alag: Casual Finance +1.12 (p=0.001), Crayon +1.12 (p=0.03), Capital Case +2.54 (p=0.025), Nutshell +3.06 (p=0.06), Economics Explained -0.14 (p=0.74), Primate +0.76 (p=0.39, sirf 1 STAKE video, bekaar).
- Monkey: 43/45 openings ek hi template ("This is X and he's got a huge problem"), isliye opening se kuch alag nahi hota; strong aur weak dono mein wahi (15/15).

## 3. Isse kya nikalta hai (aur kya NAHI)
1. **INFERRED, MEDIUM-LOW:** 4 channels (Casual Finance, Crayon, Capital Case, aur kamzor tareeqe se Nutshell) mein jo video pehle 30 words mein koi number/tareekh/bara stake rakhti hai, wo apne channel ke median se zyada chali. Ye pichli line ("sirf Casual Finance/Primate mein ishara") se **zyada mazboot** hai, kyunki ab 181 videos par ginti hai.
2. **Economics Explained mein koi asar nahi** (p=0.74) aur Monkey mein template ek hi hai. Yani rule har channel par nahi lagta.
3. **Ye opening ka asar saabit nahi karta.** Do wajah: (a) topic confound: jis topic ka bara number hota hai (SpaceX $1.75T, 58% housing gap) wo topic hi bara hota hai; opening aur topic alag nahi kiye ja sakte. (b) Studio retention/CTR UNKNOWN hai, to "opening ne viewer roka" yahan naapa hi nahi gaya. Age confound bhi hai (Economics Explained ke publish dates DB mein nahi).
4. Weak taraf ka pattern jo text se saaf parha gaya (VERIFIED text): Casual Finance ke weak 11 mein se 7+ mazaq/persona/sawal se shuru ("Meet Dave", "Wall Street, a place where...", "Let me ask you a question", "Ah, 2025"); Nutshell ke 4 weakest sab **banawati (invented) kirdaar** se shuru (Lisa, Linda, Frank, Gary), jabke uske top-2 asli naam/waqia (Sinaloa cartel, Ronald Read). Magar Nutshell mein 2 invented-kirdaar videos (Ry, Paul) strong tier mein bhi hain (32-36k), to ye ishara hai, rule nahi.
5. Rule-based label ki kamzori: Nutshell ke Linda/Gary jaise invented-persona openings ko rule ne STAKE/OTHER mein daal diya (date ya $ ki wajah se). Isliye Nutshell ka row sirf andaza hai; asli test human-blind relabel maangta hai (agla qadam).

## 4. Launch model par asar (HYPOTHESIS)
Opening line ab bhi hypothesis hai magar pehle se behtar support: **pehle 15 s mein asli tareekh/naam + ek bara number + viewer ka stake; invented kirdaar, mazaq, "Meet X", ya sawal se shuru nahi.** Kill rule: agar apne pehle 10 videos mein STAKE-opening aur non-STAKE-opening ka median views ka farq 1.0x ke aas-paas rahe (jaise Economics Explained), to opening ko lever mat maano.

## 5. Abhi bhi NAHI hua
PENNY/Paper Billions transcripts; human-blind relabel; Studio retention; age-controlled version (publish dates ke saath views-per-day).

## SHA-256 (2026-11-13)
```
dede9ee25606f12b921e51c7b70007fd61bf66a0c6441a0f4f12bae22211f51e  openings_150w_2026-11-13.csv
94d64ee5766c0c9b294fce93ea36658d7f06279cb9caf2296c6d4f9a7fde543c  openings_labeled_2026-11-13.csv
418cf72b8abe114a5b38d920cc5e63363ff6db95de5cf5ad7a01ab4485919153  openings_tiered_2026-11-13.csv
6c0ba485c511ce5b3d31627f3bc1f3c330b69991eee65b28e0e55672f4288eca  opening_test_output_2026-11-13.txt
```
