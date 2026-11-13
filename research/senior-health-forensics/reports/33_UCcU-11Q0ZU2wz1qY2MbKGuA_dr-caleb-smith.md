# 33 — DR. CALEB SMITH (UCcU-11Q0ZU2wz1qY2MbKGuA, @Dr.CalebSmith-l9e) — STATUS: PARTIAL
Checked 2026-11-14. Sources: senior_health_complete.db (tier 2: Apify complete catalog; 8 videos; 8/8 transcripts), live channel page in built-in Chrome (header only; grid did not render), curl of all 8 watch pages (status, views, likes, publish date, description) and the channel page, 6 hqdefault thumbnails viewed, `script_reuse.py` (8/8 ≥0.85), `title_families.csv`, DB chronology for the two top titles.

## A. Seedha jawab (Roman Urdu)
1. **Kis ke liye / promise:** 60–80+ seniors; sone ki position aur stroke, BP dawaiyan (amlodipine/losartan), "once you turn 80", subah ka dil par bojh, raat ko peshab, gale ka phlegm, surgeries. Promise: "ek doctor jo chhupa khatra batata hai" (channel bio: "Dr. Caleb Smith — your destination for better health, healthy aging"). **Bilkul naya:** DB row joined 2026-10-27; 8 videos 2026-10-28 → 11-09 (**4.7/hafta**); header **"9 videos", 1.23k subs**.
2. **Kya repeat hota hai:** (a) Titles ek ke baad ek **doosre channels ke bade titles** ke mutabiq ("Cardiologist Warns: This Sleeping Position Increases STROKE Risk Overnight!", "Doctor Explains: What Happens When You Eat Peanut Butter Every Day?", "Once You Turn 80, THESE 5 Things…", "Doctor Warns: That Stuck Throat Mucus Is NOT What You Think!"). (b) Thumbnail: kaala background, bold peela/safed + laal label + illustrated chehra ("I'M BEGGING YOU TO STOP SLEEPING IN THIS POSITION", "THE SHOCKING EFFECTS OF PEANUT BUTTER", "5 FATAL SURGERIES! DO NOT DO THEM"). (c) Opening: manzar ("You went to bed last night completely fine…", "You've got a jar of peanut butter sitting in your kitchen…"). (d) Ending: "That video builds directly on what we covered today… Sleep well. Your brain is counting on it." **Concentration (live, 8 videos, ~122.3K views):** top-1 73% (`nzJKdpJl4xE` 88,763), top-3 ~91%; median ~960.
3. **Winner vs weaker (matched, recency confound ke saath):** `nzJKdpJl4xE` (2026-11-03, 25:48, **88,763 live views**, 1,247 likes) "Cardiologist Warns: This Sleeping Position Increases STROKE Risk Overnight!" vs `8ua8yqDafBw` (2026-11-09, 21:24, **58 views**, 1 like) "Doctor Warns: That Stuck Throat Mucus Is NOT What You Think!" — same channel, 6 din ka farq, same illustrated template, **1,530x**. Thumbnail: winner "I'M BEGGING YOU TO STOP SLEEPING IN THIS POSITION" + sota hua bujurg; weak "STUCK THROAT PHLEGM? DON'T IGNORE THIS HIDDEN CAUSE" + chehra + gale par haath. Opening winner: *"You went to bed last night completely fine. No chest pain, no dizziness, no warning signs…"*. **Confound: recency** — weak sirf 5 din purana, aur channel ke baad ke sab videos (11-07 se 11-09) ≤920 views par; "weak" kehna abhi qabil-e-bharosa nahi. Jo farq dikhta hai: sleeping-position topic (jo is niche mein channel 04 par 2.06M tha) vs throat mucus. Plausible (interpretation, low): topic-level proven demand + date; **testable nahi** (traffic/CTR UNKNOWN). Counterexample: same-script/same-topic dusre channels par chhote: `Z22jBlg1qI4` (ch 31, 2026-10-09) 25, `UCtdjBmg…` 184, `UCxb05F-…` 146 vs bade 1.48M/764K/159K — yaani **wahi title/script 3 se 1.5M tak**; is channel ka 51K→88K ek mazboot copy. Confidence: low.
4. **Topic source / demand (title-family chronology, DB):** **"Sleeping Position Increases STROKE Risk"**: 2026-04-25 764,656 → … 08-19 1,475,129 (ch 04, report 04) → 08-29 34 → 08-31 28,352 → 09-12 17,042 (ch 32) → 09-24 146 → 10-09 25 (ch 31) → 10-23 159,363 (ch 09) → 10-23 184 → **11-03 51,255 (yeh channel; live 88,763)**. **"Stuck Throat Mucus"**: 05-02 60,498 → 09-12 160,522 (ch 04) → 10-04 1,183 (ch 31) → 10-31 11,851 → 11-07 344,267 (ch 09) → 11-09 199 → **11-09 32 (yeh channel)**. **Fact:** har family mein 2–5 bade copies (≥17K) aur kai ≤200 — order se decay seedha nahi (bade copies Oct–Nov mein bhi aaye: 159K, 344K). Google Trends nahi chalaya (UNKNOWN). Competitor example: channel 09 `_uaOTaWxWaY` (344,267; throat mucus) aur channel 04 `8IDSe2S5hkw` (2.06M; sleeping position).
5. **Playbook rule:** Outlier concept (Playbook p.6–8, Module 2.1): topic-level outlier ke liye cross-validation maujood (sleeping-position ke 5 bade copies) → hypothesis medium-high, **par AGENTS rule 9: copies independent evidence nahi** (neeche B) — views har copy ka alag sample hain, scripts same hain. Against: wahi script par 25–184 views wale copies (upar). Script Audit (Playbook p.353): is channel ke sab 8 scripts verbatim hain — **original content ka sifar**.
6. **Kya banayein (original idea, evidence-gated):** Sleeping position topic ka original, sourced angle (copy nahi): "Does Your Sleeping Position Really Affect Stroke Risk? What Sleep Studies Actually Show". Thumbnail: asli sleep-medicine clinician + bed ka diagram + "what the evidence shows", koi "I'M BEGGING YOU". First 30s: "Kya sona kisi ek taraf se dil ya dimagh par asar daalta hai? Teen studies, ek jawab", payoff = kya prove hua (sleep apnea/position, left-side sleeping ke observational data) aur kya nahi. Clinical source jo verify karna hai (yahan fetch NAHI kiya): sleep position aur sleep-disordered breathing/stroke par peer-reviewed reviews (obstructive sleep apnea aur stroke risk); video se pehle verify karein.

