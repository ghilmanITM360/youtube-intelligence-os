# Casual Economics — Performance and Virality Research (11 videos)

Research only. The channel has **11 public videos** and 92,500 subscribers (DS-000036 snapshot 2026-10-12T09:38:39Z). With n = 11, nothing here is statistically reliable. Each conclusion carries one of these labels: **SUPPORTED** (direct evidence, consistent), **PLAUSIBLE** (consistent evidence, alternative explanations remain), **WEAK_EVIDENCE**, or **UNKNOWN**.

**Private analytics are UNKNOWN for every video:** CTR, impressions, retention, traffic-source mix (Browse/Suggested/Search/external), RPM/earnings and subscriber conversion. Nothing in this document infers them.

Data files: `PERFORMANCE_COMPARISON.csv` (metrics), `TRENDS_WINDOWS.csv` + `TRENDS_RAW.json` (per-video Google Trends windows), `TOPIC_DEMAND.csv` + `TOPIC_DEMAND_RAW.json` (cross-topic demand), `NEWS_CONTEXT.md` (dated events), plus the collectors `collect_trends.py` and `collect_topic_demand.py`.

## 1. Performance

Historical snapshot 2026-10-12 versus current public watch-page counts retrieved 2026-10-14 ~18:15Z, a 2.36-day gap. The Greece watch page returned `LOGIN_REQUIRED` to an unauthenticated request, so its current views are UNAVAILABLE. Recent views/day is the change across that 2.36-day gap and is very noisy.

| Tier | Video | Published | Views (snapshot) | Lifetime views/day | × median | Recent views/day | Likes /1k | Comments /1k |
|---|---|---|---|---|---|---|---|---|
| STRONG | Great Depression in 12 Minutes `qF3ekm9Gx_E` | 2025-03-19 | 3,116,682 | 5,452 | 6.25 | 1,311 | 20.2 | 1.43 |
| STRONG | How The Big Short Actually Happened `Iwz0fhJWN9Q` | 2026-07-29 | 238,165 | 3,197 | 3.67 | 1,785 | 15.5 | 0.65 |
| STRONG* | Lee Kuan Yew / Singapore `kbPauzdHhcI` | 2026-09-19 | 52,212 | 2,320 | 2.66 | 139 | 12.8 | 0.84 |
| TYPICAL | Debt Crisis Ruined Greece `nr5dcBPACH0` | 2026-03-22 | 261,380 | 1,283 | 1.47 | UNKNOWN | 16.1 | 1.82 |
| TYPICAL | 2008 Financial Crisis in 12 Minutes `APlGPpM-nBo` | 2025-08-26 | 406,244 | 987 | 1.13 | 956 | 13.0 | 0.86 |
| TYPICAL | Switzerland INSANELY Rich `3tVMjRRXQIg` | 2024-03-26 | 810,708 | 872 | 1.00 | 299 | 14.8 | 0.73 |
| TYPICAL | Ancient Rome Worst Collapse? `rl6ggpS13ao` | 2026-05-31 | 80,952 | 605 | 0.69 | 87 | 19.8 | 1.41 |
| TYPICAL | Japan's Lost Decade in 16 Minutes `x_MZu-QF-6o` | 2025-06-11 | 204,074 | 419 | 0.48 | 412 | 20.1 | 1.06 |
| WEAK | How Dubai Got So Rich `N9GUfsfiM4M` | 2024-09-08 | 186,506 | 244 | 0.28 | 84 | 17.7 | 1.00 |
| WEAK | Did Norway Create a Perfect Economy? `xVhMZPiIIGs` | 2026-01-31 | 31,084 | 122 | 0.14 | 100 | 28.1 | 3.54 |
| WEAK | How Did The Great Depression Affect Europe? `VTx478EUybo` | 2025-11-11 | 29,302 | 88 | 0.10 | 46 | 27.7 | 2.22 |

Tiers use lifetime views/day relative to the median (872): STRONG ≥ 2×, WEAK < 0.4×. **Caveat (*)**: lifetime views/day favours young videos because launch bursts decay. Singapore is 22 days old and its recent rate (139/day) is far below its lifetime rate, so its STRONG tier is provisional. Older videos with steady recent rates (Great Depression 1,311/day after 19 months; 2008 at 956/day after 13 months; Japan at 412/day) show **evergreen long tails**.

**Findings:**
- One breakout: the Great Depression video has 3.1 M views, about 57% of the eleven-video total (5.42 M). **SUPPORTED** (counts).
- It was the channel's 3rd upload. The two follow-ups with the same "[Event] in N Minutes (Casual Economics)" formula (Japan, 2008) are TYPICAL rather than breakouts, but both keep high recent velocity. **SUPPORTED** (counts); any reason for this is UNKNOWN.
- Engagement ratios are inversely related to reach. The weakest videos (Norway, Europe) have the highest likes/1k (≈28) and comments/1k. This pattern fits a small audience made up mostly of existing subscribers. **PLAUSIBLE.** Engagement ratios cannot explain reach.

