# 09 — Healing & Health (UCwdi3NgBtFc_LfhoxQ2eB7w, @HealingHealth-l4c) — STATUS: PARTIAL
Checked 2026-11-13. Sources: senior_health_complete.db (tier 2: Apify 2026-11-11 complete catalog, with likes/comments), live channel /videos page in built-in Chrome (22 rows), curl of 12 public watch pages, transcripts 21/21, hqdefault thumbnails (12 viewed), `script_reuse.py` (word-5-gram Jaccard, first 200 words) over all DB transcripts.

## A. Seedha jawab (Roman Urdu)
1. **Kis ke liye / promise:** 60+ seniors; gala/mucus, dry mouth, neend ki position, peshab, chalna/balance, hygiene. Promise: "ye chhupa kaaran hai / ye sirf ek cheez" + 15–29 min explainer. Naya channel: joined Oct 18 2026, pehla video 2026-10-21; 22 videos 3 hafton mein (~7/hafta). Presenter "Dr. Michael (Mike) Carter".
2. **Kya repeat hota hai:** (a) Title: wahi shared-title family (22 mein se 21 DB-videos title_families.csv mein) jo 04/05/06/07 mein hain. (b) Thumbnail template: kaala background, peela/safed/laal text, cartoon senior; dekhe gaye 12 mein se kam az kam 8 channel 04/05/06/07 ke thumbnails jaise ya same wording (e.g., "I'M BEGGING YOU TO STOP SLEEPING IN THIS POSITION", "THE FRUIT REPAIRS EYES OVERNIGHT CATARACTS", "UNSTABLE WALK IF YOU ARE 70, 80 OR 90"). (c) **Script: 21 mein se 13 videos ke pehle 200 words dusre channels ke transcripts se ≥0.85 match (5 ka 1.00 = bilkul same)** — neeche B. **Concentration (live, 22 videos, ~0.85M listed views, rounded):** top-1 42%, top-3 93% (352K/232K/208K); baaki 19 videos 17K ya kam; median ~1.4K.
3. **Winner vs weaker (matched):** `F8U3cX7G_x8` (2026-10-23, 24:40, **208,308 views**, 1,749 likes) "Cardiologist Warns: This Sleeping Position Increases STROKE Risk Overnight!" vs `qwBsA0l3bn0` (2026-11-08, 29:27, **329 views**, 2 likes) "NEVER Agree to This: 5 Deadly Surgeries for Seniors!". Dono ki script dusre channel ke bade video ki **verbatim copy** (F8U3 ≡ ch 04 `8IDSe2S5hkw` 2.06M, Jaccard 1.00; qwBs ≡ ch 06 `g9qSvSLTUfU` 1.37M, Jaccard 1.00), dono same template/thumbnail style. Farq jo dikhta hai: F8U3 channel ke pehle hafte (Oct 23) ka upload, topic jo 04 par 2.06M par proven; qwBs 16 din baad (Nov 8) ka, sirf 5 din purana. **Confound: recency** — Nov 8 ke baad ke sab videos (≤5 din purane) 253–1.5K par hain; isliye "weak" kaha jaana abhi qabil-e-bharosa nahi. Counterexample: `3n2WWl0mjUg` (nocturia, 14K) ki script ch 04 ke 995K video jaisi (0.92) — copy ka size bohat kam. Confidence: low (recency + sirf views).
4. **Topic source / demand:** Top-3: throat mucus `_uaOTaWxWaY` 352,001 (2026-11-07), dry mouth `mHFU21qjgEo` 232,862, sleeping position 208,308. **Dry-mouth topic 3 channels mein bada:** 06 `mGjzEwTmoXc` 436,911, 07 `LjZ9t5R-7ac` DB 243,136, 09 232,862; counterexample 04 `PWc0zfa2lWU` 5.6K — cross-channel validation medium. Google Trends nahi chalaya (UNKNOWN). Competitor example: 06 ka `mGjzEwTmoXc` (dry mouth, 2026-08-26) — report 06.
5. **Playbook rule:** Outlier concept (Playbook p.6–8, Module 2.1): outlier ko cross-validate karo — dry mouth/throat mucus/sleeping-position teen-chaar channels par outlier → topic hypothesis medium-high; par yeh *kopi shuda* scripts hain, isliye "independent evidence" nahi (AGENTS rule 9: duplication detect karo). Rule ke khilaaf example: same script, nearly same packaging, 208K vs 329 (upar #3) aur ch 04 ka dry-mouth 5.6K.
6. **Kya banayein (original idea, evidence-gated):** Dry mouth ka apna angle: "Waking Up With a Dry Mouth After 60? 4 Causes to Check Before Blaming Age (Medications, Mouth-Breathing, Sleep Apnea, Dehydration)". Thumbnail: asli clinician + ek tick-list, kam text. First 30s: subah ka scene (apne alfaaz), phir payoff "pehla check 60 second mein: dawai ki list dekho". Clinical source jo verify karna hai (yahan fetch NAHI kiya): xerostomia/dry mouth ka peer-reviewed review ya NIDCR guidance, aur sleep-apnea screening guidance; video se pehle verify karein.

## B. Script reuse (fact) — `script_reuse.py 09`
| 09 video | matched other-channel video (Jaccard) | matched ch / date |
|---|---|---|
| `F8U3cX7G_x8` sleeping position | `8IDSe2S5hkw` (1.00) | 04 / 2026-08-19 |
| `qwBsA0l3bn0` 5 surgeries | `g9qSvSLTUfU` (1.00) | 06 / 2026-08-28 |
| `_GdIM8Eb6hw` bed time | `QiBYlf1-Ih4` (1.00) | 06 / 2026-08-14 |
| `Muu5MrtwsTg` ideal BP | `BP6wmPs5SnE` (0.95) | 06 / 2026-09-10 |
| `GF-2EUDlSnE` best fruit eyes | `d5BsOk9lVXI` (0.87) | 06 / 2026-08-16 |
| `3n2WWl0mjUg`, `uhrLL_1sgWA`, `BfbexDg_mIQ` | `lRn0p4YL0Bk` (0.92), `EkcaJ18NLAU` (0.89), `ML_f1bVqiZk` (0.90) | 04 / Aug–Sep |
| `_uaOTaWxWaY` throat mucus | `8ua8yqDafBw` (1.00) | 33 / 2026-11-09 |
| `yzaES2w2h6M`, `3mkXMRnrf08` | `v7uF7gTOVtY` (1.00), `SjcUPvTuc9o` (0.90) | 31 / Nov, Oct |
| `-685iKw4NYU`, `gZB9oyX4zB0` | `iJhmxqrgTa4` (0.92), `vhfV71o8Xl8` (0.90) | 28, 32 |
Ek hi cheez 04's `8IDSe2S5hkw` aur 09's `F8U3cX7G_x8` ke end mein: *"That video builds directly on what we covered today… Sleep well. Your brain is counting on it. I'm Dr. Eric Smith / I'm Dr. Michael Carter"* — **text same, presenter ka naam alag** (fact, transcripts).
**Observation across 01–09** (same script): reuse≥0.85 — ch 04: 9 videos (matches 31, 33, 09), ch 06: 5 (33, 09), ch 05: 1 (31), ch 07: 1 (31; sirf 9 transcripts hain), ch 01/03/08: 0. Yaani 04/05/06/07/08 ke titles milte hain par scripts alag likhe gaye; baad ke channels (09, 31, 33, …) mein **scripts verbatim dohraye gaye**. **Not known:** kaun kis se, ownership, tool/service, ya ek shared script-supplier. Kuch matches ke dates 09 ke baad ke hain (33 ka `8ua8yqDafBw` 2026-11-09 vs 09 ka 2026-11-07) — isliye "09 ne copy kiya" ya "common source" ka faisla source se nahi hota.

## C. Credibility (facts vs interpretation)
- **Fact:** 12 sampled descriptions mein AI-production disclosure nahi. Presenter ka chehra/awaaz maine nahi dekhi/suni (Chrome playback nahi hua). Presenter ka naam "Dr. Michael Carter / Dr. Mike Carter"; credentials kisi source se verify nahi.
- **Fact:** `_GdIM8Eb6hw` transcript mein "Harvard aur National Institute on Aging ne confirm kiya" (bina citation) — wahi line 06 `QiBYlf1-Ih4` mein bhi hai (copy), UNVERIFIED.
- **Fact:** thumbnails title se zyada extreme (e.g., `stQ52UGPt1Y` "DEATH IS CLOSE", `qwBsA0l3bn0` "5 FATAL SURGERIES").

## D. Live vs snapshot
- Live 2026-11-13: **22 videos, 5.26k subs**; DB (Apify 2026-11-11): 21 videos, 5.01K subs. 1 naya video `r6XoN7wvw44` ("6 Golden Habits…", 2026-11-12, 1,527 views). DB ke sab 21 IDs live. Views: `_uaOTaWxWaY` 344,267 → 352,001; `mHFU21qjgEo` 228,420 → 232,862.
- Subs/views ratio: 5.26k subs par 352K views wala video — views zyadatar non-subscribers se (interpretation; traffic source UNKNOWN).

## E. Coverage
| Layer | Status |
|---|---|
| Catalog titles/views/dates/durations (DB) | 21/21 (date 20/21) |
| Transcripts | 21/21 (open/end of 11 read; all 21 reuse-checked) |
| Live channel page | yes (22 rows) |
| Live watch metadata (curl) | 12 of 22 (incl. 11 planned) |
| Thumbnails | 12 of 20 |
| Chrome playback / comments | NOT done / NOT read (DB likes/comments counts present) |
| vidIQ / Trends | not run |
| Credentials | NOT verified |
Pending IDs: uhrLL_1sgWA gZB9oyX4zB0 jmqoPvfmfUg Z1v9Yh-qUZ8 LAWALzaQU_8 p9HkVSA25FA BfbexDg_mIQ zUpn9vGUSvM (watch metadata); playback + comments for all 11.

## F. Evidence ledger
| Claim | Evidence | Conf |
|---|---|---|
| 13/21 videos have ≥0.85 script match elsewhere | script_reuse.py over DB transcripts | high (metric) |
| F8U3cX7G_x8 ≡ 8IDSe2S5hkw (1.00), name swapped Eric→Michael | DB transcripts open+end | high |
| F8U3cX7G_x8 208,308 views; qwBsA0l3bn0 329 | curl watch pages 2026-11-13 | high |
| Live 22 videos, 5.26k subs | Chrome /videos | high |
| Copy direction / ownership | not in any source | unknown |
| Recency confounds "weak" label | upload dates 11-08…11-12 | high |
