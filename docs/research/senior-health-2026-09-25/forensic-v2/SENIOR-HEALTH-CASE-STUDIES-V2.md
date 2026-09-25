# Senior Health Forensic Case Studies — V2 (actual evidence)

**Date:** 2026-09-25 · **Supersedes:** `../SENIOR-HEALTH-CASE-STUDIES.md` (kept unchanged; its errors are listed in `DATA-QUALITY-CORRECTIONS.json`)

**Evidence rules used here**
- Facts (dates, durations, views, medians) come from `VERIFIED-FACTS.json`, which re-queries `data/catalog/youtube_channel_registry.db` and the raw Apify files.
- Script quotes are from the stored transcript text. Stored transcripts have no timestamps, so every time is labelled **APPROXIMATED_FROM_WORD_POSITION**: word index × (duration ÷ word count).
- Thumbnails are labelled **LIVE_WEB_VISUAL**: I looked at each one in a browser on 2026-09-25. The `#n` numbers refer to `THUMBNAIL-MATRIX.json`.
- Google Trends values are **LIVE_GOOGLE_TRENDS** (`GT-xx`, see `TRENDS-REGISTER.json`). They are relative interest on a 0–100 scale, not search volume.
- External videos are **LIVE_WEB_SEARCH_RESULT** (`external/*.txt`).
- Causation is never proven. We have no CTR, retention or traffic-source data for any of these videos.

| # | Case | Category |
|---|---|---|
| 1 | Dr. Okoro: "9 Foot Signs of Hidden Diabetes" | Top relative breakout (2,485x) |
| 2 | Senior Health Hub: the clove franchise (3.09M) | Top absolute breakout, trend-amplified, series |
| 3 | Doctor Thomas walking cluster and its copies | Evergreen, duplicate divergence |
| 4 | Dr. Ares ↔ Dr. Elias twin network | Duplicate-script divergence, sister-channel inversion |
| 5 | "Dr. Aliza Wright" on two channels (941K vs 160) | Duplicate divergence, persona clone |
| 6 | Okoro neuropathy follow-up (100.9K) | Trend-amplified, copied external winner |
| 7 | "What a stroke looks like the day before": 3 channels, 3 failures | Unexpected failure, replicated |
| 8 | Fit Lit Health | Small-channel external breakout |
| 9 | Bathing after 60 | Evergreen browse topic with no search demand |
| 10 | Matched pair 20: tongue vs face, one day apart | Matched-pair contrast, the cleanest control |
| 11 | TopHealthTips: hit, cluster, decay | External series lifecycle |

---

## 1. Dr. Okoro: "Cardiologist Warns: 9 Foot Signs of Hidden Diabetes After 60" (CJxCjygEnmo)

**Verified facts:** uploaded 2026-05-16. Duration 911 s. 494,473 views, which is 2,484.8x the channel's all-video median of 199 (the recent-10 median is 75). Channel joined 2026-03-19 with 3,800 subscribers at scrape. First upload was 2026-03-20. This was the channel's 26th upload (58 days after joining). 40 uploads followed it. Transcript: `data/raw/competitors/DS-000028/.../transcripts/CJxCjygEnmo.txt`, 3,042 words. Thumbnail: `i.ytimg.com/vi/CJxCjygEnmo/maxresdefault.jpg`.

**Actual script structure** (times are APPROXIMATED_FROM_WORD_POSITION):
- **0–10 s, direct command:** "Stop what you're doing for 30 seconds and look down at your feet."
- **~10–60 s, patient case:** "Walter, 71 … retired plumber from Ohio … fasting glucose 218 … A1C 9.2 … a full-blown diabetic for at least 2 years."
- **~60 s, authority:** "I'm a heart surgeon … 20 years." The title says "Cardiologist". The ASR spells the presenter's name "Acuora"/"Acord".
- **Reframe:** "Diabetes is not really a sugar disease. It is a vascular disease … the vessels that fail first … your feet."
- **~96 s, two open loops:** "sign number five is the one almost nobody connects … sign number nine is the easiest to see."
- **~105 s, first payoff** (sign 1). After that, about 250 words per sign through sign 9 (~700 s).
- **Close:** hope ("manageable condition"). CTA: "share it on Facebook right now and tag one person you love who is over 50", then subscribe, a disclaimer, and "I will see you in the next video."
- **Counts:** medical claims 7, credibility cues 4.3 per 1,000 words, story 1.0 per 1,000 words.

