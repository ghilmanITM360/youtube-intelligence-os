# Codex Brief 2 — How Others Scripted Our Final Topics, Plus a Deep Google Recheck

> **Roman Urdu summary:**
> - **Kaam A:** final topics par doosre channels ne videos kaise banayi, yeh dekhna hai. Editing nahi, **script**: opening, kahani, points ki tarteeb, re-hooks, ending, aur kaun se medical claims ghalat ya bara-chara kar bataye.
> - **Kaam B:** [05 file](05-WINNING-MODELS-AND-FACT-RECHECK.md) ke har fact (F1–F20) aur [06 cards](06-DR-REHAN-TALKING-CARDS.md) ke har "Codex check" ko primary source (paper, guideline, FDA) khol kar confirm karna hai.
> - **Kaam C:** final titles aur thumbnails ko YouTube par check karna hai.
> - Statin long-form online hai, use chhod dein. Sirf statin Shorts ke facts check karne hain.
> - Results `08-...md` mein Roman Urdu mein, aur raw data alag folder mein.

## 0. Context and order of work
- **Read first:** `05-WINNING-MODELS-AND-FACT-RECHECK.md`, then `06-DR-REHAN-TALKING-CARDS.md` (Part A and the card for each topic), then `04-CODEX-VALIDATION-RESULTS.md` §2 (calendar).
- **Pending from brief 1:** take the T0+24h YouTube snapshot on **17 Nov 06:42–06:48 UTC** and fill `yt_24h_delta_top5` in the 03 CSV, as brief 1 specified.
- **Final topics, in recording order.** Do them in this order; the first three are recorded soonest.

| Order | Date | Topic | Card | YouTube queries (add the autocomplete phrasing you find) |
|---|---|---|---|---|
| 1 | 21 Nov | T15 walk after meals | B1 | walking after eating blood sugar · walk after dinner blood sugar seniors · 10 minute walk after meals |
| 2 | 25 Nov | T03 cold medicine + high BP | B2 | cold medicine high blood pressure · decongestant blood pressure seniors · pills that raise blood pressure after 60 |
| 3 | 28 Nov | T04 calcium score | B3 | calcium score after 65 · coronary calcium score explained · calcium score zero statin |
| 4 | 2 Dec | T05 dizzy standing / BP after 65 | B4 | ideal blood pressure after 65 · dizzy when standing up elderly · orthostatic hypotension seniors |
| 5 | 5 Dec | T12 morning heart attack | B5 | why heart attacks happen in the morning · morning heart attack symptoms after 60 |
| 6 | 9 Dec | T07 mini stroke / TIA | B6 | mini stroke symptoms · TIA warning signs elderly · warning stroke |
| 7 | 12 Dec | T08 walking speed | B7 | walking speed after 60 · gait speed life expectancy · how fast should a 70 year old walk |
| 8 | 16 Dec | T09 calf pain / ABI | B8 | calf pain when walking · poor leg circulation after 60 · ankle brachial index test |
| Shorts | 19 Nov–15 Dec | T10, T14 + statin Shorts | Part C | silent heart attack symptoms · blood pressure medication recall · statins after 70 |

**Seed videos already in the repo** (`senior_health_core.db` + transcript DBs on `origin/research/senior-health-apify-2026-11-11`). Include them, read their transcripts from the DB, and re-check their current views. Clone family (synthesis §2: 04/06/09/31/32/33) = **one** data point.

| Topic | Seed IDs (views at DB snapshot) |
|---|---|
| T15 | `oD22jpWirB0` Waterling 778K · `RizcPYWs3IQ` Waterling 354K |
| T03 | `ML_f1bVqiZk` Ares 647K · `UmNTryXlgR0` Atlas 166K · `SC6UKDSQsdU` Hargrove 131K · `B7LeyE4K1eg` Nora Khalil 64K · BHWA `R7uXQBjnTjk` 665K (real clinician) |
| T04 | `29bCvmQTwuM` Hargrove 967K · `Z0PP5eBKaWA` Dr Thomas 414K · `VIjreQgk7SE` Parker 210K · `u8qKy7P7Wx8` Ares 63K |
| T05 | `xk_lyMuLevE` Waterling 458K · `nGtzJ9a3bk8` Parker 352K · `8_depH-gT4o` BHWA 330K · `nno8iS887Xo` Ares 267K |
| T12 | `H3nD5WnBhH4` Parker 269K · `225EhTo273s` Elias 217K · `raoN4tf21ic` Mitchell 23K |
| T07 | `dyft-l78b04` Waterling 2.19M · `tURIDup-bYQ` Parker 1.22M |
| T08 | `fu70r63mo7A` Waterling 1.25M · `UGmIU2dS5zc` Doctor Thomas 1.0M |
| T09 | `7tXXgqrmji0` SeniorHood 1.07M · `vaM_lAcnJJ8` Body Fix 616K |
| T14 | Codex brief-1 hit `t0FllVY2Fio` 505K · Jeremy London, MD (real clinician, from your 03 CSV) |

