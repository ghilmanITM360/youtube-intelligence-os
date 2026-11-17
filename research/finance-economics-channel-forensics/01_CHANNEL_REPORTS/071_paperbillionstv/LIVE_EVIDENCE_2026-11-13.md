# Paper Billions @PaperBillionsTV (071, outside the 69-channel DB) — Apify + Chrome + vidIQ pass, 2026-11-13


> **Correction 2026-11-13:** this channel was not in the DB/tracker, but an earlier Apify spot scrape of it exists in `05_OWNER_QA/` (`APIFY_SPOT_SCRAPES_README.md`, `CHANNEL_QA_paperbillionstv.md`, snapshot 2026-11-12, 3 videos, 9.65k subs). I missed it because a repo-wide search errored. This 2026-11-13 pass supersedes that snapshot (now 4 of 4 videos, 14.1k subs); the two agree on the main numbers (e.g. Nvidia-spy 1,467,942 then vs 2,101,211 now; views were still rising).

Labels: VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN. Studio CTR, retention, traffic split are UNKNOWN.
**Source:** channel is NOT in `finance_economics_complete.db` or MASTER_TRACKER. Data = Apify "YouTube Scraper" run `JsyvS0PVokzdfwCAb` (owner's Apify account, 2026-11-13 17:02, 6 requests, $0.020, channel UCMQDlRCUK5Lh7kxp_fqFK3w). Raw: `raw/apify_youtube_scraper_JsyvS0PVokzdfwCAb.json`, SHA-256 `0dc7e70158345104afe374715a2f802692d537eb1876b6382cc8bdeabe53da01` (identical to Downloads copy). The file has 5 rows: 4 videos + 1 "channel has no Shorts" note row.

## 0. Seedhe jawab (Roman Urdu)

**1. Channel ka promise?** "Paisa ki bari, khabar mein chal rahi kahani (Nvidia, stock market crash, bara IPO) kagaz par bani drawing/cartoon mein 14-20 minute mein." (INFERRED; 4 titles; description "Money stories, drawn on paper.") 14,100 subscribers, 4 videos, 2,865,511 total views (VERIFIED, Apify). Koi Shorts nahi (VERIFIED, Apify note).

**2. Kaun sa model chal raha hai?** (VERIFIED numbers)
- **Poora channel sirf 4 videos hai, aur sab 6-13 Nov 2026 ke 8 din mein.** DB/sample ka sawal nahi, ye poori channel hai.
- Views: How a Chinese Spy Got Inside Nvidia 2,101,211 (10 Nov, 19:48); Why the Stock Market Just Crashed 1,142,123 (8 Nov, 15:00); Why Nvidia Would Fail Without Jensen Huang 472,238 (13 Nov, 14:20, ~10 ghante pehle tak); The Biggest IPO in History Lost $80 Billion 144,108 (6 Nov, 14:09). Median ~807k.
- Channel Apify ke mutabiq Sep 21, 2022 ko bana, lekin pehli video 6 Nov 2026 ki hai. Isliye "naya channel" ya purana dormant/repurposed channel, ye UNKNOWN hai (kya pehle videos hatayi gayi, UNKNOWN).
- Sab 4 videos ka vidIQ VPH bohat bara: 35.8K, 44.6K, 2.8K, 1.8K (24 ghante wale rate, jab scrape hua).

**3. Similar videos fail kyun hoti hain?** (INFERRED, bohat LOW; n=4, 8 din)
- Strong (views): Nvidia spy 2.1M, stock market crash 1.14M, Nvidia/Jensen 472k (sirf 10 ghante, abhi chadh rahi, VPH 44.6K).
- Weakest: "Biggest IPO Lost $80 Billion" 144k, jo sabse purani hai (6 Nov); is ka VPH ab 2.8K hai. Is ka wazahat (kamzor topic ya purani) alag nahi hoti.
- Nvidia par 2 videos (2.1M aur 472k+); do videos "market crash/IPO" par (1.14M, 144k). Topic-framing farq: kahani/jasoosi ("Chinese Spy") 2.1M vs company-nuqsan ("lost $80B") 144k, INFERRED.
- vidIQ engagement 0.5-0.8% (chaaron mein); farq nahi karta (INFERRED).
- Failure ka koi saboot nahi: sab 4 videos 144k+ par hain, naye channel ke liye bohat zyada.

**4. Naye channel ke liye pehli video?** (HYPOTHESIS) Is channel se nahi seekha ja sakta ke kya "fail" hota hai (n=4, koi fail nahi). Dekha gaya: khabar mein chal rahe bare company/market topic (Nvidia, crash) ko ek kahani (jasoosi, "kaise girta") ke angle se 14-20 min mein kagaz-drawing style mein, 8 din mein 4 videos. Pehle channel size/audience ka floor 14.1k hai, jo naye channel ke paas nahi; aur channel ki pehle se ki ginti (2022 join) UNKNOWN hai. Test: ek khabar mein chal raha bara company topic ek "kahani" angle se, 14-15 min, ek hi topic, uske 2-3 angle test karo.

**5. PDF rule?**
- **P21 topic selection (Playbook p.33)**: weak support. 4 videos sab khabar-wale bare topic; kaun sa topic choose hua yeh to dikhta hai, magar fail wala koi nahi to rule test nahi hota.
- **P05 formats**: ek hi format (kagaz drawing, 14-20 min); format ka alag test nahi (n=4).
- **P13 stakes**: titles mein stake ("Crashed", "Lost $80 Billion", "Fail", "Spy"); opening transcripts nahi parhe, to opening par kuch nahi keh sakta.

## 7. Evidence

| video_id | title | published | length | views (Apify) | likes | comments | vidIQ Eng / Outlier / VPH |
|---|---|---|---|---|---|---|---|
| _MG4v3foET8 | How a Chinese Spy Got Inside Nvidia | 2026-11-10 | 19:48 | 2,101,211 | 8,400 | 1,181 | 0.5% / N/A / 35.8K |
| zEUKLSrbRZk | Why the Stock Market Just Crashed | 2026-11-08 | 15:00 | 1,142,123 | 5,800 | 652 | 0.6% / N/A / 1.8K |
| Vy1m4ZXNzpo | Why Nvidia Would Fail Without Jensen Huang | 2026-11-13 | 14:20 | 472,238 | 2,900 | 587 | 0.8% / N/A / 44.6K |
| hPCywNDA60o | The Biggest IPO in History Lost $80 Billion | 2026-11-06 | 14:09 | 144,108 | 674 | 90 | 0.5% / N/A / 2.8K |

Apify and live page matched (live list at scrape time: 466k, 2m, 1.1m, 143k).

### Web
One standard search: no page about Paper Billions found; owner/team UNKNOWN. Unrelated "Paper Wealth" came up (not this channel).

### Limits
- Not done: transcripts/openings (Apify scraper returned none; no yt-dlp), mid-video frames, thumbnails, Google Trends, Studio data.
- Not in 69-channel DB; no tracker row.
- n=4 videos in 8 days: no strong/typical/weak split of 5/5/5 possible; channel age UNKNOWN (join date 2022, first video 2026-11-06). Views are still growing.
