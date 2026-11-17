# 9-channel live comparison + one launch model (2026-11-13)

Labels: VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN. Source = the nine `LIVE_EVIDENCE_2026-11-13.md` files (Chrome + vidIQ + Trends + web; DB or Apify numbers). Studio CTR, retention and traffic-source split are UNKNOWN for all nine. This file is a synthesis of those reports; it was not re-checked against the DB. It does not replace `FINANCE_ECONOMICS_WINNING_MODELS.md`, which still needs to be reconciled with it (not done).

## 1. Nine channels, ek table (numbers as written in each report)

| # | channel | subs (live) | videos seen | views range / median | channel age | main format |
|---|---|---|---|---|---|---|
| 024 | MonkeyExplains | 261k | 15 of 48 long (DB 63) | 88k–1.92M; DB median 348k | 2025-05 onwards | gorilla cartoon, 6–16 min |
| 037 | Casual Finance | n/a here | 15 of 33 long (DB) | DB median 485k; 16/33 at 500k+ | 2025-07 onwards | stick-figure + real charts, ~15 min |
| 039 | Crayon Capital | 304k | 15 of 30 | 40k–4.2M (live); DB median 250k | 2025-04 onwards | crayon cartoon ELI5, 10–21 min |
| 040 | Economics Explained | 2.89M | 15 of DB's 30 (live 457 videos) | 149k–1.5M; DB median 546k (sample) | 2012 | narration + stock/data, 13–23 min |
| 055 | Primate Economics | 577k | 15 of 17 long | 2025 median 980k; 2026 median 162k | 2022 | banana-monkey allegory, 2–12 min |
| 059 | Capital Case | 11.9k | 13 of 13 (whole channel) | 5.1k–380k; median 54k | 2026-02 onwards | 2D cartoon, 9:31–11:59 |
| 066 | Econ in a Nutshell | 4.87k | 14 DB (live 17) | 2.7k–1.04M; 2 videos = 90.7% of views; rest median ~3.1k | ~3 weeks (first upload 2026-10-25) | stick-figure animation, ~9–10 min |
| 070 | PENNY | 7.83k | 13 of 13 long (+5 Shorts) | 3.3k–1.15M; median 13k; 1 video = ~74% of views | ~4 weeks (joined 2026-10-16) | coin-head cartoon ELI5, 6–17 min |
| 071 | Paper Billions | 14.1k | 4 of 4 | 144k–2.1M; median ~807k | videos 2026-11-06 to 11-13 (join date 2022 UNKNOWN meaning) | drawn-on-paper, 14–20 min |

Coverage is not equal: three of the nine (Capital Case, PENNY, Paper Billions) are whole channels; the others are 15-video samples. 070 and 071 are not in the 69-channel DB, but earlier Apify spot scrapes (2026-11-12: PENNY 13 of 18 videos, Paper Billions 3 of 3) exist in `05_OWNER_QA/`; this pass supersedes them (PENNY 18/18, Paper Billions 4/4). Reconciled with `FINAL_RESEARCH_CONCLUSIONS.md` (section A1-A7) and `FINANCE_ECONOMICS_WINNING_MODELS.md` (section D) on 2026-11-13.

## 2. Jo baat kai channels mein baar baar mili (VERIFIED numbers, INFERRED explanation)