## 1. Rules (AGENTS.md, same as brief 1)
1. No YouTube Data API and no paid tools. Use the public website, logged out or incognito. Record the region you see; brief 1 showed `PK`. If you can, also run a US-region pass (e.g. `&gl=US&hl=en` in the URL) and label which is which.
2. **Raw evidence:** new folder `data/raw/channel-data/dr-rehan-script-research-<YYYY-MM-DD>/` with `README.md` and `SHA256SUMS.txt`. Never edit existing raw folders.
3. Label every number OBSERVED / INFERRED / NOT VERIFIED.
4. **Transcripts:**
   - Capture them via the public "Show transcript" panel or the repo DB, for internal analysis only.
   - In the results file, **summarize structure in your own words**; quote at most one short line (under 15 words) per video.
   - Never copy a competitor's wording into a card.
5. Don't edit 01–06. Put proposed changes to titles, cards or facts in `08-...md` as a "change request" table.
6. Medical content: you check sources; Dr Rehan decides.

## 2. Task A — Script research (YouTube)
**Pick 6 videos per long-form topic:**
- The seed IDs above (top 2–3 by current views, clone family counted once)
- The top 2 from "This year" search (Upload date = This year, Sort = View count) not already in the seeds
- At least **1 real clinician** (named, verifiable: BHWA, a hospital channel, a named MD with public registration)

For Shorts topics (T10, T14, statin), pick 3 Shorts each.

**For each video, fill one row of `09-script-map.csv` (new file):**

| Column | What to capture |
|---|---|
| `topic_id`, `video_id`, `channel`, `channel_type` | channel_type: CLONE / REAL-CLINICIAN / INSTITUTION / PERSONA-UNVERIFIED |
| `views_now`, `published`, `duration`, `word_count` | OBSERVED |
| `delivery` | READ-SCRIPT / CONVERSATIONAL / AI-VOICE. Signals: filler words, self-corrections, repetition, synthetic voice |
| `opening_type` | scene / patient-story / stat / what-if / credential-first / fear-insider / question (Report 2 K.4 types) |
| `opening_summary` | First 30 seconds in your words: what the line does, and what question it plants |
| `story_used` | none / composite-unnamed / named-real / presenter-personal. Where it appears (% of runtime), and whether the ending is held back |
| `analogy_used` | The main everyday comparison, if any |
| `spine` | e.g. "5-item list", "myth → truth", "timeline", "Q&A". Count the sections |
| `rehooks` | Count, plus one example line in your words, plus average interval |
| `payoff_position_pct` | Where the main promise is paid (% of runtime) |
| `red_flag_section` | yes/no, and does it say "call emergency services"? |
| `doctor_questions` | Does it give the viewer questions to ask? yes/no |
| `cta_positions` | Early / mid / end, and what kind (subscribe, comment number, next video) |
| `sources_named` | Guidelines or studies named on air (list) |
| `claims_flag` | Any claim that is wrong, overstated or contradicts the guideline in 05 (e.g. "drops sugar 52%", "signs the day before a stroke"). Short note + the guideline it conflicts with |
| `title_promise_match` | yes / partly / no |
| `thumbnail` | Visible text (exact words), face (real/AI/none), main object, colours, number shown, answer shown or hidden |
| `gap_for_rehan` | One line: what this video does not do that a real cardiologist could (e.g. "no standing-BP how-to", "no emergency line") |

**Then, per topic, write in `08-...md`:**
1. **What the top videos have in common:** structure, story type, length.
2. **What they get wrong or leave out:** the claim flags, plus the gaps.
3. **Card check:** does Dr Rehan's card (06) already cover the gap? If not, give one suggested beat change, in your words.
4. **Best opening scene:** pick 1 of the 3 openings you saw that would work for the card, or propose your own. Not copied.

