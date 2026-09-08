# YouTube Algorithm Primary-Source Validation — 2026 Algorithm Update (DS-000018)

> **Current authority: Step 15C-R, 2026-09-08.** The Final DS-000018 Validation Synthesis below is the only current disposition register (33/33). Batch 1 and Batch 2 remain historical records, including superseded conclusions. S6, S7 and S8 are secondary reporting, not primary authority. Their former classification is explicitly withdrawn by the remediation pass. Earlier safe conclusions and counts must not override the final register.

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

---

# Validation Batch 2

## Scope

- Source dataset validated: DS-000018 — 2026 Algorithm Update — Multi-Tab Creator Research Corpus (unchanged; same 33-claim source artifact)
- Claims validated in this batch: **exactly 12**, selected from the 21 claims left unvalidated by Batch 1
- Claims not revalidated: the 12 Batch 1 claims (ALG26-CLM-001, 002, 004, 005, 008, 009, 012, 014, 016, 017, 018, ALG26-INT-002) are unchanged and not re-scored here
- Claims still unvalidated after this batch: 9 (listed under "Claims Still Requiring Evidence — Batch 2")
- This batch is an additional evidence layer. It does not modify, delete, or promote any of the 33 original claims, and it creates zero `MEASURED_FACT` rows.
- Batch date: 2026-09-04

## Method

1. Confirmed the 21 remaining unvalidated claim IDs directly from the DS-000018 source-intelligence artifact and Batch 1's "Claims Still Requiring Evidence" list before selecting: `ALG26-CLM-003, 006, 007, 010, 011, 013, 015`; `ALG26-INT-001, 003, 004, 005`; `ALG26-REC-001` through `ALG26-REC-010`. Count confirmed as 21 (7 + 4 + 10).
2. Selected 12 claims prioritizing the task's named themes, with `ALG26-REC-007` (AEO/citation-friendliness) and `ALG26-REC-008` (off-platform trust for faceless channels) selected first per explicit instruction, since Batch 1 recorded the "off-platform/external signals" theme as uncovered.
3. Re-verified provenance for every selected claim by resolving its cited tab alias (T36/T39/T43/T48/T49/T51) to `source_files.file_id`/`sha256` in `data/catalog/youtube_inventory.db` and confirming an exact match against the intelligence artifact's alias table (see table below). One new alias (T43) is used in this batch and is now cross-checked for the first time.
4. Researched current official evidence for each claim from YouTube Help, the YouTube Official Blog, Google Search Central developer documentation (for the two AEO-adjacent claims), and the same Google Research/DeepMind Semantic-IDs paper used in Batch 1, per the task's primary-source priority list. No SEO blog, agency, newsletter, or press-summary source was used to determine any validation status; several SEO/agency search results for Shorts-vs-long-form "separate algorithms" and TV/living-room viewing statistics were deliberately excluded as non-primary and are not cited below.
5. Assigned exactly one of the five required validation states per claim.
6. Checked all 12 claims against: the Batch 1 twelve, the DS-000018 source artifact's own claims, Batch 1's recorded Safe OS Conclusions, DS-000011 (still `INGESTED`, no structured claim artifact — nothing to conflict against there, unchanged from Batch 1), and the primary evidence gathered in this batch.

### Provenance re-verification (Batch 2)

| Alias | FILE ID | DB `sha256` matches intelligence-artifact table | Selected claims using this member |
|---|---|---|---|
| T36 | FILE-006439 | ✅ match (re-confirmed) | ALG26-INT-001 |
| T39 | FILE-006442 | ✅ match (re-confirmed) | ALG26-CLM-006, ALG26-CLM-007 |
| T43 | FILE-006446 | ✅ match (first use) | ALG26-REC-007, ALG26-REC-008 |
| T48 | FILE-006451 | ✅ match (re-confirmed) | ALG26-CLM-011 |
| T49 | FILE-006452 | ✅ match (re-confirmed) | ALG26-CLM-015, ALG26-INT-003, ALG26-INT-004, ALG26-INT-005 |
| T51 | FILE-006454 | ✅ match (re-confirmed) | ALG26-CLM-013 |

Note: `ALG26-CLM-003` also resolves to T39 (1:19–2:57 block region, 5:48–6:58 specifically), already covered by the T39 row above via the same file/hash.

## Primary Sources Used (Batch 2 — new sources; S1–S8 from Batch 1 are reused where noted)

| ID | Organization | Title | URL | Retrieved | Section used |
|---|---|---|---|---|---|
| S9 | Google / YouTube Help | Good to know about recommendations for YouTube's recommendation system | https://support.google.com/youtube/answer/16559651 | 2026-09-04 | "Our search and recommendation systems look at audience activity while a video is publicly available"; Shorts-feed recency note |
| S10 | Google / YouTube Help | Hyping videos eligibility, availability & policies; Leaderboard for hyped videos on YouTube | https://support.google.com/youtube/answer/15509925 ; https://support.google.com/youtube/answer/15334500 | 2026-09-04 | Eligibility (500–500,000 subscriber creators), small-creator bonus points, non-personalized discovery leaderboard |
| S11 | Google / Google Search Central | AI Features and Your Website | https://developers.google.com/search/docs/appearance/ai-features | 2026-09-04 | "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary"; scope is Google Search web results, not YouTube |
| S12 | Google / Google Search Central | Google's Guide to Optimizing for Generative AI Features on Google Search | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | 2026-09-04 | No prescriptive "early direct answer" or specific-fact-density structural requirement; explicitly no requirement to fragment content for AI parsing |
| S13 | Google / YouTube Help | Impersonation policy | https://support.google.com/youtube/answer/2801947 | 2026-09-04 | Channel must represent the real creator/brand/entity it claims to be |
| S14 | Google / YouTube Help | Spam, deceptive practices & scams policies | https://support.google.com/youtube/answer/2801973 | 2026-09-04 | "Off-platform diversion" listed as a violation category; no off-platform-presence ranking benefit documented |
| S1, S2 (reused) | Google / YouTube Help | YouTube's Recommendation System; How YouTube recommendations work | https://support.google.com/youtube/answer/16533387 ; https://support.google.com/youtube/answer/16089387 | 2026-09-04 | Watch history as a signal; "give as many videos as possible a chance to be discovered"; per-surface signal weighting; "fresh performance data...rather than relying on past results" |
| S4 (reused) | YouTube Official Blog | YouTube CEO Neal Mohan's 2026 Letter: The Future of YouTube | https://blog.youtube/inside-youtube/the-future-of-youtube-2026/ | 2026-09-04 | AI-slop reduction, mandatory synthetic-content disclosure, "AI will remain a tool for expression, not a replacement" |
| S5 (reused) | Google Research / Google DeepMind | Better Generalization with Semantic IDs: A Case Study in Ranking for Recommendations | arXiv:2306.08121 | 2026-09-04 | Semantic IDs from frozen content embeddings via RQ-VAE, evaluated on a real-world YouTube ranking model; no mention of a "mood" cluster construct |

S10 is an official YouTube Help feature description, not press-reported, and is treated as full-confidence primary evidence (stronger than S6–S8 from Batch 1). S11 and S12 are official Google Search Central documentation but are explicitly scoped to Google Search web results, not YouTube — see the cross-system inference warnings below.

## Claim-by-Claim Validation

