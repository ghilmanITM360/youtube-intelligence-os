# PENNY @pennyexplainsfinance (070, outside the 69-channel DB) — Apify + Chrome + vidIQ pass, 2026-11-13


> **Correction 2026-11-13:** this channel was not in the DB/tracker, but an earlier Apify spot scrape of it exists in `05_OWNER_QA/` (`APIFY_SPOT_SCRAPES_README.md`, `CHANNEL_QA_pennyexplainsfinance.md`, snapshot 2026-11-12, 13 of 18 videos, 7.69k subs). I missed it because a repo-wide search errored. This 2026-11-13 pass supersedes that snapshot (now 13 long + 5 Shorts = 18 of 18, 7.83k subs); the two agree on the main numbers (e.g. $40T video 1,151,039 then vs 1,151,493 now).

Labels: VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN. Studio CTR, retention, traffic-source split are UNKNOWN (no Studio access).
**Source:** this channel is NOT in `finance_economics_complete.db` (69 channels) or MASTER_TRACKER. Data = Apify "YouTube Scraper" run `dnL4zjyF4Ec7G4yLa` (owner's Apify account, 2026-11-13 16:44, 21 requests, $0.068, input: channel UCrq_LwknwB3P9rSWy5CLTvQ, 30 videos + 30 shorts). Raw file: `raw/apify_youtube_scraper_dnL4zjyF4Ec7G4yLa.json`, SHA-256 `a3b6a802b97820badc718834d99fd46bb26dbe04b423151c2d121715c39b8dd6` (same as Downloads copy). Not added to the DB or tracker.

## 0. Seedhe jawab (Roman Urdu)

**1. Channel kis cheez ka promise karta hai?** "Paisa/economy ki bari khabar ya sawal ('America ka $40 trillion qarz kis ka?', 'AI bubble phat gaya?') 'Explained Like You're 5' style mein 9-17 minute mein, ek sikke ke sir wale cartoon 'Penny' ke saath." (INFERRED; 13 long videos ke titles, description "Money, explained like you're 5. Hi, I'm Penny. Yes, my head is a coin.") Apify: 7,830 subscribers, 18 videos (13 long + 5 Shorts), total views 1,529,247, joined Oct 16, 2026 (VERIFIED). **Channel sirf ~4 hafte purana hai.**

**2. Kaun sa model baar baar chalta hai?** (VERIFIED, Apify + live)
- 13 long videos 16 Oct - 11 Nov 2026, lagbhag roz ya har doosre din 1 video; 5 Shorts (28 Oct onwards), sab 145-1,618 views, yaani Shorts ne kuch nahi diya.
- Long views: 1,151,493 / 148,503 / 99,362 / 44,478 / 40,193 / 13,586 / 13,455 / 9,388 / 7,206 / 6,235 / 5,716 / 4,324 / 3,269. **Median 13,455**; 13 long videos ke total views (1,547,208) ka ~74% ek video (1.15M, "Who Does America Owe $40 Trillion?") se aata hai. Us ke bagair baqi 12 ka median ~11.4k.
- Titles: 7 mein "(Explained Like You're 5)" (median 40k, 1.15M se 3.3k tak), 6 baqi (median 8.3k). Farq hai magar ELI5 ke andar bhi 1.15M se 3.3k tak phailao hai.
- Cadence ka asar UNKNOWN: 13 long videos 27 din mein; kya zyada upload ne har video ki reach kam ki, ye isolate nahi kar sakta.

**3. Similar videos fail kyun hoti hain?** (INFERRED, LOW; 13 videos, 4 hafte, Studio nahi)
- Strong (views): America Owes $40T 1.15M, "Is the AI Bubble About to Pop?" 148.5k, "Did the AI Bubble Just Burst?" 99k, Renting vs Buying 44.5k, Nvidia in Big Trouble 40k.
- Weak: Japan trade 7.2k, "1 cent doubles" 6.2k, "Google Lost $500 Billion" 5.7k, ASML 4.3k, Who Owns the Federal Reserve 3.3k.
- **Same topic, bohat alag result:** "$40T" topic par 1.15M (owes kis ko) vs 13.6k ("Ponzi scheme?") vs 3.3k (Fed). AI-bubble topic par 148k, 99k, 40k aur 5.7k (Google), 4.3k (ASML). Matlab topic akela nahi, framing/sawal bhi farq karta hai (INFERRED). Abstract/institution wale sawal (Fed kis ka, paisa kahan se) 3k-9k par; seedha "meri jeb/ghar/naukri/bubble" wale 40k-148k.
- **Age ka confound:** 5 weak mein se 4 sirf 5-9 din purani (3-10 Nov), jab ke strong mein 3 pehle hafton ki (20-29 Oct). Nvidia (11 Nov, 2 din) already 40k aur Google video VPH 88, to naye videos abhi bhi chal rahe hain. Isliye "weak" abhi final nahi (UNKNOWN).
- vidIQ engagement: strong 0.7-2.2%, weak 1.2-2.0%; engagement % farq nahi karta (INFERRED).
- vidIQ outlier: $40T 14.5x, "AI bubble burst" 12.8x, Nvidia 10.7x (channel ke apne baseline se; 4 hafte purane channel ka baseline bhi naya hai, isliye zyada nahi padhna).
- Retitle/test: ASML video Apify mein "Why Can't Anyone Copy ASML? (Explained Like You're 5)" aur live list mein "Why Can Only One Company Build This $400 Million Machine?" dikha; title badla ya A/B tha, UNKNOWN.

**4. Naye channel ke liye pehli video?** (HYPOTHESIS) Is channel se: ek 4 hafte purane channel ne ek video par 1.15M liya, baqi 12 ka median ~11.4k. Yaani naya channel bhi ek "bara, deen/qarz/bubble wala sawal jo viewer se juda ho" par break ho sakta hai, magar ye ek video hai, repeatable nahi (n=1). Test: ek seedha, rozmarra paisa ka sawal ("X ko kitna qarz dena hai?") ELI5 title ke saath, 13-15 min, ek hi topic. Pehli video mein institution ya "paisa kahan se aata hai" jaisa abstract sawal mat lo. Iske baad same topic ke 2 angle test karo (jaise yahan $40T ke 3 angle: 1.15M / 13.6k / 3.3k).

**5. PDF rule?**
- **P21 topic selection (Playbook p.33)**: partial support. Topic aur framing ne 1.15M vs 3.3k banaya, magar age confound hai.
- **P05 formats**: partial. ELI5 title wali 7 ka median 40k vs baqi 6 ka 8.3k, magar ELI5 ke andar 1.15M-3.3k.
- **P13 stakes (pp.283, 320)**: strong titles mein bara number/stake ("$40 Trillion", "AI Bubble Burst", "Nvidia in Big Trouble"); weak mein bhi number ("$500 Billion") hai, to akela rule nahi. Opening transcript pada nahi gaya (neeche limits).

## 7. Evidence

### 7.1 13 long videos (Apify views at 16:44 UTC+5 scrape; vidIQ read this session; ALL long videos of the channel; 5 Shorts excluded)
Selection: strong = top 5, typical = next 3, weak = bottom 5 by Apify views.

| group | video_id | title (Apify) | published | length | views | likes | comments | vidIQ Eng / Outlier / VPH |
|---|---|---|---|---|---|---|---|---|
| strong | TmlvDH0ZFB4 | Who Does America Owe $40 Trillion? (Explained Like You're 5) | 2026-10-24 | 14:47 | 1,151,493 | 13,000 | 2,002 | 1.3% / 14.5x / 56.1 |
| strong | xZw6B0V6y3I | Is the AI Bubble About to Pop? (Explained Like You're 5) | 2026-10-20 | 13:13 | 148,503 | 930 | 103 | 0.7% / 1.8x / 385.6 |
| strong | QEcJOf32Vus | Did the AI Bubble Just Burst? Explained Like You're 5 | 2026-11-06 | 15:42 | 99,362 | 703 | 83 | 0.8% / 12.8x / 72.8 |
| strong | WYE_t61pUio | Renting vs Buying: The Real Math Over 20 Years | 2026-10-29 | 11:11 | 44,478 | 744 | 214 | 2.2% / 1.7x / 2.5 |
| strong | mKZw4C09wX8 | Nvidia Is in Big Trouble (Explained Like You're 5) | 2026-11-11 | 13:18 | 40,193 | 242 | 41 | 0.7% / 10.7x / 1.7K |
| typical | jyqH4fOgozg | Is America's $40 Trillion Debt a Ponzi Scheme? | 2026-11-05 | 14:00 | 13,586 | 123 | 42 | 1.2% / 1.7x / 0.5 |
| typical | HUf-eA4-mL0 | Why Is Everything So Expensive? (Explained Like You're 5) | 2026-10-26 | 6:29 | 13,455 | 342 | 36 | 2.8% / N/A / 3.8 |
| typical | cN7kUSh8OZA | Where Money Actually Comes From | 2026-10-16 | 12:42 | 9,388 | 162 | 23 | 2.0% / N/A / 2.5 |
| weak | Asl_DSYdCEw | The Crazy Trade That Crashed Japan in One Day | 2026-10-27 | 9:55 | 7,206 | 121 | 7 | 1.8% / N/A / 6.4 |
| weak | -R6L1Im7QFA | What If You Started With 1 Cent and It Doubled Every Day? | 2026-11-03 | 9:20 | 6,235 | 61 | 14 | 1.2% / N/A / 6.1 |
| weak | bqvAk1Vdi-s | Google Just Lost $500 Billion. Here's How It Started | 2026-11-09 | 16:38 | 5,716 | 63 | 9 | 1.3% / N/A / 88.5 |
| weak | W6UeshCISgI | Why Can't Anyone Copy ASML? (live: Why Can Only One Company Build This $400 Million Machine?) | 2026-11-10 | 17:03 | 4,324 | 56 | 6 | 1.4% / 1.2x / 26.1 |
| weak | cwF2buAF4Mk | Who Owns the Federal Reserve? (Explained Like You're 5) | 2026-11-07 | 13:01 | 3,269 | 60 | 6 | 2.0% / N/A / 10.5 |

Apify and live-page views matched within rounding (e.g. live 1.1m, 148k, 99k, 44k, 40k). Dates are Apify `date`; the dataset has day only.

### 7.2 Shorts (5, all in the last 2 weeks)
Who Really Gets Rich in a Gold Rush? 1,618; $500 Every Second Since Jesus 1,604; Most People Are Wrong About Who America Owes 1,103; He Was Right About AI 432; Why Inflation Punishes Savers 145.

### 7.3 Web
One standard search: no page about @pennyexplainsfinance or "PENNY" with this format found; owner/creator and team UNKNOWN. Description says the host is a character "Penny" with a coin head (VERIFIED, channel description in Apify).

### 7.4 Limits
- Not done: transcripts/opening lines (Apify scraper returned no subtitles; yt-dlp not installed), mid-video frames, thumbnail inspection, Google Trends, Studio data.
- Not in the 69-channel DB; no DB median or tracker row. Comparison to other channels used only the numbers above.
- Age, cadence, topic and title framing are confounded: channel is 4 weeks old, 4 of 5 weak videos are under 10 days old.
- 1.15M is one video; ~74% of the 1,547,208 total long-video views (Apify channelTotalViews 1,529,247 was a slightly older count). Channel-level conclusions from this are weak.