**Thumbnail (#93, LIVE_WEB_VISUAL):** the doctor persona in teal scrubs, pointing. A foot photo inset with a yellow arrow. Text: "YOUR FEET WILL TELL / YOUR SUGAR / IS DAMAGING YOU". Red background. The answer is withheld.

**Trends:** "diabetes feet" (US, 5 years) was already elevated in the 90 days before upload (72.8). The upload week was 75, the 90 days after were 74.1, and the 5-year peak came on Jun 7–13 (GT-05). At daily resolution the curve is flat around the upload (58.8 → 61.4 → 61.2, GT-27). The control term "signs of diabetes" is flat (GT-06). **No trend trigger.**

**Historical context:** none relevant found.

**External (C03):** Cleveland Clinic 432K and Doctor O'Donovan 316K cover diabetic feet accurately. At least six channels later copied the title almost word for word ("Cardiologist Warns_ 9 Foot Signs…") and got **2, 5, 7, 9, 20 and 53 views**. Dr. Ares's "9 Warning Signs in Your Feet" got 20,687 (0.45x) and reused the thumbnail text "YOUR FEET WILL TELL YOUR SUGAR…" (#59).

**Follow-ups:** "5 Medical Tests That May Be Unnecessary" came out the next day (8.0x). Neuropathy exercises followed on day 18 (100,852, 507x; see case 6), then kidney vegetables on day 20 (11,319, 57x). The kidney video ends with a bridge to this breakout. After that the channel copied the *form* of the breakout ("9 Skin Signs of Hidden Diabetes" 205, "8 Signs Your Feet Have Diabetic Nerve Damage" 460), and the recent-10 median decayed to 75. Facebook-share CTAs appear in 16 Okoro videos, starting with this one. None of the other 15 passed 2,000 views, so that CTA is not sufficient.

**Medical:** foot signs are complications seen in people who have diabetes. They are not validated diagnostic signs of hidden diabetes (MV-02 PARTIAL). The script's line "long before any blood test catches the problem" is UNSUPPORTED (MV-01). Nerve damage usually appears years after onset, and diabetes is detected by an A1C test.

**What the evidence supports:** the opening combines a body check the viewer can do right now, a concrete case with lab numbers, and a withheld list. The same opening shape in the later form copies did not repeat the result. Pass-1 said "luck more than formula". That is too strong, because a second hit followed within 18 days. The replicable part was an adjacent topic (neuropathy), not the title shape.

---

## 2. Senior Health Hub: "Put 1 Clove in Coffee… What Happens 10 Minutes Later Is Shocking" (KPigGh9_gbU) and the clove franchise

**Verified facts:** uploaded 2026-04-28. Duration 542 s. 3,088,021 views (323.7x a median of 9,539.5). 1,307 words. The channel joined 2025-09-13 and had 160,000 subscribers at scrape. **This was the channel's 24th clove upload and its fourth clove hit, not a novel one-off:**
- qUSMccJH_bM, 2025-09-17: 1,090,015
- xF0xfmUsSB4, 2026-01-31: 1,055,564
- UY7FY-kcrAs, 2026-02-12: 554,619
- **The franchise is 41 clove videos out of the channel's 122 (34%), and they hold 73.1% of channel views.** 14 of the 41 reached ≥3x. The median clove video is 1.52x, against 0.65x for non-clove videos (19 of 81 non-clove videos reached ≥3x).
- Other hits: 326K, 290K, 173K, 144K, 117K, 107K, 97K. Misses include 2,255 ("Drink Clove Water Before Bed…", 2025-11-22), 3,315, 3,511 and 7,141.
- **SHH's own direct repeats of the 3.09M format failed:** "I Added 2 Cloves to My Coffee Every Morning for 7 Days" 12,918 (1.35x), "Drop 1 Clove Into Warm Milk Tonight — What Happens in 10 Min" 8,694 (0.91x), "I Tried Adding Cloves to My Coffee for 30 Days" 9,418 (0.99x), and "Put 1 Garlic Clove in Honey… What Happens 10 Minutes Later" 5,107 (0.54x).

**Actual script:**
- **Opens with an anti-pharma conspiracy:** "Your doctor will never tell you this. Billion-dollar supplement companies are hoping you never find out."
- **Cost and habit:** "one single clove… less than 10 cents… your morning cup of coffee… you've probably been doing it wrong for years."
- **Audience ID as a symptom checklist:** brain fog, bloating, sugar spikes, knee aches, fatigue.
- **Mechanism:** chlorogenic acid plus eugenol, "1 + 1 … equals 10".
- **"Mistakes"** (sugar, milk, instant coffee).
- **Dated benefit ladder:** 15 minutes, 1 day, 3 days, 1 week, 1 month, 3 months.
- **Mid-video subscribe ask at ~43% of runtime (~234 s):** "99% of viewers still haven't subscribed… aiming to hit 100,000."
- **Exact protocol:** 3 whole cloves, 10 oz water, 5-minute simmer. Then a quick method, then three mistakes.
- **Contraindications:** warfarin/aspirin, ulcer, reflux.
- **Close:** "You're not broken, your coffee is broken." The same closing formula appears in the colon-cleanse script ("You're not broken. Your diet is broken.").
- **Title/script mismatch:** the title says 10 minutes, the script says 15.

**Thumbnail (#119):** no face and no doctor. A hand drops a clove into black coffee. Text: "CLOVE + COFFEE?", three numbered organ renders (liver, intestine, brain), and "…MIN LATER…". The same template on #130 got 116,950 and on #131 got 97,060, so the thumbnail alone does not explain 3M.

**Trends:**
- "clove water" US web (GT-01) rose from 5 to 86 (monthly) over five years and peaked on Jan 4–10, 2026. The 3.09M upload sat in a slowly declining band (62.5 before, 58 at upload, 54.2 after).
- On YouTube search (GT-30), interest jumped from 45.6 to 71.5 in the week of SHH's first clove video (Sep 2025). The direction of cause is unknown.
- Rising queries are about hair and women ("clove water benefits for female" Breakout), not seniors.
- **Classification: TREND-AMPLIFIED SERIES.** A multi-year wellness wave, reframed for seniors (HX-02).

**External (C01):** Dr. Eric Berg's "Benefits of Drinking Clove Water at Night" has 5.9M. Dr. Sebi-framed "HealthQuest" has 816K. Failed copies: "I DRANK CLOVE WATER for 7 Days" (Healthy Choices) got **277**, and Health Eclipse's copy of SHH's "Clove Water at Night Triggers Irreversible Changes" got **8.5K** (the original has 116K). Four days before retrieval, a large pharmacist channel (1.07M subscribers) posted "Add 1 Clove To Your Morning Coffee" and had 75K.

**Baseline after the hit:** median 9,539 before vs 9,418 after, so **no lift**. Pass-1's "maintains higher baseline" was wrong (DQ-09).

**Medical:** the time-bound effects are UNSUPPORTED (MV-03 and MV-05). "Stronger than ibuprofen" is UNSUPPORTED (MV-04). The warfarin caution is SUPPORTED (MV-06).

**Lesson:** a 41-episode franchise on a rising wellness wave produced the largest absolute results, but only about 1 in 3 episodes reached ≥3x, and exact repeats of the biggest episode returned to baseline. The franchise works as a lottery with a better-than-average hit rate, not as a repeatable formula. A new medical-first channel should copy the mechanic (a ritual inside a daily habit, episodes that differ) and not the claims.

---

## 3. Doctor Thomas walking cluster and its copies

**Verified facts:**

| Video | Date | Views | Multiple |
|---|---|---|---|
| RuxmqVyJKb0 "A SIMPLE Exercise Every 70+ Should Do Daily" | 06-12 | 596,346 | 72x |
| UGmIU2dS5zc "One SIMPLE Change to How You Walk" | 06-19 | 1,004,391 | 122x |
| 5oC-lLe7k6s "Why You Can't Walk Straight Anymore" | 06-21 | 328,707 | 40x |

Median 8,234.5. The channel joined 2026-05-20. All three videos are 19–20 minutes. One transcript is absent (fj4TaPrLl8U, no caption track).

**Actual script (UGmIU2dS5zc):**
- **Opens with a negation stack:** "not something you buy, not something you install, and not a new exercise routine… It is a change in how you walk."
- **Authority at ~40 s:** "After 26 years of working with adults over 70 as a physical therapist".
- **Core reveal (heel strike) withheld until ~242 s** (APPROX).
- No study citations. Medical claims 2.
- **Ending template:** "leave a comment with one… If not, feel free to comment with zero". The identical ending is used on the 2,526-view knee video, so the ending is not a differentiator.

**Thumbnails (#1–3):** the same male doctor persona in navy scrubs, pointing at stacked yellow/white text ("NEVER LOSE BALANCE / WALK LIKE THIS / SAVE YOUR LIFE / AFTER 70"). The answer is withheld. By contrast, the channel's low performers show full-body demonstrations (#5, #7, #9–11).

**Copies:**
- **Aliza cohort channel:** same titles 7 and 2 days later. 219,009 (**1,009x** its 217 median) and 20,701 (95x). The scripts were rewritten, not copied (5-gram Jaccard 0.003–0.008). The thumbnail *text* on #22 and #24 copies Thomas #3 verbatim.
- **Gentle Health:** a 2:35 condensed version got 145K.
- **Search sample (C04):** Balance Builders has 2M and 5.1M. Low-effort copies ("Over 70? Walking Isn't Enough…", "Walking After 70? Do THIS") got **167–452**.

**Trends:** "fall prevention" (US) sat on a 5-year plateau of 85–89 from Feb to Jun 2026 (GT-28, with occupational-safety noise in the query). "Balance exercises for seniors" is evergreen at 57–66 (GT-07). YouTube "exercises for seniors" doubled in five years and peaks every January (GT-08). **The upload week was not a spike.**

**Medical:** fall-prevention exercise is SUPPORTED (Cochrane, MV-14). "One change could save your life" is PARTIAL (MV-15).

**Lesson:** a demand-validated evergreen topic. The copy got 1,009x on a tiny channel, which is the strongest evidence in the dataset that the topic and packaging carried demand. But once the title space fills with copies, only substantive (PT-led) versions keep winning.

---

## 4. Dr. Ares ↔ Dr. Elias: a same-operator twin network

**Signals (LIVE_WEB_VISUAL + titles):**
- Identical thumbnail text on #49 = #76, #62 = #77, #60 = #80 and #50 = #81. The last pair shares the typo "ONES OR TWICE A WEEK".
- #53 = #79 share the same *mismatch*: the thumbnail says "Sleeping during the day…" on a title about "6 Golden Habits".
- Near-identical illustrated woman on #65 vs #72.
- 15 shared titles.
- Scripts differ (max 5-gram Jaccard 0.011).
- Ownership is UNVERIFIED.

**Performance of shared titles (first → second mover):**

| Title | First | Second |
|---|---|---|
| Pee at night | Ares 350,960 (08-08) | Elias 18,355 (09-05) |
| Stool stuck | Ares 10,537 | Elias 271,573 |
| Sleeping position | Ares 1,475,129 | Elias 28,352 |
| Bath | Elias 184,341 | Ares 506,628 |
| Bedtime | Elias 357,295 | Ares 13,023 |
| Eyesight fruit | Elias 568,520 | Ares 3,845 |
| Dry mouth | Elias 387,174 | Ares 2,083 |
| Surgeries | Elias 555,870 | Ares 45,512 |
| Water & sugar | Elias 129,474 | Ares 1,555 |
| Morning habits | Elias 216,963 | Ares 17,260 (Sep 19) |

Neither channel always wins, and first-mover status does not decide it. **Within this twin pair, re-runs posted 15 or more days after the sibling lost 4 of 6** (18K vs 351K, 1.8K vs 569K, 1.6K vs 129K, 17K vs 217K; the wins were 587K vs 356K and 265K vs 249K). Re-runs within 14 days split 5–5. Across the whole network, late copies usually *won* (14 of 16 pairs at 29 or more days), because stronger channels re-ran weak channels' titles; for example Okoro's 162-view mucus video was re-run by Ares at 87.5K. **The copying channel matters more than the order.** Ares's September winners (5 pills 647K, anesthesia 613K) were topics Elias had not run.

**External copying after Ares hits (C12, C13):** within 7–13 days, 8–9 verbatim-title copies appeared, mostly at 1–150 views. One reached 142K (Dr. Atlas, 5 days after). Persona clones ("Dr. Ares Smith Senior Health!", "Wellness After 70 – Dr. Elias") got 1 and 122 views.

**DS-000018 link:** ALG26-CLM-009 (templated near-duplicates can be treated as inauthentic) is SUPPORTED as policy. The observed results are consistent with it but do not prove it.

---

## 5. "Dr. Aliza Wright" on two channels: same persona, same titles, 941K vs 160

**Cohort channel** "Dr. Aliza Wright | Advice" (UCXZi5JVeuTluazF-fYqQgNA, median 217):
- "Taking Amlodipine, Losartan, or Lisinopril for Blood Pressure? Here's What Many Seniors Don't Know": **160** (2026-06-05)
- Variants: 173, 244, 409
- "Taking Amlodipine for Blood Pressure | Here is What Your Doctors Won't Tell You This!": **31** and 169
- 26 of 32 transcripts disclose AI-assisted production and composite patients.

**External channel** @Dr.AlizaWrightSeniorHealth (22.9K subscribers, 35 videos, about 4 months old, LIVE channel page):
- Same amlodipine/losartan/lisinopril title: **941K**
- "Taking Losartan, Valsartan, Amlodipine, Metoprolol… Doctors Won't Tell You": **175K**
- "Taking Amlodipine… Doctors Won't Tell You This!": **103K**
- **Watch-page check (LIVE, 2026-09-25):** 6nyp-aRcyNs was published **2026-05-31**, 5 days before the cohort channel's 2026-06-05 upload. It runs 1,717 s, YouTube shows an "AI" label, and the on-screen presenter is the same female persona. Its thumbnail is **identical to cohort thumbnail #39, including the typo "LOSARTON"**. So the second channel re-posted the same title and the same thumbnail 5 days later and got 160 views.
- Opening: UNKNOWN. The transcript panel does not load without sign-in.

**Cohort winner in the same family:** _dt5OX_1fx8 "If You Take Losartan, Amlodipine, or Metoprolol After 60 | Watch This First" got 47,032 (217x). Its actual opening: "Three pills are sitting on your nightstand right now, and one of them could drop your blood pressure so fast tonight, you'll hit the floor before you reach the bathroom. I'll show you which one…". The open loop comes at ~11 s, then a four-drug roll-call ("If you take losartan, valsartan, amlodipine, or metoprolol, this video is for you"). The loser (31 views) opens "That little white pill…" and uses a doctor-distrust framing. Thumbnails #23 (47K) and #37/#45 (≤170) are near-identical templates.

**Trends / history:** "amlodipine side effects" has a high, flat floor of 48 (GT-12). The Ascend amlodipine-olmesartan Class II recall was classified on 2026-06-02 (HX-03). The link is weak (LOW).

**Lesson:** the same persona, title, thumbnail and niche produced 941K on one channel and 160 on another. Packaging does not transfer between channels. Whatever the platform learned about each channel and video (unobservable here) dominated.

---

## 6. Okoro neuropathy: "The ONLY 6 Exercises YOU Need to Relieve Neuropathy in Feet & Legs" (hBZhkr-UYuA)

**Verified facts:** 2026-06-03, 608 s, 100,852 views (507x). This was the channel's second hit, 18 days after case 1.

**Borrowed title and thumbnail:** TopHealthTips published the identical title on **2026-03-14** (81 days earlier; watch-page verified) and reached **1,307,863**. Its thumbnail is a BEFORE/AFTER (barbed-wire foot vs healthy foot) with "FOOT & LEG NEUROPATHY? DO THESE EXERCISES". Okoro's #94 copies that concept and wording. Md Apo's "ONLY 7" got 207K. Seniors Circle's "I'm 102…" got 11K and Gentle Health's got 701. So Okoro was a later copy of an external winner that still worked.

**Trends:** the 5-year worldwide peak week of "neuropathy exercises" was May 31–Jun 6, 2026, **exactly the upload week** (GT-24: 91 vs 70.7 in the prior 90 days). In the US the upload window was 94.5 vs 77.2 (GT-04). US and Canada index at 100, the UK and Australia at 50. Rising YouTube queries include unproven remedies and a non-physician wellness personality (GT-26). **Classification: TREND-AMPLIFIED.** The 2026 Peripheral Nerve Society meeting (Jun 13–16) was checked and rejected as a driver (HX-06).

**Thumbnail (#94):** the only before/after thumbnail in the sample (bandaged red foot vs healthy foot). The same template on #108 got 188 views.

**Medical:** PARTIAL. Exercise improves balance and symptoms, but a meta-analysis found no clear effect on falls, and "relieve" must not read as a cure (MV-16).

---

## 7. "What a Stroke Looks Like the Day Before It Hits": three channels, three failures

| Channel | Date | Views | Multiple |
|---|---|---|---|
| Doctor Thomas | 2026-06-09 | 2,078 | 0.25x |
| Dr. Elias | 2026-08-10 | 1,186 | 0.01x |
| Dr. Ares | 2026-08-25 | 1,890 | 0.04x |

**Actual scripts:** Ares opens with a named-woman story ("Olivia, 71… left hand felt like it was wearing an invisible glove"). It has the **highest fear density among matched-pair videos, 13.5 per 1,000 words**. Elias opens "What if I told you that most strokes send a message…". The formats differ, and all of them fail.

**Thumbnails:**
- Thomas #17: doctor with an arrow pointing to an inset woman.
- Ares #68: man clutching his chest. That is a heart-attack cue on a stroke topic.
- Elias #92: woman clutching her chest.

**Trends:** Doctor Thomas's video launched in the week "stroke symptoms" hit 92 (GT-11). But the top related query was "heat stroke symptoms", during the June 2026 heat wave (HX-05). **The apparent demand spike was a different meaning of the word.**

**Opportunity signal:** the rising query "mini stroke symptoms in females" (+350%) suggests a more specific angle (N16).

**Lesson:** replicated negative evidence. A generic warning-sign list for a feared event fails regardless of opening style, channel or fear density.

---

## 8. Fit Lit Health: a small channel's breakout (external natural experiment)

**LIVE channel page:** 65.9K subscribers, 144 videos, "Dr. Malaika" persona.

**Phase 1 (8–9 months ago):** 18 uploads of 6–7 minutes on generic remedy topics, 70–2,900 views each.

**Gap:** about 7 months with no uploads.

**Phase 2 (last ~5 weeks):** 9–12 minute videos with senior template titles. About 11 of roughly 20 uploads exceeded 250K:
- Kidney toxins: 785K
- Egg mistakes: 710K
- Belly fat: 647K
- Gut flush: 608K
- B12: 600K
- Tooth decay: 509K
- Eyesight (a copy of the Elias title): 412K

Misses: 3.9K, 8.4K and 34K (clove).

**What changed:** length, title template, and topics copied from proven winners. **Follow-up:** sustained, so not a one-hit channel.

**Watch-page check (LIVE):** the eyesight copy J8zNi4_CqgA was published 2026-08-27, 11 days after the Elias original. Its captions are hi:asr (Hindi/Urdu speech). Its **thumbnail text is in Urdu** ("this fruit fixes the eyes! cataract gone overnight!"), with a woman in hijab pointing, a cataract close-up and a bowl of dates. **This breakout serves a South-Asian-language audience with English titles, so it is not a like-for-like comparator for a US senior channel.**

**Unknowns:** script openings (the transcript panel does not load without sign-in) and exact channel age.

**Medical risk:** many titles make cure-adjacent claims ("Repair Your Kidneys", "Reverse Tooth Decay").

**Lesson:** a small channel can break out quickly when packaging and length move to a proven template on proven topics. That route often depends on claims this project would reject.

---

## 9. "How Often Should Seniors Take a Bath After 60?": an evergreen topic with no search demand

**Internal:**
- Ares E4Qsvz-ggXE (08-22): 506,628 (11.1x), live 527K.
- Elias uIOusFFv13k (08-13): 184,341, live 188K.

The actual Ares opening is a routine morning shower turned "quietly damaging". The core answer ("three times") is withheld until **~690 s** (APPROX).

**External (C10):** the template originates with Gentle Health's 150-second video, published **2025-07-06** (watch-page verified), at **602,566**. Its thumbnail is a photoreal older male doctor with "How often Should Seniors Shower". Later copies: Aging with Wisdom 63K, Dr. Aven Royce 20K, Gentle Health's own re-runs 39K/33K/555, others 89–840.

**Trends:** "how often should seniors shower" had **zero measurable interest for five years** until after these uploads (GT-20).

**DS-000018:** consistent with personalized recommendation surfaces (ALG26-CLM-001, SUPPORTED). Traffic sources are UNKNOWN.

**Medical:** 2–3 baths a week, per dermatology guidance via secondary sources (MV-18, PARTIAL).

**Lesson:** topics can be large on YouTube without search demand. Trends is not a veto.

---

## 10. Matched pair 20: tongue vs face, one day apart (the cleanest control)

**Videos:** Okoro VhYXmAU8X-s "Look at Your Tongue Right Now — 6 Warning Signs" (2026-07-12) got **1,133** (5.7x). eH0FmM100wc "4 Heart Warning Signs Hiding on Your Face After 60 (Grab a Mirror)" (2026-07-11) got **32** (0.16x). Same channel, same template, same week.

**Actual first 30 s:**
- **Winner:** "Stick out your tongue and look at it in a mirror right now. Go ahead. I am serious." The self-check is instant.
- **Loser:** "Go and grab a mirror or turn your phone to the front-facing camera… I will wait because this only works if you look…". The viewer has to do a friction task before any value arrives. Its first sign comes at ~14 s, with no open loop.

**Thumbnails:** the winner (#101) has a large tongue photo, the doctor holding a mirror, and a white coat. The loser (#117) has a small earlobe inset and "LOOK IN THE MIRROR / YOUR FACE".

**Lesson:** with channel state held constant, a 35x gap separates a no-friction self-check with a large visual subject from a friction task with a small subject.

---

## 11. TopHealthTips: hit, cluster, decay (external lifecycle)

**LIVE channel page:** 336K subscribers, 147 videos.

**Hits (5–7 months ago):**
- Stiff and sore: 1.9M
- Leg-circulation test: 1.5M
- Neuropathy: 1.3M
- Varicose: 1.3M
- Knee: 1M
- Sciatica: 969K
- Walking won't make legs stronger: 800K
- Bladder: 520K

**Nocturia series:** 7 or more entries, 7.4K–520K.

**Recent 2–3 months:** mostly 2.3K–28K.

**Lesson:** a format ("The ONLY N exercises…", "30-second test + fixes") can carry a cluster for about two months and then decay, even on a 336K-subscriber channel. This is consistent with ALG26-CLM-008 (a subscription does not guarantee interest) and with DS-000031 "Doubling Down", where survivorship is visible.