### ALG26-CLM-003 — Evergreen discovery
- **Original claim locator:** T39, 5:48–6:58 (FILE-006442)
- **SOURCE SAYS:** Initial performance is not the sole basis for later recommendations; evergreen videos may receive most of their views well after publication.
- **PRIMARY EVIDENCE SAYS:** S9: "Our search and recommendation systems look at audience activity while a video is publicly available" — evaluation is ongoing, not fixed at launch. S1: "The algorithm uses fresh performance data for each individual video, rather than relying on past results" — recent signals, not a permanent early verdict, drive continued recommendation. Neither page states that evergreen videos typically receive most of their lifetime views after an initial window, or gives any frequency/magnitude for this pattern.
- **Heuristic vs. platform fact:** A (documented platform behavior) for the mechanism; E (source interpretation) for the "most views well after publication" outcome framing.
- **Validation status:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** A video's recommendation eligibility is not permanently fixed by its first-days performance; ongoing audience activity while the video remains public continues to matter. The stronger claim that evergreen videos typically get most of their views long after publication is a plausible source interpretation, not something either official page states.
- **Confidence/limitations:** Medium-high on the mechanism (two independent official pages point the same direction); no confidence on the "most views" outcome framing, which no source measures.
- **Conflict check:** NO_CONFLICT with Batch 1 (complements CLM-001/CLM-004's "fresh, per-viewer, not fixed" framing) and with other DS-000018 claims.

### ALG26-CLM-006 — Suggested traffic / cross-topic connection
- **Original claim locator:** T39, 28:38–31:15 (FILE-006442)
- **SOURCE SAYS:** A suggested video need not share the current video's topic; personalization can connect cross-topic videos through a viewer's broader interests and co-viewing behavior.
- **PRIMARY EVIDENCE SAYS:** S1/S2 confirm the system "learns from what videos similar viewers also watched, like 'viewers of video A also watched video B,'" and separately describes recognizing a viewer's "favored themes, topics, and formats" across their activity. Neither page states whether a specific "Up Next"/suggested placement can cross topic boundaries, or only reorders within a topic.
- **Heuristic vs. platform fact:** A (documented platform behavior — co-viewing signal exists) blended with E (source interpretation of what that implies for cross-topic suggestion specifically).
- **Validation status:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Co-viewing behavior ("viewers of A also watched B") is a documented, official recommendation input, which is consistent with suggestions sometimes crossing topic lines when a broader interest pattern connects two videos. The stronger claim that this is a general, reliable cross-topic bridge mechanism is not itself confirmed.
- **Confidence/limitations:** Medium. The underlying co-viewing signal is well documented; its cross-topic scope specifically is not addressed.
- **Conflict check:** NO_CONFLICT with CLM-005/CLM-018 (channel/format boundaries operate at a different level — channel identity vs. per-video suggestion — so no contradiction).

### ALG26-CLM-007 — New-channel discovery without prior history
- **Original claim locator:** T39, 31:47–32:39 (FILE-006442)
- **SOURCE SAYS:** New channels and fresh videos can be matched to interested viewers without prior channel-viewer history, using topical preferences and an understanding of the video's subject.
- **PRIMARY EVIDENCE SAYS:** S1 states directly: "YouTube aims to give as many videos as possible a chance to be discovered by audiences who are interested in them." S10 (Hype feature, official) provides a concrete, documented mechanism aimed specifically at creators without an established audience: eligible for channels with 500–500,000 subscribers, with a "small creator bonus" that weights a hype from a smaller channel's viewer more heavily, surfaced via a non-personalized, topic-filterable public leaderboard. Neither source describes the exact content-understanding mechanism (e.g., topical/semantic matching) used for a genuinely brand-new, zero-subscriber channel's very first upload.
- **Heuristic vs. platform fact:** A (documented platform behavior and a named product feature) for the general "new content gets a discovery chance" principle; E (source interpretation) for the specific "topical preferences and subject understanding" mechanism.
- **Validation status:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** YouTube states an explicit goal of giving new/undiscovered content a chance to reach interested audiences, and has at least one official, documented feature (Hype) built to help smaller/newer creators gain visibility independent of subscriber count. The precise content-understanding mechanism for a zero-history channel's first video is not confirmed in detail by the sources found.
- **Confidence/limitations:** Medium-high on the general principle and the existence of a supporting feature; low on the specific mechanism claimed.
- **Conflict check:** NO_CONFLICT with CLM-002/INT-002 (Batch 1) — consistent with those claims' theme that subscriber totals are not the dominant distribution driver.

### ALG26-CLM-011 — Watch history as an important recommendation input
- **Original claim locator:** T48, 15:08–15:56 (FILE-006451)
- **SOURCE SAYS:** Watch history is an important recommendation input because it indicates viewer interests.
- **PRIMARY EVIDENCE SAYS:** S2, directly: "Watch history: The YouTube videos you've watched help to give you better recommendations." S1 confirms watch history as part of real-time per-viewer profiling. S2 further states that for homepage recommendations specifically, "our system primarily relies on your watch history."
- **Heuristic vs. platform fact:** A (documented platform behavior) — this is a directly and consistently stated official mechanism.
- **Validation status:** SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Watch history is an official, explicitly named, high-weight recommendation signal, particularly for homepage recommendations.
- **Confidence/limitations:** High confidence — stated plainly and consistently across two official Help pages.
- **Conflict check:** NO_CONFLICT — directly reinforces Batch 1's CLM-001 (per-viewer, signal-driven ranking).

### ALG26-CLM-013 — Semantic IDs connected to watch-history "mood" clusters
- **Original claim locator:** T51, 7:31–8:12 (FILE-006454)
- **SOURCE SAYS:** Semantic IDs are connected to watch-history clusters representing a viewer's recent formats, styles, interests, and mood.
- **PRIMARY EVIDENCE SAYS:** S5 (the same Google Research/DeepMind paper used for CLM-012 in Batch 1) confirms Semantic IDs are discrete codes derived from frozen content embeddings, used in a real-world YouTube ranking model to improve generalization for new/long-tail videos. The paper's publicly available description does not mention "mood," or any watch-history clustering construct by that name; it addresses item (video) representation, not a described viewer-mood-state feature.
- **Heuristic vs. platform fact:** F (speculative internal-algorithm claim) — this compounds an already-partially-unconfirmed mechanism (CLM-012) with an additional, more specific claim that has no located primary support.
- **Validation status:** NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
- **OS CAN SAFELY CONCLUDE:** The published research basis for content-derived semantic IDs (already recorded under CLM-012) exists, but no primary source found describes a "mood cluster" construct tied to watch history. This should not be treated as confirmed; "not found" here reflects a genuine research-basis published on a different, narrower aspect (item embeddings), not a denial that any mood-related signal could exist.
- **Confidence/limitations:** Low. The claim is a translated creator transcript's technical extrapolation beyond what the cited-style research publicly documents.
- **Conflict check:** PARTIAL_TENSION with CLM-012 (Batch 1, PARTIALLY_SUPPORTED) — CLM-013 extends CLM-012's already-flagged "exact input-modality list unconfirmed" caution with an even more specific, unsupported claim. This is not a contradiction (both can be false-until-shown or true-but-unconfirmed) but the compounding specificity increases overclaim risk and both should be flagged together in any downstream use.

### ALG26-CLM-015 — Long-form duration +51% since 2020 (100B-view analysis)
- **Original claim locator:** T49, 2:44–3:03 (FILE-006452)
- **SOURCE SAYS:** A strategist reports an analysis of 100 billion views in which mean/median long-form video duration increased 51% since 2020.
- **PRIMARY EVIDENCE SAYS:** No official YouTube or Google source describing a 100-billion-view duration analysis, or confirming/denying a 51% duration increase, was located. S9 confirms YouTube's own framing is normative, not statistical: "There's no universal 'ideal' length for YouTube videos" — creators are told to match length to content, not given a platform-published duration trend figure.
- **Heuristic vs. platform fact:** E (source interpretation) / self-reported quantitative claim with no accompanying raw data, structurally identical in kind to CLM-014 (Batch 1).
- **Validation status:** NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
- **OS CAN SAFELY CONCLUDE:** No official confirmation or denial of this specific statistic exists in the sources checked; "not found" means unverified, not false. YouTube's own guidance is that video length should be need-driven rather than trend-driven, which neither confirms nor is contradicted by a possible real-world lengthening trend.
- **Confidence/limitations:** None on the specific figure. The claim should not be repeated as an established platform statistic.
- **Conflict check:** NO_CONFLICT with CLM-014 (Batch 1) — both are self-reported T49-strategist statistics with the same evidentiary limitation (no raw data, no primary corroboration); this is a repeated pattern within the source, not a contradiction between the two claims.

### ALG26-INT-001 — Semantic discovery "eras" framing
- **Original claim locator:** T36, 4:10–11:08 (FILE-006439)
- **SOURCE SAYS:** The speaker frames YouTube's history as keyword, attention, interest, then "semantic" eras, with semantic meaning layered on top of metadata, clicks, watch time, and viewer interest.
- **PRIMARY EVIDENCE SAYS:** No official YouTube or Google publication describing YouTube's recommendation history as a sequence of named "eras" (keyword/attention/interest/semantic) was located. S5 independently confirms a real, published semantic-ID research basis exists (consistent with a "semantic" capability being real), but no official source frames this as a historical stage succeeding earlier "eras."
- **Heuristic vs. platform fact:** E (source interpretation) — an explanatory narrative built by the speaker, not a platform-published history.
- **Validation status:** NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
- **OS CAN SAFELY CONCLUDE:** Semantic/content-derived matching is a real, published capability (per CLM-012's evidence), but the specific four-era historical narrative is the source's own framing device, not something YouTube or Google has published. Treat the underlying capability as supported (already recorded under CLM-012) and the "eras" narrative itself as unverified scaffolding.
- **Confidence/limitations:** None on the narrative structure; medium on the underlying capability it describes (via CLM-012, not independently re-verified here).
- **Conflict check:** NO_CONFLICT — compatible in spirit with CLM-012/INT-002 (Batch 1), which already carry the appropriate caveats for the technical mechanism.

### ALG26-INT-003 — TV friction favors show-like, bingeable content
- **Original claim locator:** T49, 7:03–10:06 (FILE-006452)
- **SOURCE SAYS:** Strategists infer that TV-screen friction and lean-back viewing can favor recognizable, show-like, bingeable experiences and sometimes longer videos.
- **PRIMARY EVIDENCE SAYS:** S4 confirms YouTube's large and growing TV-screen viewing share (Nielsen "#1 in streaming watchtime... for nearly three years") but does not describe a content-format effect of TV viewing (i.e., it does not state that TV viewing causes or correlates with a preference for show-like or longer content). No official source addressing a TV-format causal link was located.
- **Heuristic vs. platform fact:** E (source interpretation) — an inference the source's own participants qualify by noting their personal TV habits differ.
- **Validation status:** NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
- **OS CAN SAFELY CONCLUDE:** YouTube's growth on TV screens is independently, officially confirmed (already recorded under CLM-014, Batch 1). The specific inference that TV-screen friction pushes viewers toward show-like or longer formats is a creator-strategist interpretation with no located official support and should not be treated as a platform-documented effect.
- **Confidence/limitations:** None on the causal format inference; the adjacent TV-growth fact is independently well evidenced (S4) but is a different claim.
- **Conflict check:** NO_CONFLICT with CLM-014 (Batch 1) — same underlying TV-growth fact, different and separately unverified layer added on top.

### ALG26-INT-004 — Authenticity/personality as a differentiator against imitable spectacle
- **Original claim locator:** T49, 31:13–33:46 (FILE-006452)
- **SOURCE SAYS:** As high-production spectacle becomes easier to imitate (implicitly, via AI tools), personality and personal connection become a stronger differentiator.
- **PRIMARY EVIDENCE SAYS:** S4 (Neal Mohan's 2026 letter) confirms two adjacent, official platform-policy facts: YouTube requires creators to disclose "realistic altered or synthetic content," and YouTube states it is "actively building on its established systems for combatting spam and clickbait" specifically to reduce "low-quality AI content" and protect "genuine content from human creators." Neither statement asserts that personality/personal connection is becoming a stronger *audience* or *ranking* differentiator — that causal, market-level claim is not something YouTube's own communications make.
- **Heuristic vs. platform fact:** B (documented policy) for the disclosure requirement and anti-slop enforcement direction; E (source interpretation) for the "personality becomes the differentiator" market claim built on top of it.
- **Validation status:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** YouTube has officially confirmed policy actions consistent with valuing authentic, human-originated content over undisclosed synthetic content (mandatory synthetic-content disclosure, active anti-"AI slop" enforcement). The stronger claim that this environment makes personality/personal connection a *strategically stronger differentiator* is a plausible but unconfirmed market inference, not a platform-stated ranking or discovery mechanism.
- **Confidence/limitations:** Medium on the policy-direction premise; none on the differentiation conclusion itself.
- **Conflict check:** NO_CONFLICT with CLM-009 (Batch 1, SUPPORTED) — both point toward the same policy direction (against inauthentic/mass-produced/undisclosed-synthetic content).

### ALG26-INT-005 — Long-form recommender more sophisticated than Shorts recommender
- **Original claim locator:** T49, 1:00:25–1:02:14 (FILE-006452)
- **SOURCE SAYS:** A strategist speculates that the mature long-form recommender is more sophisticated than the newer Shorts recommender and may handle content volume better.
- **PRIMARY EVIDENCE SAYS:** No official YouTube or Google source comparing the relative sophistication, maturity, or architecture of a "long-form recommender" versus a "Shorts recommender" as distinct systems was located. This concerns internal system architecture and engineering comparisons that YouTube does not publish.
- **Heuristic vs. platform fact:** F (speculative internal-algorithm claim) — the source itself repeatedly frames this as personal judgment, not platform-attributed information.
- **Validation status:** NOT_CURRENTLY_VERIFIABLE
- **OS CAN SAFELY CONCLUDE:** Nothing about the relative sophistication of a long-form versus Shorts recommendation system can be drawn from public primary documentation. This should remain an open, unverifiable question for any downstream layer.
- **Confidence/limitations:** Not applicable — no evidence exists to weigh in either direction, and the claim concerns non-public system internals.
- **Conflict check:** PARTIAL_TENSION with CLM-018 (Batch 1, CONTRADICTED for its "should not share a channel" framing) — INT-005 presupposes Shorts and long-form are handled by meaningfully separate systems, which is the same unresolved sub-premise Batch 1 explicitly left open ("the underlying 'separate algorithms' technical premise is neither confirmed nor denied"). This claim does not resolve that open premise; it merely reuses it as an assumption.

### ALG26-REC-007 — AEO script structuring for AI-answer citation-friendliness
- **Original claim locator:** T43, 5:08–6:49 (FILE-006446)
- **SOURCE SAYS:** Structure scripts with an early, direct answer and specific names, dates, and places to make passages more citation-friendly for AI answer systems.
- **PRIMARY EVIDENCE SAYS:** Google Search Central's own official guidance directly addresses this exact mechanism and states the opposite: S11: "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary." S12 adds there is "no requirement to break your content into tiny pieces for AI to better understand it," and gives no early-answer or fact-density structural prescription — it instead emphasizes general content quality and organizing "by paragraphs and sections, along with headings."
- **Heuristic vs. platform fact:** D (creator best-practice recommendation) that makes an implicit, unverified platform-mechanism claim — effectively F dressed as advice.
- **Validation status:** CONTRADICTED
- **OS CAN SAFELY CONCLUDE:** The specific mechanism this recommendation asserts — that an early-direct-answer, fact-dense structure specifically improves AI-answer citation odds — is directly contradicted by Google's own official AI-features guidance, which states no such special structuring is required or necessarily rewarded. General content-quality and topical-authority guidance (which this Search Central material does endorse) is a different, much weaker claim than the specific "structure-for-citation" formula in the source.
- **Confidence/limitations:** High confidence on the contradiction, sourced to two official, directly fetched Google Search Central pages.
- **CROSS-SYSTEM INFERENCE WARNING:** S11 and S12 describe **Google Search** web-result AI Overviews/AI Mode, not **YouTube Search** or **YouTube recommendations**. No official source was located describing whether or how AI-answer citation mechanics apply to YouTube video/transcript content specifically, or to any YouTube-native answer surface. This validation should not be read as evidence about YouTube's own systems — only as evidence that the *general* AEO mechanism claimed does not hold even in Google Search itself, the system it is most likely to have been imported from.
- **Conflict check:** DIRECT_CONFLICT against primary evidence (S11/S12). NO_CONFLICT against the other 11 validated Batch 2 claims or Batch 1 claims — no prior claim addressed AEO.

### ALG26-REC-008 — Off-platform brand presence builds trust for faceless channels
- **Original claim locator:** T43, 7:05–12:38 (FILE-006446)
- **SOURCE SAYS:** Build linked off-platform profiles and publishing surfaces so a faceless channel appears as a consistent brand rather than an anonymous content farm, implying this affects platform trust/distribution.
- **PRIMARY EVIDENCE SAYS:** S13 (Impersonation policy) confirms channel identity must represent "the real creator, brand, or entity it claims to be," but this concerns not impersonating others, not building an off-platform footprint. S14 (Spam, deceptive practices & scams policy) lists "off-platform diversion" (content built to push users to external, often malicious, sites) as a *violation* category — the opposite direction from the claim's advice, though the policy targets deceptive diversion, not general brand-consistency linking. No official source states that a consistent off-platform brand presence functions as, or contributes to, a recommendation, ranking, or discovery-trust signal.
- **Heuristic vs. platform fact:** D (creator best-practice recommendation) implying an unverified F-type mechanism (an off-platform "trust signal" feeding recommendations).
- **Validation status:** NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
- **OS CAN SAFELY CONCLUDE:** No official YouTube or Google source confirms or denies that off-platform brand consistency influences recommendation, ranking, or discovery. Identity-representation policy (S13) and anti-diversion policy (S14) are adjacent but address different concerns (impersonation and malicious link-out behavior, respectively), not brand-trust scoring. This should be treated as an unverified creator-strategy hypothesis, not a platform mechanism.
- **Confidence/limitations:** None on the specific "off-platform trust signal" mechanism; the adjacent policies found are real but do not establish or refute it.
- **CROSS-SYSTEM INFERENCE WARNING:** The claim's framing resembles Google Search's E-E-A-T (Experience, Expertise, Authoritativeness, Trust) content-quality heuristics, which are a Google Search ranking concept — no official source was found extending that framework, or an equivalent, to YouTube recommendations specifically. This validation does not confirm or import any Search-side authority concept onto YouTube.
- **Conflict check:** NO_CONFLICT with any Batch 1 or Batch 2 claim (no prior claim addressed off-platform presence).

## Supported Claims (Batch 2)

- ALG26-CLM-011 (watch history is a directly documented, high-weight recommendation signal)

## Partially Supported Claims (Batch 2)

- ALG26-CLM-003 (ongoing evaluation while publicly available confirmed; "most views after publication" outcome framing unconfirmed)
- ALG26-CLM-006 (co-viewing signal confirmed; cross-topic scope specifically unconfirmed)
- ALG26-CLM-007 (general new-content discovery goal and the Hype feature confirmed; exact new-channel matching mechanism unconfirmed)
- ALG26-INT-004 (synthetic-content disclosure/anti-slop policy confirmed; "personality as stronger differentiator" market claim unconfirmed)

## Contradicted Claims (Batch 2)

- ALG26-REC-007 — the specific "early answer + specific facts = more AI-citable" structuring mechanism is directly contradicted by Google Search Central's own AI Overviews/AI Mode guidance ("no additional requirements... no special optimizations necessary"), and the guidance is scoped to Google Search, not YouTube.

## Not Supported by Primary Evidence (Batch 2)

- ALG26-CLM-013 (semantic-ID "mood cluster" construct not described in the cited research)
- ALG26-CLM-015 (100B-view, +51% duration statistic — no primary corroboration or denial found)
- ALG26-INT-001 ("keyword/attention/interest/semantic eras" historical narrative — not a published YouTube/Google framing)
- ALG26-INT-003 (TV-friction-favors-show-like-content causal inference — no official source addresses this format effect)
- ALG26-REC-008 (off-platform brand presence as a trust/discovery signal — no official source found)

## Not Currently Verifiable (Batch 2)

- ALG26-INT-005 (relative sophistication of the long-form vs. Shorts recommender — internal system architecture, not publicly documented; source itself frames this as personal judgment)

## AEO / Off-Platform Findings

- **Google Search AI Overviews/AI Mode do not require or specifically reward the "early direct answer + specific facts" script structure** claimed in ALG26-REC-007; Google's own guidance explicitly disclaims special structural requirements (S11, S12).
- **No official source, for either Google Search or YouTube, was found establishing that off-platform brand-presence consistency functions as a discovery or ranking trust signal** (ALG26-REC-008). The closest official YouTube material addresses identity-impersonation policy and anti-diversion spam policy — both adjacent but distinct concerns.
- Both AEO-adjacent findings are **Google Search-side, not YouTube-side** evidence (or, for REC-008, no primary evidence on either system). Per the task's cross-system rule, neither claim should be treated as validated or contradicted *for YouTube specifically* — REC-007 is contradicted for the system it most plausibly describes (Google Search), and REC-008 remains unconfirmed for both systems.

## Cross-System Inference Warnings

1. **ALG26-REC-007:** Evidence used (S11, S12) is Google Search Central documentation for Google Search's AI Overviews/AI Mode. It is not YouTube Search or YouTube-recommendation documentation. The CONTRADICTED status applies to the AEO mechanism as it would apply to Google Search itself; no claim is made about YouTube-native AI answer surfaces, which have no located primary documentation.
2. **ALG26-REC-008:** No primary evidence was found on either system, so no cross-system substitution actually occurred here — but the claim's framing echoes Google Search's E-E-A-T concept, and any future reasoning must not import E-E-A-T (a Search ranking framework) onto YouTube recommendations without its own primary support.
3. **ALG26-INT-003:** S4's confirmed TV-viewing-share growth (a real, official Google Search/Nielsen-sourced statistic about aggregate platform viewing) must not be read as confirming a *content-format* effect (show-like/bingeable content performing better on TV). The growth statistic and the format-preference inference are two different claims; only the former is supported.

## Important Overclaims

- **ALG26-CLM-013** compounds Batch 1's already-flagged CLM-012 overclaim risk (unconfirmed exact modality list) with an additional, more specific and less-supported claim ("mood" clustering). Any downstream layer citing CLM-012 must not silently absorb CLM-013's additional specificity as if it were part of the same confirmed mechanism.
- **ALG26-REC-007** is a creator recommendation that smuggles in an unverified, and in this case contradicted, platform-mechanism claim. Creator best-practice advice should not be treated as evidence of how AI-answer systems actually rank or select citations, on YouTube or elsewhere.
- **ALG26-INT-003** and **ALG26-INT-004** both take a real, independently confirmed platform trend (TV growth; anti-AI-slop policy) and extend it with an unconfirmed causal/behavioral inference (format preference; audience differentiation). The confirmed trend and the unconfirmed inference must be tracked separately.

## Direct Conflicts (Batch 2)

- ALG26-REC-007 vs. primary evidence (S11, S12) — the specific citation-structuring mechanism claimed is directly contradicted by Google's own AI-features guidance.

## Partial Tensions (Batch 2)

- ALG26-CLM-013 vs. ALG26-CLM-012 (Batch 1) — compounding, unconfirmed specificity added on top of an already-partial claim (see "Important Overclaims").
- ALG26-INT-005 vs. ALG26-CLM-018 (Batch 1) — both rest on the same unresolved "are Shorts and long-form handled by meaningfully separate systems" premise, which remains neither confirmed nor denied.

## New Safe OS Conclusions (Batch 2)

These extend, and do not replace, Batch 1's Safe OS Conclusions. Each is conditional and traceable to the claim entry above.

8. Recommendation evaluation continues for as long as a video is publicly available, using fresh rather than purely historical performance data — a video's discovery potential is not permanently fixed by its earliest performance (CLM-003).
9. Co-viewing behavior ("viewers of A also watched B") is an official recommendation input capable of connecting videos across a viewer's broader interests, but its specific cross-topic reach is not separately confirmed (CLM-006).
10. YouTube has stated goals and at least one official feature (Hype) supporting discovery for smaller/newer channels independent of subscriber count, though the exact content-matching mechanism for a brand-new channel's first video is unconfirmed (CLM-007).
11. Watch history is an official, high-weight, explicitly documented recommendation signal — especially for homepage recommendations — and can be treated as a defensible input with high confidence (CLM-011).
12. YouTube's official policy direction (mandatory synthetic-content disclosure, active anti-"AI slop" enforcement) supports treating authenticity and originality as an environment the platform is actively reinforcing — but the specific claim that personal connection is becoming a stronger competitive differentiator is a market inference, not a platform-stated mechanism, and should stay labeled as such (INT-004).
13. No AEO "structure for AI citation" formula should be treated as a validated YouTube discovery lever; Google's own AI Overviews guidance contradicts the specific mechanism claimed, and no YouTube-specific AI-answer documentation exists to substitute for it (REC-007).
14. No off-platform brand-consistency practice should be treated as a validated discovery or trust signal for YouTube recommendations; it remains an unverified hypothesis with no supporting or contradicting primary evidence found (REC-008).
15. Claims resting on undisclosed internal system architecture comparisons (e.g., relative sophistication of separate recommender systems) should be treated as permanently unverifiable from public documentation, not as pending validation (INT-005).

## Claims Still Requiring Evidence — Batch 2

The following 9 DS-000018 claims remain unvalidated after Batch 1 and Batch 2 combined:

- **Not selected `SOURCE_CLAIM` row:** ALG26-CLM-010
- **Not selected `SOURCE_RECOMMENDATION` rows:** ALG26-REC-001, ALG26-REC-002, ALG26-REC-003, ALG26-REC-004, ALG26-REC-005, ALG26-REC-006, ALG26-REC-009, ALG26-REC-010

## Implications for Future Intelligence Layers (Batch 2 additions)

- **Discovery / new-channel strategy:** Safe Conclusion 10 (Hype feature, general discovery-chance goal) is usable as a background fact when reasoning about small/new-channel visibility mechanics, but should not be treated as a description of organic-recommendation matching for a channel's very first video.
- **Retention / signal weighting:** Safe Conclusion 11 (watch history as a high-weight, homepage-primary signal) is directly usable with high confidence wherever a future layer reasons about which historical viewer data most plausibly drives a given surface's recommendations.
- **Content/format strategy:** Safe Conclusion 8 (ongoing, fresh-data-driven evaluation) supports not writing off older catalog videos as permanently capped by early performance — but any "evergreen resurfacing" feature should be tested, not assumed.
- **AEO / hooks / scripts:** Safe Conclusions 13 and 14 are guardrails, not opportunities — any future title/hook/script engine should not implement an "AI-citation formula" or an "off-platform trust builder" heuristic on the basis of DS-000018 alone; both remain unconfirmed or contradicted.
- **Authenticity / creator differentiation:** Safe Conclusion 12 supports flagging authenticity/originality as a platform-reinforced environment when scoring content ideas, while keeping the audience-differentiation causal claim separately labeled as unconfirmed market interpretation.
- **Still speculative for any future layer:** semantic-ID "mood" clustering (CLM-013), the four-era semantic-history narrative (INT-001), TV-friction-favors-show-format causal inference (INT-003), and any long-form-vs-Shorts recommender sophistication comparison (INT-005) — none of these should be encoded as platform fact.


# Primary-Source Remediation Pass

Date: 2026-09-08. Task: Step 15C-R. Baseline: `446deee108ff6224be7c66a744124577cc5dec37`, on `main`, matching the existing `origin/main` ref. Preflight independently counted 33 source rows, 24 distinct historical dispositions and the nine Batch 3 IDs below. No prior Batch 3 existed. Known unrelated README/docs/environment/audit changes were excluded.

This pass audits all 24 prior entries and makes 12 material source-basis or methodology remediations. Four claims (CLM-005, CLM-016, CLM-017, CLM-018) materially depended on S6/S7/S8. Other corrections address nearby-but-insufficient evidence, public/private scope and overstrong conclusions. Multiple Help pages from one publisher are not independent empirical corroboration. Dispositions are intelligence judgments, not new measured channel observations.

## Current primary-source register and retrieval checks

All R references were read and retrieved on **2026-09-08**. The publisher, relevant section and system boundary are recorded below. Older publications remain dated historical statements even when retrieved today. Help pages generally have no explicit revision date; copyright years are not revision dates. R11 is an original research paper by Google/Google DeepMind authors, hosted on arXiv, not a third-party summary. R26 uses only the signed TeamYouTube announcement; ordinary forum posts, replies and Product Expert answers are not official platform authority.

| ID / source | Publisher | System / surface | Section inspected and bounded evidence |
|---|---|---|---|
| [R1] — YouTube's Recommendation System | YouTube Help | YouTube recommendations; creator guidance | The algorithm has two goals; Recommendations are personalized; channel growth strategy. Per-viewer context, interest affinity, similar-viewer behavior, satisfaction and fresh performance; series guidance. |
| [R2] — How YouTube recommendations work | YouTube Help | Home; Up Next; Shorts Feed; channel pages | YouTube's recommendation system. History, subscriptions and feedback are inputs; Home primarily uses watch history, Up Next the current video. Surface weights differ. |
| [R3] — Good to know about recommendations | YouTube Help | YouTube recommendations; Subscriptions; Search; creator guidance | Diverse interests across formats; experimenting; optimal length; head start; unique viewers. Cross-format connections are possible, but engagement varies. No universal ideal duration. Libraries help viewer journeys; no numeric launch requirement. |
| [R4] — Understand your content performance | YouTube Help | YouTube content performance; Shorts and long-form creator guidance | Appeal; Engagement; Satisfaction; Packaging; Engaging hooks. Audience choice, continued viewing and enjoyment are distinct. Accurate packaging and concise, promise-matching intros are guidance, not fixed thresholds. |
| [R5] — YouTube performance FAQ & Troubleshooting | YouTube Help | Home; Up Next; YouTube Search; upload guidance | Suggested; Search; daily uploads; old videos; likes/dislikes. Suggested can use history; Search considers query relevance and engagement. No daily/weekly upload requirement. Older videos can regain interest. |
| [R6] — Upload schedule tips | YouTube Help | Creator scheduling guidance; videos, Shorts, live and posts | Frequency; Consistency; Content Volume. Plan a sustainable schedule around audience expectations and production resources; no documented schedule-triggered ranking reward. |
| [R7] — Add custom thumbnails on YouTube | YouTube Help | Desktop Studio; video/Shorts thumbnails; surface-specific image handling | Add a custom Short thumbnail; Image size & resolution. Current page permits verified accounts to upload Shorts thumbnails in desktop Studio. Its vertical-video surface note is not a universal Shorts-feed rule. |
| [R8] — A/B test titles & thumbnails | YouTube Help | Eligible Studio video experiments; excludes Shorts | Eligibility requirements; How does it work; Why is watch time used. Title-only, thumbnail-only and combined tests use watch-time share rather than CTR alone; no title or image formula is guaranteed. |
| [R9] — AI features and your website | Google Search Central | Google Search; AI Overviews; AI Mode | Introduction; How AI features work in Search. No special optimization is required. This does not prove that any particular writing structure is ineffective. |
| [R10] — Optimizing your website for generative AI features on Google Search | Google Search Central | Google Search; AI Overviews; AI Mode | Create valuable, non-commodity content; Mythbusting; Chunking. Useful original material and readable structure are guidance. No exact early-answer, name/date density or citation-success formula is established. |
| [R11] — Better Generalization with Semantic IDs: A Case Study in Ranking for Recommendations | Google / Google DeepMind authors; author-submitted arXiv paper | Studied YouTube recommendation ranking model; research, not every current surface | Affiliations; Introduction; 4.1 Content Embeddings; Conclusion. Google affiliations verified. The studied encoder uses audio and visual features; semantic IDs improve new/long-tail generalization. No complete 2026 architecture or mood-state model is disclosed. |
| [R12] — YouTube channel monetization policies | YouTube Help | Monetization policy | Generic or Repetitive Content; What is allowed to monetize; Reused content. Materially varied episodes can qualify; interchangeable low-value templates risk monetization eligibility. This is not a ranking-weight specification. |
| [R13] — Spam Policy | YouTube Help | Community Guidelines; platform abuse enforcement | Engagement manipulation; Automated or synthetic mass-production; Off-platform diversion. Mass-produced repetition and manipulation can violate spam policy. Ordinary branding and links are not established recommendation signals. |
| [R14] — Impersonation policy | YouTube Help | Identity policy; not recommendation ranking | What these policies mean for you. Deceptive imitation is prohibited; this does not establish a benefit for an external brand footprint. |
| [R15] — Rene's Top Five: April 18, 2024 | YouTube Blog; Rene Ritchie, YouTube Creator Liaison | 2024 Subscriptions experiment; Home versus notification/subscription traffic | Most relevant; Q&A. An optional subscription-only recommendation filter preserved chronological access. Home feedback was distinguished from ignored notifications; disabling notifications for ranking was discouraged. |
| [R16] — Rene's Top Five: August 1, 2024 | YouTube Blog; Rene Ritchie, YouTube Creator Liaison | Channel architecture guidance; Shorts, long-form, live and podcasts | Q&A on podcasts and Shorts. Channel choice depends on audience overlap; related podcast clips can coexist. This is official guidance, not a quantified ranking effect. |
| [R17] — Rene's Top Five: July 25, 2024 | YouTube Blog; Rene Ritchie, YouTube Creator Liaison | Historical Shorts Feed versus Search, Home, channel and Subscriptions; creator strategy | Q&A 1 and Q&A 2. Discusses thumbnail-free Shorts-feed viewing and thumbnail browsing elsewhere; advises balancing audience continuity with experimentation. Historical feature availability is superseded by R7/R8. |
| [R18] — Rene's Top Five: March 28, 2024 | YouTube Blog; Rene Ritchie, YouTube Creator Liaison | YouTube audience connections; deletion guidance; traffic sources | Q&A; Tip of the Week. Officially republishes deletion advice and discusses lost audience connections. It does not expose deletion timing or all retained model data. |
| [R19] — Measure key moments for audience retention | YouTube Help | YouTube Analytics; video-level retention | Key moments; Intros; Spikes; Dips; Segments. Compare similar-length videos and audience segments; inspect drop-offs. Rewatch spikes can signal confusion. The 30-second intro metric is not a mandatory hook length. |
| [R20] — Understand your YouTube engagement | YouTube Help | YouTube Analytics | Audience retention; Likes vs. dislikes. Engagement reports expose retention and like/dislike comparisons; neither defines a universal like-rate target. |
| [R21] — Explore trends on YouTube | YouTube Help | YouTube Analytics Trends; YouTube Search gaps, including Shorts | Explore the Trends Tab; Learn about Content gaps. Insufficient, outdated or low-quality search results can inspire ideas. Breakout examples are inspiration, not evidence that copying wins. |
| [R22] — Understand new, casual, & regular viewers | YouTube Help | Audience analytics; creator guidance; returning-viewer recommendations | Grow your core audience; Does the recommendation system optimize for returning viewers. Familiar formats, hosts and series can support loyalty. Returning viewers may receive more recommendations; the audience-segment metric itself is not a reach bonus. |
| [R23] — Replace or delete your video | YouTube Help | Video deletion; YouTube Search; Analytics | Delete your own videos. Deletion is permanent. Watch time remains in aggregate reports without attribution to the deleted video; deleting is not evidence that every data trace vanishes. |
| [R24] — Change video privacy settings | YouTube Help | Channel pages; Subscriptions; Search; related videos/recommendations; link access | About privacy settings; feature comparison table. Unlisted videos retain link access but lose ordinary recommendation/subscription placement. Search has a public-playlist exception. Unlisting is not continued public discovery. |
| [R25] — Impressions & click-through-rate FAQs | YouTube Help | YouTube registered impressions; excludes some external/end-screen exposures | High or low CTR; comparing performance. The reported 2–10% range for half of channels/videos is descriptive, not a target or distribution gate. Audience and traffic mix matter. |
| [R26] — Q3 & Q4 2025: Latest improvements to YouTube on TV | YouTube Help announcements; Hank (TeamYouTube) | YouTube on TV; Subscriptions shelf | Tailored Experiences for Every Viewer; signed announcement, not replies. Announces a Most Relevant shelf above the TV subscriptions feed. Does not disclose that shelf's exact recent-interest selection rule or establish identical desktop/mobile layouts. |
| [R27] — The Future of YouTube 2026 | YouTube Blog; Neal Mohan | Platform outlook; TV viewing context; policy direction | Reinventing entertainment; AI. An official platform outlook does not validate the source's private-client device percentages, duration dataset or personality-market comparison. |
| [R28] — All the YouTube news from Google I/O 2026 | YouTube Blog; The YouTube Team | Ask YouTube conversational search; not Google Search AI Overviews | Ask YouTube announcement. An official YouTube-native conversational-search announcement exists. It provides no source-script citation formula and does not authorize importing Google Search mechanisms. |

The requested legacy Test & compare thumbnails URL (`https://support.google.com/youtube/answer/13861714`) redirects to R8. It is one source, not a second corroboration. Several web-reader requests returned rate limits or incomplete bodies; alternate canonical URLs and read-only direct HTTP retrieval recovered the required pages, including R4 and R26. Only successfully read sources enter the current evidence register.

Historical S6 (Search Engine Journal), S7 (vidIQ/press) and S8 (PhoneArena/community reporting) remain visible solely to preserve history. None is a current primary reference. S8's Help component was adjacent material, not independent confirmation of the reported visibility pattern. S10's Hype feature is not used as organic cold-start evidence. S4's Nielsen-attributed platform statistic is not an independent check of the source's private client dataset.

## Search coverage and negative-evidence limits

Research covered the requested recommendation, cross-format, performance, duration, schedule, packaging tests, YouTube Search, Shorts thumbnail, monetization/spam and Search AI topics. Targeted official-domain searches included larger/bigger Home thumbnails and long-form outcomes; subscription Most Relevant shelves; semantic IDs and mood; exact audience seeding; deletion/unlisting audience connections; content gaps; and the 100-billion-view/51% statistic. Results were read only when they supplied relevant official material or original research. Ordinary community answers containing exact seeding/retention rules were rejected, even when hosted on support.google.com.

For CLM-016, retrieved current thumbnail documentation does not reproduce the source's experiment or outcome; unrelated older redesign announcements cannot substitute. No usable direct official experiment record was located. For numerical/private/internal claims, failure to locate evidence means unestablished in this review, never false by default. The search is reasonably broad, not a claim to have exhaustively inspected every official video or every private experiment.

## Audit of all 24 prior dispositions

The current register later in this document owns the final statuses. This audit records whether each historical entry requires a material remediation or retains its disposition with the final register's narrower wording.

| Claim ID | Prior status | Current official basis | Audit outcome |
|---|---|---|---|
| ALG26-CLM-001 | SUPPORTED | [R1], [R2] | Retained; use bounded final-register conclusion only |
| ALG26-CLM-002 | PARTIALLY_SUPPORTED | [R1], [R2], [R15], [R19] | Retained; use bounded final-register conclusion only |
| ALG26-CLM-003 | PARTIALLY_SUPPORTED | [R1], [R5] | Retained; use bounded final-register conclusion only |
| ALG26-CLM-004 | SUPPORTED | [R1], [R2], [R4] | Retained; use bounded final-register conclusion only |
| ALG26-CLM-005 | PARTIALLY_SUPPORTED | [R3], [R16] | VALIDATION_REMEDIATION below |
| ALG26-CLM-006 | PARTIALLY_SUPPORTED | [R1], [R5] | Retained; use bounded final-register conclusion only |
| ALG26-CLM-007 | PARTIALLY_SUPPORTED | [R5], [R11] | VALIDATION_REMEDIATION below |
| ALG26-CLM-008 | SUPPORTED | [R2], [R5], [R22] | Retained; use bounded final-register conclusion only |
| ALG26-CLM-009 | SUPPORTED | [R12], [R13] | VALIDATION_REMEDIATION below |
| ALG26-CLM-011 | SUPPORTED | [R2] | Retained; use bounded final-register conclusion only |
| ALG26-CLM-012 | PARTIALLY_SUPPORTED | [R11] | VALIDATION_REMEDIATION below |
| ALG26-CLM-013 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R11] | VALIDATION_REMEDIATION below |
| ALG26-CLM-014 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R27] | Retained; use bounded final-register conclusion only |
| ALG26-CLM-015 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R3] | Retained; use bounded final-register conclusion only |
| ALG26-CLM-016 | PARTIALLY_SUPPORTED | [R7], [R8] | VALIDATION_REMEDIATION below |
| ALG26-CLM-017 | PARTIALLY_SUPPORTED | [R7], [R17] | VALIDATION_REMEDIATION below |
| ALG26-CLM-018 | CONTRADICTED | [R3], [R16] | VALIDATION_REMEDIATION below |
| ALG26-INT-001 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R11] | Retained; use bounded final-register conclusion only |
| ALG26-INT-002 | PARTIALLY_SUPPORTED | [R1], [R2], [R22] | VALIDATION_REMEDIATION below |
| ALG26-INT-003 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R3], [R27] | Retained; use bounded final-register conclusion only |
| ALG26-INT-004 | PARTIALLY_SUPPORTED | [R12], [R22], [R27] | VALIDATION_REMEDIATION below |
| ALG26-INT-005 | NOT_CURRENTLY_VERIFIABLE | [R3], [R11] | VALIDATION_REMEDIATION below |
| ALG26-REC-007 | CONTRADICTED | [R9], [R10], [R28] | VALIDATION_REMEDIATION below |
| ALG26-REC-008 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R13], [R14], [R9] | Retained; use bounded final-register conclusion only |

