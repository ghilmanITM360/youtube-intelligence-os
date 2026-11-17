# Senior Health — 44-channel synthesis (2026-11-14)
Basis: 44 per-channel reports in `reports/`, `title_families.csv`, `script_reuse.py`, TRACKER.csv. Language: Roman Urdu. Facts / interpretation alag; confidence har jagah.
**Limits (poore project par lagu):** CTR, retention, traffic sources, monetization = UNKNOWN. Chrome playback, comments, vidIQ, Google Trends kisi channel par nahi chala; credentials sirf ch 27 aur 30 par web-check hue (dono UNVERIFIED independently). Live numbers = curl 2026-11-14. Family/reuse order sirf DB `published` date se; copy direction/ownership = **Not known**.

## 1. Coverage (fact)
| | Count |
|---|---|
| Channels with report | 44/44 (alag channel IDs; "Senior Health Today" ke do IDs alag: ch 18, 19) |
| PARTIAL | 38 |
| UNAVAILABLE (verified, removal reason koi source nahi) | 6 — ch 02, 10, 11, 15, 18, 25 |
| Title families | 97 families, 378 rows (DB) |
| Script reuse ≥0.85 | ch 33: 8/8; ch 31: 14/43; ch 09: 13/21; ch 04: 9/39; ch 06: 5/43; ch 32: 3/17; ch 05, 07, 13, 28, 36: 1 each; baaki 0 |

## 2. Sab se pehle: evidence ek doosre ki copy hai (AGENTS rule 9)
- **Fact:** channels **04, 06, 09, 31, 32, 33** ke scripts ek doosre se ≥0.85 match karte hain (ch 33 ke 8/8 scripts: 09 se 3, 31 se 2, 04 se 1). 50 families mein ≥3 dated members; **sirf 23/50 mein sab se purani date wali copy top-viewed hai**, baaki mein baad wali copy ne zyada views liye (median: baad wali copies = purani ke views ka 3.3%).
- **Interpretation (medium):** yeh cluster ek hi factory/template ho sakta hai (ownership Not known). Is cluster ke views ko "alag-alag independent proof" ginna ghalat hai — ek topic ka win ek hi data point hai. Isiliye neeche sirf unhi patterns ko "strong" kaha hai jo **kam-az-kam 2 non-cluster channels** par dikhe.
- **Decay (fact, DB):** purani copy → baad ki copies aam tor par bohat kam (examples: mucus: ch 04 160,522 → ch 40 11,851 → ch 31 1,183; olive-oil frame: ch 41 18K vs same-frame sibling 212; anesthesia: ch 04 613,366 → ch 40 625). Lekin ch 32 ka peanut-butter video (family 14) 1.13M par sab se bada, jab ke ch 43 ki copy 60 par — **order ≠ jeetne wala**.

## 3. Sab se mazboot patterns (kam-az-kam 2 non-cluster channels)
1. **Dawai-safety / "meri dawai ka chhupa sach" topic.** Ch 27 (named clinician, 98 videos, 14.5M): memory-aur-dawai 3.59M, Tylenol/Advil 825K; ch 44: BP dawaiyon ke naam 48,366 live (81% channel); ch 29: BP-dawai 25,104 (96%); ch 07: dementia-medication 724K. **Confidence: medium** (ch 29/44 ek hi frame, ch 27 alag evidence-standard).
2. **Sharminda/takleef-wala sawal-topic** (qabz, peshab raat ko, mucus, nahana/hygiene). Ch 43 qabz 38,052 (86%), ch 44 qabz 2,886 (2nd), ch 07 "stool stuck", ch 04/40 mucus & night urination. **Medium–low** (kai copies).
3. **Ek-cheez-har-roz ("2 tablespoon olive oil / peanut butter every day")** — ch 41 olive oil 18,129; ch 32 peanut butter 1.14M. **Low–medium**; isi frame ke siblings (eggs 212, ch 43 peanut butter 60) bohat kam — frame akela kaam nahi karta.
4. **Concentration:** 44 mein se zyada tar channels mein top-1 video 40–100% views leta hai (ch 12: 97%, 15: 100%, 24: 95%, 28: 99%, 29: 96%, 31: 94%, 43: 86%); sirf ch 06 (16%), 26 (11%), 30 (12%) jaise channels mein faila hua. **Fact (DB):** "ek outlier + baaki flat" is niche ki aam shakal hai — channel banane ki zameen kamzor, topic-selection hi strategy.

## 4. Sab se bade failure patterns
1. **Clone/script-copy factories** (04/06/09/31/32/33): copy se kabhi-kabhi bada outlier mila, par tail bohat patla; 6 UNAVAILABLE channels mein koi sabab kisi source ne nahi bataya — kaaran claim nahi kiya.
2. **Thumbnail/title claim > transcript tone** (ch 09 "DEATH IS CLOSE", ch 31, ch 33 "5 FATAL SURGERIES", ch 41 "EAT 2 YOLKS TO STOP IT IMMEDIATELY", ch 43 "ZERO PERCENT VISCERAL FAT INSTANTLY"): health-misinformation risk — **copy nahi**.
3. **Persona-naam / credential unverified:** "Dr. X Senior", Smith/Cale/Caleb/Kale variants, ek channel mein transcript mein alag naam (ch 31 "Dr. Vincent", ch 40 ke 7 naam-variants). Ch 43 titles mein **asli mashhoor doctor ka naam** — link UNVERIFIED, impersonation risk.
4. **Asli credential + naya channel + Shorts-only/funnel** = kam views: ch 30 (real-looking cardiologist, 56 videos, ~10K total, long video 411 views).
5. **Naye channel mein ek outlier ke baad 10+ flat videos** (ch 38–44): cadence 3–6/hafta se bhi baseline nahi bana.

