# 31 — DR. AVERY SENIOR (UC9qTnpiqpVWSXeHmL1_Dykw, @DrAverySenior) — STATUS: PARTIAL
Checked 2026-11-14. Sources: senior_health_complete.db (tier 2: Apify complete catalog; 43 videos; 43/43 transcripts), live channel page in built-in Chrome (header only; grid did not render), curl of all 43 watch pages (status, views, likes, publish date, description) and of the channel page, 6 hqdefault thumbnails viewed, `script_reuse.py` (14/43 ≥0.85 vs other channels), `title_families.csv`, DB date/view comparison of every matched pair.

## A. Seedha jawab (Roman Urdu)
1. **Kis ke liye / promise:** 60–85+ seniors; "Once you turn 80", nahana, chalna, nashta aur muscle, qabz, BP target, dawaiyan. Promise: "ek geriatric doctor (20+ saal) jo sach batata hai". Presenter naam "Dr. Avery Senior" (transcript: "I've been practicing geriatric health for over 20 years"). Naya channel: DB row joined 2026-09-22; 43 videos 2026-09-26 → 11-11 (**6.5/hafta**); header "45 videos", 6.06k subs.
2. **Kya repeat hota hai:** (a) Titles seedhe doosre channels ke titles jaise: "Once You Turn 80…", "Over 60? Add This ONE Powerful Breakfast Food…", "7 Hygiene Mistakes After 60…", "Stool STUCK in the Rectum!", "Cardiologist Warns: THAT Sleeping Position Increases STROKE Risk Overnight!" (31 mein se 14 videos ka title family doosre channels mein bhi hai). (b) Thumbnails: kaala background, bold peela/safed text + laal label + illustrated bujurg ("ONCE YOU TURN 80 THIS HAPPENS", "IF YOU'RE DOING THIS AT NIGHT DEATH IS CLOSE!"). (c) Opening: "Have you ever noticed…?" ya "welcome back to the channel, I'm Dr. Avery Senior". (d) Descriptions: **37/43 mein disclaimer** + kuch mein PubMed/PMC/AHA links. **Concentration (live, 43 videos, ~739.6K views):** top-1 94% (`-hhU9yBIYC0` 692,595), top-3 96%; median 411.
3. **Winner vs weaker (matched):** `-hhU9yBIYC0` (2026-10-10, 15:51, **692,595 views**, 4,939 likes) "Once You Turn 80, THESE 5 Things Happen Whether You Like It Or Not!" vs `SjcUPvTuc9o` (2026-10-27, 19:19, **2,268 views**, 31 likes) "Once You Turn 80: 5 Changes You Should Know About | Senior Health" — **same topic/format, 17 din ka farq, 305x**. Thumbnail winner: "ONCE YOU TURN 80 THIS HAPPENS WHETHER YOU LIKE IT OR NOT" + sota hua illustrated bujurg (stick); weak ka thumbnail maine nahi dekha. Opening winner: *"There is a birthday that changes something in your body and mind, whether you feel it happening or not. Not 60, not 70, 80."* Winner ki script ka 0.95 match channel 33 ke `bVtr4yrlN64` se (2026-11-01 — **is channel ke 22 din baad**, sirf 1,159 views); weak ka 0.90 match channel 09 ke `3mkXMRnrf08` se (1,289, 2026-10-22). Farq jo dikhta hai: **title wording ("Whether You Like It Or Not" vs "Changes You Should Know About") aur 17 din pehle ka upload**; plausible (interpretation, low): pehla upload (channel ke pehle hafton mein) + darr/"zaroori" framing; **testable nahi** (CTR/traffic UNKNOWN). Counterexample: `mCprjCe8630` ("ONE SIMPLE CHANGE TO HOW YOU WALK THAT COULD SAVE YOUR LIFE AFTER 70!" 8,991, 2026-10-30) bhi bada-sa par chhota; aur wahi topic ke copies channel 33 par 1,159 — to topic akela nahi. Confidence: low.
4. **Topic source / demand:** Is channel ke top-5 mein se 4 videos kisi aur channel ke bade video ke **topic/title copies** hain (jaise `txqcWLxB8VE` 3,870 — channel 24 ka title/thumbnail; `o1g_3An1kuk` 3,826 — hygiene family, report 28), yani demand ka saboot doosre channels ke views hain (1M, 579K, 350K…), is channel ke nahi. Google Trends nahi chalaya (UNKNOWN). Competitor example: channel 32 `vhfV71o8Xl8` ("Stool Stuck" family, 982,583 DB) — isi channel ke do copies 1,475 aur 137 par.
5. **Playbook rule:** Outlier concept (Playbook p.6–8, Module 2.1): top-1 1583x median par ek hi video (94%); matched baseline = channel ke baaki 42 (median 411) — outlier asli, par repeat nahi hua. Script Audit (Playbook p.353) + AGENTS rule 9: **14/43 scripts verbatim ya near-verbatim (≥0.85) hain** isliye "independent evidence" nahi; copies ka size originals se bohat chhota (neeche B). Against: wahi script originals par 982K/579K/350K aur is channel par 137/1,261/143.
6. **Kya banayein (original idea, evidence-gated):** Copy nahi — original, sourced: "What Changes in Your 80s? 5 Things to Watch (and Which Are Not Normal Aging)". Thumbnail: asli clinician/geriatrician + ek checklist, bina "whether you like it or not". First 30s: "Aap ke walid 80 ke ho gaye? 5 tabdeeliyan normal, 5 doctor ko dikhane wali", payoff = normal vs red-flag table (yaadasht, chalna, neend, bhook, mood). Clinical source jo verify karna hai (yahan fetch NAHI kiya): AGS/WHO ICOPE guidance on intrinsic capacity aur geriatric syndromes review; video se pehle verify karein.