## Verified source-member provenance

All 64 ZIP members were read without extraction and matched their registered DB SHA-256 values. These seven claim-bearing members also match the unchanged source-intelligence provenance table. Each entry below retains its original claim ID, assertion type and timestamp range.

| Alias | FILE ID / member | Member SHA-256 | Stable tab locator |
|---|---|---|---|
| T01 | FILE-006404 / `tabs/tab-01-video-01.md` | `8b8b01f5892fefe5e58fc517b144c65daec578ea364f83f9185c27409932c6ec` | `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.0` |
| T36 | FILE-006439 / `tabs/tab-36-video-36.md` | `e18175321820d4c28ef8d33223b9b8543057e2cc2bd6480a6d883741938a9863` | `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.iroe5hw3b8bi` |
| T39 | FILE-006442 / `tabs/tab-39-video-39.md` | `65131eb055daef65e3fa0c1804a6a5ba773c3e2f298a08a495001719528848a6` | `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.r9bzs1xopm0k` |
| T43 | FILE-006446 / `tabs/tab-43-video-43.md` | `05df85450219b4934692813f5d293a30f0176e0da5a1d753de173b22f2e4f9da` | `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.2znmr6uzc7sq` |
| T48 | FILE-006451 / `tabs/tab-48-video-48.md` | `6043129fc8ddd40f3e00023624cdd69007d0cf8f72a3b4689ca28d7695ba292d` | `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.pskezhreczge` |
| T49 | FILE-006452 / `tabs/tab-49-video-49.md` | `ce95fe8cb75e9118a610e0a140503db24bb84579c1fb9157652c247199a6fe06` | `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.rkng3n2x22ds` |
| T51 | FILE-006454 / `tabs/tab-51-video-51.md` | `3cf49a2d1258f747e65076a1d15400ca7e96ab7e411fe173567d38c7f3aa49fc` | `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.3u7zutfuv3rh` |

