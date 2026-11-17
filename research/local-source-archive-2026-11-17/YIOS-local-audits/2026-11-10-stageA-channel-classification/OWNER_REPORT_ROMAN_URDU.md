# YIOS Stage A — Owner Report (Roman Urdu)

Tareekh: 2026-11-10. Stage A mukammal. **Koi Apify run nahin chala, koi paisa kharch nahin hua, DB ya branch mein koi tabdeeli nahin ki.**

## 1. Database pin

- Commit: `efd3dc0a18bc50e95ae6a6c1e1b9931b2d0abbf6` (branch `docs/yios-consolidation-index`, saaf tree).
- DB: `data/catalog/youtube_channel_registry.db`, SHA-256 `39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654`, sirf read-only khola.
- DB mein schema version number nahin hai (`user_version=0`). Build ki tareekh 2026-09-28 hai.
- **Channels: 75**, aap ka andaza ~73 tha. Wazahat: registry doc (2026-09-23) 71 batata hai. 2026-09-28 ko PR #6 ne 4 Senior Health channels jore (Doctor Thomas, Senior Health Hub, Decode Your Heart, Better Health While Aging). 71 + 4 = 75. 73 ka koi saboot nahin mila.

## 2. Incoming list

- 144 entries se 124 normalized URLs bane (20 repeats nikale, 15 suffix hataye). Note: raw 144-line list nahin mili thi, is liye occurrence counts Appendix ke summary se dobara banaye gaye hain.
- **120 ki UC ID verify hui. 4 handles HTTP 404 dete hain:** `@FrankSutherlandVA`, `@WilliamThorneUK01`, `@Olliee_Finance`, `@HealthDecoded-r9h`. Web search se bhi koi suraagh nahin mila, is liye yeh `IDENTITY_UNRESOLVED` hain.
- Koi do alag URLs ek hi ID par resolve nahin hue.
- **ALREADY_IN_DB: 5.** Primate Economics, Unknown Frequencies, Ink Explainer, Brofessor Stein (sirf identity), Dr. Elias.
- **NEW_TO_DB: 115.**
- **Package registry se bahar maujood hai: 14 incoming.**
  - 12 PR #39 mein (2026-10-20 ka snapshot).
  - MonkeyExplains PR #38 mein: 76 public, 45 members-only, 0 captions. **Dobara run ki zaroorat nahin.**
  - Dr. William Parker `DS-000034` mein (26 records). Yeh dataset DB mein hai magar channel register nahin hua.
- Existing side par Casual Finance DB mein sirf identity ke taur par hai. Is ka package PR #37/#46 aur CF hub mein maujood hai.

## 3. Niche tasweer (ID ki buniyad par, dedup ke baad 190 channels)

| Niche | Existing | Incoming | Combined |
|---|---:|---:|---:|
| FINANCE | 24 | 24 | 47 |
| SENIOR_HEALTH | 8 | 19 | 26 |
| HISTORY | 9 | 18 | 25 |
| ECONOMICS | 7 | 7 | 14 |

**Chautha group aap ko chunna hai.** Saboot ke saath candidates yeh hain:

- **SURVIVAL_STORYTELLING:** 21 channels, sab naye (zombie, bunker, disaster serials). Sab se bara group yahi hai.
- **HYPOTHETICAL_POV:** 9 channels (What-if).
- **PREHISTORY_HUMAN_ORIGINS:** 9 channels ("ancient humans" explainers, zyada tar existing).
- ANIMALS_NATURE aur GENERAL_HEALTH: 6–6 channels.

Ahem mushahidaat:

- Bohat se "senior" channels darasal **FINANCE ke sub-niche** hain (Social Security, Medicare, pensions), jaise Kevin Explains, Marcus Retires, Arthur Penrose UK aur Walter Canada. Health nahin, paisa ghalib hai.
- Identity drift: registry ka "Overhead" ab "911 Bodycam" (@911BWC) hai, aur "Nostalgic Wheels" ab "The Wealth Cortex" hai. ID dono mein wahi hai.

**Ehtiyaat:** classification AI ki tafseer hai, jo titles aur description par mabni hai. Thumbnails nahin dekhe gaye. Jahan description khud presentation nahin batati, wahan `channel_type` UNOBSERVED likha hai.

## 4. Access ka tareeqa

Har channel ka public `/videos` aur `/shorts` page bina login ke HTTP se parha gaya. Har page se 8 recent titles, Shorts tab ke 4 titles, description, subscriber count aur page SHA-256 liye gaye. Firefox/browser session use nahin hua, kyunke 124 channels ke liye woh mehenga tha. Agar aap chahein to B1 channels ka browser se thumbnail spot-check kiya ja sakta hai. Koi media download nahin hua.

## 5. Apify queue (sab `NOT_APPROVED`)

| Action | Channels |
|---|---:|
| NEW_FULL_SNAPSHOT | 74 (B1: 15, B2: 59) |
| GAP_FILL | 5 |
| REUSE | 54 |
| HOLD | 61 (chautha group ka faisla baqi + 4 unresolved + 1 identity drift) |

**Pehla batch B1 (tajweez), 15 naye channels, 4 priority niches:**

- FINANCE: Kevin Explains, Lana Maynes, Mark Calloway, Marcus Retires.
- ECONOMICS: Capital Case, Business Decoded, Built On You.
- SENIOR_HEALTH: Dr. Vitalis, Dr. Cale Smith, Dr. Wade Collins, Dr. Dinnes Senior.
- HISTORY: Historically, ThePastInLines, Ethos, Rome Unscrolled.

Kharch ka andaza:

- 810 results ki limit, taqreeban **$3.24 (estimate)**. Yeh 2026-09-20 ke $4.00/1,000 ke rate par hai, jo live dobara check karna hoga.
- Pilot ka thora sa izafa alag hai.
- **Tajweez karda ceiling: $3.50.** Free credits bhi isi budget mein ginay jayen ge.

## 6. Aap se manzoori chahiye

1. B1 ki exact channel IDs (workbook ke Apify Queue mein `proposed_batch=B1`), har channel ki result limit, aur dollar ceiling.
2. Chautha niche group.
3. Captions: kya B1 mein existing-subtitles mode on ho (paid transcription off rahe)?
4. 4 unresolved handles ke liye sahih URL ya UC ID.