## B. Script reuse — order aur decay (fact) — `script_reuse.py 31`
31 ke 14 videos ka pehla 200-word script doosre channel ke video se ≥0.85 match (Jaccard 5-gram); **order = publish dates (DB), copy direction nahi**:
| 31 video (date, views) | match (channel, date, views) | J | order |
|---|---|---|---|
| ANuxdobOkA0 (11-10, 82) | `wp-wk_Zm6NU` ch UC356D… (09-14, 93,042) | 1.00 | 31 baad |
| auy0Tw9Z4Z0 (10-03, 1,261) | `8Cvibr_sYNE` UCsPba6P… (09-09, 579,349) | 1.00 | 31 baad |
| P7c-Evu1LnA (10-04, 137) / 6jnULeXsc6w (10-15, 1,475) | `vhfV71o8Xl8` UCsPba6P… (09-21, 982,583) | 0.94 / 0.89 | 31 baad |
| cB7H6LxGYwc (10-08, 27) | `UmNTryXlgR0` UC1BwGJg… (09-19, 165,787) | 0.95 | 31 baad |
| -54Dqx2J6wg (11-08, 143) / s3fC4RjvaTY (11-10, 86) | `lRn0p4YL0Bk` (08-08, 350,960) / `C8zmIX_9NCo` (08-27, 127,627) UC356D… | 0.94 / 0.89 | 31 baad |
| 3C5D5dXIwPI (11-03, 298) | `-bc9q11OBkQ` UC356D… (09-19, 17,260) | 0.86 | 31 baad |
| v7uF7gTOVtY (11-09, 128) / SjcUPvTuc9o (10-27, 2,238) | `yzaES2w2h6M` (11-04, 15,949) / `3mkXMRnrf08` (10-22, 1,289) ch 09 | 1.00 / 0.90 | 31 baad (ch 09 ke baad) |
| **-hhU9yBIYC0 (10-10, 692,595)** | `bVtr4yrlN64` ch 33 (11-01, 1,159) | 0.95 | **31 pehle** |
| XPxJMNjeBkE (10-25, 1,630) / tDh1EtV3Ol8 (10-19, 967) | `bswfMAYcuhk` ch 33 (10-28, 4,917) | 1.00 / 0.95 | 31 pehle |
| NGbG0nydmfk (11-06, 166) | `ka2RkQPQBZo` ch 07 (309,000 DB, date nahi) | 1.00 | ? |
**Fact:** 10 matches mein is channel ka video baad ka hai aur views originals ke ≤1% (27 se 2,238 vs 17K–982K); 3 mein (`-hhU9yBIYC0`, `XPxJMNjeBkE`, `tDh1EtV3Ol8`) is channel ka video pehle ka hai. **Not known:** copy direction, ownership, shared script supplier. Is channel ke andar bhi 4 same-title duplicates: peanut butter (`XPxJMNjeBkE` 1,665 / `tDh1EtV3Ol8` 972), "Stool STUCK" (1,616 / 138), "Cardiologist Warns… Every Morning" (473 / 150), "#1 Best Fruit… Eyesight" (798 / 398) — dusra copy aam taur par ≈ aadha ya kam.