### VALIDATION_REMEDIATION — ALG26-CLM-005

- **CLAIM ID:** ALG26-CLM-005
- **CLAIM TYPE:** SOURCE_CLAIM
- **SOURCE LOCATOR:** T39, 23:43–26:36; FILE-006442 / `tabs/tab-39-video-39.md`; member SHA-256 `65131eb055daef65e3fa0c1804a6a5ba773c3e2f298a08a495001719528848a6`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.r9bzs1xopm0k`
- **SOURCE SAYS:** Channels should align with audiences, while recommendations may still distinguish topic, length, Shorts, long-form, podcast, or live-stream preferences within one channel.
- **PREVIOUS STATUS:** PARTIALLY_SUPPORTED
- **PREVIOUS EVIDENCE BASIS:** S7: vidIQ/press-mediated executive guidance and a reported 2026 bridge.
- **PRIMARY REPLACEMENT:** [R3], [R16]. The cited sections and surface limits are specified in the current source register.
- **FINAL STATUS:** PARTIALLY_SUPPORTED
- **RATIONALE:** The direct official sources now establish format-specific preferences and conditional channel guidance. R3 explicitly says experimenting across formats does not inherently confuse the algorithm or directly penalize the channel. Status remains partial because the full granular mechanism is not documented.
- **OS CAN SAFELY CONCLUDE:** Cross-format preference differences are documented; the full length/podcast/internal partition list remains unestablished.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** DIRECT_CONFLICT with CLM-018 only in its universal channel-separation form.

### VALIDATION_REMEDIATION — ALG26-CLM-007

- **CLAIM ID:** ALG26-CLM-007
- **CLAIM TYPE:** SOURCE_CLAIM
- **SOURCE LOCATOR:** T39, 31:47–32:39; FILE-006442 / `tabs/tab-39-video-39.md`; member SHA-256 `65131eb055daef65e3fa0c1804a6a5ba773c3e2f298a08a495001719528848a6`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.r9bzs1xopm0k`
- **SOURCE SAYS:** New channels and fresh videos can be matched without prior channel-viewer history by using topical preferences and an understanding of the video's subject.
- **PREVIOUS STATUS:** PARTIALLY_SUPPORTED
- **PREVIOUS EVIDENCE BASIS:** S1 plus S10 Hype eligibility/leaderboard evidence was used for organic new-channel matching.
- **PRIMARY REPLACEMENT:** [R5], [R11]. The cited sections and surface limits are specified in the current source register.
- **FINAL STATUS:** PARTIALLY_SUPPORTED
- **RATIONALE:** Hype is a distinct discovery feature and cannot establish zero-history organic matching. Replace that analogy with direct Home guidance and bounded cold-start research; retain partial status.
- **OS CAN SAFELY CONCLUDE:** New-video discovery and researched cold-start handling have primary support; exact first-upload audience assignment does not.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT established; prior overreach is superseded as described above.