## B. Script reuse (fact) — `script_reuse.py 33`: 8/8 ≥0.85
| 33 video (date, live views) | match (channel, date, DB views) | J | order |
|---|---|---|---|
| nzJKdpJl4xE (11-03, 88,763) | `F8U3cX7G_x8` ch 09 (10-23, 159,363) | 0.94 | 33 baad |
| bswfMAYcuhk (10-28, 18,904) | `XPxJMNjeBkE` ch 31 (10-25, 1,630) | 1.00 | 33 baad |
| wjqxdytTdtY (11-04, 10,024) | `CvXavlG9eQI` UCKMngg0… (10-31, 83,515) | 1.00 | 33 baad |
| bVtr4yrlN64 (11-01, 1,458) | `-hhU9yBIYC0` ch 31 (10-10, 630,088) | 0.95 | 33 baad |
| zsAPklotyvE (11-08, 920) | `3Po1bEJte9c` UC356D… (08-31, 587,249) | 0.94 | 33 baad |
| A7qpRZElzk4 (11-07, 516) | `wmTO_GWNEro` UCQcBYZx… (08-27, 265,825) | 0.92 | 33 baad |
| 8ua8yqDafBw (11-09, 58) | `_uaOTaWxWaY` ch 09 (11-07, 344,267) | 1.00 | 33 baad |
| qhZDSWd27Lo (10-30, 32) | `qwBsA0l3bn0` ch 09 (11-08, 306) | 0.94 | **33 pehle** |
**Fact:** 7/8 mein is channel ka video match ke baad ka hai; bade copies hain `nzJKdpJl4xE` (88K) aur `bswfMAYcuhk` (19K) jab ke originals 159K/1.6K the. **Is channel ke 8/8 scripts duplicate — Not known:** direction, ownership, supplier. Ek cheez: `nzJKdpJl4xE` ka ending "Sleep well. Your brain is counting on it" aur ch 04/09 ke same script mein wahi, **presenter ka naam alag** (ch 04 "Dr. Eric Smith", ch 09 "Dr. Michael Carter", yahan "Dr. Caleb Smith") — fact, transcripts.