## C. Persona / claims / monetization (facts vs interpretation)
- **Fact:** "I'm Dr. Avery Senior… practicing geriatric health for over 20 years" (`ahOhpfTf6Wc`); **`o1g_3An1kuk` ending "I'm Dr. Vincent"** — isi channel ke ek video mein alag naam (fact; wajah UNKNOWN). Credentials UNVERIFIED; "Dr. Avery Senior" naam ek **persona-jaisa** hai (naam mein "Senior"; interpretation, low). Presenter ki awaaz/video maine nahi dekhi/suni (playback nahi hua); thumbnails illustrated.
- **Fact:** descriptions mein 37/43 disclaimer; AI-disclosure nahi; links PubMed (6), NCBI (4), PMC (3), AHA journals (2) — verify nahi kiye; shop/affiliate link nahi dekha — monetization UNKNOWN.
- **Fact (claims):** "7 Signs An Older Person May Be Entering Their Final Year Of Life", "He Died In His Sleep From Doing This", thumbnail "IF YOU'RE DOING THIS AT NIGHT DEATH IS CLOSE!" — fear framing; koi cited case/study verify nahi (UNVERIFIED). "I Wish I'd Never Had Cataract Surgery — Doctor Explains" (`HLSma4GFYlI`) ek first-person "doctor" claim.

## D. Live vs snapshot
- Live 2026-11-14: header **"45 videos", 6.06k subs**; DB 43 videos, 5,460 subs. 43/43 saved IDs playable (curl OK); publish dates 2026-09-26 → 2026-11-11. **2 header videos DB mein nahi** — Not known.
- Views DB → live: `-hhU9yBIYC0` 630,088 → 692,595 (+10%, ~7 hafte); `mCprjCe8630` 8,161 → 8,991; `ahOhpfTf6Wc` 7,819 → 7,841.

## E. Coverage
| Layer | Status |
|---|---|
| Catalog titles/views/dates/durations (DB) | 43/43 (of header 45) |
| Playability / publish date / views / likes (curl 43) | 43/43 |
| Transcripts | 43/43; open/end read for 8; all 43 reuse-checked |
| Live channel header (Chrome) | yes (grid not rendered) |
| Thumbnails | 6 of 20 |
| Chrome playback / comments | NOT done / NOT read (DB comment counts present) |
| vidIQ / Trends | not run |
| Credentials / claims | NOT verified |
Pending IDs: 2 header videos not in DB; playback + comments for all 11; remaining 14 thumbnails.

## F. Evidence ledger
| Claim | Evidence | Conf |
|---|---|---|
| -hhU9yBIYC0 692,595 views; SjcUPvTuc9o 2,268 | curl 2026-11-14 | high |
| 14/43 scripts ≥0.85 vs other channels | script_reuse.py | high (metric) |
| 10 of 14 matches: 31 published after the matched video; views ≤1% of originals | DB dates/views | high (DB views, dates) |
| 3 of 14: 31 published before the match (incl. top video) | DB dates | high; direction unknown |
| "Dr. Vincent" ending in o1g_3An1kuk | DB transcript | high |
| Header 45 videos, 6.06k subs | Chrome header | high |
| Why Once-You-Turn-80 video won | interpretation | low |