### VALIDATION_REMEDIATION — ALG26-CLM-009

- **CLAIM ID:** ALG26-CLM-009
- **CLAIM TYPE:** SOURCE_CLAIM
- **SOURCE LOCATOR:** T48, 6:56–9:06; FILE-006451 / `tabs/tab-48-video-48.md`; member SHA-256 `6043129fc8ddd40f3e00023624cdd69007d0cf8f72a3b4689ca28d7695ba292d`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.pskezhreczge`
- **SOURCE SAYS:** The source distinguishes literal, near-identical templated repetition from a reusable format: the former may be spam, while consistent topic formulas can remain acceptable when episodes differ.
- **PREVIOUS STATUS:** SUPPORTED
- **PREVIOUS EVIDENCE BASIS:** S3 monetization eligibility was used to validate a claim that also described spam.
- **PRIMARY REPLACEMENT:** [R12], [R13]. The cited sections and surface limits are specified in the current source register.
- **FINAL STATUS:** SUPPORTED
- **RATIONALE:** The current Spam Policy directly covers abusive repetitive mass production; the monetization page separately permits materially varied episodes. Status remains supported within those two policy scopes, with no ranking inference.
- **OS CAN SAFELY CONCLUDE:** Repetitive mass production can violate policy; materially varied formats can qualify for monetization. No ranking penalty or blanket exemption is inferred.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT established; prior overreach is superseded as described above.

### VALIDATION_REMEDIATION — ALG26-CLM-012

- **CLAIM ID:** ALG26-CLM-012
- **CLAIM TYPE:** SOURCE_CLAIM
- **SOURCE LOCATOR:** T51, 4:28–5:52; FILE-006454 / `tabs/tab-51-video-51.md`; member SHA-256 `3cf49a2d1258f747e65076a1d15400ca7e96ab7e411fe173567d38c7f3aa49fc`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.3u7zutfuv3rh`
- **SOURCE SAYS:** A transcript claims YouTube uses a large recommender model and semantic IDs derived from metadata, frames, audio, pacing, and format.
- **PREVIOUS STATUS:** PARTIALLY_SUPPORTED
- **PREVIOUS EVIDENCE BASIS:** S5 abstract-level reading treated the entire modality list as unconfirmed.
- **PRIMARY REPLACEMENT:** [R11]. The cited sections and surface limits are specified in the current source register.
- **FINAL STATUS:** PARTIALLY_SUPPORTED
- **RATIONALE:** The full paper, section 4.1, explicitly identifies audio and visual features. Correct that omission; do not convert a studied production model into a complete account of current recommendations. Status remains partial.
- **OS CAN SAFELY CONCLUDE:** The studied semantic-ID model uses audiovisual embeddings; metadata, pacing, format and complete current deployment claims exceed the evidence.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT established; prior overreach is superseded as described above.

### VALIDATION_REMEDIATION — ALG26-CLM-013

- **CLAIM ID:** ALG26-CLM-013
- **CLAIM TYPE:** SOURCE_CLAIM
- **SOURCE LOCATOR:** T51, 7:31–8:12; FILE-006454 / `tabs/tab-51-video-51.md`; member SHA-256 `3cf49a2d1258f747e65076a1d15400ca7e96ab7e411fe173567d38c7f3aa49fc`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.3u7zutfuv3rh`
- **SOURCE SAYS:** The same transcript claims semantic IDs are connected to watch-history clusters representing recent formats, styles, interests, and mood.
- **PREVIOUS STATUS:** NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
- **PREVIOUS EVIDENCE BASIS:** S5 lacked the asserted semantic-ID mood-cluster description; prior result was evidence-not-found.
- **PRIMARY REPLACEMENT:** [R11]. The cited sections and surface limits are specified in the current source register.
- **FINAL STATUS:** NOT_CURRENTLY_VERIFIABLE
- **RATIONALE:** The unsupported component concerns private platform internals, so NOT_CURRENTLY_VERIFIABLE better fits the task definitions. Absence from this paper does not disprove the mechanism.
- **OS CAN SAFELY CONCLUDE:** The asserted private mood-cluster linkage is not publicly verifiable from the reviewed technical evidence.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** UNRESOLVED_SPECIFICITY beyond CLM-012; lack of disclosure is not disproof.

### VALIDATION_REMEDIATION — ALG26-CLM-016

- **CLAIM ID:** ALG26-CLM-016
- **CLAIM TYPE:** SOURCE_CLAIM
- **SOURCE LOCATOR:** T48, 1:47–3:21; FILE-006451 / `tabs/tab-48-video-48.md`; member SHA-256 `6043129fc8ddd40f3e00023624cdd69007d0cf8f72a3b4689ca28d7695ba292d`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.pskezhreczge`
- **SOURCE SAYS:** The source claims experiments with larger, fewer homepage thumbnails improved selection and long-form viewing while smaller/new-channel recommendations remained near the top.
- **PREVIOUS STATUS:** PARTIALLY_SUPPORTED
- **PREVIOUS EVIDENCE BASIS:** S6: Search Engine Journal reporting, described incorrectly as weaker primary evidence.
- **PRIMARY REPLACEMENT:** [R7], [R8]. The cited sections and surface limits are specified in the current source register. These are adjacent checks, not evidence proving the claimed Home experiment.
- **FINAL STATUS:** NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
- **RATIONALE:** No direct official replacement was located for the specific experiment outcome. Current thumbnail/experiment documentation is adjacent only. Withdraw the prior positive finding and downgrade to evidence-not-found.
- **OS CAN SAFELY CONCLUDE:** No direct official record located for the claimed Home experiment outcome or small-channel placement. Packaging tools do not establish either.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT established; prior overreach is superseded as described above.

### VALIDATION_REMEDIATION — ALG26-CLM-017

- **CLAIM ID:** ALG26-CLM-017
- **CLAIM TYPE:** SOURCE_CLAIM
- **SOURCE LOCATOR:** T48, 13:05–13:52; FILE-006451 / `tabs/tab-48-video-48.md`; member SHA-256 `6043129fc8ddd40f3e00023624cdd69007d0cf8f72a3b4689ca28d7695ba292d`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.pskezhreczge`
- **SOURCE SAYS:** The source says Shorts thumbnails do not appear in the swipe feed but can matter in search, browse, and Shorts-shelf contexts.
- **PREVIOUS STATUS:** PARTIALLY_SUPPORTED
- **PREVIOUS EVIDENCE BASIS:** S8: PhoneArena/community feature reporting plus an adjacent Shorts Help page.
- **PRIMARY REPLACEMENT:** [R7], [R17]. The cited sections and surface limits are specified in the current source register.
- **FINAL STATUS:** PARTIALLY_SUPPORTED
- **RATIONALE:** Replace reporting with direct Help and the official liaison article. Current desktop custom-Shorts upload support supersedes old availability discussions; retain partial status for unverified current shelf-specific scope/effects. Upload availability does not establish Shorts-feed ranking impact.
- **OS CAN SAFELY CONCLUDE:** Direct official evidence replaces press. Current upload capability is established; historical feed guidance does not prove every current shelf or placement effect.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT established; prior overreach is superseded as described above.

### VALIDATION_REMEDIATION — ALG26-CLM-018

- **CLAIM ID:** ALG26-CLM-018
- **CLAIM TYPE:** SOURCE_CLAIM
- **SOURCE LOCATOR:** T01, 0:24–0:49; FILE-006404 / `tabs/tab-01-video-01.md`; member SHA-256 `8b8b01f5892fefe5e58fc517b144c65daec578ea364f83f9185c27409932c6ec`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.0`
- **SOURCE SAYS:** A creator claims Shorts and long-form use separate algorithms and audiences and should not share a channel.
- **PREVIOUS STATUS:** CONTRADICTED
- **PREVIOUS EVIDENCE BASIS:** S7: vidIQ/press-mediated same-channel advice and bridge reporting.
- **PRIMARY REPLACEMENT:** [R3], [R16]. The cited sections and surface limits are specified in the current source register.
- **FINAL STATUS:** CONTRADICTED
- **RATIONALE:** Direct official authority sustains contradiction of the absolute separation instruction. No secondary report or purported bridge launch date determines the current result.
- **OS CAN SAFELY CONCLUDE:** The universal channel-separation instruction conflicts with official guidance. Distinct surface behavior is not itself refuted.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** DIRECT_CONFLICT with the absolute channel-separation rule; CLM-005 is the compatible bounded alternative.

### VALIDATION_REMEDIATION — ALG26-INT-002

- **CLAIM ID:** ALG26-INT-002
- **CLAIM TYPE:** SOURCE_INTERPRETATION
- **SOURCE LOCATOR:** T36, 11:25–13:03; FILE-006439 / `tabs/tab-36-video-36.md`; member SHA-256 `e18175321820d4c28ef8d33223b9b8543057e2cc2bd6480a6d883741938a9863`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.iroe5hw3b8bi`
- **SOURCE SAYS:** The speaker interprets semantic matching as reducing the value of generic content and subscriber totals relative to specific content for a clearly understood viewer.
- **PREVIOUS STATUS:** PARTIALLY_SUPPORTED
- **PREVIOUS EVIDENCE BASIS:** S1/S2 personalized interests were extended into relative signal dominance and semantic-era devaluation.
- **PRIMARY REPLACEMENT:** [R1], [R2], [R22]. The cited sections and surface limits are specified in the current source register.
- **FINAL STATUS:** PARTIALLY_SUPPORTED
- **RATIONALE:** Retain partial support for audience matching only. Withdraw any inference of a temporal subscriber downgrade, fixed relative signal priority or hidden topic-authority weight.
- **OS CAN SAFELY CONCLUDE:** Audience relevance is documented; semantic-era subscriber devaluation and a hidden topic-authority weight are not.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT established; prior overreach is superseded as described above.

### VALIDATION_REMEDIATION — ALG26-INT-004

- **CLAIM ID:** ALG26-INT-004
- **CLAIM TYPE:** SOURCE_INTERPRETATION
- **SOURCE LOCATOR:** T49, 31:13–33:46; FILE-006452 / `tabs/tab-49-video-49.md`; member SHA-256 `ce95fe8cb75e9118a610e0a140503db24bb84579c1fb9157652c247199a6fe06`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.rkng3n2x22ds`
- **SOURCE SAYS:** The speaker argues that personality and personal connection become a stronger differentiator as high-production spectacle becomes easier to imitate.
- **PREVIOUS STATUS:** PARTIALLY_SUPPORTED
- **PREVIOUS EVIDENCE BASIS:** S4 disclosure/anti-spam policy direction was treated as partial evidence of a personality-market advantage.
- **PRIMARY REPLACEMENT:** [R12], [R22], [R27]. The cited sections and surface limits are specified in the current source register.
- **FINAL STATUS:** NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
- **RATIONALE:** Policy and audience-loyalty guidance do not establish the comparative market claim. Downgrade rather than substituting adjacent guidance for its actual causal assertion; no human-versus-AI ranking preference is established.
- **OS CAN SAFELY CONCLUDE:** Audience relationships may be useful; the claimed increase in personality differentiation as spectacle becomes imitable is unestablished.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT established; prior overreach is superseded as described above.

### VALIDATION_REMEDIATION — ALG26-INT-005

- **CLAIM ID:** ALG26-INT-005
- **CLAIM TYPE:** SOURCE_INTERPRETATION
- **SOURCE LOCATOR:** T49, 1:00:25–1:02:14; FILE-006452 / `tabs/tab-49-video-49.md`; member SHA-256 `ce95fe8cb75e9118a610e0a140503db24bb84579c1fb9157652c247199a6fe06`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.rkng3n2x22ds`
- **SOURCE SAYS:** A strategist speculates that the mature long-form recommender is more sophisticated than the newer Shorts recommender and may handle content volume better.
- **PREVIOUS STATUS:** NOT_CURRENTLY_VERIFIABLE
- **PREVIOUS EVIDENCE BASIS:** No public internal comparison; Batch 2 implications nevertheless called it permanently unverifiable.
- **PRIMARY REPLACEMENT:** [R3], [R11]. The cited sections and surface limits are specified in the current source register.
- **FINAL STATUS:** NOT_CURRENTLY_VERIFIABLE
- **RATIONALE:** Keep NOT_CURRENTLY_VERIFIABLE, but explicitly withdraw permanent unverifiability. Public evidence is incomplete today; a later technical disclosure could change the result.
- **OS CAN SAFELY CONCLUDE:** The internal sophistication/volume comparison remains unverified; future public evidence could permit reassessment.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT established; prior overreach is superseded as described above.

### VALIDATION_REMEDIATION — ALG26-REC-007

- **CLAIM ID:** ALG26-REC-007
- **CLAIM TYPE:** SOURCE_RECOMMENDATION
- **SOURCE LOCATOR:** T43, 5:08–6:49; FILE-006446 / `tabs/tab-43-video-43.md`; member SHA-256 `05df85450219b4934692813f5d293a30f0176e0da5a1d753de173b22f2e4f9da`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.2znmr6uzc7sq`
- **SOURCE SAYS:** Structure scripts with an early direct answer and specific names, dates, and places to make passages citation-friendly for AI answers.
- **PREVIOUS STATUS:** CONTRADICTED
- **PREVIOUS EVIDENCE BASIS:** S11/S12: no special optimization requirement was read as direct contradiction of citation benefit; no YouTube-native official material was said to exist.
- **PRIMARY REPLACEMENT:** [R9], [R10], [R28]. The cited sections and surface limits are specified in the current source register.
- **FINAL STATUS:** NOT_SUPPORTED_BY_PRIMARY_EVIDENCE
- **RATIONALE:** No requirement does not mean no possible benefit. Change CONTRADICTED to NOT_SUPPORTED_BY_PRIMARY_EVIDENCE. An official Ask YouTube announcement exists, but it supplies no script-selection formula. No Google Search-to-YouTube bridge is inferred.
- **OS CAN SAFELY CONCLUDE:** The early-answer citation formula is unestablished, not disproved. Google Search and Ask YouTube are distinct systems.
- **CONFIDENCE / LIMITATION:** High confidence in the cited documents' stated scope; the unsupported part of the source claim remains unestablished. Official statements do not provide independent experimental data or a complete current ranking specification.
- **CONFLICT STATUS:** PRIOR_CONFLICT_WITHDRAWN. No demonstrated contradiction of citation benefit; unsupported mechanism remains excluded.