## 2. Titles and thumbnails

| Pattern | Strong/typical examples | Weak examples | Verdict |
|---|---|---|---|
| Canonical, high-demand event name as the first words ("The Great Depression…", "The 2008 Financial Crisis…", "The Big Short") | GDP, C08, BSH | — | **PLAUSIBLE** advantage. These terms have the highest YouTube search demand of the channel's topics (§4), though Japan's term has almost none and still performs typically. |
| Question titles ("Did Norway…?", "…Affect Europe?", "…in History?") | Rome (typical) | Norway, Europe | **WEAK_EVIDENCE** that question framing underperforms. It is confounded with niche topics. |
| Regional sub-topic of a hit ("Great Depression → Europe") | — | Europe (weakest of all, despite riding the same keyword) | **PLAUSIBLE** that a sub-angle on a solved query attracts little demand. Counterexample to "repeat the winning topic". |
| "How [place] got rich" | Switzerland (typical, 810k) | Dubai (weak) | **WEAK_EVIDENCE**. The two cases split. |
| Thumbnail template: "THE + EVENT" headline, red zigzag down arrow, large panicked figure, small protest group | GDP (strong), C08 (typical) | Europe (weak; same arrow + map + panicked figure) | **UNKNOWN causal effect.** The same template appears in the top video and the weakest. Packaging alone does not explain the outcome. |
| Big numeric stat in thumbnail | none use one | — | Not testable. |
| Mobile legibility (headline + face readable at 160×90) | all reviewed thumbnails pass | all pass | No discriminating power. |

The Big Short thumbnail breaks the house style (stacked title, four portrait arrows, no distressed face) and is still STRONG. It borrows recognition from a famous film/book title. **PLAUSIBLE** that named-entity recognition matters more than template.

## 3. Topic selection and scripts

| Factor | Evidence | Verdict |
|---|---|---|
| Evergreen, school-curriculum crises (Great Depression, 2008) | high persistent YouTube search demand (§4); steady recent views/day | **PLAUSIBLE** main driver of long-tail reach |
| Contemporary news relevance at publication | GDP: tariff crash and Smoot-Hawley comparisons 2–3 weeks after upload (§5); Europe: "great depression" interest was elevated at upload yet the video is weakest | **WEAK_EVIDENCE**. A timing coincidence is not causation, and there is a direct counterexample |
| Country-wealth mechanism stories (Switzerland, Dubai, Norway, Singapore) | wide spread: 810k / 187k / 31k / 52k | **UNKNOWN**. The format can work (Switzerland) but is not reliable |
| Script structure | all 11 share the same cold-open contrast + question, chronological spine, literal metaphors and lesson ending (see channel DNA). Structure is nearly constant while results vary 60×. | **SUPPORTED** that script structure alone does not explain differences |
| Declared sources | descriptions cite sources for Japan, Greece and Rome but not for Great Depression or 2008. The top performer cites none. | **SUPPORTED** that visible source citation did not determine reach |
| Research accuracy issues | found in strong and weak videos alike (GDP -90% vs -70/-68% labels; Dubai 1983/1985; Norway Ekofisk date) | no discriminating power |
| Runtime | 615–1002 s. The top video is 720 s, the weakest 825 s, and Japan the longest (1002 s, typical) | **WEAK_EVIDENCE** for shorter = better |
| Topic originality | the highest-performing topics are the most crowded (many competing explainers exist) | **PLAUSIBLE** that demand outweighs originality for this channel. Competitor data not collected. |

## 4. Topic demand (Google Trends, worldwide, 2022-01-01 → 2026-10-13)

Mean interest relative to "great depression" (= 1.0) within shared comparisons (`TOPIC_DEMAND.csv`):

| Term | YouTube search | Web search |
|---|---|---|
| roman empire | 3.83 | 1.23 |
| the big short | 2.03 | 0.52 |
| great depression | 1.00 | 1.00 |
| lee kuan yew | 0.57 | 0.11 |
| 2008 financial crisis | 0.33 | 0.11 |
| dubai history | 0.20 | 0.22 |
| norway economy | ~0.005 | 0.04 |
| switzerland economy | ~0.003 | 0.06 |
| greece debt crisis | ~0.000 | ~0.003 |
| japan lost decade | 0 | 0 |

Interpretation:
- Topic demand matters but does not decide the outcome. "roman empire" has the highest YouTube search demand, yet the Rome video is TYPICAL. Switzerland and Greece have almost no demand for the tested terms yet reached 810k and 261k. Those videos likely drew on recommendation (browse/suggested) audiences or on other query phrasings ("why is switzerland so rich"). Traffic source is UNKNOWN. **PLAUSIBLE.**
- Search term choice limits this analysis: each topic was tested with one phrasing only. **Limitation.**

