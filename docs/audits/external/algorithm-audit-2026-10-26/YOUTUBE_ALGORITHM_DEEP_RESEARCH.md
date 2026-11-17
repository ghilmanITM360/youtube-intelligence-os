# YouTube Discovery & Recommendation — What Is Actually Known (as of 2026-10-26)

Audit package: `YIOS-Algorithm-Audit-2026-10-26` · Prepared read-only against repository HEAD `d987510b` (branch `research/finance-economics-intelligence`).
Sources were retrieved **2026-10-26** unless stated. YouTube Help pages show no revision date (footer "©2026 Google" only); treat them as *current as of retrieval*, not as dated publications.

## Evidence labels used throughout

| Label | Meaning |
|---|---|
| `OFFICIALLY_DOCUMENTED_CURRENT` | Stated on a current YouTube Help page or official YouTube blog, retrieved 2026-10-26 |
| `HISTORICAL_RESEARCH_DESCRIPTION` | Google/YouTube research paper or older official post describing a system at that time; not proof of today's architecture or weights |
| `EMPIRICALLY_OBSERVED_IN_YIOS` | Measured in our own corpus (see `YIOS_VIRALITY_HYPOTHESIS_TESTS.md`) — public proxies only |
| `PLAUSIBLE_HYPOTHESIS` | Consistent with official text and/or our data but not established |
| `UNKNOWN_OR_UNVERIFIABLE` | Not disclosed; cannot be checked from outside YouTube |

## 1. Sources inspected