# Validation Batch 3 — Final Claims

Date: 2026-09-08. Exactly the nine live-confirmed outstanding IDs are dispositioned below. The eight REC entries retain SOURCE_RECOMMENDATION identity. SUPPORTED for a recommendation means its actual bounded guidance has direct official support; it does not promote the strategy into a measured effect or guaranteed ranking mechanism. Original extracted wording remains intact; stronger statements in the cited raw passage are explicitly separated.

### ALG26-CLM-010 — Subscription feed

- **CLAIM ID:** ALG26-CLM-010
- **CLAIM TYPE:** SOURCE_CLAIM
- **SOURCE LOCATOR:** T48, 9:14–10:34; FILE-006451 / `tabs/tab-48-video-48.md`; member SHA-256 `6043129fc8ddd40f3e00023624cdd69007d0cf8f72a3b4689ca28d7695ba292d`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.pskezhreczge`
- **SOURCE SAYS:** The source says a recommendation shelf in the subscription feed selects from subscribed channels using recent interests while retaining the chronological feed below it.
- **PRIMARY EVIDENCE SAYS:** R26 documents a TV subscription shelf; R15 documents a 2024 subscription-only filter with chronological access. R3 describes a most-recent subscription list. These support the bounded product idea, not identical current layouts or the exact recent-interest rule for the shelf described in T48.
- **HEURISTIC VS PLATFORM FACT:** PLATFORM FACT: the separately documented subscription features above. CREATOR HEURISTIC: none; this entry remains SOURCE_CLAIM. CLAIMED CAUSAL MECHANISM: recent-interest selection within that exact shelf remains unconfirmed, rather than borrowed from Home personalization.
- **VALIDATION STATUS:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Subscription recommendations and chronological access are documented in bounded contexts; the exact shelf mechanism and universal rollout are not.
- **CONFIDENCE / LIMITATION:** Medium on product context; limited on current shelf selection and cross-device rollout. A dated optional filter and a TV shelf are not the same experiment.
- **CONFLICT STATUS:** PARTIAL_TENSION only if chronology is treated as exclusive. A shelf and chronological list can coexist; current layout/selection details remain unresolved. No creator-recommendation evidence substitutes for platform analysis.
- **PRIMARY SOURCES:** [R3], [R15], [R26]; retrieved 2026-09-08. See the source register for publisher, cited section and exact surface scope.

### ALG26-REC-001 — Analytics / retention

- **CLAIM ID:** ALG26-REC-001
- **CLAIM TYPE:** SOURCE_RECOMMENDATION
- **SOURCE LOCATOR:** T39, 14:02–14:34; FILE-006442 / `tabs/tab-39-video-39.md`; member SHA-256 `65131eb055daef65e3fa0c1804a6a5ba773c3e2f298a08a495001719528848a6`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.r9bzs1xopm0k`
- **SOURCE SAYS:** Compare analytics against similar videos, inspect retention-drop points and like rates, and combine metrics with direct audience feedback.
- **PRIMARY EVIDENCE SAYS:** R19 supplies similar-length retention comparisons and subscriber/new-viewer segments; R20 exposes like/dislike reports; R22 describes comments/community interaction. These support the recommended diagnostic practices, not a proven optimal metric combination.
- **HEURISTIC VS PLATFORM FACT:** PLATFORM FACT: analytics reports and feedback channels exist. CREATOR HEURISTIC: combine relative metrics and audience feedback when deciding what to test. CLAIMED CAUSAL MECHANISM: none is established for merely monitoring metrics; no CTR, retention or like-rate gate follows.
- **VALIDATION STATUS:** SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Use retention comparisons, engagement reports and audience feedback as diagnostics, without metric thresholds or ranking guarantees.
- **CONFIDENCE / LIMITATION:** High for the diagnostic guidance. Audience selection and sample size limit comparisons; comments are not a representative survey.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT. Consistent with CLM-004; a rewatch spike is not necessarily approval.
- **PRIMARY SOURCES:** [R19], [R20], [R22]; retrieved 2026-09-08. See the source register for publisher, cited section and exact surface scope.

### ALG26-REC-002 — Subscriber notifications

- **CLAIM ID:** ALG26-REC-002
- **CLAIM TYPE:** SOURCE_RECOMMENDATION
- **SOURCE LOCATOR:** T39, 34:37–36:50; FILE-006442 / `tabs/tab-39-video-39.md`; member SHA-256 `65131eb055daef65e3fa0c1804a6a5ba773c3e2f298a08a495001719528848a6`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.r9bzs1xopm0k`
- **SOURCE SAYS:** Do not disable subscriber notifications merely to game recommendations; instead inspect subscriber-source behavior separately.
- **PRIMARY EVIDENCE SAYS:** R15 directly discourages disabling subscriber delivery to improve long-form Home results. R18 reinforces the distinction between traffic sources. R19 supports subscriber/non-subscriber analysis; analytics segmentation does not disclose training architecture.
- **HEURISTIC VS PLATFORM FACT:** PLATFORM FACT: the official Home-versus-notification/subscription distinction. CREATOR HEURISTIC: examine the appropriate audience segment and delivery context. CLAIMED CAUSAL MECHANISM: no distribution advantage from disabling the checkbox is established.
- **VALIDATION STATUS:** SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Do not disable subscriber delivery as an algorithm trick; distinguish notification/subscription traffic from Home.
- **CONFIDENCE / LIMITATION:** High for the specific guidance, bounded to the documented context. This is not a claim that all traffic sources are perfectly isolated or that notification settings never have legitimate uses.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT. Complements CLM-002/008 without validating exact cohort weights.
- **PRIMARY SOURCES:** [R15], [R18], [R19]; retrieved 2026-09-08. See the source register for publisher, cited section and exact surface scope.

### ALG26-REC-003 — Channel architecture

- **CLAIM ID:** ALG26-REC-003
- **CLAIM TYPE:** SOURCE_RECOMMENDATION
- **SOURCE LOCATOR:** T39, 23:43–28:22; FILE-006442 / `tabs/tab-39-video-39.md`; member SHA-256 `65131eb055daef65e3fa0c1804a6a5ba773c3e2f298a08a495001719528848a6`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.r9bzs1xopm0k`
- **SOURCE SAYS:** Align channels with audiences and brand promises, while choosing same-channel versus separate-channel formats according to audience overlap and creator goals.
- **PRIMARY EVIDENCE SAYS:** R16 directly discusses channel architecture for long-form, live, Shorts and podcasts; R3 describes cross-format preferences. The advice is conditional, not a format-separation mandate.
- **HEURISTIC VS PLATFORM FACT:** PLATFORM FACT: format connections are possible. CREATOR HEURISTIC: use audience overlap and the channel promise to choose architecture, then experiment. CLAIMED CAUSAL MECHANISM: neither mixing nor splitting automatically improves distribution.
- **VALIDATION STATUS:** SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Choose channel architecture by audience fit and goals; this is conditional creator guidance.
- **CONFIDENCE / LIMITATION:** High for official strategic guidance. Audience overlap and creator goals still require separate channel-specific evidence before application.
- **CONFLICT STATUS:** DIRECT_CONFLICT with CLM-018 as a universal rule; compatible with bounded CLM-005.
- **PRIMARY SOURCES:** [R16], [R3]; retrieved 2026-09-08. See the source register for publisher, cited section and exact surface scope.

### ALG26-REC-004 — Differentiation / audience promise

- **CLAIM ID:** ALG26-REC-004
- **CLAIM TYPE:** SOURCE_RECOMMENDATION
- **SOURCE LOCATOR:** T48, 3:33–6:38; FILE-006451 / `tabs/tab-48-video-48.md`; member SHA-256 `6043129fc8ddd40f3e00023624cdd69007d0cf8f72a3b4689ca28d7695ba292d`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.pskezhreczge`
- **SOURCE SAYS:** Find differentiated value and make a consistent promise to a defined audience rather than becoming the twentieth interchangeable treatment of a topic.
- **PRIMARY EVIDENCE SAYS:** R4 addresses audience fit and communicating value; R17 balances continuity and experimentation; R22 describes familiar formats and branding as loyalty guidance. Together these substantiate the recommendation as strategy.
- **HEURISTIC VS PLATFORM FACT:** PLATFORM FACT: documented viewer-response signals, not a uniqueness score. CREATOR HEURISTIC: differentiate a clear audience promise. CLAIMED CAUSAL MECHANISM: no fixed topic-authority, novelty or guaranteed repeat-recommendation reward is documented.
- **VALIDATION STATUS:** SUPPORTED
- **OS CAN SAFELY CONCLUDE:** An audience promise and differentiated value are defensible strategy; no novelty weight or guaranteed repeat distribution follows.
- **CONFIDENCE / LIMITATION:** High for guidance; not evidence that every differentiated treatment beats a familiar topic. The twentieth-treatment example is rhetoric, not a threshold.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT. INT-002 cannot convert this advice into semantic-era subscriber devaluation.
- **PRIMARY SOURCES:** [R4], [R17], [R22]; retrieved 2026-09-08. See the source register for publisher, cited section and exact surface scope.

### ALG26-REC-005 — New-channel viewer journey

- **CLAIM ID:** ALG26-REC-005
- **CLAIM TYPE:** SOURCE_RECOMMENDATION
- **SOURCE LOCATOR:** T48, 15:08–15:56; FILE-006451 / `tabs/tab-48-video-48.md`; member SHA-256 `6043129fc8ddd40f3e00023624cdd69007d0cf8f72a3b4689ca28d7695ba292d`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.pskezhreczge`
- **SOURCE SAYS:** Launch with several linked videos so a viewer can continue through a coherent journey and establish multiple watch-history interactions.
- **PRIMARY EVIDENCE SAYS:** R1 recommends series and linked viewing paths; R3 discusses a library helping new viewers build engagement. Neither prescribes a launch count. T48 adds preparing ten videos and publishing three or four together; these remain the speaker's plan.
- **HEURISTIC VS PLATFORM FACT:** PLATFORM FACT: watch history is an input (CLM-011). CREATOR HEURISTIC: prepare a coherent set of follow-on videos. CLAIMED CAUSAL MECHANISM: no fixed number of uploads or watch-history interactions unlocks distribution; publication alone is not engagement.
- **VALIDATION STATUS:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** A coherent library can help continued viewing; a 3–4-video simultaneous launch or ten-video preparation rule is not established.
- **CONFIDENCE / LIMITATION:** Medium. The library rationale is documented; the launch recipe and incremental causal effect are not quantified.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT with CLM-011. Any mandatory upload-volume or same-day cadence interpretation exceeds evidence.
- **PRIMARY SOURCES:** [R1], [R3]; retrieved 2026-09-08. See the source register for publisher, cited section and exact surface scope.

### ALG26-REC-006 — Shows / returning viewers

