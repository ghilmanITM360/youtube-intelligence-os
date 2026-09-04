# YouTube Algorithm Primary-Source Validation — 2026 Algorithm Update (DS-000018)

## Validation Scope

- Source dataset validated: DS-000018 — 2026 Algorithm Update — Multi-Tab Creator Research Corpus
- Source claim artifact: `data/intelligence/global/youtube-algorithm-source-intelligence-2026-09-02.md`
- Claims registered in that artifact: 33 (18 `SOURCE_CLAIM`, 5 `SOURCE_INTERPRETATION`, 10 `SOURCE_RECOMMENDATION`)
- Claims validated in this task: **exactly 12**, selected for highest impact on future topic selection, titles/thumbnails, hooks, format strategy, and opportunity discovery
- Claims not validated here: 21 (listed under "Claims Still Requiring Evidence")
- This artifact is an additional evidence layer. It does not modify, delete, or promote any of the 33 original claims, and it creates zero `MEASURED_FACT` rows.
- Artifact date: 2026-09-04

## Method

1. Read the DS-000018 structured claim artifact and, for each of the 12 selected claims, resolved its cited tab alias (T01/T36/T39/T48/T49/T51) back to the `source_files` table in `data/catalog/youtube_inventory.db`. All 7 referenced archive-member `FILE-*` IDs were found with `sha256` values matching the intelligence artifact's alias table exactly (see table below). Provenance for all 12 claims is confirmed.
2. Selected 12 claims from the 18 `SOURCE_CLAIM` + 5 `SOURCE_INTERPRETATION` records, prioritizing the themes named in the task brief (personalized discovery, audience/interest clustering, subscriber importance, satisfaction signals, recommendations, topic/audience alignment, Shorts vs. long-form, TV/living-room viewing, thumbnails/CTR, repetitive/mass-produced content, semantic/AI understanding, off-platform signals). `SOURCE_RECOMMENDATION` rows (creator strategy advice) were excluded from selection as instructed, except where a recommendation makes a direct algorithmic claim — none of the 10 recommendations met that bar cleanly enough to outrank the 12 chosen `SOURCE_CLAIM`/`SOURCE_INTERPRETATION` rows, so no `SOURCE_RECOMMENDATION` row was selected. This means the "off-platform/external signals" theme has no selected claim; the only DS-000018 row on that theme (`ALG26-REC-008`) is creator strategy advice, not an algorithmic claim, and was excluded (see "Claims Still Requiring Evidence").
3. For each selected claim, researched current official evidence using YouTube Help, the YouTube Official Blog, an official Google Research/DeepMind publication evaluated on YouTube's own production system, and on-the-record statements from named YouTube executives (Creator Insider / VidCon), per the task's primary-source priority list. Two of the eight sources used (S6, S7) are on-record official statements accessed through press reporting rather than a directly fetched primary video/blog post; this is flagged as a limitation on those specific claims rather than treated as secondary-source authority determining status.
4. Assigned exactly one of the five required validation states per claim, using the definitions given in the task brief.
5. Checked the 12 claims against each other (the DS-000018 artifact's own flagged CLM-005/CLM-018 conflict) and against other registered Global YouTube Knowledge (semantic class `A`) datasets in the catalog. Only DS-000011 (`All Training Data of YouTube — Global Knowledge Corpus`) shares that class, and its status is `INGESTED` — no structured claim artifact exists for it yet — so there is no other structured Global YouTube Knowledge to conflict against.

### Provenance re-verification

| Alias | FILE ID | DB `sha256` matches intelligence-artifact table | Selected claims using this member |
|---|---|---|---|
| T01 | FILE-006404 | ✅ match | ALG26-CLM-018 |
| T36 | FILE-006439 | ✅ match | ALG26-INT-002 |
| T39 | FILE-006442 | ✅ match | ALG26-CLM-001, 002, 004, 005, 008 |
| T48 | FILE-006451 | ✅ match | ALG26-CLM-009, 016, 017 |
| T49 | FILE-006452 | ✅ match | ALG26-CLM-014 |
| T51 | FILE-006454 | ✅ match | ALG26-CLM-012 |

## Primary Sources Used

| ID | Organization | Title | URL | Published/updated | Retrieved | Section used |
|---|---|---|---|---|---|---|
| S1 | Google / YouTube Help | YouTube's Recommendation System | https://support.google.com/youtube/answer/16533387 | ©2026 (no specific revision date shown) | 2026-09-04 | Overview: goals, signals, per-viewer real-time profiling, per-video "fresh" performance data |
| S2 | Google / YouTube Help | How YouTube recommendations work | https://support.google.com/youtube/answer/16089387 | ©2026 (no specific revision date shown) | 2026-09-04 | Signal volume, per-surface signal weighting, subscriptions as one input, negative feedback |
| S3 | Google / YouTube Help | YouTube channel monetization policies | https://support.google.com/youtube/answer/1311392 | Inauthentic-content policy updated 2025-07-15 | 2026-09-04 | "Inauthentic content" and "Reused content" definitions |
| S4 | YouTube Official Blog | YouTube CEO Neal Mohan's 2026 Letter: The Future of YouTube | https://blog.youtube/inside-youtube/the-future-of-youtube-2026/ | 2026-01-21 | 2026-09-04 | TV/streaming share (Nielsen), AI framed as recommendation engine, Shorts scale |
| S5 | Google Research / Google DeepMind | Better Generalization with Semantic IDs: A Case Study in Ranking for Recommendations | arXiv:2306.08121; ACM RecSys 2024 (DOI 10.1145/3640457.3688190) | RecSys 2024 (Oct 2024) | 2026-09-04 | Semantic IDs built from content embeddings, evaluated on YouTube's production ranking model |
| S6 | Creator Insider (YouTube's own creator-liaison channel), via Search Engine Journal | YouTube Says Bigger Thumbnails Drove More Long-Form Views | https://www.searchenginejournal.com/youtube-bigger-thumbnails-long-form-engagement/588102/ | 2025 | 2026-09-04 | Todd Beaupré (YouTube Sr. Director of Growth & Discovery) describing the homepage thumbnail-size test |
| S7 | Todd Beaupré, YouTube Director/Sr. Director of Discovery, on-record VidCon statement, via vidIQ and 2026 press coverage of the Shorts→long-form recommendation bridge | "Same audience? Same channel. Different audience? Different channel." | https://vidiq.com/blog/post/youtube-recommends-long-form-videos-shorts-viewers/ | Statement originally 2022; bridge update reported ~2026-08-18 | 2026-09-04 | Official channel-architecture guidance and 2026 Shorts/long-form discovery bridge |
| S8 | YouTube (official Shorts thumbnail feature launch), via press/community reporting, cross-checked against YouTube Help Shorts pages | Shorts thumbnail visibility across surfaces | e.g. https://phonearena.com/news/youtube-launches-features-for-creators-to-control-the-look-of-their-shorts-thumbnails_id162189 ; https://support.google.com/youtube/answer/12319243 | Feature launch reporting, undated precisely | 2026-09-04 | Where Shorts thumbnails do/don't appear (swipe feed vs. search/hashtag/channel) |

S6, S7, and S8 are official-statement or official-feature evidence reached through press/community reporting rather than a directly fetched primary blog post or video transcript. They are treated as weaker-confidence primary evidence, not as secondary-source authority — no validation status below rests on an unattributed blogger's interpretation.

## Claim-by-Claim Validation

### ALG26-CLM-001 — Personalized recommendation ranking
- **Original claim locator:** T39, 1:19–2:57 (FILE-006442)
- **SOURCE SAYS:** Recommendations are selected when a viewer loads a surface, using that viewer's history and current context to rank candidate videos for them specifically.
- **PRIMARY EVIDENCE SAYS:** S1 states the system analyzes "each viewer's profile in real time, which considers device, time of day, and past habits" and processes signals to rank candidates per viewer. S2 confirms 80B+ signals/day and per-surface signal weighting (e.g., Up Next uses the current video as the main signal; Home primarily uses watch history).
- **Validation status:** SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Recommendation ranking is per-viewer and per-surface, computed from real-time viewer signals rather than a single global ranking.
- **Confidence/limitations:** High confidence — two independent official Help pages describe this consistently.

### ALG26-CLM-002 — Subscriber importance: segmented learning
- **Original claim locator:** T39, 3:06–5:44 (FILE-006442)
- **SOURCE SAYS:** Early subscriber response is not one global verdict; the system can learn different responses for subscribers, non-subscribers, and new viewers separately.
- **PRIMARY EVIDENCE SAYS:** S1/S2 confirm subscriptions are one signal among many, and personalization is per-viewer. Neither page describes a specific mechanism that segments learning into subscriber / non-subscriber / new-viewer response cohorts for a given video.
- **Validation status:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Subscriber reaction should not be treated as a single verdict for how a video will be recommended to everyone; per-viewer personalization means different audience segments can plausibly see different outcomes. The specific "three-cohort learning" mechanism is a source interpretation, not something the primary documentation states.
- **Confidence/limitations:** Medium. The general principle is well supported; the precise architectural mechanism is unverified.

### ALG26-CLM-004 — Satisfaction / no single metric
- **Original claim locator:** T39, 9:57–15:37 (FILE-006442)
- **SOURCE SAYS:** Long-term user value is the broad objective; ranking uses multiple context-dependent signals, not one universal metric or fixed weight.
- **PRIMARY EVIDENCE SAYS:** S1 states the system's goals are "helping viewers find videos they want to watch and maximizing long-term viewer satisfaction," using watch history, satisfaction surveys, likes/dislikes, and performance metrics together. S2 shows different surfaces weight signals differently.
- **Validation status:** SUPPORTED
- **OS CAN SAFELY CONCLUDE:** No single fixed metric (e.g., CTR alone or watch time alone) should be treated as "the" ranking signal; long-term satisfaction, assessed through multiple signals, is the stated objective.
- **Confidence/limitations:** High confidence, directly stated across both YouTube Help pages.

### ALG26-CLM-005 — Channel/format alignment with audience
- **Original claim locator:** T39, 23:43–26:36 (FILE-006442)
- **SOURCE SAYS:** Channels should align with audiences, while recommendations may still distinguish topic, length, Shorts, long-form, podcast, or live-stream preferences within one channel.
- **PRIMARY EVIDENCE SAYS:** S7 (Todd Beaupré, on record): "Same audience? Same channel. Different audience? Different channel" — official guidance is conditioned on audience overlap, not format. The 2026 Shorts→long-form recommendation bridge (S7) shows YouTube actively recommends a channel's long-form videos to its own Shorts viewers, consistent with format coexistence when the audience is shared.
- **Validation status:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Whether to combine formats on one channel is best decided by audience overlap, not format alone — this matches official guidance. The more granular claim that recommendations separately track topic/length/Shorts/podcast/live preferences within a single channel is plausible but not confirmed by the sources found.
- **Confidence/limitations:** Medium. S7 is an on-record named-executive statement, but reached via press reporting rather than a primary blog/video directly fetched.

### ALG26-CLM-008 — Subscription does not guarantee interest
- **Original claim locator:** T39, 37:04–38:16 (FILE-006442)
- **SOURCE SAYS:** A subscription does not imply interest in every upload; the system seeks the interested subset rather than relying on aggregate subscriber click behavior.
- **PRIMARY EVIDENCE SAYS:** S1: "YouTube analyzes whether they choose to click, watch, or positively engage with the content" when a video is offered — including to subscribers. S2: subscriptions "help to recommend," not guarantee distribution.
- **Validation status:** SUPPORTED
- **OS CAN SAFELY CONCLUDE:** A large subscriber count does not mean a given upload will be shown to, or watched by, most subscribers; per-video engagement among the people it is shown to still governs further distribution.
- **Confidence/limitations:** High confidence, directly and consistently stated.

### ALG26-CLM-009 — Repetitive/templated spam vs. reusable format
- **Original claim locator:** T48, 6:56–9:06 (FILE-006451)
- **SOURCE SAYS:** Literal, near-identical templated repetition may be spam, while a reusable format stays acceptable when episodes differ meaningfully.
- **PRIMARY EVIDENCE SAYS:** S3 (YouTube channel monetization policies, "inauthentic content," updated 2025-07-15): content must be "original," "authentic," and must not be "mass-produced, generic, repetitive, or manipulative" or use "generic or unoriginal templates giving the impression of mass production."
- **Validation status:** SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Templated, near-identical episodes risk classification as inauthentic/mass-produced content under official policy; a format that varies meaningfully between episodes does not meet that description.
- **Confidence/limitations:** High confidence on the policy text itself. Important scope caveat: S3 governs YouTube Partner Program monetization eligibility, not confirmed recommendation-ranking behavior — the source claim conflates a "spam"/recommendation framing with what is documented as a monetization-eligibility policy. Treat this as validated for monetization risk, not proven for discovery/ranking suppression.

### ALG26-CLM-012 — Semantic IDs / large recommender model
- **Original claim locator:** T51, 4:28–5:52 (FILE-006454)
- **SOURCE SAYS:** YouTube uses a large recommender model and semantic IDs derived from metadata, frames, audio, pacing, and format.
- **PRIMARY EVIDENCE SAYS:** S5, a Google Research/DeepMind paper (arXiv:2306.08121, ACM RecSys 2024), confirms Google built Semantic IDs — discrete codes compressed via RQ-VAE from content embeddings — to replace opaque item IDs in a real-world, billion-scale YouTube ranking model, improving generalization and cold-start handling for new videos.
- **Validation status:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** YouTube has a published, peer-reviewed research basis for using semantic/content-derived IDs (not just opaque video IDs) in its production ranking system, which can help new/cold-start videos get matched to interested viewers. The specific list of input modalities named in the source claim (metadata, frames, audio, pacing, format) is more granular than what the paper's publicly available description confirms; it should be treated as directionally plausible, not verbatim confirmed.
- **Confidence/limitations:** Medium-high on the existence of the mechanism; low on the exact modality list.

### ALG26-CLM-014 — TV / lean-back viewing share jump (23–24% → 50%+)
- **Original claim locator:** T49, 1:06–2:02 (FILE-006452)
- **SOURCE SAYS:** A strategist reports TV rose from about 23–24% of selected clients' viewing in 2021 to more than 50% in the recent period.
- **PRIMARY EVIDENCE SAYS:** S4 (YouTube CEO 2026 letter) confirms YouTube has been "#1 in streaming watchtime in the U.S. for nearly three years" per Nielsen, and Nielsen's "The Gauge" shows YouTube holding roughly 12–13% of *total U.S. TV viewing time* (an aggregate market-share metric) through 2026. Neither source publishes a per-channel or per-client device-mix statistic like the one in this claim.
- **Validation status:** NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
- **OS CAN SAFELY CONCLUDE:** YouTube's overall growth on TV screens is independently confirmed as a real, large, ongoing trend. The specific self-reported client percentage jump from ~23% to 50%+ is a different metric (one agency's client-level device mix) that no primary source confirms or denies — "not found" here means unverified, not false.
- **Confidence/limitations:** The general TV-growth direction is well evidenced; the specific number is an unverified self-reported statistic and should not be repeated as an established figure.

### ALG26-CLM-016 — Homepage thumbnails: larger/fewer improved long-form
- **Original claim locator:** T48, 1:47–3:21 (FILE-006451)
- **SOURCE SAYS:** Experiments with larger, fewer homepage thumbnails improved selection and long-form viewing while smaller/new-channel recommendations remained near the top.
- **PRIMARY EVIDENCE SAYS:** S6 reports Todd Beaupré (YouTube, on Creator Insider) describing a homepage thumbnail-size test where long-form performed better with fewer, larger thumbnails, and stating YouTube would not have shipped the change if it hurt viewership.
- **Validation status:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** YouTube has publicly acknowledged testing larger/fewer homepage thumbnails and reported a positive long-form effect. The specific detail that "smaller/new-channel recommendations remained near the top" was not found in any source and should not be treated as confirmed.
- **Confidence/limitations:** Medium — reached via press reporting of an on-record Creator Insider statement, not a directly fetched primary video or blog post.

### ALG26-CLM-017 — Shorts thumbnails: absent from swipe feed, present in search/browse
- **Original claim locator:** T48, 13:05–13:52 (FILE-006451)
- **SOURCE SAYS:** Shorts thumbnails do not appear in the swipe feed but can matter in search, browse, and Shorts-shelf contexts.
- **PRIMARY EVIDENCE SAYS:** S8 (press/community reporting of an official YouTube Shorts-thumbnail feature launch, cross-checked against YouTube Help Shorts pages) indicates Shorts thumbnails are not shown in the swipe/Shorts-feed player but do appear in search results, hashtag pages, audio-pivot pages, and the channel page.
- **Validation status:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Shorts thumbnails plausibly matter for discovery surfaces outside the swipe feed (search, channel page) and are unlikely to influence the swipe feed itself. No official YouTube Help sentence stating this outright was located, so it rests on feature-launch reporting rather than documentation.
- **Confidence/limitations:** Medium — directionally consistent evidence from two independent angles (press reporting + YouTube Help's own Shorts surface descriptions), but no single authoritative statement found.

### ALG26-CLM-018 — Shorts and long-form use separate algorithms and "should not share a channel"
- **Original claim locator:** T01, 0:24–0:49 (FILE-006404)
- **SOURCE SAYS:** A creator claims Shorts and long-form use separate algorithms and audiences and should not share a channel.
- **PRIMARY EVIDENCE SAYS:** S7 (Todd Beaupré, on record): "Same audience? Same channel. Different audience? Different channel" — official guidance is explicitly conditional on audience overlap, not an absolute rule against combining formats. The 2026 Shorts→long-form recommendation bridge (S7) actively connects a channel's Shorts and long-form videos in recommendations, which works against, not for, a hard separation rule.
- **Validation status:** CONTRADICTED
- **OS CAN SAFELY CONCLUDE:** The universal instruction "should not share a channel" is contradicted by YouTube's own conditional, audience-overlap-based guidance, and is flagged as an overclaim. The narrower premise that Shorts and long-form may use different ranking mechanics is not itself contradicted — it just does not imply the channel-separation conclusion the claim draws from it.
- **Confidence/limitations:** Medium-high on the contradiction of the "should not share a channel" framing; the underlying "separate algorithms" technical premise is neither confirmed nor denied by the sources found.

### ALG26-INT-002 — Niche/topic authority reduces subscriber-total value
- **Original claim locator:** T36, 11:25–13:03 (FILE-006439)
- **SOURCE SAYS:** Semantic matching reduces the value of generic content and subscriber totals relative to specific content for a clearly understood viewer.
- **PRIMARY EVIDENCE SAYS:** S1/S2 describe interest affinity, per-video "fresh" performance data, and subscriptions as one input among many rather than a dominant channel-authority signal — consistent with the idea that being narrowly matched to viewer interest matters more than aggregate subscriber count for a given video's distribution. Neither page frames this as subscriber totals losing value over time or in general.
- **Validation status:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Subscriber count alone should not be treated as the primary driver of a given video's recommendation distribution; specific, well-matched content to a clear audience is a documented factor. The stronger claim that subscriber totals are being actively "devalued" by a semantic-era shift is an interpretation, not something the primary sources assert.
- **Confidence/limitations:** Medium. Core mechanism supported by two official pages; the "devaluation of subscriber totals" framing is source interpretation, flagged as a partial overclaim.

## Supported Claims

- ALG26-CLM-001 (personalized ranking mechanism)
- ALG26-CLM-004 (satisfaction / no single metric)
- ALG26-CLM-008 (subscription does not guarantee interest)
- ALG26-CLM-009 (templated repetition vs. reusable format — monetization-policy scope)

## Partially Supported Claims

- ALG26-CLM-002 (subscriber segmentation mechanism unconfirmed in detail)
- ALG26-CLM-005 (audience-overlap principle confirmed; granular within-channel signal detail unconfirmed)
- ALG26-CLM-012 (semantic ID mechanism confirmed; exact input-modality list unconfirmed)
- ALG26-CLM-016 (thumbnail test acknowledged; "near-top" placement detail unconfirmed)
- ALG26-CLM-017 (surface-visibility pattern plausible; no single authoritative statement found)
- ALG26-INT-002 (interest-matching principle confirmed; "devaluation" framing is interpretation)

## Contradicted Claims

- ALG26-CLM-018 — the universal "should not share a channel" instruction is contradicted by YouTube's own conditional, audience-based channel guidance and by the 2026 Shorts/long-form recommendation bridge.

## Unverified Claims

- None of the 12 selected claims fell to `NOT_CURRENTLY_VERIFIABLE`. One (ALG26-CLM-014) fell to `NOT_SUPPORTED_BY_PRIMARY_EVIDENCE` for its specific numeric figure, while the general trend it describes is separately supported — see that claim's entry for the distinction.

## Internal Conflicts

- **ALG26-CLM-005 vs. ALG26-CLM-018** (flagged inside DS-000018 itself): primary evidence favors CLM-005's conditional, audience-overlap framing over CLM-018's absolute "should not share a channel" framing. This validation does not delete or resolve CLM-018 in the source artifact — it records that the stronger, universal form of CLM-018 is contradicted by official guidance, while a narrower "different algorithm dynamics" premise remains unverified rather than false.
- No conflicts were found against other registered Global YouTube Knowledge: DS-000011 is the only other semantic-class-`A` dataset and has no structured claim artifact yet (status `INGESTED`), so there is nothing else to check DS-000018's claims against.
- No conflicts were found between the 12 validated claims and the primary evidence gathered, beyond the CLM-005/CLM-018 pair above.

## Safe OS Conclusions

These are the narrowest defensible conclusions the YouTube Intelligence OS may use from this validation pass. Each is conditional and traceable to the claim entry above — none should be treated as a fixed rule or numeric target.

1. Recommendation ranking is computed per-viewer and per-surface from many signals, not one global metric (CLM-001, CLM-004).
2. Subscriber count does not guarantee a video will be shown to or watched by subscribers; per-video engagement among people it is shown to still matters (CLM-002, CLM-008, INT-002).
3. Whether to combine Shorts and long-form on one channel should be judged by audience overlap, not by format alone — and the claim that they must never share a channel is not supported by official guidance (CLM-005, CLM-018).
4. Near-identical, templated episode repetition carries real monetization-policy risk; formats that vary meaningfully between episodes do not meet YouTube's definition of inauthentic/mass-produced content (CLM-009). This is confirmed as a monetization-eligibility rule, not confirmed as a discovery-ranking rule.
5. YouTube has a published research basis for content-derived (semantic) IDs, not just opaque video IDs, in production ranking — useful as background for why well-described, distinctive content may generalize better to new/interested viewers, but the exact input signals are not confirmed in detail (CLM-012).
6. YouTube's growth on TV screens is a real, independently confirmed trend; specific self-reported percentage figures from any one source (creator, agency, or this DS-000018 corpus) should not be repeated as established platform statistics without their own primary support (CLM-014).
7. Homepage and Shorts thumbnail effects are plausible and partially acknowledged by YouTube, but specific placement/ranking side-effects beyond the acknowledged core effect remain unconfirmed (CLM-016, CLM-017).

## Claims Still Requiring Evidence

The following 21 DS-000018 claims were not in scope for this task and remain unvalidated. They are listed for future prioritization, not evaluated here:

- **Not selected `SOURCE_CLAIM` rows:** ALG26-CLM-003, 006, 007, 010, 011, 013, 015
- **Not selected `SOURCE_INTERPRETATION` rows:** ALG26-INT-001, 003, 004, 005
- **All `SOURCE_RECOMMENDATION` rows (excluded as creator/business advice, not algorithmic claims):** ALG26-REC-001 through ALG26-REC-010, including REC-008 (off-platform/external-signal trust claim) and REC-007 (AEO/citation claim), which are the only DS-000018 rows on the "off-platform or external signals" theme named in this task's priority list.

## Implications for Future Intelligence Layers

- No recommendation engine, channel decision, or content classification is created by this artifact. This section states only what a future layer may safely draw on, conditionally.
- **Format strategy:** A future layer may treat "same audience, same channel; different audience, different channel" (CLM-005/CLM-018, Safe Conclusion 3) as a reasonable heuristic for Shorts/long-form channel architecture decisions, sourced to an on-record YouTube executive statement — not as a proven algorithmic rule.
- **Topic selection / content-gap work:** Safe Conclusion 2 and 5 (specific, well-matched content to a clear audience, aided by content-derived semantic matching) support treating "how clearly a topic is scoped to an audience" as a more defensible heuristic input than raw subscriber count — but neither should be scored as a fixed weight.
- **Titles/thumbnails/hooks:** Safe Conclusion 7 supports testing homepage/Shorts thumbnail treatments as a plausible lever, but any future engine should treat effect size as unmeasured, not import the source's self-reported figures.
- **Format/episode design:** Safe Conclusion 4 is directly usable as a monetization-risk guardrail (avoid templated near-duplication) but should not be encoded as a discovery-ranking penalty without further evidence.
- **Still speculative for any future layer:** TV-specific device-mix percentages (CLM-014), exact semantic-ID input modalities (CLM-012), and any subscriber "devaluation" framing (INT-002) — these should remain flagged as unverified in any downstream recommendation or scoring logic.