1. **Format akela jeet nahi deta, topic/framing ka farq bara hai.** Same template, bohat alag views: Capital Case "Explained in 11 Minutes" 33k–380k; PENNY ELI5-titled 3.3k–1.15M; Crayon ELI5 40k–4.2M; Casual Finance pair 1.28M vs 48k (same style, 14 din ka gap); Economics Explained 149k–1.5M. 6 mein se 6 channels jahan 5/5/5 dekha gaya, template ke andar poora phailao hai. Confidence MEDIUM.
2. **Strong videos zyadatar bara, pehle se mashhoor ya khabar mein chal raha event hain jo viewer ke paise se juda ho.** Capital Case: Rockefeller, Great Depression, Hormuz, WW2, BYD (150k–380k, 11.9k subscribers par). Casual Finance: Tokyo bond yields, SpaceX IPO, housing. Crayon: Wolf of Wall Street 4.2M, Depression 3M, 2008 2.3M. PENNY: "$40T kis ko dena hai?" 1.15M. Paper Billions: Nvidia, stock market crash. Monkey: national debt, OpenAI, SpaceX, Epstein. MEDIUM-LOW (selection by me from 4 hafte se 15 mahine ke mixed-age videos).
3. **Weak videos mein abstract sawal, institution, ya company ki puri tareekh zyada hai.** Capital Case: debt "who owns the money", bread, FTX, BlackRock (5k–6k). PENNY: Fed kis ka hai 3.3k, "paisa kahan se aata hai" 9.4k. Crayon: slave-system essay, WW2 repeat. Primate: 401k, options, ponzi. Casual Finance: Private Credit, oil "secretly good". Ye pattern 5 channels mein dikha, exceptions bhi hain (Economics Explained ka "Economics is a Junk Science" 1.2M abstract hai, Paper Billions mein "lost $80B" jaisa company-nuqsan 144k hai lekin fail nahi).
4. **vidIQ engagement % strong aur weak ko alag nahi karta.** Capital Case, Monkey, Crayon, Economics Explained, PENNY, Paper Billions: sab mein weak ka engagement strong se kam nahi (kai mein zyada). Ye engagement ko selection metric ke taur par rad karta hai. VERIFIED (6 channels).
5. **[2026-11-13 update: 181 transcripts par ginti ke baad dekho `OPENING_LINE_TEST_2026-11-13.md`: number/tareekh/stake-first opening Casual Finance, Crayon, Capital Case (p<=0.03) mein apne channel median se upar, Economics Explained mein koi asar nahi, Monkey ka template ek hi; topic confound baqi, INFERRED MEDIUM-LOW.]** Pehle ka note: Opening style ka asar mixed hai, sirf do channels mein ishara. Casual Finance: strong 4/4 claim-first, weak 4/4 joke-first. Primate: concept-first (Tax 1.56M) vs skit/boring-joke (401k 119k). Magar Monkey, Crayon, Capital Case mein opening strong aur weak dono mein same (date/number ya "huge problem" formula), to akela rule nahi. HYPOTHESIS.
6. **Repeat topic chhota hota hai.** Monkey: Epstein 838k → doosri video 137k; OpenAI 587k, 456k, 224k. Crayon: WW2 video Depression ki kahani dohrati hai (67k vs 3M). PENNY: ek hi $40T topic ke 3 angle 1.15M / 13.6k / 3.3k, yani angle bhi bara farq hai. MEDIUM-LOW.
7. **Trends views ko rank nahi karta, magar ek jagah topic-interest ne madad ki.** Monkey, Crayon, Capital Case, Economics Explained, Primate mein kam search-interest wale topic bhi bare chale. Econ in a Nutshell: money laundering (≈62) 1.04M vs "Social Security 2032" (≈0) 2.7k, magar Vancouver real named case sirf 26k. Trends sirf topic-interest hai; traffic source UNKNOWN. Mixed.
8. **Age/channel-size/topic alag nahi kiye ja sakte, har channel mein.** Capital Case ke 4 weakest sabse purane (channel tiny); PENNY ke 4 weak 5–9 din purane; Casual Finance ke 5 weak sab Aug 2025–Feb 2026 (channel chhota); Crayon BYD DB 98k → live 287k; Monkey 2025 median 466k vs 2026 292k. "Weak" ko final na maano.
9. **Hit concentration.** Econ in a Nutshell: 2 videos = 90.7%; PENNY: 1 video = ~74%. Channel-level "model" in dono ka lagbhag ek hit hai; isse repeatable system nahi nikalta.
10. **Retitle/re-thumbnail aam hai.** Crayon 6 videos, Casual Finance 5 weak, Econ in a Nutshell (khud weak videos ko retitle), PENNY ASML. DB ke purane titles par judge karna risky hai; asar UNKNOWN.
11. **Sponsor/Shorts engine nahi.** Primate ke 2 weak mein sponsor; Crayon ki ek strong video mein sponsor, to sponsor akela wajah nahi. Shorts: PENNY ke 5 Shorts 145–1,618 views; Econ in a Nutshell mein Shorts nahi; Primate ka "Shorts-first" claim live check mein galat nikla.