- **CLAIM ID:** ALG26-REC-006
- **CLAIM TYPE:** SOURCE_RECOMMENDATION
- **SOURCE LOCATOR:** T49, 14:10–17:24 and 31:13–33:46; FILE-006452 / `tabs/tab-49-video-49.md`; member SHA-256 `ce95fe8cb75e9118a610e0a140503db24bb84579c1fb9157652c247199a6fe06`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.rkng3n2x22ds`
- **SOURCE SAYS:** Develop repeatable formats into recognizable shows that support multiple episodes, binge paths, returning viewers, and audience relationships rather than maximizing every isolated view.
- **PRIMARY EVIDENCE SAYS:** R1 recommends series and continuation links; R22 describes familiar formats, series and hosts in audience-loyalty guidance. These directly support experimenting with recurring shows.
- **HEURISTIC VS PLATFORM FACT:** PLATFORM FACT: returning-viewer behavior is relevant; the regular-viewer analytics label itself is not a reach reward. CREATOR HEURISTIC: build recognizable episodes and voluntary continuation paths. CLAIMED CAUSAL MECHANISM: no automatic show-format, emotion or session-time ranking bonus is established.
- **VALIDATION STATUS:** SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Series and familiar formats are supported creator guidance; shows do not receive a documented automatic ranking boost.
- **CONFIDENCE / LIMITATION:** High for guidance, limited for any comparative performance claim. This does not establish INT-003's TV-friction theory or INT-004's temporal personality advantage.
- **CONFLICT STATUS:** NO_DIRECT_CONFLICT. Series still need material variation under CLM-009; repeating a successful template is not guaranteed success.
- **PRIMARY SOURCES:** [R1], [R22]; retrieved 2026-09-08. See the source register for publisher, cited section and exact surface scope.

### ALG26-REC-009 — Content gaps / market research

- **CLAIM ID:** ALG26-REC-009
- **CLAIM TYPE:** SOURCE_RECOMMENDATION
- **SOURCE LOCATOR:** T01, 6:29–8:08; FILE-006404 / `tabs/tab-01-video-01.md`; member SHA-256 `8b8b01f5892fefe5e58fc517b144c65daec578ea364f83f9185c27409932c6ec`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.0`
- **SOURCE SAYS:** Seek specific questions or subjects not already covered well in video and contribute net-new information rather than generic duplication.
- **PRIMARY EVIDENCE SAYS:** R21 directly supports researching inadequate YouTube search results. T01's surrounding passage adds AI-citation/information-gain claims and guaranteed commercial examples. R9/R10 do not establish those formulas; their scope is Google Search.
- **HEURISTIC VS PLATFORM FACT:** PLATFORM FACT: Trends exposes search-gap research. CREATOR HEURISTIC: contribute useful missing information. CLAIMED CAUSAL MECHANISM: novelty does not establish automatic YouTube ranking, AI citation, Gemini transcript-selection or revenue rewards.
- **VALIDATION STATUS:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Content-gap research is official creator guidance; the source passage adds an unverified AI-citation/information-gain mechanism.
- **CONFIDENCE / LIMITATION:** Medium: the research practice is supported; the passage's causal and commercial promises are not. Trends availability and audience demand vary.
- **CONFLICT STATUS:** CROSS_SYSTEM_OVERCLAIM with the source's Google AI framing. Same evidence boundary as REC-007; not a contradiction of useful gap research.
- **PRIMARY SOURCES:** [R21], [R9], [R10]; retrieved 2026-09-08. See the source register for publisher, cited section and exact surface scope.

### ALG26-REC-010 — Deletion / audience data

- **CLAIM ID:** ALG26-REC-010
- **CLAIM TYPE:** SOURCE_RECOMMENDATION
- **SOURCE LOCATOR:** T01, 8:16–8:48; FILE-006404 / `tabs/tab-01-video-01.md`; member SHA-256 `8b8b01f5892fefe5e58fc517b144c65daec578ea364f83f9185c27409932c6ec`; tab `https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?tab=t.0`
- **SOURCE SAYS:** Prefer unlisting to deleting an underperforming video because the speaker claims deletion removes useful audience-learning data.
- **PRIMARY EVIDENCE SAYS:** R18 directly advises caution about deleting audience connections and permits unlisting when necessary. R23 says aggregate watch time remains after deletion. R24 documents lost discovery surfaces for unlisted videos. These do not expose all internal learning-state retention.
- **HEURISTIC VS PLATFORM FACT:** PLATFORM FACT: deletion and unlisting have different documented visibility/data effects. CREATOR HEURISTIC: avoid irreversible deletion merely because performance disappoints. CLAIMED CAUSAL MECHANISM: T01's all-data-disappears-immediately assertion and a guaranteed unlisting benefit are overclaims.
- **VALIDATION STATUS:** PARTIALLY_SUPPORTED
- **OS CAN SAFELY CONCLUDE:** Official guidance supports caution about deletion; neither total instant data erasure nor complete signal preservation by unlisting is established.
- **CONFIDENCE / LIMITATION:** Medium. R18's wording about removing content from public view is broader than its unlisting advice; retain R23/R24's precise distinctions. Aggregate analytics and recommender state are different things.
- **CONFLICT STATUS:** PARTIAL_CONFLICT: literal erasure of all data conflicts with R23; the main deletion-caution guidance has primary support. No claim that unlisting preserves every audience signal.
- **PRIMARY SOURCES:** [R18], [R23], [R24]; retrieved 2026-09-08. See the source register for publisher, cited section and exact surface scope.

# Final DS-000018 Validation Synthesis

## Authoritative current dispositions

This table is the sole current disposition register as of 2026-09-08. Each of the 33 original IDs occurs exactly once here. Historical Batch 1/2 statuses and remediation logs are not extra current dispositions. A completed disposition means the claim has been evaluated, not necessarily supported. Source identity remains **Semantic Class A — Global YouTube Knowledge** and all original assertion types remain unchanged.

| Claim ID | CURRENT FINAL DISPOSITION | Primary basis / boundary check | Authoritative bounded conclusion |
|---|---|---|---|
| ALG26-CLM-001 | SUPPORTED | [R1], [R2] | Personalized ranking uses viewer context; surface-specific inputs differ. |
| ALG26-CLM-002 | PARTIALLY_SUPPORTED | [R1], [R2], [R15], [R19] | Personalization and distinct traffic/analytics segments are documented; an exact three-cohort training architecture is not. |
| ALG26-CLM-003 | PARTIALLY_SUPPORTED | [R1], [R5] | Later discovery is possible. The source says may, not typically; a majority-of-lifetime-views outcome is not measured by these sources. |
| ALG26-CLM-004 | SUPPORTED | [R1], [R2], [R4] | Satisfaction involves multiple signals; no universal metric hierarchy follows. |
| ALG26-CLM-005 | PARTIALLY_SUPPORTED | [R3], [R16] | Cross-format preference differences are documented; the full length/podcast/internal partition list remains unestablished. |
| ALG26-CLM-006 | PARTIALLY_SUPPORTED | [R1], [R5] | Suggested can use personal history beyond current-video relevance; no exact cross-topic co-viewing matcher is disclosed. |
| ALG26-CLM-007 | PARTIALLY_SUPPORTED | [R5], [R11] | New-video discovery and researched cold-start handling have primary support; exact first-upload audience assignment does not. |
| ALG26-CLM-008 | SUPPORTED | [R2], [R5], [R22] | Subscribers are not guaranteed viewers. No numerical subscriber-CTR gate or universal propagation rule is validated. |
| ALG26-CLM-009 | SUPPORTED | [R12], [R13] | Repetitive mass production can violate policy; materially varied formats can qualify for monetization. No ranking penalty or blanket exemption is inferred. |
| ALG26-CLM-010 | PARTIALLY_SUPPORTED | [R3], [R15], [R26] | Subscription recommendations and chronological access are documented in bounded contexts; the exact shelf mechanism and universal rollout are not. |
| ALG26-CLM-011 | SUPPORTED | [R2] | Watch history informs recommendations, primarily Home; no universal high weight across surfaces is asserted. |
| ALG26-CLM-012 | PARTIALLY_SUPPORTED | [R11] | The studied semantic-ID model uses audiovisual embeddings; metadata, pacing, format and complete current deployment claims exceed the evidence. |
| ALG26-CLM-013 | NOT_CURRENTLY_VERIFIABLE | [R11] | The asserted private mood-cluster linkage is not publicly verifiable from the reviewed technical evidence. |
| ALG26-CLM-014 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R27] | The selected-client 23–24% to over-50% device mix lacks its underlying data; platform outlook is not verification. |
| ALG26-CLM-015 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R3] | The 100-billion-view, 51% duration statistic lacks its underlying data. No ideal-length rule follows. |
| ALG26-CLM-016 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R7], [R8] | No direct official record located for the claimed Home experiment outcome or small-channel placement. Packaging tools do not establish either. |
| ALG26-CLM-017 | PARTIALLY_SUPPORTED | [R7], [R17] | Direct official evidence replaces press. Current upload capability is established; historical feed guidance does not prove every current shelf or placement effect. |
| ALG26-CLM-018 | CONTRADICTED | [R3], [R16] | The universal channel-separation instruction conflicts with official guidance. Distinct surface behavior is not itself refuted. |
| ALG26-INT-001 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R11] | The four-era narrative remains the creator interpretation, not a published platform chronology. |
| ALG26-INT-002 | PARTIALLY_SUPPORTED | [R1], [R2], [R22] | Audience relevance is documented; semantic-era subscriber devaluation and a hidden topic-authority weight are not. |
| ALG26-INT-003 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R3], [R27] | Device context is documented, but a TV-friction advantage for long shows has not been established. |
| ALG26-INT-004 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R12], [R22], [R27] | Audience relationships may be useful; the claimed increase in personality differentiation as spectacle becomes imitable is unestablished. |
| ALG26-INT-005 | NOT_CURRENTLY_VERIFIABLE | [R3], [R11] | The internal sophistication/volume comparison remains unverified; future public evidence could permit reassessment. |
| ALG26-REC-001 | SUPPORTED | [R19], [R20], [R22] | Use retention comparisons, engagement reports and audience feedback as diagnostics, without metric thresholds or ranking guarantees. |
| ALG26-REC-002 | SUPPORTED | [R15], [R18], [R19] | Do not disable subscriber delivery as an algorithm trick; distinguish notification/subscription traffic from Home. |
| ALG26-REC-003 | SUPPORTED | [R16], [R3] | Choose channel architecture by audience fit and goals; this is conditional creator guidance. |
| ALG26-REC-004 | SUPPORTED | [R4], [R17], [R22] | An audience promise and differentiated value are defensible strategy; no novelty weight or guaranteed repeat distribution follows. |
| ALG26-REC-005 | PARTIALLY_SUPPORTED | [R1], [R3] | A coherent library can help continued viewing; a 3–4-video simultaneous launch or ten-video preparation rule is not established. |
| ALG26-REC-006 | SUPPORTED | [R1], [R22] | Series and familiar formats are supported creator guidance; shows do not receive a documented automatic ranking boost. |
| ALG26-REC-007 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R9], [R10], [R28] | The early-answer citation formula is unestablished, not disproved. Google Search and Ask YouTube are distinct systems. |
| ALG26-REC-008 | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | [R13], [R14], [R9] | Off-platform branding can remain strategy; no recommendation trust-score benefit is established by these policies or Search guidance. |
| ALG26-REC-009 | PARTIALLY_SUPPORTED | [R21], [R9], [R10] | Content-gap research is official creator guidance; the source passage adds an unverified AI-citation/information-gain mechanism. |
| ALG26-REC-010 | PARTIALLY_SUPPORTED | [R18], [R23], [R24] | Official guidance supports caution about deletion; neither total instant data erasure nor complete signal preservation by unlisting is established. |

## Final validation distribution

| Validation status | Final source-wide total | Batch 3 total |
|---|---:|---:|
| SUPPORTED | 10 | 5 |
| PARTIALLY_SUPPORTED | 12 | 4 |
| CONTRADICTED | 1 | 0 |
| NOT_SUPPORTED_BY_PRIMARY_EVIDENCE | 8 | 0 |
| NOT_CURRENTLY_VERIFIABLE | 2 | 0 |

- TOTAL CLAIMS: 33 (18 SOURCE_CLAIM, 5 SOURCE_INTERPRETATION, 10 SOURCE_RECOMMENDATION).
- VALIDATED UNIQUE CLAIMS: 33.
- UNVALIDATED: 0.
- DUPLICATE CURRENT DISPOSITIONS: 0.
- TOTAL CHECK: 33/33; Batch 3: 9/9.

The totals were recomputed from the authoritative table, not copied from prior batches. Four historical statuses changed: CLM-013 from NOT_SUPPORTED_BY_PRIMARY_EVIDENCE to NOT_CURRENTLY_VERIFIABLE; CLM-016 and INT-004 from PARTIALLY_SUPPORTED to NOT_SUPPORTED_BY_PRIMARY_EVIDENCE; REC-007 from CONTRADICTED to NOT_SUPPORTED_BY_PRIMARY_EVIDENCE. Eight other material remediations retain their status while changing authority or interpretation. The prior 24/33 coverage and distribution remain historical only.

## DS-000018 reliability assessment

**MIXED_RELIABILITY.** Of 33 claims, 10 are supported, 12 partial, and 11 contradicted, unsupported or currently unverifiable. Some supported outcomes establish creator guidance rather than platform mechanisms. Provenance is strong at the captured-member level, but the corpus mixes interviews, translated commentary, strategies and inaccessible private analyses. The uncertainty lies in the source assertions, not a lack of claim identity. Use individual bounded conclusions and their limitations; never assign the whole corpus factual authority. This is an intelligence-layer judgment, not a change to semantic class or dataset identity.

## A. SAFE PLATFORM KNOWLEDGE

Only the following bounded facts may be used as platform knowledge. References resolve to the original claim identities; the linked current primary source register supplies the independent authority. Allowed-use labels grant evidence scope only, not permission to build an engine or make channel recommendations.