## C. Persona / claims / monetization (facts vs interpretation)
- **Fact:** channel "Dr. Caleb Smith", titles mein "Cardiologist/Doctor/Urologist"; koi licence/institution/specialty nahi; **credentials UNVERIFIED**; thumbnails illustrated; presenter ki awaaz/video maine nahi dekhi/suni (playback nahi hua). Persona-naam ka pattern (Smith/Carter/Caleb/Cale/Avery) channels 04/09/31/32/33 par — **interpretation (low)**, ownership UNKNOWN.
- **Fact:** descriptions: disclaimer 8/8; links nahi; shop/affiliate nahi; AI-disclosure nahi — monetization UNKNOWN. Hashtags (#PeanutButter…) description mein.
- **Fact (claims):** "5 FATAL SURGERIES! DO NOT DO THEM", "I'M BEGGING YOU TO STOP SLEEPING IN THIS POSITION" — thumbnail title se zyada extreme; source UNVERIFIED (health-misinformation risk, interpretation).

## D. Live vs snapshot
- Live 2026-11-14: header **"9 videos", 1.23k subs**; DB 8 videos, 663 subs. 8/8 saved IDs playable (curl OK); publish dates 2026-10-28 → 2026-11-09. **1 header video DB mein nahi** — Not known.
- Views DB → live (~2 hafte): `nzJKdpJl4xE` 51,255 → 88,763 (+73%); `bswfMAYcuhk` 4,917 → 18,904 (+284%); `wjqxdytTdtY` 4,499 → 10,024; `bVtr4yrlN64` 1,159 → 1,458.

## E. Coverage
| Layer | Status |
|---|---|
| Catalog titles/views/dates/durations (DB) | 8/8 (of header 9) |
| Playability / publish date / views / likes (curl 8) | 8/8 |
| Transcripts | 8/8; open/end read for 5; all 8 reuse-checked |
| Live channel header (Chrome) | yes (grid not rendered) |
| Thumbnails | 6 of 8 |
| Chrome playback / comments | NOT done / NOT read |
| vidIQ / Trends | not run |
| Credentials / claims | NOT verified |
Pending IDs: 1 header video not in DB; playback + comments for all 8; 2 thumbnails.

## F. Evidence ledger
| Claim | Evidence | Conf |
|---|---|---|
| nzJKdpJl4xE 88,763 vs 8ua8yqDafBw 58 | curl 2026-11-14 | high |
| 8/8 scripts ≥0.85 vs other channels | script_reuse.py | high |
| 7/8: 33 published after the matched video; 1/8 before | DB dates | high; direction unknown |
| Sleeping-position / throat-mucus chronologies | DB title query | high (DB views) |
| Header 9 videos, 1.23k subs | Chrome header | high |
| Weak label confounded by recency (5 days) | upload dates | high |
| Why sleeping-position beat throat mucus | interpretation | low |