| ID | Source | Type | Date shown | What it was used for |
|---|---|---|---|---|
| S1 | [YouTube's Recommendation System](https://support.google.com/youtube/answer/16533387) | Help | none (©2026) | Goals, signals, "fresh performance data for each individual video" |
| S2 | [How YouTube recommendations work](https://support.google.com/youtube/answer/16089387) | Help | none | Per-surface primary signal, 80B+ signals, negative feedback, surveys |
| S3 | [Understand your content performance for YouTube's recommendation system](https://support.google.com/youtube/answer/16559650) | Help | none | Appeal / Engagement / Satisfaction buckets; packaging advice |
| S4 | [Search & discovery tips](https://support.google.com/youtube/answer/11914225) | Help | none | "doesn't favor any particular format"; AVD/APV; topic interest, competition, seasonality |
| S5 | [YouTube performance FAQ & Troubleshooting](https://support.google.com/youtube/answer/141805) | Help | none | Search: title/description/content match + engagement for that search; "not a list of the most-viewed" |
| S6 | [How YouTube search works](https://support.google.com/youtube/answer/16090438) | Help | none | Relevance, engagement, quality (expertise/authoritativeness/trustworthiness); personalization |
| S7 | [Impressions & CTR FAQs](https://support.google.com/youtube/answer/7628154) | Help | none | CTR definition, 2–10% for half of channels, clickbait pattern, don't over-read small changes |
| S8 | [Understand your video reach](https://support.google.com/youtube/answer/9314355) | Help | none | Shorts "Stayed to watch" definition; AVD among those who stayed |
| S9 | [A/B test titles & thumbnails](https://support.google.com/youtube/answer/13861714) | Help | none | Up to 3 variants; winner by **watch-time share**, not CTR; long-form only; ≤2 weeks |
| S10 | [On YouTube's recommendation system](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/) — C. Goodrow | Official blog | 2021-09-15 | History: popularity → watch time (2012) → surveys / "valued watchtime"; borderline demotion; no set formula |
| S11 | [Deep Neural Networks for YouTube Recommendations](https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/) — Covington, Adams, Sargin | RecSys 2016 | 2016 | Two-stage candidate generation → ranking; expected-watch-time objective; "example age" feature. PDF SHA-256 `efb4aa82…ed482ab` |
| S12 | [Recommending What Video to Watch Next: A Multitask Ranking System](https://research.google/pubs/recommending-what-video-to-watch-next-a-multitask-ranking-system/) — Zhao et al. | RecSys 2019 | 2019 | Multiple competing objectives (MMoE); selection/position bias correction |
| S13 | [Top-K Off-Policy Correction for a REINFORCE Recommender System](https://arxiv.org/abs/1812.02353) — Chen et al. | WSDM 2019 | 2019 | Logged-feedback bias; exploration in a production YouTube top-K recommender |
| S14 | Better Generalization with Semantic IDs (arXiv:2306.08121, RecSys 2024) | Google research | 2024 | Content-derived IDs for cold-start items in a YouTube ranking model — previously validated in `data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md` (not re-fetched today) |

Third-party Shorts guides (vidIQ, socialinsider, contentstudio, etc.) were seen in search results only. They are **not** used as authority; where they are mentioned it is to mark a claim as *unverified*.

## 2. The stated objective

- **`OFFICIALLY_DOCUMENTED_CURRENT`** — Two goals: "help each viewer find videos they want to watch" and "maximize long-term viewer satisfaction" (S1).
- **`OFFICIALLY_DOCUMENTED_CURRENT`** — Performance signals are grouped as **Appeal** (chose to watch vs ignored / "not interested"), **Engagement** (whether viewers stay), **Satisfaction** (whether they enjoyed it). Specific signals vary by format (S3).
- **`HISTORICAL_RESEARCH_DESCRIPTION`** — The objective moved from popularity → clicks → watch time (2012; first change reportedly cut views ~20%) → survey-trained "valued watchtime" counting only time on videos rated 4–5★ (S10, 2021). Use this as history, not as the 2026 loss function.
- **`OFFICIALLY_DOCUMENTED_CURRENT`** — The system "doesn't follow a set formula" (S10); weights differ by surface (S2) and by user — e.g. a user who shares everything gets less weight on shares (S10).

**What follows:** there is no single public "algorithm score", no published CTR threshold that triggers distribution and no fixed feature weights. Any YIOS artifact that implies one would be inventing it.

## 3. Mechanisms, one at a time

| Mechanism | What is known | Label |
|---|---|---|
| Candidate generation → ranking | A two-stage system that cuts millions of videos to "hundreds", then ranks them (S11). | `HISTORICAL_RESEARCH_DESCRIPTION` (2016) |
| Per-viewer, real-time personalization | Each viewer's profile is analysed in real time (device, time of day, past habits) (S1). Home relies "primarily" on watch history (S2). | `OFFICIALLY_DOCUMENTED_CURRENT` |
| Collaborative filtering / interest affinity | The system learns from topic preferences and "what similar viewers watch" (S1). 2016: embeddings of watch and search history (S11). | Current at the principle level; architecture historical |
| Content representation | Content-derived Semantic IDs were tested in a YouTube production ranking model and helped cold-start (S14). Exact modalities used today are unknown. | `HISTORICAL_RESEARCH_DESCRIPTION` + `UNKNOWN` |
| Multi-objective ranking | Engagement and satisfaction objectives are balanced with MMoE-style multi-task models; position/selection bias is modelled (S12). | `HISTORICAL_RESEARCH_DESCRIPTION` (2019) |
| Engagement prediction | Ranking by expected watch time, because ranking by CTR "often promotes deceptive videos that the user does not complete ('clickbait')" (S11). Today: AVD and average percentage viewed are named ranking inputs (S4). | Historical, plus current at metric-name level |
| Long-term satisfaction | Surveys and a model that predicts survey answers for unsurveyed views (S10); surveys are listed as current signals (S1, S2). | `OFFICIALLY_DOCUMENTED_CURRENT` |
| Negative feedback | Dislikes, "Not interested", "Don't recommend channel" (S2). | `OFFICIALLY_DOCUMENTED_CURRENT` |
| Fresh evaluation of each video | "The algorithm uses fresh performance data for each individual video" (S1). Past results don't carry over automatically. | `OFFICIALLY_DOCUMENTED_CURRENT` |
| Exploration vs exploitation | Exploration and off-policy correction were used in a production YouTube recommender (S13). "Give as many videos as possible a chance to be discovered" (S1). | Historical mechanism; current stated intent |
| Feedback loops & selection bias | Logged feedback only covers what the previous recommender chose to show (S13), so a video that is never shown generates no signal. | `HISTORICAL_RESEARCH_DESCRIPTION` |
| Freshness / changing interests | 2016 used an "example age" feature so the model could represent recent uploads (S11). Today the system "adapts as viewing habits change" (S10). | Historical + current intent |
| Upload timing | Publish time "doesn't appear to affect long-term viewership"; premieres and lives benefit from audience-active timing (S1). | `OFFICIALLY_DOCUMENTED_CURRENT` |
| Upload frequency / breaks | Prioritize consistent quality over frequency; breaks aren't penalized (S1). | `OFFICIALLY_DOCUMENTED_CURRENT` |
| Format neutrality | The system "has no opinion about what type of video you make" (S4). | `OFFICIALLY_DOCUMENTED_CURRENT` |
| Competition & seasonality | Topic interest, competition from other channels and seasonality affect how many people see a video (S4). Videos are ranked against everything a viewer might watch, not just the channel's own videos (S7). | `OFFICIALLY_DOCUMENTED_CURRENT` |
| Borderline / authoritative content | Borderline content is demoted; authoritative sources are boosted for news and information, with expert raters (e.g. doctors for health) (S10). | Official (2021); current scope not re-verified |
| AI-made content | AI-made videos "can be recommended as broadly" as others (S2). Monetization's inauthentic/mass-produced policy is separate (prior YIOS validation). | `OFFICIALLY_DOCUMENTED_CURRENT` |
| Exact weights, thresholds, feature list, model sizes in 2026 | Not disclosed. | `UNKNOWN_OR_UNVERIFIABLE` |

## 4. Surfaces are different systems in practice

### A. Home / Browse
- **Official:** personalized and "primarily" driven by watch history, mixed with subscriptions and news (S2). Each viewer's profile is analysed in real time (S1). New videos are judged on their own fresh data (S1).
- **Why videos plateau** (`PLAUSIBLE_HYPOTHESIS`): exposure grows while viewers who are shown the video choose and enjoy it. Once the viewers whose interests match well are used up, the response from more distant viewers is weaker and impressions stop growing. This follows from S1/S3/S7 but YouTube has not stated it as a rule.
- **Why old videos keep getting views** (`PLAUSIBLE_HYPOTHESIS`, partly official): performance is evaluated per video and per viewer, with no stated expiry. Search engagement is per query (S5, S6). An evergreen topic can therefore keep matching new viewers and new queries.
- **YIOS observation** (`EMPIRICALLY_OBSERVED_IN_YIOS`): within channels, lifetime views grow far more slowly than age. The median within-channel slope of log(views) on log(age) is **0.34** (9 Finance channels) and **0.57** (29 channels across all niches). So "views per day since upload" falls with age, and raw views/day cannot be compared across ages. This is why every YIOS comparison is age-matched.

### B. Suggested / Up Next
- **Official:** "the video you're watching" is "the main signal" (S2).
- **Historical:** the 2019 multitask paper was specifically about what-to-watch-next ranking, with explicit position-bias modelling (S12).
- **Co-viewing / audience overlap** (`PLAUSIBLE_HYPOTHESIS`): suggestions draw on related-video relationships learned from what similar viewers watch (S1). How co-viewing is weighted today is undisclosed.
- **YIOS:** we have **no traffic-source data**, so we cannot tell which public views came from Suggested.

### C. Search
- **Official:** ranks on **relevance** (title, tags, description and video content match the query), **engagement** (e.g. "the watch time of a particular video for a particular query") and **quality** (expertise, authoritativeness, trustworthiness), with weights varying by query type (S6). Search results are "not a list of the most-viewed videos" (S5). Search is personalized when history is on (S6). Placement isn't sold (S6).
- **Difference from recommendation:** in search the viewer states the intent; recommendations are system-initiated. In search, engagement is measured *for that query*.
- **YIOS:** no search-volume, query or traffic-source data. "Renting vs Buying — The Real Math" is the strongest video on two separate channels (Logical Money 350×, Mark Invests 297×). That pattern is consistent with durable search demand, but it is a `PLAUSIBLE_HYPOTHESIS`; we cannot see the search traffic share.

### D. Shorts feed
- **Official:** the feed is personalized (S2). "Stayed to watch" is the percentage of times viewers stayed past the first seconds of a Short; Shorts AVD is computed among those who stayed (S8). The first seconds decide stay/leave for both Shorts and long-form (S3). Shorts can't be A/B tested (S9).
- **Not verified from a primary page today:** the "Viewed vs swiped away" wording, the "engaged views" definition and the March-2025 Shorts view-counting change. These were seen only in third-party articles. Treat them as unverified until read on a YouTube Help page.
- **YIOS:** Shorts and long-form lifetime views/day are **not comparable units**, because view counting and surface differ. In channels that publish both, medians differ in both directions (e.g. Casually Finance Shorts 217/day vs long-form 2,647/day; xkcd's What If? Shorts 4,676/day vs long-form 4,123/day). We do not compare them as performance.

### E. Other sources
- Subscriptions help suggest other videos; they guarantee neither distribution nor viewing (S2; prior YIOS validation CLM-008). Notifications, channel pages, playlists, end screens and external traffic are named as viewing paths. YouTube advises playlists, end screens and clear calls to action (S1). Views from impressions outside YouTube are not counted in CTR (S7).
- Live / Premiere timing matters for live audiences (S1).
- Cross-format bridging (a channel's Shorts audience being offered its long-form) was reported in 2026 through press and executive statements (prior YIOS validation S7). It has `PARTIALLY_SUPPORTED` status and was not re-verified today.

## 5. Practical rules of thumb that are *officially* supported

1. Packaging sets an expectation and the opening must pay it off quickly (S3). High CTR + low AVD + lower-than-expected impressions is the official clickbait pattern (S7).
2. Title/thumbnail tests are judged on **watch-time share**, not CTR (S9). A "winner" that lifts clicks but loses watch time is not a winner by YouTube's own test.
3. Don't read CTR early or act on small changes. Compare over the long term and by traffic source (S7).
4. Broader framing of a niche topic can widen reach. YouTube's own example retitles a coffee-market economics video as "Why Is Your Coffee So Expensive?" (S3).
5. Tags mainly fix misspellings. Titles, thumbnails and descriptions are the important metadata (S3).
6. Consistency of quality beats upload frequency; timing barely matters except for lives and premieres (S1).

## 6. Things commonly claimed that the official record does **not** support

| Claim | Status |
|---|---|
| "CTR above X% triggers distribution" | `UNKNOWN` — no threshold is published. Official: half of channels sit at 2–10% and CTR naturally falls as impressions grow (S7) |
| "The first 24/48 hours decide a video's fate" | Not stated. Official: fresh per-video evaluation and no set formula (S1, S10). Our data can't test it (no time series) |
| "Upload at the perfect hour" | Contradicted for long-term viewership (S1) |
| "Breaks kill your channel" | Contradicted (S1) |
| "Subscribers see every upload" | Contradicted (S2) |
| "Shorts and long-form must never share a channel" | Prior YIOS validation: `CONTRADICTED` in universal form (audience-overlap heuristic instead) |
| "Tags are critical for ranking" | Contradicted (S3) |
| "YouTube favours format X" | Contradicted at the policy level (S4) |
| "The 2016 paper is how YouTube works today" | Overreach: it is a historical description (S11) |

## 7. What can only be answered with owned-channel Studio data

Impressions, impressions CTR, traffic-source split (Browse / Suggested / Search / Shorts feed / External), retention curves including the first 30 s, relative retention, AVD, APV, stayed-to-watch for Shorts, new vs returning viewers, unique viewers, subscribers gained per video, survey-based satisfaction (not exposed to creators) and A/B-test watch-time share. YIOS holds **none** of these: 75/75 channels are `SCHEMA_READY_NO_DATA` in `youtube_channel_registry.db.channels.first_party_analytics_status`. See `RESEARCH_LIMITATIONS_AND_MISSING_DATA.md`.