**Cross-topic summary:**
- How many winners are conversational vs read scripts?
- Do real clinicians use patient stories?
- What view range do real clinicians reach on these topics vs clone channels?

Label this as INFERRED; n is small.

## 3. Task B — Deep Google recheck (primary sources)
For **every row F1–F20 in 05 §2** and **every "Codex check" in 06**:
1. Open the **primary** source: the journal article or abstract on PubMed/journal site, the guideline text (JACC/Circulation), the FDA page or the label.
2. Record the exact number and wording in your own words, the URL and the access date.
3. Give a verdict:
   - **CONFIRMED:** card text is fine
   - **CORRECT-IT:** give the corrected number or wording
   - **UNSUPPORTED:** remove from the card
   - **NEEDS-QUALIFIER:** give the qualifier

Specific checks:

| Item | What to find |
|---|---|
| F1 Reynolds 2016 | Diabetologia: n, age, the comparison, the % reduction and in what measure (postprandial glycaemia) |
| F2 DiPietro 2013 | Diabetes Care: population (age, glucose status), the exact comparison |
| F5 | The 2005 pseudoephedrine meta-analysis: citation and the SBP/DBP/HR effect, including in hypertensive subgroups |
| F6 phenylephrine | FDA OTC monograph page: is there a **final order** as of today? Effective date? |
| F7 CAC | 2026 ACC/AHA lipid guideline: exact recommendation wording for 40–75 and >75, CAC score bands used (0, 1–99, ≥100?), repeat-scan interval if stated |
| F9 BP guideline | 2025 AHA/ACC: target wording for older adults, and the orthostatic hypotension recommendations |
| F10 Muller 1985 | NEJM 313:1315: confirm the 6 am–noon peak, n, and the beta-blocker finding |
| F12 TIA | AHA/ASA statement figures for 48 h and 90 days; choose the number the card should use |
| F14 Studenski | JAMA 2011: HR per 0.1 m/s, and the 0.8 and 1.0 m/s statements |
| F15/F16 PAD | 2024 guideline: ABI categories, supervised exercise wording, how long an ABI test takes |
| F17 silent MI | Best AHA-published estimate (2016 Circulation ARIC; any 2023 AHA figure) |

Also check these (from 05, "Abhi verify nahi hue"):
- older-adult physical activity guidance
- the decongestant nasal spray day limit on the label
- BP and prostate drug classes that cause orthostatic drops
- the AHA hypertensive crisis wording and threshold
- current guidance on not giving aspirin at home for suspected stroke
- AHA guidance on aspirin advice from emergency dispatchers for a suspected heart attack

**Fresh news per topic since 16 Nov:** Google News for the past 7 days, plus FDA recalls and safety communications, AHA and ACC newsrooms. In particular:
- new BP or statin recalls
- recall status on 19 Nov for the T10 Short
- any phenylephrine final order

## 4. Task C — Titles and thumbnails
1. Search each **title #1** from 06 on YouTube.
   - Is there an identical or near-identical title already? Then propose title #2 or #3.
   - Record the first 5 autocomplete suggestions for each title's key phrase.
2. For each topic, write in your own words the text and layout of the **top 3 thumbnails** from Task A.
   - Does our thumbnail prompt in 06 stand out from them? If it looks the same, propose one change.
3. No image downloads beyond what the transcript or page view already shows; describe thumbnails in text.

## 5. Deliverables
1. `docs/research/dr-rehan-content-plan-2026-11-16/08-CODEX-SCRIPT-RESEARCH-RESULTS.md` in **Roman Urdu**:
   - per-topic script findings and the card check (Task A)
   - fact verdict table F1–F20 plus the extra items (Task B)
   - title and thumbnail notes (Task C)
   - one **change request table**: card / line / current / proposed / reason / source
   - limits: region, sample size, logged-out personalization, transcripts missing
2. `docs/research/dr-rehan-content-plan-2026-11-16/09-script-map.csv` (Task A rows).
3. Raw folder `data/raw/channel-data/dr-rehan-script-research-<date>/` with README and SHA256SUMS.
4. Also update `03-topics-for-validation.csv` **only** for the brief-1 24h columns.
5. Commit on the current branch with only these files.

**Time budget:** topics 1–3 (T15, T03, T04) and all of Task B's F-rows first, because they are recorded first. Then 4–8. Then Shorts.