## 3. Jo cheezein 9 channels ke baad bhi saabit NAHI hui
- Kaun si opening/title/thumbnail click ya retention badhati hai (Studio ke bina UNKNOWN).
- Kya koi bhi format naye channel par transfer hota hai: Monkey (261k), Crayon (304k), Economics Explained (2.89M), Primate (577k) ke paas bara subscriber floor hai (Casual Finance ka size is report mein nahi); sirf Capital Case (11.9k), PENNY (7.8k), Paper Billions (14.1k), Econ in a Nutshell (4.9k) chhote hain, aur inmein se 3 (PENNY, Paper Billions, Nutshell) sirf 1–4 hafte ke data par.
- Creator/team/production workflow: kisi bhi channel ka web par nahi mila (Economics Explained ka host naam third-party listing se, sources conflict).

## 4. Ek launch model (HYPOTHESIS, testable; naya channel, original packaging, koi copy nahi)

**Promise:** "Ek asli, tareekh wali ghatna jo aapke paise se juri hai, ek hi kahani mein 11–14 minute mein."

**Topic rule (sab 9 se jo sabse zyada baar dikha):**
- Ek asli, naam/tareekh wali ghatna, jo ya to pehle se mashhoor ho ya abhi khabar mein ho, aur seedha viewer ke paise (qarz, ghar, retirement, naukri, daam) se jure.
- Ek video = ek topic. Institution ("Fed kis ka hai"), abstract concept ("paisa kahan se aata hai") aur company ki puri tareekh pehle 10 videos mein nahi.
- Topic ki demand jahan mumkin ho YouTube Search Trends se dekho (head term), magar Trends ko selection ka akela rule mat banao (point 7).

**Opening (pehle 15 s):** asli tareekh ya naam + ek bara number + viewer ka nuqsan/stake. Joke, skit, invented kirdaar, sponsor, "boring" disclaimer nahi. Support: 181-video opening test (OPENING_LINE_TEST_2026-11-13.md), association hai, causal nahi. Kill rule: STAKE aur non-STAKE openings ka median farq ~1.0x rahe to opening ko lever na maano.

**Format:** ek hi visual character system (kisi aur channel ka character copy nahi), 11–14 min, kam se kam ek asli source chart/screenshot screen par (Casual Finance ke strong videos ka pattern).

**Pehle 10 videos ka plan (test, guarantee nahi):**
1. 8 alag asli ghatnayen (viewer-paisa se juri), har ek ek video.
2. Un mein jo sabse acha chale uske 2 alag angle (PENNY ka $40T sabaq), 14 din ke baad.
3. Har video ka title/thumbnail change timestamp ke saath likho, warna asar alag nahi hoga (point 10).
4. Shorts pehle 10 videos tak mat banao (point 11), sponsor nahi.

**Faisla kab:** apne channel ke apne median se. Agar 10 mein se koi bhi video apne pehle 3 videos ke median ka 3x na kare (Studio CTR + 30 s retention ke saath), to ye model kamzor hai; agar 1 video bhi 10x kare, usi topic-framing ko dubara test karo, pehle ye na maano ke repeat hoga (point 9).

**Is model mein jo UNKNOWN hai:** Studio data, channel size ka asar, kya "ghatna + viewer-paisa" asli wajah hai ya sirf hamare chunav ka asar (selection bias, MEDIUM-LOW), aur kya 11–14 min sahi length hai (6 channels ke strong 10–20 min dikhte hain, magar length confounded hai).

## 5. Agla qadam (owner ke faisle par)
- Baqi 60 channels ki live pass ya sirf is model ke 10 videos ka test shuru karna.
- Is file ko `FINANCE_ECONOMICS_WINNING_MODELS.md` aur `FINAL_RESEARCH_CONCLUSIONS.md` se reconcile karna (3 overstated lines abhi unedited hain).