**Publication windows** (`TRENDS_WINDOWS.csv`, worldwide, daily, normalized per request): averages for d-90..-31, d-30..-8, d-7..-1, publication week, d+7..+30 and d+31..+60, plus peak date.
- Great Depression (2025-03-19): YouTube-search interest rose from 27 → 47 average in the 30 days after upload, peaking **2025-04-09** (web peak 2025-04-03). This aligns with the April 2025 tariff announcements, market sell-off and Smoot-Hawley comparisons (§5). **PLAUSIBLE** contributor to early momentum; causation UNKNOWN.
- 2008 Crisis (2025-08-26): interest rose after upload (web +30 days avg 74.7, peak 2025-09-25, near the Lehman anniversary). No single dominant news trigger was found. **WEAK_EVIDENCE.**
- Europe Depression (2025-11-11): "great depression" interest was at its window peak in the week of upload (YouTube 2025-11-05, web 2025-11-12), yet the video is the weakest. **Counterexample. SUPPORTED** that topical interest at upload was insufficient.
- Big Short (2026-07-29): YouTube interest was flat-high (~60) throughout, with a peak on 2026-06-01, before upload. No reliable news trigger was found. **UNKNOWN.**
- Rome (2026-05-31): consistently high, evergreen. Singapore (2026-09-19): YouTube interest *declined* into upload (peak 2026-08-02, near Singapore National Day period). Greece: very low-volume series (sparse zeros), small web bump 2026-03-27 right after upload, no linked news found. Japan, Switzerland and Norway (YouTube): insufficient data / zeros.

## 5. News context (see `NEWS_CONTEXT.md`)

Only the Great Depression video has a clearly dated, credible-source event in its window: the April 2–9, 2025 "Liberation Day" tariffs and market drop, which were widely compared with Smoot-Hawley (LPL Research, NAM, CNBC/Cramer commentary). The video's own tariff section (480–540 s) covers Smoot-Hawley and retaliation, so the topic matched what people were searching for. Searches for September 2025 (2008), November 2025 (Europe), June 2026 (Burry) and March 2026 (Greece) found no dominant trigger. Some low-quality or undated pages were discarded.

## 6. Discovery / SEO

Public tags (watch-page `keywords`, retrieved 2026-10-14): every video tags exact-match head terms ("great depression explained", "2008 financial crisis explained", "japan economy explained", "history of dubai"). Switzerland's tags include a competitor channel name ("economics raven"). Descriptions are a summary paragraph plus music credits (plus source notes for Japan, Greece and Rome).

YouTube's official documentation says search ranks by **relevance (title, tags, description, content), engagement (e.g. watch time for that query) and quality/authority**. Recommendations are personalized from watch/search history, subscriptions, likes and "not interested" feedback, and **satisfaction surveys** (valued watch time) are modelled for everyone ([How YouTube recommendations work](https://support.google.com/youtube/answer/16089387?hl=en); [On YouTube's recommendation system](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/); [Search & discovery tips](https://support.google.com/youtube/answer/11914225?hl=en)).

Hypotheses (not findings):
1. The Great Depression video's title is an exact match for a high-volume evergreen query, so search plus "suggested next to other Depression videos" likely sustains it. **PLAUSIBLE**; traffic-source split UNKNOWN.
2. Switzerland and Greece reached 0.26–0.81 M views with near-zero search demand for the tested terms, which suggests browse/suggested distribution. **PLAUSIBLE**; UNKNOWN without analytics.
3. A sub-topic of a hit (Europe) can be crowded out by the channel's own winner and by competitors on the same query. **WEAK_EVIDENCE.**
4. Satisfaction/retention probably differs between videos, but it is unobservable here. **UNKNOWN.**

## 7. Conclusions

| Claim | Verdict |
|---|---|
| The channel's success is concentrated in one evergreen breakout (Great Depression) | **SUPPORTED** |
| Production style is near-constant across videos, so style alone does not explain the performance spread | **SUPPORTED** |
| High-demand canonical topics with exact-match titles tend to perform better | **PLAUSIBLE** (Japan, Rome and Switzerland are counterexamples in different directions) |
| The April 2025 tariff news amplified the Great Depression video | **PLAUSIBLE** (timing plus topic match; no traffic data) |
| Question-style titles underperform | **WEAK_EVIDENCE** |
| The thumbnail template drives views | **UNKNOWN** (the same template is in the best and worst videos) |
| Higher like/comment ratios lead to more reach | **Not supported**. Ratios are highest on the weakest videos |
| CTR, retention or traffic source explain the differences | **UNKNOWN** (private analytics) |

**Useful patterns for an original channel (hypotheses to test, not formulas):** prioritise evergreen, high-demand economic events with exact-match titles; time uploads ahead of predictable news cycles but do not rely on them; avoid narrow sub-angles of already-saturated queries; measure CTR and retention in first-party analytics before generalising.