## 5. Clinician-led authentic content: ch 27 vs ch 30 (contrast)
| | Ch 27 Better Health While Aging | Ch 30 Decode Your Heart |
|---|---|---|
| Fact | named geriatrician claim (public footprint consistent; registry check NAHI), 98 videos, 193k subs, 14.5M views, 26 videos ≥100K | cardiologist bio-claim (closest directory match spelling/years alag — UNVERIFIED), 56 videos (29 Shorts), ~10K views, max 1,222 |
| Packaging | ek chehra, ek template, kam text, "board certified" intro, named guideline | photo thumbnails, Shorts-heavy, "tap link" funnel |
| Topic | dawai-safety / B12 / memory / caregiver | Ozempic, walking test, dil ke signs |
| Interpretation | **credential akela kaafi nahi** (ch 30); ch 27 mein **topic (dawai-safety) + asli identity + wahi audience (caregiver) + 5 saal ka tail** alag kaam karte hain. n = 2, **low confidence**; kya clinician-trust ne farq dala ya sirf topic/age — UNKNOWN. |

## 6. Recommendation
**Sub-niche: "60+ ke liye dawai-safety aur dawai-se-jude chhupe asraat" — ek asli, naam wala clinician ya pharmacist ke saath** (BP, sleep aid, OTC painkillers/anticholinergics, kidney-safe dawaiyan).
- **Kyun:** (a) dawai-safety cluster ch 27 par 3.59M/825K, (b) ch 44 48K aur ch 29 25K naye channels par bhi, (c) ch 07 724K — 4 channels, ch 27 independent hai (non-cluster). (d) **Faida:** clone factories "wellness food" par bhare hain; dawai-safety mein named clinician + guideline citation ek differentiator hai. **Confidence: medium–low** (CTR/retention/Trends UNKNOWN).
- **Risk:** medical claims — har claim ke liye guideline/label; "stop your pill" jaisa kabhi nahi, hamesha "doctor/pharmacist se poochhein".

## 7. Repeatable channel format (original, copy nahi)
1. Title: `<Dawai/class ka naam>? <Ek specific sawal> — <kis ke liye>` (naam + payoff; "SHOCKING" nahi).
2. Thumbnail: asli presenter ka chehra + dawai ki botal/icon + ek 3–4 lafz ka sawal; claim kam. (Ch 27 ka template + ch 44 ka dawai-naam hook, par cartoon/AI-face nahi.)
3. Pehle 30s: roz ka manzar ya "aap ki botal par jo naam hai" (apne alfaaz) → ek promise jo video poora karta hai.
4. Beech: har claim par guideline/label ka naam screen par; "kab doctor ko batayein" ek section.
5. Ant: ek clear next step + sources description mein + disclaimer; subscribe-CTA chhota.
6. Cadence: 1–2 long videos/hafta; Shorts ko long ki taraf funnel nahi (ch 30 ka sabak).

## 8. Pehle 3 video ideas (live-checked evidence + clinical source to verify)
"Live-validated" yahan matlab: 2026-11-14 ko curl se live views mile; **Google Trends / vidIQ / playback NAHI chala** — demand abhi bhi low-confidence.
1. **"BP ki teen dawaiyan (ACE-inhibitor, ARB, beta-blocker): har ek ka sach mein common side-effect aur kab doctor ko batana hai"**
   - Live evidence: ch 44 `cfP4RVGtx3Q` 48,366 (sibling `9FqlARM5rrA` 816); ch 29 `k60S_3aPZN0` 25,104.
   - Thumbnail: clinician + 3 dawai-class icon + "KAUNSA SIDE-EFFECT?".
   - Hook (30s): "Aap ki botal par teen mein se ek naam hai… zyada tar log in ka sirf ek asar jaante hain."
   - Sources (VERIFY, fetch nahi): ACC/AHA hypertension guideline; drug label (FDA/MHRA) common adverse reactions.
2. **"Qabz after 60: 5 cheezein jo madad karti hain, aur 3 red flags jin par fauran doctor se milein"**
   - Live evidence: ch 43 `xCh_vhbyf-w` 38,052; ch 44 `Y6ntdtEI2aM` 2,886; (ch 43 sibling bath 263 = topic matter karta hai).
   - Thumbnail: clinician + footstool/psyllium + "KAB DOCTOR?" — "POOP IN SECONDS" nahi.
   - Hook: "Do din se pet saaf nahi? Pehle ek cheez check karein…"
   - Sources (VERIFY): ACG/AGA chronic constipation guideline; NIDDK constipation page.
3. **"Raat ko 'PM' wali goli (diphenhydramine) after 65: kya dimagh aur girne ka khatra badhta hai?"**
   - Live evidence: ch 44 `ZnvdnsLTr78` (sleep pill, 140 — kamzor, packaging "DOCTORS WARN" generic) aur ch 27 dawai-safety/memory 3.59M — **kamzor evidence (low)**; isliye test video.
   - Thumbnail: asli presenter + goli ki botal + "YAADASHT?"; hook: "Raat 1:15 baje aap goli lete hain…" (apne alfaaz).
   - Sources (VERIFY): AGS Beers Criteria (latest); anticholinergic-dementia cohort studies — pehle verify.

## 9. Open items (owner ke faisle ke liye, shuru nahi kiye)
- 6 near-complete channels add karna; tier 3/4 Apify job (~$18, approval chahiye).
- Chrome playback, comments, vidIQ, Trends — sab 44 par pending.
- TRACKER mein ab 44 unique rows, statuses normalized (PENDING 35–38 → PARTIAL).