| Safe conclusion and claim IDs | Primary basis | Allowed downstream uses | Prohibited expansion |
|---|---|---|---|
| Personalized, surface-dependent matching; watch history matters particularly on Home (ALG26-CLM-001, ALG26-CLM-004, ALG26-CLM-011). | [R1], [R2] | GENERAL_PLATFORM_CONTEXT; TOPIC_INTELLIGENCE | Fixed signal weights, universal session-time or emotion hierarchy. |
| Subscriptions do not guarantee viewing; analytics audience groups do not establish model cohorts (ALG26-CLM-002, ALG26-CLM-008). | [R19], [R22] | GENERAL_PLATFORM_CONTEXT | Subscriber devaluation, aggregate CTR gates, subscriber-first seeding rules. |
| Format connections can occur with different viewer preferences (ALG26-CLM-005, ALG26-CLM-018). | [R3] | FORMAT_STRATEGY; GENERAL_PLATFORM_CONTEXT | Automatic Shorts-to-long-form conversion, universal same/separate-channel rules. |
| Later discovery and history-personalized Suggested are documented (ALG26-CLM-003, ALG26-CLM-006). | [R5] | OPPORTUNITY_DISCOVERY; GENERAL_PLATFORM_CONTEXT | Guaranteed evergreen view shares or exact cross-topic matching rules. |
| Published research studies semantic IDs and cold-start generalization (ALG26-CLM-007, ALG26-CLM-012). | [R11] | GENERAL_PLATFORM_CONTEXT | Current universal architecture, semantic scores, mood features or seeding quotas. |
| Repetitive mass production carries policy risk; varied episodes can meet monetization rules (ALG26-CLM-009). | [R12], [R13] | FORMAT_STRATEGY; SCRIPT_INTELLIGENCE; GENERAL_PLATFORM_CONTEXT | Encoding demonetization as a ranking penalty or promising blanket policy clearance. |
| Subscription features have specific device/experiment boundaries (ALG26-CLM-010). | [R15], [R26] | GENERAL_PLATFORM_CONTEXT | Borrowing Home mechanisms or claiming a uniform live shelf layout. |
| Shorts thumbnail uploads are currently documented; historical feed guidance is separately dated (ALG26-CLM-017). | [R7], [R17] | THUMBNAIL_INTELLIGENCE; FORMAT_STRATEGY | Claims that custom Shorts uploads are impossible, every Shorts surface uses the image identically, or upload availability proves Shorts-feed ranking impact. |
| Viewer retention/engagement reports enable diagnosis (ALG26-REC-001, ALG26-REC-002). | [R19], [R20] | HOOK_INTELLIGENCE; SCRIPT_INTELLIGENCE; GENERAL_PLATFORM_CONTEXT | Treating analytics thresholds as guaranteed distribution gates. |
| Public, unlisted and deleted videos have different visibility and reporting consequences (ALG26-REC-010). | [R23], [R24] | GENERAL_PLATFORM_CONTEXT | Total-data-erasure claims, automatic deletion or unlisting, preserved reach guarantees. |

## B. CREATOR HEURISTICS — NOT PLATFORM FACTS

| Bounded practice and claim IDs | Basis | Allowed downstream uses | Prohibited expansion |
|---|---|---|---|
| Compare retention and engagement with context; seek audience feedback (ALG26-REC-001). | [R19], [R20], [R22] | HOOK_INTELLIGENCE; SCRIPT_INTELLIGENCE | Universal hook seconds, retention percentages, rewatch targets or like-rate recipes. |
| Preserve subscriber delivery unless a real publishing reason suggests otherwise (ALG26-REC-002). | [R15], [R18] | GENERAL_PLATFORM_CONTEXT | Gaming notifications for a claimed Home boost. |
| Choose channel architecture by audience overlap and goals (ALG26-REC-003). | [R16] | FORMAT_STRATEGY | Automatic split/merge recommendations without channel-specific evidence. |
| Clarify an audience promise; test differentiated value (ALG26-REC-004, ALG26-INT-002). | [R4], [R17] | TOPIC_INTELLIGENCE; TITLE_INTELLIGENCE; THUMBNAIL_INTELLIGENCE; OPPORTUNITY_DISCOVERY | Hidden authority/novelty scores, subscriber devaluation, copied winning templates. |
| Create useful continuation paths and recurring episodes (ALG26-REC-005, ALG26-REC-006). | [R1], [R22] | FORMAT_STRATEGY; SCRIPT_INTELLIGENCE | Fixed launch volume/cadence, compulsory binge sessions, show-format bonuses. |
| Explore genuine search gaps, checking demand and usefulness (ALG26-REC-009). | [R21] | TOPIC_INTELLIGENCE; OPPORTUNITY_DISCOVERY | Guaranteed citations, information-gain boosts, revenue promises or copying breakout videos as a rule. |
| Consider reversibility before removing underperforming content (ALG26-REC-010). | [R18], [R23], [R24] | GENERAL_PLATFORM_CONTEXT | Automatic content removal or assumed preservation of all recommendation state. |
| Personality, recognizable shows, clear answers and brand consistency can be tested as strategy (ALG26-INT-003, ALG26-INT-004, ALG26-REC-007, ALG26-REC-008). | Creator hypotheses; adjacent guidance [R16], [R22]. | FORMAT_STRATEGY; HOOK_INTELLIGENCE; SCRIPT_INTELLIGENCE | Platform-fact labels, TV causal advantages, AEO formulas or off-platform trust weights. |

The last row preserves potentially useful ideas as hypotheses; it does not upgrade their unsupported source claims. No title, hook, script, thumbnail, topic or opportunity engine is created here.

## C. DO NOT USE AS FACT

- ALG26-CLM-002, ALG26-CLM-007, ALG26-CLM-008, ALG26-INT-002: exact audience-seeding cohorts, subscriber devaluation, hidden topic-authority weights or a subscriber-count distribution formula.
- ALG26-CLM-012, ALG26-CLM-013, ALG26-INT-001, ALG26-INT-005: the full asserted modality list, mood clusters, four semantic eras, or a ranking-system sophistication/volume hierarchy.
- ALG26-CLM-014, ALG26-CLM-015: the private-client device percentages and 100-billion-view/51% duration result. Different platform metrics do not validate these statistics.
- ALG26-CLM-016: an established positive Home redesign effect or guaranteed near-top placement for smaller creators.
- ALG26-CLM-017, ALG26-CLM-018: universal Shorts-thumbnail surface effects, automatic cross-format conversion, or compulsory separate channels.
- ALG26-INT-003, ALG26-INT-004, ALG26-REC-006: TV friction necessarily favors longer shows; personality has gained a measured ranking/market premium; the algorithm rewards emotion or total session duration above all else.
- ALG26-REC-001, ALG26-REC-004, ALG26-REC-005, ALG26-REC-006: exact CTR/retention/rewatch thresholds, one/two/three-second hook rules, fixed ideal duration, fixed upload cadence, mandatory launch volume, or copied-format guarantees.
- ALG26-REC-007, ALG26-REC-008, ALG26-REC-009: early-answer/name/date formulas for AI citations, off-platform authority as YouTube trust scoring, or guaranteed net-information-gain/ranking/revenue outcomes.
- ALG26-REC-010: deletion erases every data trace immediately; unlisting preserves every learning signal or improves ranking. The raw passage's literal all-data assertion conflicts with retained aggregate analytics [R23].

All uses above are prohibited as facts in every listed downstream layer. They may be retained only as labeled source claims or explicitly testable hypotheses where the heuristic set allows that use. No evidence found does not mean false; only CLM-018 has an authoritative CONTRADICTED disposition.

## Numeric, causal and cross-system guardrails

| Issue investigated | Finding / permitted interpretation | Relevant original IDs |
|---|---|---|
| CTR and packaging formulas | [R25]'s 2–10% is a population description, not a target. [R8] evaluates eligible concurrent tests by watch-time share; it excludes Shorts. Exact title templates and thumbnail formulas are unestablished. | ALG26-CLM-004, ALG26-CLM-008, ALG26-CLM-016, ALG26-CLM-017, ALG26-REC-001, ALG26-REC-004 |
| Hooks, retention and rewatch | [R4] recommends early value. [R19]'s 30-second intro measurement is not a hook-length rule; spikes can have multiple explanations. No required retention/rewatch percentage is established. | ALG26-CLM-004, ALG26-REC-001, ALG26-REC-007 |
| Length, cadence and volume | [R3] rejects a universal ideal duration. [R6] concerns sustainable audience expectations; [R5] rejects a daily/weekly requirement. R5 also lists reduced upload frequency as a possible traffic-decline context; fewer viewing opportunities are not proof of a schedule ranking bonus. | ALG26-CLM-015, ALG26-REC-005, ALG26-REC-006 |
| Emotion, sessions and format copying | Storytelling and continuation are strategies [R4], [R1]; no emotion score, universal session-time hierarchy, or copied-format reward is established. | ALG26-CLM-004, ALG26-INT-003, ALG26-REC-006 |
| YouTube Search | Query relevance includes title, description and video content, plus query engagement [R5]. This is Search evidence, not a Home or Shorts-feed formula. | ALG26-REC-004, ALG26-REC-009 |
| Policy versus recommendations | [R12]/[R13] address eligibility or abuse; they do not establish a generic ranking penalty. Distinct enforcement and content suitability effects must remain distinguishable. | ALG26-CLM-009, ALG26-INT-004, ALG26-REC-008 |
| Google Search and AI answers | [R9]/[R10] concern websites in Google Search. [R28] documents Ask YouTube separately. Neither proves REC-007/009's citation formulas. External traffic is also distinct from registered YouTube impressions [R25]. | ALG26-REC-007, ALG26-REC-008, ALG26-REC-009 |
| Home, Up Next, Shorts Feed, channel pages and Subscriptions | [R2], [R7], [R15], [R26] have different surface scopes. The sole explicit format bridge used is [R3]'s documented cross-format connection, without a guaranteed conversion rate. | ALG26-CLM-001, ALG26-CLM-005, ALG26-CLM-006, ALG26-CLM-010, ALG26-CLM-017, ALG26-CLM-018 |

Numeric/topic requests without a standalone registered claim were investigated as guardrails, not invented as new claim IDs. Preserve the corpus's 33-claim boundary.

## Evidence preservation and verification

The original source-intelligence artifact remains byte-identical to baseline, SHA-256 `c2fd52471e75df74ee02c8d3c0b0ce13e7fdf9b323605ec36c6a5dbf69763928`. Raw DS-000018 remains `3992987b88dd4faa16f37b84b502d38b1defaab8fdef8c03722baa1622855a1f`; all 64 registered members match. No original assertion type, source locator, source archive member, channel record or transcript is edited. No dataset is ingested and no MEASURED_FACT row is created.

Final verification on 2026-09-08:

- Independent focused checks found 33 original IDs (18 claims, 5 interpretations, 10 recommendations), 33 unique final dispositions, zero missing IDs and zero duplicate current dispositions. All 28 R aliases resolve. All nine Batch 3 entries and 12 remediation entries contain their required fields; exactly four historical statuses changed.
- Batch 1 and Batch 2 remain byte-identical after excluding the new authority notice. Every repeated SOURCE SAYS assertion, assertion type and timestamp locator agrees with the unchanged source-intelligence artifact.
- The ZIP hash matches the registered snapshot; all 64 members match the catalog and all seven claim-bearing provenance aliases resolve. All 123 transcript-named files in the surviving pre-task hash baseline remain unchanged.
- `.venv/bin/python -B -m pytest -p no:cacheprovider`: 73 collected, 73 passed, 0 failed, 0 skipped, 1 warning. `pytest.ini` restricts discovery to `tests/`; the ignored DS-000014 orphan test was not included. The warning is the intentional duplicate ZIP member `ChannelA/sameid00001.txt` in the duplicate-workbook rejection test.
- SQLite was opened with URI `mode=ro`: `PRAGMA integrity_check` returned `ok`; `PRAGMA foreign_key_check` returned zero rows; `content_classifications` remained 546. Catalog SHA-256 before and after verification matches the surviving pre-task baseline: `74cb0480924ee73800c5ac9bc1040cc6e9ac3e1b7268bbe750494f070b241987`. Hash equality preserves all catalog rows, including transcript hashes, classifications and channel records; MEASURED_FACT promotions remain zero.
- `git diff --check` passed. Task changes are limited to this validation artifact and `data/manifests/DS-000018.md`. Unrelated pre-existing changes remain excluded; temporary source notes, builder and verification scripts remain outside the repository.

## Current reference links

[R1]: https://support.google.com/youtube/answer/16533387?hl=en
[R2]: https://support.google.com/youtube/answer/16089387?hl=en
[R3]: https://support.google.com/youtube/answer/16559651?hl=en
[R4]: https://support.google.com/youtube/answer/16559650?hl=en
[R5]: https://support.google.com/youtube/answer/141805?hl=en
[R6]: https://support.google.com/youtube/answer/13616979
[R7]: https://support.google.com/youtube/answer/72431
[R8]: https://support.google.com/youtube/answer/16391400?hl=en
[R9]: https://developers.google.com/search/docs/appearance/ai-features
[R10]: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
[R11]: https://arxiv.org/html/2306.08121v2
[R12]: https://support.google.com/youtube/answer/1311392?hl=en
[R13]: https://support.google.com/youtube/answer/2801973?hl=en
[R14]: https://support.google.com/youtube/answer/2801947?hl=en
[R15]: https://blog.youtube/culture-and-trends/renes-top-five-on-youtube-april-18-2024-edition/
[R16]: https://blog.youtube/creator-and-artist-stories/renes-top-five-august-1-2024/
[R17]: https://blog.youtube/creator-and-artist-stories/renes-top-five-july-25-2024/
[R18]: https://blog.youtube/culture-and-trends/renes-top-five-on-youtube-march-28-2024-edition/
[R19]: https://support.google.com/youtube/answer/9314415?hl=en
[R20]: https://support.google.com/youtube/answer/9313698?hl=en
[R21]: https://support.google.com/youtube/answer/11962757?co=GENIE.Platform%3DDesktop&hl=en
[R22]: https://support.google.com/youtube/answer/10246996?hl=en
[R23]: https://support.google.com/youtube/answer/55770?hl=en
[R24]: https://support.google.com/youtube/answer/157177
[R25]: https://support.google.com/youtube/answer/7628154
[R26]: https://support.google.com/youtube/thread/396097464?hl=en&msgid=428283639
[R27]: https://blog.youtube/inside-youtube/the-future-of-youtube-2026/
[R28]: https://blog.youtube/news-and-events/youtube-news-google-io-2026/
